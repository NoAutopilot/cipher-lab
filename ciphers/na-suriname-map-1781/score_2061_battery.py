#!/usr/bin/env python3
"""Score the transferred-key decode of 4.VEL 2061's battery list and a-g legend (reading_2061_battery_tokens.tsv) for
Dutch-ness, against shuffled-key controls (CLAUDE.md rule 3). GAPS8-na-suriname-map-1781, 2 Oct 2026.

Statistic: mean log P(b|a) over every pair of ADJACENT keyed positions inside one cipher word (both signs keyed, grade
M), with a letter-bigram model (add-one smoothing) built from tools/data/nl_repo's 17th-century Dutch print texts.
Control: the same ciphertext decoded with a SHUFFLED key -- the key's value column permuted among its codes (value
multiset kept, aliases follow their code), N seeds. The control changes which letter each sign yields, which is exactly
what the bigram statistic reads, so it can vary on the statistic's own axis (not a coverage-only non-test). A real key
that transfers to this sheet should put the real statistic above most shuffled keys; a key that does not, inside them.
Exit 0 always; the numbers are what counts. Usage: python3 score_2061_battery.py [--seeds 20]
"""
import csv, os, random, re, sys, math, statistics, collections
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
seeds = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 20

def rows(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))

# bigram model
txt = ''
for f in sorted(os.listdir(os.path.join(root, 'tools/data/nl_repo'))):
    if f.endswith('_plaintext_print.txt'):
        txt += open(os.path.join(root, 'tools/data/nl_repo', f), errors='ignore').read().lower()
words = re.findall(r'[a-z]+', txt)
big = collections.Counter(); uni = collections.Counter()
for w in words:
    for a, b in zip(w, w[1:]):
        big[a + b] += 1; uni[a] += 1
def lp(a, b):
    return math.log((big[a + b] + 1) / (uni[a] + 26))

# key: code -> value (key.tsv + key_2039_aliases.tsv)
key = {r['code']: r['value'] for r in rows(os.path.join(here, 'key.tsv'))}
alias = {r['code']: r['value'] for r in rows(os.path.join(here, 'key_2039_aliases.tsv'))}
ct = rows(os.path.join(here, 'ciphertext_2061_battery.tsv'))
# word segmentation: a new word starts where the ciphertext row's 'word' column changes
seq = [(r['line'], r['word'], r['sign']) for r in ct]

def score(k):
    vals = []
    for (l1, w1, s1), (l2, w2, s2) in zip(seq, seq[1:]):
        if (l1, w1) != (l2, w2):
            continue
        a, b = k.get(s1), k.get(s2)
        if a and b and len(a) == 1 and len(b) == 1:
            vals.append(lp(a, b))
    return (statistics.mean(vals) if vals else float('nan')), len(vals)

full = dict(key); full.update(alias)
real, npairs = score(full)
codes = list(key); values = [key[c] for c in codes]
ctrl = []
for s in range(seeds):
    rnd = random.Random(s); v = values[:]; rnd.shuffle(v)
    k = dict(zip(codes, v))
    for a, val in alias.items():  # an alias follows the code whose value it shares in the real key
        tgt = [c for c in codes if key[c] == val]
        k[a] = k[tgt[0]] if tgt else val
    ctrl.append(score(k)[0])
m = statistics.mean(ctrl); sd = statistics.pstdev(ctrl) or 1e-9
ge = sum(1 for c in ctrl if c >= real)
p95 = sorted(ctrl)[int(0.95 * (len(ctrl) - 1))]
print(f"keyed adjacent pairs: {npairs}")
print(f"real mean log P(b|a) {real:.3f}; shuffled-key ({seeds} seeds) mean {m:.3f} sd {sd:.3f} p95 {p95:.3f}; "
      f"z {(real - m) / sd:+.2f}; {ge}/{seeds} controls at or above real")
