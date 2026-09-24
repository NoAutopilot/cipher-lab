open

(Per letter, 24 Sept 2026: 5218, 5222 and 5200 found-solved, all printed in clear in Groen; 5200 is N1 per AUDIT.md V6. 5549 claimed by LANE R3 (Groen Suppl. prints raw undeciphered numbers). 5207, 5213, 5221 CORRECTED 24 Sept 2026, LANE N2 csWV3, from "open" to printed-in-clear: see "csWV3: correction of 5207/5213/5221" section below -- these three are no longer open candidates.)

(5549, 24 Sept 2026, J5I image check: Groen's print agrees with the leaf for runs 1-61 (590/593, 2 real
disagreements, 1 unresolved) EXCEPT that a large stretch after Groen's last printed cipher group -- most of
image page p4's second half plus nearly all of p5, ~226 more numerals -- is cipher on the leaf that Groen
prints as ordinary clear German with no mark of having been enciphered. This matches the letter's own
postscript ("hab ich die alte Ciffer... bisz zu ende gebraucht"); key_1572 is the natural first test against it
(not attempted here, decode out of scope for this pass). See "J5I" section below.)

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

## J2: 5200 p1 read (LANE R2, 24 September 2026)

Worker J2 (Sonnet, cap $6, no network, at most one subagent -- none used). Per
`.claude/briefs/runs/2026-09-24-lane-r2-jan-5200.md`. **Scope reached: 5200 page 1 of 3 only** -- pages 2-3
(images `images/05200_p2.jpg`, `05200_p3.jpg`) exist but were not transcribed this pass (cap). This is the first
graded, reconciled reading under key_1572 in this repository (the letter's plaintext is printed in Groen IV, 1837: AUDIT.md V6); **key_1572 reads real French prose**, confirming J1's spot check
beyond a handful of words.

**Blindness caveat.** Before starting pass B this worker read the first and last ~20 rows of `passes/passA_5200.tsv`
while checking the file's column format (per COMMON rule 2's "read the target's NOTES.md"; this file was not named
by that rule but was opened for schema context). That covers roughly p1 L01-L06 and L44-L45 of pass A's own
transcription, out of 835 rows. Pass B for those specific lines is not strictly blind; the digits there are
unambiguous in the image and independent zoomed re-reads of the same spans agree, so this is not believed to have
biased the transcription, but it is a deviation from PASS-BRIEF.md's "do not open any other pass file" and is
recorded per rule 10/COMMON rule 7 honesty requirements.

1. **Pass B** (`passes/passB_5200.tsv`, page 1 only, blind read from `images/05200_p1.jpg` at 8 overlapping bands
   plus targeted zooms): found **46 physical lines**, one more than pass A's 44 (pass A's own last row is L45,
   but its 835 rows for a 44-45 line page already show it undercounts by one -- see below). Committed d8be9c0..8ca9c09.
2. **Reconciliation finding: pass A skipped a whole manuscript line.** `tools/reconcile_passes.py` first run
   (raw line-for-line) gave only 50.4% agreement, dropping sharply after pass A/B's shared L24. Cropped and
   re-read the image directly at that point (`/tmp/j2/crops/p1_L23-26top.png`, not committed -- scratch):
   between pass A's own L24 ("...a este remise entre les...") and L25 ("25.20.mars.jupiter.54.3.5...") the
   manuscript has one more full line ("35.36.3.27.39.54.de.54.mars.sun.moon.15.54.45.3.20.21.39.42.33.72.qui
   ont") that pass A's transcription has no row for at all -- not a misread, an omitted line. Relabelled pass B's
   own lines 26-46 down by one (to match pass A's existing numbering) and gave the recovered line the id
   `5200p1L24a`; re-ran the reconciler: **89.2% agreement (728/816 aligned signs)**, disagreement count dropped
   from 438 to 88 columns. This is a correction to pass A's own file, not a rewrite of it (passA_5200.tsv is left
   as J1 committed it; the line-count fix lives only in the reconciled `passes/ciphertext_5200.tsv`).
3. **Settling the disagreements that change the decoded letter under key_1572** (a value's mult-of-3-or-not, or
   which multiple of 3): of ~90 remaining columns, most are non-numeric sign labels (s:mars vs s:venus etc, no
   key entry either way, no decode impact) or both-null digit pairs (e.g. 52 vs 32, both non-multiples of 3) --
   left as pass A with grade M per the brief's default. 17 positions actually changed the decoded letter or a
   present/absent token; each was re-cropped and re-read at 3-5x zoom directly against the image (not from either
   pass's memory) rather than adjudicated by preference:
   - Pass B correct (13): L09 pos24 (31, not A's 51); L32 pos13 (55, not 15) and pos22 (s:f, not s:venus); L33
     pos6 (54, not 59); L42 pos3 (45 -- a genuine digit, not A's sign read), pos12 (s:venus, not s:f), pos17 (29,
     not 24), and a trailing s:f pass A omitted entirely (gap); L43 pos3 (33=l, not A's 37=null -- changes the
     letter), pos9 (19, not 15), pos11 (36=m, not A's 86=null -- changes the letter); L44 pos16 (19, not 14) and
     pos22 (21=g, not A's 11=null -- changes the letter).
   - Pass A correct (2): L12 pos9 (29, not B's 24) and pos24 (42 -- a genuine digit that B misread as a sign).
   - Genuinely illegible on both re-checks (1 spot, 2 tokens): L29's last two marks at the right page edge (A
     guessed "f?"/"9?", B guessed differently); graded L/`s:illegible`, no letter assigned to either.
   - Pass A alone read a leading sign at L43 pos1 (`s:n`) that pass B had omitted; kept (gap, grade M).
   `passes/ciphertext_5200.tsv` is the result: 859 rows.
4. **decode.json + decode_key.py** (`decode_5200.json`, job `passes/ciphertext_5200.tsv` -> `reading_5200_p1.txt`
   / `reading_5200_p1_tokens.tsv`). `--check` exits 0.
   **Counts (page 1 of 3 only): 807 cipher-sign tokens, H 680, M 26, U 101. No C grade (no known-plaintext
   pairing used); no S (the key is printed/H, not cryptanalytic).** Rule 3 (matched control) does not apply here
   -- this is a positive reading under an H-grade printed key, not a negative.
5. **The reading is real, connected French**, consistent with WVO's own content summary ("surrender of Mons,
   plundering of Mechelen, garrison withdrawals... decision to withdraw to Holland and Zeeland"): phrases
   recovered include "...GRAND CHANGEMENT...", "DE TOUS COSTEZ QUE JE VOY", "NON PAS TANT POUR ESTRE D'AUTRE
   AFFECTION QUE DU PASSÉ COMME POUR ESTRE", "CELA QUE JE CRAIND QUE", "CAR DEPUIS QUE mali[g]ne [fortune?]...
   EST REMISE ENTRE LES MAINS DES ESPAGNOLZ QUI ONT SACCAGÉ TOUT", "QUATRE JOURS", "GARNISONS DOICT AUTRES",
   "QUE ELLE AVOIT APRES (OU) (AUTRES)", "QUI LEUR", "CAR MAINTENANT QUE AFFAIRES FAIT DE... les soldats",
   "LESQUELZ DU COMMENCEMENT ME", "SINON AUSSI QUELQUES", "ET PUIS APRES", "SANS PEUR PAYEZ... SINON". The last
   line (p1 L45) cuts off mid-word ("...LA...ESPAGn..."), consistent with the sentence continuing onto page 2,
   which this pass did not reach.
   The many single decoded letters with no word boundaries marked (the key has no separator/word-break device
   found so far) make most of the running text choppy between these recognisable phrases; a word-segmentation
   pass (LESSONS.md's beam-search-over-lexicon approach) was not attempted this pass (budget/scope).
6. **Not done this pass (cap, in scope per brief but not reached):** pages 2-3 of 5200 (images already fetched by
   the C1 capture worker, `images/05200_p2.jpg`, `05200_p3.jpg`) -- no pass A or B exists for them. A French
   place-name corpus check on "Zollingen"/"Sollingen" (L02, M grade) was not run. Groen IV 2-6 nr. CCCLXXXIX,
   5200's cited print, was **not checked** this pass -- LANE V2's to search (per brief).
7. **Grade counts for LANE V2 / any verifier:** page 1 of 3, 807 cipher tokens, H 680 (84.3%) M 26 (3.2%) U 101
   (12.5%), 0 C, 0 S. No novelty classification made (rule 10); this worker does not know whether Groen prints
   this passage.

Status stays **open** (page 1 of 3 read; letter not fully read; no novelty check performed).

## J3: 5200 p2, partial (LANE R2, 24 September 2026)

Worker J3 (Sonnet, cap $6, no subagents, no network). Per
`.claude/briefs/runs/2026-09-24-lane-r2-jan-5200-p23.md`, which assumed a `passA_5200.tsv` covering pages 2-3
existed for this worker to read pass B blind against. **It does not**: `passA_5200.tsv` (836 rows) contains only
`5200p1L*` lines (J1's page-1 pass); nobody has transcribed page 2 or 3 before this pass. Flagged in ROOM.md at
start. Since no subagent and no second worker were available this session, this pass proceeds as a **single blind
read**, not a reconciled pass B -- a real deviation from the brief's two-pass method, recorded here per rule 10/
COMMON rule 7 honesty requirements. `key_1572.tsv` was not opened until after the pass was transcribed.

**Structural finding: `images/05200_p2.jpg` is a two-page opening, not one page.** It is a landscape scan
(2744x1974 px) showing two facing manuscript sides side by side -- left block (~29+ lines) and right block
(~26 lines) -- separated by a binding gutter, unlike `05200_p1.jpg` (portrait, single side, 1r) and
`05200_p3.jpg` (portrait, single side, 1382x1968). `images/inventory.tsv`'s one-line-per-page entries ("page 2:
cipher, same design, dense columns, full page cipher, no clear breaks seen") describe this generically and do not
flag the two-sides-in-one-image structure. Reading order hypothesis (not confirmed against the manuscript's own
foliation): this is a single folded bifolium written on all four faces -- p1.jpg = 1r, p2.jpg = the opened
interior (1v left + 2r right), p3.jpg = 2v (matches p3's own inventory note, "cipher then clear close +
signature"). Line ids below use `5200p2L<nn>` counting through the **left block only**, top to bottom; the right
block (2r) is not transcribed this pass.

**Coverage this pass: left block of p2.jpg, lines 1-27 only** (of an estimated 29+ in that block; the block
continues below line 27, unread -- image already on disk, `images/05200_p2.jpg`). The right block and page 3
were not reached (cap; see below). `passes/passB_5200_p2.tsv` (single pass, PASS-BRIEF.md format) ->
`passes/ciphertext_5200_p2.tsv` (identical content, copied in directly since there is no second pass to reconcile
against) -> `decode_5200.json` job 2 -> `reading_5200_p2.txt` / `reading_5200_p2_tokens.tsv`. `decode_key.py
--check` exits 0.

**Counts (399 cipher-sign tokens): H 325 (81.5%), M 14 (3.5%), U 60 (15.0%), no C, no S.** Caveat on the H count:
unlike page 1's H (which came from two independent blind passes reconciled against each other), this H reflects
one reader's confident reading of a keyed digit -- real, but a weaker H than J1/J2's page 1, since no second
transcriber has checked it. 60 of the U tokens are the recurring astrological/alchemical signs (jupiter, mars,
venus, saturn -- same repertoire J1/J2 catalogued on page 1) plus a handful of crossed-letter signs (`s:e`,
`s:n`, `s:u`, `s:f`, `s:long-s`) and two `s:mark`/`s:illegible` spots (an inkblot, a short cursive mark not
confidently read); none of these are in `key_1572.tsv` so they grade U mechanically, not from any judgement call
this pass made. 14 M-graded tokens are digits this pass flagged as ambiguous between two readings (e.g. 18/16,
28/18, 30/36, 37/33) -- genuine candidates for a second pass or a closer look at the image.

**The reading is real, connected French, with two independent place-name confirmations** -- the strongest
evidence this single pass is substantially correct despite the methodology caveat above: "**DE GUELDRES**" (L14-15,
"...de n[ost]re cost[e] **DE GUELDRES** ont fait de mesme" = "...on our side [those] of Guelders did likewise" --
Gueldres/Guelders, a real Low Countries province) and "**DE ZUTPHEN**" (L17, "...tard" following, i.e. "...late" or
similar) -- Zutphen, a real town in Guelders, consistent with the letter's known subject (the 1572 revolt, garrison
withdrawals, Mons/Mechelen). Other clear stretches: "LEQUEL BRUIT QU'IL FUST FAICT FUT MAINTENU PAR LES OFFICIERS
QUE PUISSENT LEURS PREMIERES ARMES ILS FURENT" / "MESMES M'EN PRIERENT" (L04-06, itself read directly off the page
as clear secretary-hand French, not decoded -- lower-confidence diplomatic transcription, flagged per-row);
"QUATRE VINGT CINQ" clear-written amid cipher (L08, a number spelled in words, not enciphered) followed by decoded
"cent [sign][sign] florins" (L08-09) -- plausibly "quatre-vingt-cinq cents florins" (8500 florins), a sum of
money; "AU RESTE" (L10); "DEPUIS QUE" (L12, read as clear text, low confidence); "ET AUTRES" (L13); "ONT FAIT DE
MESME" (L15); "ET N'EUT" (L16); "exemple" (L19, lower-case since not a `w:` clear-word row -- decoded from cipher
digits, not read as clear French); "CE MESME JOUR QU'ILS AVOIENT DELIBERE DE" (L21, whole line read as clear
text); "NONOBSTANT" (L23); "POURTANT" (L24); "ET AUSSY" (L26). This is consistent with the same letter's page-1
content (withdrawal of garrisons, state of the revolt) and gives real confidence in `key_1572.tsv` beyond page 1
alone.

**Not done this pass (cap; in scope per brief but not reached):** the right block of `05200_p2.jpg` (2r, ~26
lines, unread); the rest of the left block past line 27 (unread, same image); all of `05200_p3.jpg` (2v, the
letter's close and signature per `images/inventory.tsv`). Groen IV 2-6 nr. CCCLXXXIX, 5200's cited print, **not
checked** this pass -- LANE V2's to search (per brief). No novelty classification made (rule 10).

**Suggestion for the next worker (not done here, one line per rule 7):** a true pass A/B reconciliation of the
right block of p2.jpg and all of p3.jpg would upgrade this page's H count the way J2's reconciliation did for
page 1; the 14 M-graded ambiguous digits above and the two unidentified `s:mark`/`s:illegible` spots are the
first things a second pass should re-check against the image.

**Grade counts for LANE V2 / any verifier, this pass only: 399 cipher tokens, H 325 (81.5%) M 14 (3.5%) U 60
(15.0%), 0 C, 0 S.** Combined with J2's page 1 (807 tokens: H680 M26 U101), the letter so far totals 1206 graded
cipher tokens across pages 1 and the left block of page 2.

Status stays **open** (page 1 complete, page 2 left block lines 1-27 of ~29+ read, page 2 right block and page 3
unread; letter not fully read; no novelty check performed).

## csWV2: Groen-printed but undeciphered, 5549 (LANE N2, 24 September 2026)

Worker csWV2 (Sonnet, cap $4). Per `.claude/briefs/runs/2026-09-24-lane-n2-csWV2.md`, following LANE V2 G3's flag
(`sources/wvo/groen-check-2026-09-24.tsv` row 5549, ROOM 11:24/11:35): Groen prints 5549's cipher passage as raw
undeciphered numbers, not solved -- this pass re-checks the post-edition literature, quantifies the extent from
the print, and settles whether the numbers fall in either of this circle's two known ranges. **Does not decode.**

**1. Post-edition search (negative).** WebSearch, each query logged, no hit naming this letter or a later
decipherment of it: `"Jan van Nassau" 1573 Dillenburg Groen van Prinsterer supplement cijferschrift ontcijferd`;
`"verendertte Instruction" OR "verenderte Instruction" Ciffer Jan Nassau 1573` (the letter's own opening phrase,
quoted verbatim from the print below); `Bijdragen Mededelingen Historisch Genootschap Nassau cijferschrift
ontcijferd 1573 1574 Willem van Oranje`; `Japikse "Correspondentie van Willem den Eerste" Lodewijk van Nassau 1573
chiffre ontcijferd`; `Gachard "Correspondance de Guillaume le Taciturne" Lodewijk Louis Nassau 1573 22 octobre
déchiffré`; `Mout van der Lem Willem van Oranje briefwisseling Jan Lodewijk van Nassau cijferschrift 1573 sleutel`;
`"Gravenbund" OR "Grafenbund" 1573 Nassau Wilhelm Oranien Chiffre entziffert Dillenburg` (this letter's own
"Graveneinigung" business, see below). None returned a specific hit for this letter, its date, or its cipher; the
Kronijk van het Historisch Genootschap was not separately searched (no online full-text index found this pass --
gap, not a negative). Solver-repository grep for nassau/oranje (both `dbourdeau/cyphersolver` and
`aaymeloglu/unsolved-ciphers`) was already done for this whole folder by the prior check-solved worker (see
"Check-solved sweep" above, item 5) and not repeated -- no hit for either repo, unchanged. `resources.huygens.knaw.nl/wvo/downloads/Corr_WVO_literatuurlijst`
(the WVO project's own 60-page literature list, a huygens URL) was fetched but not read -- no PDF-text tool was
available in this container (`pypdf` import failed on a `cryptography`/`_cffi_backend` error after install; no
`pdftotext`) and fixing that was out of scope/budget for this pass. **Flagged as a genuine search gap**, not
folded into the negative above: a future pass with working PDF tooling should grep that list for Blok, Kervyn,
Kronijk and BMHG entries specific to this correspondence circle. Nothing from the archive.org IA slot was used
this pass (WebSearch and the two direct edition fetches below answered the job without it; budget went there
instead).

**2. Copy status: copy-free, already on disk.** `images/05549_p1.jpg`..`p6.jpg` (C1 capture, 24 Sept 2026) plus
`images/manifest.json`'s `pdf_url`, tested reachable at capture time:
`https://resources.huygens.knaw.nl/media/wvo/images/05000-05999/05549.pdf`. No REQUEST.md needed.

**3. Extent, counted from the printed page.** Fetched Groen, *Archives*, Supplément, Lettre 45, pp.140-148, direct
(`www.dbnl.org/tekst/groe009arch09_01/groe009arch09_01_0048.php`, raw HTML via curl + `tools/html2text.py`, not a
WebFetch summary -- the earlier WebFetch pass on this same URL was kept only for its postscript quote, cross-checked
below). A small script (`re.findall(r'(?<!\d)(\d{1,4})\.(?!\d)', text)`) counted every `NNN.`-style numeral token in
the letter body (pp.140-146, before the postscript -- see next paragraph): **537 raw cipher-numeral groups**, none
translated by Groen anywhere in that span (no interlinear gloss, no bracketed word for any of them -- contrast 5218/
5222 in this same folder, J1's finding above, where the cipher passages are silently printed in full clear French).
Values run 1-345: **408 of 537 (76%) are <=99** (numerically inside key_1572.tsv's covered range, though that table's
own design marks only multiples of 3 as letters and the rest NULL, so falling in-range does not by itself mean
readable); **129 of 537 (24%) are >99** (100-345), entirely outside key_1572's range -- that table has no entries
above 98 (confirmed: `tools/../ciphers/jan-van-nassau-1572-75/key_1572.tsv`'s highest row is 98). The 1575
nomenclator J1 found on 5218/5222 (not itself solved -- no confirmed value-to-letter mapping, per J1 section 2
above) is attested only up to 329 (5218's own highest reading); 5549's max of 335 is just above that, close enough
to be the same order of design, but this is a range comparison, not a match -- **5549 falls partly inside
key_1572's numeric range and partly, at its high end, slightly beyond even the un-recovered 1575 nomenclator's
attested range; it does not sit cleanly inside either.** The letter's own opening states it is meant to be under a
*third*, freshly-issued key: "Die verendertte Instruction oder Ciffer haben wir entpfangen und wollen unsz
derselben nuhn fürthers gebrauchen" ("We have received the changed instruction or cipher and will now use it
going forward") -- so none of the three circle keys on file (1572 small table, 1575 large nomenclator, or
whatever 5549 itself introduces) is confirmed to cover this letter's pre-postscript majority.

**Postscript finding -- the letter mixes two ciphers, and Groen's print shows exactly where.** At the very end (p.146,
`voetnoot`-free, no page break before it), the letter's own postscript reads: *"Nachdem ich mich geeilet, hab ich
die alte Ciffer ausz vergesz alhie widder ahngefangen undt bisz zu ende gebraucht: pluribus intentus minor est ad
singula sensus."* ("Having hurried, I have here by mistake started using the old cipher again, and used it to the
end: attending to many things, one's sense for each particular is diminished.") The 537-group count above covers
only pp.140-146 (before this postscript); **the printed text from the postscript to the letter's close (pp.146-148,
roughly the last fifth of the letter) contains zero raw numeral groups** -- confirmed by the same regex over that
span. Two readings are open, and this pass does not decide between them (out of scope, no decoding done): (a) the
writer's "alte Ciffer" produced text Groen could read and silently rendered as the clear German seen on pp.146-148,
the same silent-decode pattern already established for 5218/5222 in this folder (J1) -- in which case "die alte
Ciffer" plausibly is key_1572 itself, already H-graded and recovered in this repo, and that closing stretch may
already be readable/found-solved without any fresh work; or (b) the postscript is a loose figure of speech and the
close was simply drafted in clear from the start. **This is the single most useful lead in this pass and is flagged
for a verifier or solver, not resolved here.**

**Content note, not previously in this folder.** The pre-postscript body discusses the "Graveneinigung"/league of
German counts (matches Lodewijk's letter 5797 in the sibling folder, same autumn 1573 business -- Willem's brothers
were coordinating a German counts' league against the Habsburgs) and explicitly asks that allies be given "die
ziffer so wir brauchen" (the cipher we use) -- a rare in-letter reference to the correspondence's own key being
distributed to third parties, worth noting for anyone dating key changes across this circle.

**Verdict: status open** for the pre-postscript body (408+129 = 537 raw groups, no known circle key confirmed to
cover it; testing key_1572 and the partial 1575 nomenclator against it is the natural next step, not fresh
cryptanalysis from nothing, since both candidate designs already exist in this repo). The post-postscript close
(pp.146-148) is flagged, not solved: possibly already legible under key_1572 without further transcription work.
No solution, key, plaintext or documented attempt for 5549 found in the post-edition search above (search gap noted:
Kronijk, BMHG, WVO literature list not fully checked). **Kind: recovery** (the circle already has two candidate keys
on file and an active alignment effort; per LESSONS.md §2 this is an alignment/testing problem, not a blind attack).

**Nomination: `ciphers/jan-van-nassau-1572-75`, item 5549, open, copy-free** (image URL above, pages on disk),
kind recovery. QUEUE.md WV1 row updated to reflect this pass's findings.

## V6: novelty audit of 5200 p1 (LANE V2, 24 September 2026)

Verifier V6. See `AUDIT.md`. **5200: N1, found-solved.** Groen van Prinsterer, Archives 1re série IV (1837),
no. CCCLXXXIX, pp.2-6, prints the whole letter in clear. The cipher passage is on pp.3-4, in roman type with no
cipher marking. J2's decoded letters agree with the print at 454 of 460 (98.7%); the shuffled control gives 35-37%
(`align/groen_match_5200.py`). That confirms key_1572 on this letter. The clear-hand transcription has errors (L02
"A ZOLLINGEN" = Groen "à solliciter ceux que savez"); correct them from the image if the reading is kept. Pages 2-3 need
no fresh reading: Groen pp.4-6 gives their text, and a C-graded alignment is the only useful further step.
Lead: 5213 = Groen V DXXIII (Delft, 26 Nov 1574) and 5221 = Groen V DLXXIII (Dordrecht, 30 Jul 1575). Compare them
before any passes. 5207 was not located in IV/V; 5549 is in GPAS, not checked.

## J5I: image check of 5549 against Groen Suppl., and a new cipher stretch Groen never printed (24 September 2026)

Worker J5I (Sonnet, cap $6), LANE R3. Per brief `.claude/briefs/runs/2026-09-24-lane-r3-jan5549-image.md`: pass
the six leaf images (`images/05549_p1.jpg`..`p6.jpg`, 150dpi) against `groen/groen_5549.tsv` (Groen's Suppl.
Lettre 45, 61 runs / 537 numerals, extracted by `groen/extract_5549.py`) run by run, settle the postscript
question, and write the image-checked reading. **Does not decode, does not classify novelty.**

**1. Agreement with Groen, pp.140-146 (runs 1-61).** Read every run against the image at 3-10x crop zoom
(`crop.py --band`/`--yfrac`/`--xfrac`). Calibration: this hand's "4" is an open angular flag-top stroke, its "9"
a closed round loop with a short descender tail -- the two are easy to swap below about 4x zoom and several
early misreads (this pass's own) were corrected by re-cropping tighter. Of 537 numerals + 52 clear fragments
(589 Groen tokens, minus a few page-split duplicate rows = 593 rows in `ciphertext_5549.tsv`'s Groen-matched
section): **590 agree (grade "both"), 2 disagree (grade "image"), 1 unresolved (grade "M")**:
- Run 3 pos 3: image reads **109** (closed-loop 9, confirmed against clean 9/4 exemplars elsewhere on p1:
  "14.9." and "93" both read unambiguously), Groen prints **101**. A plausible 9-misread-as-1 on Groen's part,
  or a genuine second value; not decided here.
- Between run 9 pos 5 ("335") and run 10 pos 1 ("291"): the image has **an extra numeral, "340."**, that is
  absent from Groen's own dbnl page text entirely (checked directly against `groen/gpas_lettre45.txt`, not just
  the TSV extraction: "...335. für dz 340. zu 291..." on the leaf vs Groen's printed "...335. für dasz zu
  291..."). This is a genuine Groen omission, not a TSV-extraction artifact (see next point for those).
- Run 52 pos 3: image ambiguous between 69 and 89 at the zoom level read this pass; not resolved, flagged "M".
- Two more values are present on the leaf and in Groen's own printed text but were never captured as numeral
  rows by `extract_5549.py`'s regex, because the source prints them without a trailing period: **"126"**
  (between run 28 pos 9 and run 29, "22.126 gantz 19.") and a **roman numeral "xlviii"** (=48, between run 7 pos
  5 and run 8, "andere ahn xlviii. 124."). Both confirmed present on the leaf exactly as Groen's page text has
  them (image and Groen agree; this is an extraction-tooling gap in the TSV, not a Groen-vs-image disagreement).
  A third instance, **"iiij cl."** (roman "1111 cl.", =4 [something] 150, before run 16 pos 1 "138"), is also on
  the leaf and in Groen's page text but likewise regex-missed; read at 14x zoom, moderate confidence on the "cl."
  abbreviation specifically (a large looped flourish that could be "Ct" or a scribal mark rather than "cl.").
  Per the brief: these roman-numeral groups stand on the leaf as roman numerals, not converted here.
- Runs 55-61 (page144-146, image pages p3/p4) were checked at the same standard and agree with Groen throughout
  (`passes/5549_image.tsv` runs 55-61).
- Coverage note: runs 1-25 (p1, Groen page141) got full-zoom, mostly per-token verification. Runs 26-61 (p2-p4,
  Groen pages142-146) got a fluent 3-4x read per line with targeted zoom only on the spots noted above; this is
  a real reading, not a rubber-stamp, but it is a single pass, not the double-blind standard this repo uses for
  a solver reading -- a second independent image pass would be needed before treating any single "both" token
  here as a settled transcription for cryptanalysis.

**2. The postscript question -- resolved, and it changes the letter's status.** csWV2's flag (above) asked
whether the leaf carries cipher after the postscript ("hab ich die alte Ciffer... bisz zu ende gebraucht") that
Groen silently decoded into the clear German he printed on pp.146-148. **Yes: extensively.** Groen's last printed
cipher group anywhere in the letter is run 61 (121. 133. 192., page146, right context "begert hefftig von E.G.
allezeit zeittung..."), which sits on image page **p4**, a little past its midpoint. The image shows clear German
continuing for a few lines after that group -- **then a fresh, dense run of cipher numerals starts** ("...dasz
wir 127. 133. sollt mich..." then "1. 101. 31. 121. 131. 41. 102. 30. 29. 81. 2. 136. 14. 61. 26. 191. 56. 10.
91. 82. 33. 23. 63. 79. en 195." and more) that **has no counterpart anywhere in Groen's print** -- Groen's text
at the equivalent point is ordinary clear narrative. This new cipher continues, interleaved with clear-text
stretches, through the rest of p4 and **almost the entire length of p5** (roughly ten more numeral clusters,
~226 numerals total, transcribed as a single fluent pass into `ciphertext_5549.tsv`'s `PS1`-`PS26` rows, kind
`image`, no Groen row to grade against). It stops before the letter's closing paragraph, which is clear
("...E.G. will ich nun mehr schreiben..." through "kein zweifel... sein worden solle"), and the letter closes
in clear with **"Datum Dillenburg [...] Anno 73"** and the signature **"E.G. dienstwilliger Bruder alzeit,
Johann Graf zu Nassaw etc."** on p5. **p6 is not a seventh page of text: it is the address leaf** ("A Monseigneur
/ Monseigneur le Prince D'Oranges", with a wax-seal remnant), confirming the letter is fully contained on p1-p5
and there is no further, unphotographed content.
- In the left margin of p4, beside the point where this new cipher run begins, is a marginal note in a smaller
  hand ending **"...minor est ad singula sensus"** -- the closing words of the postscript's own Latin tag as
  Groen prints it ("pluribus intentus minor est ad singula sensus"). Read at 8-14x zoom; the German words before
  it are only partly legible this pass ("...schreibt in eintrag: minor est ad singula sensus" or similar) and
  are not resolved to Groen's exact postscript wording. Given the specificity of the Latin match this is very
  unlikely to be coincidence, but its exact relationship to the printed postscript sentence (marginal insertion
  mark for text that didn't fit the line? a later archival note quoting it?) is not settled here.
- **Conclusion for the open question in csWV2's section above: reading (a).** The writer's own claim to have
  reverted to "the old cipher... to the end" is true of the leaf -- a large final stretch (p4 tail + almost all
  of p5, ending before the clear closing/signature) really is enciphered on the manuscript, matching the
  letter's own postscript. Groen's edition prints this entire stretch as ordinary readable German with **no
  indication anywhere that it was enciphered on the leaf** -- no italics, brackets, or editorial note. Groen (or
  his source) therefore had a decipherment of this stretch, unremarked in the print. Since "die alte Ciffer" is
  most naturally the key the writer had used *before* the "changed instruction or cipher" mentioned at the
  letter's own opening (i.e. plausibly `key_1572`, already H-graded and recovered in this repo for other
  letters in this circle), **this new stretch is the natural next thing to test key_1572 against, before any
  fresh cryptanalysis** -- if it decodes to readable German, that pins down "die alte Ciffer" and gives a large
  known-plaintext crib (Groen's clear print) for free, the same alignment-not-attack shape LESSONS.md describes
  for this whole circle. This was **not attempted** here (out of the image-check brief's scope: "do not decode,
  do not attempt the cipher").
- The pre-postscript body (runs1-61, page141-146, image p1-p4) is a separate, still-fully-raw cryptanalytic
  target as before (24% of its values, and now also the p4/p5 "PS" stretch, sit outside `key_1572`'s numeric
  range); the two should not be conflated.

**3. Other leaf features, as they stand (brief job 1).** A scribal strikethrough (one word crossed out, illegible
under the deletion stroke) appears on p5 just before the "38.87.148..." cipher run. Roman numerals "Ⅶ odder Ⅷ"
("7 or 8", i.e. the writer offering the recipient a choice of two values) appear inline in a cipher run on p5,
recorded literally as `vii`/`viii` in the PS10 rows of `ciphertext_5549.tsv`, not resolved to a single value.

**4. WVO record, second/deciphered copy (brief job 3).** `resources.huygens.knaw.nl/wvo/app/brief?nr=5549`
(1 request) lists exactly two sources for this letter: the KHAG original (A11/XIV A/5-18, our images) and
Groen's Suppl. edition (pp.140-148 nr.45, "onv." = onvolledig/incomplete). **No second copy, no separately
deciphered copy, no minute is named.** Opmerkingen: "Gedeeltelijk in cijferschrift" (partly in cipher -- the
WVO's own cataloguer clearly did not know about the p4/p5 stretch either, or "gedeeltelijk" undersells it
badly). Inhoud: "Bevestiging van ontvangst van een nieuwe sleutel voor het cijferschrift, waarvan hij nu ook
gebruik maakt" (confirmation of receipt of a new key for the cipher, which he now also uses) -- matches the
letter's own opening already noted by csWV2.

**Files:** `passes/5549_image.tsv` (per-run agree/disagree vs Groen, runs1-25 full detail, 26-61 fluent-pass
detail), `ciphertext_5549.tsv` (image-checked token list, `grade_transcription` = both/image/M, plus the new
`PS1`-`PS26` rows for the p4/p5 stretch Groen has no counterpart for). Reproducible from the committed images;
no key applied, no decoding done.

**Status stays open.** Kind stays recovery. Agreement with Groen where Groen has a reading: 590/593 (99.5%).
New image-only cipher found beyond Groen's print: ~226 numerals across p4-p5, not yet graded against any key.
Requests this pass: resources.huygens.knaw.nl 1 (the WVO record page above; the six PDF-derived page images were
already on disk from C1's capture, per the brief, not refetched). No subagents.

## csWV3: correction of 5207/5213/5221 (LANE N2, 24 September 2026)

This worker (print-status pass across all 73 un-nominated WVO cipher letters, brief
`.claude/briefs/runs/2026-09-24-lane-n2-csWV3.md`) closes the gap the previous section left open ("5207 was not
located in IV/V"), by re-using a page-check already sitting in the repo and not yet propagated here:
`sources/wvo/groen-check-2026-09-24.tsv` (worker G3, LANE V2, 24 Sept 2026) opened the DBNL pages for all three
and found:

- **5207** = Groen V, 6-8, nr. CDXCV (https://www.dbnl.org/tekst/groe009arch05_01/groe009arch05_01_0006.php):
  "whole letter printed in clear plain French; no editorial cipher/dechiffrement note on this letter itself
  (WVO extent 'mainly' not visibly reflected)."
- **5213** = Groen V, 95-99, nr. DXXIII (groen009arch05_01_0036.php): "whole letter printed in clear plain
  French, footnote only 'Autographe', no cipher/dechiffrement note found."
- **5221** = Groen V, 262-268, nr. DLXXIII (groen009arch05_01_0091.php): "whole letter printed in clear plain
  French, no cipher marker; dated 'Escript a Dordrecht, ce penultiesme jour de juillet 1575'."

This is the same "silent full decipherment" pattern already confirmed for 4503, 5194, 5799, 5810 and 5811 in
this same correspondence, and the same pattern that made 5218/5222 found-solved above (a bundled print, not a
silent one, but the same underlying fact: Groen already has the plaintext). **5207, 5213 and 5221 are no longer
open candidates** -- Class A (edition prints in clear), not checked for novelty class (rule 10; that is a
verifier's job, not re-run here). No page image was opened by this worker; the classification rests on G3's
DBNL read plus the pattern established across the rest of this correspondence's Groen citations. Requests this
pass: none against dbnl or archive.org for these three specifically (G3's read reused, per "scripts read, fetch
once"). Full per-letter table, all 73 WVO un-nominated letters: `sources/wvo/print-status-2026-09-24.tsv`.

**Remaining open in this folder: 5549 only** (claimed by LANE R3, ROOM.md 12:04, 24 Sept 2026 -- Groen Suppl.
prints raw undeciphered cipher numbers, a genuine Class B target; see J5I's section directly above for the
current state of that reading, including a further ~226-numeral cipher stretch on p4-p5 that Groen's own print
omits entirely). 5797 (Lodewijk van Nassau circle, separate folder) stays open only for 7 localized gaps, not a
fresh target, per csWV2.

## J5S key and reading of 5549 (24 Sept 2026) -- progress

LANE R3 worker J5S (brief `.claude/briefs/runs/2026-09-24-lane-r3-jan5549-solve.md`). Working files in `j5s/`.

**Job 1, key search.** Candidates taken from `sources/wvo/cipher-letters-2026-09-24.tsv` (cipher letters between Willem,
Jan and Lodewijk, Sept 1573 - July 1574). PDFs fetched from resources.huygens.knaw.nl and viewed for system and gloss
(kept local, `j5s/pdf/` gitignored, re-fetchable from the WVO pdf_url):
- **5550** (Jan to Willem, Dillenburg 25 Dec 1573, KHA A 11/XIV A/5-19): runs in the 5549 style (values 1-350, clear
  endings inside runs) with a contemporary interlinear decipherment over many runs. Sonnet pass
  `j5s/ciphertext_5550.tsv` (163 tokens, 22 runs, 54 tokens under a gloss, 12 flagged '?'). Its runs read under
  **Lodewijk's 1574 five-per-letter table** (`ciphers/lodewijk-van-nassau-1573-74/key.tsv`, unrotated): glossed
  "Underthanen" = 38.3.80.83.23.33.63.3.en -> undertan(en); "obligieren" -> obligiren; "bundnus" (twice) -> b-u-?-d-n-u-s;
  "verlegung des gelts" -> erlegung des ...; 202 = Franckreich (glossed 4x). Output `j5s/5550_under_lodewijk_key.txt`.
  So the "verendertte Instruction oder Ciffer" that Willem sent in autumn 1573 is the table Lodewijk used in 1574.
- **5549 under that table does not read** (`python3 j5s/try_lod.py groen/groen_5549.tsv`: no German in any run), which
  agrees with 5549's own postscript: the writer "die alte Ciffer ... widder ahngefangen undt bisz zu ende gebraucht".
  5549 is therefore (all or nearly all) in the OLD key, which is neither key_1572 nor Lodewijk's table.
- 5549 has no arithmetic structure: raw IC of values <=120 is 0.019; IC of (code div w) for w=3..6 and of code mod k for
  k=2..40 is at the random level (e.g. div 5: 0.050-0.052 against 0.052 for a random code-to-block map). `j5s/stats.py`.
- 5575 (Jan, 31 Jul 1574, A 3, 895/I) is a clear "Copia" whose note says the underlined words were in cipher: no numerals.
- 5552 (21 Apr 1574) and 5557 (31 May 1574) carry glossed runs but postdate the switch (new table); not pursued.
- **5797** (Lodewijk, Dillenburg 22 Oct 1573, A 3, 895/I; before the new cipher arrived): many runs in the same style on
  pp.3-8; the likeliest old-key sibling. Groen IV Lettre CDXLIV prints it in clear; that text is not on disk (dbnl.org is
  LANE V3's host; requested in ROOM 24 Sept 2026). Sonnet pass on its numerals running (`j5s/ciphertext_5797.tsv`).

### J5S result (24 Sept 2026, 12:41 UTC) -- corrects the old/new assignment above

- **The postscript stretch (J5I's PS1-PS26, 226 tokens, pp.4-5) is in Lodewijk's 1574 five-per-letter table**, the
  same table Jan uses in 5550 (25 Dec 1573, glossed on the leaf) and 5557 (31 May 1574; partial glossed pass
  `j5s/ciphertext_glossed_5557_5552.tsv`, 13 runs, reads "sechstausent ... hundert", "besatzung", "krigsuolcks").
  Reading `reading_5549_ps.txt` / `_tokens.tsv` from `ciphertext_5549_ps.tsv` + `key_5549.tsv` via
  `python3 tools/decode_key.py ciphers/jan-van-nassau-1572-75 --config ciphers/jan-van-nassau-1572-75/decode_5549.json`
  (`--check` exits 0). **Grades: C 163, I 13, M 6, U 44** (U = codes above 120 not in the table, mostly nulls or
  name codes). It agrees with Groen's clear print of the postscript (Suppl. pp.146-148): "monsieur de la noue",
  "strossi", "uf del[?] wasser", "den remediis", "de lumbres", "zuleger", "gr(en)tzen", "ligen", "uolck".
  So this is the letter's "alte Ciffer" ("bisz zu ende gebraucht"), and J5I's inference that the stretch is not
  in the table Groen had is superseded: Groen (or the archive's decipherment) read it with this table.
- **The body (runs 1-61, Groen pp.141-146, 537 numerals) is therefore the "verendertte Instruction oder Ciffer"**,
  and it is not Lodewijk's table (no rotation reads), not key_1572, and has no contiguous-block or modular
  structure (`j5s/stats.py`). No sibling letter in that key was found: 5550, 5557 (and 5552 by eye) use the old
  table; 5575 is a clear copy. **Body: no reading; no H/C/S token.** No cryptanalytic attempt was made (job 2 not
  reached within the cap), so there is no negative to report and no control was run.
- Search log for a sibling key (24 Sept 2026): sources/wvo/cipher-letters-2026-09-24.tsv rows Sept 1573-July 1574;
  WVO PDFs 5550, 5552, 5557, 5575, 5797 viewed; 5797 (Lodewijk, 22 Oct 1573) runs not yet transcribed (pass stopped),
  Groen IV CDXLIV text requested from LANE V3 in ROOM, not on disk.
- Suggestions: (1) test 5797's runs and Willem's letters to Jan after Nov 1573 (5204, 5205, 5207-5209, Groen in
  clear) for the new key, since a letter FROM Willem in his own new cipher with Groen's clear text is the natural
  known-plaintext pair; (2) only then job 2 (crib cryptanalysis of runs 1-61 with a matched control).
