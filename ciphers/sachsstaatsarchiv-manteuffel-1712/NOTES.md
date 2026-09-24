blocked

# Krauske's 1893 decipherment of Manteuffel's 1712-13 reports to Flemming — SHStA Dresden (print check only)

QUEUE row: DA4 (sources/solver-diffs/2026-09-24-lane-n2-dea.tsv, "German state archives, online finding aids
(LANE N2 scout of 24 September 2026)"). **Per brief: this target gets a print check only, not a full
check-solved campaign** — the question is whether Krauske's 1893 decipherment was ever printed.

## Source

Sächsisches Hauptstaatsarchiv Dresden, **10026 Geheimes Kabinett**:
- **Loc. 00694/10 (08/09)**: "Chiffren in Schreiben Manteuffels an Flemming (angefertigt von Dr. Krauske,
  1893)[.] Enthält u. a.: Einige Chiffre-Auflösungen zu den Berichten Manteuffels an Flemming 1712 und 1713,
  (Loc. 694/08 und Loc. 694/09)." — i.e. the underlying 1712-13 ciphered reports are Loc. 694/08 and /09; a
  set of cipher solutions ("Chiffre-Auflösungen") made by "Dr. Krauske" in 1893 is filed with them at Loc.
  694/10.

Correspondents: **Ernst Christoph von Manteuffel** (1676-1749), Saxon diplomat, close collaborator of
**Jakob Heinrich von Flemming** (1667-1728), directing Saxon-Polish cabinet minister from 1712 (both confirmed,
Sächsische Biografie/ISGV, WebSearch 24 Sept 2026). **"Dr. Krauske"** is almost certainly **Otto Krauske**
(1859-1930), a Prussian-trained historian and archivist active in this period (Wikipedia; "Historiker und
Archivar im Dienste Preußens" festschrift, 2015) — his other confirmed editorial work, *Die Briefe König
Friedrich Wilhelms I. an den Fürsten Leopold zu Anhalt-Dessau 1704-1740*, is Prussian court correspondence of
the same general era, consistent with an archivist capable of and likely to be commissioned for this kind of
deciphering/editing work at a state archive; not independently confirmed as the same Krauske who worked at
Dresden specifically.

## Print check (24 September 2026)

1. **The 1893 year itself.** *Neues Archiv für sächsische Geschichte* is the standard Saxon regional-history
   journal (named in the brief) and its volume 14 corresponds to 1893 (annual since vol. 1 in 1880). Full-text
   searched on archive.org (`neuesarchivfur14sach`, be-api fts): "Manteuffel" — **0 hits**. "Flemming" — 1 hit,
   p.394, but it is a genealogical article on Bautzen-area surnames ("Flemming, Bautzner Familie... Flemming,
   Feldmarsch.") mentioning the Flemming surname's local origin, not Ernst Christoph von Manteuffel's 1712-13
   reports or any cipher solution. **Real negative**, not just an unreached source.
2. **The five years after (1893-1898), per the check-solved brief's rule for editors who could not find a key —
   here inverted: an editor who could find and print a key sometimes published a fuller article on the
   correspondence afterward.** Not run this pass (budget) — a real gap.
3. **Biographical/secondary literature.** Sächsische Biografie (ISGV) entries for both Manteuffel and Flemming
   were found by WebSearch and read at snippet level; neither snippet cites Krauske's 1893 Chiffre-Auflösungen
   or quotes deciphered text from the 1712-13 reports. One modern secondary source (a ResearchGate paper on
   August Christoph von Wackerbarth / the "Société des antisobres", found by WebSearch) cites the archival
   fond "SächsHStAD, 10026, Geheimes Kabinett, Chiffren de S. Exc. Mgr. le C. de Flemming, Loc." — i.e. a
   *different*, French-titled sub-series within the same Geheimes Kabinett bestand, used as an archival source
   by a modern historian, not a printed edition of Krauske's 1893 work and not confirmed to be Loc. 694/08-10
   specifically. Not opened in full this pass (WebFetch on the PDF was not attempted — flagged, not run).
4. **Community lists / DECODE / solver repositories.** `sources/cryptiana/`, `sources/decode/`, and fresh
   shallow clones of both solver repos grepped for "Manteuffel", "Flemming", "Krauske": zero hits in all three
   (shared search pass with the other five targets this run; see their NOTES.md for the same negative).
5. **Haake's Flemming studies** (named in the brief) — Alfred Haake wrote a standard early-20th-c. biography of
   Jakob Heinrich von Flemming; not located/opened this pass — a real gap, flagged for a follow-up.

## Verdict

**Not found printed** in the one source checked in full (Neues Archiv für sächsische Geschichte 1893, the
publication year itself) — a real negative, not an unreached-source placeholder. The five-years-after sweep,
Haake's Flemming biography, and full reading of the Wackerbarth/Société-des-antisobres paper are not done this
pass and are the concrete next steps. **Krauske's decipherment already exists in the archive**, so this is not
a fresh cryptanalysis or recovery target regardless of the print-check outcome: if unprinted, the natural
product is a *transcription of Krauske's own 1893 reading* (a contribution, once a copy of Loc. 694/10 is in
hand), not a new solve. **Status: blocked** — no image of Loc. 694/10 resolved to a working URL (scout's
original sweep saw a `#digitalisat` anchor that did not resolve in a 4s render), and the print-check gaps above
(five-years-after journal sweep, Haake, full reading of the one secondary-source lead) are not closed. Not
nominated to the board: per the brief, this is a print check, not a check-solved campaign, and the target's own
`kind` (recovery/contribution) does not fit a cryptanalysis nomination in any case.

**Recommended next steps (not run this pass):** (1) run *Neues Archiv für sächsische Geschichte* vols. 15-19
(1894-98) through the same be-api fts for "Manteuffel"/"Chiffre"; (2) locate and read Haake's Flemming
biography; (3) read the Wackerbarth/Société-des-antisobres ResearchGate paper in full for its citation context
around "Chiffren de S. Exc. Mgr. le C. de Flemming, Loc." and check whether it resolves to Loc. 694 specifically;
(4) resolve the Sächsisches Staatsarchiv `#digitalisat` anchor on Loc. 694/10 to a working image URL or confirm
it does not serve one.
