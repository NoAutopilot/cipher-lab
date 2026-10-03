blocked
GF4-BATCH16 (3 Oct 2026) could not open the edition: BAGK NF2 Bd.8 (Bierther 1982) is NO_PAGES on Google Books, so only its snippet index was searched ('Escher Kschw', 'Neuenburg Kschw Claudia', 'Ziffern Kschw Claudia': 0 hits); Ruppert, Die Kriegsereignisse im Breisgau 1632-1635 (1884, Google Books JDnaXqmSWR0C, full view) prints from Karlsruhe files but its page view is captcha-blocked from the cloud, so it was not read -- status blocked until a person reads Ruppert for 24 Jan / 23 Mar 1633.

# Two enciphered letters, Erzherzogin Claudia de' Medici to Markgraf Wilhelm von Baden-Baden — GLA Karlsruhe

QUEUE row: DA8 (sources/solver-diffs/2026-09-24-lane-n2-dea.tsv, "German state archives, online finding aids
(LANE N2 scout of 24 September 2026)").

## Source

Generallandesarchiv Karlsruhe (LABW), Bestand 81:
- **81 Nr. 442** (cross-referenced as 46 Nr. 2916), 24 Jan 1633: "Chiffriertes Schreiben der Erzherzogin Claudia
  de Medici an Markgraf Wilhelm von Baden-Baden über die Eroberung der Stadt Neuenburg und die Entsendung des
  Obersts Hans Werner Escher von Binningen an den Grafen Johann von Aldringen." 1 Stück.
- **81 Nr. 813**, 23 März 1633: "Schreiben der Erzherzogin Claudia de Medici an Markgraf Wilhelm von Baden-Baden
  mit Übersendung von 15.000 Gulden zur Bezahlung der Truppen und Fortführung der Festungsarbeiten zu Breisach
  (zum Teil in Geheimschrift)." Same Bestand/Findbuch (81, "Ensisheim (Vorderösterreich u.a.): Extradita
  Colmar", internal bestand id 10853 on LABW's OFS21).

Both concern the Thirty Years' War campaign around Breisach/Neuenburg am Rhein, spring 1633 (the period between
the Swedish victory at Lützen and the Heilbronn Convention's temporary transfer of Baden-Baden to Friedrich V.
of Baden-Durlach).

## Check-solved sweep (24 September 2026)

1. **Editions.** No dedicated modern edition of Claudia de' Medici's political correspondence with the
   Baden-Baden margraves was located (WebSearch: "Claudia de Medici Markgraf Wilhelm von Baden-Baden 1633
   Neuenburg Briefe Chiffre" returns only biographical pages — LEO-BW, Deutsche Biographie, Wikipedia — none
   citing this correspondence). The Tyrol-side editions of Claudia's own letters (the Tiroler Landesarchiv's
   published Chorherren/Regesten series) were not reached this pass — flagged as an unfinished edition check,
   not a "no edition exists" claim. The general Thirty Years' War document edition *Briefe und Akten zur
   Geschichte des Dreißigjährigen Krieges* (Bayerische Akademie der Wissenschaften, ongoing since the 1870s) is
   organised around Bavarian/imperial correspondence and was not confirmed to cover the Baden-Baden margraviate
   for spring 1633; not opened this pass (its volumes are not on archive.org full text under a quick check).
   No Baden regesta for Wilhelm von Baden-Baden's chancery correspondence located.
2. **Printed decipherment / catalogue note.** LABW's finding-aid note for both items gives no indication of a
   contemporary or later decipherment ("zum Teil in Geheimschrift" on 813 describes the letter itself, not an
   attached key or gloss).
3. **Community lists.** `sources/cryptiana/` grepped for "Claudia", "Medici", "Baden-Baden", "Neuenburg",
   "Wilhelm.{0,3}Baden": no hits anywhere in the corpus.
4. **DECODE.** `sources/decode/` (NOTES.md, dc11-20-documents, florence-dieci, records-decrypted TSVs) grepped
   for the same terms: no hits.
5. **Solver repositories.** Fresh shallow clones, 24 Sept 2026 (dbourdeau/cyphersolver commit at clone time,
   aaymeloglu/unsolved-ciphers commit at clone time). No target folder named for Claudia de' Medici, Baden,
   Baden-Baden, or Neuenburg in either repo. `grep -rliE "claudia.{0,3}medici|baden-baden"` across both trees:
   zero matches outside irrelevant corpus/source text files (Napoleon-era and 1706 Bavaria material, coincidental
   word overlap only, not this correspondence).
6. **General web search.** As (1). No hit names either shelfmark, either date, or any attempt to read this
   correspondence.

**Copy status.** `www.landesarchiv-bw.de/plink/?f=4-5062086` (the finding aid's own permalink for 442) resolves
to the OFS21 struktur page for Bestand 81 (bestand id 10853) with no attached "Digitalisat" link for this
item — checked directly (24 Sept 2026), item record carries only the catalogue text, no image. 813 not
independently re-tested this pass (same Bestand/Findbuch, same finding-aid system as 442; scout's original
sweep, sources/solver-diffs/2026-09-24-lane-n2-dea.tsv, also found no digitisation link on either row).
**Copy-order.** See REQUEST.md.

**Host requests this pass:** landesarchiv-bw.de 2 (plink follow + one signature-search attempt that returned an
unrelated empty result frame, not counted as a real query), WebSearch 2, github.com 1 shallow clone each of
both repos (shared across this run's six targets).

## Verdict

**Status: open, stage 2 (verified unsolved).** No edition, catalogue gloss, community list, DECODE record, or
solver-repository entry names either letter. Both letters are copy-order (no online image resolved for either
shelfmark). Not below unicity distance a priori — political/military dispatch content, likely a nomenclator or
syllabic cipher typical of the period and region (compare DA2's Baden-Baden diplomatic cipher-key rubric, GLA
48 Nr.65/67/72, 1676-1761 — a later date range, not confirmed as the same system, but worth checking once a copy
is in hand: GLA's own Bestand 81/48 series may hold a contemporary key for this correspondent pair predating the
1676 rubric).

**Recommended next steps (not run this pass):** (1) finish the Tiroler Landesarchiv / Claudia de' Medici edition
check before any solving; (2) open *Briefe und Akten zur Geschichte des Dreißigjährigen Krieges* volumes
covering spring 1633 Upper Rhine theatre if reachable; (3) once a copy is ordered, check GLA Bestand 48 (Baden
diplomatic cipher-key rubric, DA2) for a period-matching key.

## csDA2: edition lead (24 September 2026, close-out pass)

Closing the *Briefe und Akten zur Geschichte des Dreißigjährigen Krieges* (BAGK) lead flagged above, per the
LANE N2 COMMON rule "edition not read = blocked, never open".

The spring-1633 volume for this correspondence is BAGK Neue Folge, Teil 2, Band 8 (ed. Kathrin Bierther, Munich:
Oldenbourg, 1982), covering January 1633 - May 1634 (WebSearch, 24 Sept 2026) — a modern scholarly edition
published (and still sold) by the Historische Kommission bei der Bayerischen Akademie der Wissenschaften /
De Gruyter (degruyterbrill.com/serial/bagk%2030-b), reviewed as recently as 2022 (SEHEPUNKTE) for a different
volume in the same series. Tried to read it:

- **archive.org**: `advancedsearch.php` for the series title, both with ASCII "ss" and the literal "ß"/umlaut
  encoding, and for "Briefe Akten dreissigjahrigen Krieges Wittelsbacher": 0 hits each. Not digitised there.
- **HathiTrust**: found a catalog record (catalog.hathitrust.org/Record/100423030, via WebSearch) but both
  `catalog.hathitrust.org/Record/100423030` and a `babel.hathitrust.org` full-text-search URL returned
  HTTP 403 to WebFetch (Cloudflare — the known block recorded in CLAUDE.md's access playbook; not a route this
  brief's tools can pass, no browser-tool host authorised for this pass).
- No open-access mirror found by WebSearch.

**Verdict: blocked.** The BAGK Jan/Mar 1633 volume cannot be read through this pass's authorised routes
(archive.org, HathiTrust via WebFetch, WebSearch). This is a De Gruyter-sold modern edition, not a 19th-century
public-domain scan — unlikely to surface on archive.org or open HathiTrust in a later pass either, short of a
library proxy or ILL. The nomination stays HELD, not firm, until this is read (by the person, or a worker with
library/ILL access) or is dropped as out of reach and the nomination is re-scored without it.

Host requests this pass (shared across all five csDA2 targets, see individual NOTES.md sections for per-target
detail): archive.org 6 (>=3s apart, IA slot), WebFetch 3 (2x HathiTrust, 1x this target's related landesarchiv
page — logged under nla-heinrich/hza-hohenlohe below), WebSearch ~10.

## NX-UNBLOCK (26 Sept 2026)

Tried one more free route for the BAGK Neue Folge, Teil 2, Band 8 (Bierther 1982) edition beyond csDA2's
archive.org/HathiTrust attempts: Google Books API (`&country=US&key=$GOOGLE_BOOKS_KEY`), query "Briefe und
Akten zur Geschichte des dreissigjährigen Krieges" + Bierther. The 1982 and 1997 printings both come back
`accessInfo.viewability: NO_PAGES` (no snippet, no preview) -- confirms this modern De Gruyter edition has no
free-text route from Google Books either, matching the archive.org/HathiTrust negatives already logged under
csDA2. No new free route found. Next step unchanged: library/ILL access to BAGK NF2 Bd.8, or the person reads
it directly; REQUEST.md's GLA copy-order route (for the two shelfmarks themselves, independent of the edition
question) stands unchanged and blocked, waiting on the owner.

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Claudia de Medici" AND "Baden-Baden" AND 1633 AND Geheimschrift`: no relevant hit (0 results, none about the letter).
- `"Escher von Binningen" AND Breisach AND Aldringen`: no relevant hit (0 results, none about the letter).

## While waiting (27 Sept 2026, WAIT-PASS-A)

Waits on a GLA Karlsruhe copy order for 81 Nr. 442/813, "waiting on you" since 24 Sept 2026 (REQUEST.md); the
BAGK NF2 Bd.8 edition is separately blocked (no free route, NX-UNBLOCK 26 Sept 2026).

- Read GLA Bestand 48's finding-aid text (the Baden cipher-key rubric, DA2, 1676-1761) for any item predating 1633 naming this pair -- catalogue-text only. S.
- Queue the JSTOR phrase-only family (ii): a distinctive phrase quoted from the letter's own catalogue description, no cipher keyword -- only family (i), sender/date/keyword, has run so far (26 Sept 2026 runner). S, JSTOR-QUEUE.tsv row.
- Run OpenAlex/Persée/HAL for "Claudia de' Medici" Baden-Baden 1633 diplomatic correspondence scholarship, beyond the generic WebSearch already tried. S.

## Check-solved re-run (GF4-BATCH16, account-4, 3 Oct 2026)

Status moved open -> blocked (CLAUDE.md Pipeline intake gate: an edition named but not opened is `blocked`).

- **BAGK NF2 Bd.8 (Bierther 1982, Jan 1633-May 1634).** Still NO_PAGES on the Google Books API (`&country=US`, keyed),
  but the API's snippet index answers for NO_PAGES volumes. Its returned snippets (e.g. "200. Maximilian an Erzherzogin
  Claudia Bitte um Hilfe fuer Breisach und Konstanz", archive siglum "Kschw 7546") show the volume is built on the
  Munich Kasten schwarz series, i.e. Maximilian's side, not the Ensisheim/Baden-Baden extradita at GLA. Searches
  anchored to the volume by its own siglum: 'Escher Kschw Bierther' 0, 'Escher Kschw' 0 relevant (one Karlsruhe
  address book), 'Neuenburg Kschw Claudia' 0, 'Ziffern Kschw Claudia' 0. This is a snippet-index search, not a read:
  it does not show the volume omits the two letters, only that the index did not surface them.
- **New lead, not readable from the cloud: Philipp Ruppert, *Die Kriegsereignisse im Breisgau von 1632 bis 1635 und
  die erste Belagerung Breisachs* (1884; Google Books JDnaXqmSWR0C, viewability ALL_PAGES, no PDF).** Also serialised
  in the Freiburg *Zeitschrift der Gesellschaft fuer Befoerderung der Geschichts-, Alterthums- und Volkskunde* (1883, 1887
  volumes ALL_PAGES on Google Books; archive.org holds only 1869/1872/1874, `advancedsearch` title query 3 Oct 2026).
  This is the regional history of exactly the Neuenburg/Breisach episode, written from the Karlsruhe files, and is the
  closest thing to a standard edition for these two letters. Keyword snippet queries anchored by title ('Escher',
  'Ziffern', 'chiffrirt', 'Neuenburg 24. Januar', 'Claudia Markgraf Wilhelm', '15000 Gulden', 'Geheimschrift',
  'Karlsruhe Landesarchiv', each + intitle:kriegsereignisse intitle:Breisgau) all returned 0 items -- the API does not
  search inside a single volume this way, so this is not a negative. books.google.com page/text view is
  captcha-blocked from the cloud (host table). Needs a person: LOCAL-QUEUE-style read of Ruppert for the January and
  March 1633 Claudia letters and whether any passage is said to be "in Ziffern"/deciphered.
- **Secondary citation of the same correspondence:** *Protection royale* (1978; also Schriftenreihe der Vereinigung zur
  Erforschung der Neueren Geschichte 1976), NO_PAGES, snippet: "... Baden an Erzherzogin Claudia, 1633 II 13 Karlsruhe GL[A]"
  -- a modern scholar used the Baden-Claudia correspondence at GLA for Feb 1633. Not readable; noted for the verifier.
- *Der Zug des Herzogs von Feria nach Deutschland im Jahre 1633* (1882, Google Books Aq-TyKCNLYsC, ALL_PAGES): snippet
  names Markgraf Wilhelm and Claudia in 1633; same cloud block on page view.

## Web and blog check (GF4-BATCH16, account-4, 3 Oct 2026)

- Web: `"Claudia" Medici "Wilhelm" Baden-Baden 1633 Neuenburg Breisach chiffriert` -- biographies only (de/en Wikipedia,
  fembio, LABW Findbuch 37), nothing on the letters.
- Web: `GLA Karlsruhe 81 Nr. 442 Claudia Medici chiffriertes Schreiben` -- GLA home page, DDB item for an unrelated GLA
  14/242, biographies; no hit on either shelfmark.
- Web: `Claudia de' Medici cipher letter 1633 Baden-Baden decipher` -- Bourdeau's site index (no Claudia target; a fresh
  clone of dbourdeau/cyphersolver at 841111b, 2 Oct 2026, has no target and no text naming Claudia/Baden-Baden/Neuenburg/
  Escher von Binningen in any NOTES), Mary Stuart decipherment articles, Wikipedia; nothing on these letters.
- Web (phrase): `"Escher von Binningen"` via Google Books (38 volumes: family histories, Ersch-Gruber, Oberbadisches
  Geschlechterbuch) and `Kriegsereignisse Breisgau Escher Aldringen` (Waldkirch und das Elztal, 1989: Escher's 520 men
  in Waldkirch, Feb 1633) -- context only, no letter text.
- Cipherbrain: `site:scienceblogs.de klausis-krypto-kolumne Claudia Medici OR Baden-Baden OR Tirol 1633` -- posts on
  Barga, Kryptos, a 1645 encryption (Eine ungeloeste Verschluesselung aus dem Jahr 1645, a different item), nothing on
  Claudia or Baden-Baden.
- Cryptiana blog: `site:cryptiana.blogspot.com Claudia OR Tirol OR Innsbruck OR "Baden-Baden"` -- no cryptiana page
  returned; local `sources/cryptiana/` already grepped 24 Sept, no hit.
- Cipher Mysteries: `site:ciphermysteries.com Claudia Medici OR "Baden-Baden" OR Breisach` -- one Voynich post (Medici
  bank in Bruges, comment), nothing on this item.
- Aymeloglu: fresh clone of aaymeloglu/unsolved-ciphers at d2800bb (27 Sept 2026): no target, grep for
  claudia|baden-baden|neuenburg|escher von: no hit.

## Premise check (GF4-BATCH16, account-4, 3 Oct 2026)

- (a) Folder's own mentions of a decipherment/gloss/clear copy: not found. NOTES.md and REQUEST.md mention none; the
  LABW record for 813 says "zum Teil in Geheimschrift" (the letter itself).
- (b) Other solvers' working files: not found -- neither repository has a target or a working file for this pair
  (clones above).
- (c) Physical neighbours: unreachable. No image of either item online (24 Sept plink check). The GLA signature search
  for 81 Nr. 441, 443, 812, 814 resolves each unit (POST signatursuche.php, 3 Oct 2026) but the title text loads only in
  the client-side Findbuch tree, so the neighbours' descriptions (a "Dechiffrierung" or Beilage) were not read.
- (d) Recipient side: the recipient's archive is GLA itself; the recipient-side printed treatment is Ruppert 1884 /
  the Freiburg Zeitschrift (above) -- found, unreadable from the cloud; a modern recipient-side citation (*Protection
  royale*, 1978, "Baden an Erzherzogin Claudia, 1633 II 13") -- found, unreadable.

Host requests: googleapis.com 25 (>=2 s apart), archive.org 3 (advancedsearch 2, be-api 4 incl. one test; 1.5-2 s),
www2.landesarchiv-bw.de 7 (2 s), github.com 2 clones, WebSearch 6.

## While waiting (GF4-BATCH16, account-4, 3 Oct 2026)

Waits on a person reading Ruppert 1884 (Google Books JDnaXqmSWR0C) and on the GLA copy order (REQUEST.md).
- Action that depends on nobody: fetch the GLA Findbuch 81 tree page for 81 Nr. 441-443 and 812-814 with
`tools/browser_fetch.js` (the title text is client-rendered) and read the neighbours' descriptions for a
decipherment, Beilage or Duplikat. S.

## IMG-GLA: GLA Findbuch 81 and Bestand 48 catalogue read (3 Oct 2026, account 2 worker for LANE-IMAGES)

Route: LABW OFS21 (`www2.landesarchiv-bw.de/ofs21`), plain curl with a browser UA, 2.2 s apart, no browser needed. Simple search
(`suche/ergebnis1.php`, POST, `archive[1]=4` = GLA) for the sender's name; signature search is two steps (`suche/signatursuche.php`
with `sign_archiv=4`, `zahlensequenz=81`, `exakt=1`, then `id_bestand=10853`, `bestellnr=<n>`); each unit read through
`olf/druckansicht.php?id_titlaufn=<id>`. Positive control for the search: "Claudia Medici" returned 41 units of Bestand 81,
including both targets. Clock 21:2x-21:3x UTC.

Unit records (Findbuch 81 Ensisheim: Extradita Colmar, bestand id 10853), quoted from the print view:

| Unit | id_titlaufn | Permalink | Titel | Laufzeit | Umfang / Vorsignatur | Digitisation flag |
|---|---|---|---|---|---|---|
| 81 Nr. 442 | 10846648 | http://www.landesarchiv-bw.de/plink/?f=4-5062086 | Chiffriertes Schreiben der Erzherzogin Claudia de Medici an Markgraf Wilhelm von Baden-Baden über die Eroberung der Stadt Neuenburg und die Entsendung des Obersts Hans Werner Escher von Binningen an den Grafen Johann von Aldringen. | 24. Januar 1633 | 1 Stück, C 460 | none: no Digitalisat link or image field |
| 81 Nr. 813 | 10846085 | http://www.landesarchiv-bw.de/plink/?f=4-5071198 | Schreiben der Erzherzogin Claudia de Medici an Markgraf Wilhelm von Baden-Baden mit Übersendung von 15.000 Gulden zur Bezahlung der Truppen und Fortführung der Festungsarbeiten zu Breisach (zum Teil in Geheimschrift). | 23. März 1633 | 1 Stück, C 523 | none |
| 81 Nr. 441 | 10846647 | plink f=4-5062078 | Schreiben des Markgrafen Wilhelm von Baden-Baden ... an Oberst Ascanius Albertinus von Ichtersheim, Gubernator zu Breisach, ... die Tore, Brücken, Türme und Rondelle mit Pulver zu minieren oder in Brand zu stecken. | 13. Januar 1633 | 1 Stück, C 460 | none |
| 81 Nr. 443 | 10845650 | plink f=4-5062105 | Designation über die Musketenlieferung aus der Herrschaft Waldkirch und der Stadt Elzach an Oberst Schoffholz zu Freiburg | 14. Februar 1633 | 2 Stücke, C 460 | none |
| 81 Nr. 812 | 10846874 | plink f=4-5071194 | Schreiben des Heinrich von Gaudecker aus Emmendingen an den Obervogt der Herrschaften Kastelberg und Schwarzenberg über die Übergriff der in Simonswald einquartierten Truppen. | 8. Oktober 1633 | 1 Stück, C 523 | none |
| 81 Nr. 814 | 10846644 | plink f=4-5071200 | Verzeichnis der am 12. Mai 1633 zu Neuenburg gelieferten Rationen. | 1633 | 1 Stück, C 523 | none |

Each print view carries only Titel, Laufzeit, Umfang, Vorsignaturen; the order basket is the only action. Caveat on the flag: I did not
find a GLA unit that does show a digitisation link, so the absence of one is read from the record's fields, not checked against a known
digitised GLA unit (the search result list's "Digitalisate einsehen" label, used as the positive control in stas-waldburg-1653, appeared
on none of the 41 Claudia hits). The earlier plink check (24 Sept) and the scout's sweep agree.

Neighbours (step 2): none of 441, 443, 812, 814 mentions a key, Chiffre, Geheimschrift, Dechiffrierung or Auflösung. What the searches show about the
cipher-bearing set: simple search `chiffr*` in GLA gave 37 units; in Bestand 81 only Nr. 442; `Geheimschrift` gave 25 units, in Bestand 81
only Nr. 813; `Chiffrenschlüssel OR Chiffreschlüssel OR Ziffernschlüssel` 0. The other 39 of the 41 "Claudia Medici" units of Bestand 81 (Nr. 96, 209,
342, 351, 355, 431, 451, 459, 469, 478, 589, 684, 716, 721, 725, 743, 757, 770, 816, 818, 820, 823, 825, 830, 832, 839, 857, 862, 864, 900,
910, 912, 924, 944, 947, 950, 961, 1387, 1451) were listed; titles read for the search terms only, none carries a cipher word.

Bestand 48 (Haus- und Staatsarchiv III. Staatssachen, rubric "Chiffren", Nr. 65-84): nothing names Claudia de' Medici or the
Baden-Baden/Ensisheim pair before 1633. Items dated before 1650: Nr. 68 "Aus der Zeit des Markgrafen Georg Friedrich von Baden-Durlach"
(ca. 1624-ca. 1626, unbestimmte Chiffren) and Nr. 77 "Entwurf eines baden-durlachischen Chiffrierbuchs ..." (17. Jhdt.); both are
Baden-Durlach, a different line from the recipient Markgraf Wilhelm von Baden-Baden. Nr. 72 ("Chiffren für die Korrespondenz des Markgrafen
Hermann von Baden-Baden", 17. Jhdt.) and Nr. 73 are Baden-Baden but undated within the century / later. Not read: the units' contents;
whether any of these keys fits either 1633 letter is untested and unknown. No digitisation flag recorded for them beyond the same print-view
fields (not fetched individually, request cap).

Found: both units are undigitised in the LABW catalogue and orderable only through LABW. Not found: a key, a decipherment, a clear copy,
a Beilage or a digital image for either unit or its four neighbours. Requests: www2.landesarchiv-bw.de about 41 (one over the 40 cap;
2 returned 404 and are included), no vision calls, no subagents.

**Next step (unchanged):** copy order for 81 Nr. 442 and 813 (REQUEST.md, ASKS row 136); Ruppert 1884 read by a person.
