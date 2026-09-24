blocked

# Nevers to La Vieuville, St-Aignan, 30 September 1587 — BnF Français 3975 ff. 101r–102v, DECODE R4289

QUEUE row: CS2-17 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 184 and write-up `vieuville1587.html` at dbourdeau.github.io/cyphersolver). Check-solved
run 24 September 2026 by LANE N3 csCS2b (session_01711qcbvcwvGDsSAtVXwfJB), brief
`.claude/briefs/runs/2026-09-24-lane-n3-csCS2b.md`.

## What it is

A copy of a letter from the duc de Nevers to La Vieuville, dated "De St Aignen, ce 30 septembre 1587," about
110 lines of mostly clear French in a very hasty secretarial hand, with code numbers (30, 42, 43, 48, 63...) and
short runs of mixed figures/letter-signs inserted. D. Bourdeau's own working folder (`vieuville1587/`, sessions
of 22 September 2026, two passes) matched Tomokiyo's Nevers cipher key no. 16 (fr. 3995 f. 32v) against the code
numbers, confirmed by context ("42 et 43" = eschevins et maire de ville; "63̄" = La Vieuville, three times) and
against a dated sibling letter (31 Aug 1587, fr. 3416 f.53v). The three short letter-sign runs (33 signs) do
**not** decode under key no. 16 or any of the substitution/noise/confusable-class variants he tried, scored
against a matched-control ladder (900 real-French letters enciphered with a random 27-sign homophonic key at
0/20/40% glyph noise: the target's score, −4.53/char, matches the 40%-noise control, not the clean one).

## Image-quality assessment (per brief instruction)

**Not readable enough to count as copy-free.** Bourdeau's own conclusion, after native-resolution work on all
four pages across two sessions: the clear-text hand is only ~30–40% legible on the only available scan
(Gallica's B/W microfilm, `btv1b90605473`, all 396 canvases labelled "NP"; DECODE R4289's 14 images are cut from
the same microfilm). His explicit statement: "a colour scan or the original at the BnF is needed." This worker's
own confirmation fetch (below) agrees: at 500px the page is a clean-looking grayscale microfilm image, but the
hasty secretary hand is the kind of writing that needs full native resolution and better contrast than a B/W
microfilm gives to resolve reliably — consistent with Bourdeau's reported 30–40% figure from working the
originals at native zoom. **Verdict: copy-order** (a colour scan or BnF reading-room access), not copy-free.
Not nominated, per this lane's brief ("mark copy-order ... and do not nominate").

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk + Bourdeau's citations of it).** No solved tag for this item in the
   local snapshot or in Bourdeau's transcription of Tomokiyo's hidden comments (`nevers_tomokiyo.htm`, cited in
   his NOTES.md). Tomokiyo's own transcription of the 31 Aug 1587 sibling (fr. 3416 f.53v) is the source of key
   no. 16's confirmation, but he marks that sibling "NG" under a different key (no. 11) and does not claim a
   reading of this letter.
2. **Standard printed edition.** Actually read (by Bourdeau, cited with volume and search terms): Gomberville,
   *Mémoires du duc de Nevers* (1665) — part 1, Gallica `bpt6k6435941k` and `bpt6k8717151d`; part 2, Google
   Books `H2eV4wAmIr0C` (full-text searchable). Searched for "Vieuville / Vieville / Vieuuille / Aignan" near
   1587: **no hit**. This worker did not re-run the Google Books portion (out of this lane's allowed hosts) but
   the part-1 Gallica volumes and search terms are named and the negative is Bourdeau's own, not inferred.
3. **DECODE (sources/decode/) + both solver-repo clones.** Local DECODE snapshot: **R4289** (f.101, 1587–,
   Non-decrypted, French/French?) confirmed present (`records-non-decrypted-2026-09-24.tsv` line 448), matching
   the QUEUE row. dbourdeau/cyphersolver (shallow clone, 24 Sept 2026): `vieuville1587/NOTES.md` gives the
   fullest account (above); verdict "attempted, open (closed 22 Sept 2026, second session)... Not read." Full
   escalation checklist run (siblings, clear-pages, known-keys, print, key-rebuild, retry, images — all checked
   [x]). aaymeloglu/unsolved-ciphers: fresh shallow clone, no hit for "3975" or "Vieuville".
4. **Web search** (nothing beyond Tomokiyo/Bourdeau's own pages found in this pass; not separately re-run given
   Bourdeau's own escalation checklist already covers print/web).
5. **Ciphertext confirmed present on the Gallica leaf.** IIIF fetch, gallica.bnf.fr, 24 Sept 2026, 1 request:
   `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90605473/f185/full/500,/0/native.jpg` (view 185, f.101r). Image
   shows a full page of hasty French cursive script, grayscale/microfilm in character (flat contrast, faint
   ruling from the film), confirming both the cipher's presence (per Bourdeau's detailed inventory) and the
   image-quality concern above. Leaf: https://gallica.bnf.fr/ark:/12148/btv1b90605473/f185.item

## Verdict

**Blocked (copy-order): the only online image is a B/W microfilm Bourdeau's own close work reads at only
30–40%.** Not open, not nominated. No source of the six claims a decipherment beyond the code numbers (key
no. 16), which Bourdeau has already read; the three short letter-sign runs (33 signs) resist every substitution
model tried, validated against a matched noise-ladder control (rule 3): the target's score matches a 40%-noise
control, meaning the blocker is transcription accuracy, not the cryptanalysis. A colour scan or BnF
reading-room access, not more solver work, is what would move this.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 184; write-up
https://dbourdeau.github.io/cyphersolver/vieuville1587.html; `vieuville1587/` working folder — key no. 16
transcription, matched-control noise ladder, Gomberville/Google Books print check), CC BY 4.0 — prior attempt,
partial (code numbers read at grade H/C, the letter-sign runs not solved). S. Tomokiyo, cryptiana.web.fc2.com
(Nevers cipher key no. 16, fr. 3995 f. 32v; the 31 Aug 1587 sibling transcription).

Not decoded, not transcribed here (out of scope for check-solved). Rule 10: no novelty claim made; this is a
search result, not a verifier's classification.
