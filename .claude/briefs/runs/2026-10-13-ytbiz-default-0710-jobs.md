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
