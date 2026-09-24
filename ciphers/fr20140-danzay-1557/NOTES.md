# BnF fr.20140 — Charles de Danzay to Henri II / Cardinal of Lorraine, January 1557

Status: found-solved (3 of 4 items); partial (1 of 4, f.35: Tomokiyo's key read, 24 Sept 2026)
Novelty (f.35): N3 per AUDIT.md (verifier, 24 Sept 2026); use only the safe sentence there.

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
- H 508: the sign was read clearly and Tomokiyo keys it to one value. 61 of these are his nulls.
- M 61: 21 keyed signs that are doubtful in the image, plus the 40 glyphs he keys twice (T = a/luy, hook = u/a). A 22nd doubtful sign, `D`, is unkeyed and counted under U.
- U 69: signs in none of his cells.

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
Janvier 1557" — the same 27 Jan 1557 despatch — signed "Dantzay" at the foot), then the native-resolution
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

