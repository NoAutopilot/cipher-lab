# LANE-NEAR3 (account 2) and LANE-RUN1 (account 1) -- 4 Oct 2026 00:4x UTC (account-3 orchestrator)

Operating rules for both exactly as `.claude/briefs/runs/2026-10-03-acct3-lane-pools-images.md` paragraph 1 (own-account lane
orchestrator, Opus 5.5, workers via create_session, ~6 live, refill within 15 min, ledger from get_session, stop on allowed_warning
or backlog spent; "LANE <X> handoff" in STATUS.md + one done ROOM line). Off limits: Birago/Nevers-Birago/Ceppo (owner sorter),
Armstrong, Debosnys, any folder with a ROOM claim < 6 h, any folder account 4 claimed (GAPS*/FT4*/CLOSER* lines; account 4 is out of
usage -- account 3 re-queues its stale claims itself). tools/intake_gate_check.py pasted before each deep-work brief; TRANSCRIPTION.md
for every transcription; per-pass pricing; "report what was found and where it was not found; do not classify novelty".

LANE-NEAR3 (account 2) -- push the two NEAR rows from LANE-READ2 (STATUS.md "LANE READ2 handoff"), then keep going.
1. hellen-frederick-1752: open R4376 (f.56, 1754) and the pre-f.44 Add MS 32276 key records on DECODE for codes 1-800 (~6; one login per
   worker, images never committed); if a sheet carries 1-800 of the same series, transcribe it (2 blind passes + reconciliation) and
   re-run the pre-registered LR100 test on R1953 with the full key. Then a VERIFIER session (separate, CLAUDE.md template) -> AUDIT.md.
2. clair1161-avis-flandre-1688: rule-7 re-derivation (fresh session, spec + key only, ~3); pre-registered looser repair rule (~5); q/ls and S
   split test (~3); then c186L, c187L, c187R, c188L transcription (~6 each) and a pooled re-anneal with the same gloss gate.
3. Backlog left: NEXT-STEPS.tsv rows with blocker `runnable`, cost band S first, near rows first (python3 tools/next_steps.py fresh).
LANE-RUN1 (account 1) -- clear runnable next steps.
1. Tool job: a segmenter for the DECODE cursive hand (rah-juan-manuel-1521; glyph_atlas gave 4 px fragments) as an option on the shared
   tool (Usage 8: no private copy), offline test included; then a sorter sheet over R9528 f.194 + R9529 f.199 + R9501 (account 3 publishes
   it -- say so in ROOM). Cap 12.
2. es132-vargas-mexia-1578 test 1: rest of f.119 + f.89 under Cp.30 vs Teulet where printed, with a statistic that is not at ceiling
   (pre-register it; FT-B found word-cover at ceiling). Only letters NOT in el-descifrador/cabinet-noir's list (cabinet_noir_map.tsv).
3. NEXT-STEPS.tsv `runnable` rows not taken by LANE-NEAR3 (claim each in ROOM first), cost band S then M, one worker each, at the row's
   own named next step and estimate. Skip rows whose next step names a person's pass or the owner sorter.
