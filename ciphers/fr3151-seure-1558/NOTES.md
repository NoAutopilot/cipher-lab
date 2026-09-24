blocked


**Held by the LANE N3 orchestrator, 24 Sept 2026 15:36 UTC:** status `blocked`, not `open`. The standard printed edition or calendar for the date was not located or read in the check-solved pass (section 2 below); under the lane rule (R8 lesson) that verdict is `blocked` until an edition check reads it. The nomination line posted 15:22-15:23 is held, not firm. Edition check: brief `.claude/briefs/runs/2026-09-24-lane-n3-csED.md`.
# Chevalier de Seure (Lisbon) to de Fresne and to Henri II, six letters, 12-27 Dec 1558 — BnF fr. 3151 nos. 39-44

QUEUE row: CS2-02 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 10 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026
by LANE N3 csCS2a (session_01JrahDoApcsEHgiQigjaJPY), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2a.md`.

## What it is

Six letters of the Chevalier de Seure, French agent in Lisbon, dated 12 and 27 December 1558: to Monsieur de
Fresne (Florimond II Robertet, seigneur du Fresne) and to King Henri II. Nos. 40/41 and 43/44 are duplicate
copies (confirmed by Bourdeau's repository -- see below). Bound in the same BnF fr. 3151 recueil as two other,
unrelated ambassadors' ciphers (La Guiche to Montmorency, Rome 1551, no. 22; Noailles, Venice, no. 33) which
Bourdeau's repository treats as one catalogue entry (no. 10) but are separate keys and separate items from
Seure's.

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk).** No mention of BnF fr. 3151, "Seure", "de Fresne" or a 1558
   Lisbon-Henri II correspondence found in any of the 104 locally snapshotted cryptiana pages (grep by shelfmark
   and by name across sources/cryptiana/web/*.htm). No live fetch was needed to reach this negative, since the
   name/shelfmark grep covers the full local mirror; not separately confirmed against the live site this pass
   (in budget, not run -- flagged for a future pass if this target is promoted).
2. **Standard printed edition / calendar.** Not located this pass. Seure's Lisbon dispatches of 1558 were not
   found in a quick web search; no Ribier or other printed *Lettres et memoires* collection was checked for this
   specific correspondent (Bourdeau's own escalation log for the same volume notes the same gap: "not done --
   only a web search; Ribier, Lettres et memoires d'estat (1666), and the Noailles ambassade edition (Vertot
   1763) not grepped for these letters").
3. **Lasry's publications.** No Lasry solution of fr. 3151 or a Seure/Lisbon 1558 cipher found in Tomokiyo's
   pages or web search.
4. **DECODE (sources/decode/ on disk) + both solver-repo clones (grepped by shelfmark).** No DECODE record for
   fr. 3151 in the local snapshot. dbourdeau/cyphersolver (shallow clone, 24 Sept 2026): `guiche1551/NOTES.md`
   (catalogue no. 10, worked 21 Sept 2026) covers the whole recueil and states of Seure specifically: *"The
   catalogue says 'no siblings', which is wrong. The volume holds six Seure letters of 12 and 27 Dec 1558 (nos.
   39-44, Gallica views ~72-88), and nos. 40/41 and 43/44 are duplicate copies. Each mixes clear text with long
   cipher blocks, about eight pages and roughly 2,000 signs in all: a homophonic symbol alphabet of about 60
   signs plus numerals (12, 13, 23, 100), so a nomenclator. There is no decipherment on the leaves... This is
   solvable in principle with a full transcription (large corpus, one key), but that is a multi-session job."*
   Escalation log for the item: *"Seure fr. 3151 nos. 39-44 (about 2,000 signs, homophonic with numerals) --
   blocker: not-attempted; left as a multi-session job; not transcribed"*; and *"known-keys: not done -- no
   French diplomatic key of the 1550s (Tomokiyo's Henri II pages, Lasry's GL.htm) was tried on ... Seure."*
   So Bourdeau's own repository confirms Seure was never even attempted, let alone solved. aaymeloglu/
   unsolved-ciphers: no hit for fr.3151 in this shallow clone. WebSearch ("fr.3151 Seure Fresne Henri II
   chiffre"; "Seure ambassadeur Lisbonne 1558 chiffre dechiffre Henri II"): both confirm the manuscript and the
   Chevalier de Seure's Lisbon letters exist in fr.3151, no hit for a decipherment.
5. **Ciphertext confirmed present on the Gallica leaf.** IIIF fetch, gallica.bnf.fr, 24 Sept 2026, 1 request:
   `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9059865k/f75/full/500,/0/native.jpg` (view 75, within the ~72-88
   range). Image shows a two-page opening: the left leaf is a dense block of closely-set text distinct in
   character from the ordinary secretary hand on the right leaf, and the right leaf carries a clearly separate
   symbol/cipher paragraph mid-page -- consistent with Bourdeau's "clear text with long cipher blocks" account.
   Leaf: https://gallica.bnf.fr/ark:/12148/btv1b9059865k/f75.item

## Verdict

**Stage 2, open.** No source of the six names a decipherment of the Seure letters. This is a genuinely untried
target, not merely unsolved: Bourdeau's own repository explicitly left it as "not attempted... a multi-session
job", distinct from the La Guiche and Noailles items in the same recueil (which were partly read in the same
session). ~2,000 signs across six letters (two duplicate pairs) of a single homophonic-plus-numeral nomenclator
is a substantial corpus for one key -- a plausible cryptanalysis or key-recovery candidate once transcribed.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 10; `guiche1551/`
working folder), CC BY 4.0 -- prior scoping, not an attempt at Seure specifically.

Not decoded, not transcribed here (out of scope for check-solved). Rule 10: no novelty claim made; this is a
search result, not a verifier's classification.
