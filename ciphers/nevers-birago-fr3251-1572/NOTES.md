open

INTAKE-3251, 27 Sept 2026: solver-ready intake only (Layout, no reading, no decoding, no class). Sibling folder
to `ciphers/ceppo-nevers-fr3251-1570s` -- same shelfmark and correspondents, one cipher generation later. Built
from KEY-ADJACENT.tsv row 2 (SCOUT-OWN-6, 27 Sept 2026) and `sources/cryptiana/web/nevers.htm` (local mirror,
read in full by this worker, not re-fetched, section id=BnFfr3251). Tomokiyo, verbatim:

> "In 1572, the year of Birago's death, they used a new cipher, which can be reconstructed from the
> decipherment attached to no.87 is called the Nevers-Birago Cipher (1572) herein."

# Nevers-Birago Cipher (1572) letters (BnF fr.3251), Lodovico Birago to Duke of Nevers

All from Saluzzo. Digits, per Tomokiyo (KEY-ADJACENT.tsv row 2, `token_shape` column).

## Undeciphered (this folder's targets)

| folio | no. | date |
|---|---|---|
| f.138 | no.71 | 7 February 1572 |
| f.144 | no.73 | 27 March 1572 |
| f.152 | no.77 | 9 June 1572 |
| f.160 | no.82 | 27 June 1572 |
| f.168 | no.85 | 29 July 1572 |
| f.174 | no.86 | 27 August 1572 |
| f.184 | no.90 | 2 October 1572 |

(Only f.138/f.144/f.152/f.160 are named in KEY-ADJACENT.tsv row 2's own summary and the SCOUT-OWN-6 ROOM line;
this job's brief named all seven -- nevers.htm lists the full 1572 run as ff.138, 144, 152, 160, 168, 174, 178,
184, and only f.178 carries the decipherment the key was built from.)

**Date note (images/manifest.json):** the f.138r image fetched this session shows a marginal endorsement partly
reading "...alli 7 di Gennaro 1572" (7 January), not the "7 February 1572" nevers.htm gives for no.71 -- flagged,
not resolved, for the SOLVE parent to check against the image before transcribing.

## Witness (known-plaintext sibling -- carries a period decipherment, the calibration set per the fr7129 lesson)

| folio | no. | date |
|---|---|---|
| f.178 | no.87 | 8 September 1572 (the decipherment attached to this letter is what the whole 1572 key was reconstructed from) |

## The key

Tomokiyo's printed table is the hand-drawn image `NeversBirago.png`, embedded in nevers.htm directly after the
"Nevers-Birago Cipher (1572)" sentence quoted above (i.e. before the f.138 list, not after). See "Key blocker"
below; it was not transcribed this session.

## Check-solved header (not a formal check-solved pass -- see "What remains" below)

Identical evidence base to the sibling folder's own check-solved header (`ciphers/ceppo-nevers-fr3251-1570s/NOTES.md`
"Check-solved header"), same correspondence and shelfmark, not repeated verbatim here to avoid drift between the
two copies -- read that section. In short: Tomokiyo names all seven target folios and marks none of them "(with
decipherment)"; `ciphers/birago-nevers-1571/NOTES.md`'s six-source sweep on this exact sender-recipient pair found
no printed edition, no DECODE record, and Bourdeau's own `profile.json` records no prior solution; Bourdeau's
`SOLVED_CATALOGUE.md` (via `sources/cryptiana/READABLE.tsv`) independently lists "138-174, 184" among the folios
he has read in part but not published a reading for, corroborating Tomokiyo. (Bourdeau's own range does not
explicitly name f.152 or f.160 as intermediate stops, but "138-174" as printed is inclusive of them.)

What remains before any class (rule 10) or any deep-work brief:
- A formal `.claude/briefs/check-solved.md` pass proper -- `tools/intake_gate_check.py nevers-birago-fr3251-1572`
  should be run before any deep-work brief.
- The date discrepancy on f.138 (above) checked against the image.
- Once a reading exists: `tools/print_check.py` on the decoded phrases (rule 10).

## Key blocker: resolved (KEY-IMG-3251, 27 Sept 2026)

`keys/key_nevers_birago_1572.tsv` is transcribed and on disk: 50 hand-drawn/printed symbol cells (43 in the
letter grid across 18 of 22 letter columns plus "et?" -- q, x, y carry none -- and 7 in the word-code grid:
che, per, qual, quello as hand-drawn signs, carmagnola/turino/bugonotti as plain two-digit numbers 85/86/89),
from `NeversBirago.png` (fetched from `cryptiana.web.fc2.com/code/NeversBirago.png`, manifest in
`sources/cryptiana/web/manifest_2026-09-27-keyimg.tsv`). Two independent blind Sonnet subagent reads,
mechanically merged: 49 of 53 rows agreed cell-for-cell (grade AB); 4 rows graded M -- two (r row2, s row2)
where the position agreed but the exact shape did not fully resolve, and a real column-assignment disagreement
on a "dumbbell" mark and a three-humped "m" mark near the end of the alphabet: one blind pass placed the
dumbbell under y and left z's row1 silent, the other placed it under z and called y blank. Settled by this
worker pixel-cropping the header's own white-text glyph positions to get exact column-cell boundaries (not
just centers) and overlaying them on a zoomed crop of the x/y/z/et? region: both marks sit inside z's column
cell, y is genuinely blank. `tools/key_design.py` reads the key as `usable=yes`, design_family `nomenclator`
(20 distinct letters plus a small word-code table) -- consistent with Tomokiyo's own description. KEY-OFFICES.tsv
and KEY-DESIGN.tsv both carry rows for this key; `tools/key_design.py --check` passes.

**Next step:** transcribe the cipher passages of the seven target folios (two blind passes) and apply
`keys/key_nevers_birago_1572.tsv` with a 20-shuffled-key control (rule 3); reading to a verifier. The f.138
date discrepancy (above) is still unresolved and should be checked against the image before or during that
transcription pass.

## NEV-C1 witness calibration (27 Sept 2026)

Per `.claude/briefs/runs/2026-09-27-lane-nev-owner-c1-calibrate-f178.md`. **FAIL at step (a): no clerk
plaintext decipherment located and read.** Status stays `open`. No target work done; no class, no novelty
wording, no grades.

**What the page shows.** The brief's predicted canvas for f.178 (179, on a +1 folio-to-canvas offset carried
over from the sibling folder's manifest) is wrong for this span of the volume: canvas 179 is ink-stamped
folio **176**, not 178 (confirmed by eye, zoomed crop). Stepping forward one canvas at a time and reading each
ink foliation directly (not predicting): canvas 180 = f.177 (ends "...da Saluzzo li 27. de Agosto 1572",
matching no.86's 27 Aug 1572 date from nevers.htm), canvas 181 = **f.178** (ink foliation '178' confirmed),
canvas 182's right page = f.179 (ink foliation '179' confirmed). So the offset here is folio+3, not folio+1;
recorded as `canvas_rule_correction_NEV-C1` in `images/manifest.json`, since the +1 rule that held at the
four points checked when this folder was built (f.11r/f.19r/f.119r/f.189r, all far earlier in the volume) has
drifted by the time the volume reaches f.176-179 -- do not assume either offset for the other five target
folios without eye-checking each one, the same lesson CLAUDE.md already records for fr.20140 at f.50v.

Canvas 181's left page is f.177v, the letter's own address leaf ("Al Ill.mo et Ecc.mo Sig.re et Sig.r mio
oss.mo il Sig.r Duca di Nevers Par di Francia..."), confirming no.87 opens on the facing recto, f.178r. f.178r
opens "Subito che s'hebbe la nuova della ferita, et poi della morte di Monsig. l'Armuraglio..." (the Amiraglio,
i.e. Coligny, killed in the August 1572 St. Bartholomew's Day massacre -- content-consistent with the 8 Sept
1572 date nevers.htm gives for no.87). Ordinary Italian handwriting continues for most of the page; the last
two lines are cipher signs. Those two lines have **no interlinear plaintext** above or below them -- checked
directly and by an independent subagent read of the same crop (`f178r_cipher.png`, scratch), which also
transcribed the preceding four plaintext lines for confirmation (not used for anything beyond confirming the
image is legible and cipher-free of any gloss). The cipher continues onto the whole of f.178v (canvas 182's
left page): a full page of cipher signs, roughly 24-26 lines, again no interlinear gloss anywhere on the page
(checked directly at 1000px and by the same subagent on a zoomed crop, `f178v_top_zoom.png`, scratch). Total
cipher passage: roughly 26-28 lines, well over the brief's "take the first 12 lines" cap for a passage over
about 14 lines -- moot here since no plaintext to align it to was found. f.179r (canvas 182's right page)
resumes ordinary prose and mentions "Bellagarda" again, reading as a plausible direct continuation of no.87
rather than a clearly new letter (no new heading/address observed) -- not conclusively settled, not needed
for this job.

**The attached decipherment.** Canvas 183 shows, on its left page, a small loose/tipped-in sheet of paper
(roughly half the page's width, photographed at an angle, lying over what would be f.179v), with f.179r's
ink foliation '179' visible again on the facing right page of this same canvas. Position (immediately after
the cipher passage) and a faint archival annotation in the sheet's bottom-left corner -- a subagent read it
as possibly containing '87' and a date-like group resembling '1572', confidence L-M, not a confirmed
transcription -- make it a plausible candidate for Tomokiyo's "decipherment attached to no.87". **Its visible
face is illegible**: out-of-focus, low-contrast text consistent with ink bleeding through from the far side of
the thin sheet, not a front-facing legible hand. Checked at three zoom/contrast levels (1000px overview,
2200px native crop, and an autocontrast-enhanced crop, `images/f179v_insert_crop_enhanced.png`) by this
worker directly, and independently by a subagent given the enhanced crop with no other context, which reached
the same conclusion ("bleed-through, not front-facing legible writing... too soft-focus and low-contrast to
resolve individual letterforms"). Neither pass invented a reading. This is not confirmed to actually be the
decipherment Tomokiyo meant -- it could be an unrelated filed note -- and was not confirmed to be illegible
for a structural reason (e.g. it may simply be photographed from the wrong side); a future pass with a
different exposure/angle, or the archive's own finding aid, might resolve it.

**Verdict.** Plaintext read (a) FAILS: no legible clerk decipherment was found, interlinear or attached, so
subagent (b) (sign read) and (c) (blind check) were not run -- there is nothing to align a sign transcription
against, and running them without a comparison would not calibrate anything. `witness/key_rows_f178.tsv` is
written with 0 rows for the same reason (brief step 8, "either way"). The key itself (`key_nevers_birago_1572.tsv`)
is neither confirmed nor contradicted by this job; `tools/decode_witness.py` (this job's shared deliverable,
step 7) is written and offline-tested but has not yet been run against real witness data for this target.

**Named next step:** a worker with the Gallica request budget to (i) re-fetch canvas 183 at full native
resolution with a different crop/orientation in case the sheet's legible face is elsewhere in frame, and/or
(ii) check the BnF catalogue record or finding aid for this ark for any note about a loose insert near f.179,
before spending further budget re-transcribing f.178's cipher passage blind. Ceppo-Nevers f.27 (this key's
own next witness pass, per the lane orchestrator's job order) is unaffected by this finding and should proceed
on its own merits; `tools/decode_witness.py` is ready for it.

**Requests:** gallica.bnf.fr 9 in this job (canvas 179 at 1000px and 1800px; canvas 181 at 1000px [1
connection-reset, retried once after a pause] and 2000px; canvas 180 at 1000px; canvas 182 at 1000px; canvas
183 at 1000px and 2200px) -- one over the brief's stated 8-request allowance, spent entirely on locating the
witness and searching for its decipherment (the brief's own predicted canvas was two folios off, see above)
rather than on any target folio; logged here rather than hidden. Subagents: 2 (both read-only image review,
no transcription committed as a reading). No hosts but gallica.bnf.fr; no credentials; no AskUserQuestion.

### LANE NEV orchestrator follow-up on NEV-C1 (27 Sept 2026)

Three gallica.bnf.fr requests, one at a time, 2 s apart: canvas 183 and canvas 184 at 1000 px, and canvas 183
region pct:19,12,38,56 at native resolution (3092x3276). They were looked at directly, contrast-stretched and
mirrored; scratch only, nothing committed. The tipped-in sheet's writing is on its far side. The photographed
face shows only bleed-through, and even mirrored no word of it can be read with confidence. So this image cannot
calibrate the key. Canvas 184 settles the extent of no.87: the letter ends on f.179v, "Da Saluzzo li 8 di settembre
1572", signed Lodovico Birago. f.180r is blank apart from bleed-through. The cipher of no.87 runs over the last two
lines of f.178r, all of f.178v and the first three lines of f.179r. The Nevers-Birago group has no legible witness on
Gallica. Its calibration waits on (i) the sheet's written face (an archive photograph: a REQUEST.md item, not
queued yet), or (ii) a control-backed decode of the no.87 cipher passage itself: the key of record against 20
shuffled keys, with the language judge, run as a target-style test and labelled as such. LANE NEV runs the
Ceppo-Nevers calibration (NEV-C2) first.

## Web and blog check (PARENT WORKER HARVEST-A, 28 Sept 2026)

Run per `.claude/briefs/check-solved.md` "Open web and blog comment threads" before key application; covers both
fr.3251 folders (same sender, recipient and volume). (a) Plain web searches: "Lodovico Birago Duca di Nevers 1572
lettere cifra Saluzzo" (Treccani/Wikipedia biography, BnF fr.4702 finding aid; no reading); "fr. 3251" OR
"français 3251" Birago Nevers chiffre (BnF finding aid cc49712p only); "Ceppo-Nevers cipher Birago deciphered"
(dbourdeau.github.io/cyphersolver index and two GitHub forks of that repository; the index lists fr.3251 ff.11,
21v, 35, 87, 138-174, 184 as having no published reading, SOLVED_CATALOGUE.md "Birago and Ceppo to Nevers",
checked 22 Sept 2026 there; its only fr.3251 reading work is f.119, a different cipher); "Birago Nevers 1570 1571
cifra Ceppo lettere decifrate Carmagnola" (the same index; a 2019 Birago family chapter on ResearchGate, not about
ciphers). (b) Blog site searches: site:scienceblogs.de klausis-krypto-kolumne Nevers Birago (no hit);
site:cryptiana.blogspot.com Nevers Birago, plus the blog's own search for "3251" and "Birago" (hits are the July
and August 2024 posts on f.119, 13 Nov 1571, the numeric figure cipher -- not these letters; no comment on them
gives a reading); site:ciphermysteries.com Nevers cipher Birago (no hit). (c) Bourdeau's repository cloned fresh
28 Sept 2026 and grepped for 3251 / birago: only targets/birago (f.119). Result: no reading or decipherment of
the ff.11, 21v, 35, 87 (Ceppo-Nevers) or ff.138-184 (1572) letters located on the open web or the three blogs.
Requests: web search 7, cryptiana.blogspot.com 2, github.com 1 clone.

## HARVEST-D2: value-blind sign sheet cut; targets held for a cipher-locating pass (PARENT WORKER HARVEST-D2, 28 Sept 2026)

Brief `.claude/briefs/runs/2026-09-28-harvest-d2-3.md` item 2, second part. The key is on disk (`keys/key_nevers_birago_1572.tsv`,
KEY-IMG-3251), so the group is not blocked on the key. Status stays `open`; no reading, no class.

**Sheet.** `harvest/cut_sign_sheet.py` cuts the 51 signs of Tomokiyo's `NeversBirago.png` (44 letter homophones plus the
7 word codes; one per key row, q/x/y blank as in the table) by ink blobs assigned to the header columns, relabels them
T## by a seeded shuffle and writes `harvest/sign_sheet_blind_1572.png` (headers removed, for readers) and
`harvest/sign_id_map_1572.json` (id -> value, never shown to a reader). Column assignment checked by eye against the
key table on a labelled render (D and the n-like zigzag under i, T under g, B under l, R under m, as the table has them).
The same reader brief, reconciliation and control scripts as the Ceppo-Nevers folder
(`../ceppo-nevers-fr3251-1570s/harvest/{blind_pass_brief.md,reconcile_blind.py,adjudication_sheet.py,decode_control.py}`)
apply with this sheet and map.

**Images: no cipher located yet.** f.138 (no.71): canvas 139 right half at 2400 px (f.138r) and canvas 140 at 2000 px
(f.138v, f.139r) are clear text throughout -- a long report on the Pinerolo fortification money, the Conte da Coconato's
company and Capitano Voluera -- with no cipher block visible; the letter runs on past f.139r and its cipher insertions,
if short, sit on a later leaf. The other six letters (ff.144, 152, 160, 168, 174, 184) have no image on disk, and the
canvas offset drifts from +1 to +3 across this span (NEV-C1), so each needs its own eye-checked canvas. Gallica served
every request this job (3 here, 2 s apart). Held, not negative: nothing was read.

**Next step (named):** one worker fetches each letter's canvases at 1200 px until its cipher passage is found (about
2-4 requests per letter, well inside 20), records the canvas and the region in `harvest/<folio>/manifest.json`, fetches
the native region, cuts 2x crops with `cut_folio_lines.py`'s tracked mode if the lines slope, and runs two blind passes
against `sign_sheet_blind_1572.png`, the value-blind reconciliation, `decode_control.py` with a `--map` pointing at
`sign_id_map_1572.json` (one line to add: the script reads the Ceppo map by name), and the blind reader. Order by
cipher length once located.

Requests this job: gallica.bnf.fr 3. Subagents: 0.
