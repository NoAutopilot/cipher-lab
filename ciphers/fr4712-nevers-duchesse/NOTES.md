open
Verdict: open -- key no.1 applied (DUCH-KEY1B, 3 Oct 2026): non-test at 37 tokens (power 0/20 on two pre-registered statistics); next: transcribe fr.3995 no.4 (fol.8, two-digit word list, 1585) and apply, ~USD 6.
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
