# LOOKALIKE-TOOL (account-3 orchestrator, 2 Oct 2026): promote the look-alike pass to tools/ and validate it

Model Opus 5.5. Cap $6, box 60 min. CLAUDE.md Usage 8 ("shared scripts before new ones") and 8a.
Source: ciphers/nevers-birago-fr3251-1572/harvest/{confusion_1572.py, lookalike_packet.py, lookalike_reconcile.py}
and NOTES.md section "NEVBIR-LOOKALIKE". These are target-local; any symbol-cipher transcription with two blind
passes can use the same method.

1. Build `tools/lookalike_pass.py` with subcommands:
   `confusion PASS_AGREEMENT_TSV... --out confusion.tsv` (label swaps with counts across every two-reader alignment);
   `packet --agreement A.tsv --confusion confusion.tsv --top 10 --crops DIR --sheet SHEET --out DIR` (flag tiles
   whose readers split or whose label sits in a top-N pair; write the candidate-only sheet cut and the subagent
   prompt, value-blind, ids only); `reconcile --passA --passB --reread --out passD.tsv` (the fixed 2-of-3 rule from
   lookalike_reconcile.py's docstring; UNSETTLED keeps the passC label; also writes focus.tsv for tools/sign_sorter.py
   --focus). `--help`; offline test in tools/tests/test_lookalike_pass.py; docstring states what it is for and one case
   it must not be used for (8a). Leave the target-local scripts in place, each pointing at the tool in its header.
2. Known-answer validation (the method has only been measured by reader agreement, not against truth): run it on a
   1572 leaf whose text is known from a period witness -- no.87 f.178r/v + f.179r against the clerk's clear sheet
   (canvas 182; GAPS4), and/or no.77 f.152r against the f.151v slip. Report TRUE sign error before and after the pass
   (against the witness, normalised per rule 3's transcription-convention paragraph), and how many look-alike
   "corrections" moved a correct label to a wrong one. If true error does not drop, say so plainly: the method is then
   "agreement-raising, not accuracy-raising" and the f.144r residual-based control is downgraded in NOTES.md.
3. Document: one line in CLAUDE.md Usage 6 (transcription paragraph: when two passes disagree by >10% or on named
   sign pairs, run tools/lookalike_pass.py before a third full pass; what machines still split goes to the owner's
   sign sorter via focus.tsv, never blocking); LESSONS.md entry with the validation numbers; SYSTEM.md entry
   (tools/system_map_check.py must pass); .claude/briefs/transcription.md step naming it.
Report what was found; file_shrink_guard on CLAUDE.md, LESSONS.md, SYSTEM.md before push. Done line "for the account-3 orchestrator".
