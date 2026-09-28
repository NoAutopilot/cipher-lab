# f.61r for the verifier (CAMPAIGN.md H66) -- the runner's page, 28 Sept 2026

Compiled by campaign runner session_01NQpd6L9ZvLvjU1L7ttFmZs (step H84) for LANE VO3. It collects paths and results
already recorded in NOTES.md; it adds no claim, no reading and no class. Nothing on f.61r is solved, new or first. The
verifier rules on H66 itself; the classing is the verifier's.

## What audit 1 asked for, and where it now stands

Audit 1 (AUDIT.md, 27 Sept 2026) held the L10 fragment and named three things that would move it:

1. **A pre-registered judge re-run with ties counted against the target.** H25 (NOTES.md "Campaign step H25"): known
   lines PASS 3/3 (prompt verbatim on disk, key withheld, rank 1 of 21 each); L10 FAIL 3/3 (target rank 3 / 7 / 4 of
   21). The judge reproduces as a gate; L10 does not pass it. The context route on the period-key skeleton also failed
   its own control (H33, H57). H82/H83 (28 Sept) were dropped because narrowing the period sets to their cells gives
   back the H25 map.
2. **Whether the "qo" (side-by-side loops) form is PHI or a class of its own, with a control.**
   - On f.61/f.108r, by our fit: H26 blind sort, 38/38, P < 0.0005 (SBS = b/o, trefoil = e/r).
   - By the period gloss of two other hands (f.101r, f.188r), blind tile sorts with the gloss cut away:
     H65 o under the side-by-side glyph 18/20, e under the trefoil 18/19 (36/39, P < 0.0005, p95 26);
     H67 b goes with o (b 11/14 vs e 3/13 in the SBS group, Fisher P 0.0056); H77 the f.101r readers' LOOPS-under-o
     is the same stemmed glyph (31/32); H89 a third hand, f.274: o 7/7 vs e 7/7 (exact P 0.0006). The s/t split of the
     V-with-bar (H15 on f.61) is period-attested in two hands (H70 f.101r, thin; H89 f.274, 13/13).
   - Controls for the method: two clean one-symbol cells FAIL as they should, H75 d/q (20/32, P 0.087) and H80 g/t
     (12/20, P 0.84).
   - All ten tests in one table: `scripts/f61_glyph_splits.tsv` (H81, `scripts/f61splits.py --check`).
3. **A pair-choice test beyond L10 (a second letter in this cipher).** H85 (28 Sept): the f.61-fitted cells on fr.3983
   f.108v (Mayenne to de Diou, Soissons, 4 March 1593, same secretary; reconciled draft H59, grade M; 274 pair
   positions) -- control on the known lines under the same 14 cells PASS (7.5 vs 1.0), then the target ranks 1 of 21
   in 3 of 3 blind calls (6.5 vs 0.5, 2.0 vs 1.5, 3.5 vs 2.0; thin on two); the three resolutions agree on 184/274
   letters (`scripts/f108v_consensus.txt`, H91). Calibration (H90): on the known lines the judge picks Tomokiyo's letter
   within the right pair at 43/47, but a permuted set still scores 16/20 (a letter-frequency prior) and the reused prompt
   example "beau-pere" is one of his words there. Tomokiyo lists f.108v among the letters in this cipher
   (`sources/cryptiana/web/mayenne.htm`), and the BnF finding aid catalogues fr.3983 f.108 as "chiffre et
   déchiffrement" (a sparse interlined gloss on f.108v), so its plaintext is at least partly known in period: the print
   search and the known-answer weighing are H88, yours. Checks since (28 Sept, 15:38-16:06): H93 a model-free fr16
   4-gram score puts the target resolution first against the same judge's 20 wrong-map resolutions in all three calls,
   though below real 16th-c. prose (a noisy grade-M text); H94 the judge rerun without the leaked example word, control
   6.0 vs 2.0 and f.108v 6.5 vs 1.0; H101 per row, rank 1 in 23 of 28 row-calls (rows L03, L04, L06, L07 in all four);
   H102/H110 against one-swap neighbour maps on the known lines, 7.0 vs 5.5 and 8.0 vs 6.5 (controls PASS); the f.108v
   one-swap calls H100 and H110 are VOID (the judge scripted its verdict from the sets file, found 16:5x) and H103, which
   scored H100, falls with them: the f.108v hard null is untested (H111). H105: the c/p <-> d/q swap changes only 6 of
   f.108v's 274 positions (no 4PI on the leaf), so f.108v cannot test that assignment in any case; it rests on H72 and
   H69. H106: the four resolutions disagree most on e/r and a/n choices
   (row L05 no worse than others). H107: a pre-registered prediction of f.108r rows L04-L06 failed its gate (rank 4) on
   an uncorrected pass; it stays committed for scoring against the ASKS 88 gloss; H108 gives it a fair input. Before H85: f.108r/f.108v
   gloss readings wait on a person (ASKS rows 88/89; desk packs in `images/person_pack/` and
   `images/person_pack_108v/`). The model routes on that hand's gloss FAILed (H34, H35, H57).

## H108-H134 (runner 5, 28 Sept 2026, 17:17-19:16 UTC) -- what changed for the verifier

- **f.108r L04-L06 input (H108).** L06 was cut in half by the H34 region; re-cut whole from a taller strip, two blind passes
  (34/40 agree), reconciled draft `f61recon108r_draft.tsv` (gate PASS, 1/85 flagged; 13/85 grade L). The loop-sign relabel
  instrument failed its control twice (H108 13/18, H113 18/26) and is retired for this question (rule 3).
- **Judge on f.108r (H112): FAIL both seeds** on the corrected input (all sets <= 2.0). **Valid f.108v one-swap null (H111):
  PASS thin**, 5.0 vs the powerless c/p-d/q swap 4.0, every swap with power <= 3.5 -- replaces the void H100.
- **The 4-gram beam, known-answer accuracy of its within-pair choices** (14-cell map): f.61 spans 38/49 = 0.776 (H116),
  f.108r overlay 69/76 = 0.908 (H121), period gloss of f.101r/f.188r 0.716 -> 0.753 with KEY.md equivalences (H130/H133, noisy
  automatic alignment). Under key v4's wide sets it is near chance (H117, 23/42). Margin grading: FAIL by one (H126, 85/95);
  the misses cluster on the a/n cell in span S3 (H131). Word rescoring changes nothing (H134).
- **Correction (H124): a plain permutation rank is not evidence on long texts** -- the fitted map ranks first on f.108v even
  with the signs shuffled (letter frequency). Use **sequence gain** instead (real order minus shuffled, `f61beam_seqgain.py`),
  null on shuffled text (H128, 1 of 25 in the top 10). By sequence gain the fitted map ranks 1 of 201 on the known lines,
  on f.108v (about twice the best permuted gain), thinly on f.108r with HASH4 = i/x (H127), and on the family leaves f.97r,
  f.101r, f.188r (rank 1; f.124r, f.106r, f.274 at the edge, H129). On the pooled family leaves 128 of 129 one-swaps lose
  (H132); the near-ties sit on classes the family passes merge (43 into 4TRI, mixed EBR_A).
- **HASH4 on f.108r:** i/x best of four values (H118), replicated rank 1 of 1001 (H119); d/q hurts (H114).
- **Committed predictions** for scoring when the glosses are read: f.108r L04-L06 by the judge (H107, H112) and the beam
  (`f61beam_f108r_prediction.txt`, H120); f.108v by the beam (`f61beam_f108v_prediction.txt`, H123).
- Nothing here reads f.61r: its text outside Tomokiyo's spans is 17 signs (H125 dropped); the beam is a grading aid at about
  three right in four, not a reading.

## H135-H152 (runner 5, 28 Sept 2026; section times in NOTES.md before H142 were typed, see its correction)

- **Word-lattice beam** (`f61beam_lattice.py`): known letters 111/125 (f.61 spans 44/49 = 0.898, f.108r overlay 67/76; gate 115
  FAIL, H136); against the period gloss of f.101r/f.188r 0.782 (gate 0.80 FAIL, H138). Under key v4's wide sets it is near
  chance (23/42, H141): the obstacle is v4's sets, not the instrument.
- **Key v4 vs the 14-cell map** (`f61v4_vs_14.tsv`, H145): v4 widens seven classes at frac 0.1; on the family pool the third
  letters are rejected for SBS, 4PI, HASH4 and open for 4TRI, 4STEM (H148); VBAR_A g/t over v4's t/s is a lean that did not
  replicate (29/30 then 41/50, H146/H151); VBAR_B s over f/s. Candidates for the family worker in `family/PROPOSAL_H146.md`;
  none changes f.61's map (H147: the refined map scores 110 vs 111 known letters).
- **Sequence-gain results bootstrapped**: f.108v in f.61's cells stands (rank 1 of 51 in 29/30 line resamples, H152); on the
  family pool 13 of the 15 closest one-swaps are within resampling noise (H142).
- **Rare classes** (CA, C6, LOOPBAR, CROSS, ELOOP, LL): under 10 occurrences each in all f.61-hand text on disk, untestable
  (H150). Only one Tomokiyo dash falls on a mapped sign (H139).
- **Key-hunt lead** (H143): BnF Français 2751 fol. 116, de Diou to Mayenne "escripte en chiffre" with its decipherment
  (Gallica btv1b52523734p f241-f242); images 403 from the cloud; `family/REQUEST_fr2751.md`, retry row H144.
- **Committed predictions**: lattice resolutions of f.108r L04-L06 and f.108v (`f61lattice_*_prediction.txt`, H140) beside
  H107/H112/H120/H123; `f61score_gloss108.py` scores all f.108r ones when the ASKS 88 gloss lands (H137).

## H153-H161 (runner 5, 28 Sept 2026, times read from the clock)

- **Bootstraps of the sequence-gain results:** f.108v in f.61's cells stands (29/30, H152); f.108r L04-L06 does not (5/30;
  20/30 with HASH4 = i/x -- a lean, H154); family leaves: f.97r and f.188r robust, f.101r and f.124r at the edge, the short
  f.106r and f.274 not robust (H158).
- **Sign values by sequence gain on f.108v (f.61's hand):** ZHOOK = i/x (Tomokiyo's published value) beats a/e, a/u, e/u and
  null 30/30 each (H157); HASH4 leans d/q over i/x (6/30) and is undecided -- the passes probably lump bare hash (i) and
  4-over-hash (d/q), H160. On the family pool ZHOOK occurs 5 times: untestable (H161).
- **f.108v rows:** L06, L04, L01, L03 fit f.61's cells alone (rank 1-7 of 201); L02, L05, L07 at chance, not explained by
  transcription grade or coverage (H155, H156). The ASKS 89 desk pack carries that reading order, no letters.

## Files to read

| what | path | step |
|---|---|---|
| f.61r skeleton, no letter chosen in any pair | `scripts/f61_skeleton.txt` (`f61skeleton.py --check`) | H58 |
| the same with each cell's support tagged (period tile sort / period key / published / our fit) | `scripts/f61_skeleton_attest.txt` (`f61attest.py --check`) | H76 |
| L10 fragment as revised (pos 6 and 11 as [b/o]) | `scripts/fragment_L10.tsv` (`f61fragment.py --check`) | H51 |
| glyph-split tests H65-H89 | `scripts/f61_glyph_splits.tsv`, tiles `images/h65`..`images/h80`, prompts `scripts/PROMPTS.md` | H81 |
| judge results | `scripts/f61judge_known_s10{1,2,3}_*`, `scripts/f61judge_unmarked_s10{1,2,3}_*` | H25 |
| published rare-class values (ZHOOK i/x) | `family/key_published_rare.tsv` | H44 |
| f.108v skeleton (same hand as f.61) | `scripts/f108v_skeleton.txt` | H62 |
| f.108v judge (control + three calls) and its consensus | `scripts/f61judge_known_h51_s101_*`, `scripts/f61judge_f108v_s10{1,2,3}_*`, `scripts/f108v_consensus.txt` (`f61judge108v.py score ... --check`, `f108v_consensus.py --check`) | H85, H91 |
| judge letter-choice calibration | `scripts/f61judgeletters_result.txt`, `f61judgeletters_known_h51_s104_result.txt` (`f61judgeletters.py [--tag known_h51_s104] --check`) | H90, H94 |
| model-free checks and hard null | `scripts/f61judge_ngram_result.txt`, `f61judge_ngram_hard_result.txt` (`f61judge_ngram.py [--hard] --check`), `scripts/f108v_lines.txt`, `scripts/f61judge_{known_h51,f108v}_swaps105_*`, no-leak `*_s104_*` | H93, H94, H100-H103 |
| coding merges found in the family readers' classes (for the family worker) | `scripts/family_relabel_proposal.tsv` | H99 |
| runner 5 (H108-H134): f.108r draft, beam and sequence-gain scripts | `f61recon108r.py`, `f61loop108r.py`, `f61hash4_108r.py`, `f61ngram108r_repl.py`, `f61beam_known.py`, `f61beam_margin*.py`, `f61beam_shuffle.py`, `f61beam_seqgain.py`, `f61seqgain_shuffle.py`, `f61seqgain_family.py`, `f61swap_family.py`, `f61beam_period.py`, `f61beam_words.py`, `f61beam_f108r_predict.py` (each `--check`) | H108-H134 |

## Counts the verifier can re-derive

- f.61r: 99 signs; 54 of Tomokiyo's letters on his five spans (his tentative reading, grade M as a reading), 15 pair
  positions with no letter chosen, 28 nulls, 2 unread (`f61_skeleton.txt` header).
- Cell support over the 69 lettered or paired positions (`f61_skeleton_attest.txt`): both letters period-attested by a
  blind tile sort 13; one letter 10; published 3; period key 39; one letter of the period key 2; our fit only 2.
- L10: 13 signs, 8 pairs, 5 nulls; cells: 2 period-attested by tile sort on both letters ([b/o] x2), 2 on one letter
  ([g/t] t, [f/s] s), 4 period key ([l/y], [e/r] x2, [h/u]). No letter within any pair is settled.

## Open questions only the verifier or a person can close

- Whether anything on f.61r beyond "held" is classable at letter level (audit 1: 0 H, 0 C, 0 S, 8 M on L10).
- H88: whether f.108v's plaintext is already in print or in the archive, and what H85's result is worth for this cipher.
- Which of ASKS 88 (f.108r rows 4-6) and 89 (f.108v) goes on the desk first.
- The table's two drawn a/n and e/r symbols are unmatched to any hand: H73 (a/n) and H71 (e/r) found no split in the
  period gloss (untestable by blind shape sort after H24b and H73).
