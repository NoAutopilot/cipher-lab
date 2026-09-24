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

## 10. Fauconberg pool (LANE T worker A, 24 Sept 2026)

Brief: confirm sender/recipient/dateline and full cipher extent for P16-P24 (nine rows) against
the heading scan (LANE T orchestrator, ROOM.md 03:03 UTC), align each letter's printed
decipherment with `tools/interlinear_align.py`, and build one combined key. No cryptanalysis, no
anneal (LANE T worker F runs the real-data benchmark separately, section 15).

**1. Attribution, confirmed directly from the print.** All nine rows are Lord Fauconberg to
Henry Cromwell, lord deputy (later lord lieutenant) of Ireland -- read from `sources/ia-fulltext/
collectionofstat07thur_djvu.txt` (restored from the committed gzip, no network fetch this pass).
Five of the nine correct a wrong attribution in `index.tsv` inherited from the previous
detector/leaf-check pass (which read the signature or a nearby name, not the heading above the
window); the other four (P19, P21-23) were already corrected by the Monck-pool solver (section 8).

| Row | index.tsv had | Corrected sender/recipient | Date (from the print) | Full letter, djvu lines | Detector window |
|---|---|---|---|---|---|
| P16 | Capt. Stoakes / secretary Thurloe | Lord Fauconberg / H. Cromwell, lord deputy of Ireland | Whitehall, 20 April [1658] | 7179-7251 | 7198-7210 |
| P17 | Mr. Downing / secretary Thurloe | Lord Fauconberg / H. Cromwell, lord deputy of Ireland | A.D.1658, no closer date printed (content: Cromwell "in great daunger" of dying -- placed here among late-Aug/early-Sept 1658 letters, i.e. shortly before or after the Protector's death 3 Sept 1658) | 32122-32356 | 32138-32355 |
| P18 | Dr. Tho. Harrison / secretary Thurloe | Lord Fauconberg / H. Cromwell, lord deputy of Ireland | Whitehall, 14 Sept [1658] | 34074-34114 | 34083-34111 |
| P19 | (already Fauconberg, section 8) | -- | dateline reads "Sept. 21. 28." in the OCR -- the "28" is not understood (not a day-of-month; possibly a running item number or OCR noise); placed among Sept 1658 letters | 35655-35800 | 35658-35670 |
| P20 | Mr. S. Disbrowe, one of the council of Scotland / secretary Thurloe | Lord Fauconberg / H. Cromwell, lord deputy of Ireland | October the 12. [1658.], signed "B." | 39860-39962 | 39931-39943 |
| P21 | (already Fauconberg, section 8) | -- | October 1658; exact day not found in this window | 41199-41367 | 41232-41354 |
| P22 | (already Fauconberg, section 8) | -- | "Oaob.26. [1658.]" (26 October 1658), signed "B." | 42243-42324 | 42242-42307 |
| P23 | (already Fauconberg, section 8) | -- | c. 23 Nov 1658 (mentions the Protector's funeral solemnity "this day") | 49474-49660 | 49509-49608 |
| P24 | Consul Maynard / secretary Thurloe | Lord Fauconberg / H. Cromwell, lord LIEUTENANT of Ireland (title changed by this date) | "Feb. 75. 1658." -- OCR misreads "25" as "75" (no 75th of February); read as 25 Feb 1658 O.S. = 1659 N.S., signed "B." | 56496-56615 | 56521-56593 |

The window column is `index.tsv`'s existing narrow detector window (padded around the numeral
cluster the 23 Sept detector found); the "full letter" column is this pass's reading of the whole
letter, heading to the next document's own heading -- several of the windows cut a letter off
mid-cipher (P17's window alone was 217 lines short of the letter's true 234-line extent; P16's,
P18's, P20's and P24's detector windows also start partway into an already-running cipher
passage, since Birch's decipherment is set in the same paragraph as the surrounding clear text and
the detector's numeral-density threshold only catches the densest lines). `P16`-B. (`Fauconberg,`)
is the only one of the nine with a clean, unambiguous signature-and-postscript ending in the
extract; P20/P22/P24 are all signed "B." (Belasyse, Fauconberg's family name), matching the
Monck-pool solver's reading of P22's "B." (section 8).

Not checked or corrected this pass: `sources/ia-fulltext/thurloe-check.tsv` and `status.json`
(out of scope for this brief; LANE T applies index.tsv corrections, listed below, from here).

**2. Method.** `tools/interlinear_align.py` (built for Montagu, NOTES section 9, used unchanged)
extracts every (plain line, cipher line) pair over each letter's full extent above into
`fauconberg_<date>_<row>_pairs.tsv`, then aligns each pair by dynamic programming, iterating so a
value's chunk agrees with what the same value reads elsewhere **within that one letter**.
`decode_fauconberg.py` (new; does not touch `decode.py`, which another worker owns) then combines
all nine letters' per-value vote counts into one pool-wide vote per value and writes
`key_fauconberg.tsv`: grade H only for values 11 and 13 (Tomokiyo, thurloe.htm, "Henry Cromwell
(1658-1659)": "a numerical cipher ... (E=11/13)" -- kept at "e" regardless of a given letter's own
noisier vote); grade C where the pool-wide top meaning holds a majority of all votes for that
value (>=2 votes, more than half); grade M otherwise (single occurrence or no majority). Tomokiyo's
four single-capital name codes (A = Henry Cromwell, O = Lambert, V = Desbrowe, Z = Protector) are
not enciphered -- Birch prints them as literal capitals inside the cipher line -- so they are
counted separately by a plain regex over the pairs files, not voted on, and listed at H.
`python3 decode_fauconberg.py --check` regenerates every pairs/key/reading file in memory and
exits non-zero if a committed one is stale (rule 7); confirmed clean immediately after generation.

**3. What the combined key shows.** 55 numeral values (2-56, plus five outliers above 100 that are
almost certainly OCR-merged multi-word chunks, not real high-value codes -- e.g. `723` aligned to
"refentanoutwar", a merged run of "resented an outward") plus the four name codes. Values 2-49
resolve cleanly onto the 24-letter alphabet Birch's compositor had (i/j and u/v not distinguished),
with a visible **two-homophones-per-letter structure that falls straight out of the print's own
decipherment** (not cryptanalysis; reported because the pool-wide vote surfaces it): b=2/4, a=3/5,
d=6/8(/56), c=7/9, f=10/12(/36), e=11/13, h=14/16, g=15/17(/139), k=18/20, i=19/21, m=22/24, l=23/25,
o=26/28, n=27/29(/129), q=30/32, p=31/33, s=34(alone), r=35/37, u=38/40, t=39/41, x=42/44, w=43/45,
y=47/49; z has no confirmed value in these nine letters. 11 and 13 both landing on "e" (Tomokiyo's
own statement) independently in 8 of the 9 letters (P16 9/9, P17 120/124, P18 12/12, P19 52/55 and
50/51, P22 30/32 and 17/19, P24 33/33 and 27/30) is a strong internal check on the alignment method
itself, not a new claim about the cipher.

**4. Grade counts per letter** (H/C/M/U/I per CLAUDE.md rule 4; `clear` = not a cipher group --
parenthesised numerals or plain-text words interleaved with the cipher, not counted in any grade):

| Row | H | C | M | U | I | clear | total tokens |
|---|---|---|---|---|---|---|---|
| P16 | 9 | 130 | 6 | 2 | 0 | 15 | 162 |
| P17 | 124 | 809 | 102 | 134 | 5 | 81 | 1255 |
| P18 | 12 | 89 | 7 | 17 | 1 | 15 | 141 |
| P19 | 106 | 568 | 70 | 12 | 7 | 24 | 787 |
| P20 | 34 | 104 | 171 | 68 | 1 | 30 | 408 |
| P21 | 87 | 151 | 416 | 108 | 0 | 41 | 803 |
| P22 | 51 | 260 | 41 | 15 | 2 | 16 | 385 |
| P23 | 77 | 132 | 406 | 89 | 0 | 29 | 733 |
| P24 | 63 | 334 | 66 | 48 | 6 | 52 | 569 |
| **total** | **563** | **2577** | **1285** | **493** | **22** | **303** | **5243** |

H+C = 3140 of 4940 cipher-group tokens (63.5%) read with the print's own decipherment agreeing at
least twice pool-wide. **P20, P21 and P23 are the three where the print leaves the most
unaligned** -- M exceeds C in all three (visible already in the interlinear pairs as heavier OCR
damage: merged words with no spaces, long-s/f confusion, and several digit runs the aligner could
not chunk against any recurring plain-text span). P17, P19, P22, P24 align well (C well ahead of M,
few U). P16 and P18 are short (7 pairs each) but very clean. No group in any of the nine is claimed
as newly read beyond what `key_fauconberg.tsv`/the per-letter `reading_fauconberg_*.txt` show; the
M/U tokens are exactly the extent to which Birch's own decipherment does not settle a group.

**5. Flags for LANE T.**
- **`decode.py` and `key_downing.tsv`/`reading_P17.txt` are now wrong for P17.** `decode.py`
  (owned by another worker, not touched here) still treats P17 as George Downing's letter with
  Downing's cipher (E=39-45, THE=468) applied to the old, short detector window. P17 is this
  Fauconberg letter; its real cipher is the one in `key_fauconberg.tsv`, and its real extent is
  32122-32356, not window 32138-32355 alone. Whoever owns `decode.py` should drop P17 from its
  `LETTERS` table (or repoint it at `key_fauconberg.tsv`) and `index.tsv`/`thurloe-check.tsv`'s
  `P17` row needs the same correction as the block below. Tomokiyo's Downing cipher may still be a
  real, separate reconstruction -- it is just not what is printed at djvu lines 32122-32356.
- **More Fauconberg-to-H.-Cromwell letters exist in vol. 7 beyond this pool's nine rows.** A plain
  grep for "Fauconb" against the cached djvu text finds "Lord Fauconberg to H. Cromwell" (or "to
  fecretary Thurloe", or the reverse direction) headings at djvu lines 3582, 7179, 12754, 13222,
  13868, 15589, 16845, 18891, 29597, 32122, 33205, 33323, 34074, 35655, 39860, 41199, 42243, 46115,
  46696, 49474, 56496, 58011, 59400 -- at least a dozen more than the nine P-rows this brief covers
  (some to secretary Thurloe rather than H. Cromwell directly, and some are H. Cromwell's replies,
  which would not be in cipher). Not checked for cipher content or windows this pass (out of
  brief); a next pass could grep each for a nearby numeral-dense line the 23 Sept detector missed
  because the letter's opening or closing paragraphs (not just its middle) were outside every
  P-row's original window.
- **Tomokiyo's key image (`fauconberg.jpg`) is not in the local mirror and was not fetched this
  pass** (brief's instruction); the next step for anyone continuing this is a value-by-value
  comparison against `key_fauconberg.tsv` once it is retrieved -- one request to
  `cryptiana.web.fc2.com`, well within the good-citizen rule's per-host budget.
- The proposed `index.tsv` corrections (sender/recipient/date/cipher_system/keyed only; window
  widening is a separate judgement call for whoever owns re-extraction with `tools/thurloe_extract.py`,
  since widening changes `ciphertext.txt` and downstream row counts this brief does not touch):

```
row	sender	recipient	date	cipher_system	keyed
P16	Lord Fauconberg	Henry Cromwell, lord deputy/lieutenant of Ireland	20 April [1658]	Fauconberg-H. Cromwell numeral cipher (key_fauconberg.tsv; Tomokiyo thurloe.htm 'Henry Cromwell (1658-1859)', E=11/13, key table image fauconberg.jpg); Birch prints the interlinear decipherment	yes
P17	Lord Fauconberg	Henry Cromwell, lord deputy of Ireland	A.D.1658 (no closer date printed; content places it near the Protector's death, 3 Sept 1658)	Fauconberg-H. Cromwell numeral cipher (key_fauconberg.tsv; Tomokiyo thurloe.htm 'Henry Cromwell (1658-1859)', E=11/13, key table image fauconberg.jpg); Birch prints the interlinear decipherment	yes
P18	Lord Fauconberg	Henry Cromwell, lord deputy of Ireland	Whitehall, 14 Sept [1658]	Fauconberg-H. Cromwell numeral cipher (key_fauconberg.tsv; Tomokiyo thurloe.htm 'Henry Cromwell (1658-1859)', E=11/13, key table image fauconberg.jpg); Birch prints the interlinear decipherment	yes
P19	Lord Fauconberg	Henry Cromwell, lord deputy/lieutenant of Ireland	Sept. 21. [1658] (trailing "28" in the OCR dateline unexplained)	Fauconberg-H. Cromwell numeral cipher (key_fauconberg.tsv; Tomokiyo thurloe.htm 'Henry Cromwell (1658-1859)', E=11/13, key table image fauconberg.jpg); Birch prints the interlinear decipherment	yes
P20	Lord Fauconberg	Henry Cromwell, lord deputy of Ireland	October the 12. [1658.]	Fauconberg-H. Cromwell numeral cipher (key_fauconberg.tsv; Tomokiyo thurloe.htm 'Henry Cromwell (1658-1859)', E=11/13, key table image fauconberg.jpg); Birch prints the interlinear decipherment	yes
P21	Lord Fauconberg	Henry Cromwell, lord deputy/lieutenant of Ireland	October [1658] (day not found in this window)	Fauconberg-H. Cromwell numeral cipher (key_fauconberg.tsv; Tomokiyo thurloe.htm 'Henry Cromwell (1658-1859)', E=11/13, key table image fauconberg.jpg); Birch prints the interlinear decipherment	yes
P22	Lord Fauconberg	Henry Cromwell, lord deputy/lieutenant of Ireland	26 Oct. [1658.]	Fauconberg-H. Cromwell numeral cipher (key_fauconberg.tsv; Tomokiyo thurloe.htm 'Henry Cromwell (1658-1859)', E=11/13, key table image fauconberg.jpg); Birch prints the interlinear decipherment	yes
P23	Lord Fauconberg	Henry Cromwell, lord deputy/lieutenant of Ireland	c. 23 Nov [1658]	Fauconberg-H. Cromwell numeral cipher (key_fauconberg.tsv; Tomokiyo thurloe.htm 'Henry Cromwell (1658-1859)', E=11/13, key table image fauconberg.jpg); Birch prints the interlinear decipherment	yes
P24	Lord Fauconberg	Henry Cromwell, lord LIEUTENANT of Ireland	Feb. 25. 1658 O.S. (= 1659 N.S.; OCR misprints "75")	Fauconberg-H. Cromwell numeral cipher (key_fauconberg.tsv; Tomokiyo thurloe.htm 'Henry Cromwell (1658-1859)', E=11/13, key table image fauconberg.jpg); Birch prints the interlinear decipherment	yes
```

**6. Status.** Not a cryptanalytic result -- no S grades, no control, no anneal (per brief; LANE T
worker F's real-data benchmark, section 15, is the place for that). Per rule 10: found in this
project's own reading of Birch 1742 (already in hand, no new source consulted); not searched
against any external source this pass, and no claim of new/unpublished/first is made. `status`
for all nine rows should become `found-solved` once LANE T applies the corrections above (same
class of result as P11-13 and P19/P21-23: a printed 1742 decipherment, aligned, not decoded).

**Requests this pass:** none -- the vol. 7 djvu text was already committed gzipped at
`sources/ia-fulltext/thurloe-gz/` and restored locally with `zcat`; no archive.org, no other host,
no logins, no subagents.

## 12. 1654 inline pool (LANE T worker C, 24 Sept 2026)

Brief: consolidate P4/P5/P6/P7 (the four 1654 letters that print small numerals inline in clear
English, no decipherment beside them) -- confirm attribution and full cipher extent, extract
tokens/cribs, test one-system, look for a larger pool, estimate alphabet size. No cryptanalysis
attempted, per brief and rule 10.

**Headline result: two of the four are already found-solved by the print itself.** `index.tsv`'s
own premise ("no decipherment beside them") held for P4 but not for P5/P6 or P7 -- both have a
full plaintext paragraph headed "The fame letter decypherd" printed immediately after the cipher
paragraph, in the same style Birch used for P11-13 and the Fauconberg-to-H.-Cromwell group
(sections 8-9 above). Nothing here was decoded (out of this brief's scope), but the letters
should move to `found-solved` and drop out of any cryptanalysis queue; only P4 is a genuine open
target. **Recommendation for LANE T: hand P5+P6 and P7 to a solver for the same kind of
known-plaintext alignment `tools/interlinear_align.py` did for P11-13** -- and given the
one-system evidence below, that alignment would very likely also open P4, at essentially no
extra cryptanalysis cost.

### 12.1 Attribution corrections (all three checked rows were wrong in `index.tsv`)

Checked by reading the heading immediately above each cipher paragraph in the cached djvu text
(`sources/ia-fulltext/collectionofstat03thur_djvu.txt`, restored from `thurloe-gz/`), not the
signature of the preceding letter -- the same mistake flagged for the Fauconberg rows (section 8,
LANE T orchestrator note, ROOM.md 03:08). All three corrected rows are anonymous royalist
informant letters from Calais, same correspondent throughout (signs "W.S." / "W. Stamford." /
"S."), same code language ("your friend" = the Protector, via an intermediary the letters call
"Sir"), same courier ("mr. Thomas Whit at Dover"), same subject (offering intelligence on a
royalist rising in exchange for the Protector's reward/protection, an alias "Nevell" used at
Dover) -- not Thurloe's usual correspondents Prideaux, Creed or Bradshaw at all:

| Row | `index.tsv` said | Actually (djvu evidence) |
|---|---|---|
| P4 | sender "Mr. W. Prideaux", p.56, date not read | Heading L15467 "A letter of W. S. from Calais.", signed "W.S." L15648, dated "Callais, March 13, [1654. N.S.]" L15646-48, printed p.76 (Vol. xxiv, marginal L15470-71). The real Prideaux letter (heading L15424, signed "Will. Prideaux." L15464, dated "Mosco, this 3 of March", p.56) is short, plain, and ends before the W.S. letter begins -- it has no cipher at all. |
| P5+P6 | sender "Major Creed", p.273/~275, date not read | Heading L22884 "A letter of intelligence.", signed "W. Stamford." L23054/L23138, dated "Callais, March 30, [1654. N.S.]", cipher para. marginal p.319 (L22887-88), decipherment marginal p.324 (L23068-69). "Major Creed to fecretary Thurloe" (heading L22631) is the *previous* letter and is not cited by this row's window at all. |
| P7 | sender "Mr. Bradshaw, resident at Hamburgh (2nd letter)", p.277, date "A.D. 1654 (margin)" | Heading L23230 "A letter of intelligence, [March 20, 1654.]", signed "S." L23335/L23417, cipher para. marginal p.340 (L23236), decipherment marginal p.337 (L23353). The real second Bradshaw letter (heading L23175, signed "Rich. Bradshaw," L23222, dated "March 20, 1654") ends at L23227 with no cipher; this is a separate, later letter on the same page. |

P5+P6 is still correctly one letter split into two extraction clusters (as `index.tsv` already
had it), just under the wrong sender. Recipient for all three: not stated by name in the letter
body (addressed "Sir"); Birch groups them among Thurloe's papers and the endorsement on the P4
letter (L15667-71) explicitly names Thurloe's department: "W. S. Calais... His desire of a
correspondence, and promise of performing some eminent service (in case my lord protector will
engage to reward him) namely in discovering of the plott, &c." So "secretary Thurloe" (as
`index.tsv` already has for recipient) is a reasonable inference, not itself verified from the
letter's own salutation.

### 12.2 Full cipher extent (heading to signature/postscript, hand-verified)

The old windows were padded slices of the reported `ocr_lines`, not the whole letter, and cut two
of the three items well short of their actual cipher content:

| Row | Old window (`index.tsv`) | Full letter (this pass) | Cipher paragraph | Decipherment paragraph |
|---|---|---|---|---|
| P4 | 15485-15537 (53 lines) | 15467-15648 (182 lines) | ~15485-15600 | none |
| P5+P6 | 22886-22949 + 23009-23035 (128 lines total, with a gap) | 22884-23063 (180 lines, continuous) | 22887-23059 (includes a ciphered postscript the old windows missed entirely) | 23065-23144 |
| P7 | 23235-23346 (112 lines) | 23230-23422 (193 lines) | 23235-23348 (incl. a still-ciphered postscript, L23337-46, not covered by the decipherment) | 23350-23422 |

### 12.3 tokens.tsv and cribs.tsv

`pool_1654/extract_pool.py` (reproducible: `python3 extract_pool.py` from this folder against the
restored djvu text; `--check` regenerates into a temp dir and diffs, rule 7) walks each letter's
full verified span and emits `tokens.tsv` (one row per numeral token: letter, djvu line, raw OCR,
cleaned value via the existing l/i->1, o->0 convention, doubtful flag, preceding/following clear
word, and whether its line was cipher- or plain-classified) and `cribs.tsv` (numeral tokens merged
into runs when within 3 lines of each other, with 2 lines of plain context each side).

Per the brief's point 1, inline numerals inside otherwise-PLAIN lines are included -- but a first
pass over ALL letter/digit-confusable single characters produced heavy false-positive noise: the
word "I" (150 hits) and "O" (8 hits) read as cipher digit "1"/"0" on ordinary English lines, plus
running-head marginalia ("A.D. 1654.", "Vol. xxiv. p. 76.", page-number/"STATE PAPERS OF" footers)
landing inline with body text through OCR. Fixed by only applying the letter-digit substitution
within lines the existing >=70%-numeral-token test already classifies as cipher, and by dropping
plain-line tokens that are a bare 16xx year or sit next to a volume/page/running-head marker word
(`is_marginal_noise` in `extract_pool.py`). Two known residual artifacts were left in rather than
over-fit the filter: `P5_P6` L23015 has a genuine cipher run in a cipher-classified line that ends
with the marginal note "A. D. 1654;" glued on (one stray 4-digit token), and L23013 has a lone
page number "275" next to "&c," (not caught since "&c" wasn't in the marker list). Both are
visible in `tokens.tsv` and excluded from the counts and the one-system test below.

Token totals (cipher-classified lines + qualifying plain-line numerals, after the fix): P4 387,
P5+P6 694, P7 814 -- 1,895 total, well above the old raw-token counts in `index.tsv` (184+337+
167+574=1,262) because the windows now cover the whole letter instead of a padded slice.

For P4 (no printed decipherment), `cribs.tsv`'s `expected_content` is this pass's own reading of
the surrounding plain text, graded **CANDIDATE only**, per the brief. For P5+P6 and P7,
`expected_content` points to `decipherment_P5_P6.txt` / `decipherment_P7.txt` -- the full text of
Birch's own "The fame letter decypherd" paragraph, saved verbatim (OCR, not repaired). That is
**FOUND** (Birch's print), not a candidate guess, and is not a per-run alignment: Birch's
decipherment is one continuous paragraph per letter, not interlined group-by-group the way P11-13
and the Fauconberg group are, so lining up individual cipher groups to individual plaintext words
would need the same kind of DP alignment `tools/interlinear_align.py` used for P11-13 -- not run
here (out of this brief's "no cryptanalysis" scope; it is known-plaintext alignment, not
cryptanalysis, so it belongs with a solver, not this consolidation pass).

### 12.4 One-system test (`pool_1654/analyze.py`, cipher-classified-line tokens only)

| | P4 | P5+P6 | P7 | combined |
|---|---|---|---|---|
| n (clean tokens) | 233 | 437 | 482 | 1,152 |
| distinct values | 33 | 41 | 48 | 55 |
| range | 1-158 | 1-158 | 0-171 | 0-171 |
| index of coincidence | 0.0503 | 0.0420 | 0.0410 | 0.0434 |
| 3-digit groups | 2 (0.9%) | 3 (0.7%) | 7 (1.5%) | 12 (1.0%) |
| top-5 values | 12,35,40,25,41 | 12,25,40,35,36 | 40,12,25,36,41 | 12,40,25,35,36 |

(P5+P6's one stray "1654" marginal-note token, section 12.3, is excluded from range/n above.)
Reference: uniform-55-symbol IC = 1/55 = 0.0182; English running-text letter IC ~ 0.0667.
0.041-0.050 per letter sits about 35-45% of the way from uniform to English, consistent with a
homophonic substitution over roughly 50 symbols for a 26-letter alphabet (a handful of homophones
per common letter, not one-per-letter-frequency the way Montagu's E=18/42/56/93 needed).

**Same system, strong evidence:** the top-5 most frequent values are the *same five numbers*
(12, 25, 35, 36, 40, 41 -- six numbers across three top-5 lists of five) in all three texts, just
reordered, and 30 of the 55-56 distinct values recur in all three texts (list in `analyze.py`
output). For three cipher paragraphs by the same signed correspondent, written 13/20/30 March
1654 seventeen days apart, this is exactly what one personal cipher used consistently across a
run of letters looks like -- not proof (no control was run; this is a description of the raw
statistics, not a cryptanalytic claim), but strong grounds for the recommendation in the headline
above: build the P5+P6/P7 key from the print, then try it on P4 before spending anneal budget on
P4 as an unkeyed target.

### 12.5 Alphabet size / homophone structure estimate

55 distinct clean values (excluding the one marginal-date artifact): 47 in the 1-43-ish range
(homophones for the 26-letter alphabet, ~1.8 values/letter on average if spread evenly, though
real cipher homophone counts are never even -- E-type letters get more), 8 distinct 3-digit values
(127, 130, 136, 143, 153, 158, 159, 171 -- code words/names, the brief's own examples 130/143/81
confirmed present, 81 is 2-digit here not 3). This is smaller than Montagu's (>600 elements per
Tomokiyo) or Downing's (~600) systems -- consistent with "one small homophonic alphabet plus code
words" for a single informant's personal correspondence, not a departmental cipher shared across
many letters. **Total token pool available to a solver: 1,152 clean cipher-line tokens across three texts
believed to share one system**, of which 437 (P5+P6) + 482 (P7) = 919 (80%) come from the two
letters whose plaintext is already known from the print, leaving 233 (P4, 20%) as the only part
still requiring a blind check against the resulting key -- meaning a solver does not need to
attack this pool blind at all; it needs an alignment pass on the two found-solved letters, then a
check of the resulting key against P4.

### 12.6 Wider scan for other inline-numeral letters, vols 2-3 (`pool_1654/scan_headings.py`)

Read-only scan (same >=70%-numeral-token line test, clustered) across the full text of both
cached volumes, merging cipher-line clusters within 30 lines and reporting the nearest preceding
correspondent heading. Confirms no other letter in vol. 2 or vol. 3 matches this pool's own style
(small values 1-43 plus rare 3-digit) outside the rows already in `index.tsv` -- but surfaces a
**different, larger-alphabet style** (interlinear syllable-per-number, values into the low
thousands, e.g. "1016.", "2372.") already printed with its own interlinear decipherment, at three
headings not in `index.tsv` at all: **Mr. James Nutley to secretary Thurloe** (vol. 3, heading
djvu 31934, cipher+decipherment cluster ~32078-32098), **Attorney general Prideaux to secretary
Thurloe** (vol. 3, heading djvu 34006, cluster ~34180-34210), and **Sir Benjamin Wright to
secretary Thurloe** (vol. 2, heading djvu 55802, French-language cipher, cluster ~60096-60110,
different symbol format again -- numerals plus odd single characters, not spot-read closely).
These are a distinct system from this pool and out of this brief's scope (no cipher content read
beyond the spot-checks quoted above) -- **flagged for LANE T as three more found-solved-by-print
leads**, same shape as section 12.1's discovery, not folded into `index.tsv` or claimed as part of
"the 1654 inline pool". One more found-solved item, also out of scope (different cipher type --
letter substitution, not numeral): vol. 2 djvu L12398, "The fame decyphered by fecretary Thurloe",
under a heading this pass did not identify (context at L12380-12400 mentions "8 Mar. 1653").

### 12.7 Proposed `index.tsv` correction block (not applied -- LANE T's to apply)

```tsv
row	identifier	window_lines	printed_page	sender	recipient	date	cipher_system	n_cipher_lines	n_numeral_tokens_raw	keyed
P4	collectionofstat03thur	15467-15648	76 (Vol. xxiv)	"A letter of W. S. from Calais" (unnamed informant, signs W.S.)	secretary Thurloe (inferred, not named)	Callais, March 13, [1654. N.S.]	Stamford/W.S. pool (open)	~50 (full letter; old count was window-limited)	387 (this pass, full letter)	no
P5	collectionofstat03thur	22884-22949	319 (Vol. xxiv), cipher para	"A letter of intelligence" (W. Stamford, Calais)	secretary Thurloe (inferred)	Callais, March 30, [1654. N.S.]	Stamford/W.S. pool -- FOUND-SOLVED, decipherment printed L23065-23144	part of 694 (P5+P6 combined, full letter)	part of 694	no -> found-solved
P6	collectionofstat03thur	22950-23063	319/324 (Vol. xxiv)	as P5 (same letter, second cluster + ciphered postscript L23057-63 the old window missed)	as P5	as P5	as P5	part of 694	part of 694	no -> found-solved
P7	collectionofstat03thur	23230-23348	340 (Vol. xxiv), cipher para	"A letter of intelligence" (signed "S.", same hand as P4/P5/P6)	secretary Thurloe (inferred)	[March 20, 1654.]	Stamford/W.S. pool -- FOUND-SOLVED, decipherment printed L23350-23422	part of 814	814	no -> found-solved
```

### 12.8 Requests

None. All four djvu volumes were already cached gzipped at `sources/ia-fulltext/thurloe-gz/`
(fetched by an earlier LANE T worker, ROOM.md); this pass restored `collectionofstat02thur` and
`collectionofstat03thur` with `zcat` and read nothing else. No subagents, no logins, no
credentials. Per rule 10: nothing above is described as new, unpublished, unread, first or never
printed -- P5+P6 and P7 are found-solved *by Birch's own 1742 print*, which is the opposite of a
novelty claim, and no N-class is assigned here (a verifier's job, not this worker's).

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

## 15. Solver benchmark on Fauconberg (LANE T worker F, 24 Sept 2026)

**Answer.** On the real Fauconberg groups, both solvers read at least 80 percent of tokens on all three
seeds only at the full 3,024 groups. The anneal also managed it on all three 600-group subsets, but not
at 1,200 (one seed fails at 0.35). At 600 to 1,200 groups, two runs in three succeed. At 300 groups,
one run in three succeeds. On the synthetic control, both solvers pass on every seed from 1,200 groups.
The 1654 inline pool (P4-P7) has about 1,040 clean groups by the same filter (P4 149, P5 290, P6 135,
P7 465). That puts it in the range where a single run is unreliable but several seeds usually find the
key. Solver-ready, then, only with many seeds and a choice by score, and every reading still needs a
matched control.

**Inputs.**
- *Groups:* `benchmark/data.py`, the CLEANED cipher lines of P16-P24 only. A token that is not a clean
  integer 1-60 ends the fragment (OCR merges, name capitals).
- *Scoring key:* Birch's printed decipherment, taken from the lines check_interlinear.py matches exactly
  (35 pairs, 16 kept after an agreement filter, 29 groups). It was then extended with the +-3-letter
  neighbour lines, each placed at the offset that best agrees with that key (46 lines, 39 groups, 2,773
  of 3,024 tokens scored).
- *Agreement:* the exact key and the extended key agree on every shared group. All 39 groups also
  agree with worker A's `key_fauconberg.tsv`, which landed during this run and was not used for
  scoring. Unscored groups: 34 (s, votes split by long-s OCR as f/l), 36, 25, 1, 12 partly.
- *Language model:* Gutenberg texts (tools/data) plus English lines of Thurloe vols 2, 3, 5, with a
  long-s repair.
- *Control:* vol. 7 clear English, djvu lines 2002-2119, with the cipher windows excluded. It was
  enciphered with the same homophone sets, each group drawn at its real frequency, and cut into the
  same fragment lengths.

**Runs.**
- *Solver settings:* no crib, no fixed values, each tool at its defaults. hillclimb: 40x6000, at most
  2 homophones. anneal: 8x100000, homophone cap 4, with syllables, words and nulls off.
- *Anneal alphabet:* the anneal's model alphabet folds y/i, w/u and k/c, so it is scored on folded
  letters.
- *Seeds:* seeds 1-3 choose both the subset (contiguous fragments) and the solver seed.

Token accuracy, three seeds (all rows in `benchmark/results.tsv`):

| groups | hillclimb real | hillclimb synth | anneal real | anneal synth |
|---|---|---|---|---|
| 300 | 0.95 0.31 0.16 | 0.59 0.52 0.54 | 0.99 0.12 0.26 | 0.18 0.38 0.28 |
| 600 | 0.94 1.00 0.76 | 0.41 0.69 0.97 | 0.83 0.98 0.99 | 0.16 0.99 0.98 |
| 1,200 | 0.92 0.71 0.95 | 1.00 0.96 1.00 | 0.99 0.35 0.99 | 0.99 0.99 0.99 |
| 3,024 | 0.93 0.93 0.91 | 1.00 1.00 1.00 | 0.99 0.99 0.97 | 0.99 0.99 0.99 |

Smallest length with >= 80 percent tokens on all three seeds and at every larger length:

| | real | synthetic |
|---|---|---|
| hillclimb | 3,024 | 1,200 |
| anneal | 3,024 | 1,200 |

**Reading the table.**
- *Why the real text caps lower:* the hillclimb tops out at about 0.93 on the real text.
  `truth_score_per_tok` is above the found score in nearly every real run, so this is a search
  failure: the true key scores better and the solver does not reach it. The cause is probably OCR
  noise plus the two-homophone cap.
- *Why the real text beats the control at 300-600 groups:* the real letters repeat set phrases
  ("my lord", names), and two real subsets (300/1, 600/2) use only 22 distinct groups.
- *Anneal accuracy on distinct groups:* 0.92-0.95 at full length.
- *Picking a run by score:* a failed anneal run shows a clearly worse per-token score (about -4.0 to
  -4.6) than a successful one (-2.3 to -3.3). Choosing by score across restarts or seeds is therefore
  a usable guard.

**Tool changes:** none. Both tools ran unchanged. The anneal was given an English 5-gram model built
with `tools/italian_ngram.build()`.

**Regenerate:** `python3 benchmark/bench.py --check`.

**Requests:** none (disk only).

Report on what was found: benchmark numbers only. No reading of any letter is claimed and no novelty
class is given.
