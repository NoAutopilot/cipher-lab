partial

# Ernest and Joachim of Anhalt-Zerbst to Francis I, Latin, "presque entierement en chiffres" -- BnF Dupuy 468

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
   counts as a result" (an unread letter whose key sits in the same file is the cheapest unique solve
   there is).
4. Locate and check the Beckmann Anhalt-correspondence edition named in the brief, and Champollion-Figeac,
   before any novelty claim; neither was reached this sweep.
