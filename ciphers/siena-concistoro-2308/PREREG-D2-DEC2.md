# PREREG-D2-DEC2 (8 Oct 2026, written 07:45 UTC by date -u, pushed before any scored run)

Job D2-DEC2 (LANE DEFAULT-account-2-20261008-0710). This runs the reader-bias control that PREREG-R13-SIENAJ.md already pre-registered
and R13-SIENAJ did not run (no image on disk): blind labels for no. 11 (DECODE R4800, a piece that sat below its null in R11).
Inventory `d2dec2/inv_no11.tsv` written from line crops before any transcript of no. 11 was opened.
Statistic, null and gate unchanged from PREREG-R13-SIENAJ (Jaccard vs the blind no. 7 row; 2000 curveball swaps, seed 11;
pJ <= 0.05/15 = 0.0033). Rows: nos. 7, 19, 9 = R13-SIENAJ's blind inventories (copied unchanged to `d2dec2/`), no. 11 = this blind
inventory, all other rows as R11 parsed them. Script `sign_overlap_pool.py --blind ciphers/siena-concistoro-2308/d2dec2 --tag _d2dec2`.
Pass (the control behaves): no. 11 does NOT clear (pJ > 0.0033) on the conservative set. If it clears, the convention (letters/digits
named as themselves, which carries most shared stock) is merge-biased and R13-SIENAJ's no. 19 result is logged "non-test: reader bias".
Disclosed limit: this reader is a different session from R13-SIENAJ's reader, so the control tests the shared labelling convention, not
the same reader's hand. The --liberal run is descriptive only.
