import json, csv, random
from collections import defaultdict, Counter

"""PX-BRODEC2 (25 Sept 2026): leave-one-out control over the appendix's own aligned code-letter pairs
(scripts/03_align_pairs.py's _pairs.json -- 391 pairs across 19 entries), with a matched synthetic
control per CLAUDE.md rule 3.

Why this replaces PX-BRODEC's gate: that gate compared body decodes against the appendix's Deciffrada
GLOSSES, which the period decipherer wrote abbreviated/paraphrased (documented failures, not key
failures -- NOTES.md 'Why this job'). This gate instead asks whether the key-building procedure itself
(majority vote over aligned pairs) generalises: hold out one entry's pairs, rebuild the key from every
OTHER entry's pairs with the identical majority rule 04_build_key.py uses, and see whether the
rebuilt key predicts the held-out entry's own already-known letters.

Real LOO: for entry E, tally = Counter of (code -> letter) over every pair NOT in E (04_build_key.py's
exact rule: base-fold accents, then majority). For each of E's own pairs, predict tally[code].most_common
letter if the code has >=1 observation elsewhere, else count it 'unkeyed-without-E'. Agreement is over
compared (non-unkeyed) tokens only, reported alongside the unkeyed share, per the job brief.

Matched control (rule 3): a random homophonic key of the SAME SHAPE -- the same 40 codes from key.tsv,
each retaining its own global n_occurrences (so the control's codes are exactly as skewed/frequent as
the real ones) -- applied to the appendix's own plaintexts (the real, already-known letters at each of
the 391 aligned, abbreviation-free positions) instead of to a fictitious substitute text. Construction:
(1) shuffle the code<->letter assignment by permuting key.tsv's 'value' column across the 40 codes, so
each letter keeps the same homophone GROUP SIZE it has in the real key, only which codes serve it is
randomised; (2) walk the 391 real (code, true_letter) pairs in order and, for each one, draw a
SYNTHETIC code from the shuffled group for that true_letter, weighted by the drawn code's own real
n_occurrences (so a code that was globally frequent in the real key stays frequent in the synthetic
cipher, approximating 'the same code-frequency profile' in aggregate rather than position-by-position).
The synthetic pairs then carry the SAME true letters (the real plaintext, unchanged) and the SAME entry
membership/span sizes as the real data -- only the code drawn to represent each letter is randomised.
Fixed seed for reproducibility (printed below); one run, not cherry-picked.
"""

SEED = 20260925
random.seed(SEED)

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
ACCENT_MAP = {'ã':'a','á':'a','à':'a','â':'a','é':'e','ê':'e','í':'i','ó':'o','ô':'o','õ':'o','ú':'u','ç':'c'}
def base(c):
    return ACCENT_MAP.get(c.lower(), c.lower())

pairs = json.load(open(f'{ROOT}/scripts/_pairs.json'))
pairs = [(tok, base(let), tuple(key), span) for tok, let, key, span in pairs]

entries = sorted(set(key for _, _, key, _ in pairs))

def loo(pairs_list, label):
    by_entry = defaultdict(list)
    for tok, let, key, span in pairs_list:
        by_entry[key].append((tok, let))
    rows = []
    pooled_compared = pooled_correct = pooled_unkeyed = pooled_total = 0
    for e in entries:
        held = by_entry[e]
        rest = [(tok, let) for tok, let, key, span in pairs_list if key != e]
        tally = defaultdict(Counter)
        for tok, let in rest:
            tally[tok][let] += 1
        compared = correct = unkeyed = 0
        for tok, let in held:
            if tok in tally:
                pred = tally[tok].most_common(1)[0][0]
                compared += 1
                if pred == let:
                    correct += 1
            else:
                unkeyed += 1
        total = len(held)
        pct = (100.0 * correct / compared) if compared else float('nan')
        rows.append((e, total, compared, correct, pct, unkeyed, 100.0 * unkeyed / total if total else 0.0))
        pooled_compared += compared; pooled_correct += correct; pooled_unkeyed += unkeyed; pooled_total += total
    pooled_pct = 100.0 * pooled_correct / pooled_compared if pooled_compared else float('nan')
    pooled_unkeyed_share = 100.0 * pooled_unkeyed / pooled_total if pooled_total else float('nan')
    print(f"=== {label} ===")
    print(f"{'entry':28s} {'n':>4s} {'cmp':>4s} {'ok':>4s} {'pct':>7s} {'unkeyed':>8s} {'unk%':>6s}")
    for e, total, compared, correct, pct, unkeyed, unk_pct in rows:
        pct_s = f"{pct:.1f}" if compared else "n/a"
        print(f"{e[0]+'/'+e[1]:28s} {total:4d} {compared:4d} {correct:4d} {pct_s:>7s} {unkeyed:8d} {unk_pct:5.1f}%")
    print(f"POOLED: compared={pooled_compared} correct={pooled_correct} agreement={pooled_pct:.1f}%  "
          f"unkeyed={pooled_unkeyed}/{pooled_total} ({pooled_unkeyed_share:.1f}%)")
    print()
    return pooled_pct, pooled_unkeyed_share, rows

real_pct, real_unkeyed_pct, real_rows = loo(pairs, "REAL target (appendix aligned pairs)")

# ---- matched synthetic control ----
key_header, key_rows = None, []
with open(f'{ROOT}/key.tsv') as f:
    r = csv.reader(f, delimiter='\t')
    key_header = next(r)
    for row in r:
        key_rows.append(row)
codes = [row[0] for row in key_rows]
real_values = [base(row[1]) for row in key_rows]
n_occ = {row[0]: int(row[2]) for row in key_rows}

shuffled_values = real_values[:]
random.shuffle(shuffled_values)
synthetic_key = dict(zip(codes, shuffled_values))  # code -> synthetic letter

group = defaultdict(list)  # letter -> [codes assigned to it under synthetic_key]
for c, v in synthetic_key.items():
    group[v].append(c)

def weighted_choice(cands):
    weights = [n_occ.get(c, 1) for c in cands]
    return random.choices(cands, weights=weights, k=1)[0]

synthetic_pairs = []
missing_letter_group = 0
for tok, let, key, span in pairs:
    cands = group.get(let)
    if not cands:
        # the real letter has no code assigned to it at all under the shuffle (can happen if no
        # code's real value was ever 'let'); fall back to a uniformly random code from the whole pool
        # rather than silently dropping the pair -- flagged so this rare edge case is visible.
        missing_letter_group += 1
        cands = codes
    synth_tok = weighted_choice(cands)
    synthetic_pairs.append((synth_tok, let, key, span))

print(f"(seed={SEED}; {missing_letter_group} of {len(pairs)} real pairs had no synthetic-key code for "
      f"their true letter and fell back to a uniform draw over all 40 codes)")
print()
synth_pct, synth_unkeyed_pct, synth_rows = loo(synthetic_pairs, "MATCHED SYNTHETIC CONTROL (shuffled key, same code-frequency profile, real plaintext)")

gap = real_pct - synth_pct
print(f"=== Gate ===")
print(f"real pooled agreement:      {real_pct:.1f}%  (unkeyed share {real_unkeyed_pct:.1f}%)")
print(f"synthetic pooled agreement: {synth_pct:.1f}%  (unkeyed share {synth_unkeyed_pct:.1f}%)")
print(f"gap (real - synthetic): {gap:+.1f} points")
gate_pass = real_pct >= 80.0 and abs(gap) <= 10.0
print(f"gate (>=80% AND within 10 points of synthetic): {'PASS' if gate_pass else 'FAIL'}")

if not gate_pass:
    print()
    print("=== Entries dragging the gap (real pct - synthetic pct, most negative first) ===")
    real_by_e = {e: (pct, compared) for e, total, compared, correct, pct, unkeyed, unk_pct in real_rows}
    synth_by_e = {e: (pct, compared) for e, total, compared, correct, pct, unkeyed, unk_pct in synth_rows}
    diffs = []
    for e in entries:
        rp, rc = real_by_e[e]
        sp, sc = synth_by_e[e]
        if rc == 0:
            continue
        diffs.append((rp - sp, e, rp, sp, rc))
    diffs.sort()
    for d, e, rp, sp, rc in diffs:
        print(f"{e[0]+'/'+e[1]:28s} real={rp:6.1f}%  synth={sp:6.1f}%  gap={d:+7.1f}  (n compared={rc})")
