# LANE DEFAULT-account-4-20261013-0935 jobs (account 4, lane orchestrator session_01Fof6DzsQ6Uah6Lw7sC1Lfb) -- 13 Oct 2026 09:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 09:35-19:35 UTC 13 Oct (80% line 17:35). Gate 0a: no SESSION-SWEEP-account-4 row.
Backlog read 09:4x UTC: VERIFY-BACKLOG.tsv regenerated 09:41 -- high rows Birago/ceppo (off limits) plus fr16104 ink 52 audit2 (held for
wave 2, after the f.191v view below, since that view may bear on prior plaintext); low rows audit2 on N0/N1. Then `next_steps.py --hot-only`
runnable rows minus the 13 Oct A1/A2 lanes' completed jobs and LANE BNF-FOCUS (account 2) holdings (fr3982, fr3985, fr3986, fr3987, fr3622,
fr3613). Probes 09:4x UTC: openapi.bnf.fr 200, keyed googleapis 503 (eckert-1864 / thurloe Verbael stay parked).
Intake gate 09:4x UTC (tools/intake_gate_check.py, exit 0 each): baluze167-davaux-1637 partial, fr4712-nevers-duchesse partial,
fr15575-syllabic-1592-95 partial, fr16104-vivonne-spain-1572 partial; colbert26-lathuillerie-1644 and na-suriname-map-1781 checked by
each worker as its first command (paste the output).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A4-0935 (account 4)"; the hosts bullet below replaces "No Gallica".
Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session` is not available to
you: say "cost not visible to this session" in the done line. Export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call.
**Hosts: openapi.bnf.fr** (IIIF Image API v3), exactly as `.claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md` "Hosts this wave"
(descriptive User-Agent; one request at a time, >= 3 s apart; per-job request limit stated below; `openapi.bnf.fr take` / `release` ROOM
lines around each batch -- other lanes (BNF-FOCUS) use the host too, so if anyone holds it with no release in the last 30 min, wait;
on 403/429/5xx or a challenge: one retry after 60 s, then stop the host). `tools/iiif_lines.py` and `tools/gallica_folio.py` take
`--iiif-host openapi` (IIIF-HOST, 13 Oct). Never gallica.bnf.fr (403). Images stay under the folder's `images/` (folder < 30 MB);
crops a later eye check needs are committed.

## Wave 1 (09:4x UTC 13 Oct)

### VIV-191V (Opus, cap 1.5, box 35 min, openapi.bnf.fr <= 5): fr16104-vivonne-spain-1572, view f.191v and its docket
NOTES.md Remaining gaps line "ink 52 La Ferriere f.191v lead (V-VIV52, AUDIT 5)": La Ferriere, Catherine IV intro p.cxx, quotes a
Saint-Gouard letter to the Queen (Anjou/England/Infante, early Sept 1572) citing fr.16104 f.191v. Find the canvas for f.191v (about c207;
confirm with `tools/gallica_folio.py --iiif-host openapi` or the cached manifest and by the folio number on the leaf), fetch an overview
(size `1600,`) of f.191v and the leaf carrying its docket/address. Answer, from the image only, in a NOTES.md section "## VIV-191V":
(a) is f.191v in cipher, clear, or a clear copy/decipherment; (b) its date, sender, addressee as written; (c) whether its text is the
same letter as ink 52 f.164r-v (compare the decoded f.164r-v phrases in the folder against what is legible -- name three phrases checked
and the result); (d) whether it is the passage La Ferriere quotes. No transcription beyond what (a)-(d) need; one vision call at most on
line crops if the overview is not legible. Update the Remaining gaps line (done, with the answer) and pass gaps_check. This answer feeds a
second verifier audit (wave 2): write it plainly, with the canvas number and the image file.

### V-BAL167 (Opus, verifier, cap 4, box 70 min, disk only): baluze167-davaux-1637, re-audit of the BAL-WL regrade and the f.228 depth
You are a verifier, not the solver (BAL-CROP/BAL-WL were other sessions). CLAUDE.md "Verifier brief (template)" steps 1, 3a and 4 only
(the N-class is not in question; no novelty search): read PREREG-BAL-SHAPE / PREREG of BAL-WL (commit 418e47a36), the balshape/ tiles,
the blind pass output and the 31 f.228 letter tokens regraded M -> S (H 56 S 31 M 39 I 27 U 1 of 154). Check: (1) the PREREG was pushed
before the read (git log order); (2) the positive control (0.917) and the same-key wrong-label negative (0.000) can each differ from the
target on the statistic scored (CLAUDE.md rule 3 "a control that cannot vary on the same axis"); (3) the 31 regrades are exactly the ones
the gate licenses, no more; (4) re-derive with the folder's decode script `--check` (rule 7); (5) depth per rule 4a for f.228 with
`tools/depth_check.py` -- D1 or D2, one true sentence if D2. Write the verdict as a dated section in AUDIT.md (and status.json depth fields
only if depth changes, via the documented fields); revert any regrade the gate does not license. One eye-look subagent call on tiles at most
(~1.5), only if (3) cannot be settled from the files.

### F4712-C39 (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 10): fr4712-nevers-duchesse, census canvases 39-45
NOTES.md Verdict "census of canvases 39-45 (ff.28v-35r) at 600 px via openapi.bnf.fr, ~$1.5" (F4712-71 lost these overviews to a filename
bug in its loop: name each file by canvas before the next fetch and check it exists). Ark from NOTES.md (F4712-CENSUS / F4712-71
sections). One overview per canvas at size `600,`; for each, one line in a table: canvas, folio as written, clear/cipher/blank/mixed, any
interlinear gloss, hand, date/addressee if legible. If a cipher leaf with an interlinear gloss in the f.10r/f.13r system appears, fetch at
most two native regions of it and stop there (name it as the next step; do not transcribe). Update Remaining gaps (siblings line) and the
Verdict; gaps_check.

### SYL54-LEG (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 4): fr15575-syllabic-1592-95, the no.54 mark legend
NOTES.md Remaining gaps "no.54 mark legend (f.97r right, 8 French lines) - not-attempted; next: one crop of canvas f188 f.97r right, 2 blind
passes + reconcile, ~$1.5". Ark btv1b525085665 (fr.3995). info.json for f188, one native region of the right-hand legend, line crops with
iiif_lines.py, two blind Sonnet passes (one call each, line crops only) + your reconciliation (3 units at ~0.7). Write
`key_no54_legend.tsv` (line, text, grade) and a NOTES.md section; say what the legend says each mark does, and whether that changes any
row of key_no54 (if it would, list the rows, do not edit the key -- a later job applies it with `decode_key.py --try`). Folder is at
29.75 MB: keep only the region file and crops you cite, shrink reference copies, and check `du -sh` before pushing.

### COL26-42 (Opus, cap 2.5, box 50 min, disk only): colbert26-lathuillerie-1644, pre-registered per-code test of 42 = s(ieur)
NOTES.md Remaining gaps "[ ] 42 = s(ieur) per-code test on canvas 20-21 + f.24 + canvas 29, pre-registered, rotation control, scripts only;
~$1.5; source: COL26-C29 post hoc lead". The lead is post hoc on canvas 29 (all three occurrences under "S."), so canvas 29 cannot be the
test set: PREREG-COL26-42.md pushed before scoring must name the held-out occurrences (canvas 20-21 interlinear units, f.24), the
statistic (gloss agreement of 42 with s/sieur/Sr vs the competing value si), the rotation/value-shuffle control and its gate, and the
power at that N (if the held-out N is too small for the control to reject, say non-test and stop before scoring). Scripts only, using the
existing interlinear/*.tsv and key files; no image work. Record in HYPOTHESES.md; key edit only if the gate passes, through
`decode_key.py --try 42=...` first. gaps_check.

### SUR-2039R (Opus, cap 2.5, box 50 min, disk only unless the crops are missing): na-suriname-map-1781, 2039 Remarque K/O/&/[J-rev] blind call
NOTES.md Verdict (SUR-GAPS list, 13 Oct update): "the 2039 Remarque K/O/&/[J-rev] blind call, ~$1.5". Follow the folder's own blind-call
pattern (SUR-2046, PREREG 6b9676d75): PREREG-SUR-2039R.md pushed first with a control built from already-keyed signs of the same sheet
whose answer the subagent does not see, and a gate the control must meet before any target call is accepted; one blind subagent call on
crops already on disk (or regenerated from the folder's regen script; NA host only if neither exists, <= 4 requests, `NA take/release`);
relabels enter as exceptions at the grade the gate licenses (M unless the control clears its bar with margin). decode `--check`; gaps_check.
