open
Vochezer, Geschichte des fürstlichen Hauses Waldburg in Schwaben vol. 3 (archive.org djvu full text, 67,235 lines) re-fetched and grepped by this worker (GF-A2-7, 2 Oct 2026) for Chiffre/Geheimschrift/Ziffer, Walburga, Pröpstin, Essen, Christoph Karl: no cipher term, neither correspondent, letters absent. GAPS116 (3 Oct 2026): Regesten/regional-journal full-text search (IA fts, Google Books, Hohenzollern Mitteilungen 1887-91 djvu) found no mention of Nr. 702, its cipher or a decipherment; Friedberg-Scheer leads for the recipient logged. GAPS121 (3 Oct 2026): LABW record of Nr. 702 (plink/?f=6-24180) reads Bemerkung "mit Auflösung der Geheimschrift", 8 Schr., no digitisation link; recipient = brother Christoph Karl (1613-1672), son of Wilhelm Heinrich (Dep. 30/1 T 1 Nr. 882); copy is the blocker.

# Maria Walburga Eusebia von Waldburg to Christoph Karl von Waldburg, partly ciphered — StA Sigmaringen

QUEUE row: DA9 (sources/solver-diffs/2026-09-24-lane-n2-dea.tsv, "German state archives, online finding aids
(LANE N2 scout of 24 September 2026)").

## Source

Staatsarchiv Sigmaringen, **Dep. 30/1 T 3 Nr. 702**: "Korrespondenz der Truchsessin Maria Walburga Eusebia von
Waldburg, Pröpstin zu Essen, an ihren Bruder Truchseß Christoph Karl (?) z.T. in Geheimschrift", 1653-1654.

Identified persons (WebSearch, 24 Sept 2026): **Maria Walburga (Eusebia) Truchsess von Waldburg-Trauchburg**
was Pröpstin (provost) of the Essen women's abbey until 1668 (Wikipedia/BLKÖ). Her likely brother
**Christoph Karl (Karl Christoph) Graf von Waldburg-Trauchburg** (24 Aug 1613 - 28 Mar 1672), Reichserbtruchsess,
married to Maria Elisabeth von Sulz (kaiserhof.geschichte.lmu.de/16378) — the catalogue's own "(?)" on the
brother's identity is not resolved by this pass, just corroborated as plausible.

## Check-solved sweep (24 September 2026)

1. **Editions.** No dedicated edition of Waldburg family correspondence covering this pair or these years was
   located. The Deutsche Digitale Bibliothek holds several *unpublished* Waldburg family correspondence
   bundles at item level (Waldburg-Wolfegg'sches Gesamtarchiv material, e.g. items
   4Q6VGO4AFOYYMBS43B3TQHXXUTFNTJJO and E65VUJJ63AAMXORAELJDFFRHUAAAWZTP, both catalogue descriptions, not
   editions) — none of these DDB item descriptions names either correspondent by this date range or mentions a
   cipher. A dedicated printed *Zeitschrift für Hohenzollerische Geschichte* or Waldburg-archive Regesten
   series was not reached this pass.
2. **Printed decipherment / catalogue note.** The finding-aid title gives no indication of an attached key or
   contemporary decipherment.
3. **Community lists.** `sources/cryptiana/` grepped for "Waldburg": no hits.
4. **DECODE.** `sources/decode/` grepped for "Waldburg", "Walburga", "Trauchburg", "Sigmaringen": no hits.
5. **Solver repositories.** Fresh shallow clones, 24 Sept 2026. No target folder for Waldburg in either repo;
   `grep -rli waldburg` across both trees: zero matches.
6. **General web search.** As (1). No result names an attempt to read this correspondence's cipher passages.

**Copy status.** Not independently re-tested this pass against LABW's viewer (StA Sigmaringen's finding aids
are served through the same LABW OFS21 system as GLA Karlsruhe and HStA Stuttgart). Scout's original sweep
(sources/solver-diffs/2026-09-24-lane-n2-dea.tsv) recorded "none tested (no digitisation link)" for this row.
**Copy-order**, pending a direct re-check. See REQUEST.md.

**Host requests this pass:** WebSearch 1, github.com 1 shallow clone each of both repos (shared across this
run's six targets); no direct LABW request this pass.

## Verdict

**Status: open, stage 2 (verified unsolved).** No edition, catalogue gloss, community list, DECODE record, or
solver-repository entry names this correspondence. Convent/family correspondence "z.T. in Geheimschrift" between
a Reichsstift provost and her brother is a plausible small nomenclator or letter-substitution system, likely
short given it is only "z.T." (partly) enciphered within otherwise plain letters — those plain portions, once
copied, may themselves be a crib for the ciphered portions per the same letter (LESSONS.md "structure before
search" / verify-against-the-world pattern).

**Recommended next steps (not run this pass):** (1) search for a Waldburg-Trauchburg family archive Regesten
or Zeitschrift für Hohenzollerische Geschichte covering 1653-54; (2) resolve the catalogue's "(?)" on
Christoph Karl's identity against Waldburg genealogies before any solving; (3) re-test LABW's viewer for
Dep. 30/1 T 3 Nr. 702 directly.

## csDA2: edition lead (24 September 2026, close-out pass)

Closing the Waldburg family edition lead flagged above (brief named it as "Vochezer, Geschichte des
fürstlichen Hauses Waldburg"). Vochezer's 3-volume *Geschichte des fürstlichen Hauses Waldburg in Schwaben*
(Kempten, 1888-1907) is on archive.org; volume 3 (identifier `GeschichteDesFuerstlichenHausesWaldburgInSchwaben3`,
Vochezer_Waldburg_3_djvu.txt, 67,235 lines) is the one that reaches the 17th century — confirmed by nine "1653"
hits in the narrative (e.g. line 54725 "erftatteten am 23. Januar 1653", line 58984 "23. September 1653"), and
one hit for "Trauchburg" (line 20214, "Christoph, Erbtruchsess, Freiherr zu Waldburg... zu Trauchburg" — a
different Christoph, not Christoph Karl).

Fetched the full djvu.txt and grepped for the correspondents and the cipher terms (with loose substrings
"iffr"/"eheim" against the same Fraktur-OCR noise seen in the Havemann volume): no occurrence of "Chiffre",
"Geheimschrift" (only "Geheimer/Geheimen Rat", the privy-council sense, appears — 15 hits total for "eheim"),
"Christoph Karl", "Walburga" (the two "Walburgen" hits at lines 16078-16582 are the saint, S. Walburga, not the
person), or "Essen"/"Pröpstin". The correspondence (StA Sigmaringen Dep. 30/1 T 3 Nr. 702) is not named.

**Verdict: open, edition lead closed.** Vochezer's volume covers the right decade and the Trauchburg line of
the family but never names either correspondent, the letters, or a cipher. The genuine caveat: 19th-century
Fraktur OCR on this scan is noisy (many common words misrecognised, e.g. "Sriefe" for "Briefe"), so a rare
proper name could in principle be missed; the negative is on the same footing as the Havemann one, not
stronger. Posting `confirm` to ROOM.

Host requests this section: archive.org 3 (advancedsearch + metadata + djvu.txt fetch for
`GeschichteDesFuerstlichenHausesWaldburgInSchwaben3`, >=3s apart, IA slot); WebSearch 1 (to confirm which
archive.org identifier is volume 3 and its year range).

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Waldburg" AND "Christoph Karl" AND 1653 AND Geheimschrift`: no relevant hit (0 results, none about the letter).
- `"Truchsessin Maria Walburga" AND Essen`: no relevant hit (0 results, none about the letter).

## Web and blog check (GF-A2-7, 2 Oct 2026)

Plain web searches (WebSearch, standard): (1) `Maria Walburga Eusebia Waldburg Pröpstin Essen Geheimschrift Briefe
Bruder 1653` -- one plausible-looking hit, verlag-regionalkultur.de/presse/bib/bib_05-218-8.pdf, opened and read: it
is the contents and sample of a book on Charlotte of Hessen-Kassel, Electress Palatine (1650s, with a ciphered letter
of Döringenberg to the Electress that Karl Ludwig objected to) -- a different correspondence, no Waldburg; the uni-due.de and other hits
are unrelated; (2) `"Dep. 30/1 T 3" Waldburg Geheimschrift` (shelfmark) -- no hit on the shelfmark; (3)
`Waldburg-Trauchburg Christoph Karl Schwester Essen Korrespondenz Staatsarchiv Sigmaringen Geheimschrift` --
Archivportal-D records for other Waldburg correspondence in Dep. 30/1 T 3 (e.g. Nr. 1331, family letters; Christoph
Karl's letters to brothers and cousins), no decipherment; (4) `Truchsessin Waldburg Pröpstin Essen Korrespondenz
1653 1654 z.T. in Geheimschrift` (the folder's catalogue title) -- Archivportal-D Waldburg items, not this one; nothing
read or decoded. Blog site searches: Cipherbrain `Waldburg Geheimschrift Brief` -- Ferdinand III, Wallenstein,
"Geheimschrift aus dem Nachlass einer Adeligen" (2016/02/10, a modern-era item, not Waldburg) and other unrelated
posts; Cryptiana `Waldburg cipher` -- no results; Cipher Mysteries `Waldburg Essen abbess cipher letters` -- unrelated
posts only. No hit named this correspondence, so no comment thread to read. Result: no decipherment or plaintext found.

## Premise check (GF-A2-7, 2 Oct 2026)

(a) Folder's own mentions: NOTES.md and REQUEST.md name no decipherment, key or clear copy; the plain parts of the
letters ("z.T." enciphered) are a possible crib once copied, not a decipherment. Not found. (b) Other solvers'
working files: fresh shallow clones 2 Oct 2026, `grep -rliE` waldburg, walburga, trauchburg, sigmaringen, "Dep. 30":
cyphersolver hits are other Waldburgs only (Cardinal Otto and Bishop Johann IV in targets/pallotto1629/ed/, "Waldburg
Ottó" in targets/buda1489/vestigia/), Hohenzollern-Sigmaringen in targets/napoleon/src/; Aymeloglu: none (cited,
nothing copied). Not found. (c) Physical neighbours: no image of Nr. 702 on disk or known online; the neighbouring
Waldburg family correspondence in Dep. 30/1 T 3 (e.g. Nr. 1331) is catalogue-only; unreachable until a copy exists.
(d) Recipient side: recipient Christoph Karl (Waldburg-Trauchburg line); Vochezer vol. 3, the family history,
re-grepped in full by this worker (status line), names neither the letters nor a cipher; no edition of the Essen
abbey's (sender's side) correspondence for 1653-54 found. Not found.

## GAPS116-stas-waldburg-1653 (3 Oct 2026, account-4): next step (1), Regesten / regional-journal full-text search

Clock read 13:00 UTC. Intake gate `python3 tools/intake_gate_check.py stas-waldburg-1653` exit 0 before work. Scripts
only (no vision, no subagents); the model read only the hit snippets.

**Hosts and positive controls.** (a) Internet Archive cross-item full-text search (`be-api.us.archive.org/fts/v1/search`),
control `"Truchsess von Waldburg"` -> 8,375 hits (works). (b) Google Books API (`&country=US`, keyed), control
`"Truchsess von Waldburg"` -> 311 volumes (works). (c) IA `advancedsearch` title search for the journals. (d) IA djvu text
of *Mitteilungen des Vereins für Geschichte und Altertumskunde in Hohenzollern* 1887-1891 (`MitteilungenHohenzollern18871891`,
39,383 lines), control "Sigmaringen" -> 308 lines (OCR readable). The second IA copy `bub_gb_CIgAAAAAcAAJ` has a 7-line
djvu text and no fts index (control "Hohenzollern" 0): not searchable, a non-test. BSB's own full-text search was not
queried; BSB-digitised volumes were reached through their IA mirrors (`*bsb` identifiers) in (a).

**What is online.** No *Zeitschrift für Hohenzollerische Geschichte* (1965-) or *Hohenzollerische Jahreshefte* volume on
IA by title search (0 each); the in-copyright journal is reachable only as Google Books snippets, covered by (b). The only
Hohenzollern society volume online (1887-91) has 0 lines for Waldburg/Truchsess/Walburga/Trauchburg/Friedberg variants
(Fraktur OCR, loose substrings `aldburg`, `ruchse`, `rauchburg` tried), and 0 for Geheimschrift/Chiffre/Ziffer.
*Beiträge zur Geschichte von Stadt und Stift Essen* (1881, `bub_gb_PFzVAAAAMAAJ`): 0 hits for Waldburg or Walburga
(control "Essen" hits).

**Queries and results** (IA fts / Google Books): `"Maria Walburga" Essen Waldburg` (229 / -), `Walburga Pröpstin Essen
Truchsessin` (10), `"Christoph Karl" Trauchburg` (122), `Waldburg Geheimschrift` (1,310), `Waldburg Chiffre 1653`
(2,845), `"Pröpstin" Essen Waldburg` (348), `Eusebia Waldburg Essen` (1,301), `Truchsessin Essen 1653` (525); GB:
`"Maria Walburga" Waldburg Essen Pröpstin` (2), `Waldburg Trauchburg Geheimschrift` (11), `"Dep. 30/1 T 3"` (8),
`"Nr. 702" "Dep. 30/1"` (157, all noise), `Walburga Eusebia Waldburg Geheimschrift` (0), `"Walburga Eusebia" Waldburg`
(15), `"Pröpstin zu Essen" Waldburg` (3), `"Archivinventare" Walburga Eusebia Trauchburg` (2), `Walburga Trauchburg Essen
Geheimschrift` (0), `"Christoph Karl" Friedberg-Scheer 1653` (3), and three more with 0-1 hits. Every hit's snippet read:
**no hit names Dep. 30/1 T 3 Nr. 702, these letters, a cipher of this family, a key or a decipherment.** Not found.

**Leads (for step 2, not resolved here; grade M, snippet-level only):**
- Ute Küppers-Braun, *Frauen des hohen Adels im kaiserlich-freiweltlichen Damenstift Essen, 1605-1803* (1997, GB
  X-f5rjgmscwC, no preview): an entry "Maria Walburga Eusebia Truchseß von Waldburg-Trauchburg", Essen, with a
  parents line naming a "Hans Ernst Truchseß von Waldburg" (snippet; whether as father is not legible from it).
  Same author, *Macht in Frauenhand* (2002, N3ElAQAAIAAJ): "Maria Walburga Eusebia Truchseß v. Waldburg-Trauchburg",
  date 1668 Juni 18 (her death or resignation as Pröpstin). This is the prosopography that settles her parents and so
  her brothers; snippet-only from the cloud.
- *Württembergische Archivinventare* (1947, GB bzhmAAAAMAAJ, no preview): an inventory entry grouping letters of
  "Walburga Eusebia von Königsegg geb. Gräfin zu Trauchburg, Christoph Carl Graf zu Friedberg-Scheer, Maria Franziska
  von Wolkenstein geb. Gräfin zu Trauchburg von ihrer Schwester Maria Veroni[ka?]" -- a sibling group with a Christoph
  Carl styled **Graf zu Friedberg-Scheer**. Obermarchtal Urkunden (1993, YThmAAAAMAAJ) and *Die Grafen von Sulz* (1992,
  ZCZoAAAAMAAJ) name "Christoph Karl Gf. v. Friedberg[-Scheer]" with brother Otto, 1653; the Sulz marriage matches the
  kaiserhof record cited under Source. Dep. 30/1 T 3 is itself the Grafschaft Friedberg-Scheer fonds (GB lPjMQgAACAAJ,
  "Bestand Dep. 30/1 T 3 - Grafschaft Friedberg-Scheer", 2001). So the recipient is more likely styled Friedberg-Scheer
  than Trauchburg (the Source section's "Waldburg-Trauchburg" is an inference from 24 Sept, not established).
- *Ortskirche und Weltkirche in der Geschichte* (Festgabe Trippen, GB 3SP8fxb7CfoC, PARTIAL) has an essay drawing all
  its unprinted sources from Dep. 30/1 T 3 (cites Nr. 1649); a Cologne church-history volume, so plausibly about a
  Waldburg canoness or cleric in the Rhineland. Snippet does not show Nr. 702.
- Separate person, not ours: Zündorf 1911 (St. Ursula, Cologne) lists Waldburg-Zeil canonesses; a Walburga Eusebia
  daughter of Christoph of Friedberg-Scheer married into Königsegg/Niederösterreich lines (d. 1656/1663/1673 by
  source) -- name collision to keep apart in step (2).

**Requests per host:** archive.org advancedsearch 8, metadata 3, download 2; be-api.us.archive.org 25;
www.googleapis.com (Books) 26 (one 503, not retried). No 429 or challenge.

**Next step:** (2) resolve the sender's parents and the recipient's line from Küppers-Braun 1997 (the Essen
prosopography entry for Maria Walburga Eusebia) and the *Württembergische Archivinventare* 1947 entry -- both
snippet-only from the cloud; a LOCAL-QUEUE row (owner's browser, Google Books snippet view or a library copy) or a
CORE/OpenAlex check for an open-access Küppers-Braun text, ~USD 1. Then (3), the LABW viewer re-test for Nr. 702; the
copy (REQUEST.md) is still what any reading needs. Also worth a ~USD 1 check: the Trippen-Festgabe essay built on
Dep. 30/1 T 3 (GB 3SP8fxb7CfoC, PARTIAL) for a citation of Nr. 702.

## GAPS121-stas-waldburg-1653 (3 Oct 2026, account-4): step 2, sibling group and LABW finding-aid re-check

Clock read 13:17 UTC. Intake gate exit 0 (status `open`, edition citation found). Scripts only; no vision, no subagents.

**(b) LABW online finding aid, done first because it answered (a) too.** Route: OFS21 simple search
(`www2.landesarchiv-bw.de/ofs21/suche/ergebnis1.php`, POST, QUEUE.md "LABW, OFS21" recipe), then the unit's print view
(`olf/druckansicht.php?id_titlaufn=9008`) and the Findbuch structure view (`olf/struktur.php?bestand=2242`). Positive
control for the search: `Walburga Eusebia` -> 4 hits, Nr. 702 among them. Positive control for the digitisation flag: the
same search engine's result list shows "Digitalisate einsehen" on HStA Stuttgart A 2 Bü 10 and Bü 11 (digitised), so its
absence on a record is a real signal for this view.

Nr. 702's own record, quoted (permalink as the record gives it: `http://www.landesarchiv-bw.de/plink/?f=6-24180`):
Titel "Korrespondenz der Truchsessin Maria Walburga Eusebia von Waldburg, Pröpstin zu Essen, an ihren Bruder Truchseß
Christoph Karl (?) z.T. in Geheimschrift"; Laufzeit 1653-1654; **Umfang "8 Schr."**; **Bemerkung "mit Auflösung der
Geheimschrift"**; Vorsignaturen "Rep. I Erg. Pk. 20; K. XIII, L. 1 Nr. 1"; Provenienz Friedberg-Scheer; Stichworte
"Waldburg-Trauchburg, Christoph Karl von; Reichserbtruchsess, Graf, 1613-1672" and "Waldburg-Trauchburg, Maria Walburga
Eusebia von; Reicherbtruchsessin, Gräfin, Pröpstin zu Essen, 1630-1668". Section "1.5. Interne Beziehungen der
Mitglieder des truchsessischen Hauses untereinander: Korrespondenz" of Dep. 30/1 T 3 (Friedberg-Scheer: Akten).
**Digitisation flag: none** -- no "Digitalisate einsehen" link in the result list, the print view or the structure view;
the record offers only the order basket. Copy still needed (REQUEST.md).

So the unit itself is catalogued as carrying a decipherment ("Auflösung") of its cipher passages -- a period clear
text or key beside the ciphertext, which would make this a recovery (grade H/C from the unit's own decipherment), not a
cryptanalysis. Whether the "Auflösung" is contemporary or a later archivist's is not stated; the copy decides.

**Sibling units (structure view, section 1.5, read in full):** none other carries Geheimschrift/Chiffre/Schlüssel wording.
Nearest neighbours: Nr. 721 "Korrespondenz der Truchsessen Leopold Friedrich und Wilhelm Wunibald von Waldburg, Domherrn
zu Köln und Straßburg und Wilhelm Eusebius aus Rom, später Jesuit, mit ihrem Bruder Truchseß Christoph Karl von Waldburg
v.a. wegen Deputatsgeldern", 1 Bü, 1652-1653 (same recipient, same years, no cipher wording; a candidate plain-text
neighbour, possibly same hands/couriers). Nr. 29 (Testament und Verlassenschaft der Maria Walburga Eusebia, gest. 1668,
1667-1669). Fonds-wide cipher searches: `Geheimschrift Friedberg-Scheer` 1 hit (Nr. 702), `Geheimschrift Waldburg` 3
(Nr. 702; HStAS A 2 Bü 10/11, 1534, unrelated), `Auflösung Geheimschrift` 3 (Nr. 702; HStAS M 77/1, a 19th-20th c.
military fonds), `Chiffre Truchseß` 3 (1525-1566, unrelated Bauernkrieg/Bamberg units), `chiffriert Truchseß` 0.

**Family settled from the archive's own record (grade H for the identification, from the catalogue):** Dep. 30/1 T 1
Nr. 882 (1652 Januar 13): Reichserbtruchseß Wilhelm Heinrich hands the government to his two eldest sons Christoph Karl
and Otto; the three other brothers Leopold Friedrich, Wilhelm Wunibald and Wilhelm Heinrich Eusebius; "Den beiden
Schwestern Maria Walburga Eusebia und Maria Anna Eusebia ...". So the recipient is her brother Christoph Karl (1613-1672),
son of Wilhelm Heinrich; the catalogue's "(?)" is supported by its own index and by Nr. 882. The 24 Sept "Waldburg-
Trauchburg" styling is the archive's index heading; "Friedberg-Scheer" is the same man's county.

**(a) Württembergische Archivinventare 1947** (GB bzhmAAAAMAAJ, 974 pp., NO_PAGES; no IA copy; Open Library 0 records, so
no OCLC for the HathiTrust EF route). Snippets only, via keyed Books API (`&country=US`): the GAPS116 group is letters
of the Trauchburg-line Gräfin **Maria Veronika Preysing** to her siblings ("Walburga Eusebia von Königsegg geb. Gräfin zu
Trauchburg, Christoph Carl Graf zu Friedberg-Scheer, Maria Franziska von Wolkenstein geb. Gräfin zu Trauchburg von ihrer
Schwester Maria Veronika Gräfin Preysing, Maria Monika von Königsegg geb. Gräfin zu Friedberg von dem Domherrn Johann
...", then "d) seinem Vetter, dem Domherrn Friedrich Wilhelm Wunibald Grafen zu Friedberg-Scheer, e) von Maria Veronika
Khuen, Johann Ludwig Grafen zu Sulz ..."), and another entry "Nr. 1010" region names "Hans Ernst und Christoph Carl zu
Friedberg 1666/73". This is a *different* sibling set (the Königsegg-married Walburga Eusebia, not the Essen Pröpstin),
the name collision GAPS116 flagged; it is not Nr. 702's sibling group. In-volume probes for cipher wording
(`intitle:Archivinventare` + Geheimschrift / chiffriert / Chiffre Friedberg / Ziffern Truchsess / "Walburga Eusebia" /
Pröpstin Essen) all 0. Snippet-limited: not found, not excluded.

**(c) Küppers-Braun 1997** (GB X-f5rjgmscwC, snippet): "... Wilhelm Heinrich Truchseß von Waldburg-Trauchburg und Anna
Maria Gräfin von Waldburg-Wolfegg, Schwester: Maria Walburga Eusebia (031), geb. 21. Juli 1633, gest. Apr. 1656 ..." --
an entry (apparently the sister Maria Anna Eusebia's) naming the same parents; to which sister the dates belong is not
legible from the snippet (grade M). Agrees with Nr. 882.

**Requests per host:** www2.landesarchiv-bw.de 13 (2 route probes, 7 searches, 1 print view, 1 structure view, plus the 2
first probes 302/404); www.googleapis.com (Books) 22 (one 503, not retried); openlibrary.org 1. No 429 or challenge.

**Next step:** the copy (REQUEST.md) -- now with the reason that the unit is catalogued "mit Auflösung der Geheimschrift",
8 letters, undigitised, orderable through LABW's order basket (permalink above). One while-waiting action that depends on
nobody: none cheap remains online; the copy is the blocker. Status unchanged (`open`): a catalogued decipherment inside
the unit is not a printed decipherment, so this is not found-solved; any reading from it would be key source `period`.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

Nothing depends on anyone: the folder's own GAPS pass found no cheap online action left; the unit (catalogued "mit Aufloesung der Geheimschrift", 8 letters, undigitised) waits on the copy order, ASKS row 117 / REQUEST.md.
