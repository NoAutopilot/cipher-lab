# VERIFY-DIN2 (account-3 orchestrator, 3 Oct 2026): second audit of fr3621-dinteville-1592 f.130r, print-built key

CLAUDE.md verifier template; you are separate from the solvers (A2-DIN*, DIN-PRINT) and from VERIFY-DIN. Claim under audit:
DIN-PRINT (d10eb096 prereg, 09d32335): the key rebuilt by aligning the f.128 cipher to its 1882 printed plaintext (Revue de
Champagne et de Brie XII p.340) reads f.130r at fr16 -1.271 vs 1000 free (p95 -1.705) and frequency-banded (p95 -1.575)
shuffles, 0/1000; grades C 291 M 197 U 39 (conservative; pre-registered C 357). Model Opus 5.5, cap USD 6, box 50 min.
vision calls: 1 x USD 1.5 = 1.5 (one native crop of the date line, to settle 3 vs 4 July; tools/iiif_lines.py, never a page).
1. Re-derive (align_print.py --check, score_print.py --check, decode_key --check); rerun controls at fresh seeds; check the
   alignment's own controls can fail (rule 3: a control orthogonal to the statistic is a non-test).
2. Are C grades licensed only where the print supports the value with >=2 occurrences and no conflict? Polyphones (# c/d, v a/t)
   at M. Recount.
3. Second rule-10 search, families VERIFY-DIN did not cover or could not reach: the Revue de Champagne series' other volumes
   and the 1899 reprint (does any print the f.130 cipher text or a decipherment?), Boltanski 2006, ARCSI PDFs (try pdftotext
   via pip pypdf if absent), BnF finding aid for fr.3621, Dinteville family scholarship (OpenAlex/S2/HAL/Persée), Google Books.
4. Settle the date from the crop. AUDIT.md: add "Second audit" with N-class, key source `period` (plaintext of the sibling
   printed 1882), safe/unsafe sentence, the class-relevant fact that f.130's own clear parts are summarised in print; propagate
   to SO-DIN-F130. NEAR row numbers. Done line "for the account-3 orchestrator" with a one-line English gist (interpretation).
