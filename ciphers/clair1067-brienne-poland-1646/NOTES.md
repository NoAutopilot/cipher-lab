open

# Loménie de Brienne to the Queen of Poland, BnF Clairambault 1067, 19 May 1646

QUEUE row: M18 (sources/solver-diffs — "Third pass, 24 September 2026 (M17-M21)" section of QUEUE.md).

## Source

BnF, Departement des Manuscrits, **Clairambault 1067**, part of the composite "Clairambault 1058-1110,
Mélanges généalogiques et historiques, classés par ordre alphabétique des noms de familles et de matières"
series (finding aid `archivesetmanuscrits.bnf.fr/ark:/12148/cc137820/FRBNFEAD000013782_info`, fetched this
sweep). Gallica digitisation: `ark:/12148/btv1b9000856f` (422 canvases; QUEUE also names `btv1b90008551` as a
second, unconfirmed digitisation of the same volume, not checked this pass). This individual volume is
catalogued "X BRUN (DE)-BUX (DU)" — confirmed by the finding aid: the item immediately before and after the
Brienne entry are "Bournonville" (Fol. 223) and "Bourc de Geoli" (Fol. 225)/"Bouvery" (Fol. 230), all B-names.

**Precise catalogue entry, from the finding aid's own item list (not just the OAI summary QUEUE quoted):**
"**Fol. 226** • Lettre avec chiffres adressée par de Brienne à la reine de Pologne (19 mai 1646)." A short,
single-item entry (the next item starts at Fol. 230), so probably a 1-4 folio letter.

## Check-solved sweep (24 September 2026)

1. **Web search.** "Loménie de Brienne lettre reine de Pologne Marie-Louise de Gonzague 1646 correspondance" and
   "'Marie-Louise de Gonzague' correspondance France 1646 Brienne édition lettres". Surfaced: Marie-Louise de
   Gonzague (Queen of Poland from her March 1646 proxy marriage) corresponded with Mazarin in cipher after
   arriving in Warsaw (fr.wikisource.org, "Un Mariage politique au XVIIe siècle — Marie de Gonzague à Varsovie":
   *"En quittant Paris, elle avait emporté un chiffre qui lui permettait de correspondre avec Mazarin en toute
   sécurité"* and a later "letter half in ciphers, half in clear" to Mazarin on arrival) — general context for
   why a Secretary-of-State letter to her might be ciphered, not a hit on this specific 19 May 1646 letter. That
   Wikisource article was fetched directly and checked for a 19 May 1646 date or any Brienne letter: **none
   found** (its cipher discussion is all Queen-to-Mazarin, not Brienne-to-Queen). Also surfaced *Lettres inédites
   à Marie-Louise de Gonzague... sur la cour de Louis XIV (1660-1667)* (Magne ed., 1920) — wrong decade (1646
   vs. 1660s), not the same letter. No dedicated printed edition of Brienne's own outgoing letters to the Queen
   located.

2. **Print/scholarship.** Tomokiyo's `louisxiv0.htm` (local mirror, already flagged as a same-office lead by the
   QUEUE row) gives two Brienne ciphers, both to a **different correspondent** (Comte d'Estrades, the
   Netherlands ambassador) and **later dates**: "Brienne's Cipher 1" (p.501, letter of 28 June 1647, also used
   19 Sept 1647) and "Brienne's Cipher 2" (p.45/163, letters of 28 April and 20 September 1651). Neither is
   dated 1646 and neither is addressed to the Queen of Poland. This is a plausible same-office design lead (the
   Secretary of State's bureau likely reused cipher designs across correspondents in a similar period) but **not
   a match, not tried as a key this pass** — flagged for a solver, not applied here.

3. **Community lists.** `sources/cryptiana/` grepped for "clairambault 1067", "brienne.*pologne", "pologne.*
   brienne", "gonzague": no hit beyond `louisxiv0.htm`'s unrelated D'Estrades ciphers above.

4. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` grepped for "Clairambault 1067", "clair1067",
   "Brienne.*Pologne", "Pologne.*Brienne", "Gonzague": no row.

5. **Bourdeau.** Fresh shallow clone grepped for the ark (`btv1b9000856f`/`btv1b90008551`, 0 hits) and bounded
   "Clairambault 1067" (0 hits). The repo's only Brienne item is unrelated: "Bordeaux → Brienne" (Brienne as
   *recipient* at London, 30 May 1653, BL Add MS 4200, solved 18 Sept 2026 with the English Deciphering Branch's
   own key sheet) — a different direction (someone writing *to* Brienne, not Brienne writing out), a different
   archive (BL not BnF), a different year, no overlap.

6. **Aymeloglu.** Fresh shallow clone; catalogue and target folders grepped for "1067", "brienne", "pologne",
   "gonzague": no hit.

Requests: gallica.bnf.fr 5 (1 IIIF manifest, 1 Pagination service call [422/422 pages "NP", confirms this
manuscript carries no Gallica-indexed foliation, same finding as clairambault361-marini-1610's precedent], 1
ContentSearch call [0 hits for "Pologne", confirms no OCR index either], 2 native-image probe fetches at
naively-offset canvas guesses [f246, f232] — both landed on unrelated **later, printed** material bound into
the same composite volume (an 18th-c. judicial "Arrêt"/factum text mentioning dates 1701-1702, folio stamps
"117"/"45" and "110"/"32" respectively, neither matching the target period), matching the clairambault361
precedent that naive folio=canvas guesses fail on these composite Clairambault volumes), archivesetmanuscrits.
bnf.fr 1 (the finding-aid info page, HTTP 200 after a 302 redirect handled with `-L`), WebSearch 2, WebFetch 1.

## What the leaf shows

**Not located by image this sweep.** Two calibration probes, both wrong (see above); a third/fourth attempt
was not made this pass to stay within a reasonable request budget for one target, given the good-citizen
1.5s-apart /≈40-total-request ceiling shared across all three M17-M19 targets and that M19's leaf (below) still
needed fetching. The manuscript is not paginated or OCR'd in Gallica's own services, so folio 226 cannot be
reached without either a better calibration point (a labelled facing page, a known sibling item's confirmed
canvas) or a further, more patient probing pass — left as the next concrete step for whoever picks this target
up next.

## Verdict

**Open.** No published plaintext, decipherment, or key lead specific to this letter found in six sources. The
Tomokiyo same-office cipher designs (1647, 1651, different correspondent) are a real but unconfirmed lead, not
a match — a solver should try Brienne's Cipher 1/2 against this letter's ciphertext once an image is obtained,
before any cryptanalysis from scratch. **Leaf not viewed** — the single open item before this target can go to
stage 2 with confidence on the image side; the finding-aid text itself (precise folio, single short item,
correct alphabetical neighbours) is solid.

Not touched: no key application, no decoding, no novelty wording.

## (1) Leaf pinned, 24 September 2026

**The leaf is on Gallica, but not on the ark used by the prior sweep.** `btv1b9000856f` (the ark checked so
far) is a different/incomplete digitisation of this shelfmark: its own foliation (read directly off the
pencil/ink stamps visible on the leaves, not assumed) only reaches roughly fol.205-211 by its last real
canvas, confirmed by three probes (canvas280 stamped fol.134, canvas372 stamped fol.180, canvas400 stamped
fol.194 — a consistent 2-canvases-per-folio rate that extrapolates to canvas ~460-465 for fol.226, beyond that
ark's 422-canvas extent). Its earlier probes (canvas232/246, from the check-solved pass) and this pass's own
(canvas280/372/400/415) all land in the SAME two large printed-factum clusters bound early in the volume (the
Roland/Mège/Caille Grenoble lawsuit series, fol.95-195ish, and the Buray/Mahieu/Santeuil succession treatise
starting fol.253) — internally consistent, just short of the target.

The correct ark is **`btv1b90008551`** (flagged by the scout as an "unconfirmed second digitisation" — now
confirmed as the real one for anything past ~fol.205). Its own IIIF manifest metadata states "381 feuillets",
exactly matching the finding aid's own maximum folio citation (Fol.381, "Ginot du Bux", the volume's last
item). Calibration: canvas5 stamped fol.205 (content matches the finding aid's "Fol.205 Abbé Brunier de
Larnage, lettres autogr."), canvas226 stamped fol.313 (content matches "Fol.253 dame Buray" treatise, still
running at fol.313), giving a fitted rate of (313-205)/(226-5) ≈ 0.489 folio/canvas. That predicted canvas 48
for fol.226, and canvas 48 is confirmed by direct read of its own stamp ("226", clearly legible top-right) and
by content: the leaf opens "Madame" and the letter closes (canvas 53) "A Compiegne ce XIXe May 1646" signed
"Brienne" — an exact match to the finding aid's "Lettre avec chiffres adressée par de Brienne à la reine de
Pologne (19 mai 1646)".

Full item-list extraction from the finding aid's own HTML (`archivesetmanuscrits.bnf.fr/ark:/12148/cc137820/
FRBNFEAD000013782_info`, one fetch, cached at `/tmp` this session only — not yet mirrored to the repo) gives
every "Fol. N" citation for Clairambault 1067 end to end (Fol.1 "Isaac de Brun de Castellanne" through Fol.381
"Ginot du Bux"), which is what let this pass identify the two printed-factum clusters by content and rule out
the first ark with confidence rather than guessing offsets blind. Worth mirroring to `sources/` for the next
worker who needs another folio in this shelfmark.

Gallica requests this pass: ~19 to gallica.bnf.fr (1 manifest fetch each ark; probes at canvas 280/372/400/415/
422 on btv1b9000856f, canvas 5/48/49/50/51/52/53/139/226/227 native+thumbnail fetches on btv1b90008551, plus
line-crop native fetches for canvas 48/49/50 already counted in the crop tool's own one-request-per-region
design), one at a time, ≥1.5s apart, UA `cipher-lab research script (contact via repository)`. Two proxy-side
`ws_closed_mid_exchange`/connection-reset failures (canvas400 first attempt, canvas52), both recovered on the
single allowed retry (confirmed proxy-side per `/root/.ccr` status, not a Gallica block, matching the
established precedent). 1 request to archivesetmanuscrits.bnf.fr (the finding-aid info page).

## (2) What the leaf shows

**Extent:** canvas 48-53 on `btv1b90008551` = fol.226r, 226v, 227r, 227v, 228r, 228v. Six sides, three folios.
No fol.229 content found before the next finding-aid item (fol.230, Bouvery) — canvas 54 not checked this pass
(out of scope once the extent needed was established).

**How much is cipher:** fol.226r (canvas48) is mostly clear French (8 text lines) with cipher confined to its
last two lines only (e.g. "35 18 84 35" and "40 54 [overline]65 64 88 48 [overline]d 13 no 27"). fol.226v
(canvas49) and fol.227r (canvas50) are dense throughout: short clear-French captions ("aux Minisitres", "de
gouvernement", "Voſtre Maté", etc., mostly 1-3 words) followed immediately by a line of cipher groups, some
with an overline/macron. fol.227v (canvas51), fol.228r (canvas52) and fol.228v (canvas53, the closing +
signature + dateline) are **pure clear French, no cipher** — matter-of-fact military/diplomatic news (Monsieur
le Duc d'Anguien's army, the Prince Thomas's fleet at Vigo, Compiègne). So: cipher is concentrated in the
first three of six sides (226r sparse, 226v and 227r dense), then the letter turns to plain French for its
back half. This matches the finding aid's own description, "Lettre avec chiffres" (a letter *with* ciphers,
not entirely in cipher), and the same hybrid clear/cipher style already characterised for this office in
`ciphers/fr5160-letellier-1653/NOTES.md`.

**No interlined or facing decipherment.** fol.226r shows faint, differently-oriented handwriting bleeding
through from the verso in the left margin (checked at 3x crop: it runs in a different flow/orientation than
the recto's bold cursive and does not line up with the recto's own lines) — this is ordinary paper bleed-
through, not a contemporary decipherment beside the cipher. No decipherment was found on any of the six sides
or on the two probed neighbouring canvases (canvas47, blank/stained; canvas53, closing text only). This
target proceeds as a blind transcription + mechanical key trial, per the brief; it is not a recovery-by-
alignment case like fr5160-letellier-1653's fol.87.

Images: `images/src_ark_12148_btv1b90008551_f48_full_ref1600.jpg` (and f49/f50, downscaled to 1600px wide to
keep the folder under 30MB; native fetched fresh on demand), plus line crops `f226r_body_L*`, `f226v_L*`,
`f227r_L*` and their `*_lines_debug.jpg` overlays. Calibration-only probes (`probe_f*.jpg`, `probe2_f*.jpg`)
kept for the reproducibility trail.

## (3) Two blind transcription passes, 24 September 2026

Two independent Sonnet subagents transcribed the three cipher-bearing leaf-sides (fol.226r's last line,
226v, 227r) blind from the line crops — neither given the other's output, neither given any existing key or
reading — to `passA.tsv` and `passB.tsv` (line/position/group/confidence, the project's standard format;
overline/macron marked with a leading `_`). Both independently reported that the tool's automatic line-crop
boundaries frequently split or merged physical lines on this page (tight interlinear spacing, captions
bleeding across crop numbers) and reconstructed the true line sequence from the full-leaf reference images
rather than transcribing each crop slot literally — flagged here since a future reconciler should expect the
two passes' line-numbering to already represent each transcriber's own best line segmentation, not a
mechanical 1:1 crop mapping.

| pass | lines | cipher tokens (226r/226v/227r) | total |
|---|---|---|---|
| A | 57 | 16 / 156 / 161 | 333 |
| B | 57 | 17 / 159 / 156 | 332 |

Both passes agree with the brief's own description: cipher confined to fol.226r's last physical line, dense
on 226v and 227r. Both independently flagged the same trouble spots by kind (not necessarily the same exact
tokens): a recurring loop-shaped symbol read inconsistently as `v`/`c`/a null-letter code, a few digit pairs
genuinely hard to call (e.g. 75/73/59, 38/88), one dense stretch of 227r (pass A: lines 14-17; pass B similar
region) marked low-confidence throughout, and one very faint near-illegible line low on 227r. No third pass or
reconciliation attempted — out of scope for this brief (mechanical key trial runs on pass A only, per
instruction); a future transcription campaign on this target should expect the same "more than a tenth of
rows disagree" trigger for a third pass that fr5160-letellier-1653 and fr20140-danzay-1557 hit, given the
independently-reported line-segmentation ambiguity above.

## (4) Mechanical key trial (pass A only), 24 September 2026

`decode.py key_brienne_1647.tsv passA.tsv --check` and the same for `key_brienne_1651.tsv`, both seed 1
(script and both key tables copied in from `ciphers/fr5160-letellier-1653/`, Tomokiyo's published Brienne's
Cipher 1 [DE=46, Clairambault 411, 1647] and Cipher 2 [DE=47, Clairambault 579, 1651] tables, per the same
same-office lead already flagged for fr.5160). `--check` confirms both runs are deterministic. passA.tsv has
333 cipher-group tokens.

| key | resolved (H) | unresolved (U) | decoded chars | French-word chars (real) | French-word chars (shuffled control) |
|---|---|---|---|---|---|
| key_brienne_1647.tsv (DE=46, 1647) | 123/333 | 210/333 | 173 | 72 (41.6%), 31 words | **80 (39.0%), 40 words** |
| key_brienne_1651.tsv (DE=47, 1651) | 129/333 | 204/333 | 176 | 43 (24.4%), 20 words | **58 (22.1%), 23 words** |

**Both keys score at or below their own shuffled-key control** (rule 3: no negative without a matched
control) — the 1647 key gives fewer French words than its control (31 vs 40) and the 1651 key does too (20 vs
23). Same clean-negative pattern already established for fr.5160 against these same two published keys: this
is Loménie de Brienne père's office, but writing to a *different* correspondent (D'Estrades, 1647 and 1651)
than the Queen of Poland (1646) — a same-office lead, not this letter's own key. Grade: mechanical trial only,
no H/C grade applies (the "resolved(H)" counts mean only "this code string appears in Tomokiyo's table", not
that the resulting plaintext is correct). No cryptanalysis attempted beyond this trial, per brief.

## Status and next step

**Status stays `open`.** This pass: pinned the leaf on the correct ark and diagnosed why the other ark
looked empty for this folio (section 1); established extent and confirmed no interlined/facing decipherment
exists, so this is a blind-transcription target, not a recovery-by-alignment case (section 2); produced two
independent blind transcription passes (section 3); mechanically ruled out both published same-office Brienne
keys as direct hits, with matched controls (section 4). No decipherment recovered, no novelty wording.

**Cheapest next step:** a third transcription pass or higher-resolution/tighter-region crops to resolve the
line-segmentation disagreement flagged in section 3, before committing a canonical ciphertext.txt — this
letter's own key still needs to be recovered from scratch (cryptanalytically, or by finding a sibling
Brienne-to-Warsaw letter with a facing decipherment elsewhere in this correspondence), which is out of scope
for this brief.
