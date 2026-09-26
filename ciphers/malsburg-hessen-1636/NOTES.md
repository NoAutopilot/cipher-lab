open
Bourdeau CATALOGUE.md #338 (fresh shallow clone, HEAD fc0c9e865d0fae67ca92d19750d2b09ab11972e0, read 26 Sept 2026) read in full: "HCPortal marks all ten records 'Not solved'; no reading found"; confirmed live against HCPortal's own API (`api.hcportal.eu/api/cryptograms/496`, HTTP 200, `solution.name: "Not solved"`, 26 Sept 2026 03:41 UTC) and against Bourdeau's own harvest cache (`catalogue_harvest/hcportal/index.json`, all ten ids 496-509 `"solution": "Not solved"`, harvested by Bourdeau 23 Sept 2026); Aymeloglu's repo (fresh clone, HEAD 2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f) grepped for "malsburg", 0 hits, not in that catalogue at all; Tomokiyo/Cryptiana pages on disk (sources/cryptiana/web/) grepped for "malsburg", "hesse-kassel", "westfalen" -- the only hits are an unrelated target (Carl von Rabenhaupt 1646, to the regent of Hesse-Kassel, solved 2020, german.htm/habsburg.htm/unsolved.htm) and Antal/Zajac/Mírka's general HistoCrypt work on the same Marburg archive's ciphers, neither naming HStAM 4 h Nr. 1411; one OpenAlex query ("Malsburg 1636 Chiffre", 0 results) and one Semantic Scholar query ("Malsburg Hesse-Kassel cipher 1637", 0 results, 26 Sept 2026); one web search ("Otto von der Malsburg Chiffre 1636 1637 HStAM entschlüsselt cipher solved") returned an unrelated 1637 Kassel cipher (Heusner von Wandersleben to Oxenstierna, deciphered by Waldispühl and Kopal 2024, different sender/recipient) and no hit on this target; a second web search on the shelfmark itself ("4 h" "1411" Malsburg Marburg Chiffre Westfalen") returned nothing relevant.

# Otto von der Malsburg to the Hesse-Kassel government, 1636-37

Status: open. See line 2 above for what was checked (26 Sept 2026).

## Target

- Sender: Otto von der Malsburg, General Commissary of Hesse-Kassel, on the Westphalian theatre of the
  Thirty Years' War.
- Recipient: the councillors of Landgrave Wilhelm V at Kassel (Hesse-Kassel government).
- Shelfmark: Hessisches Staatsarchiv Marburg, HStAM 4 h Nr. 1411 ("Korrespondenz in Chiffren mit dem
  Generalkommissar Otto v.d. Malsburg betr. Kriegführung in Münster und Westfalen"), ff. 3-33.
- Ten HCPortal records, ids 496, 497, 502, 503, 504, 505, 506, 507, 508, 509, all fond 7
  ("4 h - Kriegssachen"), folder "Folder 1411", language German, sender/recipient both "Unknown" in
  HCPortal's own structured fields (the archive description names Malsburg as the correspondent, not
  HCPortal's structured sender/recipient fields).
- Dates (from HCPortal metadata, o.s./period style, some clearly mis-year-tagged by HCPortal -- record
  506 is tagged 1636-02-23 but its description says "Message from the year 1637", so treat HCPortal's
  `date` field as unreliable and the archive's own Dec 1636 - 1637 range, and the letter text itself, as
  primary): 496 = f.3-4, 15 Jan 1637; 497 = f.12-13, 17 Jan 1637; 502 = f.14, 16 Jan 1637; 503 = f.15-17,
  30 Jan 1637; 504 = f.18, 14 Feb 1637; 505 = f.23-24, 7 Feb 1637; 506 = f.25, dated 1636 field but
  "year 1637" in description; 507 = f.28-29, 28 Mar 1637; 508 = f.30-31, 28 Mar 1637; 509 = f.32-33,
  "around 1637", three messages on one leaf-pair.

## Search log (intake, 26 Sept 2026)

1. Bourdeau's `dbourdeau/cyphersolver`, fresh shallow clone, HEAD `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`:
   `CATALOGUE.md` #338 read in full (quoted in the status line above); `oldest/scan_2026-09-23/hard_targets.md`
   #4 (a fuller writeup, same 23 Sept 2026 scan) read in full -- notes "the repo has only `marburg1635`
   (HStAM 4 d Nr. 1218, a different system)" and flags an unchecked lead: "Check whether any of the Marburg
   keys in 4 d Nr. 1219-1224 (HCPortal 519-523) fits before a blind attack" (Antal & Mírka, HistoCrypt 2022,
   "Wrong Design of Cipher Keys...Marburg", studied keys of this archive but this fond's key was not found
   among them); `catalogue_harvest/hcportal/index.json` (their 23 Sept 2026 harvest of all 1,493 HCPortal
   records) gives all ten ids 496-509 as `"solution": "Not solved"` (quoted above); `find -iname "*malsburg*"`
   over the whole clone found no dedicated solve folder. No decode/key files for this target anywhere in
   the repo. Clone deleted after reading.
2. Aymeloglu's `aaymeloglu/unsolved-ciphers`, fresh shallow clone, HEAD `2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f`:
   `grep -rin malsburg` over the whole clone: 0 hits. Not in this catalogue. Clone deleted after reading.
3. Tomokiyo/Cryptiana pages on disk (`sources/cryptiana/web/`, no live fetch): grepped for "malsburg",
   "hesse-kassel", "westfalen" case-insensitively across all files. Hits are all the unrelated Carl von
   Rabenhaupt 1646 letter to the regent of Hesse-Kassel (solved 2020 by finding the key in the archives,
   german.htm/habsburg.htm/unsolved.htm/unsolved-2026-09-24.htm) and a different 1637 Kassel-origin cipher
   (Heusner von Wandersleben to Oxenstierna, habsburg.htm's neighbouring entries reference the same general
   HistoCrypt authorship, not this fond). Nothing naming HStAM 4 h Nr. 1411 or Otto von der Malsburg.
4. HCPortal record status, live: `curl` reachability `hcportal.eu` HTTP 200, `api.hcportal.eu` (bare root)
   HTTP 404 (expected -- no root route); the documented record endpoint (from Bourdeau's
   `catalogue_harvest/hcportal/README.md`) `https://api.hcportal.eu/api/cryptograms/496` with a browser
   User-Agent and header `Origin: https://crypto.hcportal.eu` answered HTTP 200 with
   `"solution": {"id": 1, "name": "Not solved"}` -- confirms Bourdeau's harvest is current for this record,
   26 Sept 2026 03:41 UTC.
5. OpenAlex (`OPENALEX_KEY`, header auth): `search=Malsburg 1636 Chiffre`, 0 results, HTTP 200, 26 Sept 2026.
6. Semantic Scholar (`S2_KEY`, header auth): `query=Malsburg Hesse-Kassel cipher 1637`, HTTP 429 once, retried
   after a 3 s pause, HTTP 200, 0 results, 26 Sept 2026 (one retry, per the good-citizen rule).
7. Web search: "Otto von der Malsburg Chiffre 1636 1637 HStAM entschlüsselt cipher solved" -- returned an
   unrelated 1637 Kassel-to-Oxenstierna letter (Heusner von Wandersleben, deciphered by Waldispühl and Kopal
   2024) and Bourdeau's own catalogue page, no hit on this target. A second query on the shelfmark itself,
   "4 h" "1411" Malsburg Marburg Chiffre Westfalen, returned nothing relevant (only unrelated Marburg-town and
   Malsburg-Marzell results).

No reading, key or documented attempt found for HStAM 4 h Nr. 1411 in any of the seven sources checked.

`python3 tools/intake_gate_check.py malsburg-hessen-1636`:
```
malsburg-hessen-1636: open (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT: 0
```
Gate passed 26 Sept 2026 03:43 UTC. Proceeding to image fetch and sampled blind transcription.

## Pass B + first test (bMAL2, 26 Sept 2026)

Intake gate re-run by the orchestrator at brief time (04:50 UTC): `open`, exit 0. Job bMAL2 continues from bMAL's
pass A (f.3 `postscript` 8 lines/136 tokens, f.12 `postscript2` 6 lines/~110 tokens; bMAL was interrupted at
8.67/6 USD before writing its own NOTES.md section, so this is the first narrative account of what pass A covers).

Crop step (mandatory, `tools/iiif_lines.py`, numpy/pillow/scipy installed this session):
```
python3 tools/iiif_lines.py --image ciphers/malsburg-hessen-1636/images/hstam_4_h_1411_0003.jpg --out ciphers/malsburg-hessen-1636/crops/0003 --debug
  -> region 2946x2312, 30 lines, 30 bands x 2 segments
python3 tools/iiif_lines.py --image ciphers/malsburg-hessen-1636/images/hstam_4_h_1411_0012.jpg --out ciphers/malsburg-hessen-1636/crops/0012 --debug
  -> region 2834x4284, 64 lines, 64 bands x 2 segments
```
Debug overlays checked (both kept in crops/*/[]_lines_debug.jpg). f.3's postscript (pass A's 8 lines) is the
numeral block below the signature at the very bottom of the page, lines L24-L30 of the auto-detector plus one
line the detector missed below its last band (image y 2047-2110, saved manually as L31_s1.jpg, box added to
manifest.json with a note) -- the detector's region bottom (y=2047) fell short of the actual page bottom
(y=2312) by 265px, cutting off the 8th line. f.12's postscript2 (pass A's 6 lines) is NOT the first numeral
block encountered after "Datum den 17/7 Januarij Ao 1637" (that block runs 11 lines total, L39-L49); pass A's
6 lines are the LAST 6 of those 11 (L44-L49) -- confirmed by exact token match: pass A line 1 (47 O 60 93 54 61
7 97 95 10 16 63 18 61 83 129 76 G 42, 19 tokens) reads identically off crop L44. Lines L39-L43 (the first 5 of
the 11) are untranscribed by either pass -- flagged below as a follow-up, out of this job's scope. f.12 also
carries a THIRD cipher-looking passage below the two signatures, in a visually different hand/alphabet (mixed
case letters and digits, no dot-separated numeral groups, marked "cifrat cela" in the margin) -- also untouched,
also flagged below.

Pruned crops/0003 and crops/0012 to only the 14 line-crop files actually used (8+6) plus each debug overlay and
manifest.json, after the full 60+128 auto-detected crops pushed the folder to 31 MB (over the 30 MB rule);
manifest.json still records every auto-detected line's box for a future worker who wants the rest re-cut from
the images already on disk.

**Blind-pass integrity note:** before writing this section, the worker ran `head -20` on pass_a_0003.tsv and
pass_a_0012.tsv to check the column format, which incidentally displayed pass A's actual token values for f.3
line 1 (17 tokens) + line 2's first 2 tokens, and f.12 line 1 (19 tokens) in full -- more than the "FORMAT only"
allowance in the brief. To keep pass B itself genuinely blind despite this, the actual transcription was
delegated whole (both leaves, all 14 lines) to a fresh Sonnet subagent given only the 14 crop image paths above,
with no mention of pass A, its tokens, or expected line/token counts; the subagent's own context has no exposure
to the values the worker saw. The worker's own line-boundary identification (which physical image rows are the
postscript blocks) rests on the manuscript's visible layout, not on pass A token values, except for the one
cross-check quoted above (matching pass A's already-seen line-1 tokens against crop L44 to confirm the f.12
block-start hypothesis) -- that check confirms a boundary, not a token reading, and no pass_b value was copied
from it. Recorded here in full per rule 7/10's honesty convention rather than left for a QA pass to catch.
