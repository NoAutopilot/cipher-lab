#!/usr/bin/env python3
"""THUR-83274: decode l.83274's two unglossed rows (row 9 after 'the', row 10) under the period key sheet f.117.

python3 decode_83274_tail.py [--check]
- numerals: bm/passes/l83274_B1.tsv and _B2.tsv (blind passes; they agree on every numeral of these rows, asserted).
- key: bm/key_period_f117.tsv (sheet, H) cross-read with bm/key_blankmarshall_7.tsv (printed-gloss key, C); both must agree for H.
- slips: SLIPS below (group -> intended letter, grade M).
- control: PREREG-THUR83274.md (200 shuffles of the sheet's letter values, mean log10 4-gram, corpus tools/data/en16_repo) + power check.
Writes reading_l83274_tail.tsv/.txt and control_l83274_tail.tsv. --check exits 1 if any differs.
"""
import csv, math, os, random, sys, collections, glob
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
SLIPS = {(10, 18): 's'}   # 45 (l) where 'tricks' wants s; encipherment or printing slip, M
def rd(p): return list(csv.DictReader(open(os.path.join(H, p)), delimiter='\t'))
def passes(k): return rd(f'passes/l83274_{k}.tsv')
def norm(s): return ''.join(c for c in s.lower() if c.isalpha())
sheet = {int(r['value']): r['meaning'] for r in rd('key_period_f117.tsv') if r['kind'] == 'letter'}
gk = {int(r['value']): r['meaning'] for r in rd('key_blankmarshall_7.tsv') if r['value'].isdigit() and int(r['value']) < 100}
def tail(rows):
    out = []
    for r in rows:
        row, pos = int(r['row']), int(r['pos'])
        if (row == 9 and pos >= 13) or row == 10: out.append((row, pos, r['kind'], r['token']))
    return out
T1, T2 = tail(passes('B1')), tail(passes('B2'))
assert T1 == T2, 'B1 and B2 differ on the tail'
def grade(row, pos, v):
    if (row, pos) in SLIPS: return 'M'
    return 'H' if norm(sheet[v]) == norm(gk.get(v, '')) else 'M'
stream, tsv, segs, cur = [], ['row\tpos\ttoken\tsheet\tprinted_gloss_key\tgrade'], [], ''
for row, pos, kind, tok in T1:
    if kind == 'W': 
        out = tok; segs.append(cur); cur = ''
    else:
        v = int(tok); m = sheet[v]; g = grade(row, pos, v); cur += m
        tsv.append(f'{row}\t{pos}\t{tok}\t{m}\t{gk.get(v, "")}\t{g}')
segs.append(cur)
segs = [s for s in segs if s]
words, line = [], []
for row, pos, kind, tok in T1:
    words.append(tok if kind == 'W' else sheet[int(tok)])
text = ''.join(w if len(w) == 1 else ' ' + w + ' ' for w in words)
g = collections.Counter(l.split('\t')[5] for l in tsv[1:])
summ = f'groups {len(tsv)-1}; H {g["H"]}; C 0; S 0; M {g["M"]}; unread 0; slip {sorted(SLIPS)}\n'
rtxt = '(row 9 after "the" + row 10; clear words as printed, letters as sheet values, no word division imposed)\n' + ' '.join(
    ''.join(sheet[int(t[3])] if t[2] == 'N' else ' ' + t[3] + ' ' for t in T1[i:i+1]) for i in range(len(T1))) + '\n' + summ
# corpus / model
txt = []
for f in sorted(glob.glob(os.path.join(ROOT, 'tools', 'data', 'en16_repo', '*.txt'))):
    for l in open(f, encoding='utf-8', errors='ignore'):
        if not l.startswith('#'): txt.append(norm(l))
t = ''.join(txt); c4, c3 = collections.Counter(), collections.Counter()
for i in range(len(t) - 3): c4[t[i:i+4]] += 1; c3[t[i:i+3]] += 1
def score(segs):
    tot, n = 0.0, 0
    for s in segs:
        for i in range(len(s) - 3): tot += math.log10((c4[s[i:i+4]] + 0.1) / (c3[s[i:i+3]] + 2.6)); n += 1
    return tot / n if n else float('nan'), n
def shuffled(codes, vals, seed):
    v = vals[:]; random.Random(seed).shuffle(v); return dict(zip(codes, v))
codes = sorted(sheet); vals = [sheet[c] for c in codes]
def stats(numseg):  # numseg: list of lists of codes
    real, n = score([''.join(sheet[c] for c in s) for s in numseg])
    sh = sorted(score([''.join(m[c] for c in s) for s in numseg])[0] for m in (shuffled(codes, vals, k) for k in range(200)))
    return real, sum(sh) / 200, sh[190], n
segn, cur = [], []
for row, pos, kind, tok in T1:
    if kind == 'W':
        if cur: segn.append(cur); cur = []
    else: cur.append(int(tok))
if cur: segn.append(cur)
real, mean, p95, n = stats(segn)
# power: 28-letter windows of glossed rows 1-8
body = [r for r in passes('B1') if int(r['row']) <= 8 and r['kind'] == 'N']
ws = [[int(r['token']) for r in body[i:i+28] if int(r['token']) < 100] for i in range(0, len(body) - 27, 14)]
above = 0
for w in ws:
    rr, mm, pp, nn = stats([w]); above += rr > pp
pw = above / len(ws)
ctrl = ('statistic\treal\tshuffle_mean\tshuffle_p95\tn_4grams\tabove_p95\tcorpus_letters\n'
        f'mean_log10_4gram\t{real:.4f}\t{mean:.4f}\t{p95:.4f}\t{n}\t{real > p95}\t{len(t)}\n'
        f'power_windows(28 letters, rows1-8)\t{pw:.3f}\t\t\t{len(ws)}\t{pw >= 0.8}\t\n')
outs = {'reading_l83274_tail.tsv': '\n'.join(tsv) + '\n', 'reading_l83274_tail.txt': rtxt, 'control_l83274_tail.tsv': ctrl}
bad = 0
for f, s in outs.items():
    p = os.path.join(H, f)
    if '--check' in sys.argv:
        if not os.path.exists(p) or open(p).read() != s: print('STALE', f); bad = 1
    else: open(p, 'w').write(s)
if '--check' not in sys.argv: print(rtxt); print(ctrl)
sys.exit(bad)
