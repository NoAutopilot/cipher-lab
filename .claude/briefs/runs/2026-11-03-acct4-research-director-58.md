# Research director, wave 58 (3 Nov 2026, 03:1x UTC by date -u): wave-57 follow-ups and RETRO-2026-11-02 apply

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Owner's directive 3 Nov 2026: all purchases on hold -- free routes
only. Stop before starting any unit that would cross 80% of the box or the cap. Price basis (ledger 3 Nov): an Opus crop read with a
sign guide in context is USD 0.40 a call, a Sonnet page read USD 0.30.

## JOB RETRO-APPLY-1102 (account 4; Sonnet 5; cap USD 4; box 40 minutes; hosts: none (disk only); Price: vision calls: 0 x USD 0 = 0)

Read RETRO-2026-11-02.md section 5 (P1-P5, each with a diff block), RETRO-PROPOSALS.tsv's five RETRO-2026-11-02 rows (status open),
CLAUDE.md Usage 8a (a gate states in its docstring what it must catch and must NOT block, each with an offline test) and
.claude/briefs/README.md. Apply all five; every one touches only briefs or tools:
1. P1 and P2 -> .claude/briefs/parent.md: add the two paragraphs verbatim from the diff blocks under the check-in duties, and add to
   tools/orphan_check.py a check "(i) PARENT STALL: <role> last check-in line <h> h ago (> 6 h)" that reads ROOM.md for the newest
   line whose role field matches `parent` or `orchestrator (owner account)` and prints the warning (exit code unchanged) with an
   offline test in tools/tests/ (two synthetic ROOM files: 5 h old must NOT fire, 7 h old must fire).
2. P3 -> the BNF-FOCUS lane brief (find it under .claude/briefs/ by grepping "BNF-FOCUS"; if it lives only in the lane's run brief,
   add the sentence there and note the path in the register row): the sentence from the diff block.
3. P4 -> tools/brief_price_check.py: exclude markdown quote lines ("> ") and fenced code blocks from TABLE_RE/ROWS_RE scanning;
   docstring updated; offline test: a brief whose only "table" word sits in a "> " line must pass, brief -52 must still fail, and
   brief -57 (which was edited to "(columns: ...)" to dodge the rule on 3 Nov) must pass both before and after.
4. P5 -> .claude/briefs/retrospective.md: the sentence from the diff block.
5. Run the offline suites you touched, `python3 tools/system_map_check.py`, set the five register rows to `applied` with the files and
   tests in the evidence cell, file_shrink_guard on every touched file, commit, push. Report: five lines (one per proposal, file and test).

## JOB NEVREVOL-ATLAS (account 4; Opus 5.5; cap USD 6; box 60 minutes; hosts: none (disk only); Price: vision calls: 12 x USD 0.40 + 1 reconciliation = 5.20)

Target ciphers/fr3987-nevers-revol-1593 (status `open`). Read NOTES.md from "## NEVREVOL-PREREG (3 Nov 2026" to the end including the
parent notes, PREREG-NEVREVOL-2.md, controls_sup.py (--mixed, --local-key), tools/keys/key60_atlas/ (atlas264ext.tsv and
contact_sheet_264ext.png) and images/v2/crops_note.md. Paste `python3 tools/intake_gate_check.py fr3987-nevers-revol-1593` first.
The question: do the six lines beat BOTH nulls when every sign is labelled directly with key60's 264ext atlas labels (no sign_guide
tag step)? One run, then stop either way (rule 3; the parent notes name this as the last instrument before the target waits on ASKS 102).
1. PREREG-NEVREVOL-3.md first: same gate as PREREG-NEVREVOL-2 (rank <= 10/201 against 200 length-class key shuffles AND 200 shuffled
   orders), the existing key60.tsv + key_atlas_extra control row (controls_mixed.txt, 10/10 at 0/10/20%) cited as the control -- do not
   re-run it; Decision block with the stop criterion before any pass.
2. Pass A: you read the 12 crops in images/v2 one at a time, strictly before reading anything pass B returns, labelling each sign with
   an atlas264ext label (or `?`); pass B: 6 Opus subagent calls, one per line pair, given only the two crops, the contact sheet and the
   atlas TSV. Order enforced: launch pass B only after passes/nevrevol3_passA.tsv is written and committed. Reconcile disagreements
   from the crops (the +1 unit), never from the key; write ciphertext_v3.tsv and reconcile_v3.tsv; record agreement.
3. Score with controls_sup.py's target branch under key60.tsv (not --local-key), paste the output, write the HYPOTHESES.md row with both
   null ranks and the judge line. Decode with decode_key.py --check only on a PASS; no reading otherwise; grades per token.
4. NOTES.md section "## NEVREVOL-ATLAS (3 Nov 2026)" with the six questions in five lines; on FAIL write the head line
   `open` unchanged and the gap as "untestable-by-this-instrument at this N (rule 3); waits on the Revol-hand sorter, ASKS 102";
   update Remaining gaps and the retry box; gaps_check must pass; file_shrink_guard; commit; push. Report: five lines (agreement,
   both ranks, judge, decision, commit).

## JOB ELEC-L29 (account 4; Sonnet 5; cap USD 3; box 40 minutes; hosts: openapi.bnf.fr at most 6 requests, archive.org at most 8, >= 1.5 s apart; Price: vision calls: 2 x USD 0.30 = 0.60)

Target ciphers/fr5761-election-1519 (status `open`). Read NOTES.md from "## ELEC-KLUCK" to the end including the parent notes, and the
ELEC-SRC section (search "nr. 357 found at BnF fr.3897 ff.116r-117r") for the fr.3897 Gallica ark and canvases (f142 right page = f.116r).
Paste `python3 tools/intake_gate_check.py fr5761-election-1519` first. Probe reachability before planning: `curl -sS -o /dev/null -w
"%{http_code}" https://openapi.bnf.fr/` with a browser UA; on 403/429 or a challenge page log it in NOTES.md and ROOM.md and skip step 1.
1. **l.29 position.** Fetch the f.116r canvas region once with `python3 tools/iiif_lines.py --ark <ark> --canvas <n> --region <x,y,w,h>
   --out ciphers/fr5761-election-1519/images --debug` (the region from NOTES.md's prior crops if recorded, else the lower third of the
   page), check the debug overlay, keep the l.29 crop (commit it this time, under 2500 px wide, and record it in images/manifest.json).
   Read the crop (1 vision call): transcribe the clear words of l.29 and the position of each non-letter sign; count words against the
   printed sentence at Kluckhohn p.814 l.14 (quoted in the ELEC-KLUCK section) and state which sign (the now-Lbar or the neighbouring 4)
   sits where the print has "Palatin". One second blind look at the crop by a Sonnet subagent (1 vision call) asked the same question
   without your answer. Grade C only if both agree and the word count is exact; else M. Propose any key change as a `--try` line in
   NOTES.md; never edit key.tsv.
2. **Lisch V pp.323-347.** archive.org advancedsearch with three broader queries (<= 3 requests: `Jahrbücher des Vereins für
   mecklenburgische Geschichte 1840`, `creator:(Lisch) AND date:1840`, `title:(Jahrb*) AND subject:(Mecklenburg)`), then one
   `_djvu.txt` fetch of the right volume (Jahrgang 5, 1840) and a grep of pp.323-347 for the 1519 election letters and the names
   Palatin/Pfalz, Trier, Mainz, Koeln, Sachsen, Brandenburg; hits as a table (columns: page, line, name, sentence) in NOTES.md.
   If no volume is found in 3 searches, say so and stop that step.
3. NOTES.md section "## ELEC-L29 (3 Nov 2026)" with six questions in five lines; update Remaining gaps and the escalation boxes;
   gaps_check; file_shrink_guard; commit; push. Report: five lines (reachability, l.29 verdict and grade, Lisch result, requests per host, commit).
