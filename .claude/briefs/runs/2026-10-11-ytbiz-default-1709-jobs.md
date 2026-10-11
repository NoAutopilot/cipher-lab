# LANE DEFAULT-account-2-20261011-1709 jobs (account 2, lane orchestrator session_015WKywfZ8oP5C4zKcddumib) -- 11 Oct 2026 17:3x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 17:09 UTC 11 Oct - 03:09 UTC 12 Oct (80% line 01:09). No SESSION-SWEEP-account-2
row in WORK-QUEUE.tsv (gate 0a not applicable). Backlog read 17:2x UTC: VERIFY-BACKLOG.tsv regenerated -- Birago rows off limits, the
remaining high rows are eckert-1864 Washington-ledger N1/D1 items (Outreach gate 2 is only for classes above N1; left to the account-1
LEDGER/DEFAULT lanes, as the 05:09 incarnation did). `next_steps.py --hot-only` runnable rows: Gallica answers 403 to manifest and image
API (probed 17:2x UTC), which removes baluze167, fr4712, fr3985 f.143r, fr5160, fr3993, colbert26, gramont, ceppo; hessen-daenemark,
la-garde, lodewijk, hellen (held campaign) and pro3055 have no cheap in-session step. Left: the three jobs below.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE DEFAULT-A2-1709 (account 2)"; the hosts bullet below replaces the one there. Halfway line:
one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session` is not available to you: say
"cost not visible to this session" in the done line.
Hosts this wave: archive.org ("IA": THUR-356 only, >= 1.5 s, <= 40 requests, take/release lines); cryptiana.web.fc2.com (THUR-356 only,
<= 6 requests, cache first: sources/cryptiana/); data.htrc.illinois.edu (RAH-EF only, the one command, one retry after 60 s). PISA-T31 disk
only. No Gallica.

## Wave 1 (17:3x UTC 11 Oct)

### THUR-356 (Opus, cap 2.5, box 70 min): thurloe-printed, Bamfylde code 356 and the code-94 conflict
NOTES.md "## Remaining gaps" (l.3772 on) items "Bamfylde p.160 code 356" and "Code 94 conflict"; Verdict cheapest next. Intake gate (17:2x UTC,
pasted): `thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
Units: (1) grep the on-disk / IA `_djvu.txt` of Birch vol 6 (pp.161-700, the 1657 Bamfylde letters) and the vol 7 index for printed glosses
of codes 350-360 in the First/Second Cipher runs (use bamf/scan_codes_hits.tsv's method; script, not a model read); (2) locate Tomokiyo's
94 = t instance in his thurloe page (cache first) and the Birch page it cites; (3) if (1) gives a gloss for 356 at the same key, check it
against the p.160 context and grade (C only from a printed gloss of the same table; else M). ~3 units at ~0.6. No reading of new letters,
no key edits beyond the 356/94 cells your evidence supports; rule 7: rerun the folder's p.160 decode script with --check after any edit.
Report what was found and where it was not found; do not classify novelty.

### PISA-T31 (Opus, cap 2.5, box 60 min): fr16045-pisany-rome-1585, third blind reader on the UNSETTLED key86 T31 tokens
The folder's Verdict cheapest next (NOTES.md: "a third blind reader on the 14 UNSETTLED key86 T31 tokens (key86 T31 row above), disk only,
~$2"). Intake gate (17:2x UTC, pasted): `fr16045-pisany-rome-1585: partial (line 1) -- edition/page or full-text-search citation found within
6 lines`, exit 0. Read the key86 T31 row and the UNA-PISA / UNA3-PISA / V-PISA3 sections first; follow the same protocol as the earlier
reader rounds (blind: the reader is shown the sign crops and the two candidate sign shapes, never the key values or the copy's letter),
pre-registered in PREREG-PISA-T31.md pushed before any score. Crops already on disk under images/ (f244v_*, f245r_*); cut token crops with
the folder's existing tool if needed, commit them. 14 tokens: one blind subagent call per leaf on token crops (2-3 calls, ~0.5 each) + one reconciliation unit. Apply the relabel only if the registered gate passes; then kp86 --check and decode_key --check.
Known-text item (counts toward the lane's light-guardrail share). Report what was found and where it was not found; do not classify novelty.

### RAH-EF (Sonnet, cap 0.6, box 25 min): rah-salazar-soria-sanchez-1524-28, HTRC EF rerun
NOTES.md l.503-506: rerun exactly `python3 tools/htrc_ef_headwords.py osu.32435013919725 --words cifra,cifras,salazar,sanchez,sánchez,soria,mirandola,descifrar,descifrado,cifrada,cifrado --target '' --json`
(the EF API answered HTTP 200 at 17:2x UTC 11 Oct). Record the per-page hits in a dated NOTES.md section; if hits fall on pages that could
carry the Salazar ciphers' period decipherment or key, list them as the next step (a page read, owner or IA route) with its cost; status
unchanged unless the folder's own Verdict rule says otherwise; gaps_check if the folder is partial. If the API still errors, one retry after
60 s, log it, stop.
