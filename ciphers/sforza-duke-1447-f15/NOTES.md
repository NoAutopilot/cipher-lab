open
Check-solved for this one letter (SFZ-D, 7 Oct 2026): Osio, Documenti diplomatici tratti dagli archivj milanesi vol. III (Milan 1872, IA bub_gb_88IStucIdgAC), the standard printed edition of the Visconti state letters, was searched whole by full-text grep (SFZ-0, same day: Cusago 32 hits, all 1431; no regest of a 23 Jan 1447 letter of the Duke); Mazzatinti, "Inventario delle carte dell'Archivio sforzesco contenute nei codici italiani 1583-1593 della Biblioteca nazionale di Parigi", Archivio storico lombardo X (1883), IA archiviostoricol10cava, read at its entry for cod. 1584 (printed p. 233-234, djvu text lines 10736-10780): "15. [Lettera] del Duca al medesimo (Cusago 23 gennaio). In cifre : membran." -- listed as cipher, with no "Traduzione" entry after it (contrast f.5/f.6 and f.8/f.9, "Traduzione della lettera precedente"); no decipherment of f.15 located.

# BnF italien 1584 f.15: the Duke's cipher slip, Cusago 23 Jan 1447 -- target folder (SFZ-D)

Worker SFZ-D for LANE ST-REBUILD (account 2), brief `.claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md` (Wave 2).
Pool folder: `../sforza-italien1584-1447/NOTES.md` (SFZ-0). Key units: `../sforza-italien1584-1447/duke/`.

## Item

- BnF italien 1584 f.15 (Gallica ark:/12148/btv1b100373864, canvas 17, right page). Filippo Maria Visconti, Duke of Milan,
  to Francesco Sforza, Cusago 23 Jan 1447 (Mazzatinti's attribution and date; the slip is unsigned; later hand on the slip
  "1447, 23 janvier"). One slip, cipher only, 14 lines, about 600-650 signs (SFZ-0's estimate at 1200 px).
- f.17 (canvas 18) is the Duke's clear letter of the same day and place, signed, with two blanks; it is context, not a copy
  (SFZ-0). Used here for names only.

## Check-solved (SFZ-D, 7 Oct 2026; one letter, reusing SFZ-0's pool pass by citation)

- **Osio III** (standard edition of the Visconti/Sforza diplomatic letters): SFZ-0's whole-volume grep, cited above; no f.15.
- **Mazzatinti 1883** (ASL X, IA `archiviostoricol10cava`, `_djvu.txt` downloaded once, 7 Oct 2026, read at cod. 1584):
  f.15 listed "In cifre : membran.", no translation listed after it. The same list gives the Duke's glossed pairs used for
  the key: f.5 (Abiate 10 Jan, in cifre) / f.6 traduzione; f.8 (Abiate 11 Jan, in cifre) / f.9 traduzione; f.23, f.24 (Milano 5
  Feb, in cifre); f.30-31 (two letters, Milano 9 Feb, in cifre); f.36-37 (two letters, Milano 12 Feb, in cifre). SFZ-0 had read
  the f.8 inventory line as "f.8 / f.10": f.9 is the contemporary translation and f.10 a later clear copy (both seen on the
  images, canvases 11 and 12).
- **Google Books API** (key, country=US), two full-text queries on 7 Oct 2026: `"23 gennaio 1447" Cusago` (30 hits: Mazzatinti's
  ASL 1883 inventory itself, Verri's Storia di Milano on a 23 Aug 1447 edict, the Archivio civico inventory 1932 on a 3 Jan 1447
  letter to the podestà; none is this letter), `"Cusaghi" 1447 cifra Sforza` (0 hits).
- **Internet Archive full text** (be-api fts, `"Cusago 23 gennaio"`): 4 Italian items, the Mazzatinti inventory and ASL volumes;
  no edition of the letter.
- **DECODE** (login-free listings in `sources/decode/`, SFZ-0): no italien 1584 record.
- **Solver repositories**: Bourdeau's local snapshots `sources/cyphersolver/2026-10-01..03`, no hit for italien 1584 /
  Sforza / Visconti 1447 (SFZ-0 grep; re-run by SFZ-D: see "Premise check" (b)). Aymeloglu's repository: not re-checked.
- **Cerioni 1970** (La diplomazia sforzesca nella seconda meta del Quattrocento e i suoi cifrari segreti) is a study of the
  Sforza chancery's cipher keys from 1450 on, not an edition of the 1447 Visconti letters; it was not opened in this pass. It
  is relevant as a possible known key (Escalation, known-keys), not as the edition of this letter.

Verdict: `open` -- no decipherment or print of f.15 located in the edition, inventory and full-text searches above.

## Web and blog check

SFZ-0's open-web pass for the pool (seven queries, the Cipher Mysteries "Milanese enciphered letters" post and first 100,000
characters of its comment thread, voynich.ninja thread 5828; Cryptiana blog and Cipherbrain / klausis-krypto-kolumne logged as
not covered by a site search) is reused by citation (`../sforza-italien1584-1447/NOTES.md`, "Web and blog check"). For this
letter, SFZ-D added the two Google Books and one IA full-text query above. No decipherment of f.15 was found on the web, on
Cipher Mysteries, Cryptiana or Cipherbrain as far as those passes reached.

## Premise check

(a) Decipherments the folder already mentions: none for f.15. SFZ-0 records f.17 as a same-day clear companion with blanks
(not a decipherment); Mazzatinti lists no translation for f.15.
(b) Other solvers' working files: `grep -ril "italien 1584\|visconti\|cusago" sources/cyphersolver/` (SFZ-D, 7 Oct 2026): no file.
Aymeloglu's repository not re-checked.
(c) Physical neighbours: f.14 (Pusterla, clear, 21 Jan), f.16 (not listed by Mazzatinti), f.17 (Duke clear, 23 Jan, blanks),
f.18 (instruction to the ambassadors to Aragon, s.d.). None is a copy of f.15's cipher text (SFZ-0, canvases 16-19 at 1200 px).
(d) Recipient's side: Francesco Sforza at Pesaro; the Sforza-side editions are Osio III (read) and the Carteggio degli
oratori (Battioni 2013, from 27 Feb 1447, after this letter's date). No recipient-side decipherment located.

## Intake gate output

`python3 tools/intake_gate_check.py sforza-duke-1447-f15` (7 Oct 2026, 22:02 UTC):

    sforza-duke-1447-f15: open (line 1) -- edition/page or full-text-search citation found within 6 lines
    exit 0

## Key work and result (SFZ-D, 7 Oct 2026): no decode of f.15

Details, numbers and files are in `../sforza-italien1584-1447/duke/NOTES.md`. In short:
- S1: the Amidani key (`../sforza-italien1584-1447/amidani/key.tsv`) on the Duke's glossed slip f.8 scores 0.267 against
  shuffle mean 0.295 / p95 0.334: FAIL, so the Duke's key is not Amidani's at this transcription.
- S2: the Duke's own key from two glossed pairs (f.5/f.7, f.8/f.10), leave-one-letter-out G1 FAILs: mean held-out
  0.441 (run 2, dateline corrected; run 1 0.435) against the 0.60 gate, and f.8 falls below its own shuffle p95 (0.384 vs 0.408).
- S3 (f.15 crop, two passes, decode, controls) was therefore not run, per the brief's stop rule. f.15 has no transcription,
  no decode and no reading; `tools/judge_plaintext.py` was not run (nothing to judge).

## SFZ-SORT (13 Oct 2026, account 4, LANE DEFAULT-A4-2135): owner sign-sorter packet for f.5 + f.8, built, not published
Prior work: `tools/prior_work.py sforza-duke-1447-f15 --item-spec 'shelfmark=BnF italien 1584;folio=5,8;date=1447-01-10;sender=Duke of Milan'
--step-type transcribe --offline` exit 2 (plaintext KNOWN from Tomokiyo/leaf hits that name other volumes or this folder's own f.5/f.7, f.8/f.10
gloss pairs; step LEAD = this job's own claim only). Check 1 by hand: ROOM.md and ciphers/*/sorter* carry no earlier Sforza sorter; ASKS.md
no Sforza row. Output prior-work.tsv.
Built: `sh ciphers/sforza-duke-1447-f15/sorter/build.sh OUTDIR` (sorter/README.md; no network, disk only). 2,325 tiles from 31 straightened
lines (f.5 L01-L15, f.8 L01-L16), 40 starting shape piles (machine clusters on the images alone, `shape-NN`, default blind mode: no key,
value or reader label on the page), 40 focus tiles. Tool preflight (inside sign_sorter.py): PASS -- template, answerable 40/40, right line
0 off-list, shape 13 of 2,325 (0.6%) ink outside 3-60% after a 2 px box margin (191 without it), contact sheet, colour (cvd_check) PASS.
Full preflight, run separately: `--gestures` PASS (228 checks, 11 skipped, iPhone 13, iPhone SE, mouse; 7 min), `--pan` PASS (4 checks). Contact sheet eyed: single signs in most tiles, a few over-split parts (a superscript, half a sign) for the re-cut tool. Not committed: the page, its JSON, tiles, pages/, debug/,
region.jpg (sorter/.gitignore); no image file enters git. Tiles are 1.32x reader A's 1,761 tokens (over-split on purpose; some cursive joins
such as the p-a-r and g-# runs stay joined: the page's re-cut tool and BAD-CUT handle both). Key family not registered in
tools/data/sorter_families.tsv: sign_sorter.py consults it only for --show-values, not for a blind build.
Check after the owner's sort (not on the page): the dateline run (f.8 L15-16, f.5 L14-15), read twice identically by SFZ-DUKE, must come
out sign-for-sign the same under the owner's piles; then sign_sorter_apply.py -> settled labels -> g1_duke.py / g1_duke_anchored.py unchanged.

## Remaining gaps (SFZ-SORT, 13 Oct 2026)
Read so far: 0 signs of f.15 transcribed or read; the Duke key gate G1 failed (0.441 mean held-out, 2 units; anchored 0.422)
- f.15 decode - blocker: waiting-on ASKS row 165 (the owner's blind sort of f.5+f.8, packet built by SFZ-SORT 13 Oct 2026, sorter/README.md); a Duke key that passes G1 is needed first, and the second machine reader is retired for this hand (SFZ-DUKE, 8 Oct 2026); next after the sort: dateline check, sign_sorter_apply.py, then g1_duke.py / g1_duke_anchored.py unchanged, ~$2
- f.17 blanks vs f.15 - blocker: not-attempted; whether f.15's cipher fills f.17's two blanks is unexamined; next: only after a readable key, ~$1

## Escalation (SFZ-SORT, 13 Oct 2026)
- [x] siblings: the Duke's glossed pairs f.5/f.7 and f.8/f.10 used; f.23-24/f.26, f.30-31/f.29, f.36-37/f.35 not yet
- [x] clear-pages: f.17 (same-day clear letter) noted as context; no copy of f.15 exists in the volume per Mazzatinti
- [ ] known-keys: Cerioni 1970 / ASMi Visconti cipher registers not checked
- [ ] print: no print of f.15 located (check-solved above); verifier pass belongs to a later reading
- [x] key-rebuild: attempted, G1 FAIL
- [x] image-check: second machine reader tried and retired (SFZ-DUKE, 8 Oct); owner sign-sorter packet for f.5+f.8 built (SFZ-SORT, 13 Oct), waiting on the owner's sort (ASKS 165)
- [ ] retry: G1 after the sort (anchored learner on reader A FAIL 0.422, 8 Oct), then S3 on f.15
Verdict: keep going: 1 internal gap; cheapest next: known-keys check of Cerioni 1970 / the ASMi Visconti cipher registers for the Duke's 1447 key, ~$1

## Requests (SFZ-D, 7 Oct 2026)

gallica.bnf.fr: 5 overview canvases at 1400 px (c9-c13), 2 info.json, 4 native regions (c9, c10, c11, c12) = 11, one at a
time, >= 2 s apart, no errors. archive.org: 4 (advancedsearch 2, download 1 `_djvu.txt`); be-api.us.archive.org: 1;
googleapis.com/books: 2. No other host.

## SFZ-KEYS (14 Oct 2026, account 4, LANE DEFAULT-A4-0935-14): known-keys check, Cerioni 1970 and the ASMi cipher series
Job: find any printed or digitised key of 1447 (or 1440s Visconti) and, if a table is readable, count sign-stock overlap with f.5/f.8/f.15.
No decode. Sources, one line each (route, query, result), 14 Oct 2026 09:48-09:59 UTC:
- **Internet Archive** (advancedsearch): `creator:(Cerioni)` 21 hits, none the book; `title:(diplomazia sforzesca)` 0;
  `title:(cifrari) AND (milano OR sforza OR visconti)` 0. **Cerioni 1970 is not on IA.** Meister, *Die Geheimschrift im Dienste der
  päpstlichen Kurie* (1906), IA `diegeheimschrift00meis`, `_djvu.txt` downloaded once and grepped (Mailand/Visconti/Sforza/1446/1447):
  p. 22 states that the Visconti cipher of the late 14th century is not known ("daß wir die Geheimschrift der Visconti aus dieser Zeit
  nicht kennen"); no Visconti key of the 1440s printed there. Meister 1902 (*Die Anfänge der modernen diplomatischen Geheimschrift*):
  no IA copy found by title search.
- **Google Books API** (key, country=US): Cerioni 1970 = volume `EncKAQAAIAAJ`, NO_PAGES (snippet search only). Snippets seen: vol. I has a
  biographical index of Sforza agents (e.g. "PUSTERLA Baldassarre ... alla morte di Filippo Maria parteggia..."; "FIGINO Lancellotto ...
  presso lo Sforza già nel 1447"); a passage on "cifrari che sono stati riuniti ... [corrispondenza con] Filippo Maria Visconti, con i
  rappresentanti del conte presso di lui"; key entries of the form "Il cifrario comprende 154 segni, di cui 77 per l'alfabeto ... tav. 41"
  (a 1485 key); a citation of "Manoscritti italiani 1594, f. 147" (BnF italien 1594) and "1594, f. 126t" as key/letter sources. No
  snippet gives a 1446-47 Visconti key table. Google Books answered HTTP 503 on 9 of 16 calls (each retried once after 20 s); stopped
  there per the good-citizen rule. Rivista delle biblioteche e degli archivi 1903/1904 (`7he1XZKjGJcC`, full view) shows a "cifrario"
  snippet next to Filippo Maria Visconti: not opened (a later follow-up, see below).
- **OpenAlex** (key): `Visconti cifrari` 10 hits and `Sforza cipher Visconti Milan fifteenth` 9 hits; nothing on a 1440s Visconti key
  ("Crittografia: tra successi e fallimenti", 2019, doi 10.54103/2531-5994/31106, is a general survey, not opened). Semantic Scholar not
  run (key_livecheck: 429 at 09:48 UTC).
- **HathiTrust bibliographic/HTRC EF**: not reached. No HathiTrust record number for Cerioni 1970 was found (web search, 1 query);
  openlibrary.org (to get an OCLC number) reset the connection twice and was left alone.
- **ASMi online inventory** (archiviodistatomilano.cultura.gov.it, "Carteggio Visconteo-Sforzesco. Potenze sovrane e altre voci", PDF,
  258 pp., 1,811,078 bytes, sha1 a47f1c92bb4f5b847429fe9d0eb285c41abbe54c, fetched once, not committed; URL
  https://archiviodistatomilano.cultura.gov.it/fileadmin/risorse/Patrimonio_archivistico/Fondi_e_Inventari/Visconteo-Sforzesco__1183-1593_/Potenze_sovrane_e_altre_voci-VS_2-1.pdf),
  serie 13 "Cancelleria segreta. Chiavi e cifrari", 1447-1736, pp. 215-217, studied by Cerioni. **scat. 1597** (1447-1486, 194 docs) is
  the relevant unit: it holds "cifra degli oratori di Milano al re d'Aragona, pergamena di mm 270x210, 1447" and doc. n° 78 "Documenti
  diplomatici. Repubblica Ambrosiana. 1447... Cifre". (Compare f.18 of italien 1584: instruction to the Duke's ambassadors to Aragon,
  s.d., SFZ-0.) scat. 1591 carries an undated key with a shirt "Decreti viscontei 1439". Not digitised: the inventory gives no image link,
  and the archive told an outside researcher that no finer inventory of scatt. 1591/1597/1598 exists beyond Cerioni (below).
- **Cipher Mysteries** (ciphermysteries.com/2011/06/28/milanese-enciphered-letters-call-for-help, whole page fetched once, 1,132,639 bytes,
  comments to July 2026; SFZ-0 had read only the first 100,000 characters). Comments of 13 Apr 2023 (N. Pelling and M. Knowles): ASMi's
  1597 set holds **two cipher keys for Filippo Maria Visconti**, "one dates from 1446 to 1447 and I think the other fits within that time
  range"; both look like keys **reconstructed from enciphered letters** ("generated cipher keys"); a key headed "Marcolinus de Barbavarjis"
  is "the same key as the larger Filippo Maria Visconti key"; that key "appears to have been used to communicate with then condottieri
  Francesco Sforza"; and "in the Bibliothèque Nationale de France - Archivio Sforzesco collection ... one can see enciphered letters that
  correspond to the more complex of the two cipher keys". Cerioni vol. I refers to these keys but vol. II (the plates) does not reproduce
  them (Knowles, 13 Apr 2023). Knowles holds ASMi photoreproductions; they are not published on the page. Which BnF letters he matched is
  not stated, so whether italien 1584 f.5/f.8/f.15 are among them is unknown.

Result: a period key that is plausibly the Duke's 1446-47 key (or a sibling: the Barbavara key, the 1447 Aragon orators' key) is
**located at ASMi, Carteggio Visconteo-Sforzesco, Cancelleria segreta, scat. 1597**, but no image or printed table of it is reachable from
here, so the sign-stock overlap count was **not run** (no table to compare). Nothing here is a reading or a key value.
Follow-ups (not run, beyond this brief): (1) a REQUEST.md / ASKS row for an ASMi photoreproduction of scat. 1597's Filippo Maria
Visconti keys, the "Marcolinus de Barbavarjis" key and the 1447 Aragon parchment (owner-side, a copy order); (2) an outreach draft to
the Cipher Mysteries correspondents asking which BnF letters match the larger key (the person's to send, rule 7 gates); (3) open
Rivista delle biblioteche 1904 `7he1XZKjGJcC` (full view) at its "cifrario"/Filippo Maria snippet.
Requests: archive.org 6 (advancedsearch 5, download 1); googleapis.com/books 16 (9 answered 503); api.openalex.org 2;
ciphermysteries.com 2 (one Mod_Security 406, one 200); archiviodistatomilano.cultura.gov.it 1; openlibrary.org 2 (connection reset);
WebSearch 2. Cost not visible to this session.

## Remaining gaps (SFZ-KEYS, 14 Oct 2026)
Read so far: 0 signs of f.15 transcribed or read; the Duke key gate G1 failed (0.441 mean held-out, 2 units; anchored 0.422)
- f.15 decode - blocker: waiting-on ASKS row 165 (the owner's blind sort of f.5+f.8, packet built by SFZ-SORT 13 Oct 2026, sorter/README.md); a Duke key that passes G1 is needed first; next after the sort: dateline check, sign_sorter_apply.py, then g1_duke.py / g1_duke_anchored.py unchanged, ~$2
- period Duke key - blocker: needs-physical-access; the ASMi scat. 1597 Filippo Maria Visconti keys (one 1446-47) and the 1447 Aragon orators' parchment are not digitised and not in Cerioni vol. II (SFZ-KEYS above); a photoreproduction order is owner-side; quote request drafted in REQUEST.md (SFZ-REQ, 14 Oct 2026), waiting-on ASKS row 166 (gate-7 check, then the person sends)
- f.17 blanks vs f.15 - blocker: not-attempted; whether f.15's cipher fills f.17's two blanks is unexamined; next: only after a readable key, ~$1

## Escalation (SFZ-KEYS, 14 Oct 2026)
- [x] siblings: the Duke's glossed pairs f.5/f.7 and f.8/f.10 used; f.23-24/f.26, f.30-31/f.29, f.36-37/f.35 not yet
- [x] clear-pages: f.17 (same-day clear letter) noted as context; no copy of f.15 exists in the volume per Mazzatinti
- [x] known-keys: SFZ-KEYS 14 Oct 2026: Cerioni 1970 snippet-only (Google Books NO_PAGES, not on IA); Duke's 1446-47 keys located at ASMi scat. 1597, not digitised; sign-stock comparison not possible
- [ ] print: no print of f.15 located (check-solved above); verifier pass belongs to a later reading
- [x] key-rebuild: attempted, G1 FAIL
- [x] image-check: second machine reader tried and retired (SFZ-DUKE, 8 Oct); owner sign-sorter packet for f.5+f.8 built (SFZ-SORT, 13 Oct), waiting on the owner's sort (ASKS 165)
- [ ] retry: G1 after the sort (anchored learner on reader A FAIL 0.422, 8 Oct), then S3 on f.15
Verdict: keep going: 1 internal gap; cheapest next: write the ASMi scat. 1597 photoreproduction request (REQUEST.md + ASKS row) for the Filippo Maria Visconti 1446-47 keys, ~$0.5
