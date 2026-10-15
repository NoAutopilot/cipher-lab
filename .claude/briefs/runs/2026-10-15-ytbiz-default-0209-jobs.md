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
