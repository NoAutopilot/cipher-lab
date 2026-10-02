#!/usr/bin/env python3
"""ce36_context.py -- GAPS12 (2 Oct 2026): is code 36 c or e? Disk-only context test (CLAUDE.md rule 3).
Statistic: at each body occurrence of 36, D = sum of log10 P over the 4-grams covering that letter (es18 model,
tools/judge_plaintext.NgramModel, n=4) with 36=c minus with 36=e, in the key-regenerated body text (L01-L14,
NULL/[?] dropped, every other token at its committed value). Target: D summed over the 4 occurrences, and the
count of occurrences preferring c.
Controls (each can vary on D, since it moves the substitution to positions with different neighbours):
 (a) shuffled-assignment, --seeds seeds: the same c-vs-e substitution at 4 random C-graded body positions (any
     letter, not code 36) -- the model's bare c/e bias in arbitrary context; the target beats it only above the max.
 (b) known answer: every C-graded body token whose value is c or e, swapped to the other letter; the share where
     the model prefers the true letter is the instrument's single-position power at this N.
Usage: python3 body/ce36_context.py [--seeds 20] [--corpus es18]
"""
import argparse, csv, math, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, 'tools')); import judge_plaintext as J
ap = argparse.ArgumentParser(); ap.add_argument('--seeds', type=int, default=20); ap.add_argument('--corpus', default='es18'); a = ap.parse_args()
BODY = ['L%02d' % i for i in range(1, 15)]
toks = [r for r in csv.DictReader(open(os.path.join(T, 'reading_tokens.tsv'), encoding='utf-8'), delimiter='\t')
        if r['line'] in BODY and r['value'] not in ('[?]', 'NULL') and J.fold(r['value'])]
text = [J.fold(r['value']) for r in toks]  # one letter per token
assert all(len(x) == 1 for x in text), 'multi-letter token'
M = J.NgramModel([J.read_corpus(q) for q in J.LANG_CORPORA[a.corpus]]); n = M.n
def lp(s, i):
    t = 0.0
    for j in range(max(n - 1, i), min(len(s), i + n)):
        g = s[j - n + 1:j + 1]; t += math.log10((M.c.get(g, 0) + M.k) / (M.ctx.get(g[:-1], 0) + 26 * M.k))
    return t
def D(i, x='c', y='e'):
    s = text[:]; s[i] = x; a1 = lp(''.join(s), i); s[i] = y; return a1 - lp(''.join(s), i)
pos36 = [i for i, r in enumerate(toks) if r['sign'] == '36']
print('corpus %s, body letters %d, code 36 at %d positions' % (a.corpus, len(text), len(pos36)))
tgt = []
for i in pos36:
    r = toks[i]; ctx = ''.join(text[max(0, i - 6):i]) + '[' + text[i] + ']' + ''.join(text[i + 1:i + 7])
    d = D(i); tgt.append(d); print('  %s pos%s  %s  D(c-e)=%+.3f  prefers %s' % (r['line'], r['pos'], ctx, d, 'c' if d > 0 else 'e'))
T_sum = sum(tgt); T_c = sum(1 for d in tgt if d > 0)
print('TARGET: sum D = %+.3f, %d of %d prefer c' % (T_sum, T_c, len(tgt)))
cand = [i for i, r in enumerate(toks) if r['grade'] == 'C' and r['sign'] != '36']
sums = []; cs = []
for sd in range(1, a.seeds + 1):
    rng = random.Random(sd); ps = rng.sample(cand, len(pos36)); ds = [D(i) for i in ps]
    sums.append(sum(ds)); cs.append(sum(1 for d in ds if d > 0))
ge = sum(1 for s in sums if s >= T_sum)
print('CONTROL (a) shuffled-assignment, %d seeds: sum D min %+.3f max %+.3f mean %+.3f; %d of %d at or above target; prefer-c count mean %.2f max %d'
      % (a.seeds, min(sums), max(sums), sum(sums) / len(sums), ge, a.seeds, sum(cs) / len(cs), max(cs)))
ka = [i for i, r in enumerate(toks) if r['grade'] == 'C' and text[i] in 'ce' and r['sign'] != '36']
ok = {'c': [0, 0], 'e': [0, 0]}
for i in ka:
    tr = text[i]; d = D(i, tr, 'e' if tr == 'c' else 'c'); ok[tr][1] += 1; ok[tr][0] += d > 0
tot = ok['c'][0] + ok['e'][0]; N = ok['c'][1] + ok['e'][1]
print('CONTROL (b) known answer: true letter preferred %d of %d (%.3f); true c %d/%d, true e %d/%d'
      % (tot, N, tot / max(N, 1), ok['c'][0], ok['c'][1], ok['e'][0], ok['e'][1]))
beat = T_sum > max(sums) and tot / max(N, 1) >= 0.8
print('VERDICT: %s' % ('target beats control (a) max and (b) >= 0.8 -- licenses S for the preferred letter' if beat else 'does not clear both controls -- code 36 stays M'))
