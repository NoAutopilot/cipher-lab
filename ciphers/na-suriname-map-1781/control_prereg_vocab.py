#!/usr/bin/env python3
"""Pre-registered rule-3 control for the period key (GAPS14-na-suriname-map-1781, 2 Oct 2026).

Replaces control_period_key.py's post-hoc vocabulary (GAPS13 caveat) with vocab_prereg.txt, built mechanically from the
plain sibling legends crib_2038_legend.tsv and crib_2042_legend.tsv and committed BEFORE this script was first run.
Statistic: number of (word, start) hits of a vocabulary word (4+ letters) inside one line of the 2039 legend and the
2061 block decoded under key_period_codes.tsv (two-valued entries a|b match either value; i/j/y match each other;
multi-letter code-group values never match a letter, so they act as breaks). Nulls, both able to vary on this statistic:
  (1) shuffled-value: the same codes with their single-letter values permuted (same value multiset and coverage);
  (2) shuffled-order: each line's tokens permuted under the real key (same letters, order destroyed).
1000 draws each, seed 14. Prints one line per null; exit 0."""
import csv, random, sys
VOCAB = [w.strip() for w in open('vocab_prereg.txt') if w.strip() and not w.startswith('#')]
def keymap(f):
    k = {}
    for r in csv.reader(open(f), delimiter='\t'):
        if not r or r[0].startswith('#') or r[0] == 'code': continue
        k[r[0]] = r[1]
    return k
def seqs(f):
    out = {}
    for r in csv.reader(open(f), delimiter='\t'):
        if not r or r[0].startswith('#') or r[0] == 'line': continue
        s = r[2]
        if s.startswith('w:') or s.startswith('p:'): continue
        out.setdefault(r[0], []).append(s)
    return list(out.values())
def opts_of(v):
    return set(x for x in v.split('|') if len(x) == 1) if v else set()
def hits(S, k):
    n = 0
    for seq in S:
        opts = [opts_of(k.get(s)) for s in seq]
        for w in VOCAB:
            L = len(w)
            for i in range(len(seq) - L + 1):
                if all(w[j] in opts[i+j] or (w[j] in 'ijy' and opts[i+j] & set('ijy')) for j in range(L)): n += 1
    return n
k = keymap(sys.argv[2] if len(sys.argv) > 2 else 'key_period_codes.tsv')  # arg 2 (key file) added GAPS14 after pre-registration; vocab and statistic unchanged
S = seqs('ciphertext_2039_legend.tsv') + seqs('ciphertext_2061_battery.tsv')
real = hits(S, k)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
rng = random.Random(14)
single = [c for c in k if all(len(x) == 1 for x in k[c].split('|'))]
def report(name, null):
    null.sort(); ge = sum(x >= real for x in null)
    print(f"{name}: real {real}; null mean {sum(null)/len(null):.2f}, p95 {null[int(.95*len(null))]}, max {null[-1]}; null >= real {ge}/{len(null)}")
vals = [k[c] for c in single]; null = []
for _ in range(N):
    rng.shuffle(vals); kk = dict(k); kk.update(zip(single, vals)); null.append(hits(S, kk))
report(f"vocab_prereg ({len(VOCAB)} words) shuffled-value", null)
null = []
for _ in range(N):
    SS = [rng.sample(s, len(s)) for s in S]; null.append(hits(SS, k))
report(f"vocab_prereg ({len(VOCAB)} words) shuffled-order", null)
