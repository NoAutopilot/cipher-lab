#!/usr/bin/env python3
"""TXE3-6 UNIT step 1: box sets for Vivonne f.102r (PREREG-txeng3-6.md). Runs tools/glyph_atlas.py segment over the
74 line crops (one crop = one page), maps every sign box into line coordinates by the crop's manifest x0, dedupes
the s1/s2 overlap at its midpoint (OL1-BOXES rule), orders by centre x, and writes DIR/boxes.tsv
(line, pos, sid, page, x_line, x, y, w, h). Marks are not tokens. No truth value is read here; the grid chooser reads
truth COUNTS on train lines only.

  python3 benchmark-tx/txeng3/6/seg.py run NAME [--split-wide W --split-piece P --split-random S] [--lines L02,...]
  python3 benchmark-tx/txeng3/6/seg.py grid        # (W,P) chosen on TRAIN lines by |boxes - truth positions|
"""
import argparse, csv, json, os, subprocess, sys, collections
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, '..', '..', '..'))
IMG = os.path.join(REPO, 'ciphers/fr16104-vivonne-spain-1572/images')
TRUTH = os.path.join(REPO, 'benchmark-tx/vivonne1573-f102r-dev2.truth.tsv')
TEST = ['L%02d' % n for n in (2, 4, 8, 10, 14, 16, 18, 20, 24, 28, 30, 32, 34, 36)]
TRAIN = ['L%02d' % n for n in range(1, 37) if 'L%02d' % n not in TEST]


def crops():
    m = json.load(open(os.path.join(IMG, 'manifest.json')))['iiif_lines']
    out = {}
    for e in m:
        c = e['crop']
        if 'f102r_L' not in c:
            continue
        ln = c.split('_')[2]            # L02
        seg = int(c.split('_s')[1].split('.')[0])
        out[(ln, seg)] = dict(path=os.path.join(IMG, c), x0=e['box'][0], x1=e['box'][2], page=f'f102r_{ln}_s{seg}')
    return out


def truth_counts():
    c = collections.Counter()
    for r in csv.DictReader((l for l in open(TRUTH) if not l.startswith('#')), delimiter='\t'):
        c[r['line'].split('_')[1]] += 1
    return c


def run(name, extra, lines):
    cr = crops()
    out = os.path.join(ROOT, 'seg', name)
    os.makedirs(out, exist_ok=True)
    pages = []
    for (ln, seg), e in sorted(cr.items()):
        if ln in lines:
            pages += ['--page', f"{e['page']}={e['path']}"]
    cmd = [sys.executable, os.path.join(REPO, 'tools/glyph_atlas.py'), 'segment', '--out', out] + pages + extra
    log = subprocess.run(cmd, capture_output=True, text=True)
    if log.returncode:
        sys.exit(log.stdout + log.stderr)
    open(os.path.join(out, 'segment.log'), 'w').write(' '.join(cmd[2:5]) + ' ...' + ' '.join(extra) + '\n' + log.stdout)
    rows = list(csv.DictReader(open(os.path.join(out, 'signs.tsv')), delimiter='\t'))
    byline = collections.defaultdict(list)
    for r in rows:
        ln, seg = r['page'].split('_')[1], int(r['page'][-1])
        e = cr[(ln, seg)]
        xc = e['x0'] + int(r['x']) + int(r['w']) / 2
        byline[ln].append(dict(r, seg=seg, xl=e['x0'] + int(r['x']), xc=xc))
    with open(os.path.join(out, 'boxes.tsv'), 'w') as f:
        f.write('line\tpos\tsid\tpage\tx_line\tx\ty\tw\th\n')
        n = collections.Counter()
        for ln in sorted(byline):
            segs = sorted({s for (l2, s) in cr if l2 == ln})
            keep = []
            for b in byline[ln]:
                lo = -1e9 if b['seg'] == segs[0] else (cr[(ln, b['seg'])]['x0'] + cr[(ln, b['seg'] - 1)]['x1']) / 2
                hi = 1e9 if b['seg'] == segs[-1] else (cr[(ln, b['seg'] + 1)]['x0'] + cr[(ln, b['seg'])]['x1']) / 2
                if lo <= b['xc'] < hi:
                    keep.append(b)
            keep.sort(key=lambda b: b['xc'])
            for i, b in enumerate(keep):
                f.write(f"f102r_{ln}\t{i + 1}\t{b['sid']}\t{b['page']}\t{b['xl']}\t{b['x']}\t{b['y']}\t{b['w']}\t{b['h']}\n")
            n[ln] = len(keep)
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=['run', 'grid'])
    ap.add_argument('name', nargs='?')
    ap.add_argument('--split-wide', type=float)
    ap.add_argument('--split-piece', type=float)
    ap.add_argument('--split-random', type=int)
    ap.add_argument('--lines', help='comma list L02,...; default all 36 truth lines')
    a = ap.parse_args()
    lines = a.lines.split(',') if a.lines else TRAIN + TEST
    if a.cmd == 'run':
        extra = []
        if a.split_wide:
            extra += ['--split-wide', str(a.split_wide), '--split-piece', str(a.split_piece or 1.0)]
        if a.split_random is not None:
            extra += ['--split-random', str(a.split_random)]
        n = run(a.name, extra, lines)
        tc = truth_counts()
        print(a.name, 'boxes', sum(n.values()), 'truth', sum(tc[l] for l in lines),
              'train', sum(n[l] for l in TRAIN if l in lines), '/', sum(tc[l] for l in TRAIN if l in lines),
              'test', sum(n[l] for l in TEST if l in lines), '/', sum(tc[l] for l in TEST if l in lines))
        return
    tc = truth_counts()
    res = []
    for W in (1.2, 1.5, 1.8, 2.2):
        for P in (0.7, 0.85, 1.0, 1.2):
            n = run(f'grid_W{W}_P{P}', ['--split-wide', str(W), '--split-piece', str(P)], TRAIN)
            d = sum(abs(n[l] - tc[l]) for l in TRAIN)
            res.append((d, -W, abs(P - 1.0), W, P, sum(n[l] for l in TRAIN)))
            print(f'W {W} P {P}: train boxes {sum(n[l] for l in TRAIN)} vs truth {sum(tc[l] for l in TRAIN)}, sum|diff| {d}')
    res.sort()
    d, _, _, W, P, nb = res[0]
    print(f'CHOSEN W {W} P {P} (sum|diff| {d}, train boxes {nb} vs truth {sum(tc[l] for l in TRAIN)})')
    with open(os.path.join(ROOT, 'grid.tsv'), 'w') as f:
        f.write('W\tP\ttrain_boxes\ttrain_truth\tsum_absdiff\tchosen\n')
        for d, _, _, W2, P2, nb2 in sorted(res, key=lambda r: (r[3], r[4])):
            f.write(f'{W2}\t{P2}\t{nb2}\t{sum(tc[l] for l in TRAIN)}\t{d}\t{int((W2, P2) == (W, P))}\n')


if __name__ == '__main__':
    main()
