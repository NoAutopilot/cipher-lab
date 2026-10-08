# PREREG-D1A-D1411 (written 8 Oct 2026, before any tile is cut or read)

Job D1A-D1411, LANE DEFAULT-account-1-20261008-0540. Question: the 12 substitution ops (13 numbers) where p5L_L11_b-L31_a
(d1411p5/numbers.tsv) and its p.2 source def1411 p2Lb_L01-p2R_L02 (def1411/numbers.tsv) differ (d1411p5/posthoc_copy.json
`replace_ops`): which numeral does each copy's ink show?

## Instrument
- Per op: one tile of each copy's number, cut by the worker from the committed line crops (images/def1411_crops,
  images/d1411p5_crops) using placement views (d1a/ruler.py). For the 2-number op (p.2 "6 12" vs p.5 "60 22") each number
  is its own tile pair (13 tile pairs).
- Exemplars: 2-3 tiles of each candidate numeral involved in the ops, cut from numbers that are *equal* in both copies' aligned
  span (posthoc alignment `equal` blocks) and graded ok in the relevant numbers.tsv -- undisputed same-hand readings. Exemplar
  truth = that agreed value. Exemplar tiles are never one of the 26 disputed tiles.
- Montage: all disputed and exemplar tiles shuffled together (seed 1411), each labelled only with a neutral id (T01...). The
  reader is not told which tiles are pairs, which are exemplars, the page, the candidate values, or any key.
- Reader: one blind Opus subagent call, shapes only: for each tile, the number it shows, confidence (sure / unsure), and
  alternative if unsure. Then one worker reconciliation unit (the worker looks at the same montages beside the reader's answers).

## Control (gate before any settlement)
- Exemplar accuracy = exact reads of exemplar tiles / exemplar tiles. **If < 80%, the comparison is a non-test**: no difference is
  settled, nothing is changed, the step is logged "non-test (exemplar control below gate)".
- The control can differ from the target statistic: exemplar tiles are scored against independent agreed truth, disputed tiles
  against nothing; a reader who cannot tell the look-alikes fails the exemplars.

## Settlement rule (per op, only if the control passes)
- S1 settled-same: the reader reads both copies' tiles as one numeral N (sure on at least one) -> both copies show N; the
  transcription that differed was a reader error; settled value N.
- S2 settled-legible: one tile read sure as value V equal to its own transcription, the other read unsure with V or that
  transcription as the alternative / look-alike -> settled V.
- S3 genuine variant: both tiles read sure, each matching its own transcription and differing -> the copies really differ
  (a copyist variant); unsettled for the text, both kept.
- U unsettled: anything else (a read matching neither candidate, both unsure).
- The worker's reconciliation may move an op only toward U (never upgrade U/S3 to S1/S2), and records any disagreement with the
  reader beside it.

## Re-score (descriptive only, AM-D1411V ruling)
- Settled text: p.2 and p.5-copy numbers.tsv with S1/S2 values substituted. Coverage of p.2 (def1411 set) + p.5 copy span under
  T21r and T21r_h12 (the score_p5.py statistic, 200 order shuffles seed 1411 p99), before vs after. In-sample for T21r: **no S
  grades move**, whatever the number. Committed numbers.tsv files are not edited (rule 7: earlier readings untouched); the settled
  values go to d1a/settled.tsv.
