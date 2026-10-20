# PREREG MONL-KING4 (20 Oct 2026, 23:2x UTC; addendum to PREREG-MONL-KING2.md and -KING3.md; pushed before any crop is re-cut or re-read)

Question: after one look-alike pass on the f.133 (Gallica c258) L01-L25 positions where blind passes A and B split, does any decoded run
under key.tsv (Tomokiyo's Cipher 1 table, unchanged) clear the registered S bar, and does the band gate move?
Tiles: every row of ciphertext_c258.tsv (passC = the committed reconciled reading) whose pass_a != pass_b: 124 rows (the brief said 125;
124 is what the file holds). Rows where one pass has '-' are 'single' tiles (one candidate plus its two top confusion partners).
Instrument: tools/lookalike_pass.py -- `confusion` from the A/B split pairs of king2+king3, then `windows` (not `packet`: the tool's own
docstring records packet-style prompts drawing re-reads that copied passC; windows hides the tile's label, lists candidates
alphabetically, and is what MONL-LOOK used on c268), then `reconcile` with its fixed rule: a firm (H/M, not SPLIT) re-read equal to A or B
settles the tile 2-of-3 with the re-read label; anything else stays UNSETTLED, keeps passC and goes to king4/focus.tsv. Crops: the folder's
own regen_monlking2.sh + regen_monlking3.sh (one openapi.bnf.fr request for the native page; the brief's "crops on disk" did not hold in
this container -- logged). Candidate cells cut from images/keysheet_monluc1_ids.png (ids only). Readers: 3 subagent calls (about 41 tiles
each), strongest model (CLAUDE.md Usage 1 measured exception for glyph reading), value-blind: no key, no decode, no tile label.
Echo check (reported, not gated): share of firm re-reads agreeing with A, with B, and with passC; a re-read that sides with passC on > 95%
of tiles where passC differs from one reader is read as possible echo of the context labels, and the new error figure is then marked so.
New error: (a) residual = unsettled / all 897 signs (the tool's 2-of-3 figure); (b) for the noise bracket, r_new = (unsettled tiles +
tiles relabelled away from passC) / 897 is NOT used; the control noise is r = unsettled / 897 floored at 0.05 (agreement is not accuracy,
LESSONS.md "Look-alike pass"; no figure below 5% is claimed as reader error).
Scoring (unchanged scripts, no edits): king2/king2_score.py on (a) L01-L10 (king4/c258_L01-L10.tsv), (b) L11-L25 band (king4/c258_L11-L25.tsv),
(c) joint L01-L25 (ciphertext_c258.tsv after the fold), each `--noise r --out king4/results_<x>.json`; same statistics (run, lm), same null
(20 value-shuffled keys, seed as in the script, p95), same f.138 positive control at each file's own keyed N, same gate (control window 1
passes AND target beats null on both AND target >= range minimum on both). S bar: king2/king2_grade.py on the joint file, threshold
max(shuffled-key max run, 42); MONL-KING3's joint bar was 53.
Registered decision: if no run clears the S bar after the fold, the king letter (f.133) is parked at D1 (fragments read) pending the owner's
sign sort (tools/sign_sorter.py on the K39|K19, K61|K38, K12|K04 tiles in king4/focus.tsv); no further machine pass on it. If a run clears
the bar, its tokens are S, the gate results are reported as they fall, and the next step is the rule-7 re-derivation and a verifier.
If ciphertext_c258.tsv changes: decode_key.py . --check regenerated, judge re-run and pasted (FAIL reported as FAIL).

## Decision
Belief: the f.133 miss under the clean f.138 range is transcription error on known look-alike pairs (MONL-KING3: band lm above its 13%-noise
control median), so settling the split tiles should raise run and lm.
Would change it: after the fold the band still sits below the f.138 range minimum on both statistics and the longest run does not move
(within +-3 letters of 43), with the control passing at the new noise level -- then the error is not on the split tiles (or not on them alone).
Observed: <pending>
Decision: <pending>
Lesson: <pending>
