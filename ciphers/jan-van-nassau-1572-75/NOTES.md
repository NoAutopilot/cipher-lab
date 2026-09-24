open

(Per letter, 24 Sept 2026: 5218, 5222 and 5200 found-solved, all printed in clear in Groen; 5200 is N1 per AUDIT.md V6. 5207, 5213, 5221 and 5549 open; 5213 and 5221 have Groen prints to compare first, see AUDIT.md.)

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
## V6: novelty audit of 5200 p1 (LANE V2, 24 September 2026)

Verifier V6. See `AUDIT.md`. **5200: N1, found-solved.** Groen van Prinsterer, Archives 1re série IV (1837),
no. CCCLXXXIX, pp.2-6, prints the whole letter in clear. The cipher passage is on pp.3-4, in roman type with no
cipher marking. J2's decoded letters agree with the print at 454 of 460 (98.7%); the shuffled control gives 35-37%
(`align/groen_match_5200.py`). That confirms key_1572 on this letter. The clear-hand transcription has errors (L02
"A ZOLLINGEN" = Groen "à solliciter ceux que savez"); correct them from the image if the reading is kept. Pages 2-3 need
no fresh reading: Groen pp.4-6 gives their text, and a C-graded alignment is the only useful further step.
Lead: 5213 = Groen V DXXIII (Delft, 26 Nov 1574) and 5221 = Groen V DLXXIII (Dordrecht, 30 Jul 1575). Compare them
before any passes. 5207 was not located in IV/V; 5549 is in GPAS, not checked.
