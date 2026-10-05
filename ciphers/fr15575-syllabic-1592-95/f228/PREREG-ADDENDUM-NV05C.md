# f.228 B2 (L05-L08) gloss re-read, pre-registration ADDENDUM to PREREG-ADDENDUM-N8B (RUN6-NV05C, LANE-RUN6 account-1 worker), 5 Oct 2026 04:47 UTC by `date -u`

Pushed before any gloss call of this job. Instrument change named by N8-NV05B's rule-3 note and NEAR8: per-band calls (one
gloss line per Sonnet call, anchored by the cipher line under it) on three views of each crop, voted. Not a new threshold.
Disclosed: this worker has read NOTES.md, which carries the N8-NV05B reconciled gloss and its post-score look at the decode.
That is why the gloss below is built mechanically from the blind reads (vote rule), with no hand settlement of words.

## Unchanged (PREREG.md + ADDENDUM-N8 + ADDENDUM-N8B)
Statistic S (`../control_fr3641/score_control.py` score(), norm(), abbreviation table; `build_gloss_v2.py` clean()), key
`key_syllabary.tsv`, tokeniser, ciphertext `ciphertext_b2.tsv` (unchanged, not re-read), control (values shuffled among the
95 coded rows, 1000 draws, seed 1), **gate PASS iff S > control p99 AND S >= 0.60**, gated number = L05-L08 alone; pooled
L01-L08 reported ungated. Crops unchanged: `images/b2/f228b2_L0{1..4}_s{1,2}.jpg` (= leaf L05-L08).

## What changes (the instrument only)
- Views: `tools/iiif_lines.py --views pad,s125,contrast --views-of images/b2/f228b2_L0*_s*.jpg --out <scratch>/nv05c`
  (byte-identical on re-run; views kept in scratch, not committed).
- Reads: one Sonnet call per (line, view) = 4 lines x 3 views = **12 calls**; each call sees only that line's two segment
  crops in that one view, plus the anchor (the bold cipher line's opening signs from cipher pass A: L05 "57 90 8917",
  L06 "50 97348 (188025", L07 "56 9 24:3283", L08 "∞o2 1661 18:7345"), told to transcribe only the faint cursive line
  directly ABOVE that bold line and nothing below it, write the overlap once, `[..]` for illegible spans, `?` after a
  doubtful word. No call sees the decode, any other read, gloss*.tsv or NOTES.md. These 3 reads per line are the
  "2 passes x view-set" of the brief, widened to 3 so the vote has a majority (budget allows 12 calls, not 24).
- Vote (mechanical, = the reconciliation unit): per line, the three reads as word sequences in `tools/reconcile_passes.py`
  wide format (pass order pad, s125, contrast), `--vote`; a column's word is kept iff vote_share >= 0.66 (2 of 3 agree
  after lower-casing and stripping a trailing `?`); every other column -> `[..]`. The voted line -> `gloss_c_diplomatic.tsv`
  -> `build_gloss_c.py` (clean() imported) -> `gloss_c.tsv`. No word is added, moved or settled by hand. The only manual
  step allowed: if a read plainly transcribes the line below the bold line (its own note says so), that read is dropped
  for that line and the line is voted on the remaining reads with 2 of 2 required; reported if used.
- Units: 12 calls (~USD 0.25-0.35 each) + 1 vote/reconciliation; self-stop before a unit that would cross 80% of USD 5.5
  or 75 min.

## Reporting
`score_c.py` (score_b2.py with gloss_c.tsv): L05-L08 S, p99, mean, max, >= real, gate; pooled L01-L08 ungated; per line;
beside N8-NV05 L01-L04 PASS 0.674 and N8-NV05B L05-L08 FAIL 0.439. If FAIL: third attempt on this pair of leaves/instrument
family (rule 3 third-attempt clause) -> the gloss-read instrument is logged [retired] for f.228 B2, next step new material
(AGS Estado leg. 609 fol. 86). A PASS licenses nothing beyond B2's gate (C grades only where the gate PASSes; the
decode itself is H/U per VERIFY-NV05 and does not change).
