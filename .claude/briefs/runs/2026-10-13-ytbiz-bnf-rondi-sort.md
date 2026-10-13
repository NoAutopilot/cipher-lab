# BNF-RONDI-SORT (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: build a BLIND sign-sorter page (not published) for the f.62r cipher of `ciphers/fr3613-rondinelli-1590` (Hercole
Rondinelli to the duc de Nevers, Paris, 11 Nov 1590), plus ONE ASKS row, nothing else: no transcription pass, no decode, no key.
Why: BNF-RONDI-TX's two blind machine passes agree on only 376/698 tokens (53.9%); under CLAUDE.md Usage 6 a split above a tenth
means the next pass is a person's -- the owner settles the sign inventory in the sorter, then machine passes run against those
labels. Cap USD 2.5, box 60 min. Disk only. Model: Sonnet.

Read first: CLAUDE.md Usage 6 (sorter paragraph) and the MQS sorter bullets (blind by default, `--show-values` never),
TRANSCRIPTION.md, the folder's NOTES.md (BNF-RONDI-TX section), `tools/sign_sorter.py --help`, `tools/sorter_preflight.py --help`,
and one existing build to copy the pattern: `ciphers/jan-van-nassau-1572-75/sorter/a2o/build.sh` (SORT-A2o, 10 Oct) or
`ciphers/na-oldenbarnevelt-2442-1605/sorter/build.sh`; last 30 lines of ROOM.md.

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap. Check 1 of `.claude/briefs/prior-work-step.md`: grep
   ROOM/NOTES/ASKS for a sorter already built for this folder; if one exists, stop.
2. Cut sign tiles from the committed line crops `images/f62/` (reuse the repository's tile cutter as the a2o build does; one tile
   per sign, vowel marks kept on their base sign). Focus list: the tiles at positions where pass A and pass B disagree
   (tx/passA.tsv vs tx/passB.tsv), first.
3. Build with `tools/sign_sorter.py` in its DEFAULT blind mode (no values, no key blocks, no machine labels on the page), run
   `tools/sorter_preflight.py` (and `tools/cvd_check.py` if the preflight does not) until PASS. Commit `sorter/build.sh`, the
   inputs and a sorter/README.md (what the page asks, how to export, that `tools/sign_sorter_apply.py` is the follow-up). Register
   the family in `tools/data/sorter_families.tsv` only if the tool requires it for a blind build. Do NOT publish an artifact.
4. ASKS.md: ONE row (fetch and rebase first; next free number), 7 columns like the rows above it: what is needed (the f.62 sign
   inventory; why it matters: a period partial key for this correspondent exists, fr.3995 f.63r no.34, and by eye covers ~85% of the
   agreed tokens), the exact action (the build command, focus tiles first, minutes estimate), who (owner), status backlog. One ROOM
   `flag:` line naming the row for the orchestrator (owner account).
5. NOTES.md: section "## BNF-RONDI-SORT (13 Oct 2026, account 2)" with tile counts, focus count and the preflight output; update
   the Remaining gaps blocker for the transcription to "waiting-on ASKS <n>"; `python3 tools/gaps_check.py fr3613-rondinelli-1590`.
6. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM done line
   "for LANE BNF-FOCUS (account 2)": tiles, focus tiles, preflight result, ASKS number.

No reading, no decode; do not classify novelty (rule 10). Never print credentials. Never the words solved, cracked, novel, first,
new for anything this project did. Never call AskUserQuestion. If `tools/room.py --start` fails to push from a detached HEAD:
`git push origin HEAD:main; git checkout -B main HEAD`.
