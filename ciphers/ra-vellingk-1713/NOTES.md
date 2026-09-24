# Mauritz Vellingk reports partly in cipher, Hamburg exile, 1713-1714

**Status: open**

## Item

Mauritz Vellingk (1651-1727, former Swedish governor-general of Bremen-Verden, general and privy councillor),
reports sent partly in cipher from Hamburg after the Danish conquest of Bremen-Verden (occupied from late
1712), plus his own collected copies referencing the 1713 neutrality treaty. Two related holdings, same
repository:
1. SE/RA/1411/E/E VI/1 (Kanslikollegium, "Inkomna handlingar / Skrivelser i utrikesärenden samt ansökningar
   till diplomat- och konsulstjänster"), catalogue note: "Från M. Vellingk, förutvarande generalguvernör i
   Bremen-Verden, som efter dessa provinsers erövring av danskarna vistades i Hamburg utan egentligt uppdrag men
   sände rapporter, delvis i chiffer." (from M. Vellingk, former governor-general of Bremen-Verden, who after
   the provinces' conquest by the Danes stayed in Hamburg without formal assignment but sent reports, partly in
   cipher).
2. SE/RA/720626/E/E 6015 (Mauritz Vellingks samling, "Avskrifter"), catalogue note: "Avskrifter. Chiffer.
   Handlingar angående neutralitetstraktaten 1713." (copies. Cipher. Documents concerning the 1713 neutrality
   treaty).
Riksarkivet i Stockholm/Täby. Found by the LANE S scout of 24 September 2026, QUEUE.md row R7, kind:
cryptanalysis (no key is catalogued alongside either holding).

No transcription or image exists in this repository; `ciphertext.txt` is not created (rule 2).

## Check-solved sweep, 24 September 2026

Run directly by this worker, per `.claude/briefs/check-solved.md`'s six sources. 6/6 checked, 0/6 found a
solution, key transcription, or documented prior attempt.

**Editions first:** the relevant documentary-edition candidates named in the row (Sveriges traktater med
främmande magter, and Karl XII's letters, ed. Ernst Carlson) were checked for digitisation:
`archive.org/advancedsearch.php?q=title%3A(Sveriges+traktater)` returns 0 hits, and a plain-text search for
`Vellingk` across all of Internet Archive full text (`archive.org/advancedsearch.php?q=Vellingk`) also returns
0 hits — neither series, nor any other IA-held volume, is reachable there. Not checked on HathiTrust this pass
(no HTRC Extracted Features run for "Vellingk" — should be the next step given both editions are far more
likely to be a HathiTrust-only German/Swedish scholarly series than an Internet Archive Google-scan). The
German Wikipedia article on Vellingk (`de.wikipedia.org/wiki/Mauritz_Vellingk`, fetched directly) covers his
1712-1714 Hamburg period and the 1713 burning of Altona in detail but cites no edition of his Hamburg reports
or any cipher, and mentions no decipherment.

**Web:** WebSearch "Mauritz Vellingk Hamburg 1713 chiffer rapport Bremen Verden" — results (Wikipedia,
Bremen-Verden campaign pages, a Niedersachsen Arcinsys archival finding-aid entry, a Rigsarkivet Bremen-Verden
register) confirm the historical context (Vellingk in Hamburg from Sept 1712, the Altona affair) but no mention
of a cipher report or any decipherment.

**Community lists:** `sources/cryptiana/` grepped for "vellingk" — no hits.

**DECODE:** not logged separately — same session, same negative result as R1-R3 (no login attempted per this
brief; de-crypt.org not indexed by the web search engine for this name).

**Bourdeau:** same shallow clone. `grep -rli "vellingk"` across the whole tree — no matches at all.

**Aymeloglu:** same shallow clone, same grep — no matches.

**Riksarkivet digitisation check:** queried `text=chiffer Vellingk&type=Record` (1 retried transient
`SSL_ERROR_SYSCALL`, 200 on the retry after a ~5s pause). 2 hits, matching both of this row's shelfmarks.
SE/RA/720626/E/E 6015: `onlyDigitisedMaterials: false`. SE/RA/1411/E/E VI/1: `onlyDigitisedMaterials: false`.
**Neither is digitised.** No IIIF manifest or image link for either.

**Verdict:** open. No prior solution, key transcription, or attempt found anywhere searched. This is the one
cryptanalysis-kind row of the four in this batch — no key is catalogued with either holding, so even after a
copy is obtained, this would need either the key found elsewhere (a Kanslikollegium chiffernyckel volume from
the same 1712-1714 window) or a genuine ciphertext-only attack with a matched control (rule 3), not a
straightforward key application.

**Not digitised — copy order needed.** See REQUEST.md.

## Request log

24 Sept 2026: no personal data logged here.
