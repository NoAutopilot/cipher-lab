open
Verdict: open -- key no.1 a non-test at 37 tokens (DUCH-KEY1B, power 0/20); key no.4 cannot cover f.10r (DUCH-KEY4); ff.9, 11, 12 carry no cipher (DUCH-LEAVES); f.13r's glossed codes (DUCH-F13, 3 Oct 2026: 34 codes, both passes agree on every number, 6 codes glossed at H) cover 6 of f.10r's 37 tokens (82 82, 21 21, 12 12; p 0.029 vs random code sets), all M because the f.13r and f.10r hands were not shown to be the same writer, so the pre-registered crib gate (>=3 C) fails; f.13r's list is not key no.1 (0/6 agree). next: settle the hand question (a person's palaeographic look at images/f10b vs images/f13r, ASKS) and a third read of the 40 gloss (Vill./Lill.) ~USD 2; if the hands match, the 6 carries become C and the gate is met.
Gomberville (ed.), *Les Mémoires de M. le duc de Nevers* (1665; Google Books H2eV4wAmIr0C and three other copies) full-text searched by this worker (NV-INTAKE, 3 Oct 2026) via the Books API with `&country=US`: "duchesse ma femme" hits only Nevers' 1593-94 Roman legation speech ("...qu'à la Duchesse ma femme, à mes terres...", also in the *Discours de la legation* 1594) and "Madame ma femme" 0 -- no letter to the duchess with a cipher passage printed there.

# BnF fr.4712 f.10, the duc de Nevers to the duchesse de Nevers, undated: 37-number cipher passage -- NV-09

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

Next (Verdict line):
- More ciphertext is the only route to power. DUCH-KEY1B measured 0/20 at N=37 with no.1, the only one of the three
  duchess keys whose code set includes 0-numbers (10, 60).
- Next step: view fr.4712 ff.9, 11 and 12 (Gallica btv1b9058289m, canvases near 17-21) for further cipher passages.
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
