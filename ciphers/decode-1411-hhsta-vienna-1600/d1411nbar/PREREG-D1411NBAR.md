# PREREG-D1411NBAR -- noise-matched gloss bar for the de1600 coverage of frozen T21r (10 Oct 2026, account 2)

Brief D1411-NBAR (LANE FAMILY-A2o, account 2). Written and pushed in its own commit, with the scorer `d1411nbar/nbar.py`, before any
noisy-bar number is computed. Disk only; no new reads, no image work, no table change.

**Question.** D1411-POOL compared de1600 word coverage of the decoded pooled independent numerals (p.4+p.5+p.6, N=308; T21r 0.513,
order-shuffle p99 0.458, shifted max 0.393) against the coverage of the leaf's clean gloss text (`gaps150/gloss_text.txt`, 63 letters,
0.6129). The decoded numerals carry reader error; the gloss does not. What coverage would a CORRECT table reach on THIS transcription?

**Known before writing (stated, not hidden).** T21r pooled 0.513, shuffle p99 0.458, shifted max 0.393, gloss bar 0.6129 (D1411-POOL).
No noisy-bar number has been computed by anyone.

**Reference text.** `gaps150/gloss_text.txt` (the file `score_pool.py` reads) repeated to length 308: `(g*5)[:308]` (63 x 5 = 315).
The clean coverage of this tiled text and of the single 63-letter copy are reported (calibration, not gated).

**Encoding through frozen T21r** (`def1411/tables.py`, primary letters `t[r][0]`, alphabet as table; the gloss contains no letter
outside it). For each letter: a residue drawn uniformly from the residues whose T21r letter equals it (s: 2/12/22; g: 11/20; others
single), then a number drawn uniformly from the pooled N=308 independent numbers (`d1411pool/score_pool.material()`) having that
residue; if none has it, uniformly from 1..100 with that residue. Fresh encoding per seed.

**Error model (primary, gated): substitution only.** Each number independently, with probability r, has one of its digits (chosen
uniformly) replaced by a uniformly drawn different digit; a result of 0 is redrawn. Errors can hit any number (no number class is
spared). **Secondary (reported, not gated): substitution + split/merge** -- error events at rate r, of which 70% substitution as
above, 15% split (a two-digit number becomes its two digits as two numbers; a one-digit number gets a substitution instead), 15%
merge (a one-digit number joined to the next number's digits if the result is <= 100; otherwise a substitution).

**Rates (bracket spanning the folder's own figures).** Measured pass disagreement on aligned numbers: p.3 11.6% (38/328), p.4 13.0%
(33/254), p.5 12.3% (34/276), p.6 10.9% (15/138); pooled p.4-p.6 82/668 = 12.3%; two independent transcriptions of the p.2 text
(p.2 vs p.5 copy) differ on 13.7% (13/95, including genuine copy variants). Registered: **low r = 0.06** (about half the disagreement:
the reconciled reading if the two passes erred independently), **central r = 0.123** (pooled p.4-p.6 disagreement), **high r = 0.25**
(twice central; covers the 13.7% copy figure and common-mode errors both passes made, e.g. p.6's three merged splits).
Descriptive sweep (reported, not gated): r in 0.00, 0.03, ..., 0.40 at 200 seeds each.

**Seeds.** 1000 per registered rate, `random.Random(1411 * 100000 + k)` for k = 0..999 (the rate index enters the seed as
`+ 10**7 * i`, i = 0 low, 1 central, 2 high, 3+ sweep; 4 secondary model).

**Per seed** (same encoding, independent noise draws per arm):
- noisy gloss: encode, inject, decode with T21r, de1600 `cover` (`judge_plaintext.NgramModel.cover`, the corpus `LANG_CORPORA["de1600"]`
  exactly as `d1411v/rescore_v.score`).
- noisy shuffle (control): the same encoded numbers in a seeded random order, then injected and decoded with T21r.
- noisy shifted (control): the noisy gloss numbers decoded under each of the 23 shifted rules (shift 1..23, `score_p5.dec`); max of 23.

**Bar statistic.** B = 5th percentile of noisy-gloss coverage at central r (1000 seeds).

**Informativeness check (rule 3: the control must be able to differ).** At central r: B > p99 of noisy-shuffle coverage AND B > p99 of
the per-seed noisy-shifted max. If either fails, the bar falls to control level and the outcome is **NON-TEST** whatever T21r scores.

**Decision rule (T21r pooled 0.513, already known).**
- **PASS** iff informative AND 0.513 >= B: "the coverage gap to the clean gloss is explained by reader error at the measured central
  rate". No S grades written; one ROOM line asks the lane for a verifier.
- **FAIL** iff informative AND 0.513 < B: the gap is not explained by reader error at the central rate under this model.
- **NON-TEST** iff not informative.
Reported beside the verdict, not gated: B, median and p95 at low and high r with their own control checks (a FAIL at high r is a
stronger negative; a PASS only at high r is reported as such, not as PASS); the percentile of 0.513 in the central noisy-gloss
distribution; the rate at which the sweep's noisy-gloss median falls to 0.513 (linear interpolation); the secondary model's B at
central r; noisy-shuffle p99 beside the real pooled shuffle p99 0.458 (sanity).

**Limits stated in advance.** Uniform digit substitution is not the hand's look-alike structure (4/5, 7/2, 1/2, 5/3); any residual
table error is not modelled (by design: the bar is what a correct table reaches); one 63-letter gloss repeated is a narrow reference
text (its clean coverage is reported so the reader can see the length effect).

`python3 d1411nbar/nbar.py` writes `d1411nbar/nbar.json`; `--check` exits 1 if it is stale (rule 7).
