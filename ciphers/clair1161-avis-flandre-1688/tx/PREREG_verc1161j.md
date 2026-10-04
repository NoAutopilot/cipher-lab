# PREREG-VER-C1161J: selection-matched nulls for the nine C1161-JOINT9 values (4 Oct 2026, account-3 verifier)

Written and pushed before any score below is computed. Disk only. Brief `.claude/briefs/runs/2026-10-04-acct3-ver-c1161j.md`.
Script `two/verc1161j.py`, output `two/verc1161j.tsv`. Baseline key = `two/key_pre_joint9.tsv`; nine = K s, iib d, l f,
ls m, o m, rot h, spiralG n, to s, x f. G and J exactly as in two/joint9.py (glossctl stat on the c186R block vs the 170
gloss letters; fr16 judge NgramModel.score on the 3375-letter decode).

Facts established before scoring (read from disk, no statistic computed):
- The gloss text is not an input of the LOLO anneal (two/reanneal.py stage 1 = fr17 4-gram on the cipher stream only).
- The c186R-dropped LOLO stream (`two/lolo/key_lolo_tgt_c186R.tsv`, which never saw the glossed block's tokens) carries all
  nine proposed values. So the value choice does not depend on the c186R tokens; G is out-of-sample for that stream.
- J (an fr16 n-gram French model) and the anneal objective (fr17 4-gram) measure the same thing; a dJ gain from values chosen
  to maximise French 4-gram fit is expected whether or not the values are right. dJ is therefore declared NON-EVIDENTIAL for
  the grade, reported only.

Tests (one run each, no re-tuning):
- T2 content-specificity null (the main confound: moving tokens from e/n/s onto m/d/f/h raises agreement with any French
  text): dG_w = stat(dec_nine, w) - stat(dec_pre, w) for 200 windows w of len(gloss) letters drawn from the fr16 judge
  corpora (random.Random(1), same construction as glossctl `windows`). Pass iff real dG > p95 of dG_w (190th of 200).
- T3 selection-matched best-of-K null: 50 draws (seeds 1..50); each draw samples K = 2000 nine-value tuples, every value
  uniform over a-z, keeps the tuple with the highest fr17 L4 (reanneal.py's L4 on the full stream, other signs at the
  baseline key), and records its dG and dJ. Pass iff real dG > p95 (48th of 50) of the selected tuples' dG. The selected
  tuples' dL4 is reported beside the real nine's: if the null's selection is much weaker than the anneal's (mean dL4 well
  below real), T3 can falsify but a T3 pass is weak, and is said so.
Decision: the nine keep grade S iff T2 AND T3 pass. Otherwise all nine go back to M in key.tsv (values may stay as the
working reading only if the verifier states why; grade M either way). Rule 3 check: both nulls change letters G depends on
(T2 changes the reference text, T3 the nine signs' letters), so either can sit above or below the real value.
