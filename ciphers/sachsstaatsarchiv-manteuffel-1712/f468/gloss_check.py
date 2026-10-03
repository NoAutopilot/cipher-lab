#!/usr/bin/env python3
"""f.468 (694/08 frame 0580): Krauske key value vs the leaf's own interlinear gloss, with a shuffled-key control.
Match rule (fixed before scoring, GAPS154 3 Oct 2026): a single-letter key value matches when the gloss's first letter
is that letter (the leaf uses letter codes standing alone as initials: 39/9 Ilg., 44 Lol., 66 Arn); a longer value
matches when every content token of the gloss is a prefix of some content token of the value (Stenb. -> Stenbock,
Czar -> le czar). Alternatives (a|b) match if any does. The spelled group g13 (gloss Welling) is scored per letter
separately. Control: key values permuted over the key's codes, 10,000 draws, same instances, same rule; the statistic
(agreement) depends on which value sits on which code, which is what the permutation changes (rule 3).
python3 f468/gloss_check.py [--check]  (--check exits 1 if f468/gloss_check.txt is stale)"""
import csv, random, sys, unicodedata, os
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D)
key = {r['code']: r['value'] for r in csv.DictReader(open(f'{T}/key.tsv'), delimiter='\t')}
rows = [l.rstrip('\n').split('\t') for l in open(f'{D}/passes.tsv') if not l.startswith('#')]
STOP = {'le', 'la', 'l', 'de', 'du', 'des', 'et'}
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('roy', 'roi').replace("'", ' ')
    return [t for t in ''.join(c if c.isalpha() else ' ' for c in s).split() if t not in STOP]
def match(value, gloss):
    g = norm(gloss)
    for v in value.split('|'):
        vt = norm(v)
        if len(v.strip()) == 1:
            if g and g[0][0] == v.strip().lower(): return True
        elif g and vt and all(any(x.startswith(t) for x in vt) for t in g): return True
    return False
inst = [(r[4], r[7]) for r in rows if r[7] and '.' not in r[4]]
spelled = [(r[4].split('.'), r[7]) for r in rows if '.' in r[4]]
def score(k):
    a = sum(match(k.get(c, ''), g) for c, g in inst)
    sp = [(k.get(c, '?') if len(k.get(c, '')) == 1 else '?') for codes, _ in spelled for c in codes]
    return a, ''.join(sp)
def letters_ok(sp, word='welling'):
    return sum(a == b for a, b in zip(sp, word))
real, sp = score(key)
codes = list(key); vals = [key[c] for c in codes]; rng = random.Random(154); ctl = []; ctlsp = []
for _ in range(10000):
    rng.shuffle(vals); k = dict(zip(codes, vals)); a, s = score(k); ctl.append(a); ctlsp.append(letters_ok(s))
ctl.sort(); ctlsp.sort()
mean = sum(ctl) / len(ctl); p95 = ctl[9499]; p99 = ctl[9899]
distinct = {}
for c, g in inst: distinct.setdefault(c, []).append(match(key.get(c, ''), g))
out = [f'glossed single-code instances: {len(inst)}; key agrees: {real}/{len(inst)}',
       f'distinct glossed codes: {len(distinct)}; agree on all instances: {sum(all(v) for v in distinct.values())}/{len(distinct)}',
       f'shuffled-key control (10000 draws, seed 154): mean {mean:.2f}, p95 {p95}, p99 {p99}, max {ctl[-1]}; real >= p99: {real >= p99}',
       f'spelled group g13 (gloss Welling): key spells {sp!r}; letters matching "welling" by position: {letters_ok(sp)}/7; control mean {sum(ctlsp)/len(ctlsp):.2f}, p99 {ctlsp[9899]}',
       'misses: ' + (', '.join(f'{c}={key.get(c)!r} vs {g!r}' for c, g in inst if not match(key.get(c, ''), g)) or 'none')]
txt = '\n'.join(out) + '\n'
if '--check' in sys.argv:
    ok = open(f'{D}/gloss_check.txt').read() == txt; print('gloss_check.txt up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(f'{D}/gloss_check.txt', 'w').write(txt); print(txt, end='')
