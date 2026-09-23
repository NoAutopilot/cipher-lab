# Ernest and Joachim of Anhalt-Zerbst to Francis I, Latin, "presque entierement en chiffres" -- BnF Dupuy 468

partial

**Status: partial** (23 September 2026). The letter spans f.28r-v (canvases 63-64; the check-solved sweep saw only
canvas 64). All 687 cipher tokens were transcribed. The later hand's interlinear gloss gives a self-consistent
simple-substitution key (21 letter signs, 5 word signs). With it, 663 of the 687 tokens read as continuous Latin:
630 at grade H, 33 at grade S. 18 are M and 6 are unread. Novelty is not classified here (rule 10; a verifier
session has not run). The status stays partial, not solved, until then and until the six unread tokens and the
gloss hand are settled.


QUEUE row: M7 (sources/solver-diffs/2026-09-23-digitised-hits.tsv, "Digitised candidates, no copy needed").

## Source

BnF, Departement des Manuscrits, **Dupuy 468**, Gallica `ark:/12148/btv1b10035959t` (492 leaves),
"Recueil de documents concernant l'histoire de l'ALLEMAGNE, du DANEMARK, de la HONGRIE, de la POLOGNE et
de la SUEDE... de 1447 a 1633 environ" (Gallica OAI title). BnF Archives et manuscrits notice
`http://archivesetmanuscrits.bnf.fr/ark:/12148/cc88606j`. Finding-aid text (Gallica OAI `dc:description`,
quoted verbatim): "Lettres adressees a Francois Ier par les personnages suivants : **Ernest, [prince
d'Anhalt-Zerbst-Dessau], et de Joachim, son frere, s. l., veille de la saint Paul, s. d. [1515 ou 1516],
orig., en latin, presque entierement en chiffres (28)**." Ernest of Anhalt-Zerbst (1455-1516; confirmed by
web search) died 2 July 1516, consistent with the finding aid's 1515/1516 dating.

## Check-solved sweep (23 September 2026)

1. **Web search.** `"Dupuy 468" Anhalt Francois Ier chiffre OR cipher 1515 1516` -- no hit connecting this
   shelfmark to any cipher scholarship, blog or edition; only generic BnF/Dupuy-collection and unrelated
   pages surfaced. `Ernst Joachim Anhalt-Zerbst 1515 1516 Francis I cipher letter Beckmann correspondence`
   -- confirmed Ernest's dates (d. 1516) but found no edition, no "Beckmann" correspondence volume, and no
   cipher-scholarship hit of any kind for this letter.
2. **Print/scholarship.** Champollion-Figeac (named in the brief for this target too, since he prints
   Francis I's early-reign correspondence broadly) and the Anhalt correspondence edition named in the brief
   ("Beckmann") were not reached this sweep beyond the web search above -- no volume or archive.org
   identifier for a Beckmann Anhalt-correspondence edition was found by search; flagged as unchecked, not
   negative.
3. **Community lists.** `sources/cryptiana/` grepped for "anhalt": no hit anywhere in the mirror
   (francis.htm, the most relevant page, covers French-cipher volumes and does not mention this German
   correspondence).
4. **DECODE.** Cached catalogue grepped for "anhalt": no hit.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `TARGETS.md` grepped for "anhalt": no
   hit.
6. **Aymeloglu.** `ay/CATALOGUE.md`, `TARGETS.md`, `SHORTLIST.md` grepped for "anhalt": no hit.

Requests: gallica.bnf.fr 13 (1 OAI GetRecord, 1 IIIF manifest, 11 IIIF image fetches at reduced/higher
width, folio-pinning bracket via a long historical memoir's internal page numbers), WebSearch 2 queries
(shared budget with M6's Anhalt-adjacent checks).

## What the leaves show

**The letter is real, digitised, and genuinely mostly enciphered** -- confirmed by direct image inspection
at canvas 64 (bracketed against canvas 45/55, where a preceding long memoir's internal page numbers were
tracked, and canvas 67, the following plain Palatine letter of the same 1516 date). One leaf, roughly 15
lines: Latin grammatical connectives left in clear (ut, et, quod, sed, oportet omnino, non mittat...)
alternate word-by-word with cipher tokens -- arithmetic numerals (4,6,7,8,9) and several distinct symbol
shapes (Greek-letter-like marks, pi/tau shapes, asterisks). Cipher type: **mixed numeral+symbol
nomenclature**, not a single homophonic alphabet. Approximate token count: on the order of **100-130
tokens total**, of which roughly half to two-thirds are cipher groups (not an exact transcription, per the
brief's "do not transcribe").

**The important finding: this leaf is not a blind ciphertext.** A later, lighter hand has written
gloss-words interlinearly, directly above roughly 15-20 of the cipher tokens across the letter --
legible examples include "maiorem", "quam", "et", "confoederationem", "infamorum", "principibus",
"foedus"/"foederis", "marchonem", "inter", "nos" (several more are present but too faint to read reliably
at the resolution fetched). This is a **partial period or near-period interlinear decipherment already
sitting on the document**, not a key stored elsewhere in the volume and not a printed edition. Whether the
gloss hand is contemporary with the letter (a 1515/16 codebreaker's crib) or a later antiquarian annotation
(Theodore Godefroy, whose own signed notes appear elsewhere in this volume at ff.8-9, on the Reichskammer-
gericht and the 1447 concordat) was **not established this sweep** -- the hand was not compared letter-
for-letter against Godefroy's known notes, and no date accompanies the gloss.

## Edition risk

**Not established either way.** No printed edition, cipher-scholarship page, or solver-repository entry
names this shelfmark, this letter, or this correspondence (see sweep above), but the brief's own named
edition (a Beckmann Anhalt correspondence) was not actually located or checked, only searched for by web
query. This is a real gap, not a clean negative.

## Verdict

**Partial, not open** -- reclassified from QUEUE's "cryptanalysis, no key named" because a **key is
present on the document itself**: someone (identity/date unresolved) already glossed roughly 15-20 of the
letter's ~100+ cipher tokens with their plaintext Latin equivalents. This is closer to a "solved-in-place"
recovery candidate than a blind cryptanalysis target -- any reading built from these existing glosses would
be grade **H** (read from a key/gloss source) for the glossed tokens, with the remaining tokens needing
either cryptanalysis or a matching published key to fill in. **No H or C reading has been produced this
sweep** (check-solved does not transcribe or solve); this is reported as what the leaf shows, not as a
claimed decipherment. Nothing here is claimed as new, unpublished or unread (rule 10) -- the recommendation
below is a search result, not a novelty verdict, and no verifier session has run.

## Next

1. **Transcribe the existing interlinear gloss first**, before any cryptanalysis -- re-fetch canvas 64 at
   the highest available IIIF width (2400px+) or request a sharper scan, since several gloss words were
   too faint to read reliably at 1800px. This could turn a chunk of the letter into an H-grade reading with
   no cryptanalysis at all.
2. **Identify the gloss hand** against Theodore Godefroy's signed notes elsewhere in this same volume
   (ff.8-9, both already viewed as plain items in the finding aid) to settle whether this is a period
   decipherment (stronger claim) or a 17th-century antiquarian's reading (still useful, but a different
   grade and a different "sibling" story).
3. **Recharacterise this target's kind** from "cryptanalysis" (QUEUE's label) toward **recovery** once the
   gloss is transcribed and confirmed -- the key effectively already exists in the box, per README "What
   counts as a result" (an unread letter whose key sits in the same file is the cheapest unique solve [Solver note, 23 Sept 2026: 'unread' and 'unique' here are the README category wording, not a novelty verdict; see rule 10 and the Status line.]
   there is).
4. Locate and check the Beckmann Anhalt-correspondence edition named in the brief, and Champollion-Figeac,
   before any novelty claim; neither was reached this sweep.

## Transcription (23 September 2026)

- **Leaves.** Canvas 63 = f.28r: the address line, then 30 lines, mostly cipher, glossed throughout. Canvas 64 =
  f.28v: 11 lines of mixed clear and cipher, then 6 plain lines and the date "in vigilia sancti Pauli in mane
  hora quinta". Canvas 65 carries only the subscription ("humillimi servitores / Ernestus dux etc. / Joachimus
  etc."), fetched at 700 px as a record. The check-solved sweep above saw canvas 64 only; the letter begins on 63.
- **Access route 1** (IIIF, curl). The manifest was fetched once (one connection reset, retried once). Canvases 63
  and 64 were fetched at full/full (4039 x 5950), canvas 63 at 700 px (one reset, retried once), canvas 65 at
  700 px. 7 requests to gallica.bnf.fr, 1.5 s apart, descriptive User-Agent. images/manifest.json has the URLs,
  sizes and rights.
- **Crops.** 84 native-resolution line crops (two per line, each under 2400 px wide, quality 80, greyscale with a
  levels stretch that brings up the faint gloss), cut by images/crop.py. The folder totals about 8.5 MB. The first
  cut clipped sloping right halves; the committed crops are the recut with separate right-half centres.
- **Passes.** Two independent Sonnet sessions worked from the crops and the legend sheet: passA.tsv and passB.tsv.
  They agreed on 59.9% of token rows and 10 of 153 glossed rows. The disagreement was systematic (q and 9 are two
  signs, Po was read as P, D as T, gloss words shifted). The reconciler (Opus) therefore read every line from the
  crops, taller band views and native zooms. That reading is ciphertext.txt. reconciliation.md has the causes,
  the 35 contested positions and what is still uncertain.
- **Counts.** 929 tokens on 49 rows: 687 cipher tokens and 242 words in clear. 31 distinct cipher symbols (plus a
  placeholder for 3 blotted symbols). 659 cipher tokens stand under a gloss word; 643 align letter for letter
  with it.

## Key from the gloss

key_from_gloss.py aligns every gloss word with the tokens under it. A word split over a line end is joined
across the two lines. It writes one vote per aligned token to key_from_gloss.tsv. 643 votes give one dominant
value per symbol (key.tsv, source 'gloss'):

a 6, b 7, c L, d T, e q, f 3, g +, h Π, i V, l 9, m D, n U, o Y, p 4, q Z, r R (and R2), s P, t Po, u/v cc, x II.
Word signs: K = christianissimus (rex), glossed chrmus/chrmo/chrmi, 12 tokens; F = marchio, 6; O (theta) =
Luneburg, 5; PW (the P-shape standing alone) = Mekleburg, 4; SX = Saxonie, 1, uncertain.

**Self-consistency.** No symbol carries two gloss values except in 9 minority votes, and each has a reason in
the text:
- The cipher spells -cio- and n where the gloss writes -tio- and m (confederacionem, amiciciam, inponetur,
  conmissionem), 4 votes.
- There are three single-token slips in the cipher: D for i in r06 commissionem, P for t in r18 consentiente,
  Po for s in r14 articulus.
- The glossator wrote "nos" over q Y P at v09, which the key reads "eos"; he glossed the same group "eos" at r12.
- One gloss read 'rum' over c-u-[blot] at r29.

**The gloss hand.** It is a lighter, later-looking humanist cursive in grey ink, written over the cipher. It
abbreviates christianissimus as chrmus, spells fedus and luneburg/luneborg, and normalises the cipher's
spelling. The places where it departs from the cipher (nos for eos, commissionem for conmissionem) show a reader
applying a key, not a copyist. It was not compared letter for letter with Godefroy's signed notes at ff.8-9 and is
not identified here.

## Control (rule 3)

- **Model.** A Latin character 5-gram model (tools/latin_ngram.py, same format as tools/italian_ngram.py) was
  trained on 2.86 M letters of the CLTK mirror of The Latin Library (github.com/cltk/latin_text_latin_library,
  shallow sparse clone, not committed). The texts were Erasmus, Melanchthon, Pico della Mirandola, Thomas a
  Kempis, Bultelius, and Cicero ad Familiares and ad Atticum.
- **Held-out control plaintext.** Five consecutive paragraphs of Erasmus's Epistolae (solve/control_source.txt),
  excluded from the model.
- **Control design** (solve/design.json). The same as the target's letter layer: one sign per letter, a rare
  second r sign, and two nulls at the target's rate (16 of 653). Word signs become run breaks in both texts.
- **Control length and pattern.** Built with tools/nomenclator_anneal.py synth --pattern
  solve/target_anneal.txt: 653 letter-run tokens, the target's clear/cipher run structure, 23 sign types.
- **Settings for every run.** --restarts 16 --iters 300000 --syl none --max-word 0 --max-null 2 --max-homo 2.

| run | per-token score | tokens correct | shuffled baseline (per token) |
|---|---|---|---|
| C1 blind (seed 1) | -2.053 | 99.8% (letters 99.8%), best in 10/16 restarts | -3.946 |
| C2 blind (seed 2) | -2.043 | 100.0% | -4.036 |
| C1 with 93.9% of tokens revealed (the target's glossed fraction; 21 signs fixed) | -2.084 | 100.0% | |

## Runs (runs.tsv)

| run | per-token score | result |
|---|---|---|
| T-blind (no gloss values used) | -2.174 | agrees with the gloss key on 602/637 letter-sign tokens (94.5%) |
| T-blind shuffled baseline | -4.002 | |
| T-glossfixed (21 gloss values fixed; g and o free) | -2.239 | g and o come out null |

- **Blind against the gloss key.** The blind search recovers the gloss key on its own except for three signs: 3
  as d, T as m, R2 as h. It scores higher than the gloss key because a classical and humanist model prefers
  "demus" to the medieval spelling "fedus", which occurs 10 times. The gloss settles those signs.
- **The target against the control.** The target's per-token score (-2.17 to -2.24) is within 0.2 of the
  controls' (-2.04 to -2.08). The shuffled target is at -4.00.
- **The nulls.** g and o have no gloss. The search makes g null in both runs and o null in one (h in the other),
  so both are graded M.

## Reading

reading.txt is regenerated by check.py (python3 check.py --check exits 1 if stale). Below, the cipher runs have
word division **added by the solver** (the cipher does not mark it), cipher text is upper case, clear text lower
case, and <...> marks word signs. [..] marks tokens unread or M.

f.28r: Amicissime potentissime ac christianissime rex ac domine domine observandissime. Post humilimam atque
humilimam commendationem maiestatem vestram certiorem reddimus nos ambos saluos ac fortunatos venisse IN OPIDUM
CERBESS ET IBI ERANT SIMUL [HHH] <SAXONIE> <MARCHIO> <LUNEBURG> ambos <MEKLEBURG> ET MULTI ALII [Y~] EGO
FILIUS [<PW>] <LUNEBURG> tractatum cum patre meo ad patrem, et EGO IOCHIN UT PROPOSUI <MARCHIO> CONMISSMONEM [sic]
MEAM. In presentia <LUNEBURG> vnius de <MEKLEBURG> et consortij mei, quia <MARCHIO> hic placuit, conclusum hic
est <MARCHIO> CUM AUXILIO <LUNEBURG> [?]ET <MEKLEBURG> faciant totis viribus ut FEDUS CONCLUDATUR [o g] cum tot
sint; possibile est per ipsos, omnibus melius et utiliter pro <CHRISTIANISSIMO> videtur, ut primo de
<CHRISTIANISSIMO> nulla fiat mencio, sed INTER EOS ET QUI INTER GERMANIE PRINCIPES ATTRAHI POSSUNT FIAT [g] FEDUS,
[?]ET UNUS ARTICULU[S] INPONETUR UT NULLUS ALIUS IN ISTUD FEDUS ACCEPTARETUR NISI MAIORE PARTE CONFEDERATORUM
CONSEN[T]IENTE, ET QUEMCUMQUE MAIOR PARS ADMITTERET aut quoniam [ß] CONSENTIRET, UT MINOR PARS ADMITTERE ET
CONSENTIRE TENERETUR. Deinde potest palatinus TRACTARI CUM HIS QUI NON dum habent speciale FEDUS AUT singulare
AMICICIAM CUM <CHRISTIANISSIMO>, UT SPECIALE FEDUS FIAT aut amicitia; a[?] tandem ubi SECURUM SIT [g] quod LONGE
MAIOR PARS erit et conficiet PRO <CHRISTIANISSIMO> [g], tunc optimum erit ut <CHRISTIANISSIMUS> HOC FEDUS PETAT
VELLE INIRE; hoc modo etiam si aliquem noluissent ESSE IN FEDERE CU[M] <CHRISTIANISSIMO>, hoc modo ASTRICTI ERUNT
ESSE CONFEDERATORES ES <CHRISTIANISSIMI>; vri[?] prudenti pauca.

f.28v: Nos omnino speramus quod firmiter ut cito faciemus MAIOREM LIGAM [g] ET CONFEDERACIONEM IN FAUOREM
<CHRISTIANISSIMI> quod sit IN TOTA GERMANIA [g o], sed oportet omnino ut <MARCHIO> <LUNEBURG> omnino consultum ut
aliquos etiam nobis necesse et consultum videtur ut huius qui non habent A <CHRISTIANISSIMO> PENSIONEM [o g] IPSIS
PROMITTATUR [g] Q(UE?) et videtur <MARCHIO> consultum ut consortii nobis GALLUM [g] Q(UE?) <CHRISTIANISSIMUS> non
mittat principaliter pro posse, sed nobis duobus autoritate det privatis PRINCIPIBUS [g] promittendi donec quando
FEDUS [g] INTER EOS FACTUM SIT, ac tempus erit ut <CHRISTIANISSIMUS> INGREDIATUR; deinde <CHRISTIANISSIMUS> poterit
mittere ad placitum eius. Ita si pars adversa de ista materia intelligeret aliquid, impediret totis viribus ne
perficeretur. Nos minore suspicione faciemus et citius perficiemus ... quas ego Joachimus ad dominum Cancellarium
et dominum admiraldum scripsi ... Datum in vigilia sancti Pauli in mane hora quinta.

**What it says (solver's paraphrase, inferred).** The two princes report their arrival at Zerbst ("Cerbes"),
where Saxony, the margrave and Lüneburg and Mecklenburg met with them. They propose that the margrave, Lüneburg and
Mecklenburg conclude a league with the German princes who can be drawn in, at first without naming the Most
Christian King. One article would admit no new member without the consent of the majority of the confederates.
The Count Palatine could be approached. Once the majority is secure, the King himself would ask to join. The King
should promise pensions to princes who have none. He should not send a Frenchman openly; instead he should give
the two writers authority to make promises privately until the league is made. The clear parts name letters that
Joachim wrote to the Chancellor and the Admiral.

## Grading (rule 4, per token, check.py)

| grade | tokens | what |
|---|---|---|
| H | 630 | under a gloss word that aligns with it, with the gloss letter or word equal to the key value |
| S | 33 | not so glossed, read with a gloss-derived value (the key applied; control 99.8-100%) |
| M | 18 | g (13) and o (3), null by the search only; PW at r04:25, glossed 'dux'; SX (Saxonie, from the gloss 'saxo') |
| unread | 6 | HHH r03:23, Y~ r04:15, ß r19:18, three ink blots (r08:16, r14:6, r29:3) |

There are 687 cipher tokens and 242 clear words (clear words are not graded). There is no C grade: nothing was
read from outside known plaintext.

## Where it was not found

Searched on 23 September 2026:
- **dbourdeau/cyphersolver** (fresh shallow clone, head 763a3b9 of 23 Sept 2026) grepped for anhalt, Dupuy 468,
  btv1b10035959t, zerbst, cerbes and the finding-aid phrases ("Joachim, son frère", "presque entièrement en
  chiffres"). No hit for this letter. Its gallica_sweep lists other Anhalt items (Christian of Anhalt, 1591-92,
  Henri IV); vanreede1787 mentions Anhalt in another context.
- **aaymeloglu/unsolved-ciphers** (head 2495c45 of 23 Sept 2026) grepped with the same terms: no hit.
- **WebSearch** for "nisi maiore parte confederatorum consentiente" OR "fedus acceptaretur nisi" with Anhalt,
  Francis I and 1516: no page with the phrase.
- **Not searched:** the Beckmann Anhalt edition and Champollion-Figeac (see the check-solved section), the calendars
  and editions of Francis I's German diplomacy, Gallica full text, HathiTrust and Google Books phrase searches.
  A verifier needs all of these.

## What a next solver needs

1. A verifier session (rule 10) with the plaintext above and this search log. The sender- and recipient-specific
   editions come first: Anhalt correspondence, Francis I's German negotiations of 1515-16 and the 1519 election
   literature. Nothing here says whether this reading is known.
2. The six unread tokens need a sharper look, preferably a colour image or the original: HHH and SX at r03:23-24
   (the gloss there reads 'ma?ch??' and 'saxo'), Y~ at r04:15 (the gloss 't', perhaps "et"), ß at r19:18, and
   the blots. The Y~ reading is uncertain.
3. The gloss hand, compared with Godefroy's notes at ff.8-9 of the same volume.
4. The date. "Vigilia sancti Pauli" is 24 January (the Conversion) or 28 June (Peter and Paul). The finding aid
   gives 1515 or 1516, and Ernest died 2 July 1516. The content (a league for Francis I among the German princes)
   could help a historian fix the year.
5. Suggested, not done: the same key may open other Anhalt or German-prince letters to Francis I in Dupuy 468 or
   neighbouring Dupuy volumes.
