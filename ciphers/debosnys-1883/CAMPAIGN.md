target: debosnys-1883
goal: a reading of any one of the four cryptograms at N3 or better, or a control-backed identification of the system
started: 2026-09-28 21:15 UTC
daily_budget_usd: 200
spent_today_usd: 0
spent_day: 2026-09-28
key_known: no (the Adirondack History Museum found no key sheet or cipher alphabet among Debosnys's papers, reply of 28 Sept 2026, MAIL-3, NOTES.md "Museum reply")
crib_available: partial (published clear poems: the 14-line French poem on the cryptogram-3 page, clear_poems.tsv, plus the Greek poem Sektu reports on the c4 reverse, not on disk; the museum's restricted clear-text scans, about 43 images, are NOT available to account 3 and never enter this repository or this runner's work, RESTRICTED.md)
pool_signs: 1251 signs over 160 ids after GOLD-4C's by-eye split (c1 132, c2 734, c3 116, c4 269; 29 `_` and 35 `MULTI` boxes excluded); K_base 128 with 16 mark classes (GOLD-D1); pooled IC 0.0391 at 160 ids, 0.0489 at base level, against uniform-at-K 0.0063 and French 0.0697
solvability: transcription-limited, nothing read. The 62 pct figure is TRANSCRIPTION agreement between two blind passes on cryptogram 1, not a reading: c1 62.3 pct full-id / 66.4 pct family-level (160 ids, 52 columns unsettled, GOLD-4E); c4 22.4 pct at 68 ids (GOLD-4A, three quarters of it inventory confusion per GOLD-4C, settled ceiling on the image about 91 pct); c2 and c3 have one pass only. The 80 pct gate for writing ciphertext.txt is unmet on every cryptogram.
keyless_threshold: letter-substitution designs are not licensed by the numbers (GOLD-D1/D2, tools/family_run.py --family homophonic, fr19, profile=target, seeds 1-3, controls only, target never run): at base level (N 1251, K_base 128) the control recovers 0.859 of plaintext clean, 0.816 at 2.5 pct type noise, 0.385 at 5 pct, 0.322 at 7.5 pct, 0.314 at 10 pct; at K 160 it is 0.440 clean, 0.421 at 5 pct; c2 alone (N 734, K 102) 0.669 clean, 0.433 at 5 pct. A settled two-pass transcription carries 5-10 pct type noise, on the flat part of that curve. So a reading needs one of: a transcription under about 3 pct type noise (H2), a design other than letter substitution whose own control tolerates the measured noise (H3), or a crib that pins types by position (H4).
closed:

## Attempts already made

- GOLD-0D (25 Sept 2026, check-solved, Sonnet): eight source families (Farnsworth 2010 and Bauer 2017 by Google Books
  snippet and IA full text, Cipherbrain FAQ and Top-50 post 3 with comments, Cipher Mysteries 7 Nov 2015 with 90
  comments, DECODE crawl, both solver-repo snapshots, OpenAlex/S2/CrossRef, web search incl. Reddit/forums/AI-solve
  claims, the Sektu 2017 series): verdict `open`, no solution or key found; the only partial guess on record is one
  Cipher Mysteries commenter's "ULTIME" for the last word of the L.M.F. page, no method, no key. Neither book was read
  page by page (no loan). Rule 10: a search result, not a novelty verdict.
- LANE B2 bDEB (25 Sept 2026): images of c1, c2a, c2b, c3 from Schmeh's post; machine segmentation and k=90 clustering
  (tools/glyph_atlas.py); IC indistinguishable from uniform at that over-split K.
- GOLD-4A (25 Sept 2026): c4a/c4b fetched (six page images now on disk); 90 clusters merged by eye to 68 ids; c4 pass B
  (Sonnet, blind) agreed 22.4 pct with the kNN pass A; X is 15 pct of tokens and self-adjacent (not a divider); Y-CURL
  never self-adjacent.
- GOLD-4B (25 Sept 2026, form test): clear_poems.tsv (the c3-page poem, 14 lines, 9-15 syllables, irregular meter);
  sektu-2017.md; only c4a's line count (14) matches the poem's, r 0.44 against syllables/line at the 93.6th percentile
  of a shuffle null, and Sektu's own count of the cipher poem is 20 lines (both pages), so the 14-line match reads as
  half the object: control-backed negative for "the c3 poem is a full crib for one cryptogram as paired here".
- GOLD-4C (25 Sept 2026, Fable): every box labelled by eye, 160 ids / 158 families (glyphs/box_labels.tsv,
  inventory.png); 36 composite ids (base sign plus stacked strokes) cover 20 pct of signs; c4's 228 disagreement columns
  classed 76 pct inventory confusion, 15 pct segmentation, 9 pct reading error; `glyph_atlas.py classify --exclude-page`.
- GOLD-4E (25 Sept 2026, Sonnet): c1 pass B blind against the 160-id atlas: 62.3 pct full-id, 66.4 pct family; 52
  disagreement columns classed mechanically only (segmentation 7, inventory 5, reading 40), never settled on the image.
- GOLD-D1, GOLD-D2 (25 Sept 2026, Sonnet, controls only): base+mark recount (K_base 128), `profile=target` and
  `noise=p` params for tools/families/homophonic.py, the noise curve in the header above; gate written before the numbers
  (base mean >= 0.5 at 5 pct and >= 0.4 at 7.5 pct) failed both, verdict (c) for the letter families; nothing run on the
  target. GOLD-CONS3/CONS4 parked the target on ASKS 52 (museum).
- MAIL-3 (28 Sept 2026): the museum's reply -- no key; restricted clear-text scans shared to the project's Google
  account under RESTRICTED.md (off this account, off the repo).
- Sektu 2017 (not ours, credited): rejected one-symbol-per-syllable French alexandrine for the cipher poem against a
  Baudelaire control; N-glyph nasalisation count "promising, more work needed"; corpus-wide 1188 glyphs of 425 types
  under his own segmentation.

## Hypotheses

| id | rank | hypothesis | needs | est_usd | status | result |
|---|---|---|---|---|---|---|
| H1 | 1 | Check-solved refresh, 28 Sept 2026: every published claimed solution or partial reading (Cipherbrain posts and their comment threads incl. the 2021 posts, Cipher Mysteries posts and comments, cipherfoundation.org's Debosnys page, Farnsworth's Adirondack Enigma and Bauer's Unsolved! by snippet/full-text, Sektu 2017, Reddit r/codes and r/cryptography and forums, news and podcasts 2019-2026, the two solver repositories fresh); for each claim, what it reads and whether it survives a control (a reading that reproduces from a stated key on the image, or a method that beats a shuffled-text null); a prior accepted reading of any cryptogram is N0 and closes the campaign | nobody | 6 | open | |
| H2 | 2 | Settle cryptogram 1 at native resolution: a third blind pass (Fable vision, value-blind: crops of glyphs/strips/c1_L0*.jpg cut per sign with tools/iiif_lines.py --image, never passA/passB opened first) on the 52 unsettled columns of disagreements_c1_passB.tsv, adjudicated against passes A and B with a per-sign rule written in scripts/PROMPTS_c1.md before any crop is looked at (two-of-three on full id; family fold as fallback; a three-way split stays M); target 80 pct full-id agreement; report the new agreement, the settled K for c1, and the type-noise estimate the settled draft carries against the GOLD-D2 curve | nobody | 12 | open | |
| H3 | 3 | System identification beyond letter substitution, each with a known-answer control built from a period sample of the system: (a) French shorthand of the 1870s-80s (Duployé 1867, Prévost-Delaunay, Aimé-Paris), (b) Pitman, (c) a syllabary or nomenclator with pictograms, (d) a mixed Greek/Latin letter alphabet (the Greek poem on the c4 reverse and Debosnys's own Greek), (e) rebus/pictogram code. For each: sign-shape fit (stroke inventory, composite/mark structure) and frequency fit (sorted profile, IC, mark share 18.6 pct) of the settled c1 inventory against a matched null (a shuffled-id inventory and a random-stroke inventory); a system whose control fits and whose target fit clears its null gets a follow-up row | nobody | 15 | open | |
| H4 | 4 | Crib test: the published clear poems (clear_poems.tsv c3 poem, 14 lines; the Anacreon-preface Greek poem Sektu identifies on the c4 reverse once its text is on disk from Moore's printed Odes of Anacreon) as candidate plaintexts or host texts for any cryptogram: length, line structure, and repeated-sign positions vs repeated-word/repeated-syllable positions, under each of sign=letter, sign=syllable, sign=word, against shuffled-poem and shuffled-line controls (1000 trials each); a pairing that clears the 97.5th percentile on two independent statistics gets a follow-up row | nobody | 8 | open | |

## Log

2026-09-28 21:15 | session_018qnyJQbVSd2NyPvDVApXqS | seed | 0 | CAMPAIGN.md written, 4 hypotheses; trigger trig_01VgraqxhG9sBZqKGB3FopQa (:35) bound to this session.
