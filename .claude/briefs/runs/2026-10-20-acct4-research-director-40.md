# Research director, wave 40 (20 Oct 2026, 15:5x UTC by date -u): Monluc's 28 Apr 1573 letter to the king -- find its decipherment, else read it

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`, `python3 tools/dup_check.py fr4735-monluc-lansac-poland-1573` pasted). Solver
job: report what was found and where it was not found; no novelty class (rule 10). Done line addressed for the account-4 parent.

## JOB MONL-KING (account 2; Opus 5.5; cap USD 9; box 90 minutes; hosts: openapi.bnf.fr (overviews and native line regions, at most 14 requests, one at a time, 1.5 s apart; NOT gallica.bnf.fr), archivesetmanuscrits.bnf.fr (fr.4735 finding aid), archive.org full text, Google Books API (key, country=US), OpenAlex; Price: vision calls: 8 x USD 0.75 + 1 reconciliation = 6.75)

ciphers/fr4735-monluc-lansac-poland-1573. MONL-CENSUS (5a8265dbd, census_cipher1.tsv): Monluc's Cipher 1 letter to the king (aid items
53-55, 28 Apr 1573, ff.132-136, about 1,200+ signs, "incomplete at the end") has no in-volume decipherment found so far (f.139 and
ff.140-141 tested, chance level), while the queen-mother letter on f.138 turned out to be N0 (its decipherment is ff.140r-141r).
Tomokiyo's Monluc Cipher 1 table (key.tsv) is now checked token by token on about 2,000 signs (VERIFY-MONLUC, AUDIT.md). Rule: a reading
gets capacity only if it would be new content. Order, stop at the first that settles it:
1. Decipherment search (no decode yet): overviews of the leaves the finding aid ties to decipherments (items 17/18 and 112-120, per
   NOTES.md line "look at ff.140-141 and items 17/18/112-120 for a Monluc 28 Apr text") for a clear text dated about 28 Apr 1573 to the
   king; the finding aid's own wording for items 53-55; and print: Noailles 1867 vols II-III (IA djvu, grep 28 avril / avril 1573 /
   Monluc's distinctive phrases), Tomokiyo's henryiii page (he quotes jargon from f.132: does he give plaintext?), Lasry's BnF cipher
   research in the cyphersolver repository, Google Books/OpenAlex for the letter. If a decipherment or print is found: record it,
   stop, and say "known text".
2. Only if step 1 finds nothing: PREREG (pushed before any line is read): decode f.133 (c258) L01-L10 with key.tsv; statistics are the
   longest run of in-lexicon French (fr16 word list) and the judge score (`tools/judge_plaintext.py specs/fr4735-monluc-lansac-poland-
   1573.json`), each against the same pipeline with a value-shuffled key (20 draws, p95) and against the known-good f.138 decode at the
   same length as a positive control. Gate: the f.133 decode beats the shuffled key on both and sits within the positive control's
   range. Crops (`tools/iiif_lines.py`, levelled, overlay checked), two blind passes (one call per 5 lines per pass), reconcile, decode.
3. If the gate passes: grade per token (S where the key reads in context above the clause test; M otherwise), write reading_c258.txt,
   `decode_key.py --check` passing, the judge output pasted (rule 7). If it fails: no grades; say whether the cause looks like reading
   error, a different key, or jargon/nulls.
4. NOTES.md "## MONL-KING (20 Oct 2026)" with the six research-director questions; gaps_check passes.
Report: decipherment/print found or not (with where searched), gate result, tokens graded, five lines.
