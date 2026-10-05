open
No printed edition of the Birago-Nevers correspondence exists (searched, none found); Tomokiyo's catalogue (`sources/cryptiana/web/nevers.htm`, BnF fr.3251, folio 119) was read in full by this worker and names this exact letter (no.63, Saluzzo 13 Nov 1571) as using "a numerical cipher (not deciphered)", quoted verbatim below, and Bourdeau's own matched-control cryptanalysis of the same Gallica image (16 Sept 2026) independently confirms no prior solution.

# Lodovico Birago to the Duke of Nevers (13 November 1571)

## Check-solved (LANE CX, 25 Sept 2026)

Formal six-source sweep per `.claude/briefs/check-solved.md` — this folder previously had no formal check-solved
section, only the "Solver status" line below citing Bourdeau's summary third-hand.

1. **Web search.** `"Birago" "Nevers" 1571 cipher chiffre déchiffré Saluzzo` (this worker) surfaced Bourdeau's own
   published site (`dbourdeau.github.io/cyphersolver`, the same closed-negative already on file), Wikipedia pages
   for Louis de Gonzague and René de Birague (a different Birago), and general Saluzzo history — no edition,
   article or solution. A second query, `"Lodovico Birago" lettere Nevers Saluzzo edizione carteggio pubblicato`,
   found only Birago's Treccani biographical entry and unrelated Birago-surname genealogies — **no published
   edition of Birago's letters to Nevers exists**, confirmed by this search, not merely assumed. Model-solve-
   announcement family (checked once for all four targets) found nothing relevant.
2. **Standard edition/calendar.** None exists to check (previous item) — this correspondence survives only in the
   Gallica-digitised archival volume itself (BnF fr.3251, `archivesetmanuscrits.bnf.fr/ark:/12148/cc49712p`), not
   in a modern or period printed edition. Not a gate failure by the intake-gate's own logic (there is no edition
   to have failed to open); the controlled cryptanalytic negative below stands in its place.
3. **Community lists.** Tomokiyo's `nevers.htm` (mirrored locally, read in full, not re-fetched) states, of the
   November 1570-May 1571 Ceppo-Nevers cipher letters and this one specifically: *"In November 1571, they used a
   numerical cipher (not deciphered). f.119 (no.63) Saluzzo, 13 November 1571."* — this is the letter under audit,
   named by shelfmark, date and folio, quoted verbatim per rule 10 and the check-solved.md "named source"
   lesson. No Cipherbrain/Schmeh-specific page found for this item.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` (local cache) and Aymeloglu's cached DECODE
   catalogue mirror (`catalogue/decode-catalog.csv`, fresh clone) both grepped for "birago"/"3251": the catalogue
   mirror has four hits, all for **different** Lodovico Birago items — BnF fr.3623 no.27 f.41 (1591), fr.3621
   nos.31/35/36 (1592, Sainte-Menehould), fr.3619 f.73 (1591, Langres) — different shelfmarks, a different decade,
   status "Decrypted" on DECODE. None is fr.3251 f.119 or this letter's 13 Nov 1571 date; flagged as a fact about
   the correspondent's other, later, already-decrypted correspondence, not evidence bearing on this item. Zero
   hits for "3251" itself in either source.
5. **Bourdeau** (`github.com/dbourdeau/cyphersolver`, fresh depth-1 clone by this worker, 25 Sept 2026, not the
   19 Sept citation already in this file): `birago/NOTES.md` and `birago/profile.json` read in full. Confirms and
   extends the existing "Solver status" line below: glyph-level re-transcription from the 8521x5849px Gallica
   image (`btv1b9060248g` view 120) corrects four errors in Tomokiyo's own transcription; five cipher designs
   (prefix/suffix variable-length codes, structured homophony, polyphonic single figures, a two-digit
   letter-with-marked-code-groups design, a syllabic two-digit alphabet) were each tested against matched
   synthetic controls of the same length/symbol profile and excluded or left unread; `profile.json`'s own
   `conditions.prior_solution` field records `"exists": "no"`, `"found": "not found"`, and `outcome.method`:
   `"not solved"`. A sweep of all 118 remaining openings of the same volume (fr.3251) for a second letter in the
   same figure cipher, and a check against the 1574 Nevers key (fr.3315), both failed to find a sibling or a
   matching key. Code MIT / text CC BY 4.0, cited not copied.
6. **Aymeloglu** (`github.com/aaymeloglu/unsolved-ciphers`, fresh depth-1 clone by this worker, 25 Sept 2026):
   `grep -rli "birago"` across json/md/csv/txt/tsv finds only the DECODE catalogue mirror hits already covered
   under item 4 (the different, later Birago items); no dedicated treatment of this letter anywhere in the
   repository.

**Verdict: open, unchanged.** No printed edition exists to check; the one community source that names this exact
letter (Tomokiyo) states it as not deciphered; DECODE, Bourdeau and Aymeloglu all independently confirm no prior
solution of fr.3251 f.119 specifically (as opposed to the correspondent's other, later, already-decrypted
letters). Bourdeau's own attempt is a genuine matched-control cryptanalytic negative (rule 3), not merely an
absence claim, and is the strongest evidence here. Grade: no reading exists to grade. Novelty not classified
(rule 10; not this brief's job).

Requests this pass: github.com 2 (fresh shallow clones, dbourdeau + aaymeloglu, deleted after grep). WebSearch 2
queries. No other hosts, no subagents, no logins, no credentials.

## Background (pre-existing)

- **Source:** BnF fr.3251, f.119. Letter in Italian. One paragraph is in a numerical cipher that the keys reconstructed for Birago's other 1570-1572 letters do not solve. Image: https://gallica.bnf.fr/ark:/12148/btv1b9060248g/f120.item
- **Status:** Open.
- **Transcription:** `ciphertext.txt` (Tomokiyo's). Note his warning: the diacritics (÷ ¯ ¨ + and letters n, f, c, m, a, l) should be placed over the following one or two characters. Check the Gallica image before trusting any parse.
- **Background page:** `sources/cryptiana/web/nevers.htm` (section BnFfr3251).
- **Ideas:** Digits run continuously without separators, so the first problem is tokenisation. Try two-digit groups, then variable-length. The diacritics probably modify the following digit pair (syllable vs. letter, or a vowel change). Plaintext is Italian.
- **Solver status (19 Sept 2026):** Closed-negative by Bourdeau (cyphersolver/birago), 16 Sept 2026, after glyph-level re-transcription from Gallica (the "+" signs are superscript crosses). Variable-length designs excluded against controls; the only consistent design is beyond the annealer at this length. Needs a sibling letter or a crib.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/birago/NOTES.md ; TARGETS.md
- Their extent, in their words: attempted 16 Sept, structure narrowed, not read (483 digits)
- Their date: 16 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Pooled with fr.3252 f.100r (BIRAGO-NUM, 2 Oct 2026)

Full record: `../birago-fr3252-1571-72/NOTES.md`, section "f.100r (no.67, 8 Jan 1572): transcription and pooled design
analysis with f.119"; scripts and outputs in `../birago-fr3252-1571-72/num/`; family rows in `HYPOTHESES.md` (this
folder); decode file `families/homophonic-1-profile=target-it16dip.txt` (not a reading). Summary:
- fr.3252 f.100r (Birago to Nevers, Saluzzo 8 Jan 1572) is a second text of 565 digits in this system, transcribed
  blind twice (two-reader disagreement 1.4%, none on a digit value) in Bourdeau's ct2 notation.
- Same key, controlled: 21 shared 6-mers between the two letters (shuffled null max 5; two-key synthetic max 8), one
  shared 10-mer `1503985803`, residual bigram r 0.728 (two-key synthetic max 0.52). The letter table looks closer to
  ~30-50 effective two-digit cells than to the 62 symbols of Bourdeau's pairing.
- The marks: a dot sits over both figures of a two-digit code group (Nevers key no.7's stated convention; Tomokiyo's
  f.119 transcription already wrote ":41 :41 :25 :36"). On f.119, Bourdeau's two "4. 1" are a dotted 4 + dotted i
  (checked by eye on his `cipher_full.png`), i.e. dotted group 41, which also occurs six times in f.100r.
- Bourdeau's "75 pairings" constraint does not discriminate (200/200 random mark placements also segment); it is a
  description, not a test.
- Pooled homophonic family (N=476 pairs, K=64): clean control 0.896 (gate met), target judge FAIL (-1.272 vs real_p05
  -0.959); control with 0.25 noise (the segmentation's probable error at this K) 0.249, below gate. A non-test, not a
  negative. Next: joint phase+key anneal controlled at N=476, or a crib from the clear-text names.
Status unchanged (`open`): no reading, no token graded. Novelty not classified (rule 10).

## Pre-registered crib drag, pooled with f.100r (BIRAGO-NUM2, 2 Oct 2026)

Full record: `../birago-fr3252-1571-72/NOTES.md`, section "f.119 + f.100r: pre-registered crib drag"; files in
`../birago-fr3252-1571-72/num/crib/` (PREREG.md pushed before scoring, commit e8633359). Summary:
- 12 name/title cribs (carmagnola, bellagarda/bellegarda, ualletta, sauoia, turino, duca, regina, ugonotti, centurione,
  maresciale, maesta) dragged over the pooled 473-pair stream; score = bigram PMI of the induced key elsewhere in both
  letters; null = 200 token permutations.
- Power control (synthetic, 476 pairs, 30-55 cells, 5% strays): a 10-letter crib present is accepted 0-50% of the time,
  short cribs 0-20%, and a wrong placement passes in about 1 trial in 10: weak and anti-conservative.
- Target: 11 of 12 not accepted; maesta accepted by the pre-registered rule (p 0.005) at a hot spot (codes 15, 19) where
  5.7% of 300 random six-letter decoy words score as high, so it is void. No crib-backed pair value; fewer than 8 types,
  so the joint anneal (step 2) was not run.
- Premise risk: in Birago's 1572 key names are single word codes; here they may sit in the dotted two-figure groups.
Status unchanged (`open`): no reading, no token graded. Novelty not classified (rule 10).

## Joint phase+key anneal, pooled with f.100r (BIRAGO-NUM3, 2 Oct 2026)

Full record: `../birago-fr3252-1571-72/NOTES.md`, section "f.119 + f.100r: joint phase+key anneal". Files are in
`../birago-fr3252-1571-72/num/joint/`; PREREG.md was pushed in d27489c6 before any run. The instrument is the new
family `tools/family_run.py --family phased_homophonic`, which resamples the phase of every digit run jointly with the
key. Both rows are in `HYPOTHESES.md`. Summary:
- Control: synthetic it16dip, 48 runs / 985 digits, 5% strays. At the pre-registered 55 cells it reads **0.386**
  (0.100-0.827), below the 0.6 gate. At 40 cells it reads 0.645 (0.090-0.934), which is curve only, not gating.
- The target was not run. Seeds lock into either the right phase or a whole-stream phase flip. At 55 cells the true
  cut and the flip score level on the joint objective, so this is a model limit at this length, not a search limit.
- This is the third attempt at this key. The instrument is retired for this hypothesis (untested-by-this-tool, not
  refuted). Next: a decoy-null, joint-consistency crib test (~$2), or the dotted groups read as name codes, or a third
  letter in the same key.
Status unchanged (`open`): no reading, no token graded. Novelty not classified (rule 10). Credit: D. Bourdeau
(cyphersolver, f.119 transcription and the matched-control negative this builds on).


## Tomokiyo's reply, 5 Oct 2026 10:58 UTC (project mailbox; logged 5 Oct 2026 13:16 UTC by the account-3 orchestrator)

S. Tomokiyo answered the owner's note: he is "really interested in the numerical cipher of f.119 (no.63) of BnF fr.3251" and glad of
the second letter in it (fr.3252 f.100r); he has no key for it and offers two related systems as leads: (1) "A Simple Numerical
Cipher in Cinq Cent de Colbert 398 (1576-1577)", https://cryptiana.web.fc2.com/code/frenchnumerical.htm -- "the date is (a bit)
close but this is a simple system"; (2) "Variable-length Figure Cipher between Henry de la Tour and Duke of Nevers (1589, 1591)",
https://cryptiana.blogspot.com/2025/02/variable-length-figure-cipher-between.html -- "This is Nevers, but from a later date". He
notes his page does not mention BnF fr.3251. For the other letters he has no time; once keys are identified he leaves the texts to
historians. Next: snapshot both pages to sources/cryptiana/, transcribe both systems, and test each against the pooled f.119+f.100
digits with tools/key_crossmatch.py + its control (and, for the variable-length system, a segmentation test against the Nov 1571
digit stream) -- worker TOMO-NUM (~$4). No reply owed now; a thank-you rides with the result (outreach README 1c).

## Tomokiyo's two numerical systems tested (TOMO-NUM, 5 Oct 2026)

Brief `.claude/briefs/runs/2026-10-05-acct3-tomo-num.md`; PREREG `keys/PREREG-TOMO-NUM.md` pushed in 6371272f before any score.
Script `keys/tomo_test.py`, output `keys/tomo_test_out.txt`. Credit: S. Tomokiyo (Cryptiana) for both leads and the Colbert 398 table.
- **Sources.** `sources/cryptiana/web/frenchnumerical.htm` re-fetched 5 Oct 2026: byte-identical to the 26 Sept snapshot (sha1
  e27ed5b0), so not re-saved; its table image `frenchnumerical.png` added. The 2025/02 post is saved as
  `sources/cryptiana/blog/2025_02_variable-length-figure-cipher-between.html`; it prints no table but names the system: Nevers
  collection no.23 (BnF fr.3995 f.46-47, Oct 1589). Its alphabet was read from the period key sheet itself (Gallica
  btv1b525085665 canvas f95, label 47r; crop `keys/img/f95_alpha.jpg`): a3 b9 c4 d5 e2 f1 g8 h6 i7, l = the letter x, m79 n51
  o97 p36 qu42 r18 s25 t84 u63 (dot over the tens figure), y a triangle; nulls 0 and dotted 2 3 4.
- **Keys.** `keys/tomo_colbert398.tsv` (system A, two-digit + 7 = space; his table prints 31 under both a and m, kept as a|m)
  and `keys/tomo_nevers_no23.tsv` (system B, grade H for the table).
- **Test 1, segmentation fit** (985 digits, 48 runs; beam parse into each system's codes with a stray option; objective per digit):
  | system | control (3 seeds, same length/runs/5% strays) vs its shuffle max | target | target shuffle max (20) | strays parsed | verdict |
  |---|---|---|---|---|---|
  | A Colbert 398 | -0.575/-0.585/-0.577 vs -1.16 to -1.19 (3/3 above) | -1.624 | -1.536 (19/20 shuffles >= target) | 71% | no fit (control-backed) |
  | B Nevers no.23 | -0.697/-0.746/-0.671 vs -1.21 to -1.25 (3/3 above) | -1.293 | -1.252 (20/20 >= target) | 32% | no fit (control-backed) |
- **Test 2, `tools/key_crossmatch.py` gate (system A, pair files):** f.119 coverage 0.15, stat 0.33; f.100r coverage 0.19, stat
  2.12; both `none` against gate 3.292 / coverage 0.5. Matched control (system A synthetic, ~240 pairs, em-phase cut): 3/3 `hit`
  (stat 16.9, 9.5, 8.9; coverage 0.74-0.79). Not run for B (its variable-length codes do not fit a pair cut).
- **Outcome: no fit, control-backed, for both systems.** Neither table, nor a design with this table, is the Nov 1571 key. The
  target scores at or below its own shuffles under both keys, so it is not even partly in either alphabet. Not a test of the
  design family (an unknown two-digit or variable-length key), which stays open. No reading, no token graded.
- Suggestion (not run, brief did not name it): Tomokiyo's France numerical page links a 2024/09 post, "duke-of-nevers-variable-
  length-figure", which his 2025/02 post calls "the 1571 instance"; reading it for what he says about this letter's code
  lengths is a ~$0.5 snapshot job.
Status unchanged (`open`). Novelty not classified (rule 10). Requests: cryptiana.web.fc2.com 4, cryptiana.blogspot.com 1, Gallica
IIIF 4.
