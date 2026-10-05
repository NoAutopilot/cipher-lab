# zbz-busbecq-1587

Status: open
Busbecq, *Omnia quae extant* (Elzevir 1633, archive.org bub_gb_EKzs2F1JIA4C) and *Epistolarum legationis Gallicae libri 2* (Louvain 1632, bub_gb_OqDGk6ENA4YC) full OCR text read by this worker on 2 Oct 2026: the French-legation letters in both end with Epist. XLIX, April-May 1585 (dates "xxv./xxvIII. Aprilis clo.Io.lxxxv"), no 1586-87 letter and no Iunii 1587 date; Forster & Daniell vol. 2 (1881, lifelettbusbecq02forsuoft) whole-volume grep for "1587", "June 6", "6th of June": only an unrelated Dohna footnote (line 4352).

## What this is

Augerius Ghislen de Busbecke (Ogier Ghiselin de Busbecq, imperial diplomat, resident in France as agent for
Archduchess Elisabeth and reporting to the Emperor) to Emperor Rudolf II, 6 June 1587, Latin. ZB Zürich,
Ms F 42.5 (swisscollections `ZBC73e7677281a24c689e4d1c1e2a9dd36d`). Scored as K1 by LANE S scout, 24 Sept 2026
(QUEUE.md, "German and Austrian catalogue candidates" section). No image seen this session — access is
`gesuchspflichtig` (application required) at ZB Zürich, Handschriftenabteilung; no ciphertext.txt exists yet.
Catalogue note field (`500 |a`): "Verschlüsselter Brief eines Gesandten an den Kaiser" (an envoy's enciphered
letter to the Emperor) — the cataloguer's own word.

## Check-solved sweep, 24 Sept 2026

Six sources, run directly (no subagents), by the LANE S check-solved worker (batch F).

1. **Web.** WebSearch: `Busbecq Rudolf II 1587 cipher letter Zurich manuscript`, `"Busbecq" cipher solved
   decrypted`. No result names this letter, this shelfmark, or a solution/attempt on it. Nothing found.
2. **Print.** Busbecq's letters from France (1582-1592, to Rudolf II and the Empire) are collected in English
   translation in Forster & Daniell, *The Life and Letters of Ogier Ghiselin de Busbecq* (1881), vol. 2
   (archive.org `lifelettbusbecq02forsuoft`; public, full OCR text fetched to `/tmp/busbecq_vol2.txt`, not kept
   in the repo). Full-text grep for `1587`: one hit, an unrelated footnote about Dohna's 1587 service, not a
   letter date. Grep for `cipher`: three hits, all in one letter (their "Letter XIV") where Busbecq discusses
   drawing up "a code" for the Emperor's use ("what your Majesty's wishes were with regard to the cipher I was
   to use... I drew up a code at Speyer, and put it in a letter, of which I now enclose a copy"), undated in
   the surrounding text but evidently earlier in the sequence (discusses the dowager Queen's return to Vienna).
   No letter dated 6 June (or "June 6") 1587 located in this volume's text. Forster & Daniell state their volume
   is a selection, not the complete correspondence, and most of the France-period letters they print are in
   French, not Latin — consistent with this specific Latin letter to Rudolf II simply not being among the
   letters they chose to translate. Not checked this session: any Latin-language edition of Busbecq's
   collected letters/opera beyond the well-known 1633 Elzevir *Legationis Turcicae Epistolae* (which covers the
   1554-62 Turkish embassy, not the 1580s France period).
3. **Lists.** `sources/cryptiana/web/habsburg.htm` (Tomokiyo, local snapshot) names Busbecq once: "A cipher of
   Ogier Ghislen de Busbecq, a Habsburg delegate to the Turks between 1554-1562, and those of Castaldo and
   Caraffa have 'sophisticated metaphors in the nomenclator table'" — this is his earlier Turkish-embassy cipher
   system (Vienna ÖStA HHStA Staatskanzlei Interiora), a different period, different court archive and
   different working language from this letter's 1587 Latin text to Rudolf II from France; not the same item.
   No hit in `sources/cryptiana/blog/` or `unsolved.htm`. Live Cipherbrain/Cipher Mysteries not fetched this
   session (budget; nothing in the web pass suggested a hit worth a live fetch).
4. **DECODE.** Cannot log in (ASKS row 1, known broken). Checked the cached DECODE catalogue snapshot in
   `aaymeloglu/unsolved-ciphers` (`catalogue/decode-catalog.csv`, 10,107 rows): only two Busbecq/Busbeck records,
   R1220 and R1221 (Vienna ÖStA HHStA Staatskanzlei Interiora, Chiffrenschlüssel, Kt.13 Fasc.20 ff.50-55, dated
   1559, French plaintext, status "Key") — 28 years earlier, a different archive, a different working language.
   Confirms QUEUE.md's own K1 caveat: these are a different item, not this letter.
5. **Bourdeau.** Fresh shallow clone (`GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1
   https://github.com/dbourdeau/cyphersolver /tmp/cyphersolver`, 24 Sept 2026). `grep -ril -iE "Busbecq|Busbeck"`
   across the repo: no hit outside unrelated files (Napoleon-era corpora, an 1812 letters volume) that merely
   contain the substring by coincidence of OCR noise; none is this letter or shelfmark.
6. **Aymeloglu.** Fresh shallow clone (`git clone --depth 1 https://github.com/aaymeloglu/unsolved-ciphers
   /tmp/unsolved-ciphers`, 24 Sept 2026). Same grep: no hit beyond the cached DECODE catalogue rows already
   covered under source 4.

**Verdict: open**, stage 2 verified unsolved (conditional — catalogue-metadata match only, no image or
transcription seen, per CLAUDE.md rule 2). Copy-order target: `gesuchspflichtig` at ZB Zürich, no digitisation
found. See `REQUEST.md`.

Requests this pass: archive.org 3 (advancedsearch metadata query, `lifelettbusbecq02forsuoft` metadata +
djvu.txt fetch), github.com 2 (shallow clones, shared with K2-K4). No swisscollections.ch or kalliope-verbund.info
calls needed for this target this pass (scout already read the record page). No TNA Discovery, no Google Books.

## Web and blog check (CS-A2-A, 2 Oct 2026)

Five WebSearch queries, no hit on this letter:
1. `Busbecq Rudolf II 6 June 1587 enciphered letter Zürich Zentralbibliothek Ms F 42` -- Wikipedia, Wikisource author page, Forster & Daniell catalogue records, Britannica; nothing on the shelfmark.
2. `Busbecq 1587 Chiffre Brief Kaiser Rudolf Paris Gesandter verschlüsselt Zürich Zentralbibliothek` -- Deutsche Biographie, inlibris listing; nothing on this letter.
3. `"Busbecq" cipher decipherment letter Rudolf II France ambassador 1587` -- Gutenberg F&D vol. 2 (opened as the IA copy), Cambridge listing; no cipher item for 1587.
4. Site search, allowed_domains ciphermysteries.com, cryptiana.blogspot.com, scienceblogs.de (Cipherbrain), cryptiana.web.fc2.com: `Busbecq cipher` -- only Cipher Mysteries Voynich posts (Busbecq as a Voynich-provenance figure: Visual Map of Voynich evidence, f116v multispectral, Three Crowns, Tale of Two Voynich Articles, Purdue lecture); none concerns a 1587 letter to Rudolf II; no Cryptiana or Cipherbrain hit. Opened none (titles and snippets only, no Busbecq-letter content), so no comment thread was read: the Voynich threads are not about this letter.
5. Catalogue: swisscollections record ZBC73e7677281a24c689e4d1c1e2a9dd36d fetched once (HTTP 200) but it is a script-rendered page; no text (availability flag, Zugang) could be extracted, so the earlier "gesuchspflichtig" flag recorded 24 Sept 2026 is carried, not re-read by this worker.

Local `sources/cryptiana` last grepped 24 Sept 2026 (habsburg.htm names Busbecq's 1554-62 Turkish-embassy cipher only).

## Premise check (CS-A2-A, 2 Oct 2026)

- (a) folder's own mentions: NOTES.md/REQUEST.md name no decipherment, gloss or clear copy; the catalogue calls the letter "verschlüsselt". Not found.
- (b) solver repos, fresh shallow clones 2 Oct 2026, grep `busbe`: dbourdeau/cyphersolver only targets/matignon1586/corpus_words_v1.txt (a word list, not this letter, not opened further); aaymeloglu/unsolved-ciphers only the DECODE catalogue rows R1220/R1221 (1559 Chiffrenschlüssel, ÖStA, a different item). Not found for this letter.
- (c) physical neighbours: no image; nothing to view. Unreachable.
- (d) recipient's side: Rudolf II's Austrian side -- not searched this pass (no edition located; Busbecq's own letters-in-print end 1585 as above). Unreachable/unsearched. Lead: F&D vol. 2 Letter XIV prints a cipher/"code drawn up at Speyer" for the Emperor's use (undated); a sibling key may exist in print or in Vienna.

Where it was not found: the printed Latin letters to Rudolf II cover 1582-85 only, so the 1587 letter lies outside every printed Busbecq edition opened; Austrian archive editions (HHStA Staatskanzlei Frankreich) were not searched.

## Next step (NO-CRACKS, 5 Oct 2026)

next: search the Austrian side: HHStA Staatskanzlei Frankreich finding aids and any printed edition of Busbecq's 1586-87 reports to Rudolf II, plus the Speyer code in F&D vol. 2 Letter XIV as a possible sibling key, ~$1. Who acts: agent. Source: this file's premise check (d) ("Austrian archive editions ... were not searched"); written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.
