LANE R8 L3034 -- BnF Français 3034 item 68, "Lettre, en chiffre", Landriano, 30 Aug 1528 (anonymous): intake (Sonnet, cap $4, box 40 minutes;
hosts gallica.bnf.fr and archivesetmanuscrits.bnf.fr only, >= 1.5-2 s apart; general web search allowed; no subagents).
Authority: LANE R8 brief job 2 (scout lead from R7-SSIB, ciphers/fr2933-salviati-1525/siblings.tsv and leafnotes/siblings.md); CLAUDE.md
Pipeline 2 (check-solved before any deep work) and rule 1. Common: 2026-09-25-lane-r8-common.md.
Job:
(1) Folder ciphers/fr3034-landriano-1528/ with NOTES.md: first line a status word (open / found-solved / blocked ...), then the check-solved
    verdict per `.claude/briefs/check-solved.md` naming the standard edition and the pages or full-text search actually read within 6 lines of
    the status word. Sources in order: web search; the BnF finding aid entry for Français 3034 items 68 and 69 (read both; say whether 69 is a
    decipherment or a second cipher letter); Desjardins/Canestrini, Négociations ... avec la Toscane II (archive.org, the 1528 section) and any
    Sforza/Milan edition for Aug 1528 (the Landriano campaign, Saint-Pol's army); Tomokiyo's Cryptiana pages (sources/cryptiana/ first);
    DECODE listing (tools/decode_list.py, login-free); both solver repositories (grep only). Record what was checked and the date.
(2) `python3 tools/intake_gate_check.py fr3034-landriano-1528` -- paste its output; iterate NOTES until exit 0 if the verdict supports it.
(3) Images once: find the Gallica ark (finding aid link or Gallica SRU), `tools/gallica_folio.py` to pin the leaf canvases of items 68 (and 69),
    fetch each leaf once at native resolution into images/ with images/manifest.json (tools/iiif_lines.py or a plain IIIF fetch); <= 30 MB.
(4) Describe, from the images: sign count (estimate per line x lines, and the whole letter), symbol inventory estimate, design class
    (invented signs / digits / letters; with or without marks, nulls, code words; plain words interleaved?), any interlinear gloss or
    decipherment on the leaf. Compare its sign shapes to ciphers/fr5761-election-1519/glyphs/atlas_part1.png/atlas_part2.png (the 1519 embassy
    key) and ciphers/fr2933-salviati-1525/glyphs/atlas_part1.png/atlas_part2.png (Salviati 1525): list shared shapes, if any, with crops.
    A match to either is a pool (CLAUDE.md Pipeline 3): post "for the parent: fr3034 item 68 shares <n> signs with <target>" in ROOM and stop.
Do not decode or try a key. ROOM done: "done: for LANE R8: fr3034-landriano-1528 <status>, <n> signs, <design>, match <none|target:n>",
requests per host.
