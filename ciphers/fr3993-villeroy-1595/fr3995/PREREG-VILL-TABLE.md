# PREREG VILL-TABLE (3 Oct 2026, committed before any new fr.3995 canvas is viewed)

Worker A1-VILL-TABLE (account 1), brief .claude/briefs/runs/2026-10-03-acct3-a1-wave7.md job 3, VILL-NOMEN next step (h).

Candidates (Tomokiyo, sources/cryptiana/web/nevers.htm, French tables 1592-95 with figures AND symbols, not in Bourdeau's
checked set 60/65/66/68-76 and not viewed by VILL-KEYS/STRIPS/7280/NOMEN): no.44 f.82 (Jan 1592, Gisors), no.45 f.84
(Aug 1592, Camp Provin), no.52 f.92 (Nov 1592, Corbeil), no.57 f.102 (Feb 1593, La Verriere). Canvases from the manifest
labels (tools/gallica_folio.py btv1b525085665): f161 82r, f162 82v, f165 84r, f166 84v-85r, f179 92r, f180 92v,
f196 102r, f197 102v. Spanish/Italian/Mayenne-intercept tables (nos.47-51, 53-56, 59, 61-64, 67) are out of scope.

Vision budget: 3 calls. Call 1 = one contact sheet (iiif_lines --debug overviews at 1600 px) to LOCATE: a table is a
"family candidate" only if, on the sheet, it shows figure codes in the alphabet AND at least 2 of pi, varpi, theta,
infinity as cipher signs. If none is a family candidate: log "no 1592-93 French figure+symbol table among nos.44/45/52/57
carries the target's pi/varpi/theta/infinity at overview resolution" (a search result, M) and stop; no crops, no reads.
Calls 2-3 (only for the single best family candidate) = native line crops via iiif_lines of only the alphabet rows
holding pi/varpi/theta/infinity/tau/reversed-c, read blind twice: reader A (worker) and reader B (Sonnet subagent, not
told A's answer), each comparing the crop with the committed target stack images/f148r_ct_stack.jpg.

Certification rule: a target sign (P pi, V varpi, Q theta, W infinity, T tau, R reversed c) is CERTIFIED to the table
value only if BOTH readers call it SAME (as VILL-SIGNS/VILL-NOMEN) and both read the same plaintext letter (or "null")
for it. LIKE or one-reader-only = not certified. No reading of the target is committed from this job; any certified
signs go to keys/ as M and the power re-run is a later job (signs_score.py method, gate 16/20).

## Addendum A1B-VILL-57-44 (3 Oct 2026, ~17:05 UTC, committed before any crop of f162/f198-f200 is viewed)

Brief .claude/briefs/runs/2026-10-03-acct1-a1b-vill-57-44.md, steps (k) then (j). Same certification rule as above
(both readers SAME + same plaintext value, else not certified; certified signs go to keys/ as M only).

(k) no.44 f.82v (canvas f162): native crops via iiif_lines of the right-hand symbol column (and the lower names block if its
symbols fall in the same crop). Call 1: reader A (worker) looks at the crop beside images/f148r_ct_stack.jpg and lists, per
table symbol, SAME / LIKE / NO against the target signs P pi, V varpi, Q theta, W infinity, T tau, R reversed c, L lambda,
w, +, K. Only if A calls at least one SAME is call 2 spent: reader B (Sonnet subagent, blind to A) does the same. A sign
called SAME by both, with both reading the same table entry for it, is certified at M (here a symbol means a word/name code,
so a certified value is a code meaning, not a letter). Otherwise log "no target sign among no.44's symbols at native
resolution" (search result, M).

(j) no.57: one overview call on canvases f198-f200 (iiif_lines --debug reference copies, tiled) to locate the table. It is a
family candidate only on the original rule (figure codes in the alphabet AND at least 2 of pi/varpi/theta/infinity). If a
candidate: native crops of the rows carrying those signs, read blind twice (A worker, B Sonnet subagent) as above. Scoring
(power check rank 1 of 201 with 20 synthetic French texts; coverage < 0.5 = "not testable") is run only if signs are certified
and the resulting key covers >= 0.5 of the target; otherwise no score is computed.
Vision budget for this job: at most 5 calls total; stop before any call that would cross 80 pct of USD 8 or of the 50-min box.
Tool shelf: glyph_atlas.py (proven) not used -- a dozen table symbols against ten target signs is one visual comparison, not a
segmentation/clustering job.
