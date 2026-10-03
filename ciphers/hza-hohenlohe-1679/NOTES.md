open
LABW unit records (GAPS101, 3 Oct 2026): Bü 161 plink http://www.landesarchiv-bw.de/plink/?f=3-88062 "Enthält: Beilage: Chiffrierschlüssel" (key enclosed); Bü 165 plink .../?f=3-88066; no digitisation on either.
Ruland, Graf Wolfgang Julius von Hohenlohe-Neuenstein, Archiv für hohenlohische Geschichte 2 (1870) pp. 271-290 read in full by this worker (GF-A2-7, 2 Oct 2026, PDF via a browser past the WLB Anubis check): Melchior, Pape, Köhler, the reports and any cipher absent.

# Reports of Lic. Melchior and of Pape/Köhler to Graf Wolfgang Julius von Hohenlohe, partly ciphered — HZA Neuenstein

QUEUE row: DA10 (sources/solver-diffs/2026-09-24-lane-n2-dea.tsv, "German state archives, online finding aids
(LANE N2 scout of 24 September 2026)").

## Source

Hohenlohe-Zentralarchiv Neuenstein (a private/house archive, catalogued via LABW's portal), **Sf 35 Bü 161 and
Bü 165** (Wilhermsdorf I):
- **Bü 161**, 1679-1680: "Berichte (teilweise chiffriert) des Lic. Melchior an Graf Wolfgang Julius aus Wien,
  Prag und Straßburg."
- **Bü 165**, 1689: "Berichte (teilweise chiffriert) der in Hausangelegenheiten nach Wien entsandten Diener
  Kanzleirat Johann Christoph Pape und Kammersekretär Georg Ludwig Köhler."

Recipient: **Graf Wolfgang Julius von Hohenlohe-Neuenstein** (3 Aug 1622 - 26 Dec 1698), Imperial field marshal
and the last Count of Hohenlohe-Neuenstein (Wikipedia, BLKÖ, confirmed). A dedicated journal for this family's
history exists and was located: **Archiv für hohenlohische Geschichte** (journals.wlb-stuttgart.de/index.php/afhg),
which carries at least one article specifically on Wolfgang Julius ("Graf Wolfgang Julius von Hohenlohe-Neuenstein.
Geb. den 3. Aug. 1622. † 26. Dec. 1698.", found this pass).

## Check-solved sweep (24 September 2026)

1. **Editions.** The *Archiv für hohenlohische Geschichte* biographical article on Wolfgang Julius was located
   but **not opened this pass** (budget) — it is the single most relevant named source for this target and
   should be the first thing a follow-up pass reads, specifically for any mention of Lic. Melchior, Pape, Köhler,
   or a cipher/"Chiffre". No other dedicated edition of Wolfgang Julius's diplomatic correspondence was found.
2. **Printed decipherment / catalogue note.** Both finding-aid titles give no indication of an attached key or
   contemporary decipherment; "teilweise chiffriert" describes the reports themselves.
3. **Community lists.** `sources/cryptiana/` grepped for "Hohenlohe": no hits.
4. **DECODE.** `sources/decode/` grepped for "Hohenlohe", "Neuenstein", "Melchior", "Köhler", "Pape": no hits
   (note: "Melchior" and "Pape" are common enough words/names that a false-negative from over-specific grep
   terms is possible; not cross-checked against a broader DECODE catalogue dump this pass).
5. **Solver repositories.** Fresh shallow clones, 24 Sept 2026. No target folder for Hohenlohe in either repo;
   `grep -rli hohenlohe` across both trees: zero matches (aside from `windischgraetz1720/` incidentally
   discussing an unrelated Habsburg-era figure, not Hohenlohe — checked, no name overlap).
6. **General web search.** As (1). No result names an attempt to read either report's cipher passages.

**Copy status.** Not independently re-tested this pass against LABW's viewer. Scout's original sweep
(sources/solver-diffs/2026-09-24-lane-n2-dea.tsv) recorded "none tested (no digitisation link)" for this row;
worth noting HZA Neuenstein is a private house archive, so a plink resolving to LABW's OFS21 (as tested
directly for DA8) is not guaranteed to exist for a private-archive fond — unconfirmed this pass.
**Copy-order**, pending a direct re-check. See REQUEST.md.

**Host requests this pass:** WebSearch 1, github.com 1 shallow clone each of both repos (shared across this
run's six targets); no direct LABW request this pass.

## Verdict

**Status: open, stage 2 (verified unsolved), with one open edition gap.** No printed decipherment, catalogue
gloss, community list, DECODE record, or solver-repository entry names either bundle of reports. The
*Archiv für hohenlohische Geschichte* biographical article on the recipient is a real, specific, locatable lead
that a follow-up pass must read before this target advances past stage 2 in practice, even though the verdict
itself (no solution found in six sources) stands.

**Recommended next steps (not run this pass):** (1) read the *Archiv für hohenlohische Geschichte* Wolfgang
Julius article for any mention of these reports, "Chiffre", Melchior, Pape or Köhler; (2) confirm whether HZA
Neuenstein's finding aids resolve to a LABW plink at all (private-archive digitisation status untested); (3) two
separate correspondents/decades (Melchior 1679-80 from Vienna/Prague/Strasbourg; Pape+Köhler 1689 from Vienna) —
treat as two sub-targets once copies exist, since they are unlikely to share one key.

## csDA2: edition lead (24 September 2026, close-out pass)

Closing the *Archiv für hohenlohische Geschichte* lead flagged above. Identified the specific article by
WebSearch: K. Ruland, "Graf Wolfgang Julius von Hohenlohe-Neuenstein. Geb. den 3. Aug. 1622. † 26. Dec. 1698.
Ein biographischer Versuch", *Archiv für hohenlohische Geschichte* 2 (1870), pp. 271-290, hosted at
`journals.wlb-stuttgart.de/index.php/afhg/article/view/4600`.

Tried to read it: `WebFetch` on the article page returned an Anubis bot-challenge interstitial ("Access Denied:
error code 9e4edb5b6b850c41", not the article) — the same JS proof-of-work gate CLAUDE.md's access playbook
records for bibliotecadigital.rah.es; this pass has no browser-tool host authorisation for wlb-stuttgart.de to
try the intermittent-clear workaround. Not on archive.org (`advancedsearch` for the journal title: 0 hits — it
is a regional-society journal, unlikely to have a Google Books/IA scan). WebSearch (including a
`site:journals.wlb-stuttgart.de` query naming "Melchior") surfaced only the article's title, author, date and
page range — no snippet of its text, and nothing naming Lic. Melchior, Pape, Köhler, or a cipher.

**Verdict: blocked.** The one named edition lead for this target cannot be read through this pass's authorised
routes. The nomination stays HELD until either the Anubis gate is cleared (a browser-tool pass with this host
in scope) or the article is read by another route (ILL, a library proxy, or a direct request to the journal).

Host requests this section: WebFetch 1 (Anubis-blocked), WebSearch 2, archive.org 1 (advancedsearch, 0 hits).

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Wolfgang Julius von Hohenlohe" AND 1679 AND chiffriert`: no relevant hit (0 results, none about the letter).
- `"Sf 35 Bü 161" OR "Melchior" AND "Hohenlohe" AND Wien AND Prag`: no relevant hit (0 results, none about the letter).

## Web and blog check (GF-A2-7, 2 Oct 2026)

Plain web searches (WebSearch, standard): (1) `Wolfgang Julius Hohenlohe Melchior Berichte Wien Prag Straßburg 1679
chiffriert` -- Wurzbach BLKÖ 9 (austria-forum), a WLB Württembergisch Franken article, and a reference to the
Ferdinand III / Leopold Wilhelm letters to Hatzfeld in the Neuenstein archive (a different, known cipher corpus);
nothing on Bü 161/165; (2) `"Sf 35" Hohenlohe Neuenstein Wilhermsdorf Bü 161 chiffriert` -- Archivportal-D finding-aid
records for Herrschaft Wilhermsdorf, no decipherment; (3) `Pape Köhler 1689 Wien Hohenlohe Kanzleirat Kammersekretär
Berichte` -- unrelated Köhler/Pape persons; (4) `Ruland "Graf Wolfgang Julius von Hohenlohe-Neuenstein" Archiv für
hohenlohische Geschichte` -- Wikipedia, NDB/ADB, Archivportal-D (Sf 35 Bü 174, GA 55 Bü 146), and J. Brüser, "Sieger
ohne Sold" (AfhG, on 1663-65) -- none mentions the reports or a cipher. The Ruland article itself was then read in
full (status line). Blog site searches: Cipherbrain `Hohenlohe chiffriert Geheimschrift Brief` -- Ferdinand III,
Wallenstein, Thirty Years War posts; no Hohenlohe; Cryptiana `Hohenlohe cipher 1679` -- no results on either domain;
Cipher Mysteries `Hohenlohe cipher letter` -- unrelated posts only. No hit named either bundle, so no comment
thread to read. Result: no decipherment or plaintext found.
Note for a later step: the Ferdinand III -> Hatzfeld cipher letters said to be in the Neuenstein archive (Cipherbrain
2014/05/23 "Die ungelöste Geheimschrift von Kaiser Ferdinand III.") are a different, imperial correspondence of the
1640s, not these 1679-80/1689 house reports.

## Premise check (GF-A2-7, 2 Oct 2026)

(a) Folder's own mentions: NOTES.md and REQUEST.md name no decipherment, key, gloss or clear copy; the catalogue says
only "teilweise chiffriert". Not found. (b) Other solvers' working files: fresh shallow clones 2 Oct 2026 of
dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, `grep -rliE` hohenlohe, neuenstein, Wilhermsdorf, "Sf 35":
the only "neuenstein" hit is a substring inside a decoded string in cyphersolver/targets/waldeck1744/runs/real_h1.txt
(an unrelated target); nothing on these reports (cited, nothing copied). Not found. (c) Physical neighbours: no images
of Bü 161/165 on disk or known online; neighbouring Bü (e.g. 174, Aktivkapitalien) are catalogue entries only;
unreachable until a copy exists. (d) Recipient side: the recipient is Wolfgang Julius himself; his biography (Ruland
1870, read in full) mentions his chairing of the Franconian counts' college 1679-81 and his 1689 widowerhood and
remarriage at Wilhermsdorf (plausible context for the Vienna "Hausangelegenheiten" mission), but no agents, reports or
cipher. The senders' side (Lic. Melchior; Pape and Köhler) has no printed papers found. Not found.

## GAPS101-hza-hohenlohe-1679 (3 Oct 2026, account-4)

The NEXT-STEPS row (24 Sep) named step (1), the *Archiv für hohenlohische Geschichte* article read. That step was
already done by GF-A2-7 on 2 Oct 2026 (status line and premise check above: Ruland 1870, pp. 271-290, read in full,
reports and cipher not mentioned), so it was not repeated. Ran the next named step instead, (2): do the HZA Neuenstein
units resolve to an LABW record and to images?

Route: LABW online finding-aid system (www2.landesarchiv-bw.de/ofs21), plain curl with a browser UA, about 2 s apart.
Findbuch Sf 35 "Wilhermsdorf I / 1650-1719" (bestand 19846; finding-aid permalink f=3-543), section "3. Graf Wolfgang
Julius und Gräfin Franziska Barbara / 3.1. Persönliche Angelegenheiten und Korrespondenzen". Signature search, then the
unit's print view (druckansicht.php):

| Unit | id_titlaufn | Permalink (quoted from the record) | Titel / Enthält | Laufzeit | Umfang |
|---|---|---|---|---|---|
| Sf 35 Bü 161 | 974107 | http://www.landesarchiv-bw.de/plink/?f=3-88062 | Berichte (teilweise chiffriert) des Lic. Melchior an Graf Wolfgang Julius aus Wien, Prag und Straßburg. **Enthält: Beilage: Chiffrierschlüssel.** | 1679-1680 | 1 Fasz., Folio |
| Sf 35 Bü 165 | 974111 | http://www.landesarchiv-bw.de/plink/?f=3-88066 | Berichte (teilweise chiffriert) der in Hausangelegenheiten nach Wien entsandten Diener Kanzleirat Johann Christoph Pape und Kammersekretär Georg Ludwig Köhler. | 1689 | 1 Fasz., Folio |

Availability: neither record carries a digitisation link or image field; each offers only "Einheit in den Bestellkorb
übernehmen" (an order basket). The LABW list "Findbücher mit digitalem Archivgut" (suche/findbuecher_dimag.php) names
no Hohenlohe-Zentralarchiv finding aid. So: **undigitised, orderable through LABW's own order system** (the HZA is
maintained by the Landesarchiv as a branch of the Staatsarchiv Ludwigsburg, per LABW's site and Wikipedia), not
only by direct application to a private archive as REQUEST.md first assumed.

Correction to the 24 Sept sweep: "Both finding-aid titles give no indication of an attached key" was read from the
unit title only. The full unit record for **Bü 161 lists a key as an enclosure ("Beilage: Chiffrierschlüssel")**. Once
a copy exists, Bü 161 is a key-application (recovery) job, not cryptanalysis. Whether the same key also serves Bü 165
(1689, different senders) is untested. Neighbour noted: Bü 162 (Köhler's reports from Neuenstein, 1680-81), with no
cipher in its title.

Not found: a decipherment, plaintext or image of either unit. Requests: www2.landesarchiv-bw.de 10, WebSearch 1.
No vision calls, no subagents.

**Recommended next steps (refreshed 3 Oct 2026):** (1) [done 2 Oct, GF-A2-7] AfhG article; (2) [done 3 Oct, this
section] LABW records: undigitised, orderable, Bü 161 encloses a key; (3) copy order for Bü 161 first, key leaf
included (REQUEST.md, the owner's step), then Bü 165; nothing runnable in the cloud remains until copies exist.

## While waiting

- Search the LABW finding aids (ofs21 full-text search, Hohenlohe-Zentralarchiv scope) for other "Chiffre"/"Chiffrierschlüssel"/"chiffriert" units of Wolfgang Julius or his agents (1670-1698), and check each hit's record for a digitisation link; a digitised sibling key or a ciphered letter from the same agent would give a copy-free start. About 10-20 LABW requests, no vision, about USD 1.
