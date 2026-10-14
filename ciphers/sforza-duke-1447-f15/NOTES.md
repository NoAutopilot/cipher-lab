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
