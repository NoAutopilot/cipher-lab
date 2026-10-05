# PREREG_settle7ms -- multi-seed settle7 rule (RUN6-PAGET, LANE-RUN6 account 1, 5 Oct 2026, written 05:04 UTC by date -u, before any run)

Brief: `.claude/briefs/runs/2026-10-05-acct1-run6-wave2.md` section RUN6-PAGET. Disk only, no network, no vision call, no subagent.

Problem (A3V3-PAGR, reproduced by A3V3-PG7): settle7.py's S/M rule reads one Gibbs sampler path (per-letter, seed 0). On the
corrected pairs, seeds 0-9 give 126 he 5/10 and 86 dame 6/10 at the "Madame"/"Duchesse" tokens, so their rulings depend on which
seed was run. Already known before this file: those seed 0-9 tallies (RD7-2026-10-04-a3v3.md). Seeds 10-19 have not been looked at.

Rule (registered here, applied uniformly to all 15 settle7 codes and every occurrence, not only 126/86 -- a rule applied to two
codes only would be selective):
1. Seeds: per-letter Gibbs (settle7.gibbs_tokens, the same L1/L2 split, tools/gibbs_align.py unchanged), seeds 0..19 (K = 20).
2. A token's multi-seed chunk = its modal chunk across the 20 seeds; its stability = modal count / 20.
3. **S** only if modal chunk == the code's GIBBS value **and** stability >= 0.80 (16/20) **and** the token is not in DEMOTE.
   Otherwise **M**. (DEMOTE list unchanged; no new eye demotions or lifts in this job.)
4. GIBBS values unchanged (no code value changes in this job; only grades move).
5. Grades move only per this rule: a seed-0 S that fails it goes to M (its exceptions.tsv S row removed); a seed-0 M that
   passes it goes to S (an exceptions.tsv S row added, value = code value, reason citing the multi-seed ruling).
6. Afterwards: settle7.py --check, then `tools/decode_key.py ciphers/clairambault1225-paget-1714` and `--check` (rule 7);
   counts before and after reported per token.

Reported for every ruling: seed-0 chunk, modal chunk, stability, old ruling, new ruling ("seed-stable" = modal == seed-0 chunk
with stability >= 0.80). No value or novelty claim follows from this job; it is a grading-stability rule only.
