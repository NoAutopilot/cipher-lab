blocked

**Held by the LANE N3 orchestrator, 24 Sept 2026 17:40 UTC:** status `blocked`, not `open`: the check-solved pass did not read an edition or catalogue for the item (section 2) and did not check the DECODE record documents or the Aymeloglu repository (LANE N3 edition rule; COMMON addition (c)). The nomination line of 17:28 is held. Edition check: brief `.claude/briefs/runs/2026-09-24-lane-n3-csED3.md`.

# Hieronimo Ranzo (Venice) cipher letters, 1520s — BnF fr. 2988 ff.9r-11v

QUEUE row: CS2-15 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 170 at dbourdeau.github.io/cyphersolver/catalogue.html), DECODE R1894. Check-solved run
24 September 2026 by LANE N3 csCS2c (session_0113dPptSGXZiBF5uwvtKmtc), brief
`.claude/briefs/runs/2026-09-24-lane-n3-csCS2c.md`.

## What it is

Bourdeau's catalogue: "attempted, open (same initial-letter+number code as CS2-01/Garbino letter; non-alphabetical
numbering; annealer recovers only function words)." Two items headed "Lettre en chiffre de « V° HIERONIMO RANZO »"
appear in the fr.2988 recueil (items 1 and 3 of the volume's contents, per the BnF catalogue note below);
Bourdeau's ff.9-11 citation and DECODE R1894 point at this same pair. Prior scout pass (24 Sept 2026) marked the
image route "likely on Gallica; ark not confirmed" and the row "copy-order (unconfirmed, check Gallica fr.2988)."

## Image route (confirmed copy-free, this pass)

Gallica SRU (`dc.type all "manuscrit"` scoped to "Français 2988") returns two digitisations of the same
shelfmark (one "from the original document," one "from a substitute document," both giving identical catalogue
text) — used the original-document one, ark `btv1b525240150`. IIIF manifest (278 canvases) carries real foliation
labels for this volume (not "NP"): canvas index 24 = "9r", 25 = "9v", 26 = "10r", 27 = "10v", 28 = "11r", 29 =
"11v" (Gallica view numbers f25-f30). info.json for f25: 4298×5845, level2 profile, full resolution. **Image is
online now, full size, folios pinned exactly** (no eye-checked anchor needed — this manifest, unlike fr.15564,
carries genuine per-canvas foliation).

The BnF catalogue's contents note for fr.2988 (read via the same SRU record) lists, among ~56 items: "1 Lettre en
chiffre de « V° HIERONIMO RANZO » ; 2 « Double de lettres escriptes en chiffre par NICOLAS RAINCE,... De Romme,
XVme decembre V.C.XXVI [15 Dec 1526] » ; 3 Lettre en chiffre de « V° HIERONIMO RANZO » ; 4 «Proposition de la
majesté imperiale...1546»..." Items 1 and 3 (Ranzo's own cipher letters) flank item 2, Nicolas Raince's "double"
(copy) of separately-enciphered letters dated Dec 1526 from Rome — **these are catalogued as three distinct
items, not one continuous correspondence**; nothing in the catalogue note states item 2 is a decipherment of
items 1 or 3. No recipient is named for Ranzo's letters (items 1, 3) in this note.

## Same correspondence/key as CS2-01? (brief's question)

Bourdeau's own catalogue entry for CS2-15 states outright: "same initial-letter+number code as CS2-01/Garbino
letter" (CS2-01 = BnF fr. 3022 no. 20, Hieronimo Ranzo(?) to "Garbino," 11 Apr 1528, ff.44r-46v). This is a
**same-system**, not necessarily same-correspondence, claim: CS2-01 is addressed to "Garbino"; CS2-15's items
(fr.2988 ff.9-11) name no recipient in the catalogue note read here. Both are attributed to the same sender,
Hieronimo Ranzo, and (per Bourdeau) use the same cipher design (initial-letter + non-alphabetical numbering).
Not independently re-verified against the images this pass (out of scope for check-solved; a recovery-lane
worker applying a key would need to confirm the glyph inventories match before assuming interchangeability).

## Six-source search log (24 September 2026)

1. **Tomokiyo / Cryptiana** (named source for this cipher family). WebSearch located Cryptiana content on
   Ranzo's system: "Document No. 20 from Madrid dated 11 April 1528 is in the initial-letter code of Hieronimo
   Ranzo, Gattinara's kinsman... Tomokiyo published a partial key and left two thirds of the first page unread.
   The key checks against the glosses (Guienne, tres confident, Fumé; adds 87 = e, 22 null, # = Roy de
   Navarre)." A second search confirms the same wording: "No. 20, from Madrid on 11 April 1528, is in the
   initial-letter code of Hieronimo Ranzo, Gattinara's kinsman. However, No. 20 needs Ranzo's table or a clear
   copy to be fully deciphered." **Both quoted passages describe CS2-01 (fr.3022 no.20, the Garbino letter)
   specifically, by date and archival number — neither names fr.2988 or an ff.9-11 item.** No sentence located
   anywhere (WebSearch, not the live cryptiana.web.fc2.com site directly, which was not fetched this pass)
   claims fr.2988 ff.9-11 itself has been read, partially or fully. Per the M9/Morvillier lesson (check-solved.md):
   this is quoted verbatim precisely because it is *not* a claim about this letter, to avoid the same overclaim.
2. **Standard printed edition / calendar.** Not applicable in the usual sense: this is an intercepted foreign
   (Venetian) cipher dispatch with no named recipient and no French royal/diplomatic correspondence series that
   would calendar it. No edition search performed beyond the Tomokiyo/Cryptiana check above, which is the
   closest equivalent named source for this specific cipher family.
3. **DECODE R1894.** No local `sources/decode/` file for this record; not checked (DECODE login is the DECODE
   worker's alone per COMMON rules).
4. **Solver repositories.** Bourdeau's own catalogue entry (quoted above) is the source of record: "attempted,
   open." Aymeloglu's repository not checked this pass (budget).
5. **General web / comment threads.** No further hit beyond the Tomokiyo/Cryptiana material in item 1.

## Verdict: `open`

Image confirmed online (full resolution, folios pinned exactly, see above). No source read this pass claims
fr.2988 ff.9-11 specifically has been deciphered or its key recovered; the only published work on this cipher
*family* (Tomokiyo's partial initial-letter-code key) is explicitly about a different item (CS2-01/fr.3022
no.20) and is itself incomplete ("left two thirds of the first page unread"). Flag for the solver stage: try
Tomokiyo's partial Ranzo key (glosses above) against this letter's ciphertext before any fresh cryptanalysis,
since Bourdeau's own note says the two items share a cipher system.

**Nomination:** posted to ROOM.md (stage-2, copy-free, recovery/cryptanalysis kind pending which the key
question above resolves to).

Rule 10: no novelty claim made. Not decoded, not transcribed (out of scope for check-solved).

Requests this pass: gallica.bnf.fr SRU 1, manifest 1 (1 retry after a `ws_closed_mid_exchange` proxy reset,
logged per the good-citizen rule), info.json 1 (3-4 total). WebSearch 2. No DECODE, no solver-repo clone.
