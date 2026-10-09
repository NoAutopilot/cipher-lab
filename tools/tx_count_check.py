#!/usr/bin/env python3
"""Read-free sign-count doubt signal per line crop (LANE TX-ENGINEER-2 X19 deletion detector, 9 Oct 2026).

    python3 tools/tx_count_check.py count --manifest M.json [--manifest ...] --read PASS.tsv [--gap-frac F] --out OUT.tsv
    python3 tools/tx_count_check.py tune  --manifest M.json --truth TRUTH.tsv --lines UNIT.tsv --out TUNE.tsv
    python3 tools/tx_count_check.py recall --manifest M.json --read PASS.tsv --bench BENCHMARK-TX.tsv --item ITEM
                                           [--lines UNIT.tsv] --gap-frac F

Expected sign count of a line, from the image only (no model, no read):
  1. The line strip is rebuilt from its segment crops (`<line>_s<k>.jpg`) placed at their page `box` x offsets from the
     iiif_lines manifest (overlapping segments: later segment wins; a crop narrower than its box is rescaled to the box).
  2. Grey -> ink by Otsu's threshold; the row band is the contiguous run of rows around the row-ink peak whose ink is
     >= 30% of the peak (cuts most of the neighbouring lines' ascenders and descenders).
  3. A column is ink when >= 2 band pixels are ink. Connected ink runs along x are found; runs narrower than 3 px are
     dropped as specks. Two runs separated by a gap shorter than gap_frac x the median run width are merged (one
     sign drawn with a pen lift); the count of merged runs is the expected sign count.
The fixed constants (30%, 2 px, 3 px) are set here before any tuning; only gap_frac is tuned (`tune`: the value in
0.0..1.5 step 0.05 minimising mean |expected - truth line length| over the named dev lines; ties to the smaller).
`count` flags a line when |expected - read count| >= 1 (PREREG X19). `recall` reports, against the benchmark truth via
tools/tx_bench.py's alignment, the share of lines carrying a deleted or inserted sign that are flagged, and the share of
all lines flagged. A doubt signal for the sorter feed, never a correction; no truth file is written.
Test: tools/tests/test_tx_count_check.py (synthetic strip of N blobs, one with a pen-lift gap: counted N).
"""
import argparse, glob, json, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tx_bench  # noqa: E402

BAND_FRAC, COL_MIN, SPECK = 0.30, 2, 3


def manifest_entries(paths):
    """{line: [(crop_path, box)]} from iiif_lines manifests (any nesting)."""
    out = defaultdict(list)

    def walk(x, d):
        if isinstance(x, dict):
            c = x.get('crop')
            if c and x.get('box'):
                m = re.match(r'^(.+_L\d+)_s\d+\.(jpg|png)$', os.path.basename(c))
                if m:
                    out[m.group(1)].append((os.path.join(d, os.path.basename(c)), x['box']))
            for v in x.values():
                walk(v, d)
        elif isinstance(x, list):
            for v in x:
                walk(v, d)
    for p in paths:
        walk(json.load(open(p)), os.path.dirname(p))
    return out


def line_strip(segs):
    import numpy as np
    from PIL import Image
    segs = [(p, b) for p, b in segs if os.path.exists(p)]
    if not segs:
        return None
    x0 = min(b[0] for _, b in segs); x1 = max(b[2] for _, b in segs)
    h = max(b[3] - b[1] for _, b in segs)
    strip = np.full((h, x1 - x0), 255, dtype=np.uint8)
    for p, b in sorted(segs, key=lambda t: t[1][0]):
        im = Image.open(p).convert('L')
        bw, bh = b[2] - b[0], b[3] - b[1]
        if im.size != (bw, bh):
            im = im.resize((bw, bh))
        a = np.asarray(im)
        strip[:bh, b[0] - x0:b[0] - x0 + bw] = a
    return strip


def otsu(a):
    import numpy as np
    hist = np.bincount(a.ravel(), minlength=256).astype(float)
    w = hist.cumsum(); mu = (hist * np.arange(256)).cumsum(); tot = w[-1]; mt = mu[-1]
    best, t = -1, 128
    for i in range(1, 255):
        w0, w1 = w[i], tot - w[i]
        if w0 == 0 or w1 == 0:
            continue
        m0, m1 = mu[i] / w0, (mt - mu[i]) / w1
        v = w0 * w1 * (m0 - m1) ** 2
        if v > best:
            best, t = v, i
    return t


def runs_of(strip):
    """Ink runs [(x_start, x_end)] in the row band, specks dropped."""
    import numpy as np
    ink = strip <= otsu(strip)
    rp = ink.sum(1)
    pk = int(rp.argmax()); thr = BAND_FRAC * rp[pk]
    a = pk
    while a > 0 and rp[a - 1] >= thr:
        a -= 1
    b = pk
    while b < len(rp) - 1 and rp[b + 1] >= thr:
        b += 1
    col = ink[a:b + 1].sum(0) >= COL_MIN
    runs, s = [], None
    for x, v in enumerate(list(col) + [False]):
        if v and s is None:
            s = x
        elif not v and s is not None:
            if x - s >= SPECK:
                runs.append((s, x))
            s = None
    return runs


def count_from_runs(runs, gap_frac):
    if not runs:
        return 0
    widths = sorted(e - s for s, e in runs)
    med = widths[len(widths) // 2]
    n = 1
    for (s0, e0), (s1, e1) in zip(runs, runs[1:]):
        if s1 - e0 >= gap_frac * med:
            n += 1
    return n


def line_runs(manifests):
    return {ln: runs_of(st) for ln, segs in manifest_entries(manifests).items()
            for st in [line_strip(segs)] if st is not None}


def per_line_errors(truth, out_lines):
    """{line: (deleted, inserted, wrong)} by tx_bench's alignment (all positions, scored or not, for indels)."""
    by = defaultdict(list)
    for r in truth:
        by[r['line']].append(r)
    res = {}
    for ln, rows in by.items():
        if ln not in out_lines:
            continue
        rows.sort(key=lambda r: float(r['pos']))
        ref = [r['ref_sign'] for r in rows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        d = i = w = 0
        for ri, osg in tx_bench.align(ref, ts, out_lines[ln]):
            if ri is None:
                i += 1
            elif rows[ri]['status'] == 'scored':
                if osg is None:
                    d += 1
                elif osg not in ts[ri]:
                    w += 1
        res[ln] = (d, i, w)
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('cmd', choices=['count', 'tune', 'recall'])
    ap.add_argument('--manifest', action='append', required=True)
    ap.add_argument('--read'); ap.add_argument('--truth'); ap.add_argument('--lines')
    ap.add_argument('--bench', default='BENCHMARK-TX.tsv'); ap.add_argument('--item')
    ap.add_argument('--gap-frac', type=float, default=0.5)
    ap.add_argument('--out')
    a = ap.parse_args(argv)
    R = line_runs(a.manifest)
    keep = set(r['line'] for r in tx_bench.read_tsv(a.lines)) if a.lines else None
    if a.cmd == 'tune':
        if not a.truth:
            print('tune needs --truth', file=sys.stderr); return 2
        L = defaultdict(int)
        for r in tx_bench.read_tsv(a.truth):
            L[r['line']] += 1
        lines = [ln for ln in R if ln in L and (keep is None or ln in keep)]
        rows = []
        for k in range(0, 31):
            g = round(0.05 * k, 2)
            mae = sum(abs(count_from_runs(R[ln], g) - L[ln]) for ln in lines) / max(1, len(lines))
            rows.append((g, mae))
        best = min(rows, key=lambda t: (round(t[1], 9), t[0]))
        if a.out:
            with open(a.out, 'w') as f:
                f.write('gap_frac\tmae\n' + ''.join('%.2f\t%.3f\n' % r for r in rows))
        print('tune: %d lines; best gap_frac %.2f, mean |expected - truth| %.2f' % (len(lines), best[0], best[1]))
        return 0
    if not a.read:
        print('%s needs --read' % a.cmd, file=sys.stderr); return 2
    reads = tx_bench.load_output([a.read])
    lines = sorted(ln for ln in reads if ln in R and (keep is None or ln in keep))
    flag = {ln: count_from_runs(R[ln], a.gap_frac) - len(reads[ln]) for ln in lines}
    if a.cmd == 'count':
        with open(a.out, 'w') as f:
            f.write('line\texpected\tread\tdiff\tflag\n')
            for ln in lines:
                e = count_from_runs(R[ln], a.gap_frac)
                f.write('%s\t%d\t%d\t%+d\t%d\n' % (ln, e, len(reads[ln]), flag[ln], abs(flag[ln]) >= 1))
        print('count: %d lines, %d flagged -> %s' % (len(lines), sum(abs(v) >= 1 for v in flag.values()), a.out))
        return 0
    base = os.path.dirname(os.path.abspath(a.bench))
    truth = None
    for it in tx_bench.read_tsv(a.bench):
        if it['item'] == a.item:
            truth = tx_bench.read_tsv(os.path.join(base, it['truth']))
    if truth is None:
        print('recall: no item %s' % a.item, file=sys.stderr); return 2
    E = per_line_errors(truth, {ln: reads[ln] for ln in lines})
    lines = [ln for ln in lines if ln in E]
    pos = [ln for ln in lines if E[ln][0] + E[ln][1] > 0]
    fl = [ln for ln in lines if abs(flag[ln]) >= 1]
    hit = [ln for ln in pos if abs(flag[ln]) >= 1]
    print('recall %s %s: lines %d, with indel %d, flagged %d (%.0f%%), indel lines flagged %d -> recall %s'
          % (a.item, os.path.basename(a.read), len(lines), len(pos), len(fl), 100.0 * len(fl) / max(1, len(lines)),
             len(hit), ('%.2f' % (len(hit) / len(pos))) if pos else 'n/a'))
    for ln in lines:
        print('  %s expected-read %+d  deleted %d inserted %d wrong %d' % (ln, flag[ln], *E[ln]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
