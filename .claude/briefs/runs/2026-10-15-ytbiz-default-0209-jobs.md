# LANE DEFAULT-account-2-20261015-0209 jobs (account 2, lane orchestrator session_01Gd58WqYtVh88ZYsT485HT7) -- 15 Oct 2026 02:2x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 02:09-12:09 UTC 15 Oct. Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct;
proceeded, as earlier incarnations did. VERIFY-BACKLOG (21:40 UTC 14 Oct): high rows Birago/ceppo (off limits), audit2 rows N0/N1 (Outreach
gate 2 n/a), so no verifier job. `next_steps.py --hot-only` runnable rows; LANE DEFAULT-account-1-20261015-0206 runs in parallel, so the picks
are named in ROOM (02:2x) for it to exclude. VIV-KEYSTONE folders (fr16104/5/6 vivonne) excluded: live account-2 VIV jobs. Guardrail fifth:
CL1161-S7 (Lasry's key of record is published, AUDIT 3 N0; this job tests our labels against it).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A2-0209-15 (account 2)"; the hosts named in your job replace that file's
hosts lines. Export `CIPHERLAB_ACCOUNT=ytbiz` before any tools/room.py call. `get_session` is not available to you: say "cost not visible
to this session" in the done line; every claim/halfway/done line ends "usage: not readable here" (owner rule, 15 Oct 2026). Halfway line:
one ROOM line at half the box or half the cap, whichever first (skip if done before). Check 1 before any unit: grep the folder's NOTES.md
AND AUDIT.md section titles for a later section that already ran the unit; if it did, one ROOM line and stop. Never the words solved,
cracked, novel, first, new for anything this project did. Do not touch status.json, NEAR.md, STATUS.md or the board (the lane
orchestrator does). Birago, Armstrong, Debosnys and the vivonne folders are off limits. Report what was found and where it was not found;
do not classify novelty (solver jobs). Stop before starting a unit that would cross 80% of the cap or the box. Price per vision call
(~1.0-1.5 each), not per page (CLAUDE.md Usage 6). At the end: Remaining gaps / Escalation updated, `python3 tools/gaps_check.py <target>`
pasted, `tools/file_shrink_guard.py` on every touched file, push, one done line.

## Wave 1 (02:2x UTC 15 Oct)

### GB-PASS2 (Opus, cap 2.5, box 50 min, www.googleapis.com only, <= 60 requests at >= 1.5 s, key + `&country=US`): one serialized Google Books pass for three folders
Hold the host with a ROOM "googleapis take" line and a "release" line. Probe first: one known-good control query (the GB-2-form control the
folder scripts already carry); on 503/429 retry once after >= 60 s, and if it fails again stop the whole job (host rule) and log it in each
folder's Escalation retry line. Intake gate (02:2x UTC, pasted): `eckert-1864: partial (line 3) -- edition/page or full-text-search citation
found within 6 lines`; `thurloe-printed: partial (line 2) -- ...`; `baluze167-davaux-1637: partial (line 1) -- ...`; all exit 0. Units, in order:
(a) eckert-1864, Remaining gaps (GB-E13): re-run `fortmonroe/eck_gbpass_gb.py` with E590 removed from T, GB-2-form control first, for E591,
E592 and the looser E589 query (`Monohansett Monroe`) in Grant Papers vol. 13 (~0.3).
(b) thurloe-printed, Remaining gaps (GB-VERB): the Verbael (1725) date-phrase snippet queries (`gb2_verbael_snip.py`) on the two full-view ids
GB-2 located (vZzvg46MRdEC, T2JVAAAAYAAJ) for Beverning's 27 June / 22 Aug 1653 letters and No. 37 pp.252-253 (~0.5). A snippet hit is a
location, not a reading; say what text the snippet carries.
(c) baluze167-davaux-1637, Escalation print line: Google Books for the 169 f.22r phrases (the VER-BAL22 phrase list; 503 on 14 Oct) (~0.3).
Each folder: its own NOTES.md section, Remaining gaps / Escalation, gaps_check.

### BAL22-NUM (Opus, cap 3, box 60 min, disk first; openapi.bnf.fr/gallica only if an exemplar crop is missing, <= 6 requests, ROOM take/release): baluze167-davaux-1637 169 f.22r remaining numerals
Remaining gaps item "169 f.22r name and remaining signs" and Verdict: the f.22r remaining numerals (16 x4, 45', 12:, 13:, 65) by the same
same-hand glossed-exemplar test BAL169-F22B used (shuffle control, 200 permutations; read its section and reuse its script/option, never a
private copy). Intake gate pasted under GB-PASS2. Units: (1) PREREG pushed before any score (statistic, null, gate as BAL169-F22B, and a
power line: the gate can fail); (2) exemplar crops (disk; `tools/iiif_lines.py --image FILE --out DIR` pasted if a crop is cut); (3) blind
comparison, one vision call per numeral group, two passes + one reconciliation unit (~1.2 each); (4) grade changes only M -> S where the gate
passes; decode re-run with `--check`. Coordinate with GB-PASS2 on NOTES.md edits (fetch/rebase before writing).

### F4712-C131 (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 16 requests at >= 2 s, ROOM take/release lines; VIV workers share this host): fr4712-nevers-duchesse sibling census, canvases 131-142
Verdict: census of canvases 131-142 (f.121v onward, the last 12) at 600 px, the same method as F4712-C119 (read its section; same tool and
output TSV). Intake gate (02:2x UTC, pasted): `fr4712-nevers-duchesse: partial (line 1) -- edition/page or full-text-search citation found
within 6 lines`, exit 0. Units: 12 canvases at 600 px (fetch once, manifest), looked at in vision calls of 4-6 canvases each (~1.0 per call);
any canvas carrying cipher or an interlinear gloss in the f.10r figure system gets one 1600 px look. Record each canvas (clear / cipher /
glossed / blank). Close the siblings rung if nothing is found; do not decode.

### CL1161-S7 (Opus, cap 2, box 45 min, disk only): clair1161-avis-flandre-1688, S and 7 exemplar image check
Remaining gaps item "S-sign conflicts 7 (i vs b) and S (u vs n)" and Verdict: image check of the S and 7 exemplars for merged shapes (u vs n
minims; i vs b) with atlas crops beside Lasry's sheet (on disk from C1161-LKEY / CL1161-KA; credit Lasry, rule 8), then `tools/decode_key.py
--try` per split at every occurrence. Intake gate (02:2x UTC, pasted): `clair1161-avis-flandre-1688: partial (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0. Units: (1) PREREG pushed before any look (what counts as two shapes; a power line:
a planted split of a known two-shape label must be detected); (2) exemplar crops (disk; `tools/glyph_atlas.py` or iiif_lines --image,
pasted); (3) two blind vision passes (one call per sign) + reconciliation (~1.2 each); (4) --try per split; no key.tsv edit unless --try's
own control passed (graded M otherwise).

### ERBA-SWAP (Opus, cap 2.5, box 50 min, disk/CPU only): erba-2006 K=13 case-sensitive design with a search fix
NOTES.md "## Next step (ERBA-CASE, 14 Oct 2026)": add a letter-swap move (and more restarts, e.g. 32 x 16,000, or seeds from splits of test
4b's case-folded best keys) as an option on `test4_wordconstrained.py` (calls without it unchanged; offline test if the script is in tools/).
Intake gate (02:2x UTC, pasted): `erba-2006: open (line 3) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
Units: (1) PREREG-test4d.md pushed before any score: same N, dictionary and every-seed >= 0.60 gate as test 4c, design unchanged, search
change only; (2) matched control, 5 seeds; (3) target and 10 nulls only if the control passes. This is the design's second search-side
attempt: if the control still misses, log the design "untested by this instrument" (rule 3's third-attempt clause) and name a genuinely
different instrument or new material in the Verdict. Rows into HYPOTHESES.md (both numbers). CPU serialized (no background run beside it).

## Wave 2 (02:5x UTC 15 Oct)
Wave 1 note: BAL22-NUM and F4712-C131 stood down at check 1 (account-1's lane spawned the same picks two minutes earlier). Before
your first priced unit, also grep the last 60 ROOM lines for your folder name: a live claim from any lane means stand down.

### SFZP-SIB (Opus, cap 8, box 120 min, Gallica IIIF btv1b100373864 via tools/iiif_lines.py <= 12 requests at >= 2 s, ROOM take/release lines "gallica"): Pusterla key units 5-6, f.72/f.73 then f.75/f.74
Folder ciphers/sforza-italien1584-1447/pusterla/ (the key's units; read its NOTES.md "Remaining gaps" lines ~123 and ~237 and Verdict
~248) feeding ciphers/sforza-pusterla-1447-f13 (Verdict line ~431: "pair check + two passes + reconciliation on sibling f.72 (unit 5 of
the key), ~$3"). Intake gate (02:5x UTC, pasted): `sforza-pusterla-1447-f13: partial (line 1) -- edition/page or full-text-search citation
found within 6 lines`, exit 0. Units at ~1.3 each, per slip: (1) pair check -- does the copy (f.73 for f.72; f.74 or f.76 for f.75) carry the
same text as the cipher slip (eye check of the canvas at 600 px, one vision call); (2) crops by the same pasted `tools/iiif_lines.py --ark
btv1b100373864 --canvas N --region ...` form units 1-4 used; (3) two blind passes (passA Opus, passB Sonnet, as f.81/f.42) + one
reconciliation unit with `tools/reconcile_passes.py`; (4) align with the clear copy as align_f81.tsv was built and re-run the unit G1 /
key pool exactly as the four-unit key was gated (control and shuffle p95 as before); key rows enter only through that gate. f.72 first;
start f.75 only if f.72 finished under 50% of cap and box. Then re-run the f.13 lattice decode (lattice_decode.py, both corpora) once on the
re-pooled key and paste the judge line. Credit and grades as the folder does. Update both folders' Remaining gaps / Escalation, gaps_check.

### SP105-SOAS (Opus, cap 1.5, box 40 min, soas.ac.uk contact page only, <= 4 requests): sp105-paget-1693 item-level enquiry draft
Verdict (line ~258): draft an item-level enquiry to SOAS Special Collections for PP MS 4/02/47 and sub-series 01-25 in outreach/. Intake
gate (02:5x UTC, pasted): `sp105-paget-1693: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
Follow outreach/README.md exactly (rule 1 AI-disclosure sentence in the first paragraph, rule 1a voice, subject/recipient/sign-off lines;
recipient = the institution's public contact address read from SOAS's own contact page with the date). Draft only: no CONTRIBUTIONS.md
send row, no SEND-QUEUE row, no mail; status `drafted`, "checked:" line left for a separate gate-7 session; one ASKS.md row only if
outreach/README.md says drafts get one. Update the folder's gaps (the gap becomes waiting-on the gate-7 check / send), gaps_check.
