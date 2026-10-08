open
Groen van Prinsterer, Archives 1re série, read by this worker 7 Oct 2026: tome III letter list pp.CI-CIII and pp.428-449, 460-468 (the Certain letters; nothing dated 12 Aug 1572 to Louis), plus Huygens retroboeken full-text search of tomes III, IV and the Supplément for "Lambert Certain", "George Certein", "jourduy", "deux vostres", "remerchiant", "Holstein", "Ermuyden", "Arnemuyden", "Vlissinghen", "12 aoust", "Arnoult", "Dominique": letter absent; WVO record 11008 gives no edition (no GPA/GPAS/JC line).

Check-solved verdict (KHF-2, 7 Oct 2026 by `date -u`): `open`. Details in "## Check-solved (KHF-2, 7 Oct 2026)",
"## Web and blog check (KHF-2, 7 Oct 2026)" and "## Premise check (KHF-2, 7 Oct 2026)" at the end of this file.

# WVO 11008: Willem van Oranje ("George Certain") to Lodewijk van Nassau ("Lambert Certain"), Keulen, 12 Aug 1572

Found by KH2-D (LANE KH-2, account 2), 7 Oct 2026 18:17-18:3x UTC by `date -u`, brief
`.claude/briefs/runs/2026-10-07-acct2-kh2-workers.md` (KEYHUNT: unread siblings of keys already held).

## Source

- WVO record https://resources.huygens.knaw.nl/wvo/app/brief?nr=11008 (read 7 Oct 2026). Inhoud: "Behoefte aan
  geld. Vorderingen van de veldtocht." Incipit "J'ay recheu ce jourduy les deux vostres du 5 et 7 du courant, vous
  remerchiant". Opmerkingen: written as a merchant's letter from George Certain (= the prince) to Lambert Certain
  (= Lodewijk); address "Au s.r Lambert Certain, nostre bon amy et compere estant pour le present a Tournay".
  **The remarks do not mention cipher**, which is why the 24 Sept 2026 WVO harvest (`sources/wvo/`, opmerkingen
  "cijfer") never listed it. Found here through an opmerkingen search for "koopman" (merchant).
- Holding: Koninklijk Huisarchief Den Haag, A 11/XI 15, original. Image: WVO PDF
  https://resources.huygens.knaw.nl/media/wvo/images/11000-11999/11008.pdf (2 images; page 1 is one wide sheet
  3754x2096 px carrying the whole letter, page 2 the address). Manifest and the four crops used: `images/`.
- WVO gives no printed edition for 11008 (no GPA line). Sister letters in the same cover scheme are printed in Groen
  III: 5194 (pp.448-449, CCCLXIX, in cipher), 6222 (pp.450-451), 6223 (pp.451-452); "George Certain est le Prince
  d'Orange" is Groen III p.428's footnote.

## What is on the leaf

French clear text with five short runs of numbers separated by colons (54 numerals in all). The numbers are mostly
multiples of 3, the design of the printed 1572 Orange-Nassau table (`../jan-van-nassau-1572-75/key_1572.tsv`, same
values as `../orange-nassau-1572/key_nepveu.tsv`: a=3, b=6 ... u/v=60, y=69, z=72; other numbers null). No
interlinear gloss on the leaf.

## Transcription

`iiif_lines.py --image <page 1> --prefix p1 --lines-per-crop 3 --max-width 2000` (15 bands x 2 segments); bands
L01, L02, L07, L08 (8 crops) went to two blind Sonnet passes, one call each (`passes/passA.tsv`, `passB.tsv`).
`tools/reconcile_passes.py`: 51/57 aligned signs agree (89.5%), 6 disagreement columns; the worker settled them
from native-resolution crops of the page. Passes split only on run 3's first two numbers (damaged paper; A "36 36?",
B "2? 9?") and its fourth (36/38); the other runs agree except "?" flags. `ciphertext.tsv` (per token, conf H/M/L
and the clear words around each run), `ciphertext.txt` (one line per run).

## Reading under the held key (`decode.py`, `reading.txt`)

| run | context (clear text) | codes | reading |
|---|---|---|---|
| 1 | end of line 4 | 10 9 12 120 | c d [120] (120 outside the table) |
| 2 | line 5, before "lequel a faict charge pour ... 2000 escus" | 33 15 12 60 9 12 15 24 42 33 54 57 15 27 39 + 11 14 17 | **le duc de holstein** + 3 nulls |
| 3 | line 20, damaged, before "le Sr Dominique est venu" | 2? 9? 36 38 15 25 37 40 | c m e (uncertain) |
| 4 | line 21, "... [la balle marquée ◇] et s'est" | 15 51 36 60 69 12 15 39 + 40 44 52 31 | **ermuyden** (Arnemuiden, Zeeland) + nulls |
| 5 | "Arnoult est" ... "Or pour" | 60 33 21 54 54 27 39 21 24 15 39 43 | **ulgssinghen** = vlissinghen (Flushing) with code 21 (g) where 27 (i) is expected at position 3 |

Grade (rule 4): 54 tokens; H 39 (read from the period table: run 2 all 18, run 4 11, run 5 10), M 15 (run 1 4,
run 3 8, run 4 pos 5, run 5 pos 3 and pos 12). No C, S or I. Depth for the verifier (rule 4a): looks like D1
(scattered words; three names read, no clause) -- the verifier sets it.

## Control (rule 3) and judge

`python3 decode.py` (writes `control.tsv`; `--check` exits 1 if stale). Matched control: same 54 tokens, the 23
letter values permuted among the 23 letter codes (nulls fixed), 1000 seeded shuffles; three statistics a shuffled
key can change:

| statistic | real key | shuffle mean | shuffle p95 | shuffles >= real |
|---|---|---|---|---|
| mean log10 4-gram prob./letter, fr16 corpus, no word list | -1.435 | -1.813 | -1.576 | 6 / 1000 |
| letters covered by fr16 words (4+ letters) only | 7 | 2.23 | 8 | 100 / 1000 |
| letters covered by fr16 words + a place list written after the decode was seen (post hoc) | 23 | 2.23 | 8 | 0 / 1000 |

The 4-gram figure passes (real above the shuffle p95, p about 0.006); the word-cover figure without names does not
separate (the readable plaintext is almost all proper names, which the fr16 vocabulary lacks); the third row is post
hoc and is shown only for completeness.

`tools/judge_plaintext.py` with the fr16 corpora (temporary spec, `corpora` = the three tools/data/fr16 files), on
"le duc de holstein ermuyden ulgssinghen cme cd":

```
FAIL language: score=-1.648, null_p99=-1.402, real_p05=-1.098, real_median=-0.804, mode=both, N=39
FAIL - wvo-11008 (a PASS is a gate for a verifier, not a reading; rule 10)
```

A FAIL at N=39 on a names-only string; the judge's letter-shuffle null is not the key-permutation null above.

## Where it was not found (search log, 7 Oct 2026)

- `ciphers/` (no folder for 11008), `sources/wvo/cipher-letters-2026-09-24.tsv` (absent), `sources/decode/*.tsv`,
  `sources/cryptiana/`, `sources/cyphersolver/` (grep 11008 / Certain / Holstein: no hit for this letter).
- Huygens retroboeken, Groen *Archives* 1re série full-text search (`archives/search_in_text`): tome III
  "Lambert Certain" 3 hits (pp.428, 430, 431, other letters), "Holstein" 5 hits (none this letter), "Arnoult" 0;
  tome IV "Arnoult" 0, "jourduy" 0. Not searched: Groen's Supplément, Japikse, Gachard, Kervyn, any secondary
  literature, DECODE live listing, the solver repositories' live trees. No novelty claim (rule 10).

## Requests

resources.huygens.knaw.nl (whole KH2-D job): about 40 (WVO searches and detail pages, 6 PDFs, 6 retroboeken
searches), >= 2 s apart, no 403/429.

## Remaining gaps (W11008-KP, 8 Oct 2026)
Read so far: 39 of 54 tokens at H under the table, confirmed on sibling 5194 (PASS, see "## 5194 known-plaintext check"); runs 2, 4 and 5 read as three names.
- run 3 positions 1-2 (two codes under a stain; pos 3-4 now read 36, 38 at H by the native look of 8 Oct 2026) - blocker: illegible; paper damage at native size, images/p1_L07_s1.jpg and the W11008-KP native crop
- run 1 position 4 ("1?0", middle digit smudged, a three-digit group outside the table either way) - blocker: illegible; native look 8 Oct 2026
- run 1 positions 1-3 and run 3 read only "c d" / "c m e" (no word) - blocker: too-short; four and six codes with no clear context that narrows them
- AUDIT.md does not yet carry the 5194 key-family confirmation - blocker: not-attempted; the verifier, not the solver, writes AUDIT.md; next: verifier audit update, ~$1

## Escalation (W11008-KP, 8 Oct 2026)
- [x] siblings: 5194 used as a known-plaintext sibling (PASS); 6222/6223 are clear in Groen with no cipher recorded in WVO
- [n/a] clear-pages: the 11008 leaf is clear text except the five runs
- [x] known-keys: the 1572 table, confirmed on 5194 by the pre-registered gate
- [x] print: Groen III and IV searched by KHF-2; 11008 is not printed
- [n/a] key-rebuild: the table is a period printed table, so nothing needs rebuilding
- [x] image-check: native look at runs 1 and 3, 8 Oct 2026
- [n/a] retry: no failed step to retry here
Verdict: keep going: 1 internal gaps; cheapest next: verifier AUDIT.md update with the 5194 confirmation, ~$1

Optional, wider than 11008 (one-line suggestion, not a gap): the rest of 5194 (3 pages, about 1,500 numerals) against
Groen as a full known-plaintext alignment, for null-usage statistics and to check the interlinear letters; ~$6.

## Check-solved (KHF-2, 7 Oct 2026)

Worker KHF-2 (account 2, session_01Y8ZhnFiRmJqcV5pQK87fP4), 20:12-20:3x UTC by `date -u`, brief
`.claude/briefs/runs/2026-10-07-acct3-kh-follow.md`. Six sources:

1. **Web**: logged in the next section. No decipherment, plaintext or discussion of this letter's cipher found.
2. **Print**: Groen van Prinsterer, *Archives ou correspondance inédite de la maison d'Orange-Nassau*, 1re série,
   via Huygens retroboeken (`retroboeken/archives/search_in_text/index_html?search_term:ustring:utf-8=<term>&source_id=`,
   whole edition; OCR page HTML through `pages.json?source=3|4`). Tome III letter list (pp.CI-CIII) read: the letters
   to Louis in the Certain period are CCCLXIX (pp.448-449, = WVO 5194, 24 June), CCCLXXVI (p.460) and CCCLXXVII
   (p.464), both July 1572 (p.463 "à Essen, le 7me jour de juillet 1572"); no 12 Aug letter from Cologne. Phrase and
   name searches across the whole edition: "Lambert Certain" 4 hits (III pp.428, 430, 431; table p.29 index entry),
   "George Certein" 1 (III p.449, letter 5194), "jourduy" 4 (1566 and Supplément p.89*, other letters), "deux vostres"
   12 (none this letter), "remerchiant" 2 (other volumes), "Holstein" 20 shown (III p.LXII and IV p.CII are other
   letters: IV p.CII is Groen's addition giving the deciphered passages of III pp.503-510, a Sept 1572 letter,
   deciphered by Van der Kemp), "Ermuyden"/"Arnemuyden"/"Arnoult"/"Dominique"/"2000 escus" 0, "Vlissinghen" 3 (III
   pp.433, 435, 453, other letters), "12 aoust" 8 (none 1572). Japikse's *Correspondentie van Willem den Eerste*
   (deel 1, 1551-1561, the volume this repo has used, ciphers/gunther-van-schwarzburg-1561) ends before 1572.
   Internet Archive full text (be-api fts, global): "Lambert Certain" 182 / "George Certain" 1133 hits, first 10 each
   all modern noise; "duc de holstein" ermuyden 0; "jourduy les deux vostres" 0. Google Books API (country=US, key):
   "George Certain" Oranje 20 volumes, all 1865-1897 histories naming the pseudonyms (Putnam 1897 Dutch ed. snippet:
   "George Certain, aan zijn broeder Lodewijk ... over zijn nijpend geldgebrek", a summary, no cipher text);
   Holstein Ermuyden 1572 0. OpenAlex: "Willem van Oranje in brieven" 0 works.
3. **Community lists**: Cipherbrain, Cryptiana, Cipher Mysteries site searches (next section) 0 relevant;
   sources/cryptiana and sources/ciphermysteries grep 0.
4. **DECODE**: sources/decode dumps (24 Sept 2026) and Aymeloglu's catalogue/decode-catalog.csv (27 Sept 2026): the
   only 1572 records are the BL Harley 260 Walsingham letter-book items; no KHA 1572 Orange-Nassau record. No live
   DECODE crawl this pass (cost).
5. **Bourdeau** (github.com/dbourdeau/cyphersolver, cloned 7 Oct 2026 at 1fb3c46): grep 11008 / "Lambert Certain" /
   "George Certain" / Ermuyden: only numeric false hits (Zeschau ciphertext, an MZV message number, 4-gram tables);
   CATALOGUE.md has no Orange-Nassau 1572 row; no planning line names this letter.
6. **Aymeloglu** (github.com/aaymeloglu/unsolved-ciphers, cloned 7 Oct 2026 at d2800bb): same grep, one false hit
   (a BNE mms number). Cited, no code copied (rule 8).

Not opened: *Willem van Oranje in brieven. De Opstand in 1572* (Waanders 2022, eds. Eekhout, Huysman, Van Nierop,
Pollmann, Visser), a 40-letter popular selection; its table of contents could not be found online (neerlandistiek
review, DARE chapter records pp.124-179 seen: Gorinchem, an aanvalsplan, katholieken, 18 Oct letter). It is a
selection with introductions, not the standard edition; a letter whose cipher passages were deciphered there would
still be found by the verifier's phrase search. Next: its ToC via the owner's desk or a library catalogue, ~$0.5.

Verdict: `open` -- no printed text, decipherment or discussion of WVO 11008's numeral runs located.

`python3 tools/intake_gate_check.py wvo-11008-certain-1572` (KHF-2, 7 Oct 2026):

```
wvo-11008-certain-1572: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Web and blog check (KHF-2, 7 Oct 2026)

Plain web searches (WebSearch, standard): (1) `"Lambert Certain" "George Certain" Orange Lodewijk 1572` -- DBNL
biographical entry for the pseudonyms (points to Groen III p.428), DBNL Groen III pages; no decipherment. (2)
`Willem van Oranje Lodewijk van Nassau 12 augustus 1572 Keulen brief cijfer` -- WVO edition PDFs of other letters,
Scientias news; nothing on 11008. (3) `"A 11" "XI 15" Koninklijk Huisarchief Oranje 1572 chiffre` (shelfmark +
cipher word) -- WVO KHA introduction, no item hit. (4) `"J'ay recheu ce jourduy les deux vostres"` (incipit) -- 0
relevant. (5) `WVO 11008 Willem van Oranje Lambert Certain koopmansbrief Tournay 1572` (folder title) -- other WVO
edition PDFs, Waanders 2022 volume chapters; nothing on 11008. (6) `"Willem van Oranje in brieven" "Opstand in 1572"
...` and (7) the same with Lodewijk/Bergen -- ToC not listed (see above). (8) `"Certain" Oranje Lodewijk 1572
koopmansbrief schuilnaam cijferschrift Bergen Mons` -- 0 relevant. (9) model-solve announcements: `William of Orange
cipher letter 1572 decoded "Louis of Nassau" Claude OR GPT solves` -- Vals AI / Urquhart and GPT Napoleonic stories
only, two HistoCrypt papers opened (Lasry, French Wars of Religion letter; Lasry, d'Avaux 1684): neither concerns
Orange-Nassau 1572.
Blogs: `site:scienceblogs.de klausis-krypto-kolumne Oranje Nassau 1572 Lodewijk`, `site:cryptiana.blogspot.com
Orange Nassau 1572 cipher Louis of Nassau`, `site:ciphermysteries.com William of Orange Louis of Nassau cipher 1572`
-- no page from any of the three blogs returned, so no comment thread to open. No hit read as a decipherment.

## Premise check (KHF-2, 7 Oct 2026)

(a) Folder's own files: NOTES.md, passes/, decode.py, control.tsv mention no decipherment, gloss, clear copy or
"dechiffrement" other than this project's own held-key reading -- not found.
(b) Other solvers' working files: Bourdeau and Aymeloglu trees cloned and grepped (above); neither holds this letter,
the 1572 table, or a rendering of it -- not found. The held key is this repo's own (jan-van-nassau-1572-75
key_1572.tsv = orange-nassau-1572 key_nepveu.tsv); no other application of it to this text was located (searched as logged here and in AUDIT.md, 7 Oct 2026 -- a search result, not a novelty verdict; corrected by KHF2-VERIFIER).
(c) Physical neighbours: WVO PDF page 2 (address leaf, 3696x2100) viewed at native resolution, address and right
edge: the address in the clerk's hand, seal traces and the KHA stamp only; no decipherment, endorsement or slip.
Page 1 has no interlinear gloss (KH2-D, native crops). Neighbours in the WVO by the same cover names (opmerkingen
"Certain"): 5194 (24 June, KHA A 3, 895/I, in cipher, printed Groen III 448-449), 6222, 6223, 11096 (Louis to the
prince, 2 July, reply to 5194), 11097 (30 July, KHA A 11/XI 26, "thans in het archief ontbreekt"); none is a copy
or decipherment of 11008 -- not found. Note: Groen prints 5194 entire in clear French with no cipher mark, while WVO
calls the original "in cijferschrift": 5194's original image against Groen's text is a known-plaintext pair for the
same correspondence (the named next step in Remaining gaps).
(d) Recipient's side: the recipient is Louis, whose papers are this KHA A 11 series; his side is printed in Groen
(searched above). Spanish side (intercepts): Gachard's *Correspondance de Philippe II* / Alba not searched this pass
-- the letter reached Louis (it survives in his archive), so an intercept copy is unlikely; next for the verifier.

## While waiting

Not waiting on anyone: the next step (5194 known-plaintext check, ~$2.5) depends on nobody.

## Grading and language (KHF-2, 7 Oct 2026)

Re-counted from `ciphertext.tsv` and the table: run 1 M4 (120 outside the table); run 2 H18 (15 letters + 3 table
nulls); run 3 M8 (damaged start, no word); run 4 H11 M1 (pos 5, 69=y in "ermuyden"); run 5 H10 M2 (pos 3, 21=g for
the expected i; pos 12, 43). Total 54 = H39 M15, no C/S/I -- agrees with KH2-D. Seven of the 39 H tokens are table
nulls (run 2: 11 14 17; run 4: 40 44 52 31), so letters read at H = 32. `python3 decode.py --check` exits 0
(reading not stale, rule 7). Language: the clear text of the letter is French (incipit, address, "lequel a faict
charge", "Or pour"); the decoded runs are proper names inside French sentences ("le duc de holstein", Arnemuiden,
Vlissingen in Dutch place-name spelling). `tools/data/fr16` (16th-century French) is the era- and language-matched
corpus; the KH2-D judge FAIL (-1.648 vs real_p05 -1.098, N=39) reflects a names-only string at N=39, not a corpus
mismatch -- no Dutch or German corpus would fit better, since the only common word is French. The key-permutation
control (4-gram -1.435 vs shuffle p95 -1.576, 6/1000) is the result that carries the reading.

## 5194 known-plaintext check (W11008-KP, 8 Oct 2026)

Worker W11008-KP (LANE FAMILY-A2c, account 2), 22:19-22:3x UTC 8 Oct 2026 by `date -u`, brief
`.claude/briefs/runs/2026-10-08-ytbiz-family-2209-jobs.md`.

Prior work: `tools/prior_work.py wvo-11008-certain-1572 --item-spec 5194 --step-type key --fetch` exit 4. The only
row owed was the LEAD on this worker's own claim, recorded CLEAR in prior-work.tsv. The Groen-edition LEAD is the
input for this step (Groen prints 5194 in clear), not a stop. No earlier artefact for 5194 exists in ciphers/ (grep 5194).

Material. WVO 5194 (KHA A 3, 895/I; 24 June 1572, "George Certain" to "Lambert Certain", Frankfurt). The WVO PDF
(05194.pdf) has 3 pages. **Unlike 11008, almost the whole letter is in numerals.** Clear words appear only here and
there ("Mon frere Lambert Ceste servira pour vous advertir que", "suis", "toussiours", "Selon que desia plus.rs fois
vous ay escrit", ...). Small letters are written above some numerals (see below). Groen III pp.447-449 (CCCLXIX)
prints the letter in clear French; its OCR html was read through the Huygens retroboeken `pages.json?source=3` route,
pages 448-449.

Sample (cap 3.5, so not the whole letter). Page 1 manuscript lines 3-8 are `iiif_lines.py` bands L02-L04 (crops in
`images/w5194/`). Two blind Sonnet passes ran per band (`passes/w5194/`). Of the 140 tokens they disagree on 4: two
were settled from the image as clear letters (t, u), one clear letter stays c/e (M), and one is a spelling of
"toussiours". The reconciled file is `w5194_ciphertext.tsv`. It holds two runs bounded by clear anchors that Groen
also prints: R1 que..suis (14 numerals) and R2 suis..toussiours (97 numerals, plus the clear fragments me, d, a, r,
e, t, u).

Gate (pre-registered in `PREREG-W11008KP.md`, pushed before the diff): the LCS between the key_nepveu decode (letter
codes only, every other number a null) and Groen's span, against 1000 seeded permutations of the 24 letter values.
`python3 w5194_gate.py` (`--check` for rule 7) writes `w5194_gate.tsv`:

| run | numerals | letter codes | decode | Groen span | LCS | shuffle mean | p95 | shuffles >= real | verdict |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 14 | 5 | comie | comme je | 5 | 0.85 | 2 | 0/1000 | PASS |
| R2 | 97 | 33 | resouetrecytroiousncampagnfitroue | resolu de me mettre d icy a trois jours en campagne je me trouve | 32 | 10.79 | 14 | 0/1000 | PASS |

Result: **PASS on both runs.** 37 of the 38 decoded letters fall in order inside Groen's text. The Certain letters
use the printed 1572 Orange-Nassau table (multiples of 3 = letters), and 5194 pads it heavily with nulls: 38 of 111
numerals are letter codes and 73 are nulls. This confirms the key family for 11008. On 5194 the agreeing values are
grade C (aligned from print), on top of the H the table already carries. 11008's own reading is unchanged. The
control can differ from the target on this statistic, since a permutation changes which letters come out. The
shuffle p95 is far below ceiling (2 and 14, against maxima of 7 and 51), so the gate had headroom.

Interlinear letters on 5194 (descriptive only, not used in the gate). Both passes saw small letters above about 25
numerals in the sample. Where one sits over a letter code it often equals the table value (o over 42, m over 36,
t over 57, r over 51, a over 3, p over 45, n over 39, e over 15). The passes graded the attachment M, though, and
several sit over nulls. This looks like a partial period decipherment on the leaf; check it at native size before
citing it.

Where it was not found: no decipherment of 5194's numerals against Groen was found in ciphers/, sources/ or the WVO
record (which says only "in cijferschrift"). Groen prints the clear text without saying where the decipherment came
from. Not searched: Groen's notes on the neighbouring pages for a decipherment source, or secondary literature.

Native look at 11008 (gap item 2): run 1 reads "10 . 9 . 12 . 1?0", with the last group's middle digit smudged; at
three digits it falls outside the table either way. Run 3 reads "[stain] 36 : 38 : 15 : 25 : 37 : 40": 36 and 38
are confirmed (now H in ciphertext.tsv; 38 is a null), and the first two codes lie under a stain. `decode.py --check` OK.

Requests: resources.huygens.knaw.nl 7 (the 5194 record, 05194.pdf, one 404 on a wrong-path PDF, 11008.pdf,
pages.json source 3, Groen pp.448 and 449 html), >= 2 s apart, no 403/429.
