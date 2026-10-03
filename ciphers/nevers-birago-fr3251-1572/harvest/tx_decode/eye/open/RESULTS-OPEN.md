# BIR-OPEN results (3 Oct 2026, account-3 worker)

Pre-registration `PREREG-OPEN.md` + `prereg_open.py`, `score_open.py`, `oposnull.py` pushed at e5076ee1 before any crop or score.

## Crops (scratchpad only; commands run before the first reader call, 13:0x UTC)
    S=<scratchpad>/crops
    python3 tools/iiif_lines.py --image ciphers/birago-fr3252-1571-72/images/f117/src_ark_12148_btv1b9060232m_f118_4380_1400_3150_1300.jpg --out $S/f117 --prefix f117 --centres 103,223,347,462,580,702,815,944,1062,1210 --max-width 1100 --overlap 60 --top-margin 15 --bottom-margin 45 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f168r/src_ark_12148_btv1b9060248g_f171_4600_2560_3500_480.jpg --out $S/f168r --prefix f168r --max-width 1250 --overlap 50 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f168v/src_ark_12148_btv1b9060248g_f172_1650_700_2750_650.jpg --out $S/f168v --prefix f168v --max-width 1250 --overlap 50 --debug
f117: 30 crops (10 lines x 3 segments); f168r 12 (4 x 3); f168v 9 (3 x 3). Passage R0n = f168r_L0n, V0n = f168v_L0n.
