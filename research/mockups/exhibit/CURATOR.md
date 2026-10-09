# Curator's notes: three cipher displays (private mock-up)

Written 9 Oct 2026 (22:45 UTC by date -u) before building. Private mock-up for the owner; not published, not linked.

## What the maker wants to convey, worries about, is excited by
- **One story per display**: Rome 1530 (a king's divorce suit held up), Berlin 1712 (what London would and would not do to end
  the war in the North), Dillenburg 1573 (the names a 19th-century editor had to leave blank).
- **Worried about**: over-claiming (rule 10 wording only: "no prior decipherment located", never "first" or "new"); showing the
  audit's class (N) and depth (D) where the visitor can find them; whose key it was (Tomokiyo and Lasry; Krauske 1893; the
  contemporary gloss); every image credited, with its reuse terms stated or marked "to check before any publication".
- **Excited by**: the object itself (the page), and the reveal: signs on top, the words underneath.

## What the visitor wants
- A story and a secret; to see the real page; to watch the secret open; to recognise faces and a moment they half know
  (Henry VIII's divorce, the end of the Great Northern War, the Dutch Revolt); to try a sign; one sentence to take home.
- More interesting with: hero object first; faces; a dated moment; a map; layers (headline, panel, proof); a hands-on bit.

## Plan (each display, top to bottom)
1. HERO: a real cipher line from the page; a button lays the reading under it, three layers per line: the signs (image),
   the plain text as read in its own language with grade marks (colour + letter), and "English (translation, interpretation)".
2. HEADLINE: one sentence, drawn from the audit's safe sentence and depth sentence.
3. FACES: public-domain portraits from Wikimedia Commons (extmetadata checked), five-word caption; silhouette where none.
4. THE MOMENT: three to five dated events, and a small inline SVG map.
5. THE SECRET: the gist once, marked interpretation, with the cipher words that carry it.
6. TRY IT: three signs from the key, click to reveal.
7. HOW WE KNOW: badges (N-class, depth, audit dates, grade bar, whose key, regenerate script). No paragraph over two sentences.

Choices: Gramont's hero is f.29r (N4, to Villandry); the papal suspension is context from the Montmorency letter of 28 Mar
1530, which is *known text* (printed by Le Grand) and is shown as a key check, never as our reading. Manteuffel's hero is
f.410 (N4); frame 0391 (N3) supplies the Oxford/Bolingbroke story, labelled as its own item. Nassau's hero is WVO 5797 p.7
and p.5 (N4 for the two blanks only; the rest of the letter is Groen's print).

## What happened in the build (9 Oct 2026, 22:4x-22:5x UTC)
- Portraits: Wikimedia answered 429 to all three requests (2 en.wikipedia, 1 Commons); stopped there. Every face is a labelled
  placeholder (`portraits/manifest.tsv` says how to fill them). No non-free image used.
- Gramont: Gallica's IIIF answered 403 twice; the crops come from the folder's own 1400 px page image (`images/f29_item21.jpg`), so
  they are soft. A native-resolution fetch from a desk browser would sharpen the hero.
- Nassau pages 5 and 7: rendered from the Huygens WVO PDF for letter 5797 (1 request).
- Manteuffel: crops cut from the frame already on disk (0511), deskewed 1.75 degrees.
- Image reuse terms: BnF not public domain (permission); SHStA Dresden and KHA/Huygens not recorded. All three are flagged on the
  page; nothing here is fit to publish until those are settled.
- Colours: grades use the repo's CVD palette (blue firm, orange uncertain, grey unread; `tools/cvd_check.py` PASS light and dark);
  grade letter and underline style carry the grade without hue.
- Rebuild: `python3 research/mockups/exhibit/build_exhibit.py` (reads token files and keys; writes nothing under ciphers/).
