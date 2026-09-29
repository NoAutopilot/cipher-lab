# Group H log: the Copiale decipherment method, replicated and tested (DEB-SWARM-H)

29 Sept 2026, one session (claim 03:13 UTC). Times are this container's `date -u`, read at each step. Grade S
throughout; nothing on c1 or c2 is read. Status of the target is unchanged (`open`).

**Headline for the merge.** The Copiale method, automated (context clusters, a homophonic solve that finds the
word-space signs itself, language chosen by fit), recovers **79-94 pct of real Copiale letters blind at 770 and 1,200
tokens (10 of 10 windows, German ranked first of 12 languages every time)**. It fails at 135 tokens (c1's size),
it fails at 658 tokens (c2's size) in 2 of 3 windows even clean, and it **fails at every size once 8 pct or more of the
tokens are noise** (crossover between 3 and 8 pct at 1,200). The settled drafts carry 14-18 pct. So this method
cannot license a negative, or a reading, on c1 or c2 as transcribed: Phase 1 is not met at the target's noise, and no
key was scored on a real text.

| # | time (UTC) | method | parameters | control result | real-text held-out | why it failed / what it showed |
|---|---|---|---|---|---|---|
| 0 | 03:13-03:20 | sources | [K11] and [K06] read in full; data from HF learnable-typewriter (cipher) + leitro GitHub (plaintext) | gold = [K11] Fig. 6 key on the transcription agrees with the published plaintext at 0.990 letter similarity over 1,701 lines | -- | Wikipedia's "80 languages" and "EM" belong to [K06]; on the Copiale EM gave nonsense and the reading was done by hand (SOURCES.md) |
| 1 | 03:21 | annealer, add-k quadgrams | `hsolve_h.c`, spaces given | Copiale 1,200 oracle spaces: all one letter | not run | add-k smoothing gives unseen contexts a flat 1/27, so nonsense like "wwww" scores as well as German; replaced by recursive Dirichlet backoff |
| 2 | 03:23 | same, backoff LM; screen by gap to held-out real text | oracle spaces, 4 languages | German 93.3 pct, but Latin ranked first | not run | a degenerate "iiii" solve fits the Latin corpus (Roman numerals); fixed by subtracting the letter-curve divergence from the gap |
| 3 | 03:24 | spaces from the best context cluster (word-length KL) | 5 windows x 3 sizes | space class found in 2/5 windows at 1,200; 0/5 at 135 | not run | clusters are nearly pure but word-length KL alone does not pick the right one; the true class was never among the candidates whole |
| 4 | 03:25 | candidate classes judged by quick solves minus a shuffled-order null | 1,200, one window | wrong 18-sign class won (+2.34 over its null) | not run | a shuffled null keeps the space choice, so the delta measures "text has structure", not "right spaces" |
| 5 | 03:28-03:38 | **v1: the solve may give any sign the value space (27 values), seeded from the top 6 clusters and from none; each language keeps its best gap; top 2 solved deeper** | 12 languages, 6 restarts x 400k, deep 24; 5 windows per size + a token-shuffled null each | **1,200: 87-94 pct (median 92.5), German 1st 5/5, spaces P 1.0 R 0.96-1.0; 770: 79-94 pct (median 86), German 1st 5/5; 135: 4-18 pct, German 9th-11th, real gap = null gap** | not run | works where [K11]'s own automatic attack did not, because the n-gram model carries word spaces |
| 6 | 03:40-03:42 | harness control FR-HOMO (unspaced French verse, K 136), v1 | fit c2 part (658) and pooled (790); -N15 beside | FR-HOMO c2 6.4 pct, pooled 22.3; -N15 c2 5.6, pooled 4.4 (score.py --control); the solve invents a ~22-sign space class, Latin/Danish rank first | not run | the text has no space class; with French given and no spaces assumed (`nospace_solve.py`, 30 restarts) recovery is still only 28.5 (c2) / 35.7 (pooled), about the harness climber's 25.8: the 70 pct bar on FR-HOMO is out of reach for letter solving at this K and N, not only for this method |
| 7 | 03:42 | v1 plus a "no space class" solve per language (`--allow-nospace`) | FR-HOMO c2 and N15; Copiale 770 x2 | FR-HOMO: French ranks 4th, 6.8 pct; Copiale 770 falls from 94/79 to 0/30 pct | not run | a no-space solve with ~80 free signs overfits every language; reverted (flag kept off, results in control/attempt7/, phase1/attempt7/) |
| 8 | 03:43-03:50 | v1, size and noise brackets | noise = share of tokens replaced by a sign drawn from the window's own curve | **658 clean: 92 pct in 1/3 windows, 3-5 pct in 2/3 (2x restarts do not rescue them); 658 at 5/10/15 pct: 2-8 pct; 1,200 at 3 pct: 84-90, German 1st 2/3; 1,200 at 8 pct: 1-7; 1,200 at 15 pct: 4-8, German 7th-10th** | not run | the solve needs nearly clean text: crossover between 3 and 8 pct at 1,200 tokens, below the drafts' 14-18 pct; at c2's length it is near its size threshold even clean |
| 9 | 03:33-03:37 | task 3, word symbols (WORDSIGNS.md) | Copiale logograms as the known-answer control; neighbour-concentration G test, 60 anchors | Copiale 5/5 at p<0.0005, also at Debosnys's own size (1,184 tokens, 51-56 planted word symbols) | Debosnys pictograms (H31 class, all four drafts): G 103.9 vs null median 109, **p 0.68** | a Copiale-type design (word symbols between space signs) is excluded for the pictograms; H31's line-initial excess (3.7x) is far above the Copiale's own word symbols (1.75x, p 0.006), so the Copiale gives no precedent for it |
| 10 | 03:50 | step 2(a) on Debosnys, descriptive (space_class_debosnys.json) | X as space; top 6 clusters; beside the Copiale true space class | Copiale true space word-length KL: clean 0.08-0.43, 15 pct noise 0.14-0.70 | X: KL 0.62 (c2) / 0.61 (c1+c2), below X's own within-text shuffle p05 (0.72 / 0.75); best cluster {X, X-DOT} 0.69 | X's gaps lean slightly word-like: inside the noisy Copiale band's top, above every clean window. Weak, not a finding |

## Transferable insights (for DIGEST-1)

1. **Structural/limit fact.** A homophonic solve on Copiale-shaped text needs roughly 700+ clean tokens and under
   about 5 pct noise. c1 (132) is out of reach at any noise; c2 (658) is at the edge even clean; the settled drafts'
   14-18 pct noise is past the crossover at every length tested. A letter-design negative from any group at this
   noise is a non-test unless its own control reads at 15 pct noise (CLAUDE.md rule 3, SALV-DIAG).
2. **A constraint that kills a class of designs.** Word symbols set between word-space signs (the Copiale design) are
   excluded for the pictograms (WORDSIGNS.md, control 5/5 at Debosnys's size).
3. **Tools.** `hsolve_h.c` (C annealer; a sign may take the value "space", so the space class is found by the solve);
   `pipeline.py copiale --noise` (a real known-answer text with any noise level at any length, for any group's
   bracket); `neighbour_test.py` (blind word-symbol test); the Copiale token file with gold labels
   (`data/copiale_tokens.tsv`, 73,391 tokens).

## Next (one line each, not run)

- The only route this method leaves open is a cleaner transcription: re-run v1 on a c2 whose disputed boxes are
  settled to under ~5 pct noise, pooled with c3/c4 (about 1,200 tokens).
- Group E: rebus syllables for STAR/SUN/TREE against the sign that follows each pictogram (WORDSIGNS.md).

## Files

`SOURCES.md`, `WORDSIGNS.md`, `copiale_key.py`, `prep_copiale.py`, `build_lm.py` (the `lm/*.bin` tables are
regenerated by it, not committed), `hsolve_h.c`, `pipeline.py`, `nospace_solve.py`, `run_control.sh`,
`summarize_control.py` (`control/SUMMARY.json`), `logogram_test.py`, `neighbour_test.py`,
`space_class_debosnys.py`, `control/`, `phase1/`, `data/`.
Rebuild: `python3 build_lm.py && gcc -O2 -o hsolve_h hsolve_h.c -lm && python3 prep_copiale.py && ./run_control.sh`.
