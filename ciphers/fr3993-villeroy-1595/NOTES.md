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

## Control-first cryptanalysis (24 Sept 2026, LANE R4 N)

Brief `.claude/briefs/runs/2026-09-24-lane-r4-n-villeroy-garbino.md` (Opus, cap $7, session_018cVYFykz1TpBPHHHgWqHuN).
Transcription: D. Bourdeau's first pass (`bourdeau/`, copied unchanged with attribution, MIT / CC BY 4.0); not
re-checked on the image, so everything here is conditional on it (rule 2).

**What Bourdeau had not tested.** His ladder assigns one letter (or one CV syllable) per unit. The design not yet
tried is a mixed nomenclator: letters with homophones, plus syllable signs, plus word codes, plus nulls, solved
jointly. Segmented 1x/2x as in his `seg.py` (`solver/target_pairs.txt`), the runs give **607 units, 69 types**.

**Matched control first (rule 3).** `solver/design_nomen69.json`: 45 letter signs (e 5, a/i/s/u 3, ...), 12
syllables, 8 French word codes (from de que le la les et pour roi nous vous qui est ennemi dessein), 4 nulls at 5%,
syllables used 80% of the time; enciphered on held-out French 16th-c. letter prose (every 10th paragraph of
`tools/data/fr16`, Catherine de Médicis t.1-2 and Marguerite de Valois, never seen by the model) in the target's own
17-run pattern: 607 tokens, 61-62 types. Solved blind with `tools/nomenclator_anneal.py solve` (French order-5
model built by `solver/fr_corpus.py` + `tools/italian_ngram.py build`; `--syl both --max-syl 12 --max-word 8
--max-null 4`, 12 restarts x 1.5 M iterations). Reproduce: `solver/run_controls.sh`.

| control | token accuracy | letter accuracy | sign accuracy | reading |
|---|---|---|---|---|
| nomenclator, seed 1 | **2.0%** | 21.5% | 1.6% | gibberish |
| nomenclator, seed 2 | **5.9%** | 12.5% | 4.9% | gibberish |
| sanity: pure homophonic, 45 signs + 3 nulls, same length and pattern | 61.1% | 56.2% | 53.3% | partly readable ("medicis elle ua de...") |

**Target: not run.** The brief says run the target only if the control reads; it does not, so a target run could
say nothing either way. Result: **the mixed-nomenclator design has no working control at 607 units with this
solver** (2.0% / 5.9%, against 61% for a homophonic control of the same size through the same solver; Bourdeau's
`hsolve.py` reads the homophonic control fully). With Bourdeau's six negatives this closes ciphertext-only attack on
the transcription as it stands: every design that could be controlled has been, and the remaining one cannot be.

**Keys on file.** No key in `ciphers/*/key.tsv` dates from 1593-96 or belongs to Nevers's circle (the 14 keys on
file are 1446-1869, none French 1590s), so none was applied. Bourdeau's Court cipher of 1593 (fr. 3995 no. 60)
and nos. 65, 66, 68-76 are already ruled out above.

Grade counts: H 0, C 0, S 0, M 0, I 0 (nothing read). Status stays `open`.

Suggestions (not done, outside this brief): read the fr. 3995 keys other than nos. 60/65/66/68-76 on the image for
the sign family `λ π θ Δ ϖ ∞` with 1x/2x figures (no. 76 is the nearest family); look for the as-sent letter in
Villeroy's papers (fr. 15xxx / Cinq Cents de Colbert). No request was made to any host in this step.
