# AUDIT -- oldenbarnevelt-brederode-1605

## Verifier: R9-OBRED4 corrections (R10-OBREDV, 6 Oct 2026, 07:22-07:3x UTC, account 2)

Separate session from the solver (R9-OBRED4). Scope: the two cipher-group rows of `imagecheck_1490/corrections.tsv` only. No novelty
class asked or given. Evidence: the line crops on disk (`images/crops_1490/s2L_L20/L21/L22/L24.jpg`, cut from
`images/na_301_14_1490_p0002.jpg` by R9-OBRED4), zoomed and contrast-stretched by this verifier (PIL, local, no network); one look per
entry plus same-scan controls. Zoom regions (crop pixel x ranges, full crop height): L21 x 1040-1220 (the group) and 1160-1215 (third
digit); L21 x 540-660 ("30", the 0 control); L20 x 2180-2380 ("49 314", the 9 control); L19-L23 x 1120-1260 stacked (fold check);
L24 x 1940-2380 and the scan itself at y 2558-2708, x 2200-2700 (line end and margin).

| entry | print | proposed | verdict | reasons |
|---|---|---|---|---|
| s2L_L21, 6th group of "636 ende 49 314 30 467 387 [170]" | 170 | 179 | **uphold** | First two digits are a clear 1 and 7. The third is a closed bowl with a stroke on its right rising to a point at the bowl's top, and a dark tapering wedge below the baseline under that stroke: the shape of this hand's 9 in "49" on L20 (bowl, stroke joining at top right, descender). Control 0s on the same scan ("30" on L21, "oo" in "oock" on L22) are plain closed ovals with no right stroke and no descender. A crease runs vertically through the glyph's right side; on the stacked L19-L23 strip it shows only on L21 and only as a thin grey line above the bowl, so the black wedge below is ink, not crease shadow. Caveat: the descender lies on the crease line, so the bowl-plus-stroke shape carries most of the weight; grade H kept, but a reader with the original could confirm in one look. |
| s2L_L24, last group of "bij 623, 703 ende [704]" | 704 | 70? | **uphold (undecidable digit, print kept)** | "7" and "0" are clear; the third digit is under an ink blot. A descending stroke shows below the blot, which fits this hand's 4 (long stem) but equally its 3 and 9, which also descend. The scan beyond the crop edge shows the line ends at the blot (blank margin, then the gutter), so nothing is cut off by the crop. M is right; keeping the print's 704 as the working value is right. |

Editorial rows (30.000 = "XXX M.", 12 off 13.000 = "XII off XIII M."): not cipher groups; not re-checked beyond seeing "XII off XIII M."
on L21, which agrees.

**If 170 -> 179 is applied** (ciphertext.txt not edited here, per rule 2's never-silently-repaired): neither 170 nor 179 occurs elsewhere
in the letter, so repeat counts, the group inventory size and the numeral range (max 741) are unchanged; the key screens on disk
(`decode_keys_1600s.tsv`, `decode_keys_palatine_hessian.tsv`; OLD-DKEY, R8-OBRED2, R9-OBRED3) tested range, office and design, not
single values, so none changes. Only digit-level statistics move (one 0 becomes a 9 in 355 digits) and `imagecheck_1490/printed_numerals.txt`
(regenerated from ciphertext.txt) would change if ciphertext.txt were edited. No reading, key.tsv or decode script exists for this folder,
so no rule-7 check is affected. `specs/na-oldenbarnevelt-2442-1605.json` does not contain the group.

Verifier's verdict: corrections.tsv may be applied as it stands -- 179 as the manuscript's reading (H, with the caveat above), 704 kept
as printed at M.
