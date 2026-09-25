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

PX-BRODEC3 (25 Sept 2026): the clean synthetic control above (a shuffled key, no other noise) reads
96.7% -- as PX-BRODEC2 itself flagged, and the lane orchestrator confirmed ("the synthetic had no
transcription noise or abbreviations, so it was not design-matched", CLAUDE.md rule 3: match the design,
not only the length/symbol count). This adds a NOISE-MATCHED synthetic mode on top of the same shuffled
key, injecting the two noise sources actually measured on this target:

(a) Token substitution at the transcription M rate. `ciphertext_appendix.tsv`'s own `grade` column
    (PX-BROGLYPH) grades 114 of 1702 tokens M (not crop-confirmed) -- 6.7%. With that per-token
    probability, a synthetic pair's drawn code is replaced by one drawn from the observed confusion
    pairs in `disagreements.tsv` (183 `replace`-kind (a_token, b_token) rows from the pass-A/pass-B
    disagreement, kept with their natural duplication so a frequently-confused shape is drawn more
    often) -- the other member of a randomly-drawn confusion pair, or, if that pair's two tokens are
    the same as the code being corrupted, the pair's first element regardless.
(b) The gloss-side mismatch rate: of the appendix's 38 entries, only 7 have every one of their code
    tokens land in a resolved pair (`code_count == pairs_count`); 19 contribute zero pairs and 12
    contribute some but not all -- 31/38 = 81.6% of entries lose at least one span to a code-count/
    gloss-letter-count mismatch (abbreviation or paraphrase inside the coded span, PX-BROKEY2/
    PX-BROKEY's own diagnosis). The clean control above already inherits this exactly, because its
    391 synthetic pairs are drawn 1:1 from the SAME 391 real pairs `03_align_pairs.py` resolved from
    those same 19 entries -- the entries and spans this run drops are, by construction, the identical
    ones the real alignment dropped, not a resampled or invented set. Reported here as a number (not
    a second, independent random cut) precisely because "exactly as the real run drops them" rules out
    resampling it.

Five seeds (not one, since (a)'s noise draw and the shuffle/weighted-draw are now both stochastic);
mean and range reported, none cherry-picked.
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

# ---- measured noise inputs (PX-BRODEC3) ----
tok_grades = [row['grade'] for row in csv.DictReader(open(f'{ROOT}/ciphertext_appendix.tsv'), delimiter='\t')]
m_rate = tok_grades.count('M') / len(tok_grades)
print(f"measured transcription M rate: {tok_grades.count('M')}/{len(tok_grades)} = {100*m_rate:.1f}%")

disagreement_rows = list(csv.DictReader(open(f'{ROOT}/disagreements.tsv'), delimiter='\t'))
confusion_pairs = [(r['a_token'], r['b_token']) for r in disagreement_rows if r['kind'] == 'replace']
print(f"confusion pairs from disagreements.tsv (kind=replace): {len(confusion_pairs)}")

code_count_by_entry = defaultdict(int)
for tr in csv.DictReader(open(f'{ROOT}/ciphertext_appendix.tsv'), delimiter='\t'):
    code_count_by_entry[(tr['leaf'], tr['entry_label'])] += 1
pair_count_by_entry = Counter(tuple(key) for _, _, key, _ in pairs)
n_clean = sum(1 for e in code_count_by_entry if pair_count_by_entry.get(e, 0) == code_count_by_entry[e])
gloss_mismatch_rate = 1.0 - n_clean / len(code_count_by_entry)
print(f"gloss-side mismatch rate: {len(code_count_by_entry) - n_clean}/{len(code_count_by_entry)} entries "
      f"lose >=1 span to a code-count/gloss-letter-count mismatch = {100*gloss_mismatch_rate:.1f}% "
      f"(already reflected in the 391 real/synthetic pairs above -- same entries/spans the real run drops,"
      f" not resampled)")
print()

# ---- matched synthetic control: shuffled key (clean), then noise-matched, 5 seeds ----
key_header, key_rows = None, []
with open(f'{ROOT}/key.tsv') as f:
    r = csv.reader(f, delimiter='\t')
    key_header = next(r)
    for row in r:
        key_rows.append(row)
codes = [row[0] for row in key_rows]
real_values = [base(row[1]) for row in key_rows]
n_occ = {row[0]: int(row[2]) for row in key_rows}

def weighted_choice(cands, weights_map):
    weights = [weights_map.get(c, 1) for c in cands]
    return random.choices(cands, weights=weights, k=1)[0]

def build_shuffled_key():
    shuffled_values = real_values[:]
    random.shuffle(shuffled_values)
    synthetic_key = dict(zip(codes, shuffled_values))
    group = defaultdict(list)
    for c, v in synthetic_key.items():
        group[v].append(c)
    return group

def draw_synthetic_pairs(group, inject_noise):
    """One shuffled-key draw over the 391 real (code, true_letter, entry, span) pairs. When
    inject_noise, each drawn code is independently replaced (probability m_rate) by one member of a
    randomly-drawn observed confusion pair -- the same per-token M rate and the same confusion pairs
    measured on the real transcription, not a fresh assumption."""
    out = []
    missing = 0
    for tok, let, key, span in pairs:
        cands = group.get(let)
        if not cands:
            missing += 1
            cands = codes
        synth_tok = weighted_choice(cands, n_occ)
        if inject_noise and random.random() < m_rate:
            a, b = confusion_pairs[random.randrange(len(confusion_pairs))]
            synth_tok = b if a == synth_tok else a
        out.append((synth_tok, let, key, span))
    return out, missing

random.seed(SEED)
clean_group = build_shuffled_key()
clean_pairs, missing_letter_group = draw_synthetic_pairs(clean_group, inject_noise=False)
print(f"(seed={SEED}; {missing_letter_group} of {len(pairs)} real pairs had no synthetic-key code for "
      f"their true letter and fell back to a uniform draw over all 40 codes)")
print()
synth_pct, synth_unkeyed_pct, synth_rows = loo(clean_pairs, "CLEAN SYNTHETIC CONTROL (shuffled key only, no noise -- PX-BRODEC2's original control, kept for comparison)")

SEEDS = [20260925, 20260926, 20260927, 20260928, 20260929]
noisy_results = []
for s in SEEDS:
    random.seed(s)
    group = build_shuffled_key()
    noisy_pairs, _ = draw_synthetic_pairs(group, inject_noise=True)
    pct, unkeyed_pct, rows = loo(noisy_pairs, f"NOISE-MATCHED SYNTHETIC CONTROL (shuffled key + {100*m_rate:.1f}% confusion-pair substitution, seed={s})")
    noisy_results.append((s, pct, unkeyed_pct, rows))

noisy_pcts = [pct for s, pct, u, rows in noisy_results]
noisy_mean = sum(noisy_pcts) / len(noisy_pcts)
noisy_min, noisy_max = min(noisy_pcts), max(noisy_pcts)

gap_clean = real_pct - synth_pct
gap_noisy = real_pct - noisy_mean
print(f"=== Gate (PX-BRODEC3: noise-matched synthetic replaces the clean one) ===")
print(f"real pooled agreement:            {real_pct:.1f}%  (unkeyed share {real_unkeyed_pct:.1f}%)")
print(f"clean synthetic (for reference):  {synth_pct:.1f}%  (gap {gap_clean:+.1f})")
print(f"noise-matched synthetic, 5 seeds: mean={noisy_mean:.1f}%  range=[{noisy_min:.1f}, {noisy_max:.1f}]  "
      f"(per-seed: {', '.join(f'{s}:{p:.1f}%' for s, p, u, r in noisy_results)})")
print(f"gap (real - noise-matched mean): {gap_noisy:+.1f} points")
gate_pass = real_pct >= 80.0 and abs(gap_noisy) <= 10.0
print(f"gate (real >=80% AND within 10 points of noise-matched synthetic mean): {'PASS' if gate_pass else 'FAIL'}")

if not gate_pass:
    print()
    print("=== Entries dragging the gap vs. the LAST noise-matched seed (real pct - synth pct, most negative first) ===")
    last_rows = noisy_results[-1][3]
    real_by_e = {e: (pct, compared) for e, total, compared, correct, pct, unkeyed, unk_pct in real_rows}
    synth_by_e = {e: (pct, compared) for e, total, compared, correct, pct, unkeyed, unk_pct in last_rows}
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
