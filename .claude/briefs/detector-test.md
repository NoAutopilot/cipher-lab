Read CLAUDE.md (rules 1, 3, 10; Access playbook good-citizen rule) and RETRO-2026-09-23.md section 4 A.
Build the list of public-domain editions named there (identifiers from archive.org advancedsearch, one call per
title). Run `tools/ia_numeral_runs.py` over all of them into sources/ia-fulltext/runs.tsv. Controls first: Thurloe
vol. 1, the 1819 Catinat Mémoires and Rommel 1840 must show their printed cipher; if not, stop and report. Keep
clusters with repeat_rate >= 0.3, numerals >= 15, prose_words >= 5; judge each from its context line only, marking
cipher-with-decipherment, cipher-without-decipherment, table, noise. For each cipher-without-decipherment cluster,
grep sources/cryptiana/, and fresh clones of both solver repositories, for the edition and the letter's date. Write
QUEUE.md section "Printed ciphertext (detector test of <date>)" with one row per surviving cluster; report
precision in the top 50, control recall, and survivors. Never promote, never solve. + common tail.
