# LANE V4 verifier V2: second opinion SO-GRAMONT-F29R (pull request 1), Opus, cap $8

Common rules: `.claude/briefs/runs/2026-09-24-lane-v4-common.md`. Target: ciphers/fr2980-gramont, item f.29r (no.21, Gramont
to Villandry, Rome, 20 May [1530]), class N4 in AUDIT.md. An outside model (ChatGPT, GPT-6) answered our adversarial prompt;
its file is on branch `second-opinion/SO-GRAMONT-F29R` (pull request 1) at
`ciphers/fr2980-gramont/second-opinions/chatgpt-2026-09-24.md`. `git fetch origin second-opinion/SO-GRAMONT-F29R` and read it
from that ref. Your job: check every checkable claim in it against the source, correct our files where it is right, and
record the outcome. Do not decode; do not merge or touch the pull request; the parent closes it.

Checks, each with the source you used and the result:
1. Catalogue des actes de François Ier IX (IA `collectiondesord09acad`, full text already fetched by earlier audits; fetch
   once if not on disk): is the Gramont entry [412] on p.61 and [411] Villebon's 1528 mission? Correct AUDIT.md's three
   "[411]" citations (lines near 160, 1067, 1253) if so. Note the volume date (title page 1907 vs IA metadata).
2. Sign count: reading.txt header, ciphertext.txt, key.tsv: is the total 568 (H 533 M 30 U 5)? Make AUDIT.md, NOTES.md and
   the prompt consistent (569 appears in AUDIT.md lines 9, 16, 49, 66 and NOTES.md 232, 238).
3. NOTES.md's attribution of the OpenEdition chapter pur/120024: Philippe Hamon, "Jean Breton", in Michon (ed.), Les
   conseillers de François Ier (2011), pp.335-342, not Thierry Rentet? Fix if so.
4. The prompt's opening search phrase ("il y baille a ce porteur") versus the reading's first tokens ("IAYEAI[LL]E", i.e.
   "j'ay [b]aillé"?): which is right, and does the prompt need its phrase list corrected? Update PROMPT-chatgpt.md's phrases
   if the reading supports it; do not change the reading itself (that is a solver's job; log it as a one-line suggestion).
5. The bracketed year [1530]: keep the bracket where the manuscript does not carry the year; make files consistent.
6. Its leads 1-7: for each, one line: already covered by AUDIT.md (cite the section), or new, or not actionable. Camusat
   1619 vs 1644 edition equivalence: what AUDIT.md actually established, in one sentence.
Then: append to AUDIT.md a section "Second opinion SO-GRAMONT-F29R (ChatGPT, pull request 1), checked <date -u>" with a
table of claims, verdicts and corrections made; the class stays N4 unless a check finds a prior print or decipherment (then
reclass with the evidence). Copy the file from the branch into ciphers/fr2980-gramont/second-opinions/ on main (same name),
set the SECOND-OPINIONS-QUEUE.tsv row SO-GRAMONT-F29R to status `checked` with the `outcome` column one short phrase
(e.g. "no prior print found; catalogue entry, chapter author and sign count corrected"), update the Gramont f.29r results row
in status.json only if the class changes. ROOM done line `for LANE V4: SO-GRAMONT-F29R checked -- <outcome>`.
