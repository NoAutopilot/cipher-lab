#!/usr/bin/env python3
"""Known-plaintext alignment of 4.VEL 2061's No.1-6 battery list and a-g legend against the Atlas of Mutual Heritage
page 2218 English summary rendered as period-Dutch candidate words (candidates_2061_amh.tsv, committed before this
script was first run). GAPS10-na-suriname-map-1781, 2 Oct 2026 (CLAUDE.md rule 3).

Pre-registered decision rule (fixed before the first run):
  placement  every candidate word of an entry against every same-length window inside every cipher word of that entry
             (plain 'w:' tokens are skipped; entries are cut at the plain label letters a-g and at line starts No1-No6/L07).
  fit        0 conflicts with the current key (key.tsv + key_2039_aliases.tsv + key_2061_crib.tsv; one sign never asked
             for two letters) and >= 2 keyed signs agreeing.
  control A  the same candidate at every other same-length window of every cipher word on 2061 and on 2039's legend
             (same hand and key): share of windows that are also 0-conflict with agree >= the placement's agree.
             Pass: share <= 0.05.
  control B  the placement's implied values permuted among its implied signs, 20 seeds; S2 = mean nl_repo bigram
             log P over adjacent keyed pairs outside the placement that use an implied value (as crib_2061_batterijen.py).
             Pass: <= 1/20 seeds at or above the real S2. Fewer than 2 distinct implied letters: B cannot vary, no pass.
  S          a fit passing both A and B; its implied values are proposals (grade S only on the placement's own tokens).
  Values asked of one sign by two passing fits with different letters are held (not added).
Output: TSV of every fit to align_2061_amh.out.tsv, summary to stdout. Usage: python3 align_2061_amh.py [--seeds 20] [--entry-null] [--round2]
(--entry-null and --round2 added after the first run, declared as such in NOTES.md; the rule itself is unchanged.)
"""
import csv, os, re, sys, math, random, statistics, collections
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
seeds = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 20

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

key = {}
for f in ('key.tsv', 'key_2039_aliases.tsv', 'key_2061_crib.tsv'):
    key.update({r['code']: r['value'] for r in rows(os.path.join(here, f))
                if r.get('source') != 'align_2061_amh'})  # round 1 scores against the pre-GAPS10 key

# 2061 cipher words with their entry label
words = collections.OrderedDict(); entry_of = {}; cur = None
for r in rows(os.path.join(here, 'ciphertext_2061_battery.tsv')):
    s = r['sign']; ln = r['line']; n = int(ln.split('_L')[1])
    if r['pos'] == '0':
        cur = f'No{n}' if n <= 6 else ('L07' if n == 7 else cur)
    if s.startswith('w:'):
        if n >= 8 and s[2:] in list('abcdefg'): cur = s[2:]  # label letters only on L08-L10 ('w:d' in No.1-6 is the plain lb sign)
        continue
    wk = (ln, r['word']); words.setdefault(wk, []).append(s); entry_of.setdefault(wk, cur)
# 2039 cipher words (control pool)
w39 = collections.OrderedDict()
for r in rows(os.path.join(here, 'ciphertext_2039_legend.tsv')):
    if not r['sign'].startswith('w:'):
        w39.setdefault((r['line'], r.get('word', '')), []).append(r['sign'])

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

def s2(wk, start, L, implied):
    k = dict(key); k.update(implied); vals = []
    for w, signs in words.items():
        for i in range(len(signs) - 1):
            if w == wk and start <= i and i + 1 < start + L:
                continue
            a, b = signs[i], signs[i + 1]
            if (a in implied or b in implied) and a in k and b in k:
                vals.append(lp(k[a], k[b]))
    return (statistics.mean(vals) if vals else float('nan')), len(vals)

pool = {}
def windows(L):
    if L not in pool:
        pool[L] = [((src, wk, i), s[i:i + L]) for src, d in (('2061', words), ('2039', w39))
                   for wk, s in d.items() for i in range(len(s) - L + 1)]
    return pool[L]

cands = {r['entry']: r['words'].split() for r in rows(os.path.join(here, 'candidates_2061_amh.tsv'))}

def run(cands):
  tested = 0; fits = []
  for wk, signs in words.items():
      e = entry_of[wk]
      for cand in dict.fromkeys(cands.get(e, [])):
          L = len(cand)
          for i in range(len(signs) - L + 1):
              tested += 1
              ag, cf, imp = place(signs[i:i + L], cand)
              if cf or ag < 2:
                  continue
              others = [p for p in windows(L) if p[0] != ('2061', wk, i)]
              hit = sum(1 for _, sg in others if (lambda a, c, _i: c == 0 and a >= ag)(*place(sg, cand)))
              shareA = hit / len(others)
              real, n2 = s2(wk, i, L, imp)
              letters = list(imp.values())
              if len(set(letters)) < 2 or real != real:
                  bge = None
              else:
                  cb = []
                  for sd in range(seeds):
                      v = letters[:]; random.Random(sd).shuffle(v)
                      cb.append(s2(wk, i, L, dict(zip(imp, v)))[0])
                  bge = sum(1 for c in cb if c >= real)
              ok = shareA <= 0.05 and bge is not None and bge <= seeds // 20
              fits.append(dict(entry=e, line=wk[0], word=wk[1], start=i, cand=cand, signs=' '.join(signs[i:i + L]),
                               agree=ag, implied=' '.join(f'{s}={c}' for s, c in imp.items()), shareA=round(shareA, 4),
                               nA=len(others), S2=round(real, 3) if real == real else '', nS2=n2,
                               Bge=('cannot-vary' if bge is None else f'{bge}/{seeds}'), passed='S' if ok else '-'))
  return tested, fits

# null 3 (whole procedure): candidate lists derangement-shuffled across entries, same rule, 20 seeds
ents = list(cands)
if '--entry-null' in sys.argv:
    res = []
    for sd in range(seeds):
        rng = random.Random(1000 + sd)
        while True:
            perm = ents[:]; rng.shuffle(perm)
            if all(a != b for a, b in zip(ents, perm)): break
        _, f0 = run({a: cands[b] for a, b in zip(ents, perm)})
        res.append(sum(f['passed'] == 'S' for f in f0))
        for f in f0:
            if f['passed'] == 'S': print(f'  null seed {sd}: {f["entry"]} {f["line"]} w{f["word"]} {f["cand"]} = {f["signs"]} (list from {dict(zip(ents, perm))[f["entry"]]})')
    print(f'entry-shuffle null ({seeds} seeds): passing fits per run {res}; mean {statistics.mean(res):.2f}; '
          f'runs with >= 1 pass {sum(r >= 1 for r in res)}/{seeds}')
    sys.exit(0)
if '--round2' in sys.argv:  # declared iteration: passing round-1 values join the key as M, identical rule
    _, f1 = run(cands)
    for f in f1:
        if f['passed'] == 'S':
            for kv in f['implied'].split():
                a, c = kv.rsplit('=', 1); key[a] = c
    print('round 2 key adds:', ' '.join(kv for f in f1 if f['passed'] == 'S' for kv in f['implied'].split()))
tested, fits = run(cands)
out = os.path.join(here, 'align_2061_amh.out' + ('_round2' if '--round2' in sys.argv else '') + '.tsv')
with open(out, 'w') as fh:
    fh.write('# Generated by align_2061_amh.py (GAPS10, 2 Oct 2026); every fit (0 conflicts, >=2 agree) with both controls.\n')
    wr = csv.DictWriter(fh, fieldnames=list(fits[0]), delimiter='\t') if fits else None
    if wr:
        wr.writeheader(); wr.writerows(fits)
print(f'placements tested {tested}; fits (0 conflicts, >=2 keyed agree) {len(fits)}; passing both controls '
      f'{sum(f["passed"] == "S" for f in fits)}')
for f in fits:
    print('\t'.join(str(f[k]) for k in ('passed', 'entry', 'line', 'word', 'start', 'cand', 'signs', 'agree', 'implied',
                                         'shareA', 'S2', 'nS2', 'Bge')))
held = collections.defaultdict(set)
for f in fits:
    if f['passed'] == 'S':
        for kv in f['implied'].split():
            s, c = kv.rsplit('=', 1); held[s].add(c)
print('values from passing fits:', ' '.join(f'{s}={"/".join(sorted(v))}' for s, v in held.items()) or 'none')
