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

## OUT-CHECK-SFZ (14 Oct 2026 10:41-10:5x UTC, account 4, LANE DEFAULT-A4-0935-14): gate-7 check of REQUEST.md -- FAIL, held
Separate session from the drafter (SFZ-REQ). The draft's premise, and SFZ-KEYS's "not digitised" line, are wrong: DECODE lists 115 key
records of "Milan State Archives, Carteggio_Sforzesco_scat._n.1597_*" (R5301-R5471; plus 64 of scat. 1591 and 29 of scat. 1598) in
sources/decode/keys-all-2026-09-28-merged.tsv, and Bourdeau thumbnail-scanned all 208 and read the headings of 1597 nos. 2-36
(ciphers/sforza-maino-1446/NOTES.md, "Where it was not found"). SFZ-KEYS's inventory and blog sources stand; what it missed is this
repository's own DECODE cache and the sibling folder. Also missing from the draft: rule 1d holdings line, rule 8 prior_contact line, rule 1b
work paragraph, rule 7 English version, the rule 1 disclosure text. Confirmed: as-mi@cultura.gov.it is the archive's quote address
(Servizio di fotoriproduzione page, HTTP 200, read 14 Oct 2026 10:43 UTC); no other draft to it (rule 1c). Requests:
archiviodistatomilano.cultura.gov.it 1. No CONTRIBUTIONS.md row written (a row is for a draft to be sent; this one is held).

## Remaining gaps (OUT-CHECK-SFZ, 14 Oct 2026)
Read so far: 0 signs of f.15 transcribed or read; the Duke key gate G1 failed (0.441 mean held-out, 2 units; anchored 0.422)
- f.15 decode - blocker: waiting-on ASKS row 165 (the owner's blind sort of f.5+f.8, packet built by SFZ-SORT 13 Oct 2026, sorter/README.md); a Duke key that passes G1 is needed first; next after the sort: dateline check, sign_sorter_apply.py, then g1_duke.py / g1_duke_anchored.py unchanged, ~$2
- period Duke key - blocker: not-attempted; the ASMi scat. 1597 keys are on DECODE (R5301-R5471, 115 records); next: list the scat. 1597 records' headings and thumbnails (login-free) to find the Filippo Maria Visconti 1446-47, Barbavara and Aragon-orators keys, then one browser login for full size and the sign-stock overlap count against f.5/f.8/f.15, ~$2
- f.17 blanks vs f.15 - blocker: not-attempted; whether f.15's cipher fills f.17's two blanks is unexamined; next: only after a readable key, ~$1

## Escalation (OUT-CHECK-SFZ, 14 Oct 2026)
- [x] siblings: the Duke's glossed pairs f.5/f.7 and f.8/f.10 used; f.23-24/f.26, f.30-31/f.29, f.36-37/f.35 not yet
- [x] clear-pages: f.17 (same-day clear letter) noted as context; no copy of f.15 exists in the volume per Mazzatinti
- [ ] known-keys: Cerioni 1970 snippet-only (SFZ-KEYS); the ASMi scat. 1597 keys are on DECODE and not yet opened (OUT-CHECK-SFZ); the ASMi quote request is held at gate 7 until DECODE is read
- [ ] print: no print of f.15 located (check-solved above); verifier pass belongs to a later reading
- [x] key-rebuild: attempted, G1 FAIL
- [x] image-check: second machine reader tried and retired (SFZ-DUKE, 8 Oct); owner sign-sorter packet for f.5+f.8 built (SFZ-SORT, 13 Oct), waiting on the owner's sort (ASKS 165)
- [ ] retry: G1 after the sort (anchored learner on reader A FAIL 0.422, 8 Oct), then S3 on f.15
Verdict: keep going: 2 internal gaps; cheapest next: read the DECODE scat. 1597 key records (R5301-R5471) for the Filippo Maria Visconti 1446-47 keys, ~$2

## SFZ-DEC (14 Oct 2026 11:09-11:3x UTC, account 4, LANE DEFAULT-A4-0935-14): DECODE scat. 1597 key records, nos. 1-11 and 78 opened
Job: find the Filippo Maria Visconti 1446-47, Barbavara and Aragon-orators keys among the ASMi Carteggio Sforzesco scat. 1597 records on
DECODE, and compare their signs with the Duke's slips. Credit: D. Bourdeau (dbourdeau/cyphersolver, it1583/) thumbnail-scanned all 208
ASMi records of scatt. 1591/1597/1598 and read the headings of 1597 nos. 2-36 for the Maino/Amidani pair (none headed Maino or Amidani;
no. 14 "Angelus cum cifra Vincentij"); his heading list is not in this repository, so the records were reopened here.
- **Login-free filter (8 requests).** DECODE's RecordsList accepts `x_c_holder=1597&z_c_holder=LIKE` (115 key records, as the cache).
  Every scat. 1597 record carries only "1450 - 1555", no sender, receiver or note: `x_sender=Visconti`, `x_receiver=Visconti`,
  `x_additional_information=Visconti` and `x_start_year<1450` all return "No records found". The catalogue cannot pick the 1440s
  keys out; only the sheet headings can.
- **One browser login** (tools/decode_browser_login.js with `--listen`), 26 requests in the session. Full-size files are PDFs named
  `IMG_R<rec>_I<img>_P[n].pdf`; image ids are not predictable from the record id (a guessed id returned the 5,244-byte forbidden
  placeholder), so each record needs its RecordsView page first. Twelve records opened; table `decode_1597/records.tsv`, files and
  sha1s `decode_1597/manifest.json` (PDFs not committed: publishing needs the holder's permission).
- **What they are.** No. 1 is the box cover. Nos. 2-7 and 9-11 and 78 are later fair copies (one hand, pencil numbers 204-217 and 44),
  one sheet per correspondent, headed by the correspondent: Angelus de Valeto / Baptista (2), Antonius M. (3), Lanzalotus de Figino (4),
  Petrus de Monteferrato (5), Antonius (6), Raphael de Pugnellis (7), Cosimo de Medici (9), Robertus de Malatestis a Sagramoro de
  Arimino 1468 (10), Stephanus Taberna (11), Anonimo (78). No. 8 is an unheaded period sheet in brown ink with a syllable grid and a
  nomenclator naming "Conte Iacomo" and "Sig. Sigismondo" (so 1450s-60s, not the Duke). **None of the twelve is headed Filippo Maria
  Visconti, Duca, Barbavara or the Aragon orators.** The DECODE numbering is not the ASMi inventory's: DECODE no. 78 is "Anonimo", not
  the inventory's doc. 78 "Repubblica Ambrosiana 1447 ... Cifre".
- **Sign comparison (one reader, by eye, grade M).** A stock-overlap count with a shuffled control was not run: shuffling the Duke's text
  cannot change which shapes it uses, so that control could not differ from the target (rule 3, the bCAS/AX-5799 shape). Run instead:
  the seven sign-letter pairs graded C from the glosses (O=a, Y=o, N8=d, N2=h, N11=r, ce=r, cu=n; ../sforza-italien1584-1447/duke/key.tsv)
  checked against each key. The Duke's own key would agree on most of the seven whose shape it carries; an unrelated key agrees by chance
  about 1 in 20 per shape. Result: 0 of 7 on ten keys; 1 of 7 on Pugnellis (7) and Malatesta 1468 (10), both the o-with-tail = a
  pair, which looks like a common chancery convention rather than a shared key. The generic shapes (3, 8, x, ÷, ħ, ∂, 9, +) recur in
  almost every sheet, so shape presence alone does not single out any key.
- **Result:** the Duke's 1446-47 key is not among DECODE scat. 1597 nos. 1-11 and 78. Not opened: nos. 12-114 (except 14, Bourdeau's)
  and 169-171; DECODE holds 115 of the inventory's 194 documents, so the Visconti keys may also be among the 79 not on DECODE.
- Requests: de-crypt.org 37 (8 login-free RecordsSearch/RecordsList; 3 for the login and RecordsView/5301; 26 in the session: 11
  RecordsView pages, 15 file gets including the one forbidden guess). Cost not visible to this session.

## Remaining gaps (SFZ-DEC, 14 Oct 2026)
Read so far: 0 signs of f.15 transcribed or read; the Duke key gate G1 failed (0.441 mean held-out, 2 units; anchored 0.422)
- f.15 decode - blocker: waiting-on ASKS row 165 (the owner's blind sort of f.5+f.8, packet built by SFZ-SORT 13 Oct 2026, sorter/README.md); a Duke key that passes G1 is needed first; next after the sort: dateline check, sign_sorter_apply.py, then g1_duke.py / g1_duke_anchored.py unchanged, ~$2
- period Duke key - blocker: not-attempted; DECODE scat. 1597 nos. 1-11 and 78 opened (SFZ-DEC), none Visconti; next: open nos. 12-114 (skip 14) and 169-171 by heading, about 2 requests per record in one login (RecordsView, then the PDF), ~45 per session, so three sessions, ~$2 each; if none is the Duke's, the ASMi request (REQUEST.md, held at gate 7) is redrafted for the documents DECODE lacks
- f.17 blanks vs f.15 - blocker: not-attempted; whether f.15's cipher fills f.17's two blanks is unexamined; next: only after a readable key, ~$1

## Escalation (SFZ-DEC, 14 Oct 2026)
- [x] siblings: the Duke's glossed pairs f.5/f.7 and f.8/f.10 used; f.23-24/f.26, f.30-31/f.29, f.36-37/f.35 not yet
- [x] clear-pages: f.17 (same-day clear letter) noted as context; no copy of f.15 exists in the volume per Mazzatinti
- [ ] known-keys: Cerioni 1970 snippet-only (SFZ-KEYS); DECODE scat. 1597 nos. 1-11 and 78 opened, none Visconti (SFZ-DEC); nos. 12-114 and 169-171 not opened
- [ ] print: no print of f.15 located (check-solved above); verifier pass belongs to a later reading
- [x] key-rebuild: attempted, G1 FAIL
- [x] image-check: second machine reader tried and retired (SFZ-DUKE, 8 Oct); owner sign-sorter packet for f.5+f.8 built (SFZ-SORT, 13 Oct), waiting on the owner's sort (ASKS 165)
- [ ] retry: G1 after the sort (anchored learner on reader A FAIL 0.422, 8 Oct), then S3 on f.15
Verdict: keep going: 2 internal gaps; cheapest next: open DECODE scat. 1597 nos. 12-40 by heading (one login, ~45 requests), ~$2

## SFZ-DEC2 (14 Oct 2026 18:51-19:0x UTC, account 1, LANE DEFAULT-A1-1840-14): DECODE scat. 1597 nos. 12-35 by heading -- two sheets headed "Filippo Maria Duca di Milano"
Job: open DECODE scat. 1597 nos. 12-40 by heading (SFZ-DEC's next band), one browser login, <= 50 requests; for each record heading,
date, correspondent and whether it is a Visconti / Barbavara / Aragon or 1446-47 key; no decode.
- **Prior work.** `tools/prior_work.py sforza-duke-1447-f15 --item-spec 'it1584 f.15' --step-type lookup --offline`: exit 4, the one LEAD is
  this job's own ROOM claim; plaintext UNCHECKED (generic: no unit ids). By hand: check 1 (own work) SFZ-DEC opened nos. 1-11 and 78 only;
  check 3 (solvers) Bourdeau read the headings of 1597 nos. 2-36 for Maino/Amidani (../sforza-maino-1446/NOTES.md) but his heading list is
  not in this repository (sources/cyphersolver has no scat. 1597 file, grep 14 Oct 2026); Cipher Mysteries (SFZ-KEYS) already reports two
  Filippo Maria Visconti keys in the 1597 set (Pelling and Knowles, 13 Apr 2023). Check 4 (editions): not applicable (a key lookup).
- **Route.** A login-free RecordsList page carries no image filenames, nor does the logged-in one (checked once each), so each record
  needs RecordsView then its PDF. One browser login (tools/decode_browser_login.js 5312 --listen); requests: 1 login-free list,
  the login run (login + RecordsView/5312), 46 listen requests (1 logged-in list page, 22 RecordsView, 23 PDFs); all 200, none the
  forbidden placeholder. That reached the 50-request limit at **no. 35**; nos. 36-40 not opened. All PDFs are one page.
  Table: `decode_1597/records.tsv` (rows 5312-5335); files and sha1s: `decode_1597/manifest.json` (PDFs not committed).
- **What nos. 12-35 are** (heading as read, one reader): 12 Io. Stephanus Castilioneus a Bartholomeo Chalco; 13 Carazolus et Salicetus /
  Card. Ascanio Maria Sforza Visconti; 15 Antonio da Pistoia 1458; 16 Andreas Biragus (one name, Francesco Piccinino); **17 period
  parchment "Zifra Oratorum Illustris et Excelse Comunitatis Mediolani ... ad Serenissimum dominum Aragonum Regem", dated MCCCCXLVII**
  (the inventory's 1447 Aragon-orators parchment: the Milanese Comunità's, i.e. after the Duke's death, not his); 18 Nicodemus (pencil:
  1451); 19 Cum Nicodemo Romae; 20 Cum ... duce Calabrie; 21 Duca di Milano con Bartolomeo da Recanati, Dec. 1458; 22 Ducalis cum Branda
  Castiliono Neapoli; **23 "Filippo Maria Duca di Milano"** (homophonic alphabet, bigram table ab..vo, 12 words, nomenclator: Duca di
  Milano, Roma, Duca di Ferrara, Conte d'Urbino, Papa, Veneziani, Re de Ragona, S. Malatesti); **24 "Filipo Maria Duca di Milano"**
  (smaller: alphabet, syllables, words: Dux Mediolani, Papa, Re de Ragona, Ambassadore); 25 1460, Naples; 26 unheaded (same alphabet as
  27); 27 Re Ferdinando di Napoli con Bartolomeo da Recanati; 28-29 Ottone del Carretto (29 "a Roma"); 30 Antonio da Trezzo 1458-;
  31 Re Ferdinando d'Aragona con Francesco Sforza, Feb. 1459-60; 32 Bartolomeo da Recanati 1458; 33 a modern "Traduzione" of the Carretto
  key; 34 unheaded period sheet (Legatus, Consistorium: Rome); 35 Sigismondo Malatesta. Nos. 23 and 24 are later fair copies (pencil 178,
  177), in the same copyist's hand as nos. 2-11. No sheet headed Barbavara in 12-35.
- **Sign check (SFZ-DEC's method, one reader, by eye, grade M, NOT blind: the reader knew the seven pairs while looking).** The seven
  sign-letter pairs graded C from the Duke's glosses (O=a, Y=o, N8=d, N2=h, N11=r, ce=r, cu=n; ../sforza-italien1584-1447/duke/key.tsv,
  shapes per duke_labels.md) against each key's columns:
  **no. 23: 5 of 7** -- the o with a long right tail stands under a; a y-shape under o; a "<o"-like curl under d; the double-barred
  vertical (‡) under h; a u/ʋ shape under n; r's column (L, ∂) carries neither N11 nor the e-shape. No. 23's o column also has a ß-like
  sign, the Duke's K (=o, grade M). **No. 24: 0-1 of 7** (the o-tail stands under b). Every other sheet in 12-35, and the 1447 orators'
  parchment (no. 17), 0 of 7; SFZ-DEC's ten keys 0-1 of 7. A stock-overlap count with a shuffled control was again not run (shuffling the
  Duke's text cannot change which shapes it uses: rule 3, a non-test); the comparison set is the other keys of the same box, all 0-1 of 7.
- **Result:** DECODE scat. 1597 no. 23 (R5323), a later fair copy headed "Filippo Maria Duca di Milano", is a candidate for the key of the
  Duke's slips f.5/f.8 (and so f.15): 5 of the 7 C pairs agree by eye against at most 1 of 7 on 31 other keys of the box. This is a lead,
  graded M, from an unblinded single reader; nothing here is a reading. It matches Pelling and Knowles's report (Cipher Mysteries, 13 Apr
  2023) of two Filippo Maria Visconti keys in the 1597 set, the larger corresponding to enciphered letters at the BnF.
- **ASMi request (REQUEST.md, held at gate 7):** no longer needed to *locate* the Duke's keys -- they are on DECODE (R5323, R5324) and
  the 1447 Aragon parchment is R5317. It stays relevant only for permission to reproduce the sheets (DECODE files are not committed) or for
  the 79 documents DECODE lacks; the redraft is the lane's call.
- Requests: de-crypt.org about 50 (see Route). Cost not visible to this session.

## Remaining gaps (SFZ-DEC2, 14 Oct 2026)
Read so far: 0 signs of f.15 transcribed or read; the Duke key gate G1 failed (0.441 mean held-out, 2 units; anchored 0.422); a candidate period key located (DECODE scat. 1597 no. 23, R5323, 5/7 C pairs by eye, grade M)
- R5323 key check - blocker: not-attempted; the 5/7 agreement is one unblinded reader; next: a blind second reader (separate session, not told the Duke's values) transcribes R5323's alphabet columns into key_r5323.tsv in duke_labels.md labels, then the C-pair agreement is scored by script against key.tsv with the other 1597 keys as the null, ~$2
- f.15 decode - blocker: not-attempted; the owner's blind sort (ASKS row 165) remains the transcription route for f.15 itself; next: if R5323 passes the blind check, apply it to f.5/f.8 against their glosses (decode_key.py, G1 gate unchanged) before f.15, ~$2
- f.17 blanks vs f.15 - blocker: not-attempted; whether f.15's cipher fills f.17's two blanks is unexamined; next: only after a readable key, ~$1

## Escalation (SFZ-DEC2, 14 Oct 2026)
- [x] siblings: the Duke's glossed pairs f.5/f.7 and f.8/f.10 used; f.23-24/f.26, f.30-31/f.29, f.36-37/f.35 not yet
- [x] clear-pages: f.17 (same-day clear letter) noted as context; no copy of f.15 exists in the volume per Mazzatinti
- [x] known-keys: DECODE scat. 1597 nos. 1-35 and 78 opened (SFZ-DEC, SFZ-DEC2); nos. 23 and 24 headed "Filippo Maria Duca di Milano", no. 23 agrees 5/7 with the Duke's C pairs by eye (grade M); no. 17 is the 1447 Milan orators-to-Aragon parchment; nos. 36-114 and 169-171 not opened (not needed for the Duke unless R5323 fails its blind check)
- [ ] print: no print of f.15 located (check-solved above); verifier pass belongs to a later reading
- [x] key-rebuild: attempted, G1 FAIL
- [x] image-check: second machine reader tried and retired (SFZ-DUKE, 8 Oct); owner sign-sorter packet for f.5+f.8 built (SFZ-SORT, 13 Oct), waiting on the owner's sort (ASKS 165)
- [ ] retry: blind check of R5323, then the period key against the f.5/f.8 glosses, then S3 on f.15
Verdict: keep going: 3 internal gaps; cheapest next: blind transcription of DECODE R5323's alphabet columns and a scripted C-pair score against the 1597 null, ~$2

## SFZ-R5323 (14 Oct 2026 19:10-19:3x UTC by date -u, account 1, LANE DEFAULT-A1-1840-14): blind test of DECODE R5323 -- registered gate FAIL (3 of 7, threshold 4), above every control
Job: test SFZ-DEC2's lead (R5323 "Filippo Maria Duca di Milano", 5/7 C pairs by an unblinded eye) with readers who never saw the pairs.
- **Prior work.** Check 1 (own work): SFZ-DEC2 above is the only look at R5323; no blind pass existed. Checks 2-4 as SFZ-DEC2 (same day,
  same records; a key-sheet test, no edition). Pelling and Knowles (Cipher Mysteries, 13 Apr 2023) report two Filippo Maria keys in the
  1597 set; no transcription of R5323 by them located in this repository's sources.
- **Fetch.** One browser login (tools/decode_browser_login.js 5323 --fetch, 12 PDFs by the filenames in decode_1597/manifest.json): 14
  de-crypt.org requests, all 200, sha1s equal to the manifest. Nothing committed but text; images re-derive with `r5323/regen.sh`.
- **PREREG** `PREREG-SFZ-R5323.md`, pushed 9c81f442b before any reader ran. Statistic S = how many of the 7 C pairs (O=a, Y=o, N8=d,
  N2=h, N11=r, ce=r, cu=n) a blind reader lists in that letter's column; R5323 scored on cells both passes agree on.
- **Readers.** 13 Sonnet subagent calls, each given only duke_labels.md's shape table (r5323/labels.md; no values, no f.5/f.8, no
  mention of the Duke): R5323 passes A and B on two 300 dpi strip crops of the alphabet block; one pass each on the top half of R5324 and
  ten other scat. 1597 keys (5302 5304 5305 5306 5309 5310 5311 5312 5313 5315). Reader TSVs in r5323/; no reconciliation call was run
  (the gate scores agreed cells only, and on FAIL no key is built).
- **Result** (`python3 score_r5323.py` in r5323/, output r5323/score.out):

  | sheet | S (of 7) | pairs |
  |---|---|---|
  | R5323 pass A | 3 | O=a, Y=o, N8=d |
  | R5323 pass B | 4 | O=a, Y=o, N8=d, N2=h |
  | **R5323 agreed** | **3** | O=a, Y=o, N8=d |
  | R5324 (other "Filipo Maria" sheet) | 0 | |
  | 10 other 1597 keys | 0,0,0,0,1,0,1,0,0,0 | 5306 Y=o; 5310 O=a |
  | shuffled-value null on R5323's agreed columns | p = 0.0006 (10,000 perms, seed 5323) | |

  Gate (S_agreed >= 4 AND > max control AND p <= 0.01): **FAIL** on the first clause only (3 < 4); the second (3 > 1) and third
  (p 0.0006) pass. Logged as registered; the gate is not re-tuned.
- **What the misses are (post hoc, not scored).** N2=h: pass B read h's ‡ as N2, pass A as # (the two double-barred labels). cu=n:
  both readers wrote n's first sign as "X:v" -- the label table packs `ca cr ce cu cm ci` into one row, so a u-shape had no
  separable label to pick; a reader-instrument gap, not evidence either way. N11 and ce under r: neither reader listed them (r column
  read N4 d by both), as SFZ-DEC2's eye also found. So the blind readers reproduce 3 of SFZ-DEC2's 5 and disagree on one.
- **Grade.** R5323 stays a lead (M): blind readers agree on 3 of the 7 C pairs against at most 1 on eleven other keys of the same box,
  but the pre-registered threshold was not met, so no key_r5323.tsv, no decode of f.5/f.8/f.15, no H grade. Nothing here is a reading.
- Requests: de-crypt.org 14. Sonnet calls 13. Cost not visible to this session.

## Remaining gaps (SFZ-R5323, 14 Oct 2026)
Read so far: 0 signs of f.15 transcribed or read; the Duke key gate G1 failed (0.441 mean held-out, 2 units; anchored 0.422); candidate period key DECODE R5323: blind readers agree on 3 of 7 C pairs (gate needed 4; controls max 1, shuffled p 0.0006), grade M
- R5323 key check - blocker: not-attempted; the label instrument could not express cu (u-shape) or settle #/N2; next: split the cursive-letter row of the label table into one row per label (ca, cr, ce, cu, cm, ci) and add an exemplar crop per C-pair label from f.5/f.8 without values, then a fresh PREREG and two blind passes on the same crops (rule 3 third-attempt clause: this would be attempt 2 with a changed instrument), ~$1.5
- f.15 decode - blocker: not-attempted; the owner's blind sort (ASKS row 165) remains the transcription route for f.15 itself; next: only if R5323 passes a blind check, apply it to f.5/f.8 against their glosses (decode_key.py, G1 unchanged) before f.15, ~$2
- f.17 blanks vs f.15 - blocker: not-attempted; whether f.15's cipher fills f.17's two blanks is unexamined; next: only after a readable key, ~$1

## Escalation (SFZ-R5323, 14 Oct 2026)
- [x] siblings: the Duke's glossed pairs f.5/f.7 and f.8/f.10 used; f.23-24/f.26, f.30-31/f.29, f.36-37/f.35 not yet
- [x] clear-pages: f.17 (same-day clear letter) noted as context; no copy of f.15 exists in the volume per Mazzatinti
- [x] known-keys: DECODE scat. 1597 nos. 1-35 and 78 opened; R5323 blind-tested (SFZ-R5323): 3/7 agreed vs controls <= 1, gate FAIL at threshold 4
- [ ] print: no print of f.15 located (check-solved above); verifier pass belongs to a later reading
- [x] key-rebuild: attempted, G1 FAIL
- [x] image-check: second machine reader tried and retired (SFZ-DUKE, 8 Oct); owner sign-sorter packet for f.5+f.8 built (SFZ-SORT, 13 Oct), waiting on the owner's sort (ASKS 165)
- [ ] retry: R5323 blind check with a per-label table and exemplar crops (attempt 2, changed instrument), then the period key against the f.5/f.8 glosses, then S3 on f.15
Verdict: keep going: 3 internal gaps; cheapest next: R5323 blind check with a split label table and value-free exemplar crops, fresh PREREG, ~$1.5

## SFZ-R5323B (14 Oct 2026 21:48-22:0x UTC by date -u, account 4, LANE DEFAULT-A4-2135-14): R5323 blind re-test with a split label table and value-free exemplars -- registered gate PASS (4 of 7, threshold 4), every control <= 1
Job: SFZ-R5323's named next step, attempt 2 of the blind eye-pairing method with a changed instrument (rule 3 third-attempt clause).
- **Prior work.** Check 1 (own work): SFZ-DEC2 (unblinded eye, 5/7) and SFZ-R5323 (blind, 3/7, FAIL at threshold 4) above are the only
  looks at R5323; nothing else in the repository transcribes it (grep of ciphers/ and sources/ for R5323/5323, 14 Oct 2026). Checks 2-4 as
  SFZ-R5323 (same records; a key-sheet test, no edition). Pelling and Knowles (Cipher Mysteries, 13 Apr 2023) report two Filippo Maria
  keys in the 1597 set; no transcription of R5323 by them in sources/.
- **Fetch.** One browser login (`r5323/regen.sh`, unchanged): 14 de-crypt.org requests, all 12 PDF sha1s equal to decode_1597/manifest.json.
  Nothing image-shaped committed; reader packets re-derive with `r5323b/regen.sh <r5323 regen dir> <out dir>`.
- **PREREG** `PREREG-SFZ-R5323B.md`, pushed e6acd17ff before any reader ran (same 7 C pairs, same 11 control sheets, same gate).
- **Instrument changes.** (1) Split label table, 40 labels in two groups of 20 (`r5323b/labels_G1.md`, `labels_G2.md`; ca/cr/ce/cu/cm/ci
  one row each; # with N2, and O/co/Y/N8/cu/ce in the same group). (2) Value-free exemplar crops: 24 labels, one crop each from the f.8
  line crops on disk (`r5323b/exemplars.json`, `exemplar_sheet.py`), 7 of them C-pair labels, 17 decoys, label text only. (3) One label
  group per call. (4) The 11 controls read in the same calls as R5323, under neutral names sheet_01..12 (`r5323b/sheet_map.tsv`, seeded
  shuffle; R5323 = sheet_03), so controls also got two passes. 8 Sonnet calls (2 passes x 2 groups x 2 batches of 6 sheets).
- **Result** (`python3 r5323b/score_r5323b.py r5323b`, output `r5323b/score.out`; reader TSVs `r5323b/pass*_G*_b*.tsv`):

  | sheet | S_A | S_B | S_agreed (of 7) | pairs agreed |
  |---|---|---|---|---|
  | **R5323** | 4 | 4 | **4** | O=a, N8=d, N2=h, cu=n |
  | R5324 (other "Filipo Maria" sheet) | 0 | 1 | 0 | |
  | R5310 | 1 | 1 | 1 | O=a |
  | R5305 | 0 | 1 | 0 | |
  | 8 other 1597 keys (5302 5304 5306 5309 5311 5312 5313 5315) | 0 | 0 | 0 | |
  | shuffled-value null on R5323's agreed columns | | | p < 0.0001 (0 of 10,000, seed 5323) | |

  Gate (S_agreed >= 4 AND > max control 1 AND p <= 0.01): **PASS**, at the threshold exactly. Loose line (A/B? tokens) identical.
- **What changed and what did not (post hoc, not scored).** The two named gaps of SFZ-R5323 both moved: cu=n is now listed by both
  readers (the split row made u expressible), and both put ‡ under h as N2 (and also # -- both labels sit in G2). Y=o, agreed in SFZ-R5323,
  dropped out: pass A wrote Y under n, pass B wrote cp under o. N11 and ce under r: neither reader (r read `N4 d` by both, as in
  SFZ-R5323 and SFZ-DEC2's eye). So the pairs agreed by blind readers across the two attempts are O, Y, N8, N2, cu (5 of 7, the same
  five as SFZ-DEC2's unblinded eye), but no single attempt agreed on more than 4.
- **Caveats.** Every reader call took 24-38 s for 6 sheets and described its own read as low-confidence (small, dense sheets; column
  alignment approximate). The PASS is at the threshold with no margin; one lost pair would have failed it. It is a PASS of the
  identification gate only: no key_r5323.tsv was built, nothing was decoded, and nothing here is a reading.
- **Grade.** R5323 moves from an M lead to a candidate period key supported by a passed registered blind gate (matched controls max 1);
  the identification is cryptanalytic (S-level), not H: the decisive test is the key against the Duke's own glosses on f.5/f.8.
- Requests: de-crypt.org 14. Sonnet calls 8. Cost not visible to this session.

## Remaining gaps (SFZ-R5323B, 14 Oct 2026)
Read so far: 0 signs of f.15 transcribed or read; the Duke key gate G1 failed (0.441 mean held-out, 2 units; anchored 0.422); candidate period key DECODE R5323: blind gate PASS (SFZ-R5323B, 4 of 7 C pairs agreed, controls max 1, p < 0.0001), no key built yet
- R5323 key build - blocker: not-attempted; only the 7 C-pair cells were scored, no full transcription of R5323 exists; next: two blind passes transcribing R5323's whole alphabet block (all columns, both label groups, the r5323b instrument) into key_r5323.tsv, agreed cells only, then decode_key.py on f.5/f.8 and score against their glosses with the G1 gate unchanged (a key that fails the glosses voids the identification), ~$2
- f.15 decode - blocker: not-attempted; the owner's blind sort (ASKS row 165) remains the transcription route for f.15 itself; next: only after R5323 passes the f.5/f.8 gloss gate, apply it to f.15, ~$2
- f.17 blanks vs f.15 - blocker: not-attempted; whether f.15's cipher fills f.17's two blanks is unexamined; next: only after a readable key, ~$1

## Escalation (SFZ-R5323B, 14 Oct 2026)
- [x] siblings: the Duke's glossed pairs f.5/f.7 and f.8/f.10 used; f.23-24/f.26, f.30-31/f.29, f.36-37/f.35 not yet
- [x] clear-pages: f.17 (same-day clear letter) noted as context; no copy of f.15 exists in the volume per Mazzatinti
- [x] known-keys: DECODE scat. 1597 nos. 1-35 and 78 opened; R5323 blind gate FAIL at 3/7 (SFZ-R5323), then PASS at 4/7 with the split-label instrument (SFZ-R5323B), controls max 1
- [ ] print: no print of f.15 located (check-solved above); verifier pass belongs to a later reading
- [x] key-rebuild: attempted, G1 FAIL
- [x] image-check: second machine reader tried and retired (SFZ-DUKE, 8 Oct); owner sign-sorter packet for f.5+f.8 built (SFZ-SORT, 13 Oct), waiting on the owner's sort (ASKS 165)
- [ ] retry: build key_r5323.tsv from two blind passes and test it against the f.5/f.8 glosses (G1 unchanged), then S3 on f.15
Verdict: keep going: 3 internal gaps; cheapest next: key_r5323.tsv from two blind passes and decode_key.py on f.5/f.8 against their glosses, ~$2

## SFZ-DEC3 (14 Oct 2026 21:48-22:0x UTC by date -u, account 4, LANE DEFAULT-A4-2135-14): DECODE scat. 1597 nos. 36-77 by heading -- one 1440s sheet ("Cum duce Mediolani", no. 50), not the slips' key
Job: LANE DEFAULT-A1-1840-14 next item 1, nos. 36-114 by heading, SFZ-DEC/SFZ-DEC2's method; for any 1446-47 key a sign-stock overlap
with the Duke's inventory against a control; no decode. Credit as SFZ-DEC (Bourdeau's thumbnail scan of the 1597 records; Pelling and
Knowles, Cipher Mysteries 13 Apr 2023, on the Filippo Maria keys).
- **Route.** Waited for SFZ-R5323B's de-crypt.org release (21:50), then one browser login (`tools/decode_browser_login.js 5336 --listen`,
  2.5 s apart). Record N = DECODE 5300+N, confirmed on RecordsView/5336 ("scat. n.1597_36"). File ids run nearly in sequence, so each
  next PDF was first requested by guess (`IMG_R<N>_I<previous+1>_P.pdf`; a miss returns a small non-PDF placeholder) and RecordsView was
  opened only on a miss: 60 requests (login run 2; 58 in the listener: 8 RecordsView pages, 50 file gets of which 42 PDFs and 8
  placeholders) reached **no. 77**; nos. 79-114 and 169-171 not opened (78 was opened by SFZ-DEC). Nos. 52, 54 and 64 have a second
  page (P2) not fetched. Table: `decode_1597/records.tsv` (rows 5336-5377); files and sha1s `decode_1597/manifest.json` (PDFs not
  committed; re-fetch by filename as SFZ-DEC's note says). Headings read by one reader from 110 dpi renders of the top of each page.
- **What nos. 36-77 are.** Dated or datable headings: 38 Conradino de Georgiis to Savoy, 27 Oct 1467; 56 Jacobus de Calcaterris with the
  Duke, June 1465(?); 58 **Scipione Barbavara, 22 Sept 1485** (the only Barbavara sheet so far; 57 is the same key); 62 22 Apr 1462;
  69 the provost of S. Antonio of Cremona and Branda da Castiglione, 26 Aug 1483; 72 Gio. Angelo da Firenze, 27 May 1484. Sforza-era
  correspondents without a date: 37 and 41 Angelo Geraldini of Amelia; 55 Agostino Rossi(?); 59, 60, 63 Francesco Casati; 64 "Zifra
  Ill.mi d. ducis cum Petro de Pusterla" (undated; which duke not stated); 66, 67 Filippo Sagramoro; 68 Cristoforo Sagramoro(?); 70
  Count Girolamo; 71 a protonotary; 73 a Lodovico, Marquis (nomenclator Papa, Rex neapolitanus); 74 and 77 Fieschi; 75 the bishop of
  Alessandria; 76 Branda da Castiglione. No. 54 is a later folder cover, "Ciffre di diverse sorti di diversi tempi". Unheaded at the
  top: 39, 40, 42-49, 51-53, 61, 65 (not attributable by heading). **No sheet headed Filippo Maria, Visconti or the Aragon orators.**
- **No. 50 (R5350), "Cum duce Mediolani".** Period hand, alphabet of bar-and-stroke signs, "Nichil importantes", a syllable table and a
  nomenclator: Papa, Imperator, Rex Aragonum, Rex Renatus, Dux Sabaudie, Marchio Mantue, Comes Urbini, Bononienses, Senenses,
  Lucenses, Roma, Neapolis, **Nicolaus Picininus**, Franciscus Picininus, Talianus Furlanus. Niccolò Piccinino died in October 1444, so the
  sheet is most likely before then: a correspondent's key with Filippo Maria Visconti in the early 1440s (inferred from the names, grade
  I; the date is not on the sheet). It is not the key of the Duke's slips:
  - Sign-stock overlap (`dec3/overlap_dec3.py`, output `dec3/overlap_dec3.out`). Statistic: the share of the Duke's 1,741 f.5+f.8 tokens
    whose duke_labels.md label is in the key's stock. R5350's stock (`dec3/stock_r5350.tsv`, one reader, by eye, NOT blind, grade M) has
    only 6 labelled shapes (#, D, N12, N13, N2, t; its other signs have no duke_labels label). **Coverage 0.157**; random 6-label stocks
    from the same 40-label table (10,000, seed 5350): mean 0.149, p95 0.266, P(>= 0.157) = 0.40. The control can differ from the target
    because it changes which labels are in the stock, which is what coverage counts (SFZ-DEC's shuffled-text control could not). For
    comparison, the 12 sheets read blind by SFZ-R5323 cover 0.36-0.64 with stocks of 13-25 labels (R5323 0.62-0.64), but they are larger
    stocks and not a size-matched null.
  - C pairs by eye: the a column holds wavy and barred signs, no o with a tail; o holds a ⊥-type sign, no y: 0 of 7.
- **Unheaded sheets, C-pair glance.** Only 48, 52 and 53 were looked at closer (a and o columns, 170 dpi, unblinded): at most 1 of 7
  each. The other twelve unheaded sheets were not C-pair checked.
- **ASMi REQUEST.md.** Still not needed to find the Duke's key (R5323 passed its blind gate, SFZ-R5323B); it stays relevant only for
  reproduction permission or for the inventory documents DECODE lacks, as SFZ-DEC2 said.
- Cross-target note (one line, not acted on): no. 64 is the (a) Duke's key with Pietro Pusterla; Pusterla's own 1447 slip
  (../sforza-pusterla-1447-f13) went to Sforza, so this is at best a weak lead there.
- Requests: de-crypt.org 60. No model subagent calls. Cost not visible to this session.

## Remaining gaps (SFZ-DEC3, 14 Oct 2026)
Read so far: 0 signs of f.15 transcribed or read; the Duke key gate G1 failed (0.441 mean held-out, 2 units; anchored 0.422); candidate period key DECODE R5323: blind gate PASS (SFZ-R5323B, 4 of 7 C pairs agreed, controls max 1, p < 0.0001), no key built yet
- R5323 key build - blocker: not-attempted; only the 7 C-pair cells were scored, no full transcription of R5323 exists; next: two blind passes transcribing R5323's whole alphabet block into key_r5323.tsv, agreed cells only, then decode_key.py on f.5/f.8 against their glosses with the G1 gate unchanged, ~$2
- f.15 decode - blocker: not-attempted; the owner's blind sort (ASKS row 165) remains the transcription route for f.15 itself; next: only after R5323 passes the f.5/f.8 gloss gate, apply it to f.15, ~$2
- f.17 blanks vs f.15 - blocker: not-attempted; whether f.15's cipher fills f.17's two blanks is unexamined; next: only after a readable key, ~$1
- DECODE scat. 1597 rest - blocker: not-attempted; nos. 79-114 and 169-171 unopened (nos. 1-78 done), and the twelve unheaded sheets in 36-77 not C-pair checked; next: only if R5323 fails the gloss gate, one login by the guess route (~45 requests), ~$2

## Escalation (SFZ-DEC3, 14 Oct 2026)
- [x] siblings: the Duke's glossed pairs f.5/f.7 and f.8/f.10 used; f.23-24/f.26, f.30-31/f.29, f.36-37/f.35 not yet
- [x] clear-pages: f.17 (same-day clear letter) noted as context; no copy of f.15 exists in the volume per Mazzatinti
- [x] known-keys: DECODE scat. 1597 nos. 1-78 opened by heading (SFZ-DEC, SFZ-DEC2, SFZ-DEC3); R5323 blind gate PASS at 4/7 (SFZ-R5323B); no. 50 "Cum duce Mediolani" (early 1440s by its nomenclator) is not the slips' key (stock coverage 0.157 vs random-stock null mean 0.149, p 0.40); nos. 79-114 and 169-171 not opened
- [ ] print: no print of f.15 located (check-solved above); verifier pass belongs to a later reading
- [x] key-rebuild: attempted, G1 FAIL
- [x] image-check: second machine reader tried and retired (SFZ-DUKE, 8 Oct); owner sign-sorter packet for f.5+f.8 built (SFZ-SORT, 13 Oct), waiting on the owner's sort (ASKS 165)
- [ ] retry: build key_r5323.tsv from two blind passes and test it against the f.5/f.8 glosses (G1 unchanged), then S3 on f.15
Verdict: keep going: 4 internal gaps; cheapest next: key_r5323.tsv from two blind passes and decode_key.py on f.5/f.8 against their glosses, ~$2

## SFZ-G1 (14 Oct 2026 22:05-22:2x UTC by date -u, account 4, LANE DEFAULT-A4-2135-14): key_r5323.tsv against the f.5/f.8 glosses -- registered gate FAIL (p 0.14 vs value permutations; both units under their own p95)
Job: SFZ-R5323B's named next step: a key from the two blind passes, decoded on f.5/f.8 and scored against their period glosses (f.7, f.10).
- **Prior work.** `tools/prior_work.py sforza-duke-1447-f15 --item-spec 'shelfmark=BnF italien 1584;folio=8;date=1447-01-10;...' --step-type
  key --offline`: exit 4, three own-work LEADs (escalation lines of SFZ-D/SFZ-SORT and SFZ-DEC2's claim), none a key test of R5323 on f.5/f.8;
  recorded CLEAR in prior-work.tsv. Its two plaintext KNOWN rows are Cryptiana valle.htm (Anjou 1583, f.5-9 of another volume): a
  folio-number collision, not this item. The f.5/f.8 plaintexts are known by design (their glosses are the known answer).
- **PREREG** `PREREG-SFZ-G1.md` with `g1/build_key.py` and `g1/score_g1.py`, pushed a94d400c9 before any key was built or decode run.
- **No new blind calls.** SFZ-R5323B's eight reader TSVs already list every letter column of R5323 in both label groups, so the two passes
  the brief asks for exist; 0 Sonnet calls here.
- **Key** (`python3 g1/build_key.py [--check]`, log g1/build.log): 13 labels with exactly one agreed letter (grade S): 3=i 8=u D=e N2=h
  N6=i N8=d O=a b=i c=m cu=n d=r f=s t=b. Left out as agreed in two or more columns: # (g/h/t), N4 (e/r), g (g/t), l (e/g), q (p/z).
  Control keys from the 11 other sheets by the same rule: 0-10 rows.
- **Decode** `python3 tools/decode_key.py ciphers/sforza-duke-1447-f15/g1` (g1/decode.json; ciphertext the committed SFZ-D transcriptions
  ../sforza-italien1584-1447/duke/ciphertext_f5/f8.tsv): f.5 896 tokens S 285 U 611; f.8 865 tokens S 305 U 560 (coverage 0.335 pooled);
  `--check` exit 0. Readings g1/reading_f5.txt, reading_f8.txt are test output, not readings of anything.
- **Result** (`python3 g1/score_g1.py`, g1/score.out): pooled gloss agreement R 0.1295 (f.5 0.1172, f.8 0.1422); value-permutation null
  (1000, seed 1447) mean 0.1178, p95 0.1352, p = 0.1429; unit p95 f.5 0.1317, f.8 0.1434; 11 other-key controls 0.000-0.102 (max R5312).
  Gate: (a) FAIL, (b) pass (0.1295 > 0.1022), (c) FAIL -> **FAIL**, logged as registered, not re-tuned. Loose key (16 rows, not gated) 0.1437.
- **Scorer change after the PREREG push (disclosed).** The pre-registered pure-Python alignment was too slow for 2000 alignments; it is
  kept as `align_py` and the same recurrence was vectorised (`align`): equal on 30 random pairs and on both real units (105, 123 matches).
- **Post hoc, not scored.** Clause (b) passes on coverage, not reading: the controls key fewer tokens (0.003-0.287). Against the Duke's
  own alignment key (../sforza-italien1584-1447/duke/key.tsv, mostly M, from a failed G1) 6 of the 13 rows agree (O, N8, N2, cu -- four of
  the seven C pairs the identification gate scored -- plus f=s and 8=u/v); 7 disagree (3, D, N6, b, c, d, t). Keyed tokens matched the gloss
  at about 39% (228 of 590) against about 35% under permutation; a right key with right cells should match most keyed tokens.
- **Grade.** The R5323 identification is not supported by the glosses at the blind readers' transcription of the sheet. Whether the
  failure is the sheet or the readers' cell placement cannot be told from this test: blind Sonnet reading of R5323 is retired as the
  instrument (attempts SFZ-R5323, SFZ-R5323B, SFZ-G1; rule 3 third-attempt clause). Nothing here is a reading.
- Requests: none (disk only). Sonnet calls 0. Cost not visible to this session.

## Remaining gaps (SFZ-G1, 14 Oct 2026)
Read so far: 0 signs of f.15 transcribed or read; the Duke key gate G1 failed (0.441 mean held-out, 2 units; anchored 0.422); DECODE R5323: blind identification gate PASS at threshold (SFZ-R5323B) but its blind-read key FAILs the f.5/f.8 gloss gate (SFZ-G1, p 0.14), so no period key is identified
- R5323 key - blocker: not-attempted; blind Sonnet reading of the sheet is retired (SFZ-R5323, SFZ-R5323B, SFZ-G1), the untried instrument is a person's cell-by-cell read of R5323's alphabet block, then the same g1 scorer unchanged; next: draft an ASKS row for that read, ~$0.5
- f.15 decode - blocker: waiting-on ASKS row 165 (the owner's blind sort of f.5+f.8 signs) for the transcription route; no key is identified for f.15
- f.17 blanks vs f.15 - blocker: not-attempted; whether f.15's cipher fills f.17's two blanks is unexamined; next: only after a readable key, ~$1
- DECODE scat. 1597 rest - blocker: not-attempted; nos. 79-114 and 169-171 unopened, and the twelve unheaded sheets in 36-77 not C-pair checked; next: one login by the guess route (~45 requests), C-pair check of any 1440s sheet against the f.5/f.8 glosses with g1/score_g1.py, ~$2

## Escalation (SFZ-G1, 14 Oct 2026)
- [x] siblings: the Duke's glossed pairs f.5/f.7 and f.8/f.10 used; f.23-24/f.26, f.30-31/f.29, f.36-37/f.35 not yet
- [x] clear-pages: f.17 (same-day clear letter) noted as context; no copy of f.15 exists in the volume per Mazzatinti
- [ ] known-keys: DECODE scat. 1597 nos. 1-78 opened by heading; R5323 identification gate PASS at 4/7 (SFZ-R5323B) but its key FAILs the f.5/f.8 glosses (SFZ-G1); nos. 79-114 and 169-171 not opened
- [ ] print: no print of f.15 located (check-solved above); verifier pass belongs to a later reading
- [x] key-rebuild: attempted, G1 FAIL
- [x] image-check: second machine reader tried and retired (SFZ-DUKE, 8 Oct); owner sign-sorter packet for f.5+f.8 built (SFZ-SORT, 13 Oct), waiting on the owner's sort (ASKS 165)
- [ ] retry: DECODE scat. 1597 nos. 79-114 and 169-171 by heading, then any 1440s sheet through the g1 gloss scorer
Verdict: keep going: 3 internal gaps; cheapest next: DECODE scat. 1597 nos. 79-114 and 169-171 by heading, one login (~45 requests), ~$2
