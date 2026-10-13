partial
Verdict: partial -- 6 of f.10r's 37 tokens (S1) carry f.13r's H glosses at grade C (82 82 "D. n.", 21 21 "Berry", 12 12 "b. Pal."; D2-F4712, 8 Oct 2026, applying the owner's ASKS 113 same-writer judgement under PREREG_duchf13.md; pre-registered crib gate met: 6 C >= 3, p 0.029 vs random code sets); the other 31 tokens have no reading (key no.1 a non-test at 37 tokens, DUCH-KEY1B; key no.4 cannot cover f.10r, DUCH-KEY4; key no.71 a control-backed negative as an unmarked letter text, F4712-K71 11 Oct 2026, and as an all-code text on its Motz list, F4712-71 13 Oct 2026; f.13r's list is not key no.1, 0/6). No glossed sibling in ff.13v-35r (F4712-CENSUS, F4712-71, F4712-C39, 13 Oct 2026). The same-writer basis is one person's "I think the same" against our own "leaning different" on the 8-form, and R11A-F4712's blind digit test was a NON-TEST (6 Oct). See "## Remaining gaps" at the end.
Gomberville (ed.), *Les Mémoires de M. le duc de Nevers* (1665; Google Books H2eV4wAmIr0C and three other copies) full-text searched by this worker (NV-INTAKE, 3 Oct 2026) via the Books API with `&country=US`: "duchesse ma femme" hits only Nevers' 1593-94 Roman legation speech ("...qu'à la Duchesse ma femme, à mes terres...", also in the *Discours de la legation* 1594) and "Madame ma femme" 0 -- no letter to the duchess with a cipher passage printed there.

# BnF fr.4712 f.10, the duc de Nevers to the duchesse de Nevers, undated: 37-number cipher passage -- NV-09

> Correction (D2V-F4712, 8 Oct 2026): not undated. The BnF *Catalogue général des manuscrits français, Ancien fonds* t. IV (1895),
> fr.4712 items 9-10, says the first letter (f.10) "a une partie chiffrée. Elle est datée du i octobre 1592 et est signée d'un
> monogramme" (IA p1cataloguegnr04bibluoft OCR; the day is not settled, not yet checked on the leaf). See AUDIT.md "AUDIT 1".

Intake (NV-INTAKE, account 2 for the account-3 orchestrator, brief `.claude/briefs/runs/2026-10-03-acct3-nv-intake.md`).
Source row: NEVERS-VEIN.tsv NV-09. No image read in this job.

- Holding: BnF Français 4712, Gallica ark:/12148/btv1b9058289m (142 canvases, all labelled NP). Cabinet Noir places
  f.7r at vue 15 (right page), so f.10 is near vues 16-18 -- inferred, not checked.
- BnF items 9-10 (record cc57762j, as quoted by the NEVERS-VEIN scout; html not on disk): "Lettres ... a la duchesse de
  Nevers".
- Tomokiyo (nevers.htm, "BnF fr.4712"), verbatim: "f.9-12 Catalogued as \"Lettres de LOUIS DE GONZAGUE, duc DE NEVERS, a
  la duchesse de Nevers\". There is a short passage in ciper on f.10, undeciphered." followed by the 37 numbers now in
  `ciphertext.txt` (as printed; 37 numbers, 29 distinct, range 8-95, 2 signs printed "♀"; repeats 10x3, 82, 52, 85, 92,
  21, 12 x2; opens "82 82").

## Check-solved (NV-INTAKE, 3 Oct 2026)

(1) web -- below; the exact number string returns nothing; (2) print -- Gomberville 1665, not printed; (3) community
lists -- Tomokiyo: "undeciphered" (quoted); (4) DECODE -- no record; (5) Bourdeau -- only a copy of Tomokiyo's line
"BnF fr.4712 contains some undeciphered letters" (targets/napoleon/unsolved.htm); (6) Aymeloglu -- nothing. Cabinet
Noir uses fr.4712 f.7r only (period pair for no.71). Verdict: **open** (too short to carry a negative: 37 tokens).

## Solver repositories and Cabinet Noir (NV-INTAKE, 3 Oct 2026)

Shallow clones, 3 Oct 2026 03:13 UTC: el-descifrador/cabinet-noir HEAD 47b6db9 (Cabinet Noir v1.0, 29 Sept 2026,
CC BY 4.0), dbourdeau/cyphersolver HEAD 4aedb40, aaymeloglu/unsolved-ciphers HEAD d2800bb. Grepped every file for the
shelfmark (3993, 3416, 4712, 4715 + folio), the Gallica arks (btv1b9059229n, btv1b9058240c, btv1b52509819x,
btv1b9058289m) and the key numbers (no.25, no.70, duchess no.1/2/4).
- Cabinet Noir: reads only Montholon letters (fr.3414 ff.126-127; fr.4715 n27 f.50, n35 f.58, n37 f.60, n47 f.70,
  n48 f.71, n58 f.81; vues 115, 131, 135, 155, 157, 177 of btv1b52509819x) with keys Vieuville-Nevers and fr.3995 no.71.
  Its only fr.4712 mention is f.7r (vue 15), used as the period pair for no.71. No fr.3993, fr.3416, fr.4715 f.38 or
  fr.4712 f.10, no key no.25 or no.70.
- Bourdeau: targets nevers1574/1587/1588/1589/1593/1595. nevers1595 is fr.3993 no.102 ff.148r-149r (Nevers to
  Villeroy, 16 Aug 1595), not ff.71-72; its NOTES.md says "the Balagny and Charles de Gonzague ciphers of the same weeks
  are different systems" from the f.148 cipher and lists fr.3995 nos.68-74 as "Italian or figures only" -- no.70 was
  looked at for a different letter and not applied to any Charles de Gonzague letter. fr.3416, fr.4712 and fr.4715 f.38:
  only in the raw nevers.htm/league.htm copies under research/gallica_siblings/src/ and the fr.4715 manifest/notice in
  research/gallica_sweep/ (a sweep, no reading). targets/napoleon/unsolved.htm repeats Tomokiyo's line "BnF fr.4712
  contains some undeciphered letters".
- Aymeloglu: no hit for these shelfmarks (the decode-catalog.csv hits on 3993/3416/4712 are DECODE record ids of
  unrelated items).
- DECODE: our catalogue snapshots in sources/decode/ (records-non-decrypted-2026-09-24-diff.tsv, keys-all-2026-09-28*.tsv,
  keys-na-p58/p59-128) carry no record for BnF Français 3993, 3416, 4712 or 4715; DECODE's Nevers records there are
  fr.3975/3976 (Bourdeau's targets). Not re-queried live this session.

## Web and blog check (NV-INTAKE, 3 Oct 2026)

Plain web searches: (1) `"Français 4712" Nevers lettres à la duchesse de Nevers chiffre f.10` -- Biblissima fr.3375,
CCFr Nièvre letters, archives.nievre.fr pdf, donum.uliege.be: none about this letter; (2) `"fr.4712" OR "fr. 4712" Duke of
Nevers letter to the duchess cipher undeciphered` -- Desenclos & Lasry 1592, Heidelberg HüB, Exeter "revolutionary
duchess" blog (18th c.), Yale: nothing; (3) distinctive string: `"82 82 52 14 10 85 92" OR "duc de Nevers" "à la duchesse"
chiffre non déchiffré` -- no page carries the number string; (4) title covered by 1-2. Nothing plausible to open.
Blog site searches (shared by NV-01/02/03/09, 3 Oct 2026): `site:ciphermysteries.com Nevers cipher Gonzague` -- no ciphermysteries.com page returned; `site:scienceblogs.de klausis-krypto-kolumne Nevers Gonzague` -- Cipherbrain 2019/01 archive, page/60, a Louis XIV letter post (31 Jan 2019) and "Norbert Biermann solves encrypted letters from the 17th century": none about a Nevers family letter; `site:cryptiana.blogspot.com Nevers` -- no Cryptiana blog page returned; Tomokiyo's own pages read from the local mirror (nevers.htm, bnf4715.htm, league.htm). Recurring hit: Desenclos & Lasry, HistoCrypt, "deciphering a letter from the King of France to the Duke of Nevers (1592)" (dspace.ut.ee cb0c82a2) -- a Henri IV letter, not this one.

## Premise check (NV-INTAKE, 3 Oct 2026)

(a) Folder's own files: new folder; repo grep for "4712" in ciphers/ finds no other folder -- not found.
(b) Other solvers: Tomokiyo prints the numbers and says undeciphered; no apply-key run of the duchess keys on these
numbers in Bourdeau, Aymeloglu or Cabinet Noir -- not found.
(c) Physical neighbours: ff.9, 11, 12 are further letters to the duchess (Tomokiyo, catalogue); f.7 (no.71 pair) and f.13
("Fragment de dépêche en clair et en chiffre", interlinear decipherment of two-digit word codes, "25 appears to read
Paris") per Tomokiyo -- f.13's codes may share a code list; no decipherment of f.10 named. Leaf and facing page **not
viewed** (no image reads in this job).
(d) Recipient side: Henriette de Clèves' papers -- no printed correspondence with a cipher passage located by queries 1-2.

## Key application (brief step 4): blocked, no key material on disk

The brief names "the duchess keys Tomokiyo publishes (no.1, no.2, no.4)". Tomokiyo describes them but does **not print
their tables** (nevers.htm, verbatim): no.1 (fol.1, June 1580) "\"Chifre avec Mad[am]e\". Substitution by figures.
Homophones for vowels. Nulls. Code numbers for names and words: Le Roy, ..."; no.2 (fol.3, October 1584) "\"chifre avec la
Duc[hesse].\" ... Substitution by symbols, letters, and figures. ... The main part consists of listing of names to be
represented by code words. ... A wavy symbol attached to a code word for a person represents his spouse."; no.4 (fol.8,
1585) "\"Chifre avec la Duchesse ma feme en ce voiage des bains de Lu[c]ques\" ... List of words represented by two-digit
figures or figures with an overbar or an underbar). Notes appear to explain use of symbols." No key.tsv for any of the
three exists in the repo (grep of ciphers/, KEY-OFFICES.tsv, KEY-DESIGN.tsv). Transcribing them means reading fr.3995
ff.1, 3, 8 (Gallica ark:/12148/btv1b525085665), an image job this brief forbids. So no reading, no coverage figure and no
judge run: there is nothing to score (the brief's shuffle-judge control needs a reading). Grade counts: none (0 tokens
read). Of the three, no.1 (all-figure substitution with vowel homophones) is the design that fits a numbers-only passage;
no.2 is mostly symbols/letters; no.4 is a word list -- design read from Tomokiyo's descriptions only.

## Intake gate

`python3 tools/intake_gate_check.py fr4712-nevers-duchesse` (NV-INTAKE, 3 Oct 2026):

```
fr4712-nevers-duchesse: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## While waiting

Next step depends on nobody: transcribe fr.3995 f.1 (no.1) and f.8 (no.4) into key.tsv from the Gallica image (line crops
with `tools/iiif_lines.py --ark btv1b525085665`, two blind passes + reconciliation per key = 3 calls x ~USD 1.5, ~USD 9 for
both; no.2 only if both fail), then apply with tools/decode_key.py to `ciphertext.txt` and score with
`tools/judge_plaintext.py` fr16 against 200 shuffles (rank, z). Before that, view the f.10 leaf (near vue 17) once to check
Tomokiyo's 37 numbers and the "♀" sign (~USD 1.5). Expect little power at 37 tokens; a key with full coverage and French
is the only result that would mean anything.

`python3 tools/next_steps.py --wait-only | grep fr4712-nevers-duchesse` (NV-INTAKE, 3 Oct 2026, run about 03:23 UTC by the container clock): no line.

## DUCH-KEY1 (account 1 for LANE-A1, 3 Oct 2026, 09:44-09:55 UTC): leaf located, stopped on a tool denial

- f.10r is **canvas 18, right-hand page** of btv1b9058289m (folio "10" written top right; checked on a 900 px view of
  canvases 18-20, 3 Oct 2026). The NV-INTAKE guess "vues 16-18" holds at 18; Cabinet Noir's f.7r = vue 15 does not give
  f.10 by a fixed offset (canvases are two-page openings; `tools/gallica_folio.py` reports 20 offsets for this ark).
- The cipher sits in native region about x 4000-7500, y 2560-3100 (canvas 7987x5633): three lines, the third embedded
  after "ce laquay ne ma falle", followed by a clear line "et neanmoins il dit ... ". Seen on the iiif_lines debug
  overlay only (no subagent read, no number checked): the figures are written as **unspaced digit runs**, so Tomokiyo's
  word-division into 37 numbers is itself a segmentation, not a transcription of spacing. The non-numeric sign he prints
  "♀" looks on the overlay like a looped/crossed "8"-like sign opening lines 2 and 3; not settled.
- Crops: `images/` holds an iiif_lines run whose region cut the first cipher line at the top
  (region 4100,2750,3300,560); the next run should use `--region 4000,2560,3500,520`.
- Stopped: a cleanup `rm` of that bad run was refused by the session's safety check (common tail: one denial = flag
  and stop). Units (1) number check, (2) fr.3995 f.1 key (canvas f9, label '1r', 4293x6248), (3) scoring: not done.
- Next: rerun the crop at the region above into a fresh `--prefix f10b`, two blind reads of the digit runs with
  `tools/decode_key.py --split-check`-style segmentation left open (the split is part of the key test), then units (2)-(3)
  as briefed; ~USD 6.

## DUCH-KEY1B (account 1 for LANE-A1, 3 Oct 2026, 10:03-10:15 UTC by the container clock): f.10r read, key no.1 transcribed and applied -- non-test

Superseded files: `images/f10_L0*_s*.jpg`, `images/f10_lines_debug.jpg` and
`images/src_ark_12148_btv1b9058289m_f18_4100_2750_3300_560.jpg` are DUCH-KEY1's earlier crop run, whose region cut off
the first cipher line. They are kept as they are (not deleted) and superseded by `images/f10b/`.

**(1) f.10r digits.** Crop command (pasted): `python3 tools/iiif_lines.py --ark btv1b9058289m --canvas 18 --region
4000,2560,3500,520 --out <scratch> --prefix f10c --lines-per-crop 3 --max-width 1800 --overlap 200`. The used crops are in
`images/f10b/`. I read them myself in one Opus vision call plus one zoom on line 1 (21-69). The raw digit strings are in
`ciphertext_f10_digits.tsv`.
- **The digit strings agree with Tomokiyo's 37 numbers on every digit (0 differences in 74+ digits).** One digit is M:
  the 1 of "13" in line 1, which is ligatured to the preceding 0.
- The figures are written unspaced, so Tomokiyo's division is a segmentation and not a transcription. His single "8"
  before "59" sits inside the run "92859". Line 1 has an odd number of digits (33).
- The non-numeric sign that opens lines 2 and 3 is a loop with the cross **above** it. Tomokiyo prints it as the female
  sign, with the cross below.
- Before the cipher a struck-out false start reads "82 82 5? 7 20 +". It is not part of the text, but it repeats the
  opening "82 82".
- The cipher sits inside clear text: "... angoir[?]" before line 1, and "ce laquay ne ma falle" before line 3.

**(2) Key no.1** is on fr.3995 Gallica canvas 10. That leaf is foliated "2", while f.1r (canvas 9) carries only the docket
"Juin 1580". The key is written sideways, so it was read rotated 270.
- Crops (IIIF region + rotation, at native resolution): `images/key_no1/` a1-a3 (the alphabet and the Nulles line) and
  c1-c4 (the code list).
- Two blind passes: A by Opus (this worker), B by a Sonnet subagent. Both are kept as `keys/key_no1_passA.tsv` and
  `keys/key_no1_passB.tsv`; the reconciled key is `keys/key_no1.tsv`.
- **The two passes agree on all 89 codes and on every letter value.** Name spellings differ only in orthography.
- M grades:
  - 45: vous or tous. Pass A read "tous", as Tomokiyo does; pass B read "vous".
  - 90: the last null, cut at the crop edge.
  - 95: Chiverny, read by pass B as "Gievrny".
- **Design:**
  - Letters run 12-58, assigned in descending order a 36-38, b 35 ... z 12, with homophones a 36-38, e 56-58,
    i 46-48, o 42-44 and u 16-18.
  - Nulls: 39 40 50 60-65 70 80 90.
  - Codes: 10, 11, 13-15, 19, 45, 49, 51-55, 59, 66-69, 71-79, 81-89, 91-99.
  - Note: Tomokiyo lists "Monsieur" twice; the key has it at both 69 and 59.

**(3) Score.** The rule was pre-registered in `PREREG_duchkey1b.md` (commit 62c1978b) before any score was computed. The
script is `score_key1.py`; `--check` and `--a1 --check` both print OK. Outputs are in `key1_score.tsv`,
`key1_readings.txt`, `key1_score_A1.tsv` and `key1_readings_A1.txt`.

Main statistic (fr16 4-gram, code names expanded), target vs 200 value-shuffled keys, with its power control:

| segmentation | rank of 201 | z | judge |
|---|---|---|---|
| S1 Tomokiyo | 94 | 0.20 | FAIL (-0.899 vs real_p05 -0.883, null_p99 -1.833) |
| S2 pairs from start | 104 | -0.01 | FAIL |
| S3 offset 1 | 197 | -2.49 | FAIL |
| **Power control** (20 synthetic French texts of 37 tokens, key no.1, 3% digit error) | rank 1 with z>=3 in **0/20** | | |

Amendment A1 was pre-registered after that 0/20 and before any A1 score. Its statistic gives code tokens no letters and
treats them as word breaks. A1 power is also **0/20**: the true key ranks 3-23 of 201 with z of about 1.1-1.8.
Neither statistic can separate key no.1 from a shuffle at 37 tokens. **The result is a non-test (rule 3), not a
negative.**

`tools/judge_plaintext.py specs/fr4712-nevers-duchesse.json --file <S1 reading>` (spec written by this job):
```
FAIL language: score=-0.899, null_p99=-1.833, real_p05=-0.883, real_median=-0.774, mode=both, N=287
ok   words: cover=0.93, min=0.5, real_text_median_cover=0.948
FAIL - fr4712-nevers-duchesse (a PASS is a gate for a verifier, not a reading; rule 10)
```
The language score and the cover above come mostly from the expanded code names. They are not evidence of a reading.

Descriptive only (no gate). Under key no.1, 59-61% of the tokens decode to name codes, against a mean of 49-50% under
the shuffles. The S1 decode is a run of names ("Mareschal de Cosse, Mareschal de Cosse, Reistres, Mons d'O, Mons
d'Arques ...") with isolated letters ("x", "u", "e", "g", "z", "y x t", "q z", "r u", "p") and no letter run of four or
more. It does not look like a no.1 letter. Grades: no reading claimed, so there are 0 H/C/S tokens.

Next step: the run of repeated two-digit words fits Tomokiyo's no.4 better than no.1. No.4 is fol.8, the 1585 key
"avec la Duchesse ma feme en ce voiage des bains de Lucques", described as a "List of words represented by two-digit
figures". Transcribe it the way no.1 was done here: rotate-and-crop with IIIF, two blind passes, reconcile. Then apply it
under S1 and S2. The power control has to be rebuilt for a word-code design, because the letter-based one has no power
at N=37. That is about 3 vision calls, ~USD 6.

## DUCH-KEY4 (account 1 for LANE-A1, 3 Oct 2026, 10:22-10:30 UTC by the container clock): key no.4 does not fit f.10r -- design mismatch, steps 2-3 not run

Brief `.claude/briefs/runs/2026-10-03-acct1-duch-key4.md`. Rule pre-registered in `PREREG_duchkey4.md` (commit fd47ed94)
before any count. Two vision batches (both by this worker, Opus); crops in `images/key_no4/` with `manifest.tsv`.

- **Where no.4 is.** Tomokiyo's "fol.8" is canvas f22 (label 8r). It carries only a docket ("Chifre", with a word above
  it, M). The table itself is **f.9v, canvas f25**. Canvases f23 (8v) and f24 (9r) are blank apart from show-through
  (700 px views).
- **Design, as seen on f.9v.** It is a word list grouped under initial-letter sections, each headed "÷ A ÷" and so on.
  The two-digit codes **restart in each section**:
  - A 11-19, 21-29, 31-39 (Abandonner 11 ... Archiers 39);
  - B 41-49;
  - C 51-59, 61-69, 71-79 (Car 51 ... Croy 79);
  - D 81-88 and, in a second block, 89 (Descouvrir), 91-99;
  - E 11-19, F 21-26 and G 31-39, all written with an **overbar**;
  - I 41-49, 51-53.

  The 8 is written as an "ɑ"-like form. The left note reads, M: "Il fault se servir en ce chifre avec 2 lettres
  premieres ...". The "Advertissement" explains stacked forms such as 59/74 and 74 with a bar. So a code is made unique
  by its bar, and the note may mean the first letters are written too. Not transcribed beyond this (brief step 3 not
  reached).
- **Gate F1 holds.** On every visible column, **no code contains the digit 0**: x0 is skipped in each decade (A has no
  20 or 30, C has no 60 or 70, D has no 90).
- **f.10r cannot be covered.** It has a 0 in every line: line 1 at digits 10 and 18, line 2 at 6 and 14, line 3 at 2.
  Under Tomokiyo's segmentation 5 of the 37 tokens contain a 0 (10, 60, 10, 20, 10), and his "8" is a single digit.
  No segmentation can read these runs wholly as no.4 codes.
- **Gate F2 also holds.** Codes repeat across 2 or 3 sections (11-39 in A and E/F/G; 41-53 in B and I). f.10r carries no
  section letters, and DUCH-KEY1B noted no bars.

**Verdict by the pre-registered rule:** this is a design mismatch, not a negative on a reading. It is also not a
power-tested negative. Rule 3: a power control would have no meaning when the key cannot spell the text. So steps 2
(power control) and 3 (transcription, scoring) were not run. Grades: 0 tokens read, so 0 H, C or S.

Caveat (M):
- The f.10r zeros were read the same way by two readers (DUCH-KEY1B and Tomokiyo). The ɑ-form 8 of this key's hand is
  not the f.10r hand's 8.
- If a 0 were a null or a separator in some other duchess key, that would be a different key, not no.4. The
  Advertissement was not fully read; nothing in the readable part mentions nulls.

Where not found: no table of no.4 in Tomokiyo (description only) or in the solver repositories (NV-INTAKE grep).

Next (Verdict line, 3 Oct 2026; superseded -- see "Next step (FRESH-0914 staleness sweep, 7 Oct 2026)" at the end):
- More ciphertext is the only route to power. DUCH-KEY1B measured 0/20 at N=37 with no.1, the only one of the three
  duchess keys whose code set includes 0-numbers (10, 60).
- ~~Next step: view fr.4712 ff.9, 11 and 12 (Gallica btv1b9058289m, canvases near 17-21) for further cipher passages.~~ Done by DUCH-LEAVES (3 Oct 2026, section below: no figure runs on ff.9, 11 or 12); struck by FRESH-0914, 7 Oct 2026.
- Key no.2 (f.3, mostly symbols) only if figures appear there.

## Leaf census ff.9-12 (DUCH-LEAVES, account-1 worker for LANE-A1, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct1-duch-leaves.md`. Gallica btv1b9058289m canvases f16-f22 viewed at 808 px as one
contact sheet (`images/contact_c16-21_808.jpg`, `images/contact_c22_808.jpg`), then four regional looks at 1000-1400 px
(f.9r; f.9v foot; f.11r; f.13r top, kept as `images/f13r_top_c22_4300_200_3500_2900_1400.jpg`). Per-leaf table in
`ciphertext_more.tsv`. Requests: 11 to gallica.bnf.fr, 1.6 s apart.

- Map: canvases are two-page openings. f17 right = f.9r; f18 left = f.9v, right = f.10r; f19 = f.10v | f.11r, and **f20 is a
  duplicate image of f19**; f21 = f.11v | f.12r (both blank); f22 = f.12v (address "A Ma Duchesse de Nevers", M) | f.13r.
- **No figure runs on ff.9, 11 or 12.** f.9r is a memorandum of questions and answers in clear; f.9v carries only seal blots
  and arithmetic sums at the foot (100 x 24 = 2400, 96 + 24 = 120; partly mirror show-through); f.11r is a 23-line clear
  letter with date numerals only. So no native crop batch and no blind digit read were made (brief: crops only for a leaf
  with figure runs). New tokens: **0**; pooled total stays **37** (f.10r only). The loop-with-cross sign was not seen on any
  of these leaves. Key no.1's re-run is not named: 37 tokens is the length DUCH-KEY1B already measured at power 0/20.
- **Where more material is (not read, outside the brief's leaves).** f.13r, the right page of canvas f22, is a letter in
  clear with about 40 single code numbers set between dots in the text (6 to 93 as glimpsed at 1400 px), most with an
  interlinear gloss above in a second hand (e.g. 25 "Paris", 82 "D. n.", 58 "R" -- all M, one look, not transcribed).
  Its layout differs from f.10r (single dotted codes in prose, not unbroken runs), so the hand and key may differ, and the
  BnF unit "ff.9-12" ends before it. Codes seen there that also occur on f.10r: 10, 12, 21, 25, 56, 82, 92, 93 (8 of
  f.10r's 29 distinct values; M, single glimpse). If the glosses read cleanly, they are period decipherment pairs (grade C
  material for those codes) and the only route this target has found to f.10r: a known-plaintext crib rather than more
  ciphertext for a power control.
- Not done (outside the brief): transcription of f.13r and any leaf after f.13 (f.13v onward, canvas f23+).

## DUCH-F13 (account-1 worker for LANE-A1, 3 Oct 2026, from 10:58 UTC): f.13r glossed codes as a crib for f.10r

Pre-registration `PREREG_duchf13.md` (commit 1d4fcd95, before any f.13r read).

**Hand condition (prereg (c)), recorded about 11:02 UTC by the container clock (commit 893e0375) before `f13_carry.py` was first run.** Side by side: f.10r's crop
`images/f10b/f10c_L01_s1.jpg` and f.13r's line crops. f.10r's clear words ("ce laquay ne ma falle") are a light, small,
fast cursive; f.13r's body is a larger, heavier hand. The decisive sign is the figure 8: f.10r writes it as an open
ɑ-form (its "82 82" reads "ɑ2 ɑ2"), f.13r writes a closed looped 8 in ".82." and ".58.". Layout also differs (f.10r unbroken
digit runs, f.13r single dotted codes in prose). **Judged: not shown to be the same writer (undecided, leaning different).**
So condition (c) is not met and every carried value is graded **M**, not C (`HAND_SAME = None` in `f13_carry.py`).
Date window: both undated, same volume, same addressee -- recorded as unverifiable.

**Crops (pasted commands).** `python3 tools/iiif_lines.py --ark btv1b9058289m --canvas 22 --region 4250,200,3350,2900 --out
<scratch>/f13 --prefix f13 --lines-per-crop 2 --max-width 1800 --overlap 200 --debug` (16 band crops, 16 centres = 15 text
lines + the top gloss). The bands cut the interlinear glosses, so a second cut: `... --prefix f13g --centres
312,476,635,791,968,1131,1308,1474,1619,1772,1960,2157,2337,2523,2698 --lines-per-crop 1 --top-margin 70 --max-width 1750
--overlap 150` (30 per-line crops with the gloss band above). Used crops in `images/f13r/` (manifests
`manifest_f13.json`, `manifest_f13g.json`); `recon_1.jpg`/`recon_2.jpg` are the zoomed gloss tiles of the reconciliation.
Gallica requests: 2.

**Passes.** A (Opus, this worker, per-line crops stacked three to an image) `f13_passA.tsv`; B (Opus subagent, blind,
band crops only) `f13_passB.tsv`; one reconciliation look -> `f13_code_gloss.tsv`.
- **34 code occurrences, and the two passes agree on all 34 code numbers and their lines** (single-digit codes 6, 3, 4, 9, 9).
  Distinct codes: 3 4 6 9 10 11 12 13 21 25 35 36 37 39 40 41 54 56 58 61 82 90 92 93.
- **Glosses at grade H (same gloss in both passes, neither marked illegible): 6 codes** -- 82 "D. n.", 58 "R" (twice),
  21 "Berry", 12 "b. Pal.", 54 "Lorm." (line 15), 35 "ap." (line 10). Everything else is M (`f13_code_gloss.tsv`):
  the most frequent code, **40 (5 occurrences), reads "l. Vill." in pass A and "Lill." in pass B, unresolved on the zoom**;
  25 "Paris" (M: pass B saw only "Pa?"); 93 has two different glosses (line 2 "Pari."/"Pon.", line 13 "Inge?"/"Iuge?");
  54 on line 5 reads "Lux-?" against line 15's "Lorm." (only the line-15 one is H).
- No reading of the glosses' referents is claimed ("D. n.", "b. Pal." are left as written).

**Carry to f.10r** (`f13_carry.py`, `--check` OK; `f13_carry.tsv`, `f13_carry_stats.tsv`), PREREG_duchf13.md:

| segmentation | f.10r tokens | glossed (coverage) | graded C | p (random 6-code sets from 1-99, 1000) |
|---|---|---|---|---|
| S1 Tomokiyo | 37 | 6 (82 82, 21 21, 12 12) | 0 | 0.029 |
| S2 pairs from start | 36 | 6 (same tokens) | 0 | 0.035 |
| S3 offset 1 | 34 | 6 (21 x3, 12 x2, 58) | 0 | 0.021 |

- All six carried values are **M**, not C: the hand condition (c) failed (recorded above, before the run).
- The briefed rotated-gloss control **cannot differ** on coverage (which tokens get *a* gloss does not depend on *which*
  gloss), so it is reported as a non-test (rule 3), as the prereg said before the run. The control that can differ
  (random code sets) puts f.10r's overlap with f.13r's six H codes at p 0.02-0.04. That p is mildly anti-conservative,
  because the null draws single digits 1-9, which can match only f.10r's one single-digit token. Either way it says only
  that f.10r's numbers sit on f.13r's codes more than chance would; it reads nothing.
- **Key family (can differ under rotation):** 0 of 6 f.13r H glosses agree with key no.1 for the same number (no.1 has 82
  Mareschal de Cosse, 21 x, 12 z, 58 e, 35 b, 54 Armee). f.13r's code list is **not key no.1**; on 25 (Paris vs q) and 40
  (a name vs a null) the M glosses disagree with no.1 too.
- **Gate** (p <= 0.05 AND >= 3 C tokens under S1): **not met** (0 C). No crib for f.10r is licensed. The six M look-ups are
  not a reading: "82 82" = "D. n. D. n." opening f.10r is what an M carry *would* give, and it is recorded as a lookup only.

Remaining for this route: a third reader on the 40 gloss (V vs L) and on the 93 conflict, and a hand comparison by a
person (the owner's eye or a palaeographer) to settle condition (c); if (c) passes, the six carries become C and the gate
is met on S1 (6 >= 3, p 0.029). Any leaf after f.13 (f.13v onward, canvas f23+) is still unviewed.

## Owner eye check, ASKS 113 (5 Oct 2026 04:01 UTC)

Shown a side-by-side of f.10r line 1 (three crops, f10b/f10c_L01_s1-3) and f.13r lines 1-4 (f13r/f13g_L01-L04_s1), the owner
answered: **"I think the same"** (same writer for f.10r and f.13r). Recorded as the owner's judgement at moderate confidence
("I think"), against our own earlier "not shown, leaning different" (the 8 written as an open form on f.10r vs a closed loop on
f.13r). Per ASKS 113's pre-registered rule, a "same" answer carries f.13r's six H glosses (82 "D. n.", 21 "Berry", 12 "b. Pal."
...) to the matching tokens of f.10r at grade C. Not yet applied: the next worker on this target applies them through
key.tsv/exceptions with decode_key.py --check, notes the conflicting 8-shape evidence beside each carried value, and leaves the
"Vill."/"Lill." gloss over code 40 open (not asked this time).

## R11A-F4712 (account 1 for LANE LANE-RUN11-account-1, 6 Oct 2026, 13:48-14:0x UTC by date -u): blind digit-hand test -- NON-TEST

Pre-registered `PREREG_duchhand.md` (commit e8cea837, before any scored call; deviation commit 63e7eef3). One blind Sonnet call
compared digit shapes in R = f.10r lines 1-2 against three shuffled candidates: P = f.10r lines 3-4 (same writer by construction),
T = f.13r lines 1, 4, 7 (codes 6 82 58 / 25 35 / 21 40), N = key no.4 table, fr.3995 f.9v column A (a presumed different hand).
N came from the on-disk DUCH-KEY4 sheet, upscaled 1/0.55, because Gallica answered 503 to the native crop (1 request, not retried).

| candidate | digits seen | score (0-10, same writer as R) |
|---|---|---|
| P f.10r L3-4 (positive) | 3 | 4 |
| T f.13r | 5 | 5 |
| N key no.4 table (negative) | ~30 | 4 |

The calibration gate (a) fails (P 4 < 6, P - N = 0): the scorer cannot separate f.10r from a different hand at this sample size, so
this is a **non-test**, not evidence for or against the same writer. Cause (our panel design, not the scorer): the f.10r L3-L4 crops
carry only about 3 digits, and f.13r gives 5 digits with no 8 at all, so the decisive open-vs-looped 8 never entered the comparison.
The subagent's notes call T's 2 "only partially" like R's. Nothing about the hand is settled here. The open evidence stays as it was:
the owner's eye says "I think the same" (ASKS 113, 5 Oct), and DUCH-F13's look says "leaning different" (the 8-form).
Next (not run, outside this brief): the owner's ASKS 113 answer already licenses the C carry under ASKS 113's own pre-registered
rule; applying it through key.tsv + decode_key.py --check, with the 8-form conflict noted per value, is the step the 5 Oct section
names (~USD 1.5). A machine digit test would need digit-rich panels: f.10r has about 30 digits in L1-2, but f.13r has only about 34
codes in all, so the power stays low.
Requests: gallica.bnf.fr 1 (503). Vision: 1 Sonnet subagent call.

## Next step (FRESH-0914 staleness sweep, 7 Oct 2026)

The 3 Oct leaf-census step (ff.9, 11, 12) was done by DUCH-LEAVES (no figure runs) and the blind hand test by R11A-F4712 (a
NON-TEST, 6 Oct 2026); the live step is the one the top-of-file Verdict names. next: apply the owner's same-writer judgement
(ASKS 113, 5 Oct 2026, "I think the same") to the 6 f.13r-glossed carries as C per that row's rule, re-run the decode with
--check, ~$1.5. Who acts: agent.

## D2-F4712 (account 2 for LANE DEFAULT-account-2-20261008-0710, 8 Oct 2026, 07:21-07:3x UTC by date -u): ASKS 113 applied -- six carries at C

Applied exactly what PREREG_duchf13.md (commit 1d4fcd95) and ASKS row 113 pre-registered; no new gate. `f13_carry.py` now has
`HAND_SAME = True` (with the 3 Oct `None` and the reason for the change in a comment); `python3 f13_carry.py` rewrote
`f13_carry.tsv` / `f13_carry_stats.tsv`, and `python3 f13_carry.py --check` answers OK. The folder has no key.tsv/decode.json,
so the folder's own carry script is the rule-7 decode for these tokens.

Same-writer evidence, side by side (prereg condition (c)); the carry follows the person's judgement, the other two rows stay on record:

| source | date | judgement | basis |
|---|---|---|---|
| owner's eye check, ASKS 113 | 5 Oct 2026 | "I think the same" (moderate confidence) | side-by-side f10c_L01_s1-3 vs f13g_L01-L04_s1 |
| DUCH-F13 (our look) | 3 Oct 2026 | not shown, leaning different | 8 written as an open form on f.10r ("82 82"), a closed loop on f.13r (".82.", ".58.") |
| R11A-F4712 blind digit test | 6 Oct 2026 | NON-TEST (positive control 4/10 = negative 4/10) | too few digits; no 8 on the f.13r panels |

The six carried tokens (S1, Tomokiyo's segmentation), each graded C; caveat on every one: the open-8 vs looped-8 conflict above.

| f.10r idx (S1) | token | f.13r gloss (H on f.13r) | grade |
|---|---|---|---|
| 1 | 82 | D. n. | C |
| 2 | 82 | D. n. | C |
| 8 | 21 | Berry | C |
| 22 | 12 | b. Pal. | C |
| 25 | 21 | Berry | C |
| 30 | 12 | b. Pal. | C |

S2 gives the same six tokens (idx 1, 2, 8, 21, 24, 29); S3 (offset 1) gives 21 x3, 12 x2 and 58 "R" (six C).
Rule 4 counts for f.10r under S1 (37 tokens): **H 0, C 6, S 0, M 0, I 0; 31 unread** (16% of tokens at C). No H or C letter-level
reading exists; this is a crib lookup, not a reading of the passage: "D. n.", "Berry", "b. Pal." are left as written on f.13r
and no referent is claimed. Pre-registered gate (stat 2 p <= 0.05 AND >= 3 C under S1): **met** (p 0.029, 6 C). What the
gate licenses (prereg): f.10r gets a crib at these six positions; nothing beyond the glossed tokens.
Stat 3 unchanged: 0/6 f.13r H glosses agree with key no.1 (rotation p 1.000) -- f.13r's list is not key no.1.
Code 40's gloss ("Vill."/"Lill.") is still M on f.13r and does not occur on f.10r under S1, so it does not affect this carry.
No AUDIT.md exists for this target, so no audited reading changed; the move open -> partial is flagged in ROOM for a verifier.
Requests: none (no network). Vision calls: 0.

## Remaining gaps (D2-F4712, 8 Oct 2026)
Read so far: 6 of 37 f.10r tokens at C under S1 (16%), f13_carry.tsv; 31 tokens unread
- f.10r tokens outside f.13r's H-glossed codes (31 of 37) - blocker: no-key-material; key no.1 is a non-test at 37 tokens (DUCH-KEY1B), key no.4 cannot cover f.10r (DUCH-KEY4), f.13r's M glosses do not reach them; next: view the leaves after f.13 (f.13v onward, canvas 23+) for another glossed or deciphered sibling, ~$2
- same-writer basis of the six C carries - blocker: not-attempted; one person's eye vs our 8-form reading, the machine digit test was a NON-TEST; next: a digit-rich f.13r/f.10r comparison or a palaeographer's look, ~$2
- f.13r code 40 gloss (Vill. vs Lill.) and code 93 conflict - blocker: not-attempted; neither occurs on f.10r under S1, so they do not limit this letter; next: a third reader on recon_1.jpg tiles 40a/40b, ~$1.5

## Escalation (D2-F4712, 8 Oct 2026)
- [ ] siblings: leaves after f.13 (f.13v onward, canvas 23+) are unviewed; planned: a leaf census like DUCH-LEAVES
- [x] clear-pages: ff.9, 11, 12 checked, no cipher (DUCH-LEAVES); f.13r's glossed codes used as the crib (DUCH-F13, this job)
- [x] known-keys: key no.1 applied (non-test, DUCH-KEY1B), key no.4 tried (design mismatch, DUCH-KEY4)
- [x] print: Gomberville's Mémoires (1665) full-text searched (NV-INTAKE, 3 Oct 2026), no cipher passage printed
- [n/a] key-rebuild: 37 tokens is far below any cryptanalytic length for a code of this size
- [x] image-check: f.10r read from crops (DUCH-KEY1B), f.13r two blind passes agree on all 34 codes (DUCH-F13)
- [x] retry: hand question retried by a blind digit test (R11A-F4712, NON-TEST) and settled by the person's look (ASKS 113)
Verdict: keep going: 2 internal gaps; cheapest next: leaf census of f.13v onward for a glossed sibling, ~$2 (the code 40 third read, ~$1.5, does not touch f.10r)

## D2V-F4712 AUDIT 1 (verifier, account 2, 8 Oct 2026)
AUDIT.md "## AUDIT 1 (D2V-F4712)": the six f.10r C carries are confirmed as pre-registered (PREREG_duchf13.md 1d4fcd95c, 3 Oct, two
days before the ASKS 113 answer) and reproduce (`f13_carry.py --check` OK); gate p re-computed 0.023-0.038 under three nulls. Class
**N3, depth D1** ("fragments read"; class without a reading, not counted); f.13r's gloss table N0 (period gloss on the leaf). Key
source period. Correction: the BnF 1895 catalogue dates f.10 "i octobre 1592", monogram signature (note under the title). No
reading changed. SO-F4712-F10 queued. Next for audit 2: Boltanski (2006) on fr.4712 f°10-13, Semantic Scholar/Persée/HAL, one crop of
the f.10 date line.

## V1-F4712 AUDIT 2 (second adversarial verifier, account 3, 8 Oct 2026)
AUDIT.md "## AUDIT 2 (second adversarial, V1-F4712)": item A stays **N3, D1**; G3 run (19 Google Books queries on the six tokens'
context, plus IA, OpenAlex, S2, HAL, Persée). No prior decipherment of f.10r located. Context lead only: royal letters of
9 Oct 1592 moved Bourges's (Berry's) finance bureau and mint to Nevers -- same month as f.10, not a printed version of it.
Known-key gap: f.35 of this volume (1592) was solved by G. Lasry in 2022 (Tomokiyo GL.htm), but its key is a one-symbol letter
substitution, not a two-digit code -- ruled out by form. Key no.71 (f.7 of this volume, figures for names and words) was never
tried on f.10r.
- [ ] known-keys (added by V1-F4712): key no.71 (fr.3995 Nevers collection; f.7 of this volume, Cabinet Noir's key) on f.10r's 37 numbers,
  with a matched control; ~$2. f.35 (Lasry 2022) ruled out by design.

## F4712-40 (worker for LANE DEFAULT-A1-0540, account 1, 11 Oct 2026, 06:17-06:2x UTC by date -u): f.13r code 40 gloss, third blind read -- NON-TEST

Brief: `.claude/briefs/runs/2026-10-11-acct1-default-0540-jobs.md` "F4712-40". Disk only (0 requests). Pre-registered
`PREREG-F4712-40.md` (commit 1dcd8b4b8, on origin/main before the read). Tiles cut with `tools/iiif_lines.py --image
images/f13r/recon_1.jpg --region 620,1215,320,120 --centres 60 --lines-per-crop 1 --top-margin 60 --bottom-margin 60 --prefix t1
--out images/f13r/g40` (t2: recon_1 1080,1220,330,110 centre 55; t3: recon_2 640,950,380,120; t4: recon_1 600,315,400,120),
committed in `images/f13r/g40/` (manifest.json). t1 = code 21 (decoy, H "Berry"), t2 = code 40 tile 40b, t3 = code 54 line 15
(decoy, H "Lorm."), t4 = code 40 tile 40a. One blind Sonnet subagent call, told only "four abbreviated words ... French hand of
about 1592; transcribe each letter by letter"; no code numbers, no earlier reading, no candidate letters.

Result (`g40_read.tsv`): t1 "Bery" (it added "most plausible: Berry"), t3 "Lasmi-": **both decoys miss** under the
pre-registered exact-letter rule, so the gate fails and **the read is a NON-TEST**; no vote counted. For the record only: the
reader gave **R** as the first letter of the main word on both code-40 tiles (t2 "Ril.", t4 "l Rill."), naming V and L only as
alternatives, so even a passed gate would have given a TIE (neither V nor L). Code 40's gloss stays **M** ("Vill." pass A /
"Lill." pass B); no key edit, so no decode_key run was needed.
Per CLAUDE.md rule 3's third-attempt clause (two Opus passes split, this third model read is a non-test), the **model-reader
instrument is [retired] for this gloss**; the gloss goes to the owner's eye as ASKS 162 (backlog, never blocking).
Code 93 (report only, not read here): two different glosses on the same code, line 2 "Pari."/"Pon." and line 13
"Inge?"/"Iuge?" (DUCH-F13, `f13_code_gloss.tsv`); an unresolved data conflict on f.13r, M, and code 93 does not occur on
f.10r under S1. Neither code 40 nor code 93 limits the f.10r carry.

## Remaining gaps (F4712-40, 11 Oct 2026)
Read so far: 6 of 37 f.10r tokens at C under S1 (16%), f13_carry.tsv; 31 tokens unread
- f.10r tokens outside f.13r's H-glossed codes (31 of 37) - blocker: no-key-material; key no.1 is a non-test at 37 tokens (DUCH-KEY1B), key no.4 cannot cover f.10r (DUCH-KEY4), f.13r's M glosses do not reach them; key no.71 (V1-F4712) and the leaves after f.13 are the untried routes (Escalation siblings, known-keys)
- same-writer basis of the six C carries - blocker: not-attempted; one person's eye vs our 8-form reading, the machine digit test was a NON-TEST; next: a digit-rich f.13r/f.10r comparison or a palaeographer's look, ~$2
- f.13r code 40 gloss (Vill. vs Lill.) and code 93 conflict - blocker: waiting-on ASKS 162 (the owner's eye on images/f13r/g40 t2/t4 and recon_1/recon_2 tiles 93a/93b); model-reader instrument retired for this gloss (F4712-40 NON-TEST, g40_read.tsv); neither code occurs on f.10r under S1

## Escalation (F4712-40, 11 Oct 2026)
- [ ] siblings: leaves after f.13 (f.13v onward, canvas 23+) are unviewed; planned: a leaf census like DUCH-LEAVES
- [x] clear-pages: ff.9, 11, 12 checked, no cipher (DUCH-LEAVES); f.13r's glossed codes used as the crib (DUCH-F13)
- [ ] known-keys: key no.1 applied (non-test, DUCH-KEY1B), key no.4 tried (design mismatch, DUCH-KEY4); planned: key no.71 (fr.3995; f.7 of this volume) on f.10r's 37 numbers with a matched control, ~$2 (V1-F4712)
- [x] print: Gomberville's Mémoires (1665) full-text searched (NV-INTAKE, 3 Oct 2026), no cipher passage printed
- [n/a] key-rebuild: 37 tokens is far below any cryptanalytic length for a code of this size
- [x] image-check: f.10r read from crops (DUCH-KEY1B), f.13r two blind passes agree on all 34 codes (DUCH-F13); code 40 gloss third model read a NON-TEST (F4712-40), model reader retired for that gloss, owner's eye ASKS 162
- [x] retry: hand question retried by a blind digit test (R11A-F4712, NON-TEST) and settled by the person's look (ASKS 113)
Verdict: keep going: 1 internal gaps; cheapest next: leaf census of f.13v onward for a glossed sibling, ~$2 (or key no.71 on f.10r with a matched control, ~$2)

## F4712-K71 (worker for LANE DEFAULT-A1-1840, account 1, 11 Oct 2026, 18:56-19:0x UTC by date -u): key no.71 on f.10r -- control-backed negative

Brief: `.claude/briefs/runs/2026-10-11-acct1-default-1840-jobs.md` "F4712-K71" (the V1-F4712 known-keys rung). Disk only, 0 requests.
Prior work: `tools/prior_work.py fr4712-nevers-duchesse --item-spec 'shelfmark=BnF fr.4712;folio=10r;canvas=18;date=1592-10-01;...'
--step-type decode --offline` exit 2: the one KNOWN row is a false hit (sources/cryptiana/web/habsburg.htm l.364, a Habsburg two-part
code, not this leaf); LEADs are this folder's own done image-check and V1-F4712's audit, neither applied no.71; check 1 (own work):
no.71 never applied to f.10r (NOTES.md "V1-F4712 AUDIT 2"); checks 3-4 by the intake and both audits (Tomokiyo "undeciphered",
Gomberville 1665 not printed); check 5 after decode: no reading claimed, nothing to search.
Pre-registered `PREREG-F4712-K71.md` (commit 990de8d8e, on origin/main before any score).

- **Key copy.** `keys/key_no71.tsv`: the 26 letter rows of `ciphers/birago-fr3252-1571-72/keys/key_fr3995_no71_f133r.tsv` (read only)
  plus 44 dotted-word / overlined-person rows read by this worker from the same native crop `read_f133r.jpg` (one reader; the
  18-51 and 60-91 word codes, town codes and the right-hand person codes are cut or off the crop, so unread). The alphabet strip ends
  with a non-numeric sign, a loop with a cross **above** it, under a curled header (z or &, not settled; M): the same shape as
  f.10r's line-opening sign (DUCH-KEY1B). A shape match only.
- **Marks.** f.10r's figures (images/f10b/f10c_L01_s1-s2) show no dot or overline over any code at this crop's resolution; under no.71
  an unmarked figure is a letter.
- **Results** (`k71_decode.py`, `--check` OK; `k71_score.tsv`, `k71_decode.tsv`):

| statistic | target | matched control | null / power | gate |
|---|---|---|---|---|
| D: S1 numbers on no.71 letter codes (of 37) | **12** | C1 (no.71, read word list) mean 36.0, p01 33; C2 (89 word codes) mean 32.7, p05 29, p01 27 | N0 uniform 8-99 mean 10.2, p95 15 | **INCONSISTENT** (12 < 27 and 29 > 15) |
| R: fr16 4-gram of the decode vs 200 value-shuffled keys | rank 173 of 201, z -0.97 | power: 20/20 synthetic no.71 texts rank 1 with z >= 3 | -- | **NO SIGNAL** (power passed) |

  Both controls can differ from the target on their statistic (rule 3) and both did. f.10r's letter-code share sits with uniform
  noise, far below any no.71 text with its marks dropped, and the decode scores worse than most shuffled keys. **Key no.71 does not
  read f.10r as an unmarked letter text** -- conditional on Tomokiyo's S1 division (digits checked on the leaf) and on the crops
  showing no marks.
- Per token (all M, PREREG grading rule): 12 tokens on letter codes, 13 on word/person codes read on the crop (si, ce, quant, car /
  Royne de Navarre, de, amis, Roy, reistres, bon / Royne mere, dit; each needs a mark the leaf lacks), **12 on unread word/person
  codes: 82 82 21 59 31 72 69 21 22 19 81 26** (positions 1 2 8 17 18 19 23 25 26 31 36 37).
- Descriptive: f.13r's H glosses vs no.71 on the three shared read codes -- 12 "b. Pal." vs bon / Royne mere, 54 "Lorm." vs temps,
  58 "R" vs argent: **0/3 agree**, so f.13r's code list is not no.71 either.
- Not excluded: an all-code text (every figure a dotted word or overlined name, marks omitted or too faint for this crop). That
  reading would need the unread word columns and a native-resolution look at the figures for dots/overlines.
Requests: none. Vision: five looks at on-disk images (the key crop, two f.10r strips, two zooms of the key strip end), no subagent.

## Remaining gaps (F4712-K71, 11 Oct 2026)
Read so far: 6 of 37 f.10r tokens at C under S1 (16%), f13_carry.tsv; 31 tokens unread
- f.10r tokens outside f.13r's H-glossed codes (31 of 37) - blocker: no-key-material; key no.1 is a non-test at 37 tokens (DUCH-KEY1B), key no.4 cannot cover f.10r (DUCH-KEY4), key no.71 is a control-backed negative as an unmarked letter text (F4712-K71); the leaves after f.13 are the untried route (Escalation siblings); next: leaf census of f.13v onward, ~$2 (Gallica, waiting on the host)
- key no.71 as an all-code text (dots/overlines too faint at 1800 px) - blocker: not-attempted; needs the no.71 word columns 18-51/60-91 read and one native-resolution look at f.10r's figures for marks; next: native crops of fr.3995 f.133r word columns and f.10r canvas 18 when Gallica answers, ~$2
- same-writer basis of the six C carries - blocker: not-attempted; one person's eye vs our 8-form reading, the machine digit test was a NON-TEST; next: a digit-rich f.13r/f.10r comparison or a palaeographer's look, ~$2
- f.13r code 40 gloss (Vill. vs Lill.) and code 93 conflict - blocker: waiting-on ASKS 162 (the owner's eye on images/f13r/g40 t2/t4 and recon_1/recon_2 tiles 93a/93b); model-reader instrument retired for this gloss (F4712-40 NON-TEST, g40_read.tsv); neither code occurs on f.10r under S1

## Escalation (F4712-K71, 11 Oct 2026)
- [ ] siblings: leaves after f.13 (f.13v onward, canvas 23+) are unviewed; planned: a leaf census like DUCH-LEAVES
- [x] clear-pages: ff.9, 11, 12 checked, no cipher (DUCH-LEAVES); f.13r's glossed codes used as the crib (DUCH-F13)
- [x] known-keys: key no.1 applied (non-test, DUCH-KEY1B), key no.4 tried (design mismatch, DUCH-KEY4), key no.71 applied with matched controls (control-backed negative as a letter text, F4712-K71; all-code reading kept as a gap)
- [x] print: Gomberville's Mémoires (1665) full-text searched (NV-INTAKE, 3 Oct 2026), no cipher passage printed
- [n/a] key-rebuild: 37 tokens is far below any cryptanalytic length for a code of this size
- [x] image-check: f.10r read from crops (DUCH-KEY1B), f.13r two blind passes agree on all 34 codes (DUCH-F13); code 40 gloss third model read a NON-TEST (F4712-40), model reader retired for that gloss, owner's eye ASKS 162
- [x] retry: hand question retried by a blind digit test (R11A-F4712, NON-TEST) and settled by the person's look (ASKS 113)
Verdict: keep going: 2 internal gaps; cheapest next: leaf census of f.13v onward for a glossed sibling, ~$2 (Gallica 403 at 18:5x UTC 11 Oct; or the no.71 all-code check with native crops, ~$2)

## F4712-CENSUS (worker for LANE DEFAULT-A1-0640, owner account, 13 Oct 2026, 06:52-07:2x UTC by date -u): leaf census f.13v-f.24r -- no cipher, no glossed sibling
Brief `.claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md` "### F4712-CENSUS". Prior work: `tools/prior_work.py fr4712-nevers-duchesse
--item-spec 'shelfmark=BnF fr.4712;folio=13v-24;...' --step-type lookup --fetch` exit 4 on five own-work LEADs (DUCH-LEAVES/DUCH-F13 covered
ff.9-13r only; own claim), all recorded CLEAR in prior-work.tsv; solver caches CLEAR; aymeloglu cache and editions UNCHECKED-NET (generic).
Tomokiyo (nevers.htm, BnF fr.4712) lists only f.7, ff.9-12, f.13 and f.35 (a letter to Pasquier, 1592, read by G. Lasry in 2022) in this
volume -- nothing between f.13 and f.35.
Host: openapi.bnf.fr IIIF v3 (ark btv1b9058289m), 14 requests, all HTTP 200: canvases f23-f34 at width 600, then f25 and f26 at width 1600.
Images in `images/census/`, entries under `census_f13v_on` in images/manifest.json. No transcription, no subagent call.
- Map: canvas = two-page opening, foliation visible top right: f23 = f.13v | f.14r ... f32 = f.22v | f.23r, **f33 duplicates f32**,
  f34 = f.23v | f.24r. So the twelve canvases cover f.13v-f.24r.
- Per leaf in `leaves_f13v_on.tsv`. **No figure runs, no dotted codes, no interlinear code glosses on any leaf f.13v-f.24r** at 600 px; the
  densest small-hand letter (f.16r-17r) was re-checked at 1600 px: clear French prose, one caret insertion ("Montigny", a correction).
  Contents: a formal letter in clear (f.14r-v); a memorandum (f.15r-v); a letter in clear (f.16r-17r, postscript, dated "... Juing", M);
  a letter (f.18r); blank or faint f.18v-19r; an address on f.19v ("Monsieur mon frere ... Duc de Nevers", M, one look); a dense letter
  (f.20r-21v); "Articles du sieur de ..." (f.22r); f.22v two lines; blanks f.23r, f.23v (docket strip); a memorandum f.24r.
- Hand like f.10r/f.13r: not settled at 600 px for most leaves ("unsure" in the TSV); f.14r and f.22r are clearly other formal hands.
- Result: the sibling route of the Escalation is closed for f.13v-f.24r: no glossed sibling in the f.10r figure system there. New tokens 0.
- Not done (outside the brief): canvas 35+ (f.24v onward; f.35 is Tomokiyo's Pasquier letter, a different correspondent); a native look at
  the f.17v sideways endorsement and the f.23v docket strip (may name recipients; not cipher).

## Remaining gaps (F4712-CENSUS, 13 Oct 2026)
Read so far: 6 of 37 f.10r tokens at C under S1 (16%), f13_carry.tsv; 31 tokens unread
- f.10r tokens outside f.13r's H-glossed codes (31 of 37) - blocker: no-key-material; key no.1 is a non-test at 37 tokens (DUCH-KEY1B), key no.4 cannot cover f.10r (DUCH-KEY4), key no.71 is a control-backed negative as an unmarked letter text (F4712-K71); ff.13v-24r carry no cipher (F4712-CENSUS); next: leaf census of canvas 35+ (f.24v to the volume's end, ~108 canvases, 600 px, two contact sheets per 12 canvases), ~$2 per 12 canvases via openapi.bnf.fr
- key no.71 as an all-code text (dots/overlines too faint at 1800 px) - blocker: not-attempted; needs the no.71 word columns 18-51/60-91 read and one native-resolution look at f.10r's figures for marks; next: native crops of fr.3995 f.133r word columns and f.10r canvas 18 via openapi.bnf.fr, ~$2
- same-writer basis of the six C carries - blocker: not-attempted; one person's eye vs our 8-form reading, the machine digit test was a NON-TEST; next: a digit-rich f.13r/f.10r comparison or a palaeographer's look, ~$2
- f.13r code 40 gloss (Vill. vs Lill.) and code 93 conflict - blocker: waiting-on ASKS 162 (the owner's eye on images/f13r/g40 t2/t4 and recon_1/recon_2 tiles 93a/93b); model-reader instrument retired for this gloss (F4712-40 NON-TEST, g40_read.tsv); neither code occurs on f.10r under S1

## Escalation (F4712-CENSUS, 13 Oct 2026)
- [ ] siblings: ff.13v-24r censused, no cipher (F4712-CENSUS); canvas 35+ (f.24v onward) unviewed; planned: same census, 12 canvases per job
- [x] clear-pages: ff.9, 11, 12 checked, no cipher (DUCH-LEAVES); f.13r's glossed codes used as the crib (DUCH-F13); ff.13v-24r clear (F4712-CENSUS)
- [x] known-keys: key no.1 applied (non-test, DUCH-KEY1B), key no.4 tried (design mismatch, DUCH-KEY4), key no.71 applied with matched controls (control-backed negative as a letter text, F4712-K71; all-code reading kept as a gap)
- [x] print: Gomberville's Mémoires (1665) full-text searched (NV-INTAKE, 3 Oct 2026), no cipher passage printed
- [n/a] key-rebuild: 37 tokens is far below any cryptanalytic length for a code of this size
- [x] image-check: f.10r read from crops (DUCH-KEY1B), f.13r two blind passes agree on all 34 codes (DUCH-F13); code 40 gloss third model read a NON-TEST (F4712-40), model reader retired for that gloss, owner's eye ASKS 162
- [x] retry: hand question retried by a blind digit test (R11A-F4712, NON-TEST) and settled by the person's look (ASKS 113)
Verdict: keep going: 2 internal gaps and the sibling census; cheapest next: census of canvas 35-46 (f.24v onward) at 600 px via openapi.bnf.fr, ~$2, or the no.71 all-code check with native crops, ~$2

## F4712-71 (worker for LANE DEFAULT-A1-0640, owner account, 13 Oct 2026, 07:39-07:5x UTC by date -u): census c35-38 + c46; key no.71 all-code check -- control-backed negative
Brief `.claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md` "### F4712-71". Prior work: `tools/prior_work.py fr4712-nevers-duchesse
--item-spec 'shelfmark=BnF fr.4712;folio=24v-35;canvas=35-46;date=1592-10-01' --step-type lookup --offline` exit 4 on one own-work LEAD
(the ff.9-12 clear-pages line; recorded CLEAR, canvas 35+ never viewed); Tomokiyo CONTEXT rows name f.35 (Pasquier letter, 1592) only;
solver caches CLEAR; aymeloglu cache and editions UNCHECKED-NET (generic). Check 5 after decode: no reading claimed, nothing to search.
Host: openapi.bnf.fr IIIF v3, **17 requests, all HTTP 200**: 12 overviews btv1b9058289m f35-f46 at width 600, of which **11 were lost**
(a shell-variable error in my fetch loop wrote every file to one name; only f46 survived), 1 native region btv1b525085665 f256
600,4250,3700,1450 (fr.3995 f.133r word columns), 4 re-fetches of f35-f38. f39-f45 stay unviewed: the 18-request budget was spent.

**Unit 1, census.** c35 = f.24v|25r ... c38 = f.27v|28r (foliation top right); c46 = f.35v|36r. Per leaf in `leaves_f13v_on.tsv`
(appended). ff.24v-28r: clear prose and blanks only, no figure runs, no dots, no interlinear gloss at 600 px. f.35v carries a dense
cipher letter in letters/signs with an address "A Monsieur / Monsieur Pasquier ... des finances" (M): Tomokiyo's f.35 (read by G. Lasry,
2022, per nevers.htm), a letter/sign cipher at this size, not the f.10r figure system. No glossed sibling found; ff.28v-35r unviewed.

**Unit 2, key no.71 as an all-code text.**
- Key: no.71's **Motz** list is now complete, codes 11-99 (`keys/key_no71.tsv`, 18-51 and 59-91 added): crops `images/k71/wc_L01-L10.jpg`
  cut by `python3 tools/iiif_lines.py --image ciphers/fr4712-nevers-duchesse/images/k71/wc_rot.jpg --out .../images/k71 --prefix wc
  --lines-per-crop 4 --debug` ("region 1450x3700, 38 lines, 10 bands x 1 segments; pitch 70"; overlay checked), one blind Sonnet read
  against my own eye read of the overlay: 0 code disagreements; 28 luy, 29 son, 36 n'a, 86 leuee|lence M. The key reuses the same figures
  in other dotted columns (Villes 11-48, Provinces, Cavallerye 73-100); the test uses the Motz list only.
- Marks: at native resolution (images/f10b/f10c_L01_s1-s2; images/k71/f10_native_left/right.jpg, autocontrast halves of the on-disk
  native f18 crop, no request) **no dot or overline stands over any of the 37 figures**; the only mark is the cross over the loop sign.
  The F4712-K71 gap called these crops "1800 px"; they are native-resolution segments 1800 px wide, so the earlier look was already native.
- PREREG-F4712-71.md (commit a795a1944, on origin/main before any score). `k71_allcode.py` (`--check` OK): `k71_allcode_score.tsv`,
  `k71_allcode_decode.tsv`.

| statistic | target | power P (20 held-out fr16 all-code windows, N=37) | false-positive F (20 uniform code runs) | gate |
|---|---|---|---|---|
| W: word-bigram score of the Motz decode, rank vs 200 permuted Motz keys | **rank 86 of 201, z 0.25** | 20/20 at rank 1 | 1/20 at rank <= 10 | **NO SIGNAL** (P >= 10, F <= 3) |

  The controls can differ from the target on W (word order changes under every permutation) and did, in opposite directions.
  **Key no.71's Motz list does not read f.10r as an all-code text**, conditional on S1, on the Motz column being the one used, and on
  the language model being a filtered fr16 stream. Together with F4712-K71 (letter text) and the leaf's missing marks, no.71 is not
  f.10r's key in either reading.
- Decode (all M, PREREG grading): "huguenotz huguenotz si ce [Royne mere] lettre quant fort artillerye car de si faict amis quant [Roy]
  armee / me escrit [Royne mere] femme bon dissimule est fort je recherche lettre la bon et qu'il / [Royne mere] il dit garnison le".
  Not a reading. f.13r H glosses vs the Motz values: 82 "D. n." vs huguenotz, 21 "Berry" vs fort, 12 "b. Pal." vs bon: 0/3.
Vision: 1 Sonnet subagent call (word columns); my own looks: c46, c35-38 contact sheet, f.133r overview and crop overlay, f.10r native.

## Remaining gaps (F4712-71, 13 Oct 2026)
Read so far: 6 of 37 f.10r tokens at C under S1 (16%), f13_carry.tsv; 31 tokens unread
- f.10r tokens outside f.13r's H-glossed codes (31 of 37) - blocker: no-key-material; key no.1 is a non-test at 37 tokens (DUCH-KEY1B), key no.4 cannot cover f.10r (DUCH-KEY4), key no.71 is a control-backed negative both as an unmarked letter text (F4712-K71) and as an all-code Motz text (F4712-71); ff.13v-28r carry no cipher (F4712-CENSUS, F4712-71); next: census of canvases 39-45 (ff.28v-35r, 7 requests at 600 px) and 47+ (f.36v onward), ~$1.5 per 12 canvases via openapi.bnf.fr
- same-writer basis of the six C carries - blocker: not-attempted; one person's eye vs our 8-form reading, the machine digit test was a NON-TEST; next: a digit-rich f.13r/f.10r comparison or a palaeographer's look, ~$2
- f.13r code 40 gloss (Vill. vs Lill.) and code 93 conflict - blocker: waiting-on ASKS 162 (the owner's eye on images/f13r/g40 t2/t4 and recon_1/recon_2 tiles 93a/93b); model-reader instrument retired for this gloss (F4712-40 NON-TEST, g40_read.tsv); neither code occurs on f.10r under S1

## Escalation (F4712-71, 13 Oct 2026)
- [ ] siblings: ff.13v-28r censused, no cipher (F4712-CENSUS, F4712-71); f.35v is Tomokiyo's Pasquier letter (letter/sign cipher, not the f.10r figure system at 600 px); canvases 39-45 and 47+ unviewed; planned: same census
- [x] clear-pages: ff.9, 11, 12 checked, no cipher (DUCH-LEAVES); f.13r's glossed codes used as the crib (DUCH-F13); ff.13v-28r clear (F4712-CENSUS, F4712-71)
- [x] known-keys: key no.1 applied (non-test, DUCH-KEY1B), key no.4 tried (design mismatch, DUCH-KEY4), key no.71 applied with matched controls as a letter text (F4712-K71) and as an all-code Motz text (F4712-71), control-backed negative both ways
- [x] print: Gomberville's Mémoires (1665) full-text searched (NV-INTAKE, 3 Oct 2026), no cipher passage printed
- [n/a] key-rebuild: 37 tokens is far below any cryptanalytic length for a code of this size
- [x] image-check: f.10r read from crops (DUCH-KEY1B) and checked at native resolution for marks (none, F4712-71); f.13r two blind passes agree on all 34 codes (DUCH-F13); code 40 gloss third model read a NON-TEST (F4712-40), model reader retired for that gloss, owner's eye ASKS 162
- [x] retry: hand question retried by a blind digit test (R11A-F4712, NON-TEST) and settled by the person's look (ASKS 113)
Verdict: keep going: 1 internal gap and the sibling census; cheapest next: census of canvases 39-45 (ff.28v-35r) at 600 px via openapi.bnf.fr, ~$1.5

## F4712-C39 (worker for LANE DEFAULT-A4-0935, account 4, 13 Oct 2026, 09:45-09:5x UTC by date -u): census canvases 39-45 (ff.28v-35r) -- no glossed sibling
Brief `.claude/briefs/runs/2026-10-13-acct4-default-0935-jobs.md` "### F4712-C39". Prior work: `tools/prior_work.py fr4712-nevers-duchesse
--item-spec 'shelfmark=BnF fr.4712;folio=28v-35r;canvas=39-45;date=1592-10-01' --step-type lookup --offline` exit 4 on one own-work LEAD (the
ff.9-28r clear-pages line; recorded CLEAR, canvases 39-45 never viewed); Tomokiyo CONTEXT rows name f.35 (Pasquier letter, 1592) only;
solver caches CLEAR; aymeloglu cache and editions UNCHECKED-NET (generic). No decode, so no check 5.
Host: openapi.bnf.fr IIIF v3 (ark btv1b9058289m), **8 requests, all HTTP 200**: f39-f45 at width 600 (each file named by canvas and checked
as a JPEG before the next fetch), then one region f45 `pct:52,45,43,35` at width 1600. Files in `images/census/`, entries under
`census_f13v_on` in images/manifest.json (job F4712-C39). No subagent call, no transcription.
- Map: c39 = f.28v | f.29r ... c45 = f.34v | f.35r (foliation top right, read on every right page, 29-35). Per leaf in `leaves_f13v_on.tsv`
  (the F4712-71 placeholder row for f39-f45 replaced by 14 rows).
- ff.28v-34v: clear prose, a formal royal document "Henry par la grace de dieu Roy de France et de Pologne" (f.30r-31r, M), memoranda with
  marginal "c" marks (f.33r-34r), endorsements written sideways (f.28v, f.31v), blanks (f.29v, f.34v). **No figure runs, no dotted codes,
  no interlinear code glosses** at 600 px.
- **f.35r** (c45 right): clear prose above, then about 13 lines of cipher mixed into running clear French -- digits together with signs
  (#, dotted signs, ≡, ʒ-like forms) and clear words between ("Monsieur", "plust a sa divine Ma[jes]te", M). This is the recto of
  Tomokiyo's f.35 Pasquier letter (address on f.35v, F4712-71). At 1600 px over the cipher block **no interlinear gloss** stands over any
  group, and the system is a mixed digit-and-sign cipher, not f.10r's two-digit figure run. The brief's condition for native regions (a
  glossed leaf in the f.10r/f.13r system) is not met, so no native region was fetched.
- Result: no glossed sibling of f.10r in ff.28v-35r. New f.10r tokens read: 0.
- Suggestion (outside the brief): canvases 47+ (f.36v onward) are unviewed; the volume has 142 canvases.

## Remaining gaps (F4712-C39, 13 Oct 2026)
Read so far: 6 of 37 f.10r tokens at C under S1 (16%), f13_carry.tsv; 31 tokens unread
- f.10r tokens outside f.13r's H-glossed codes (31 of 37) - blocker: no-key-material; key no.1 is a non-test at 37 tokens (DUCH-KEY1B), key no.4 cannot cover f.10r (DUCH-KEY4), key no.71 is a control-backed negative both as an unmarked letter text (F4712-K71) and as an all-code Motz text (F4712-71); ff.13v-35r carry no glossed sibling (F4712-CENSUS, F4712-71, F4712-C39; f.35r-v is the Pasquier letter in a mixed digit/sign cipher); next: census of canvases 47-58 (f.36v onward, 12 requests at 600 px), ~$1.5 per 12 canvases via openapi.bnf.fr
- same-writer basis of the six C carries - blocker: not-attempted; one person's eye vs our 8-form reading, the machine digit test was a NON-TEST; next: a digit-rich f.13r/f.10r comparison or a palaeographer's look, ~$2
- f.13r code 40 gloss (Vill. vs Lill.) and code 93 conflict - blocker: waiting-on ASKS 162 (the owner's eye on images/f13r/g40 t2/t4 and recon_1/recon_2 tiles 93a/93b); model-reader instrument retired for this gloss (F4712-40 NON-TEST, g40_read.tsv); neither code occurs on f.10r under S1

## Escalation (F4712-C39, 13 Oct 2026)
- [ ] siblings: ff.13v-35r censused, no glossed sibling in the f.10r figure system (F4712-CENSUS, F4712-71, F4712-C39); f.35r-v is Tomokiyo's Pasquier letter (mixed digit/sign cipher, no interlinear gloss at 1600 px); canvases 47+ (f.36v onward) unviewed; planned: same census, 12 canvases per job
- [x] clear-pages: ff.9, 11, 12 checked, no cipher (DUCH-LEAVES); f.13r's glossed codes used as the crib (DUCH-F13); ff.13v-34v clear (F4712-CENSUS, F4712-71, F4712-C39)
- [x] known-keys: key no.1 applied (non-test, DUCH-KEY1B), key no.4 tried (design mismatch, DUCH-KEY4), key no.71 applied with matched controls as a letter text (F4712-K71) and as an all-code Motz text (F4712-71), control-backed negative both ways
- [x] print: Gomberville's Mémoires (1665) full-text searched (NV-INTAKE, 3 Oct 2026), no cipher passage printed
- [n/a] key-rebuild: 37 tokens is far below any cryptanalytic length for a code of this size
- [x] image-check: f.10r read from crops (DUCH-KEY1B) and checked at native resolution for marks (none, F4712-71); f.13r two blind passes agree on all 34 codes (DUCH-F13); code 40 gloss third model read a NON-TEST (F4712-40), model reader retired for that gloss, owner's eye ASKS 162
- [x] retry: hand question retried by a blind digit test (R11A-F4712, NON-TEST) and settled by the person's look (ASKS 113)
Verdict: keep going: 1 internal gap and the sibling census; cheapest next: census of canvases 47-58 (f.36v onward) at 600 px via openapi.bnf.fr, ~$1.5
