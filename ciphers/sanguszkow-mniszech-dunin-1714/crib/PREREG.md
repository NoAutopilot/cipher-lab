# PREREG RUN3-SANG: crib-drag homophonic, control first (4 Oct 2026, 09:1x UTC, committed before any run)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run3-wave2.md` RUN3-SANG (LANE-RUN3, account 1). Hypothesis H3: R7524 is a
homophonic letter cipher whose two exact sign repeats are plaintext repeats: R6 = 22.118.82.36.31.81 (x3) and
R2 = 15.20 (x8). Nothing below is run before this file is committed.

## Instrument (one shared option, not a private copy)
`tools/family_run.py SPEC --family homophonic --param crib=drag ...` (new option in `tools/families/homophonic.py`).
The SAME procedure runs on control and target:
1. In the cipher, R6 = the most frequent sign 6-gram with count >= 3; R2 = the most frequent sign bigram (count >= 3)
   whose signs are not in R6. (Target: R6 = 22 118 82 36 31 81, R2 = 15 20.)
2. Candidates: the top `m6` (200) most frequent 6-letter substrings and top `m2` (40) bigrams of the solver's own
   training corpus (folded, word spaces removed), filtered only by sign identity (a repeated sign = same letter).
3. Stage 1: each R6 candidate pinned (`fixed=`), one short anneal (`drag_iters` 8000, trigram + unigram KL, as the
   homophonic family); keep the best `keep` (5) by final score. Stage 2: each kept R6 x each R2 candidate, one short
   anneal; the best-scoring pair wins. Final: full anneal (iters 40000, `--restarts`) with the winning pair pinned.
4. Clear anchors: used only for the language/corpus choice (pl18); no anchor-derived crib (none is adjacent to a
   repeat in a way that fixes letters without a guess).

## Control (matched on N, K, design, language AND crib count/kind)
N=232, K=77, `profile=target` (target's own sign-count profile), corpus pl18 (held-out window, as family_run.py).
`crib=drag` also makes the control carry the target's crib kind: the window is drawn (up to 2000 tries) until it holds a
6-letter string occurring >= 3 times and a bigram >= 8 times; after enciphering, every occurrence of that 6-gram is
given the first occurrence's signs and 8 occurrences of the bigram (outside the 6-gram) the first's signs -- so the
control carries one 6-sign repeat x3 and one 2-sign repeat x8, as the target does. Seeds 1-3.

## Statistic and gate (pre-registered)
- Control: token recovery over all 232 positions (family_run.py score_recovery), mean over seeds 1-3. **Gate 0.6**
  (family_run.py default; blind homophonic control at this N read 0.076, H2). Also reported, not gated: crib pair
  correct (R6 and R2 letters both right) per seed, and recovery on unpinned positions only.
- Target: run only if the gate is met. Judge pl18 (`tools/judge_plaintext.py`; fold spread 11-80.5% FN, unknown
  reliability, A3V3-SANGP), plus one `--shuffle-target 1` run of the same procedure; a target best score not above the
  shuffled target's is no reading. Grades: S only if control passed; M otherwise.
- If CONTROL BELOW GATE: logged as a non-test of crib-drag at N=232 (not a negative); target not run.

## Orthogonality (rule 3)
The control's statistic is token recovery against the known plaintext; the crib-drag can pick a wrong 6-gram/bigram
(the plaintext is not in the candidate list's top or a wrong candidate scores higher), and a wrong pin drags the
anneal away, so recovery can fall to the blind 0.0-0.16 band: the control can fail, and differently from a pass. The
shuffled-target run destroys the target's repeats (order statistic), and the drag's score depends on order, so that
null can differ from the target.

## Box
Per unit: one control seed ~(200 + 200 short anneals + 1 full) -- timed on seed 1 before the battery; stop before a
unit that crosses 80% of cap (USD 7) or box (90 min, to 10:35 UTC).
