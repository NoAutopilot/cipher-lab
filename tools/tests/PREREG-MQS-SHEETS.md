# PREREG-MQS-SHEETS (A1, MQS-SHEETS worker, account 4; written 9 Oct 2026 03:04 UTC by date -u, before any control below was run)

Pre-registered before the control runs: colour gate (unit 1), regression tests (unit 4), the box-to-token map test KM
(unit 4), and the programmatic part of K3 that A2 uses on rendered sheets. A2 appends its K3 results block at the end.

## G1. Colour gate threshold (tools/cvd_check.py)
- **The CIEDE2000 gate of 20 between every pair of mark colours, in normal vision and in each of protan, deutan and tritan
  (Machado et al. 2009, severity 1.0), is a declared design threshold, not a sourced one.** No published CVD-palette
  minimum was cited; the 9 Oct 2026 pass that chose the palettes also chose the 20, so sorter_light's worst pair (20.7,
  protan, blue vs grey) passes by 0.7. PASS at >= 20; WARN (exit 2, "judgement call: under the declared gate by < 2") for
  18 <= worst < 20; FAIL (exit 1) below 18 or on any contrast failure (marks 3:1, text 4.5:1, text on a tint 4.5:1).
- Expected (the 9 Oct pass's own computation, tolerances in tools/tests/test_cvd_check.py): legacy ok/bad FAILS (deutan 11.3,
  protan 8.7, +-0.5); first proposed set FAILS (orange vs yellow deutan 11.6 +-0.5; #E69F00 on white 2.25 +-0.02); light ink on
  yellow 1.07 FAILS; sorter_light 20.7, sheets_light 22.7, dark 25.5 PASS (+-0.5). Not a statistical control: a deterministic
  colour computation, so no null; the "must not block" cases are the three palettes.

## G2. Regression tests R-K1 and R-K2 (named as regression tests, not known-answer controls)
They can fail only through a code bug: the value row is loaded through decode_key's own functions and compared with decode_key's
own output, and R-K1's tile coordinates are compared with the map they were cut from.
- R-K1: every tile on Birago no.87 is cut at the box atlas/no87_box_token.tsv assigns (gate 100%) and the value row equals
  decode_key's no.87 reading (gate 100%).
- R-K2: Gramont f.29r's value row equals reading_tokens.tsv (gate 100%); a key with two values swapped changes the value row at
  exactly those two codes' tokens (gate: exact set equality).

## G3. KM, the box-to-token map test (the open risk; BIR-ADJ / BIR87-ALIGN "tile-to-position mapping")
- Statistic: top-1 agreement between glyph_atlas.py classify --holdout (held-out lines kept out of the vote) of the tile this
  tool cuts at each 1:1 box of the held-out lines (f.178v L13-L23 and f.179r L01-L03; 'split' not 'tune'), and the token's own
  sign label in the map's row. Own-label and neighbour-label counts are reported beside it. The 26 2:1 and 8 1:2 rows are
  counted apart and never in the gate.
- Expected: about 0.61 (TX-ATLAS-B72's one earlier measurement, 0.609: 225 own-label, 77 neighbour-label; that figure is from
  tune-and-split tokens, the held-out figure may differ).
- **Gate: agreement >= 0.55 AND above the p95 of the null.** Null: permute box ids within each line (20 draws, re-cutting each
  tile each time): the image moves with the permutation and the sign label does not. Why this null can fail differently from
  the target: the statistic compares an image to a label; the permutation moves the image to another position's label, so a
  correct map scores the unpermuted value and a map that is wrong by position scores at the permuted level; a statistic
  computed from labels alone (the sign-vs-truth check, 0.896 in BIR87-ALIGN) is invariant under it and is not used.
- If the gate is missed: box mode ships shelf grade weak for Birago; every Birago sheet carries "tile placement unverified";
  the number goes in the report as the answer to BIR-ADJ's open suggestion; nothing is run on a target from it.
- Near-ceiling check: the null is not a solved control (permuted agreement is expected near the label base rate); the real
  agreement cannot be near ceiling because the earlier measurement was 0.609.

## G4. K3, the tile check on a rendered sheet (used by A2; pre-registered here as A2's brief requires)
- Programmatic, every tile: crop non-empty (at least 8 x 8 px); ink share (fraction of pixels darker than the crop's Otsu
  threshold) within [0.02, 0.65] -- below 0.02 is a blank/ghost crop, above 0.65 is a dark smear; where the tile has a sign
  label and the key gives that label a value, the label/value pair agrees with the token's value row (counts of tiles failing
  each test reported separately).
- Eye check: at most 60 tiles on one grid, each cell the tile beside its code's key-sheet exemplar, one vision call; tiles
  unusable or misplaced by eye counted.
- **A sheet with more than 10% unusable or misplaced tiles in either count (programmatic or eye; RUN3-MOR's line, 11 of 102 =
  10.8%) is labelled "not fit to show" in the README and is not offered.**
- Never send a whole-sheet screenshot to a vision call (Usage 6).

## A1 results (MQS-SHEETS worker, account 4; run 9 Oct 2026 03:15 UTC by date -u, after the pre-registration above was pushed in de825230c)
- G1 colour gate: every expected number met (tools/tests/test_cvd_check.py passes; de2000 agrees with skimage.color.deltaE_ciede2000 on 20 random pairs, max difference 0.0028, and with the Sharma, Wu and Dalal 2005 published pairs to 1e-3; scikit-image was pip-installed in this container for the run, the test skips it where absent). sorter_light 20.7 (protan, #0072B2 vs #767676, margin +0.7), sheets_light 22.7, dark 25.5; legacy ok/bad deutan 11.2 protan 8.6; orange/yellow deutan 11.5. The 20 stays a declared design threshold.
- G2 regression tests (they can fail only through a code bug): R-K1 714/714 1:1 tiles cut at the box the map assigns, value row equal to decode_key's f.178v reading (667 tokens); R-K2 Gramont f.29r value row equals reading_tokens.tsv 568/568, and swapping the values of codes x and 9 changes exactly those codes' 44 tokens. Both 100%.
- G3 KM (tools/tests/km_birago_map.py, same code path as `test_decipher_sheet.py --km`): held-out 1:1 tokens 381; classify top-1 = own sign label 231 (0.606, expected about 0.61); neighbour label (not own) 75; null (box ids permuted within line, 20 draws) mean 0.066, p95 0.085, max 0.094; apart and not in the gate: 2:1 13, 1:2 4, no box 4. Gate >= 0.55 and above p95: **PASS**. Box mode is not downgraded for Birago. What it does not show: it tests the box ids against the sign labels the same map carries via classify's reading of each box, so a map wrong by one position fails and a map right passes, but a map right for the wrong reason (labels agreeing across homophones) is not excluded; image-level correctness of the cut itself is R-K1's job (the crop equals the box). It answers BIR-ADJ's open suggestion ("tile-to-position mapping") at about 0 extra cost: 0.606 held-out, close to TX-ATLAS-B72's 0.609, no sign of a systematic mis-mapping.
- G4 K3 programmatic counts: no real sheet rendered by A1 beyond the tests (A2 renders and appends below). The label/value agreement count flags a token whose graded value differs from the key's value for its code (an exceptions.tsv correction, e.g. 9 of 659 tiles on Birago f.178v); it is reported, not a failure.
