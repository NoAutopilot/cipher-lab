# PREREG D1-BAL170B (account 1 worker, for LANE DEFAULT-account-1-20261006-1240), written 6 Oct 2026 13:5x UTC before any pass

Addendum to d1bal170/PREREG-D1BAL170.md (same prompt d1bal170/prompt.txt, same token forms, same norm.py, same gate 0.10).
Passes (Sonnet subagents, blind, crops + d1bal167/exemplar_sheet.png only, one call per page per pass):
 f.228r pass C on the re-cut crops b170f228r_a_L02, _c_L01, _b_L01, _b_L02 (s1/s2).
 f.228v passes A and B on b170f228v_a_L01-L02, b170f228v_b_L01-L07 (s1/s2).
Split statistic: 1 - agree/aligned columns from `tools/reconcile_passes.py` (no --keep-plain), cipher tokens only, marks included.
 f.228r: primary = pass C vs passes/reconciled_b170f228r.tsv normalised by norm.py (the eye reconciliation from the native region;
 C is blind to it); secondary, reported only = C vs normA and C vs normB (the clipped-crop passes).
 f.228v: pass A vs pass B.
Both comparisons are agreement, not accuracy (TRANSCRIPTION.md). Gate: split > 0.10 on either page -> reconcile by eye (1 unit) and stop;
next step a sign sorter. Split <= 0.10 on both -> reconcile; no decode in this job (brief: "Do not decode").
