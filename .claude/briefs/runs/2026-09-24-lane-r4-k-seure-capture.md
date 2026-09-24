LANE R4 WORKER K -- fr3151 SEURE 1558 CAPTURE: images, glyph atlas, two passes (Sonnet, cap $8). Target: ciphers/fr3151-seure-1558.
Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md (you are one of the two gallica.bnf.fr fetchers). Read .claude/briefs/
transcription.md and NOTES.md (ark btv1b9059865k; nos. 39-44 around views 72-88; about eight pages, ~2,000 signs: ~60 invented signs plus
numerals; two duplicate pairs among the six letters).
1. tools/gallica_folio.py for the canvases; fetch each cipher page once at native resolution into images/ with manifest.json (folder under
   30 MB: keep natives of cipher pages only). Record which letters are duplicates of which (two minutes, per the transcription template).
2. Atlas first (tools/glyph_atlas.py over all cipher pages; codes by shape, numerals as digits). Commit.
3. Box-keyed passes, as fr2933-salviati-1525 did (script classifies each box against the atlas; pass A by you, pass B by one Sonnet
   subagent blind; confirm/correct per box). Transcribe ONE letter of each duplicate pair first, then the singletons; commit per page.
4. Per page agreement by (line, pos); gate 80%; settle disagreements; ciphertext_<letter>.tsv. Stop at the cap with what is done.
No solving. NOTES.md "Capture and passes (24 Sept 2026, LANE R4 K)". Report gallica request count. ROOM done: "for LANE R4: seure capture <pages>, <tokens>".
