"""N8-BIRNUM post-hoc qualifier (NOT pre-registered, not gating): power control with the target's own code-occurrence
profile (family D: 5 types x 8,8,4,4,3 occurrences), 40 and 30 cells, 5% strays. The 5 most frequent words (len >= 2)
in a ~560-letter it16dip span become word codes; each code's occurrences beyond its target count stay spelled."""
import random, collections, sys
from codes_test import corpus_text, occurrences, select, T_stat, null_T, pct
PROFILE = [8, 8, 4, 4, 3]

def trial(words, seed, cells, draws=500):
    rng = random.Random(seed)
    start = rng.randrange(0, len(words) - 600)
    span, n = [], 0
    for w in words[start:]:
        span.append(w); n += len(w)
        if n >= 560: break
    top = [w for w, k in collections.Counter(w for w in span if len(w) >= 2).most_common(5)]
    pool = [a + b for a in '01234589' for b in '01234589']; rng.shuffle(pool)
    codes = {w: pool.pop() for w in top}; left = {w: PROFILE[i] for i, w in enumerate(top)}
    freq = collections.Counter(''.join(span)); letters = sorted(freq, key=lambda x: -freq[x])
    table = {l: [pool.pop()] for l in letters}
    for k in range(max(0, cells - len(letters))): table[letters[k % len(letters)]].append(pool.pop())
    items = []
    for w in span:
        if w in codes and left[w] > 0:
            left[w] -= 1; items.append(('g', codes[w])); continue
        for ch in w:
            for d in rng.choice(table[ch]): items.append(('d', d))
            if rng.random() < 0.05: items.append(('d', rng.choice('01234589')))
    streams, occ = occurrences([items], 'D'); occ = select(occ, 'D')
    T, _ = T_stat(streams, occ); nl = null_T(streams, occ, draws, rng)
    return T, pct(nl, 0.99), sum(len(v) for v in occ.values())

words = corpus_text().split()
out = []
for cells in (40, 30):
    rows, hits = [], 0
    for s in range(1, 21):
        T, p99, nocc = trial(words, 100 + s, cells); hits += T > p99; rows.append(f'{s}:T{T}/p99 {p99}/occ{nocc}')
    out.append(f'matched control {cells} cells: {hits}/20 trials T > own null p99; ' + ' '.join(rows))
    print(out[-1])
open('matched_control_out.txt', 'w').write('\n'.join(out) + '\n')
