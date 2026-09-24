open

# Jan van Nassau to/from Willem van Oranje, seven cipher letters, 1572-1575

QUEUE row: WV1 (`QUEUE.md`, "Willem van Oranje correspondence: unsolved cipher letters (LANE N harvest of 24
September 2026)"). Brief `.claude/briefs/runs/2026-09-24-lane-n-csWV.md`.

## Source

Seven letters between Willem van Oranje and his brother Jan (VI) van Nassau, all citing Koninklijk Huisarchief
Den Haag (KHAG) and Groen van Prinsterer's edition (GPA) as the manuscript's archival/edition trail, none
carrying a solution word (oplossing/opgelost/ontcijferd) in the WVO database's own Opmerkingen field:

| briefnr | date | direction | place | cipher extent | GPA citation |
|---|---|---|---|---|---|
| 5200 | 18 Oct 1572 | to Jan | Zwolle | mainly ("Grotendeels in cijferschrift") | IV, 2-6 nr. CCCLXXXIX |
| 5207 | 23 May 1574 | to Jan | Gorinchem | mainly | not fetched this pass |
| 5213 | 26 Nov 1574 | to Jan | Delft | mainly | not fetched this pass |
| 5218 | 4 Mar 1575 | to Jan | Dordrecht | partly | not fetched this pass |
| 5221 | 30 Jul 1575 | to Jan | Dordrecht | partly | not fetched this pass |
| 5222 | 29 Sep 1575 | to Jan | Dordrecht | partly | not fetched this pass |
| 5549 | 21 Nov 1573 | from Jan | Dillenburg | partly | not fetched this pass (GPAS, the Groen supplement) |

Full detail-page text fetched and read directly this pass only for 5200 (the rest rely on
`sources/wvo/cipher-letters-2026-09-24.tsv`, itself built from each letter's full Opmerkingen text by the
harvest worker, truncation-checked -- see `sources/wvo/NOTES.md` item 4; none of these seven briefnrs was among
the three rows flagged as truncated there).

**5200's WVO record, read directly** (https://resources.huygens.knaw.nl/wvo/app/brief?nr=5200): Opmerkingen
"Grotendeels in cijferschrift." (no solution word). Content summary: report on the miserable state of the
revolt (surrender of Mons, plundering of Mechelen, garrison withdrawals) and the decision to withdraw
definitively to Holland and Zeeland. Bron: Groen van Prinsterer, Archives d'Orange-Nassau, **IV, 2-6, nr.
CCCLXXXIX** -- no "(onv)" incomplete flag shown in the citation itself (contrast 10260/WV4 below, where "(onv)"
is explicit), which is not the same as confirming the printed text includes the cipher passages deciphered;
not checked directly against the DBNL/Groen tome IV text this pass (see "Search gap" below).

**Confirmed by eye this pass** (`images/05200_p1.png`, fetched from
`resources.huygens.knaw.nl/media/wvo/images/05000-05999/05200.pdf`): continuous French prose ("Monsieur mon
frere, J'ay heu response...") with dense numeral-cipher groups (two- and sometimes three-digit, values seen up
to at least 98, e.g. "25.31.74.17.20.25.40.51.15...") running through most of the page -- a genuine, extensive
numeral nomenclator cipher, consistent with "grotendeels in cijferschrift." The other six letters' PDFs were
not fetched or viewed this pass (budget; per brief item 3, one page per circle satisfies the eye-check).

**Solved siblings in the same circle** (per the QUEUE.md WV1 row, from the harvest worker's classification, not
independently re-verified this pass): briefnrs 5198 and 5199 both marked "solved on leaf" (afgebeeld) --
5198 is in fact the autograph of the already-known found-solved orange-nassau-1572 letter
(`ciphers/orange-nassau-1572/NOTES.md`), so this circle overlaps directly with a target already resolved
there; 5033 "solved via Groen van Prinsterer"; plus the already-queued NB6 (briefnr 5551, two lines only,
Jan van Nassau reporting the accident that killed Lodewijk van Nassau at Mookerheyde) and NB4's fetched
candidate 5564 ("opgelost cijferschrift", per `ciphers/la-garde-1577/NOTES.md`'s image-capture section) in the
same correspondence circle.

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents), per `.claude/briefs/check-solved.md`.

1. **Editions first.** Groen van Prinsterer, *Archives ou correspondance inédite de la maison d'Orange-Nassau*,
   1re série, tome IV (1572-1574) and tome V (1574-1577) are the correct editions for this date range (tome IV
   confirmed directly against 5200's own citation above; both tomes already located and confirmed readable on
   DBNL by the sibling worker for `ciphers/lodewijk-van-nassau-1573-74/NOTES.md`, same house/correspondence, not
   refetched here). **Search gap, same shape as that sibling folder:** this worker did not exhaustively check
   the DBNL text of tome IV pp.2-6 (5200) or locate the tome IV/V pages for the other six dates (23 May 1574,
   26 Nov 1574, 4 Mar 1575, 30 Jul 1575, 29 Sep 1575, 21 Nov 1573) letter-by-letter; DBNL's tome-level table of
   contents proved unreliable to parse via a summarising fetch tool in the sibling folder's own attempt, and
   this worker did not repeat that attempt within budget. This verdict rests on WVO's own curatorial silence
   (no solution word in any of the seven Opmerkingen fields) plus the sweep below, not on a page-by-page reading
   of Groen's tomes.
2. **WVO database's own curatorial silence.** None of the seven Opmerkingen fields carries oplossing/opgelost/
   ontcijferd/déchyffré, in contrast to the circle's own solved siblings (5198, 5199, 5033, 5564) which the
   harvest worker's classification did flag with those words or an "afgebeeld" marker. The editors are
   evidently willing to note a solution in this same Bron/Opmerkingen apparatus when one exists (see WV3/WV4
   below for direct examples), so the absence across all seven is meaningful, though not conclusive (rule 10).
3. **Community lists.** `sources/cryptiana/web/dutch.htm` (repo snapshot, read via `tools/html2text.py`): no
   mention of Jan van Nassau or any of these seven letters/dates; general Dutch cipher-history material only
   (Marnix as decipherer from 1576, Huygens, d'Alaume). WebSearch (`"Jan van Nassau" Willem van Oranje 1572 1575
   cijferschrift ontcijferd`) returned only general Dutch Revolt history (DBNL Swart, Wikipedia); one hit found
   an unrelated 1579 Jan-van-Nassau-to-Oranje letter already published on DBNL (Nederlandse historische bronnen
   4, `_ned017198401_01_0064.php`) -- a different date, not checked further, not one of the seven.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for nassau/oranje: zero hits.
5. **Solver repositories.** Fresh shallow clones this pass (24 Sept 2026, shared across all four WV targets):
   `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`, grepped for nassau/oranje/orange/schwarzburg/
   marnix. All cyphersolver hits are unrelated 18th-century Orange-Nassau items (Willem Frederik/Prince William
   V correspondence, 1795-1804) or the already-catalogued Mondoucet-to-Charles-IX dispatch (about, not by,
   Louis of Nassau, already read/printed per Bourdeau's own SOLVED_RANKING.md). Neither repository names Jan
   van Nassau or any of these seven letters. unsolved-ciphers: zero hits for any of the four search terms.
6. **General web search.** As item 3.

## Verdict

**Status: open** (all seven: 5200, 5207, 5213, 5218, 5221, 5222, 5549). No solution, key, plaintext or
documented attempt found in six sources. Caveat as in item 1: the standard printed edition was located and one
citation (5200, tome IV pp.2-6) confirmed to exist, but not read page-by-page for any of the seven; the verdict
rests on WVO's curatorial silence plus the sweep, not a direct reading of Groen's text.

**Copy status: copy-free.** Free PDF scans confirmed reachable (HTTP 200); one (5200) viewed by eye and cipher
confirmed present. The other six not fetched this pass; a future capture worker can reuse the `pdf_url` pattern
in `images/manifest.json`.

**Kind: recovery** (via the circle's solved siblings -- 5198/5199 solved on leaf, 5033 via Groen, and the
already-queued 5551/5564 -- an alignment problem per LESSONS.md §2, not cryptanalysis from scratch. Nobody has
yet attempted that alignment; this pass only confirms the seven target letters exist, are reachable, and carry
genuine cipher).

**Next step (not this brief's scope):** fetch and image the remaining six letters; locate and image 5198/5199/
5033's decipherments (5198's autograph is already imaged at `ciphers/orange-nassau-1572/`'s WVO record, but its
1842 Nepveu tot Ameyde decipherment is not yet transcribed anywhere in this repo); test whether the same key
covers 5200 and the other six.
