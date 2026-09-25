# fair-game-2010

open
Minimal check-solved, 25 Sept 2026 (LANE B3 worker bFAI), before any transcription/solve (intake step, `.claude/briefs/breadth.md`): Cipherbrain post 36 (Schmeh, 13 Apr 2017, scienceblogs.de/klausis-krypto-kolumne, already on disk as `sources/schmeh/posts/36-fair-game.txt`/`.html`, fetched by bSPEC2 this same window) and its comment thread read in full: no solution posted by any commenter. Schmeh's own text: "not much can be found about the Fair Game code online... nothing seems to have been published about this mystery." One commenter ("Martin Halpin", the only comment ever posted under that name, 2014-15 window) proposed reading the letter immediately after each marked letter instead of the marked letter itself -- Schmeh states this is untested by him. A second commenter, James Mulliss (9 Feb 2023, comment #5/#6), transcribed the actual credit words containing each of the ~64 marked positions (word with the marked letter capitalised), which is real primary-source context text, not just the AboveTopSecret marked-letter sequence -- this is the "original unmarked credits text" the spec's test 1 says is needed, already on disk, no new fetch required for it. Both solver repositories grepped via shallow clone (github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers; cloned to /tmp, grepped, deleted, not committed): cyphersolver's `TARGETS.md`/`top50/NOTES.md` list Fair Game among items "open but not settleable by cryptanalysis", grouped with Shugborough/Powers as "Ten letters; a disputed transcription of film credits" (that repo counts 71 letters, not 68 -- a source discrepancy, not reconciled this pass); aaymeloglu/unsolved-ciphers `SHORTLIST.md` describes the SAME Halpin-type hypothesis independently ("A 2014 anonymous commenter claimed the yellow letters mark the letters that follow them") and recommends "Enumerate marker schemes (next letter, previous letter, first letter of next name, offsets) and check for an English sentence" -- confirming this specific test has not been run and reported anywhere found. It also flags two later Schmeh posts with "complete screenshots" (2017-06-22) and a "2019 revisit" -- not fetched this pass, out of scope (imdb.com is the only extra host this brief allows). OpenAlex (`api.openalex.org/works?search=`, key header) for "Fair Game film cipher yellow letters credits": 125 hits, none relevant (film-studies/Indigenous-history/comics papers, no cryptography match). Semantic Scholar (`api.semanticscholar.org/graph/v1/paper/search`, key header) for "Fair Game film cipher yellow letters end credits": 0 hits.

Status: open, unsolved by any source checked. Proceeding to cheap test 1 (Halpin "next letter" hypothesis, using the James Mulliss comment-thread transcription already on disk) per brief `.claude/briefs/runs/2026-09-25-lane-b3-fair-game-2010.md`.

Intake gate check (`python3 tools/intake_gate_check.py fair-game-2010`):
```
fair-game-2010: open (line 3) -- edition/page or full-text-search citation found within 6 lines
exit=0
```
Proceeding.

## Cheap test 1: Martin Halpin "next letter" hypothesis (25 Sept 2026, LANE B3 worker bFAI)

Data: James Mulliss's real credit-context transcription (comment #5/#6, already on disk, see intake
paragraph above) gives the actual word each of ~65 recoverable marked letters sits in -- the "original
unmarked credits text" cheap_tests_in_order[0] called for; no IMDb fetch was needed once this was found in
the post already on disk (the spec's proposed IMDb route was written before this comment was located).
Multiset check: the 65 letters recoverable this way match the ciphertext's 67 known letters exactly except
one missing S and one missing T -- strong corroboration this is the real marking (not fabricated), but the
transcription is incomplete by 2/67 and the commenter's list order is an UNVERIFIED proxy for the true
credit-roll order (a caveat on the negative below).

Procedure: for each marked occurrence, in list order, take the letter immediately following the mark
inside its word (a documented proxy -- next listed word's first letter -- for the handful of marks that
are a word's last letter). Script: `specs/cheap-tests/fair-game-2010/run_test1.py` +
`credits_words.py`; output `specs/cheap-tests/fair-game-2010/test1_output.json`.

**Target**: next-letter sequence (65 letters: `tatdmotaeaepmlefciceaselrtirinseoranaeouiugleaobadoauearussvwberr`)
judged with `tools/judge_plaintext.py specs/fair-game-2010.json`: language score -2.202 (random-null p99
-1.77, real-English p05 -0.944), word cover 0.462 (min 0.6) -- **FAIL**.

**Control (a), planted-name sanity check**: same extraction procedure, same word pool, marks placed to
spell a known 13-letter name (ROBERTJOHNSON, unrelated to the film's plot) -- recovered exactly in 3/3
trials. Confirms the procedure and script work correctly and can recover a real signal when one exists.

**Control (b), random-marking false-positive rate**: 3 trials of random marks in the same word pool at the
same N=65: judge FAIL on 3/3 (scores -2.134 to -2.261, word cover 0.246-0.523). The real target's score
(-2.202, cover 0.462) sits **inside** this random-noise band, not below or above it.

**Verdict**: control-backed negative for this specific reconstruction of the Halpin hypothesis -- the real
target's next-letter sequence is indistinguishable from random-marking noise of the same design, while the
sanity control confirms the test has power to detect a real signal. Caveated per the missing-2-letters and
unverified-order limitation above: this negative applies to this particular reconstruction of the mapping,
not to every possible true ordering of the same underlying words. Does not close the target on its own
(only test 1 of 3 run this pass, per brief; do not run test 2).

Status stays `open` (a single cheap test's control-backed negative is not `closed-negative` per rule 5 --
the full ladder for this target is only one test long so far). No NEAR.md candidate: this is a clean
negative with its own control landing in the expected band, not a control-below-gate gap.

Requests this pass: github.com 2 shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers;
grepped, deleted, not committed), api.openalex.org 1, api.semanticscholar.org 1. No imdb.com or
web.archive.org requests needed (real data already on disk covered the test). No subagents.
