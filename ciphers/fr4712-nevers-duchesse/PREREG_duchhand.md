# PREREG_duchhand -- same-writer digit test, f.10r vs f.13r (R11A-F4712, 6 Oct 2026, written before any scored call)

Question: is f.13r (BnF fr.4712, canvas f22) written by the same hand as f.10r (canvas f18), so that DUCH-F13's six H glosses
carry to f.10r at grade C (PREREG_duchf13.md condition (c))? The owner's eye answered "I think the same" (ASKS 113, 5 Oct 2026);
DUCH-F13's worker judged "not shown, leaning different" (8 open on f.10r, looped on f.13r). This test is a blind machine look
with controls; it does not overrule either judgement, it is a third, control-backed one.

Panels (all native-resolution crops cut by tools/iiif_lines.py, same Gallica scan scale for the fr.4712 crops):
- R (reference, f.10r): images/f10_L01_s1.jpg + f10_L02_s1.jpg (cipher digit lines).
- P (positive control, f.10r itself, other lines): images/f10_L03_s1.jpg + f10_L04_s1.jpg. Same writer by construction.
- T (target, f.13r): images/f13r/f13g_L01_s1.jpg (codes 6, 82, 58), f13g_L04_s1.jpg (25, 35), f13g_L07_s1.jpg (21, 40).
- N (negative control, a different hand): key no.4 table, BnF fr.3995 f.9v (ark btv1b525085665, canvas f25), a native crop
  of one code column (two-digit codes) cut by iiif_lines.py. Presumed a different writer (a secretary's key table in another
  volume); this is an assumption, stated, not shown. Limitation: N is a formal table hand, T and R are cursive letters, so
  N may score low on ductus/format alone; P guards the other side (the scorer must recognise the same writer at all).
Candidates P, T, N are shown in one call to one blind Sonnet subagent as X, Y, Z in a shuffled order (seed fixed below),
with no folio, no hypothesis and no names; it is asked to compare digit shapes only (0-9, especially 8, 2, 1, 5, 9) and
to give each candidate a 0-10 score "same writer as R", plus per-digit notes.

Shuffle: python3 random.Random(4712).shuffle(['P','T','N']) -> X,Y,Z.

Gate (fixed now): same-writer verdict only if ALL of
  (a) calibration: P >= 6 and P >= N + 3 (else the scorer cannot separate writers at this scale -> NON-TEST, record, stop);
  (b) T >= N + 3 (f.13r clearly above the different-hand control);
  (c) T >= P - 2 (f.13r close to f.10r's own other lines).
(a) pass, (b) or (c) fail -> "not shown the same writer by this test" (not "different writer"); the six carries stay M by
this test. If the gate passes, the six H codes may go M -> C per PREREG_duchf13.md's crib gate, with decode --check.
One call only (Units: 1 Sonnet pass ~1.5); no re-run with changed panels or wording.

Deviation, logged 14:0x UTC 6 Oct 2026 before the scored call: the Gallica fetch of N (canvas f25 region 1150,1150,800,1000)
answered HTTP 503 (1 request, not retried). N is instead cut by `tools/iiif_lines.py --image images/key_no4/f9v_code_columns_sheet.jpg
--region 0,0,450,820 --out images/hand --prefix ctrl_k4 --lines-per-crop 40` (the same f.9v leaf, DUCH-KEY4's on-disk sheet,
first column A 11-39) and upscaled by 1/0.55 to native-equivalent scale -> images/hand/ctrl_k4_native.jpg. Same hand and
leaf as planned; only resampling differs (slightly softer strokes). Gate unchanged.

## Result (14:0x UTC 6 Oct 2026, one call, not re-run)
Shuffle X=N, Y=P, Z=T. Scores: N 4, P 4, T 5 (digits seen R ~30, N ~30, P 3, T 5).
Gate (a) calibration: P 4 < 6 and P - N = 0 < 3 -> **NON-TEST**. (b), (c) not evaluated. The six carries are not moved by this test.
