# PREREG-VIVF191D -- a 5-pass reconciliation rule for f.191r L22-L36 (registered before any run)

Registered 15 Oct 2026, 04:5x UTC by date -u, worker VIV-F191D (account 4, LANE VIV-KEYSTONE). Brief:
.claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md, JOB VIV-F191D. Disk only; no new reads, no key, reading or
status.json edit. Pushed before `f191.py --five-pass` exists or runs.

## 1. Material
Passes A, B (tx/f191r_passA/B.tsv), C, D, E (tx/viv63_f191/f191r_passC/D/E.tsv), each through f191.clean(). E covers
L22-L36 only (VIV-F191C: drift check 15/15; noisier than A-C). D is the drifted pass on these lines (VIV-F191C NOTES).

## 2. Columns
On L22-L36 only: star alignment on A exactly as f191c_report.cols5 (NW of B, C, D, E each against A; insertion columns after
the same A sign paired by order within each pass). A column in which A, B, C, D are all '-' (an E-only insertion) is dropped
before any decision. Every other column's A-D votes are identical to f191.cols() (the E column is added, nothing else moves).
Lines outside L22-L36: unchanged, f191.cols() + f191.decide() as committed.

## 3. Rule (exact decision table; v = counts over the five votes A B C D E, '-' a value; E has weight 1, the same as D)
| case | condition | result | flag | how |
|---|---|---|---|---|
| R1 | top count >= 3, top sign != '-' | top sign | 0 (settled) | maj5 |
| R2 | top count >= 3, top = '-' | column dropped | -- | drop5 |
| R3 | pattern 2-2-1 (two values with 2, one with 1), f191.decide(A-D) returns how = rule or drop | decide's result | decide's | decide's |
| R4 | pattern 2-2-1, decide(A-D) flagged (plural/tieCD/tieA/tie), E == C, C != '-', and C is one of the two 2-vote values | C | 1 (flagged) | tieEC |
| R5 | pattern 2-2-1, otherwise | f191.decide(A-D) | decide's | decide's |
| R6 | any other pattern (2-1-1-1, 1-1-1-1-1) | f191.decide(A-D) (E ignored) | decide's | decide's |

A 2-2-1 is never settled by E: only R3 (A-D's own registered rule pair, or A-D's strict '-' plurality) settles it. E breaks a
tie only toward C and the result stays flagged (M). Then the existing 'o'+'o' -> 'oo' merge, key, grading as f191.build().

## 4. No-liberty clause
No position may be settled by E alone: (a) E-only columns are dropped (s.2); (b) R1/R2 need at least two of A-D with E;
(c) R4 never clears a flag; (d) E never introduces a sign that no A-D pass read (R1 needs >= 2 A-D votes for the sign; R4
picks C). A position settled at R1 with exactly 2 A-D votes + E is reported in a separate count ("E-decisive") and every
flip is listed with its five votes.

## 5. Gates (before = committed rec.tsv, i.e. the 4-pass build `--check` certifies; after = the 5-pass build)
Same instrument as f191.stats(): longest all-H run on f.191r; V_strict top-1 / top-3 mean against the 200-shuffle null (seed
f191.SEED); b2 and wrong-key gates with controls C1 (f103r) and C2 (ink 54) at 200, unchanged. Recorded before: longest all-H 37
(L10-L11), V_strict top-1 21 (null p99 19), top-3 mean 17.67 (stats_packet3.json 'before').

## 6. Decision (PREREG-VIVPACKET3 s.5, unchanged)
A stretch >= 42 letters all H (no M/U inside) on the 'after' build goes to a verifier (rule 7 re-derivation); otherwise logged.
A gain in longest all-H run below 42 is logged as a number, not a reading. rec.tsv and decode.tsv stay untouched; the 5-pass
build writes rec_5pass.tsv, decode_5pass.tsv, stats_5pass.json (and owner_questions_5pass.tsv from the shared stats()).

## 7. Reports
Positions settled (flag 1 -> 0), flipped (sign differs from rec.tsv at the same column), still flagged, dropped; E-decisive
count; every flip with its five votes; before/after gate numbers.
