# PREREG RUN3-COSK2, 4 Oct 2026 (written and committed before either blind pass was run)

Target: R1166 P1 (20 line crops, same `tools/iiif_lines.py` command as RUN3-COSK) and P2 (14 line crops,
`--region 330,760,1850,1540 --centres 230,300,385,460,545,635,725,810,895,985,1075,1170,1320,1400 --top-margin 135
--bottom-margin 10 --lines-per-crop 1`), images scratch-only, sha1 = images_manifest.tsv.
Change from RUN3-COSK (the one knob): the convention is stated to both blind readers, and the crops are marked.
- Convention given to the readers: a horizontal dash/stroke leading into a sign is a lead-in stroke, not a sign; drop it,
  EXCEPT dash+z, which is a distinct sign written `Z`; a bare z is `z`. Nothing else about values is told (no glosses, no key).
- Marking: each crop carries margin labels "gloss >" and "TARGET >" (both sides, lines slope) at the target line and the
  interlinear zone above it; readers record as gloss ONLY the small interlinear writing directly above a cipher group of
  the target line, never main-line clear words and never another line's writing.
Method, statistic, control and gate: identical to PREREG-RUN3-COSK.md (pairs filter 0.8-1.25 sign/letter ratio;
`tools/interlinear_align.py align --code-prefix @ --keep-fs`; statistic = share of aligned tokens agreeing with the
sign's majority value; gloss-shuffle control 20 seeds, which can change the statistic since it re-pairs glosses with
groups; gate per pass: real >= shuffle p95 + 0.20). Run on P1+P2 pooled per pass (the gate); per-page figures reported
alongside, not gating.
Grading: a sign is C only if both passes clear the gate and both read the same value with >= 2 agreeing occurrences
each; otherwise M. No upgrade from the reconciliation (it is reported, grade M at most, as in RUN3-COSK).
Comparison with ciphers/decode-1168-modena-costabili-1492/key.tsv per sign: agree / disagree / new.
P4 decode with the rebuilt key only if >= 80% of P4's unglossed signs have a C-grade value.
