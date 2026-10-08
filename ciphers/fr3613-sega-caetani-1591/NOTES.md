blocked
Meister 1906 (archive.org diegeheimschrift00meis, full text) read by this worker pp.420-421 and grepped whole-volume for Sega/Caetani/Rondinelli; no printed edition of Sega's 1590-91 letters could be opened (Acta Nuntiaturae Gallicae not on archive.org, searched 8 Oct 2026), so the verdict is blocked, not open.

# Sega (bishop of Piacenza) to Cardinal Caetani, Paris, 9 January 1591 -- BnF Français 3613 no.88, fol. 148

Job BNF-Q13-CS for LANE BNF-FOCUS (account 2), 8 Oct 2026, 00:02-~00:40 UTC. Status word: `blocked` (edition unread), not a negative.
BnF notice (sources/bnf-findingaids/2026-10-07/cc50063m.html, via tools/bnf_findingaid.py): "Lettre, avec chiffre, de FILIPPO SEGA, vescovo di Piacenza ... all' illmo ... Sor cardinale Caetano ... Di Parigi, li 9 di gennaro 1591. En italien." No decipherment flag.

## Leaf look (Gallica btv1b90582263, canvases unlabeled; canvas = folio + 9 here)
Canvas 157 = f.148r (clear Italian, addressed "Illmo et Rmo ... Cardinale"); canvas 158 = f.148v: the letter's last lines carry a block of about four lines of digits (single digits and two-digit groups, ~200 digits) inside the clear text, then "Di Parigi li 9 di Gennaro 1591", signed Sega. No interlinear or marginal decipherment, no slip, facing page (f.149r) blank. Viewed at 700-900 px only, not native.
Which cipher: not decoded. The digit repertoire (single digits for some letters, two-digit numbers in the 20s-40s) is the same kind as the Caetani table Meister prints, but that is a visual impression at low resolution, not a match. Tomokiyo's Jan 1591 Mayenne-Sega cipher: not compared.

## Key availability (unit 4)
Meister 1906 is on archive.org in full text (identifiers diegeheimschrift00meis, diegeheimschrift00meisgoog). pp.420-421 print "Cifra con Ill.mo signor cardinal Caetano legato in Francia, 28 Settembre 1589": five alphabets (1-5) with nulls 1, 5, 0, 10, 50, 11, 15, 51, 55, 00 and a word list (et, con, non, che, chi, per, perche ... V.S. Illma = 99), two-digit values 22-49 plus single digits for some vowels. The table prints in full in the OCR (djvu line ~92890). Meister footnote: Caetani, sent by Sixtus V 1589 to support the League (Ehses, Nuntiaturberichte I,2, p.LX). Meister p.~71 text (djvu line 6771) also mentions a cipher usage with "cardinal Sega legato in Francia". Whether Sega's letter to Caetani in Jan 1591 uses this 1589 table is untested; the cipher given to Caetani was for correspondence with Caetani, which fits the addressee.

## Prior-art search (what was checked, 8 Oct 2026)
- Bourdeau cyphersolver (shallow clone, grep of md/tsv/json): no hit for Sega, Caetani, Rondinelli, fr.3613. Existing folder ciphers/fr3984-sega-1593 concerns other Sega-era items (Baudouin-Desportes, 1593), blocked on Acta Nuntiaturae Gallicae too.
- Tomokiyo (sources/cryptiana/web, grep): polyalphabetic.htm line 126 names Caetani's cipher "four substitution tables numbered 1-5 (Meister (1906), p.420)", possibly broken by Chorrin; no mention of this letter.
- Meister whole-volume grep: no letter of Sega's printed, only keys.
- Desenclos and Lasry 2024 (NEALT 53): cited for fr.3615 f.52 interlinear (Henri IV, 19 Apr 1591); different volume.
- Not reached: Acta Nuntiaturae Gallicae / Nuntiaturberichte for the Sega legation; DECODE; Aymeloglu repo; HathiTrust; JSTOR.

## Web and blog check (BNF-Q13-CS, 8 Oct 2026)
Queries (WebSearch standard): "Filippo Sega Caetani 1591 lettera cifra Parigi decifrata"; "Cipher Mysteries OR Cipherbrain OR Cryptiana Sega legate France 1591 cipher Caetani Meister BnF". Hits: Penzi on Sega (Classiques Garnier, La Sainte Union, pp.157-173: Sega came with the Caetani legation), Desenclos and Lasry 2024, Lasry HistoCrypt Colbert 500/33. None mentions this letter. Blog site searches (Cipherbrain, Cryptiana blog, Cipher Mysteries) were not run as site searches; only the combined query above.

## Premise check (BNF-Q13-CS, 8 Oct 2026)
(a) folder: none existed before; BnF record names no decipherment: not found. (b) other solvers' files: Bourdeau none, Aymeloglu not checked: not found/unreached. (c) neighbours: f.148r-149r viewed at 700-900 px, no clear copy: not found. (d) recipient side (Caetani papers, Rome): unreachable.

## While waiting
Next step needing nobody: view canvas 158 native (iiif_lines.py) and see whether the digit groups fit the 1589 table's value set.

## Gate
```
ciphers/fr3613-sega-caetani-1591: blocked (line 1) -- already terminal, nothing to gate
exit 0
```


## Edition search (BNF-SEGA-ED, 8 Oct 2026)
Result: no edition or calendar of Sega's 1590-91 Paris letters, or of Caetani's 1589-90 legation letters, was located; none could be opened. Status stays `blocked` (a search result, not a statement that none exists).
1. Acta Nuntiaturae Gallicae (ANG) volume list: WebSearch x2 returned only catalogue records for vols 2 (Ragazzoni 1583-86), 5 (Scotti), 10-11 (Ranuzzi), 12-13 (Salviati 1572-78), 15 (Spada), 16 (Frangipani 1568-72, 1586-87), 17 (Silingardi 1599-1601). None covers Caetani or Sega; the complete series list was not obtained (fr.wikipedia page 404; EFR/Gregoriana catalogue pages not reached). Numbering is by order of publication, so a gap in the numbers seen is not evidence of absence. Sega's 1586-87 German nunciature (Nuntiaturberichte aus Deutschland) is a different mission, not searched here.
2. OpenAlex (keyed, 3 queries: "Filippo Sega Caetani 1591", "legazione Caetani Francia 1589 lettere", "nunziatura Sega Francia 1591 Acta Nuntiaturae Gallicae"): 18 results, none an edition of these letters (nearest: Jesuit Missio Castrensis 2017; Philip II/Rudolf II 2011). Semantic Scholar, Persée, HAL: not run (box/cap kept small).
3. Google Books API (key, country=US, 3 queries): no volume printing Sega/Caetani 1591 letters; hits were Paruta's Roman legation 1887 (ALL_PAGES, unrelated: Venetian ambassador), Maria de' Medici regency 1962 and Theologischer Jahresbericht (NO_PAGES/unrelated).
4. Internet Archive: advancedsearch title "nuntiaturae gallicae" = 0 items; be-api fts "legazione Caetani Francia" returned only aggregations (not read); "Sega AND Caetani AND Parigi AND 1591" 502 (not retried).
5. Open web: Penzi's chapter (Classiques Garnier, pp.157-173) says Sega's letters are an important source for the League, but the page was 403 to WebFetch, so its bibliography was not read; this is the next lead (which archives/editions Penzi cites). Pastor, Geschichte der Paepste (Gregor XIV): not located in full text, no confirmed print of a 9 Jan 1591 letter. Phrase check "di Parigi, li 9 di gennaro 1591": no work found quoting it.
Not run: Persée, HAL, Semantic Scholar, Goujet/Lettres de Henri IV, Ehses Nuntiaturberichte I,2 text.
Next step needing nobody: obtain Penzi's footnotes (Garnier/OpenEdition/academia route or a Google Books snippet) for the edition he cites; ~$1.
Requests: WebSearch 5, OpenAlex 3, Google Books 3, archive.org 3, classiques-garnier 1 (403), fr.wikipedia 1 (404).

## Gate (BNF-SEGA-ED)
```
fr3613-sega-caetani-1591: blocked (line 1) -- already terminal, nothing to gate
exit 0
```

## Edition and key leads added (BNF-SEGA-POOL, 8 Oct 2026)
DBI "SEGA, Filippo" and "CAETANI, Enrico" Fonti e Bibl. read in full: no edition of Sega's 1591 letters or of Caetani's legation despatches is listed; Manfroni 1893 (Riv. stor. ital. X, archive.org BIBLIOFBK-RIVSTOITA-1893-010-2) grepped whole-number: narrative from Caetani's diary, no 9 Jan 1591 letter, no cipher. ANG complete volume list still not obtained (no Sega or Caetani volume seen). Tomokiyo's Cryptologia article (2017) concerns Farnese/Mayenne letters TO Sega, Jan 1591 (fr.3980), not this letter's cipher. Per Cauare cipher (mantua.htm; Barberini to Sega 1593) is a further untested key candidate beside Meister's Caetani table. Verdict unchanged: blocked. See ciphers/fr3984-sega-memoirs-1593/NOTES.md.

## Remaining gaps (loose-ends pass, 8 Oct 2026)
Read so far: unmeasured; the loose-ends pass of 8 Oct 2026 did not measure the reading
- the bibliography of Penzi's chapter (Classiques Garnier pp.157-173), never read (403); may name an edition of Sega's letters - blocker: not-attempted; noted in the body at NOTES.md:45, never carried as a step (loose-ends 8 Oct 2026); next: read the chapter's footnotes through OpenEdition or a Google Books snippet (country=US) for an edition of the Sega 1591 letters, ~$1

## Escalation (loose-ends pass, 8 Oct 2026)
- [ ] siblings: not assessed in the loose-ends pass of 8 Oct 2026; the next worker on this folder fills it
- [ ] clear-pages: not assessed in the loose-ends pass of 8 Oct 2026; the next worker on this folder fills it
- [ ] known-keys: not assessed in the loose-ends pass of 8 Oct 2026; the next worker on this folder fills it
- [ ] print: read the chapter's footnotes through OpenEdition or a Google Books snippet (country=US) for an edition of the Sega 1591 letters; ~$1; source: loose-ends 8 Oct
- [ ] key-rebuild: not assessed in the loose-ends pass of 8 Oct 2026; the next worker on this folder fills it
- [ ] image-check: not assessed in the loose-ends pass of 8 Oct 2026; the next worker on this folder fills it
- [ ] retry: not assessed in the loose-ends pass of 8 Oct 2026; the next worker on this folder fills it
Verdict: keep going: 1 internal gaps; cheapest next: read the chapter's footnotes through OpenEdition or a Google Books snippet (country=US) for an edition of the Sega 1591 letters, ~$1
