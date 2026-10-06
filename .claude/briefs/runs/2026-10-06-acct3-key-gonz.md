# KEY-GONZ (written by account 3, 6 Oct 2026 17:4x UTC; run IN the account-4 standing session -- the image is in cipher-lab-private). Opus 5.5. Cap $6, box 60 min.
New material (owner ILL, 6 Oct 2026): exhibition catalogue "Mantova e i Gonzaga di Nevers / Mantoue et les Gonzague de Nevers"
(ed. U. Bazzotti, D. Ferrari), p.28 no.18, reproduces a cipher key of Duke Charles (Carlo) Gonzaga-Nevers, undated, Archivio di
Stato di Mantova, Archivio Gonzaga, busta 423, c.396. Private repo: lit/ill-2026-10-06/gonzaga-nevers-cifrario-ASMn-AG-b423-c396-catalogue-p28.png
(and the PDF beside it). It shows: a letter row a..z with 1-3 two-digit homophones each (about 11-71); a nomenclator of ~70 names and
words (Papa 23, Imperatore 31, Re di 91, Cardinale 96, Duca di 41, Italia 69, Spagna 72, Francia 73, Roma 115, Mantova 10, Nevers 99,
Casale 54, Monferrato 51, Savoia 66, ... the, non 88, per 89, perche 108, ...; values up to ~123, some struck through and rewritten);
and a nulls box of ~12 symbols.
1. Transcribe the key from the image (two independent blind Opus reads of the cropped table, + 1 reconciliation; crop with
   tools/iiif_lines.py --image or a PIL crop of the three table blocks, paste the command), into ciphers/_keys/gonzaga-nevers-asmn-ag423-c396/
   key.tsv (value, meaning, kind letter|word|null, grade H, note for struck/rewritten entries, read_agreement). Public repo gets
   the transcription and a README crediting the catalogue and ASMn; the image stays private. key_source: period (archival key,
   seen in a published reproduction).
2. Add rows to KEY-OFFICES.tsv and KEY-DESIGN.tsv (tools/key_design.py), office "Gonzaga-Nevers ducal chancery (Mantua)", decade
   unknown -- Carlo I Gonzaga-Nevers, duke of Mantua 1627-37 (Charles de Gonzague-Nevers b.1580) -- say "1600s-1630s, undated".
3. Run tools/key_crossmatch.py with this key against every unkeyed two-digit ciphertext on disk (the tool's own gate,
   tools/data/key_crossmatch_gate.json, and its control). Any target scoring above the gate: one decode_key trial on that target
   with the matched control first (CLAUDE.md rule 3), Italian or French judge by the letter's language and era. Report the full
   crossmatch table (top 10) whatever happens. Likely candidates by office: Gonzaga/Nevers folders (fr3416-nevers-fils-1589,
   fr398x-nevers-*, arsenal6334-longueville-1650-59, belmesseri-napoli-1627, any Mantua or Monferrato item).
4. NOTES.md in each target touched; ROOM done line for the account-3 orchestrator with the crossmatch top hits and any gate pass.
   No novelty words (rule 10). Stop at 80% of cap/box before a unit.
