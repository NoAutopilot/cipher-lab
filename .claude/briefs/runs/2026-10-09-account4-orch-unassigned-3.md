# Orchestrator jobs, unassigned progress rows, batch 3 (account-4 orchestrator session_012sGNgiddCpz4QUhQsMyoPU, written 9 Oct 2026 19:5x UTC by date -u)

Source: `python3 tools/progress_block.py --unassigned` at the 19:5x UTC successor check-in listed rows in five folders with nobody on them.
Three get a worker here (the cheapest named next step in each folder's own Verdict line); the others are recorded, not queued:
fr3416-nevers-fils-1589 (next step is a person reading the f.27r L09 gloss: an owner card, which account 4 cannot write to the desk
board; carried under "Waiting on you (optional)" in STATUS); birago-fr3252-1571-72 (its own Verdict says the per-sign tiles are retired
after two attempts and the Nov 1571 system needs new material: UNA3-BIR-VERDICT below only makes the line say so);
lodewijk-van-nassau-1573-74 (gap-1 band: three different instruments at gate FAIL; read at the next check-in, not queued blind).

Common rules: exactly those of .claude/briefs/runs/2026-10-09-account4-orch-unassigned-2.md "Common rules" (read them there), plus:
done line "for orchestrator (account-4)"; cost by get_session is the orchestrator's; stage by path; never force-push.

## UNA3-PISA (account 2, Opus 5.5, cap USD 1.5, box 40 min)
Folder ciphers/fr16045-pisany-rome-1585. Step: the Verdict's cheapest next (9 Oct): the T47 -> T27 relabel re-score of the 3 T47
tokens UNA-PISA/PISA-275R settled on T27 (f), UNA2/PISA-T32 shape, disk only. Read UNA-PISA's and PISA-T32's NOTES sections and their
PREREG files first; write the PREREG amendment (gate as in PREREG-UNA-PISA.md) before scoring; a transcription-label question, never a
key86 value edit; commit the relabel only if the gate passes, else log the numbers. Gallica untouched.

## V-PISA-T32 (account 1, Opus 5.5, cap USD 1.5, box 40 min)
Folder ciphers/fr16045-pisany-rome-1585. Step: the Verdict's second item: a verifier check of the PISA-T32 carry-over in AUDIT.md
(UNA2-PISA's was checked as AUDIT 3; PISA-T32's is not). A session other than UNA3-PISA. Rule 10 wording; corrects any over-claim; adds
the AUDIT section; no decode.

## UNA3-BAL (account 1, Opus 5.5, cap USD 3, box 60 min)
Folder ciphers/baluze167-davaux-1637. Step: the Verdict's cheapest next: a separate verifier on the f.228 reading (f.228r-v; the
lane's named next step). Verifier brief template in CLAUDE.md "Verifier brief (template)": N-class and depth (rule 4a,
tools/depth_check.py) per item, AUDIT.md section, SECOND-OPINIONS-QUEUE row if N3 or better, JSTOR-QUEUE rows in both families. Not
the f.247-hand glossed-text search (a later row).

## UNA3-BIR-VERDICT (account 2, Opus 5.5, cap USD 1, box 20 min)
Folder ciphers/birago-fr3252-1571-72. The Verdict line (NOTES.md line ~1931) names as cheapest next a step its own parenthesis says is
retired (per-sign split tiles, two attempts, UNA2-BIR3252) and then "new material". Rewrite the Verdict and "## Remaining gaps" /
"## Escalation" so the next step is the outside blocker (a letter or key sheet in another Nevers/Birago volume; Gallica 403 on 9 Oct,
re-probe after 10 Oct 00:00 UTC) with the [retired] step marked and its RETIRED.tsv reopen condition cited; `tools/gaps_check.py` and
`tools/retired.py --check` pass; NEXT-STEPS "next:" updated. No reading, no decode, no key edit.
