# PREREG OLD-ES17A (3 Oct 2026, LANE-A1, account 1) -- written and committed before any target score under es17a

Corpus `tools/data/es17a` fixed before scoring (MANIFEST.tsv, build.py; 5 files, 1590-1625 Spanish state/diplomatic/
court prose, 650k folded-letter cap per file). No file is added, dropped or re-cleaned after the target is scored.

Texts scored, each through `tools/judge_plaintext.py` with a spec identical to specs/na-oldenbarnevelt-2442-1605.json
except the judge's corpus (`"language": "es17a"`, then `"language": "es17c"`), min_word_cover 0.5, control_samples 200:
1. B/C1 committed reading: the `value` column of reading_tokens.tsv for blocks B and C1, space-joined (N=634 letters).
2. Whole committed reading.txt (N=1226), for comparison with sections 8/9.
3. Shuffled-target decodes (ARM-C1 voiding check), both of the B/C1 ciphertext (`raw_used`, blocks B+C1) with all
   signs shuffled across the stream (token lengths kept), seeds 1, 2, 3:
   (a) the committed digit_key.json applied to the shuffled stream (no overrides);
   (b) scripts/solve_digit_subst.py target mode on the shuffled stream (its own key found blind, default settings
       except --restarts 4), using the spec's own es16 corpus as it was used for the real key.
Gate (judge's own, unchanged): PASS iff score > real_p05 of the corpus's own N-letter real windows and word cover >= 0.5.
Voiding rule (CLAUDE.md rule 3, ARM-C1): if any shuffled decode PASSes under a corpus, that corpus is void as a gate
for this family at this N, whatever the B/C1 result. Corpus reliability rule (rule 3 fold-count paragraph): the
leave-one-file-out false-negative rate at N=634 is reported with its per-fold spread; a corpus with <~5 files and a
wide spread (max fold > 2x min fold and > 20 pct) is "unknown reliability", and its PASS/FAIL is reported as such.
No reading is changed by this job.
