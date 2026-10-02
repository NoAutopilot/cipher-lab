#!/usr/bin/env python3
"""Within-sheet crib test on 4.VEL 2061: legend e's 10-sign word (ciphertext_2061_battery.tsv L09 word 4,
"d [delta] r λ 7 o b t a h") against "batterijen", the word the sheet's own interlinear gloss writes over the
battery-list header ("De Batterijen zijn gedeponeerd"). GAPS9-na-suriname-map-1781, 2 Oct 2026 (CLAUDE.md rule 3).

S1 (key agreement): of the crib positions whose sign is already keyed (key.tsv + key_2039_aliases.tsv), how many
    carry the crib's letter; a placement that asks one sign for two letters, or a keyed sign for another letter, is a
    conflict.
S2 (rest-of-sheet fit): the crib's implied values for the unkeyed signs are added to the key and every adjacent pair of
    keyed signs inside one cipher word OUTSIDE the crib window that involves at least one implied sign is scored with
    the same nl_repo letter-bigram model as score_2061_battery.py (mean log P(b|a)); n = how many such pairs recur.
Control A (placement): the same crib at every other 10-sign word on the sheet (only one exists, L08 word 3) and, since
    one is too few, at every 10-sign window inside any cipher word of 10+ signs on the sheet; S1 and S2 for each.
Control B (shuffled implied values): the implied letters permuted among the implied signs, N seeds (default 20); S2
    each. S1 cannot vary under control B (it reads only the already-keyed signs), so B is a control on S2 only.
Exit 0 always. Usage: python3 crib_2061_batterijen.py [--seeds 20] [--crib batterijen] [--pool2039]
(--pool2039 adds control A': S1 at every 10-sign window of ciphertext_2039_legend.tsv, same hand and key.)
"""
import csv, os, re, sys, math, random, statistics, collections
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
arg = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
seeds = int(arg('--seeds', 20)); crib = arg('--crib', 'batterijen')

def rows(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))

txt = ''
for f in sorted(os.listdir(os.path.join(root, 'tools/data/nl_repo'))):
    if f.endswith('_plaintext_print.txt'):
        txt += open(os.path.join(root, 'tools/data/nl_repo', f), errors='ignore').read().lower()
big = collections.Counter(); uni = collections.Counter()
for w in re.findall(r'[a-z]+', txt):
    for a, b in zip(w, w[1:]):
        big[a + b] += 1; uni[a] += 1
lp = lambda a, b: math.log((big[a + b] + 1) / (uni[a] + 26))

key = {r['code']: r['value'] for r in rows(os.path.join(here, 'key.tsv'))}
key.update({r['code']: r['value'] for r in rows(os.path.join(here, 'key_2039_aliases.tsv'))})
words = collections.OrderedDict()
for r in rows(os.path.join(here, 'ciphertext_2061_battery.tsv')):
    if r['sign'].startswith('w:'):
        continue
    words.setdefault((r['line'], r['word']), []).append(r['sign'])
L = len(crib)
TARGET = ('2061_bat_L09', '4')

def place(wk, start):
    signs = words[wk][start:start + L]
    agree = conflict = 0; implied = {}
    for s, c in zip(signs, crib):
        if s in key:
            if key[s] == c: agree += 1
            else: conflict += 1
        elif s in implied and implied[s] != c:
            conflict += 1
        else:
            implied[s] = c
    return agree, conflict, implied

def s2(wk, start, implied):
    k = dict(key); k.update(implied); vals = []
    for w, signs in words.items():
        for i in range(len(signs) - 1):
            if w == wk and start <= i < start + L and i + 1 < start + L:
                continue  # pair inside the crib window
            a, b = signs[i], signs[i + 1]
            if (a in implied or b in implied) and a in k and b in k:
                vals.append(lp(k[a], k[b]))
    return (statistics.mean(vals) if vals else float('nan')), len(vals)

ag, cf, imp = place(TARGET, 0)
real2, n2 = s2(TARGET, 0, imp)
print(f"crib '{crib}' on {TARGET[0]} word {TARGET[1]}: {' '.join(words[TARGET][:L])}")
print(f"S1 real: {ag} keyed signs agree, {cf} conflicts; implied {len(imp)}: " +
      ' '.join(f"{s}={c}" for s, c in imp.items()))
print(f"S2 real: mean log P {real2:.3f} over {n2} recurring pairs outside the window")

# control A
same = [(w, 0) for w, s in words.items() if len(s) == L and w != TARGET]
wins = [(w, i) for w, s in words.items() for i in range(len(s) - L + 1) if (w, i) != (TARGET, 0)]
def ctlA(pl, name):
    if not pl:
        print(f'control A ({name}): no placements'); return
    s1 = []; s2v = []
    for w, i in pl:
        a, c, im = place(w, i); s1.append((a, c))
        if c == 0:
            s2v.append(s2(w, i, im)[0])
    ge1 = sum(1 for a, c in s1 if a >= ag and c <= cf)
    clean = [v for v in s2v if v == v]
    ge2 = sum(1 for v in clean if v >= real2)
    print(f"control A ({name}, {len(pl)} placements): S1 agree>={ag} with conflicts<={cf}: {ge1}/{len(pl)}; "
          f"mean agree {statistics.mean(a for a, c in s1):.2f}, mean conflicts {statistics.mean(c for a, c in s1):.2f}; "
          f"conflict-free placements {len(s2v)}, S2 at or above real {ge2}/{len(clean)}" +
          (f" (their mean {statistics.mean(clean):.3f})" if clean else ''))
ctlA(same, 'other 10-sign words')
ctlA(wins, 'every other 10-sign window')
if '--pool2039' in sys.argv:  # S1 only: the same hand and key on 2039's legend (S2 is scored on 2061, so not here)
    w39 = collections.OrderedDict()
    for r in rows(os.path.join(here, 'ciphertext_2039_legend.tsv')):
        if not r['sign'].startswith('w:'):
            w39.setdefault((r['line'], r.get('word', '')), []).append(r['sign'])
    pl = [s[i:i + L] for s in w39.values() for i in range(len(s) - L + 1)]
    res = []
    for signs in pl:
        a = c = 0; im = {}
        for x, ch in zip(signs, crib):
            if x in key: a, c = (a + 1, c) if key[x] == ch else (a, c + 1)
            elif x in im and im[x] != ch: c += 1
            else: im[x] = ch
        res.append((a, c))
    print(f"control A' (every 10-sign window of 2039's legend, S1 only, {len(pl)} placements): agree>={ag} with "
          f"conflicts<={cf}: {sum(1 for a, c in res if a >= ag and c <= cf)}/{len(pl)}; max agree {max(a for a, c in res)}; "
          f"conflict-free {sum(1 for a, c in res if c == 0)}")

# control B
signs_imp = list(imp); letters = [imp[s] for s in signs_imp]; cb = []
for sd in range(seeds):
    v = letters[:]; random.Random(sd).shuffle(v)
    cb.append(s2(TARGET, 0, dict(zip(signs_imp, v)))[0])
m = statistics.mean(cb); sdv = statistics.pstdev(cb) or 1e-9
print(f"control B (implied values shuffled, {seeds} seeds): S2 mean {m:.3f} sd {sdv:.3f} "
      f"p95 {sorted(cb)[int(0.95 * (seeds - 1))]:.3f}; real z {(real2 - m) / sdv:+.2f}; "
      f"{sum(1 for c in cb if c >= real2)}/{seeds} at or above real")
