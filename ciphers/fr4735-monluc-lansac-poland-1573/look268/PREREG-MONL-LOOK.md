# PREREG MONL-LOOK (11 Oct 2026, written before any re-read; LANE DEFAULT-A1-1840, account 1)

Target: c268 (BnF fr.4735 f.138) lines 1-5, passes/c268_passA.tsv (with MONLUC-RELABEL's 10 K38 relabels = committed
ciphertext_c268.tsv, "passC") vs passes/c268_passB.tsv. Alignment: tools/reconcile_passes.py (nw) -> look268/ciphertext_draft.tsv:
182 columns, 129 agree, 53 disagree (29.1% of columns; 70.9% agreement). K38 is its own label.

Instrument: tools/lookalike_pass.py `windows` (label hidden, candidates alphabetical), one Sonnet subagent call, crops from the
folder's own c268 line bands (images/c268cipher_L0N_s1/s2.jpg, stitched on source x), candidate cells cut from
images/keysheet_monluc1_ids.png (ids only, no values).

Tiles: every column where A and B differ and passC has a sign (split: both labels; single: B has none). Columns where only B has a
sign (A '-') have no passC position: they go to focus.tsv as count questions without a re-read.

Rule (the tool's, fixed): a firm (H/M, not SPLIT) re-read equal to A or B settles the tile at 2-of-3 (re-read label wins);
anything else is UNSETTLED, keeps passC, goes to focus.tsv. Exception fixed here: the 10 tiles MONLUC-RELABEL wrote K38 after the
gated blind sort (MONLUC-BLIND, --try both nulls passed) are not overturned by this 2-of-3 machine vote; if the re-read does not
read K38 there, the tile keeps K38 and goes to focus.tsv as a question for the owner.

Reported: before = A/B column disagreement 53/182; after = unsettled tiles / 182 (the 2-of-3 residual). The residual is
agreement, not accuracy (LESSONS.md "Look-alike pass") and is not a reader-error figure. Echo check: the reader never sees any
tile's own label; a re-read is not a confirmation of passC by construction of the prompt, and the share agreeing with A vs B is
reported.

If any label in ciphertext_c268.tsv changes: score_c268.py and k07_c268.py re-run with --check, judge re-run, FAIL reported as FAIL.
