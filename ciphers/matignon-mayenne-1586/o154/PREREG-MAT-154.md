# PREREG-MAT-154 (15 Oct 2026, 15:1x UTC by date -u; account-4 worker MAT-154, LANE DEFAULT-A4-1441-15)

Written and pushed before any reader call and any score. Brief: `.claude/briefs/runs/2026-10-15-acct4-default-1441-jobs.md` job MAT-154
(MAT-ORL's named next: shape-sort f.154's own `o` tokens from 3x per-token crops with 2 blind Sonnet readers, then `decode_key.py --try oB=a`
on f.154 with MAT-ORL's power controls). Disk-first; `tools/prior_work.py` run before the first priced step (`o154/prior_work.txt`, exit 2
KNOWN = Tomokiyo's published opening of f.154, which this job does not use; leaf look rows appended to look.tsv by the tool).

## Material (done before this PREREG; no score)
- BnF fr.15572, `ark:/12148/btv1b9061879d`, canvas 161 = f.154r (gallica_folio anchor 161=154r; foliation "154" seen on the 1600 px
  overview). openapi.bnf.fr requests: 1 overview (full/1600), 1 region `pct:52.5,32.5,42,64.5/max` (3579x4090, sha1 3416510e...).
  `o154/regen_o154.sh` re-fetches; images in scratch only.
- `o154/lines154.py`: region levelled by the common slope of the `iiif_lines.py --follow-slope` fits (-0.0163), row ink profile ->
  **28 line centres = Bourdeau f154-1..28** (checked by eye at both line ends). Bourdeau f154-1's first 6 tokens (`4+ g g x .v. 14`) sit
  at the end of the clear line above the strip, so line 1's positions are shifted by 6 (n = 39 on the strip).
- **Tokens: all 47 `o` tokens of `ciphertext.txt` f154** (`o154/tokens154.tsv`: id, line, position).

## Crops and readers
- `o154/crops154.py`: per token, sign columns from the strip's column ink profile (read-free), the column estimated proportionally from the
  position, window = estimate +- 4 columns, upscaled 3x, no marker (the o3x_crops.py recipe). Each crop comes with Bourdeau's LABEL
  sequence p-4..p+4, the target shown as `[id]` (labels only, no values, no gloss).
- **Exemplars:** from the f.91 consensus set (`osplit/sort_answers_r2cons.tsv`, both readers agreed, high confidence), the first three
  ids in sort order per shape (A, B), regenerated with `osplit/o3x_crops.py` from `f91/regen_f91*.sh` (2 more openapi.bnf.fr requests,
  total 4, the brief's limit); plus MAT-BOX's words: A = "a small plain closed round o", B = "round with a right stem or tail".
  If the exemplar fetch fails, words only (declared deviation).
- **Readers:** two independent Sonnet subagents (R1, R2), each in 2 calls (lines 1-14, lines 15-28; <= 40 crops per call), given only
  opaque ids, crop paths, the label context and the exemplars; answer A / B / X per id with high/low confidence; unanswered = X. Neither
  sees the other's answers, any value, any gloss. Output `o154/answers_r1.tsv`, `answers_r2.tsv` verbatim.

## Agreement rule and kappa gate (gating)
- **Consensus label:** both A -> oA; both B -> oB; anything else -> X (stays `o`). Low-confidence A/B answers count as given.
- **Gate K:** Cohen's kappa on the tokens both readers called A or B >= **0.6**, AND at least **24 of 47** tokens called A or B by both.
  If K fails: the sort is reader-dependent on f.154; **no --try** (non-test by construction); next step = the owner's sign sorter.
  Kappa over all 47 on A/B/X is reported, not gating.
- **Too-short:** consensus oB n < 5 -> oB=a not run (too-short); same for oA.

## --try (only if gate K passes)
`o154/make154.py build DIR`: a decode_key-ready copy of the 28 f154 lines from ciphertext.txt, consensus `o` relabelled `oA` / `oB`
(both unkeyed), X stays `o` (key i, H); key.tsv and decode.json copied unchanged. Then
`tools/decode_key.py DIR --try CODE=VALUE --lm fr16 --window 8 --nulls 100`, default acceptance, one code per call.
- **Power control first** (MAT-ORL's recipe; wrong letter of the same class, next letter, wrapping): **n=m** (n=l, 37 on f.154),
  **c=q** (c=p, 23), **s=a** (s=u, 15), and in place of **oo=f** (oo has 0 tokens on f.154, declared now) **e=s** (e=r, 17, consonant).
  **Gate P:** if any of the four is `accept`ed, the scope is a non-test on f.154 and no candidate is licensed.
- **Candidate (gating): oB=a.** Reported only: oA=i, and the swaps oA=a, oB=i.
- **Grade rule:** oB=a `accept` with gates K and P passed -> **S for the f.154 oB tokens only**, in HYPOTHESES.md and NOTES.md. Reject ->
  oB stays `o` = i (H, Bourdeau) on f.154 and the f.91 result is logged as not reproduced on this leaf (M). **No key.tsv, ciphertext.txt,
  reading or grade edit in any outcome** (the brief: never edit files another job may touch; a relabel of ciphertext.txt is a separate
  step after this test). This is the first --try of the o shapes on a target leaf (MAT-ORL ran the f.91 copy only).

## Stop rules
Cap USD 7, box 15:12-16:42 UTC; no unit started past 80% (5.6 / 16:24 UTC). openapi.bnf.fr <= 4 requests total, ROOM take/release.
