# RESEARCH -- fr16104-vivonne-spain-1572 (flagship, program B)

Living map of the Saint-Gouard 1572-74 cipher pool. First written 17 Oct 2026 by VIV-SYNTH (account-4 worker; brief
`.claude/briefs/runs/2026-10-17-acct4-research-director-1.md`) from NOTES.md (4,363 lines), HYPOTHESES.md, 38 PREREG-*.md, AUDIT.md
(AUDITs 1-7), BENCHMARK-TX.tsv and TRANSCRIPTION.md. No experiment run, no reading changed, no key edited. One new disk-only
re-scoring of existing outputs (section 4.1, `tx/viv_synth_errsplit.py`, report only). Update this file at every worker report;
do not let it fall behind NOTES.md. Rule 10: nothing here is a novelty claim; status stays `partial`.

## 1. Question

**What is unread.** All of these letters use one key: Tomokiyo's published key for Apr 1572-Nov 1574 (sources/cryptiana/web/henryiii.htm;
key.tsv plus VIV-ANCHOR's V -> n at grade C and VIV-KEY's e -> m, now grade M). Every other cipher letter in fr.16104/16105 that we have
looked at has a clerk's "dechiffre de la precedente" beside it (N5-VIVTAB; the decipherments 41, 44, 51, 58, 68, 71, 76 and the heads of
56, 60, 62, 78, 83, 89, 91, 97 and 101 were all viewed).

| piece | date, addressee | leaves | cipher tokens on disk | grades (H / M / U) | depth | what is missing |
|---|---|---|---|---|---|---|
| fr.16105 ink 63 (Gachard LXIII, "sans le dechiffrement") | 10 Oct 1573, King | ff.190r-194r, about 300 cipher lines | 15,762 (whole piece) | 12,290 / 2,530 / 942 (78.0% H) | D1 (AUDIT 7) | no period decipherment anywhere in fr.16105 c95-c248; longest all-H run 40 is salad; f.191r best clean run 37 before the owner packet, 24 after |
| fr.16104 ink 52 (not in Gachard) | 5 Sept 1572, Queen | ff.164r-168v, about 290 lines | 2,727 (f.164r-v only) | 2,217 / 411 / 99 (81.3%) | D1 | ff.165r-168v not transcribed (8 pages, est. USD 34) |
| fr.16104 ink 53 | 5 Sept 1572, duc d'Anjou | ff.170r-171v | 4,380 | 3,744 / 456 / 180 (85.5%) | D1 | 82 split tiles and 133 kept gaps unsettled; f/m/p cells |
| fr.16104 ink 54 | 7 Sept 1572, King | f.173r-v | 1,954 | 1,491 / 279 / 184 (76.3%) | D1 | "qae" for "que" (u after q not settled); 275 look-alike questions |
| fr.16104 ink 38 | 16 July 1572 | -- | -- | -- | -- | its twin was deciphered: not an open text |
| not known | -- | fr.16104 c1-c169, c192-c324; fr.16105 c1-c94, c113-c191 | -- | -- | -- | not viewed (N5-VIVTAB); fr.16106 strays not checked |

**What a reading needs.** Rule 4a D2: at least one clause that clears the authentication distance (AD) with every liberty counted,
plus one true, specific sentence about the content. No piece has one. The decision rule used in every Vivonne PREREG is ">= 42
letters all-H". That figure is a floor, not the bar (section 4.4). The question the flagship has to answer first is whether the
pipeline can produce such a clause from this hand at all. Only after that is it a question about the key.

## 2. Hypotheses in play

| # | hypothesis | for | against / open | status |
|---|---|---|---|---|
| K1 | Ink 63 is in the same key family as 40/41 and 67/70 (Tomokiyo 1572-74) | ink 40 held-out under Tomokiyo, no training: PASS (N5-VIVK); ink 67 f.201r 0.744 vs shuffled p95 0.507, f.201v 0.714 vs 0.498, ink 70 f.211r 0.769 vs 0.522, f.211v 0.792 vs 0.502, rank 1 of 201 each time (VIV-67/67B/70B/70C2); ink 63 itself: b2 -1.548 vs p99 -1.836, wrong-key specificity 0.288 vs p99 0.064 (N7-VIV63G) | the letter-to-letter checks (b2, wrong-key) cannot tell a variant row from the published one | **strongly supported**; not the bottleneck |
| K2 | Key rows for the unkeyed or merged labels (f, m, p, u-after-q, c, o, 2, y) can be fixed from clerk anchors | VIV-ANCHOR control 5/7 PASS, V -> n 7/8 at grade C; c -> p recurs on three leaves (8 + 14 + 3 aligned) | f is a SPLIT across labels g 16, p 7, o 6, y 6 (VIV-FKEY); e -> m downgraded to M because label e merges three signs (VIV-KEYV, AUDIT 7); m, p, qu each under 3 decided positions | **open**, limited by the labels rather than the anchors |
| K3 | Label d carries clerk s in some cells (a homophone or a cell we read wrongly) | s<-d is the top confusion on f.201r (x11), f.211r (x16-17) and f.103r, in every output including the committed one | no per-label gate run; could be truth-side | **untested**; cheap (disk) |
| T1 | The reader-label alphabet merges signs: labels e, c, o, p, y, g, z, s each hold 2-3 written signs | VIV-KEYV shape look (e = 3 signs); VIV-ESPLIT (y = an l-group and an h-group, held out); VIV-GSPLIT3C (g holds f: F1 0.789 vs null p99 0.400); the owner made 18 "new sign" calls in 13 new piles (VIVPACKET3); owner's R14 note: label piles "mix shapes that I can clearly see" | splitting by machine is untestable at the truth leaves' N for e (15 items); the y split on ink 63 does no better than random (rank 119 of 201) | **supported**; it is the leading explanation of the error floor |
| T2 | The g/f split recovers plaintext f on ink 63 | GSPLIT3C PASS (recall 0.833, precision 0.750) | at precision 0.750 an override is a liberty; on f.191r it cut the strict run 37 -> 24 (GSPLIT3E) | **consumed**: six f.191r positions go to the owner as questions |
| T3 | The s1/s2 crop overlap makes readers write strings twice | 40 blocks / 205 tokens on ink 63 fit rule DEDUP (VIV-LOOKALIKE) | known-answer check vacuous (0 removals on the truth leaves) | **untested** (G1 non-test); next is f.102v pass A, 22 blocks |
| T4 | Steep, uneven line slope causes segmentation loss | `iiif_lines.py --deskew-region` built and clean on f.191r (VIV-F191) | not applied to f.194r L5-10; no known-answer measure of deskew's effect | **untested** |
| T5 | A person reads this hand where machine readers fail | VIV-HUMAN2 W 6/7, R 1/1 on piles built from certain-answer tiles; attempt 1 W 5/12 was undecided, and its four "wrong" answers were a defect of the page's exemplars | VIVPACKET3 on reader-label piles: negative on the run gate | **supported at n 8**; the step-1 sort is published and waiting on the owner |
| L1 | French in the clerk's 1573 spelling, so the fr16 judge applies | decodes PASS b2 on every piece | the fr16 judge FAILs the known-good f.103r control at this noise (N5-VIV54, N6-VIV53), so a judge verdict on these decodes means nothing | **language supported, judge uncalibrated** |
| A1 | AD of about 42 letters (French simple-substitution unicity of about 28, times 1.5) is the D2 bar | AUDITs 1-3, 7 | DV-MERCY2 (espagnol142-mercy-1648 AUDIT, 15 Oct 2026): the corpus R governs, R 3.4 is only a sensitivity figure, and every liberty is charged in H(K). For a homophonic key of about 32 signs the governing AD is much higher (Mercy: 125.9 letters at es17c) | **untested for this item**; 42 understates the bar |

## 3. Ruled out, with the number

**Retired** (no rerun without a different instrument or new material):
- Key rebuild from a flat start (`tools/stream_align.py`, Arm A): converged on 2 of 30 codes. A published key exists anyway.
- Lattice decode with a confusion matrix learnt on this hand (VIV-LAT): dev PASS (fx lines 14/3), confirm2 FAIL (0.296 vs 0.291).
  Only 0.124 of the top-1 errors have the true sign anywhere in the lattice. Logged as untested by this tool at this error. A matrix
  learnt on one set of readers does not transfer to another.
- Pen-unit tile kNN classifier (VIV-CLS): top-1 err on f.201r 0.313 vs pass A 0.154. The truth is in the top-3 for 0.359 of pass A's
  errors (gate 0.50), and only 0.46 of the page is covered. FAIL.
- Whole-label key-cell n-gram rank for f/m/p (D1-F16104K): negative. Hand-placed shape judges (D07-VIV53 control 4-5/12 vs 8/12;
  N7-VIV54R; DEF1-VIV54 0/18): NON-TEST.
- Label-e supervised split (VIV-ESPLIT): untestable (15 items, no class >= 8). y split applied to ink 63: rank 119 of 201 against
  random picks.
- **f.191r re-reads by the same reader family.** Rule 3's third-attempt clause, shape (b), now applies. Four passes (VIV-F191, F191B)
  took the longest all-H run 32 -> 37. A fifth pass E (F191C) and a 5-vote rule (F191D) left it at 37 (V_strict 21 -> 21). The
  reader-label owner packet (VIVPACKET3) gave 37 -> 24, and the g-split override (GSPLIT3E) also gave 37 -> 24. More passes or more
  reconciliation rules by the same Sonnet readers on the same leaf will not change this result; the method is the limit, not the
  setting.

**Consumed** (the last attempt passed or was informative; the yield is banked):
- The g-split family (VIV-GSPLIT, 2, 3, 3B, 3C, 3D, 3E). It yielded six f.191r owner questions (Parent reading, 15 Oct 2026).
- Known-plaintext sibling pairs 40/41, 67/68 and 70/71. They yielded the key-family proof (K1), the label-count tables and eight
  BENCHMARK-TX items. Unread rest: f.202r/f.207r and f.212r/ff.216r-216v.
- Print and premise: Gachard I-II, d'Ars (book and RQH article), Catherine IV-V/X, Groen IV and Kervyn I-VI. Neither cites the
  10 Oct 1573 cipher text. Ribera 2007 has been seen only as snippets (note 139 not seen).

**Not a test yet** (logged non-tests, which are not negatives): the DEDUP rule (T3); the judge on these decodes (L1); every "no stretch
>= 42" verdict on ink 63, for the reason in 4.1.

## 4. Shared assumptions every experiment rested on

### 4.1 Transcription error. Tested: it is too high for any ink-63 negative to count
Standard: true per-sign error <= 0.05 (TRANSCRIPTION.md row 1). Measured on the known leaves (tx_bench, pass A, as measured): f.102r-dev2
0.194, f.103r-confirm2 0.232, f.201r-dev 0.185 (the three items in PREREG-SORTER-STEP1-INK63 s.3). The five later leaves give 0.138-0.211
(f.211r 0.138, f.202r 0.163, f.211v 0.164, f.201r-dev-3 0.179, f.201v-dev-3 0.211). Pass B is 0.02-0.04 worse on each.

Is that error in the readers or in the truth? VIV-SYNTH re-scored the committed outputs, treating one flag class at a time as flagged
(`tx/viv_synth_errsplit.py`, report only, run 17 Oct 2026):

| item | pass A as measured | excluding only clerk-doubt rows (truth doubtful) | excluding only align-conflict rows |
|---|---|---|---|
| f102r-dev2 | 0.194 | 0.159 | 0.005 (circular) |
| f103r-confirm2 (verifier-classed flags, TXV-VIV) | 0.232 | 0.225 | **0.139** |
| f201r-dev | 0.185 | 0.160 | 0.033 (circular) |
| f201r-dev-3 | 0.179 | 0.174 | 0.042 (circular) |
| f201v-dev-3 | 0.211 | 0.210 | 0.025 (circular) |
| f202r-dev | 0.163 | 0.140 | 0.013 (circular) |
| f211r-dev | 0.138 | 0.125 | 0.006 (circular) |
| f211v-dev | 0.164 | 0.152 | 0.038 (circular) |

Reading the table:
- Doubt about the clerk's text explains only 0.00-0.035 of the error.
- The rest sits at "align-conflict" positions, where the reference sign decodes to a letter other than the clerk's. Excluding those
  rows is circular on the dev items: their reference is the reconciled reading, which scores 0.000 there by construction.
- The only item where a verifier classed those positions (confirm2, TXV-VIV 9 Oct 2026) keeps **0.139** after the doubtful classes are
  removed.
- Best estimate: true reader error on this hand is about 0.14 on clean truth, and 0.14-0.23 as measured. That is three to four times
  the standard.
- The tool shelf's "flagged-excluded" figures for these items (0.003-0.048) must not be quoted as reader error.

Ink 63 was read by the same kind of reader (two blind Sonnet passes per page, reconciled; N6-VIV63/63B/63C). Its own two readers
disagree on 0.297 of f.193r's signs (VIV-LOOKALIKE), which is worse than the known leaves. Nothing yet shows that its reader error is
lower than 0.14.

**ERR-SIM result (17 Oct 2026, PREREG-ERR-SIM, NOTES "ERR-SIM").** The zero-error synthetic control reaches only a 54-letter all-H
run, against the recounted AD of 94.6 (58.9 at R 3.4). The cap is the key, not the reader. p, f, k, x and y have no code, and b, h, m
and z decode only from M rows, so no reader error level can surface a clause at or above AD. Giving p and m H codes lifts the ceiling to
143. The reader-error crossover cannot be measured until the key has those cells. What follows still holds for every negative on file.

**Can an ink-63 negative be read as a negative?** No. The bar was never calibrated at this error: no synthetic text of ink 63's length,
enciphered with this key, read with this hand's measured confusions and decoded the same way, has ever been run to show that a clause
>= AD *would* surface. Rule 3 (SALV-DIAG) requires the injected error to bracket the target's own measured error before a FAIL counts.
That bracketing has not been done here. These rest on the uncalibrated bar:
- every "no stretch >= 42" decision: VIV-F191, F191B, F191D, VIVPACKET3, GSPLIT3E;
- the D1 depth calls on 63/52/53/54 (correct as a description, but no evidence that D2 is out of reach);
- every gate scored on decoded letters at this noise: VIV-KEY's non-discriminating b2/wrong-key, and the fr16 judge FAIL on f.103r.

**What would falsify "the pipeline cannot read this hand below 10%"** (none of these has been tried):
1. A reader that writes Tomokiyo key cells straight from a sheet of certain-answer exemplars, instead of a free label alphabet that
   merges signs (T1). This is the cheapest different instrument; experiment 2.
2. The measured-exception reader tier. Since 16 Oct, sign transcription runs on the strongest model (CLAUDE.md Usage 1: clair349,
   Sonnet 39-42% vs 70.7% agreement). Every Vivonne pass on file is a Sonnet pass.
3. A different segmentation: whole-line strips or per-token windows instead of pen-unit tiles. VIV-CLS covered only 0.46 of the
   page because the clerk joins signs.
4. The owner's settled alphabet (step-1 sort, PREREG-SORTER-STEP1-INK63 s.3). This is one instrument, and it waits on the owner.
5. A key-constrained decode with a lattice that actually contains the true sign. VIV-LAT's ceiling of 0.124 says the readers' second
   choices are wrong, not that the lattice idea is.

### 4.2 Key family. Tested; holds (K1)
The open parts are cells, not the family: f, m, p, qu, c, o, 2, y, and label d vs clerk s (K2, K3). Cell questions cannot be settled
while the labels merge signs (VIV-KEYV's postmortem): anchors that all fall in one word family need a shape check of the label's
other occurrences first.

### 4.3 Language and judge. Partly tested
French is supported by b2 order tests on every piece. The fr16 judge cannot gate at this noise: it FAILs a known-good control.
Its fold spread (1.5-71.5%, MQS-LANGS) makes any French score of unknown reliability. No era-matched corpus has been built for 1570s
diplomatic French; the clerk decipherments 41, 44, 51, 58, 68, 71 and 76 are period text from this very office, a ready source
(rule 3's pt18 lesson).

### 4.4 AD convention. Untested for this item
AUDITs 1-3 and 7 use an AD of "about 42" (simple-substitution unicity of 28 times 1.5) and note it is "higher for this homophonic key".
DV-MERCY2 (espagnol142-mercy-1648 AUDIT, Depth re-rule 2, 15 Oct 2026) ruled the convention: AD = 1.5 x H(K)/R with R from the corpus
(`tools/depth_stats.py`). R 3.4 is reported only as a sensitivity figure, and every M/U liberty is charged in H(K). There, that put the
bar at 125.9 letters (es17c), not 84 (R 3.4). For Vivonne, `depth_stats.py` has never been run. With about 32 cipher-class codes and
corpus R near 2, the governing AD is likely around 100 letters, more than twice the 42 every PREREG used. Because nothing reached 42,
no verdict was too generous. But the target is further away than the lane has been working towards, and experiment 1 needs the
right bar. **Recounted 17 Oct 2026 (ERR-SIM):** fr16 R 2.116, H_design 133.4 bits. AD for an all-H clause = 94.6 letters; R 3.4
sensitivity 58.9. The tool's item-wide figure, 4,671.6, charges every M/U token of the item to one clause and cannot be reached on any
item of this size.

### 4.5 Smaller assumptions
- Line crops: s1/s2 halves overlapping by 400 px. T3 asks whether that makes readers write strings twice; the check so far was vacuous.
- Deskew is not applied on f.194r (T4).
- The frozen truth builders `--check` as stale. Only the status column changed (0 truth rows differ).

## 5. The three most informative next experiments (ranked by expected information per USD)

**Experiment 1 RUN 17 Oct 2026, outcome: non-test by its own control (C0 run 54 < AD 94.6). The cap is the key (p and m cells), so the
ranking changes. New first experiment: the p and m key cells (K-cells: anchor p, m and f on the clerk-decipherment pairs of inks 40/41
and 67/68, the way VIV-ANCHOR found V = n; disk only, about USD 2-3). Then rerun ERR-SIM on the extended key (seconds). Experiment 2
(KEYCELL-READ) stays useful, but its yardstick waits on that rerun. Experiment 3 is unchanged.**

**1. ERR-SIM: an error-matched synthetic control for ink 63, with the AD recounted (disk only; cap USD 2.5; box 45 min).** [RUN, see above]
- Assumption tested: 4.1 and 4.4. Would a clause >= AD surface from a text like ink 63 at this hand's measured error?
- Method:
  - Recount the AD: `tools/depth_stats.py` on reading_piece63.tsv with fr16 (and a 1573 clerk-decipherment corpus if built), giving
    the governing AD and the R 3.4 sensitivity figure.
  - Plaintext: the merged clerk decipherments (dec of 41, 68, 71; same office and year), cut to 15,762 letters.
  - Encipher with key.tsv, using homophones at ink 63's own per-code frequencies.
  - Simulate two readers from pass A/pass B confusion matrices learnt on the known leaves
    (`tools/key_decode_lattice.py learn-confusion`), scaled to injected error 0.05 / 0.10 / 0.14 / 0.19 / 0.23 (brackets the measured
    0.14-0.23), 5 seeds each.
  - Reconcile as committed (disagreement -> M), decode, measure the longest all-H run, V_strict and the depth_stats runs.
- Controls: the same pipeline at 0.0 error (the ceiling; must give a run >= AD) and with a value-shuffled key (must give none). Both
  can differ from the target on the run statistic.
- Stop: one sweep; PREREG with a Decision block before any run; no target file touched.
- Outcomes:
  - (a) No run >= AD appears at 0.14 or above in most seeds. Every ink-63 negative is a non-test; the crossover error becomes the
    transcription target; decode-side work on ink 63 stops until a known leaf reads below it.
  - (b) Runs >= AD do appear at 0.14-0.23. Ink 63's failure is informative; pivot to the key-structure hypotheses (nomenclator or
    code groups beside the letter key, nulls, a variant table for Oct 1573).
- Price: nearest rows are VIV-LAT and VIV-ESPLIT, disk jobs priced about USD 2-4.
- Does not depend on the owner. A different instrument (simulation, not classification).

**2. KEYCELL-READ: a key-cell reader on two known leaves (cap USD 8; box 75 min; openapi.bnf.fr <= 4 requests).**
- Assumption tested: T1 and 4.1's falsifier 1+2. Is the error floor caused by the free label alphabet and the reader tier?
- Method:
  - Build an exemplar sheet: one row per Tomokiyo key cell, 2-4 certain-answer tiles per cell from `tx/sorter_step1/pool.tsv`
    (628 tiles, 24 codes), plus the key image for cells with no tile.
  - One blind pass per leaf by the strongest model, writing cell ids, never letters or free labels.
  - Leaves: f.211r L02-L11 (398 scored) and f.201r (dev-3, 924), with crops cut as a pasted command.
  - Vision calls: 2 leaves x 1 pass x about USD 2.5, plus 1 control x USD 2.5 = 7.5.
- Score: tx_bench, as measured and with clerk-doubt rows excluded (`tx/viv_synth_errsplit.py` modes), against pass A (0.138 / 0.179).
- Control: the same reader on f.211r with the sheet's cell labels permuted. It must do worse; it can, because the labels drive the
  output.
- Gate (written before the run): as-measured err <= 0.10 on both leaves and >= 0.05 below pass A on each.
- Stop: FAIL on both means "model readers at their floor on this hand under both alphabets"; log untested-by-this-tool; the next
  instrument is non-model (the owner's sort, or atlas segmentation).
- Outcomes: PASS means re-read f.191r with this reader (about USD 4), take the ERR-SIM crossover as the yardstick, then decide on
  ink 52 ff.165r-168v (USD 34) and the rest of ink 63.
- Price: per-pass rates from the README common tail and AX-COMP2 (USD 1.46 per Sonnet page-pass), scaled for the strongest model.
- Does not depend on the owner. A different instrument from the g-split/classifier family (a reader with a closed key-cell alphabet).

**3. SORT-CONSUME: the owner's step-1 alphabet, consumed as registered (agent USD 1; owner about 20 minutes; waits on him).**
- Assumption tested: T1/T5. Does a person's settled inventory lower err_true on the known leaves?
- Method and controls are fixed in PREREG-SORTER-STEP1-INK63 s.3:
  - leave-one-leaf-out kNN relabel of pass A;
  - gate: no item rises and >= 2 of 0.194 / 0.232 / 0.185 fall;
  - controls: the seed piles unchanged, and 20 shuffled pile memberships, which must not pass.
- Stop: as registered. Price: SORTER-PILES-ANSWERED and VIV-HUMAN parent scoring rows, under USD 1.
- Outcomes:
  - PASS: the settled piles seed PREREG-VIVPACKET4 (one-shape piles, the six g-split questions) and the exemplar sheet of
    experiment 2, which gets cleaner.
  - FAIL with controls valid: the person's eye helps on disputed tiles (T5), not as an inventory for kNN relabelling.
- Ranked third, not first: the cash price is the lowest, but the expected gain is small (only unanimous k = 3 neighbours relabel a
  token) and it waits on the owner.

Not in the top three, named so they are not lost: K3 (label d vs clerk s, disk-only per-label anchor gate on the 67/70 streams,
about USD 2); the fr16 corpus built from the clerk decipherments (L1, about USD 2); Ribera 2007 note 139 by interlibrary loan
(acquisition, owner minutes); the ink 50/51 known-plaintext pair for f/m/p/qu anchors (USD 15; worth it only after experiment 2,
because the anchors are limited by the labels).

## 6. Recommendation

**Pivot**: stop decode-side and re-read work on ink 63 until the input is trusted.
- The last ten jobs on f.191r re-read the same leaf with the same reader family, moved the decisive number only 32 -> 37 -> 24, and
  were judged against a bar (42) that is below the governing AD.
- The known leaves say the readers err at about 0.14 on clean truth, nearly three times the standard.
- No synthetic control has ever shown that a clause would surface at that error, so not one ink-63 negative has yet been a test.

Order:
- Run ERR-SIM first (USD 2.5). It decides whether the question is transcription or key.
- If transcription: run KEYCELL-READ (USD 8). Hold the USD 34 ink-52 transcription and any further f.191r pass until a reader beats
  the crossover on a known leaf.
- Keep SORT-CONSUME armed for when the owner's piles land.
- Pursue Ribera 2007 in parallel as program-A acquisition. A Spanish-side copy or decipherment would be a key source, and every
  counted reading so far came from one.

Counterfactual: continuing as before means packet 4 on reader-label piles, more g-split variants and more f.191r passes. On the
record that costs about USD 20-40 and, by the 37 -> 24 history, most likely leaves the run under 42 and every negative still a
non-test. Rule 3's third-attempt clause already bars that path for the same instrument.

### 6a. Recommendation revised after ERR-SIM (17 Oct 2026, 02:2x UTC; account-4 parent)
The pivot above was half right. Reader error is high (s.4.1) but it is not the binding limit: the zero-error control reads 54 letters on
key.tsv against an AD of 94.6, so no transcription of any quality can surface a clause while p, m and f have no code. **Order now:**
(1) VIV-KCELLS (running): p/m/f cells by whole-stream alignment on the deciphered pairs, known-answer control on the 14 keyed letters;
(2) rerun err_sim on the extended key for the reader-error crossover, which is the number KEYCELL-READ needs as its yardstick;
(3) only then KEYCELL-READ, scoped to the signs the alignment names. KEYCELL-READ at USD 8 is held, not briefed. If (1) finds the p/m
positions scattered across labels, that confirms T1 for those letters and the reader brief gets the exact tiles. Counterfactual: the
reader experiment first would have cost USD 8 to measure a floor that, on this key, cannot reach the bar at any error.

### 6b. After VIV-KCELLS (17 Oct 2026, 03:2x UTC; account-4 parent)
Known-answer control PASS (12/14). p sits under unkeyed label c (share 0.62, purity 0.75), m under unkeyed label 2 (0.61, 0.69): merged
labels (T1), not absent signs. Next: VIV-KCELLS2, the crossword test on ink 63 (c=p, 2=m as trial cells vs a value-shuffled control) and
the ERR-SIM crossover on the extended key; then split labels c and 2 at the exact tiles (tile reader, or the owner's targeted sort of
about 100 tiles). KEYCELL-READ on whole leaves stays held.
