LANE SALV2 JOB 1 -- code+mark transcription of the 98 SALV-SPLIT-confirmed boxes, fr2933-salviati-1525.
Written 27 Sept 2026 by LANE SALV2 orchestrator (Opus, session_01288kYmmNxAqAedKtgvxyD1) from the 01:58 UTC clock read.
Sonnet worker. Two workers share this brief; your prompt says whether you are WORKER A or WORKER B.

  WORKER A: f54r (12 boxes) then f54v (30 boxes) -- 4 subagent calls + 2 reconciliation units.
  WORKER B: f55r (31 boxes) then f56r+f56v together (19 + 6 = 25 boxes; one call covers both leaves) -- 4 calls + 2 units.

Cap USD 18, box 75 minutes, per worker. Per-unit pricing (CLAUDE.md Usage 6): 1 unit = one blind Sonnet subagent call on
one leaf's per-box crops, estimated USD 4 (SALV-SPLIT's full-line-crop calls cost about 5.5 each; per-box crops are
smaller); 1 reconciliation unit per leaf, about USD 1. Planned: 4 calls + 2 units = about 18. You cannot see your own cost;
the orchestrator reads get_session every 15 minutes and will interrupt you if the dollar figure crosses 80 percent of the
cap. You enforce the time line: do not START a subagent call after minute 60 of your box; if you stop early, say which
leaf/pass is left in your done line.

Start: `date -u`; `python3 tools/room.py --start`; read the last 30 lines of ROOM.md; append a claim line with
tools/room.py ("LANE SALV2 worker SALV2-J1A|J1B (Sonnet)", naming your leaves and files). Read, and nothing else in full:
ciphers/fr2933-salviati-1525/NOTES.md sections "SALV-SPLIT" and "bSALC"; `.claude/briefs/README.md` common-tail bullet
"Marks and numerals as drawn"; the head docstrings of crop_plain_leaf.py and regen_images.sh.

WHICH BOXES. The 98 confirmed boxes are the rows of `ciphertext_<leaf>.split-candidate.tsv` whose grade ends
`|split-candidate` (f54r 12, f54v 30, f55r 31, f56r 19, f56v 6). Take ONLY (line, pos) from those rows. Their `code` column
is SALV-SPLIT's one-pass guess: a "pass 0" of unknown grade. Never show it to a subagent, never use it as a pass, never
use it to settle a disagreement. You may report, after reconciliation, how often it agrees with your result.

STEP 1, crops (paste every command and its output summary into NOTES.md before the first subagent call).
 a. Renders (not committed; `.gitignore`d already). gallica.bnf.fr only, at most 7 requests, >=2 s apart, browser UA,
    one retry after a pause on a reset, never a loop:
    WORKER A:  `bash regen_images.sh page src_ark_12148_btv1b90600674_f55_4085_0_4086_5513.jpg`   (f54r native crop)
               `curl -sS -A "Mozilla/5.0" "https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f56/pct:0,0,50,100/2400,/0/default.jpg" -o images/f54v_ref2400.jpg`
    WORKER B:  `curl ... f56/pct:50,0,50,100/2400,/0/default.jpg -o images/f55r_ref2400.jpg`
               `curl ... f57/pct:50,0,50,100/2400,/0/default.jpg -o images/f56r_ref2400.jpg`
               `curl ... f58/pct:0,0,50,100/2400,/0/default.jpg -o images/f56v_ref2400.jpg`
    (run from ciphers/fr2933-salviati-1525; same URLs as SALV-SPLIT U0; check each is a JPEG, not HTML.)
 b. `python3 crop_plain_leaf.py <leaf>` for each of your leaves (line crops; box counts must match SALV-SPLIT's
    139/152/173/171/207 for f54r/f54v/f55r/f56r/f56v).
 c. Per-box crops: the orchestrator added `--boxes LIST.tsv --out DIR --seed N [--leaf-col]` to crop_plain_leaf.py
    (see its --help; smoke-tested on a synthetic render). Build LIST.tsv (leaf, line, pos) from the confirmed rows, then
    `python3 crop_plain_leaf.py <leaf> --boxes split2_<leaf>_list.tsv --out split2_crops/<leaf>_A --seed <sA> --leaf-col`
    and again with `_B` and a different seed. The id -> box key lands beside DIR (split2_crops/<leaf>_A_key.tsv), never
    inside it; give a subagent only DIR's paths. Worker B passes f56r+f56v in one list (leaf column) under the name f56rv.
    Crops carry context and a blue box round the target only. Eye-check two crops yourself before the first call; if the
    context or headroom is wrong for this hand, fix the option (docstring kept current), do not fork a private copy.

STEP 2, two blind passes per leaf (f56r+f56v is one "leaf" for calls). Each pass = ONE subagent call (model sonnet)
given ONLY: that leaf's shuffled crop paths for that pass's seed; glyphs/atlas_part1.png and glyphs/atlas_part2.png;
the code list and shape descriptions from glyphs/labels.json ("desc"), and the mark vocabulary with its descriptions from
labels.json "mark_desc" (~ dot 1 5 o 7 ot # +; several marks on one sign are joined with `|`, as in ciphertext_*.tsv);
nothing about flags, plain/sign status, prior guesses, or hypotheses. Ask, per crop id: `code` (an atlas code name, or
`?` if none fits; name the nearest atlas code in a note if you choose `?`), `marks` as drawn above the boxed sign, in
its own column (blank if none; never folded into the code), `conf` (H/M/L), `note` (shape words). If a box holds a
plain-Italian word rather than a sign, answer code `WORD` -- do not force a code. Output TSV: id, code, marks, conf, note.
If a reply comes back short, one follow-up message listing only the missing ids (SALV-SPLIT precedent), not a new call.
Pass B's call is fresh (a new subagent), never a continuation of pass A's.

STEP 3, reconciliation (1 unit per leaf). Map ids back to (line,pos); write passA_split_<leaf>.tsv and
passB_split_<leaf>.tsv (long format: line, pos, sign, conf, marks); run `python3 tools/reconcile_passes.py
passA_split_<leaf>.tsv passB_split_<leaf>.tsv --rows --out-dir recon_split_<leaf>` (or, if --rows does not fit the
per-box shape, compare by (line,pos) key in a few lines of Python and say so). Then YOU settle every disagreement
from the crop (code and marks separately): grade `AB` where both passes agree on code and marks; `M` where you settled
it from the crop (write how in a `how` column of recon_split_<leaf>/settled.tsv); code `?` where undecidable (grade M).
A box both passes call WORD stays plain (`_`), and say so -- it counts against SALV-SPLIT's confirmation.
SALV-SPLIT's `O` guess at f56r line 19 pos 20 (not in the 36-code inventory): resolve it from the atlas plates on the
crop, or grade `?` (WORKER B).

STEP 4, write back (rule 7 inputs; do NOT run build_spec.py -- job 2 does). For each leaf, update the REAL
`ciphertext_<leaf>.tsv` in place, only at the confirmed (line,pos) rows: code, marks, grade (`AB`/`M`, with `|split2`
appended so the rows are traceable, e.g. `AB|split2`); the `_` plain marker replaced. The 39 unconfirmed flagged boxes
stay plain; every other row byte-identical (check with `git diff --stat` and a row-count diff). Do not touch the
`.split-candidate` files, the spec, ciphertext.txt or ciphertext_with_plain.txt.

REPORT (NOTES.md section "SALV2-J1<A|B>: code+mark transcription of the confirmed boxes (27 Sept 2026, LANE SALV2)",
compact): commands pasted; per leaf: boxes, pass A/B agreement on code, on marks, on code+mark (the transcription control,
beside bSALC's 6.4 percent per-sign measured error), grades AB/M/?, WORD count, pass-0 agreement with the settled code;
the `O` resolution (B). Commit: passA/passB_split TSVs, recon_split_<leaf>/, the updated ciphertext_<leaf>.tsv,
crop_plain_leaf.py, the crop key files, NOTES.md -- not the renders or crop PNGs. `git diff --stat` before commit;
`python3 tools/file_shrink_guard.py` on every file you touched; push only via `python3 tools/room.py --push <paths>`.
Done line through tools/room.py starting "done: for LANE SALV2 --" with the agreement figures, request count per host,
and anything left. Then stop.

Rules: no decoding, no family run, no reading, no grades above M except AB for agreement (no H/C/S), no "solved", "new",
"first", "unpublished"; no host but gallica.bnf.fr; never print or commit credentials; never call AskUserQuestion;
never write the owner's name. If this brief conflicts with CLAUDE.md, CLAUDE.md wins -- say so in ROOM.md.
