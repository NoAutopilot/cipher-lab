# PREREG-NOAICH: Charriere III p.207 n.1 (and p.168 note) against c231 (15 Oct 2026, written before any score)

Worker NOAI-CH, LANE DEFAULT-A4-0437-15 (account 4). Brief `.claude/briefs/runs/2026-10-15-acct4-default-0437-jobs.md` NOAI-CH.

## What is on disk for c231 (inventory, before scoring)
- c231 clear opening, logged by RUN1-NX (NOTES.md line ~315): "Le gain de ceste grande bataille advenue en saison incommode" (9 words).
- c231 sign estimates: letters_coverage.tsv est 3000; NOTES.md RUN1-NX open-sign estimate ~1,500. No transcription, no reader pass,
  no decoded token of c231's cipher body exists. So the footnote can be tested against c231's clear words and length only; the
  cipher body cannot be aligned here (no tokens), whatever the score.
- Print: Charriere III, disk copy `sources/ia-fulltext/print-check/ngociationsdel03charuoft_djvu.txt.gz` (0 requests).

## Test G1 (identity of the opening)
Normalise both sides: lower case, strip accents, u/v -> u, i/j/y -> i, drop punctuation, rejoin OCR hyphenation at line ends.
Score = number of the 9 c231 words matched in order at the same position by a footnote word with character edit distance <= 1
(OCR tolerance). Target = the first 9 words of the quoted text in p.207 n.1.
Controls: (a) every other 9-word window in the whole of Charriere III, same score; (b) the 9 target words shuffled 1000 times (seed 1)
against c231's order.
PASS: target >= 8/9 AND control (a) max <= 4/9 AND control (b) p95 <= 4/9. Otherwise FAIL.

## Test G2 (whole piece or part), descriptive band, no licence beyond the band
Ratio R = letters in the footnote's quoted text / c231 sign estimate, computed on both estimates (1,500 and 3,000).
WHOLE if R in [0.8, 1.25] on both; PART if R < 0.8 on both; UNDECIDED otherwise. Caveat registered now: a nomenclator code stands for
a whole word and c231 has clear words inline, so signs undercount letters; R is a rough bound, not a measurement.

## What a result licenses
- G1 PASS: the footnote prints the same piece as c231 (its clear opening), and the footnote's later words are a CANDIDATE crib for c231's
  cipher body -- not a C-grade crib. It becomes C only through the folder's existing alignment path (reader passes on c231 under settled
  labels, then scripts/test0.py / nxaln with their controls), not run here.
- G1 FAIL: no claim that the footnote is c231's text beyond what NOAI-C262 logged.
- No token of c231 is graded by this job (H 0, C 0, S 0, M 0, I 0 either way).
- p.168 note: read for Charriere's stated source only; it is not scored.
