# ARM-H73: vocabulary-prior solver for the Armstrong 20 Feb 1808 code, matched control first
(LANE-ARM-B, account 2 lane orchestrator session_017E8NVaLGF23Wd9DtaiA91T, 3 Oct 2026 19:2x UTC)

Target: ciphers/armstrong-madison-1808 (369 numeral groups, a unique two-level code; 0/369 read). Row H73 in CAMPAIGN.md is yours
(already claimed by the lane; set it to done/result when you stop, and add your log line). Model: Opus 5.5. Cap USD 10, box 120 min;
stop before starting any unit that would cross 80% of either. No vision calls in this job (all inputs are on disk).

Read first, in this order: CAMPAIGN.md (header, "Attempts already made", rows H27 and H73, log); HYPOTHESES.md "Summary" sections and
the ARM-C1, ARM3-LOOP and H27 entries; NOTES.md ARM-DESIGN, ARM-C1, ARM3-LOOP, H27; h27/PREREGISTRATION.md; tools/families/nomenclator.py
--help; tools/data/uscodes-1800/README.md. Run `python3 tools/intake_gate_check.py armstrong-madison-1808` and paste its output into your
NOTES.md section; nonzero exit stops the job. Run `python3 tools/tool_shelf.py` on "nomenclator vocabulary prior" before writing code, and
extend tools/families/nomenclator.py (an option, with an offline test in tools/tests/) rather than a private copy (CLAUDE.md Usage 8).

What is new (say it in the prereg in one paragraph, or do not run): Tomokiyo's suggestion, "a model might read it if it learns the
vocabulary of a sibling code". ARM-C1 was blind (no word list), ARM3-LOOP and H27 were crib loops (H27 with slot grammar, no vocabulary).
H73 constrains book values (>=100) to a code-maker's word list from a sibling code (WE028 1600 entries; THE=972 580) and particles (1-99)
to the siblings' short-word lists, with the ARM-DESIGN slot rule (units digit = inflection slot of a decade root), scored by the en18
judge corpus. Two pre-registered variants: V1 one-part (book value order monotone in the word list's alphabetical order; DP/Viterbi
alignment of the target's sorted distinct book values to the list) and V2 two-part (vocabulary only, no order). If either variant is
the same instrument as ARM-C1/ARM3-LOOP/H27 under a different name, stop and log why.

1. Pre-register (h73/PREREGISTRATION.md, committed and pushed BEFORE any score): variants, the vocabulary sets, the gate (word accuracy
   on the control >= 0.6, the ARM-C1 gate, on at least 2 of 3 control letters/seeds), how the target output is judged (en18 judge PASS
   AND the same solver's decode of the shuffled target order must FAIL the judge, ARM-C1 lesson in CLAUDE.md rule 3), and the stop rule.
2. Matched control, design- and vocabulary-matched (CLAUDE.md rule 3: match the design, not only N and K): take held-out real Armstrong
   plaintext from tools/data/uscodes-1800/decodes/ (15 Feb and 22 Feb 1808; never used to tune), re-encode into a synthetic code of the
   target's design at N=369 with the target's singleton rate and slot shares, whose word list is the OTHER sibling's (prior from WE028
   -> synthetic book from THE=972's list, and vice versa) so the prior is not the answer; measure and record the vocabulary overlap
   between prior and synthetic book, and also run one control at the overlap you judge realistic for a different maker in 1808
   (pre-registered). Check the control's own blind baseline (nomenclator.py without the prior) is not already near ceiling (rule 3
   gain-gate paragraph). Report blind and prior numbers side by side.
3. Gate: below gate on the control -> do not run the target; log in HYPOTHESES.md and CAMPAIGN.md "untestable by this tool at N=369
   (vocabulary prior, matched control X vs gate 0.6)" and stop. At or above gate -> run V1/V2 on the target once each, judge, shuffled
   check, and report the decode graded S/M per token (rule 4; no H or C exists) only if both judge conditions hold.
4. Write h73/ (code invocations, outputs TSV/JSON), NOTES.md "## Step H73" (intake output pasted, both numbers side by side, what was
   found and where it was not found), HYPOTHESES.md row with control and target numbers side by side (tools/family_run.py convention),
   CAMPAIGN.md H73 status/result and a log line with cost. Rule 7: any reading gets a regenerating script with --check.
5. tools/gaps_check.py armstrong-madison-1808 before the done line. Commit by explicit path, fetch/rebase, push.

ROOM: claim line first with your box end time; a halfway cost line; a done line addressed to LANE-ARM-B with the two numbers. A cost
figure comes from get_session, not your own estimate. Report what was found and where it was not found; do not classify novelty.
Never call AskUserQuestion; never print credentials; never name the owner; never the words solved, cracked, novel, first, new for
anything this project did.
