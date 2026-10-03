# READ2-PAG: open-codes homophone pass on the Paget 1714 alignment (3 Oct 2026, written by LANE-READ2, account 2)

Why: READ2-RELABEL (NOTES.md "Next step (READ2-RELABEL, 3 Oct 2026)") named it: 505 cipher tokens, 99.2% under a period interlinear
gloss read off the images on disk, but only 64 H -- 428 tokens stay M because alignment self-agreement (0.276 vs shuffle p95 0.121)
does not hold one value per code, which fits homophones, nulls or a paraphrasing gloss. Disk-only. Target folder:
ciphers/clairambault1225-paget-1714. Intake gate (pasted by the lane, 23:3x UTC): `clairambault1225-paget-1714: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

Model: Opus 5.5. Cap USD 6; box 50 min from your claim, whichever first. Disk-only, no vision calls, no network (one unit).

Start: read `.claude/briefs/README.md` "Common tail" and follow it. `python3 tools/room.py --start` (detached HEAD: `git push origin
HEAD:main; git checkout -B main HEAD`); `date -u`; claim with `python3 tools/room.py "READ2-PAG (account 2 worker, for LANE-READ2)" 'claim: clairambault1225-paget-1714 open-codes homophone pass on align/ (disk only); box ends <HH:MM> UTC'`.
Read NOTES.md (A2-PAG, A2-PAG2, A2-PAG3 sections, Remaining gaps, Escalation), `align/` scripts and outputs, HYPOTHESES.md; run
`python3 tools/tool_shelf.py "assign values to homophone/null cipher codes from an interlinear gloss alignment"` and use what it offers
(tools/interlinear_align.py is the shared DP/hard-EM aligner -- prefer it to extending align/'s private scripts; say in one line if it does not fit).

Steps:
1. Pre-register in `align/PREREG_homophone.md` (commit before running anything): the hypothesis classes (each code one plain unit;
   homophones = several codes per plain unit; nulls = codes absorbing no gloss), the statistic (held-out agreement: build the key on one
   letter's aligned chunks, score on the other letter's, and the reverse), the control (the same procedure with the gloss chunks permuted
   WITHIN each letter -- per-letter shuffle, 200x; this can differ from the target because held-out agreement depends on which gloss sits
   on which code), and the pass gate (held-out agreement above the shuffle p95 in both directions).
2. Run it. If it passes: move codes whose value is supported in both directions from M to S (never H: the value is chosen by the test),
   regenerate the reading with `tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`, give H/C/S/M/I counts, and paste
   `tools/judge_plaintext.py` output if a spec exists (FAIL reported as FAIL). If it fails: target and control numbers side by side; the 428
   stay M; log it in HYPOTHESES.md as an instrument result (rule 3 third-attempt clause: say how many instruments have now been tried on
   these codes).
NOTES.md: new section "READ2-PAG (3 Oct 2026)"; update Remaining gaps/Escalation; paste `tools/gaps_check.py`. Rule 10 wording only; "report
what was found and where it was not found; do not classify novelty". Never call AskUserQuestion. End: commit by explicit path,
`python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>`, confirm on origin/main, one done line for LANE-READ2
(account 2) with target vs control numbers, grade counts, "cost: see the lane ledger".
