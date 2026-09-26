# RAH Índice de la Colección Salazar y Castro — cipher mentions

Manifest for a single large source text, not committed here (30MB convention, CLAUDE.md Access
playbook item 4): the full 49-volume *Índice de la Colección Salazar y Castro* (Real Academia de
la Historia, Madrid, 1949-1979), scanned and OCRed (Tesseract 5.3.0) as a single volume.

- Internet Archive identifier: `salazary-castro-22-nov-2016`
- Full-text URL: `https://archive.org/download/salazary-castro-22-nov-2016/SalazaryCastro_22_nov_2016_djvu.txt`
- Fetched 26 Sept 2026 (LANE NX2 worker NX2-INDEX): 30,940,299 bytes, 1,084,507 lines, matches the
  size SCOUT-OWN-4 recorded on first discovery (25 Sept 2026).
- One request to archive.org this session, `curl -A "cipher-lab research script (contact via repository)"`.

## cipher_mentions.tsv

Every catalogue entry in the OCR that mentions "cifra"/"cifr"/"desci" (2,297 of the Índice's
~77,750 parsed entries), classified U (marked undeciphered by the RAH's own cataloguers),
D (a decipherment, translation, or period marginal/interlinear reading is on file for this same
entry, or the entry is itself that companion decipherment), or P (bare mention or non-cryptographic
use of "cifra"/"descifrar", e.g. "imposible de descifrar a causa de la humedad" = illegible
handwriting, not cryptography).

Method: fetch once, grep and parse by script (CLAUDE.md Usage item 2); no subagents. Entries were
split on each `N2 <n> del inventario` end-marker (the catalogue's own per-document boundary). U/D
classification used a small set of Spanish phrase patterns (see `classify.py`/`classify2.py` in
this worker's own scratch directory, not committed — a future worker should port the regex into
`tools/` if this source gets a second pass, per CLAUDE.md Usage item 8). A cross-entry check
promotes a bare "en cifra" mention to D when the *immediately following* catalogue entry opens
"Texto descifrado ..." or "Traducción del documento anterior ..." (the Índice systematically files
period decipherments/translations as their own following entry, not as a note on the cipher
entry itself).

Columns: `line` (1-indexed line in the OCR where the entry's own trailing `N2 ... del inventario`
line starts, i.e. an anchor for `sed -n` re-inspection), `tomo` (the shelfmark's letter prefix,
e.g. `A` for `A-NN`), `inv_no`, `shelfmark`, `date`, `place`, `sender` (best-effort name match
against a short known-correspondent list, blank if not matched), `recipient` (best-effort, default
"Carlos V" when the entry says "dirigida a éste"), `class` (U/D/P; `U+D` means both an undeciphered
marker and a decipherment-shaped phrase matched in the same entry span — read by hand, see
QUEUE.md), `index_wording` (the matched sentence, truncated), `key_route` (a published-key
pointer for the sender if known, from `sources/cryptiana/web/spanish2C.htm`'s Ko.1-Ko.17 list and
`sources/cryptiana/web/AlonsoSanchez.htm`, else "none known").

**Known limitation, entry-boundary attribution.** A handful of entries carry a trailing
"Observaciones:" note (e.g. "a continuación se notan arrancadas las hojas que debieron contener
el texto descifrado...") that the RAH's own catalogue prints *after* the entry's own
`N2 ... del inventario` line and *before* the next dated entry's heading. This script's
end-marker splitting attributes that trailing note to the *following* entry, not the one it
actually describes. Two cases found and hand-corrected in QUEUE.md: inv. 3090 (Alonso Sánchez,
1522.05.14 Venecia, A-24 f.65-67) — the "hojas arrancadas" note at line ~43411 that the TSV
attaches to the unrelated next entry (inv. 3091, Próspero Colonna) actually says *3090's own*
decipherment leaves (and two Fernando Marín letters catalogued in "Apéndice B" nos. 124-125)
were torn out of the volume. **"Apéndice B" is not a hidden decipherment appendix** — its own
header reads "Documentos sustraídos a la Colección, y que no han sido reseñados en el cuerpo del
[catálogo]" (documents *stolen* from the collection, not described in the catalogue body): items
cross-referenced there are catalogued as missing/stolen, not recoverable from RAH's own holdings.

## Counts (this pass)

U 18, U+D 9 (27 total genuinely-undeciphered-or-ambiguous entries, read by hand), D 1,424, P 846.
Full breakdown and the P spot-check in QUEUE.md's "RAH Salazar y Castro index, cipher mentions"
section.
