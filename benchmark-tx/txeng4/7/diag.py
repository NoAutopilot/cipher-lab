#!/usr/bin/env python3
"""TXE4-7 diagnostic of the positive control (dev_tune only, no eval line, no target score): for each of the 20 planted
piles, Delta_real for the restoring candidate against its 20 shuffled-key nulls, and whether the null maximum comes from a
shuffle that gives the candidate (or the planted sign) a multi-letter word value. EXPLORATORY beside it (declared here, not
pre-registered, never applied to a target): the same control with the null drawn by permuting values among single-letter
signs only (word codes keep their value)."""
import json, random, statistics, sys, os
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run as R  # noqa: E402
K = R.K
lm = R.load_lm(); key = K.read_key(R.F / 'harvest/key_1572_sheet.tsv'); nb = K.read_confusion(R.F / 'harvest/confusion_1572.tsv')
clusters = K.read_clusters(R.F / 'atlas/clusters.tsv'); cfg = R.ITEMS['no87']
base_dev = R.restrict(K.read_reading(cfg['base']), set(R.DEV)); pos_of = K.read_map_1to1(cfg['map'])
piles_dev = K.build_piles(base_dev, pos_of, clusters, set(R.DEV))
runs = json.load(open(HERE / 'out/build.json'))['positive_control']['runs']
letters = sorted(s for s, v in key.items() if len(v) == 1)
words = sorted(s for s, v in key.items() if len(v) > 1)
print(f'key: {len(letters)} single-letter signs, {len(words)} word/null signs ({", ".join(words)})')


def letter_shuffle(key, rnd):
    k2 = dict(key); vals = [key[s] for s in letters]; rnd.shuffle(vals)
    for s, v in zip(letters, vals):
        k2[s] = v
    return k2


rows = []; restored_L = 0
for r in runs:
    cl, sg, new = r['cluster'], r['sign'], r['planted']
    pos = piles_dev[(cl, sg)]
    b2 = {ln: [(p, new if (ln, p) in set(pos) else s) for p, s in rws] for ln, rws in base_dev.items()}
    sc = {ln: K.line_score([s for _, s in rws], key, lm) for ln, rws in b2.items()}
    d_real = K.pile_delta(b2, pos, sg, key, lm, sc)
    nulls, wordy = [], []
    for i in range(20):
        k2 = K.shuffled(key, random.Random(1 + i))
        sc2 = {ln: K.line_score([s for _, s in rws], k2, lm) for ln, rws in b2.items()}
        nulls.append(K.pile_delta(b2, pos, sg, k2, lm, sc2)); wordy.append(len(k2[sg]) > 1 or len(k2[new]) > 1)
    imax = max(range(20), key=lambda i: nulls[i])
    nullsL = []
    for i in range(20):
        k2 = letter_shuffle(key, random.Random(1 + i))
        sc2 = {ln: K.line_score([s for _, s in rws], k2, lm) for ln, rws in b2.items()}
        nullsL.append(K.pile_delta(b2, pos, sg, k2, lm, sc2))
    okL = d_real > 0 and d_real > max(nullsL)
    restored_L += okL
    rows.append(dict(seed=r['seed'], pile=f'({cl},{sg})->{new}', n=len(pos), d_real=round(d_real, 2), null_max=round(max(nulls), 2),
                     null_mean=round(statistics.mean(nulls), 2), argmax_wordy=wordy[imax], wordy_share=sum(wordy) / 20,
                     letter_null_max=round(max(nullsL), 2), letter_null_mean=round(statistics.mean(nullsL), 2), restored_letter_null=okL))
    print(rows[-1])
print(f'registered null: restored {sum(1 for r in rows if r["d_real"] > 0 and r["d_real"] > r["null_max"])}/20; null max from a word-valued shuffle in '
      f'{sum(r["argmax_wordy"] for r in rows)}/20 plants; mean share of shuffles giving the pair a word value {statistics.mean(r["wordy_share"] for r in rows):.2f}')
print(f'EXPLORATORY letter-only null: restored {restored_L}/20 (false accepts not measured here)')
json.dump(rows, open(HERE / 'score/diag_positive.json', 'w'), indent=1)
