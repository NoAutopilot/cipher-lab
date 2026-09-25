open
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
