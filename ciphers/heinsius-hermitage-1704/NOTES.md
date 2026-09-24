open

# René de Sauniere de l'Hermitage (London) to Anthonie Heinsius, three unsolved cipher passages, Feb-May 1704

QUEUE row: HU2 (`QUEUE.md`, "Huygens and Nationaal Archief correspondence editions: letters noted in cipher
(LANE N harvest of 24 September 2026)"). Brief `.claude/briefs/runs/2026-09-24-lane-n2-csHU2.md` (LANE N2,
follow-up to csHU, which reached HU4/HU5/HU6/HU8 but not HU2 -- budget).

## Source

Anthonie Heinsius correspondence archive, Nationaal Archief 3.01.19 ("H.A." in the edition), inv.nr. 946.
Printed in J.G. Smit / A.J. Veenendaal (ed.), *Briefwisseling van Anthonie Heinsius 1702-1720*, Deel 3
(GS169), letters no. 166 (p.59), no. 177 (p.64), no. 477 (p.169), via the Huygens `retroboeken/heinsius`
viewer. Image `images/heinsius_03_GS169_059.jpg` (printed edition's page scan; rule 2 applies).

## Check-solved sweep, 24 September 2026

1. **Editions first -- all three letters and their footnotes re-fetched and read directly this pass** (not
   only trusted from the harvest paraphrase), located via the retroboeken full-text search restricted to
   Deel 3 (`source_id=3`, confirmed option value from the search form's own `<select>`):
   - **No. 166** (26 Feb 1704, H.A. 946, p.59): "Nouvelles uit Londen over de samenzwering in Schotland en
     verslag van de werkzaamheden van het Parlement." Footnote: **"166. 1. Gedeeltelijk in onopgelost
     cijferschrift."** (Partly in unsolved cipher.)
   - **No. 177** (29 Feb 1704, H.A. 946, p.64): same regest ("Nouvelles uit Londen..."). Footnote: **"177. 1.
     Gedeeltelijk in onopgelost cijferschrift (zie ook hiervóór nr. 166)."** (...see also above, no. 166 --
     confirms the two are the same unsolved system, cross-referenced by the editor himself.)
   - **No. 477** (30 May 1704, H.A. 946, p.169): "Harley is benoemd tot secretary of state..." Footnote:
     **"477. 1. Gedeeltelijk in onopgelost cijfer."**
   All three entries in this edition are editorial *regests* (Dutch paraphrase-summaries), not verbatim
   transcriptions with the cipher printed inline as running numerals (unlike HU1/HU4) -- the actual
   ciphertext is **not in this printed edition at all**, only in the NA original (H.A. 946).
2. **A fourth, related instance found this pass, not in the original QUEUE row.** The same "cijferschrift"
   search (Deel 3, `source_id=3`) surfaces a third footnote: **"251. 1. Door Sauniere gedeeltelijk in
   cijferschrift gesteld."** (Partly put in cipher by Sauniere) -- letter no. 251, 25 Mar 1704, H.A. 946
   (p.92, read and confirmed this pass). This footnote does **not** use "onopgelost" (unsolved), unlike 166/
   177/477 -- ambiguous whether this means letter 251's cipher passage *was* resolved by the editor (and
   simply not flagged as a problem) or whether the editor is only describing that Sauniere originally wrote
   part of it in cipher without commenting on solvability. Not carried into the "open" verdict below as a
   confirmed fourth unsolved instance; flagged for whoever next reads H.A. 946 in full to check by eye.
   `sources/huygens/NOTES.md`'s table should note this as an unresolved fourth candidate in the same dossier.
3. **A candidate key in the same archive -- the most important finding of this pass.** `WebSearch` for
   Dopff's cipher (HU1, above) surfaced, as an incidental hit, Nationaal Archief 3.01.19 **inv.nr. 2317**:
   *"Sleutel van een cijferschrift, waarschijnlijk voor correspondentie met Engeland."* (Key to a cipher,
   probably for correspondence with England), dated c.1705. Followed up directly on nationaalarchief.nl (the
   real per-item JSON, not a search snippet): the item exists, `unittitle` matches verbatim, `availability:
   PHYSICAL`, no scans (see Copy status below). Reading the finding aid's own hierarchy around it (the escaped
   JSON tree embedded in the invnr page, decoded and walked this pass) shows it sits in a small, three-item
   subsection of its own, titled **"2.4.10 Cijferschrift"** (Cipher-writing), at the very end of Heinsius's
   correspondence series, immediately before "RETROACTA EN ANDERE STUKKEN" (other/background materials):
   - **2315**: "Stukken betreffende cijfers en sleutels van cijferschrift." (Pieces concerning ciphers and
     keys of cipher-writing) -- a general miscellany, could hold more than one system.
   - **2316**: "Cijfer voor de het cijferschrift met P. Battier." (Cipher for the cipher-writing with P.
     Battier) -- a *named* correspondent's cipher, not Sauniere/l'Hermitage; ruled out as this target's key.
   - **2317**: "Sleutel van een cijferschrift, waarschijnlijk voor correspondentie met Engeland." -- the
     editor's own uncertainty ("waarschijnlijk", probably) means this is not a confirmed match either, but
     Sauniere de l'Hermitage (writing from London throughout 1702-1720+) is exactly the kind of correspondent
     this description would fit, and no other English correspondent in this batch (HU1-HU8) is a better fit
     by geography. **This has not been confirmed to be the key used for letters 166/177/251(?)/477** -- that
     requires seeing both 2317 and the H.A. 946 originals side by side, which needs an archive visit (see
     Copy status). Recorded here as the strongest single lead found this pass, upgrading this target from a
     pure ciphertext-only problem to a candidate "key in the archive beside the letter" case (LESSONS.md's
     most productive route class).
4. **Post-edition literature search (check-solved.md's Oxenstierna/Torpadie lesson).** `WebSearch` (English
   Wikipedia on René de Sauniere de l'Hermitage; a BMGN/TvG/Nederlands Archievenblad-restricted query) found
   general biographical material (Huguenot exile, agent for the States-General and Heinsius in London from
   1693) but no article reporting a solved cipher for this correspondence. Not a positive result (rule 10);
   BMGN/TvG/NAB were queried via WebSearch only, not their own journal indexes directly.
5. **Community lists.** `sources/cryptiana/web/dutch.htm`: no mention of Sauniere, l'Hermitage, or H.A. 946.
6. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for "sauniere"/"hermitage": zero
   hits.
7. **Solver repositories.** Fresh shallow clones this pass, grepped for "sauniere", "hermitage", "946",
   "heinsius" (target-folder names/READMEs): no hit in either repository.

## Verdict

**Status: open.** Three cross-referenced instances (166, 177, 477) in one three-month correspondence run, the
editor's own footnotes explicit that the cipher was never solved, no later print or list naming a solution.
Letter 251's ambiguous, non-"onopgelost" footnote is a flagged fourth candidate, not counted toward this
verdict.

**Copy status: NOT copy-free.** H.A. 946 (`www.nationaalarchief.nl/onderzoeken/archief/3.01.19/invnr/946`):
real per-item JSON gives `"availability":"PHYSICAL","scans":[]` -- not digitised (same method and positive
control as HU1, see `sources/huygens/NOTES.md`). The candidate key items 2315/2316/2317 are **also**
PHYSICAL/no scans -- the whole "Cijferschrift" subsection of this archive is undigitised. `ciphers/heinsius-
hermitage-1704/REQUEST.md` written: both H.A. 946 (the three letters) and H.A. 2317 (the candidate key) should
be requested together, since comparing them is the actual next step, not two separate visits.

**Kind: recovery (candidate key, unconfirmed).** Upgraded from the harvest's "cryptanalysis" because a
plausible archive-held key (2317) was found this pass, even though the match to this specific correspondent is
the editor's own "waarschijnlijk" (probably), not a confirmed identification -- exactly LESSONS.md's "the key
was in the archive beside the letter" pattern, pending archive confirmation. If 2317 is not the right key,
this reverts to cryptanalysis with three (or four, pending letter 251) short ciphertext instances, likely
below unicity distance individually but not necessarily as a group.

Search log (rule 10): reported above, per source. Not classified for novelty (verifier's job, rule 10).
Requests this pass: `resources.huygens.knaw.nl` ~8 (search_in_text form, 3 search queries [l'Hermitage all-
books, l'Hermitage source=3, cijferschrift source=3, onopgelost source=3, sleutel source=3], pages.json
source=3, 3 html_url OCR fetches [p.59, p.64, p.169] + 1 more [p.92, letter 251], 1 image fetch), `www.
nationaalarchief.nl` ~5 (invnr 946, 2315, 2316, 2317, plus the shared batch with HU1/HU4/HU5, see sources/
huygens/NOTES.md), `github.com` 0 (reused this pass's HU1 clones). WebSearch 4. No subagents.

## Addendum, 24 September 2026 (LANE N2 check-solved worker csHU3): HU10, Sauniere de l'Hermitage, 4 Dec 1705

QUEUE row: HU10 (`QUEUE.md` Huygens round-2 sub-heading; `sources/huygens/cipher-letters-round2-2026-09-24.tsv`).
Brief `.claude/briefs/runs/2026-09-24-lane-n2-csHU3.md`. A **second, later instance** of the same correspondent's
cipher, a different H.A. number (1034, not 946) and a different edition volume (Deel 4/GS177, not Deel 3/GS169).

### Source

Nationaal Archief 3.01.19, inv.nr. 1034 (H.A. 1034). Printed in Veenendaal's edition, Deel 4 (GS177), p.446,
letter no. 1231, via `retroboeken/heinsius`. Image `images/heinsius_04_GS177_446.jpg` (printed edition's own
page scan; rule 2 applies).

### Check-solved sweep

1. **Edition read directly this pass**, `pages.json?source=4` mapped printed p.446/447 to `page_index`
   453/454, fetched and read in full. Unlike letters 166/177/477 in Deel 3 (Dutch paraphrase regests only, no
   ciphertext printed -- see above), **Deel 4 prints letter 1231 as a full verbatim French transcription**
   ("Eigenh. orig. H.A. 1034"), with the actual cipher numerals inline. Quoted:
   > "...Elles me paroissent, monsieur, présentement aussi grandes que jamais par la fureur où sont les **14**.
   > Ce sont des gens dont les principes iroient constament à destruire la Hollande..."
   > "...peut-estre ne faudroit-il par cela que la mort de **33** (qui est le véritable bien du reste)..."
   > "...et je tâche mesme souvent de luy rendre de bons offices envers les **15** dont par je ne sçai quelle
   > raison il a perdu la confiance le croyant attaché aus **14**..."
   > "...un seigneur me mena chez **50** et c'estoit d'une affaire dont on ne pouvoit escrire."
   Four distinct numeric codes across the letter: **14** (repeated twice), **33**, **15**, **50** -- a
   political/personal name-code embedded in otherwise plain French, the same design class as HU1 (Dopff) and
   HU9 (Van Haersolte). Footnote, quoted verbatim: **"1231. 1. De code is onbekend, een sleutel is niet
   aanwezig. Voor 14 zou Tories gelezen kunnen worden, de lezing van de andere cijfers blijft een gissing."**
   (The code is unknown, no key is present. For 14, "Tories" might tentatively be read; the reading of the
   other numbers remains a guess.) The very next letter in the volume, **no. 1232** (also l'Hermitage, also 4
   Dec 1705, p.447), is a Dutch regest that discusses "Tories" in the Hogerhuis openly in clear -- consistent
   with, but not confirming, the editor's guess that 14 = Tories.
2. **Does HU10's numbers overlap HU2's code? Cannot be determined from the print.** HU2's three letters (166,
   177, 477, all H.A. 946, Deel 3) are printed **only as Dutch paraphrase regests** -- verified directly this
   pass by re-fetching and reading pp.59, 64 and 169 of Deel 3 in full (not just trusting HU2's NOTES.md,
   rule 2): none of the three shows a single cipher numeral in the printed edition, only the editor's footnote
   that a passage was "gedeeltelijk in onopgelost cijferschrift/cijfer". **The actual ciphertext for HU2's
   letters exists only in the NA 3.01.19 original (H.A. 946)**, not in print anywhere found this pass, so
   HU10's numbers (14, 33, 15, 50) cannot be checked against HU2's numbers until someone reads H.A. 946
   directly. This is worth flagging strongly for whoever visits the archive for `ciphers/heinsius-hermitage-
   1704/REQUEST.md`'s H.A. 946 order: photographing 946 would let a future worker test directly whether the
   same code numbers recur across the two H.A. numbers (946, 1034), which — given the same sender, the same
   general shape of code, and only 19 months apart — is the single most useful comparison available for this
   whole l'Hermitage cipher problem.
3. **Candidate key NA 3.01.19 invnr 2317**: not independently re-checked this pass (already established as
   PHYSICAL/no scans by csHU2, see above); its own description ("waarschijnlijk voor correspondentie met
   Engeland", c.1705) matches H.A. 1034's own date (Dec 1705) as well as it matches H.A. 946 (1704) -- if
   anything, 2317's *date* sits closer to 1034 than to 946, which is new context this pass adds in 2317's
   favour as a candidate for either or both H.A. numbers, not resolved further.
4. **Post-edition literature search.** `WebSearch "Sauniere de l'Hermitage Heinsius cijfer 1705 code sleutel
   Tories"`: confirms l'Hermitage's biography (Huguenot exile, States-General/Heinsius agent in London from
   1693, per English Wikipedia) but no article reporting a solved cipher. Search result, not proof of absence.
5. **Community lists.** `sources/cryptiana/web/dutch.htm`, `unsolved.htm`: no "Hermitage"/"Sauniere"/"1034" hit.
6. **DECODE.** All three local TSVs grepped for "hermitage", "sauniere", "1034": zero hits.
7. **Solver repositories.** Fresh clones grepped for "hermitage", "sauniere", "1034": no hit in either
   repository (reused this pass's shallow clones, same as HU9/HU11).

### Verdict (HU10)

**Status: open.** Full ciphertext (four numeric codes) printed with the editor's explicit "code is onbekend"
statement; no later print, list, DECODE record or solver repository names a solution. Grouped with HU2 as the
same broader l'Hermitage cipher problem (same sender, two H.A. numbers 19 months apart), not a fully separate
target -- kept as a section of this same folder per the brief's instruction, rather than a new folder.

**Copy status: NOT copy-free.** `www.nationaalarchief.nl/onderzoeken/archief/3.01.19/invnr/1034`: embedded
JSON gives `"unittitle":"Saunière, René de-, sieur de l'Hermitage-, uit Londen.","availability":"PHYSICAL",
"scans":[]` -- confirmed matching sender, not digitised.

**Kind: recovery (candidate key, unconfirmed)**, same reasoning and same caveat as HU2 above (invnr 2317's
"waarschijnlijk" is the editor's own uncertainty, and now arguably a slightly better date match to 1034 than
to 946, but not confirmed to either).

Search log (rule 10): reported above. Not classified for novelty (verifier's job, rule 10). Requests this pass
for HU10 specifically: `resources.huygens.knaw.nl` 5 (pages.json source=4, pp.445/446/447, one search-pane
fetch to locate the letter's page_index), `www.nationaalarchief.nl` 1 (invnr 1034). WebSearch 1. See `ciphers/
breda-statengeneraal-1624-25/NOTES.md` for this session's full request accounting across all three rows.
