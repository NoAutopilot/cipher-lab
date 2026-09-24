WORKER J6 -- KEY FOR 5549's NEW CIPHER from Willem's own letters of 1574 printed in clear by Groen (Opus, cap $10, TSV-first).
Target: ciphers/jan-van-nassau-1572-75, letter 5549 body (runs 1-61, 537 numerals; ciphertext_5549.tsv rows not PS*).
Common rules: .claude/briefs/runs/2026-09-24-lane-r3-common.md. Hosts: resources.huygens.knaw.nl (WVO PDFs, 2 s apart,
at most 10 requests). Never dbnl.org: LANE V3 is putting the Groen texts on disk (ROOM 12:58 request); git pull for them.

Established (do not redo): the body is the "verendertte Instruction oder Ciffer" Willem sent in autumn 1573. It is not
key_1572, not any rotation of Lodewijk's five-per-letter table (which reads 5549's closing stretch and 5550/5552/5557),
and its value profile does not match the unrecovered 1575 nomenclator of 5218/5222 (cosine 0.48; top values 14, 9, 19
against 29, 28, 26). Body values run 1-345, 133 distinct, 24% above 99, short clear endings inside runs (en, er, ge, ch, n).
J5S's search log is NOTES.md "J5S result".

The natural known-plaintext pair is a letter FROM Willem in his new cipher whose clear text Groen prints: WVO 5204
(22 Apr 1574), 5205 (28 Apr 1574), 5207 (23 May 1574, Groen V 6-8 CDXCV; images/05207_p1-3 on disk), 5208 (7 Jun
1574), 5209 (24 Jun 1574), 5213 (26 Nov 1574, Groen V 95-99 DXXIII; images/05213_p1-4 on disk; French, values to ~110).

JOBS, stop at the first key that reads:
1. Fit test, cheap: for each candidate, a Sonnet subagent transcribes ONE page's numerals only (TSV to disk, push per
   page; fetch the PDF from sources/wvo/cipher-letters-2026-09-24.tsv's URL at 150 dpi only if not on disk). Compare with
   the 5549 body by value range, share above 99, the top-10 values and the clear-ending habit. Rank; write
   j6/fit.tsv. Stop fitting when one candidate clearly matches (shares most of 5549's top values).
2. Align the best fit to Groen's clear text (from LANE V3's file; if not yet there, wait by doing job 1 on the next
   candidate): letter-level alignment as in align/em_align.py or ciphers/lodewijk-van-nassau-1573-74/r18/; key_new.tsv
   with C grades and counts.
3. Apply to 5549's body with tools/decode_key.py (add a job to decode_5549.json), grade per token (C from the aligned
   sibling, I from the clear frame only, M, U), --check exits 0. The clear frames in groen/groen_5549.tsv are the check:
   report how many runs read as grammatical German in their frame.
If no candidate fits, say so with the fit table; do not start crib cryptanalysis (a separate brief with a control).
Report what was found and where it was not found; do not classify novelty. At 80% of cap push a progress section in
NOTES.md "J6 new key (24 Sept 2026)". Final ROOM `done:` with grade counts, and `for LANE V3: ciphers/jan-van-nassau-1572-75
5549 body reading ready` if one exists.
