# MQS-CVD-FIX (LANE MQS-3, account 4) -- job brief

Written 9 Oct 2026 (clock read 10:1x UTC by date -u) by the LANE MQS-3 orchestrator (account 4,
session_01An6QVEiGnTrULNnQG5xqvG). Lane brief: `2026-10-09-acct3-mqs-lane.md`; research row: `research/MARY-STUART-TALK-2026-10-09.tsv`.

- **Model, cap, box:** Opus 5.5, cap USD 2.5, box 70 min. Stop at the cap; at 80% of the box do not start a new unit.
- **Row:** M47 follow-up (MQS-CVD-AUDIT 9e102d301 found glyph_atlas.py's cv2 overlays red vs green, lines ~230/234/930, deutan dE 3.7-5.1, and build_dashboard.py green vs amber RED-GREEN hue pairs).
- **Goal:** replace those colour pairs with a CVD-safe pair plus a non-colour cue (line style, marker shape or a text label) so meaning never rides on hue alone (CLAUDE.md MQS-SHEETS line: never red against green). Remember cv2 tuples are BGR.
- **Known answer and gate (pre-register in `tools/tests/PREREG-MQS-CVD-FIX.md`, pushed before any control runs):** `python3 tools/cvd_check.py --audit tools/glyph_atlas.py tools/build_dashboard.py` before and after, pasted: zero CVD-COLLAPSE and zero RED-GREEN on the edited lines after (before: the audit's own lead list). Control: the audit's own held-out set is unchanged (do not edit cvd_check.py). Existing glyph_atlas/build_dashboard tests and outputs otherwise unchanged (pixel diff limited to the overlay colours). This is a fix, not a method: shelf rows updated only if a row describes the colours.
  Say in one line why the null can fail differently from the known answer for the statistic computed (rule 3). A control
  that misses its gate ships the option `weak` with both numbers; nothing is run on a target from it; it is not re-briefed.
- **Files:** `tools/glyph_atlas.py` (colour constants and overlay drawing only), `tools/build_dashboard.py` (colours only), their tests; the PREREG file; `tools/data/tool_shelf.tsv` rows and `SYSTEM.md` (append and rebase). No status,
  key, reading or AUDIT.md change anywhere; nothing from ciphers/debosnys-1883 or the private repository; no Birago 1572
  family value-bearing page for the owner while ASKS 118 is open. No host.
- **Credit (rule 8):** Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2); CTTS (Apache-2.0) where its design is followed.
- **Common rules:** as in `2026-10-09-acct3-mqs-sheets.md` ("Common rules"), with this job's name MQS-CVD-FIX and "for LANE MQS-3
  (account 4)" in your ROOM lines. Do not edit CLAUDE.md or `.claude/briefs/README.md`: give your one Registration line in
  the final report and in your ROOM done line. Done line names: option, control vs null, shelf grade, commit.
