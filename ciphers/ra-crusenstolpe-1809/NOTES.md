# ra-crusenstolpe-1809

Status: open

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
- S: run the still-untried 'standard Swedish 1809 historiography' search (Odhner, Hjärne, Almqvist) named in the verdict but never actually run.
- S: retry Project Runeberg for a listing of Crusenstolpe's Portefeuille parts 1-4 (1837-44) under a different work id than the 1840/1845 volume already checked.

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
