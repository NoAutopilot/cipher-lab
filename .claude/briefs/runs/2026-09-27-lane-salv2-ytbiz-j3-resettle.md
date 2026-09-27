LANE SALV2 JOB 3 (reserve) -- re-settle f55v and f56v's plain-Italian boxes from the image, blind, against a matched control.
Written 27 Sept 2026 by LANE SALV2 orchestrator (Opus, session_01288kYmmNxAqAedKtgvxyD1). Sonnet worker. Cap USD 14, box 60
minutes. Units: 2 blind subagent calls on line crops (one per leaf, about USD 5.5 each, SALV-SPLIT's ledger rate for line-crop
calls) + 2 reconciliation units (about 1 each) = about 13. Do not START a call after minute 45; the orchestrator reads your cost
every 15 minutes.

Why: the LANE SALV handoff's still-open (b). SALV-PLAIN1/2 settled f55v's and f56v's plain-word disagreements by pass
confidence, not from the image (NOTES.md "SALV-PLAIN1", "SALV-PLAIN2": f56v 106 disagreements, f55v's in
recon_plain_f55v/disagreements.tsv). plain_boxes.tsv grades on these leaves: f55v A 79 / R 24 / M 62; f56v A 100 / R 69 / M 37.
(f55v carries no [C] flag at all, so SALV-SPLIT never covered it; f56v's 6 flagged boxes were checked there.)

Start: `date -u`; `python3 tools/room.py --start`; last 30 lines of ROOM.md; claim via tools/room.py ("LANE SALV2 worker
SALV2-J3 (Sonnet)"). Read only: NOTES.md sections "SALV-SPLIT", "SALV-PLAIN1" (its f55v part), "SALV-PLAIN2" (its f56v part),
"SALV2-J2" (if present); crop_plain_leaf.py --help.

Design (SALV-SPLIT's, rule 3). Per leaf: TARGET set = every plain box whose grade is R or M (the confidence-settled and unsettled
rows; f55v 86, f56v 106). CONTROL set = an equal-size uniform random sample (seed 20260927 + leaf index, recorded) of that leaf's
A-graded rows (both passes agreed) -- if the leaf has fewer A rows than target rows, take all A rows and say so. Both sets go to
the reader unlabelled and interleaved.

1. Crops (paste commands before any call): renders at most 2 gallica.bnf.fr requests, 2 s apart, browser UA:
   `curl -sS -A "Mozilla/5.0" "https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f57/pct:0,0,50,100/2400,/0/default.jpg" -o images/f55v_ref2400.jpg`
   `curl -sS -A "Mozilla/5.0" "https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f58/pct:0,0,50,100/2400,/0/default.jpg" -o images/f56v_ref2400.jpg`
   then `python3 crop_plain_leaf.py f55v` and `python3 crop_plain_leaf.py f56v` (line crops; every plain box underlined and
   numbered, so the sampled boxes are indistinguishable from the others). Never a full-leaf image to a subagent.
2. One blind Sonnet call per leaf: only that leaf's line crops + glyphs/atlas_part1.png/atlas_part2.png; for each listed
   (line, pos) -- target and control interleaved in line order, no labels, no prior readings -- answer verdict
   (word / sign / mixed / blank) and, for a word, the word as written (abbreviation marks kept as drawn: a tilde or stroke is
   written, not expanded), conf H/M/L. One follow-up message for missing rows, not a new call.
3. Reconciliation unit per leaf: control agreement = share of control rows where the fresh read matches the agreed A reading
   (normalize both to one convention first: lowercase, u/v and i/j folded, abbreviation marks compared as marks -- CLAUDE.md rule 3,
   PX-BRODEC); that figure is the fresh reader's reliability on this leaf. Target rows: where the fresh read matches pass A or
   pass B, take it (grade `R3`, 2-of-3); where it matches neither, settle from the crop yourself (`R`, say how) or keep `x|y`
   (`M`). Report the share of target rows the fresh read called sign against the control's sign share (the SALV-SPLIT table
   shape) -- a clear excess names more split candidates on these leaves; list them, do not write them into ciphertext_*.tsv.
4. Write: update plain_boxes.tsv (and plain_f55v.tsv / plain_f56v.tsv if that is where the settled words live -- follow the
   existing build path) for the re-settled rows only; `python3 build_ciphertext_with_plain.py` and its `--check` exit 0;
   `python3 build_spec.py --check` must still exit 0 (the spec is untouched: plain words do not enter it). NOTES.md section
   "SALV2-J3: f55v/f56v plain boxes re-settled from the image (27 Sept 2026, LANE SALV2)": commands, per-leaf control
   agreement, target settled counts by grade, sign-share table, split candidates listed. `git diff --stat`; file_shrink_guard
   on every touched file (paste); push via `python3 tools/room.py --push <paths>`. Done line "done: for LANE SALV2 --" with the
   control and target numbers, request count per host. Then stop.

Rules: no decoding, no family run, no reading of signs; never "solved", "new", "first", "unpublished"; no host but
gallica.bnf.fr; never print credentials; never AskUserQuestion; never the owner's name. CLAUDE.md wins over this brief.
