# BnF Baluze 103, f.50 — Michel Le Tellier (Secretary of War) to Pierre de Marca, governor of Catalonia, April 1644

Status: blocked
DECODE catalogue (files on disk, `aaymeloglu/unsolved-ciphers` cached snapshot; no login used, per lane rule
that only the DECODE worker logs in) names a record whose shelfmark tag is this exact leaf and whose status is
"Decrypted" — see below. This contradicts Tomokiyo's "undeciphered" tag for the same folio and cannot be
resolved from files on disk; RecordsView needs a DECODE login this worker does not have.

Check-solved pass, 24 Sept 2026 (Sonnet, csKT/LANE N4, cap $5 shared with KT-01). Row KT-02 from
`sources/solver-diffs/2026-09-24-tomokiyo-vs-siblings.tsv` (scTOMO, LANE N4).

## Identification

- Image: Gallica `btv1b9001389d`, canvas f111 r (recto, 50r) / f112 v (verso), confirmed by the leaf's own
  "avril 1644 ... 50" dateline+foliation (eye-read at high zoom by scTOMO, not re-verified this pass).
- Native size: 4864x6996 both sides.
- Image URLs: `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9001389d/f111/full/full/0/native.jpg`,
  `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9001389d/f112/full/full/0/native.jpg` — copy-free, full
  resolution, no login. The volume's own Gallica title (found by web search this pass): "Affaires de
  CATALOGNE. — Correspondance de MARCA. Baluze 103."
- Key: Le Tellier-Marca Cipher (`sources/cryptiana/web/louisxiv0.htm`, table image
  `louisxiv_0marca1644.png`, "not using syllable representations").

## Tomokiyo (`louisxiv0.htm`), quoted verbatim

*"Le Tellier's letters use the following cipher in April to October 1644 (f.50 (undeciphered), f.171, f.189,
f.200, f.230 (deciphered on separate pages))."* — f.50 is the one leaf of this five-leaf group Tomokiyo tags
undeciphered; the other four are explicitly "deciphered on separate pages."

## DECODE finding — the blocker

`sources/decode/records-decrypted-2026-09-24.tsv` (this session's own DECODE-worker sweep, on disk, no login
used to read it) row:

```
id=2742  status=Decrypted  holder="Paris, Bibliothèque nationale de France, Baluze 103, f.51-52"
shelfmark_code=BnF_Baluze103_f50  date_range="1644 -"  plaintext_lang=French  pages=2
```

Cross-checked against `aaymeloglu/unsolved-ciphers`'s cached `catalogue/decode-catalog.csv` /
`catalogue/decode-records.jsonl` (fresh shallow clone this pass), same record: sender field "Le Tellier",
country "France", record URL `https://de-crypt.org/decrypt-web/RecordsView/2742`.

The four siblings Tomokiyo calls "deciphered on separate pages" are also in this file, and their DECODE tags
match their folio numbers exactly:

| DECODE id | holder folios | shelfmark tag |
|---|---|---|
| 2743 | f.171-173 | BnF_Baluze103_f171 |
| 2744 | f.189-191 | BnF_Baluze103_f189 |
| 2745 | f.200-206 | BnF_Baluze103_f200 |
| 2746 | f.230-233 | BnF_Baluze103_f230 |
| **2742** | **f.51-52** | **BnF_Baluze103_f50** |

For 2743-2746 the tag's folio number is the first folio of the holder string's own range (171=171, 189=189,
200=200, 230=230) — the tag and the description agree. For 2742 they do not: holder says "f.51-52", tag says
"f50". Two readings are possible: (a) this is our leaf (f.50, tagged correctly, with "f.51-52" a cataloguing
slip for "f.50-52" or similar), and DECODE holds it as already Decrypted, contradicting Tomokiyo; or (b) this
is a different, adjacent leaf that happens to generate the same tag pattern. Given DECODE's own tagging
convention on the four siblings (tag = first folio of the holder range), reading (a) is the more likely one —
the tag was very likely built from the same "f.50" locator Tomokiyo uses, and the holder string's "51-52" is
the slip, not the tag.

This cannot be resolved further from files on disk: RecordsView and DocumentsList (needed to see whether an
actual decipherment document is attached, and to check the leaf image DECODE is describing) both require a
DECODE login, and per this lane's common rules only the DECODE worker logs in — this worker does not have
DECODE_USER/DECODE_PASS access this session. No unauthenticated fetch of `de-crypt.org/decrypt-web/*` was
made (host not in this brief's list; per common rule 4, DECODE beyond files-on-disk is out of scope for a
non-DECODE worker).

## Other sources checked, 24 Sept 2026

1. **Web search.** "Le Tellier Marca 1644 chiffre déchiffré Baluze 103" and "Sanabre Le Tellier Marca 1644
   Catalogne chiffre lettre déchiffrée Baluze": both return only generic biographical pages (Wikipedia on
   Baluze, Marca, Le Tellier) and the BnF archivesetmanuscrits catalogue title for Baluze 103 itself
   ("Affaires de CATALOGNE. — Correspondance de MARCA. Baluze 103", with a snippet noting "eighty-one original
   letters addressed to Marca by the comte d'Harcourt, vice-roi of Catalonia, 14 Dec 1644-19 Oct 1645" — a
   different correspondent, not this letter). No page found naming this specific letter as solved or citing a
   reading of it in a Le Tellier/Marca/Catalonia-1644 secondary literature.
2. **Print editions named in the brief** — not opened this pass: Sanabre's *La Acción de Francia en Cataluña*,
   the printed *Lettres de Le Tellier* series, *Mémoires de Marca*, and Chéruel's *Lettres de Mazarin* t.1-2
   were not located as free full-text and not read; this is a gap in the pass, not a negative result — see
   "blocked" status. Google Books API search ("Le Tellier Marca 1644 chiffre Baluze") returned only unrelated
   sale catalogues and modern Catalan-history volumes, no snippet naming this letter.
3. **Cryptiana blog / Cipherbrain.** `louisxiv0.htm` quoted above. No scienceblogs.de/klausis-krypto-kolumne
   post found for "Le Tellier" "Marca" "chiffre" (not separately re-searched this pass beyond the KT-01 query
   pattern; treat as unchecked, not a negative).
4. **Bourdeau shallow clone.** Grepped all folder READMEs/NOTES for "marca", "baluze 103", "le tellier"/
   "letellier": the repo's `letellier/` folder is a *different* item — its own NOTES.md header reads "Le
   Tellier -> Marquis de Castelnau, 12 May 1657 — tracker item #15" (BnF fr.5160-family, cryptiana
   transcription `LeTellier_Castelnau1657.txt`), confirmed by opening the file this pass, not merely cited from
   an earlier worker's grep. `louis1615/NOTES.md` mentions "Baluze" only for Baluze 155 (a different volume,
   Louis XIII to Sabran, 1631). No Baluze 103 folder or NOTES hit anywhere in the clone.
5. **Aymeloglu shallow clone.** No dedicated folder for Baluze 103/Marca/Le Tellier 1644; the only hits are the
   cached DECODE catalogue files used above (`catalogue/decode-catalog.csv`, `catalogue/decode-records.jsonl`),
   which is the census this worker is relying on for the blocking finding, not an independent solve claim.
6. **DECODE files on disk.** See "DECODE finding" above — this is the source of the block, not a clean negative.

## Leaf check (24 Sept 2026, scTOMO)

Both sides at native resolution: recto and verso entirely in cipher, no interlinear or marginal gloss. Not
re-verified by this worker.

## Verdict

**blocked** — DECODE record R2742 (shelfmark tag `BnF_Baluze103_f50`, sender Le Tellier, 1644, 2 pages) is
tagged "Decrypted" and most likely names this very leaf, contradicting Tomokiyo's "undeciphered" tag for
fr./Baluze 103 f.50; confirming or ruling this out needs `RecordsView`/`DocumentsList` for record 2742, which
require the DECODE login this worker does not hold. No nomination line posted. Do not promote KT-02 until the
DECODE worker opens record 2742 and reports what it holds.

**flag for the lane orchestrator**: route record 2742 (`https://de-crypt.org/decrypt-web/RecordsView/2742`) to
the DECODE worker as a priority check before any further work on this target; if it does hold an attached
decipherment of Baluze 103 f.50, this is `found-solved`, not a stage-2 nomination target, and the same check
should be run before nominating any other Le Tellier-Marca-cipher leaf from `louisxiv0.htm`.

Grades: none (no reading attempted). Novelty: not assessed (rule 10 — this is a check-solved verdict, not a
verifier pass).
