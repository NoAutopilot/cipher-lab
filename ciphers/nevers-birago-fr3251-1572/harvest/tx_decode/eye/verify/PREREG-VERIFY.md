# A1-BIR-VERIFY pre-registration (3 Oct 2026, 12:3x UTC, account-1 verifier for LANE-A1; a session other than A1-BIR-EYE's)

Brief `.claude/briefs/runs/2026-10-03-acct3-a1-wave7.md` job 5. Written and pushed **before any crop is shown to any reader**.

## (b) Audit of A1-BIR-EYE's draw, done before this file
- `../prereg_positions.py` re-run: positions.tsv, blind_*.tsv, orient_*.txt reproduce byte-identically (seed 20261003).
- `../score.py .` re-run: score.json byte-identical (f.117r 27/32 vs 3/32, f.168 7/11 vs 1/11, f.144r 5/12 vs 0/12).
- Option order: key-implied sign shown as A on 21/32, 6/11 and 8/12 changed questions; the reader picked A on 18/32, 6/11 and 7/12
  changed questions and 19/32, 8/11 and 7/12 decoys. That is no A/B position leak large enough to make the result.
- **Confound found:** the decoys were drawn from *all* unchanged positions with a second candidate, as PREREG.md says. So they are
  mostly unambiguous: the median lattice ratio (second candidate / top-1 score) is 0.12 / 0.11 / 0.18 for decoys and 0.68 / 0.28 / 0.34 for changed positions
  (f.117r / f.168 / f.144r). A reader who flips any genuinely ambiguous sign would pass the A1-BIR-EYE gate without the key being
  right. In A1-BIR-EYE's own answers on the decoys with ratio >= 0.3, the reader picked the swap sign 2 of 6 times on f.117r, against 24 of 26 changed positions; that
  decoy count is too small to settle the question, hence arm 'mdecoy' below.

## Question sets (`prereg_verify.py`, seed 20261004 -> vpositions.tsv hidden truth; vblind_/vorient_ reader files)
Per leaf: arm 'orig' = A1-BIR-EYE's changed + decoy questions, same positions and the same A/B order; arm 'mdecoy' = unused unchanged
positions whose lattice ratio is >= 0.3 (ambiguity-matched decoys), a seeded sample capped at the leaf's changed count: f.117r 30,
f.168 7, f.144r 12. All questions are renumbered and reshuffled together.

## Reader
One fresh blind Opus subagent per leaf, 3 vision calls in all. It sees only line crops, `../../../sign_sheet_blind_1572.png`, `vblind_<leaf>.tsv` and
`vorient_<leaf>.txt`, and is never told of a key, a decode, an earlier read, or which candidate is which kind. Crops:
- f.117r **re-cut at the original band height** (`--top-margin 15 --bottom-margin 45`; all 30 boxes identical to the committed
  `ciphers/birago-fr3252-1571-72/images/f117/manifest.json` boxes, checked before this file):
  `python3 tools/iiif_lines.py --image ciphers/birago-fr3252-1571-72/images/f117/src_ark_12148_btv1b9060232m_f118_4380_1400_3150_1300.jpg --out $S/f117 --prefix f117 --centres 103,223,347,462,580,702,815,944,1062,1210 --max-width 1100 --overlap 60 --top-margin 15 --bottom-margin 45 --debug`
- f.168 and f.144r: A1-BIR-EYE's own commands (RESULTS.md), which reproduce the committed boxes.

## Gates (per leaf; `score_verify.py`, pushed with this file)
- **G1 (the brief's gate, unchanged):** arm 'orig', changed key-implied picks c/n_c against decoy swap picks d/n_d, PASS iff r_c > r_d
  AND binomial P(X >= c | n_c, p0=(d+1)/(n_d+2)) < 0.05. This is required on the f.117r re-cut. On f.168 and f.144r it is a replication.
- **G2 (matched):** the same rule on changed positions with ratio >= 0.3 against arm 'mdecoy'.
- **Survivor rule for (c):** one of A1-BIR-EYE's 28 S candidates is kept only if its leaf passes G1 AND G2 on this read AND this read
  also picks the key-implied sign there at H or M confidence. Anything else is dropped (left at its current grade). A leaf that fails
  either gate keeps none. Kept candidates are applied at S through decode_key.py's exceptions path, then `--check` and the judge are run per leaf.
No reading claimed beyond S, no novelty classed.
