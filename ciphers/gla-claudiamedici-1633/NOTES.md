open

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
