# PREREG MONL-C269A (20 Oct 2026, 08:2x UTC by date -u; account 2, Opus; written and pushed before any c269 fetch, read or score)

Question: is c269 (f.138v, the verso of c268) the cipher of the clear text after c268's end (f.140r L26 "...entendans que l")?
MONL-LEAF's lead (one-pass L01-L02 read, post hoc, not counted) is NOT used: those reads are not re-scored or shown to anyone here.

**Line count.** One overview of c269 (openapi.bnf.fr f269 full/1000,); lines of cipher counted by eye on it, clear closing lines counted apart.

**Crops.** One openapi.bnf.fr native region on f269 covering L01-L10 (plus a margin line), levelled as regen_monll26.sh (rotation from
left/right ink-profile peaks agreeing within ~3 px, centre +-95 px, s1 x 0-1700, s2 x 1400-end), with `tools/iiif_lines.py --debug` run
on the same region for the overlay; every crop is checked by eye against the region before any reader sees it (line on centre, top band
identity). Command pasted in NOTES.md (regen_monlc269.sh).

**Passes.** Two blind passes on the strongest model, one call per 5 lines per pass (4 calls: A L01-L05, A L06-L10, B L01-L05, B L06-L10,
pass B lines in reverse order), the c268e/MONL-LEAF prompt with paths changed; readers see only the ids-only key sheet and the crops.
Reconciliation by rule (agree -> H; split -> settled by the folder's conventions K36/K38/?h_bar/K09/K16 or by eye, M) before any decode
or clear text is looked at for c269. Agreement reported (agreement, not accuracy).

**Statistic (registered).** `c269/score_c269.py` (align_c268.py's DP, scores and folds, key.tsv unchanged): confirm share of keyed tokens
of the reconciled c269 L01-L10 stream aligned (free start and end) against the clear window f.140r:L26 - f.141r:L11 (the clear text from
c268's last aligned line onward). Control: 200 windows of the same letter length placed at random in a word-shuffled copy of the whole clear
letter (shuffle and placement redrawn every draw, seed 2690) -- leaf_score.py's control. Also reported: the same on L01-L05 and L06-L10
apart, the whole-letter alignment span (where the stream lands), and f.139 (c270_text.txt) as an other-letter control.

**Calibration before the c269 read is scored** (on committed c268 tokens, same script): power = c268 L21-L30 against window f.140r:L19 -
f.141r:L11 (its true clear starts near f.140r L19-L20); wrong window = c268 L01-L10 against f.140r:L26 - f.141r:L11. If the power run
fails the gate or the wrong window passes, stop: the instrument cannot decide, log non-test, no grades.

**Gate (as SUP-MONLUC's):** PASS iff the L01-L10 real share is above the control p95 AND 0/200 control draws are at or above it, AND
the whole-letter alignment span starts on f.140r L26 or L27. Otherwise: no grades, no fold into decode.json, the lead stays a lead.

**If PASS:** grades per token (C where the aligned clear letter equals the table letter and the clear word is unbracketed; fills only as
align_c268 FILLS rules; M otherwise; U unkeyed with no fill), c269 folded into decode.json as its own job, `decode_key.py . --check` passing,
target token counts before/after (C/M/U). No key.tsv edit; no c268 token relabelled.

## Decision
(appended after the run, 20 Oct 2026; the gate and decision rule above were pushed at d8b8c1d1f before any c269 fetch)
Belief: c269 (f.138v) is the cipher of the clear text after c268's end (f.140r L26 "...entendans que l")
Would change it: c269 L01-L10 at or below the placed-shuffled-window p95, any of 200 draws at or above it, or the whole-letter span not starting at f.140r L26-L27
Observed: calibration power PASS (c268 L21-L30 0.650 vs p95 0.417, 0/200), wrong window FAIL (c268 L01-L10 0.384 vs p95 0.402, 53/200); pass agreement 252/317 = 0.795; c269 L01-L10 0.509 vs p95 0.422 (mean 0.394, max 0.453, 0/200), span f.140r L26 - f.140v L03, f.139 0.373; L01-L05 0.533 vs p95 0.475 (0/200), L06-L10 0.507 vs p95 0.427 (0/200)
Decision: continue -- gate met; c269 L01-L10 graded and folded into decode.json (job c269); next: c269 L11-L33 in five-line bands
Lesson: c269 L01 (with W:Sepbre) aligns mostly as contradictions and, unrestricted, over clear letters c268 already covers; grade a continuation leaf against the clear text after the previous leaf's aligned end
