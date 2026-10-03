# AVS175 pre-registration (3 Oct 2026, ~15:07 UTC, worker AVS175, account 2, LANE-A2PUSH3)

Committed before any read of WVO 175 at native resolution (00175.pdf fetched to the scratchpad, 10 pages, 355-389 ppi).

Runs: the glossed cipher runs of WVO 175 pp.1, 3, 4, 5, 6, 8 (f.348r, 349r, 349v, 350r, 350v, 351v; A2-AVS-2's run list);
p2 is left out (no 'wir'/'Fürsten' gloss reported there). Only cipher signs with a gloss over them enter the alignment.

Sign questions (126's M left on key_98):
- Q1 NW (word sign, 98 'wir' n=1 M): does NW occur under a gloss 'wir'?
- Q2 Qf (98 'f' n=2 M): is the sign under gloss f (e.g. 'Fürsten', glossed 3 times) Qf, and where Qf occurs is the gloss letter f?
- Q3 K (word sign; 124 'der' n=1, 126 'die' by context): what article does the gloss give at each K?
- Q4 sign 1 (98 h; 124 once i): at each sign-1 position, is the gloss letter h or i?

Reads: 2 blind reads of the cipher runs (one subagent call each, line crops only, from `tools/iiif_lines.py --image`), 1 reconciliation
(by this worker against the crops), 1 gloss read (gloss lines only). A gloss letter is H-read only where both the gloss read and the
reconciliation agree it is legible.

Statistic: gloss-letter agreement = share of the cipher's single-letter sign positions (key_98 letter signs, word signs excluded) whose
aligned gloss chunk equals key_98's value (u=v), from `tools/interlinear_align.py align` with signs mapped to numerals (letter signs
< 100, word signs >= 100), `--prior` key_98 letter values, `--keep-fs`. For Q1-Q4 the statistic is the aligned chunk at the sign's positions.

Controls (>= 200 draws each, same tool, same flags): (a) rotated gloss: each run's cipher paired with the gloss of the run k places on
(k = 1..n-1, cycled to 200 draws with a fresh letter-offset each); (b) shuffled gloss: each gloss line's letters permuted (seeded). The
control can differ from the target: a gloss that does not belong to its cipher run cannot agree with key_98 above chance.

Gate: system test PASS if real agreement >= 0.60 AND above the p95 of both nulls. A sign value moves to C only if the gate passes, the
gloss at that position is H-read, and every aligned occurrence of the sign in 175 gives the same value (n >= 1); a split stays M and is
logged as a data conflict (rule 4). If the gate fails, nothing is regraded.
If fewer than 3 glossed runs are readable at native resolution, stop and log "too-short".
