#!/usr/bin/env python3
"""Round 3 of the AMH page 2218 alignment of 4.VEL 2061 (GAPS11-na-suriname-map-1781, 2 Oct 2026): the i/j/y(/ij) letter
class and multi-word candidates. The rule is pre-registered in candidates_2061_amh_r3.tsv's header (commit 102e88a1,
before this script was first run); the single-word lists of candidates_2061_amh.tsv (GAPS10) are re-run under the merge.
Usage: python3 align_2061_amh_r3.py [--seeds 20] [--entry-null] [--y-free]
"""
import csv, os, re, sys, math, random, statistics, collections
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
seeds = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 20
N = lambda s: s.lower().replace('ij', 'y').replace('i', 'y').replace('j', 'y')
Nl = lambda c: 'y' if c in 'ijy' else c

def rows(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))

txt = ''
for f in sorted(os.listdir(os.path.join(root, 'tools/data/nl_repo'))):
    if f.endswith('_plaintext_print.txt'):
        txt += open(os.path.join(root, 'tools/data/nl_repo', f), errors='ignore').read().lower()
big = collections.Counter(); uni = collections.Counter()
for w in re.findall(r'[a-z]+', txt):
    w = N(w)
    for a, b in zip(w, w[1:]):
        big[a + b] += 1; uni[a] += 1
lp = lambda a, b: math.log((big[a + b] + 1) / (uni[a] + 26))

key = {}
for f in ('key.tsv', 'key_2039_aliases.tsv', 'key_2061_crib.tsv'):
    key.update({r['code']: Nl(r['value']) for r in rows(os.path.join(here, f)) if r.get('source') != 'align_2061_amh_r3'})
if '--y-free' in sys.argv:
    key.pop('y', None)

# entry streams on 2061 (signs + (line,pos)), line streams on 2061 and 2039 for control A
ent = collections.OrderedDict(); lines61 = collections.OrderedDict(); cur = None
for r in rows(os.path.join(here, 'ciphertext_2061_battery.tsv')):
    s = r['sign']; ln = r['line']; n = int(ln.split('_L')[1])
    if r['pos'] == '0':
        cur = f'No{n}' if n <= 6 else ('L07' if n == 7 else cur)
    if s.startswith('w:'):
        if n >= 8 and s[2:] in list('abcdefg'): cur = s[2:]
        continue
    ent.setdefault(cur, []).append((s, ln, int(r['pos'])))
    lines61.setdefault(ln, []).append((s, ln, int(r['pos'])))
lines39 = collections.OrderedDict()
for r in rows(os.path.join(here, 'ciphertext_2039_legend.tsv')):
    if not r['sign'].startswith('w:'):
        lines39.setdefault(r['line'], []).append(r['sign'])

def place(signs, cand):
    ag = cf = 0; imp = {}
    for s, c in zip(signs, cand):
        if s in key:
            if key[s] == c: ag += 1
            else: cf += 1
        elif s in imp:
            if imp[s] != c: cf += 1
        else:
            imp[s] = c
    return ag, cf, imp

def s2(skip, implied):
    k = dict(key); k.update(implied); vals = []
    for ln, st in lines61.items():
        for i in range(len(st) - 1):
            if (ln, st[i][2]) in skip and (ln, st[i + 1][2]) in skip:
                continue
            a, b = st[i][0], st[i + 1][0]
            if (a in implied or b in implied) and a in k and b in k:
                vals.append(lp(k[a], k[b]))
    return (statistics.mean(vals) if vals else float('nan')), len(vals)

pool = {}
def windows(L):
    if L not in pool:
        pool[L] = [(('61', ln, st[i][2]), [x[0] for x in st[i:i + L]]) for ln, st in lines61.items() for i in range(len(st) - L + 1)]
        pool[L] += [(('39', ln, i), st[i:i + L]) for ln, st in lines39.items() for i in range(len(st) - L + 1)]
    return pool[L]

def renderings(w):
    w = w.lower().replace(' ', '')
    r1 = ''.join(Nl(c) for c in w); r2 = N(w)
    return list(dict.fromkeys([r1, r2]))

single = {r['entry']: r['words'].split() for r in rows(os.path.join(here, 'candidates_2061_amh.tsv'))}
multi = {r['entry']: r['words'].split('|') for r in rows(os.path.join(here, 'candidates_2061_amh_r3.tsv'))}
cands = {e: list(dict.fromkeys(rd for w in single.get(e, []) + multi.get(e, []) for rd in renderings(w)))
         for e in list(dict.fromkeys(list(single) + list(multi)))}
src = {}
for e in cands:
    for w in single.get(e, []) + multi.get(e, []):
        for rd in renderings(w): src.setdefault((e, rd), w)

def run(cands, slow=True):
    tested = 0; fits = []
    for e, st in ent.items():
        signs = [x[0] for x in st]
        for cand in cands.get(e, []):
            L = len(cand)
            for i in range(len(signs) - L + 1):
                tested += 1
                ag, cf, imp = place(signs[i:i + L], cand)
                if cf or ag < 2:
                    continue
                me = ('61', st[i][1], st[i][2])
                others = [p for p in windows(L) if p[0] != me]
                hit = sum(1 for _, sg in others if (lambda a, c, _i: c == 0 and a >= ag)(*place(sg, cand)))
                shareA = hit / len(others) if others else 1.0
                skip = {(x[1], x[2]) for x in st[i:i + L]}
                real, n2 = s2(skip, imp)
                letters = list(imp.values())
                if len(set(letters)) < 2 or real != real:
                    bge = None
                else:
                    cb = []
                    for sd in range(seeds):
                        v = letters[:]; random.Random(sd).shuffle(v)
                        cb.append(s2(skip, dict(zip(imp, v)))[0])
                    bge = sum(1 for c in cb if c >= real)
                ok = shareA <= 0.05 and bge is not None and bge <= seeds // 20
                fits.append(dict(entry=e, line=st[i][1], pos=st[i][2], cand=cand, from_word=src.get((e, cand), '?'),
                                 signs=' '.join(signs[i:i + L]), agree=ag,
                                 implied=' '.join(f'{s}={c}' for s, c in imp.items()), shareA=round(shareA, 4),
                                 nA=len(others), S2=round(real, 3) if real == real else '', nS2=n2,
                                 Bge=('cannot-vary' if bge is None else f'{bge}/{seeds}'), passed='S' if ok else '-',
                                 positions=' '.join(f'{x[1]}:{x[2]}' for x in st[i:i + L])))
    return tested, fits

if '--entry-null' in sys.argv:
    ents = list(cands); res = []
    for sd in range(seeds):
        rng = random.Random(1000 + sd)
        while True:
            perm = ents[:]; rng.shuffle(perm)
            if all(a != b for a, b in zip(ents, perm)): break
        _, f0 = run({a: cands[b] for a, b in zip(ents, perm)})
        res.append(sum(f['passed'] == 'S' for f in f0))
        for f in f0:
            if f['passed'] == 'S': print(f'  null seed {sd}: {f["entry"]} {f["line"]}:{f["pos"]} {f["cand"]} = {f["signs"]} (list from {dict(zip(ents, perm))[f["entry"]]})')
    print(f'entry-shuffle null ({seeds} seeds): passing fits per run {res}; mean {statistics.mean(res):.2f}; '
          f'runs with >= 1 pass {sum(r >= 1 for r in res)}/{seeds}')
    sys.exit(0)
tested, fits = run(cands)
tag = '_yfree' if '--y-free' in sys.argv else ''
out = os.path.join(here, f'align_2061_amh_r3{tag}.out.tsv')
with open(out, 'w') as fh:
    fh.write('# Generated by align_2061_amh_r3.py (GAPS11, 2 Oct 2026); every fit (0 conflicts, >=2 agree, i/j/y class) with both controls.\n')
    if fits:
        wr = csv.DictWriter(fh, fieldnames=list(fits[0]), delimiter='\t'); wr.writeheader(); wr.writerows(fits)
print(f'candidate renderings {sum(len(v) for v in cands.values())}; placements tested {tested}; fits {len(fits)}; '
      f'passing both controls {sum(f["passed"] == "S" for f in fits)}')
for f in fits:
    print('\t'.join(str(f[k]) for k in ('passed', 'entry', 'line', 'pos', 'cand', 'signs', 'agree', 'implied', 'shareA', 'nA', 'S2', 'nS2', 'Bge')))
held = collections.defaultdict(set)
for f in fits:
    if f['passed'] == 'S':
        for kv in f['implied'].split():
            s, c = kv.rsplit('=', 1); held[s].add(c)
print('values from passing fits:', ' '.join(f'{s}={"/".join(sorted(v))}' for s, v in held.items()) or 'none')
