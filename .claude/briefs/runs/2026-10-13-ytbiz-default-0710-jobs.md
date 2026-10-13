# LANE DEFAULT-account-2-20261013-0710 jobs (account 2, lane orchestrator session_01BEZndkMNpPo1xSNoWRDks9) -- 13 Oct 2026 07:2x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 07:10-17:10 UTC 13 Oct (80% line 15:10). Gate 0a: SESSION-SWEEP-account-2
stale-claimed since 5 Oct, proceeded as every incarnation since 9 Oct. Backlog read 07:1x UTC: VERIFY-BACKLOG high rows Birago (off
limits), low rows audit2 on N0/N1 (gate 2 n/a). `next_steps.py --hot-only` runnable rows, minus what LANE DEFAULT-A1-0640 (baluze167,
fr5160, colbert26, fr4712, fr3993) and LANE BNF-FOCUS (fr3622, fr3986, fr3985, fr3987-3990 key no.60 family, fr3613) hold; eckert-1864
and thurloe Verbael wait on googleapis (503 at 07:2x UTC, one probe). Exclusions as default-lane.md step 1.
Intake gate 07:2x UTC (tools/intake_gate_check.py, exit 0 each): thurloe-printed partial, na-suriname-map-1781 partial,
la-garde-1577 open, lodewijk-van-nassau-1573-74 partial.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A2-0710 (account 2)"; the hosts named in your own job replace that file's
"Hosts this wave" bullet. Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before).
`get_session` is not available to you: say "cost not visible to this session" in the done line.

## Wave 1 (07:2x UTC 13 Oct)

### THUR-51 (Opus, cap 3, box 75 min, archive.org "IA" take/release, <= 25 requests): thurloe-printed, code 51 witness, then 45/87
NOTES.md "## Remaining gaps (THUR-198, 12 Oct 2026)" items 3 and 4 and Escalation "[ ] image-check". Step 1 (~1.5): image Birch vol 4
l.10355 (the remaining 1655 Bamfylde letter whose OCR shows 51; identifiers and leaf-fetch route as THUR-198 used them, see its section),
crop the cipher runs with printed glosses, one blind subagent read of the run(s) carrying 51 (strip crops only), and record the printed
value at 51 beside the existing witnesses (vol 4 p.195 e x2, p.306 i, Tomokiyo i) in HYPOTHESES.md. Change key values only if the gate
THUR-198 used still PASSes and the evidence is a printed gloss; otherwise log it. Step 2 (~1.5, only if step 1 left room under 80%):
scan the Birch vol 7 djvu text (script, not a model) for 1658 Bamfylde runs carrying 45 or 87 with printed glosses; image at most one leaf
and read it as in step 1. Units: 2 leaf fetch+crop, 2 vision calls. Rule 4 grades; any decode `--check` the folder has must pass.

### V-SUR2046 (Opus verifier, cap 2.5, box 60 min, disk only): na-suriname-map-1781, check of SUR-2046's 16 M relabels
You are a verifier, separate from the SUR-2046 solver session; do not protect its conclusions. NOTES.md "## SUR-2046" (l.4024 ff.) and
`passes/signcmp_sur2046/` (prereg.md, result.tsv, decisions.tsv, apply.py). The control passed at the bar exactly (14/20, gate 14). Task:
(1) audit the call -- were the 20 control tokens and the 31 targets drawn from comparable crops (same hand, same crop scale), and was
#30's wrong settle (o -> sigma) handled the same way for [o-flag] and for any relabel whose winning tile is a near look-alike of another
value; (2) one independent blind re-call of the 16 relabelled tokens with a FRESH control set (different seed, 20 H tokens not used by
SUR-2046, same gate and settle rule, pre-registered in PREREG-V-SUR2046.md pushed before the call); (3) verdict per relabel: stands at M,
or reverts to U (remove its row from exceptions_nieuw_image.tsv). If the fresh control misses its gate, no relabel is confirmed and the
verdict is "unconfirmed, held at M pending a stronger instrument" -- do not revert on a failed control. Write an "## V-SUR2046" section in
AUDIT.md (create the section if AUDIT.md lacks one; no N-class change), update NOTES.md Remaining gaps if counts change, decode `--check`.
Units: 1 audit read, 1 vision call, 1 reconciliation.

### LAG-HIRES (Opus, cap 3, box 75 min, resources.huygens.knaw.nl "huygens" take/release, <= 6 requests): la-garde-1577, native-res 6179
NOTES.md "## Remaining gaps (LAG-CHECK, 9 Oct 2026)" items 1 and 3: the 16 LAG-MARKS doubt cells and the two `10`/`18` cells (p2L26.6,
p2L27.13) are resolution-limited at the 150-dpi render. Step 1: get the WVO PDF `resources.huygens.knaw.nl/media/wvo/images/06000-06999/
06179.pdf` (use the copy on disk if present), and measure its embedded image resolution (`pdfimages -list`, or PyMuPDF). If the embedded
scan is not materially above the 150-dpi render (under ~1.5x linear), stop: record that the WVO PDF cannot settle these cells and name the
KHA original (needs-physical-access / reproduction) as the only route in Remaining gaps. Step 2 otherwise: extract pp.2-3 at native
resolution, crop the 18 cells (strip crops with a few cells of context, iiif_lines.py --image for the lines), one blind subagent read of
the 18 cells (two candidate values per cell shown unlabelled where LAG-MARKS gave them), settle by eye, then re-measure the marks-kept
error the way LAG-MARKS did and say which side of 0.107 / 0.125 it lands. Carry settled cells into the transcription with a provenance
column (never silently repaired), re-run the folder's --check scripts. Do NOT re-run any family (wordcode/syllabary are [retired] at
these error levels); if the measured error falls clearly below 0.071, name the re-test as the next step with a price. Units: 1 fetch/
extract, 1 crop job, 1 vision call, 1 reconciliation.

### LVN16-3R (Opus, cap 3, box 75 min, disk only): lodewijk-van-nassau-1573-74, 4616 remainder third read
NOTES.md "## Remaining gaps (finish-or-blocker pass, 2 Oct 2026)" item 3 ("4616 remainder: 15 M rows and 22/112, 33/5, 25/81, 27/16,
92/2, next a per-token zoomed third read, ~$2") and the R12-LVN16 / R12-LVN16R sections (`lvn16/`, 300-dpi images on disk). One zoomed
crop per token (tight + one-token context), one blind subagent read of all 20 tokens (code values shown as candidates only where R12-LVN16
already listed them, unlabelled as to which pass gave which), plus 10 H control tokens from the same page mixed in blind (gate >= 8/10 on
the known value, pre-registered in PREREG-LVN16-3R.md pushed before the call). Settle only tokens where the read agrees with one of the two
earlier passes and the control passed; regrade per rule 4 (M -> H only where key_full gives the value and the image is now sure), re-run
the reading scripts with `--check`, recount the "Read so far" line. Units: 1 crop job, 1 vision call, 1 reconciliation.

## Wave 2 (07:3x UTC 13 Oct) -- openapi.bnf.fr jobs
Hosts: **openapi.bnf.fr only** (IIIF Image API v3; gallica.bnf.fr/iiif is 403 -- do not use it). URL form
`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<canvas>/<region>/<size>/0/default.jpg` (region `full`, `x,y,w,h` or
`pct:x,y,w,h`; size `max`, `1600,`, `pct:50`); `info.json` once per canvas for the native size; `tools/iiif_lines.py` and
`tools/gallica_folio.py` now take `--iiif-host openapi` (IIIF-HOST, 17483295). Descriptive User-Agent; one request at a time, >= 3 s
apart; <= the per-job count below; post `openapi.bnf.fr take` / `openapi.bnf.fr release` ROOM lines around each batch, and if any worker of
any lane holds it (a take with no release in the last 30 min), work from disk and wait. On 403/429/5xx or a challenge: one retry after
60 s, then stop the host, log it, finish from disk or stop. Save every fetched region under the folder's `images/` with a manifest entry.

### BAL103-189 (Opus, cap 6, box 100 min, openapi.bnf.fr <= 10): baluze103-letellier-marca-1644, f.189r vs its period decipherment
NOTES.md "## While waiting (9 Oct 2026, WAIT-PASS-5)" item 1 and the f.171r calibration it extends (R7C-BAL103K and later sections): f.189r
(Baluze 103, ark btv1b9001389d; canvas from the folio offset recorded in NOTES.md, or `gallica_folio.py --iiif-host openapi --folio 189`)
carries a period decipherment and more known-value 9s than f.171r's six. Steps: fetch the cipher + decipherment region at native size, cut
line crops, two blind passes of the cipher signs (one Sonnet subagent call per pass, half page each if long) using the f.50 sign names,
one reconciliation; read the period decipherment once (transcription, not a gloss to be scored); PREREG-BAL103-189.md pushed BEFORE
alignment: the per-sign test of Tomokiyo's table against the decipherment (statistic and shuffled-alignment control as R7C-BAL103K ran
it on f.171r), and the count k_i / k_r / k_s of 9s aligned to each letter, with the decision rule for the 9 shape split stated in advance.
Report the table cells confirmed / contradicted. No key.tsv edit except cells the pre-registered gate licenses; f.50's sorter-bound gaps
stay as they are (the owner's pass). Units: 1 fetch+crop, 2-4 pass calls, 1 reconciliation, 1 alignment/scoring at ~1.5 each; if after
the reconciliation the cap cannot cover the alignment, push the transcription and stop with the test as the next step.

### SYL-NOM (Opus, cap 6.5, box 110 min, openapi.bnf.fr <= 10): fr15575-syllabic-1592-95, the no.54 key nomenclator
NOTES.md "## Remaining gaps (D4-15576, 6 Oct 2026)" item "key nomenclator and no.31" and Escalation "[ ] known-keys": BnF fr.3995 (ark
btv1b525085665) no.54 = canvas f188 (f.96v-97r); NV05B transcribed only the syllabary and header signs (key_no54.tsv). Fetch canvas f188
region y 1600-6055 at native size (check info.json first), cut 4-6 band crops with iiif_lines.py (paste the command and output, check the
debug overlay), two blind passes of the nomenclator (code -> word/name entries) and one reconciliation (`tools/reconcile_passes.py`).
Write `key_no54_nomenclator.tsv` (code, entry, conf, pass A, pass B, settled-by) beside key_no54.tsv -- a period key sheet, so entries are
H where both passes and the image agree, M otherwise. Then the cheap check the gap names: do fr.15576 f.2's 3-digit codes fall inside the
nomenclator's code range and format (count, list; no reading claimed, no decode of f.2 unless the existing decode config already reads
key files by name -- then `--check` only). Do NOT start no.31 (canvas f126) in this job; name it as the next step with its price.
Units: 1 fetch+crop, 2-4 pass calls, 1 reconciliation at ~1.5 each.

## Wave 3 (07:4x UTC 13 Oct) -- follow-ups of waves 1-2
Pricing lesson from waves 1-2 (V-SUR2046 4.60 on 2.5, LVN16-3R 4.71 on 3): a verifier re-call with its own fresh control set, or a
re-render the brief assumed was on disk, is a full extra unit; caps below include it.

### V-LVN16 (Opus verifier, cap 3.5, box 60 min, disk + <= 1 huygens request): lodewijk-van-nassau-1573-74, carry LVN16-3R into AUDIT.md
You are a verifier, separate from the LVN16-3R solver session; do not protect its conclusions. Read the LVN16-3R section of NOTES.md, its
PREREG (92e86face) and its ROOM flag (07:31 UTC 13 Oct). (1) Eye-check the four rows it named -- p1_L16/19 (81 eye vs 91, third blind read
91), p1_L07/8, p1_L16/4 (its crops were off-token), p1_L13/11 (27/16 vs 21/16 vs read 27/6) -- on tight crops you cut yourself from the
300-dpi render (`regen_images.sh` or the 04616.pdf route LVN16-3R used; one huygens request at most, take/release); revert any settle the
image does not support. (2) Carry the revision into AUDIT.md ("## V-LVN16" section: what changed, the new counts, depth per rule 4a re-checked
against tools/depth_check.py, no N-class change unless a sentence over-claims), and into any SECOND-OPINIONS-QUEUE.tsv row for this target.
Re-run the reading scripts with `--check`. Units: 1 crop job, 1 eye pass, 1 write-up.

### SUR-ALIGN (Opus, cap 4.5, box 90 min, disk only): na-suriname-map-1781, 2046 legend a-k vs crib_2042
NOTES.md Verdict "cheapest next" and Escalation clear-pages "Not yet used: crib_2042 against 2046 legend a-k" (l.4087), plus the V-SUR2046
note (l.4100 ff.): the alignment is the named instrument for [d-hook] and [3-breve], now back at U. Read GAPS5/6 (crib_2042 vs 2039, the
method and its controls) and GAPS18 (the 2046 legend transcription). PREREG-SUR-ALIGN.md pushed BEFORE any score: statistic, a label-shuffle
control (crib entries permuted across legend letters) and a value-shuffle control (key values permuted within the Nieuw alphabet), both able
to differ from the target on the statistic (rule 3, check it in the PREREG), gate, and the decision rule for any U/M token the alignment
would assign. Use tools/interlinear_align.py if its model fits (do not write a private DP). Grade per rule 4: a PASS licenses at most C for
legend words whose crib entry is a period gloss, M otherwise; FAIL changes nothing. decode `--check`; update Remaining gaps / Escalation.
Units: 1 setup + PREREG, 1 alignment run with both controls, 1 write-up.

### BAL103-200 (Opus, cap 5, box 90 min, openapi.bnf.fr <= 10): baluze103-letellier-marca-1644, f.200 and/or f.230 vs period decipherments
NOTES.md Verdict (l.942): "f.200/f.230 (DECODE R2745/R2746) for an i-valued 9 is optional while waiting, ~$4"; BAL103-189 (13 Oct) left the
9 shape split a NON-TEST at pooled N 9 with k_i 0. Same design as BAL103-189 (read its section and PREREG-BAL103-189.md; reuse its scripts):
f.200 first (canvas from the folio offset BAL103-189 used), one native region, 2 blind passes + reconciliation, PREREG-BAL103-200.md pushed
before alignment (the per-sign table test and the 9 counts pooled with f.171r + f.189r, decision rule stated in advance, including what N
makes the split test a real test). f.230 only if f.200 leaves room under 80% of cap and box and the pooled N is still below that bar.
No key edit unless the pre-registered gate licenses it. Units: per leaf 1 fetch+crop, 2 pass calls, 1 reconciliation+alignment.
