# Beltrame Costabili (Esztergom) to Eleonora d'Aragona, 20 March 1492, State Archives of Modena, Amb. Ung. b.2/21 no.8

**Status: found-solved** (account-3 orchestrator, 3 Oct 2026 01:0x UTC, from A2-COS's identity check e7eade5f: R1168 = Berzeviczy 1914 no. CLV, printed in clear; the record itself holds a period interlinear decipherment and a clear Exemplum, f.13. Was: partial per DECODE's own status field.) Remaining optional step: period key by alignment to f.13 (A2-COS2, grade C).
Berzeviczy, *Acta vitam Beatricis reginae Hungariae illustrantia* (MHH Diplomataria 39, 1914), no. CLV, pp. 216-219, read by this worker (GF-A2-10, 3 Oct 2026): prints a Costabili letter to the Duchess of Ferrara, Strigonii XX Martii 1492 (postscript XXIII Martii), from the Modena state archive, headed "Titkos írásjegyekkel írva" (written in secret characters), in clear Italian -- see "## Premise check" below.

## Item

DECODE R1168. Metadata (Aymeloglu `decode-records.jsonl`): author Beltrame Costabili, receiver Eleonora
d'Aragona (Duchess of Ferrara, Modena and Reggio, consort of Ercole I d'Este), origin Esztergom, Hungary,
20 March 1492, 4 pages, cleartext Italian, cipher type "Homophonic or simple substitution", symbol set
graphic signs. **DECODE's own `Status` field for this record is "Partially decrypted", not "Non-decrypted".**

QUEUE.md row **DC10** placed this in the "DECODE non-decrypted records with images" section (which pools both
Non-decrypted and Partially-decrypted rows from the underlying crawl, per `sources/decode/NOTES.md`'s "What
was fetched" section) and scored it `held_by: none`, next step "transcription", framed only by its membership
in the same Este/Sforza envoy-report cluster as R1162 (an attached-`[transc]` record, DC4, handled by another
worker this session). The "partially decrypted" status itself was not surfaced or acted on at the ranking
stage.

Brief: `.claude/briefs/runs/2026-09-24-lane-n-csDC2.md`. de-crypt.org and archive.org not queried directly by
this worker (held by other LANE N workers this session); this verdict rests on the census-diff TSV's own
`status` column plus two WebSearches and a check of the local Cryptiana snapshot, since DocumentsList (the
DECODE page that would show what, if anything, is attached as a partial reading) could not be checked under
this brief's host restrictions.

## Check-solved sweep, 24 September 2026

- **Editions first.** Este ambassador editions for Hungary in this period (the brief names these for the
  Ferrara/Modena 1492 cluster): not located or checked this pass. Two WebSearches
  (`Beltrame Costabili Eleonora d'Aragona 1492 cifra Modena ambasciatori Ungheria`; `"Costabili" Modena
  archivio cifrario Ungheria 1492 decifrato`) surfaced general context (Costabili was one of several agents
  reporting from Hungary to the Este court in this period; a 26 Sept 1489 letter of his from Buda is
  documented) and a general Modena-archive page on "Lettere e cifrari" at the Este court, but **no specific
  mention of this letter (20 March 1492) or its cipher, solved or not**, and no confirmation either way.
- **Web / lists (Cryptiana).** No page in the local `sources/cryptiana/` snapshot mentions "Costabili",
  "Eleonora" (in this Hungarian-ambassador sense) or this shelfmark (checked by grep across `web/`, `blog/`,
  `PAPERS.tsv`, `READABLE.tsv`); not separately searched live beyond the two WebSearches above.
- **Bourdeau (github.com/dbourdeau/cyphersolver).** No file matches "Costabili", "b.2/21" or "R1168"
  specifically (broad substring greps on "1168" alone returned only unrelated false positives — numeric
  substrings inside unrelated JSON/TSV files, checked and dismissed). The repo's Este/Sforza-cluster work
  (`sadoleto1482/`, `buda1489/`) covers a different correspondent (Nicolo Sadoleto) and different box
  (Ambasciatori b.1/9), not b.2/21.
- **Aymeloglu (github.com/aaymeloglu/unsolved-ciphers).** R1168 appears in `catalogue/decode-ranked.md`,
  `decode-records.jsonl` and `decode-catalog.csv` — raw catalogue-harvest presence only, matching this
  project's own census-diff finding; no independent write-up or attempt found.
- **DECODE.** Not queried live (per brief). The census diff's own `status` column, already committed to this
  repo (`records-non-decrypted-2026-09-24-diff.tsv`), reads **"Partially decrypted"** for id 1168 — this is
  DECODE's own catalogue signal that some prior work exists on this record (a partial key, a partial reading,
  or a partially-completed transcription attached via DocumentsList), which none of this pass's other five
  sources independently corroborated or could explain further. This is the single most important fact this
  check-solved pass surfaced and it was not checked by anyone assembling QUEUE.md's DC10 row.

**Verdict: partial**, called directly from DECODE's own status field, not independently confirmed. This is
**not** the same as "open" and this record should not be nominated to the board as an open cryptanalysis or
recovery lead until a worker with DECODE access (a) confirms what "Partially decrypted" refers to via
DocumentsList / RecordsView, and (b) reports what portion is already read and by whom. No novelty claim made
(rule 10).

## Correction to QUEUE.md

DC10 (and, by the same logic, any other row in that section whose underlying `status` column in
`records-non-decrypted-2026-09-24-diff.tsv` reads "Partially decrypted" rather than "Non-decrypted") should
carry an explicit flag distinguishing the two statuses; the ranking pass pooled them without surfacing which
rows already carry DECODE's own partial-work signal. Flagged in ROOM.md, 24 Sept 2026, for the LANE N
orchestrator to re-check the rest of the DC1-DC20 list against the `status` column for the same issue.

## Web and blog check (GF-A2-10, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `Beltrame Costabili Eleonora d'Aragona 1492 Esztergom cifra` -- hits: Verbum (PPKE) articles on the Este court in
   Esztergom (Domokos 2022 on Taddeo Lardi, ojs.ppke.hu/verbum/article/download/188/171/195, opened: grep for 1492 /
   cifr / marzo finds no discussion of this letter), Kuffart's academia.edu list (not opened: academia.edu 403s from
   the cloud), mnl.gov.hu account-book pages. No mention of the 20 March 1492 letter's cipher.
2. `"Costabili" Ambasciatori Ungheria busta 2 Modena 1492 cifra decifrata` -- ASMo finding-aid PDFs (Germania,
   Bologna, Firenze) and Verbum articles; nothing on this letter.
3. `DECODE record 1168 Costabili Modena partially decrypted` -- only the DECODE v2 HistoCrypt papers; no record-level page.
4. `Berzeviczy Aragóniai Beatrix okiratok Costabili 1492 jelentés` -- led to real-eod.mtak.hu/2850 (Berzeviczy 1914,
   full PDF), opened and grepped: **hit**, see Premise check (d).
5. `"Amb. Ung." Modena Costabili 1492 cipher letter Beatrix deciphered` -- general press on Spanish and Modena
   ciphers, Voynich Ninja threads; nothing on this letter.

Blog site searches:
- Cipherbrain (`site:scienceblogs.de klausis-krypto-kolumne Costabili OR Esztergom 1492 Modena`): one blog hit,
  2017/03/24 "who can solve this encrypted text from the 16th century" -- a 16th-century Spinelli letter, not this
  item (its thread was read for spinelli-beinecke-c1515). Nothing on Costabili.
- Cryptiana blog (`site:cryptiana.blogspot.com Costabili OR Ferrara Hungary 1492 cipher`): no blog page returned;
  the local Tomokiyo snapshot (`sources/cryptiana/`) has no "Costabili" (grep, this session).
- Cipher Mysteries (`site:ciphermysteries.com Costabili OR "Eleonora d'Aragona" OR Esztergom cipher`): three
  ciphermysteries.com pages returned (?p=34, 2008/01/11, category page 134), all Voynich/general, none on this item.
No comment thread found that discusses this letter. Result of the web/blog step: no decipherment found on the web or
in the three blogs; the printed clear text was found through the edition search (below).

## Premise check (GF-A2-10, 3 Oct 2026)

(a) Folder's own mentions -- **found (signal)**: this NOTES.md already records DECODE's own status "Partially
decrypted" for R1168 (from the census diff), never opened. DECODE was not logged into this pass (brief: no login
needed for a gate fix), so what is attached to R1168 is still unknown.
(b) Other solvers' working files -- not found for this letter. Shallow clones 3 Oct 2026: dbourdeau/cyphersolver
(HEAD 2341682, 2 Oct): `research/oldest/CANDIDATES.md` B2 lists "Beltrame Costabili, Esztergom 1491-93 (R1162-R1168,
R1095-R1097)", "Partially decrypted", "sibling letters in the same buste are 'Decrypted' (keys and cribs)", and
"Valentini and Costabili not checked"; `targets/buda1489/vestigia/search_rows.json` carries 25 Vestigia rows for
Costabili's 1492 letters (nos. 4-7 dated 7 and 19 March, 16a/18a 3 May, 33, 38) but **no row for no. 8**, and no
rendering or key applied to it. aaymeloglu/unsolved-ciphers (HEAD d2800bb, 27 Sept): R1168 only in the catalogue
harvest (`catalogue/decode-records.jsonl` line 728), no working file (cited, not copied).
(c) Physical neighbours -- **found (in print)**: the leaf before, b.2 no. 6/7 (Vestigia 3014/3015, 19 March 1492,
incipit "Havendo inteso quanto me scripse vostra excellentia ... circa il mandato"), is Berzeviczy no. CLIV pp. 214-216,
in clear (not cipher). Images not viewed this pass (DECODE images are login-gated; the Vestigia viewer not opened).
(d) Recipient's side / documentary edition -- **FOUND**: Berzeviczy Albert (ed.), *Acta vitam Beatricis reginae
Hungariae illustrantia / Aragoniai Beatrix magyar királyné életére vonatkozó okiratok*, Monumenta Hungariae Historica,
Diplomataria 39 (Budapest 1914), full PDF at http://real-eod.mtak.hu/2850/1/1_MHHD_Okmanytarak_Diplomataria_39.pdf,
fetched and grepped 3 Oct 2026. Contents entry: "CLV. 1492. márczius 20., 22. Beltramo Costabili jelentése a ferrarai
herczegnéhez Esztergomból, melyben Beatrix helyzetét s az országgyűlés alkalmából Budára menetelét írja le" (p. 216).
Document head: "Titkos írásjegyekkel írva, Modenái áll. levéltár, előbb id. osztály" (written in secret characters;
Modena State Archive, section cited for CLIV: Canc. Duc., Disp. d. Orat. Est. dall' Ungheria). Text printed in full in
Italian, pp. 216-219, incipit "Dopo mie humili raccomandationi et per altre mie V. Ex.tia a questa hora può havere
inteso come le cose de la Regina furono differite ala futura dièta", dated "Strigonii, XX. Martii, 1492", with a
postscript "Strigonii, XXIII. Martii, 1492" ("Ho inteso a bocha che heri S. M.tà intrò in Buda"). Gist: the Queen's
(Beatrix's) marriage business was put off to the next Diet; the Neapolitan ambassador has had only good words at Buda;
Beatrix resolved to go to Buda in person, the King sent his chamberlain and then a letter in his own hand protesting
against it; the Bishop of Győr (royal secretary) blamed the King's obstinacy on "that other wife"; Beatrix went and
lodged at Old Buda. Match to R1168 (sender, recipient, place, 20 March 1492, cipher, Modena) is by catalogue data,
not by image or incipit: not yet confirmed that R1168 is this despatch rather than a duplicate. Berzeviczy does not say
whether he printed from a contemporary decipherment or deciphered it himself.

Consequence: a clear text of this letter is in print (1914). Flagged to the account-3 orchestrator in ROOM.md as a
found-solved candidate; status line left to the orchestrator (brief). Next step if kept: confirm R1168 = Berzeviczy
CLV from the DECODE images or the Vestigia record for b.2 no. 8, ~USD 1.

## Intake gate (A2-COS, 3 Oct 2026, 00:42 UTC)

```
$ python3 tools/intake_gate_check.py decode-1168-modena-costabili-1492
decode-1168-modena-costabili-1492: partial (line 3) -- edition/page or full-text-search citation found within 6 lines
EXIT 0
```

## Identity check from the DECODE images (A2-COS, 3 Oct 2026)

Brief: `.claude/briefs/runs/2026-10-03-acct2-a2-cos.md` (settle whether Berzeviczy no. CLV is this record's letter).

**Route.** One DECODE browser login (`tools/decode_browser_login.js 1168 <scratch> --fetch-page ImagesList,DocumentsList
--guess-fullsize --max-files 16 --delay 1800`, 00:43 UTC), logged in first time. RecordsView/1168 shows **Images 9,
Documents 0, Associated records 0**, Status "Partially decrypted", Name `SAMo_Amb_Ung_b_2_21_8`, Pages 4. Full-size PNGs
(2592x3888) were served for images 1-8 (not the forbidden.png placeholder; sha1s in `images/manifest.json`); image 9
(`IMG_R1168_I5872_P9`) was not fetched (file cap reached; one login per session, so not re-run). Committed: 1400-px JPEG
copies `images/s_IMG_*.jpg` and five crops `images/c*.jpg` (2.4 MB). Each image carries the archive's own target strip
"1492 év 03 hó 20 nap / Ambasciatori 2" (image 8: "03 hó 23 nap").

**What the record holds** (read from the images; 7 vision reads by this worker, no subagent):
- Images 1-4: the despatch itself, modern foliation **12**. A mixed letter: Italian in clear with cipher-sign groups
  (Greek-like letters, crosses, pi-shapes) inside the lines, and **a contemporary decipherment written above most cipher
  groups** (image 1: "le cosse de la Regina", "ala futura dieta", "Dieta fu facta a questi di", "Conclusioni", "de
  hungaria excusandosse", "sopra sua M.ta"; image 3: "Episcopo Janarino", "passato", "renunciato", "li beneficii",
  "frate", "se farà per ogni modo", "cardinale o consistoriale", "salvare questo loco", "per omnem eventum"). Head
  "1492 / 20 Marzo" (archival hand); incipit "Ill.ma et Ex.ma m[adam]a mia. Dopo mie humile recomendatione et per altre
  mie V. Ex.tia a questa hora può haver inteso como [le cosse de la Regina] furono differite [ala futura dieta]";
  explicit "... per omnem eventum. In gratia de la qualle de continuo me ricomando. Strig. 20 martii 1492 ... Fidelis
  servitor Bel. Cost[abi]le". Image 4 is the address leaf: "Ill.me ac Exc.me D. Dne Helyonore de Aragonia Ducisse ...
  Dne singularissime", red seal trace. **No postscript on this leaf.**
- Images 5-8: a **contemporary clear copy**, foliation **13**, headed "Exemplum literarum R[everen]di d[omi]ni
  Beltrandi ad Ill.mam d. Ducissam Ferrarie" with archival "1492 / 20 e 23 Marzo". It contains (i) the 20 March letter
  in full clear text, same incipit ("Ill.ma madama mia. Dopo mie humile Racomendatione et per altre mie V. Ex.tia a questa
  hora puole havere inteso come le cose de la Regina furono differite ala futura Dieta. Per la presente li significo come
  la Dieta fu facta a questi die et dal fine del Zenaro passato insino ad hora lo ambassatore ... se retrova in Buda per
  cavare de epse conclusione. Ma lassando le particularitade che non importano ..."), ending "mi ricomando. Strigonii 20
  martii 1492"; (ii) "Exemplum aliarum literarum p[raefati] d. Beltrami ad p[raefat]am Ill.mam D. Ducissam", a second
  letter on the peace with the King of the Romans published at the Diet in Buda, ending "Strig. 22 Martii 1492";
  (iii) "Exemplum post scripte": "Mons. suo pr[efa]to figliolo non fu ala dieta ... mandò il suo sugillo per sugillare li
  capitoli de la pace. Questa matina ho lettere da Pandolfo ... ho inteso a bocha che heri sua M.ta intrò in Buda ...
  Strigon. 23 Martii 1492".

**Comparison with Berzeviczy CLV** (PDF re-fetched from real-eod.mtak.hu/2850, pdftotext, pp. 216-219):
| feature | R1168 images | Berzeviczy CLV |
|---|---|---|
| incipit | "Dopo mie humile recomendatione et per altre mie V. Ex.tia a questa hora può haver inteso como le cosse de la Regina furono differite ala futura dieta" (f.12, gloss + clear); same on f.13 | "Dopo mie humili raccomandationi et per altre mie V. Ex tia a questa hora puö havere inteso come le cose de la Regina furono differite ala futura diéta" |
| explicit | "... cardinale o consistoriale ... salvare questo loco per omnem eventum. In gratia de la qualle de continuo me ricomando" | "... cardinale concistoriale, quantunque se differisse la publicatione, seria la via de salvare questo loco per omnem eventum. In gratia de la quale de continuo me ricommando" |
| date / place | "Strig. 20 martii 1492" (f.12), "Strigonii 20 martii 1492" (f.13) | "Strigonii, XX. Mártii, 1492" |
| signature | "Fidelis servitor Bel. Cost[abi]le" | "Bel[trando] Cosle [Costabile]" |
| episcopus | gloss "Episcopo Janarino passato ... renunciato li beneficii ... frate" | "lo episcopo Javarino passato, il quale ... habi renuntiato li beneficii, anchora non se ha facta frate" |
| postscript | only on the clear copy f.13 (image 8), dated 23 March, "ho inteso a bocha che heri sua M.ta intrò in Buda" | "Post datum ... Ho inteso a bocha che heri S. Mtá intro in Buda ... Strigonii, XXIII. Mártii, 1492" |
| address | "Ill.me ac Exc.me D. Dne Helyonore de Aragonia Ducisse ... Dne singularissime" (image 4) | "Czím: Illlustrissimae ac excellentissimae dominae, dominae Helyonorae de Aragónia, ducissae ... dominae singularissimae" |
| 22 March peace letter | on f.13 (images 6-7) | not printed in CLV (heading dates CLV "márczius 20., 22.") |

Length ratio (brief): not computed -- the leaf is mixed clear and cipher with a gloss over the cipher groups, so a
cipher-length-to-print ratio would compare unlike things; the incipit/explicit/date/signature/address/PS matches above
settle identity without it.

**Verdict (check-solved, 3 Oct 2026): found-solved.** Berzeviczy, *Acta vitam Beatricis* (MHH Dipl. 39, 1914) no. CLV,
pp. 216-219, prints the plaintext of this letter (DECODE R1168, ASMo Ambasciatori Ungheria b.2/21 no. 8, f.12) and its
23 March postscript, the PS evidently taken from the clear copy f.13 (the cipher leaf carries none). The record itself
also holds two period readings: the interlinear decipherment over the cipher groups on f.12 and the clear "Exemplum" on
f.13 -- which is presumably what DECODE's "Partially decrypted" refers to (not confirmed from DECODE: Documents 0).
Who did not know (README F-grades): **F1** -- DECODE's record carries no document and no link to the 1914 print, and
its status reads "Partially decrypted" although the images contain a full period clear copy; **F2** contribution -- no
key or mapping of these cipher signs to the print was found published (sources checked: this folder's searches, the two
solver repositories per the Premise check above). Not classified for novelty (rule 10). Key source for any reading:
`period` (gloss + Exemplum), print `published` (Berzeviczy 1914, credited).

Next step (named, not run): key recovery by aligning the clear copy / print to the cipher groups of f.12, grade C,
`tools/interlinear_align.py` -- the f.12 gloss already gives group -> word pairs, so this is alignment and transcription
of the sign groups, no cryptanalysis. Needs a sign inventory first (Usage 6: line crops via `tools/iiif_lines.py --image`,
2 passes + 1 reconciliation). Sibling interest: the same Esztergom 1492 letters R1162-R1167 (Bourdeau CANDIDATES.md B2)
may share the key.

Requests: de-crypt.org 1 login + 2 pages + 16 files (1.8 s apart); real-eod.mtak.hu 2 (HEAD + PDF). Vision reads 7.

## Remaining gaps (finish-or-blocker pass, 3 Oct 2026)
Read so far: 100% of the plaintext in print and in the period clear copy (Berzeviczy CLV; f.13 images 5-8); cipher-sign key unmeasured, 0 signs mapped
- cipher-sign key for f.12 (sign -> letter table) - blocker: not-attempted; the period gloss and the clear copy give the alignment, no key table has been built; next: sign inventory from line crops + interlinear_align.py alignment to the f.13 text, ~$6
- image 9 of 9 (IMG_R1168_I5872_P9) - blocker: not-attempted; not fetched this session (file cap, one login per session); next: fetch at the start of the key-recovery job's own login, ~$0.2

## Escalation (3 Oct 2026)
- [n/a] siblings: plaintext already complete from print and copy
- [x] clear-pages: f.13 period clear Exemplum (images 5-8) read, A2-COS 3 Oct 2026
- [n/a] known-keys: no key needed to read; plaintext already period-deciphered
- [x] print: Berzeviczy 1914 no. CLV pp. 216-219 matched to the images, A2-COS 3 Oct 2026
- [ ] key-rebuild: planned -- align f.12 cipher groups to the f.13 clear text with tools/interlinear_align.py (grade C)
- [x] image-check: DECODE full-size images 1-8 read, A2-COS 3 Oct 2026
- [n/a] retry: nothing failed that a retry would change
Verdict: keep going: 2 internal gaps; cheapest next: fetch image 9 and build the f.12 sign key by alignment to f.13 (interlinear_align.py, grade C), ~$6
