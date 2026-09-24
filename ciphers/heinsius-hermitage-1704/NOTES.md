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
