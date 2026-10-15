# PREREG-MAT-F91B (addendum to PREREG-MAT-F91; 15 Oct 2026, 06:3x UTC by date -u; account-2 worker MAT-F91B, LANE DEFAULT-A2-0509-15)

Written and pushed before any --try, transcription, alignment or score of this job.
Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0509-jobs.md` job MAT-F91B.

## (a) --try of MAT-F91's candidates: U=e, T=r, D2=a, BOX2=u
- Instrument: `tools/decode_key.py ciphers/matignon-mayenne-1586 --try CODE=VALUE` (fr16 model, window 8, nulls 100: null 1
  shuffled positions, null 2 value class), one call per code, each alone (other unkeyed codes as the key has them), logged
  with `--try-log ciphers/matignon-mayenne-1586/crossword_log.tsv`.
- Acceptance = the tool's own verdict `accept` (statistic above both null p95s, breakage rule passed). Undecided/reject
  -> not accepted. An accepted value is grade M (MQS-CROSSWORD rule; the f.91 gloss is a known-answer witness for the
  label, but the label identity across readers is not settled). No key.tsv edit in this job (lane rule); an accepted
  value is recorded in crossword_log.tsv, HYPOTHESES.md and NOTES.md as the licence for a later key row.
- Power control on this target (fixed now, run first): for four H single-letter codes nearest in token count to
  U/T/D2/BOX2 respectively, --try each with a WRONG letter (the letter of the key's next-commonest French vowel/consonant
  of the same class: vowel->other vowel, consonant->other consonant, chosen as the alphabetically next in that class).
  If any wrong value is `accept`ed, the instrument is non-discriminating here and every candidate verdict is logged
  "non-test at this target"; nothing is accepted.

## (b) blocks C and F (and E only if (a)+(b) leave >= 25% of cap)
Exactly PREREG-MAT-F91's material, alignment, statistic R, confirmed/conflict rules and shuffled-gloss control (200 draws,
seeds 1-200, gloss words permuted within each block), applied to the new blocks: gate real R > max of the 200 draws AND
R >= 0.60, computed on C+F pooled (and per block reported). Same reader brief (`f91/PASS_BRIEF_F91.md`), blind to key and gloss.
`f91/align_f91.py` is reused unchanged except for the block list.
Candidates for unkeyed labels again reported as M, untested. Conflicts with >= 2 occurrences go to HYPOTHESES.md with
witnesses (f.91 block and line), combined with MAT-F91's A/B/D counts only as separate witnesses, never summed into a
majority override.

## Stop rules
Cap 6, box 90 min from 06:25 UTC; no unit started past 80% of either (4.8 / 07:37 UTC). openapi.bnf.fr <= 6.
