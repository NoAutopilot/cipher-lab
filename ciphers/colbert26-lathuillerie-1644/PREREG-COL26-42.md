# PREREG-COL26-42 (account 4, LANE DEFAULT-A4-0935, 13 Oct 2026): per-code test of 42 = s(ieur)

Registered before any score is computed. Scripts and disk only; no images, no network.

**Hypothesis.** H1: code 42 = s(ieur) (written "S.", "s.r", "Sr", "sieur"). Competing value H0: 42 = si (key_period.tsv lead, grade M).
Source of H1: COL26-C29 (13 Oct 2026), post hoc: all three canvas 29 occurrences of 42 sit under "S." (U03, U16, U18). Canvas 29 is
therefore the discovery set and is excluded from scoring.

**Held-out occurrences.** canvas 20-21 (interlinear/c20c21_reconciled.tsv: c20U02, c20U05a, c20U05b, c20U09; 4 occurrences) and f.24
(interlinear/f24_reconciled.tsv: U09, U10; 2 occurrences). N = 6. Disclosure: the glosses over these six were already printed in
NOTES.md (D07-COL26K, 7 Oct 2026), so the set is held out from the H1 discovery, not blind to its content. Canvas 20-21 is also the
discovery set of H0 (si), so H0 is circular there.

**Statistic.** Per occurrence, a hit for value v if a v-token appears in the unit's gloss within +-0.25 of the occurrence's relative
position (D07-COL26K's positional statistic, interlinear/c20c21_positional_k26.py). H1 tokens: a gloss word matching
`(?i)sieur|s\.|sr|s\.r` (whole word); H0 token: "si" (letters only, as D07-COL26K). Contrast D = H(H1) - H(H0) over the 6 occurrences.

**Control and gate.** Rotation control (each unit's gloss rotated circularly, 20000 draws) and a value-shuffle control (42's six
positions replaced by six random token positions in the same units). PASS for H1 iff H(H1) > p95 of both controls and P < 0.05.

**Power check (run before scoring, decides whether scoring runs).** For H1 to be testable the held-out glosses must contain at least
one H1 token somewhere, otherwise H(H1) = 0 on the target and on every draw of either control by construction (rule 3: a control that
cannot differ from the target licenses nothing). Check (regex above over every gloss of both files, not only 42's units): if zero
units carry an H1 token -> **NON-TEST, stop; do not score.** The contrast D then reduces to the H0 test, which is circular on canvas
20-21 and HELD-OUT-UNDERPOWERED on f.24 (N 2, D07-COL26K) -- not rerun here.

**Power check result (13 Oct 2026, 09:47 UTC by date -u):** canvas 20-21 20 units / 222 tokens, f.24 11 units / 168 tokens: **0 units
carry an H1 token.** Verdict: **NON-TEST**; no score computed; key_period.tsv and every key file unchanged.
