# BIR87-ALIGN pre-registration (4 Oct 2026, 16:1x UTC, account-3 worker; pushed before any alignment run)

Brief `.claude/briefs/runs/2026-10-04-acct3-bir87-align.md`. Disk only, no LM in steps 1-2.

## Inputs (step 1, `relabel.py`, already run; counts in `relabel_counts.json`)
- no.87 = harvest/ciphertext_f178r/f178v/f179r.tsv (853 tokens). Primary sequence `cipher_owner/`: 205 tokens relabelled to
  the owner pile (186 kept + 18 moved + 1 not-letter, sorter tiles whose atlas box maps 1:1 to a token); 648 keep the committed
  atlas/line-read label (31 sorter tiles have no token, 9 map 2:1/1:2, 3 bad-cut: all keep the committed label).
  "kept" = the owner reviewed the page and left the tile in its seeded pile (sorter README: a computer seed the owner did not move).
  Sensitivity sequence `cipher_moved/`: only the 18 moved + 1 not-letter tiles relabelled (reported, never decisive).
- 4 Oct sort labels: settled_labels.tsv + corrections.tsv (7 applied, latest row per tile wins; f144r_L04.1_07 ends in T60-e)
  -> `settled_corrected.tsv`.

## Alignment (step 2)
Instrument exactly as NEVBIR-87ALIGN: `tools/interlinear_align.py align` with `--floor 5000 --digits 4 --keep-fs --word-prior
--prior harvest/align87/prior.tsv` (printed table, T42 = g, first EM iteration only), pairs from `harvest/align87/build_pairs.py
--cipher-dir <seq>`. Each owner pile is ONE code (2000+k; 7000+k if its family is a word sign, e.g. T89-b), unseeded, so its
value comes from the clerk sheet alone. Null: the same with the sheet's words permuted within each span, seeds 1-20.
Also run once on the committed labels (should reproduce 0.896 / max 0.376).

Gate for the whole run: real 'agrees' share > max over the 20 shuffled runs (else no pile value is reported as C).

Per owner pile: n = aligned occurrences (key.tsv n), C value = majority meaning, agree, share = agree/n.
- grade C: n >= 2, agree >= 2, share >= 0.6, AND share above the pile's own shuffled null (real share > max share over the 20
  shuffled runs for the same pile code, ties = not above).
- n < 2: "no evidence" (never guessed). Otherwise M (value listed, not usable).
Split families (piles sharing a family: T60 vs T60-d/-c/-e, T19 vs T19-b/-c/-d/X_NEW-l(T19 members), T85 vs T85-b, T86, T83-b, T24
vs T24-b, T89 vs T89-b): REAL homophone split only if parent and sub-pile both grade C with different letters; same letter at C
on both = over-split (merge recommended, not applied); anything else = no evidence. X_NEW-l is compared with the T19 parent.

## Re-decode (step 3, only if step 2 passes its gate and some pile gets C)
`harvest/ownersort/ownersort.py --new-piles-unknown` step-3 machinery (BIR-OWNER random-change control, 200 draws, seed
20261004, judge it16dip/fr16 per leaf spec as that script uses), with corrections applied and each C pile's value replacing the
key/'?' value for tiles in that pile (new options `--corrections`, `--pile-values`, outputs `v4_bir87/`). Report per leaf b vs a
(current reading) vs control p95, rank, and judge PASS/FAIL. Gate unchanged: PASS iff b > a and b > p95. Nothing applied.
