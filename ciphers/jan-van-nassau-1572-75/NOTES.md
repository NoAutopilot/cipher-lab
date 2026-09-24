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

## C1: capture and inventory (LANE R2, 24 September 2026)

Per `.claude/briefs/runs/2026-09-24-lane-r2-capture-huygens.md`. All seven targets (5200 rest of pages, 5207,
5213, 5218, 5221, 5222, 5549) plus siblings 5198, 5199, 5033 fetched in full to `images/` (150dpi, JPEG q80;
`images/manifest.json` updated, `images/inventory.tsv` written per page). First render pass used PNG and put the
folder at 128MB; converted the whole folder to JPEG q80 in place, now 23MB, under the 30MB cap. No decoding, no
novelty search, no transcription -- capture and eye-check only, per brief. Host: resources.huygens.knaw.nl, ~19
PDF fetches this pass (>=1.5s apart, descriptive UA), well under the 90-request cap for this worker.

**Flag for the orchestrator and any check-solved re-pass -- printed editions bundled directly in the WVO scans:**
Two of the seven open targets have Groen van Prinsterer's own printed edition pages scanned into the *same* PDF
file as the manuscript, immediately after the manuscript leaves:

- **5218** (4 March 1575, Dordrecht): pages 5-8 of the PDF are Groen, *Archives ou correspondance inedite de la
  Maison d'Orange-Nassau*, **Lettre DXLII, "Le Prince d'Orange au Comte Jean de Nassau"**, pp.141-143, ending
  "Dordrecht, 4 mars[1575]. Guillaume de Nassau." -- date, place, correspondent and signature all match this
  target exactly. The printed text discusses "l'affaire de Besançon", a salt-monopoly (salines) negotiation, and
  names **"le Comte Günther de Schwartzenburg"** -- a direct cross-reference to `ciphers/gunther-van-schwarzburg-1561/`.
- **5222** (29 September 1575, Dordrecht): pages 8-12 are Groen, **Lettre DLXXVII, "Le Prince d'Orange au Comte
  Jean de Nassau. Sieges et combats en Hollande et Zelande"**, pp.280-283, ending "Dordrecht, 29 septembre 1575.
  Guillaume de Nassau." -- again an exact date/place/signature match. Page 7 (between the manuscript and the
  print) is a separate-leaf worksheet of eight numbered plaintext phrases ("1. quand paix affaires de celle de
  Saxe", "...l'instruction don(n)ee au Conte Wolf d'Hohenlohe", etc.) in a different hand from the letter's own
  secretary -- possibly a contemporary briefing note or partial decipherment, not itself verified against the
  ciphertext this pass.

**This was not caught by this same folder's own check-solved sweep above**, which searched WVO's Opmerkingen
field (silent for both) and the solver repositories/DECODE/web, but did not open Groen's tomes IV-V
letter-by-letter -- exactly the gap that sweep flagged as unresolved ("this worker did not achieve an exhaustive
letter-by-letter search... DBNL's tome-level index pages... could not reliably enumerate every entry"). The
printed pages were sitting inside the manuscript's own digitised file the whole time, not requiring the DBNL
search at all. **Per brief, this worker did not read the printed French text closely, compare it word-for-word
to the cipher, or classify novelty/solved status -- that is a check-solved or verifier job, not this one's.** But
5218 and 5222 should not be treated as "open" without that comparison first; the other five targets (5200, 5207,
5213, 5221, 5549) showed no such bundled print in this pass, though 5221's and 5549's own cipher extent looked
lighter/sparser than expected for "partly"/"mainly" and deserve a second look at higher resolution.

**Second flag -- a recoverable key for this whole circle, found on sibling 5198's own bundled print:** 5198's PDF
pages 8-9 are a scan of a **19th-century periodical page** (an "Algemeenen Konst- en Letterbode" Haarlem reprint
of a reader's letter to the editor) that prints a **complete key table** for this cipher: a=3, b=6, c=9, d=12,
e=15, f=18, g=21, h=24, i/j=27, k=30, l=33, m=36, n=39, o=42, p=45, q=48, r=51, s=54, t=57, u/v=60, w=63, x=66,
y=69, z=72 (a straight multiples-of-3 substitution over a merged ~24-letter alphabet), with the note "de overige
cijfers zijn zoogenaamde non-valeurs, ter beveiliging" (the remaining numbers are nulls, for security) -- then
gives the opening plaintext of GPA CCCLXXXV (=5198 itself, "Lettre du Prince d'Orange au Cte Jean de Nassau, datte
de Malines, 21 Sept. 1572)". **Not tested this pass** against any of the seven open targets' ciphertext (out of
brief scope: capture and inventory only, no decoding) -- but the numeral ranges seen by eye in 5200/5207/5213
(mostly 2-digit, up into the 80s-90s) are consistent with a design using 3-72 for real letters plus higher-value
nulls, so this key is the first thing a solver should try before any fresh cryptanalysis. Whether it is the
*same* specific key (same numbers to same letters) across different dates in this correspondence, or just the
same *design* with a fresh mapping each time, is untested.

Per-page detail (content, cipher design, hand) for every page fetched this pass: `images/inventory.tsv`.
5033's scan is heavily faded and this worker's contact-sheet resolution could not confirm its cipher density or
rule out a bundled print of its own "solved elsewhere" edition text -- flagged in inventory.tsv for a closer,
better-contrast pass. No transcription, no key application, no novelty classification this pass.

## J1: key and readings (LANE R2, 24 September 2026)

Worker J1 (Opus, cap $9; Sonnet subagents for passes and alignment). No network use; everything from `images/`.

### 1. Does Groen print the cipher passages of 5218 and 5222? Yes, both, in plain type.

- **5218** (4 Mar 1575). The manuscript p1 (`images/05218_p1.jpg`, last four lines) reads in clear "Par vostre lre du
  xxviij^e jour de janvier dernier passé j'ay veu la poursuyte" then a numeral run
  `106.120.3.22.88.150.122.4.7.66 ...` (57 groups) then clear "a raison par vous alleguee"; margin "Touchant le
  payement d'argent qui est deu a Hans Casimir". Groen, Lettre DXLII, p.141 (`images/05218_p6.jpg`) prints the whole
  sentence in roman type with no italics, brackets or "en chiffre" note: "Par vostre lettre du xxviij^e jour de janvier
  dernier passé j'ay veu la poursuyte du duc Hans-Casimir pour avoir remboursement de quelque argent à luy deu à raison
  par vous alléguée". The Sonnet aligner (`passes/align_5218.tsv`) matched all 5 cipher runs (320 groups, pp.1-3) to
  printed spans in DXLII pp.140-143 (Hans-Casimir; "Quant à l'affaire de Besançon"; two passages on Count Günther
  von Schwarzburg; the Knuetel affair). None is marked as cipher in the print.
- **5222** (29 Sep 1575). Aligner (`passes/align_5222.tsv`): all 10 cipher runs (324 groups, pp.3-5) have their text
  in Groen, Lettre DLXXVII pp.281-282, in plain prose, e.g. "Quant aux affaires de celle de Saxe", "ses parens
  eussent pourveu à son entreténement", "je vous envoyeray mille florins", "l'instruction donnée au Conte Wolff de
  Hohenlohe", "du traicté de mariage passé entre moy et celle de Saxe". The separate leaf p7 (another hand) is a
  numbered summary of the same cipher passages in order (items 2-8, header "Le conte Palatyn"): a contemporary
  decipherment note for this letter.
- So 5218 and 5222 are alignment pairs, and their cipher passages are known in print (Groen 1^re série t.V). Status
  question flagged to LANE N in ROOM; not classified here.

### 2. The printed 1572 table does not read 5218 or 5222; neither does the Lodewijk key

`key_1572.tsv` is the table printed in the Konst- en Letterbode reprint (5198 PDF p8, p.19): a=3 b=6 ... z=72 in steps
of 3 (i/j 27, u/v 60, w/x 66; 63 printed as '....'), "de overige cijfers zijn zoogenaamde non-valeurs". Grade H
for every row (a printed key source); rows 1-99 not multiples of 3 are the printed "non-valeurs" (NULL, H).

- 5222 under key_1572: of 324 groups, 60 fall on a table letter, 194 on a "null", 65 are above 99 (not in the table);
  the letters give no French (`c######a.......d..#..l...i.....ir...`). Values run 1-158, codes above 100 recur (111,
  112, 116-134), 28/29/27/26 are the commonest. A different, larger nomenclator.
- 5218 likewise (values 1-329, e.g. 106, 120, 150, 329 in the Hans-Casimir run, and many non-multiples of 3 in letter
  positions).
- R18's Lodewijk table (`../lodewijk-van-nassau-1573-74/key.tsv`, 139 values) applied to the 5222 runs gives no French
  either (run "donnée au Conte Wolff de Hohenlohe" -> `nosvzeedfqevaznrazzssnpf??`).
- An exploratory hard-EM aligner (`align/em_align.py`) over the positional alignments found no value with >=4
  occurrences mapping >=75% to one letter: the single positional alignment is too loose (nulls and word codes shift
  every span) to build a key from. Recovering the 1575 key from these two printed pairs is a known-plaintext job for
  a later brief (suggestion below), not done here.

### 3. Progress at the cap (24 Sep 2026 09:44 UTC; stopped by the lane orchestrator at $12.6 on a $9 cap)

- key_1572.tsv (H, printed table) committed; spot check on 5200 p1 by eye reads under it: "36.15.39.57" = MENT,
  "3.57.27.42.39" = ATION, "51.3.39.12" = RAND, "57.15.33" = TEL, with non-multiples of 3 as nulls. Not yet a graded
  reading: no reconciled ciphertext, no decode.json, decode_key.py not run. No H/C counts to report.
- Blind passes on disk at stop (rows): passA_5200.tsv 835;. Committed as they stood; passes were still running, so
  the last letter of each may be partial. Not reconciled.
- Not started: 5221, 5549 passes; reconciliation; decode.json; readings.
- Next (suggestions): (a) finish passes B, run tools/reconcile_passes.py per letter, settle disagreements.tsv, add
  decode.json (tsv format, clear_prefix 'w:', key key_1572.tsv) and run decode_key.py --check for 5200/5207/5213;
  (b) 5218/5222: known-plaintext recovery of the 1575 nomenclator needs a careful group-by-group aligner pass
  (the positional ones in passes/align_*.tsv are too loose), then test the resulting key on 5221 (values to ~137).
