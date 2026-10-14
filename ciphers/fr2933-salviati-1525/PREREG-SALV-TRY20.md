# PREREG-SALV-TRY20 (14 Oct 2026, written 09:3x UTC by date -u, before any --try run or re-score)

Worker SALV-TRY20 (Opus), LANE DEFAULT-A2-0911-14 (account 2), brief `.claude/briefs/runs/2026-10-14-ytbiz-default-0911-jobs.md`
row SALV-TRY20. Key: lkey/key_lasry.tsv (published, credit George Lasry, D. Bourdeau cyphersolver dde5b0ea, CC BY 4.0). Hypotheses
are held in memory only; key_lasry.tsv gains rows only per item 4. key.tsv: none exists, none written.

1. Types: the 20 sign types whose two SALV-LKEY passes named different cells (lkey/pass{A,B}_part{1,2}.tsv), plus eps^7 (keyed ci;
   his f54r L14 excerpt reads ti/tu there). Candidates per type = every value named by either pass, cells split on '|', his '?'
   stripped, SALV-LKEY's normalisation (p2->p, et2->et, u/v->u); 'none' is not a candidate:
   #^ et | H^ che | L^ fa, fo, fe | Lx^ u | S4^ t, ge | S7^+ na, ni | S^ o, m | Z^o la, lu, li | ]^dot li | ]^o la, lu | a^dot ma |
   bh^ p, b, o | bh^dot bi | ch^ che | dl^ r, b, bi | e^+ da, di | m^1 pu | sq^ qua | sq^o qua | sq^~ qua | eps^7 ti, tu.
   Types with 0 tokens in lkey/ciphertext_lasry.tsv (Z^o, ]^dot) are listed as untestable, not run.
2. Each candidate is run alone (one hypothesis per call, the rest of the key as committed):
   `python3 tools/decode_key.py ciphers/fr2933-salviati-1525 --config ciphers/fr2933-salviati-1525/decode_lasry.json --try 'SIGN=VAL'
   --lm it16 --nulls 200 --try-log ciphers/fr2933-salviati-1525/crossword_log.tsv`. Verdict as the tool prints it (its own two nulls).
3. Acceptance per type: a type takes a value only if exactly that candidate's verdict is `accept`; if two or more candidates of one type
   are accepted, the one with the larger statistic. Any other outcome (reject, undecided, null not built) leaves the type unchanged
   (unkeyed, or ci for eps^7). Grade of an accepted value: M (the tool's known-answer controls passed only for single letters in a
   letter cipher; syllables failed, K2), whatever the class.
4. Whole-key re-score: lkey/score_lasry.py with all accepted values set together (`--set`, extended this session to take SIGN=VALUE:CLASS
   for a sign not yet keyed; default behaviour unchanged), same 300 permuted keys, seed 1, accepted signs joining their class's
   permutation. Written to lkey/score_try20.json. Reproduction check first: the run with no --set must reproduce score.json exactly
   (target, p99, mean, rank) or the comparison is void. Gate (as PREREG-SALV-LKEY item 5 / PREREG-SALV-TRY item 3): all-leaf 4-gram
   target > permuted p99. Reported beside it: >=4-letter it16 word hits, target vs p99 and rank, and per leaf. If no value is accepted,
   no re-score is run and "after" = "before".
5. Reading: gate PASS => "accepted values raise the published-key decode above its control", the accepted rows go into key_lasry.tsv
   graded M with a dated note; gate FAIL => accepted values (if any) are recorded in NOTES.md only, key_lasry.tsv unchanged, and the
   whole-key re-score is closed for this instrument (rule 3 third-attempt clause: SALV-LKEY, SALV-TRY, SALV-TRY20). No novelty
   classification.
