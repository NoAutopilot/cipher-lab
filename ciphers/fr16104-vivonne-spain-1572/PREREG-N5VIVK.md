# PREREG N5-VIVK (4 Oct 2026, written before any decode of f.103r is compared with any plaintext)

Worker N5-VIVK (account 2, for LANE-NEAR5). Brief: .claude/briefs/runs/2026-10-04-ytbiz-near5-wave1.md "N5-VIVK".
Pushed before the cipher transcription of f.103r is reconciled and before any decode of it exists.

## Material
- Cipher (fr.16105, ark btv1b9009663p): training = f.102r (canvas 105 right) + f.102v (canvas 106 left); held-out = f.103r
  (canvas 106 right), cipher lines L01-L37 only (L38-L40 are the plain "Je baise ..." subscription and are excluded).
  Line crops: images/c105_f102r_*, c106_f102v_*, c106_f103r_* (tools/iiif_lines.py commands in NOTES.md "N5-VIVK").
  Each page: two blind Sonnet passes (tx/<page>_passA.tsv, _passB.tsv), tools/reconcile_passes.py, reconciliation by
  the worker from the crops -> tx/<page>_rec.tsv (wide format). Sign labels: tx/SIGNS.md.
- Plaintext: the clerk decipherment ink 41 ("dechiffre de la precedente"), fr.16105 ff.106r-108v (two blind passes per
  page, merged by the worker), normalized to tx/dec_norm.txt: lowercase, letters a-z only, accents stripped, u/v folded
  to u, i/j folded to i, abbreviations expanded. The decode output is normalized the same way (j->i, v->u).
- Published key: key_tomokiyo.tsv (S. Tomokiyo, Cryptiana henryiii.htm, image henryiii_Vivonne1.png, the 1572-74
  Saint-Gouard cipher), mapped by the worker onto the SIGNS.md labels before any decode was run.

## Token preparation (both arms, identical)
Drop [PLAIN:...], DUP rows, [...] stretches; strip a trailing "?"; keep {..} tokens as their own codes; collapse each
adjacent pair "o o" to the single code "oo" (Tomokiyo col u), left to right.

## Fixed alignment and statistic
Tool: tools/stream_align.py (also reachable as `tools/interlinear_align.py stream`), defaults band 150, step 300,
iters 3, gap_sym 1.5, gap_let 1.5, alpha 0.5, seed_win 12, first 200.
- Training start anchor j0: the offset into dec_norm.txt that maximizes stream_align.nw_score of the Tomokiyo decode of
  the first 80 training codes against dec_norm[j:j+120], j over the whole text. (This uses the published key for the
  start offset only; disclosed as a limit on Arm A's independence.) If the best offset's score is under 0.30 the anchor
  is reported as unfound and the worker falls back to the proportional estimate stated in NOTES before running.
- Training span: dec_norm[j0:] (end free on the clear side). Training end jend = j0 + the last matched letter index of
  Arm A's final path.
- Held-out plaintext span H = dec_norm[jend-50:] (to the end of the decipherment, "... de ses necessitez"); the 50-letter
  margin absorbs a slightly early training end; nw_score has free leading/trailing clear-side gaps.
- Statistic: stream_align.nw_score(decoded f.103r codes, H) with its defaults (match 2, mismatch -1, gap 1, band
  max(200, |M-N|+200)) = identical aligned pairs / number of f.103r codes. An unread code (-1) counts as a miss.

## Arms
- Arm A (C, independent of the published key except j0): stream_align.learn on the training codes vs dec_norm[j0:],
  flat start (the tool has no prior), key frozen = decode(counts, min_count=1); f.103r codes unseen in training = -1.
- Arm B (published key): decode f.103r codes with key_tomokiyo.tsv; codes not in it = -1. No training.

## Nulls (200 draws each, numpy default_rng(20261004))
(i) shuffled key: the arm's meanings permuted across the arm's keyed codes (the set of codes that have a value), then
    f.103r decoded with the permuted key. (ii) shuffled order: f.103r code order permuted, same key.
Both can move the statistic (key permutation changes which letters appear; order permutation destroys sequence while
keeping letter frequencies).

## Pass rule
An arm PASSES if its real statistic is greater than the 95th percentile of BOTH of its nulls. Ceiling check: if either
null's median is >= 0.95 that arm is VOID (no headroom), whatever the real value. Both arms are reported side by side,
with the null medians and p95s. Also reported: per-code agreement of Arm A's frozen key with key_tomokiyo.tsv on codes
with >= 3 training occurrences (count agreeing / count compared, and the list of disagreements).

## After
At least one arm passes -> key.tsv for this target: Tomokiyo values, with C counts from Arm A where they agree,
disagreements listed and not settled by majority (rule 4); stop (fr.16104 ff.157-159v is wave 2).
Both fail -> numbers to HYPOTHESES.md as a known-plaintext test, next step named, stop.
Script: tx/vivk_test.py (committed with the result). Transcription error is reported per page as err_2reader.

## Amendment 1 (4 Oct 2026, before any decode of f.103r exists or is compared)
Training-side evidence only: the Tomokiyo decode of f.102r (rec draft) reads "particularitez du siege et du secours ...
conte de Montgommery" and "avoit tres bien considere" (f.106r lines 2-6 of the decipherment) about 14 cipher lines into
f.102r, preceded by "nulle esperance" / "reconciliation", which are not on ff.106r-106v. So f.102r starts on f.105v.
The plaintext is widened by that one page (the brief's allowance): dec_norm.txt = ff.105v-108v (canvas 109 left -
112 left), same normalization. Nothing else changes (anchor rule, statistic, arms, nulls, pass rule).
Cipher reconciliation (tx/reconcile_vivk.py) uses only label rules fixed on f.102r/f.102v crops before any f.103r decode.
