# H61 pre-registration (29 Sept 2026, DEBOSNYS-RUNNER-3b; written and pushed before any score is computed)

Row: CAMPAIGN.md H61 (swarm DIGEST-2 row 3). Data: swarm/R2/R2-2/control/{truth.tsv, reads_R1_sonnet.tsv,
reads_R2_opus.tsv}; no new reader calls.

Folds, applied on top of R2-2's own (PCT-SLASH->PCT, X-DOT->X, X-CURL->X) and RULE.md's marks (BLOB, BAR-SOLID,
HOOK-L, DASH-V, `_`, MARK -> `_`):
EIGHT+VENUS+THREE; C-BAR-X+ARCH-DASH; CIRC-O+BLOB; O-SLASH+PHI; II-DASH+CC-DASH; S-CURL+DOUBLE-LOOP.
Note: CIRC-O+BLOB conflicts with RULE.md (BLOB is a mark); the fold is applied first, so CIRC-O and BLOB both become
one sign class "CIRC-O/BLOB" and neither is a mark under this scoring. Stated here before scoring.

Scores reported (both unfolded-coarse, i.e. R2-2's folds only, and coarse-folded):
- two-reader control error = (boxes where R1 != R2 after folding + boxes where R1 == R2 != truth after folding) / 96;
- single-reader error for R1 and R2;
- folded K on c1+c2 settled drafts (settled_lines, drop_clear), and the share of c1+c2 tokens the new folds touch.
Kill: folded two-reader error >= 5 pct -> the coarse folds do not give a low-noise text on the public pixels.
Caveat fixed in advance: these six folds were named from R2-2's own split list on this same control page, so a pass
here is optimistic (the folds were chosen on the test data) and would need a fresh known-answer page before use; a
pass names a lower-noise folded text (polyphony caveat, every later use reported both ways), not a reading.
