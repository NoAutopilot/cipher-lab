# PREREG-SUR-CTX (13 Oct 2026, 10:1x UTC by date -u; account 4, Opus worker for LANE DEFAULT-A4-0935)

Written and pushed before any score. Script: `ctx_2039_remarque.py` (committed with this file); only its `--dry` mode (vocabulary
size, segment and slot counts, the tested ids, the calibration classes; no anchor computed) has run.

## Question
Do the 2039 Remarque's own words (Nieuw key decode, `reading_2039_remarque_nieuw_tokens.tsv` as of ab48e49cb: Remarque lines
head, L1-L5; 255 letter slots in 7 segments) license a value for each unkeyed class K x4 (L3:7, L4:5, L4:35, L5:2), O x2 (head:0,
L3:48), & x2 (L3:60, L4:42), [J-rev] x2 (L2:11, L4:26)? SUR-2039R's sheet-tile call was a non-test (controls 13/20 < 14).

Disclosed before scoring: SUR-2039R logged by eye that K at L5:2 sits in "{8½} v?et" (voet wants o); this worker read the decoded
Remarque text (reading_2039_remarque_nieuw.txt) before writing this file. The rule below is mechanical and fixed now.

## Vocabulary (frozen rule, no word added or removed by hand)
`tools/data/nl18` (Dutch prose 1770-1799, colonial/official register; 3.4M letters): lowercased, accents stripped, ij -> y,
u -> v, j -> i (the Nieuw key writes y, v, i); words of 4-12 letters with corpus count >= 5 whose letters all lie in the key's
value alphabet {a b c d e f g h i k l n o p q r s t v w y z}: **7,439 words** (`--dry`). Words with m or x drop out (the key has no
m or x value); a French or technical word absent from nl18 cannot anchor. Not a gloss of this text: any licence is grade M.

## Statistic
Anchor: a vocabulary word of length L covering the tested slot, all L slots in one segment, every keyed slot agreeing (H/C and
single-valued M exact; g|l, k|i either letter), at most one other wildcard slot (other U signs, and in calibration the masked
class), keyed agreements >= max(3, L-2). The word's letter at the tested slot is that instance's candidate. Per class:
A(v) = tested instances with >= 1 anchor giving v; v* = argmax A. **Licence**: A(v*) = k (every tested instance), v* unique,
anchors from >= 2 distinct words, and both controls at p <= 0.0025 (0.01 Bonferroni over 4 classes).

## Controls (seed 20391013) and the rule-3 check
| control | permutes | can it differ from the target on A? |
|---|---|---|
| value-shuffle | the values of the Remarque's keyed single-valued sign classes, permuted among them | yes: every context letter can move |
| letter-shuffle | letters within each vocabulary word, lengths kept | yes: every word changes |
Null statistic per draw: max A with the same uniqueness and >= 2-word conditions (0 when not licensed); p = share of draws >= the
real A(v*). N = 1000 per control for targets (p <= 2/1000), N = 200 in calibration (p = 0/200 required).

## Power check at this N (run FIRST, `--calib`; targets scored only if it passes)
Known-answer classes: every H/C sign class with >= 2 instances in the Remarque (21 classes, `--dry`). For each, all its instances
are masked (wildcards), k = 2 (and k = 4 where it has >= 4) instances are drawn (seed 20391013), and the full licence procedure
runs. Gate, per k:
- wrong licences (licensed, v* != the class's key value) <= 1 and <= 5% of the trials at that k, AND
- correct licences >= 30% of the trials at that k.
k = 2 governs O, & and [J-rev]; k = 4 governs K. A k that fails: its classes are **non-test**, not scored, written as such.
Caveat stated now: the known-answer classes are frequent signs (e, r, t, n ...), easier to anchor than a rare letter, so a
passing power check is an upper bound on power for the targets.

## Decision rule
- Licensed class: each tested instance gets a per-token row in `exceptions_nieuw_image.tsv`, grade **M**; grade **S** only if
  the calibration at that k had 0 wrong licences and >= 80% correct AND the target's p = 0/1000 on both controls. No key-file
  change (`key_period_codes_nieuw.tsv` untouched); no class-wide value.
- Not licensed: nothing changes; per-instance candidates logged as observations in NOTES.md only.
- After any change `tools/decode_key.py ciphers/na-suriname-map-1781 --check` must pass.
