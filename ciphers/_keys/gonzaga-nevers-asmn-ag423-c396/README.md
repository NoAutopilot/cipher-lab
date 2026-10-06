# Gonzaga-Nevers cipher key, ASMn Archivio Gonzaga b.423 c.396 (KEY-GONZ, 6 Oct 2026)

Source: Archivio di Stato di Mantova, Archivio Gonzaga, busta 423, c.396 -- an undated cipher key ("cifrario, con le relative chiavi di
lettura") of Duke Carlo I Gonzaga-Nevers (Charles de Gonzague-Nevers, 1580-1637, duke of Mantua 1627-37), as reproduced in the exhibition
catalogue *Mantova e i Gonzaga di Nevers / Mantoue et les Gonzague de Nevers*, ed. U. Bazzotti and D. Ferrari, p.28, no.18. Credit: the
catalogue's editors and the Archivio di Stato di Mantova. The reproduction (owner's interlibrary loan, 6 Oct 2026) is kept in the private
repository only; this folder holds our transcription of it. key_source: **period** (archival key, seen in a published reproduction).
Years: 1600s-1630s, undated.

Design: letter row a..z (no j, k, v, w, x, y; "qu" one cell) with 2-3 two-digit homophones each (10-90); a nomenclator of names and words
with values 22-128 (titles, places in Italy and Monferrato, address forms, articles and particles); a box of 15 null symbols ("Nulle").
Several column-1 and column-3 entries are struck through with other words written beside them (a later re-use of the codes); most of
those replacement words are not legible in the reproduction and are graded M.

`key.tsv`: code, value, kind (letter | word | null), grade, note, read_agreement. Transcription: two independent blind Opus reads of
nine crops of the catalogue page (PDF p.15 rendered at 275 dpi; PIL crops of the letter block and the four nomenclator columns, upper and
lower halves, 2x upscale), reconciled by the job session against zoomed crops. 142 rows: letters 45 (38 H, 7 M), words 82 (55 H, 27 M),
nulls 15 (symbol descriptions). The two reads disagreed on 4 cells (a 11/15, Re di 95/91 noted, 81's label V.S.ria/S.S.ria, 81's added
number 121/123); each was settled on a zoomed crop and is graded M. Codes 93, 94, 98, 100, 113, 121, 128 (column 1), 58, 59 carry both
the struck word and its replacement; 122 is read for both "Consiglio" (struck, column 1) and "dal" (column 4, 122|127 unclear).

## Crossmatch (KEY-GONZ step 3, 6 Oct 2026 19:51-20:27 UTC): non-test, language not read

`python3 tools/key_crossmatch.py --out-tsv <scratch> --quiet` (full sweep, 36 min) paired this key with 89 digit ciphertexts at coverage
>= 0.5, but every pair came back `no_corpus` (0 scored): the tool reads a key's language from its folder's NOTES.md, and for a path under
`ciphers/_keys/` the folder is `_keys`, which has none; the `# language: it` header line is read only for `EXTRA_KEY_GLOBS` paths. So this is
a non-test, not a negative. Top coverage (unscored, for the next run): szembek-bk1560 1.000 (n=434), colbert26-lathuillerie-1644 f23 0.997
(306), fr3993-gonzague-nevers-1595 0.947 (189), fr4712-nevers-duchesse 0.923 (39), malsburg-hessen-1636 0.903 (352),
oxenstierna-gustav-adolf-1632 0.882 (771), sanguszkow-mniszech-dunin-1714 0.875 (232), birago-fr3252-1571-72 f100 0.872 (274),
lodewijk-van-nassau-1573-74 4614 0.864 (2456), lodewijk 4503 0.844 (237). High coverage alone means only that the codes 10-128 occur.
Next: add `ciphers/_keys/*/key*.tsv` to `EXTRA_KEY_GLOBS` in tools/key_crossmatch.py (so the header's language/office/years are used, with
an offline test), then rerun the sweep (~36 min) or a `--since` run on this key; fr3993-gonzague-nevers-1595 is the office-matched
candidate (Nevers, 1595) to try first with decode_key and a matched control if it clears the gate. ~$2.
