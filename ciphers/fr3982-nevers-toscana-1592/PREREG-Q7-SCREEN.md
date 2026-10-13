# PREREG-Q7-SCREEN (BNF-Q7-SCREEN, Opus worker for LANE BNF-FOCUS, account 2), written 13 Oct 2026 ~11:20 UTC by date -u

Committed before any score on a synthetic text or on f.25. Script: `q7test/screen.py` (+ `q7test/vit.c`, compiled at
run time). Brief: .claude/briefs/runs/2026-10-13-ytbiz-bnf-q7-screen.md.

## Question
Does a decode-level, order-sensitive statistic separate "f.25 is enciphered in key K" from "it is not", at f.25's
length (260 digits, `?` removed) and at the transcription's error band (passes disagree ~9.5%)? Then: does f.25 fit
key no.46 (series A/N/P, Bourdeau's key46.txt) or no.70 (alphabet + nulls only)?

## Decoder (fixed)
- Exact Viterbi over digit positions x 4-gram context (last 3 letters, 26-letter fold: lower case, accents stripped,
  a-z only). Transitions from position i: every key code matching the digits at i (lengths 1-3 as the key has them);
  every meaning of a code is a separate transition (homophones are separate codes; polyphones -- a code with several
  meanings, e.g. no.62 "bc", no.46 87 i/si -- are expanded).
- Meanings: letters, "qu"/"et" as two letters, words as their folded letters; NULL (and no.46 "-" cells) emit nothing
  at a fixed penalty of -2.0 (log10); one uncovered digit may be skipped at -3.0 (log10), no letters.
- Initial 3-letter context free (score 0 for every context).
- LM: 4-gram, add-k 0.01, V=26. Italian = tools/data/it16dip all files EXCEPT letterediprincip03char.txt.gz (held out:
  every synthetic window comes from it). French = tools/data/fr16, all three files.
- Path chosen by maximum total score (LM + penalties). **Statistic S = LM log10-likelihood of the letters on that
  path / number of letters on it** (per-character). Not coverage (order-blind).
- Target string: f.25 consensus (ciphertext.tsv), `?` removed, N = 260.

## Nulls (both can move S: S depends on digit order and on which meaning each code carries)
- (a) key shuffle: meanings permuted within the key's own classes -- letter cells among letter cells, word cells among
  word cells -- nulls/"-" kept in place; the ciphertext unchanged.
- (b) digit shuffle: the target's digits permuted, decoded with the real key.

## Validation (before any target run)
- Synthetic plaintext: 200 windows of ~300 words from letterediprincip03char (held out of the LM), seed 46.
- Encipherment with key K as on disk: a word that has a word code is enciphered by it; other words letter by letter,
  homophone chosen uniformly; q+u by a "qu" cell if the key has one; letters with no figure dropped (no.62: h s u z;
  x j k y w for any key lacking them); a null code inserted before 3% of tokens; string cut to 260 digits.
- Errors at 0/5/10/15% of digits: 2/3 substitution, 1/6 deletion, 1/6 insertion (random digit). Same 200 base texts
  at every level.
- Per synthetic text: 100 key shuffles + 100 digit shuffles. Detected iff S exceeds every null of both kinds (empirical
  p <= 1/101 for each). Power = detected share.
- Keys: no.62 (key_no62.tsv: sparse, letter row lacks h s u z) and no.46 (q7test/key_no46_codes.tsv: dense two-digit).
- **Gate: power >= 0.80 at 10% error for BOTH keys.** If no.62 passes and no.46 fails: stop, log "decode-level screen
  non-test for dense tables at N=260". If no.62 fails: stop, log the screen as NON-TEST at N=260.
- Cost fallback (declared now): if the full grid would exceed the box, the 0/5/15% levels run on the first 50 texts;
  10% always runs on all 200.
- Specificity (secondary, reported, not a gate): 100 texts enciphered in no.62 at 10% error, screened with no.46 and
  with no.70 (nulls 100+100 each); share wrongly detected.

## Targets (only if the gate passes)
- f.25 under no.46 and under no.70 (alphabet + nulls only; nomenclator untranscribed, so word codes fall to skips --
  a fit could be missed, never manufactured). 1000 key shuffles + 1000 digit shuffles each, seed 25.
- **Italian counts** (the letter's clear text is Italian). For no.46 a French run is ALSO reported (no.46's known
  letters are French); it has its own nulls but no French validation, so it is an indication only.
- Fit iff p_a <= 0.01 AND p_b <= 0.01. Reported: S, null means/p99, p_a, p_b, and the best decode as a draft, grade M
  at most. A fit goes to a separate verifier; a no-fit is "no fit at this transcription", conditional on the 9.5%
  band and on the key as transcribed.
- No.70 control caveat declared now: validation is on no.62 and no.46; no.70 (dense-ish two-digit, 64 codes) gets its
  own 50-text 10% power check before its target number is read, same rules.

## Addendum A (11:4x UTC 13 Oct 2026 by date -u, before any validation or target score)
- Speed: exact Viterbi ran ~0.06-0.3 s per decode (too slow for ~320k validation decodes in the box). A score-threshold
  beam is added: at each digit position, states more than 6.0 log10 below that position's best are dropped
  (`Q7_BEAM`, default 6.0). Tooling check on 12 decodes of 6 synthetic texts (3 per key no.62/no.46, 10% error, real
  and shuffled key): beam 6.0 gave the same S as beam 100 on all 12 (beam 4.0 differed on 2). These 12 are a tooling
  check, not validation; the validation texts use seed 46 and were not decoded before this addendum.
- "One digit may be skipped" is implemented as a skip transition available at every position (-3.0), not only at
  digits no code covers (a covered digit can be a transcription error).
