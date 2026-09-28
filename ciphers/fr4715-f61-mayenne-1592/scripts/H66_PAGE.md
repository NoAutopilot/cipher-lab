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
   H100/H102 against 20 one-swap neighbour maps, the known lines 7.0 vs 5.5 and f.108v 5.0 vs 4.5, the runner-up on
   f.108v being the 4TRI c/p <-> 4PI d/q swap, which the 4-gram score (H103) even prefers by a hair: f.108v resolves
   every cell pair but c/p against d/q (Tomokiyo's own confusable pair), so the c/p and d/q letters of the consensus are
   its least supported. H105 (16:07): that swap changes only 6 of f.108v's 274 positions (the leaf has no 4PI), so the
   near tie is a null that could hardly differ -- a non-test of c/p versus d/q, which rests instead on H72 and H69; every
   swap with 11 or more changed positions loses clearly. H106: the four resolutions disagree most on e/r and a/n choices
   (row L05 no worse than others). H107: a pre-registered prediction of f.108r rows L04-L06 failed its gate (rank 4) on
   an uncorrected pass; it stays committed for scoring against the ASKS 88 gloss; H108 gives it a fair input. Before H85: f.108r/f.108v
   gloss readings wait on a person (ASKS rows 88/89; desk packs in `images/person_pack/` and
   `images/person_pack_108v/`). The model routes on that hand's gloss FAILed (H34, H35, H57).

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
