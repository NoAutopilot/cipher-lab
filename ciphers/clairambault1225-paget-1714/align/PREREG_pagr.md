# Pre-registration: per-token rulings on the A3V3-PAGA findings (A3V3-PAGR, 4 Oct 2026, written 06:4x UTC)

Written and committed before `align/pin_pagr.py` is run on any target token. Disk only (align/pairs.tsv, reading_tokens.tsv,
key.tsv, exceptions.tsv at commit 4b518e74: H 50 S 79 M 363 I 7 U 6). Brief: `.claude/briefs/runs/2026-10-04-acct3-a3v3-wave2.md`
section A3V3-PAGR. Findings under test (AUDIT.md, A3V3-PAGA section R2):

| # | proposal | tokens ruled |
|---|---|---|
| 1 | 77 = ce (key q, M) and 20 = qui (key ui, M) | every token of 77 (3) and of 20 |
| 2 | 84 = cette (key ce, M) | every token of 84 (4) |
| 3 | 34 = e (key de, M) | every token of 34 |
| 4 | 38 = i (key a, M) | every token of 38 |
| 5 | 158 = mo at f66L:48 back to H (key mo, M; f66L:143 already S) | f66L:48 |
| 6 | gloss transcription P23 "ne" -> "nee" (leaf "née", PAGA R2 finding 5) | applied in build_pairs.py before the run (a gloss read, not a ruling) |
| 7 | f66L:189 20 vs leaf 220 | already applied: exceptions.tsv row "image reads 220, ciphertext.tsv 20 (image override: NEXT-PAG, A2-PAG2)" and pairs.tsv P28 override 189:20->220; nothing to rule |

## Why a mechanical instrument
settle7.py's S rule needs the token's own per-letter Gibbs chunk to equal the value. For 77 and 84 Gibbs gives no single value
(ceq/p/quoi; cet/ette/ette/ato), for 34 and 38 neither aligner holds one; PAGA's readings are by eye. An eye reading alone is not
a grade S (rule 4: S needs a control). So each proposal is ruled per token by a deterministic constraint check whose own
known-answer accuracy and shuffled-value null are measured first.

## Instrument: firm-neighbour pin (`align/pin_pagr.py`)
Per pair: the gloss letters exactly as tools/gibbs_align.prepare folds them (ia.plain_letters, ia.fold, y -> i); the pair's code
tokens in order (clear tokens carry no letters, as in gibbs_align). FIRM = tokens graded H, C or S in reading_tokens.tsv at
4b518e74, each emitting exactly its current value folded the same way. Every other code token emits 0-5 letters (5 so that
"cette" is reachable). Gloss letters not covered by a token are allowed only before the first and after the last code token
(the gloss overhang PAGA describes); none inside. A token's candidate set = the chunks it takes over all complete alignments.
**pinned(t) = the candidate set has exactly one member.** A pair with no complete alignment pins nothing.
When a token is ruled, it is itself removed from FIRM (never pins itself).

## Step 1: known-answer check (gate; target not ruled if it fails)
Hide each FIRM token (H/C/S) in turn (only that one removed from FIRM) and compute its candidate set. Coverage = share pinned;
accuracy = share of pinned whose single chunk equals its current value. **Gate: accuracy >= 0.90 on >= 20 pinned tokens.**

## Step 2: shuffled-value null (gate)
200 seeds: the code -> value map of the FIRM tokens is permuted across codes (seed s, random.Random(s); a code keeps one value at
all its firm tokens; grades and positions unchanged), then the target statistic is recomputed: T = number of proposal tokens
(rows 1-5) pinned to their proposed value. It can differ from the real T: which gloss letters are left in a gap depends on the
neighbours' values, which is exactly what the permutation changes. **Gate: real T > shuffle p95.** Known-answer accuracy under
the shuffle is reported too.

## Ruling (only if both gates pass)
- Proposal token pinned to the proposed value: **S** (exceptions.tsv row, value = proposal, reason citing pin_pagr_rulings.tsv);
  row 5 (158 at f66L:48, value unchanged mo, code held at 2 occurrences) pinned to mo: **H** (the gloss chunk located over this
  very token, decode.json's H definition).
- Pinned to another value, or not pinned, or infeasible pair: **M**, value unchanged (no exception row; logged in the rulings).
- key.tsv: a code's value changes to the proposal only when >= 2 of its tokens pin to it and none pins to another value; the row
  keeps grade M with an "unsettled per token" note (settle7 convention: only the ruled tokens are firm). Otherwise key.tsv is
  unchanged and only the pinned tokens move (exceptions).
- Then `tools/decode_key.py ciphers/clairambault1225-paget-1714 --check` exit 0, settle7.py --check, per-grade counts before/after.
- Fail of either gate: every proposal stays M, findings logged as "untested by this instrument", numbers side by side in NOTES.md.

No further tuning: max chunk 5 and the overhang rule are fixed here and not changed after the first run.
