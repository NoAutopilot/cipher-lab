# NV05E pre-registration ADDENDUM (N8-NV05, account-2 worker for LANE-NEAR8), 4 Oct 2026, written ~16:25 UTC before any new read

Pushed before any new gloss pass is run or any re-score computed. NV05E's registered FAIL (S 0.430 vs value-shuffled
p99 0.186; gate S > p99 AND S >= 0.60) stands as the record of that run whatever this re-score gives.

## Unchanged (PREREG.md)
Statistic S (../control_fr3641/score_control.py score(), imported), normalisation and abbreviation table (NV05C's
fixed table), control (values shuffled among the 95 coded rows, 1000 draws, seed 1), gate (PASS iff S > control p99
AND S >= 0.60), cipher side (ciphertext.tsv as reconciled by NV05E, unchanged, `decode_key --check`), key
(key_syllabary.tsv, unedited), scope (f.228 L01-L04 only). The language judge is re-reported, secondary, unchanged.

## The one change: the gloss
gloss.tsv (pass G, one Sonnet read that stopped short on L01, L03, L04) is replaced for the re-score by gloss_v2.tsv:
- New crops cut for the gloss itself, not the cipher: `tools/iiif_lines.py` on canvas 235, region 5250,640,3700,640
  (starts 100 px higher than NV05E's region, so the L01 gloss's left start at the old region's top edge is inside),
  bands centred on the gloss lines (between cipher lines), segments <= 1900 px with overlap, native resolution.
  Command and debug overlay pasted in NOTES.md before the first read.
- Two blind Sonnet passes (GA, GB), one subagent call each on all gloss crops, told: the gloss is the faint cursive
  Spanish line ABOVE the bold cipher line, it runs the FULL width of the line across all segments (segments overlap,
  boundary given), read every word left to right, mark unread spans [..], mark abbreviations as written (q, q~, qe,
  V.M. ...) without expanding, no guessing from context. Neither pass sees the decode, the cipher reading, pass G,
  NV05E's NOTES or the other pass.
- Reconciliation (1 unit, by this worker on the crops): disagreements only, settled from glyph shape; where unsettled,
  the span is [..] (dropped from scoring). Disclosure: this worker has read the decode, gloss.tsv and NV05E's
  post-score looks at the crops ("tarde como vs", "lo que bivan los deach[..]", "por ello tan de buena gana como por")
  before writing this file; that is why the two passes are blind and the worker settles only A/B disagreements, never
  adds words neither pass read.
- Convention (rule 3 PX-BRODEC): gloss_v2 text is normalised to the decode's convention only by (a) score_control's
  existing norm() + abbreviation table, and (b) one fixed extra rule, stated now: a reader-marked abbreviation is
  expanded only by this list -- qe/qȷe -> que, ql/qel -> que el, dho/dha -> dicho/dicha, V.Md/V.Mg -> vuestramagestad,
  p/p~ -> por/para left as written (not expanded). Unread [..] spans are removed. Nothing else is edited.

## Why the control still discriminates
A longer gloss raises the chance an LCS match lands; the value-shuffled control is scored against the same gloss_v2,
so its p99 moves with it (it can differ from the target on S: values change which letters the tokens decode to).
Both S and p99 are reported side by side with NV05E's.

## Reporting
score_v2.tsv by `score_f228.py --gloss gloss_v2.tsv --out score_v2.tsv` (same code path; `--check` for both
score.tsv and score_v2.tsv). PASS or FAIL is written as is. If PASS: price the next 4-line batch in the Verdict, do
not start it. If FAIL: the gloss-read explanation is tested and the next step names a different instrument.

## Units and stop rule
3 units (GA, GB, reconciliation). Cap USD 3, box to 17:01 UTC; no unit started past 80% of either.
