# PREREG MQS-STRUCK-2 (LANE MQS-3, account 4, 9 Oct 2026, committed 10:08 UTC (commit 9c5f81b3d time; the header first said 10:15, an estimate, corrected 10:12 by date -u -- rule 6), before any control ran)

Job: research/MARY-STUART-TALK-2026-10-09.tsv row M44, second half (the first half, MQS-STRUCK e01966990, gave
tools/decode_key.py the token states `struck` and `over=OLD>NEW`, a tsv `state` column and --corrections final|original).
Method credit: Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2), the encipherer's own deletions and overwrites
shown in the reading; CTTS (Apache-2.0) is not followed here (no code or format taken from it).

Tools:
- tools/sign_sorter_apply.py: a pile doc `state: struck` (every tile settled in that pile is struck) or a per-box doc
  DIR/states/*.json {sid, state: 'struck'} / {sid, state: 'over', old: OLD} / {sid, state: 'over=OLD>NEW'} writes a
  `state` column into --out (only when any state was saved: no state, the export is byte for byte as before), and
  --pass-out FILE writes line, pos, sign, state (the decode_key.py tsv format; line/pos from --signs).
- tools/decipher_sheet.py reading: a struck token is a bordered tile with the text label STRUCK, its sign in
  [brackets], value row "not read" (final) or the as-written value with "as written" (original); an overwrite shows
  OLD>NEW with the text label OVER; each one is also listed under "Corrections on the page" as a callout
  (`data-corr="<kind> <line>:<pos>"`). Dark ink and text labels; no meaning by colour; tools/cvd_check.py passes on the render.

## Control K (known answer, synthetic round trip; seeds 0-4)
Fixture: 120 boxes on 4 lines (signs.tsv sid, page, x, y, w, h, line, pos), labels.tsv from a 120-letter French passage under
a random 2-digit substitution key; a sorter db with one ordinary move, plus 10 planted states per seed: 5 struck (a pile doc
state struck on a pile of 2 tiles + 3 per-box struck docs) and 5 per-box overwrites (old = a random wrong code).
Pipeline: sign_sorter_apply --pass-out -> decode_key (format tsv) with --corrections final and original -> decipher_sheet
reading --tokens-tsv style records via the target's decode.json. Statistic: planted states found on the sheet as callouts at
the exact line:pos with the exact kind (struck/over) and, for overwrites, the exact OLD>NEW text.
- Expected: 10/10 on every seed, both modes. **Gate: 10/10 planted on 5/5 seeds, final and original.**
- Null N1 (state column dropped from the pass TSV): expected 0/10. Null N2 (state column row-shuffled within the pass TSV,
  seeded): expected well under 10 (a shuffled state lands on a planted position only by chance, and an overwrite also needs
  its OLD>NEW pair, which a shuffle moves). **Null gate: < 10/10 on 5/5 seeds for N1 and N2.**
- Why the nulls can fail differently from K on this statistic (rule 3): the statistic is position- and kind-specific, and
  both nulls change exactly which positions carry a state (N1 none, N2 permuted), so the callout count or position must
  differ unless the plumbing ignores the column -- not orthogonal.
- Ceiling: K is a plumbing control expected at ceiling; it licenses `controlled-only` (plumbing), never a claim that the
  tools find corrections on a page (that is the person's eye, on the image).

## Must-not (Usage 8a)
M1: no state saved -> sign_sorter_apply --out byte-identical to the export without this option (existing tests unchanged).
M2: a reading sheet with no state on any token has no "Corrections on the page" section; Gramont reading sheet (existing
    test, already-read control, no marker) renders unchanged apart from volatile footer.
M3: a state doc whose sid is not in the labels is dropped and counted (summary states_dropped), never attached elsewhere.
M4: an unknown state ('weird') is refused with a message, never written.
No Birago 1572 family, no debosnys, no target folder written; temporary directories only.

## Outcome (run 9 Oct 2026, between 10:09 and 10:11 UTC by date -u; `python3 tools/tests/test_struck_roundtrip.py --controls`)
| seed | planted | K final | K original | final decode accuracy | N1 drop | N2 shuffle |
|---|---|---|---|---|---|---|
| 0 | 10 | 10/10 | 10/10 | 1.000 | 0/10 | 0/10 |
| 1 | 10 | 10/10 | 10/10 | 1.000 | 0/10 | 0/10 |
| 2 | 10 | 10/10 | 10/10 | 1.000 | 0/10 | 0/10 |
| 3 | 10 | 10/10 | 10/10 | 1.000 | 0/10 | 0/10 |
| 4 | 10 | 10/10 | 10/10 | 1.000 | 0/10 | 0/10 |

K 10/10 on 5/5 seeds in both modes (gate 5/5): PASS. Nulls < 10/10 on 5/5 (gate 5/5): PASS. N2 came out 0/10 rather
than "well under 10": a shuffled state lands on a planted position with the right kind only by chance (about 5/125 per
struck state) and an overwrite also needs its OLD>NEW at that position. Must-nots M1-M4 PASS (test_struck_roundtrip.py);
M2 on Gramont: the reading sheet renders byte-identical to the pre-change render apart from the volatile footer (the
correction CSS is emitted only when a sheet carries a correction, so committed sheets do not go stale under --check).
cvd_check --audit on the rendered synthetic sheet: 0 flags; every colour in the sheet is in the checked palettes.
Shelf: `controlled-only` (plumbing). Nothing run on a target.
