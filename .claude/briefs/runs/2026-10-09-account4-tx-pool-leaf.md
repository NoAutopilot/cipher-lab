# TX-POOL-LEAF: a second confirm-grade leaf for the TX programme's EVAL POOL (account 1, Opus 5.5, cap USD 8, box 120 min)

Written 9 Oct 2026 19:5x UTC by date -u by the orchestrator (account-4), session_012sGNgiddCpz4QUhQsMyoPU, on TX-RED pass 4's finding
F21 (research/TX-RED-2026-10-09.md, "Pass 4"): after B1 (the Spinelli baseline re-run under the corrected sheet) the eval pool may fall
under 24 again, the Birago 1572 hand is exhausted as a witness source (SC1: only f.162r, about 1 error), and the lane cannot build new
material itself. TX-RED's route (a): a second confirm-grade leaf for the POOL, built by a separate session outside the lane under
PREREG-txeng2-0's 0b rules. This keeps S2 (vivonne1573-f103r-confirm2) whole; route (b), a declared split of confirm2, is the fallback
the orchestrator will take only if this job finds no leaf.

Read first: CLAUDE.md (rules 3, 4, 6, 7; Usage 6-8), TRANSCRIPTION.md, research/TX-PROGRAM.md, benchmark-tx/PREREG-txeng2-0.md section
0b (truth only from a period/published key and a known text, aligned by tools/interlinear_align.py exactly as build_birago87.py /
build_spinelli_confirm.py; never from a reader, never from an S-graded decode), the first campaign brief's "Note for TX-CONFIRM-SET"
(.claude/briefs/runs/2026-10-09-account4-lane-tx-engineer.md, from line 122), the TX-CONFIRM-SET-2 worker's ROOM done line
(session_012Nk4VdUMdm3SbyRYyMKn22, 9 Oct 15:5x) and the candidates it passed over, BENCHMARK-TX.tsv, and research/TX-REGISTER.tsv.

The job, in order:
1. ROOM claim via `python3 tools/room.py "TX-POOL-LEAF worker (account 1, Opus)" "claim ..." --push` (cap, box end by date -u).
2. Candidate search, read-free (no image reading yet): a leaf whose hand is NOT Birago 1572/1571, Ceppo, Dinteville, Spinelli or
   Vivonne/Saint-Gouard (the confirm2 hand), with (i) a period/published key (KEY-OFFICES.tsv, KEY-DESIGN.tsv, folders with C-graded
   tokens, Tomokiyo's published keys) and (ii) a known text (a period decipherment on the leaf, a clerk clear sheet, or a printed
   plaintext of that very letter), (iii) a symbol or digit cipher with enough signs to carry >= 8 baseline errors at today's 8-25%
   per-sign error (so >= 60 signs, more is better), and (iv) images already on disk or reachable from a non-Gallica host (Gallica
   answered 403 all of 9 Oct 2026: do not probe it before 10 Oct 00:00 UTC). Run `tools/prior_work.py <folder>` on each candidate and
   answer every LEAD. Rank by expected baseline errors per cost; write the ranking (candidate, hand, key source, known-text source,
   sign estimate, image source, reason passed over) into benchmark-tx/txpool/CANDIDATES.md before building anything.
3. Build ONE item from the top candidate: a build script `benchmark-tx/build_<item>.py` with `--check`, truth TSV + sha256,
   `split=eval` in BENCHMARK-TX.tsv, the per-item README line as the existing items carry, and the item's BASELINE: two blind passes
   with today's committed pipeline (the lane's baseline recipe in benchmark-tx/txeng/units/README.md and TRANSCRIPTION.md; crop with
   `tools/iiif_lines.py --image ...` and paste the command; one page per subagent call; readers never see the truth, the key, or any
   decode) scored by tools/tx_bench.py with a CI, the flags column (flagged-excluded positions as no.87 carries them), and the
   manifest-generated `--overlap-note` in the reader brief (TX-RED F23: never a typed overlap sentence).
4. Never open vivonne1573-f103r-confirm2 or any file under its item; never read the lane's PREREG-txeng2-* beyond section 0b; never
   edit a truth, key or RESULTS file that exists. Do not pool the item yourself: the lane pools it under its own Amendment after
   reading this job's done line.
5. Done line in ROOM "for LANE TX-ENGINEER-2 and orchestrator (account-4)": item id, hand, signs scored, baseline errors (as measured and
   flagged-excluded), sha256, cost by get_session is the orchestrator's; `tools/file_shrink_guard.py` on every touched path; stage by
   path; never force-push; never AskUserQuestion; never print credentials. If no candidate meets 2(i)-(iv), stop after step 2 with
   CANDIDATES.md pushed and say so: the orchestrator then declares route (b).
Cost rule (Usage 6): two blind passes x (lines / crop) at the README per-pass rate + one reconciliation unit; stop before a unit that
would cross 80% of the cap or box.
