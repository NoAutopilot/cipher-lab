# TXE-P split flags (M8), dint-f128-print -- committed 08:15 UTC 9 Oct 2026 by date -u, BEFORE any truth was opened

Made by: `python3 tools/tx_split_groups.py --images ciphers/fr3621-dinteville-1592/images --prefix f128 --lines L02,L03,L04,L05
--pass A=benchmark-tx/outputs/dint-f128-print/passA.tsv --pass B=.../passB.tsv --pass F=.../passF_fable.tsv --out benchmark-tx/txeng/split`
(defaults: gaps 2-12, ink 120, core 0.55, minw 2, pitch 100). Files: sweep.tsv, pieces.tsv, flags.tsv. 0 vision calls.

L02 is unfit by the tool's fixed rule (16 pieces at gap 12 vs 8-9 signs: the band holds non-cipher ink) and carries no flags.
On L03/L04 no gap in 2..12 reaches any pass's sign count (49 and 45 pieces at gap 2 vs 56-58 and 60-61 signs): the hand
glues more than the sweep can open. L05 matches pass A's 61 at gap 2.

Scoring rule, fixed here before tx_bench is run: per pass, tx_bench.py's own align() against the label-mapped truth
(benchmark-tx/dint128_label_map.tsv) on the fitted lines L03-L05 gives the output positions inserted (no reference
position) and the reference positions deleted. An insertion is caught when its output position is flagged; a deletion is
caught when the output position immediately before or after the gap is flagged. Recall = caught / (F's insertions + A's
deletions) on the fitted lines; flag share = flagged positions / output positions, per pass and pooled over A and F.
Gate (brief): recall >= 0.6 at flag share <= 15%. Insertions/deletions on L02 are reported as outside the instrument.
