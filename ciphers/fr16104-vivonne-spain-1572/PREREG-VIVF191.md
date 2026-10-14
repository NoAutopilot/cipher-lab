# PREREG-VIVF191 -- f.191r (ink 63) re-cut, four-pass reconciliation, re-decode (14 Oct 2026, 02:2x UTC by date -u)

Job VIV-F191 (account 4, for LANE VIV-KEYSTONE; brief .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md "Wave 5").
Written and pushed BEFORE any transcription pass, decode or statistic of this job. Measurement only: key.tsv,
reading_piece63.tsv, status.json and every committed reading are not changed by this job.

## 1. Crop recipe (fixed)
- Source: fr.16105 canvas 196 (f.190v | f.191r), native region `5020,540,2760,4400` (N6-VIV63's f.191r region), one request to
  openapi.bnf.fr (IIIF v3), cached locally; any re-cut works from the cached file (`--image`), no further request.
- Command: `python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 196 --iiif-host openapi --region 5020,540,2760,4400
  --out <scratch>/p63f191 --prefix c196_f191r_dr --deskew-region --distance 70 --max-width 1600 --overlap 150
  --band-extent 0.1 --mask-neighbours --debug` (`--deskew-region` with no DEG = the read-free fitted angle; option added by
  this job to tools/iiif_lines.py with tools/tests/test_iiif_deskew_region.py).
- Acceptance (debug overlay, by eye, before any pass): 36 bands, one per written line, no band centred between two lines.
  If it fails, ONE re-cut is allowed from the cached file (a given angle and/or `--centres` by eye), recorded with its reason; if
  that fails too, stop before any pass and report.

## 2. Passes
- Two fresh blind Sonnet passes, C and D, one call each for the whole page's crops (crop paths only, never the region image),
  prompt = tx/SIGNS.md + "segments s1/s2 of a line overlap ~150 px: write the overlapping signs once", output `row<TAB>codes`.
  Readers see no key, no decode, no earlier pass.
- The existing passes A and B (tx/f191r_passA.tsv, tx/f191r_passB.tsv, N6-VIV63 first-cut crops) are kept as they are.
- All four cleaned with tx/viv63_clean.py's rules (DUP rows, [PLAIN:], [...] removed; pi -> P; "Il non" removed).
- Line mapping: new band Lnn <-> old row Lnn. Check: for each line the NW agreement of pass C with A at the same id must exceed its
  agreement with ids +-1; if that holds on >= 32 of 36 lines the id mapping is used; otherwise each new line is mapped to the old
  id with the highest agreement (recorded per line).

## 3. Reconciliation rule (fixed)
`tools/reconcile_passes.py A B C D --vote` (A reference, NW). Per aligned column, votes over the four passes ('-' = no sign
is a vote):
- >= 3 of 4 the same sign -> that sign, settled; >= 3 of 4 '-' -> no token.
- 2-2 between two signs whose pair is in tx/viv63_decode.py RULES (reconcile_vivk RULES + RULES54 + RULES63) -> the rule's sign,
  settled.
- anything else (2-2 other pairs, 2-1-1, 1-1-1-1, 2 signs vs 2 '-') -> the plurality sign (ties: the sign of the pair C=D if they
  agree, else A's; a '-' plurality drops the column only when it is a strict plurality) and the token is FLAGGED (grade M).
- "o o" -> "oo" and the label MAP as tx/viv63_decode.py.

## 4. Decode and grades
key.tsv as committed at this PREREG's commit; grades as tx/viv63_decode.py: U code not in key.tsv; M flagged token or key grade M;
H otherwise. Written to tx/viv63_f191/ only (not reading_piece63.tsv).

## 5. Statistics (all reported; "before" = the committed f.191r rows of reading_piece63.tsv / tx/rec_f191r, "after" = this job)
(a) err_2reader = 1 - agreement (tools/reconcile_passes.py, NW) for each of the 6 pass pairs; before A-B 0.156 (N6-VIV63).
(b) Longest all-H run on the page, across line ends (AUDIT 2's measure, tx/vivanchor_gates.py runs()): before / after.
(c) Gates on the page under seed `20261014VIVF191` (tx/viv63_test.run and tx/vivanchor_gates.wrong code paths): b2 vs 200
    letter-order shuffles (p99), with controls C1 f.103r and C2 ink 54 as in vivanchor_gates (control first: a control that fails
    makes b2 "not a gate"); 200 value-shuffled wrong keys, real margin vs wrong-key margin p99. Before and after.
(d) Registered stretch statistic: V_strict (tx/viv53G_decode.strict_vocab) top-1 and top-3-mean stretch on the page (tx/viv53L_stretches
    top(), unread '_' breaks), against 200 letter-order shuffles of the page's letters (unread breaks in place), seed
    `20261014VIVF191-stretch`; before / after; above-null = real top-1 > null p99.
(e) The five longest V_strict stretches after, as decoded text with words, grades per letter, and the M/U/flagged tokens inside them
    (with line, position and crop tile id) -> tx/viv63_f191/owner_questions.tsv.

## 6. Decision wording (fixed in advance)
- "Clears the authentication distance" only for a V_strict stretch of >= 42 letters with every token H (no M, no U, no flagged
  token, no letter repair; word division and v/u, i/j only). Such a stretch goes to the parent as a candidate for a verifier
  (reading_piece63.tsv is not changed here; rule 4a/D2 is the verifier's).
- A stretch >= 42 with any M/U inside: "candidate with liberties, N", listed in owner_questions.tsv, not a clearance.
- Otherwise: "no stretch clears 42 letters with no liberty"; the before/after numbers stand as a measurement.

## 7. Stop rule
Stop at the cap (USD 10), at 80% of the 120-minute box (03:56 UTC 14 Oct by date -u), or when section 5 is written, whichever
first; do not start a pass that would cross 80%. openapi.bnf.fr <= 3 requests (1 planned). No image file into git.
