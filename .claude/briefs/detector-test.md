Read CLAUDE.md (rules 1, 3, 10; Access playbook good-citizen rule) and RETRO-2026-09-23.md section 4 A.
Build the list of public-domain editions named there (identifiers from archive.org advancedsearch, one call per
title). Run `tools/ia_numeral_runs.py` over all of them into sources/ia-fulltext/runs.tsv. Controls first: Thurloe
vol. 1, the 1819 Catinat Mémoires and Rommel 1840 must show their printed cipher; if not, stop and report. Keep
clusters with repeat_rate >= 0.3, numerals >= 15, prose_words >= 5; judge each from its context line only, marking
cipher-with-decipherment, cipher-without-decipherment, table, noise. For each cipher-without-decipherment cluster,
grep sources/cryptiana/, and fresh clones of both solver repositories, for the edition and the letter's date. Write
QUEUE.md section "Printed ciphertext (detector test of <date>)" with one row per surviving cluster; report
precision in the top 50, control recall, and survivors. Never promote, never solve. + common tail.
Lessons of 24 Sept 2026 (LANE S rounds 2-4): pre-filter back-of-volume indexes and Regesten (last 8% of lines; ascending page
references) and spot-check 10 dropped clusters; judge from +-10 lines, run the interlinear test, AND grep the whole cached
volume for a decipherment indicator ("dechiffr", "deciphered", "Dechifrerede", "decyphered", "Nyckeln", "clave") before calling
any passage undeciphered (round 4: Christian IV's letters were deciphered in a same-volume appendix). Never commit+rebase or
checkout while a background fetch still writes a tracked file (round 4 lost 130 identifiers' clusters to an orphaned handle).
Lesson of 24 Sept 2026 (Urquhart 1653, Vals AI): host-text-as-key pass before solver -- for each cipher-without-decipherment
cluster, test the host edition's own structure (sections, stanzas, lines, words matching the cipher's counts, index-into-text
rules) before handing the cluster to a substitution or frequency solver. See LESSONS.md, "24 September 2026: a printed
cryptogram's key is often the host text".
