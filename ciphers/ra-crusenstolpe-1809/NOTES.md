# ra-crusenstolpe-1809

Status: open

Editions searched for a printed copy (2 Oct 2026, full-text search of the Project Runeberg OCR for chiff/dechiff/
spion/nyckel/Crusenstolpe/Ericsberg/1809): Crusenstolpe, *Portefeuille* Del 1-5 (1837-45; `portef`, pp. 1-end of all
five volumes, 1809 items at Del 1 pp. 207-17 and Del 3 pp. 134-88, both clear text), Clason and af Petersens, *För
hundra år sen* (1909; `cs100`, scans 0019-0270) and Crusenstolpe, *1720, 1772, 1809* (1836; `cmj1720`): no 1809 spy
report, cipher document or decipherment printed. Detail in the OPEN and Premise check sections below.

## What this is

Spy reports and cipher documents concerning the 1809 revolution (the coup against Gustav IV Adolf), held among
the papers of Magnus Jakob Crusenstolpe (1795-1865). Riksarkivet i Stockholm/Täby, Ericsbergsarkivet, "Smärre
enskilda arkiv och arkivfragment / Crusenstolpe-papper", reference code `SE/RA/720266/03/08/~/2,5`. Catalogue
note (verbatim): "Ink brev och skrivelser, diverse utkast och anteckningar m m. Spionrapporter, chiffer
handlingar rörande revolutionen 1809." Crusenstolpe was 14 in 1809 and a well-known later writer/censor/
politician; the note describes material *about* 1809 gathered in his papers, not necessarily material *by* him,
and does not attribute authorship of the cipher documents themselves. QUEUE.md row R6.

No transcription exists anywhere the searches below reached; `ciphertext.txt` is not created.

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `"Crusenstolpe 1809 revolutionen chiffer spionrapporter Riksarkivet"`. Hits: Crusenstolpe's
   Svenskt Biografiskt Lexikon entries, the Ericsberg-palace/Ericsbergsarkivet Wikipedia and Nättidningen Svensk
   Historia pages, a Historisk tidskrift PDF on "märkesåret 1809", and the English Wikipedia "Coup of 1809"
   article. All confirm Crusenstolpe was "one of the most active forces in Gustav IV Adolf's deposition in
   1809" (his biographical fact, already well known) but none names or quotes this specific bundle of spy
   reports or cipher documents. Not found.
2. **Print — Crusenstolpe's own published works.** Crusenstolpe's own document collection "Portefeuille,
   utgifven af författaren till Skildringar ur det inre af dagens historia" (parts 1-4, 1837-1844, plus
   "Portefeuille, belysande det inre af tidernas historia", 1840) is a printed primary-source collection, full
   text on Project Runeberg (`runeberg.org/portef/`). It was not read cover-to-cover this pass — that is an
   edition-search job for a solver/verifier, not this check-solved sweep — but its existence is recorded as the
   standing candidate for a facing-page/interlinear check if this target is ever promoted: whether the specific
   cipher documents in `SE/RA/720266/03/08/~/2,5` were themselves printed (deciphered or in cipher) in
   Portefeuille is unresolved and flagged as a next step, not closed either way.
3. **Print — Swedish 1809 historiography.** Not separately searched by name (Odhner, Hjärne, Almqvist, etc.) —
   out of scope for a check-solved pass's budget; flagged as the same open next step as (2), one edition search,
   not run here.
4. **Lists.** `sources/cryptiana/` grepped for `crusenstolpe|1809`: no relevant hits (a `1809`-adjacent false
   positive in an unrelated file was checked and is not about this item). Live community-list sites not
   separately fetched (same reasoning as ra-morner-welin: the local snapshot is the productive check and
   returned nothing for a name this specific).
5. **DECODE.** `sources/decode/` grepped for `crusenstolpe`: no hits. Live de-crypt.org not queried this pass.
6. **Bourdeau/Aymeloglu.** Same fresh shallow clones as ra-morner-welin. `grep -n -i "crusenstolpe"` against both
   repos' `README.md`/`TARGETS.md`/`SOLVED_CATALOGUE.md`/`SHORTLIST.md`/`CATALOGUE.md`: no matches. A
   repo-wide grep for "1809" alone returned only unrelated numeric/data-file false positives (napoleon-era
   digit files, glyph-segmentation JSON, etc.), none naming Crusenstolpe or this shelfmark. Not found.

**Riksarkivet digitisation check** (`data.riksarkivet.se/api/records`, `text=Crusenstolpe chiffer`, one request):
confirms the record at `SE/RA/720266/03/08/~/2,5` with `"onlyDigitisedMaterials":false` and reproduces the
catalogue note above verbatim. Not digitised.

## Verdict

**Open.** No source located a solution, key, plaintext, transcription or documented attempt specific to this
item. Unlike ra-morner-welin, this row carries a real, unclosed edition risk: Crusenstolpe's own printed
Portefeuille collection and the general Swedish 1809-coup historiography have not been searched for this
material, only judged out of scope for this pass's budget. **Before any campaign or promotion past stage 2, run
that edition search** (Portefeuille full text on runeberg.org, plus a named search of the standard 1809
historiography) — this is exactly the Raince/Thurloe-lesson gap the brief and CLAUDE.md rule 1 warn about, left
open rather than silently closed.

Copy-order (not digitised). REQUEST.md below drafts the Riksarkivet reading-room request.

Requests this pass: data.riksarkivet.se 1, WebSearch 1, github.com clones shared with the batch (grepped only),
sources/cryptiana and sources/decode local grep only. No Google Books, no TNA, no DECODE login.

## NX-UNBLOCK (26 Sept 2026)

Ran the edition search this row's own verdict named as the open next step (Crusenstolpe's own "Portefeuille,
belysande det inre af tidernas historia," 1840/1845). Free routes tried:
- **Google Books API** (`&country=US&key=$GOOGLE_BOOKS_KEY`): confirms the 1845 printing exists as a catalogue
  entry but `viewability: NO_PAGES` -- no snippet, no full text.
- **archive.org** `advancedsearch.php`: 0 hits for "Crusenstolpe Portefeuille". Not digitised there.
- **Project Runeberg** (runeberg.org): has an author-id page reserved for Crusenstolpe (`authors/crusenmj.html`)
  but no book listed under it, and the site's own full-text search (`search.pl`) redirects to a Google
  site-restricted search that returns a JS/consent challenge page to curl, not usable from this pass's tools.
- **Litteraturbanken.se**: author page loads (HTTP 200) but is JS-rendered; no "chiffer"/"1809"/"Portefeuille"
  text found in the raw HTML this pass -- would need a browser-tool fetch, not tried (time budget).

No free full text of Portefeuille found this pass. The "standard 1809 historiography" half of the named next
step (a named search of general coup historiography) was not attempted either, for the same reason. This edition
risk stays open, unclosed. REQUEST.md (Riksarkivet reading-room copy order) stands unchanged.

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Crusenstolpe" AND 1809 AND chiffer`: no relevant hit (0 results, none about the letter).
- `"spionrapporter" AND "revolutionen 1809" AND Ericsberg`: no relevant hit (0 results, none about the letter).

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: a Riksarkivet reading-room copy order for `SE/RA/720266/03/08/~/2,5` (REQUEST.md, since 24 Sept
2026).

- M: fetch Litteraturbanken.se's Crusenstolpe author page via a real browser (JS-rendered, not tried) and search for 'chiffer'/'1809'/'Portefeuille' -- tools/browser_fetch.js, this file's own named next step.
- [x] S: 'standard Swedish 1809 historiography' search (Odhner, Hjärne, Almqvist) -- run 2 Oct 2026 by OPEN-ra-crusenstolpe-1809 (web search only, 9 queries, 0 hits naming cipher material of the coup; see that section). Not run: reading Alm's 2010 Historisk tidskrift review or Carlsson 1944 / Clason 1909 themselves.
- [x] S: Project Runeberg listing of Portefeuille parts 1-4 -- run 2 Oct 2026 by OPEN-ra-crusenstolpe-1809: work id `portef`, five volumes, Del 1-4 full OCR text fetched and grepped (0 cipher documents; see that section). Del 5 (1845) not fetched, 1 request, ~USD 0.1.

## Web and blog check (WEBCHECK-ra-crusenstolpe-1809, 2 Oct 2026)

Required step of `.claude/briefs/check-solved.md` (CHECK-SOLVED-WEB, 28 Sept 2026), run 2 Oct 2026 01:05-01:20 UTC
(clock read) per brief `.claude/briefs/runs/2026-10-01-account4-webcheck.md`. Result in one line: **no decipherment or
plaintext of this item located by these queries on 2 Oct 2026** (a search result, never a novelty verdict, rule 10).
Status word unchanged.

**(a) Plain web searches** (WebSearch, 13 queries; Swedish and English):

| # | Query | Result for THIS item |
|---|---|---|
| 1 | `Crusenstolpe 1809 chiffer spionrapporter Ericsbergsarkivet` (sender/holding + date) | Riksarkivet volume list for Ericsbergsarkivet (`sok.riksarkivet.se/?postid=Arkis+463958b4-...`), SBL article 15727, Ericsbergsarkivet record `ArkisRef SE/RA/720266`, svenskhistoria.se Crusenstolpe article, en.wikipedia Crusenstolpe/Rabulist riots, redins.se antiquarian list. None names the cipher bundle or any reading. |
| 2 | `"SE/RA/720266" Crusenstolpe chiffer` (shelfmark + chiffer) | Ericsbergsarkivet record page only (1,100 volumes, Crusenstolpe-papper among the microfilmed collections); rest are bookseller/Goodreads/Wikipedia pages. No hit on `2,5` or the cipher documents. |
| 3 | `"chiffer handlingar rörande revolutionen 1809"` (catalogue note verbatim, the item's most distinctive phrase; no clear-text or decoded phrase exists since there is no transcription) | No exact-phrase hit. Partial hits are 1809-coup history pages (ukforsk.se Adlersparre page, runeberg "För hundra år sen", Historisk tidskrift 2010:1 Alm, Wikipedia Coup of 1809, svenskhistoria.se, bo-oscarsson.org, SBL Fersen). None about cipher documents. |
| 4 | `Crusenstolpe papers spy reports cipher documents 1809 revolution Riksarkivet` (folder's descriptive title, English) | SBL 15727/15726, sok.riksarkivet.se name search, Fabian Persson *Survival and Revival* PDF preview, Clements Library spy-letters exhibit (American, unrelated), Wikipedia Kryptographik. None about this bundle. |
| 5 | `chiffer 1809 revolutionen Gustav IV Adolf statskupp chifferbrev dechiffrerat` (Swedish, topic without the name) | so-rummet.se, popularhistoria.se, livrustkammaren.se, Wikipedia Coup of 1809 / Gustav IV Adolf. No cipher letter of the coup mentioned anywhere. |
| 6 | `Crusenstolpe chiffer` (Swedish, bare) | Wikipedia, SBL family article 15724, Stockholmskällan post 8706 (Abrahamsson, Crusenstolpe 1838), projekt-gutenberg.org author page, Adelsvapen genealogy. Nothing on cipher. |
| 7 | `"Crusenstolpe-papper" OR "Crusenstolpes papper" Ericsberg 1809` | SBL 15727 (three locked boxes of autographs bought by Knut Bonde for Ericsberg; 1858 Klemming sale of manuscripts to Riksarkivet "ej där bevarats som enhetlig samling"), booksellers, Nationalmuseum portrait record. No cipher content. |
| 8 | `Portefeuille Crusenstolpe 1809 chiffer dechiffrering spion rapporter Adlersparre` | `runeberg.org/portef/` (Portefeuille, utgifven af författaren till Skildringar ur det inre af dagens historia -- a live Runeberg work page, see suggestion below), SBL Adlersparre 5563, Riddarhuset Minerva, Wikipedia. No cipher content in any snippet. |
| 9 | `Crusenstolpe cipher 1809 solved Claude OR GPT OR ChatGPT` (model-solve announcement check, check-solved.md) | carter.church "Breaking the Marmont Cipher, 1809" (Napoleon to Eugène, a different 1809 letter, not Swedish, not this item); uu.se 2011 Copiale news; Wikipedia list of ciphertexts. No announcement about this item. |
| 10 | `cryptiana.web.fc2.com Swedish cipher 1809 Gustav IV Adolf` (Tomokiyo's pages, live) | Only Wikipedia/kungligaslotten.se pages on Gustav IV Adolf; no Tomokiyo page returned. |

**(b) Blog site searches** (each blog's own search, one request per query, >= 1.5 s apart):

| Blog | Query | Result |
|---|---|---|
| Cipherbrain (scienceblogs.de/klausis-krypto-kolumne) | WebSearch `site:scienceblogs.de klausis-krypto-kolumne Schweden 1809 Crusenstolpe` | Returned the 2015-04-03 post "Schwedische Literatur-Wissenschaftlerin sucht Unterstützung beim Knacken einer Verschlüsselung" and the 2013 Top-25 no. 10 Van-Gelder cryptogram post (Dutch ambassador in Turkey, Feb 1809 -- a different 1809 cipher). Both opened, see (c). |
| Cipherbrain | site search `?s=Crusenstolpe` | "Wir konnten leider keine Beiträge finden" -- no posts. |
| Cipherbrain | site search `?s=Schweden+1809` | no posts. |
| Cryptiana blog (cryptiana.blogspot.com) | WebSearch `site:cryptiana.blogspot.com Sweden 1809 Crusenstolpe cipher` | Only the forum front page and the 2018 archive page; no matching post. |
| Cryptiana blog | Blogger search `search?q=Crusenstolpe` | "No posts matching the query". |
| Cryptiana blog | Blogger search `search?q=Sweden` | 2 posts: "British Codebreakers' Keys of French Ciphers during the War of American Revolution" (2 Jan 2024) and "Update on Korean Ciphers" (23 Jul 2026, credits a Torbjörn Andersson from Sweden). Neither mentions 1809, Gustav IV Adolf, Crusenstolpe, Adlersparre or Riksarkivet. |
| Tomokiyo's pages (cryptiana.web.fc2.com) | on-disk snapshot `sources/cryptiana/` grepped for `crusenstolpe`, `gustav iv adolf`, `gustaf iv adolf`, `swed.*1809` (zero requests) | No hit. `fersen.htm` (Swedish, Axel von Fersen) has no 1809 line; `unsolved-2026-09-24.htm`'s one "1809" string is a HistoCrypt 2022 Linköping citation, unrelated. `sources/schmeh/posts` and `sources/ciphermysteries/posts` grepped the same way: no hit. |
| Cipher Mysteries (ciphermysteries.com) | WebSearch `site:ciphermysteries.com Sweden 1809 Crusenstolpe cipher` | Only Golden Dawn / Masonic / 15th-century posts; nothing Swedish. |
| Cipher Mysteries | site search `?s=Crusenstolpe` | "no results were found". |
| Cipher Mysteries | site search `?s=Gustav+IV+Adolf` | One unrelated post (Welscher Gast, 20 Mar 2020). |

**(c) Hits opened and comment threads read:**

- Cipherbrain, 3 Apr 2015, "Schwedische Literatur-Wissenschaftlerin sucht Unterstützung beim Knacken einer
  Verschlüsselung" (`scienceblogs.de/klausis-krypto-kolumne/2015/04/03/...`): about the encrypted almanacs (1800,
  1803) of the Swedish writer Clas Livijn (1781-1844), held by Ljubica Miočević, Stockholm University. Five comments,
  all 4 Apr 2015; commenter Kent reads them as monoalphabetic substitution ("var hos Baner om afton", "Atterbom var hos
  mig spelade Boston"). Neither post nor comments mention Crusenstolpe, Ericsberg, Riksarkivet, 1809, Gustav IV Adolf,
  spy reports or the coup. A different Swedish document; not this item.
- Cipherbrain, 2013 Top-25 no. 10, Van-Gelder cryptogram: Dutch ambassador in Constantinople, Feb 1809. Not Swedish,
  not this item; not opened further (the search snippet already identifies the document).
- SBL article 15727 on Crusenstolpe (`sok.riksarkivet.se/sbl/Artikel/15727`), read for "chiffer", "spion", "1809",
  "Portefeuille", archive history: no reference to chiffer, cipher or spionrapporter. Records the 1858 Klemming sale of
  his manuscript collection to Riksarkivet ("har ej där bevarats som enhetlig samling"), the Ericsberg autograph boxes,
  and the 1809 works *1720, 1772, 1809* (1836; 2nd ed. 1837) and *Revolutionen den 13 mars 1809. Åsyna vittnets
  hågkomster* (1859). No reading of any cipher document.
- svenskhistoria.se "Magnus Jacob Crusenstolpe i 1800-talets offentlighet": no mention of chiffer, spion, 1809,
  Portefeuille, Ericsberg or Riksarkivet; no reader comments.
- ukforsk.se "Adlersparre - revolutionen 1809 - regeringsformen": links to 1809 proclamations and documents; no
  chiffer/kod/spion/Crusenstolpe; no comment section.
- Riksarkivet volume list `sok.riksarkivet.se/?postid=Arkis+463958b4-f366-489a-a036-0295335516b2` (Ericsbergsarkivet,
  volumes in running-number order): served a CAPTCHA ("Verifiera att du är människa") to the fetch; not retried
  (good-citizen rule). The catalogue record itself was already read via `data.riksarkivet.se/api/records` on 24 Sept
  2026 (above), so nothing is lost; logged here as unreachable by this route.
- carter.church "Breaking the Marmont Cipher, 1809": Napoleon to Eugène, a French 1809 letter; not opened, the title
  and snippet identify a different document.

**Requests per host:** WebSearch 13; scienceblogs.de 3 (1 post, 2 site searches); cryptiana.blogspot.com 2;
ciphermysteries.com 2; sok.riksarkivet.se 2 (1 CAPTCHA, 1 SBL page read); svenskhistoria.se 1; ukforsk.se 1;
cryptiana.web.fc2.com 0 (snapshot grep). No 403/429 other than the Riksarkivet CAPTCHA noted.

Suggestion (not run, outside this brief): query 8 returned a live `runeberg.org/portef/` work page for Crusenstolpe's
Portefeuille (1837-44), where the NX-UNBLOCK pass of 26 Sept 2026 found only an empty author page -- the "While waiting"
S-item on Runeberg above may now be a one-fetch check of that page's table of contents for 1809 cipher material.

Gate re-run after this section:

```
ra-crusenstolpe-1809: open (line 52) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## OPEN-ra-crusenstolpe-1809 (2 Oct 2026, account-4)

Run 2 Oct 2026 02:45-02:5x UTC (clock read) per `.claude/briefs/runs/2026-10-02-account4-open-step.md`: the step the
WEBCHECK pass suggested at 01:08 UTC (one-fetch TOC check of `runeberg.org/portef/`) plus the two "While waiting" S
items (historiography search; Runeberg retry for Portefeuille 1-4). Intake gate before the step: `exit=0`. Status
word unchanged: **open**. Result in one line: **the 1809 cipher documents of `SE/RA/720266/03/08/~/2,5` are not
printed, in cipher or in clear, in Portefeuille Del 1-4 (1837-1844) by full-text grep of the Runeberg OCR on 2 Oct
2026, and no 1809 historiography title located by 9 web queries names cipher material of the coup** -- a search
result, never a novelty verdict (rule 10). Del 5 (1845) is unread (below).

**1. Portefeuille on Runeberg (snapshot `sources/runeberg/portef/`, manifest.tsv).** The 26 Sept pass found only an
empty author page; the work page `runeberg.org/portef/` is now live: "Portefeuille, utgifven af författaren till
Skildringar ur det inre af dagens historia", five volumes, Del 1 (1837), 2 (1841), 3 (1842), 4 (1844), Del 5 =
"Belysande det inre af tidernas historia" (1845), Libris 8213351. The subvolume index pages carry a page list only,
no article TOC, and the download page says "OCR texts (missing for this volume)" -- but the per-page HTML carries raw
OCR, and `download.pl?mode=txtzip&work=portef/<N>` returns the whole volume's OCR as one zip (route recorded in the
snapshot's NOTES.md). Fetched Del 1-4 (991 page files, 1.1 MB); Del 5 not fetched, the 15-request budget was reached.

Tables of contents (OCR of the printed Innehåll pages; 16 + 19 + 21 + 20 items). Items touching 1808-1810:

| Vol. | No. | Title (as printed) | Pages | What it is |
|---|---|---|---|---|
| 1 | XIII | Om Ryske Ministern Alopæi arrestering 1808 | 201-206 | clear documents (royal orders, Alopeus letter 1810) |
| 1 | XIV | Vestra Arméens insurrektion 1809 | 207-217 | clear: Carlstad protocols of 6-7 March 1809 (night, kl. 1; Landskansli 7 March kl. 7 e.m.), billeting orders for 2,000 men |
| 1 | XV | Baron Dübens berättelse om den 20 Juni 1810 | 218-225 | clear narrative (Fersen murder) |
| 2 | XII | Ryska invasionen på Gottland 1808 | 163-174 | clear |
| 2 | XIII, XV | Thronföljarevalet 1810 (Engeström, Silfverstolpe) | 175-214 | clear |
| 3 | XIV | Hemliga Krigsberedningens utlåtande ... krigets utbrott 1808 | 127-133 | clear |
| 3 | XV | Nya facta, förtäljde af ett ögonvittne till revolutionen i Sverige 1809 (two Afdelningar) | 134-188 | clear first-person narrative, unsigned |
| 3 | XVI | Hemlig dagorder af Napoleon (Schönbrunn, 11 July 1809) | 189-190 | clear, French |

Full-text grep of all 991 pages (pages matching, Del 1/2/3/4): `chiff` 1/1/2/0, `dechiff` 0/0/1/0, `spion` 0/1/3/1,
`nyckel` 1/0/2/0, `kunskapare` 1/0/0/0, `cipher|chifre|ziffer|hemlig skrift` 0 everywhere, `Crusenstolpe` 0/0/0/1,
`Ericsberg` 0, `1809` 14/2/4/4, `Adlersparre` 7/5/9/0. Every cipher/spy hit read in context:

- Del 1 p.194 (file 0203): Armfelt conspiracy 1793-94, "de flera i chiffer satta ställen utaf hans många bref ... till
  Fröken Rudenschöld" -- narrative mention, 1790s, no cipher text printed.
- Del 2 p.29 (0034): "I depechen den 4 Juli 1736 heter det, skrifvet med chiffer:" -- Cederhielm dispatch 1736, printed
  deciphered in clear; not 1809.
- Del 3 p.85 (0090): legation secretary in London, "om jag var spion på honom", "dechiff-rörer" (decipherers at the
  legation) -- 1780s London, narrative.
- Del 3 p.92 (0097): "Chiffren af 300,000 L. St." -- a sum in a caricature caption, not a cipher.
- Del 3 pp.138, 151 (0143, 0156), inside item XV (1809 eyewitness): "här spioneras starkt på tänkesätten bland
  ståndspersoner"; "utan att vara spion" -- clear prose about surveillance in early 1809; no cipher, no report text.
- Del 2 p.96, Del 4 p.40: 1756 and 1740s "spioner", unrelated.

So Del 1-4 print two 1809-coup items (1-XIV, 3-XV), both in clear, neither described as deciphered, and no 1809 spy
report or cipher document. Whether these two clear items are the *plaintext* of anything in the Riksarkivet bundle
cannot be tested without the bundle (no transcription exists; REQUEST.md stands); they are recorded here as the
crib candidates to carry to any future reading (grade C material if a match is ever shown, nothing graded now).
OCR caveat: unproofread Runeberg OCR ("ir." for "II.", "t809" for "1809", "S;t"), so the greps were run on stems
(`chiff`, `spion`) and the `1809` count is a floor, not an exact count; the TOC pages were read in full by eye.

**2. Historiography search (web search, 9 queries, 0 hits naming cipher material of the coup).** Queries: Odhner +
1809 + chiffer/spionrapporter; Hjärne + statshvälfningen + chifferbrev + Adlersparre; Almquist + 1809 + chiffer +
Crusenstolpe + Ericsberg; Crusenstolpe "1720, 1772, 1809" + chiffer/spion; "Revolutionen den 13 mars 1809" "åsyna
vittnets" + chiffer; Sten Carlsson / Sam Clason + chifferskrift/chifferbrev; Carlsson "Gustaf IV Adolfs fall" 1944 +
chiffer; Clason "För hundra år sen" + chiffer; "Ericsbergsarkivet" "Crusenstolpe" spionrapporter + avhandling/uppsats.
Returned pages were SBL articles (Crusenstolpe 15727, Clason 14876, Ehrenheim 16674), Wikipedia/so-rummet/
popularhistoria coup pages, Riddarhuset Minerva Adlersparre, ukforsk.se Adlersparre, Alm's "Kring märkesåret 1809"
(Historisk tidskrift 2010:1, pp. 53-64, a historiography review), Stockholmskällan post 28194 (an eyewitness account
of the king's arrest). None names cipher letters, spy reports or this shelfmark. The three standard works surfaced
are: Sten Carlsson, *Gustaf IV Adolfs fall* (Lund 1944); Sam Clason and Carl af Petersens (eds), *För hundra år sen.
Skildringar och bref från revolutionsåren 1809-1810* (Stockholm 1909; full text on Runeberg as `cs100`, 272 pp.,
three coup-day accounts plus a letter collection); Crusenstolpe's own *1720, 1772, 1809* (1836; Runeberg `cmj1720`).
None of the three was opened (Runeberg budget spent; the others are not online here). Odhner wrote on Gustaf III,
not 1809; nothing by Hjärne or Almquist on the coup surfaced in these queries.

**Next step (one):** grep the two Runeberg full texts not yet read, Clason-af Petersens `cs100` (1909, the standard
printed letter collection for 1809-10, where a deciphered spy letter would most plausibly appear) and Portefeuille
Del 5 (`portef/5`), via the same `mode=txtzip` route: 2 requests, ~USD 0.5, no vision. Then Crusenstolpe's `cmj1720`
(1 request). After that the edition risk on free full text is closed as far as Runeberg reaches, and the remaining
step is the owner-side one already filed (REQUEST.md copy order; Carlsson 1944 is in-copyright and not online).

Requests: runeberg.org 15 (all HTTP 200, 1.6 s apart, no 403/429/challenge), web search 9, no other host. Vision
calls 0. Fetched text on disk once: `sources/runeberg/portef/` (manifest.tsv, 1.2 MB).

## Premise check (GF4-BATCH2, account-4, 2-3 Oct 2026)

Adversarial pass per `.claude/briefs/check-solved.md` "Premise check" (run 2 Oct 23:58 - 3 Oct 00:0x UTC), asked to
prove the bundle's cipher documents are already read. Result first: **not found** -- no decipherment, clear copy or
printed text of the cipher documents or spy reports in `SE/RA/720266/03/08/~/2,5` located by (a)-(d) (a search
result, rule 10). Status stays `open`. The intake-gate fix this pass also made: the status line now carries the
edition citation (lines 5-9), after grepping the three Runeberg texts the OPEN section named as its next step.

**(a) Decipherments the folder mentions -- not found.** The folder mentions no decipherment of this bundle; the
catalogue note says only "chiffer handlingar". The decipherments the folder's printed sources do contain were
opened and are other items: Portefeuille Del 2 p.29, a Cederhielm dispatch of 4 July 1736 "skrifvet med chiffer",
printed in clear (OPEN section); Crusenstolpe, *1720, 1772, 1809* (1836), scan 0336, "en de-chiffrerad depêche af
år 1779, från Gustaf III till Svenska Ministern hos Hofvet i Preussen, General Zöge von Manteuffel" -- 1779, not
1809. New full-text greps this pass (Runeberg `download.pl?mode=txtzip`, snapshots in `sources/runeberg/portef/`
(Del 5 added), `sources/runeberg/cs100/`, `sources/runeberg/cmj1720/`, files matching per stem):
Portefeuille Del 5 (1845) chiff 0, dechiff 0, spion 0, nyckel 1 (a door key, scan 0040), 1809 1; Clason-af
Petersens 1909 (`cs100`) chiff 0, dechiff 0, spion 3, nyckel 1 (a chamberlain's key), 1809 71; `cmj1720` chiff 1
(the 1779 dispatch), spion 2 (1830s-style comment on "spion-systemet", political spies in general), 1809 36. No 1809
cipher document or spy-report text is printed in any of the three.

**(b) Other solvers' working files -- not found.** Fresh shallow clones of dbourdeau/cyphersolver and
aaymeloglu/unsolved-ciphers (2 Oct 2026), repo-wide case-insensitive grep for `crusenstolpe|ericsberg|720266`:
one hit, `cyphersolver/targets/lorraine1592/src/fr4.json`, a numeric false positive inside an n-gram table
(`...0720266`). No working file, key or rendering touches this item (grep only, rule 8).

**(c) Physical neighbours -- unreachable for the leaves; catalogue neighbours not cipher-flagged.** The volume is not
digitised (`onlyDigitisedMaterials: false`), so no facing page or laid-in slip can be viewed. Riksarkivet API
(`data.riksarkivet.se/api/records?text=Crusenstolpe`, 1 request after one TLS reset and a 15 s pause; 44 hits): the
sibling volumes of the Crusenstolpe papers are ~/1 (J. M. Crusenstolpe, "rättfärdigad inför efterverlden", mostly
protocol extracts), ~/2 (M. J. Crusenstolpe, drafts of justice reports 1824-25, copied news notices 1830-32,
letters), ~/3 (copies of Adlerbrant's notes, 1840s), ~/4 and ~/5 (Fredrik and Carl Denis Crusenstolpe: a Swedish
Koran translation, a memento journal 1840-41, appointment papers 1826-27); none names cipher. In the same archive's
manuscript collection two 1809 volumes sit nearby: `SE/RA/720266/05/~/33` ("1809: Berättelse om revolutionen 1809
(avskrift, 3 ex.)") and `SE/RA/720266/05/~/49` ("Några handlingar rörande revolutionen 1809. Förteckning i
bunten"); neither is cipher-flagged and neither is digitised. Recorded for a copy order alongside ~/2,5, not opened.

**(d) Recipient side -- not found for the bundle; one printed lead.** The spy reports' readers were either the
king's government or the western-army conspirators. Royal side: Clason-af Petersens 1909 prints the court accounts
(von Schoting, af Melin, von Greiff, von Hausswolff's letters); they describe police agents sent "för att utspionera"
the western army in March 1809 (cs100 scans 0028, 0032, 0071; one agent was caught at Örebro) but print no report
text. Conspirators' side: Google Books API (country=US, keyed), 5 queries: `"1809" revolutionen spionrapporter
chiffer` 0; `Adlersparre "Handlingar rörande Sveriges" 1809 chiffer` 3 (Historisk tidskrift 1903; a catalogue entry
"Handlingar rörande 1809 års Revolution", 1810, NO_PAGES); `Adlersparre 1809 "i chiffer" bref` 20, of which two are
about 1809 cipher letters: C. A. Adlersparre, *1809 och 1810. Tidsbilder* (1850, Google id jspAAAAAcAAJ, full view):
"... chiffer samt ett handbref från en schweitzare, Pollier, guvernör för prins Gustaf och f. d. drottningens
förtrogne. Allt detta lemnades i händerna på Carl XIII ..."; and Svenskt biografiskt lexikon (1864), on a man
questioned over a cipher matter, citing "ett bref, d. 15 Aug. 1809 skrifvet af konung Carl XIII till Georg
Adlersparre (C. A. Adlersparre, 1809 och 1810. Tidsbilder, Del I s. 207)". Whether these 1809 cipher letters
belong to the Crusenstolpe bundle cannot be judged from the catalogue note; they are a **lead for the folder**
(the Adlersparre print, Del I around p. 207, is the recipient-side edition to read next, from a full-view copy),
not a decipherment of this item. Its page text is served only by books.google.com (blocked from the cloud) unless a
Runeberg or archive.org copy exists; not searched further this pass.

Requests this pass: runeberg.org 3 (txtzip, all 200), data.riksarkivet.se 2 (1 TLS reset, 1 x 200), googleapis 5,
github.com 2 shallow clones (shared with the hellen pass). No 403/429/challenge. Nothing read, graded or tested.

## FT4: Adlersparre, *1809 och 1810. Tidstaflor*, Del I p.207 (3 Oct 2026, account-4)

Run 3 Oct 2026 01:06-01:10 UTC (clock read), lead (d) of the Premise check. Intake gate `exit=0`; key_livecheck
01:07 UTC: "Google Books (googleapis.com/books/v1) | yes | yes | HTTP 200". Status word unchanged: **open**.
Result in one line: **Adlersparre prints no cipher text, key or plaintext of any 1809 cipher document; p.207 is a
clear letter, and the one cipher item he mentions (Del 3 p.127) is described, not printed** -- a search result,
rule 10. Nothing to test, so no matched control was run (rule 3 needs a key or ciphertext; neither exists).

**Route.** Google Books API (keyed, `country=US`): volume `jspAAAAAcAAJ` = *1809 och 1810. Tidstaflor*, 1850, 267
pp., `ALL_PAGES`, public domain; 6 snippet queries (`Pollier chiffer Carl XIII`; `Adlersparre "1809 och 1810"
chiffer`; `Pollier handbref schweitzare`; `"befallte" "brefvets egare" Adlersparre`; `"afhöres han ej vidare"
chiffer`; `Adlersparre 1809 tidstaflor "i chiffer"`; plus 2 with 0 hits). The API's PDF download link
(books.google.com) answered HTTP 429 (captcha page), once, not retried. A web search then found the full OCR on
Project Runeberg, work `acatidstav` (all five Delar); Del 1-3 fetched with the `mode=txtzip` route, snapshot in
`sources/runeberg/acatidstav/` (manifest.tsv). No LOCAL-QUEUE row needed.

**What Del I p.207 says.** Letters of Carl XIII to Georg Adlersparre, ending on p.207 and continuing to p.208:
(i) the tail of a letter about the Augustenburg succession, with a warning that "statsrådet Platen sagt mig i dag,
att en viss landt-råd Manderfelt skulle utgifva sig för ett hemligt sändebud från mig till Norge, hvilket är en
stor osanning ... som han varit dömd här för uppenbar tjufnad"; (ii) "Stockholm den 15 Augusti" [1809], thanking
Adlersparre for Prince Christian August's answer and planning the Danish peace talks at Jönköping. All clear text,
no cipher, no key. The 1864 *Biographiskt lexikon* entry citing "Del. I s. 207" for a man "afhöres han ej vidare"
in a cipher matter is about this Manderfelt affair (Carl Manderfelt, called Ingman; also Del 1 p.189, Del 3 p.17);
the cipher side of that affair is not printed on p.207 or anywhere in Del 1 (`chif` 0 pages).

**The "chiffer ... Pollier" snippet** is Del 3 pp.126-127, not Del I: after Crown Prince Carl August's death (May
1810), police in a Scanian port took from a former court lackey, just over from Lübeck, a packet addressed to a
Stockholm official containing a German proclamation to the Swedish army, "en pro memoria skrifven med chiffer" and a
letter from Pollier, governor of Prince Gustaf; Carl XIII confronted the addressee (unnamed) and buried the matter.
Described only; no cipher text, key or decipherment printed. It is 1810 and Gustavian, so not obviously the
"revolutionen 1809" material of `~/2,5`, though it could be among Crusenstolpe's papers.

**Greps** (OCR pages matching, Del 1/2/3; 239/290/267 pages): `chif` 0/1/3 (Del 2 p.104 and Del 3 pp.190, 192 are
"namnchiffer", monograms; Del 3 p.127 above), `spion` 2/2/2 (all narrative; Del 3 p.61 "Spionrapporter" about
Saumarez's fleet provisioning in western ports, 1810, no report text), `nyckel` 0/1/3 (door/ammunition keys),
`Crusenstolpe` 0/0/1 (Del 3 p.116, "Vice landssekreteraren C--e (Crusenstolpe?)", 1810 narrative). Del 4-5 not
fetched (2 requests, about USD 0.2, if a later pass wants the whole work closed).

**Lead for the copy order:** two items to name alongside `~/2,5` when REQUEST.md is sent: the 1810 Pollier packet
(the cipher pro memoria) and the Manderfelt cipher matter of Aug 1809. The bundle's own leaves decide whether
either is in it.

Requests: googleapis.com 9 (all 200), books.google.com 1 (429, stopped), archive.org 1 (advancedsearch, no copy of
this title), runeberg.org 3 (200), WebSearch 1. No vision. Nothing read, graded or tested.

## R12-CRUSLB: Litteraturbanken.se works and full-text search (6 Oct 2026, account-2 worker)

Run 6 Oct 2026 11:20-11:25 UTC (clock read). Intake gate `exit=0` (open, line 3). Status word unchanged: **open**.
Closes the "JS-rendered, browser-tool fetch not tried" gap of NX-UNBLOCK above: no browser needed, the site's own JSON API
(`litteraturbanken.se/api`, OpenAPI at `/api/openapi.json`) answers curl. Raw responses in `passes/lb/`.

**Works held (author id `CrusenstolpeMJ`, `list_all/etext,faksimil,pdf/CrusenstolpeMJ`, 21 records):** *Morianen* (etext + faksimil,
parts 1-6), *Huset Tessin* (faksimil, parts 1-5), *Carl Johan och svenskarne* (parts 1, 2, 3 in two halves), *Året 1772*
(play), *Tvenne äktenskap*, *Bigtfadren*, *Kollerstad*, *Vedergällningsrätten*, *Första fjetet på skriftställarebanan*.
**Not held:** *Portefeuille* (Del 1-5) and *1720, 1772, 1809* (1836): the edition risk named in the Verdict is not closed by
this host; those two stay on Project Runeberg (searched 2 Oct 2026, OPEN section).

**Full-text queries** (`search_count/<q>?authors=CrusenstolpeMJ`; hits = works, then fragments read via `search/`):
`chiffer` 6 works/12 fragments; `chiffre` 4/6; `Portefeuille` 10/51; `1809` 13/209; `spion` 2/3; `spionrapport` 0;
`chifferskrift` 0; `nyckel` 16/85 (keys of doors etc., not read).
Fragments of `chiffer`/`chiffre`, read: Morianen 6 (Gustaf III's monogram "chiffer" on an inscription: monogram sense);
Morianen 4 ("en hemlig statsskrift i chiffer" from the Swedish envoy at Stanislaus; an author's note that the numeric "chiffrer"
were let in at random, "Den sista chiffren 9174 betyder Ryssland" -- a fictional/period 18th-c. code gloss, Holstein-Gottorp
era); Morianen 5 and 2 (a letter "på en chiffer som jag ey har"; letters in cipher from Sprengtporten, 18th c.);
Huset Tessin 1 ("svårare att utfundera än chiffer"); Huset Tessin 2-4 (French "chiffre" = royal monogram, once "en chiffre"
as an advice on a message); Carl Johan och svenskarne 3 ("Sekreterare i färdigheten att tyda chiffer?" followed by a note
citing a newspaper). `spion`: two spy mentions in Carl Johan och svenskarne 1-2, narrative. `Portefeuille` fragments are the
author's footnotes citing his own Del 1-3 (Del 1 p.103 and sid. 329 etc.), i.e. pointers to a work we already searched on Runeberg.
**None is an 1809 spy report, a ciphertext, a key or a decipherment of the Ericsbergsarkivet bundle.** These are novels and
history-novels of the 1840s; the numeric-code gloss in Morianen 4 is a different (18th-century) matter. A search result,
rule 10; not read: the 1809 fragments (209 in 13 works) beyond counts, since they are narrative of the coup and no query
tied them to cipher material. A reader who wants them can run `search/1809?authors=CrusenstolpeMJ`.
No cipher text exists in these results, so no key, no control and no grading (rule 3/4 not engaged).

**Updated While waiting / Verdict:** Litteraturbanken parallel action done; it adds no printed 1809 cipher document. The open
edition risk is unchanged (Portefeuille and 1720-1772-1809 are not on this host; Runeberg pass of 2 Oct stands). Next step
remains the Riksarkivet copy order (REQUEST.md), naming the Manderfelt (Aug 1809) and Pollier (1810) leads from FT4.

Requests: litteraturbanken.se 24 (curl, 2 s apart, all HTTP 200 except 3 early 404/422 probes of wrong parameter names).
No browser, no vision, no credentials.
