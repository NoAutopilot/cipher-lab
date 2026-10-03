# FT4ac pre-registration (account-4, 3 Oct 2026, written 17:5x UTC by the clock, pushed before any run of align/ft4ac_scan.py)

Step (FT4ab's next, ROOM 17:34 UTC): single-release scan on f.206 ALONE. Hypothesis pins, one at a time:
H-T = 338 tou (f.216v's unique value), H-C = 534 che (S1's unique value); always 121 s (C, VERIFY-ROU121) and the C pins
22 de, 66 r, 581 au. Both H-T and H-C are already known nofit on f.206 alone (FT4ab secondary). Question: which ONE f.206 key
row, released, restores f.206's exact fit under that hypothesis.

Instrument: FT4x/FT4z/FT4aa/FT4ab exact (0-edit) CP-SAT (ft4x_pool.solve_exact), unchanged; MAXLEN 12, 30 s per solve.
Candidate rows: the f.206 rows the model constrains -- pinned 22, 66, 581, 121 and repeated 279, 336, 501, 722 (8 rows; the
hypothesis code itself is never released; single-occurrence unpinned codes are already free in the model, so releasing one
cannot change the result and they are out of scope by construction). Release = every occurrence of the row becomes an
independent token (pin removed, repetition removed). Descriptor only (no decision weight): for a restoring row, whether
unpin-with-repetition-kept also restores.

Controls, run FIRST, seed 3, n 40 each, same pins as the arm:
- (s) slip words of f.206 shuffled, tokens unchanged; (g) f.206 tokens shuffled, text unchanged.
  Per draw: base (0-release) fit?, release-all-8 fit? (the CAN-fit check: a draw where even release-all is nofit is
  counted and reported; if more than half are, the null control is non-discriminating, as FT4aa's were), restoring set.
  False-decisive = base nofit AND exactly one restoring row (complete). Share reported per arm.
- (p) planted-change known-answer control (n 40, seed 3): real f.206 under 121 s + C pins (fits), one random
  single-occurrence unpinned code occurrence renamed to a random candidate row X; draws whose base becomes nofit are kept
  (others redrawn, count reported). Scan the 8 rows. Report contains-X share (expected 1.0 by construction) and
  unique-located share (restoring set == {X}).

Decisive outcome (per arm H-T, H-C): REAL base nofit, scan complete (no unresolved solve), exactly one restoring row R; AND
(s) and (g) false-decisive shares both <= 0.10 with release-all fit in >= half of draws; AND (p) unique-located share >= 0.80.
Then: ROOM.md VERIFY flag line naming R and the arm; no key value, grade or status change by this worker.
Other outcomes: one row but a control condition fails -> locator, not control-backed (rule-4 note); >= 2 rows -> non-unique
readout (list); 0 rows -> no single f.206 row restores fit under that hypothesis (needs >= 2 changes in f.206, or the hypothesis
value is wrong for f.206); control-backed as a negative only if (p) contains-X = 1.0.
Rule 3 count: the pooled/exact CP-SAT instrument's fifth use on the f.206 conflict (FT4x, FT4z, FT4aa, FT4ab, FT4ac); the
question "where does f.206 conflict with its partners" has had FT4z (locate), FT4aa (locate pairs), FT4ab (values); if this
does not decide, the exact instrument is retired for the f.206 conflict and the Verdict names new material.
Box 17:48-18:13 UTC, stop line 18:08. Cap USD 2. Script only, no vision, no subagents.
