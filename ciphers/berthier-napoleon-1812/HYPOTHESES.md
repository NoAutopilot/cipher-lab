# berthier-napoleon-1812 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

## Crib-fit control pool rebuilt (GF4b, 2 Oct 2026)

`scripts/crib_test.py` (Y9/BBER, unchanged) re-run on a rebuilt pool. The v1 pool (`scripts/letters_v1_mixedpool.json`,
34 letters) was cut from Chuquet 1912 djvu lines 7100-9600, which start mid-way through note 45 "Berthier a Napoleon"
and run into note 46 "Murat a Napoleon" (line 8917): Murat's Roman keys overwrote Berthier's, so v1's **II, III, IV, VI,
VII, VIII, IX, X, XI are Murat's letters** (nine, not the two GF4 flagged), and Berthier's I-XI were missing. The v2 pool
(`scripts/letters.json`, 38 letters, each with a `source` field: Chuquet 1912 3e serie note 45, archive.org
`1812laguerrederu03chuquoft_djvu.txt` line N) is note 45 only, I-XXXVIII, with OCR-damaged markers III ("1I[", line 6583)
and XXII ("XXll", line 7935) mapped, a stray page-header "V" (line 7123) skipped, and the two Lefebvre-to-Berthier
letters inside the note dropped. Rank of each candidate among the pool (lower = better; three metrics
length/rate/gap), both pools side by side:

| candidate | v1 mixed pool (N=34, median 17.5) | v2 Berthier-only (N=38, median 19.5) |
|---|---|---|
| XIX (22 Dec) | 15 / 3 / 18 -- beats median 2 of 3 | 14 / 3 / 17 -- beats median 3 of 3 |
| XXIII (22 Dec, 9 pm) | 18 / 29 / 30 -- 0 of 3 | 17 / 29 / 33 -- 1 of 3 |
| XXIX (28 Dec, best length) | 1 / 12 / 17 -- 3 of 3 | 1 / 11 / 16 -- 3 of 3 |

Reading: the rebuild moves no candidate by more than 3 places; XIX and XXIII each gain one "beats median" only by sitting
just under the larger pool's median (17 vs 19.5; 17 vs 19.5), not by a better fit. These are ranking statistics on word
counts and repeat structure, not an alignment: no candidate is a crib, nothing is graded (rule 4), and the Y9/BBER
"no fit" reading of XIX/XXIII stands. (Y9's prose said XIX beat the median on rate_fit only; on v1's own numbers it also
beat it on length_fit, 15 < 17.5 -- corrected here.)

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 27 Sept 2026 07:27 | homophonic | N=325 K=207 restarts=8 corpus=memoiresdemonsie01torc.txt.gz+memoiresdemonsie02torc.txt.gz+mmoiresduducde01invill.txt.gz+mmoiresduducde02vill.txt.gz+mmoiresetlettre01margoog.txt.gz+lagazettedefran01unkngoog.txt.gz | 1-3 | 0.061 (0.058-0.062) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | BER-HOMO 27 Sept 2026: rule-3 control-then-target homophonic run, N=325 K=207 (spec's own N/K; spec's own ciphertext field is a pointer string, not data -- overridden with structure/flat.txt per BER-KWIC's settled 325-token reading) |

## Napoleon-Davout Nov 1813 grand chiffre: value-overlap test (GF4c, 3 Oct 2026)

Source: Bazeries 1896 pp.38-45 as reproduced verbatim on Bouchaudy's jfbouch.fr (`sources/jfbouch/2026-10-03/`), key
class `published` (cipher plus Bazeries' translation; no key table printed by Bouchaudy or Bazeries, so nothing is H).
Script `davout1813/value_overlap_test.py` (`--check` passes). Statistic: value-frequency overlap S between a test text
and Davout letter 1 (N=297). Shuffled-key control: letter 1's values relabelled by a random permutation of 1-1200,
20,000 draws, seed 1812. Positive control: Davout letters 2+3 (same code) subsampled to the target's N=325.

| text | N | S observed | shuffled-key null mean | p |
|---|---|---|---|---|
| positive control, Davout L2+L3 (5 subsamples) | 325 | 207-229 | 80.3-80.5 | 0.00005 each |
| positive control, Davout L2+L3 | 150 | 115 | 37.2 | 0.00005 |
| **target, Berthier 22 Dec 1812** | 325 | **118** | 79.7 | 0.040 |
| target vs all three Davout letters | 325 | 238 | 181.6 | 0.050 |

Reading: the method has power at the target's N (same-code text runs 2.6-2.8x its null; the target runs 1.5x). The
target's small excess comes from two values only: 173 (Davout's commonest group, 12x in letter 1, 2x on the Berthier
page) contributes 24 and 13 (the Berthier page's commonest, 8x; 2x in Davout) 16; without them S = 78 against a null of
about 80. A shared code would put Davout's commonest group among the page's commonest too. So the page is **not** in the
Nov 1813 Napoleon-Davout code (control-backed negative for this one key; it was in service from 23 Aug 1813 per
Bouchaudy, so a negative was expected). This says nothing about GC34 (Berthier-Davout, May 1813, Bazeries 1896
pp.19-36), which Bouchaudy's page does not reproduce: LOCAL-QUEUE L38 stays the route for that.
