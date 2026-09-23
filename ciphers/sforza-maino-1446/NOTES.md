closed-negative

(Conditional on Bourdeau's draft transcriptions: solver campaign of 23 Sept 2026, at the end of this file. The check-solved verdict of the same date, below, was open / Stage 2.)
(Image gate of 23 Sept 2026, end of this file: BnF italien 1583 is not on Gallica, so the condition stands.)

# Sforza reply to Zorzo (Giorgio) del Maino, 4 May 1446 (BnF italien 1583 f.68, DECODE R7898) and Vincenzo
# Amidani to Francesco Sforza, Milan, 4 May 1446 (BnF italien 1583 f.70, imaged inside DECODE R7899)

Two items, same shelfmark, same date, same graphic-sign cipher family:

- **f.68** (DECODE R7898): reply from the Sforza side (Francesco Sforza, then condottiere in the Marche, or
  his chancery) to what his agent Giorgio (Zorzo) del Maino had reported. 404 signs, 26 types.
- **f.70** (imaged as the second slip, image P1, inside DECODE R7899, whose primary catalogue heading is
  "f.75"): Vincenzo Amidani to Francesco Sforza, Milan, 4 May 1446. 390 signs, 31 types, a different hand,
  same sign family as f.68.

## Source

Transcriptions, sign inventories, DECODE image identifiers and the Mazzatinti inventory pointer are all
Bourdeau's work (`dbourdeau/cyphersolver`, folder `it1583/`, commit `2e9ec01`, checked 23 Sept 2026 in this
sweep; code MIT, text CC BY 4.0, cite per CLAUDE.md rule 8). [Solver, 23 Sept 2026: both are now copied, with credit, as ciphertext.txt and ciphertext_f70.txt.] At the time of the sweep no transcription was copied into this folder; a
solver session does that with attribution. Inventory identification of both items ("f. 68. Risposta a quanto
ha riferito Zorzo Maino (4 maggio). In cifre." / "f. 70. Lettera di Vincenzo Amidani a Fr. Sforza (Milano 4
maggio). In cifre.") is from Girolamo Mazzatinti's inventory of the BnF Sforza papers, *Archivio storico
lombardo* X (1883), p. 230 (OCR at `cs-recheck/it1583/asl1883.txt`, verified directly by this worker at lines
10500-10506, matching Bourdeau's citation exactly, no decipherment noted).

## Check-solved sweep (23 September 2026)

Six sources, each logged with what was searched, found or unreachable. This environment egress-blocks every
archive host (de-crypt.org, archive.org, web.archive.org, gallica.bnf.fr, catalog.hathitrust.org,
wikisource.org, Google Books); only github.com and the WebSearch tool are reachable.

1. **Web search engine.** Queries run: `"italien 1583" cifra Sforza 1446 Maino Amidani`; `"Zorzo Maino" OR
   "Giorgio del Maino" 1446 cifra Sforza`; `"Vincenzo Amidani" 1446 Sforza cifra`; `Cerioni "La diplomazia
   sforzesca" cifrari Maino Amidani`; `DECODE R7898 R7899 de-crypt.org BnF italien 1583`; plus follow-ups
   `Cipher Mysteries "Milanese enciphered letters" call for help Cerioni Sforza`; `lombardiabeniculturali
   "Vincenzo Amidani" 1446 maggio Francesco Sforza cifra`; `"Giorgio del Maino" OR "Zorzo Maino" 1446
   Francesco Sforza risposta cifra lettera`; `Voynich Ninja diplomatic ciphers Sforza Milanese enciphered
   letters thread`; `"cifrari" Sforza "1446" Cicco Simonetta Tranchedini nomenclatore Amidani studi storia
   medioevale diplomatica`. Found: general biographical pages for Giorgio del Maino and Vincenzo Amidani (both
   served the Sforza chancery; Amidani joined Sforza's service in 1437 and was in Venice for Sforza's interests
   in 1446 -- consistent with, not a reading of, the cipher), Lombardia Beni Culturali's "La memoria degli
   Sforza" letter registers (searched for a May 1446 Maino/Amidani entry; nothing found for that month --
   the registers indexed there run mostly 1450 onward), Cerioni's 1970 *La diplomazia sforzesca* cited only
   bibliographically (Cancelleria segreta keys from ASMi Sforzesco busta 1591 and 1597-1598, same busta numbers
   Bourdeau already worked from), a 2011 Cipher Mysteries post "Milanese enciphered letters, call for help..."
   (a general call to locate Sforza-era ciphers, cites Cerioni, no mention of Maino, Amidani, f.68, f.70,
   R7898 or R7899), and a paper on Nicodemo Tranchedini's cipher (a different named correspondent, not this
   pair). No search surfaced a plaintext, a transcription, or a key specific to f.68 or f.70.
2. **Print.** Cerioni, *La diplomazia sforzesca* (1970), located bibliographically (Librinlinea, SearchWorks,
   WorldCat, Google Books records) but not obtainable in this environment (no full text online; the volume's
   own key facsimiles are print-only) -- unreachable, would need the person or a library visit; recorded as a
   reopening route, not searched further. Mazzatinti 1883 (`asl1883.txt`, already on disk from Bourdeau's
   fetch): grepped directly by this worker for "maino" (line 10271 index entry, line 10502 the f.68 heading
   itself, plus five further Maino letters elsewhere in the volume), "amidani" (line 10506 the f.70 heading,
   plus six further Amidani letters "in cifre" elsewhere in the same volume -- additional related leads, not
   decipherments of these two folios), and the text around f.68/f.70 (lines 10495-10515, transcribed above) --
   confirms both headings read "In cifre" with no decipherment or edition noted anywhere in the inventory.
   Meroni and the Sforza letter editions (Carteggio degli oratori mantovani etc.) were not separately reachable
   from this environment (no online full text found by web search) and were not searched further; logged as a
   gap, not a finding.
3. **Community lists.** `grep -rn "1583\|Maino\|Amidani\|Sforza"` in `sources/cryptiana/` (this repo's local
   snapshot of Cryptiana): matches are all coincidental -- other manuscripts or people that happen to share the
   string "1583" as a year (Henry III correspondence, Mary Stuart letters, a different "Maximilian Sforza"
   cipher in BnF fr.3034, Marino Caracciolo). No match for the shelfmark "italien 1583", for Cerioni, for
   Tranchedini in the context of this pair, or for the diplomazia sforzesca title. WebSearch of Cryptiana and
   Cipherbrain directly (queries above) returned nothing on this pair either.
4. **DECODE.** de-crypt.org is fully egress-blocked from this environment (no login attempted, per the
   playbook). Would-be URLs: `https://de-crypt.org/decrypt-web/RecordsView/7898` and
   `https://de-crypt.org/decrypt-web/RecordsView/7899`. A cached DECODE catalogue snapshot inside
   `ay/catalogue/decode-catalog.csv` (Aymeloglu's repository, scraped from DECODE, no licence, cite only) does
   reach both records: row 7898 = "Paris, BnF (BnF), italien 1583, f 68. BnF_1583_068", status
   **Non-decrypted**; row 7899 = "Paris, BnF (BnF), 1583, f 75. BnF_1583_075" (the record under which f.70's
   image is also filed), status **Non-decrypted**. Both fields for cleartext/plaintext are empty in that
   snapshot. This is the closest this sweep could get to DECODE's own status field and it agrees with
   Bourdeau's report that DECODE marks both "Non-decrypted".
5. **Bourdeau (dbourdeau/cyphersolver, it1583/, fresh clone commit 2e9ec01, 23 Sept 2026).** Read `NOTES.md`
   and `profile.json` in full. He: downloaded both DECODE images with an authenticated session cookie; found
   Mazzatinti's 1883 heading for both folios (as above); transcribed f.68 (404 signs/26 types) and, separately,
   found and transcribed f.70 inside the R7899 image (390 signs/31 types); ran homophonic simulated annealing
   (it-cinquecento model) on f.68 alone -- unconstrained, capped-homophone, and nulls-allowed variants all
   collapsed to nonsense; ran one-to-one substitution annealing, 16 restarts, all nonsense; tried a word-pattern
   match on repeated sign-groups (FpBHcdSp fits "uisconti" but contradicts the other repeats); ran annealing on
   f.70 alone, also nonsense; downloaded and thumbnail-scanned all 208 ASMi Carteggio Sforzesco key records
   (cart. 1591, 1597, 1598) on DECODE, reading headings and alphabets of the 15th-century copies (cart. 1597
   nos. 2-36) -- none headed Maino or Amidani; the nearest match by system design, 1597 no. 14 ("Angelus cum
   cifra Vincentij", shared among Johannes de Stavolis, Augustinus, Baptista, Matheus and Vincentius), has the
   same homophonic-plus-syllable-plus-word-sign-plus-null structure but different letter signs from f.68/f.70,
   so it is ruled out as the actual key, not confirmed as the system. **He never annealed f.68 and f.70
   jointly as one key** -- each was only ever attacked alone, which is the standard next move for two ciphers
   sharing a chancery system (this is why the target was harvested as G7 rather than left closed). His control:
   the same one-to-one solver verified on a synthetic 400-letter Italian cipher, solved in 1 of 3 restarts.
   That is a control for **one-to-one substitution only** -- it says nothing about whether the homophonic/
   nomenclator annealing attempts (points 1-2 and 5 above, which are the more plausible system for a
   26-31-type sign inventory this size) were properly tuned, since no synthetic homophonic-nomenclator control
   of matching design was run for those. Per rule 3, the homophonic negative on this target is not backed by a
   matched control and should be treated as unconfirmed until one is run.
6. **Aymeloglu (aaymeloglu/unsolved-ciphers, `ay/`, no licence, cite only).** No target folder for this pair
   (top-level folders are `burgess-1912`, `ferdinand-1635-1640`, `forster-1644`, `moray-1568`, `ottobon-1589`,
   `royalist-1646`, `starhemberg-1758`, `vande-perre-1653`; none named for Sforza, Maino, Amidani or it1583).
   `grep -rn "1583\|Maino\|Amidani\|R7898\|R7899"` across the whole repository: the only real hits are inside
   `ay/catalogue/decode-catalog.csv` and `decode-records.jsonl`, a scraped mirror of the DECODE database
   itself (see point 4) -- confirms both records' "Non-decrypted" status but is not independent solving work
   by Aymeloglu on this pair. `TARGETS.md`, `SHORTLIST.md` and `CATALOGUE.md` at the repository root: no
   mention of this pair.

## Verdict

No decipherment, transcription-into-plaintext, or key specific to BnF italien 1583 f.68 or f.70 was found in
any of the six sources. DECODE's own status field (via the cached catalogue snapshot) still reads
"Non-decrypted" for both R7898 and R7899. Mazzatinti's 1883 inventory, the only pre-existing catalogue entry
located, gives only "In cifre" for both, no reading. Bourdeau attempted both, separately, and closed the target
unread; the negative rests on a one-to-one-substitution control only, not a homophonic/nomenclator one, so it
does not by itself rule out the more plausible system (rule 3). Aymeloglu has not worked this pair. Per rule
10, this is a search result, not a claim of novelty: absence from these six sources does not mean unpublished,
only not found here.

**Stage 2, verified unsolved (conditional: DECODE, Gallica and print sources unreachable from this
environment; verdict rests on WebSearch, GitHub and the local Cryptiana snapshot)**

---

# Solver campaign, 23 September 2026 (joint nomenclator anneal, matched controls)

**Result: closed-negative, conditional on the transcription.** The joint solver reads every matched
control (4 control pairs, 99.2-99.9% of tokens, joint and each half alone) and reads nothing on the target:
target best -3.82 nats/token (joint, map B) against -4.23 for the same search on shuffled target tokens, a
margin of 0.25-0.42 nats/token; the solved controls score -1.95 to -2.49 and beat their own shuffled
baselines by 1.8-2.0 nats/token. No run gives Italian a reader can follow, and the best keys disagree from
run to run. No token is claimed (grades: H 0, C 0, S 0, M 0, I 0; all 794 cipher tokens unread).

**Image not seen.** Every archive host (de-crypt.org, gallica, archive.org, hathitrust) is blocked from this
environment, so the manuscript was not looked at. Everything here runs on D. Bourdeau's draft transcriptions
(dbourdeau/cyphersolver `it1583/`, commit 2e9ec01; text CC BY 4.0), made from binarized DECODE images with
diacritic variants merged. Per CLAUDE.md rule 2, the negative holds only for those transcriptions.

## Method

- **Files.** `ciphertext.txt` (f.68) and `ciphertext_f70.txt` (f.70): Bourdeau's `transcription.txt` and
  `transcription_f70.txt` copied unchanged, with a credit header.
- **Language model** (`tools/italian_ngram.py`). Corpus: paragraphs of period chancery Italian filtered by
  archaic function words (et, ad, de, el, dela, havemo, nuy...), with modern, French, Spanish and Latin
  paragraphs rejected, from Mazzatinti's *Archivio storico lombardo* X (1883) OCR (`cs-recheck/it1583/asl1883.txt`,
  15th-c. Lombard documents quoted in it) and the 1491 Sforza-chancery letters edited in D. Labancz's thesis
  (`cs-recheck/buda1489/labancz_1491.txt`, weight 2), 316,697 letters, the six control passages excluded.
  Normalised to j->i, y->i, v->u, k->ch, no accents; 21 letters; words run together (the sign stream shows no
  word division: Bourdeau's `.` separators fall 2-54 signs apart). Order-5 interpolated Witten-Bell model.
  Rebuild: `python3 tools/italian_ngram.py corpus <cs>/it1583/asl1883.txt:1 <cs>/buda1489/labancz_1491.txt:2
  --min-ratio 1.0 --exclude <control plain_*.txt concatenated> --out corpus.txt`, then `build corpus.txt
  --order 5 --out it15_o5.npz` (model not committed: 15 MB, and the thesis text is not ours to redistribute).
- **Solver** (`tools/nomenclator_anneal.py`, own code). A key maps every sign to a letter, a vowel+consonant
  syllable (80 possible; `--syl both` adds consonant+vowel), a word (de che per quale con ma quello perche et
  el la lo non) or null, one key shared by all files (joint). Score is generative: log P(reading) under the
  5-gram model, plus log P(sign | value) with uniform choice among the signs sharing a value, plus a 3%
  null-insertion prior. (The first version scored log-likelihood ratio and was degenerate: "quello" on every
  sign beat the true control key, 2240 vs 752; fixed before any target run.) Caps: at most 6 syllable signs,
  4 word signs, 2 nulls, 4 signs per letter. Simulated annealing, 300,000 moves per restart (T 3.0 -> 0.05),
  16 restarts, greedy steepest-ascent finish. Every run, control and target, used exactly these settings.
  Options used on the target only as extra variants: `--context clear` (clear phrases of f.68 as fixed
  context scored across the boundaries), `--fix V=...`, `--unit` (a repeated group must decode to one or two
  whole corpus words, 25 nats per violation), `--shuffle` (search baseline).
- **Runner.** `campaign.py` runs one configuration and appends a row to `runs.tsv`; `run_controls.sh`,
  `run_target.sh`, `run_target2.sh` are the exact batches; full results in `runs/*.json`.

## Sign inventory

Codes are Bourdeau's, per file (headers of the two transcriptions). **Identified across files:** every f.70
code his f.70 header describes as "codes as f.68" (8 p c n r z > B H F + D S J g Q d V). **Kept separate:**
f.70 `E`, which his f.70 header redefines as "b with double bar" (unified id `E70`), and the f.70-only codes
W K Y O e P 3 4 6 s b X (X is not defined in either header; f.68's lowercase x is kept apart from it).
Map A (`signs_mapA.tsv`) is this conservative identification, 39 unified signs. Map B (`signs_mapB.tsv`) adds
one hypothesis: f.70 E = f.68 B (barred b vs b with double bar; each is its letter's top sign, 11.8% and
11.9%). Full table in `signs.tsv`. Cross-letter evidence for shared labels is weak: 18 trigrams shared
against 10.7 expected under shuffle (max 21 in 200 shuffles); bigram overlap equals the shuffle expectation.

| unified | description (Bourdeau) | f.68 count | f.70 count | status |
|---|---|---|---|---|
| p | p as written | 48 (11.9%) | 31 (7.9%) | shared |
| F | double-barred stroke | 30 (7.4%) | 27 (6.9%) | shared |
| B | barred b | 48 (11.9%) | 7 (1.8%) | shared |
| + | cross/stroke | 24 (5.9%) | 30 (7.7%) | shared |
| E70 | f.70 E: b with double bar | 0 (0.0%) | 46 (11.8%) | f70 only |
| 8 | 8 as written | 28 (6.9%) | 17 (4.4%) | shared |
| Q | phi | 12 (3.0%) | 32 (8.2%) | shared |
| J | barred yogh | 20 (5.0%) | 24 (6.2%) | shared |
| c | c as written (dotted c merged) | 24 (5.9%) | 19 (4.9%) | shared |
| S | long s | 17 (4.2%) | 23 (5.9%) | shared |
| H | looped h | 14 (3.5%) | 21 (5.4%) | shared |
| d | d with apostrophe | 23 (5.7%) | 10 (2.6%) | shared |
| z | z as written | 8 (2.0%) | 20 (5.1%) | shared |
| E | f.68: barred epsilon | 24 (5.9%) | 0 (0.0%) | f68 only |
| > | > as written | 6 (1.5%) | 14 (3.6%) | shared |
| r | r as written | 12 (3.0%) | 8 (2.1%) | shared |
| Y | slashed v | 0 (0.0%) | 14 (3.6%) | f70 only |
| V | cross-circle (venus) | 9 (2.2%) | 4 (1.0%) | shared |
| g | barred g | 10 (2.5%) | 2 (0.5%) | shared |
| D | divide sign | 10 (2.5%) | 1 (0.3%) | shared |
| n | n as written | 5 (1.2%) | 4 (1.0%) | shared |
| - | dash-hook | 9 (2.2%) | 0 (0.0%) | f68 only |
| X | X (undefined in f.70 header) | 0 (0.0%) | 7 (1.8%) | f70 only |
| W | ab-ligature | 0 (0.0%) | 6 (1.5%) | f70 only |
| x | x as written | 6 (1.5%) | 0 (0.0%) | f68 only |
| 7 | hooked 7 | 5 (1.2%) | 0 (0.0%) | f68 only |
| k | k as written | 5 (1.2%) | 0 (0.0%) | f68 only |
| 4 | 4 | 0 (0.0%) | 4 (1.0%) | f70 only |
| M | m-like sign with bar | 4 (1.0%) | 0 (0.0%) | f68 only |
| O | reversed c | 0 (0.0%) | 4 (1.0%) | f70 only |
| 6 | 6 | 0 (0.0%) | 3 (0.8%) | f70 only |
| e | plain epsilon | 0 (0.0%) | 3 (0.8%) | f70 only |
| 3 | 3 | 0 (0.0%) | 3 (0.8%) | f70 only |
| R | R (paragraph-initial; undefined in header) | 2 (0.5%) | 0 (0.0%) | f68 only |
| b | plain b | 0 (0.0%) | 2 (0.5%) | f70 only |
| K | hatched sign | 0 (0.0%) | 2 (0.5%) | f70 only |
| P | barred p | 0 (0.0%) | 1 (0.3%) | f70 only |
| f | f (undefined in header) | 1 (0.2%) | 0 (0.0%) | f68 only |
| s | s | 0 (0.0%) | 1 (0.3%) | f70 only |

Profile: f.68 404 tokens, 26 types, IC 0.061, doubled signs 0.8%; f.70 390 tokens, 31 types, IC 0.058,
doubles 1.8%. Corpus letter frequencies: e 13.7, a 11.0, i 9.2, o 9.1, n 6.8, t 6.7, r 6.7, s 6.0.

## Control (rule 3)

Six held-out passages of 15th-c. Lombard chancery Italian from the asl1883 OCR (`control/plain_*.txt`,
excluded from the model), enciphered with random keys of two designs, each pair sharing one key, each half
copying the real letter's run structure (f.68: 404 cipher tokens in 9 runs with 285 letters of clear text
between them; f.70: 390 tokens in 3 runs, 12 clear letters). `tools/nomenclator_anneal.py synth`.

- `control/design_1447.json` (the 1447 family): e x3, a x2, o x2, i x2 homophones (skewed use), 3 VC syllable
  signs, 3 word signs, 2 nulls at 3%, 34 signs; observed 29-32 types, IC 0.044-0.048 (flatter, so harder,
  than the target). Controls C1-C3.
- `control/design_profile.json` (matched to the target's profile): e, o, i x2, 2 syllables, 2 words, 1 null;
  observed 26/27 types, IC 0.060/0.059. Control CP.

| control | joint: tokens right / restarts at best | f.68 half alone | f.70 half alone | joint score/token | shuffled joint |
|---|---|---|---|---|---|
| C1 | 0.999 / 5 of 16 | 0.995 / 2 | 0.995 / 2 | -2.309 | -4.275, -4.229 |
| C2 | 0.997 / 10 of 16 | 0.998 / 2 | 0.992 / 4 | -2.227 | -4.277 |
| C3 | 0.995 / 1 of 16 | 0.995 / 2 | 0.995 / 5 | -2.362 | -4.314 |
| CP | 0.997 / 6 of 16 | 0.998 / 2 | 0.997 / 1 | -2.053 | -4.145 |
| C1, clear context | 0.997 / 4 of 16 | | | -2.487 | |

Letter accuracy 0.978-1.000 throughout. Controls solved: 12 of 12 solver runs (plus the clear-context run),
so the tooling is not the reason for the target result, at this length, sign count and design.

## Runs (target)

Same settings as the controls. Every run is a row in `runs.tsv` with its best reading.

| run | score/token | shuffled baseline | margin | restarts at best | readable? |
|---|---|---|---|---|---|
| joint, map A | -4.000 | -4.250, -4.205 | 0.21-0.25 | 1 of 16 | no |
| joint, map B | -3.816 | -4.233 | 0.42 | 1 of 16 | no |
| f.68 alone | -3.530 | -3.855 | 0.33 | 1 of 16 | no |
| f.70 alone | -3.542 | -3.772 | 0.23 | 1 of 16 | no |
| joint A, clear context | -4.131 | -4.417 | 0.29 | 1 of 16 | no |
| joint B, clear context | -4.063 | | | 1 of 16 | no |
| joint A, V = de | -3.975 | | | 1 of 16 | no |
| joint A, V = de, clear context | -4.184 | | | 1 of 16 | no |
| joint A, V = che, clear context | -4.124 | | | 1 of 16 | no |
| joint A, V = et, clear context | -4.150 | | | 1 of 16 | no |
| joint A, repeats as word units | -4.038 | | | 1 of 16 | no |
| joint A, units, V = de, clear ctx | -4.216 | | | 1 of 16 | no |
| joint A, loose (VC+CV, 10 syl, 6 words, 4 nulls) | -3.864 | -4.177 | 0.31 | 1 of 16 | no |
| joint A, letters only (+2 nulls) | -4.125 | -4.368 | 0.24 | 1 of 16 | no |

Against the claim criteria of the brief: (a) margin over the scrambled baseline: target 0.21-0.42 nats/token,
controls 1.8-2.0, so no target run reaches the control margin; (b) consistency between the letters: the best
keys disagree between runs and between the letters (sign F is r, d or i; p is e or a), and only 1 of 16
restarts reaches each best, where solved controls reached theirs in 1-10 of 16; (c) no reading contains
Italian a reader can follow (sample, best run, f.68: "glamlaretatmafarctadedieetaalreferitatrtdel...").
V (cross-circle) forced to "de", "che" or "et" does not help; the repeats forced to whole words do not help.

## Negative

Closed-negative conditional on the transcription (rule 3, both numbers): **target -3.82 nats/token (best of
all runs, joint map B), 0.42 above its shuffled baseline; control -1.95 to -2.49 nats/token, 1.8-2.0 above
theirs, 99.2-99.9% of tokens read.** It says: under Bourdeau's draft codes, f.68 and f.70 are not a letter
cipher with 1447-style homophones, a few syllable and word signs and 1-2 nulls in 15th-c. chancery Italian,
whether read jointly under one key (either identification map) or each alone. It does not rule out: (1)
transcription error, especially the merged diacritic variants (a merged pair that stood for two letters makes
the stream polyphonic, which this solver cannot read); (2) a key with many more syllable or word signs than
the caps (the 1447 family has a sign for every vowel+consonant pair); (3) the two letters in different keys
under similar shapes (the cross-letter trigram test is weak); (4) Latin, or long stretches of names and code
words; (5) the doubled-sign rate on f.68 (0.8%, lower than every control, 0.8-2.6%) may mean doubled letters
are written once or with a sign, which the model was not built for.

## Grading

No reading is claimed. H 0, C 0, S 0, M 0, I 0; 794 of 794 cipher tokens unread. `key.tsv` and
`best_reading.txt` are the best-scoring key and its decode, kept only so the negative is reproducible;
`check.py` regenerates `best_reading.txt` from the two transcriptions, `key.tsv` and `signs_mapB.tsv`, and
exits 1 if it is stale.

## Where it was not found

- Bourdeau's checks (his NOTES and profile, 21 Sept 2026): 208 Sforza key records on DECODE (ASMi Carteggio
  Sforzesco cart. 1591, 1597, 1598), none headed Maino or Amidani; 1597 no. 14 ("Angelus cum cifra
  Vincentij") same design, different letter signs; Mazzatinti 1883 gives only "In cifre".
- Check-solved sweep of 23 Sept 2026 (above, six sources): nothing.
- This session's WebSearch, 23 Sept 2026: `cifra Amidani 1446 Francesco Sforza chiave cifrario "Amidani"`
  (nothing on this pair; one lead: a Biblioteca di Cremona post on a "codice segreto degli Sforza" with
  cipher material spanning 1444-1479, lanuovapadania.it, not followed up); `"italien 1583" Bibliothèque
  nationale Sforza 1446 chiffre déchiffrement` (BnF archives-et-manuscrits catalogue records for italien
  1583-1615, no decipherment mentioned). No phrase search was possible: nothing was decoded.

## What a next solver needs

1. [23 Sept 2026: not on Gallica, see "Image gate" below; a BnF order is the only route.] A sign-exact transcription from a colour image of BnF italien 1583 ff.68 and 70 (Gallica or a BnF order),
   with the diacritic variants (dotted c, d with apostrophe, barred g, the bars on b) kept apart and the two
   hands compared sign by sign. Then rerun `run_target.sh` unchanged; the controls already stand.
2. The key: ASMi Sforzesco cart. 1597 at full size, Cerioni, *La diplomazia sforzesca* (1970) vol. 2, and the
   Cremona Sforza cipher material (1444-1479) named above.
3. Mazzatinti lists six more Amidani letters "in cifre" in the same volumes (check-solved notes above) and
   DECODE R7899-R7915 hold seventeen more 1446 cipher records from ital. 1583: more text in the same hand or
   key would double the length and may be the practical route. (Suggestion only; not started here.)

## Image gate (23 September 2026)

**Result: BnF italien 1583 is not digitised on Gallica.** Nothing was fetched and nothing was transcribed or rerun. The target
stays **closed-negative, conditional on Bourdeau's draft transcriptions** (rule 2).

Queries, all on 23 Sept 2026, 19:32-19:35 UTC, descriptive User-Agent, one request at a time:

1. Gallica SRU `dc.title all "italien 1583"`: 68 records, all coins (Desana 1583) and unrelated printed books.
2. Gallica SRU `gallica all "Italien 1583"`: 19,065 records. The top hits include the "Archivio Sforzesco" series titles
   (whose shared title quotes "Codd. 1583-1593") but none has source italien 1583.
3. Gallica SRU `dc.title all "Archivio Sforzesco Documenti originali"`: 35 records, the whole series on Gallica:
   **italien 1584 through 1615, every volume, and no italien 1583.** For example, italien 1584 is
   ark:/12148/btv1b100373864, digitised from the microfilm ("document de substitution"), and 1585 from the original.
4. Gallica SRU `dc.source all "italien 1583"`: 0 records.
5. Gallica SRU `dc.title all "Sforzesco" and dc.type all "manuscrit"`: the same 35, no 1583.
6. Gallica SRU `gallica all "italien 1583" and dc.type all "manuscrit"`: 64 records, none italien 1583.
7. BnF Archives et manuscrits, record for italien 1583 (`archivesetmanuscrits.bnf.fr/ark:/12148/cc10584q/cd0e61`):
   the record has no Gallica link. The only surrogate listed is a black-and-white microfilm: reading-room shelfmark
   **MF 16151**, and **R 151450** as the matrix to cite when ordering a reproduction. The detailed description is
   Mazzatinti, *Manoscritti italiani delle biblioteche di Francia* t. II, pp. 285-291. The record for italien 1584
   (`.../cd0e76`), fetched as a comparison, does link its Gallica ark. So the missing link on the 1583 record means
   the volume is not digitised; it is not a quirk of the page.

DECODE (R7898 and R7899 hold Bourdeau's images) requires a login, and this brief allowed no credentials. It was not
tried. Requests: gallica.bnf.fr 6 (SRU only; no IIIF manifest or image, since there is no ark), archivesetmanuscrits.bnf.fr 2.

Suggestion only, not started: a reproduction of ff.68 and 70 ordered from the BnF under matrix R 151450 (or Gallica's
digitisation-on-demand for italien 1583) is the one route to the image. It would go into REQUEST.md and ASKS.md if the
orchestrator promotes it. Mazzatinti t. II pp. 285-291 has not been checked against the 1883 ASL inventory already cited.

