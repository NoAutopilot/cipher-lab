open

# Nevers to Villeroy, Saint-Quentin, 16 August 1595 — BnF fr. 3993 no. 102 (ff. 148r–149r)

QUEUE row: CS2-26 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 277 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September
2026 by LANE N3 csCS2b (session_01711qcbvcwvGDsSAtVXwfJB), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2b.md`.

## What it is

Nevers's file copy (secretary's hand) of a letter to Villeroy, dated "16 d'aoust 1595" / "De St Quentin ce 16
aoust 1595," about the relief of Cambrai (besieged by Fuentes) and the loss of Doullens. Clear French with 17
inserted cipher runs (753 signs total: mostly 1–4-digit figures — `1 2 o 3 7 4 9 ...` — plus about 45 non-figure
signs `ↄ T λ π θ ∞ ‡ ϖ Δ ∩ Ⱡ`). The letter itself explains why cipher is used: "ce qui est de plus pregnant seroit
bon d'estre en chiffre ... affin que 72 ne puissent prendre cognoissance de noz affaires" (72 = code number for
the enemy). D. Bourdeau's own working folder (`nevers1595/`, session of 22 September 2026) transcribed both
cipher blocks (`ct_f148r.txt`, `ct_f148v_149r.txt`) and tried six Nevers keys from fr. 3995 (nos. 60, 65, 66,
68–76, including the Court cipher of 1593 and the Balagny–Nevers alphabet reconstructed by Tomokiyo from the
same volume, fr. 3993 f. 130) — none fits. Six unit-segmentation models were run through a letter-level solver
(`hsolve.py`) and a syllabic-unit solver (`hsyl.py`), each validated against a matched control built from Henri
IV's letters enciphered with the letter's own run-length profile: **the homophonic control solves cleanly
(−1.84/char, all restarts agree) and every target run scores far worse (−2.5 to −3.1, no restart agreement, no
French)**; the syllabic-unit control itself fails to solve at this length, so that design cannot even be tested
here. This satisfies rule 3 (no negative without a matched control) directly.

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk).** No sentence in the local snapshot names fr. 3993 no. 102
   specifically (grep for "3993" hits only two unrelated 1595 items, f.71 and f.254, in `nevers.htm`). Bourdeau
   cites Tomokiyo's *League* page directly (not in the local snapshot, so not independently re-verified here):
   *"Portions in cipher. Undeciphered. The cipher uses figures and other symbols ... It seems none of the Nevers
   collection decodes these."* No later publication cited.
2. **Standard printed edition — actually read.** Gomberville, *Mémoires du duc de Nevers* (1665), tome 2,
   **searched by Bourdeau via Gallica's own full-text search** against this letter's exact clear phrases (e.g.
   "assez intelligiblement," the Cambrai/Doullens/Fuentes context): **no hit**. This is the strongest edition
   check of this batch — a genuine full-text search of the correct tome for the correct date and content, not
   an index lookup. This worker did not have Gallica full-text search access this pass (IIIF-only grant) and so
   did not independently re-run it, but the search terms, tome and method are named, matching this lane's rule
   (LANE N3 addition, 24 Sept 2026).
3. **DECODE (sources/decode/) + both solver-repo clones.** No DECODE record found for fr. 3993 no. 102 in the
   local snapshot (grep for "3993": no hit in `records-non-decrypted-2026-09-24.tsv` or
   `records-decrypted-2026-09-24.tsv`). dbourdeau/cyphersolver (shallow clone, 24 Sept 2026):
   `nevers1595/NOTES.md` gives the fullest account (above); verdict "attempted, closed from the evidence (not
   read)... the runs are not a plain homophonic cipher"; full escalation checklist [x] on siblings, clear-pages,
   known-keys, print, key-rebuild; sibling fr. 3993 no. 133 (18 Aug 1595, next letter to Villeroy) checked and
   confirmed all-clear, no cipher. aaymeloglu/unsolved-ciphers: fresh shallow clone, no hit for "3993" or
   "Villeroy" + "1595".
4. **Web search** (Nevers Villeroy Saint-Quentin 16 août 1595 chiffre fr.3993): only BnF/Wikipedia catalogue-type
   results surface (the manuscript series record, Louis de Gonzague's Wikipedia page); no solution or key found.
5. **Ciphertext confirmed present on the Gallica leaf.** IIIF fetch, gallica.bnf.fr, 24 Sept 2026, 1 request:
   `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9059229n/f161/full/500,/0/native.jpg` (canvas 161, f.148r, right
   half of the two-page spread). Image shows clear French prose with a block of cipher figures at the foot of
   the page, matching Bourdeau's description and layout (a two-page-spread volume, *Collection Mémoires de la
   Ligue*). Leaf: https://gallica.bnf.fr/ark:/12148/btv1b9059229n/f161.item

## Verdict

**Stage 2, open.** No source of the six claims a decipherment of BnF fr. 3993 no. 102. Bourdeau's own attempt —
the deepest single source, and the only one of this batch to run an actual full-text search of the correct
Gomberville tome against the letter's own clear phrases — closes it as a genuine ciphertext-resistant target: a
753-sign mixed nomenclator that fails every tested unit-segmentation model under a rigorously matched
homophonic control (rule 3 satisfied), and is not any of eleven candidate Nevers keys checked against the image.
What would move it, per Bourdeau: the as-sent letter to Villeroy (Nevers's copy is what survives here), or a
key among the unexamined portions of fr. 3995 beyond nos. 60/65/66/68–76.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 277; `nevers1595/`
working folder — full transcription, matched-control solver ladder across six unit models, Gomberville tome-2
full-text search), CC BY 4.0 — prior attempt (not a solution). S. Tomokiyo, cryptiana *League* page (cited via
Bourdeau; not independently re-verified from the local snapshot this pass).

Not decoded, not transcribed here (out of scope for check-solved; Bourdeau's `nevers1595/` already has a full
transcription and solver ladder if a solver picks this up). Rule 10: no novelty claim made; this is a search
result, not a verifier's classification.
