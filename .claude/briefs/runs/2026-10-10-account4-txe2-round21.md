# TXE2 round-21 jobs (LANE TX-ENGINEER-2 incarnation 5, session_01ERAcUeCn1HuAUASaqBTzcf; Opus 5.5; one job per worker; PREREG benchmark-tx/PREREG-txeng2-21.md is binding)
For LANE TX-ENGINEER-2 (account 4). Written 10 Oct 2026 02:1x UTC by date -u.
Same preamble and rules as `.claude/briefs/runs/2026-10-09-account4-txe2-round5.md` (first command `git fetch origin && git checkout -B main
origin/main`; `export CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py --start`; ROOM.md last 30 lines; claim line with cap and box;
read your PREREG section + PREREG-txeng2-0.md Amendment 9 and its dated additions, PREREG-txeng2-19/20, CLAUDE.md Usage 6 and rule 3;
commit every output BEFORE any score with its sha256 in RESULTS.md beside the commit hash; never score an eval item for an experiment;
never edit a *.truth.tsv by hand; no result JSON printed whole (F52); never AskUserQuestion; never print credentials; stage by path; never
force-push; stop before a unit that would cross 80% of cap or box; `tools/file_shrink_guard.py` on every tracked file you touched before
the final push; done line "for LANE TX-ENGINEER-2 (account-4)" with every number, "Openings of eval truth: N" and "cost: the orchestrator
get_session reading"). + `.claude/briefs/README.md` common tail. A tool change (build_vivonne_confirm2.py options) carries an offline test
where one exists for the file, and `python3 benchmark-tx/build_vivonne_confirm2.py --check` output before and after the edit.
| job | PREREG section | cap | box | inputs to read first |
|---|---|---|---|---|
| TXV-GROEN | WIT-FLAGS | 6 | 60 min | benchmark-tx/build_vivonne_confirm2.py (the flag column, clerk_mask, the --start pattern), benchmark-tx/vivonne1573-f103r-confirm2.flags.tsv (format), benchmark-tx/txeng2/vivflags/RESULTS.md (the prior verifier's method), benchmark-tx/txeng2/witanchor/{wit_groen.py,result_groen.json,RESULTS.md} (the Groen passage, fold, offsets), ciphers/fr16104-vivonne-spain-1572/tx/{dec_norm.txt,dec_f10*_passA.txt,dec_f10*_passB.txt,merge_dec.py}, benchmark-tx/txeng2/scorerfix/run_audit.sh (what the lane runs after you; you do NOT run it), BENCHMARK-TX.tsv row 11. You are a VERIFIER: you may open the truth and the --offsets dump; you never open any reader pass of f.103r or any f.103r crop. |
| TXE2-OL1BOXES | OL1-BOXES | 5 | 60 min | benchmark-tx/txeng2/oracle1/{manifest.tsv,manifest.tsv.sha256,make_manifest.py} (verify the sha256 first; never re-sample), benchmark-tx/txeng2/boxes/{RESULTS.md,build_boxes.py,spin_join.py} (the recipe), tools/glyph_atlas.py --help (segment), tools/sign_sorter.py docstring (--signs/--labels/--pages, blind by default), tools/sorter_preflight.py, tools/cvd_check.py, LOCAL-QUEUE.tsv row L74 (the owner's instruction, for the lede), research/SO-TX-TRANSCRIPTION-2026-10-10.md section 4 "Reference". Read-free: no pass, no truth, no key, no decode, no label from any read; counts compared to nothing. |
