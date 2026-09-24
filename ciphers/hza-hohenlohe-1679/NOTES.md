open

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
