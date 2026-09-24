# Thurloe printed cipher letters (23 items, Birch 1742, vols 2/3/5/7)

**Status: partial** for the 5 letters with a Tomokiyo-reconstructed cipher system (7 rows:
P9, P11, P12, P13, P14, P15, P17); **found-solved** for P19, P21, P22, P23 (24 Sept 2026: four
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

None of the 5 is `found-solved`: Tomokiyo's page reconstructs each correspondent's cipher
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

**None of the five outputs is continuous English, or close to it** -- H-graded tokens are
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
| P11-13 | partial | image check of BL Add MS 4166 (Montagu's original) would let a real key be built; not attempted here |
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
