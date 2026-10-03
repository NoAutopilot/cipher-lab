open
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
