open

# Willem van Hessen to Willem van Oranje, partly unsolved cipher, 28 January 1567

QUEUE row: NB3 (`QUEUE.md`, "Dutch and Belgian archives (LANE N scout of 24 September 2026)").

## Source

WVO briefnr **1127** (https://resources.huygens.knaw.nl/wvo/app/brief?nr=1127), 28 January 1567, from Kassel.
William IV "the Wise", Landgrave of Hesse-Kassel (1532-1592; Anna of Saxony, William of Orange's second wife,
was his niece), to William of Orange. WVO's Inhoud field: "Bericht over de geboorte van een jonge dochter en
over het geschil tussen August van Saksen en Johan Frederik II van Saksen-Weimar" (news of the birth of a young
daughter, and of the dispute between August of Saxony and Johann Friedrich II of Saxe-Weimar) -- this is the
**Grumbach Feud / siege of Gotha** (Dec 1566-Apr 1567: Johann Friedrich II sheltered the outlawed Wilhelm von
Grumbach, was placed under the Imperial ban 12 Dec 1566, and August of Saxony besieged him at Burg Grimmenstein,
Gotha, until its fall 13 Apr 1567 -- a well-documented episode, confirmed by WebSearch, but no source located
naming this specific letter).

**One WVO record covers both copies:**
- The **original** (where the cipher sits): Koninklijk Huisarchief Den Haag, A 11/XIV B/15-43. **No PDF listed
  in the WVO database this pass** -- not copy-free for the cipher passage itself.
- The **draft/minuut**: Hessisches Staatsarchiv Marburg, Bestand 3II, Nassau-Niederlande, Korr. 1567, f.
  151r-152v. Free PDF, no login: `resources.huygens.knaw.nl/media/wvo/images/01000-01999/01127.pdf`.

WVO's Opmerkingen field states plainly: **"Een gedeelte van het origineel is in onopgelost cijferschrift. De
minuut geeft de complete tekst."** (Part of the original is in unsolved cipher. The draft gives the complete
text.) **Confirmed by eye this pass** (`images/01127_p1-1.png`): page 1 of the draft PDF is the outer address
leaf, docketed "An Printzen zu Uranien" (To the Prince of Orange) with a receipt note "28 Januarij ... 1567",
confirming the correct record and date. The draft's running text (its other pages) was not opened further this
pass -- not required to confirm the record, and this brief's instruction is to confirm presence, not transcribe.

**This is explicitly flagged by the WVO curators as the crib case named in the brief**: if the draft is a
compositional draft (not simply an earlier version covering different content -- see caveat below) of the same
letter whose original is partly enciphered, the plain draft text corresponding to the enciphered original
passage is a known-plaintext crib, and the task becomes alignment against the (unseen) original ciphertext, not
cryptanalysis from scratch. **Caveat, not resolved this pass**: a "minuut" can be an earlier compositional stage
that was then revised before the fair copy was made and partly enciphered, so the draft and the enciphered
passage are not guaranteed to cover identical wording -- this needs checking directly against the original once
imaged (see REQUEST.md).

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents).

1. **Editions first.** No printed-edition citation in WVO's own Brongegevens for 1127 (manuscript only, both
   copies). Rommel's *Geschichte von Hessen* (named in CLAUDE.md's editions-first list for Hesse) covers only
   up to Philip the Magnanimous's death in 1567 in its original four volumes (1820-1830); its continuation,
   *Neuere Geschichte von Hessen* (1835-1843), was not located specifically for William IV's Kassel
   correspondence by WebSearch this pass -- flagged as unread, a genuine gap. The Grumbach Feud / siege of
   Gotha is separately well documented in German historiography (Wikipedia's Grumbach Feud article, Deutsche
   Biographie, Gotha local-history pages, all read via WebSearch this pass) but none of the sources surfaced
   name this specific letter, its cipher, or a decipherment.
2. **WVO curatorial field.** As above: the curators explicitly label the cipher "onopgelost" (unsolved) in
   their own Opmerkingen field -- the strongest and most direct of any of this batch's four targets (contrast
   NB1/NB2, which are silent rather than explicit).
3. **Community lists.** `sources/cryptiana/web/dutch.htm` read in full: no mention. WebSearch (`Rommel
   Geschichte von Hessen Wilhelm von Hessen Willem van Oranje 1567 brief Chiffre`; `Grumbach Fehde 1567 Gotha
   Johann Friedrich Wilhelm Landgraf Hessen Brief 28 Januar`) found nothing naming this letter or a solution.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for the same terms as NB1/NB2:
   zero hits.
5. **Solver repositories.** Same fresh clones as NB1/NB2 (24 Sept 2026): no hits relevant to Willem van Hessen
   or this correspondence.
6. **General web search.** As item 3.

## Verdict

**Status: open.** WVO's own curators state the cipher is unsolved; no printed edition, community list, DECODE
record or solver repository names a decipherment. The Rommel continuation volumes (*Neuere Geschichte von
Hessen*) remain unread -- flagged as the clearest next step for a future edition check.

**Copy status: partial / not fully copy-free.** The draft is copy-free (free PDF, confirmed reachable and
viewed). **The original, where the cipher itself sits, has no PDF in the WVO database this pass** -- see
REQUEST.md for a copy-order ask to the Koninklijk Huisarchief Den Haag (A 11/XIV B/15-43).

**Kind: cryptanalysis (crib available)**, pending confirmation that the draft and the enciphered original
passage cover the same content once the original is imaged.

## csWV3: two further circle letters, not candidates (LANE N2, 24 September 2026)

Print-status pass across all 73 un-nominated WVO cipher letters (`.claude/briefs/runs/2026-09-24-lane-n2-csWV3.md`;
full table `sources/wvo/print-status-2026-09-24.tsv`). Two more Willem van Hessen letters, not in this folder's
existing table (which covers 1127 above):

- **Briefnr 174** (9 Apr 1567, "to Willem van Hessen", Antwerpen, GPA;HHSAWB;HSAM;KHAG). WVO's own remark:
  "solved on leaf" -- a contemporary decipherment accompanies the manuscript. Not fetched or imaged this pass.
  Flag for LANE R3 as a possible key source for the circle's cipher design (same correspondent as 1127, the
  cryptanalysis target above).
- **Briefnr 1069** (23 Mar 1563, "from Willem van Hessen", Marburg, HSAM;KHAG, no edition code). WVO Opmerkingen
  (fetched 24 Sept 2026, https://resources.huygens.knaw.nl/wvo/app/brief?nr=1069): "bij het origineel een
  exemplaar in cijferschrift en met ontcijfering" (beside the original, a copy in cipher AND WITH a
  decipherment). Not fetched or imaged this pass. Flag for LANE R3 as a second, earlier (1563 vs 1567) key
  source in the same correspondent circle.

Neither is a candidate; neither changes 1127's own cryptanalysis status above. Requests this pass:
resources.huygens.knaw.nl 1 (briefnr 1069 detail page, shared with the wider 9-page batch logged in
`sources/wvo/NOTES.md`); 174 read from `sources/wvo/cipher-letters-2026-09-24.tsv` only, no fresh fetch.

## OX-WVH, 25 September 2026: siblings 174 and 1069 fetched and eye-checked, sign-system check

Brief: `.claude/briefs/runs/2026-09-25-lane-ox-wvh.md`. Files fetched into `siblings/` (manifest.json there has
full detail; folder trimmed to 21 MB total to stay under the 30 MB/folder guidance -- both source PDFs and
several intermediate renders were deleted after review, refetch URLs are in the manifest).

**1. Briefnr 174 (9 Apr 1567, William of Orange to Willem van Hessen).** WVO record read in full
(Brongegevens, Opmerkingen). Its PDF (`pdf_url` in manifest, listed against the Hessisches Staatsarchiv Marburg
row) is a 12-page scan of a wider run of the same 1567 correspondence box, not only this letter's own 4 leaves
-- foliation jumps across the 12 pages confirm several distinct items are bundled in one PDF. Letter 174's own
cipher passages (p1-p10ish of the PDF) carry **no interlinear decipherment on the manuscript itself** -- plain
cipher blocks of geometric/arrow-style signs (Δ, arrows, □, ○, R, 8, Z, Π, X), visually a different "font" from
1069's system (below). **Page 11 of the same PDF is a loose nomenclator/alphabet KEY leaf** (different hand and
foliation from 174's own letter, so probably a sibling item from the same bundle, not literally part of letter
174) -- rotated -90 in the scan (`siblings/00174_p11_rot.png`). It gives: a plaintext a-z alphabet with 1-4
homophonic cipher signs per letter; a "Nulla" row of ~12 null signs; and roughly 24 nomenclator code-words with
their own homophonic signs, covering exactly the political vocabulary of the mid-1560s French/Imperial/Dutch
crisis -- Hispaniae rex, Franciae rex, Hispania, Gallia, Guise, Conde, Connestable, Bapst, Card. Lorraine,
Religio nostra / Religio papistica, La gouvernante(?), Imperator, Maximilianus (Emperor Maximilian II, reigning
from 1564 -- dates this key to 1564 or later), Reingraff, Engelandt, Denmark, Schweden, Rom, imperium. This
matches WVO's Opmerkingen for 174 almost exactly ("aan het eind van het ontwerp ... is aangegeven welke namen
door cijfers dienden te worden vervangen"), though the leaf's own foliation/hand doesn't cleanly match 174's 4
pages, so it is reported here as "found in the same bundle", not confirmed as 174's own appendix. Extracted to
`siblings/key_174_nomenclator.tsv` (grade H on the plaintext label almost throughout; grade M on a handful of
uncertain word readings and most exact glyph shapes, since these are invented signs with no Unicode equivalent
-- see the image for the true shape).

**Printed edition check (brief item 4, 174):** Groen van Prinsterer, *Archives ou correspondance inedite de la
Maison d'Orange-Nassau*, serie 1 deel 3 (1567-1572), pp.54-57, Lettre CCLXIX, viewed page-by-page via
resources.huygens.knaw.nl/retroboeken (`tools/browser_fetch.js`, a JS viewer). The full letter prints as
continuous German plaintext with no cipher markers, footnotes or italics anywhere -- since WVO's own Opmerkingen
says a decipherment copy exists beside the original, Groen printed the already-deciphered text seamlessly. So
**briefnr 174's plaintext, cipher passage included, has been in print since 1835-1847.** This matches its
existing table entry ("solved on leaf") and confirms it is not a candidate on its own; no new folder opened.

**2. Briefnr 1069 (23 Mar 1563, Willem van Hessen to William of Orange, answer to nr. 1068).** WVO record read
in full. Its PDF is the KHAG **origineel** itself (B 12, 6), 7 pages: p1 plain closing/signature leaf; **p2-p4
are the cipher passage, each WITH a contemporary interlinear decipherment written in a second, smaller hand
directly above the cipher lines** -- confirms WVO's Opmerkingen "bij het origineel een exemplaar in
cijferschrift en met ontcijfering" literally and visibly (`siblings/01069_p2.png` etc.). p5-p6 are a plain-text
postscript (news from France); p7 is the outer address leaf, confirming the record. Read closely (400dpi crop)
for line 1 of p2 only: the gloss spells out (with some letter ambiguity) "...mit Gr[u/m][n/mb]ach[s]", plausibly
"Grumbachs" -- Wilhelm von Grumbach, the outlawed knight whose feud (siege of Gotha, Dec 1566-Apr 1567) is the
same affair named in the TARGET's own WVO Inhoud field for 1127 (28 Jan 1567), three-plus years later --
consistent political context across this correspondent's letters even though 1563 predates the Feud's acute
phase. Extracted 10 sign->letter pairs to `siblings/key_1069.tsv` (7 grade H, 3 grade M; only line 1 of p2 read
this pass -- p2's remaining lines and p3-p4 are unread, flagged as the clear next step for a dedicated
transcription pass, out of this brief's scope).

**Printed edition check (brief item 4, 1069):** no "editie" row in WVO's Brongegevens for 1069 -- only the two
manuscript sources (HSAM minuut, KHAG origineel). Not found printed elsewhere this pass (no further search run,
out of brief scope). Note for the orchestrator: the earlier scout tsv's "solved elsewhere (edition not resolved
this pass)" for 1069 is corrected by this pass -- 1069 is solved **on the document itself** (contemporary
interlinear decipherment, confirmed by eye above), not in a printed edition; no edition exists to resolve.

**3. Do 174 and 1069 use the same cipher system (sign shapes)?** Not conclusively the same, and probably not
identical, but with one suggestive overlap. 1069's interlinear system (curvy, zodiac/alchemical-flavoured signs:
H, œ-loop, dagger-cross, W-hump, hooked-o, yogh, X, h-with-bar, Π, R) and 174's own letter-body cipher (angular
arrows, Δ, □, ○, Z, Π, X, R) read visually as different "fonts", and the loose key leaf on 174's page 11 reads
as a third, more astrological-symbol-heavy set (☉, a Pisces-like sign, roman-numeral-like marks) again distinct
from both. The one specific match worth flagging: the sign this worker reads as "h-with-a-horizontal-crossbar"
decodes to plaintext **c** in *both* 1069's interlinear gloss (this pass, line 1 of p2) and 174's alphabet key
(page 11, column c) -- by eye, at this scan resolution, not a certain match, but a concrete, checkable one for a
follow-up pass with a side-by-side crop. No other pair was checked closely enough to compare. Overall: same
cryptographic tradition and design (homophonic substitution with word-nomenclature and nulls, arbitrary
invented signs, not a real alphabet or shorthand), consistent with a shared Hessian chancery workshop across
this correspondent's letters and years, but not demonstrated to be the literal same key. A dedicated
side-by-side glyph comparison (crop every distinct sign from both systems at matched zoom, align by decoded
letter) is the clean next step and was out of this brief's scope (no decoding beyond sign-system identity).

**4. The target's own ciphertext (1127) -- still not copy-free.** No change from the existing REQUEST.md /
images/manifest.json finding: only the draft (crib, no cipher) is online; the original at KHAG A 11/XIV
B/15-43, where the cipher itself sits, has no PDF in the WVO database. This pass did not find it via 174 or
1069's records either (174 and 1069 are a different letter-pair, at KHAG/HSAM/HHStAW shelfmarks that do not
overlap with 1127's). REQUEST.md stands unchanged. The two siblings fetched this pass are useful once the
original is in hand: 1069 demonstrates this correspondent's cipher letters do carry legible interlinear
decipherments (so the original of 1127, if any decipherment survives beside it, may too), and 174's bundle
carries a period-correct nomenclator key covering exactly the vocabulary (rulers, factions, religion, empire)
1127's own Inhoud (the Grumbach Feud) would need.

**Kind unchanged: cryptanalysis (crib available)**, still pending the original being imaged. Status: **open**,
copy status: **partial**, unchanged.

Hosts this pass: resources.huygens.knaw.nl 2 record pages + 2 PDFs (curl, browser-contact UA, >=1.5s apart) + 3
retroboeken viewer pages (`tools/browser_fetch.js`, >=1.5s apart). No other host used.
