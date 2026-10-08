# PREREG-D2-DUPL (8 Oct 2026, written and pushed before any read was made or scored)

Job D2-DUPL, LANE DEFAULT-account-2-20261008-0710. Brief: joined-hand Duployé control + blind re-read of the signature 'H'.

## Control (rule 3, design-matched on joined hand)
- Material: "VERSION 3" (four lines of joined Duployé word forms, consonants T D L R with vowels A O), Institut
  sténographique de France, *Méthode de sténographie Duployé perfectionnée* (1905), Internet Archive `cihm_84595`
  (PDF p.12 = printed p.9); its printed answer "Traduction de la version 3" (PDF p.13 = printed p.10).
- Key: `dupl_control/version3_key.tsv`, 133 primitives, phonetic, written from the printed French before any read.
- Crops: `tools/iiif_lines.py --image v-12.png (pdftoppm -r 300) --region 160,1090,1660,400 --lines-per-crop 2
  --top-margin 45 --bottom-margin 45`, then scaled so the tall strokes are ~60 px (the signature's stroke height used
  by GAPS183), Gaussian blur 1.5, halved and doubled (GAPS183's degradation). Files `images/dupl_control/v3_L01_deg.png`,
  `v3_L02_deg.png`; reference chart `images/dupl_control/duployan_chart18.png` (Noto Sans Duployan, 18 letters).
- Reader: one fresh Sonnet subagent, given only the chart and the two crops, told it is Duployé shorthand to be read as
  primitives from the chart; not told the words, the key, the target or any hypothesis.
- Statistic: `scripts/duploye_joined_control.py` edit accuracy over the whole exercise (word boundaries dropped).
- **Gate: control accuracy >= 0.60 AND above the chance p95.** If it fails, the target read below is logged but does
  not count (non-test at this resolution for this reader), and the step is not re-tuned in this job.
- Can the control fail differently from the target? Yes: the statistic is per-primitive identity; a misread R/L/A/O
  lowers it, and the known answer is independent of the reader.

## Target
- Crop: `images/Fashion-Signature.png` through `tools/iiif_lines.py --image ... --top-margin 130 --bottom-margin 130`
  (GAPS183's crop), shown at 2x.
- Reader: a second fresh Sonnet subagent (same model as the control reader), given the same chart and the signature crop,
  asked to read the capital initial of the middle word as a left-to-right sequence of chart primitives; not told any
  place name, any hypothesis, GAPS183's reading, or the caption.
- Score: `scripts/sig_hypothesis_score.py --read "<reading>"` unchanged (seed 183, 2000 trials).
- **Decision rule: the hypothesis "ARRAS (a-r-a)" or "AVANT ARRAS" is supported only if the control passes AND its p < 0.05
  AND every decoy town has p >= 0.05.** Anything else is "not supported at this resolution"; a pass is still all grade M
  (rule 4) and no reading is claimed.
