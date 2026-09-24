# LANE G3 worker F: capture M35 fr2933-salviati-1525 (Sonnet, cap $6, Gallica fetcher; ONE target)

Read .claude/briefs/transcription.md in full (its pre-capture check and script rules are binding) and ciphers/fr2933-salviati-1525/NOTES.md.
Ark btv1b90600674; ciphertext confirmed at canvas 55 (400 px). The manifest endpoint reset twice for worker E: pin with the direct image
endpoint by eye (canvases 54-60) rather than retrying the manifest more than once.
1. Pre-capture check (two minutes): interlinear/marginal gloss, a decipherment nearby (catalogue item 17 'Deschiffrement' at Fol.70 is said to
   be unrelated: glance at it at 600 px to confirm), a second copy. If a decipherment covers this letter, stop and say so: that makes it recovery.
2. Natives of every leaf of the letter only (images/manifest.json; < 30 MB). Record folio, canvas, layout, date line, address, signature.
3. If the signs are invented symbols, build one shared glyph atlas first (see ciphers/dupuy452-carpi-1520/glyphs/); if numerals/letters, skip.
   Crops with tools/iiif_lines.py --debug (check the overlay), then two blind Sonnet subagent passes (passA.tsv, passB.tsv; commit after each),
   then tools/reconcile_passes.py. Settle disagreements.tsv rows from the image only if it stays inside the cap; else leave them.
Report tokens, types, pass agreement. NOTES.md section 'Capture and passes (24 Sept 2026)'. No solving, no key trials.
