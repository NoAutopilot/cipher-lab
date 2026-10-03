found-solved
Plaintext of this very letter is in print (GAPS-berthier-napoleon-1812, 3 Oct 2026, Google Books API full-text search, volume MdBnAAAAMAAJ): V. Haegele (ed.), *Napoléon et Joseph Bonaparte: correspondance intégrale, 1784-1818* (Tallandier, 2007; ISBN 9782847344653), prints it as King Joseph to Napoleon, "Madrid, 22 décembre 1812", from "les archives du roi Joseph", opening "Je n'ai aucune nouvelle de V. M. depuis son départ de Paris"; page number not yet read (snippet view only, NO_PAGES). Vilcoq's date is right; his sender (Berthier) is not. Any later reading of the plate is N0-type (rule 10). Earlier premise line kept below.
Vilcoq 1969 (Persée, pages read in full incl. page images, not just search hits) reproduces the Berthier cryptogram itself as a plate (p.24, "Correspondance datée du 22 décembre 1812 du maréchal Berthier, Prince de Neufchâtel, à l'Empereur, (Archives Nationales.)" -- the image's opening number groups match ciphertext.txt exactly) with NO accompanying plaintext reconstitution, unlike the Rapp/Dantzig 1813 letter in the same article which Vilcoq does reconstruct in full (pp.25-27); Chuquet 1912 p.440 (letters XIX/XXIII, both 22 Dec 1812) read by this worker for cipher markers and carries none, while Chuquet's own edition elsewhere explicitly flags a different Berthier letter (VIII, 16 Dec, p.186) "En chiffres" -- so the XIX/XXIII pairing with this cryptogram is unconfirmed, not a match.

## Y9: full ciphertext and crib test (25 Sept 2026, LANE R6)

**(1) Full ciphertext from the Vilcoq plate.** Fetched the plate at the highest resolution Persée
serves: `renderIllustration/rharm_0035-3299_1969_num_25_4_T1_0024_0003_1.png` (1060x1429; the
whole-page `renderPage/..._<N>.jpg` endpoint ignores its own width parameter and returns a fixed,
lower-effective-resolution 1217x1833 whole page, confirmed by requesting widths 1500/2000/3000 and
getting the identical 424509-byte file each time -- so the standalone illustration crop is the best
available image, not the page). Manifest and all crops in `images/`.

Two blind passes on this one image: this worker (pass A) and one Sonnet subagent (pass B), each
transcribing independently without seeing `ciphertext.txt`, the other pass, or NOTES.md
(`passA.tsv`, `passB.tsv`). Both passes independently segmented the plate into the same 22 lines
with the same 325 total groups (exact per-line count match on all 22 lines) -- strong agreement on
where the groups are, if not always their values. Reconciling A vs B gave 16 disagreements (95.1%
raw agreement); every one was settled by re-cropping that exact spot at 3-5x zoom and reading the
digit shapes against unambiguous instances of the same digit elsewhere on the plate (this hand's "3"
is a looped script shape close to "8", and "5" has a long descender close to "8" -- both flagged by
the pass-B subagent unprompted as the hand's main hazards). Settled reading: `ciphertext_full.tsv`
(325 groups, 22 lines, matches passA/passB group-count exactly).

**Compared against the file (`ciphertext.txt`), per rule 2 (report every difference, never silently
repair ciphertext.txt):** 10 of 325 groups (3.1%) differ between this primary-source read and the
committed transcription (which derives from Cryptiana's `unsolved.htm`, itself presumably typed from
the same plate or a copy of it). Position is the 1-indexed group number in the flat 325-token
sequence; "image" is this worker's settled two-pass reading, confirmed by tight zoom in every case
below; "file" is the current `ciphertext.txt`:

| pos | image | file | zoom confirms |
|---|---|---|---|
| 60 | 544 | 844 | clear "5" (long descender), matches "544" shape elsewhere on the line, not "8" |
| 65 | 800 | 803 | trailing digit is "0" then a period, not "3" |
| 134 | 1063 | 1030 | both passes independently agreed 1063; zoom confirms |
| 136 | 693 | 690 | both passes independently agreed 693; zoom confirms |
| 172 | 633 | 683 | "3" not "8", same shape as "493"/"359" elsewhere |
| 173 | 718 | 713 | clear "8" at 4x zoom |
| 182 | 1016 | 1015 | third digit is "1" not "5" |
| 191 | 635 | 605 | middle digit is "3" not "0" |
| 296 | 1066 | 1068 | ends in two matching "6" loops, confirmed twice independently (initial pass-A/B disagreement was 1096/1098 one group earlier at pos 292 -- that one settles to **1096**, matching the file; the real diff is one group later, at 1066 vs 1068) |
| 305 | 463 | 460 | "3" not "0", matches Bourdeau's own `berthier_ct.txt` reading of "460" too -- so this is a primary-image correction against **both** existing transcriptions, not just this repo's |

No group-count or line-count discrepancy: image, passA, passB and the file all agree the plate holds
exactly 325 groups, and (checked directly) the plate's last line is the visible end of the text --
no further lines below it, no second plate. So Bourdeau's "opening only, 325 groups, then '....'"
description (his `napoleon/NOTES.md`, cited below) is now confirmed as the **whole printed
cryptogram**, not a truncated excerpt of a longer one Vilcoq's article holds back; the "...." in this
repo's `ciphertext.txt` marks where transcription happened to stop, not where the plate's own text
continues. `ciphertext.txt` is left as-is (rule 2); `ciphertext_full.tsv` is the line-broken, image-
sourced, two-pass-settled reading and is the one to use for any future crib or key work.

Structure (from `ciphertext_full.tsv`): 325 groups, 207 distinct, 136 hapax (66% of the 207 distinct
codes occur once), commonest codes 918 and 13 (8x each, 2.5% of tokens), range 2-1388, occupancy
near-flat across 1-1199 with only a few groups above 1200. This reproduces Bourdeau's own
`napoleon/berthier.py` structural read almost exactly (his 325/207/64%/918&13-8x-2.5%/2-1388) --
his `berthier_ct.txt` is in fact byte-identical to this repo's `ciphertext.txt` (diffed directly).

**(2) Lead classes, in order (stop at the first that reads).**

**(a) Same letter in print -- Chuquet 1912's two 22 Dec 1812 clear letters (XIX, XXIII).** Fetched
the full djvu.txt of `archive.org/1812laguerrederu03chuquoft` (already known reachable, CX2-BERT)
and wrote `scripts/extract_chuquet_letters.py`, which segments Berthier's whole December run by its
Roman-numeral letter markers and drops page-header/footnote noise. It recovered 34 dated Dec 1812
letters (II-XXXVIII; a few numbers are absent because the marker itself misparsed in the OCR), giving
a real matched-control pool far bigger than the 20 the brief asked for. `scripts/letters.json` is the
extracted text; `scripts/letter_stats.json` and `scripts/crib_test_results.json` are the numbers.

Three honestly-reported, non-cherry-picked fit metrics, each scored for XIX (157 words), XXIII (529
words) and all 32 other letters against the 325-group cryptogram (`scripts/crib_test.py`):

1. **length fit** `|n_words - 325| / 325` (would a one-code-per-word system make sense length-wise):
   XIX ranks 15th of 34 (0.517, i.e. barely half as many words as groups); XXIII ranks 18th (0.628,
   62% more words than groups). The single best length match in the whole pool is letter **XXIX**
   (28 Dec, 316 words, fit 0.028) -- not one of the two candidates the brief named, out of scope here,
   flagged as a one-line suggestion below.
2. **repeat-rate fit** `|word_repeat_rate - group_repeat_rate|` (325 groups repeat at 36.3%): XIX is
   the closest fit of the two candidates, ranking **3rd of 34** (0.026); XXIII ranks 29th (0.180).
3. **repeat-gap-distribution fit**, a KS statistic between the normalised gap-length distributions of
   repeated tokens: XIX ranks 18th of 34 (0.285); XXIII ranks 30th (0.403).

**Verdict: no fit.** XIX places respectably on one of three metrics (repeat-rate) but mid-pack on the
other two; XXIII never places above the middle of the field on any metric. Neither beats the 34-letter
control on a majority of tests, which is exactly the brief's bar for "a fit means something only if it
beats them." This agrees with Bourdeau's own conclusion in `napoleon/NOTES.md` ("an alignment can
always be manufactured [given 325 groups and a free choice of plaintext]; it would mean nothing. No
alignment is proposed") and extends it: Bourdeau compared XXIII alone against the raw cipher's own
stats (distinct/hapax/peak-frequency/repeated-bigrams) with no control; this pass adds the missing
control (33 other letters) and the same negative holds up under it.

**(b) Published key of the office.** Grepped a fresh shallow clone of `dbourdeau/cyphersolver` (MIT)
and this repo's `sources/cryptiana/` for "petit chiffre" / "petit-chiffre" and any Napoleon/Berthier
1812 table. Three hits, none applicable: `sources/cryptiana/web/napoleon2.htm` uses the phrase once,
inside a *quoted 1812 letter* about routine army correspondence ("vous servant du petit chiffre de
l'armée") -- a mention of a different, unnamed cipher in passing, not a key table for it, and not
Berthier's "Chiffre du Prince de Neufchâtel" specifically; the other two hits (`catinat1691.htm`,
`crypto.htm`) concern an unrelated 1691 Catinat cipher. Bourdeau's own repository, searched directly
(no file besides `napoleon/` mentions Berthier or Napoleon 1812), confirms no key was found there
either -- his own write-up states plainly that the 1200-entry nomenclator "is not a cipher that yields
to analysis" from structure alone, with no key on file to apply. No key exists in either source to
apply, so there is no random-draw control to run (rule 3's control requirement applies to a claimed
result; there is no result here to gate). No free cryptanalysis attempted beyond this, per brief.

**Status stays `open`.** Credit (rule 8): Bourdeau (`dbourdeau/cyphersolver`, MIT code / CC BY 4.0
text) independently found and printed the same 325-group excerpt, ran the same structural read this
pass reproduces, and ran an uncontrolled version of the same XXIII crib check this pass now controls
against 34 letters and confirms negative; Tomokiyo/Cryptiana for the original excerpt and the "et has
several codes" comparison cited in Bourdeau's own notes.

**One-line suggestions for whoever picks this up next (not followed here, out of this brief's
scope):** (1) letter XXIX (28 Dec 1812, 316 words) is the single best length-match to the 325-group
cryptogram in the whole Dec-1812 Berthier corpus (fit 0.028) -- not tested on the other two metrics
here since it wasn't one of the two candidates named, but cheap to add; (2) the "votre note chiffrée"
lead in *Correspondance de Napoléon Ier* vol. XXIV, named by both Tomokiyo and Bourdeau and not yet
retrieved by either; (3) William Urban's find of Berthier's cipher-use instructions in the Russian
State Military Historical Archive (named on Cryptiana's napoleon2.htm, not yet checked by anyone in
this repo).

Requests this section: persee.fr 7 (main doc page 1, page-fragment probes 2, illustration PNG 1,
whole-page-JPG width-parameter probe 3, all >=1.5s apart, no 429/403); archive.org 1 (djvu.txt
download, already fetched once by CX2-BERT, re-fetched here since this session did not have it on
disk); github.com 1 (shallow clone of dbourdeau/cyphersolver, MIT, removed after grep). 1 Sonnet
subagent (pass B, blind image transcription, one call).

## BBER: spec and first test (25 Sept 2026, LANE R7)

Wrote `specs/berthier-napoleon-1812.json` per `specs/README.md`'s house format (shape copied from
`specs/antt-linhares-chave.json`): ciphertext from `ciphertext_full.tsv` with source and date,
alphabet, constraints (nomenclator, one- or two-part unknown, French, Berthier to Napoleon 22 Dec
1812), `judge` block, and `cheap_tests_in_order` listing all four tests the job brief named (test 0
run this pass, test 1 attempted as a print check, tests 2-3 stated only).

**Judge language: `fr18`.** `tools/judge_plaintext.py`'s `LANG_CORPORA` wires only `fr` (fr16,
16th-c.) and `fr18` (diplomatic/official French prose c.1680-1790) for French; `tools/data/fr19/`
(1800-1890 prose) exists on disk but is **not** in `LANG_CORPORA` as of this pass, so a spec cannot
opt into it. fr18 is the closer of the two wired options to this target's Dec 1812 date (22-132
years off vs. fr16's ~230), but still an era mismatch by CLAUDE.md's V6-PTCORP lesson (era match
matters, not just language) -- flagged in the spec as a one-line suggestion (build and wire a
1800-1815 French official/military corpus) rather than built in this $3 breadth pass.

**Test [0]: crib fit, extended to letter XXIX.** Re-ran the existing `scripts/crib_test.py` (LANE
R6 Y9, unchanged) to read off letter **XXIX** (28 Dec 1812, 316 words -- the single best length
match to the 325-group cryptogram in the whole 34-letter pool, fit 0.0277) on all three of the
script's metrics against the same 34-letter control (the field of 33 other Chuquet Dec-1812
Berthier-to-Napoleon letters, median rank 17.5 of 34):

| metric | XXIX rank (of 34) | value |
|---|---|---|
| length_fit | **1st** | 0.0277 |
| rate_fit | **12th** | 0.0705 |
| gap_fit | **17th** | 0.2737 |

XXIX beats the control median on all three metrics (majority test passed), unlike the two letters
the original R6 brief scored (XIX beats the median on only rate_fit, 3rd of 34; loses on length_fit,
15th, and gap_fit, 18th; XXIII never rises above mid-pack on any metric: 18th/29th/30th). This is
**not** a crib or an alignment claim (rule 4: no grade assigned, no S/H/C token): length_fit is a
single easily-coincidental signal (one code roughly per word, 325 vs 316) and the other two metrics
for XXIX are mid-pack, not standout, so the result is reported as a lead for test [1], not a result
in itself. Numbers written to `specs/berthier-napoleon-1812.json` `cheap_test_done[0]`.

**Test [1]: Correspondance de Napoléon Ier vol. XXIV print check.** Budget allowed running this as
the brief's named exception (disk-only test 0 leaves room for one network test). `archive.org`
advancedsearch confirmed volume XXIV is `correspondancede24napouoft` (already known, LANE CX2).
be-api fts is a coarse locator only (its `page_num` field equals the item's total `imagecount`, not
a real page -- logged in CLAUDE.md's Access playbook), so after the first round of fts queries this
worker fetched the volume's full `_djvu.txt` (43,181 lines; archive.org, 302-redirect followed) and
grepped it directly for exact letter headers and dates -- a genuine read, not a search-hit count.

- `"note chiffrée"` (fts, exact phrase Tomokiyo/Bourdeau's paraphrase quotes) -> 0 hits anywhere in
  the volume (confirms CX2's prior negative).
- `chiffr` (grep, case-insensitive, whole djvu.txt): the only nearby hit is letter **19275** (Napoléon
  to Maret, Duc de Bassano, Moscou, **16 October 1812** -- a different correspondent and a two-month-
  different date), editorially marked "Lettre en chiffre dont il n'a pas été possible de faire la
  traduction" -- an untranslated ciphered letter whose gist the editor reconstructs from Bassano's own
  paraphrase to Comte Otto. Not Berthier, not December, not this cryptogram; a real but unrelated case
  of the same editorial convention ("lettre en chiffre" marked but not deciphered in this edition).
- `"lettre du 21"` and `"30 décembre"` (fts, then grepped in the djvu.txt) together locate letter
  **19408**: "AU PRINCE DE NEUFCHATEL ET DE WAGRAM, MAJOR GÉNÉRAL DE LA GRANDE ARMÉE, A KOENIGSBERG.
  Paris, 30 décembre 1812. Mon Cousin, j'ai reçu votre lettre du 21 ; j'ai reçu aussi votre note
  pertes réelles ; je vais y penser sérieusement. [...]" -- this is Napoleon's 30 Dec 1812 reply to
  Berthier at Koenigsberg (matching napoleon2.htm's claim of a 30 Dec letter acknowledging a note
  together with a dated Berthier letter), but two details do not match the lead as quoted: (a) the
  Berthier letter acknowledged is dated the **21st**, not the 22nd (this target's cryptogram date);
  (b) the note is named **"note pertes réelles"** ("note [on] real losses"), not **"note chiffrée"**
  ("ciphered note") -- a different two-word phrase, not an OCR-garbling of the same words. Read
  plainly, this looks like Napoleon replying to a *separate*, dated-the-21st letter about casualty
  figures, not to the 22 Dec ciphered dispatch.
- `"lettre du 22"` (fts, then grepped): five hits in the volume, none addressed to Berthier or
  mentioning a cipher -- Rapp (governor of Danzig, 4 Jan 1813, "votre lettre du 22 décembre. Danzig
  doit être approvisionné..."), Lauriston, and others on unrelated business.

**Verdict: not found, and the specific claim in the lead ("votre note chiffrée" in the 30 Dec
letter) does not match this printed edition's wording.** The 30 Dec letter to Berthier (19408) is a
real, located letter and is the closest match to napoleon2.htm's description (same addressee, same
date, acknowledges a dated letter and a "note"), but its own text says "note pertes réelles," not
"note chiffrée," and answers a letter of the 21st, not the 22nd. Either the secondary source's
paraphrase is imprecise about which "note" it means, or a genuinely different letter/note is meant
that this pass did not locate. Not claiming this resolves or refutes the lead -- reporting exactly
what was read and where it differs from the claim, per rule 2's "report every difference" standard
applied here to a lead rather than a transcription.

Recorded as `cheap_test_done[1]` in the spec: found letter 19408 (30 Dec 1812, Napoleon to Berthier)
as the closest match to the "votre note chiffrée" lead, with the two discrepancies above; no letter
in the volume pairs a cipher mention with Berthier's 22 Dec letter specifically.

**Status stays `open`.** Not found-solved, no key, no cryptanalytic result (rule 3's ladder still
blocks a campaign at this N against a ~1200-entry nomenclator). Credit unchanged from LANE R6/CX2's
prior work in this file; this pass extends the existing crib-test script's output table and adds a
direct full-text read of vol. XXIV that goes beyond CX2's earlier be-api-only search.

**One-line suggestion:** the discrepancy between letter 19408's actual text ("note pertes réelles")
and the lead's "votre note chiffrée" is worth checking against Urban's own source (Cryptiana's
uncredited citation, test [3]) or a different edition/volume before treating napoleon2.htm's
paraphrase as settled either way.

Requests this section: archive.org (advancedsearch 1 + be-api fts 5 + one `_djvu.txt` download,
all >=1.5s apart, no 429/403) 7. No subagents.

## Found-solved test (LANE CX2 worker CX2-BERT, 25 Sept 2026)

Ran the three-part found-solved test the orchestrator queued (CX2-FRAWI's 16:03/16:06 passes had located Chuquet p.440 and the Persée article but not yet read Chuquet's source notes or Vilcoq's actual page images -- both done in this pass).

**(a) Chuquet -- does he say either 22 Dec letter was sent in cipher / deciphered from a primata?** No. Fetched the full djvu.txt (`archive.org/download/1812laguerrederu03chuquoft/1812laguerrederu03chuquoft_djvu.txt`) and read pp.185-201 (letters VIII through XXIV) directly, not just the be-api search-hit page. Letters XIX (p.196-197, Bosset widow's pension) and XXIII (p.198-201, situation report, "louer des Prussiens") carry no cipher marker and no footnote about decipherment. By contrast letter VIII (Wirballen, 16 Dec 1812, p.186) is headed "En chiffres." in the text itself, and letter XI (Gumbinnen, 18 Dec, p.190-191) refers to "la note chiffrée que j'ai adressée à Votre Majesté par M. Atthalin" -- so Chuquet's edition *does* flag ciphered content when he has it, and does not flag XIX or XXIII that way. The chapter's own source note (p.165, "45. Berthier à Napoléon") says the whole December run of letters is "tirées soit des archives de la guerre, soit des archives nationales (A.F. iv. 1643)" with no cipher/decipherment comment. Grepped the whole djvu.txt for "chiffr" (case-insensitive): only 3 hits total in the entire book -- line "En chiffres." (VIII), "note chiffrée" (XI), and one unrelated use of "chiffre" meaning "number" (p.~300s, troop count). Conclusion: Chuquet gives no textual basis for pairing XIX or XXIII with a ciphered original; if anything the absence of a marker where Chuquet elsewhere reliably supplies one argues against the pairing.

**(b) Vilcoq -- does the plate reproduce the cryptogram, print/summarise the clear text, and which letter is it?** Read the article's actual page images (not just the OCR/search index), fetched via Persée's per-page AJAX content URLs (`persee.fr/doc/page/rharm_0035-3299_1969_num_25_4_8686/rharm_0035-3299_1969_num_25_4_T1_00NN_000M`, one per illustration/text block, 1.5-2s apart) after the collapsed initial page (T1_0022) rendered only pp.22's text and thumbnail links for the rest. The plate captioned for Berthier (`renderIllustration/rharm_0035-3299_1969_num_25_4_T1_0024_0003_1.png`, fetched and eye-checked) is a manuscript facsimile, not a transcription: marginal annotations "Duplicata", "Chiffre du Prince de Neufchâtel", "La Primata a été déchiffrée" (matching this repo's known description of the item verbatim) above an engraved "Sire," salutation and ~20 lines of number-groups. The visible opening groups (918 1045 1100 493 359 989 1105 73 710 432 118 718 544 810 1060 1135 1122 173 666 ...) match this repo's `ciphertext.txt` exactly -- this is very likely the same document (or an identical duplicate) our transcription derives from, now seen as a primary-source image for the first time in this repo, not just Cryptiana's re-typed excerpt. Vilcoq gives NO plaintext for it: the article's running text (pp.22-24, read in full) is a methodological survey of Napoleonic cipher tables, illustrated with four plates (a cipher table p.23, the Marmont 1807 correspondence p.24, this Berthier plate p.24, and a Rapp/Dantzig-1813 letter p.24) -- and only the Rapp letter gets a "reconstitution" (pp.25-27, read in full): a full transcribed text with the words that were originally ciphered marked in capitals, because that letter was sent partly in clear and partly in cipher (easier to attack, per Vilcoq's own methodological point on p.24 that "il est plus difficile d'attaquer le décryptement de correspondances entièrement chiffrées" -- exactly what the all-numeric Berthier cryptogram is). The article ends with an editorial note: "L'auteur de cet article sera très heureux d'entrer en relations... avec ceux de nos lecteurs qui désireraient connaître en détail les méthodes de décryptement utilisées pour la reconstitution du document ci-dessus" -- "du document ci-dessus" refers to the Rapp letter just printed, not Berthier's. So: the plate reproduces the cryptogram only; Vilcoq neither prints nor summarises its clear text; and because it is never deciphered in the article, it cannot be matched to XIX vs XXIII (or to neither) from Vilcoq alone.

**(c) Verdict.** Not found-solved. Chuquet's two 22 Dec clear letters are not marked as cipher-derived and Chuquet does mark cipher letters elsewhere in the same run; Vilcoq's plate is the ciphertext facsimile with no plaintext given. No source found in this pass pairs a plaintext with this specific cryptogram. Target stays `open`. What this pass leaves to hand on: (1) a primary-source image of the actual cryptogram is now known and reachable (`persee.fr/renderIllustration/rharm_0035-3299_1969_num_25_4_T1_0024_0003_1.png`, confirmed matches ciphertext.txt's opening), an upgrade on the transcription-only status rule 2 flags -- not fetched into the repo this pass (out of this brief's scope: no transcription/image capture beyond the one leaf-view already done to confirm the caption); (2) Bourdeau's own structural objection (64% hapax against a ~1200-group code) is the real blocker to cryptanalysis, unaffected by this test; (3) Urban's book (named on Cryptiana's napoleon2.htm, "Urban found Berthier's instructions for use of a great cipher in the Russian State Military Historical Archive in Moscow but apparently not the code itself") is a named, uncredited lead not yet checked.

Requests this section: archive.org (djvu.txt download) 1; persee.fr (main doc page 1, 9 per-page AJAX fetches, 1 illustration PNG fetch, one retry after a `Recv failure: Connection reset by peer` on the first illustration attempt, all >=1.5s apart) 12. WebSearch 0 (none needed for this pass). No subagents.

## Check-solved (LANE CX2, 25 Sept 2026)

1. **Web search.** `WebSearch` "Berthier Napoleon 22 décembre 1812 chiffre Vilcoq déchiffrée Primata" -- no model-solve announcement, no decipherment claim; general Berthier biography pages and the Fondation Napoléon's `napoleonica.org` correspondence database (item 29124, "Au maréchal Berthier, major général de l'armée", dated in the surrounding weeks but not confirmed as the 22 Dec letter or its 30 Dec reply -- not opened, napoleonica.org's own search endpoint 404'd on the query tried and was not pursued further this sweep). No "solves"+"Claude"/"GPT" hit for this item.
2. **Standard edition(s), this worker's own read.**
   - **Chuquet 1912** (archive.org `1812laguerrederu03chuquoft`, vol.3/"troisième série"): be-api fts, control "Bosset" -> 1 page hit, p.440: "Kônigsberg, 22 décembre 1812. Sire, M. le colonel Bosset, commandant d'armes..." (letter XIX, the Bosset-pension letter Bourdeau's write-up names); target phrase "louer des Prussiens" -> same page 440: "...n'avons jusqu'à ce moment qu'à nous louer des Prussiens" (letter XXIII, the situation report). Both of Berthier's 22 Dec 1812 clear letters that Bourdeau's `napoleon/NOTES.md` (Chuquet, 3e série, pp.165-219, letters XIX and XXIII) describes are confirmed in clear on this one page of this scan -- independently verified by this worker, not just quoted from Bourdeau.
   - **Vilcoq 1969**, previously recorded (this repo's NOTES.md line 8 and Bourdeau's `napoleon/NOTES.md`, 15 Sept 2026) as "not digitised... a Service historique de la Défense journal; a library copy or an SHD request is the route." That is now out of date: `persee.fr` carries the article at `doc/rharm_0035-3299_1969_num_25_4_8686` -- confirmed by page title "Le Chiffre sous premier Empire" and the citation block "Vilcoq J. Le Chiffre sous premier Empire. In: Revue Historique des Armées, 25e année, numéro 4, 1969. pp. 22-27." Persée's own internal search endpoint (`/doc/search/<id>?q=`) was used as the full-text search: control "Napoléon" -> hits on pp.22, 23 and 24 (three of the article's six pages); "Berthier" and "Neufchâtel" -> both hit p.24 only; "1388" (our ciphertext's max group), "Primata" and "1812" (as bare digits) -> 0 hits each. Read together, this places a paragraph naming Berthier's cipher ("Chiffre du Prince de Neufchâtel") on p.24, but the absence of "1388"/"Primata" hits means this six-page survey article most likely does not reprint the full ~1200-group cryptogram or the "Primata a été déchiffrée" note verbatim -- consistent with Cryptiana's own excerpt (below) already being the fullest published fragment, not a truncation of a longer one Vilcoq gives. This worker did not attempt to read Vilcoq's actual page images beyond the search-hit level (Persée serves them as page-image + OCR-overlay, not a plain text/PDF export found in the time available) -- a genuine next step, but the access blocker itself (an SHD-only journal) is resolved.
   - **Correspondance de Napoléon Ier vol. XXIV** (archive.org `correspondancede24napouoft`), named in the job brief for Napoleon's reply: be-api fts for "note chiffrée" -> 0 hits; control "Berthier" -> 1 page-bucket hit (this be-api endpoint appears to report a coarse per-document "any hit" total rather than a true occurrence count -- confirmed by re-running the same control on Chuquet and Doniol above, where an equally common name also returned "total: 1" -- so this is a weak negative, not a confirmed absence). Tomokiyo's own `napoleon2.htm` page (below) separately cites this exact archive.org identifier in an HTML comment as his own source for dating Berthier's location (Koenigsberg) -- corroborating this is the right volume, but this worker did not locate Napoleon's 30 Dec 1812 letter acknowledging "votre note chiffrée" within it this sweep.
3. **Community lists.** `sources/cryptiana/web/napoleon2.htm` (on disk) section "Napoleon-Berthier Code (December 1812)" (`#SEC5`) read in full by this worker: gives the same ~103-group opening as our `ciphertext.txt` (matches through "356" at the seventh line, i.e. this repo's transcription follows `unsolved.htm`'s reading, not `napoleon2.htm`'s "656" variant -- both already noted at NOTES.md line 8, no change), attributes the source as "(Vilcoq)", records "Urban found Berthier's instructions for use of a great cipher in the Russian State Military Historical Archive in Moscow but apparently not the code itself (Urban p.324)" -- a named scholarly source (William Urban) not yet checked in this repo -- and states the cipher "may correspond to 'votre note chiffrée', which is acknowledged, together with Berthier's letter of the 21st, in Napoleon's letter to Berthier dated 30 December 1812" (matching Bourdeau's independent note of the same lead). `sources/cryptiana/web/henryiii.htm` and `unsolved.htm`/`unsolved-2026-09-24.htm` also name-check Berthier but only in passing (cross-reference lists); no additional content.
4. **DECODE.** `sources/decode/*.tsv` (on disk, 24 Sept 2026 snapshot) grepped for "berthier"/"napoleon": no hit.
5. **Bourdeau.** Shallow-cloned `dbourdeau/cyphersolver` fresh this session (25 Sept 2026). `napoleon/NOTES.md` read in full (already the fullest existing treatment; quoted in point 2 above and matches this worker's own Chuquet read). Verdict there: blocked on the full ciphertext (Vilcoq 1969) -- now correctable given point 2's Persée find, though the plaintext-alignment question (Chuquet's letters vs. the code) is unchanged: with 64% hapax against a ~1200-entry code and only 325 of an unknown total groups printed anywhere this worker could find, this remains "not a cipher that yields to analysis" per Bourdeau's own structural read, which this worker did not re-derive independently (no cryptanalysis performed, per brief scope).
6. **Aymeloglu.** Shallow-cloned `aaymeloglu/unsolved-ciphers` fresh this session: no file matches "berthier" or "napoleon" anywhere in the repository.

Requests: archive.org (advancedsearch + be-api fts) 6, 1.6 s apart; persee.fr (page fetch + internal search endpoint) 8, 1.6 s apart; napoleonica.org 1 (404, not retried); WebSearch 1.

Intake gate: `open` -- Chuquet 1912 p.440 was read by this worker with a page number and controls found; the target's own primary source (Vilcoq 1969) is also now confirmed accessible where it was previously recorded as unreachable. No key or full plaintext for the ciphertext itself is established; the code (Vilcoq's own printed groups vs. Chuquet's plaintext letters) has not been aligned by this worker or, so far as found, by anyone -- Bourdeau's structural objection (64% hapax) stands unchallenged. Correction to NOTES.md line 8 (in place): Vilcoq 1969 is no longer accurately described as "not digitised" as of 25 Sept 2026 -- it is on Persée, though the ciphertext this worker could confirm inside it via search remains only the same fragment already on Cryptiana (corrected LANE CX2 25 Sept 2026).

---

# Berthier to Napoleon (22 December 1812)

- **Source:** Reproduced in J. Vilcoq, "Le Chiffre sous le Premier Empire", Revue Historique de l'Armée no.4 (1969). Bears the note "Duplicata, Chiffre du Prince de Neufchâtel, La Primata a été déchiffrée", so a contemporary decipherment likely exists in the archives.
- **Status:** Open.
- **Transcription:** `ciphertext.txt` holds the opening as quoted on unsolved.htm. Numbers up to about 1388.
- **Background page:** `sources/cryptiana/web/napoleon2.htm` (Napoleonic ciphers that may be similar).
- **Ideas:** Large code, over 1200 entries, of the Grande Armée type. Repeated triples (918 1045 1100 appears twice near the start) suggest a fixed phrase. Compare with the Grand Chiffre tables in napoleon2.htm. Date context: retreat from Russia, Berthier was chief of staff.
- **Solver status (19 Sept 2026):** Blocked per Bourdeau (cyphersolver/napoleon), 15 Sept 2026: the full ciphertext exists only in Vilcoq 1969, not digitised. Chuquet 1912 prints Berthier's clear letters of 22 Dec 1812 from the same carton, a ready crib. Cryptiana's two pages disagree on one group (356 vs 656).

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## IMG-FETCH: Vilcoq article page images fetched (26 Sept 2026)

Per NEXT-STEPS.tsv's row (search hits named pp.22-24; the article runs only pp.22-27, so "the two
pages either side" covers the rest of it): fetched all six page images of the article
(`renderPage` endpoint, 710px width, the same effective resolution the manifest already noted is
the best Persée serves for a whole page) plus the OCR text overlay for every content block on every
page (`doc/page/<doc>/<page>` fragments), saved to `images/persee/` with `manifest.json` (URLs,
page numbers, fetch time). 17 persee.fr requests total, >=1.8s apart, 2 retried once each after a
`Recv failure: Connection reset by peer` (both succeeded on retry).

**Whether these pages print the target letter's cipher, a decipherment, or neither, quoting the
OCR line that decides it:**

- **p.22-23** (`frag_0022_0000.html`, `frag_0023_0000.html`): general methodological survey (the
  1798 Bonaparte/RIMINI cipher, cipher-table sizes by post: "1807 Vienne (3.500 groupes) — 1808
  Rome (3.000 groupes) — 1812-1813 Varsovie (3.600 groupes) — 1812-1813 Espagne (1.400 groupes)").
  No mention of Berthier or a 22 Dec 1812 letter on either page. **Neither.**
- **p.24 block 0** (`frag_0024_0000.html`): article text distinguishing two kinds of ciphered
  document Vilcoq worked from -- "la lettre chiffrée comportant la traduction soit au-dessus du
  cryptogramme, soit sur une feuille séparée" (translation supplied) vs. correspondence "en partie
  en clair et en partie en chiffré" -- then states which one follows: "Nous nous contenterons donc
  de reproduire ci-après le décryptement exact que nous avons effectué de la lettre du général Rapp
  à l'Empereur, écrite le 6 novembre 1813" -- the reconstitution that follows (pp.25-27) is
  **Rapp's letter, not Berthier's**. **Neither**, for the target.
- **p.24 block 1** (`frag_0024_0001.html`): caption "Tableau de chiffrement. Chiffre utilisé sous
  le Premier Empire." -- a cipher table plate, not tied to any named letter. **Neither.**
- **p.24 block 2** (`frag_0024_0002.html`): caption "Correspondance chiffrée adressée au général
  Marmont, Chef du 11e Corps en 1807." -- a different addressee, a different year. **Neither.**
- **p.24 block 3** (already on disk as `../plate_t1_0024_0003_1.png` / `../page_0024_0003.html`,
  not refetched): caption "Correspondance datée du 22 décembre 1812 du maréchal Berthier, Prince de
  Neufchâtel, à l'Empereur, (Archives Nationales.)" over the manuscript facsimile whose opening
  groups match `ciphertext.txt`. **This is the target's cipher** (the cryptogram itself, as a
  photograph of the original) -- confirmed again, not newly found; no plaintext accompanies it.
- **p.24 block 4** (`frag_0024_0004.html`): caption "Début et fin de la lettre de dix pages du
  général Rapp à l'Empereur datée de Dantzig, le 6 novembre 1813." -- the Rapp letter's own
  facsimile, not Berthier's. **Neither.**
- **p.25-27** (`frag_0025_0000.html` through `frag_0027_0000.html`): the full reconstituted text of
  Rapp's 6 Nov 1813 Dantzig letter (capitalised words marking what was originally ciphered, per the
  article's own note at the end: "dans la reconstitution de cette lettre les mots en capitales
  correspondent aux parties chiffrées du texte original"), signed "Lieutenant-colonel J. Vilcoq,"
  followed by the editorial closing note inviting readers who want the decryption method for "le
  document ci-dessus" (the Rapp letter just printed) to contact the author. **This is a
  decipherment, but of a different letter (Rapp/Dantzig, not Berthier/22 Dec 1812) -- neither for
  the target.**

**Conclusion, matching and extending LANE CX2's 25 Sept 2026 finding (search-hit level) now that
every block on every relevant page has been read in full via OCR:** the article prints the target
letter's cryptogram once (p.24 plate) and no plaintext or decipherment of it anywhere in the piece;
the only decipherment Vilcoq gives in the whole article is of an unrelated letter (Rapp to
Napoleon, Dantzig, 6 Nov 1813). Status unchanged: `open`, no key, no cryptanalytic result.

Requests this section: persee.fr 17 (6 page JPGs + 9 OCR fragments + 2 retries), >=1.8s apart,
browser-style UA, no 429/403. file_shrink_guard clean on NOTES.md and images/persee/*.

## JSTOR runner, 26 Sept 2026

- `"Berthier" AND "Neufchâtel" AND 1812 AND chiffre`: context only, no hit about the letter -- Louis Madelin,
  "Les lettres de Napoléon à Marie-Louise", Revue des Deux Mondes 25(4), 1935, pp. 749-781,
  https://www.jstor.org/stable/44847985.
- `"maréchal Berthier" AND "22 décembre 1812"`: no relevant hit (0 results, none about the letter).

## Next step from the method registers (27 Sept 2026, parent 7k, from LESSONS-TOMOKIYO.md (d))

Named next step (not run): contact table and KWIC of the 325 groups (207 distinct) before any solver (Tomokiyo
codebreaking.htm "Statistical Analysis", kwic.htm), then Bazeries' probable-phrase search for variably-spelled repeats of a
syllabic phrase the subject must contain (cf. "les en-ne-mi-s"), cribbed from the Chuquet 1912 clear letters of 22 Dec 1812
cited above. Cost band S (script pass; `tools/freq.py --contacts/--kwic` added by the worker with an offline test). The
control for the contact-table reading is the same table on a shuffled-order copy of the groups. Status stays open.

## BER-KWIC (27 Sept 2026, parent worker BER-KWIC)

Ran the named next step. Tool: `tools/freq.py` gained `--contacts K`, `--kwic TOKEN --width W --sort left|right`,
`--repeats N` and `--split-at N`, with `--help` text and an offline test (`tools/tests/test_freq.py`, 22/22 checks
pass on a synthetic ten-line fixture, default output unchanged when no new flag is given). SYSTEM.md section 8's
three built rows (contacts+kwic, repeats, split-at) moved into the `tools/freq.py` row of section 3b;
`system_map_check.py` prints ok.

**Which file.** `ciphertext.txt` (the brief's named input) carries an uncommented second line
("Berthier to Napoleon, 22 December 1812") that freq.py's default tokeniser would fold in as five
extra non-numeric tokens plus the trailing "...." marker as a sixth -- a real defect in that file for
this kind of run, not something to silently fix (rule 2). Used `ciphertext_full.tsv` instead (the
two-pass, image-sourced, already-settled 325-group reading NOTES.md's own Y9 section names as "the
one to use for any future crib or key work"), flattened to `structure/flat.txt` (325 tokens, 207
distinct, matches the tsv exactly).

**Tables** (`ciphers/berthier-napoleon-1812/structure/`: `contacts.tsv`, `repeats.tsv`,
`kwic-918.tsv`, `kwic-13.tsv`, `kwic-73.tsv`, `split.tsv`, plus the shuffled-control pair
`contacts_shuffled.tsv`/`repeats_shuffled.tsv`).

`--contacts 20` head (real run, `structure/contacts.tsv`):

| token | count | pct | self_succession | tag | preceders | followers |
|---|---|---|---|---|---|---|
| 918 | 8 | 2.5 | 0 | neither | 10:2;820:1;69:1;450:1;838:1;388:1 | 1045:2;86:2;215:1;1043:1;29:1;694:1 |
| 13 | 8 | 2.5 | 0 | neither | 701:1;602:1;43:1;289:1;370:1;644:1;25:1;1148:1 | 572:1;782:1;821:1;741:1;1202:1;718:1;599:1;357:1 |
| 73 | 5 | 1.5 | 0 | suffix-like | 463:3;1105:2 | 710:1;793:1;1187:1;798:1 |
| 1100 | 4 | 1.2 | 0 | suffix-like | 1045:2;711:1;507:1 | 493:1;415:1;1109:1;173:1 |
| 821 | 4 | 1.2 | 0 | prefix-like | 989:1;13:1;607:1;617:1 | 791:3;694:1 |
| 168 | 4 | 1.2 | 0 | prefix-like | 851:1;1187:1;875:1;322:1 | 854:2;828:1;923:1 |

The prefix-like/suffix-like tag is **not** computed from self-succession (self-succession counts the
same "XX" adjacency from either direction, so "often preceded by itself" and "never followed by
itself" cannot literally both hold for the same statistic -- checked directly). It implements
Yardley's actual finding as quoted in `codebreaking.htm` ("it was often preceded by the same group
but was always followed by a different group"): left-context CONCENTRATION (one particular preceding
token accounts for >=40% of occurrences) with right-context DIVERSITY (every following token
distinct) tags suffix-like; the mirror tags prefix-like. Documented in the tool's own docstring.
Self-succession is reported as its own column regardless (all zero for the top 20 in this ciphertext,
both real and shuffled -- see control below).

`--repeats 2` head (`structure/repeats.tsv`, 57 lines total): 14 recurring bigrams and 2 recurring
exact trigrams (`168 854 1148` at positions 52 and 258; `918 1045 1100` at positions 0 and 41), then
41 near-repeat trigram pairs (differ in exactly one of three positions).

`--kwic` on the three most frequent groups (918, 13, 73), width 3, both sorts -- head of `kwic-918.tsv`:

| pos | left_context | token | right_context |
|---|---|---|---|
| 0 | (start) | 918 | 1045 1100 493 |
| 282 | 409 653 10 | 918 | 694 972 426 |
| 194 | 875 212 450 | 918 | 1043 340 607 |

**Range split.** The lowest gap in the 207 sorted distinct values (2..1388) that leaves a <=40-value
low block is a tie: gap=1 at 139|140 (low block 16 distinct values, 2-139) and gap=1 at 235|236 (low
block 28 distinct values, 2-235); resolved in favour of the larger block since 28 sits closer to a
full alphabet size (26 letters), the more plausible size for Wallis's "small substitution cipher
inside the code" (Tomokiyo practice 1). `--split-at 236` (`structure/split.tsv`):

| side | tokens | distinct | IC |
|---|---|---|---|
| low (<236) | 60 | 28 | 0.0395 |
| high (>=236) | 265 | 179 | 0.0039 |

(alternative split at 140: low 39 tokens/16 distinct/IC 0.0742, high 286/191/0.0037 -- both alternatives
recorded, neither chosen as definitive; this is a lead, not a result, per rule 4).

**Control (U2, rule 3): shuffled order, seed 1812, same 325 groups/207 distinct multiset.** Only
order-dependent statistics can differ; a per-token frequency figure is not a valid control here
(CLAUDE.md rule 3's bCAS paragraph) -- contacts/repeats are order-dependent, so this is a real test:

| statistic | target | shuffled (seed 1812) |
|---|---|---|
| recurring bigrams | 16 | 1 |
| longest repeat (tokens) | 3 | 2 |
| of top-20 tagged prefix/suffix-like | 9 | 1 |
| self-succession total (top 20) | 0 | 0 |

The target separates cleanly from its own shuffled-order control on every statistic that order can
move (16 vs 1 recurring bigrams, longest repeat 3 vs 2, 9 vs 1 tagged groups): **contact-table
reading is licensed at N=325** (not "not licensed", the brief's fallback wording). One caveat found
by the control itself: the shuffle's lone tagged token (637, count 3) is a false positive of the
tag rule at low counts (its 2-way-split left context of {741:1, 1388:1} clears the 0.4 concentration
threshold on a denominator of only 2) -- the 9-vs-1 gap still holds, but a tag on a count-3 token is
weaker evidence than one on a count>=5 token, noted for any future use of this tag.

**Hypothesis (U3).** (1) The contact-table and repeat-count signal is real and licensed by the control
above (16 vs 1 recurring bigrams; 9 of the top 20 groups tagged), so this is a genuine nomenclator with
word/phrase-level structure, not noise. (2) The range-split test gives no clean single answer -- two
candidate low-block sizes (16 or 28 codes) both plausible for a spelling alphabet, neither showing the
sharply higher IC a tight monoalphabetic block would give (0.0395-0.0742 vs the 0.0026 flat-207-symbol
baseline, a real but modest lift) -- and a one-part-dictionary check (the ten most frequent groups'
range-position mapped against tools/data/fr18's word-type initial-letter distribution, one volume,
`mmoiresetlettre01margoog.txt.gz`, 11,256 types) scatters the two joint-most-frequent groups (918, 13,
both count 8) to opposite ends of the alphabet (predicted initials p and a) rather than clustering them
as the same handful of extremely common short function words would under a strict one-part-alphabetical
code. (3) Taken together, a code with a real internal structure but not a simple fully one-part-alphabetical
design is the better-supported working hypothesis (two-part, or blockwise one-part per Tomokiyo practice 3);
family choice stays open, pending a period key, not decided from these tables alone -- no grade above M
anywhere in this section.

Caveat on the one-part check: word-TOKEN initial-letter shares (not used here) are dominated by function
words ("je" alone was 3.8% of all tokens in the sample file); word-TYPE shares (used here) are closer to a
dictionary's own headword distribution but still not a real period dictionary's page layout -- `--onepart-dict`
(Tomokiyo C2, still not built into freq.py) wants an actual period dictionary's headword-initial counts, not a
running-text corpus's, before this check is more than a rough lead.

**Bazeries probable-phrase list (LIST, not a run -- no group assigned a value).** From
`scripts/letters.json`'s 34 Chuquet Dec-1812 Berthier-to-Napoleon letters (computed cross-corpus doc
frequency, since XIX and XXIII -- the only two actually dated 22 Dec -- share just one 3+-word phrase
between themselves, "commandement de la"; the other nine are phrases the subject, a Berthier
dispatch of this campaign, plausibly contains, ranked by how many of the 34 letters use them).
Excluded: "la guerre de russie" / "guerre de russie" (12/34 by raw count) is a page running-header
OCR artifact bleeding into the extracted text ("y LA GUERRE DE RUSSIE 197" mid-sentence in XIX, "200
LA giehrk de Russie" in XXIII), not real letter content -- flagged, not used as a crib.

| phrase | doc freq (of 34) | syllable decomposition | units | repeats.tsv match at this length? |
|---|---|---|---|---|
| à votre majesté | 18 | à / vo-tre / ma-jes-té | 6 | no (no exact 6-gram repeat; near-repeat check only built at length 3) |
| de la division | 14 | de / la / di-vi-sion | 5 | no (no exact 5-gram repeat) |
| duc de tarente | 13 | duc / de / ta-ren-te | 5 | no |
| du duc de | 13 | du / duc / de | 3 | yes, but not diagnostic -- two exact 3-gram repeats and 41 near-repeat 3-gram pairs exist at N=325, none identifiable as this specific phrase without a key |
| la division heudelet | 11 | la / di-vi-sion / heu-de-let | 7 | no (no exact 7-gram repeat) |
| le duc de | 10 | le / duc / de | 3 | yes, same caveat as "du duc de" (same length, indistinguishable from it this way) |
| de votre majesté | 9 | de / vo-tre / ma-jes-té | 6 | no |
| que votre majesté | 8 | que / vo-tre / ma-jes-té | 6 | no |
| commandement de la | 1 (shared XIX/XXIII only) | com-man-de-ment / de / la | 6 | no |
| que je reçois | 7 | que / je / re-çois | 4 | no (no exact 4-gram repeat) |

No source letter is confirmed for this cryptogram (NOTES.md's Y9/BBER sections: the XIX/XXIII pairing
is explicitly unconfirmed, and the LANE R7 crib test's best length-fit candidate is XXIX, 28 Dec, not
either 22-Dec letter) -- so "position compatible with the clear letters' order" cannot be checked
against any single hypothesised source text; the yes/no column above answers only "does a matching-length
repeat structurally exist in the ciphertext at all", not "does this specific phrase's position match".
Grade: none of this is graded above M (rule 4); nothing here is a reading.

**NEXT-STEPS.tsv regenerated** (`python3 tools/next_steps.py`). Named next step: a family run gated
by this hypothesis -- `tools/family_run.py --family homophonic` (or a two-part/blockwise variant once
one exists) on the target with the range split reported above as a starting constraint, matched control
first (rule 3), not a further contact-table pass at this N. Status stays `open`; no "solved", "new",
"first", "unpublished" anywhere in this section.

## BER-HOMO (27 Sept 2026, parent worker BER-HOMO)

Ran BER-KWIC's named next step: `tools/family_run.py --family homophonic` at the spec's own N=325, K=207,
matched control before any target attempt (rule 3).

**Which ciphertext.** The spec's own `ciphertext` field is not data: it is a prose pointer string ("ciphers/
berthier-napoleon-1812/ciphertext_full.tsv ... use this file, not ciphertext.txt"), and `family_run.py` reads
that sentence literally as 41 space-tokens/38 distinct if given no override -- a real defect in the spec for
this kind of run (same "which file" shape BER-KWIC flagged for `ciphertext.txt` vs `ciphertext_full.tsv`, not
fixed here, read-only per this job's brief). Used `--cipher ciphers/berthier-napoleon-1812/structure/flat.txt
--tokens space` (BER-KWIC's own settled 325-token/207-distinct flat reading, already checked to match
`ciphertext_full.tsv` exactly) to get the spec's real N/K into the tool: dry-run confirmed N=325, K=207 before
the real run.

**Range-split parameter.** Checked `tools/family_run.py --help` and `tools/families/homophonic.py`'s own
docstring: the family accepts `--param profile=target`, `--param noise=p` and (units mode only) `--param
units=syl`, no parameter for a range-based starting constraint (BER-KWIC's low/high split at 236 or 140). Ran
plain, as the brief allows when no such option exists. **Wanted:** a `--param` (or a `masc`/`homophonic`
sub-mode) that seeds or constrains the anneal's letter/homophone assignment from a named low-value code block,
so a range-split hypothesis like BER-KWIC's can be tested directly rather than only informally motivating which
family to try -- named here, not built (script-only box).

**fr18 era match, checked per brief (do not build a corpus this box).** `tools/data/fr18` is 1680-1790
diplomatic/official French; the target is 22 Dec 1812, a 22-132-year mismatch already flagged in the spec's own
judge block. `tools/data/fr19` exists on disk (README: "French prose 1800-1890") and does bracket 1812 in date,
nearer than fr18 -- but it is five Project Gutenberg novels (Stendhal, Balzac, Flaubert, Maupassant), a fiction
register, not the official/military-dispatch register this target needs (fr18's own register, wrong era), and
it is not wired into `judge_plaintext.py`'s `LANG_CORPORA`, so a spec cannot opt into it without a `judge.corpora`
edit. No French corpus on disk matches both the 1800-1820 era and an official/military register; building one
is out of this box's scope, named as the next step for a future breadth pass.

**Control (rule 3, before any target).** `--seed 1 --seeds 3 --restarts 8` (defaults), corpus = the spec's own
fr18 judge corpus (six files, per the dry-run above):

| seed | control N | control K | recovery | score |
|---|---|---|---|---|
| 1 | 325 | 165 | 0.062 | -625.88 |
| 2 | 325 | 171 | 0.062 | -633.07 |
| 3 | 325 | 171 | 0.058 | -632.86 |

CONTROL mean 0.061 (range 0.058-0.062), gate 0.6 **NOT met** -- `CONTROL BELOW GATE`, exit 3, target never run.
Row appended to `HYPOTHESES.md` (real run only; the timing probe's throwaway row/decode file, written to
`/tmp` and a since-deleted `families/` file during a 1-seed dry timing check, were not committed).

**Reading (rule 3).** The homophonic-substitution family is untestable at N=325, K=207 with this solver: a
non-test, not a negative, matching the spec's own structural caution (Bourdeau's ~1200-entry-nomenclator
objection quoted in `constraints`) and this repo's general finding that a solver needs far more redundancy per
symbol than 325/207 gives it (K is 89-105% of the corpus-drawn control's own effective K here, i.e. almost no
sign repeats homophone-style at this N). Named next instrument, per the brief: a two-part/blockwise code family
(no such family exists in `tools/families/` yet; `SYSTEM.md` "Tools wanted" is the place to log it) -- not a
further homophonic re-run with other parameters or restarts at this same N (CLAUDE.md rule 3's "second attempt
at an unchanged approach" paragraph).

Status stays `open`. No "solved", "new", "first", "unpublished" anywhere in this section.

## Web and blog check (WEBCHECK-berthier-napoleon-1812, 1 Oct 2026)

The required open-web and blog comment-thread step (`.claude/briefs/check-solved.md`, CHECK-SOLVED-WEB, 28 Sept 2026),
run 1 Oct 2026 23:35-23:45 UTC by the account-4 WEBCHECK worker, brief `.claude/briefs/runs/2026-10-01-account4-webcheck.md`.
Every query and every hit is listed; "no decipherment" below is a search result, never a novelty verdict (CLAUDE.md rule 10).

**(a) Plain web searches (WebSearch, 8 queries).**

| # | Query | Result |
|---|---|---|
| 1 | `Berthier Napoléon 22 décembre 1812 chiffre déchiffré` (sender + recipient + date) | 10 results: Archives nationales Fonds Berthier finding aid (FRAN_IR_001908, not opened -- a PDF inventory, no decipherment indexed), Lehning's futura-sciences post (opened, below), napoleon.org / napoleon-series.org Berthier biographies, bibmath Grand Chiffre page (opened, below), mmbennetts "Le Grand Chiffre" post (opened, below), Wikipedia. No decipherment or plaintext of this letter. |
| 2 | `"Chiffre du Prince de Neufchâtel" OR "Primata a été déchiffrée"` (the leaf's own distinctive clear-text note) | 9 results, none about a cipher: Bataillon du prince de Neuchâtel, the US privateer *Prince de Neufchatel*, Louvre ornament "Chiffre de Monsieur le Prince", "prince-primat" dictionary entry. Zero hits for either phrase in a cryptographic sense. |
| 3 | `Berthier Napoleon 1812 cipher letter Vilcoq "Le Chiffre sous le Premier Empire"` (shelfmark/source + "cipher") | 10 results: Lehning post, napoleon.org biography, Carter Church's Marmont 1809 writeup (opened, below -- cites Vilcoq 1969 as *its* plate source too), derekbruff.org Napoleon crypto page, jfbouch.fr codebook index (opened, below), bibmath, Wikipedia Great Cipher. None names the 22 Dec 1812 letter. |
| 4 | `Berthier to Napoleon 22 December 1812 unsolved cipher code "918 1045 1100"` (folder's descriptive title + opening groups) | 9 results, none carrying the group string: napoleon-series.org biography, UNL "Napoleon Bonaparte Letters" project, jfbouch.fr "Missives using a Small Cipher" (Berthier-Augereau **1813**, Bazeries' decipherment -- a different letter and code, not opened beyond the index), jfbouch "complete codebook 1815", Wikipedia. |
| 5 | `Berthier Napoleon 1812 cipher solved Claude OR GPT OR "solves"` (model-solve announcements, check-solved.md) | 9 results: all the model-solve traffic is Carter Church's GPT-6 Astra solution of the **Marmont 1809** letter (x.com/CarterWChurch, coinbureau, AGTPinsights, runtimewire.com, zamin.uz, 18 Sept 2026), confirmed by Tomokiyo -- not this letter; plus github.com/NoAutopilot/cipher-lab (this repository) and the Malet coup Wikipedia pages. No announcement of a Berthier 1812 solve. |
| 6 | `Berthier Königsberg "22 décembre 1812" "note chiffrée" OR "lettre chiffrée" Napoléon` | 10 results: napoleon.org Correspondance générale introductions/chronology (t.12, 1812), napoleon-histoire.com "Correspondance de Napoléon Ier - Décembre 1812" (opened, below), Catawiki 1811 Berthier autograph, SHD BB8 inventory PDF, cairn Napoleonica. No decipherment. |
| 7 | `"Berthier" "1812" cipher transcription Tomokiyo "code size" 1200 unsolved` | 10 results: this repository, dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers and two forks of cyphersolver (setsunaatto, arya1515 -- forks of the repo already grepped by CX2, 25 Sept; not re-cloned), Carter Church Marmont writeup and its press echo, a 1591 Spanish-cipher Cryptologia abstract, D'Agapeyeff Wikipedia. No decipherment. |
| 8 | three `site:` searches for the blogs (see (b)) | -- |

**(b) The three blogs, by name.**

- **Cipherbrain** (scienceblogs.de/klausis-krypto-kolumne): `site:` WebSearch for `Berthier Napoleon 1812` returned only generic pages (Top-25 "wahrscheinlich gelöst" Teil 2, the Top 50 list, "Kryptografen aller Nationen" 1800s cryptogram, Columbus signature, Freimaurer-Buch -- titles unrelated; not opened except the Top 50 list). The blog's own search `?s=Berthier`: "Wir konnten leider keine Beiträge finden" -- **zero posts**. `?s=Napoleon+1812`: two posts, both Klaus Schmeh 22 June 2021, "Eine verschlüsselte Depesche aus dem Jahr 1812 und ihre spannende Geschichte" and its English twin "A coded dispatch from 1812 and its exciting story" -- opened both: the dispatch is Clarke (War Minister) to Caffarelli, Paris, 19 Oct 1812, Spanish-campaign Grand Chiffre, decoded by Karsten Hansky; German thread read in full, 14 comments (SantaColoma, Esme, Hansky x4, Norbert x3, Thomas, Schmeh; 22 June - 3 July 2021), English version has comments disabled (0); **no comment mentions Berthier, 22 Dec 1812, Königsberg, Neufchâtel or Vilcoq**. "The Top 50 unsolved encrypted messages" list page opened: no Berthier/Napoleon/1812/Vilcoq entry.
- **Cryptiana blog** (cryptiana.blogspot.com) and Tomokiyo's pages: on-disk snapshot `sources/cryptiana/` grepped first (zero requests): `web/unsolved.htm`, `web/unsolved-2026-09-24.htm`, `web/napoleon2.htm`, `web/henryiii.htm` name Berthier (already read by CX2, 25 Sept); `blog/` snapshot has no Berthier post. `site:cryptiana.blogspot.com Berthier Napoleon` WebSearch returned no blogspot result at all (engine returned Wikipedia). Blogger's own search `cryptiana.blogspot.com/search?q=Berthier`: **one post**, "Coded Letters of Admiral D'Estaing (1779) and Marshal Berthier (1812) Transcribed", 1 Oct 2025, https://cryptiana.blogspot.com/2025/10/coded-letters-of-admiral-destaing-1779.html -- opened and read in full; its whole sentence on this letter is: "I also uploaded my transcription of the available page of a letter of Marshal Berthier to Napoleon (1812). The code size appears to be 1200 and it would be difficult to solve analytically with this specimen." A transcription, no decipherment, no plaintext, no key; **0 comments**. Blog RSS feed (25 most recent posts, 12 July - 1 Oct 2026) read: no post title or description names Berthier, Napoleon, 1812, Neufchâtel or Vilcoq. Live `cryptiana.web.fc2.com/code/unsolved.htm` (page footer "Last modified on 27 September 2026", later than our 24 Sept snapshot) section "Encoded Letter from Berthier to Napoleon (1812)" re-read: no "Solved" marker (the page marks solved items with one), no solver, no plaintext. Live `code/napoleon2.htm` ("last modified 24 September 2023") section "Napoleon-Berthier Code (December 1812)": ciphertext only, no plaintext, no 2025/2026 update. (`cryptiana.web.fc2.com/web/napoleon2.htm` is a wrong path, 302 to fc2's 404 page; the pages live under `/code/`.)
- **Cipher Mysteries** (ciphermysteries.com): `site:` WebSearch for `Berthier Napoleon 1812` returned only unrelated posts (Nageon de l'Estang, La Buse, Toussaint, Voynich) plus Wikipedia -- titles unrelated, not opened. The blog's own search `?s=Berthier`: "Nothing Found" -- **zero posts**. `?s=Napoleon+chiffre`: "Nothing Found".

**(c) Plausible hits opened and their comment threads.**

| Hit | What it says about this letter | Comments |
|---|---|---|
| Hervé Lehning, "Le déclin de l'art de chiffrer sous Napoléon Ier", blogs.futura-sciences.com/lehning, 2 Feb 2019 | Nothing on 22 Dec 1812; its Berthier material is a Sept 1813 dispatch enciphered inconsistently in two copies ("the two messages are intercepted, the enemy can begin to decrypt them"). No Vilcoq, no Neufchâtel, no Primata. | 0 |
| M.M. Bennetts, "Le Grand Chiffre...or am I talking in code?", mmbennetts.wordpress.com, 5 Dec 2012 | General Scovell / Peninsular Grand Chiffre post; no Berthier 1812. | 8 (Monajem, Grace, Rappleyea, Bennetts x3, Ferguson, Cumming; Dec 2012 - Feb 2014); none names Berthier or this letter. |
| Carter Church, "Breaking the Marmont Cipher, 1809", carter.church/writeups/the-letter-to-marmont/ (18 Sept 2026) | Cites "J. Vilcoq, 'Le Chiffre sous le Premier Empire,' Revue historique des Armées" as the Marmont plate's source -- the same six-page article that carries our plate on p.24; mentions no Berthier, no 22 Dec 1812, no other unsolved Napoleonic cipher. | none (no comment section) |
| J.-F. Bouchaudy, "The codebooks of Napoleon I", jfbouch.fr/crypto/napoleon/index.html | Index read by script (curl 200 after two WebFetch 503s): the 1812 Spanish-campaign codebook (groups to 1400), Clarke-Caffarelli 1812, Bazeries' decipherments of the Emperor-Davout 1813 Great Cipher and a Berthier-**Augereau 1813** small cipher, the 1815 complete codebook, Scovell. No Berthier-to-Napoleon 22 Dec 1812 item; links out to Tomokiyo's napoleon2.htm. | none |
| bibmath.net "Le Grand Chiffre de Paris" | Peninsular War Grand Chiffre; the only deciphered example is Joseph to Marmont. No Berthier 1812, no comments section. | none |
| napoleon-histoire.com "Correspondance de Napoléon Ier - Décembre 1812" | Prints Napoleon's letters of December 1812 incl. one to the Prince de Neuchâtel dated 30 Dec 1812; the fetcher reported no "note chiffrée" wording on the page (Tomokiyo's napoleon2.htm says the 30 Dec letter acknowledges "votre note chiffrée" -- the two readings were not reconciled here; a reply acknowledging a cipher note is not a decipherment either way). No deciphered 22 Dec text. | none |
| Cipherbrain Clarke-Caffarelli 1812 posts (DE+EN), 22 June 2021 | see (b) | 14 + 0, none on this letter |
| Cryptiana blog post 1 Oct 2025 | see (b): transcription only | 0 |

Not opened, with reason: FRAN_IR_001908 (AN finding-aid PDF, an inventory, cannot carry a blog-style decipherment; the AN
fonds itself is a named next step elsewhere in this file); jfbouch `ex_ptt_chif.html` (Berthier-Augereau 1813, different letter and
code); Cipherbrain's unrelated-titled search-engine hits (Top-25 Teil 2, Kryptografen aller Nationen 1800s, Columbus, Freimaurer);
Cipher Mysteries' unrelated-titled hits (Nageon, La Buse, Toussaint, Voynich); the x.com / runtimewire / zamin.uz Marmont-Astra press
echoes (all about the 1809 Marmont letter, per their own titles and snippets).

**Result.** No decipherment or plaintext of this item located by these queries on 1 Oct 2026. Status word on line 1 stays `open`.
The one new fact for this folder: Tomokiyo's blog dates his transcription upload of "the available page" of this letter to
1 Oct 2025 (the `unsolved.htm` text our `ciphertext.txt` follows), and the live `unsolved.htm` of 27 Sept 2026 still lists it unsolved.

Requests this section: WebSearch 10 (8 plain + 3 `site:`, one duplicate counted once); scienceblogs.de 5 (2 searches, Top 50 list, 2 posts);
ciphermysteries.com 2; cryptiana.blogspot.com 3 (search, post, feed); cryptiana.web.fc2.com 3 (one 302 to fc2's 404, two pages);
blogs.futura-sciences.com 1; mmbennetts.wordpress.com 1; carter.church 1; jfbouch.fr 4 (WebFetch 503 twice, curl 200 twice -- the host
answered curl's descriptive UA and not the fetcher; no further requests); bibmath.net 1; napoleon-histoire.com 1. All one at a time,
>= 1.5 s apart, no 403/429/challenge pages. No subagents, no transcription, no decoding.

Intake gate re-run after this section:
```
berthier-napoleon-1812: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## BER-FRCORP (1 Oct 2026, account-4)

Ran BER-HOMO's named next step: built `tools/data/fr1810`, an era- and register-matched French judge corpus for this
target, the way `tools/data/pt18` was built (V6-PTCORP). No solver family was run on the target (the homophonic
control is BELOW GATE at N=325/K=207 regardless of corpus, HYPOTHESES.md; the corpus is for the next instrument, a
two-part/blockwise code family, SYSTEM.md "Tools wanted").

**Corpus.** Six Internet Archive `_djvu.txt` volumes of three works, 1800-1811 official/military French:
Correspondance de Napoléon Ier tomes XI, XVI, XX (1805-10; 1858-70 edition), Correspondance du maréchal Davout
tomes II and III cut before 1812 (Mazade 1885), Lettres inédites de Napoléon Ier tome I (an VIII-1809, Lecestre
1897). 4,820,645 letters after fold(), largest file 21.1 pct, cross-corpus word coverage 0.923-0.962 per file.
Deliberately excluded: tomes XXIII-XXIV (Napoleon's 1812 letters, including the 30 Dec 1812 reply to Berthier read
in the BBER section), Davout's 1812-13 letters, Chuquet 1912, anything from Dec 1812 -- the target's own month and
correspondents would make the judge circular. Every cut line is in `tools/data/fr1810/MANIFEST.tsv`; the README
records the sources, the trimming and the two checks. 18 archive.org requests, one at a time, >=1.5 s apart.

**Reliability (rule 3, blended AND per-fold, both corpora at the target's own N=325; `tools/data/fr1810/
holdout_check.py`, full log `holdout_2026-10-01.log`):**

| corpus | blended real-prose false-negative rate | per-fold spread (6 folds) |
|---|---|---|
| fr1810 (1800-1811, this job) | 234/1200 = 19.5% | 2.0 / 4.0 / 13.5 / 15.5 / 23.0 / 59.0% (29.5x) |
| fr18 (1680-1790, the spec's current judge corpus) | 244/1200 = 20.3% | 0.0 / 0.5 / 3.0 / 3.0 / 20.0 / 95.5% |

The blended rates are the same within noise; the shapes differ (fr18's rate is almost entirely its one newspaper
fold, the 1786 Gazette, at 95.5 pct; fr1810's worst fold is Correspondance tome XX at 59 pct, the file with the
lowest word coverage, four other folds sit at 13.5-23 pct). By rule 3's es17c/EN-FOLDS paragraphs a FAIL/PASS
against either corpus at N about 325 is of unknown reliability on the blended number alone; fr1810 is the matched
corpus this folder asked for, not a more reliable gate than fr18 at this N, and a verdict against it is reported
with the per-fold spread beside it, a FAIL close to the gate as "judge cannot decide".

**Wiring.** `LANG_CORPORA["fr1810"]` in `tools/judge_plaintext.py` (own key, the pt18/fr18 pattern; `fr` still
fr16); `specs/berthier-napoleon-1812.json` gets a `judge_note` naming the corpus, its judge block unchanged so the
recorded cheap_test_done and HYPOTHESES.md results stay reproducible; row in `tools/data/README.md`; offline test
`tools/tests/test_judge_plaintext_lang_fr1810.py` on a Davout letter of 23-24 Jan 1812 from the cut part of tome
III.

**Next step (one line).** Build the two-part/blockwise code family named by BER-HOMO and SYSTEM.md "Tools wanted",
with its matched control at N=325/K=207 drawn from fr1810, before any further judge run on this target; for the
corpus itself, a homogeneity split inside tome XX (by addressee or year) to find why that fold is the outlier.

Status stays `open`. No "solved", "new", "first", "unpublished" anywhere in this section.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/napoleon/NOTES.md ; TARGETS.md
- Their extent, in their words: attempted 15 Sept, "neither is solved"; blocked on one article (Vilcoq 1969), opening 325 groups only
- Their date: 15 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Premise check (GF4-berthier-napoleon-1812, account-4, 2 Oct 2026)

**Result: not found solved.** No decipherment, plaintext or applied key for this page located in (a)-(d) below;
(a) found nothing, (b) not found, (c) partly unreachable (the archive leaves), (d) not found in what was reachable.
Status word stays `open`. Run 2 Oct 2026 23:35-00:00 UTC (`date -u`), the adversarial pass of
`.claude/briefs/check-solved.md` "Premise check", trying to prove the item already done.

**(a) Decipherments the folder already mentions, opened. Not found.**
- *"La Primata a été déchiffrée"* (the plate's own margin note). Re-viewed the plate (`images/plate_t1_0024_0003_1.png`,
  1060x1429, the best Persée serves): no interlinear or marginal decipherment anywhere on the leaf. What the leaf carries:
  "Duplicata", a struck-out line, "Chiffre du Prince de Neufchâtel", "La Primata a été déchiffrée", an engraved
  "Sire," in clear, the Direction générale des Archives stamp, 22 lines of groups, and **a piece number "(3.)" at top
  right**, not recorded in this folder before. "Sire," in clear at the head means this is the first page of a letter;
  the continuation leaf (if any) is not reproduced by Vilcoq. The deciphered primata is not printed in any source
  opened; its home would be AN AF/IV/1643 plaquette 1/VI (below). **Not found** in print; the archive copy is unreachable.
- *Chuquet VIII, Wirballen 16 Dec 1812, "En chiffres."* (the one letter Chuquet prints as deciphered), opened
  (Chuquet 1912 3e série djvu.txt line 7379; fresh fetch this session): about 60 words, on Murat's incapacity to
  command; no "Sire". The Gotteri répertoire places this text at AF/IV/1643 plaquette **1/V** p.280 (Bourdeau's
  `an_ir.txt` line 353). Different date, different plaquette, about a fifth of the page's length: **not this item.**
- *Chuquet XI (Gumbinnen 18 Dec): "la note chiffrée que j'ai adressée à Votre Majesté par M. Atthalin"* -- a ciphered
  note sent before 18 Dec; Chuquet does not print it. **Not this 22 Dec item**, and not printed.
- *Napoleon's 30 Dec reply* (Corr. XXIV no.19408, "votre note pertes réelles", BBER) against Tomokiyo's "votre note
  chifrée": Google Books API exact phrase `"votre note chiffrée"` (country=US, keyed) -> 2 volumes, neither Napoleonic
  (Bulletin officiel 1998; Politica toscana e rivoluzione 1974, a 1796 Belleville letter). `"note chiffrée" "pertes
  réelles"` -> 338 loose matches, none on Berthier/1812 in the first 10. Lecestre, *Lettres inédites* t.2 (1810-15;
  IA `lettresindites02napo`, djvu.txt grepped): the December 1812 letters are nos.936-938 (2, 23, 29 Dec; Jérôme,
  Stéphanie), **none to Berthier**, no 30 Dec letter. Still unreconciled; no decipherment either way.
- A third Chuquet letter dated 22 Dec (`scripts/letters.json` key "X", line 9520 of the djvu.txt) is **Murat's**, not
  Berthier's: it is in the King of Naples' chapter and names "le prince major général" in the third person. Excluded.
  **Flag for whoever reuses the crib-test pool:** `letters.json` keys X and XI hold Murat's letters of 22/23 Dec (the
  extractor's Roman-numeral keys collided with the next chapter), so Y9/BBER's 34-letter control pool carries two
  non-Berthier letters and is missing Berthier's own X and XI. The Y9/BBER verdicts (no fit) do not depend on these
  two rows, but the pool should be rebuilt before it is used as a control again.
- Adversarial alignment glance at XXIII (the only long Berthier 22 Dec letter): "le général" sits at words 1, 51, 68
  against the cipher's repeated trigram 918 1045 1100 at groups 1 and 42, but XXIII's third words differ (Lagrange /
  Baillet-Latour) where the cipher repeats 1100, and the cipher's 493 359 (groups 4, 23) has no repeat in XXIII near
  words 4-26. No support for XXIII as the page's plaintext; consistent with Y9's gap-fit rank 30/34. No alignment claimed.

**(b) Other solvers' working files, not their status lines. Not found.**
- **Bourdeau**, fresh shallow clone HEAD 23416821 (2 Oct 2026 15:12 -0500), `targets/napoleon/` read file by file:
  `NOTES.md` (concludes "No alignment is proposed"), `berthier.py` (structure + compatibility stats only),
  `berthier_ct.txt` (the same 325 groups), `berthier_chuquet.txt` (Chuquet's Dec 1812 Berthier letters, clear),
  `profile.json` (plaintext "Candidate only ... no alignment made"; "attackable by analysis: no"), `an_ir.pdf/.txt`
  (the AN Gotteri répertoire AF/IV/1590-1670), `src/` (Chuquet 2e and 3e séries, *Lettres de 1812* t.1, *Ordres et
  apostilles* t.3-4). `grep -i chiffr` over every src file: only Chuquet VIII/XI (above), a general "quelques mots en
  chiffres" in the 2e série, "Raguse en chiffres" in *Ordres et apostilles* t.3 -- nothing on this letter. No output,
  rendering or key-application script for this text exists in his tree.
- **Aymeloglu**, fresh shallow clone HEAD d2800bb (27 Sept 2026): `grep -ri 'berthier|neufch|neuch|vilcoq|918 1045'`
  -> only a 14 Apr 1812 Soult-to-Berthier PARES catalogue row (AHN 3101921, Spain, partly ciphered), a DECODE postcard
  from Neuchâtel and Colbert-era "Neuchaise" rows. Nothing on this letter.

**(c) Physical neighbours. Not found where reachable; the archive leaves are unreachable.**
- The plate is a crop of one page; Vilcoq reproduces no facing page, continuation leaf or laid-in slip. Its
  neighbours on Persée p.24 (all read by IMG-FETCH): a "Tableau de chiffrement" fragment, Marmont 1807, Rapp 1813 --
  none is a decipherment of this page. Tomokiyo (`napoleon2.htm`, "A Great Cipher in the Archives") reads the
  tableau as a 1200-entry two-part code with Mediterranean-trade vocabulary and judges the Berthier code "different".
- The leaves on each side in the archive, AN **AF/IV/1643 plaquette 1/VI** ("Lettres et rapports adressés à l'Empereur
  par le major général depuis Gumbinnen puis Koenigsberg ... 17, 31 décembre 1812", Gotteri, via Bourdeau's an_ir.txt):
  not online as far as known, and archivesnationales.culture.gouv.fr does not load from the cloud (host table).
  **Unreachable** -- this is where the deciphered primata would sit.
- Same-family keys located while looking (premise-adjacent, none applied to this page by anyone found):
  "grand chiffre 34" (Berthier to Davout 7 May 1813 and Oudinot, printed with decipherments in Bazeries 1896 pp.19-36,
  entries to at least 1197, "et" = 197/413/534/821; Tomokiyo re-reconstructed it but did not print a table); the
  Napoleon-Davout code of Nov-Dec 1813 (Bazeries 1896 p.37 ff., "et" = 10/18/834/1128); code F 18 of 1815 (Bouchaudy,
  SHD 1M 2352); Tant's three 1200-entry "code inconnu" PDFs (archives.crypto.free.fr/367-369.pdf: **HTTP 404**;
  Wayback CDX connection reset twice -> unreachable). A value check with a matched control (random 4-value sets from
  1-1200, 100,000 draws, `structure/flat.txt`): GC34 "et" set occurs 5x (p=0.031, all but one from 821), Nov-1813 set
  4x (p=0.068), F18 "du" 2x (p=0.27), F18 "cet" 1x (p=0.52); null mean 1.07. Four sets tested, so the best p is not
  significant after correction; GC34's seven syllable values in Tomokiyo's sample (334, 221, 944, 873, 664, 74, 159)
  are all absent. **Not a reading and not a negative**: the handful of published values cannot test a 1200-entry
  code; the real test needs Bazeries 1896's cipher/plain pairs (Verdict below).

**(d) Recipient side (Napoleon and his Secrétairerie). Not found.**
- Gotteri's répertoire of AF/IV/1590-1670 (the recipient's own archive): describes 1/VI's subjects (retreat, losses,
  Macdonald, Prussia), prints no text. Chuquet 1912 3e série is the edition of exactly this recipient carton
  ("archives nationales (A.F. iv. 1643)"): Berthier's 22 Dec letters there are XIX and XXIII only, neither marked as
  deciphered, while VIII is (above). *Correspondance de Napoléon* XXIV (read in full text by BBER): no decipherment.
  Lecestre t.2 (above): nothing. Google Books exact phrases `"Primata a été déchiffrée"` (2 hits: a 1918 French
  intercept file and an 1848 Wallachian dispatch, unrelated) and `"chiffre du prince de Neufchâtel"` (323 loose
  matches; the first 10 are Bazeries 1896, Pougens' *Mémoires*, dictionaries -- none prints this letter).
  *Correspondance générale* t.12 (Fondation Napoléon 2012) is not open online: **unreachable** for full text.
- Russian side (the code captured or the instructions found): Urban p.324 (via Tomokiyo) -- Berthier's instructions
  for a great cipher in RGVIA, "apparently not the code itself". Not reachable from here; not a decipherment either way.

Requests this section: archive.org 4 (Chuquet 3e série djvu.txt, 2 advancedsearch, Lecestre t.2 djvu.txt);
googleapis.com/books 6; archives.crypto.free.fr 3 (404); web.archive.org 2 (connection reset, stopped); gallica.bnf.fr
SRU 1; github.com 2 shallow clones (removed after grep). All one at a time, >= 1.5 s apart, no 403/429/challenge.

**Gate.** Before: `berthier-napoleon-1812: open (line 1) passes the citation and web/blog checks but has no '## Premise
check' section ...` exit=1. After this section:
```
berthier-napoleon-1812: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

**Verdict (GF4, 2 Oct 2026): keep going.** The NEXT-STEPS row's step (build a two-part/blockwise code family, matched
control at N=325/K=207 from fr1810) was **not run**: a new `tools/families/` module with its offline test, SYSTEM.md
entry and a 3-seed control is about USD 10-15 and 60+ minutes, over this job's USD 7.5 / 40-minute box. Before anyone
builds it, check the control's own headroom (rule 3, Salviati paragraph): a 1200-entry code at 64% hapax may read near
floor by construction, which would make the family a non-test here. Steps in order:
1. **[ ] GC34 known-key test** (new, cheaper, uses key material rather than cryptanalysis): rebuild the "grand chiffre
   34" partial key from Bazeries 1896 pp.19-36 (Berthier to Davout 7 May 1813, Oudinot; cipher with printed plain,
   grade C) and the Nov-Dec 1813 Napoleon-Davout code from pp.37 ff., then apply each to `structure/flat.txt` with a
   shuffled-key control; also ask whether the 1812 page's repeated pairs (821 791 x3, 918 1045 1100 x2) fall on
   GC34 values. Access: Google Books volume `fIAuAAAAYAAJ` is full view (74 pp.), but books.google.com page/text view
   is captcha-blocked from the cloud (host table) -> a LOCAL-QUEUE row for the owner's runner to save pp.19-50 (run
   `tools/key_livecheck.py` first, per the access playbook), or HathiTrust from the owner's machine. ~USD 4 once the
   pages are on disk.
2. **[ ] Two-part/blockwise code family** as named in NEXT-STEPS, ~USD 10-15, after the headroom check above.
3. **[ ] Rebuild the crib-test pool** (`scripts/extract_chuquet_letters.py`) so keys X/XI are Berthier's, not Murat's;
   cheap (script only, ~USD 1); needed only before the pool is reused as a control.
4. AF/IV/1643 plaquette 1/VI (the deciphered primata) -- needs-physical-access or an AN reproduction order; owner-side.

## GF4b: GC34 key-rebuild routes and crib-pool rebuild (GF4b-berthier-napoleon-1812, account-4, 2 Oct 2026)

**(1) GC34 tables (Bazeries 1896, Google Books `fIAuAAAAYAAJ`): no cloud route gives them; LOCAL-QUEUE row L38 filed.**
Routes tried, in order:
- archive.org advancedsearch `Bazeries`: 3 hits (two Byte 1983 scans, a Friedman letter about Candela's book), no
  Bazeries book. be-api fts `"chiffres secrets dévoilés"`: hits are secondary literature only.
- Gallica SRU `dc.creator all "Bazeries"`: two items, *Les chiffres secrets dévoilés* (1901, `ark:/12148/bpt6k325768q`) and
  *Le Masque de fer* (1893). Gallica `gallica all "chiffres de Napoléon"`: nothing by Bazeries. The 1896 item is not on Gallica
  under either query.
- Bazeries 1901 checked as a stand-in: ContentSearch counts `chiffre` 218 and `Napoléon` 36 (controls), `Berthier` 5,
  **`Davout` 0, `Oudinot` 0, `1812` 0**. Its chapter "Chiffres de Napoléon Ier" (pp.151-196) read through Gallica's ALTO OCR
  (`RequestDigitalElement?E=ALTO`, PAG_163-188 -> `bazeries1901/alto_p163-188.txt`; PAG_184 answered HTTP 429, after which
  this worker stopped calling Gallica). It prints two examples: Berthier to Augereau, Péterswald 17 Sept 1813, primata and
  duplicata with a value-by-value translation (PAG_167-168), and Rapp from Danzig, 6 Nov 1813 (PAG_181 ff.). Both are in the
  **petit chiffre**, with values up to 177. That is not the 1812 page's code family (its values run to about 1200), and none
  of the GC34 (Davout/Oudinot) material appears. The file is kept because PAG_168 is grade-C cipher/plain material for the
  1813 petit chiffre and a future target could use it. It is not applied here.
- HTRC Extracted Features: not tried. It gives per-page bag-of-words counts only, so it can locate pages but cannot rebuild a
  table. Its only use would have been to find a HathiTrust copy of the 1896 book, and the request cap had been reached.
- Not tried, cheaper than L38 and worth doing first: J.-F. Bouchaudy's "The codebooks of Napoleon I"
  (jfbouch.fr/crypto/napoleon/, NOTES.md web check) lists "Bazeries' decipherments of the Emperor-Davout 1813 Great Cipher".
  A cloud worker should open that sub-page and check whether it prints a value table before the owner's runner reads L38.
  This job did not open it because it had reached its request cap.
- `tools/key_livecheck.py` (2 Oct 2026): `Google Books (googleapis.com/books/v1) | yes | yes | HTTP 200, totalItems=352`. The
  API works, but books.google.com page and text view are captcha-blocked from the cloud (host table), and no credential
  changes that. Hence LOCAL-QUEUE **L38** (edition-read, pp.19-50 of `fIAuAAAAYAAJ`). No ASKS row: the queue row is the
  owner's runner's input, and the row format does not need one.

**(2) Crib-test control pool rebuilt.** The pool was worse than flagged. `letters.json` v1 had nine Murat letters (II, III, IV,
VI, VII, VIII, IX, X, XI), not two, because the extractor's line range (7100-9600) ran into Chuquet's note 46 "Murat à
Napoléon" (djvu line 8917). `scripts/extract_chuquet_letters.py` now defaults to note 45 only (lines 6365-8917). It maps the
OCR-damaged markers III and XXII, skips a stray header "V", drops the two Lefebvre-to-Berthier letters in the note, and
records each letter's source line. Result: 38 Berthier letters, I-XXXVIII. The v1 files are kept as
`scripts/*_v1_mixedpool.json`. Both pools' ranks for XIX, XXIII and XXIX are in HYPOTHESES.md ("Crib-fit control pool
rebuilt"): XIX 14/3/17 (was 15/3/18), XXIII 17/29/33 (was 18/29/30), XXIX 1/11/16 (was 1/12/17) of 38. The "no fit" reading
for XIX and XXIII stands. No candidate is a crib, and nothing is graded.

Requests this job: archive.org 3 (Chuquet djvu.txt 1, advancedsearch 1, be-api fts 1); gallica.bnf.fr 35 (SRU 2,
ContentSearch 7, ALTO 26, one of them HTTP 429, after which Gallica was not called again); `tools/key_livecheck.py`'s own
6 API probes. All requests were made one at a time, at least 1.5 s apart. No vision was used.

**Escalation, updated (GF4b):** step 1 is now (a) the Bouchaudy jfbouch.fr Davout sub-page, a cloud job of about USD 1;
then (b) LOCAL-QUEUE L38 (owner's runner), followed by about USD 4 to rebuild GC34 and apply it with a shuffled-key control.
Step 3 (crib-pool rebuild) is **done**. Steps 2 and 4 are unchanged. Verdict: keep going.

## GF4c: Bouchaudy's jfbouch.fr pages (GF4c-berthier-napoleon-1812, account-4, 3 Oct 2026)

Route GF4b named as cheaper than L38. Pages read (plain HTTP; HTTPS fails with a certificate/host-name mismatch from the
cloud, TLS checking not disabled): `crypto/napoleon/index.html`, `ex_grd_chif.html`, `ex_grd_chif.fr.html`, plus HEAD
requests on three table images. Snapshots unmodified in `sources/jfbouch/2026-10-03/` (credit: J.-F. Bouchaudy, "The
codebooks of Napoleon I"; text there is Bazeries 1896 pp.38-47, rule 8). Requests: jfbouch.fr 7 (4 GET incl. one failed
HTTPS, 3 HEAD), at least 1.5 s apart. No vision.

- **GC34 not there.** The "Great Cipher" page reproduces only the Napoleon-Davout code of Nov-Dec 1813 (Davout's letters
  of 14 Nov, 19 Nov and 1 Dec 1813, cipher with Bazeries' translation; in service 23 Aug to 1 Dec 1813 per Bouchaudy).
  Bouchaudy says he rebuilt that key but did not publish it. Nothing from Bazeries 1896 pp.19-36 (Berthier-Davout
  7 May 1813, the "grand chiffre 34") is on the site. **L38 stays the route for GC34.**
- **Nov 1813 Davout code tested anyway, with controls** (HYPOTHESES.md, "Napoleon-Davout Nov 1813 grand chiffre"; script
  `davout1813/value_overlap_test.py`, `--check` OK). Value-frequency overlap against Davout letter 1, shuffled-key null:
  positive control (Davout L2+L3, same code, N=325) S = 207-229 vs null 80, p = 0.00005 on 5 subsamples; **target S = 118
  vs null 79.7, p = 0.040**, the whole excess from two values (173, Davout's commonest group, only 2x here; 13, this page's
  commonest, 2x in Davout); without them S = 78. Control-backed negative for that one key: the page is not in the Nov 1813
  Napoleon-Davout code. No reading, nothing graded.
- **New key material found, not yet tested:** the index page shows the period deciphering table of the 1812 Spanish-
  campaign grand chiffre (SHD archives, partly reconstructed by Scovell; groups 0001-1200 plus manuscript additions to
  1400) as four images, `IMG/1812_0001.jpg`, `1812_0051.jpg`, `1812_0701.jpg`, `1812_0751.jpg` (about 470 KB each), and
  `IMG/1812_tout.jpg`. It is a period key image (values would be H if applied), and a 1200-group code of 1812 is the same
  size class as this page (values to about 1200, with 1202, 1238 and 1388 above). Different theatre (Spain, not Russia),
  so the prior is low, but it is a full table and the test is cheap.

### GF4c: open steps (target is `open`, not `partial`)

1. [ ] Spanish-campaign 1812 grand chiffre (Bouchaudy's images of the SHD table) against this page: transcribe the
   table rows for this page's ~200 distinct values from the four images, apply, value-overlap plus readability check with
   a shuffled-key control; next: one vision-capable worker, line crops via `tools/iiif_lines.py --image`, ~$4.
2. [ ] GC34 (Bazeries 1896 pp.19-36): waiting-on LOCAL-QUEUE L38.
3. [ ] Two-part/blockwise code family (GF4 step 2), ~$10-15 after the headroom check.
4. [ ] AF/IV/1643 plaquette 1/VI deciphered primata: needs-physical-access.

### GF4c: next

Tried this pass: Bouchaudy's Davout page (Nov 1813 code: negative with controls). Next in order: gap 1 (cloud, ~$4),
then gap 2 when L38 lands. Verdict: keep going.

## GF4d: the SHD 1812 grand chiffre table reads this page (GF4d-berthier-napoleon-1812, account-4, 3 Oct 2026)

**Key source.** The deciphering table ("Pour déchiffrer", codes 1-1400) of the grand chiffre used in the 1812 Spanish
campaign, held at the SHD and photographed and published by **J.-F. Bouchaudy** on jfbouch.fr
(`http://www.jfbouch.fr/crypto/napoleon/IMG/1812_tout.jpg`, `_0001`, `_0051`, `_0701`, `_0751`; index page snapshot
`sources/jfbouch/2026-10-03/`). Fetched 3 Oct 2026 by this worker: 5 image requests plus 1 page
(`complet_1815.html`, checked for a text-form table for a positive control; it has images only), 1.6-2 s apart,
descriptive UA, all HTTP 200. Key class `published` (Bouchaudy's images of a period table), credited to him (rule 8).
Files: `shd1812/` (images, `grid.py` + `cut.sh` grid detection and crop cutting, `crops/` 140 one-cell crops).

**Crop step (pasted, Usage 6).** One `tools/iiif_lines.py` run per table column strip, cell centres as `--centres`
so each crop is one 10-code cell, e.g.
`python3 tools/iiif_lines.py --image ciphers/berthier-napoleon-1812/shd1812/1812_0001.jpg --out ciphers/berthier-napoleon-1812/shd1812/crops --region 335,315,554,2381 --centres 271,742,1206,1677,2132 --lines-per-crop 1 --prefix h00a`
(all 28 commands: `sh shd1812/cut.sh`). Crop `hHH{a|b}_L0r` = codes HH*100 + (a:0, b:50) + (r-1)*10 + 1..10.

**Code-range overlap (checked first).** Table 1-1400 (1-1200 base, 1201-1400 later additions); target 2-1388, all 207
distinct codes inside it (three above 1200: 1202, 1238, 1388). Full overlap, so the test ran.

**Transcription.** Only the 108 cells holding the target's 207 distinct codes were read. Two blind Opus passes, each two
subagent calls (one per page of the table: codes 1-700 / 701-1400; 59 and 49 crops), so four vision calls in all,
`shd1812/passA_{L,R}.tsv`, `passB_{L,R}.tsv`; plus this worker's reconciliation of the disagreements from row-level crops.
The brief asked for one image per call; a call covered one table page (two photographs) instead, to stay at four calls.
First-form agreement 191/207 (92.3%); the 16 splits were settled by eye (`settled=R` in the key). 851 is under a fold in
the paper and stays unread. Key: `shd1812/key_shd1812.tsv` (207 rows; conf H = both passes H, 135 rows).

**Test (rule 3).** `shd1812/known_key_test.py` (`--check` passes): decode the 325 tokens with the key (first form of each
entry), score with the 4-gram model of `tools/judge_plaintext.py` on `tools/data/fr1810` (era-matched), against 200 keys
that reassign the same 207 entries at random to the same 207 codes. Positive control, same design/N/language: Berthier's
own Dec 1812 letters (Chuquet, `scripts/letters.json`, XIX and XXIII left out) encoded with a synthetic two-part code
(300 commonest words whole, others in 3-letter pieces, codes at random in 1-1400), N=325, 198 distinct, true key vs 200
shuffles, at 0/15/30% of key entries replaced by wrong ones.

| run | observed | shuffled mean | shuffled max | p (floor 1/201) |
|---|---|---|---|---|
| positive control, 0% key error | -0.836 | -1.206 | -1.092 | 0.005 |
| positive control, 15% key error | -0.907 | -1.188 | -1.067 | 0.005 |
| positive control, 30% key error | -1.125 | -1.247 | -1.136 | 0.005 |
| **target, SHD 1812 key** | **-0.866** | -1.061 | -1.002 | **0.005** |

The target scores between the control's 0% and 15% error levels and above every one of its 200 shuffles. The shuffles
cannot match the target by construction: the statistic depends on which entry each code gets. Judge (rule 7):
`python3 tools/judge_plaintext.py specs/berthier-napoleon-1812.json --file shd1812/reading_shd1812.txt`:

```
ok   language: score=-0.946, null_p99=-1.73, real_p05=-0.997, real_median=-0.836, mode=both, N=1099
ok   words: cover=0.949, min=0.5, real_text_median_cover=0.953
PASS - berthier-napoleon-1812 (a PASS is a gate for a verifier, not a reading; rule 10)
```

**Reading.** `shd1812/decode_shd1812.py` (`--check` passes) writes `shd1812/reading_shd1812.tsv` (per token, grade) and
`reading_shd1812.txt` (first forms, one line per plate line). Grades (rule 4): **H 193, M 131, I 1** of 325. Here H
means the table entry was read H by both blind passes, so it rests on a period key source *and* on this test showing the
key is this page's. Each entry's ending (e.g. "faire, s, ..."), word joins and the code's "un point / point et virgule /
alinea" punctuation have not been resolved into running French; that is the next step. The page opens (raw first forms):
"je n ait aucun Nouveau de votre Majesté de puis do n de par de pa ri S point et virgule je n ail aucun Nouveau direct
de France de puis les lettre du Ministre de sa Guerre du Cinq Octobre un point alinea je n ait ja mais Reçu ni ...
ni Etat de situation de l'armée du nord de l'Espag^ne ...". Later lines include: copies sent in quadruplicate of the
writer's dispatches from Salamanca, the last courier taken with the correspondence near Valladolid, an enclosed copy of
a dispatch from a general "ré..Il le" (Reille is a probable reading, not settled), the provinces of the North, and
"dans l'hypothèse où la guerre avec la Russie continuerait". It ends at the plate's end, mid-sentence ("et su[r]
Votre Majesté").

**Attribution question (raised here; not settled).** Vilcoq's 1969 caption gives the sender as Berthier, 22 Dec 1812. The
plaintext reads like a letter *from Spain* to the Emperor (Salamanca, Valladolid, the army of the North of Spain, no
news from France since the War Minister's letters of 5 Oct, the Russian war as a hypothesis), and its key is the
Spanish-campaign table. Berthier was with the Grande Armée in Russia/Poland in Dec 1812. The likeliest sender is someone
commanding in Spain who writes to Napoleon as "Votre Majesté [Impériale]" (King Joseph is one candidate). That is an
inference from content and has not been checked. Next: a check-solved pass on the corrected premise, reading Du Casse,
*Mémoires et correspondance du roi Joseph* (tomes VIII-IX) and the Spanish-front series for late 1812 against the
reading. Search so far (rule 10, a search result only): IA full-text (be-api) for "mes dépêches de Salamanque" (0 hits)
and "aucune nouvelle directe de France" (5 hits, none about this letter), 3 Oct 2026.

Request count: jfbouch.fr 6, be-api.us.archive.org 3. Cost: get_session exposes no cost figure for this session.

## Premise check (GAPS-berthier-napoleon-1812, 3 Oct 2026)

Job: the GF4d Verdict step ("check-solved on the corrected premise"). Searched interior phrases of the GF4d first-form
reading (`shd1812/reading_shd1812.tsv`), modernised into ordinary French, not only the opening. No vision calls.

**Result: the plaintext of this very item is in print.** Google Books API (`GOOGLE_BOOKS_KEY`, `&country=US`), quoted
phrase search, 3 Oct 2026. Four independent phrase queries each returned the same one volume,
**MdBnAAAAMAAJ = Vincent Haegele (ed.), *Napoléon et Joseph Bonaparte: correspondance intégrale, 1784-1818*, Tallandier,
2007, 895 pp., ISBN 9782847344653** (viewability NO_PAGES: snippets only, so the **page is not yet cited**). Snippets as
returned (Google's text, not our decode):

| query (quoted) | snippet from MdBnAAAAMAAJ | our plate (GF4d first forms) |
|---|---|---|
| Reille dépêche Valladolid courrier enlevé décembre 1812 (unquoted) | "... lettre conservée dans les archives du roi Joseph. Madrid, 22 décembre 1812. Je n'ai aucune nouvelle de V. M. depuis son départ de Paris. Je n'ai aucune nouvelle directe de France depuis les lettres du ministre de la Guerre du 5 ..." | lines 1-3 |
| "aucune nouvelle directe de France" | "... depuis les lettres du ministre de la Guerre du 5 octobre. Je n'ai jamais reçu ni compte, ni rapport, ni état de situation de l'armée du Nord, ..." | lines 2-4 |
| "Je n'ai jamais reçu ni compte" | "... quelles qu'aient été mes demandes réitérées à cet égard. J'adresse à V. M. I et au Ministre de la guerre à Paris des quadruplicatas de mes dépêches ..." | lines 4-7 |
| "enlevé avec toute la correspondance" | "... près de Valladolid. V. M. trouvera ci-joint copie d'une dépêche de M. le général Reille qui m'a paru de nature à être mise sous ses yeux. C'..." | lines 8-11 |
| "le général Reille qui m'a paru" | "... C'est la première prière de ce genre que je reçois : elle m'éclaire sur la position des provinces du Nord. Je savais bien qu'elle n'était pas bonne mais je ne la ..." | lines 11-14 |
| "comte Reille et à la droiture" | "... de ses intentions. Je conçois qu'il faut trouver un remède et voici ce que je propose à V. M. dans l'hypothèse où la guerre avec la Russie continuerait ..." | lines 18-22 |

So: sender **King Joseph** (not Berthier), recipient Napoleon, **Madrid, 22 December 1812** (Vilcoq's date stands), and
the printed clear text runs through to the plate's last line. The edition's source is Joseph's own archive copy, not the
Archives nationales cipher dispatch Vilcoq photographed; it is the same letter (same date, same sequence of sentences
across the whole plate). One wording difference seen so far: the print's "première prière de ce genre" where the
plate's table entry reads "lettre" (GF4d first form); not settled here (a snippet, possibly an OCR or editorial
reading). The SHD 1812 key test (GF4d) is independently confirmed by this: the key-read words match the printed letter.

**Not found (search results only, rule 10):**
- Du Casse, *Mémoires et correspondance politique et militaire du roi Joseph*, t. VIII and IX (archive.org
  `mmoiresetcorre08joseuoft`, `mmoiresetcorre09joseuoft`, `_djvu.txt` downloaded, grep for quadruplicata, déplorable,
  droiture, hypothèse, concentration, "départ de Paris", "5 octobre", Reille, Valladolid): this letter to the Emperor
  is **not** printed there. T. IX pp. 121-125 prints Joseph's companion letter to Clarke (duc de Feltre), Madrid,
  December 1812 (margin date garbled in the OCR), which encloses the same Reille letter and says the same thing in other
  words ("Je savais bien que les affaires dans le nord n'étaient pas en très-bonne situation, mais je ne les croyais pas
  en si mauvais état ... je n'ai même pas encore reçu d'états de situation de son armée").
- IA full text (be-api fts) for ten phrases: no hit on this letter (5 unrelated hits for "aucune nouvelle directe de
  France", others unrelated or 0).
- Google Books for the other phrases tried ("depuis son départ de Paris", "mes dépêches de Salamanque", "Sacrifices
  aussi grands", "concentration dont il est question", ...): no further hit beyond MdBnAAAAMAAJ.
- Bouchaudy, jfbouch.fr `crypto/napoleon/index.html` (snapshot `sources/jfbouch/2026-10-03/`, re-read, plus one live
  GET): the plate is not discussed; his 1812 material is the SHD table and a Clarke-Caffarelli letter.
- Correspondance de Napoléon Ier: not searched, since it prints Napoleon's outgoing letters and this is an incoming one.

Not a decipherment in print: nothing found that maps this ciphertext to the text (that question is the verifier's).
Requests: archive.org 3 (1 advancedsearch, 2 djvu.txt), be-api.us.archive.org 10, www.googleapis.com 23,
jfbouch.fr 1; at least 1.6 s apart.

Gate outputs (3 Oct 2026):

```
$ python3 tools/gaps_check.py berthier-napoleon-1812
OK keep-going berthier-napoleon-1812: keep going: 2 internal gap(s), 1 step(s) untried
gaps_check: 1 checked: 0 parked, 1 keep-going, 0 FAIL, 0 skipped
$ python3 tools/intake_gate_check.py berthier-napoleon-1812
berthier-napoleon-1812: found-solved (line 1) -- edition/page or full-text-search citation found within 6 lines
```

## Remaining gaps (GF4d, 3 Oct 2026; updated GAPS-berthier-napoleon-1812, 3 Oct 2026)
Read so far: 324 of 325 tokens have a table entry (H 193, M 131; shd1812/reading_shd1812.tsv); the plaintext is in print (Haegele 2007, Joseph to Napoleon, Madrid, 22 Dec 1812), so the page is found-solved.
- token 165 (code 851) - blocker: illegible; the table entry is under a fold in the photographed sheet (shd1812/crops/h08b_L01.jpg); next: read it off the printed text once the page is in hand (no new instrument needed)
- running-French rendering of the 324 entries - blocker: not-attempted; superseded in purpose, since the clear text is printed (Haegele 2007), so this is now a grade-C alignment of the GF4d first forms against the print; next: align once the printed page is in hand, ~$2
- printed page number for Haegele 2007 - blocker: not-attempted; Google Books gives snippets only (NO_PAGES) and its page view is captcha-blocked from the cloud; next: a LOCAL-QUEUE row for an owner-side look at the volume, or the verifier's own search, ~$1
Sender and date, settled 3 Oct 2026 (GAPS-berthier-napoleon-1812): King Joseph to Napoleon, Madrid, 22 Dec 1812, printed in Haegele 2007 (Google Books MdBnAAAAMAAJ).

## Escalation (GF4d, 3 Oct 2026; updated 3 Oct 2026)
- [n/a] siblings: the plate is a single page and no sibling cipher letter in this key is identified yet
- [n/a] clear-pages: no clear text accompanies the plate in Vilcoq's article
- [x] known-keys: SHD 1812 Spanish-campaign table (Bouchaudy's images) reads the page, p 0.005 vs 200 shuffled keys (GF4d)
- [x] print: the plaintext is printed in Haegele 2007 (Joseph to Napoleon, Madrid, 22 Dec 1812), found 3 Oct 2026 by Google Books phrase search
- [n/a] key-rebuild: a period key is in hand, so no rebuild is needed
- [ ] image-check: re-read the 16 reconciled M entries and token 851 against the printed text, not only the crops
- [n/a] retry: the first known-key test succeeded, so there is nothing to retry
Verdict: keep going: 2 internal gaps; cheapest next: the Haegele 2007 page number (LOCAL-QUEUE row or the verifier's search), ~$1
