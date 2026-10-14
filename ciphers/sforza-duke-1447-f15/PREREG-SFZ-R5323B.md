# PREREG SFZ-R5323B (14 Oct 2026, 21:5x UTC by date -u; account 4, LANE DEFAULT-A4-2135-14) -- pushed before any reader runs

Question (unchanged from PREREG-SFZ-R5323.md): is DECODE scat. 1597 no. 23 (R5323, "Filippo Maria Duca di Milano") the key of the
Duke's slips italien 1584 f.5/f.8? Attempt 2 of the blind eye-pairing method, with a changed instrument. If this FAILs its gate, R5323
is logged "untested-by-this-tool" for the eye-pairing method (CLAUDE.md rule 3, third-attempt clause); no third pass.

Known answers (grade C, ../sforza-italien1584-1447/duke/key.tsv): O=a, Y=o, N8=d, N2=h, N11=r, ce=r, cu=n.

Instrument changes against SFZ-R5323 (the two named gaps):
1. Split label table: the packed row `ca cr ce cu cm ci` becomes six rows; the 40 labels are divided into two groups of 20
   (r5323b/labels_G1.md, labels_G2.md), look-alikes kept in the same group (# and N2 together; O, co, Y, N8, cu, ce together).
2. Value-free exemplar crops: one crop per label for 16 labels (G1: g co K Y cu cp ca cr ce N6 O N8 N9 cm; G2: N2 # N11 8 N4 D t l N1 b),
   cut from f.8 line crops already on disk (coordinates r5323b/exemplars.json, script r5323b/exemplar_sheet.py). The exemplar sheet
   carries the label only; 7 of its 24 exemplars are C-pair labels, the rest decoys. No values, no key, no word "Duke", no f.5/f.8 text.
3. One label group per call: a reader call has one group's table + that group's exemplar sheet, and lists, per plaintext-letter
   column, only the signs matching a label of that group (X:<desc> otherwise ignored).
4. Matched controls read in the same calls: each call holds 6 sheets under neutral names (sheet_01..sheet_12, order fixed by
   random.Random(523323).shuffle; map in r5323b/sheet_map.tsv, written now, not shown to readers). Batch 1 and batch 2 split the
   12 sheets 6/6. R5323 = the two strip crops of SFZ-R5323 (c5323_left/right, 300 dpi) shown as one sheet in two images; controls =
   SFZ-R5323's crops (top half at 150 dpi) of R5324 and R5302 R5304 R5305 R5306 R5309 R5310 R5311 R5312 R5313 R5315 (the same 11).
5. Two passes (A, B): 2 passes x 2 groups x 2 batches = 8 Sonnet calls, independent, same prompt text.

Statistic S(sheet) = number of the 7 pairs whose label is listed in that letter's column, on the cells both passes agree on (a pair counts
only if pass A and pass B both list it; pass columns are the union of the G1 and G2 calls). Same statistic for every sheet, controls
included (controls now have two passes too). S_A and S_B reported beside it.

Gate (PASS needs all three, as SFZ-R5323): S_agreed(R5323) >= 4; S_agreed(R5323) > max S_agreed over the 11 controls; shuffled-value
null p <= 0.01 (permute letters over R5323's agreed columns, 10,000 permutations, seed 5323). Scorer: r5323b/score_r5323b.py (written
before the readers run; strict exact-label tokens; 'A/B?' tokens a sensitivity line only).
On PASS: named next step is key_r5323.tsv from agreed cells and decode_key.py on f.5/f.8 against their glosses (not in this job).
On FAIL: logged as registered, R5323 "untested-by-this-tool" for blind eye-pairing; next instrument named in NOTES; gate not re-tuned.
