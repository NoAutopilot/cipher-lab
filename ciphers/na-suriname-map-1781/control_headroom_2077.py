#!/usr/bin/env python3
"""Headroom (positive) control for the pre-registered vocabulary gate on 4.VEL 2077 (GAPS19-na-suriname-map-1781, 3 Oct 2026).
Written and committed with passes/leg2077_prereg.md BEFORE either blind pass was merged and before any 2077 token was decoded.

Question (rule 3, gain-gate clause): can control_prereg_vocab.py's statistic pass at all at this sheet's length? GAPS18's 2046
run came out real 3 vs shuffled-order max 3 (1/1000), a statistic sitting at its own floor. Here the sheet carries its OWN plain
Dutch legend entries (f Menagerie, g huijs voor den Opsigter, n bootehuijs ..., x nog een oud gebouw ...), which are genuine
1781 legend prose of the same kind the cipher entries encode. This script scores those plain words (the w: tokens of
ciphertext_2077_legend.tsv, letters only, lowercased, ÿ->ij, concatenated per line exactly as the cipher tokens are) with the
SAME vocabulary, statistic, seed and shuffled-order null, as if they were a perfectly decoded text:
  - full: all plain letters;  - matched: the plain letters truncated per line to the cipher-token count of the target
    (so the positive control has the target's own N; if the plain text is shorter, it is used whole and that is said).
Rule (stated now): if the positive control does not itself clear its shuffled-order null (real > null max, 0/1000) at matched
N, the gate has no headroom on this sheet and the target's vocabulary result is reported as a NON-TEST, whatever its number.
Usage: python3 control_headroom_2077.py [N=1000]"""
import csv, random, sys, unicodedata
VOCAB = [w.strip() for w in open('vocab_prereg.txt') if w.strip() and not w.startswith('#')]
def norm(t):
    t = t.lower().replace('ÿ', 'ij')
    t = ''.join(c for c in unicodedata.normalize('NFD', t) if not unicodedata.combining(c))
    return [c for c in t if 'a' <= c <= 'z']
plain, ncipher = {}, 0
for r in csv.reader(open('ciphertext_2077_legend.tsv'), delimiter='\t'):
    if not r or r[0].startswith('#') or r[0] == 'line': continue
    if r[2].startswith('w:'): plain.setdefault(r[0], []).extend(norm(r[2][2:]))
    else: ncipher += 1
def hits(S):
    n = 0
    for seq in S:
        for w in VOCAB:
            L = len(w)
            for i in range(len(seq) - L + 1):
                if all(w[j] == seq[i+j] or (w[j] in 'ijy' and seq[i+j] in 'ijy') for j in range(L)): n += 1
    return n
full = [s for s in plain.values() if s]
tot = sum(map(len, full))
# matched N: keep whole lines in file order until the cipher-token count is reached
matched, acc = [], 0
for s in full:
    if acc >= ncipher: break
    take = s[:ncipher - acc]; matched.append(take); acc += len(take)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
for name, S in (('full', full), ('matched', matched)):
    real = hits(S); rng = random.Random(14); null = []
    for _ in range(N): null.append(hits([rng.sample(s, len(s)) for s in S]))
    null.sort(); ge = sum(x >= real for x in null)
    print(f"plain-positive {name}: letters {sum(map(len, S))} (target cipher tokens {ncipher}, plain letters total {tot}); "
          f"real {real}; shuffled-order null mean {sum(null)/N:.2f}, p95 {null[int(.95*N)]}, max {null[-1]}; null >= real {ge}/{N}; "
          f"{'HEADROOM' if real > null[-1] else 'NO HEADROOM'}")
