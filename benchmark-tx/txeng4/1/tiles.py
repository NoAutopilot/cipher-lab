#!/usr/bin/env python3
"""TXE4-1 VIV-HAND tiles (PREREG-txeng4-1.md 'Tiles'; read-free: no model call, no truth, no person, no f.102r output).

  python3 benchmark-tx/txeng4/1/tiles.py segment   # 2a: glyph_atlas segment on the 74 f.102v crops (one page per crop),
                                                   #     boxes in line coordinates, s1/s2 overlap deduped at its midpoint
                                                   #     (TXE3-6 seg.py recipe) -> seg/signs.tsv, seg/boxes.tsv, signs_line.tsv
  python3 benchmark-tx/txeng4/1/tiles.py agree     # 2b: passes to long form, reconcile_passes --method nw, agree positions
                                                   #     in pass A's numbering -> passA_long.tsv, passB_long.tsv, agree.tsv
  python3 benchmark-tx/txeng4/1/tiles.py tokens    # 2e: tokens.tsv from round1/round2 maps (run after rounds; see run.sh)
"""
import collections, csv, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
T = os.path.join(REPO, 'ciphers/fr16104-vivonne-spain-1572')
IMG = os.path.join(T, 'images')
SHEET40 = [r['token'] for r in csv.DictReader(open(os.path.join(T, 'glyphs/sheet_tomokiyo_v1.tsv')), delimiter='\t')]


def crops():
    m = json.load(open(os.path.join(IMG, 'manifest.json')))['iiif_lines']
    out = {}
    for e in m:
        c = e['crop']
        if 'f102v_L' not in c:
            continue
        ln = c.split('_')[2]
        seg = int(c.split('_s')[1].split('.')[0])
        out[(ln, seg)] = dict(path=os.path.join(IMG, c), x0=e['box'][0], x1=e['box'][2], page=f'f102v_{ln}_s{seg}')
    return out


def segment():
    cr = crops()
    out = os.path.join(HERE, 'seg')
    os.makedirs(out, exist_ok=True)
    pages = []
    for (ln, seg), e in sorted(cr.items()):
        pages += ['--page', f"{e['page']}={e['path']}"]
    cmd = [sys.executable, os.path.join(REPO, 'tools/glyph_atlas.py'), 'segment', '--out', out] + pages
    log = subprocess.run(cmd, capture_output=True, text=True)
    if log.returncode:
        sys.exit(log.stdout + log.stderr)
    open(os.path.join(out, 'segment.log'), 'w').write('glyph_atlas.py segment --out seg --page <74 f102v crops> (default pen-unit mode)\n' + log.stdout)
    rows = list(csv.DictReader(open(os.path.join(out, 'signs.tsv')), delimiter='\t'))
    byline = collections.defaultdict(list)
    for r in rows:
        ln, seg = r['page'].split('_')[1], int(r['page'][-1])
        e = cr[(ln, seg)]
        xc = e['x0'] + int(r['x']) + int(r['w']) / 2
        byline[ln].append(dict(r, seg=seg, xl=e['x0'] + int(r['x']), xc=xc))
    n = collections.Counter()
    with open(os.path.join(out, 'boxes.tsv'), 'w') as f, open(os.path.join(HERE, 'signs_line.tsv'), 'w') as g:
        f.write('line\tpos\tsid\tpage\tx_line\tx\ty\tw\th\n')
        g.write('sid\tpage\tline\tx\tw\n')
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
                f.write(f"f102v_{ln}\t{i + 1}\t{b['sid']}\t{b['page']}\t{b['xl']}\t{b['x']}\t{b['y']}\t{b['w']}\t{b['h']}\n")
                g.write(f"{b['sid']}\tf102v\t{int(ln[1:])}\t{b['xl']}\t{b['w']}\n")
            n[ln] = len(keep)
    print('segment: boxes per line', dict(sorted(n.items())), 'total', sum(n.values()))


PLAIN = re.compile(r'\[PLAIN:[^\]]*\]')


def long_form(src, dst):
    """wide 'row<TAB>codes' -> line, pos, sign, conf: [PLAIN:...] and '.' dropped, trailing '?' stripped (conf M)."""
    n = 0
    with open(dst, 'w') as f:
        f.write('line\tpos\tsign\tconf\n')
        for r in csv.DictReader(open(src), delimiter='\t'):
            toks = [t for t in PLAIN.sub(' ', r['codes']).split() if t != '.']
            p = 0
            for t in toks:
                conf = 'H'
                if t.endswith('?') and len(t) > 1:
                    t, conf = t[:-1], 'M'
                p += 1
                f.write(f"f102v_{r['row']}\t{p}\t{t}\t{conf}\n"); n += 1
    return n


def agree():
    a = long_form(os.path.join(T, 'tx/f102v_passA.tsv'), os.path.join(HERE, 'passA_long.tsv'))
    b = long_form(os.path.join(T, 'tx/f102v_passB.tsv'), os.path.join(HERE, 'passB_long.tsv'))
    out = os.path.join(HERE, 'rec')
    os.makedirs(out, exist_ok=True)
    cmd = [sys.executable, os.path.join(REPO, 'tools/reconcile_passes.py'), os.path.join(HERE, 'passA_long.tsv'),
           os.path.join(HERE, 'passB_long.tsv'), '--method', 'nw', '--out-dir', out]
    log = subprocess.run(cmd, capture_output=True, text=True)
    if log.returncode:
        sys.exit(log.stdout + log.stderr)
    open(os.path.join(out, 'reconcile.log'), 'w').write(' '.join(cmd[1:]) + '\n' + log.stdout)
    absent = set()
    for r in csv.DictReader(open(os.path.join(out, 'disagreements.tsv')), delimiter='\t'):
        if r['A'] == '-':
            absent.add((r['line'], int(r['col'])))
    posA = collections.Counter()
    n_ag = 0
    with open(os.path.join(HERE, 'agree.tsv'), 'w') as f:
        f.write('line\tpos\tsign\twhy\n')
        for r in csv.DictReader(open(os.path.join(out, 'ciphertext_draft.tsv')), delimiter='\t'):
            ln, col = r['line'], int(r['position'])
            if (ln, col) in absent:
                continue
            posA[ln] += 1
            if r['why'] in ('agree', 'agree-flagged'):
                f.write(f"{ln}\t{posA[ln]}\t{r['sign']}\t{r['why']}\n"); n_ag += 1
    # consistency: pass A positions walked == pass A token count per line
    cntA = collections.Counter(r['line'] for r in csv.DictReader(open(os.path.join(HERE, 'passA_long.tsv')), delimiter='\t'))
    bad = {l: (posA[l], cntA[l]) for l in cntA if posA[l] != cntA[l]}
    print(f'agree: pass A tokens {a}, pass B {b}; agree positions {n_ag}; pass-A walk mismatch lines: {bad or "none"}')
    print(log.stdout.strip().splitlines()[0])


if __name__ == '__main__':
    {'segment': segment, 'agree': agree}[sys.argv[1]]()
