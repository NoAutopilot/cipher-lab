# NEVBIR-OFFSHEET pre-registration (written 2 Oct 2026, 21:35 UTC, before any fit or known-answer number was computed)

Unit: an off-sheet shape class from `subtype_pool.py` (readers' own notes, value-blind); unclassified X_NEW is not fitted
(a mixed bag, not one sign). Pool: nos.87, 71, 86, 90 as committed (passC sequences rebuilt sign-for-sign).
Fit: `fit_offsheet.py` -- the class set to each single letter of the fitted 1572 map and to null, the rest of the map
held (sign_id_map_1572_fit.json), every other off-sheet class unkeyed; score = decode_control.py's per-letter mean log10
4-gram (it16dip, the spec's judge corpus), summed over all passages of the four letters. Word codes are not candidates
(GAPS3: they inflate a per-letter score). gain = best score - score with the class unkeyed.
Accept a fit only if all three hold: (1) >= 3 pooled occurrences; (2) gain >= 0.002; (3) gain above the 95th percentile of
its own control: 200 draws of the same number of randomly chosen keyed letter positions in the pool, relabelled as one
pseudo-sign, unkeyed, then fitted the same way (a set of positions with no common value must not gain as much).
Method check (known answer): the clerk's sheet (f179r_sheet/decipherment_sheet.tsv) gives, per no.87 off-sheet occurrence,
the letter that maximises the matched-letter count of the decode against the sheet (align_sheet.py's statistic; null when
dropping the sign is best; "?" when two or more values tie). PASS if, over no.87 occurrences of accepted classes with a
determinate sheet answer, >= 70% get the fitted value; otherwise stop, log "untested-by-this-tool". If no accepted class has
a determinate no.87 answer, the check cannot run: same stop. Secondary (reported, not gating): the same share over all
fitted classes, accepted or not.
