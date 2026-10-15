#!/usr/bin/env python3
"""MONL-SORT2 (15 Oct 2026): the 40 tiles of sort/srt/PREREG-MONL-SORT2.md, in tools/lookalike_pass.py windows packet format, plus the
three passc files (c268c band L0n = c268 L(n+5); c268d = L(n+13); c268e = L(n+19)). Writes sort/srt/roles.tsv (line, pos, family, role,
candidates) for the reconciler only; nothing role-related goes into a prompt. Run from the folder."""
import csv
HDR = 'run\tpassage\tpos\tpassC\tA\tB\tstatus\twhy\tcandidates\tbefore\tafter\tnoteA\tnoteB\n'
T = []
def add(fam, role, cand, s):
    for x in s.split(): T.append((x.split(':')[0], x.split(':')[1], fam, role, cand))
add('A', 'lead', 'K04,K12', 'L06:18 L06:23 L06:34 L08:10 L08:19 L09:27 L10:33 L13:14 L15:4 L16:16 L18:18 L21:9 L22:14 L24:12 L25:26')
add('A', 'control', 'K04,K12', 'L14:14 L23:16 L25:17'); add('A', 'ref', 'K04,K12', 'L12:8 L14:13')
add('B', 'lead', 'K14,K37', 'L08:6 L08:22 L15:11 L11:20 L24:10 L21:7')
add('B', 'control', 'K14,K37', 'L12:9 L17:7'); add('B', 'ref', 'K14,K37', 'L11:5 L21:18')
add('C', 'lead', 'K40,K41', 'L12:21 L22:6 L24:29 L25:16'); add('C', 'lead', 'K39,K45', 'L24:3 L24:16')
add('C', 'ref', 'K40,K41', 'L21:13 L24:26'); add('C', 'ref', 'K39,K45', 'L13:13 L18:25')
assert len(T) == 40 and len({(a, b) for a, b, *_ in T}) == 40
BANDS = (('c268c', 6, 15, 5), ('c268d', 16, 20, 13), ('c268e', 21, 25, 19))
page = lambda n: next(b for b in BANDS if b[1] <= n <= b[2])
c268 = list(csv.DictReader(open('ciphertext_c268.tsv'), delimiter='\t'))
by = {}
for r in c268: by.setdefault(r['line'], []).append(r)
want = {(l, p): (f, ro, c) for l, p, f, ro, c in T}
out = {b[0]: [] for b in BANDS}
with open('sort/srt/roles.tsv', 'w') as o:
    o.write('page\tpassage\tline\tpos\tfamily\trole\tcandidates\tcurrent\n')
    for ln, rs in by.items():
        for i, r in enumerate(rs):
            if (ln, r['pos']) in want:
                f, ro, c = want[(ln, r['pos'])]; pg, lo, hi, sh = page(int(ln[1:]))
                assert r['sign'] in c.split(','), (ln, r['pos'], r['sign'], c)
                bef = ' '.join(x['sign'] for x in rs[max(0, i - 3):i]); aft = ' '.join(x['sign'] for x in rs[i + 1:i + 4])
                psg = f'L{int(ln[1:]) - sh:02d}'
                out[pg].append(['s' + pg[1:], psg, r['pos'], r['sign'], r['sign'], '', 'check', 'sort', c, bef, aft, '', ''])
                o.write(f'{pg}\t{psg}\t{ln}\t{r["pos"]}\t{f}\t{ro}\t{c}\t{r["sign"]}\n')
assert sum(map(len, out.values())) == 40
for pg, lo, hi, sh in BANDS:
    with open(f'sort/srt/{pg}_tiles.tsv', 'w') as o:
        o.write(HDR); [o.write('\t'.join(r) + '\n') for r in out[pg]]
    with open(f'sort/srt/{pg}_passc.tsv', 'w') as o:
        o.write('passage\tpos\tsign_id\n')
        for r in c268:
            n = int(r['line'][1:])
            if n - sh >= 1: o.write(f"L{n - sh:02d}\t{r['pos']}\t{r['sign']}\n")
    print(pg, len(out[pg]))
