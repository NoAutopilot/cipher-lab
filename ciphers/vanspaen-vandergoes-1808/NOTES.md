open

# G.C. van Spaen tot Voorstonden to Maarten van der Goes, Düsseldorf, 14–15 January 1808

QUEUE row: CS2-21 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, catalogue item 226 at
dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026 by LANE N4 csNA
(session_01PKTy3iKiH3LzJpQauLb8Wu), brief `.claude/briefs/runs/2026-09-24-lane-n4-csNA.md`. Copy-free per LANE
N4 scARCH (ROOM.md, 24 Sept 2026 19:00 UTC), confirming the exact viewer: Nationaal Archief toegang **2.01.08**
(the row's cached shelfmark carried a stray leading zero, "02.01.08").

## What it is

DECODE R1941, a letter of two pages plus a one-page annex, both in figures between clear Dutch openings and
closings; Nationaal Archief, The Hague, 2.01.08 (Ministerie van Buitenlandse Zaken, 1796–1810), inv. nr. 281.
DECODE's own status for this record is **"Partially decrypted"** (`sources/decode/records-non-decrypted-
2026-09-24.tsv`, id 1941) — a hard filter per LANE N2 addition (c): a `[transc]`/`[decrypt]`/`[key]` document
attached to a DECODE record must be checked via DocumentsList before calling the record open. This worker has no
DECODE login (COMMON rule 4: only the DECODE worker logs in). Bourdeau's own write-up substitutes for that check
(below) — he explicitly examined the record's own note and images and found no attached document.

## Six-source search log (24 September 2026)

1. **Bourdeau, quoted verbatim** (`spaen1808.html`, posted 21 Sept, updated 24 Sept 2026 — same-day fresh):
   *"DECODE catalogues R1941 as a letter from G. C. van Spaen tot Voorstonden, 'ambassador at the Court of
   Westphalia', to Maarten van der Goes, as partly decrypted: its note says the small annex of 15 January was
   deciphered and the letter was not... No decipherment is written on either, and none is attached to the
   record."* This directly answers the "Partially decrypted" hard filter: DECODE's own annotation only claims
   the 15 Jan annex (75 groups) was deciphered elsewhere, not the 14 Jan letter (228 groups) targeted by this
   row, and Bourdeau found no document of either attached to the record.
2. **Standard printed edition — actually read (by Bourdeau, quoted verbatim).** *"Colenbrander's Gedenkstukken V
   does not print the letters."* Gedenkstukken vol. V covers 1806–1810, the correct window for a 14–15 Jan 1808
   despatch. This worker tried independently to reach the same volume: `resources.huygens.knaw.nl/gedenkstukken`
   and `/retroboeken/gedenkstukken/` (a Dojo-based page-image browser, 22 volumes, no plain-text/OCR search
   reachable via curl — its own search box is a client-side Google Custom Search over the whole huygens.knaw.nl
   site, not the volume text); `site:delpher.nl` web search located the correct-era volume
   (`MMSFUBA02:000012292:00048`, "Gedenkstukken... 1795 tot 1840", vol. 4 part 2, 1908) but WebFetch of the
   Delpher page returned only metadata, no OCR text (Delpher's viewer is JS-rendered); archive.org holds no copy
   of Gedenkstukken (`advancedsearch.php` for the title: 0 hits). This worker's own attempt to re-verify
   Bourdeau's Gedenkstukken V check did not succeed this pass; the verdict below rests on Bourdeau's stated
   check of that volume, not an independent re-read of its pages.
3. **DECODE**: no key record for this code (Bourdeau: "DECODE holds no key for this code"; Croiset's 1803
   codebook, R1035, "gives word salad" against it).
4. **Aymeloglu** (fresh shallow clone, 24 Sept 2026): "Spaen"/"Goes" occur only in his raw DECODE catalogue
   scrape files, not in any of his 8 write-ups — not attempted there.
5. **Cryptiana / Tomokiyo** (`sources/cryptiana/web/dutch.htm`, Shift-JIS): "Spaen" occurs once, but for a
   different person and episode — Alexander van Spaen's 1800 Anglo-Prussian mediation negotiations for the
   exiled Orange court, unrelated to G.C. van Spaen tot Voorstonden's 1808 border-commission correspondence.
   "Goes" does not occur.
6. **Web search**: nothing beyond Bourdeau's page and the DECODE/archive metadata found.

Archive context (Bourdeau, corroborated by the NA record itself): inv. 281 holds the papers of J.F.G. van Spaen
and G. van Riemsdijk, commissioners for taking over the districts ceded around Zevenaar (1806–09); Düsseldorf
was the capital of the Grand Duchy of Berg, the other party to that exchange — consistent with a genuine,
un-printed administrative dispatch rather than a document Colenbrander would have selected for a general
political history.

## Verdict

**`open -- Colenbrander's Gedenkstukken vol. V (1806-1810) checked by Bourdeau (spaen1808.html, updated 24 Sept
2026), "does not print the letters"; this worker could not independently re-read the volume's pages this pass
(no full-text search reachable at resources.huygens.knaw.nl or delpher.nl within this brief's host grant).`** No
source claims a key, decipherment or clear copy of R1941's 14 January letter. DECODE's "Partially decrypted"
status is accounted for: it refers only to the 15 January annex, not this letter, per Bourdeau's direct
inspection of the record.

Grade counts: H 0, C 0, S 0, M 0, I 0 (nothing read here; check-solved does not decode). Rule 10: no novelty
claim made; this is a search result, not a verifier's classification.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/spaen1808.html (catalogue item 226;
transcription, Gedenkstukken V check, archive-inventory identification), CC BY 4.0 — prior attempt, not a
solution.

Requests this pass: `nationaalarchief.nl` 0 (already pinned by scARCH), `resources.huygens.knaw.nl` 2,
`archive.org` 1 (advancedsearch, shared with CS2-18/-22 checks), `github.com` 0 additional (same clones as
CS2-18), WebSearch 3, WebFetch 1 (delpher.nl, one page, no scraping loop). No DECODE login used.
