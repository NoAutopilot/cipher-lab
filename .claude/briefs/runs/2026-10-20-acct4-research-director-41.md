# Research director, wave 41 (20 Oct 2026, 18:0x UTC by date -u): Monluc's 28 Apr 1573 letter to the king -- the gated decode

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`, `python3 tools/dup_check.py fr4735-monluc-lansac-poland-1573` pasted). Solver
job: report what was found and where it was not found; no novelty class (rule 10). Done line addressed for the account-4 parent.

## JOB MONL-KING2 (account 2; Opus 5.5; cap USD 8; box 75 minutes; hosts: openapi.bnf.fr (native line regions of f.133 (c258) only, at most 10 requests, one at a time, 1.5 s apart; build each region URL with tools/iiif_lines.py or the folder's existing regen script and test the first one before the rest -- MONL-KING lost 5 of its 14 requests to malformed URLs; NOT gallica.bnf.fr); Price: vision calls: 4 x USD 0.75 + 1 reconciliation = 3.75)

ciphers/fr4735-monluc-lansac-poland-1573. MONL-KING (c7f1991fb) searched for a decipherment or print of the 28 Apr 1573 letter to the
king (ff.132-136) and found none: the aid's decipherment items 17/18 and 112-120 belong to other letters, the nearby f.166 decipherment
(2 May 1573) did not place, and Noailles I-III, Tomokiyo, Lasry, Google Books and OpenAlex gave nothing. So a reading here would be new
content. This job is MONL-KING's step 2 and 3, unchanged:
1. PREREG (pushed before any line is read): decode f.133 (c258) L01-L10 with key.tsv (Tomokiyo's Monluc Cipher 1 table, verified on
   f.138 by VERIFY-MONLUC); statistics are the longest run of in-lexicon French (fr16 word list) and the judge score (`tools/judge_
   plaintext.py specs/fr4735-monluc-lansac-poland-1573.json`), each against the same pipeline with a value-shuffled key (20 draws, p95)
   and against the known-good f.138 decode at the same length as a positive control (the positive control must pass first; if it does
   not, stop: the instrument cannot see this key at this length). Gate: the f.133 decode beats the shuffled key on both statistics and
   sits within the positive control's range.
2. Crops (`tools/iiif_lines.py`, levelled, overlay checked; paste the command), two blind passes (one call per 5 lines per pass),
   reconcile, decode.
3. If the gate passes: grade per token (S where the key reads in context above the clause test; M otherwise), write reading_c258.txt,
   `decode_key.py --check` passing, the judge output pasted (rule 7). If it fails: no grades; say whether the cause looks like reading
   error, a different key, or jargon/nulls.
4. NOTES.md "## MONL-KING2 (20 Oct 2026)" with the six research-director questions; gaps_check passes.
Report: positive control, gate result, tokens graded, one decoded phrase if the gate passed, five lines.
