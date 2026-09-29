# R2-1 ORDER-DOSE: pre-registration (written 29 Sept 2026 07:1x UTC, before any real-text score in this folder)

Worker DEB-SWARM2-R2-1 (for the orchestrator). Public copies only; settled drafts; CPU only. No key is fitted or
scored here, so HARNESS-2's refit null does not apply to this prompt (it gates key scoring); nothing here is a reading.

Instrument: `swarm/G-D/dcore.py` imported unchanged -- the frozen score (z mi1 + z bigram types >= 2 + z repeated
3-grams - z doubled, per text; pair = both texts + both held-out transfer z). Only the threshold is re-picked, per
text, by D's own `threshold.py` rule (maximise balanced accuracy, NULL-IID vs the language designs) on this folder's
regenerated calibration at the decision noise below: that is D's procedure applied at a new shape, not a retuning of
the score.

Texts (`r21.py texts()`): **a** = (c3, c4) N 107 + 263, K 100; **b** = (c1, c2) with PCT-SLASH->PCT, X-DOT->X,
X-CURL->X, N 125 + 643, K 130; **c** = (c1, c2) with BAR-SOLID, BAR-THIN, DASH-V also dropped (BLOB, HOOK-L, DASH-H
already dropped by `dcore.target`), N 117 + 619; plus **raw** = D's own (c1, c2) reading, to measure what the indel
noise model alone does to D's margin.

Known-answer control (per text): 40 pairs each of FR-HOMO, EN-HOMO, PT-HOMO, LA-HOMO, FR-SYLL and NULL-IID, made at
the text's own line lengths and joint sign curve, one key per pair; noise = rate p per token, of which 3/4 replacement
and 1/4 insertion/deletion (half each), replaced/inserted signs half fresh ids, half from the curve. Noise levels bracket
the measured error (CLAUDE.md rule 3, SALV-DIAG): text a 0.10 / 0.15 / 0.20 (floor 8.5-10 pct, H53); texts b, c, raw
0.15 / 0.20 / 0.25 (floor 14-17 pct, H51: true error plausibly 20 pct or more).

**Decision noise** (fixed now): a 0.15; b, c, raw 0.20 -- each one step above the measured floor, because H51/H53 say
the floors undercount.

**Control gate:** an arm counts only if, at its decision noise, the pair score separates the five language designs
from NULL-IID at balanced accuracy >= 0.80 (threshold chosen on those rows). Below the gate the arm is a non-test.

**Real score:** median pair score over 5 shuffle seeds x 400 trials (as D's `target_score.py`).

**Kill test (stated before looking):** the structural negative stands (kill MET) if every gated arm among a, b, c
scores NULL -- real median pair score <= its threshold AND at most 5 of 40 pairs of every language design score as
low as the real text at the decision noise -- and at least text a passes its gate. If any arm scores above its
threshold, the kill is NOT met and that arm is flagged as an order signal for the orchestrator (not a reading). If
text a fails its gate, the kill is NOT met ("c3+c4 too short for the instrument"), whatever b and c show.
Secondary, reported not gated: the c2-alone score (b, c) and the pooled single-text score; the raw arm's calibration
against D's original replacement-only margin (0-1 of 40 as low as real at 15 pct).
