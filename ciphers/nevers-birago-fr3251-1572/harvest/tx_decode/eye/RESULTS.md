# A1-BIR-EYE results (3 Oct 2026, 12:0x UTC, account-1 worker for LANE-A1)

Pre-registration `PREREG.md` + `positions.tsv` + `blind_*.tsv` + `orient_*.txt` pushed at 632c8786 before any crop was shown;
`score.py` pushed at ed2f6bcc before any answer existed. 3 vision calls (one blind Opus subagent per leaf), 0 network
requests (crops cut from the committed native regions).

Crop commands (run before the first call; crops and 2x copies in the session scratchpad only, never committed):

    python3 tools/iiif_lines.py --image ciphers/birago-fr3252-1571-72/images/f117/src_ark_12148_btv1b9060232m_f118_4380_1400_3150_1300.jpg --out $S/f117 --prefix f117 --centres 103,223,347,462,580,702,815,944,1062,1210 --max-width 1100 --overlap 60 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f168r/src_ark_12148_btv1b9060248g_f171_4600_2560_3500_480.jpg --out $S/f168r --prefix f168r --max-width 1250 --overlap 50 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f168v/src_ark_12148_btv1b9060248g_f172_1650_700_2750_650.jpg --out $S/f168v --prefix f168v --max-width 1250 --overlap 50 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f144r/src_ark_12148_btv1b9060248g_f146_4350_800_3650_760.jpg --out $S/f144r --prefix f144r --max-width 1250 --overlap 50 --only-lines 3,4,5,6 --debug

f.168 and f.144r crops reproduce the committed crop boxes exactly; f.117r reproduces the committed segments horizontally,
but its vertical bands are tighter (43-163 vs 28-208 on L01) because the original run's margins were not recorded. The f.117r
reader reports that the sloping tails of L06-L09 run below their own crops and that it read those signs in the next line's top
strip. Changed and decoy questions both took that hit, so it adds noise to both arms and does not favour either.

| leaf | changed: key-implied picked | decoys: swap picked | p0 | binomial p | Fisher p (descr.) | gate |
|---|---|---|---|---|---|---|
| f.117r (fr.3252 no.77) | 27/32 (0.84) | 3/32 (0.09) | 0.118 | 8.9e-21 | 6.3e-10 | PASS |
| f.168 (no.85) | 7/11 (0.64) | 1/11 (0.09) | 0.154 | 0.0004 | 0.012 | PASS |
| f.144r (no.73) | 5/12 (0.42) | 0/12 (0.00) | 0.071 | 0.001 | 0.019 | PASS |
| pooled | 39/55 (0.71) | 4/55 (0.07) | 0.088 | 4e-29 | 1.5e-12 | PASS |

Reader confidence on the changed arm: key-implied picks were 3 H, 25 M and 11 L; original picks were 2 H, 9 M and 5 L. No
U answers.

**Verdict (pre-registered rule):** PASS on all three leaves. A blind reader, shown both candidates in random order and not told
which came from the key, picks the lam-4 key-implied sign over the two-reader top-1 far more often than it picks a lattice swap at
decoy positions. On f.144r the reader still keeps the original sign at 7 of 12 changed positions, so the image backs fewer than
half of that leaf's changes.

**S candidates for a verifier (key-implied picks at H/M; no grade applied here):** 28 positions, listed per leaf in `score.json`
(`s_candidates`): f.117r 19, f.168 5, f.144r 4. Most fall in known look-alike pairs (T60->T86, T65->T95, T81->T83,
T24->T83, X_NEW->T17).

**Caveats:**
- There was one reader per leaf, and it was a stronger model than the original Sonnet passes. The gate shows that this image
  read agrees with the key's choices, not that the key is right, because the decode chose its changes from the same lattice
  candidates.
- The decoys' swap candidates are the lattice's own second choices, mostly confusion neighbours. A reader that leans towards
  the first-listed reading would depress both arms alike, and the A/B order was randomised.

Not a reading: no reading committed, nothing above S, no novelty classed.
