# Research director, program A: Lope Hurtado 1522 key application (17 Oct 2026, 01:4x UTC by date -u)

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, PREREG with a `## Decision` block pushed before any scored run, `tools/experiment_log.py --check`). Ends the NOTES
section with the six research-director questions answered in one line each. Report what was found and where it was not found; do not
classify novelty (rule 10; a verifier does that). Credit Bourdeau (dbourdeau/cyphersolver, MIT code / CC BY 4.0 text) and Kolosova 2024
on every line that uses them.

## JOB LOPE-KEYAPP (account 4; Opus 5.5; cap USD 6; box 60 minutes; disk plus one shallow clone of github.com/dbourdeau/cyphersolver, no other host, no readers, no images; Price: vision calls: 0 x USD 0 = 0)

Target ciphers/lope-hurtado-1522 (status partial; intake gate passed 17 Oct 2026). Read first: NOTES.md "## Kolosova 2024 read" (17 Oct
2026), HYPOTHESES.md (the five data conflicts), kolosova2024_cifra7.tsv, kolosova2024_cifra10.tsv, kolosova2024_alphabets.tsv, and the
"Remaining gaps" section. Kolosova's Cifrario 7 is a published key (grade H as a source) for Lope Hurtado's 1522 Rome letters; Bourdeau
recovered 49 word codes from clear copies and read R9649 97%, R9646 84%, R9634 73% (his read_*.md). Question: how much of what Bourdeau
could not read do Kolosova's tables read, and do they read the clear-copied records correctly first?
1. `git clone --depth 1 https://github.com/dbourdeau/cyphersolver` into your scratch dir (one request; delete after). Use only
   targets/lopehurtado/: r9634_cipher.txt, r9634_tokens.txt, r9634_reading.tsv, read_r9634.md, read_r9646.md, read_r9649.md,
   read_r9644.md, key_codes.tsv, key_1522_r9634.tsv, key_1522_from1524*.tsv, decode.py. Note his HEAD commit in NOTES.md.
2. PREREG first (`PREREG-LOPE-KEYAPP.md`, Decision block below, pushed before any scoring). Notation: Kolosova's prefixes 3/y/s are
   Bourdeau's z/ɣ/ʃ (kolosova2024_cifra7.tsv header); a code token is a prefix sign plus 1-3 Latin letters.
3. Known-answer control, before any new reading: on R9649 (own clear copy f.268) and R9644 (clear ff.241-242), list every code token
   whose value Bourdeau fixed FROM THE CLEAR COPY (his source column), look each up in kolosova2024_cifra7.tsv, and count agree /
   disagree / absent. Null control: shuffle the `word` column of the Kolosova table 200 times and recount agreements. Gate: Kolosova
   agrees on >= 80% of the overlapping codes AND the real agreement count exceeds the shuffle p99. Gate fails -> log non-test, stop.
4. Only after the gate passes: apply cifra 7 to every code token in R9634 and R9646 that Bourdeau left unvalued or `possible`/`probable`
   (his reading files mark them). Write `reading_kolosova_gain.tsv` (record, line, token, Kolosova value, grade H = published key,
   Bourdeau's prior value or 'unread', context line) and the before/after coverage per record (tokens valued / cipher tokens). The five
   HYPOTHESES.md conflict codes stay M: at every occurrence report which of the two values the context admits, never pick one.
   Cifra 10 check: coverage of cifra 10's groups on R9634's and R9646's code tokens, beside cifra 7's -- a record whose code tokens fit
   cifra 10 better is flagged, not re-read.
5. Decision (pre-registered): (a) gate PASS and >= 10 new tokens read in R9634: write "## LOPE-KEYAPP (17 Oct 2026)" in NOTES.md with the
   gain table, the lines whose sense changed, per-token grades (H published-key, M conflicts, Bourdeau's as he graded them), and name
   the next step (a fresh re-derivation under rule 7 by a verifier; the label is `key application`, pipeline 7); (b) gate PASS and < 10
   new tokens: the table adds little at 1522; say so and what would (the 2024 book's discussion pages, or the BNE siblings); (c) gate
   FAIL: non-test, the table is not this pool's key as transcribed -- list the disagreements for a re-read of the scan by the parent.
   No key.tsv of our own is written; no reading is described outside NOTES.md; status stays partial.
Stop at 80% of cap or box. Report: gate numbers (agree/disagree/absent, shuffle p99), tokens gained per record, decision, five lines.
