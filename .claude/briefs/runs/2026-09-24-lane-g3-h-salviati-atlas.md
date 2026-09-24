# LANE G3 worker H: M35 fr2933-salviati-1525 shared glyph atlas + atlas-coded passes on f.54r (Opus lead, Sonnet passes; cap $8; disk only)

Read .claude/briefs/transcription.md, ciphers/fr2933-salviati-1525/NOTES.md 'Capture and passes (24 Sept 2026)' (worker F: two free-text passes
agree on 4.7%, every symbol token disagrees) and ciphers/dupuy452-carpi-1520/glyphs/ (build.py, cluster.py, classify.py: the worked atlas pattern;
reuse or extend it, do not write a parallel copy; anything reusable goes to tools/ with --help and a test).
1. From the natives on disk (no fetches), segment the non-numeral signs on all cipher pages and cluster them by shape into ONE atlas
   (glyphs/atlas.png contact sheet + atlas.tsv: code, exemplar crops, count, pages). Decide yourself (Opus) the merges and splits from the
   contact sheet; note the small superscript numbers as a separate attribute, not new codes.
2. Two blind Sonnet subagent passes of f.54r only, each given the atlas and told to use its codes (numerals as written, plain Italian words as
   w:<word>). Commit each pass. Reconcile with tools/reconcile_passes.py. Gate: >= 80% row agreement on f.54r. If it passes, settle
   disagreements.tsv from the image and write ciphertext_f54r.tsv; report tokens and types. If it fails, report the agreement, which codes
   confuse (confusion table), and stop.
No solving, no key trials, no other pages' passes. NOTES.md section 'Glyph atlas and atlas passes (24 Sept 2026)'.
