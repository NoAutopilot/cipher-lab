# PREREG RUN3-COSK, 4 Oct 2026 (written before either pass was read)

Target: R1166 P1 (b.2/20 no.16, 21 Jun 1491), cipher groups with their interlinear period gloss.
Method: two blind Sonnet passes over 20 line crops (tools/iiif_lines.py, centres by eye), sign labels from the
decode-1168 list; alignment `tools/interlinear_align.py align --code-prefix @ --keep-fs` on the gloss/group pairs whose
sign count is within 0.8-1.25x the gloss letter count (same filter and statistic as decode-1168 A2-COS2).
Statistic: share of aligned tokens whose sign agrees with that sign's majority value across the pairs.
Control (rule 3): the same groups re-paired with the glosses shuffled, 20 seeds. Orthogonality: consistency depends on
which gloss sits over which group, so a shuffle of the pairing CAN change it (unlike an order shuffle of a per-token key).
Gate, per pass: real agreement >= shuffle p95 + 0.20. A pass below gate contributes nothing to the key.
Grading: a sign is C only if both passes clear the gate and both read the same value with >= 2 agreeing occurrences each;
one agreeing occurrence each, or a split, is M. Comparison with ciphers/decode-1168-modena-costabili-1492/key.tsv per
sign: agree / disagree / new (sign not in that key).
