# Research director, wave 52 (24 Oct 2026, 13:4x UTC by date -u): read the printed pages -- are the 1659 Hyde-to-Fanshaw cipher groups in print, and is the Barwick key?

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Gallica is not involved.

## JOB HEATHCOTE-PAGES (account 4; Sonnet 5; cap USD 5; box 40 minutes; hosts: archive.org only (metadata, djvu text, page images via /download/<id>/page/n<N>_w1600.jpg or the BookReader image endpoint for public-domain items, <=20 requests, >=1.5 s apart); Price: vision calls: 8 x USD 0.5 = 4)

Read first: ciphers/_triage/heathcote-fanshawe-1659.md (all sections, including the parent note's question 4). The OCR says HMC 1899
prints "[The parts in italics are in cipher, undeciphered]" for two Hyde-to-Fanshaw letters (June 4-14 1659 and Jan 14-24 1659/60,
Brussels). OCR drops italic numerals; nobody has looked at the page. Tomokiyo (sources/cryptiana/web/charlesii.htm) says Hyde's cipher
table of 12 June 1659 is printed in *Vita Johannis Barwick* (facing p.316) and described in the English *Life of Dr. John Barwick*
(unabridged, p.408). Both books are public domain and on archive.org.
1. HMC 1899 (`manuscriptsofjmh00greauoft` or a sibling copy with page images): from the djvu text, find the leaf numbers of the two
   letters (search the datelines and "parts in italics are in cipher"); fetch those page images (at most 4 leaves) into your scratchpad
   and read them: are the italic passages (a) cipher figures or groups, (b) Fanshaw's garbled English, or (c) something else? If (a),
   transcribe every cipher group of both letters in two independent blind passes (two subagent calls, one per letter, each given only
   the page crops; the vision price line above counts them) and reconcile with tools/reconcile_passes.py or by hand into
   ciphers/_triage/heathcote-1659-ciphertext.tsv (letter, line, group, pass A, pass B, agreed) with the leaf and the IA page url per
   row; count the groups. If (b) or (c), say so, quote one line, and stop part 1.
2. Barwick: find the Latin *Vita Johannis Barwick* (1721) and the English *Life* (1724) on archive.org; fetch the table page (facing
   p.316 Latin) and p.408 English (at most 3 leaves) into your scratchpad and say what is printed: a full table (letters 1-63,
   syllables/words 70-692) or a description; transcribe the table only if it is on one or two leaves and legible, into
   ciphers/_triage/heathcote-1659-barwick-key.tsv (code, meaning, class, source page), grade H (published period key), two passes if
   under 150 rows, else one pass and say so. No decode of anything in this job.
3. Write "## Printed pages (HEATHCOTE-PAGES, 24 Oct 2026)" in the triage file: what the italics are, the group count, what the Barwick
   pages print, the IA identifiers and leaf numbers, request counts. Never promote, never create a ciphers/<slug>/ folder, never
   apply a key. Report: (a)/(b)/(c), group count, Barwick table yes/no and row count, hosts and requests, five lines.
