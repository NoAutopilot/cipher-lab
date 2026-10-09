#!/usr/bin/env python3
"""tx_split_groups.py -- read-free flags for glued (or over-split) digit groups from column ink-density profiles.

Lesson it answers (TX-TAXONOMY 9 Oct 2026 s.3, TX-IDEAS M8): on the Dinteville 1592 hand the blind passes disagree on
the COUNT of signs, not only their identity (the Fable pass inserted 9 signs, pass A deleted 2): segmentation of glued
digit groups. Every other instrument asks "which sign"; this one asks "how many signs does this ink hold", from the
image alone, and flags where a pass's count disagrees.

    python3 tools/tx_split_groups.py --images ciphers/fr3621-dinteville-1592/images --prefix f128 \\
        --lines L03,L04,L05 --pass A=benchmark-tx/outputs/dint-f128-print/passA.tsv --pass B=... --pass F=... \\
        --out benchmark-tx/txeng/split

Per line: the segment crops (<prefix>_<L>_s1.jpg, _s2.jpg ...) are stitched by their manifest.json boxes (the overlap is
dropped), the line band is the row-profile peak +- pitch/2, and tools/iiif_lines.py's group_pieces() (imported, not
copied) cuts the core rows into ink pieces at runs of >= GAP blank columns. Writes, in --out:
  sweep.tsv   piece count per line for every gap in --gaps, and the gap(s) at which it equals each pass's sign count
              ('-' when no gap in the sweep matches; 'nearest' gives the closest)
  pieces.tsv  the pieces at the working gap (per line: the sweep gap whose count is nearest the median pass count),
              their x extent, width, e = width / sign pitch and k_est = max(1, round(e)), the sign pitch calibrated
              so that the k_est sum to the median pass count
  flags.tsv   per pass: a monotone DP assigns the pass's signs to the pieces (each piece takes k = 0..4 signs, cost
              |k - e|); agreed anchors are signs on which all passes agree at aligned positions (edit-distance
              alignment of every pass to the first); between consecutive anchors, if the pass's net excess
              sum(k - k_est) is non-zero, every pass position lying in a piece with k != k_est is flagged:
              kind 'over' (k > k_est: the pass reads more signs than the ink width holds -- candidate insertion or
              over-split) or 'under' (k < k_est: candidate glued pair read as one / deletion); k = 0 pieces flag
              the next pass position as 'under'.
A line whose piece count at the widest sweep gap still exceeds 1.5 x the median pass count holds ink that is not the
cipher row (gloss, clear text) and is reported in sweep.tsv but not flagged (rule fixed before any truth was opened).
No model, no network, no truth file. Scoring is a separate step (tx_bench.py's aligner), after flags.tsv is committed.
"""
import argparse, csv, json, os, statistics, sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iiif_lines import group_pieces  # noqa: E402  (the --groups logic; do not copy)


def read_pass(path):
    lines = {}
    with open(path, encoding='utf-8') as f:
        rows = [r for r in f if not r.startswith('#')]
    for r in csv.DictReader(rows, delimiter='\t'):
        lines.setdefault(r['line'], []).append((float(r['pos']), r['pos'], r['sign'].strip()))
    return {k: [(p, s) for _, p, s in sorted(v)] for k, v in lines.items()}


def stitch(images, prefix, line):
    """Stitch <prefix>_<line>_s*.jpg left to right by the x of their manifest boxes; returns a grey array."""
    man = json.load(open(os.path.join(images, 'manifest.json'), encoding='utf-8'))
    ent = sorted((e for e in man.get('iiif_lines', []) if e['crop'].startswith(f'{prefix}_{line}_s')),
                 key=lambda e: e['box'][0])
    if not ent:
        sys.exit(f'tx_split_groups: no manifest entries for {prefix}_{line}_s*')
    x0 = ent[0]['box'][0]
    parts, upto = [], x0
    for e in ent:
        g = np.asarray(Image.open(os.path.join(images, e['crop'])).convert('L'))
        skip = max(0, upto - e['box'][0])
        parts.append(g[:, skip:])
        upto = e['box'][0] + g.shape[1]
    h = min(p.shape[0] for p in parts)
    return np.concatenate([p[:h] for p in parts], axis=1)


def band(gray, ink, pitch):
    """Row-profile peak in the middle half of the crop, +- pitch/2."""
    h = gray.shape[0]
    rows = (gray < ink).sum(axis=1).astype(float)
    sm = np.convolve(rows, np.ones(15) / 15, 'same')
    c = int(np.argmax(sm[h // 4:3 * h // 4])) + h // 4
    return max(0, c - pitch // 2), min(h, c + pitch // 2)


def sweep(gray, top, bot, gaps, ink, minw, core):
    return {g: group_pieces(gray, top, bot, 0, gray.shape[1], ink, g, core=core, minw=minw) for g in gaps}


def k_estimates(pieces, n_ref):
    """Continuous sign estimate per piece e = width / sw, sw calibrated (bisection) so that sum(round(e)) = n_ref,
    each at least 1; returns (k_est list, e list, sw)."""
    if not pieces or not n_ref:
        return [1] * len(pieces), [1.0] * len(pieces), 0.0
    ws = [x1 - x0 for x0, x1 in pieces]
    lo, hi = 1.0, float(sum(ws))
    for _ in range(60):
        sw = (lo + hi) / 2
        tot = sum(max(1, round(w / sw)) for w in ws)
        if tot > n_ref:
            lo = sw
        else:
            hi = sw
    sw = hi
    e = [max(1.0, w / sw) for w in ws]
    return [max(1, round(x)) for x in e], e, sw


def dp_assign(n, est, kmax=4):
    """Assign n signs (in order) to pieces; returns k per piece minimising sum |k - e| over the continuous
    estimates e (k=0 allowed), so an extra sign goes to the piece widest for its count, a missing one to the narrowest."""
    P = len(est)
    INF = float('inf')
    D = [[INF] * (n + 1) for _ in range(P + 1)]
    B = [[0] * (n + 1) for _ in range(P + 1)]
    D[0][0] = 0.0
    for p in range(1, P + 1):
        for j in range(n + 1):
            best, bk = INF, 0
            for k in range(0, min(kmax, j) + 1):
                v = D[p - 1][j - k] + abs(k - est[p - 1])
                if v < best - 1e-12:
                    best, bk = v, k
            D[p][j], B[p][j] = best, bk
    ks, j = [], n
    if D[P][n] == INF:          # more signs than kmax x pieces: no assignment
        return None
    for p in range(P, 0, -1):
        ks.append(B[p][j]); j -= B[p][j]
    return ks[::-1]


def align(a, b):
    """Edit-distance alignment of sequences a, b; returns pairs (i or None, j or None)."""
    n, m = len(a), len(b)
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i * 0.75
    for j in range(m + 1):
        D[0][j] = j * 0.75
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j - 1] + (a[i - 1] != b[j - 1]), D[i - 1][j] + .75, D[i][j - 1] + .75)
    i, j, out = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and abs(D[i][j] - D[i - 1][j - 1] - (a[i - 1] != b[j - 1])) < 1e-9:
            out.append((i - 1, j - 1)); i -= 1; j -= 1
        elif i > 0 and abs(D[i][j] - D[i - 1][j] - .75) < 1e-9:
            out.append((i - 1, None)); i -= 1
        else:
            out.append((None, j - 1)); j -= 1
    return out[::-1]


def anchors(seqs):
    """Indices, per pass, of signs all passes agree on at aligned positions (alignment of each pass to the first)."""
    names = list(seqs)
    ref = seqs[names[0]]
    maps = {names[0]: {i: i for i in range(len(ref))}}
    for nm in names[1:]:
        maps[nm] = {i: j for i, j in align(ref, seqs[nm]) if i is not None and j is not None and ref[i] == seqs[nm][j]}
    out = {nm: [] for nm in names}
    for i in range(len(ref)):
        if all(i in maps[nm] for nm in names):
            for nm in names:
                out[nm].append(maps[nm][i])
    return out


def flag_pass(ks, kest, anc, n):
    """Flags for one pass: list of (sign index, kind, piece index). See module doc."""
    sign_piece, j = [None] * n, 0
    zero = []
    for p, k in enumerate(ks):
        if k == 0:
            zero.append((p, j))
        for _ in range(k):
            sign_piece[j] = p; j += 1
    bounds = [-1] + sorted(set(anc)) + [n]
    flags = []
    for lo, hi in zip(bounds, bounds[1:]):
        idx = list(range(max(lo, 0), hi))       # an anchor opens the interval to its right
        ps = sorted({sign_piece[i] for i in idx})
        net = sum(ks[p] - kest[p] for p in ps) - sum(kest[p] for p, at in zero if lo <= at < hi)
        if net == 0:
            continue
        for i in idx:
            p = sign_piece[i]
            if ks[p] != kest[p]:
                flags.append((i, 'over' if ks[p] > kest[p] else 'under', p))
        for p, at in zero:
            if lo <= at < hi and at < n:
                flags.append((at, 'under', p))
    seen, out = set(), []
    for f in sorted(flags):
        if f[0] not in seen:
            seen.add(f[0]); out.append(f)
    return out


def run(lines_gray, passes, gaps, ink, minw, core, pitch, out):
    os.makedirs(out, exist_ok=True)
    names = list(passes)
    sw_rows, pc_rows, fl_rows = [], [], []
    report = {}
    for ln, gray in lines_gray.items():
        top, bot = band(gray, ink, pitch)
        sw = sweep(gray, top, bot, gaps, ink, minw, core)
        counts = {g: len(v) for g, v in sw.items()}
        ns = {nm: len(passes[nm].get(ln, [])) for nm in names}
        med = int(statistics.median(ns.values()))
        row = {'line': ln, 'band': f'{top}-{bot}', **{f'g{g}': counts[g] for g in gaps}}
        for nm in names:
            eq = [g for g in gaps if counts[g] == ns[nm]]
            near = min(gaps, key=lambda g: (abs(counts[g] - ns[nm]), g))
            row[f'n_{nm}'] = ns[nm]
            row[f'gap_eq_{nm}'] = ','.join(map(str, eq)) or '-'
            row[f'nearest_{nm}'] = f'{near}({counts[near]})'
        unfit = counts[max(gaps)] > 1.5 * med
        wg = min(gaps, key=lambda g: (abs(counts[g] - med), g))
        row['working_gap'] = wg
        row['status'] = 'unfit: ink beyond the cipher row' if unfit else 'flagged'
        sw_rows.append(row)
        if unfit:
            continue
        pieces = sw[wg]
        kest, est, signw = k_estimates(pieces, med)
        for i, ((x0, x1), k) in enumerate(zip(pieces, kest)):
            pc_rows.append({'line': ln, 'piece': i + 1, 'x0': x0, 'x1': x1, 'width': x1 - x0, 'k_est': k, 'e': f'{est[i]:.2f}',
                            'sign_pitch': f'{signw:.1f}'})
        seqs = {nm: [s for _, s in passes[nm].get(ln, [])] for nm in names}
        anc = anchors(seqs)
        for nm in names:
            n = len(seqs[nm])
            ks = dp_assign(n, est)
            if ks is None:
                continue
            for i, kind, p in flag_pass(ks, kest, anc[nm], n):
                fl_rows.append({'pass': nm, 'line': ln, 'pos': passes[nm][ln][i][0], 'sign': seqs[nm][i],
                                'kind': kind, 'piece': p + 1, 'k_read': ks[p], 'k_est': kest[p]})
        report[ln] = dict(working_gap=wg, pieces=len(pieces), n=ns, anchors=len(anc[names[0]]))
    write(os.path.join(out, 'sweep.tsv'), sw_rows)
    write(os.path.join(out, 'pieces.tsv'), pc_rows)
    write(os.path.join(out, 'flags.tsv'), fl_rows, ['pass', 'line', 'pos', 'sign', 'kind', 'piece', 'k_read', 'k_est'])
    return sw_rows, fl_rows, report


def write(path, rows, cols=None):
    cols = cols or (list(rows[0]) if rows else ['line'])
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, cols, delimiter='\t', lineterminator='\n')
        w.writeheader(); w.writerows(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--images', required=True, help='folder with the segment crops and manifest.json')
    ap.add_argument('--prefix', required=True, help='crop prefix, e.g. f128')
    ap.add_argument('--lines', required=True, help='comma list of line ids, e.g. L02,L03')
    ap.add_argument('--pass', dest='passes', action='append', default=[], metavar='NAME=TSV',
                    help='a blind pass (line, pos, sign); first one is the alignment reference')
    ap.add_argument('--gaps', default='2-12', help='gap sweep, lo-hi in px (default 2-12)')
    ap.add_argument('--ink', type=int, default=120, help='grey level below which a pixel is ink (iiif_lines default)')
    ap.add_argument('--minw', type=int, default=2, help='drop pieces narrower than this (px)')
    ap.add_argument('--core', type=float, default=0.55, help='core share of the band rows (iiif_lines default)')
    ap.add_argument('--pitch', type=int, default=100, help='line pitch in px (manifest pitch_autocorr)')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    lo, hi = map(int, a.gaps.split('-'))
    passes = {}
    for spec in a.passes:
        nm, p = spec.split('=', 1)
        passes[nm] = read_pass(p)
    if not passes:
        sys.exit('tx_split_groups: give at least one --pass')
    lines = {}
    for L in a.lines.split(','):
        ln = f'{a.prefix}_{L}'
        lines[ln] = stitch(a.images, a.prefix, L)
    sw, fl, rep = run(lines, passes, list(range(lo, hi + 1)), a.ink, a.minw, a.core, a.pitch, a.out)
    for r in sw:
        print('\t'.join(f'{k}={v}' for k, v in r.items()))
    for nm in passes:
        tot = sum(len(passes[nm].get(ln, [])) for ln in rep)
        k = sum(1 for f in fl if f['pass'] == nm)
        print(f'pass {nm}: {k} flags of {tot} positions on fitted lines ({k / tot:.1%})' if tot else f'pass {nm}: no lines')


if __name__ == '__main__':
    main()
