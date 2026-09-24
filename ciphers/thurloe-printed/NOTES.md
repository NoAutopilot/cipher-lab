# Thurloe printed cipher letters (23 items, Birch 1742, vols 2/3/5/7)

**Status: partial** for P9, P14, P15, P17 (Tomokiyo-reconstructed cipher systems);
**found-solved** for P11, P12, P13 (verifier, 24 Sept 2026, AUDIT.md: class N0 -- Birch 1742,
vol. 5 pp. 67-69, prints this letter's cipher groups with the contemporary decipherment set
above each line, and British History Online reproduces that text); **found-solved** for P19, P21, P22, P23 (24 Sept 2026: four
letters of Lord Fauconberg to Henry Cromwell, 1658, which the print gives with an interlinear
decipherment and whose cipher Tomokiyo has reconstructed -- see "Monck pool solver" below);
**open** for the other 12 rows (11 distinct letters, since P5/P6 are two cipher clusters of one
letter). No item here is `solved`;
rule 10 applies throughout -- nothing below is described as new, unpublished, unread, first
or never printed, and no N-class is assigned (that is a verifier's job).

Sources: `sources/ia-fulltext/thurloe-check.tsv` (this project's own 24 Sept 2026 leaf-check,
ROOM.md 02:05-02:12), `sources/ia-fulltext/runs.tsv` (raw numeral-cluster detector, 23 Sept
2026), `sources/cryptiana/web/thurloe.htm` (Tomokiyo, local mirror). Checked 24 Sept 2026
(this pass): re-read thurloe.htm in full for every section touching Blake, Montagu (Mountagu)
and Downing; grepped for the other 16 correspondents (Fleetwood, Bradshaw, Prideaux, Creed,
Steele, Cudworth, Stoakes, Harrison, Monck, Disbrowe, Maynard, Richard Cromwell's speech) --
no hits beyond what the 24 Sept leaf-check already logged in thurloe-check.tsv. Neither solver
repository (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers) was re-cloned this pass; their
"Fleetwood"/"Bradshaw"/etc. no-hit results are cited from the same-day leaf-check worker
(ROOM.md 02:12), not re-verified independently.

## 1. Extraction (`index.tsv`, `<Pn>/ciphertext.txt`)

`tools/thurloe_extract.py` (new, reusable) reads the cached djvu text (fetched fresh this
pass -- `sources/ia-fulltext/{collectionofstat02thur,03thur,05thur,07thur}_djvu.txt`, all 4
volumes previously cached but not present in this container; refetched once each, 1.5s apart,
gitignored per existing `.gitignore` rule), takes a window around each row's `thurloe-check.tsv`
`ocr_lines` value (padded, capped at 260 lines so the longest items -- P17 at 205 raw OCR
lines -- stay in one file), and classifies each line as cipher (>=4 tokens, >=70% look like
1-4 digit numerals, same threshold as `tools/ia_numeral_runs.py`) or plain. Cipher lines get a
RAW column (verbatim OCR) and a CLEANED column (only the l/i->1, o->0 OCR-digit-misread
substitution `ciphers/orange-nassau-1572/decode.py` already uses in this repo; a token still
not a clean 1-4 digit run after that gets a trailing `?`, marked doubtful, not fixed). Plain
lines are kept verbatim as `[PLAIN:"..."]`. This is a narrow, padded window around the
detector's own cluster, not the full printed letter -- most of these letters run several pages
of otherwise-clear English/French with the numeral cipher confined to a paragraph or two;
widening every window to the full letter was out of this pass's scope and budget.

23 `ciphertext.txt` files written (`ciphers/thurloe-printed/P2/` .. `P24/`), `index.tsv`
summarising identifier, window, printed page, sender/recipient/date, cipher system, cipher-line
and raw-numeral-token counts, and a `keyed` flag. Numeral counts are raw token counts (OCR
tokens matching the cipher-line detector), not deduplicated distinct-value counts, and are not
directly comparable across rows with different window sizes -- they measure what this pass's
window captured, not the full letter's cipher content. Two OCR-quality problems are visible
directly in the committed files and not repaired: (a) the digit-vs-letter OCR confusion the
`?`-marked CLEANED column exists for (e.g. P9's `3&.`, `6-/.`, `6^.`; P22/P23's stray letters
mixed into numeral runs), and (b) for P17 (Downing) specifically, the source note already
flagged "heavily garbled OCR... long-s/Gothic type" -- confirmed: many CLEANED tokens there are
letter/digit mixes (`f10n0fthe?`, `ear1?`) rather than clean numerals, well beyond ordinary
OCR noise.

## 2. Check-solved for the 5 keyed letters

(Corrected by the verifier, 24 Sept 2026: P11-13 *is* found-solved -- the decipherment of this
letter is printed by Birch himself, interlined above the cipher; see section 9 and AUDIT.md. The
sentence below held only for Tomokiyo's page, not for the print.) None of the 5 is `found-solved`
on Tomokiyo's evidence alone: Tomokiyo's page reconstructs each correspondent's cipher
*from other letters* (mostly BL Add MS manuscript items, DECODE records, or a crib phrase from
a different Thurloe-vol.3 letter), and does not print a decipherment of any of P9, P11-15 or
P17 specifically.

- **P9 (Blake, 14 June [1655], printed p.~611):** Tomokiyo's "General Blake (1655)" section
  names two Blake-to-Cromwell letters by date/page -- 12 June 1655, p.541 ("almost entirely in
  cipher") and 4 July 1655, p.611 ("only enciphered his reference to the Plate Fleet"). Our
  row's page (~611) matches the *4 July* letter, not "14 June" as dated in thurloe-check.tsv --
  flagged, not resolved this pass (possible "4 July"/"14 June" OCR or transcription slip
  upstream of this folder; the extraction here is of whatever text sits at djvu lines
  51599-51611 regardless of which date is correct). The window's small numeral count (29 raw
  tokens) is consistent with Tomokiyo's description of the 4 July letter as only partially
  enciphered, which supports p.611=4 July over 14 June. Not itself decoded by Tomokiyo; the
  cipher system given (E=24/54/[82], plus a worked example "26 33 39 24 36 31 24 32 38" =
  "gouerment") is reconstructed from the Hague-agent correspondence, reused for Blake because
  Tomokiyo states the two use the same cipher.
- **P11/P12/P13 (Montagu, 20 April 1656, one letter, 3 clusters):** Tomokiyo's "Edward Montagu"
  section states the cipher (E=18/42/56/93, THE=407) from Montagu's correspondence generally
  and confirms it was used in this letter's cipher family; he does not transcribe this letter's
  own plaintext. The 24 Sept leaf-check already confirmed "407" recurs at plausible "the"
  positions directly in the OCR (crib alignment, not a full reading).
  Not one of the 4 catalogued STUCK items.
- **P14 (Protector [Cromwell] to Blake and Montagu, 9 June 1656, p.101):** Tomokiyo names this
  *exact* letter by page ("Cromwell wrote to Blake and Montague (9 June 1656, Thurloe State
  Papers, p.101)") as using the same reconstructed Montagu cipher, but this is cited as an
  *example of where the cipher was used*, not as a printed plaintext of the letter. No
  decipherment of this letter appears on his page. Also cross-referenced to BL Add MS 4166
  f.90-91 / DECODE R4885 -- a manuscript item this pass did not fetch.
- **P15 (Mountagu, 16 Sept 1656, aboard the Naseby, p.~420-421):** same cipher family per
  Tomokiyo, this specific date/letter not individually named on his page (i.e. weaker
  attribution than P11-14, inferred from "same reconstructed cipher system", not a direct
  citation of this letter).
- **P17 (Downing, printed p.365):** Tomokiyo's "George Downing (1658-1660)" section gives the
  cipher (E=39-45, THE=468) reconstructed from "many of his letters" generally and cites the
  original key manuscript (BL Add MS 4166, f.115-116, DECODE R4896) -- not this specific
  printed letter, no plaintext of it given. (Tomokiyo's page also gives a *different* Downing
  code, to Lord Clarendon -- not used here, since P17 is Downing-to-Thurloe correspondence.)

## 3. Mechanical decode of the 5 keyed letters

`decode.py` (rule 7: `python3 decode.py --check` regenerates `reading_*.txt` from
`<Pn>/ciphertext.txt` + the relevant `key_blake.tsv` / `key_montagu.tsv` / `key_downing.tsv`
and exits non-zero if stale) applies exactly the values Tomokiyo's page states -- a handful of
E-homophones, THE, and under a dozen higher-value code words per system -- nothing guessed,
nothing repaired, nothing extended. **Grade key:** H = CLEANED token is a key value; M =
`thurloe_extract.py` already marked the token doubtful (OCR); U = a clean number simply not in
the key (this project has fewer than 20 values for cipher systems Tomokiyo estimates run to
several hundred to ~600 elements each, so U dominates by design, not by failure).

| Letter | H | M | U | total | H-graded content |
|---|---|---|---|---|---|
| P9 (Blake) | 13 | 4 | 12 | 29 | 3 e, 2 t, 2 r, 1 o, 1 n, 4 u (letter-frequency crumbs, no words) |
| P11-13 (Montagu) | 36 | 27 | 256 | 319 | 22 e, 8 the, 6 and |
| P14 (Protector) | 7 | 8 | 72 | 87 | 6 e, 1 the |
| P15 (Mountagu) | 15 | 8 | 61 | 84 | 10 e, 3 and, 2 the |
| P17 (Downing) | 99 | 73 | 892 | 1064 | 99 e (no other key value recurs in this window) |

(P11-13 superseded 24 Sept 2026 by section 9 below: the print carries a decipherment above the cipher, now aligned.) **None of the five outputs is continuous English, or close to it** -- H-graded tokens are
letter-frequency crumbs (mostly "e", the commonest English letter, which is exactly what a
sparse homophone-only key should surface first) plus a few correctly-recurring function words
("the", "and") that corroborate the crib alignment already logged in thurloe-check.tsv, not a
readable passage. This is the expected result of applying an intentionally partial key
(Tomokiyo's own reconstructions cover roughly 1-2% of each system's element count) and is not a
cryptanalytic negative in the rule-3 sense (no claim "this cipher resists reading" is being
made; the key itself is incomplete by its source's own account, not exhausted). U-token counts
are dominated by numbers this project has no value for, not by numbers the key rejects.

## 4. The 16 unkeyed rows (15 distinct letters), grouped

No key or reconstruction found for any of these in Tomokiyo's page or (per the 24 Sept
leaf-check, not re-run this pass) either solver repository. No cryptanalysis attempted.

By correspondent (rows, raw numeral-token count from `index.tsv`, summed per correspondent):

| Correspondent | Rows | Letters | Raw numeral tokens (summed) |
|---|---|---|---|
| Gen. Monck | P19, P22, P23 | 3 | 51 + 371 + 565 = 987 |
| [Richard Cromwell's speech, no correspondent] | P21 | 1 | 623 |
| Mr. Bradshaw (Hamburgh) | P3, P7 | 2 | 57 + 574 = 631 |
| Major Creed | P5+P6 (one letter, 2 clusters) | 1 | 337 + 167 = 504 |
| Consul Maynard | P24 | 1 | 350 |
| Ld. chief baron Steele | P8 | 1 | 316 |
| Mr. W. Prideaux | P4 | 1 | 184 |
| Dr. Tho. Harrison | P18 | 1 | 119 |
| Mr. S. Disbrowe | P20 | 1 | 73 |
| Dr. Ralph Cudworth | P10 | 1 | 66 |
| Capt. Stoakes | P16 | 1 | 48 |
| Gen. Fleetwood | P2 | 1 | 39 |

By apparent system (numeral range / group style, from thurloe-check.tsv's own notes, not
re-derived here): **P19, P21, P22, P23** (Monck x3 + Richard Cromwell's speech transcript, all
vol.7) share a small-alphabet style, numerals mostly under 50, noted by the leaf-check as
"resembles" each other -- spot-checked this pass (section 1 above) and confirmed: all four
windows' CLEANED tokens sit in the same low range with the same short-group rhythm. This is the
single largest same-style pool among the 18: **1,610 raw numeral tokens across 4 items**, well
above any other row or correspondent-group here. No reconstruction exists for it in the sources
checked, and no cryptanalysis is attempted in this pass. Every other row (P2, P3, P4, P5/P6,
P7, P8, P10, P16, P18, P20, P24) is its own apparently-unrelated numeral cipher with no noted
commonality to any other row.

**Which systems have enough text for cryptanalysis (assessment only, not attempted):** the
Monck/Cromwell's-speech pool (987 + 623 = 1,610 tokens across a shared style) is the only
unkeyed group in this set large enough that a classical homophonic/nomenclature attack would
plausibly have material to work with, and it is four separate documents rather than one long
letter, which helps a frequency-based attack more than a single short item would. Bradshaw's
two letters (631 tokens) and Creed's one letter (504 tokens) are a distant second and third,
each a single correspondent but each still under a third of the Monck/speech pool. Every
individual row under roughly 200 raw tokens (P2, P10, P16, P18, P19, P20; P19 counted alone) is
almost certainly too short on its own for anything beyond crib-hunting. Per CLAUDE.md rule 3,
any future cryptanalytic attempt on these would need a matched synthetic control of the same
length/symbol-count/design before a negative result means anything -- not attempted here.

## 5. Status per letter

| Row(s) | Status | Next step |
|---|---|---|
| P9 | partial | resolve the 14 June/4 July date question against the BHO page image before treating this as distinct from Tomokiyo's named 4 July letter |
| P11-13 | found-solved | verifier 24 Sept 2026 (AUDIT.md, N0): decipherment printed interlinearly by Birch 1742, v.67-69, and online at BHO; `reading_P11-13.txt` is an alignment of that printed decipherment. Not a cryptanalysis target. (The earlier "BL Add MS 4166" pointer was wrong for this letter: Tomokiyo's Montagu manuscript is BL Add MS 4200 f.76, 19 May 1656, DECODE 8387.) |
| P14 | partial | as P11-13; also check BL Add MS 4166 f.90-91 (DECODE R4885) Tomokiyo cites for this exact letter |
| P15 | partial | as P11-13 |
| P17 | partial | BL Add MS 4166 f.115-116 (DECODE R4896) is Downing's original key manuscript per Tomokiyo -- reading it would turn most of this letter's 892 U-tokens into H |
| P19, P21, P22, P23 | found-solved | Fauconberg to H. Cromwell, 1658: decipherment printed interlinearly by Birch, key reconstructed by Tomokiyo (section 8). Not a cryptanalysis target |
| P2, P3, P4, P5+P6, P7, P8, P10, P16, P18, P20, P24 | open | no lead found this pass; each is a short, isolated numeral cipher with no reconstructed key and no obvious shared system |

## 6. Files

- `index.tsv` -- one row per P-item (identifier, window, header fields, counts, keyed flag).
- `P2/` .. `P24/ciphertext.txt` -- the extraction, reproducible via `python3 tools/thurloe_extract.py`
  against the same cached djvu text (gitignored, refetch with `tools/ia_numeral_runs.py`).
- `key_blake.tsv`, `key_montagu.tsv`, `key_downing.tsv` -- Tomokiyo's published partial values,
  transcribed with a `source` column for every row.
- `decode.py`, `reading_P9.txt`, `reading_P11-13.txt`, `reading_P14.txt`, `reading_P15.txt`,
  `reading_P17.txt` -- the mechanical per-token decode (rule 7; `--check` verifies).

## 7. Requests

archive.org: 4 (`_djvu.txt` fetches for vols 2/3/5/7, none cached in this fresh container,
1.5s apart via `tools/ia_numeral_runs.py`). No other host touched this pass (thurloe.htm was
read from the existing local mirror, `sources/cryptiana/web/thurloe.htm`; no re-clone of either
solver repository). No subagents, no logins, no credentials.

## 8. Monck pool solver (24 Sept 2026)

Brief: attack the "Monck pool" (P19, P22, P23 as General Monck to Thurloe, P21 as Richard
Cromwell's speech; 1,610 raw groups) with a matched control and an anneal. **Stopped before any
cryptanalysis, because the premise was wrong in two ways.** No control and no anneal were run, no
`key_monck.tsv` was written, and no reading is claimed.

**1. The four items are not Monck letters or a speech.** All four are letters from **Lord
Fauconberg to Henry Cromwell** (lord deputy, later lord lieutenant, of Ireland), in vol. 7 of the
1742 print. In the cached djvu text of `collectionofstat07thur`, each window comes straight after the
heading "Lord Fauconberg to H. Cromwell, lord deputy [lieutenant] of Ireland" (djvu lines 35655,
41199, 42243, 49474). The "General Monck" attribution came from "George Monck." at djvu lines
41196 and 42241, which is the signature on the *preceding* letter. P21's "Richard Cromwell's
speech" came from reading the clear text. Dates from the print: P22 is subscribed "Oaob.26.
[1658.] B." (djvu 42314); P23 speaks of "Our solemnity ... well over ... as this day" (the
Protector's funeral, 23 Nov 1658), djvu 49610; P19 falls among September 1658 letters; P21 is
October 1658. Its dateline was not located in the window. The group values are consistent
across the four texts (next point), so they are one system. `sources/ia-fulltext/thurloe-check.tsv`,
`index.tsv` and the four `ciphertext.txt` headers are corrected. The cipher lines themselves are
untouched.

**2. The print already carries the decipherment.** Birch set the contemporary decipherment
letter-spaced on the line next to each numeral line. In P22 and P23 it comes before the cipher line,
and in P19 it straddles the line. Example, P22 djvu 42258-42260: "The councel doe just nothing," over
`39 16 11 7 28 38 29 9 11 23 6 28 11 21 38 34 41 27 26 41 16 21 29 15`, which is 24 groups for 24
letters: t h e c o u n c e l d o e j u s t n o t h i n g. `check_interlinear.py` measures this
from the extraction files alone. Cipher lines with a neighbouring clear line within +-3 letters of
their group count: P19 2/2, P22 13/17, P23 12/24, P21 14/29. The rest are OCR line-break
misalignments. Pairing letters with groups on the exact-length lines gives one consistent
substitution across all four texts: 11=e (16 of 22 votes), 13=e, 23=l (6/6), 27=n (5/5), 6=d
(4/4), 26=o (6/10), 39=t, 41=t, 16=h (`interlinear_check.tsv`). 11 and 13 as E match
Tomokiyo's statement.

**3. Tomokiyo has this cipher.** `sources/cryptiana/web/thurloe.htm`, section "Henry Cromwell
(1658-1659)": "From 1658 to 1659, he received letters in cipher from Lord Fauconberg ... a
numerical cipher as follows (E=11/13)". His table is the image `fauconberg.jpg`, which is not in
our local mirror, so the table was not compared value by value. He also gives single-capital name
codes: A = Henry Cromwell, O = Lambert, V = Desbrowe, Z = Protector. The capitals seen in these
lines match: "V." sits where the clear line reads "Desb.", "Z." sits over "made a speech", and
"A." appears in P21/P23. `unsolved.htm` does not list these letters. Neither solver repository was
re-cloned for this pass. Both are cited from the 02:12 leaf-check.

**Grades.** Nothing was decoded, so there are no per-token grades. A reading of these letters is the
printed decipherment of 1742. A key built from it would be grade C (known plaintext) throughout.
Tomokiyo's table would be H.

**Matched control (rule 3):** not run. A control is only needed to support a cryptanalytic result,
and none is claimed or needed here.

**Still unread:** nothing in these four texts, beyond OCR damage to the interlinear lines, which
the page images would settle.

**Follow-ups (suggestions only, not done):** (a) `check_interlinear.py` also finds clear lines
matching the group count in P17 (Downing, 36/46), P24 (Maynard, 12/15), P8 (Steele, 12/15), P16
and P18. Those rows may also be printed with their decipherment, so the leaf-check's "unkeyed"
list should be re-examined row by row against the page images before any other thurloe-printed
row goes to a solver. (b) Every other row's sender should be checked against the heading
*above* its window, not the signature before it. (c) Fetch Tomokiyo's `fauconberg.jpg` (one
request) if anyone wants the key as a TSV.

Requests this pass: archive.org 1 (the `collectionofstat07thur_djvu.txt` refetch; gitignored). No
other host, no subagents, no logins.

## 9. P11-13 solver (24 Sept 2026)

(Verifier, 24 Sept 2026: class N0, see AUDIT.md. The plaintext below is Birch's printed
decipherment of 1742, re-aligned to the groups; it is not an independent reading.)

**What was found.** The 1742 print (IA `collectionofstat05thur`, pp. 67-69, djvu lines 5700-6075)
sets a decipherment above every cipher line of this letter, letter by letter and word by word;
the `[PLAIN:...]` lines in `P11-13/ciphertext.txt` are that decipherment, not surrounding clear
text. The letter is a journal-letter: first entry "Aprill 20th" (the date in `index.tsv`), later
entries 8, 13-17, 20 and 22 May, endorsed by Thurloe "General Montagu, of the 29th of May 1656",
"Received by captain Lloyd, who arrived here 11th July 1656". It has 89 cipher lines (1,835 OCR
tokens); P11, P12 and P13 are 15 of them (319 tokens). A cipher line at L5958 (13 tokens, "May
20th." entry) was classed as plain by `thurloe_extract.py` and is not in the 319; it is in the
pairs file.

**Method.** `tools/interlinear_align.py` (new, reusable for any Birch interlinear) extracts all
89 plain/cipher pairs verbatim into `montagu_1656-05-29_pairs.tsv` and aligns each group to a
chunk of the printed decipherment by dynamic programming, iterating so each group agrees with its
own reading elsewhere in the letter (long-s f = s and u = v folded). `decode.py` runs it in memory
and writes `key_montagu_extended.tsv` (248 values: 8 H, 137 C, 103 M), `align_montagu.tsv` and
`reading_P11-13.txt`; `python3 decode.py --check` exits non-zero if any is stale (rule 7).
No cryptanalysis was needed or run: every meaning comes from the printed decipherment or from
Tomokiyo, so there are no S grades, and the brief's anneal over unknown groups was not run.

**Matched control (rule 3).** `control_interlinear.py`: synthetic nomenclator with the letter's
own structure (1-99 letters, e 8 homophones, t/o/r/u/s 5, ... ; 169 alphabetical word codes on
100-622; codes about 39% of groups), enciphering clear 1656 prose from the same volume
(`control_clear_vol5.txt`, Hague letters, djvu 6076-6400), 89 lines, 1,641 tokens, printed with
the OCR faults of the real pairs (long s as f, l as 1, letters and words run together, 4% mangled
groups, merges, nulls). Result (`control_result.tsv`, `--check` supported):

| | control | target (whole letter) | target P11-13 |
|---|---|---|---|
| tokens | 1,641 | 1,835 | 319 (309 cipher groups) |
| agrees (graded C) | 1,461, 100.0% correct | 1,438 | 228 C + 36 H |
| single occurrence, both OCR boundaries (M) | 50, 80.0% correct | 89 | inside M |
| conflict with same group elsewhere (M) | 55, 7.3% correct | 93 | inside M |
| doubtful repaired (I) | 44, 100.0% correct | 15 | 2 |
| key values right | 182/198, 91.9% | 248 values | |

**Grades, P11-13 (319 tokens):** H 36 (Tomokiyo: e 18/42/56/93, the 407, and 105), C 228, I 2
(`s5`->55 a, `4-35`->435 us), M 32, U 11; 10 tokens are not cipher groups (parenthesised
numerals printed in clear, e.g. "(16)" sail, "(27)" sail, and a stray "(227"). Before: H 36 /
M 27 / U 256.

**Plain sense (as printed, spelling kept).**
1. 20 April, before Cadiz: the Spanish ships in the Carraca are about [28] sail, no topmast up nor
   rigged, ships in the harbour mouth ready to sink, new platforms, guns and chains, as if to oppose
   an attempt; the merchants examined say the passage into the Carraca is a winding channel.
2. Letter from Thurloe's agent at Lisbon: the King of Portugal has signed the treaty, varied in
   the matter of religion; the money is in the agent's possession but not to be remitted until the
   Protector's acceptance is obtained; he has given his word to write to the Protector for consent
   to letters giving assurance not to oppose any of the king's fleets.
3. 20 May: under sail for Lisbon with the better ships, the rear-admiral left with [16] sail of
   frigates before Cadiz; the Phenix sent ahead to bring the agent aboard "to consult how to manage
   our business"; about [27] sail with fire ships and victuallers; hoping to meet Thurloe's
   commands on the way.

**Distinctive phrases for the verifier:** "the passage into the Carracaes is a winding channell";
"until the protector's acceptance was obteyned"; "to obteyne letters for us to give assurance not
to oppose any of his fleets"; "the Phenix before to Lisbon to get the agent on board us"; "God
guide us for the best"; "fire ships and victuallers included". Identifiers: Birch, Thurloe State
Papers vol. 5 (1742) pp. 67-69, MS vol. xxxviii.

**Where it was not found / not read.** Groups still unread or unconfirmed in P11-13 (M/U, see
`reading_P11-13.txt`): L5730 `^9?`, `193*11?` (examined), `3°6?` (march, printed "march ants" =
merchants); L5733 437 456 439 244 442, where the print's "make the work very hard and besides"
does not align one-to-one; L5736 `7218`, `*8.5?`; L5870 437 (until/make), `358,39.?`; L5874 239,
375 (fixt/past), 415; L5877 358; L5880 402; L5962 `234,253?`, 14, 610, `211,25?`; L5965 `6407`, 13;
L5967 156 308 129 228 (one occurrence each); L5971 62, 210; L5975 317; L5978 `136407?`,
`24458?`, `404431?` (merged groups), 25; L5981 54, 59. The printed decipherment is the
contemporary one as Birch printed it; where it and the key disagree (e.g. 437) this pass records
the disagreement and does not choose. This pass did not search any other edition or catalogue
and made no novelty judgement.

**Suggestions (not done):** (a) the other keyed letters (P9, P14, P15, P17) and several unkeyed
rows show the same interlinear layout and can go through `tools/interlinear_align.py` unchanged;
(b) a blind run of `tools/nomenclator_anneal.py` on this letter, scored against the printed
decipherment, would be a real-data benchmark for the solver.
(c) Verifier suggestion, 24 Sept 2026 (AUDIT.md): grade the five `°`-repaired groups (`4°4?`,
`5°?` x2, `9°?`, `4°°?`) I rather than C in `decode.py`, giving P11-13 H 36 / C 223 / I 7 / M 32 /
U 11; (d) BL Add MS 4200 f.76 (Montagu, 19 May 1656, DECODE 8387, per Tomokiyo) may be a manuscript
of part of this journal-letter -- worth a comparison if the image is ever fetched.

## 13. P2, P3, P8 (LANE T worker D, 24 Sept 2026)

Brief: confirm heading/signature/page/extent for P2, P3, P8; say whether the print carries a
decipherment; for P8 only, align it and build a key (rule 7); otherwise write `<row>/tokens.tsv`.
No cryptanalysis. All three rows' `index.tsv` attributions turn out wrong (heading-above-window
scan, not signature-of-preceding-letter, per the Monck-pool solver's method above), and all three
have far more cipher text than their committed `ciphertext.txt` window captures. `sources/ia-fulltext/*_djvu.txt`
restored from the committed gzip cache (`thurloe-gz/`) for this pass; no archive.org fetch.

**Attribution table (djvu = `sources/ia-fulltext/<identifier>_djvu.txt` line numbers):**

| Row | index.tsv said | Corrected | Evidence |
|---|---|---|---|
| P2 | Gen. Fleetwood \| Thurloe \| p.368 | **Stouppe** to **the prince of Tarante** \| London/Londres, 25 Aug. 1654 \| p.565-566 | heading "Stouppe to the prince tf'Tarante." djvu 46954, "My Lord," 46955, dateline both languages (46-47026, 47059); Fleetwood's own letter is a separate, earlier item ending djvu 46910 |
| P3 | Mr. Bradshaw (Hamburgh) \| Thurloe \| p.402 | **John Butler**, informant in Holland \| c.22 Sept 1656 \| p.575-577 | heading is the generic "A letter of intelligence." (djvu 47926, no named correspondent); signed "John Butler." djvu 47998; Bradshaw's own letters are elsewhere (row P7) |
| P8 | Ld. chief baron Steele \| Thurloe \| p.289 | **General Blake** to **the Protector** \| 12 June 1655, aboard the George \| p.541 | Steele's letter (djvu 45193-45222, signed "William Steele.", p.289 is its own MS-volume marginal note) ends before P8's cipher starts; the heading immediately above the cipher (djvu 45229, printed-page running head "541" at djvu 45227) is "General Blake to the protector.", signed "Rob. Blake." djvu 45307 |

`printed_page` in `index.tsv` looks like it was taken from the "Vol. xvii/xxiv/xxvii p.NNN"
marginal notes next to each letter (Thurloe's own manuscript-volume pagination), not from Birch's
1742 running headers (which give the print page directly, e.g. "541", "565", "576"). This is a
plausible systematic bug affecting every row in `index.tsv`, not just these three -- flagged, not
checked further (out of this brief's three rows).

**Full extent (all three rows' cipher runs well past their committed `ciphertext.txt` window):**

| Row | Committed window | Actual extent (djvu) | Raw numeral tokens (extent) vs committed |
|---|---|---|---|
| P2 | 46981-46993 (2 lines, 39 tokens) | 46965-47024 | 267 tokens / 29 lines (`P2/tokens.tsv`) |
| P3 | 47994-48006 (3 lines, 57 tokens) -- the tail postscript only | 47926-48004 | 297 tokens / 23 lines (`P3/tokens.tsv`) |
| P8 | 45228-45278 (15 lines, 316 tokens) | 45229-45309 | 526 tokens / 35 lines (`P8/tokens.tsv`); 513 cipher groups per `decode_steele.py` |

`<row>/tokens.tsv` (order, djvu line, raw, cleaned, doubtful flag, clear words either side) covers
the corrected full extent for all three, not just the old window; `ciphertext.txt` itself is
untouched (out of scope for this brief).

### P2 -- Stouppe to the prince of Tarante

**Decipherment: yes, inline (whole-passage translation, not letter-by-letter).** The letter is
French with a diplomatic nomenclature (numbers mostly under 100) embedded for names/sensitive
nouns in otherwise-plain French prose (djvu 46965-47024, spanning the 565/566 page break). Right
after it and the French dateline ("Londres, 25. Aug. 1654"), the print sets off "Deciphered
thus:" (OCR "Tiecyphered thus:", djvu 47028) followed by a continuous **English** rendering of the
whole passage (djvu 47030-47059), closing with the same date restated in English ("London, 25;
Aug. 1654."). This is a section-level translation, not a group-for-group interlinear key like
Fauconberg/Montagu/P8 below -- the English prose does not visibly line up one cipher group to one
word. No attempt was made to align specific numeral codes to specific English words (would need
careful bilingual alignment; out of this brief's scope, restricted to P8).

Searched `sources/cryptiana/web/thurloe.htm` for "Stouppe" and "Tarante"/"Tarente": no hit. No
other row in `index.tsv` shares this correspondent or system.

**Verdict: inline printed decipherment (translation) present; not aligned; no key.** Materially
stronger than "open, no lead" (this row's prior classification in section 5 above) -- the print
already supplies English content for the whole enciphered passage.

### P3 -- John Butler, informant in Holland

**This is Tomokiyo's own "John Butler (1656)" cipher**, confirmed this pass by reading
`sources/cryptiana/web/thurloe.htm` in full: "John Butler, an informant in Holland, used a
cipher, which seems to have randomly assigned numbers 1-60 and generally alphabetically assigned
numbers 400-424 to represent single letters, in a letter of 22 September 1656 (cf. deciphered
text and ciphertext (Page 575) in Thurloe State Papers). It had some codes for names such as
62(Spain) and 156(Charles). Other numbers such as 913, 350, etc. may be nulls. (E=3/5/405)."
Tomokiyo's cited page (575) matches this row's corrected printed page exactly, and he cites a
**"deciphered text"** alongside the ciphertext at that page -- unlike Blake/Montagu/Downing in
section 2 above (systems reconstructed from *other* letters), Tomokiyo already has, or has seen,
a decipherment of this *specific* letter. The two named code values check out directly against
the extracted text: "62" and "156" appear together exactly where the clear text reads "Spayne
Ch. St." (djvu 47970, "are ufed by 62 542 and 156, to..." -- 62=Spain, 156=Charles [Stuart]); the
two proposed nulls (913, 350) both appear in the passage (djvu 47931, 47978/47986).

**Decipherment: very likely yes, interlinear, for the main body (djvu 47929-47992).** Each
cipher-bearing line there is immediately preceded by a short line of otherwise-unexplained clear
English words. Letter-count vs group-count (`check_interlinear.py`'s own method, applied by hand
since no committed `ciphertext.txt` window covers this range): "arrived Rotterdam" (16 letters)
against 16 groups in the next cipher line (djvu 47932/47934) -- **exact match**; "wind contrary"
(12) against 14 groups (47929/47931); "eighteenth September" (19) against 16 groups (47936/47938);
"Strong endeavourings" (19) against 20 groups (47959/47961) -- all within the tolerance
`check_interlinear.py` uses for the Fauconberg letters. Not verified against the page image, not
aligned, no key or reading built this pass (P8 only was authorised for that work). The tail
postscript (48000-48004, after the "John Butler." signature) is a different, sparser style --
codes embedded directly in otherwise-clear running prose, closer to P2's style -- with no obvious
adjacent decipherment line.

No formal dateline for the letter was found in the clear text extracted this pass (heading,
"Sir,", and signature only, no "London, [date]" line); the internal narrative mentions "eighteenth
September ... old ftyle" and "the twentyeth-one of the month" (djvu 47936-47946), consistent with
Tomokiyo's "22 September 1656".

**Verdict: the highest-value follow-up of these three rows.** Tomokiyo already names E and two
code values for this exact letter (not a cross-letter reconstruction), and the letter's own body
looks interlinear by letter-count. A dedicated worker building `key_butler.tsv` from Tomokiyo's
stated values and running `tools/interlinear_align.py` on djvu 47926-48004 (the method this pass
used for P8, below) would very likely recover most of the letter in one pass. Flagged in `ROOM.md`
for LANE T; not attempted here (out of this brief's scope).

### P8 -- General Blake to the Protector, 12 June 1655

**This is Tomokiyo's own first-named Blake letter.** Section 2 above already records: "Tomokiyo's
'General Blake (1655)' section names two Blake-to-Cromwell letters by date/page -- 12 June 1655,
p.541 ('almost entirely in cipher') and 4 July 1655, p.611 ('only enciphered his reference to the
Plate Fleet')." P8's corrected date (12 June 1655, signed "Rob. Blake.", "George" is presumably
his flagship) and printed page (541) match the first citation exactly; the second is the
already-known P9 row. P8's density (cipher on nearly every line of the body) matches "almost
entirely in cipher".

**Decipherment: yes, confirmed.** The print sets a letter-by-letter English decipherment directly
over/under nearly every cipher line, the same technique as the Fauconberg letters and the Montagu
journal-letter (sections 8-9 above). `tools/interlinear_align.py pairs` recovers 25 verbatim
plain/cipher pairs across the corrected full extent (djvu 45229-45309) into `P8_pairs.tsv`.

**Built (rule 7: `python3 decode_steele.py` regenerates both; `--check` exits 0):**
`key_steele.tsv` (62 values) and `reading_P8.txt` (539 tokens). "Steele" is kept in both filenames
only for continuity with the brief that named them; the letter is Blake's, not Steele's (see the
attribution table above). Grading follows the P11-13 convention (section 9): H = Tomokiyo's
`key_blake.tsv` (reconstructed from *other* Blake/Hague letters), C = the print's own interlinear
decipherment agreeing at >=2 places in this letter, I = an OCR-doubtful token repaired to a value
the alignment supports elsewhere, M = aligned once only or in conflict, U = unread, "-" = not a
cipher group (a clear word printed inline, e.g. "The", "A.  D.").

| H | C | I | M | U | not-cipher | total tokens | cipher groups |
|---|---|---|---|---|---|---|---|
| 176 | 270 | 10 | 25 | 32 | 26 | 539 | 513 |

446 of 513 cipher groups (87%) now read at H or C. Every one of Tomokiyo's worked-example letters
for this system (26=g, 33=o, 39=u, 36=r, 31=m, 32=n, 38=t, from "26 33 39 24 36 31 24 32 38" =
"gouerment") agrees with the print's own independent alignment here -- a strong cross-check in
both directions, not just an application of the key. No matched control (rule 3 is for
cryptanalytic claims; every H/C value here comes from Tomokiyo's published key or the print's own
decipherment, i.e. known plaintext, the same basis as sections 8-9 above).

**Rough continuous sense** (assembling the H/C-graded `reading_P8.txt` in djvu-line order,
spelling as printed; not checked against the page image, not a claimed transcription): the letter
reports the Spanish silver-fleet galleons at Cadiz, expected in about a month or five weeks;
Blake's own position off a cape ("Cape Maries"/"Cape Sprat", OCR-uncertain); intent to range with
the wind and keep informed; the Spanish "very distrustful", with four galleons designed for the
Mediterranean and six for New Spain; closing asking the Protector to rest assured of Blake's
diligence. Consistent with Blake's 1655 Cadiz blockade and with Tomokiyo's one-line description.
Per rule 10, this is not compared against any edition or checked for prior print this pass.

**Resemblance:** same system and worked example as `key_blake.tsv` (already in this project, used
for the unrelated P9 letter, 4 July 1655); not close to any other unkeyed row.

### Proposed `index.tsv` correction (LANE T applies; not edited here)

```
row	identifier	window_lines	printed_page	sender	recipient	date	cipher_system	n_cipher_lines	n_numeral_tokens_raw	keyed
P2	collectionofstat02thur	46954-47059	565-566	Stouppe	the prince of Tarante	London/Londres, 25 Aug. 1654	French diplomatic nomenclature (<100); print gives an inline English translation "Deciphered thus:", not a letter-by-letter key	29	267	no
P3	collectionofstat02thur	47926-48004	575-577	John Butler, informant in Holland	secretary Thurloe (implicit; "Sir,")	c.22 Sept 1656 (Tomokiyo; internal dates 18th/21st Sept O.S.)	Tomokiyo's "John Butler (1656)" cipher, E=3/5/405, letters 1-60 + 400-424 alphabetic, codes incl. 62=Spain 156=Charles, nulls 913/350; print's body looks interlinear by letter-count, not yet aligned	23	297	partial (Tomokiyo has E + 2 code values; not yet applied)
P8	collectionofstat03thur	45229-45309	541	General Blake	the Protector [Cromwell]	12 June 1655, aboard the George	Blake's cipher per key_blake.tsv (E=24/54/[82]), same system as P9 (4 July 1655); print carries its own interlinear decipherment, aligned this pass	35	526 (513 cipher groups per decode_steele.py)	yes (key_steele.tsv: H from key_blake.tsv, C from the print)
```

Files this pass: `P2/tokens.tsv`, `P3/tokens.tsv`, `P8/tokens.tsv`, `P8_pairs.tsv`,
`key_steele.tsv`, `decode_steele.py`, `reading_P8.txt`. `ciphertext.txt`, `index.tsv` and every
other row untouched. Requests: archive.org 0 (djvu text restored from the committed
`sources/ia-fulltext/thurloe-gz/` cache, per this brief); no other host; no subagents; no logins.
