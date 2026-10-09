# PREREG-VB0086 -- does inv.1537 scan 0086 (Van Beuningen to De Witt, 10 Dec 1656) share the 1657 key?

Written 9 Oct 2026 by VB-0086 (LANE FAMILY-A2h, account 2) before any score is computed, pushed in its own commit.
Known-text work: the letter is printed in clear in Brieven aan Johan de Witt I (1919) pp.365-366 (print_0086.txt); it is
used only as a key source. key.tsv is frozen at the commit that carries this file (no edit to key.tsv in this job).

## Inputs
- `ciphertext_0086.tsv`: reconciled transcription of the leaf's main lines L01-L21 (crops images/crops_0086/, cut with
  tools/iiif_lines.py from the native right page), items in order, kind C (a colon-closed digit run) or W (a written word),
  from two blind Sonnet passes (A, B) per half page; disagreements settled from the crop image in one reconciliation step.
  A C item whose digits are still disputed after reconciliation is flagged M and excluded from the statistic (reported).
- `print_0086.txt`: the printed text from the opening to "Ende hebbe ik niettemin".
- `key.tsv` as committed (numeric codes only; rows graded `clear` are not codes).

## Pairing (key-free; key.tsv is not read by this step)
`align_0086.py --pairs` aligns the item sequence to the printed word sequence by dynamic programming:
- W item <-> print word: cost from normalised edit similarity (anchors);
- C item of k codes, every code <= 2 digits <-> one print word: cost |k - len(normalised word)| (0 = exact);
- C item that is a single 3-digit code <-> a run of 1-4 print words (nomenclator name), fixed cost;
- a C item of 2+ codes may also pair with a run of 2 print words written together (fixed extra cost);
- skips on either side at a fixed penalty (the copy and the print need not agree word for word).
Output `pairs_0086.tsv` is written before `--score` runs.

## Normalisation
lowercase, letters only; "ij" -> "y"; j -> i; v -> u. key.tsv values normalised the same way.

## Statistic S (pre-registered)
Scored tokens: every code token of a non-M C item whose code is in key.tsv and which is in one of two classes:
(a) letter class: the C item has only <= 2-digit codes and k equals the normalised letter count of its paired print
    word (or word run); code i is compared with letter i; agreement = key value == letter;
(b) name class: a single 3-digit code paired with a word run; agreement = edit similarity between the normalised
    key value and the normalised run >= 0.75.
S = agreements / scored tokens (both classes pooled); also reported per class.

## Control and gate
Null: 1,000 permutations (seed 0) of key.tsv's values among its numeric codes (letter and name values pooled, as
key.tsv holds them); S recomputed on the same scored positions. This control can differ from the target: it changes the
values, and S measures value agreement. Gate: S_real > p99 of the null. PASS = the 1656 letter 0086 reads with the
1657 key at these positions; FAIL = not shown at this N.

## Reported beside the gate (not gated)
- codes on 0086 absent from key.tsv, with their paired print letter or word (grade C from print) ->
  `key_1656_candidates.tsv` (never written into key.tsv);
- key.tsv codes graded M (single context) whose 0086 occurrences agree: count of codes gaining a second context;
- per-code disagreements (code, key value, print letter) listed in full;
- the interlinear gloss, read blind in both passes, compared with the print (agreement share), not used in S.
