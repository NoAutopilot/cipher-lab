# BnF fr.4687 — Marguerite Paléologue, duchesse de Mantoue, to Louis de Gonzague, duc de Nevers, 1562-1564

Status: open

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Editions-first + one-leaf pass;
a formal six-source check-solved run is still owed before board promotion.

## Correction to the queue row

QUEUE.md M14 dated the item "(undated, volume covers 1585-91 Nevers-Gonzaga affairs)". Gallica's own catalogue
description (via `services/OAIRecord`) dates items 1-3 precisely:

> Recueil de pièces originales et de copies concernant l'histoire de la maison de Nevers. De 1562 à 1625...
> 1-3 Lettres, en italien, avec chiffres, de MARGUERITE PALEOLOGUE, duchesse DE MANTOUE, au duc de Nevers, Louis
> de Gonzague, son fils. De 1562 à 1564.

Margherita Paleologa (1510-1566) was regent-mother of Mantua during this period; her son Louis/Ludovico de
Gonzague later became Duke of Nevers in France. **1562-1564, not 1585-91.** QUEUE.md M14 row updated accordingly.

The same volume's item 41 is listed separately as "Chiffre. Quelques lignes non chiffrées sont en italien" —
an undated ciphered item elsewhere in the recueil, possibly unrelated to items 1-3 (different sender/date), not
investigated this pass.

## Checked (24 Sept 2026)

- Fresh shallow clone of `dbourdeau/cyphersolver`: no hit on "4687", "Paleologue/Paléologue" or "Marguerite" tied
  to this volume.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers`: no hit.
- `sources/cryptiana/web/nevers.htm` (Tomokiyo's own catalogue of ciphers in BnF fr.3995, "the Nevers
  collection") read locally, no fetch needed: covers a *different* volume — the Duke of Nevers' own cipher
  keys and correspondence as ambassador/courtier (fr.3995, fr.3251, fr.3413, etc.) — not his mother's 1562-64
  letters to him. No hit on "4687", "Paleologue" or "Marguerite" in the full 1420-line mirror.
- WebSearch for Italian scholarship on Margherita Paleologa's correspondence with her son in this period found
  only general biographical material (Wikipedia, Treccani); no edition or article naming this specific
  correspondence or its cipher was located. Tomokiyo's own background bibliography for the Nevers material
  (Daniela Ferrari 1999, "Mantoue et les Gonzague de Nevers"; Ariane Boltanski 2006, *Les ducs de Nevers et
  l'État royal*) was not checked against this specific volume this pass — flagged as the next step, not chased
  further under the check-solved brief's scope.
- Gallica IIIF, canvas 5 (f.1, faint, mostly illegible clear Italian), canvas 7 (f.5, clear Italian salutation
  "Al Ill.mo... figlio caris[si]mo"), canvas 8 (f.6, **ciphertext confirmed**: dense two-digit numeral groups,
  roughly 15-25 groups per line across at least six lines on this one leaf alone — a high-resolution crop is at
  `images/f8_crop.jpg`). Short Italian phrases appear in the left margin beside each ciphered line (e.g.
  "questa una quan[to] a quello che...", "et como...", "vi sera che... seguira..."); these read as the clerk's
  catch-phrase cues for filing/reference, not a complete parallel plaintext — no full interlinear decipherment
  was seen on this leaf. Images: `images/f5.jpg`, `images/f7.jpg`, `images/f8.jpg`, `images/f8_crop.jpg`.

## Class gate (24 Sept 2026)

Question: is this correspondence, its cipher, or a decipherment already in print? Searched (WebSearch, Google
Books API with `&country=US` and `&key=$GOOGLE_BOOKS_KEY` never printed, IA advancedsearch, JSTOR/academia.edu
reachability):

- Daniela Ferrari (1999), "Mantoue et les Gonzague de Nevers" — the article/catalogue Tomokiyo's own
  bibliography cites via an Academia.edu link. `academia.edu` answered curl/WebFetch with HTTP 403 (login wall);
  not read this pass. A WebSearch attempt to locate the title by exact string mostly surfaced an unrelated 1999
  numismatic item ("Mantova e i Gonzaga di Nevers" / "Mantoue et les Gonzague de Nevers", a coins-and-medals
  piece, possibly the same underlying catalogue Tomokiyo cites, possibly a namesake — not disambiguated) and
  confirmed Daniela Ferrari's role as director of the Archivio di Stato di Mantova 1990-2014. IA advancedsearch
  for "Ferrari Mantoue Gonzague Nevers" returned zero hits. Not located in readable full text this pass.
- Ariane Boltanski (2006), *Les ducs de Nevers et l'État royal* (Droz) — found and reachable via the Google
  Books API (volume id `dsInahmnar8C`, no full-view/snippet search-inside without a matching-phrase hit,
  `country=US` applied). Two relevant snippets surfaced by phrase search: "Marguerite Paléologue demeure
  résolument habsbourgeoise" (a general political-alignment remark, footnote 68) and "Paléologue, qui reçoit de
  Catherine d'assez fréquentes lettres, conservées dans les archives mantouannes: A.M." — this second snippet is
  about letters Marguerite Paléologue *received from Catherine de Médicis*, held in the Mantua state archives,
  not letters she *sent to her son*, and not BnF fr.4687. Targeted phrase queries combining Boltanski with
  "chiffre" and with "duchesse de Mantoue" + "correspondance" returned no hit tying the book to fr.4687 or to
  a cipher. No full read of the book attempted (Droz academic monograph, not on IA/HathiTrust full view this
  pass).
- General Gonzaga-Nevers editions/scholarship: Google Books full-text search for `"Marguerite Paléologue" "duc
  de Nevers" 1562` surfaced one distinct catalogue entry worth flagging — *Dictionnaire des manuscrits, ou
  Recueil de catalogues de manuscrits* lists an item "9510. ... Marguerite Paléologue, Duchesse de Mantoue à M.
  de Nevers, 1559" in an unnamed manuscript collection. This is a **different, single, earlier letter** (1559,
  three years before the fr.4687 items 1-3 start), not confirmed as the same correspondence — flagged, not
  chased further this pass. No other edition, calendar, or article naming this correspondence, its cipher, or a
  decipherment was found.
- `archivesetmanuscrits.bnf.fr/ark:/12148/cc577374` (BnF's own manuscript-level catalogue notice for fr.4687,
  which may carry a fuller bibliography than the OAI record already quoted above): returned HTTP 403 to both
  curl and WebFetch this pass (Cloudflare-style block, consistent with the Access playbook's note on this
  family of BnF pages); not read. Worth a browser-tool retry in a future pass.
- JSTOR: host reachable (`curl -o /dev/null -w "%{http_code}"` returned 200), but its search page requires
  JavaScript and returned no results through WebFetch's static render; no article search completed. Not
  retried further this pass (one attempt, per the good-citizen rule).

**Class-gate verdict: no prior print or discussion of these letters, their cipher, or a decipherment located.**
This is a search result under rule 10, not a claim of absence; Ferrari 1999 in particular was not actually read
(paywalled), only searched for by title, and the BnF's own fuller catalogue notice was not reachable this pass —
both are open risks flagged for whoever promotes this target, same shape as the M13 fr.16092 flag in ROOM.md.

## Key candidates (24 Sept 2026)

Question: does Tomokiyo's catalogue of ciphers in BnF fr.3995 (`sources/cryptiana/web/nevers.htm`, read in full
locally, no fetch) contain a key that could apply to this correspondence? Checked by keyword (`Marguerite`,
`Mantoue`/`Mantua`, `Paleolog`/`Paléolog`, `mere`/`mère`, `1562`-`1564`) and by reading the catalogue's own
scope statement and date range.

**No candidate found.** Three independent reasons:

1. Tomokiyo's fr.3995 catalogue is explicitly about ciphers belonging to Louis de Gonzague *as Duke of Nevers*
   ("the collection probably belonged to the duke"), a title he did not hold until his 1565 marriage to
   Henriette de Clèves — one to three years *after* the last of these letters (1564). Its earliest entry,
   no.1 (fol.1), is dated June 1580, sixteen years after this correspondence ends; the whole catalogued run
   is 1580-1594 (with more ciphers from other volumes, fr.3251/3315/3413/3416/3612/3616/3633/3641/3974-3994/
   4702/4712/4715, in the same post-1580 political-correspondent range). No entry predates 1580.
2. Two catalogue entries are captioned "Chifre avec la Duch[ess]e" / "avec la Duchesse" (no.2, fol.3, Oct 1584;
   no.6, fol.13, 1585) — but "la Duchesse" in a Duke-of-Nevers cipher of 1584-85 is his wife Henriette de
   Clèves, duchesse de Nevers, not his mother the duchess of Mantua; no.4 (fol.8, 1585) is captioned
   explicitly "avec la Duchesse ma feme" (my wife), confirming the sense. No entry is captioned with
   "mère" (mother), "Mantoue", or "Paleologue"/"Paléologue" — zero hits for all of these across the full
   1244-line mirror.
3. No.19 (fol.38, 1588) and no.20 (fol.40, May 1589) are the catalogue's closest formal matches to fr.4687's
   cipher type (both "substitution by two-digit figures... in Italian", two-part code, enciphering/deciphering
   tables) — but both post-date this correspondence by roughly a quarter century and are captioned for
   different correspondents (place names, not "la Duchesse" or a mother-son pairing).

Conclusion: fr.3995 is the wrong volume by both period (Duke-of-Nevers-era ciphers, 1580s-90s) and relationship
(wife/political correspondents, not mother); no key transfer is plausible without an intervening, unstated
20-year reuse. No candidate key promoted; none of Tomokiyo's fr.3995-family ciphers were tested against
fr.4687's ciphertext this pass.

## Extent (24 Sept 2026)

Viewed Gallica IIIF canvases 5-15 (one request per canvas, 1.5s apart, descriptive User-Agent; one connection
reset on an `info.json` request, recovered on a single retry after a pause, per the good-citizen rule). Full
manifest and per-canvas content notes: `images/manifest.json`.

Of the eleven canvases covering items 1-3 in this range, **three carry cipher**: canvas 8 (dense multi-line
block, mid-letter-1, previously found and cropped as `images/f8_crop.jpg`), canvas 9 (one dense cipher line
near the close of letter 1, cropped as `images/f9_crop.jpg`), and canvas 10, left page (a six-line dense cipher
postscript closing letter 1, immediately after the clear-Italian line "lase le mie le posete brusare" — burn
these of mine — and above the signature; cropped as `images/f10_crop.jpg`). Canvas 6 is very faint
pencil/draft script on both pages, not legible enough at this resolution to classify as cipher or clear text
(flagged "uncertain" in the manifest, not chased further). Canvases 5, 7, 11, 12, 13, 14, and 15 are clear
Italian throughout wherever legible; canvas 15 (right page) carries what reads as letter 2 (or 3)'s closing
signature "vostra madre la Duchessa di Mantua" and a date "26 [di] 9bre [novembre] del 6-" (year's last digit
not legibly read at this resolution). This suggests the volume's three cipher passages found so far all belong
to the *first* of the three catalogued letters (the one opening near canvas 5/7 and closing on canvas 10), with
the second and/or third letters, as far as canvases 11-15 go, running entirely in clear Italian — not confirmed
beyond canvas 15, which is as far as this pass's brief went.

## Passes (24 Sept 2026)

Two blind Sonnet subagents transcribed the three cipher crops (`images/f8_crop.jpg`, `images/f9_crop.jpg`,
`images/f10_crop.jpg`) independently, neither shown the other's file: `passA.tsv`, `passB.tsv` (line, position,
group, confidence; clear Italian runs as `[PLAIN:"..."]` rows, flagged illegible spots as `[flagged: ...]`
rows). No reconciliation attempted, no decoding, no novelty wording. The two files are the primary record;
this is a description of them, not a merged reading.

Totals: pass A read 240 cipher-group rows + 25 PLAIN/flagged rows across 11+8+9=28 manuscript lines; pass B
read 171 cipher-group rows + 31 PLAIN/flagged rows across the same 28 line ids. Both passes independently
arrived at the same line count and the same high-level structure (one dense cipher block on f8, one cipher
line embedded in plain text on f9, one dense six-line cipher postscript on f10) without having seen each
other's file.

Per-line agreement, restricted to cipher-group rows and comparing by (line, position) where both passes
assigned some group to that exact slot (a coarse measure — it penalizes any upstream difference in how a
dense run was segmented into groups, not just misread digits):

| line | A groups | B groups | exact match at common positions |
|---|---|---|---|
| f8_L2 | 8 | 8 | 7/8 (88%) |
| f8_L3 | 20 | 17 | 3/17 (18%) |
| f8_L4 | 16 | 12 | 0/11 (0%) |
| f8_L5 | 13 | 8 | 0/8 (0%) |
| f8_L7 | 20 | 9 | 1/9 (11%) |
| f8_L8 | 17 | 12 | 2/12 (17%) |
| f8_L9 | 19 | 12 | 0/12 (0%) |
| f8_L10 | 21 | 11 | 0/11 (0%) |
| f8_L11 | 0 (flagged illegible/cropped) | 10 | n/a — passes disagree on whether this line is even legible |
| f9_L6 | 13 | 11 | 2/11 (18%) |
| f10_L2 | 13 | 11 | 0/11 (0%) |
| f10_L3 | 17 | 10 | 1/10 (10%) |
| f10_L4 | 18 | 10 | 0/10 (0%) |
| f10_L5 | 16 | 10 | 0/10 (0%) |
| f10_L6 | 15 | 11 | 0/11 (0%) |
| f10_L7 | 14 | 9 | 0/9 (0%) |

Overall: 16/160 (10%) position-exact agreement across the 16 cipher-bearing lines. f8_L2 (the shortest,
least-dense cipher line, 8 groups) is the one clear exception at 88%; every longer, denser line falls to
single digits of percent agreement, driven mostly by the two passes segmenting the same unbroken digit
string into a different number of groups (A consistently more groups than B on every dense line) rather than
by disagreement over individual digit shapes — both subagents independently flagged this same difficulty
(ambiguous group boundaries in a continuous cursive numeral hand) in their own reports. f8_L11 is a clean
disagreement about legibility itself, not just segmentation: pass A treated it as illegible/cropped (0 rows),
pass B read 10 groups from it.

Reading: at this crop resolution, the two passes agree closely on where cipher is present and on the overall
letter structure, but not, group-for-group, on where one cipher group ends and the next begins in the denser
lines — a transcription-quality finding, not a reconciled reading. No group boundary was adjudicated and no
group was decoded.

## Sources

- Gallica: `https://gallica.bnf.fr/ark:/12148/btv1b90075058`, OAI record via
  `https://gallica.bnf.fr/services/OAIRecord?ark=btv1b90075058`.
- `sources/cryptiana/web/nevers.htm` (S. Tomokiyo, "Ciphers in BnF fr.3995 (the Nevers collection)"), local
  mirror, no fetch.
- github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers (both checked, no relevant content;
  Aymeloglu has no licence, cite only, nothing copied).

## Requests, check-solved pass (24 Sept 2026, earlier)

gallica.bnf.fr: 1 OAI record + 4 IIIF image fetches (1 crop). github.com: 2 shallow clones (shared with M13,
deleted after grep). WebSearch: 1 query.

## Requests, literature+key-hunt+extent+passes worker (24 Sept 2026)

gallica.bnf.fr: 1 manifest.json + 8 canvas image fetches + 2 info.json (1 connection reset, retried once,
recovered) = 11. googleapis.com (Google Books, `&key=$GOOGLE_BOOKS_KEY&country=US`, key never printed): 9
queries. archive.org advancedsearch: 1. jstor.org: 1 reachability check + 1 WebFetch (no usable result,
JS-gated search page). academia.edu: 1 reachability check (403). archivesetmanuscrits.bnf.fr: 1 WebFetch (403).
WebSearch: 3 queries. No logins, no credentials printed. Two Sonnet subagents for the blind passes (within the
brief's fan-out limit).

## Segmentation (24 Sept 2026, reconciler, Opus)

Written before reconciling, from the page images. The on-disk crops (`f9_crop.jpg`, `f10_crop.jpg` at 800 px;
`f8_crop.jpg` upscaled) were too coarse to show separators, so three native-resolution IIIF regions were fetched
once (`images/f8_native_region.jpg`, `f9_native_region.jpg`, `f10_native_region.jpg`; regions and request log in
`images/manifest.json`). Evidence, read at about 400 dpi:

- **No separators.** Digits run at an even pitch across each line. There is no consistent space, point, virgule or
  superscript between groups. The dots are part of the letterforms: the tittle of `i` (the scribe writes 1 as a
  dotted i, and the dot often drifts left), the entry tick of `2` and `7`, and the ink blobs at the ends of the
  descenders of 4, 7 and 9. They occur at every position, so they do not mark group boundaries.
- **One non-digit sign, `y`** (an `ij`/`ÿ` shape with a long descender, sometimes with two dots). It occurs 28 times
  in 588 signs. Pass A saw it on its own and wrote it `11~`; pass B read it as 9 or 1. Here it is a separate sign.
  Its function (letter, null or divider) is not decided. It comes most often after 7, 4 or 3 and before 6 or 2.
- **4 and 9 are separate shapes.** 4 has a horizontal crossbar through the stem; 9 is a q with a plain descender.
  Most of the A/B digit disputes are 4/9 pairs, and the coarse crops lose the crossbar.
- **Scribal corrections** (flagged in the `note` column of ciphertext.txt): a superscript `24` over a struck group
  (f8_L4 start); an interlinear `y20` placed at a colon-shaped caret after `17` (f8_L9; pass A had put it in
  f8_L8); a superscript `17` over a blotted group (f9_L6); a superscript `2` over a blotted digit (f10_L7). Each
  replacement is one or two digits, or `y` plus two digits. None of them fixes a group length.
- **Statistical test** (`seg_test.py`). Under a fixed two-digit grid, the most frequent two-digit units should sit on
  one parity within a line. The parity lock is 0.577 with `y` kept as a sign and 0.629 with `y` dropped.
  Matched synthetic controls use the same line lengths, Italian letter frequencies and homophonic codes. A fixed
  two-digit control scores 0.716 / 0.657 / 0.643 (mean) at 0 / 5 / 10 % digit insertion-deletion error, with 5th
  percentiles 0.632 / 0.599 / 0.593. A mixed 1/2/3-digit control scores 0.584-0.586 (95th percentile about 0.62-0.63).
  Shuffled real lines score 0.611. The runs between `y` signs have odd length 24 times out of 44. So a strict
  two-digit grid with `y` as a one-sign token falls below every fixed-two-digit control's 5th percentile and sits
  at the mixed control's mean. With `y` dropped, the value is compatible with either design. The test is weak
  (shuffled lines overlap both controls) and **leans mixed-length without settling it.**

**Rule adopted.** The scribe marks no group boundaries, and neither the image nor the statistics settle the group
length. The transcription unit is therefore the **sign** (0-9 and y). Each pass's grouping is kept per sign as
an alternative (`a_start`, `b_start`), and every intra-line boundary counts as M. Frequent units are 17, 18,
20 and 22 (30, 26, 30 and 18 occurrences as adjacent pairs). They are consistent with a design built on 1x/2x
two-digit numbers plus single signs, which is a hypothesis for the solver, not a finding.

## Reconciliation (24 Sept 2026)

`reconcile.py` aligns pass A, pass B and the reconciler's native-resolution reading (`passC_native.tsv`, one sign
stream per line) and writes `ciphertext.txt` (line, pos, sign, conf, alt, a_start, b_start, note) and
`inventory.tsv`. `python3 reconcile.py --check` exits 1 if either file is stale. Confidence is H when A, B and
the native reading all give the same sign (at least two readings). Otherwise it is M, with the other readings
in `alt`. The alignment is difflib's, which pairs signs inside replaced blocks by position, so H is a slight
overcount wherever a pass dropped or added a sign.

| | count |
|---|---|
| lines | 17 (the 16 both passes read, plus f8_L11, which only pass B read; pass A called it cut off) |
| signs | 588 (H 480, M 108) |
| distinct signs | 11 (0-9, y) |
| intra-line boundaries | 572, all M under the rule; A and B agree on 327 (101 boundary, 226 no boundary), disagree on 134; one pass lacks the sign at 111 |
| distinct adjacent sign pairs | 99 |

Sign counts (inventory.tsv): 1 100, 2 93, 9 63, 4 56, 5 47, 7 45, 3 41, 8 41, 0 38, 6 36, y 28.
Top-20 adjacent pairs (candidate units, not established groups): 20 30, 17 30, 18 26, 51 19, 22 18, 41 15, 92 14,
32 14, 91 12, 61 12, 85 12, 19 11, 29 10, 24 10, 62 10, 84 10, 31 9, 73 9, 42 9, 01 8.
f8_L11 is M-heavy (15/37 H) because only one pass read it.

**Coverage gap: cipher the passes never saw.** The native regions show cipher outside the three old crops:
about 4 lines at the top of canvas 9's left page (from "...ogni cosa p. che 1759" to "...vostro S. Idio facia",
with clear words such as "et mi" mixed in), about 4 lines on canvas 8's left page (lower half, above "i cardinali
vostro fratello..."), and a twelfth cipher line on canvas 8's right page below f8_L11 (ending with a carried "184").
Estimate: about 280-300 more signs, so about 870-890 in all. They are in the native regions on disk. They need
two blind passes before anything is run on the whole text (a follow-up, not done here). Canvas 6 (faint) is
still unclassified.

**Enough for a solver run?** Not yet. `tools/nomenclator_anneal.py` takes pre-segmented group codes, and this text
has no settled segmentation. A run needs either a segmentation hypothesis fixed in advance (for example "1x/2x
are two-digit, 3-9 and y single") or a solver that infers segmentation jointly. It should also wait for the
missing ~300 signs to be transcribed. A matched control would need: Italian letter prose of the 1560s at the same
length (~880 signs); the same 11-sign alphabet with one ~5 % extra sign; the same code design as the hypothesis
under test; the text written as an unbroken stream at the same line lengths; about 18 % sign-level noise, 4/9
confusions in particular; and scoring by the same model (`tools/italian_ngram.py`, which was built on 15th-c.
Lombard chancery Italian, so a 1560s Mantuan corpus would be the better fit).

Requests this pass: gallica.bnf.fr 3 (IIIF regions, 2 s apart, all 200). No other host, no subagents, no logins.

## Joint-segmentation solver (24 Sept 2026)

Solver session (Opus, LANE G brief). Input: the reconciled 588 signs of `ciphertext.txt` only (first reading per
sign, `solver/signs.txt`). The ~290 signs of the extra regions were not included: `passA_extra`/`passB_extra`
had not been pushed when this ran. **Result: a clean negative with matched controls. No reading is claimed.
Grade counts: H 0, C 0, S 0, M 0, I 0 (no token read).**

**Model.** 16th-c. Italian letter model, built from six Internet Archive full texts: Ferrato's Gonzaga
princesses' letters (Mantua 1879), Caro, B. Tasso, letters to Aretino, Cibrario's *Lettere inedite di ...
principi* (manifest `tools/data/it16/manifest.json`). `tools/italian16_corpus.py` keeps paragraphs where
period letter markers outnumber editorial ones, giving 417 paragraphs and 282,755 letters. It feeds
`tools/italian_ngram.py build`, which fits an order-5 model. Every 10th paragraph is held out
(`solver/control_heldout.txt`) as control plaintext, and the control-solving model never saw it.

**Structure tests** (`solver/structure.py`, 20,000 shuffles of the real signs over the real line lengths):

| statistic | observed | shuffle mean | p |
|---|---|---|---|
| `1` at line end or before `y` | 0 | 7.4 | 0.00015 |
| `2` at line end or before `y` | 3 | 6.8 | 0.068 |
| `0` not preceded by `2` | 8 | 32.1 | <0.00005 |
| `7` not preceded by `1` | 15 | 37.5 | <0.00005 |
| `8` not preceded by `1` | 15 | 34.2 | <0.00005 |

`1` behaves as a prefix sign. It occurs 100 times and never ends a line or stands before `y`. `0` is almost
always the second half of `20`. The design most consistent with this is prefix-free: 1x and 2x are two-digit
units, and 0, 3-9 and `y` are single units. It parses the stream into 423 units of 30 types, with 3 exceptions
(a `2` before `y`). A single/double split does not mark vowels against consonants: adjacent single/double
alternation is 0.49, while Italian vowel/consonant alternation is 0.73. `y` is too rare for a word divider
(one per 15 units). This design is a hypothesis the statistics favour. It is not established.

**Solver** (`tools/seg_homophonic.py`, new). It takes a design (prefix set, with `y` as a letter or a null),
segments the stream, and anneals a homophonic key (any number of units per letter) against the model, with
restarts and a steepest-ascent finish. A unigram-divergence guard (weight 3) stops the collapse to an all-`i`
key that the first two runs fell into on both the target and the noisy controls. The design is chosen by
running each candidate and comparing it with nulls. Sign-shuffle nulls re-segment the shuffled signs; unit-shuffle
nulls keep the units and destroy their order.

**Matched controls (rule 3).** Held-out Italian of 360 letters under a random homophonic key over the same
29-unit inventory (1x/2x plus 0, 3-9 and `y`). It is cut into lines of the target's lengths at unit boundaries,
giving 584-646 signs against the target's 588. Sign noise is added (drops, insertions, 4/9 swaps), and the
text is solved blind with the same settings. Per-token letter accuracy, 5 seeds each (`solver/runs/control_*`):

| control | mean accuracy | per seed |
|---|---|---|
| 1x/2x, y letter, 0 % noise | 1.000 | 1.00 1.00 1.00 1.00 1.00 |
| 1x/2x, y letter, 5 % noise | 0.917 | 0.91 0.88 0.94 0.95 0.91 |
| 1x/2x, y letter, 10 % noise | 0.754 | 0.79 0.86 0.80 0.53 0.79 |
| 1x/2x, y letter, 15 % noise | 0.244 | 0.20 0.29 0.14 0.39 0.20 |
| 1x/2x, y null (6.6 %), 5 % noise | 0.781 | 0.21 0.90 0.92 0.95 0.93 |

**Target** (`solver/runs/target*`). Model score per unit, including the guard, against nulls:

| design | units | types | score/unit | null (kind) | z | output |
|---|---|---|---|---|---|---|
| 1x/2x, y letter | 423 | 30 | -3.489 | -3.802 ± 0.008 (signs) | 40.9 | not Italian |
| 1x/2x, y letter | 423 | 30 | -3.489 | -3.865 ± 0.044 (units) | 8.5 | not Italian |
| 1x/2x, y null | 395 | 29 | -3.538 | -3.789 ± 0.061 (signs) | 4.1 | not Italian |
| 1x only, y letter | 489 | 20 | -3.908 | -4.159 ± 0.045 (signs) | 5.6 | not Italian |
| 2x only, y letter | 515 | 21 | -3.866 | -4.147 ± 0.039 (signs) | 7.2 | not Italian |
| 1x/2x, y letter, 40 single-reader signs dropped | 390 | 30 | -3.458 | -3.822 ± 0.034 (units) | 10.7 | not Italian |
| 1x/2x, y null, same variant | 368 | 29 | -3.545 | -3.834 ± 0.083 (units) | 3.5 | not Italian |

The best output (1x/2x, y letter) begins `hcioteonaaleosiebratenesedrauinidratocalamabiracheonsihersosuleet
cittacarneet...`. It contains isolated short Italian strings (`che`, `et`, `citta`) but no run of words.

**Calibration.** On a 10 % noise control of the same size (`solver/runs/ctl_unitnull_n0.1.txt`), the solver
scored -3.392 per unit against a unit-shuffle null of -3.734 ± 0.043, z = 7.9. The target's -3.489 and
z = 8.5 are indistinguishable from it. True-key scores of controls are about -1.5 per unit at 0 % noise, -2.2
to -2.5 at 5 %, -2.9 to -3.1 at 10 % and -3.5 to -4.5 at 18 %. So the target's order carries some structure,
but its score sits where a noisy (roughly 10 %+) Italian control would sit, or where a non-Italian or
nomenclator design would. The solver cannot tell these apart at this length.

**What the negative means.** The solver reads a matched 1x/2x homophonic control at 100 % (clean) and 92 %
(5 % sign noise), and the target does not read under that design or any of the four others tried. The
negative holds only (a) for a pure letter-substitution design (no code words, no syllables), (b) for the
588 signs as reconciled (18 % of them M, and 40 seen by only one of the three readings), and (c) in 16th-c.
literary/chancery Italian. Margherita Paleologa's clear lines ("lase le mie le posete brusare") are strongly
Mantuan and phonetic, which the model does not cover. Above about 10 % transcription noise the control itself
fails (24 % at 15 %), so a negative on this transcription is weak evidence.

Next moves, most promising first. None of these was done here.
1. Add the ~290 extra signs once reconciled; at about 880 signs the 10-15 % noise band should be readable.
2. A second native-resolution reading of the M signs, especially 4/9 and the `A:-,B:-` signs.
3. A Mantuan dialect corpus (e.g. the Gonzaga women's letters in Ferrato 1879, weighted up).
4. A design with syllable or word codes among the 1x/2x units.

Requests this session: archive.org 13 (1 advancedsearch, 6 metadata, 6 `_djvu.txt` downloads), all 1.5 s
apart, descriptive User-Agent. No other hosts, no logins, no subagents.
