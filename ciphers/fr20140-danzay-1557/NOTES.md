# BnF fr.20140 — Charles de Danzay to Henri II / Cardinal of Lorraine, January 1557

Status: found-solved (3 of 4 items); partial (1 of 4, f.35: Tomokiyo's key read, 24 Sept 2026)
Novelty (f.35-36r, one letter): N4 (no prior decipherment located) per AUDIT.md "N4 decision (Cryptiana closed)", held after second opinion SO-DANZAY-F35 (V3b, 24 Sept 2026); use only the safe sentence there.

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Editions-first + one-leaf pass.
The formal six-source check-solved run for the f.35 remainder is done (below, same day); verdict unchanged:
open.

## Check-solved (24 Sept 2026, formal pass for f.35)

Second pass, same day, dedicated to the one remaining item, f.35 (27 Jan 1557, Danzay to the Cardinal of
Lorraine, "not deciphered" per Tomokiyo — quoted verbatim above). No reading or key application attempted;
this only asks whether the plaintext or a decipherment already exists somewhere in print. Every source below
checked 24 Sept 2026.

1. **Tomokiyo's page** (`sources/cryptiana/web/danzay.htm`, local mirror, already quoted above): the only
   source that names this exact folio and date. States f.35 is the one item of the four "not deciphered" and
   that he has "not seen (images of)" either printed edition below. No stronger claim available from this page.
2. **Correspondance de Charles Dantzai / Bricka (1901)** — checked what this edition actually covers, since the
   brief that opened this pass named it "the standard edition of exactly this correspondence." That is not
   correct and is corrected here: WebSearch confirms the 1901 volume's own title is *Indberetninger fra Charles
   de Dançay til det franske Hof om Forholdene i Norden 1567–1573* (Bricka, Copenhagen, C.A. Reitzel) — its
   subtitle states the span 1567–1573. It cannot contain a 1557 letter; ten years before its earliest despatch.
   Not chased further (HathiTrust `hvd.hnnfqp` catalog page itself 403'd to curl, Cloudflare-gated per the
   playbook; moot given the date mismatch already rules it out).
3. **Correspondance de Charles Dantzai (1824), Handlingar rörande Skandinaviens Historia vol. IX, Stockholm,
   Elmén et Granberg** — this is the actual candidate for 1557 material (from Swedish, not Danish, archives;
   Fryxell was the series' general editor across its run, hence "Fryxell's Handlingar" in the brief). Found a
   same-numbered volume on Internet Archive, `handlingarrrand06unkngoog` (Google-scan metadata: "volume": "9",
   "date": "1821" — the date field on these old Google-metadata records is frequently wrong/approximate and is
   not itself disqualifying). Fetched its full djvu text directly (no login, 447 KB, single request) and grepped
   locally: **zero** hits for "Danzay", "Dantzai", "Dançay" (any case) and **zero** hits for "1557" anywhere in
   the volume. Also checked archive.org's global full-text index (`be-api.us.archive.org/fts/v1/search`, no
   login needed) for "Dantzai" scoped to this identifier: 0 hits; and unscoped: 133 hits across the whole
   archive, none of them this identifier or an obvious sibling volume (top hits are an unrelated 1910 Danzay
   biography `undiplomatepoite00richuoft`, already known from Tomokiyo's own bibliography, and unrelated
   periodicals). Conclusion: either this Google-scan copy is a different volume that happens to share Google's
   internal "volume: 9" tag (the Handlingar series was rescanned/renumbered inconsistently across different
   Google Books projects — this is plausible, not confirmed), or the true 1824 volume IX is not on Internet
   Archive under a name this search surfaced. Google Books: no full-view edition found under the title
   "Correspondance de Charles Dantzai" or under "Handlingar rörande Skandinaviens historia" + "Dantzai" (0 hits
   both queries, `&country=US&key=$GOOGLE_BOOKS_KEY`, key never printed). **Not located; genuinely unreached,
   not searched-and-cleared** — this is the one source in this pass that stays an open gap, not a checked
   negative.
   *Verifier correction, 24 Sept 2026 (AUDIT.md):* the 1824 edition is Handlingar vol. **XI**, not IX (the
   series' own register: "Dantzai ... brefvexling, 11: 1-345"). It is IA `handlingarrrand02scangoog`, and its
   full text has no 1557 letter (years 1562-1579). Now reached; the letter is not in it. The gap is closed.
4. **Calendar of State Papers Foreign, Mary 1553–1558** (Turnbull, 1861) — a WebSearch hit surfaced a "Danzay,
   —, letter from, 290" index entry, but tracing it (British History Online, `cal-state-papers/foreign/vol16`)
   showed it belongs to volume 16 of the CSP Foreign series (context: "States' army", "Leicester's footman" —
   1580s Dutch Revolt material), not the Mary 1553-1558 volume. No Danzay entry located in the actual
   1553-1558 volume's own index by this method. Not chased further by direct page-by-page read (an English
   calendar of state papers is not where a French ambassador's outgoing despatch to a French cardinal would be
   calendared unless intercepted; low prior, and the brief's own source list treats it as a formality check).
5. **Internet Archive full text / general search**: covered under item 3 above; also ran a bare
   `archive.org/advancedsearch.php?q=Dantzai` title search — 0 hits.
6. **Solver repositories** — not re-cloned this pass; citing the M13-M16 check-solved worker's fresh shallow
   clones of both `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` from earlier the same day (24 Sept
   2026, this file's first section above), which found no hit on "20140" or "Danzay" in either. Re-cloning
   twice in one day for the same volume would be wasted cost against the same result; if this is later
   contested, redo it.

**Verdict: still open.** No source in this pass — the two printed editions, the English calendar, Internet
Archive, Google Books, or the solver repositories — produces a decipherment or plaintext for f.35 specifically.
The 1901 edition is ruled out on internal evidence (date range). The 1824 edition, the one edition that could
plausibly cover it, was not successfully located in full-text-searchable form this pass; this is a gap, not a
clearance, and should not be read as "checked, absent." Status stays open for f.35; the key is already
published (Tomokiyo) from the sibling decipherments, so this remains a recovery job, not cryptanalysis, per the
verdict already on record above.

## Images

Folio offset calibrated this pass directly from the primary ark's own IIIF manifest (`../manifest.json`, already
on disk, no fetch needed) rather than by probing: its canvas `label` fields carry the manuscript's own
foliation (e.g. canvas id `f69` → label `35r`), not just sequence position. Single-folio canvases run from
index 17 (`9r`); recto canvas index = `2×folio − 1`. Checked against three folios Tomokiyo names and confirmed
exact: `16r`→canvas 31, `24r`→canvas 47, `30r`→canvas 59. Folio 35: recto = canvas index 69 (`f69`, label
`35r`), verso = canvas index 70 (`f70`, label `35v`). This resolves the previous pass's "canvas-to-folio offset
uncalibrated" note — no probing needed once the manifest's own labels are read.

Fetched (gallica.bnf.fr, browser User-Agent, 1.5 s apart, 4 requests total this leg): a 1200px preview of each
canvas first (confirmed by eye — folio headed "35", margin dated "27 Jan. 1557", matching Tomokiyo's entry
exactly), then the native-resolution image for each (`f69` 4800×7062, `f70` 4791×7091). Also fetched, from
`cryptiana.web.fc2.com` (1 request), the key-table image `danzay_1557.png` that Tomokiyo's page embeds but that
was not previously mirrored (only the HTML was) — saved to `sources/cryptiana/web/danzay_1557.png`, needed as
the legend for the passes below.

f.35 recto is mostly clear French (Tomokiyo's letters do open in clear, per his page); the cipher is confined to
~7 lines at the foot of the page, beginning mid-sentence after "...Monseigneur je vous puis asseurer que".
f.35 verso is cipher from the first line to the last, no contemporary decipherment visible in the margin on
either leaf — consistent with Tomokiyo's "not deciphered." Cut three crops (local, from the native images, no
extra network fetch): `f69_cipher.jpg` (the recto cipher block, 2400×960), `f70_cipher_top.jpg` and
`f70_cipher_bot.jpg` (the verso cipher block split in two with a ~4-5 line overlap so no line falls on a crop
boundary, each 2400×~1515). Full provenance, pixel boxes and the offset derivation are in `images/manifest.json`.
Folder size 8.9 MB (native_f69.jpg 3.2 MB, native_f70.jpg 3.0 MB, three crops ~2.2 MB combined, two previews
~0.5 MB, plus the pre-existing 115 KB `alt_f40.jpg`) — well under the 30 MB cap.

## Passes

Two independent Sonnet subagents (`passA.tsv`, `passB.tsv`), neither shown the other's output or told what the
other found, transcribed the cipher signs on the three crops line by line (R1... for the recto, V1... for the
verso) against Tomokiyo's sign legend (`danzay_1557.png`: a–z minus j/k/v/w, a nulls column, and word-signs for
"dict/et/le/luy/quel?/son?" and "Dannemarch"/"le Roy de Dannemarch"), naming each sign by its legend letter,
"null", a "word:" gloss, or a per-pass "unkN"/"unk-shape" label for shapes matching nothing in the legend.
Format: `line position sign confidence` (H/M/L). No reconciliation, no key application, no decoding attempted —
that is explicitly out of scope for this pass. Both subagents independently reported the same limitation
unprompted: neither could confidently map individual small cursive cipher glyphs to a specific a-z legend
letter at the image resolution available to them, and both chose to invent per-pass placeholder labels for
those signs rather than force a guess into a wrong legend bucket (as their brief required). This means the
two passes' "unk" labels are **not comparable to each other** — they are two independently-invented, arbitrary
naming schemes, not two readings of the same sign inventory — so a sign-for-sign match rate between them would
be meaningless and is not reported.

What *is* comparable, and reported here:

- **Line coverage.** Pass A produced 37 lines (R1-R8, V1-V29, 796 sign tokens); pass B produced 24 lines (R1-R8,
  V1-V16, 307 sign tokens) and stopped there — it never reached the equivalent of pass A's V17-V29 (roughly the
  last third of the verso). This is a coverage gap in pass B, not a disagreement: that stretch has only one
  reading (pass A's), not two, and should not be treated as agreed.
- **Segmentation density on the cipher lines disagrees by roughly 2x.** On every recto/verso line that is still
  cipher (R1-R12, V1-V12), pass A consistently records far more tokens per line than pass B for the *same*
  manuscript line (e.g. R3: 29 vs 15 tokens; R6: 23 vs 14; V3: 28 vs 12; V12: 28 vs 10) — pass A is splitting
  individual strokes/letters more atomistically, pass B is grouping more marks into single signs. Both are
  plausible readings of dense diacritic cursive; neither should be preferred without a third pass or a
  higher-zoom re-read.
- **Clear-French runs agree well.** From V13 to the end of pass B's coverage (V16), both passes converge almost
  exactly in token count per line (12/12, 11/11, 12/11, 13/13) and in the actual words identified, once ordinary
  handwriting-to-OCR spelling variance is allowed for — e.g. pass A's V13 "le pflus comodement quil ne soea
  possible et soay buy quil y" vs pass B's V13 "le plus commodement quil me sera possible et say bien quil y":
  same 12-word sentence, recognisable as the same underlying French ("le plus commodément qu'il me sera
  possible, et sçay bien qu'il y..."), spelled differently by each pass's reading of the same secretary hand.
  Earlier partial-clear lines (R3, V7-V12) show the same pattern at lower density. This corroborates, independently
  of Tomokiyo, that plaintext French words really are interspersed as camouflage in this letter exactly as his
  page describes for the sibling ciphers, and that both passes are looking at the same underlying text.
- Both passes separately flagged a recurring symbol they associate with "Dannemarch"/"le Roy de Dannemarch"
  (pass A: 21 occurrences across the two folios; pass B did not use this label at all in its shorter coverage) —
  plausible given the letter's subject, but M-confidence in both cases, not corroborated between them the way
  the clear-French runs are, and not confirmed against the legend image at high enough zoom to be sure.

No reconciled reading, sign inventory, or decode attempt follows from this — per the brief, that is explicitly
out of scope for this pass.

## What the target is

Gallica ark `btv1b52521512h` (alt. digitisation `btv1b10782904z`), a recueil "Pièces relatives à la Suède et au
Danemark (1557-1706)". `services/OAIRecord` confirms: *"Correspondance, originale et en partie chiffrée, de
Charles de Danzay, ambassadeur en Danemark, 1557-1567 (fol. 16)."* — matches QUEUE.md M15 exactly.

## Checked (24 Sept 2026) — this is the found-solved finding

`sources/cryptiana/web/danzay.htm`, already mirrored locally (no fetch needed), S. Tomokiyo, "Danzay's Ciphers:
Ciphers of a French Diplomat with a Long Tenure" (first posted 22 Feb 2026). Per rule 10, quoted verbatim rather
than paraphrased, because it names this exact shelfmark and folios:

> BnF fr.20140 includes ciphertext in four letters from Danzay in the reign of Henry II:
> f.16 10 January 1557 (to Henry II, deciphered in separate sheets)
> f.24 10 January 1557 (to Cardinal of Lorraine, deciphered in the margin)
> f.30 27 January 1557 (to Henry II, deciphered in the margin)
> f.35 27 January 1557 (to Cardinal of Lorraine, not deciphered)
> The reconstructed cipher is as follows. It can be seen most double letters are represented by the letter
> itself with a diacritic sign above or below... many nulls are used...

Tomokiyo reconstructed the full substitution/diacritic key **from the contemporary decipherments already
present** on f.16, f.24 and f.30 (one "in separate sheets", two "in the margin") — i.e. three of the four
ciphered items are already deciphered in the manuscript itself and their plaintext is in hand; only f.35 lacks
a contemporary decipherment. He states he has not seen a fifth item beyond these four, and separately (same
page) that Ryabov (2025) independently reconstructed a *different*, later Danzay cipher (1574-1578, BnF fr.4736
and fr.2812) from similar marginal decipherments — a different volume, not this one.

- Fresh shallow clone of `dbourdeau/cyphersolver`: no hit on "20140" or "Danzay" tied to this volume.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers`: no hit.
- Printed editions Tomokiyo cites but has not seen images of: *Correspondance de Charles Dantzai, ministre de
  France à la Cour de Danemarck* (1824, from Swedish archives) and C.F. Bricka (ed. 1901, from Danish archives,
  HathiTrust `hvd.hnnfqp`) — both post-date 1557 material differently (Bricka's volume title says 1567-1573);
  neither confirmed or ruled out as covering the four January 1557 letters specifically. Not chased further this
  pass (Tomokiyo's manuscript-internal decipherment finding already settles the status for f.16/f.24/f.30
  regardless of print).
- Gallica IIIF: one connection reset on the primary ark fetching a canvas near the expected f.35 location,
  retried once per the good-citizen rule, failed again — stood down on that ark per the rule (one retry only)
  and switched to the alternate digitisation ark named in QUEUE.md. That ark's canvas 40 (`images/alt_f40.jpg`)
  showed two clear-French leaves, one headed with a leaf number "30" and a marginal date "1558" — **not
  confirmed as Tomokiyo's f.30** (canvas-to-folio offset uncalibrated for either ark, and no cipher or
  interlinear decipherment was visible on this particular canvas) — inconclusive, not a contradiction of
  Tomokiyo's report.

## Verdict

**Found-solved for f.16, f.24, f.30**: plaintext already exists in the manuscript via contemporary decipherment,
and Tomokiyo has already published the reconstructed key from it. No new cryptanalysis is possible or needed on
these three. **Open for f.35 alone**: the one item without a contemporary decipherment, but the key is already
published and this letter is written the same day (27 Jan 1557) by the same hand to the same correspondent type
as the deciphered f.30 — a cheap recovery/transcription job, not cryptanalysis. QUEUE.md M15's "kind" (currently
"cryptanalysis") should be corrected to **recovery (published key via sibling decipherment)**, matching the
Dupuy 468 / M15 pattern already established as precedent in LESSONS.md. Grade: no reading attempted by this
worker; f.16/f.24/f.30's grade is Tomokiyo's own H (contemporary decipherment) once transcribed, f.35 would
grade S (cryptanalytic, but with a key derived from H sources — closer to a recovery than a blind attack).

Cheapest next step: transcribe f.35 (one leaf) against Tomokiyo's published key and check it decodes to
coherent French; no image-hunting beyond that single leaf is needed.

## Sources

- Gallica: `https://gallica.bnf.fr/ark:/12148/btv1b52521512h` (primary), `https://gallica.bnf.fr/ark:/12148/btv1b10782904z` (alternate).
- S. Tomokiyo, "Danzay's Ciphers: Ciphers of a French Diplomat with a Long Tenure", cryptiana.web.fc2.com,
  mirrored locally at `sources/cryptiana/web/danzay.htm` — credit Tomokiyo for the key reconstruction and the
  identification of the three contemporary decipherments; this worker did no cryptanalysis.
- github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers (both checked, no relevant content).

## Requests this pass

gallica.bnf.fr: 1 OAI record + 1 manifest + 2 IIIF image attempts on the primary ark (1 connection reset,
retried once per rule, failed again, stood down) + 1 IIIF image fetch on the alternate ark (succeeded).
github.com: 2 shallow clones (shared with M13/M14, deleted after grep).

## Reading with Tomokiyo's key (solver, 24 Sept 2026)

Files: `ciphertext.txt` (791 tokens, one per row: line, position, sign code, H/M image confidence),
`inventory.tsv` (75 distinct codes, each with a glyph description, key value or UNKEYED, and count),
`reconciliation.md` (how passA/passB were settled), `key.tsv` (Tomokiyo's 1557 table as codes; source column
cites his cell), `decode.py` (writes `reading.txt` and `reading_tokens.tsv`; `--check` exits 1 if either is
stale), `reading.txt`.

**Transcription.** The two passes could not be merged sign by sign, because their `unk` labels are private to
each pass. So the cipher was read again, glyph by glyph, from native-resolution strips of f.35v (29 lines) and
from the f.35r crop (8 lines). Pass A's line numbering matches. See reconciliation.md. The letter does not end
on f.35v: V29 stops at "... du [xk]" at the foot of the page, and the text goes on to f.36, which is not on disk.

**Token grades (decode.py, cipher tokens only):** 638 cipher tokens, plus 152 clear-hand words and the 7-sign
gloss above V18.
- H 509: the sign was read clearly and Tomokiyo keys it to one value. 61 of these are his nulls.
- M 59: 19 keyed signs that are doubtful in the image, plus the 40 glyphs he keys twice (T = a/luy, hook = u/a). Two more doubtful signs, `D` and `S` (R4 pos 21), are unkeyed and counted under U.
- U 70: signs in none of his cells.
- (Counts after the second-reader adjudication of 24 Sept 2026; before it: H 508 / M 61 / U 69.)

No token is C, because there is no contemporary decipherment of f.35. Everything above is a reading
from his published key, which he built from the sibling decipherments on f.16, f.24 and f.30.

**Where the key reads continuous French** (cipher runs, allowing for nulls):
- Recto: R5 "preste ... sauf"; R6 "laquelle ... ne faultra"; R8 "present ... pour".
- Verso: V2 "chancel[l]i-r ... Danoys ... quelque"; V5 "... oyaume ... a promis"; V6 "qu'il ... renploy-er";
  V7 "-ence, dont"; V8 "les ... propos"; V9 "tenu / d'aultre part le chancelier"; V10 "peult ... beaucoup".
- Verso, continued: V11 "envers la ... "; V12 "prepare ... c'est a ... "; V17 "... et affections"; V18 "de ceulx
  desquels ... me ayder"; V19 "la resolution des"; V20 "... affaires ... pend"; V23 "de leur volonte".
- Verso, end: V24 "en doubte"; V25 "au mo[y]en ... de faire"; V26 "quelque ... Augsbourg"; V27 "par ... les
  marchans de Lion"; V28 "car de Augsbourg on le pourra".

**Where it does not:** R1, R2 (apart from "fort"), R3, R4 (apart from "n'empesche"), R7, V1, V3, V4, V29.
These lines carry most of the unkeyed signs and the M rows.

**Where the key fails, and what the image and context suggest.** These are grade I suggestions only. None is
applied in key.tsv or reading.txt.
1. `ring7` (7 with a ring, 10 uses) reads as **y** wherever the context is clear: "royaume", "moyen",
   "renployer", "Danoys".
2. `Y`, keyed by Tomokiyo as "son?" (his query), gives **e** twice ("chancellier" V2, "Royne" V11) and
   plausibly in V20 as well.
3. The script-L glyph coded `LRD` ("le Roy de Dannemarch" in his table) reads as a single **r / R** in V5
   ("royaume"), V11 ("Royne"), V26 and V28 ("Augsbourg"). Either this manuscript's glyph is a different sign
   from his, or the sign stands for more than one value.
4. The barred figure-8 `x8` (16 uses) fits best as a null (V28 "on le pourra", V17 "passions").
5. `I` reads as **q** ("quelque" V2 and V26, "desquels" V19).
6. Crossed long letters (`lsx`, `fdx`, `fdl`) look like doubled letters or d-variants ("passions",
   "affaires"). Uncertain.
7. `hk` is **u** in "Augsbourg" and **a** in "Danoys a", matching the two cells Tomokiyo draws for it.

A second reader applying these seven would still leave `ringT` (8 uses), `xk`, `circ`, `Pbar`, `S` and `Zl`
open.

**Plain sense, as far as the key reads it** (five lines; the clear passages carry much of it):
1. Danzay assures the Cardinal that the King of Denmark is ... (R1-R2 not fully read). He is anxious that ...;
   if there were an affair, it would not fail ... (R3-R8).
2. The Danish chancellor, and the Danes more generally, are discussed. Something concerning the kingdom was
   promised. The King's letters, "propos", and on the other side the chancellor, who "can do much" (V2-V10).
3. Something is said about the Queen. As soon as someone arrives Danzay will prepare ...; he has sent this
   despatch so the Cardinal knows the state of this kingdom's affairs and the long-standing promise (V11-V16,
   mostly clear).
4. He speaks of the passions and affections of those whose help he needs, and of affairs whose resolution
   depends on means he has followed and will keep to, while he awaits express command. He cannot yet vouch for
   their will, which is in doubt (V17-V24).
5. It seems good to consider the means of ... through Augsburg, by way of the merchants of Lyon, "for from
   Augsburg one could ...". The page ends mid-sentence, going on to recover something (V25-V29).

**Distinctive phrases for the verifier.** Clear hand:
- "le plus commodement qu'il me sera possible"
- "j'ay bien voulu faire ceste depesche affin que vous peussiez congnoistre l'estat des affaires de ce
  royaulme"
- "la promesse qui de long temps m'a esté faicte"
- "attendant plus certain et expres commandement de ce que je doy entreprendre"
- "il me semble qu'il seroyt bon de regarder"

From the key: "le chancelier", "Danoys", "marchans de Lion", "Augsbourg", "de ceulx desquels", "la resolution
des", "de leur volonte".

No print search was run in this session (verifier's job). Novelty is not classified.

**Follow-up suggestions** (not done):
- Fetch f.36r, where the letter continues.
- Have a second reader check the 61 M rows and the unkeyed codes on the same strips.
- Test suggestions 1-5 against the contemporary decipherments on f.16, f.24 and f.30.

## f.36 images and passes (24 Sept 2026)

Follow-up to the solver's note above that f.35v stops at "du [xk]" and the letter continues on f.36, which
was not then on disk.

**Images.** Canvas index read straight from the primary ark's own IIIF manifest labels (`../manifest.json`),
same calibration already established for f.35 (recto canvas index = 2×folio−1): folio 36 recto = canvas `f71`
(label "36r"), verso = canvas `f72` (label "36v") — confirmed by eye, no probing needed. Fetched
(gallica.bnf.fr, descriptive User-Agent, 1.5 s apart, 4 requests: 2 previews + 2 native): a 1200px preview of
each canvas first (confirmed by eye: leaf headed "36" top right, marginal date reading "...vingt sept jour de
Janvier 1557" [correction, verifier, 24 Sept 2026: this is the letter's own body dateline, not a marginal note. It reads "De Coppenhagen ce vingt sept jo[ur] de Janvier 155[7]", and f.36v carries the address to the Cardinal of Lorraine and the docket "[M]r de Danzay du xxvij de Janvier 1557"] — the same 27 Jan 1557 despatch — signed "Dantzay" at the foot), then the native-resolution
image for each (`native_f71.jpg` 4800×7062, `native_f72.jpg` 4791×7091, same dimensions class as `f69`/`f70`).

**f.36 recto carries only one line of cipher.** The top line is cipher; clear French resumes immediately on
line 2 ("Iy m'a...") and continues without interruption to the signature "Dantzay" at the foot of the page —
the letter's cipher does not run for multiple lines on this leaf, it is one more line and then the despatch
finishes in the clear.
[Correction, reconciler, 24 Sept 2026: lines 2-4 of f.36r also carry cipher signs, mixed with clear words;
clear-only text starts on line 5. See "f.36 reading (24 Sept 2026)".] **f.36 verso carries no cipher at all**: it is the address/docket panel of the folded
sheet (bleed-through of the recto text read in mirror, an address line, a wax seal), consistent with how such
letters were folded and addressed on the outside — not a continuation leaf. No crop was cut from it.

Cut one crop (local, from the native image, no extra network fetch): `f71_cipher.jpg` (2400 wide), the single
cipher line at the top of f.36r, with the start of line 2's clear French bleeding in at the bottom for
context. Full provenance and the pixel box are in `images/manifest.json`. Folder now 14 MB (adds
`preview_f71/f72.jpg`, `native_f71/f72.jpg`, `f71_cipher.jpg` to the existing f.35 set), well under the 30 MB
cap.

**Passes.** Two independent Sonnet subagents (`passA_f36.tsv`, `passB_f36.tsv`), neither shown the other's
output, this file, or any reading/key, transcribed the one cipher line (`R1`) against Tomokiyo's sign legend
(`danzay_1557.png`), same format as the f.35 passes (`line position sign confidence`, H/M/L), naming each sign
by its legend letter, "null", a "word:" gloss, or a per-pass "unkN" label for shapes matching nothing in the
legend.

- **Segmentation is close, not ~2x apart.** Pass A found 26 signs, pass B found 25 — a one-sign difference,
  much narrower than the roughly 2x segmentation gap seen on f.35's longer, denser cipher blocks. Consistent
  with a short, single, clearly-inked line rather than a dense multi-line block.
- **Position-exact agreement is low despite the close counts.** Comparing the two passes position by position,
  8 of the first 25 positions match exactly on sign label — `a`, `u`, `c`, `unk1`, `s`, `word:le`, `g`,
  `word:dict` at positions 1, 2, 4, 5, 8, 9, 10, 11 — roughly a third. Both passes agree through position 11
  (the line's first "word:dict") and then run out of position alignment for the rest of the line. Pass A's own
  report flags splitting two originally-auto-detected blobs into two signs each, at its positions 11-12 and
  22-23; this reads as a one-sign segmentation offset somewhere in that stretch, not a resolved disagreement —
  no reconciliation was attempted, per brief.
- **Both passes independently report the same word-sign occurring twice in this one line.** Pass A finds
  `word:dict` at positions 11 and 23; pass B finds it at positions 11 and 22 — offset by exactly one position
  on the second occurrence, matching the segmentation gap noted above. This is the strongest cross-pass
  corroboration in the line: both readers agree "dict" appears twice, close together, independent of the
  exact position count between the two occurrences.
- Both passes separately invented an identical placeholder label `unk1` for the same unmatched shape at
  position 5. This is a naming coincidence, not a shared code book (each pass invents its own labels blind,
  per brief, and the two are not otherwise comparable) — but it means both readers independently agree that
  shape is real, distinct, and absent from Tomokiyo's legend.
- Both passes flag the legend's own built-in ambiguity — cursive homophone shapes shared across several
  letters (a/luy, c/d/h, s/t and others) — as the main source of M-grade uncertainty, not image quality. Pass
  B judged the image itself sharp enough that no sign needed an L grade; pass A used L once, for a single
  ambiguous ink fleck.

No reconciliation, key application, decode, or novelty wording, per brief.

## f.36 reading (24 Sept 2026)

Reconciler (Opus), working from disk only (`images/native_f71.jpg`, `images/f71_cipher.jpg`, `images/f69_cipher.jpg`
for glyph comparison); no network. Files: `ciphertext_f36.tsv` (25 signs, per-sign confidence, both passes' labels
at each aligned position, a note per sign), `reading_f36.txt`, `reading_tokens_f36.tsv`. `decode.py` now runs over
both leaves (list `LEAVES`); f.35's `reading.txt` and `reading_tokens.tsv` come out byte-identical (md5 checked
before and after), and `--check` exits 1 if any of the four output files is stale (tested by corrupting
`reading_f36.txt`).

**Correction to the section above.** f.36r has cipher on more than one line. Line 1 is all cipher. Lines 2-4
mix cipher signs with clear words: line 2 "[cipher] fust et en telle sorte vous serez", line 3 "asseuré de faire
[cipher] quand [cipher] de [cipher]", line 4 "[cipher] fust [cipher]". Clear-only text starts on line 5 ("toutes
les foys qu'il vous plairoyt, ou je feray tout le debvoyr et diligence qui sera possible..."). Seen at page
scale and at native resolution. Only line 1 was briefed and transcribed. Lines 2-4 need two passes and a
reconciliation (about 35 more signs by eye).

**Reconciliation.** I reread line 1 sign by sign at native resolution and coded each glyph with the f.35 codes.
Where a glyph was not a direct match to the legend, I compared it with the same glyph on f.35r. f.35r R2 "d ϖ ч
ℓ" = "fort" fixes ч as `eps` and ℓ as `pd`; R2's barred 8 is `x8`; R8 fixes the 6-shape as `b6` = p.
- Both passes have 25 signs. Pass A's extra sign (its 13, `unk4`, L) is a small ink dot between signs 12 and 13,
  not a sign.
- Where each pass matches the reconciled key value: pass A 9 of 25, pass B 13 of 25. Pass A read every plain `x`
  as u, which is systematic. Neither pass saw that signs 3 and 12 are the same slanted lozenge.
- **"dict" twice is not upheld.** Both passes took the two 6-shapes (11, 22) for Tomokiyo's word sign "dict".
  The glyph is the one f.35 codes `b6` = p, and context gives p both times ("peu", "pour"). Both are graded M,
  because Tomokiyo draws a similar 6 for "dict". That the two passes agreed on the label is evidence that the
  glyph looks like the legend's "dict", not that it means "dict".

**Reading** (keyed values, nulls dropped, `[code]` unkeyed):
`a u e c [I] u e s <le> [x8] p e u d e p e r t e p o u r`
→ with the two unkeyed signs taken as f.35's suggestions 4 and 5 (I = q, x8 = null): **"avecques le peu de perte
pour"** ("with the little loss for ..."). Those two values are grade I suggestions and are not applied in
key.tsv or the reading.

**Grades (25 cipher tokens):** H 15 (one null, `xinf`), C 0, S 0, M 8, I 0 applied (2 suggestions noted above),
U 2.
- M: sign 1 `T` and sign 6 `hk`, which Tomokiyo keys twice (the context value is the first one, a and u). Signs
  3 and 12 `dia`, a glyph-identity doubt. Sign 9 `le`, where the z-shape is only a near match to his yogh. Signs
  11 and 22 `b6`, the "dict" look-alike. Sign 20 `pd`, identified only through f.35r.
- U: sign 5 `I` and sign 10 `x8`.
No H or C reading comes from a contemporary decipherment, so this is a reading from Tomokiyo's published key,
with no control run.

**Join with f.35v.** f.35v line 29 ends "... e r p a r h e c a r DU [xk]" (as keyed: "...[recouvr]er par ... car
du [xk]"). f.36r line 1 begins "avecques le peu de perte pour". Leaf order, hand, cipher and the 27 Jan 1557
dateline show that this is the same despatch, so the physical join is H. The sense across the join is **not
read**: "car du [xk] | avecques le peu de perte pour" makes no phrase while `xk` (unkeyed, 4 uses) is open. Grade
the textual join M, and do not repair it. Line 1 then runs into line 2's cipher, not into clear French. The first
clear words after it are "fust et en telle sorte vous serez asseuré de faire ...", so "pour [line-2 cipher]
fust ..." is also unread.

**Not read here:** the cipher signs of lines 2-4, the value of `xk` and the f.35v/f.36r bridge. There was no
print or phrase search for "avecques le peu de perte", because that is the verifier's work.

Follow-up (not done): two blind passes over f.36r lines 2-4 (crop native_f71 at y ≈ 1950-2450), then a
reconciliation into ciphertext_f36.tsv as lines 36R2-36R4.


## Second reader f.35, 24 Sept 2026

Blind pass C (LANE V, second reader). The reader re-read f.35r-v sign by sign from `passC_crops/` (made by
`crop_passC.py` from native_f69/native_f70 on disk; the crops are not committed, so rerun the script to get
them). Only key.tsv's sign inventory and Tomokiyo's key drawing (for shapes) were consulted. ciphertext.txt,
the passes, reconciliation.md and the reading files were opened only after `passC_f35.tsv` was committed
(7f41afc). Pass C holds 642 cipher signs (509 H, 79 M, 54 L) and 150 clear-hand words in 37 lines plus the
V18 interlinear gloss.

**Agreement.** A per-line sequence alignment over cipher signs only, with a naming crosswalk (listed below),
matches 558 of 643, or **86.8%**. Before the crosswalk, 82.0%. Disagreement is concentrated in R2, R4, R6,
V1, V28 and V29 (each ≤ 0.80 line agreement). The other lines score ≥ 0.82, and most are ≥ 0.88.
The crosswalk renames labels only; both readings already separate these shapes. It covers: pass C plain small
2 = committed `r2`; pass C Q-shaped script 2 = committed `LRD`; the &-shape with a bar = `x8`; the crossed Z/R
with a small o = `xk`; the D-bowl sign = `Pbar`; T or 7 with a ring above = `ringT`/`ring7`.

**Proposed changes: 12** (`passC_proposed_changes_f35.tsv`; not applied):
- R4 pos 4: `al` → `LRD`. The image shows the large Q-shaped sign, identical to every sign committed as
  `LRD` on f.35v. This change is well supported.
- 7 × `eps` → `s9` (V4 pos 6 and 10, V6 pos 6, V23 pos 23, V28 pos 11, V29 pos 3 and 22). Zoomed to 2x,
  these are a single round bowl on a straight descender (a q-shape). They differ from the two-lobed epsilon
  with stem on the same lines. The committed text reads both shapes as `eps`. The change moves the value
  from r to s at those places, so the reconciler should test it against the reading.
- R4 pos 21: `B` → `S`. R6 pos 19: `pd` → `fd`. R6 pos 22: `xinf` → `x88`. V26 pos 18: `xinf` → `O`.
  All four are rated M.

Where pass C was wrong: at 2x, pass C's readings at R4 pos 19, V9 pos 3-6, V12 pos 22 and V2 pos 18 were
misreadings, and the committed signs stand there.

Open questions (no change proposed):
- Is the plain small "2" the r cell, as committed? Tomokiyo's drawing shows a plain 2 among the nulls and a
  Q-shaped sign in the r column. This is a key question, not a transcription one.
- The same tall long-s stroke is read `ls` in some places and `loop` (null) in others (5 rows).
- An arc drawn over the next sign is read as one `circ` or as two signs, loop + sign (R7, V1, V3).
- The clear word read "bien" (4×) looks like "huy" in the image.

### Adjudicated and applied, 24 Sept 2026

LANE V adjudicator (04:01 UTC). Each row was checked on the pass C crops regenerated from native_f69/f70 on disk
(`crop_passC.py`, 2-3x zooms), against other instances of both labels on the same leaf. 11 accepted, 1 rejected.
Applied to ciphertext.txt (sign and conf columns); `decode.py` regenerated reading.txt and reading_tokens.tsv;
`decode.py --check` exits 0. f.35 grades: H 508 / M 61 / U 69 -> **H 509 / M 59 / U 70** (638 cipher tokens, 61 nulls).

| row | change | decision | image evidence | effect on reading |
|---|---|---|---|---|
| R4 pos 4 | al -> LRD (conf H) | accept | Large Q-shape with tail to right, the same form as LRD at V26 pos 9, V28 pos 15 and V29 pos 15; the alpha at R4 pos 17 is quite different | Worse under the committed key: "la c o[ring7]ne" becomes "la <le Roy de Dannemarch> o[ring7]ne". See the key note below |
| V4 pos 6 | eps -> s9 (H) | accept | Single round bowl on a straight descender (q-shape). The two-lobed epsilon-with-stem at V4 pos 17 is distinct | "tour" -> "tous" |
| V4 pos 10 | eps -> s9 (H) | accept | Same q-shape as pos 6 | "le ra..." -> "les a..."; better or the same |
| V6 pos 6 | eps -> s9 (H) | accept | q-shape; the epsilon-with-stem at V6 pos 14 is distinct | "quil renploy[ring7]ero[pdx]t" -> "quil s enploy..." (qu'il s'employeroit); better |
| V23 pos 23 | eps -> s9 (H) | accept | q-shape; the epsilon at V23 pos 10 ("leur") is two-lobed | "en ruis" -> "en suis"; better |
| V28 pos 11 | eps -> s9 (H) | accept | q-shape; the epsilon at V28 pos 4 ("car") is two-lobed | "a u q r b o u" -> "a u q s b o u", in the Augsbourg spelling at V26's end; better |
| V29 pos 3 | eps -> s9 (H) | accept | q-shape after T and = | "a i r" -> "a i s" after "pourra" (V28): "pourra ais..." fits; better |
| V29 pos 22 | eps -> s9 (H) | accept | q-shape; the epsilon at V29 pos 17 is two-lobed | "p a r h e" -> "p a s h e"; same (neither is clear) |
| R4 pos 21 | B -> S (M) | accept | A heavy, rounded S with a closed lower bowl, matching the committed S at V8 pos 18; no ascender loop, unlike B at V6 pos 9 and V8 pos 11 | "c h e p" -> "c h e [S]"; S is unkeyed (U); the same, since neither reads |
| R6 pos 19 | pd -> fd (H) | accept | An f with a heavy crossbar and a descender well below the line, as fd at V23 pos 5 and V28 pos 5; not the pound-t sitting on the line | "faultra" -> "fauldra" (a period spelling of faudra); better |
| V26 pos 18 | xinf -> O (H) | accept | A heavy closed oval with an inner stroke, the same as O at R5 | None (both are nulls) |
| R6 pos 22 | xinf -> x88 | **reject** | Two open loops crossed by one horizontal bar, identical to xinf at V29 pos 18. It lacks the tall vertical stems of x88 at R3 pos 1 | None (both are nulls) |

**The eps -> s9 group.** s9 is already in key.tsv as s ("reversed-9 with long tail", Tomokiyo s column,
row 2), and ciphertext.txt already used it at R7 pos 9 and R8 pos 6/10. At R8 pos 10 the same q-shape falls in
"present", so the s value there is set by the text. The value comes from key.tsv, and none was invented.
Six of the seven changes read better or the same, and none reads worse. The 37 remaining `eps` rows were not
re-examined one by one here.

**Open questions.** None of these is settled by the image. The key questions stay open.
- Plain 2 vs Q-shaped sign: this is still a key question. There is new evidence, but no decision has been
  made. With the q-shape now s at V28 pos 11, V28 reads "T mu q4 s9 bl pib xb [Q] g8" = "a u ? s b o u ? g",
  which is the spelling of "Augsbourg" at the end of V26 if the Q-shape is r and q4 is g. The same assumption
  gives "la ro[ring7]ne" at R4. This favours Tomokiyo's r-column Q-shape, as pass C noted. key.tsv is untouched.
- ls vs loop, and circ as one sign or two: the same stroke carries both labels, so the image cannot decide.
  These stay open.
- "bien" vs "huy": a clear-hand word, not a cipher sign. The committed reading is unchanged.
- Suggestion (not done): V28 pos 10 (committed q4?, pass C g7) looks like a 7 in the crop. Re-examine it
  together with the Q-shape key question.

Suggestion (not done): a Sonnet worker applies the accepted rows and reruns `decode.py --check`. (done: see "Adjudicated and applied" above)
- Suggestion (second audit, 24 Sept 2026): for N4 on f.35, read Delavaud 1911 (Bull. Soc. normande de géogr. XXXIII, Gallica cb328704148, pp. 49-55) and Daussy 2001 (L'épistolaire au XVIe siècle, pp. 211-226).
## f.36r lines 2-4, passes (24 Sept 2026)

Follow-up named at the end of "f.36 reading" above: lines 2-4 of f.36r (labels R2, R3, R4) mix cipher signs with
clear French words. Six line crops cut with `tools/iiif_lines.py` (ink-profile line detection) from
`images/native_f71.jpg` already on disk, no network fetch: each line is 3400 px wide at native resolution, over
the 2500 px reading limit, so each is two overlapping segments (`_L01_s1.jpg`/`_L01_s2.jpg`, ~1400 px shared in
the middle) rather than one downscaled crop as line 1 was — `images/manifest.json` records the boxes and the
`f36_lines2-4_pass_24_sept_2026` note. Two independent Sonnet subagents (`passA_f36b.tsv`, `passB_f36b.tsv`),
neither shown the other's file, `ciphertext_f36.tsv`, any reading file, `key.tsv`, or this file, transcribed all
three lines against Tomokiyo's sign legend (`danzay_1557.png`), same format as the earlier passes plus one new
column: `line position sign confidence note`, where a plaintext French word (as opposed to a cipher sign) is
written as the word itself with `clear` in the note column. No reconciliation, key application, or decode was
attempted, per brief.

**Sign counts.**

| line | pass A tokens (sign / clear) | pass B tokens (sign / clear) |
| --- | --- | --- |
| R2 | 19 (14 / 5) | 15 (10 / 5) |
| R3 | 18 (11 / 7) | 16 (12 / 4) |
| R4 | 24 (23 / 1) | 24 (23 / 1) |
| total | 61 (48 / 13) | 55 (45 / 10) |

Confidence: pass A H 19 / M 35 / L 7; pass B H 8 / M 29 / L 18. Pass A is more confident line for line, and pass
B reads more shapes as unmatched (`unkN`, see below) or as low-confidence plaintext.

**Agreement.**

- **Position-exact match is low, as with the f.36 line-1 pass** (line 1: 8/25, ~third): R2 5/15, R3 4/16, R4
  3/24 matching positions out of the shorter pass's length — a segmentation-count gap (R2 19 vs 15, R3 18 vs 16)
  throws off position alignment quickly, the same effect noted for f.35's ~2x segmentation gap and f.36 line 1's
  one-position drift, not a sign-for-sign disagreement.
- **R4's one clear word lands at the same position in both passes.** Both A and B read line 4 as 23 cipher-sign
  tokens with exactly one plaintext word, "fust", and both place it at position 20 out of 24 — the strongest
  cross-pass agreement in this pass, on both the count and the position.
- **Both passes independently find "fust" as a clear word early in R2** (A position 9, B position 9 — also
  position-exact) and **"fixuy" as the last clear word of R2** (A position 19, B position 15 — last token in
  both passes' own line, different absolute position because of the segmentation gap). Both also read "de" as a
  clear word partway through R3, though at different positions (A twice, at 3 and 17; B once, at 2).
- **Pass B recognises word-signs that pass A does not use at all in these three lines.** B labels four tokens
  `word:luy` (R2 pos 5, R3 pos 12, R4 pos 12 and 18), one `word:dict` (R4 pos 11), and one
  `word:leRoyDeDannemarch` (R4 pos 9); A has no `word:` label anywhere in R2-R4, resolving the same stretches to
  single a-z letters or `unk` shapes instead. This is a real reading disagreement (not a naming-scheme artifact
  like the two passes' `unk` labels below) and is left open — no attempt made here to judge which pass is right.
- **The two passes' `unk` labels are not comparable, as before, and by a different convention.** Pass A restarts
  its numbering each line (three different shapes are each called `unk1` in R2/R3/R4); pass B reuses a number
  for a recurring shape across all three lines (`unk2` at R2 pos 6, R3 pos 8, R4 pos 8; `unk7` three times in
  R4; `unk8` three times in R4). Neither convention was specified in the brief beyond "reused if the same shape
  recurs" — A did not do this, B did. A sign-for-sign `unk`-label match between the two passes is not reported,
  same reasoning as the earlier passes.
- **Nulls.** A reads 2 nulls, both in R4 (positions 4 and 24 — the last token of the line). B reads 5 nulls (one
  in R3 at position 4, four in R4 at positions 3, 4, 21, 24) — B's R4 position 24 null matches A's.

No reconciliation, sign inventory, key application, or decode attempt follows from this, and no novelty wording
applies. Cost note: two Sonnet subagents, well under the $5 cap for this worker.

- Toward-N4 gap worker, 24 Sept 2026: the Daussy 2001 chapter gap (above) is closed as far as this repository's tools can take it, not closed positively or negatively. The only IA copy, `lpistolaireauxvi0000unse`, is in Internet Archive's print-disabled-only access tier (`is_lendable: false`, `max_borrowable_copies: 0` on the no-login availability check) — a harder wall than the obfuscated-image limit `tools/ia_borrow.py` already documents for ordinary lending items, since `browse_book` cannot even open a loan on this account. be-api full-text search found all five of the reading's distinctive terms present somewhere in the 262-leaf book (Danzay, chancelier, cardinal de Lorraine, 1557) except Danois/Augsbourg/marchans de Lion (0 hits), but every present-term snippet reads as unrelated to this letter (a different chancellor, bibliographic citations of editions, unrelated 1557 dates, an index/name-list entry with no date). Full log and reasoning in AUDIT.md "Toward N4: Daussy 2001, 24 Sept 2026". This needs a library copy or ILL, not another automated pass; a REQUEST.md/ASKS.md row for the person is the next step, not a further worker.

## f.36r lines 2-4 reading (24 Sept 2026)

Opus reconciler (LANE G), working from disk only: `images/native_f71.jpg` (y 1880-2370, re-cut in 2x zooms in the
session scratchpad), the line crops `f71_R{2,3,4}_L01_s{1,2}.jpg`, `passA_f36b.tsv`, `passB_f36b.tsv`, and
Tomokiyo's table (`sources/cryptiana/web/danzay_1557.png`) for glyph identity. No network. Lines 36R2-36R4 are now
appended to `ciphertext_f36.tsv` (line 1 unchanged). Each row carries both passes' labels at the aligned position
and a glyph note. `decode.py` regenerates `reading_f36.txt` and `reading_tokens_f36.tsv`. f.35's `reading.txt` and
`reading_tokens.tsv` stay byte-identical (md5 checked before and after), and so does the 36R1 line of
`reading_f36.txt`. `decode.py --check` exits 0 when current and 1 when stale (tested by appending to
reading_f36.txt). `tools/tests/test_decode_key.py` passes.

**Alignment.** Neither pass is sign-for-sign right. Most of the gap is segmentation. Pass A read the clear words
"Et" and "telle" (R2) as cipher signs (r x, m l l unk1), and it split the ae ligature at R4 pos 7 into b + n.
Pass B split `iii` and `pp` in R4 into two signs each, and it has no token for the clear "en" (R2) or for the last
"de" and flourish of R3. After this reconciliation: R2 has 8 cipher signs and 7 clear words, R3 has 12 cipher
signs and 5 clear words, and R4 has 22 cipher signs and 1 clear word. That makes 42 cipher tokens and 13 clear
words. **Only one of pass B's four word-sign labels is kept as a word-sign:**
- `word:luy` (x4). These are all the T-shape, which Tomokiyo keys twice (a | luy). The context gives a at R2 pos
  5 ("change") and at R4 pos 11 and 17 ("par deça"). R3 pos 11 and 14 are unread. Graded M (decode.py grades
  every T as M).
- `word:dict` (R4 pos 10). This is the same 6-shape (`b6` = p) that the f.36 line-1 reconciliation settled. The
  context here is "par".
- `word:leRoyDeDannemarch` (R4 pos 8). The script L matches Tomokiyo's drawing, so it is coded `LRD`, grade M.
  It is kept, not repaired, although it breaks the run "...m e n [LRD] par deça". The closest alternative is his
  circled t in row 2 (a long s/f with a foot), which would give "...ment par deça". That is a suggestion only
  (grade I), not applied.

**Key cell added.** Tomokiyo's image has an h in column h, row 1: a 9/g-shape whose tail curves back to the left.
The first transcription of his table into `key.tsv` left this cell out. It is added as `h9` = h, with the source
cited. It is used once, at R2 pos 4. No f.35 token uses it, so f.35 is unchanged. Other cells of his image that
key.tsv also omits (d row 1 '9', d row 3 '4', i row 3, y row 2, t row 2 circled, z row 2, and the nulls '2', 'cf',
'ny', 'rj', 'Z0') were **not** added. That is a key-transcription check for someone else. It bears on the open
plain-2 question (see below) and on `ls`, which key.tsv cites as s row 3, where the image seems to show the
circled t cell.
New code: `ww` (R4 pos 2), a sharp double caret like an inverted w. Nothing in the table matches it, so it is
unkeyed.

**Grades, lines 2-4 (42 cipher tokens; 13 clear words not graded):** H 22 (9 of them nulls), C 0, S 0, M 18,
I 0 applied, U 2 (`ww`, `ringT`). All of f.36 (lines 1-4, 67 cipher tokens): H 37 (10 nulls), M 26, U 4.
[Correction, verifier, 24 Sept 2026 (AUDIT.md "f.36r"): lines 2-4 have 9 nulls, 5 of them at H and 4 at M, so H 22
(5 nulls). All of f.36: H 37 (6 nulls), M 26 (4 nulls), U 4.]
Every H or M value comes from Tomokiyo's published key. No contemporary decipherment of this leaf is known, and
no control was run. This is a reading from his key, not a cryptanalytic result of ours.

**Reading** (`reading_f36.txt`; CAPS = clear hand, nulls dropped, [code] = unkeyed):
```
36R1  a u e c [I] u e s <le> [x8] p e u d e p e r t e p o u r
36R2  <le> c h a n g e FUST ET EN TELLE SORTE VOUS SEREZ
36R3  ASSEURÉ DE FAIRE e u r n g QUAND a m e a r DE
36R4  q [ww] y m e n <le Roy de Dannemarch> p a r d e c a FUST r [ringT]
36R5- (clear) toutes les foys qu'il vous plairoyt, ou je feray tout le debvoyr et diligence qui sera possible ...
```
- **Read:** R2 cipher = **"le change"** (le + [null] + c h a n g e). Everything comes from key values. M on mc,
  h9, T and g8, where the dot at the 8's waist leaves x8 possible. R4 pos 10-17 = **"par deça"** (p a r d
  [null] e c a). M on the two T's and one crossed A.
- **Clear words:** "fust et en telle sorte vous serez / asseuré de faire ... quand ... de / ... fust". The
  word "serez" is by letter-form and sense. The literal forms are long-s, c-e, x-r, u, tailed z. The final
  "de" of R3 is clear by letter-form, but cipher del + x is not ruled out.
- **Not read:** R3 "e u r n g [xN]" after "faire". With the plain 2 taken as a null rather than r2, it is
  "e u n g", which is still not a word. R3 "a m e a r" after "quand". R4 "q [ww] y m e n [LRD]" before "par
  deça", and "r [ringT]" after the last "fust". `ringT` stays unkeyed.
- **Plain 2 (R3 pos 6, R4 pos 20).** Both are coded `r2`, following the committed f.35 convention. At both
  places r gives nothing and a null reads no worse. That is two more data points for the open key question
  (Tomokiyo draws a plain 2 among the nulls). No change was made.

**How lines 1-4 run with the clear French.** Joined, the text runs: "[f.35v: ...car du [xk]] avecques le peu de
perte pour le change fust. Et en telle sorte vous serez asseuré de faire [e u r n g] quand [a m e a r] de
[q ? y m e n ...] par deça fust [r ?] toutes les foys qu'il vous plairoyt, ou je feray tout le debvoyr et
diligence qui sera possible ...". The joins read as grammar where the key gives words: "pour le change" across
lines 1-2, and "par deça fust ... toutes les foys qu'il vous plairoyt" across lines 4-5. The sense fits the
f.35v run about sending by way of the Augsburg and Lyon merchants: "with as little loss as possible on the
exchange". That is an inference (grade I), not a reading. [Verifier, 24 Sept 2026: Tomokiyo's table also lists candidate null words ("bien du est il? ou / par quand?"), so the clear "quand", "de" and "fust" among cipher runs may be nulls, not text.] Three stretches (R3 twice, R4 opening) and the f.35v
`xk` bridge stay unread, and they are not repaired. No phrase or print search was run (verifier's work), and
no novelty is claimed.

Suggestions (not done): check key.tsv cell by cell against Tomokiyo's image (see above). Test `LRD` against t
row 2 in "...ment par deça". Put the two plain-2 rows here into the f.35 plain-2 question.

- Suggestion (verifier, 24 Sept 2026): test Tomokiyo's null-word list ("bien du est il? ou / par quand?") against the clear words set inside cipher runs on f.35 and f.36r.

## Second reader f.36r, 24 Sept 2026

Blind pass C (LANE V, second reader), lines 36R1-36R4 of f.36r. The reader cut crops at native size and at 2x
from `images/native_f71.jpg` on disk (scratch only, not committed; no network). Before the pass was committed
(f3c7d64) the reader consulted only key.tsv's sign and glyph columns. ciphertext_f36.tsv, the passes and the
reading files were opened only after that commit. Pass C holds 80 tokens: 67 cipher signs (37 H, 25 M, 5 L)
and 13 clear-hand words. The two sides have the same token count on every line (25/15/17/23), so positions
align 1:1.

**Agreement.** With the naming crosswalk (pass C plain 2 `z2` = committed `r2`; the circle-over-cross drawn as
`ven` = `ringT`; pass C `ry` = `loop`; `Om` = `ww`), the two readings match on 64 of 80 tokens, or **80.0%**.
Over cipher signs alone they match on 53 of 67, or **79.1%**. Five of those 14 cipher disagreements come from a
single consistent naming split: pass C calls the slanted lozenge `bd` and the committed text calls it `dia`.
Each side uses its name for all five occurrences. With that split set aside, cipher agreement is 58/67 =
**86.6%**, the same level as f.35 (86.8%). The remaining disagreement sits in 36R1 (pos 6, 9, 10, 20, 23) and
the 36R4 opening (pos 3, 8, 18). Lines 36R2 and 36R3 agree on every cipher sign apart from `dia` and 36R2 pos 2.

**Proposed changes: 1** (`passC_proposed_changes_f36.tsv`; not applied):
- 36R1 pos 9: `le` → `r2`. At 2x, side by side, it is the plain flat-footed 2. It matches 36R3 pos 6 and
  36R4 pos 20, which the committed text codes `r2`. The yogh at 36R2 pos 1 has a long descending tail, which
  this sign lacks. The committed text codes the same glyph two ways, so the reconciler should test the value
  change against the reading.

The other 15 disagreements are not proposed. Pass C was rated M or L on them, the two labels describe the same
glyph, or the token is a clear-hand word. For the adjudicator: 36R4 pos 8 (`LRD`) and 36R1 pos 20 (`pd`) are
the same looped l with a foot. They differ only by a small detached tick at the left of the stem in 36R4 pos 8.
If that tick is a crossbar stub, pos 8 is nearer `pd` than pos 20 is. The image does not settle this at 2x.

**The two places the reconciler left unread, read as signs, not as values.**
- 36R3 pos 16-17. Pos 16 is two letters, round d then e. Their letter forms are the same as the clear-hand
  "de" earlier in the same line (asseuré de faire), so pass C also reads them as clear. Pos 17 is one glyph:
  a small r whose stroke rises into a loop and descends into a yogh-like curl ending in a dot. The ink is
  continuous, so the image gives one sign here, not two (not r + yogh). Its shape agrees with committed `loop`.
- 36R4 opening, pos 1-5. The image lets each one be read as a sign:
  - pos 1: an open 4 / zigzag (`q4`).
  - pos 2: a single double-caret, one stroke, with no drawn key match (`ww`).
  - pos 3: a small loop on a stem that descends to the lower left. Pass C found no key match; the committed
    `ven` (y with looped descender) fits the image.
  - pos 4: three separate strokes leaning left (`iii`).
  - pos 5: a reversed-t and a plus. They sit closer together than neighbouring signs, which supports one `pp`,
    but two signs are not excluded.

  None of these five is illegible. The open questions are key membership (pos 2, pos 3), not reading.

### Adjudicated and applied, 24 Sept 2026

LANE V adjudicator (Opus), working from `images/native_f71.jpg` and `images/f69_cipher.jpg` on disk only (crops at 2x
and 3x in scratch, not committed; no network). Both calls were settled by comparing the glyphs with other
instances on f.35-36. Applied to `ciphertext_f36.tsv`; `reading_f36.txt` and `reading_tokens_f36.tsv` regenerated
with `decode.py`; `decode.py --check` exits 0; f.35 `reading.txt` and `reading_tokens.tsv` byte-identical.

| row | change | decision | image evidence | reading without -> with |
|---|---|---|---|---|
| 36R1 pos 9 | le -> r2 (conf stays M) | accept | Plain small 2 with a flat foot and no descender. It is the same form as 36R4 pos 20 (r2) at the same scale. The yogh at 36R2 pos 1 is a 3 with a long tail curling down and back left, which this sign lacks | "a u e c [I] u e s **le** [x8] peu de perte pour" -> "... u e s **r** [x8] peu de perte pour". Worse under the committed key: "avecques le peu de perte" becomes "avecques r [x8] peu de perte". If the plain 2 is the null that Tomokiyo also draws (the open plain-2 question above), the run reads "avecques [x8] peu de perte". That is a suggestion only; no key value changed |
| 36R4 pos 8 | LRD -> pd (conf stays M) | accept | A stem with a hook at the top curling right, a small tick at mid-stem on the left, and a flat foot. This is the form of f.35r R2 pos 11 and 22 (pd, "fort"). The f.35 LRD is a different sign: the large Q/Z-shape with a long tail to the right (f.35r R2 pos 4, and every LRD on f.35v). 36R1 pos 20 (pd) has the same tick and foot, with a more closed top loop. Pass C's "detached tick" is the mid-stem stub that every pd shows | "q [ww] y m e n **\<le Roy de Dannemarch\>** par deça" -> "q [ww] y m e n **t** par deça", i.e. "...ment par deça". Better: it removes the break in the run that the lines 2-4 reading noted |
| 36R1 pos 20 | pd kept | reject change (none proposed) | Looped l with mid-stem tick and foot, as the f.35r R2 pd | "perte" unchanged |

Grade counts on f.36r are unchanged: both rows were M before and are M now, and neither is a null. All of f.36r
remains H 37 (10 nulls) / M 26 / U 4 (line 1 H 15 M 8 U 2; lines 2-4 H 22 M 18 U 2), so the figures in this file,
AUDIT.md and status.json stand. The earlier suggestion "test LRD against t row 2 in ...ment par deça" is settled
by the sign identity, without using Tomokiyo's t row 2 cell. `<le>` now occurs on f.36r only at 36R2 pos 1.
- Suggestion (V3b, 24 Sept 2026, from second opinion SO-DANZAY-F35): reading.txt shows LRD as `<le Roy de Dannemarch>` where it reads r/R (V5, V11-12, V26, V28, item 3 above); a solver should decide whether to key LRD as letter r in context and show both values, as for T and hk.
