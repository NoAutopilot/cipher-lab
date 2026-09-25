LANE R8 DSN -- fr2933-salviati-1525: the next DESIGN family, with its own matched control (Fable, cap $15, box 90 minutes; disk only plus
read-only web search for published descriptions of Florentine/papal nomenclators of 1520-1530; no archive hosts, no subagents).
Authority: LANE R8 brief job 1; NEAR.md row "fr2933-salviati-1525" (named next step: a design change, not more restarts); CLAUDE.md rule 3
(control first, matched DESIGN not only N and K) and rule 5 (near solves). Common: 2026-09-25-lane-r8-common.md.
Intake gate (live, 25 Sept 22:22 UTC): "fr2933-salviati-1525: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
State: 2,820 pooled signs; 223 code+mark types (atlas re-pass 204 sure / 198 with likely merges -- use K=205 as the lane brief says); measured
transcription error 5% (bracket 3-7%; del:ins 60:40 plus named base-code confusions; NOTES "CM3" sec.1; control/codemark_curve.py CM_ERR generator).
Excluded so far: letter-per-type code+mark at 5% error (CM3: control 61.7/81.7/86.0% vs target -2.656 to -2.678/symbol, no Italian). Untested:
every design where a type is NOT one letter. Read NOTES.md sections CM, CM2, CM3, HYPOTHESES.md, leafnotes/siblings.md, LESSONS.md on period
keys, and what sources/ and LESSONS.md hold on 16th-century Italian nomenclators (Meister 1906 is cited in NOTES; Tomokiyo's Italian pages if on disk).
Job:
(1) Design. From the period evidence and the target's own statistics (type frequency curve, repeat structure, which base codes carry marks,
    positional behaviour of marked types, word-divider candidates), choose ONE next family and justify it in <= 5 sentences with the numbers:
    e.g. syllabic/bigram table (base code = consonant, mark = vowel, as in Italian syllabaries of the period), homophones + nulls + a small
    nomenclator (code words for names), or nulls plus a small code. Write the choice first into NOTES "## DSN: next design family (25 Sept 2026, LANE R8)".
(2) Family. Add it under tools/families/<name>.py with a generator (synthetic cipher of that design from it16 text: N 2,820, K ~205, the CM3
    measured error mix at 5%) and a solver, register it in tools/families/__init__.py / family_run.py as the existing families are, and an
    offline test in tools/tests/ that runs in < 60 s. If family_run.py needs a spec, write specs/fr2933-salviati-1525.json (ciphertext from the
    pooled ciphertext files as transcribed, source and date, alphabet, constraints, cheap tests, judge block with it16) -- none exists yet.
(3) Control first: 3 seeds, gate 0.6 token (or letter) accuracy on 2 of 3, at 5% error. Check the control's blind ceiling is not ~95% at
    0% error with a trivially easy design (rule 3's headroom note) and report the 0% number too.
    Below gate -> CONTROL BELOW GATE row; state the reason and name the transcription step that would lift it; stop.
    Gate met -> (4) target, 3 seeds: score/symbol vs the control's, cross-seed agreement, any Italian. A decode that reads goes to
    reading_dsn.txt with a regeneration script, `tools/judge_plaintext.py` output pasted, tokens graded S/M, and ROOM
    "for LANE R8: salviati reading candidate" (the orchestrator orders the re-derivation; do not call it solved).
Rows to HYPOTHESES.md (family_run writes them) and control_curve.tsv. Do not edit NEAR.md (the orchestrator does).
ROOM done: "done: for LANE R8: salviati dsn <family> control <x>/<y>/<z>% (gate 60 on 2/3, 0%-error ceiling <c>) target <t or not run>".
Report what was found and where it was not found; do not classify novelty.
