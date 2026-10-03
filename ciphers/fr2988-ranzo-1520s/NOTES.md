open
Molini, Documenti di storia italiana vol. 2 (1836), 'Omessi di copiare' list, no. 8513 (prefatory p. xxvi, Google Books page id PR26) (= fr.2988) read by this worker (GF4-BATCH14, 3 Oct 2026, archive.org documentidistor02moligoog djvu l.1031-1037): "a c. 9 e altra lettera dello stesso parimente in cifra, ma senza l'interpetrazione"; CSP Spain III pts 1-2 (1525-1529) full text, no Ranzo letter.

**LANE N3 orchestrator, 24 Sept 2026 18:03 UTC:** open, but not a separate nomination: same Ranzo corpus as ciphers/fr3022-garbino-1528 (Bourdeau pooled both); the recovery/cryptanalysis lane should treat them as one target.

**Edition check (LANE N3 csED3, 24 Sept 2026 18:xx UTC):** hold lifted -- verdict `open`, but **same key/corpus as
CS2-01 (`ciphers/fr3022-garbino-1528`), already on the board -- do not open a second board slot for this folder.**
Calendar of State Papers Venice vols III (1520-1526) and IV (1527-1533), full text, and Marino Sanudo's *I Diarii*
vol. XLIII (1 Oct 1526 - end Jan 1527, bracketing the one hard date in this volume's contents note), full text, all
read on archive.org; none names Ranzo. DECODE record documents and Aymeloglu's repository checked (below).
Bourdeau's own repository shows he already transcribed this exact letter as part of his combined Ranzo/no.20
corpus. Section 2 below. Brief `.claude/briefs/runs/2026-09-24-lane-n3-csED3.md`.

# Hieronimo Ranzo (Venice) cipher letters, 1520s — BnF fr. 2988 ff.9r-11v

QUEUE row: CS2-15 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 170 at dbourdeau.github.io/cyphersolver/catalogue.html), DECODE R1894. Check-solved run
24 September 2026 by LANE N3 csCS2c (session_0113dPptSGXZiBF5uwvtKmtc), brief
`.claude/briefs/runs/2026-09-24-lane-n3-csCS2c.md`.

## What it is

Bourdeau's catalogue: "attempted, open (same initial-letter+number code as CS2-01/Garbino letter; non-alphabetical
numbering; annealer recovers only function words)." Two items headed "Lettre en chiffre de « V° HIERONIMO RANZO »"
appear in the fr.2988 recueil (items 1 and 3 of the volume's contents, per the BnF catalogue note below);
Bourdeau's ff.9-11 citation and DECODE R1894 point at this same pair. Prior scout pass (24 Sept 2026) marked the
image route "likely on Gallica; ark not confirmed" and the row "copy-order (unconfirmed, check Gallica fr.2988)."

## Image route (confirmed copy-free, this pass)

Gallica SRU (`dc.type all "manuscrit"` scoped to "Français 2988") returns two digitisations of the same
shelfmark (one "from the original document," one "from a substitute document," both giving identical catalogue
text) — used the original-document one, ark `btv1b525240150`. IIIF manifest (278 canvases) carries real foliation
labels for this volume (not "NP"): canvas index 24 = "9r", 25 = "9v", 26 = "10r", 27 = "10v", 28 = "11r", 29 =
"11v" (Gallica view numbers f25-f30). info.json for f25: 4298×5845, level2 profile, full resolution. **Image is
online now, full size, folios pinned exactly** (no eye-checked anchor needed — this manifest, unlike fr.15564,
carries genuine per-canvas foliation).

The BnF catalogue's contents note for fr.2988 (read via the same SRU record) lists, among ~56 items: "1 Lettre en
chiffre de « V° HIERONIMO RANZO » ; 2 « Double de lettres escriptes en chiffre par NICOLAS RAINCE,... De Romme,
XVme decembre V.C.XXVI [15 Dec 1526] » ; 3 Lettre en chiffre de « V° HIERONIMO RANZO » ; 4 «Proposition de la
majesté imperiale...1546»..." Items 1 and 3 (Ranzo's own cipher letters) flank item 2, Nicolas Raince's "double"
(copy) of separately-enciphered letters dated Dec 1526 from Rome — **these are catalogued as three distinct
items, not one continuous correspondence**; nothing in the catalogue note states item 2 is a decipherment of
items 1 or 3. No recipient is named for Ranzo's letters (items 1, 3) in this note.

## Same correspondence/key as CS2-01? (brief's question) -- yes, and already merged by Bourdeau himself

Bourdeau's own catalogue entry for CS2-15 states "same initial-letter+number code as CS2-01/Garbino letter"
(CS2-01 = BnF fr. 3022 no. 20, Hieronimo Ranzo(?) to "Garbino," 11 Apr 1528, ff.44r-46v). Checking his working
folder directly (fresh shallow clone of dbourdeau/cyphersolver, 24 Sept 2026, `vasto1527/NOTES.md`) goes further
than "same system": **he already transcribed this exact letter and pooled it into his no.20 corpus**:

> "Ranzo's signed letters, BnF fr. 2988 ff. 2r-v, 9r-10v (ark btv1b9059908w, views 6, 7, 17-20) | ~2,600 [groups] |
> `n20/ranzo_c0*.txt`, transcribed by six subagents. f. 2v is marked "dup.a" (duplicate)."

and, citing the DECODE record directly:

> "DECODE R1894 (catalogue entry 170), 21 Sept 2026. The record 'BNdF AncienFonds invnr.2988 ff9-11' (Ranzo,
> Italian, 4 pp., dated 1520 by BnF's 1520-29 range) is the fr. 2988 Ranzo letter already transcribed above.
> The record has no key, decipherment or transcription. Nothing new was attempted, and the entry is marked
> 'attempted, open' in the same state as no. 20."

So this folder's target (fr.2988 ff.9r-11v, DECODE R1894) **is** one of the two Ranzo cipher items Bourdeau already
folded into the combined ~3,900-group corpus that LANE R4 worker N's control-first cryptanalysis note (ROOM.md,
17:10) already accounts for under `ciphers/fr3022-garbino-1528` ("Bourdeau's best: 46% token / 9% type at ~3,900
pooled groups"). **Recommendation: do not nominate this folder as a separate stage-2 board slot.** Either fold this
folder's content into `ciphers/fr3022-garbino-1528/NOTES.md` as a sibling-source section, or keep it as a
reference folder cross-linked from there, but any future recovery/cryptanalysis pass should work the pooled
corpus once, not attack fr3022 and fr2988 as two unrelated targets and double the cost.

**Ark discrepancy, flagged not resolved (Gallica is not a host this brief grants):** Bourdeau's ark for fr.2988 is
`btv1b9059908w` (views 6, 7 = f.2r-v; 17-20 = f.9r-10v), confirmed by him against real transcribed content. The
prior csCS2c pass in this folder used a **different** ark, `btv1b525240150`, inferred only from IIIF canvas
foliation labels, never checked against page content. Gallica documents "two digitisations of the same shelfmark"
(original vs. substitute); these may be the same two, or one may be wrong. A recovery-lane worker must confirm
which ark actually shows Ranzo's cipher before capturing images -- do not assume csCS2c's ark is correct just
because its foliation labels lined up.

f.2 itself is also its own DECODE record (R2294, "Français 2988, f.2", Non-decrypted, see below) -- so "item 1"
of the BnF contents note (the first "Lettre en chiffre de V HIERONIMO RANZO") is very likely f.2, distinct from
"item 3" (this folder's ff.9-11), consistent with Bourdeau transcribing both as one Ranzo set.

## Date (brief's question: date from the clear parts and Bourdeau's notes)

No exact date is established for ff.9r-11v specifically -- grade I (inferred), not H or C. What is known:

- DECODE's own two records for this item give only decade brackets: R1894 "1520-1529" (BnF's own range per
  Bourdeau's quote above), R2295 "1520-1540".
- The BnF contents note (section "Image route" above) catalogues Ranzo's two letters (items 1, 3) flanking
  Nicolas Raince's "double" of Dec 1526 letters (item 2) -- a shelving/binding order, not proof the Ranzo items
  are contemporary with Dec 1526, but consistent with it (recueils of this kind are often bound in roughly
  chronological blocks).
- WebSearch (this pass) on the Gattinara family: Girolamo/Hieronimo Ranzo appears in Piedmontese archival material
  on the Arborio di Gattinara family (ASVercelli finding aid; aggregated search snippets, not independently
  fetched against a citable primary text this pass -- flag as unverified) as a relative of Chancellor Mercurino
  Gattinara, in his household, presenting accounts as his **chamberlain for 1524-1529**. This is consistent with,
  not proof of, a Ranzo cipher letter from within that decade.

Taken together (grade I): **c.1524-1529, most plausibly nearer 1526** (the Raince flanking date), is the best
available estimate, not an established date. On that basis this pass read the calendars for the full decade
(CSP Venice) and the sub-period bracketing the one hard date in the volume (Sanudo vol. XLIII), rather than a
single month, since no single month can be justified as *the* date.

## Six-source search log (24 September 2026)

1. **Tomokiyo / Cryptiana** (named source for this cipher family). WebSearch located Cryptiana content on
   Ranzo's system: "Document No. 20 from Madrid dated 11 April 1528 is in the initial-letter code of Hieronimo
   Ranzo, Gattinara's kinsman... Tomokiyo published a partial key and left two thirds of the first page unread.
   The key checks against the glosses (Guienne, tres confident, Fumé; adds 87 = e, 22 null, # = Roy de
   Navarre)." A second search confirms the same wording: "No. 20, from Madrid on 11 April 1528, is in the
   initial-letter code of Hieronimo Ranzo, Gattinara's kinsman. However, No. 20 needs Ranzo's table or a clear
   copy to be fully deciphered." **Both quoted passages describe CS2-01 (fr.3022 no.20, the Garbino letter)
   specifically, by date and archival number — neither names fr.2988 or an ff.9-11 item.** No sentence located
   anywhere (WebSearch, not the live cryptiana.web.fc2.com site directly, which was not fetched this pass)
   claims fr.2988 ff.9-11 itself has been read, partially or fully. Per the M9/Morvillier lesson (check-solved.md):
   this is quoted verbatim precisely because it is *not* a claim about this letter, to avoid the same overclaim.
2. **Standard printed edition / calendar (edition check, LANE N3 csED3, 24 Sept 2026).** No French royal/
   diplomatic series calendars an intercepted Venetian dispatch, so the calendar that covers this sender and
   period is the *Calendar of State Papers, Venice* (the standard English-language calendar for exactly this
   place/decade), read in full text on archive.org: vol. III pt.1, 1520-1526 (ed. Rawdon Brown, London 1869,
   archive.org id `calendarofstatep3118brow`, 30,723 lines OCR) and vol. IV, 1527-1533 (ed. Rawdon Brown, London
   1871, id `calendarofstatep4187brow`, 57,933 lines OCR) -- both grepped for "Ranzo" and "Ranz[oc]": **no genuine
   hit in either** (only false positives on the surname "Soranzo"); OCR quality confirmed usable by "Gattinara"
   (80 + 39 hits) and "Venice" (248 + 367 hits) counts, both far above chance. Marino Sanudo's *I Diarii* --
   vol. LIX (`idiariidimarinos59sanu`) is the edition's own 1903 "Indice Generale" (a volume/date map, not a name
   index: "XLIII / 1526, 1 ottobre - 1527, [end] Jan[uary]"), used to locate the volume bracketing the one hard
   date this folder has (Dec 1526, the Raince flanking item): **vol. XLIII** (`idiariidimarinos43sanu`, Oct 1526 -
   end Jan 1527, 66,559 lines OCR), fetched and grepped: **no genuine "Ranzo" hit** (only "Soranzo" false
   positives), OCR usable (373 hits for "venezia/venetia"). The other ~9 volumes covering the wider c.1524-1529
   window (vols XXXVI-XLII, XLIV-LI roughly) were not fetched this pass (58-volume edition, no exact date to
   narrow further, out of this pass's budget) -- flagged for whoever promotes this to a solver stage, though
   given a real hit in vol. XLIII specifically (bracketing the one hard date available) would have been the most
   likely single volume to carry one.
3. **DECODE R1894 documents.** `sources/decode/records-non-decrypted-2026-09-24.tsv` (on disk) confirms status
   "Non-decrypted" for id 1894 but carries no document-attachment column. Cross-checked against a fresh shallow
   clone of aaymeloglu/unsolved-ciphers's `catalogue/decode-records.jsonl` (a public, no-login RecordsView field
   scrape, dated 23 Sept 2026 by that repo's own git log -- confirmed public: `catalogue/fetch_decode.py`'s own
   docstring states "No login is used: the fields, including... 'Available Documents', are public"): id **1894**
   carries `"Available Documents": "Transcription"` (not Key or Decryption -- DECODE's schema distinguishes these,
   confirmed by a different record in the same dataset, id 2988/BL Add MS 4136, "Partially decrypted" with
   `"Available Documents": "Key"`, a stronger category). This is a hard filter per COMMON addition (c) and was
   checked, not skipped: a "Transcription" document is a raw ciphertext transcription, not a decipherment, and is
   fully consistent with Bourdeau's own 21 Sept note (quoted above) that "the record has no key, decipherment" and
   with his own independent transcription of this exact letter around the same date -- most plausibly the same
   transcription, or one like it. DECODE's own Status field ("Non-decrypted") is unchanged between the 24 Sept
   `sources/decode/` snapshot and the 23 Sept Aymeloglu scrape. **Conclusion: hard filter checked and cleared --
   a transcription exists, a decipherment does not.** The neighbouring f.2 item (id 2294, "Français 2988, f.2",
   also Ranzo per Bourdeau's combined-corpus note above) carries the same "Transcription" tag and the same
   reasoning applies. DocumentsList itself (the document's actual content) needs a DECODE login, which this
   brief reserves to the DECODE worker; not fetched.
4. **Solver repositories.** dbourdeau/cyphersolver (fresh shallow clone): covered fully above -- this letter is
   already transcribed and pooled into the no.20/Ranzo corpus, verdict "attempted, open," in the same unsolved
   state as CS2-01. aaymeloglu/unsolved-ciphers (fresh shallow clone, 24 Sept 2026): grepped by shelfmark
   ("2988") and name ("ranzo", "garbino") across the whole repository -- the only hits are the catalogue-harvest
   files already used in item 3 above (`decode-records.jsonl`, `decode-catalog.csv`, `pares-hits.jsonl`,
   `bne-records.jsonl`, none of which is a solve claim), and no target folder (`burgess-1912/`, `ferdinand-1634/`,
   `ferdinand-1635-1640/`, `forster-1644/`, `moray-1568/`, `ottobon-1589/`, `royalist-1646/`, `starhemberg-1758/`,
   `vande-perre-1653/`) touches this shelfmark or sender.
5. **General web / comment threads.** No further hit beyond the Tomokiyo/Cryptiana material in item 1 and the
   Gattinara-household material in the Date section above.

## Verdict: `open` (same key/corpus as CS2-01 -- see above; do not double-book the board)

**3 Oct 2026 (RANZO-NB):** still `open`. fr.3019 no.27 neighbours and no.36 (f.94) carry no clear copy, gloss or key; f.74r is marked "dupp^ta". Next: compare no.27 with fr.2988 f.2r-v ("dup.a") for a second copy (section "fr.3019 no.27 neighbours" below).

**3 Oct 2026 (A1B-RANZO-2WIT):** still `open`. Full fr.3019 no.27 transcribed (813 tokens) and settled against fr.2988 f.2r-v: our read 0.018 settled error (N 813, lower bound; 0.011 reader-only, the rest a crop-region miss), Bourdeau's 0.035 (21 of 29 are a systematic s->g labelling flip on f.2v); r41/t41 is a recurring copy variant. Next: re-label Bourdeau's c007 g->s before any pooled-corpus attack (script, ~USD 0.5), then the target still needs a key-bearing source (section "Two-witness transcription" below).

**3 Oct 2026 (RANZO-DUP):** still `open`. fr.3019 no.27 (f.73r-74r) and fr.2988 f.2r-v are two copies of the same letter (41/44 and 57/66 tokens agree on the lines compared); both wholly cipher, so no crib. Next: full no.27 transcription diffed against Bourdeau c006/c007 for a measured reader error, about USD 13.5 (section "Duplicate check" below).

Image confirmed online (full resolution, folios pinned exactly, ark discrepancy flagged above). CSP Venice
(both volumes covering the full 1520-1533 range) and Sanudo vol. XLIII (bracketing the one hard date available)
read in full text: no hit. DECODE's own hard filter (an attached "Transcription" document) checked and cleared --
it is Bourdeau's own transcription work, not a decipherment. No source read this pass, including both solver
repositories, claims fr.2988 ff.9-11 has been deciphered or its key recovered; the only published work on this
cipher *family* (Tomokiyo's partial initial-letter-code key) is explicitly about a different item (CS2-01/fr.3022
no.20) and is itself incomplete. **This is not a new target: it is unread material Bourdeau already folded into
CS2-01/fr3022-garbino-1528's corpus.** Flag for whoever next works the pooled corpus: try Tomokiyo's partial
Ranzo key (glosses in item 1 above) against this letter's ciphertext before any fresh cryptanalysis.

**Nomination:** posted to ROOM.md, marked explicitly as same-key-as-CS2-01 / no new board slot (see recommendation
above), not as an independent stage-2 candidate.

Rule 10: no novelty claim made. Not decoded, not transcribed (out of scope for check-solved).

Requests this pass (csCS2c, 24 Sept, earlier): gallica.bnf.fr SRU 1, manifest 1, info.json 1 (3-4 total). WebSearch
2. This pass (csED3): archive.org 5 (2 CSP Venice djvu.txt, 1 Sanudo indice djvu.txt, 1 Sanudo vol.43 djvu.txt,
1 advancedsearch), all >=1.5s apart, single fetcher (IA slot). github.com 2 shallow clones (dbourdeau/cyphersolver,
aaymeloglu/unsolved-ciphers, grep only). WebSearch/WebFetch: see the combined report in the Mellon-29 folder's
"Requests" line for the shared background-agent pass (Gattinara-household search, CSP Venice/Sanudo index probes --
that agent's own host counts are internal to its report, not separately billed to a brief host). No DECODE login.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/catalogue.json #170 ; targets/vasto1527/n20/ranzo_c0*.txt
- Their extent, in their words: ff. 9-11 (R1894) transcribed with the Garbino letter (~2,600 groups), same initial-letter+number code; annealer gives function words only; needs Ranzo's table
- Their date: 21 Sept 2026
- Note: already cited in our NOTES.md (catalogue item 170)
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (GF4-BATCH14, account-4, 3 Oct 2026)

Plain web searches (WebSearch, 4 runs): (1) `"Ranzo" cipher letter Gattinara 1526 "2988"` -- Bourdeau's site and
three GitHub forks of cyphersolver (setsunaatto, arya1515, aryasn2026; copies, not separate work), no reading;
(2) `"Hieronimo Ranzo" chiffre lettre` -- BnF archivesetmanuscrits records for Fr. 2988, Fr. 3019, Fr. 4050-4051
(catalogue only); (3) `"Français 2988" chiffre Ranzo` -- BnF record and Biblissima manifest only; (4) `Ranzo Garbino
1528 cipher decipherment initial-letter code Tomokiyo` -- Bourdeau's pages ("~3,900 groups ... unsolved"); (5) model-solve
query `Ranzo cipher solves Claude OR GPT` -- only the Cyphral Distich news, nothing on Ranzo.
Blog site searches: **Cipherbrain** (`Ranzo cipher site:scienceblogs.de`) -- the 17 May 2016 post "Wer löst diesen
verschlüsselten Brief aus dem französischen Nationalarchiv" and the 24 Mar 2017 Spinelli post; **Cryptiana**
(`site:cryptiana.blogspot.com` Ranzo Gattinara) -- no hit; **Cipher Mysteries** (`site:ciphermysteries.com` Ranzo
Gattinara) -- no hit.
Comment threads opened and read in full (curl, scienceblogs.de, 21 comments):
- 17 May 2016 post, about Gallica btv1b9059908w (this volume). Torbjörn Andersson (#9, 29 Mar 2017) posts a key and
  English plaintext ("Pleis your Majesty ...") for the **simple-substitution letter at the head of the volume**, which he
  (#16) and Norbert (#18, 21 Oct 2017) judge misplaced and not Ranzo's. Norbert: "Die Geheimtexte auf den nachfolgenden
  Seiten [f6] und ab folio 9 [f17] sind von Ranzo unterschrieben und ganz offensichtlich wesentlich komplexer"; Thomas
  (#21): "Zu dem Nomenklator von Ranzos Brief fol. 2 konnte ich nichts finden." Norbert (#20) also refutes Molini's
  "interpretation" at c.4 (it is Raince's double of 15 Dec 1526). **Nothing in the thread deciphers ff.9-11.** It points
  to fr.3022 f.50, the "adizione nel zifra" (Ranzo's addition sheet, since used by Bourdeau).
- 24 Mar 2017 Spinelli post: comment #14 only says "the unbroken Ranzo cipher which also dates around the year 1520".
Same thread already logged independently in ciphers/decode-4450-bnf-fr20506-1525/NOTES.md (same reading of it).
Cabinet Noir (github.com/el-descifrador/cabinet-noir, shallow clone HEAD 47b6db9, 2 Oct 2026; CC BY 4.0): grep for
2988, 3022, ranzo, garbino -- no folder or file (two false hits on "zubeZalen" in malsburg-1637 key TSVs). Result: no
decipherment or plaintext of ff.9-11 found in any blog post, comment or repository searched.

## Premise check (GF4-BATCH14, account-4, 3 Oct 2026)

(a) **Folder's own mentions -- not found (checked).** The only "interpretation" anywhere is Molini's c.4 French text,
which Molini himself ties to the c.1 letter and explicitly denies for c.9 (line 2 above); the BnF 1868 catalogue and
Cipherbrain #20 identify c.4 as Raince's double of 15 Dec 1526 (FT4 viewed it: clear French, Rome news). DECODE R1894's
attached "Transcription" is a ciphertext transcription, not a decipherment (section above).
(b) **Other solvers' working files -- not found.** Bourdeau, github.com/dbourdeau/cyphersolver HEAD 4aedb40 (2 Oct 2026),
sparse clone of targets/vasto1527: `n20/ranzo_c017-c020.txt` are his transcriptions of views 17-20 (ff.9r-10v); his
`solve2.py` annealer recovers only a function-word skeleton on the pooled no.20+Ranzo corpus (control 46% token / 9% type);
no rendering, apply-key output or key exists. Aymeloglu: no target folder (prior pass). Cabinet Noir: nothing (above).
(c) **Physical neighbours -- not found.** Gallica btv1b9059908w (labels all "NP"; foliation from the leaf numbers) viewed by
this worker: view 15 and view 16 (f.8, blank, only show-through), view 21 (f.11r, blank apart from pen trials), view 22
(f.11v: **address panel**, native crop rotated 270: "R.do S. ... [G]arbino" across the seal cut, a date-like "...rzo",
and two dorse words "Luna"/"Lura" and "tup^ta"; no clear text), view 23 (f.12, blank), view 24. No clear copy, gloss or slip
beside the cipher. The f.11v address to **Garbino** (reading grade I, cut by the seal gap) ties ff.9-11 to the same addressee
as fr.3022 no.20 -- not noted in Bourdeau's NOTES, which list only ff.9r-10v.
(d) **Recipient's side -- not found.** CSP Spain vol. III pt 1 (1525-26, archive.org calendarofletter0003pasc) and pt 2
(1527-29, calendarorleters0003vari), full text grepped: "Ranzo" 1 hit (introduction, Gattinara's mother Felicita Ranzo),
"Garbino" 0; OCR usable (Gattinara 80 and 117 hits). Garbino's own papers are not located (Bourdeau's crib list names them).
Sibling lead, not this item: Molini vol. 2 no. 8544 (prefatory p. xxxii, Google Books PR32; djvu l.1326-1328) "A c. 73. Lettera senza data ne direzione, tutta in cifra,
colla sola firma Hieronimo Ranzo" = Bourdeau's fr.3019 no.27 f.73 (btv1b9059994n views 114-116, "no interlinear or separate
decipherment").

Verdict after both checks: **`open`** (unchanged). Not found-solved: no printed or posted decipherment or plaintext of ff.9-11.
Requests this pass: scienceblogs.de 1 (curl) + 2 (fetch tool); gallica.bnf.fr 10 (1 manifest, 9 IIIF images); archive.org 6
(1 advancedsearch, 2 metadata, 3 djvu.txt); github.com 2 shallow clones; WebSearch 8. All >=1.5 s apart per host.

## fr.3019 no.27 neighbours and f.94 view (RANZO-NB, LANE-A1 account 1, 3 Oct 2026)

Gallica btv1b9059994n (labels all "NP"; foliation from the leaf numbers), overviews at 808 px, crops by
`tools/iiif_lines.py --ark btv1b9059994n --canvas N --region x,y,w,h --out ciphers/fr2988-ranzo-1520s/images/fr3019`
(views 112, 114, 116, 118; manifest in that folder). Per view:

| view | folio | content | date / writer |
|---|---|---|---|
| 112 | f.71v (dorse, landscape) | endorsement of the preceding item, French, "...[me]moire p[ou]r le fait des / ligues(?)" (grade I) | not Ranzo |
| 113 | f.72 | blank | -- |
| 114 | f.73r | cipher, Ranzo's letter+superscript-number code, opening "f5 g1 p149 h4 [47 a154 s116 s9 h158 h57 f5 ..." (no interlinear) | -- |
| 115 | f.73v | cipher, same code, no interlinear | -- |
| 116 | f.74r | cipher: 3 lines with numbers above letters, a "/." break, then about 20 lines in the same code written letter-then-number inline (same tokens, e.g. [47, p149, m170; a layout change, not a second system); signature "Hieronimo Ranzo"; at lower left **"dupp^ta"** (duplicata) | Ranzo (signature) |
| 117 | f.75 | blank | -- |
| 118 | dorse, landscape | docket "Des garnisons de picardie / Pour les mois de Mars / et Avril 1559" -- belongs to another item | 1559, not Ranzo |
| 144 | f.92v | blank | -- |
| 145 | f.93r | clear Italian letter to the King ("Sire ... de Lyone al p° de Novembre M.D.XXVI"), signed Theodoro [Trivulzio] (grade M on name and date) | 1526 |
| 146 | f.94r (no.36) | clear Italian "Reporto de homo novamente venuto da Genova" (Andrea Doria, Savona, Cremona, Asti) -- an intelligence report, plausibly the "avisi" enclosed in f.93 | c. 1526 |
| 147 | f.94v | continuation of the report, clear Italian | -- |
| 153-157 | ff.98r-100v | clear French letters | not Ranzo |

**Result: no clear copy, gloss, interlinear or key for Ranzo's code in fr.3019 ff.71v-75 or ff.92v-94v (no.36 is a
clear Genoa report, not a decipherment of no.27).** One new fact: f.74r is marked **"dupp^ta"**, so no.27 is a
duplicate -- an original (or another duplicate) of the same letter existed. It is **not** fr.2988 f.9r: the opening
of f.9r (btv1b9059908w view 17, overview) is "b5 f3 c27 g72 p246 ...", against f.73r's "f5 g1 p149 h4 [47 ...";
fr.2988 f.2v's "dup.a" (Bourdeau) remains the other duplicate mark in the corpus and was not compared here.
Requests: gallica.bnf.fr 23 (1 manifest, 17 overviews, 5 native regions), >=1.5 s apart. Vision: 4 contact sheets
+ 7 crops read by this worker.

## Duplicate check: fr.3019 no.27 vs fr.2988 f.2r-v (RANZO-DUP, LANE-A1 account 1, 3 Oct 2026)

Method: Bourdeau's transcriptions (github.com/dbourdeau/cyphersolver HEAD a439937, 3 Oct 2026, sparse clone of
`targets/vasto1527/n20/`, MIT; `ranzo_c006.txt`/`c007.txt` = fr.2988 views 6-7 = f.2r-v; `c017`-`c020` = ff.9r-10v)
against 9 lines of fr.3019 read by this worker from the crops already in `images/fr3019/` (v114top_L01_s1/s2 =
f.73r lines 1-3; v116break_L01_s1/s2 = f.74r around the "/." break). My tokens: `fr3019_no27_sample_tokens.txt`.
Compared by exact trigram search over all six Bourdeau files, then difflib alignment. fr.2988's own images were
**not** viewed this pass: the fr.2988 side is Bourdeau's transcription (rule 2: conditional on it).

**Result: fr.3019 no.27 (f.73r-74r, "dupp^ta") and fr.2988 f.2r-v ("dup.a") are two copies of the same letter.**
- f.73r lines 1-3 (44 tokens) align with c006 tokens 0-44: 41 of 44 agree; differences g1/s1 (pos 1), h158/h58
  (pos 8), r41/t41 (pos 27), plus Bourdeau's "?2" at the end of his line 1 (not on f.73r line 1).
- f.74r 6 lines around the break (66 tokens) align with c007 tokens 203-268: 57 of 66 agree. The "/." break on
  f.74r falls exactly at Bourdeau's "/ |" in c007 (after "c227 L131 h10 r64 d10 t89 o3 h5"), so the layout change
  to inline letter-number writing is in both copies. Differences: s113/g113, s77/g77, b147/h147, s6/g6, s116/g116,
  "89"/g9, t137/r137, and an ink blot on f.74r (one token unreadable, X) that Bourdeau's copy reads cleanly.
  Five of nine are fr.3019 "s" vs fr.2988 "g": either a copy difference or one reader's s/g confusion in this hand
  -- **unsettled until the fr.2988 views 6-7 crops are read for those positions** (grade M on both sides).
- ff.9r-10v (c017-c020) are a **different** letter: 10 shared trigrams of 821 (common function groups), 1 shared
  4-gram, 0 shared 5-grams with c006+c007.
- **No crib.** Both copies are wholly in cipher where compared (openings, the break, the inline section's start);
  neither carries clear text, interlinear or gloss where the other is cipher. The signature "Hieronimo Ranzo" on
  f.74r is clear in fr.3019; Bourdeau's c007 ends "... t10 /" with no signature transcribed (not checked on image).
- What the pair gives: a two-witness transcription check of about 830 tokens (c006 428 + c007 396 Bourdeau tokens)
  -- a measured reader error for the Ranzo corpus, and the readings to fix where copies disagree. It adds **no** pool
  length (same plaintext), so Bourdeau's pooled-annealer negative is unchanged.
Requests this pass: github.com 1 sparse clone. Vision: 1 batch (4 existing crops) read by this worker, 0 subagents.

## While waiting

Done 3 Oct 2026 (A1B-RANZO-2WIT, section "Two-witness transcription"). Next step that depends on nobody: relabel the
compact-8 tokens of Bourdeau's c007 (and the open-g tokens of c006) from the settled pairs in `twowit_diff.tsv`, check the
other Ranzo pages c017-c020 for the same flip on their own images, and re-run his pooled-corpus annealer control with the
corrected labels (~USD 2). Earlier step, kept for the record: transcribe fr.3019 no.27 in full (ff.73r-74r, about 830 tokens, line crops by
`tools/iiif_lines.py --ark btv1b9059994n --canvas 114/115/116`) and diff it token-for-token against Bourdeau's
c006/c007, settling each disagreement on native crops of both copies (fr.2988 btv1b9059908w views 6-7); the s/g split
above is the first item. Price: about 8 Sonnet line-crop passes x USD 1.5 + 1 reconciliation = about USD 13.5. The
result is a measured transcription error for the pooled Ranzo/no.20 corpus, not a crib. Beyond that the target needs
a key-bearing source (Garbino's papers, not located) -- no clear copy of either Ranzo letter has been found.

**Passes (step 2).** Seven Sonnet subagent calls, blind, Bourdeau's sign labels as inventory, no Bourdeau tokens shown:
A f.73r/f.73v/f.74r and B f.73v on the 2-line band crops above; then, after pass A f.73v reported ~25 superscripts clipped
at band tops (2-line bands cannot keep both the descenders and the next line's superscripts), single-line crops 280 px tall
were cut from the cached native regions (`tools/iiif_lines.py --image <src> --region 0,<centre-180>,<w>,280 --centres 70,210
--lines-per-crop 2 --overlap 200`, prefixes f73rlNN / f73vlNN / f74rlNN, NN = line; f.74r lines 6-16 not re-cut: the tool
had downscaled its cached source once the folder passed 30 MB, a refetch got Gallica HTTP 500 and was not retried, and those
inline-layout lines read cleanly on the band crops), and B f.73r, B f.74r and C f.73v ran on them. A first B f.73r was
discarded unread-for-scoring: parallel subagents wrote helper files with the same names into one shared folder and its line 3
held f.73v text (lesson: give each transcription subagent a private work folder). Files: `passes/`.
Two-reader agreement (`tools/reconcile_passes.py`, token level): f.73r A/B 289/320 = 0.903; f.73v A/B 283/301 = 0.940,
A/B/C 240/307 = 0.782; f.74r A/B 183/193 = 0.948. Reconciled read (`build_fr3019_tokens.py`, my settlements in `settle.tsv`;
on a split the single-line-crop pass is taken: B f.73r, C f.73v, A f.74r): **813 tokens + 4 "/"** ->
`fr3019_no27_tokens.tsv`.

**Two-witness diff (steps 3-4).** `twowit_diff.py` aligns the reconciled read with Bourdeau's c006+c007 (copies in
`bourdeau/`, github.com/dbourdeau/cyphersolver a439937, MIT / CC BY 4.0, D. Bourdeau): 813 vs 817 tokens, **750 equal,
raw agreement 0.918**, 70 disagreement rows (+1 notation-only row, class N, our "?" uncertainty mark, removed by the script).
Each row was settled on paired native tiles of both copies (fr.3019 btv1b9059994n views 114-116; fr.2988 btv1b9059908w
views 6-7, native regions 1080,250,2900,4550 and 1330,200,2700,4450, fetched once, not committed; 12 contact sheets of 6
pairs, read by this worker) and classed per the pre-registration -> `twowit_diff.tsv` (class + note per row):

| class | n | what |
|---|---|---|
| R3019 (our error) | 15 | 9 reader errors: f5/t, q17/g17, d78/D78, z7/Q, h29/h129, Q21/c21, t222/r222, h32/h3, m170/m, r296/r (bare); 6 tokens at f.73v line starts left of this job's crop region (x<1550), settled on a native strip x 1250-1900 (one extra request): Q6, i29, o2, v42, c170, d100 -- a crop error of this job, not of the readers. `fr3019_no27_settled.tsv` carries all 15 fixes |
| RB (Bourdeau reader error) | 8 | folio number "2" read as a token, b30->h30, q12->g12, y18->y8, b147->h147, t137->r137, b26->h26, g1->s1 |
| RB-sg (Bourdeau s/g label) | 21 | see s/g below |
| V (copy variant) | 13 | numbers: 286/266, 196/296, 297/247, 159/153, 20/10, 16/6; sign: **r41 (fr.3019) / t41 (fr.2988) four times**, m/n once; fr.3019 has two extra tokens at a line break (p149 r4 / p97 r41 vs p149 r41) and one cancelled sign (ink-struck) absent from fr.2988 |
| U (unsettled) | 13 | 10 at f.73v line ends in the fr.3019 gutter; 1 fr.2988 line end beyond my fetched region (L14 vs L143); fr.2988's ink blot over a number (1); a z-tail crossing a digit on fr.2988 (1) |

**s/g settled first (pre-registration item 4).** fr.2988's hand has two forms, a compact closed "8" and an open-bowled g
(both in one line, e.g. 8^113 beside g^140 on f.2v), matching fr.3019's plain S and its g. So the 21 s/g rows are
Bourdeau labelling errors, and they are systematic: **his c007 (f.2v) labels the compact 8 (= s) as "g" in every disagreement checked (21 of 21),
while his c006 (f.2r) labels the compact 8 as "s" and at least once the open g as "s" too (g1 -> s1, an RB row)**. In his pooled Ranzo corpus the fr.2988 f.2v
s tokens are therefore filed under g, inconsistently with f.2r and with the other Ranzo files -- worth telling him with the
evidence (his annealer's type counts are affected); not posted, a parent's call (Outreach gates).

**Result (step 5, pre-registered measures; `twowit_stats.py` prints all of these):**
- raw two-copy token agreement 750/817 = **0.918** (this is agreement, not accuracy);
- reconciled fr.3019 read, settled per-token error **15/813 = 0.018 (95% 0.011-0.030)** (9 reader + 6 crop-region misses; reader errors alone 9/813 = 0.011); 0.034 if all 13 U were ours;
- Bourdeau's fr.2988 read **29/817 = 0.035 (0.025-0.051)**, of which 21 are the s/g labels; 8/817 = 0.010 (0.005-0.019) without
  them; 0.051 if all 13 U were his;
- copy variants 13/813 = 0.016 per token (genuine scribal differences between the two copies, not reader error);
- single blind passes vs the settled read: A 100/806 = 0.124, B 72/806 = 0.089, C (f.73v only) 9/298 = 0.030. These favour
  the passes (the settled read inherits every token the passes agreed on, and C is the preferred f.73v pass), and A/B include
  the band-crop clipping losses; the line-crop passes are the fair single-pass figure.
All error figures are lower bounds: a sign both readers misread the same way in both copies is invisible. TRANSCRIPTION.md
terms: **err_2reader** 0.05-0.10 per page (above); **err_true not measurable** (no benchmark item of this hand); the
two-witness settled figure 0.018 (reader-only 0.011) stands in for it with that caveat, N = 813.
BENCHMARK-TX: no row added -- the settled read was built from these same passes, so it cannot score them; a future pipeline
on the Ranzo hand could use the positions where `fr3019_no27_settled.tsv` and Bourdeau agree (two copies, two readers) as a
dev item (suggestion).
Grades: no reading, no key; H 0, C 0. Cost units: 7 Sonnet transcription calls + 12 tile sheets read by this worker (1
reconciliation unit beyond plan, as two calls were redone).
Requests: gallica.bnf.fr 16 (3+2 overviews, 2 info.json, 5 native regions, 1 HTTP 500 not retried, 2 resets on first try
re-sent once each; 1 left-margin strip), github.com 1 sparse clone.

## s/g relabel and pooled-annealer re-run (A1B-RANZO-SG, LANE-A1B account 1, 3 Oct 2026)

**Pre-registration (written and pushed 3 Oct 2026 17:2x UTC, before any annealer run on relabelled data).**
Instrument: Bourdeau's word-substitution annealer `targets/vasto1527/n20/solve2.py` (github.com/dbourdeau/cyphersolver
a439937, D. Bourdeau, MIT), run unmodified except two injected patches applied by `sg_run.py` (token-file path; control
flip injection). Corpus deviation, stated before running: his `ita/cast_fixed.txt` is rebuilt with his own `ita/prep.py` from
the two archive.org Castiglione texts he names (bub_gb_CbcpV2IS7C8C, bub_gb_laRnTtJmsDAC); his Wikisource Guicciardini/
Machiavelli file (`guicc.txt`, ~hundreds of Wikisource calls) is replaced by `tools/data/it16` (16th-c. Italian letters, 367k
words), so absolute numbers are ours, not his; his reported control is ~46% token accuracy. Pooled target: his `all_tokens.txt`
does not match his current n20 files token-for-token (an earlier build), so the pooled corpus is rebuilt from his current
files by load.py's rules (`relabel_sg.py --n20`): T0 his labels, T1 = 22 settled s/g rows (21 c007 g->s, c006 s1->g1),
T2 = T1 + the 7 other settled Bourdeau reader errors (b->h etc., folio number dropped). 3,929 tokens.
Runs: ITER 1,000,000, seeds 1-6 for every arm; T0 also seeds 7-12 (noise reference).
- Control arms (held-out Castiglione 3,900 words, his encoding): C0 clean (his control, a reproduction); C1 flip-matched:
  every s-code token in the control positions matching c007's place in the pooled order relabelled g (rate 1.0, as 21/21
  settled); C2 = C1 + positions matching c018 and c020 at rates 0.5 and 0.8 (file-level counts hypothesis, see below).
  The relabel "matters to this annealer" only if mean token accuracy C0 - C1 > 2 x SE of the difference (6 seeds each).
  Note rule 3 orthogonality: C0 cannot vary with the relabel (synthetic codes, no s/g labels); C1/C2 are the arms that can.
- Target: per arm, the stable skeleton = types assigned the same word on >= 5 of 6 seeds. **Movement** iff
  |stable(T1) - stable(T0 seeds 1-6)| > |stable(T0 seeds 1-6) - stable(T0 seeds 7-12)| + 2, same for T2. Anything less is
  "no movement" (a relabel within the annealer's own seed noise). No reading is claimed either way; content words are not
  expected (his control's ~9% type accuracy).
- c017-c020 check (script, before any vision): s/g label counts per Bourdeau file, s share of tokens: c006 0.110 (s 47, g 3),
  c007 0.005 (s 2, g 33), c017 0.103 (51/7), c018 0.045 (23/23), c019 0.117 (60/8), c020 0.019 (5/14); no.20 files
  0.07-0.16 with g 1-7. So c018 and c020 look flipped wholly or partly, c017/c019 do not -- a counts hypothesis only,
  settled (or not) by the image look below.

**c017-c020 image check (after the pre-registration, before reading any run).** Crops (scratch first, the five used copied to
`images/fr2988_sg/` with manifest): `python3 tools/iiif_lines.py --ark btv1b9059908w --canvas 20 --region 900,150,3300,1250
--out <scratch>/crops --prefix v20 --debug` and the same with `--canvas 18 --prefix v18` (Gallica view = canvas number; view 20
= Bourdeau c020, view 18 = c018; first band is the line above his line 1). Read by this worker, own looks (5 crops), no blind
subagent: the brief's 4 blind calls were not spent, to stay inside the cap -- grade M, one reader, labels seen. Result:
- view 20 (c020): his g7, g346 (line 1), g327 (line 2) are all the compact closed 8 -- the s form settled by A1B-RANZO-2WIT.
- view 18 (c018): his g44 (line 4) is the compact 8; his s153 (line 3) is a third form, a tall long-s, correctly labelled s.
  So c018 mixes tall s (labelled s) and compact 8 (labelled g): the 23/23 split is consistent with that.
- 4 of 4 sampled "g" labels on c018/c020 are the s-form compact 8; no open-bowl g was found in the sampled crops (not looked
  for exhaustively). c017 and c019 (s share 0.103, 0.117) were not viewed: counts only.
So the flip is not confined to c007: c018 and c020 carry it too (sample, M). Their full relabel needs every g token on those
two pages checked (about 37 tokens, image), not done here; arm C2 prices its effect on the control.
