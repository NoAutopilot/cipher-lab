partial

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
**Correction, 3 Oct 2026 (FIX-NO71-DATE, from OUT-CHECK-TOMO-BIRAGO2, 04:47 UTC): the "alli 7 di Genaro" docket is on f.137v (canvas 139, left, the facing verso), not f.138r, and reads "Attestat.ne fatta dal M.s ... conto di l'andata a ... alli 7 di Genaro" -- the docket of a preceding attestation, not of letter no.71 (checked on a native crop, canvas 139 region 1050,1800,800,1800). It is no evidence against Tomokiyo's 7 February 1572 for no.71.** No date conflict remains for no.71.

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

## LIKELY-3 (2 Oct 2026, account-4): known-key leaf f.178v read with the printed key, control-backed

Brief `.claude/briefs/runs/2026-10-02-account4-likely-phase2.md`, row 3 of `ciphers/_triage/likely-solves-2026-10-02.tsv`.
`tools/intake_gate_check.py nevers-birago-fr3251-1572` exit 0 at 03:35 UTC (web/blog check HARVEST-A, 28 Sept, on file).
Status `open` -> `partial` (a control-backed reading of part of one leaf exists; the seven target letters are unread).
No class, no novelty wording (rule 10).

**Why the known-answer step ran this way.** The row's `head_start` (b) and its known-answer step name "no.87's period
decipherment" as the answer to score the key and the transcription against. NEV-C1 and the LANE NEV follow-up (27 Sept,
above) already established that the tipped-in sheet (canvas 183) shows only bleed-through and cannot be read on Gallica, so
there is no clerk plaintext to diff against. The nearest instrument is LANE NEV's own named option (ii): decode the no.87
cipher passage itself -- the leaf Tomokiyo built the key from, so the key is *known* to apply to it -- with the key of record
against value-shuffled keys, plus the language judge, labelled as a target-style test. That is what ran; the f.138 unread
leaf (whose cipher passage HARVEST-D2 had not even located) was not touched, per the row's own "known answer first" order.

**Material.** Canvas 182 (f.178v, ink foliation checked by NEV-C1) native region 1703,848,2900,3452 of the 8517x5851 canvas,
fetched once by `tools/iiif_lines.py` into `harvest/f178v/src_*.jpg` (manifest `harvest/f178v/manifest.json`); 23 lines found
by the row ink profile (pitch 137 px; debug overlay `harvest/f178v/f178v_lines_debug.jpg`, checked by eye: the whole cipher
block, every line one band), 3 segments of 1250 px per line, 50 px overlap. `harvest/make_2x.py` upscales the segments 2x into
`harvest/f178v/lines2x/` (gitignored, regenerable; 1x crops were too small for readers on the sibling folder). This job read
**lines L01-L10 only** (budget: 3 vision calls); L11-L23, the two cipher lines at the foot of f.178r and the three at the head
of f.179r are cut (L11-L23) or not yet fetched (f.178r, f.179r).

**Blind passes** (`harvest/blind_pass_brief_1572.md`, the Ceppo-Nevers brief adapted to the 51-cell `sign_sheet_blind_1572.png`
and the off-sheet shapes this page shows: X_K, X_A, X_EQ, X_S, X_NEW). Two Sonnet readers, each given only the brief, the sheet
and the 30 crops: `f178v/passA.tsv` 290 signs, `f178v/passB.tsv` 294. Value-blind reconciliation by the sibling's
`reconcile_blind.py`: **259 of 294 aligned positions agreed (0.88)**, 35 unsettled; a third Sonnet reader, also value-blind,
settled 34 of them from the crops with the agreed neighbours as landmarks (`f178v/adjudicate_in.tsv` -> `adjudicate_out.tsv`:
23 to reader A, 8 to reader B, 3 NONE -- the epsilon-and-o cell T29 read by one reader as T24 + a separate T88). Final
`f178v/passC.tsv`: **290 signs, 0 '?', 4 off-sheet** (1 X_K on L05, 3 X_NEW "lone 8" on L06/L09/L10). The systematic splits
were look-alike pairs (T50/T92, T18/T98, T51/T95, T86/T60, T29/T24); this worker never saw a sign value while reconciling.

**Control (rule 3), `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py f178v/passC.tsv --map ../sign_id_map_1572.json`,
corpus it16dip, 200 value-shuffled keys (same homophone counts, values moved between signs):**

| sequence | signs | letters | real key | shuffles mean / max | z | rank of 201 | power control (rank 1), err 0.12 |
|---|---|---|---|---|---|---|---|
| pass A alone | 290 | 336 | -1.058 | -1.632 / -1.340 | 4.38 | 1 | not run |
| pass B alone | 294 | 305 | -1.091 | -1.622 / -1.303 | 4.03 | 1 | not run |
| passC before adjudication (22 '?') | 293 | 305 | -0.965 | -1.590 / -1.219 | 4.44 | 1 | 20/20, z median 3.87 min 3.04 |
| **passC final, seed 1** | 290 | 318 | **-1.043** | -1.630 / -1.346 | **4.53** | **1** | **20/20, z median 4.09 min 3.13** |
| passC final, seeds 2 and 3 | 290 | 318 | -1.043 | -1.618 / -1.328; -1.618 / -1.292 | 4.14; 4.25 | 1; 1 | -- |

Power control = 20 it16dip windows of the same passage lengths enciphered with the same key, 12% of signs (the measured
reader disagreement, 1 - 0.88) replaced at random, then the same 200-shuffle test: the real key ranks first in every window,
so at this error the test has the power to see a right key, and the target's rank 1 / z 4.1-4.5 is a real result, not noise.
Value fits for the off-sheet signs (reported, not applied): X_K (1 occurrence) per -1.037 vs unkeyed -1.043 (no decision);
X_NEW lone 8 (3) quello -1.025, che -1.036 vs unkeyed -1.043 (weak; a word code is plausible, undecided).

**Reading** (`tools/decode_key.py ciphers/nevers-birago-fr3251-1572` from `harvest/ciphertext_f178v.tsv` + `harvest/key_1572_sheet.tsv`
via `decode.json`, written by `harvest/build_decode_inputs.py f178v`; `--check` exit 0, "reading up to date"). Grades (rule 4):
**290 tokens: H 0, C 0, S 185, M 101, I 0, U 4** -- a cryptanalytic result (S from the printed key backed by the shuffled-key
control; M where the agreed sign sat at reader confidence M or was settled by the third reader; U the four off-sheet signs).
`harvest/reading_f178v.txt`, letters only in `harvest/f178v/reading_f178v_letters.txt`:

    L01 dasoriasteze[per]incaminarciala        | L02 uoltadiguascognasubitohauto
    L03 guectanouasieritornatoa[carmagnola]ne   | L04 piuceneepartitodimodi[che]esendi
    L05 nsoplagohiedelao·enione[che]coniman     | L06 tenendo[et]fauorizansotutili·n[et]de
    L07 pendendoprincipalmentedalacaca          | L08 degegorancihauendoiscastelodi[carmagnola]
    L09 [et][quello]dirauelinelemaniouelapiupa· | L10 sedncoldatisono·neglinepuofaresi

Read as Italian with word breaks (this worker's reading of the decode, not a second transcription): "...da Soria [Savoia?] ...
per incaminarsi a la volta di Guascogna; subito hauto questa nuova si e ritornato a Carmagnola, ne piu ... e ne e partito, di
modo che essendi ... la opinione che ... tenendo et favorizan[do] ... tutti li ... dependendo principalmente da la casa de
...oranci [Memoranci = Montmorency?], havendo il castello di Carmagnola et quello di Ravel[lo] ne le mani, ove la piu pa[rte]
... soldati sono ... ne gli ne puo fare si..." Content-consistent with no.87's prose (Saluzzo, 8 Sept 1572, after Coligny's
death; Carmagnola and the Montmorency connection). Known gaps in the decode: the printed key has no sign for q, and the
reader's g/c cells read "guecta" where "questa" stands -- the q homophone is one of the signs the table leaves blank or
assigns elsewhere, to be settled from more text, not by this job.

**Judge** (`tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f178v/reading_f178v_letters.txt`):

    FAIL language: score=-1.068, null_p99=-1.73, real_p05=-0.927, real_median=-0.832, mode=both, N=318
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

Shuffled-target control for the judge (ARM-C1 rule): the same key applied to the sign order of passC shuffled, three seeds,
scores -1.657 / -1.738 / -1.771 (at or below null_p99), so the judge discriminates at this N and the FAIL is a near-miss
(-1.068 against -0.927), consistent with the 12% residual reader error and the four unkeyed signs, not a non-test. No
"reading ready" line: the judge gate is not met, so no verifier hand-off and no print_check yet.

**What this settles.** The known-answer question the row asked -- is the key right, and how well do blind readers read this
hand -- is answered: the key reads the leaf it was built from at rank 1 of 201 with a power control that passes at the
measured error (key right); the readers agree at 0.88 on a dense symbol page, well above the 40-70% this repo recorded on
fr.7129 and AX-4612TR (transcription usable). The row's "decides whether to continue" is a yes. Rate for pricing: 10 lines
(290 signs), 3 Sonnet vision calls, about 13 minutes of reader time in all; see the ledger for the dollar figure.

Requests: gallica.bnf.fr 4 (info.json canvas 182; one HTTP 500 on a URL this worker built with a doubled ark prefix, its
own error, not a Gallica reset; the region at 2682 px wide; the region re-fetched at 2900 px wide after the first clipped
the right end of L07-L10). Vision calls 3 (two blind passes, one adjudication). No other host. No credentials.

## GAPS-nevers-birago-fr3251-1572 (2 Oct 2026, account-4): f.178v L11-L23 read the same way, leaf complete

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the section below as LIKELY-3 wrote it at
03:49 UTC: "f.178v L11-L23 two blind passes + adjudication, ~$6". `tools/intake_gate_check.py` exit 0 at 04:24 UTC before
the step. No class, no novelty wording (rule 10). Status stays `partial`.

**Material.** No Gallica fetch: the 1x crops of L11-L23 were already on disk (`harvest/f178v/f178v_L11..L23_s1..s3.jpg`,
cut by LIKELY-3's `tools/iiif_lines.py` run from canvas 182); `harvest/make_2x.py --lines 11-23` made the 39 2x reader
crops (gitignored, regenerable). Same brief (`harvest/blind_pass_brief_1572.md`), same 51-cell `sign_sheet_blind_1572.png`.

**Blind passes.** Two value-blind Sonnet readers, each given only the brief, the sheet and the 39 crops:
`f178v/passA_L11-23.tsv` 377 signs, `f178v/passB_L11-23.tsv` 378. Reconciliation by the sibling's `reconcile_blind.py`
(no value read): **360 of 379 aligned positions agreed (0.95)**, 19 unsettled (7 split, 5 split-H-A, 4 split-H-B, 3 gap);
a third value-blind Sonnet reader settled the 18 with a merged position from the crops with the agreed neighbours as
landmarks (`f178v/adjudicate_in_L11-23.tsv` -> `adjudicate_out_L11-23.tsv`: 10 to reader A's cell, 6 to reader B's, 1 to a
cell neither named (L20 pos 15, T66), 1 NONE (L15 pos 15: the small circle belongs to the T29 sign)). Final
`f178v/passC_L11-23.tsv`: **377 signs, 1 '?' (L16 end, both readers), 8 off-sheet** (X_A 1, X_EQ 2, X_S 1, X_NEW 4). The
recurring look-alike splits were T95/T66 (3, all settled T95 "bar crosses the stem"), T98/T18 (3, all T98), T26/T76/T27
(3), T60/T86, T64/T52. Reader A's own report: "the plain t has no clear cell, so I gave T42 at M or L confidence
throughout" -- see the g-sign note below. Joined leaf sequence `f178v/passC_L01-23.tsv` = LIKELY-3's `passC.tsv` (L01-L10,
290) + this pass (377) = 667 signs.

**Control (rule 3)**, `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py <seq> --map sign_id_map_1572.json --err 0.12`,
corpus it16dip, 200 value-shuffled keys (same homophone counts, values moved between signs), power control = 20 it16dip
windows of the same passage lengths enciphered with the same key with 12% of signs replaced (the brief's level; the measured
disagreement this pass is 5%, 8% pooled over the leaf, so 12% brackets it):

| sequence | signs | letters | real key | shuffles mean / max | z | rank of 201 | power control (rank 1), err 0.12 |
|---|---|---|---|---|---|---|---|
| **L11-L23 passC, seed 1** | 377 | 420 | **-1.038** | -1.620 / -1.270 | **4.11** | **1** | **20/20, z median 3.97 min 3.31** |
| L11-L23 passC, seeds 2 and 3 | 377 | 420 | -1.038 | -1.620 / -1.305; -1.623 / -1.251 | 4.02; 3.83 | 1; 1 | -- |
| **L01-L23 joined, seed 1** | 667 | 738 | **-1.040** | -1.622 / -1.325 | **4.60** | **1** | **20/20, z median 4.19 min 3.49** |
| (LIKELY-3, L01-L10, for comparison) | 290 | 318 | -1.043 | -1.630 / -1.346 | 4.53 | 1 | 20/20, z median 4.09 |

The new lines read under the key exactly as the first ten did (same score band, rank 1 at every seed, power control passing
at an error above the measured one): the key reads the whole witness leaf, and the readers' agreement rose from 0.88 to 0.95
on the second half of the page.

**Reading** (`tools/decode_key.py ciphers/nevers-birago-fr3251-1572`, job rebuilt by `harvest/build_decode_inputs.py f178v
--seq f178v/passC_L01-23.tsv`; `--check` exit 0, "reading up to date"). Grades (rule 4), whole leaf L01-L23: **667 tokens:
H 0, C 0, S 533, M 121, I 0, U 13** -- S = cryptanalytic, control-backed (the printed key's value, rank 1 of 201 shuffled
keys on this leaf); M = the same value where the agreed sign sat at reader confidence M or was settled by the third reader
(L01-L10: 104 M of 290; L11-L23: 22 M of 377, the readers rated this half H almost throughout); U = the 13 unkeyed signs
(X_NEW 7, X_EQ 2, X_A, X_K, X_S, '?' one each). No H or C: a cryptanalytic result. `harvest/reading_f178v.txt`, letters in
`f178v/reading_f178v_letters.txt` (via `harvest/letters_from_reading.py`), L11-L23 as decoded:

    L11 [per]uosnsenzahaugreioforgadipotnrsi | L12 rimediare[per]oenecesario[che]·seuoseasi
    L13 turaregpaeseprouedasaltriaigo        | L14 erni[che]·sianonesui·ratehonede
    L15 pendentisasui[et][che]sianoan[che][turino][turino]altri | L16 gentisaremosegpreinconfusionei·
    L17 barondesadres·[che]serendaubedie·    | L18 tisimo[et]trouibonituto[quello][che]iogli
    L19 cogansi[per]ilserui[quello]iodil[turino]nsimeno | L20 ·sipuicontenereaheuoltegeco
    L21 sigostrareunagrangalnconten          | L22 tnzadige·etoseguitoin·gpasai
    L23 piuconaltri[per][quello]intendosiganiera

Read as Italian (this worker's reading of the decode, not a transcription): "...per voi ... senza haver ... forza di poter ...
rimediare, per o e necessario che ... se vostra ... [L13] ...are ... paese, proveda ... altri amico/..., [L14] ...erni che
siano ... [L15] pendenti ... et che siano anche [Turino] [Turino] altri [L16] genti saremo sempre in confusione ...
[L17] baron des Adrets ... che se renda ubedie[n]tissimo [L18] et trovi boni tutto quello che io gli [L19] co[m]andi, per il
servi[tio] ... quello io di[ssi?] ... [Turino] ... [L20] si pui contenere a ... volte ... [L21] si mostrare una gran ... conten[te]zza
di ... [L22] et o seguito in ... passai [L23] piu con altri per quello intendo si[a?] maniera". "Baron des Adrets" (L17: François
de Beaumont, baron des Adrets, the Dauphiné captain) and "Turino" twice (L15) are content-consistent with a Saluzzo letter of
8 Sept 1572.

**g-sign note (observation, not applied).** The printed table has no sign for q and two for m (T17, T54); on this leaf T17
never occurs (0 of 667) while words that need m decode with g: `ganiera` (maniera), `segpre` (sempre), `sigostrare`
(mostrare), `cogansi` (comandi), and L01-L10's `guecta` (questa) needs q. The g value sits on T42 (12 occurrences; reader A's
"plain t" cell), T70 (8) and T88 (3). One of these is probably the second m homophone or the missing q, settled by a
value-fit (`decode_control.py --fit-sign T42 --fit-sign T70 --fit-sign T88`, disk only) -- named as the next cheapest step
below, not run here (the brief names one step). Unused sheet cells on this leaf: T15 (bugonotti), T17 (m), T51, T78.

**Judge** (`tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f178v/reading_f178v_letters.txt`,
the joined L01-L23 decode):

    FAIL language: score=-1.074, null_p99=-1.772, real_p05=-0.905, real_median=-0.835, mode=both, N=738
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

L11-L23 alone (`f178v/reading_f178v_L11-23_letters.txt`): FAIL -1.081 vs real_p05 -0.908 (null_p99 -1.718, N=420).
Shuffled-target control for the judge (ARM-C1 rule; `harvest/shuffled_judge.py`, the same key on the same signs in shuffled
order, 20 seeds): L01-L23 joined, **0 of 20 PASS**, scores mean -1.684, min -1.731, max -1.631 (null_p99 -1.772); L11-L23
alone 0 of 20, mean -1.666, max -1.581. The judge discriminates at this N and the FAIL is a near-miss of the same size as
before (-1.074 vs -0.905 on 738 letters; -1.068 vs -0.927 on 318): more text did not lift the score, which points at a
systematic key or sign-cell error (the g-sign note) rather than reader noise, since the reader agreement rose to 0.95.
No "reading ready" line: the judge gate is not met, no verifier hand-off, no print_check yet.

Vision calls 3 (two blind passes, one adjudication). Requests: none to any host (gallica.bnf.fr 0; everything from disk).
No credentials. Box 04:24-04:3x UTC of 60 minutes.

## GAPS3-nevers-birago-fr3251-1572 (2 Oct 2026, account-4): value-fit of the g-valued signs, T42 reads m

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the gaps section below as GAPS-nevers-birago
wrote it at 04:3x UTC: "value-fit of the g-valued signs T42/T70/T88 and X_NEW with decode_control.py --fit-sign (disk only,
~$1)". `tools/intake_gate_check.py` exit 0 at 05:18 UTC before the step. Disk only: 0 vision calls, 0 requests to any host.
No class, no novelty wording (rule 10). Status stays `partial`.

**Instrument.** `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py f178v/passC_L01-23.tsv --map sign_id_map_1572.json
--fit-sign T42 --fit-sign T70 --fit-sign T88 --fit-sign X_NEW --fit-sign X_EQ --fit-values q` (joined leaf, 667 signs, 738
letters, corpus it16dip). Two options added to the shared sibling tool (rule 8, an option not a private copy): `--fit-values`
(extra candidate values beyond the key's own -- the printed table has no sign for q, so q could not be a candidate before)
and `--fit-top`; `--windows 0` no longer crashes. The fit sets one sign to each candidate value in turn, the rest of the key
held, and reports the mean log10 4-gram score per letter. **Caveat read off the output:** every multi-letter word code
(quello, qual, che, per) tops every list, including for signs that are plainly letters -- inserting a well-formed word
inflates a per-letter n-gram score -- so the comparison that means anything is among single letters and null; the word
codes are reported but not read as fits.

**Fits (single letters and null; "as keyed" = the printed value):**

| sign | occ. | printed | best single letters (score) | printed value's score | contexts (decode with the rest of the key) |
|---|---|---|---|---|---|
| **T42** | 12 | g | **m -1.005**, t -1.009, s -1.010, n -1.016, null -1.016 | g -1.040 | se[g]pre, si[g]ostrare, [g]aniera, co[g]ansi, uolte[g]eco, de[g]e[g]oranci, gran[g]aln.., for[g]a, [g]enti, pla[g]o; di[g]uascogna |
| T70 | 8 | g | **g -1.005** (with T42=m), r -1.008, null -1.009, l -1.011 | g (as keyed) | guasco[g]na, ne[g]li, io[g]li, una[g]ran, se[g]uito, di[g]e, [g]paese, ai[g]o |
| T88 | 3 | g | e -0.988, null -0.989, t -0.991, o -0.991 ... q -1.006, g -1.005 | g -1.005 | [g]uectanoua (questa), hau[g]reio, in_[g]pasai |
| X_NEW | 7 | unkeyed | null -1.008, n -1.014, t -1.014, i -1.014; unkeyed -1.005 | -- | word-boundary positions throughout (desadres[_]che, erniche[_]siano, tnzadige[_]etoseguito, [_]sipui..) |
| X_EQ | 2 | unkeyed | within 0.005 of unkeyed for every value | -- | anonesui[_]rate, daubedie[_] (line end) |

**Decision, one value moves: T42 g -> m, graded S** (rule 4: two or more words read with it -- sempre L16, mostrare L21,
maniera L23, comandi L19 ("comansi" as transcribed, the d/s a reader cell), meco L20, Memoranci L08 (Montmorency, Italian
form), and malinconia/malcontent.. L21 -- against one word, Guascogna L02 pos 8, that needs g). Robustness: the same fit on
each half of the leaf alone gives m as the best single letter on L11-L23 (8 occurrences, -0.971 vs t -0.990, the half the
readers rated H throughout) but not on L01-L10 (4 occurrences: the Guascogna g, "pla[g]o" and the name Memoranci, which the
corpus cannot score; m is outside the top 8 there) -- the fit is carried by the H-confidence half and the word evidence,
and the L02 token is repaired from the word (`harvest/exceptions_f178v.tsv`, value g, grade I) rather than the sign re-read:
whether that sign is a T42/T70 look-alike or a scribal slip is an image question, not this step's. **T70 stays g** (five
clear words: Guascogna's gn, negli, gli, gran, seguito; g is also the best single letter in the fit). **T88 stays as printed,
undecided**: three occurrences, q (the "guecta" = questa reading, the one word) scores worst of all single letters (-1.006)
and e/null/t/o best, within 0.02 of each other -- no value clears rule 4's two-word bar, so no change; "guecta" also carries
a c where s is needed (T50 c / T92 s, a look-alike pair the reconciliation logged), so the word is a transcription question
as much as a key one. **X_NEW stays unkeyed**: null and the unkeyed break score the same (-1.008 vs -1.005), every letter
scores worse, and all seven sit at word boundaries, consistent with a separator or a word code the n-gram fit cannot see.
X_EQ (2): no decision possible at 2 occurrences. The printed key stays on file unchanged as `harvest/sign_id_map_1572.json`;
the fitted key is `harvest/sign_id_map_1572_fit.json` (T42 m, `value_printed` g kept in the row) and `key_1572_sheet.tsv`
row T42 (value m, grade S, note names the fit). T17 (m) still never occurs: the printed table's two m signs may be T17 and
T42's cell with T42 and T17 confused on the sheet cut, or Birago's clerk used a different m -- open, for an image check.

**Control (rule 3), before and after, same instrument (`decode_control.py --map <map> --err 0.12`, 200 value-shuffled keys,
power control 20 it16dip windows at 12% injected error, the measured pooled reader disagreement being 8%):**

| key | signs / letters | real key | shuffles mean / max | z | rank of 201 | seeds 2, 3 (z; rank) | power control, err 0.12 |
|---|---|---|---|---|---|---|---|
| printed (GAPS-nevers-birago, 04:3x) | 667 / 738 | -1.040 | -1.622 / -1.325 | 4.60 | 1 | -- | 20/20, z median 4.19 min 3.49 |
| **fitted, T42 = m** | 667 / 738 | **-1.005** | -1.615 / -1.320 | **4.84** | **1** | 4.56; 1 and 4.45; 1 | **20/20, z median 4.25 min 3.40** |

**Reading** (`tools/decode_key.py ciphers/nevers-birago-fr3251-1572`, job rebuilt by `harvest/build_decode_inputs.py f178v
--seq f178v/passC_L01-23.tsv`, now with `exceptions_f178v.tsv`; `--check` exit 0, "reading up to date"). Grades (rule 4),
whole leaf: **667 tokens: H 0, C 0, S 532, M 121, I 1, U 13** (before: S 533, M 121, I 0, U 13; the one I is L02 pos 8).
No H or C: a cryptanalytic result. Lines whose text changed (`harvest/reading_f178v.txt`):

    L05 nsoplamohiedelao·enione[che]coniman   | L08 dememorancihauendoiscastelodi[carmagnola]
    L11 [per]uosnsenzahaugreioformadipotnrsi  | L16 mentisaremosempreinconfusionei·
    L19 comansi[per]ilserui[quello]iodil[turino]nsimeno | L20 ·sipuicontenereaheuoltemeco
    L21 simostrareunagranmalnconten           | L23 piuconaltri[per][quello]intendosimaniera

"de Memoranci" (L08: the Montmorency connection no.87's prose carries), "senza haver ... forma di poter ... rimediare"
(L11-L12), "menti saremo sempre in confusione" (L16), "io gli comandi per il servitio" (L18-L19), "contenere ... volte meco"
(L20), "si mostrare una gran mal[in]conten[tezza]" (L21-L22), "per quello intendo si[a] maniera" (L23).

**Judge** (`tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f178v/reading_f178v_letters.txt`):

    FAIL language: score=-1.032, null_p99=-1.772, real_p05=-0.905, real_median=-0.835, mode=both, N=738
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

L11-L23 alone: FAIL -1.018 vs real_p05 -0.908 (null_p99 -1.718, N=420). Before this step: -1.074 and -1.081. The one sign
value moved the leaf 0.042 toward the gate and the second half 0.063, both the same direction as the control's z; the
remaining gap to real_p05 is 0.127 on the leaf. Shuffled-target control (ARM-C1 rule, `harvest/shuffled_judge.py` with the
fitted map, 20 seeds): L01-L23 **0 of 20 PASS**, mean -1.668, min -1.718, max -1.614 (null_p99 -1.772); L11-L23 0 of 20,
mean -1.647, max -1.558. The judge still discriminates at this N; the FAIL is a near-miss, smaller than before. No "reading
ready" line: the judge gate is not met, no verifier hand-off, no print_check.

**What this settles.** The hypothesis the previous step named (a systematic value error on the g-valued signs) is confirmed
for one sign and refuted for another: T42 is an m homophone on this leaf, not g, and T70 is g; T88 and the off-sheet signs
stay open at their occurrence counts. The residual judge gap (0.127) is not one more sign value of this size: the next lift
has to come from the transcription (the T50/T92 c/s and other look-alike pairs the reconciliation logged, the T42/T17 cell
question) or from more text, which is the Verdict's next step. The fit also shows what the printed key's remaining blanks
look like under this instrument: a word code or separator (X_NEW) is invisible to a letter n-gram fit, so X_NEW is for a
context read, not a re-fit.

Vision calls 0. Requests: none to any host. No credentials. Box 05:18-05:3x UTC of 45 minutes.

## GAPS4-nevers-birago-fr3251-1572 (2 Oct 2026, account-4): f.178r foot + f.179r head read; the clerk's clear decipherment found legible on canvas 182

Brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of the gaps section below as GAPS3 wrote it at
05:3x UTC: "f.178r foot + f.179r head (2 gallica requests, same pipeline under the fitted key, ~$3)". `tools/intake_gate_check.py`
exit 0 at 06:07 UTC before the step. No class, no novelty wording (rule 10). Status stays `partial`. Box 06:07-06:3x UTC.

**What the images show (corrects NEV-C1 and the gap list).** Three facts the 1000 px overviews settle at a glance once
the right crops are made (own looks on `images/f178r_verso177_canvas181.jpg`, `f178v_179r_canvas182.jpg`,
`f179v_insert_canvas183.jpg`; corrections written into `images/manifest.json`):
1. f.178r's foot carries **3** cipher lines, not 2.
2. The right page of canvas 182 is not f.179r's prose: it is **the laid-in sheet with the clerk's clear decipherment of the
   whole no.87 cipher passage** (19 lines, "che in di bellaguarda ... che altrimente", BnF stamp at its foot), lying over the
   head of f.179r; Birago's hand shows beneath it only from "...comandando alli sindici" down. NEV-C1 read it as "plaintext
   resumes, mentions Bellagarda, a direct continuation" -- it is the decipherment, legible at native resolution.
3. Canvas 183 is the same opening with that sheet flipped over onto f.178v (its blank back = the "bleed-through" NEV-C1 found
   illegible), so its right page is **f.179r uncovered: 3 cipher lines at the head**, then prose. The gap list's "tipped-in
   decipherment, needs-physical-access" blocker is lifted: the written face is photographed on canvas 182.

**Material.** Gallica native regions, `tools/iiif_lines.py` (browser UA, >= 1.5 s apart): canvas 181 `4700,3720,3050,620`
-> `harvest/f178r/` (3 lines; the autocorrelation read the tall signs under a prose tail as 5 lines at pitch 100, so the
centres were given by eye with the new `--centres` option, offline test added to `tools/tests/test_iiif_lines.py`; both
blind readers then found the lines fall 156-196 px across the region and the fixed bands clipped the tails, so
`harvest/f178r/slope/` is the `--follow-slope 300 --slope-margin 40` re-cut used for the adjudication); canvas 183
`4800,1000,3000,620` -> `harvest/f179r/` (3 lines; re-fetched once 150 px wider after the first region clipped the first
sign of each line); canvas 182 `4700,680,3150,3250` -> `harvest/f179r_sheet/` (the clear sheet, 19 lines + the prose
beneath). 2x reader crops by `harvest/make_2x.py --folio`. **Gallica requests 7** (2 HTTP 500 / reset on this worker's own
malformed doubled-ark URLs -- `--ark` takes the bare id, the same slip LIKELY-3 logged; 1 reset on canvas 183 retried once
after a pause; 3 regions fetched; 1 re-fetch), against the brief's 3: over by the two malformed calls and the re-fetch.

**Clear sheet** read by this worker by eye on three 0.62-scale strips (`harvest/f179r_sheet/decipherment_sheet.tsv`, 19 lines,
H 15 / M 4 lines; the clerk's dots and abbreviations kept: `car.la` = carmagnola, `ma.ta` = maesta). Its span: L01-L03a
("che in di bellaguarda ... et tolto licencia") = f.178r foot; L03b ("da loro altezze") to L17a ("intendo di maniera") =
f.178v L01-L23; L17b-L19 ("se'l se hauesse a fare retrenchiamento sopra questa gente laudarei piu tosto brigarsene che
altrimente") = f.179r head. The attribution rests on the match with the f.178v decode already on file (next paragraph), not
on the sheet's position alone.

**Blind passes** (same brief and 51-cell sheet, 18 crops per reader, one Sonnet call each): f.178r `passA` 88 / `passB` 90
signs, reconciled 79 of 90 aligned agreed (**0.88**), 11 unsettled; f.179r `passA` 89 / `passB` 89, **79 of 89 (0.89)**,
10 unsettled. Nineteen of the 21 splits were one systematic pair -- reader A T83 where reader B read T24 -- settled by the
third value-blind reader (one call, both folios' `adjudicate_in.tsv`, the sloped f.178r crops): all 19 to T83 ("wide two-part
sign, closed left loop plus crossed right lobe; T24 is a single small epsilon with a swash tail"), T95 at f.178r L01/6, the
two "reversed 3" signs to T24 at M, one gap row NONE, and the f.178r L03 tail (cut off in both fixed-band passes) read from
the sloped crop: 9 more signs, pos 27-35, one reader only, graded M where it said M. Final `f178r/passC.tsv` **97 signs, 0 '?',
7 off-sheet** (X_NEW 6, X_S 1); `f179r/passC.tsv` **89 signs, 0 '?', 5 off-sheet** (X_NEW 5, three of them struck through at the
line end). Joined passage `harvest/passC_no87.tsv` (`join_no87.py`: R01-R03 + L01-L23 + V01-V03) = **853 signs**.

**Control (rule 3)**, `decode_control.py --map sign_id_map_1572_fit.json --err 0.12` (200 value-shuffled keys, power control
20 it16dip windows at 12% injected error, the measured disagreement being 11-12% on these short runs):

| sequence | signs / letters | real key | shuffles mean / max | z | rank of 201 | power control, err 0.12 |
|---|---|---|---|---|---|---|
| f.178r foot L01-L03 | 97 / 98 | -1.088 | -1.622 / -1.235 | 2.90 | 1 | 16/20, z median 3.51 min -0.23 |
| f.179r head L01-L03 | 89 / 86 | -1.062 | -1.620 / -1.221 | 2.89 | 1 | 11/20, z median 2.80 min 1.40 |
| **no.87 joined, 853** | 853 / 922 | **-1.019** | -1.614 / -1.319 | **4.60** | **1** | **20/20, z median 4.57 min 3.48** |
| (GAPS3, f.178v alone, for comparison) | 667 / 738 | -1.005 | -1.615 / -1.320 | 4.84 | 1 | 20/20, z median 4.25 |

At ~90 signs the n-gram shuffle test has little power (the control's own real key ranks first in only 11-16 of 20 windows), so
the two short runs' rank-1 results are weakly backed on their own; the joined 853-sign passage carries the control.

**Known-answer check against the clerk's sheet (new instrument, `harvest/align_sheet.py`):** decode each sequence with a map,
fold decode and sheet span to a-z (word codes expanded, u/v i/j merged), share of decoded letters inside difflib matching
blocks of >= 3, against 200 value-shuffled keys (the decode_control shuffle):

| sequence | sheet span | fitted key (T42 = m) | printed key | shuffles mean / max | rank | z |
|---|---|---|---|---|---|---|
| f.178r foot | L01-L03a | 0.816 | 0.816 | 0.099 / 0.210 | 1 | 19.6 |
| f.178v L01-L23 (GAPS3's decode) | L03b-L17a | **0.829** | 0.802 | 0.066 / 0.106 | 1 | 55.1 |
| f.179r head | L17b-L19 | 0.930 | 0.930 | 0.038 / 0.104 | 1 | 50.3 |
| **no.87 joined, 853 signs** | L01-L19 | **0.837** | 0.816 | 0.069 / 0.114 | 1 | 53.2 |

So the key reads the whole passage at 0.84 of the clerk's own letters, and GAPS3's one-sign fit (T42 g -> m) is confirmed by the
period witness: it scores higher than the printed key on the clerk's text (0.837 vs 0.816; 0.829 vs 0.802 on f.178v). Where the
decode and the sheet part: the first ~8 signs of f.178r L01 ("che in di bellaguarda" reads `eueros··`), the c/s pair ("aserde"
for "a carde", "guec-"/"ques-" again), and the off-sheet signs -- of which **the t-shaped X_NEW reads m four times against the
sheet** (de·olti = de molti, ·asoto = ma solo, retrenchia·ento, altri·enti): entered as `exceptions_f178r.tsv` /
`exceptions_f179r.tsv`, value m, **grade C** (known plaintext). That t-shape is in all likelihood the printed table's second m
(T17, which never occurred on f.178v): the sheet cut draws it differently, so readers put it off-sheet; the f.178v X_NEW "lone 8"
is a different shape (it sits where the sheet reads carmagnola once, L03/4 -- one occurrence, not applied).

**Reading** (`tools/decode_key.py ciphers/nevers-birago-fr3251-1572`, three jobs now; `--check` exit 0, "reading up to date").
Grades (rule 4): f.178r **97: C 2, S 73, M 17, U 5**; f.179r **89: C 2, S 76, M 8, U 3**; f.178v unchanged 667: S 532 M 121
I 1 U 13; whole passage **853: H 0, C 4, S 681, M 146, I 1, U 21** -- a cryptanalytic result with four C tokens.

    f178r L01 eueros··[qual]demoltigiornieraaserde | sheet: che in di bellaguarda qual de molti giorni era a carde
    f178r L02 nesipretendeachauegepiuaritorna      | sheet: ne si pretendea ch'auesse piu a ritornare
    f178r L03 rea··masotoandarsenea[turino]ptoltisiienp· | sheet: a car.la ma solo andarsene a turino et tolto licencia
    f179r L01 selsehaueseafareretrenchiamento      | sheet: se'l se hauesse a fare retrenchiamento
    f179r L02 sopragufstagentelaudareipiutost      | sheet: sopra questa gente laudarei piu tosto
    f179r L03 osbrigarsene[che]altrimenti···m      | sheet: brigarsene che altrimente (then three struck signs)

**Judge** (`tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/reading_no87_letters.txt`, the whole
passage f.178r + f.178v + f.179r, letters via `letters_from_reading.py`):

    FAIL language: score=-1.046, null_p99=-1.781, real_p05=-0.902, real_median=-0.832, mode=both, N=926
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

Before the four C exceptions: -1.055 (N 922). f.178r alone -1.131 vs real_p05 -0.944 (N 98); f.179r alone -1.096 vs -0.952
(N 86): the two short runs score worse than the leaf (-1.032), as their misread line starts predict. Shuffled-target control
(`harvest/shuffled_judge.py`, fitted map, 20 seeds, 853 signs): **0 of 20 PASS**, mean -1.699, min -1.747, max -1.654
(null_p99 -1.78). The judge discriminates and the FAIL is a near-miss of the familiar size; no "reading ready" line, no
verifier hand-off, no print_check. The sheet now says what the judge could not: the decode is ~84% the clerk's text and the
residual is reader error on specific sign pairs, not the key.

**What this settles.** The Verdict step is done and the gap it named is closed: the whole no.87 passage (853 signs) is
transcribed and reads under the fitted key at rank 1 with a passing power control. The step also found the thing the folder
had filed as needing physical access: the period decipherment, legible, on canvas 182. With it, the next step is no longer a
transcription re-pass by eye but a sign-by-sign alignment of the sheet to the 853 signs (`tools/interlinear_align.py`, the
named tool for a clear text beside the cipher, disk only), which yields a C-grade key for every sign the clerk read, the
T17/t-shape and carmagnola/"8" questions, and a per-sign error map of the two readers -- the crib for the look-alike pass and
the gate for the seven target letters.

Vision calls 3 of 3 (two blind passes, one adjudication) plus this worker's own looks (overview crops, two debug overlays, a
ruler image per region, three sheet strips). Requests: gallica.bnf.fr 7 (above), no other host. No credentials.

## NEVBIR-152 (2 Oct 2026, account 2 for the account-3 orchestrator): f.152r no.77 first test under the 1572 key

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-letter.md`, WORK-QUEUE row NEVBIR-152 (f.152 no.77, 9 June 1572).
`tools/intake_gate_check.py nevers-birago-fr3251-1572` exit 0 at 15:11 UTC. Box 15:11-16:01 UTC. No class, no novelty
wording (rule 10). Status stays `partial`.

**Material.** Canvas 154 (ink foliation 152 on the right page, eye-checked on `images/f152r_canvas154.jpg`), 8517x5850.
The cipher run is one block mid-page: 7 signs after the prose "...et che bisogna", three full lines, then prose
"con uolermi fare tenere per altro di quello ch'io sono" (premise check: "one short inline cipher run"). Native region
`4350,3700,3800,580` fetched once (a first guess at `4350,3900,...` cut off the run's first line and was discarded), then
crops cut from the local file with the command:

    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f152r/src_ark_12148_btv1b9060248g_f154_4350_3700_3800_580.jpg \
      --out ciphers/nevers-birago-fr3251-1572/harvest/f152r --prefix f152r --centres 179,290,381,510 --max-width 1300 --overlap 60 --debug

4 lines x 4 segments, debug overlay `f152r/f152r_lines_debug.jpg` checked by eye; `make_2x.py --folio f152r` made the 2x
reader crops (gitignored); L01_s1/s2 are prose only and were not given to readers (14 crops per reader).

**Blind passes** (same `blind_pass_brief_1572.md` and 51-cell `sign_sheet_blind_1572.png`, with a page note: prose page, one
run). Two value-blind Sonnet readers: `f152r/passA.tsv` 97 signs, `passB.tsv` 97. `reconcile_blind.py`: **92 of 98 aligned
positions agreed (0.94)**; 6 unsettled (L01 pos 1-2 a one-step offset between readers, L03 pos 30 and 33, L04 pos 24 and 26),
all settled by a third value-blind Sonnet reader (`adjudicate_in.tsv` -> `adjudicate_out.tsv`, all M: T84, T70, T90, T27,
T78, T49; the L01 gap row was inserted by hand since the tool leaves gap rows unmerged). Final `f152r/passC.tsv`: **97 signs,
0 '?', 6 off-sheet X_NEW** (5 the t-shape both readers named, 1 a flat-bottomed U at L02/14). Lines: L01 7, L02 31, L03 33, L04 26.

**Control (rule 3)**, `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py f152r/passC.tsv --map sign_id_map_1572_fit.json
--err 0.12` (printed key + T42=m; corpus it16dip; 200 value-shuffled keys; power control 20 it16dip windows of the same
length at 12% injected error, measured disagreement 6%):

| sequence | signs / letters | real key | shuffles mean / max | z | rank of 201 | power control, err 0.12 |
|---|---|---|---|---|---|---|
| **f.152r passC, seed 1** | 97 / 103 | **-1.142** | -1.591 / -1.258 | **3.14** | **1** | 16/20, z median 3.12 min 1.76 |
| f.152r passC, seeds 2 and 3 | 97 / 103 | -1.142 | -1.563 / -1.246; -1.563 / -1.192 | 3.06; 2.73 | 1; 1 | -- |
| printed key (T42=g), seed 1 | 97 / 103 | -1.142 | -1.594 / -1.284 | 3.18 | 1 | -- (T42 does not occur here: same decode) |
| variant: t-shape X_NEW = m (`--extra X_NEW=m`) | 97 / 109 | -1.132 | -1.654 / -1.180 | 3.48 | 1 | 16/20, z median 3.17 |

Rank 1 of 201 at every seed with the real key 0.05-0.12 above the best shuffle; at 97 signs the test's own power is 16 of 20
(the GAPS4 lesson for ~90-sign runs), so the n-gram control alone backs this run only moderately. The known-answer check
below is the stronger instrument here.

**A decipherment slip for this run is filed with the letter (found this job; PREMISE-NEVBIR's (c) did not report it).** The
left page of canvas 154 (f.151v, the end of the previous letter) carries a small pasted slip of squared paper written in a
later hand than the letter: `f152r/slip_f151v_c154_1350_750_2350_1050.jpg`, read by eye into `f152r/decipherment_slip.tsv`:
"che io disimuli poiche / [struck: sen.ua a leuar..o.asione] sen.aaleu..o.asione a / ap.ns..o di leuarmi la reputa.ione ..c.ermi /
incompromesa la l'onore". Its dots are the decipherer's own unread signs. It sits between the letter's prose "et che bisogna"
and "con uolermi", the exact place of the cipher run. Who wrote it and when (squared paper suggests a modern reader, not the
1572 clerk) is not settled here; this is a prior (partial) decipherment of this item, a fact for the verifier (rule 10),
not a judgment made here.

**Known-answer check against the slip** (`align_sheet.py f152r/passC.tsv --sheet f152r/slip_for_align.tsv --sheet-lines L01-L04`,
the GAPS4 instrument, 200 value-shuffled keys): share of decoded letters in matched blocks >= 3: **fitted key 0.612**, shuffles
mean 0.047 max 0.121, **rank 1 of 201, z 25.1**; printed key 0.612 (z 25.8); with the t-shape as m 0.651 (max 0.113, z 29.2).
The ceiling is below 1 because the slip itself leaves about 15 signs as dots and the decode carries a word code
("[quello]") and a few letters the slip omits.

**Reading** (`tools/decode_key.py ciphers/nevers-birago-fr3251-1572`, job built by `harvest/build_decode_inputs.py f152r`;
`--check` exit 0, "reading up to date"). `harvest/exceptions_f152r.tsv` sets the five t-shaped X_NEW to m where the slip reads
an m at that position (disimuli, leuarmi, c.ermi, incompromesa x2) -- the same sign GAPS4 read m four times against the no.87
clerk sheet. Grades (rule 4): **97 tokens: H 0, C 0, S 84, M 12, I 0, U 1** (the five m exceptions are graded M by the tool
because both readers rated those signs M; the U is the flat-U X_NEW at L02/14, where the slip has a dot too). A cryptanalytic
result, the key published (Tomokiyo) plus the GAPS3 fit.

    f152r L01 | [quello]g[che]iodi                  slip: che io disimuli poiche
    f152r L02 | simuligoi[che]sgn·aalcunsotasioneha   slip: sen.aaleu..o.asione a
    f152r L03 | pnnsstosileuarmilareputationepmet    slip: ap.ns..o di leuarmi la reputa.ione ..c.ermi
    f152r L04 | ermiincompromesilhonore[qual]eu      slip: incompromesa la l'onore

Read as Italian (this worker's reading of the decode against the slip, not a transcription): "...che io dissimuli, poiche
sen[za] alcun[a] [oc]casione ha[nno] p[ro]curato? ... di levarmi la reputatione et cercarmi in compromes[so] il honore, quale
..." -- then the prose "con volermi fare tenere per altro di quello ch'io sono". Visible c/s and g/o look-alikes ("sotasione"
for "ocasione", "goi" for "poi") are the same sign-pair confusions logged on no.87.

**Judge** (`tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f152r/reading_f152r_letters.txt`):

    FAIL language: score=-1.171, null_p99=-1.625, real_p05=-0.951, real_median=-0.813, mode=both, N=108
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

Shuffled-target control (`harvest/shuffled_judge.py`, fitted map, 20 seeds): **0 of 20 PASS**, mean -1.659, min -1.867, max
-1.468. The judge discriminates at this N; the FAIL is a near-miss of the familiar size for a short run (f.178r foot -1.131,
f.179r head -1.096 at similar N). Secondary signal only, per the brief.

**What this settles.** The 1572 key reads the f.152r cipher run: rank 1 of 201 shuffled keys (z 2.7-3.1, power 16/20 at
this length) and 0.61 agreement with an independent clear decipherment filed beside it (shuffled max 0.12). No.77's other
pages were not searched for a further cipher run: f.152v is plain per PREMISE-NEVBIR; f.153r onward not opened this job.

Requests: gallica.bnf.fr 4 (info.json canvas 154; two cipher-region fetches, the first discarded; the slip region, whose first
attempt was a connection reset retried once after 20 s -- 5 attempts in all). Vision calls 3 (two blind passes, one
adjudication) plus this worker's own looks (overview, debug overlay, slip). No credentials.

## NEVBIR-184 (2 Oct 2026, account 2 for the account-3 orchestrator): f.184r no.90 cipher runs, first test under the 1572 key

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-letter.md`, WORK-QUEUE row NEVBIR-184 (f.184 no.90, 2 Oct 1572).
`tools/intake_gate_check.py nevers-birago-fr3251-1572` exit 0 at 16:1x UTC. Box 16:11-17:02 UTC. No class, no novelty
wording (rule 10). Status stays `partial`.

**Whole canvas first (brief step 1).** Canvas 188 (8261x5848) at 2500 px, both pages looked at by eye: the left page (f.183v)
is blank but for the vertical address docket "...Il Gran Comendatore" of the previous item; no pasted slip, no squared paper,
no interlinear gloss on f.184r. Canvases 189 and 190 (on disk from PREMISE-NEVBIR, 1000 px) show no slip either. No
decipherment of this letter's runs was found, so there is no known-answer check here.

**Where the cipher is.** no.90 carries much more cipher than its siblings: f.184r has four inline runs over 8 lines (this job);
f.184v has about 4 cipher lines at its foot and f.185r about 20 more (canvas 189), and f.185v one short run before the
signature (canvas 190 left) -- those are **not** read in this job (cap and box). Native region `4600,2550,2850,1380` of canvas
188 fetched once; crops cut from the local file with

    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f184r/src_ark_12148_btv1b9060248g_f188_4600_2550_2850_1380.jpg \
      --out ciphers/nevers-birago-fr3251-1572/harvest/f184r --prefix f184r --centres 30,130,230,330,445,570,690,800,900,1010,1133,1232,1350 \
      --follow-slope 300 --slope-margin 15 --max-width 1250 --overlap 50 --debug

(the lines drop about 110-170 px across the region, so the slope-following cut; a first autodetected cut with too few centres
gave bands holding two lines and was discarded). 13 bands; cipher in L01 (after "a V.ra Ecc."), L02, L03, L04 (to "e venuto"),
L07 (after "proposito"), L08, L09 (to "come intendo"), L12 (to ", mentre"). `make_2x.py --folio f184r` (gitignored); 21 crops
per reader.

**Blind passes.** Two value-blind Sonnet readers (`blind_pass_brief_1572.md` + page note "prose page, inline runs", the
51-cell sheet, crops only): `f184r/passA.tsv` 224, `passB.tsv` 224. `reconcile_blind.py`: **211 of 224 agreed (0.94)**, 13
splits (T89/T45 x4, T60/T86 x3, T36/T98, T50/T92, T64/T13, T90/T84, two X_NEW vs sheet), all settled by one value-blind Sonnet
adjudicator (`adjudicate_in.tsv` -> `adjudicate_out.tsv`, 2 H, 11 M). Final `f184r/passC.tsv`: **224 signs, 0 '?', 21 off-sheet**
(X_NEW 19 -- t-shapes, "3", "6", "7", a boxed/barred sign, the struck A+V pair at the start of L07 and end of L12 -- X_A 1,
X_EQ 1, X_S 1). Lines: L01 12, L02 39, L03 37, L04 23, L07 23, L08 42, L09 22, L12 26.

**Control (rule 3)**, `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py f184r/passC.tsv --map sign_id_map_1572_fit.json
--err 0.12` (printed key + T42=m; corpus it16dip; 200 value-shuffled keys; power control 20 it16dip windows of the same
passage lengths at 12% injected error, twice the measured 6% disagreement):

| sequence | signs / letters | real key | shuffles mean / max | z | rank of 201 | power control, err 0.12 |
|---|---|---|---|---|---|---|
| **f.184r passC, seed 1** | 224 / 225 | **-1.016** | -1.575 / -1.264 | **4.15** | **1** | 17/20, z median 3.28 min 1.86 |
| f.184r passC, seeds 2 and 3 | 224 / 225 | -1.016 | -1.566 / -1.276; -1.578 / -1.216 | 3.89; 3.64 | 1; 1 | -- |

T42 does not occur in this run, so the printed key and the fitted key decode it identically. The real key clears the best of
200 shuffles by 0.20-0.25 at every seed; at 224 signs the test finds a true key 17 times in 20, so the hit is informative.

**Reading** (`tools/decode_key.py ciphers/nevers-birago-fr3251-1572`, job built by `harvest/build_decode_inputs.py f184r`;
`--check` exit 0, "reading up to date"). No exceptions file. Grades (rule 4): **224 tokens: H 0, C 0, S 190, M 13, I 0, U 21** --
a cryptanalytic result (S = the published key's value where both readers agreed, backed by the rank-1 control; M = settled
by the adjudicator; U = off-sheet signs, unkeyed).

    f184r L01 | d[che]sernunnuti
    f184r L02 | a[qual][che]pranicaconilcontedi·il[che]simo[per]a[che]ordars
    f184r L03 | ocon·ousegli·ansailiarticolisapenci[che]i
    f184r L04 | lmandstodaluia·e[per]ge·eno
    f184r L07 | ··se·aieensaranoahecose
    f184r L08 | de···asi·euerso··hauensoluiil·oci·cenchio·
    f184r L09 | oltoabi·ea·ortificarsi
    f184r L12 | [quello]ilcapitanosipionecarego··

This worker's word breaks (not a second transcription): "...che s[a]r[a]nno venuti a qual[che] pra[t]ica con il conte di · il che
si mo[stra?] per a che ord[in]ars[i?] ... con ... li articoli ... mand[a]to da lui ... [f]ortificarsi ... quello il capitano
Scipione Carego[?]". "Scipione" and "il capitano" are content words; the name is not checked against the letter's prose here.
Visible look-alike slips (n for t in "pranica", "sernunnuti") are of the kind logged on no.87.

**Judge** (secondary signal, `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f184r/reading_f184r_letters.txt`):

    FAIL language: score=-1.096, null_p99=-1.648, real_p05=-0.941, real_median=-0.829, mode=both, N=225
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

Shuffled-target control (`harvest/shuffled_judge.py`, fitted map, 20 seeds): **0 of 20 PASS**, mean -1.611, min -1.763, max
-1.525. The judge discriminates at this N; the FAIL sits between the shuffled decodes and real_p05, the near-miss shape of the
sibling runs with about 9% unkeyed signs.

**What this settles.** The 1572 key reads no.90's f.184r runs: rank 1 of 201 shuffled keys (z 3.6-4.2, power 17/20). No prior
decipherment of these runs was found on canvases 188-190; that search is a page look, not a verifier's search (rule 10). The
f.184v foot, f.185r and f.185v runs remain unread. Flagged in ROOM for a separate verifier.

Requests: gallica.bnf.fr 3 (info.json canvas 188; canvas 188 at 2500 px; the native cipher region), 1.5 s+ apart, no challenge.
Vision calls 3 (two blind passes, one adjudication) plus this worker's own looks (overview, crop checks). No credentials.

## BIRAGO-SMALL: no.87 tiles labelled T50, T98, T52, T46 re-read by shape against the clerk-sheet error map (2 Oct 2026, account 2 for the account-3 orchestrator)

Brief `.claude/briefs/runs/2026-10-02-acct3-birago-small.md`, item 2. Disk only: 0 requests, 0 subagents. No class, no novelty
wording. Status stays `partial`. Nothing here changes the committed `ciphertext_f178*.tsv`/`f179r.tsv` or any firm count: the
proposed labels are in `harvest/lookalike_87/reread.tsv`, and a verifier applies them or not.

**Instrument, and how it departs from the brief.** The brief named `tools/lookalike_pass.py packet`. The packet flags tiles from a
two-reader agreement file. Most of these 41 tiles are ones where both readers agreed (the error map's conflicts are mostly
both-agree, which LESSONS.md "Look-alike pass" says the 2-of-3 rule never reaches). So the tiles were taken from the error map
instead: every no.87 token carrying one of the four labels, joined to `harvest/align87/align_real.tsv` (`lookalike_87/tiles.tsv`, 42
rows, 41 aligned). For each tile, a context window of about +-3 signs was cut from the committed line crops (`lookalike_87/windows.py`;
the position is estimated from pos/line length, and segments overlap, so a window can show a sign twice). The windows were
montaged per label (`lookalike_87/t50c_windows.jpg` with the T50/T92/T57/T98/T18/T63/T36/T52/T19/T55 sheet cells, ids only;
`t98_windows.jpg`; `t52_windows.jpg`). This worker read them in three vision reads. **The read was not value-blind**: the
sheet value of each tile was known, because the error map is the crib by brief. The evidence below is shape alone, and a verifier
should repeat it value-blind before anything is applied.

**T50 (8 tiles): a reader-label error.** The seven tiles the sheet reads s (f178v L01.23, L03.4, L04.4, L05.25, L07.29, L08.10,
L10.5; all conf M in the transcription) are one shape: a curled "Ce", an omega with a c-hook lead stroke and no tall tail. The one
tile the sheet reads c (L20.7, conf H) is omega with the tall S-tail, exactly the T50 sheet cell. The readers filed an off-sheet
"Ce" sign under T50. Proposed label X_CE; its value s rests on the sheet (C, 7/7 on no.87). This is why T50 = s failed to transfer
(NEVBIR-87ALIGN: "per conto", "domestico", "confusion" in nos.71/86/90 need c). T50 = c, the printed value, stands. The variant
key's T50 row (`harvest/key_1572_clerkvar.tsv`) is wrong as a sign-level rule.
**T46 (4 tiles): three are not the printed "86".** f178r L03.22 is "86" (turino, as printed). f178v L15.24-25 is "88" (two 8s;
the sheet has c + "atholici" there, i.e. a word sign or pair for "cattolici" -- image question), and L19.22 is a single 8 (sheet
"re"). Proposed label X_8 (M), value unset.
**T52 (11 tiles): not a reader error.** The eta-with-tail shape is the same on the tiles the sheet reads o (7) and the ones it
reads i (L04.21, L04.28, L09.10). The split is the C-vs-printed key conflict already in `keys/key_1572_clerk.tsv` (rule 4), not a
label question. One exception: L13.27 is "m" followed by a rho-like tail, not the eta shape (unsettled, `?`).
**T98 (17 aligned tiles): unsettled.** The seven tiles the sheet reads d look like circle-on-stem with little or no ascender
above the bowl, nearer the T18 (d) cell. The s tiles show the full stroke through the bowl of the T98 cell. At these crops this
is a tendency (M), not a settlement. The error map's T18/T98 pair (18 splits in the 1572 confusion table) fits it. It goes to
the owner's sorter, not relabelled here.

**True error on these tiles against the clerk sheet** (sheet value vs the label's printed value; 40 tiles with a sheet value,
the f179r L03.2 T98 is unaligned):

| label | tiles | wrong before | wrong after the proposed labels | note |
|---|---|---|---|---|
| T50 | 8 | 7 | 0 | after = 7 X_CE at the sheet's s; the label split is by shape, the s value by the sheet (circular for the value, not for the label) |
| T46 | 4 | 3 | 0 (3 now U, unvalued) | X_8 unvalued |
| T52 | 11 | 7 (printed i vs sheet o) | 7 | a key conflict, not a reader error; unchanged |
| T98 | 17 | 8 (7 d, 1 c) | 8 | unsettled; tendency toward T18 on the 7 d tiles |
| all | 40 | **25** | **15** (3 U) | of the 15, 7 are the T52 key conflict |

**Decision asked by the brief.** T50 = s is a reader-label error on no.87, not a key change. T50 stays c, and the "Ce" tiles are
a different sign. T95 = l (8/8) is still the open key conflict to test in other letters. No firm count changes. Next step for
a verifier (about $2): re-read value-blind the 8 T50 tiles and 3 T46 tiles from `reread.tsv` against these windows, and check
whether any "Ce" tile in nos.71/86/90 sits under a T50 or T92 label there. Next for the owner's sorter: the T98/T18 tiles, added
to `sorter/focus.tsv`.

## NO87-LABELS: the ruled no.87 labels applied after a second value-blind re-read (3 Oct 2026, for the account-3 orchestrator)

Brief `.claude/briefs/runs/2026-10-03-acct3-no87-labels.md`. Disk only: 0 requests, 1 subagent vision call (Sonnet, no repo
context). No class, no novelty wording, no firm count changed. Status stays `partial`.

**Blind re-read.** All 42 no.87 tiles labelled T50/T46/T98/T52 (`harvest/lookalike_87/tiles.tsv`) were cut as context windows
and shuffled (seed 1003) into panels P01-P42 with ids only (`harvest/lookalike_87/no87_labels/mk.py`, regenerates `blind_*.jpg`,
`candidates.png`, `key.tsv`, `neighbours.tsv`). The reader saw the panels, the target's neighbour ids (target as `[?]`), the
blind sheet, and a candidate-only sheet of 14 cells (T50 T92 T96 T46 T11 T15 T98 T18 T36 T45 T52 T13 T64 T38), and never a
label, value or sheet word for any tile; it was a fresh subagent that had read nothing else, so unlike VERIFY-BIRAGO-SMALL it did
not know the class counts to expect. Its read is `blind_read.tsv`; it was joined to `key.tsv` only afterwards.

| tiles | ruling (AUDIT.md, VERIFY-BIRAGO-SMALL) | blind re-read | applied |
|---|---|---|---|
| f178v L01.23 L03.4 L04.4 L05.25 L07.29 L08.10 L10.5 (T50, sheet s) | X_CE, s at C | 7/7 OFF "omega with c-hook lead, no tall tail" | **yes**: exceptions_f178v.tsv, value s |
| f178v L20.7 (T50, sheet c) | stays T50 = c | T50 "omega with tall S-like tail" | nothing to apply |
| f178r L03.22 (T46) | stays 86 | T46 "86" | nothing to apply |
| f178v L19.22 (T46, sheet re) | X_8, U | OFF "single 8" | **yes**: value ?, U |
| f178v L15.24-25 (T46 T46, sheet c / atholici) | one token X_88 | two panels, each OFF "single 8" | **no**: the ruling (one group) and the read (two separate 8s) disagree on the token count; left as T46 for the owner's sorter or a verifier |
| T98 (19 tiles) | not ruled | all 19 read T18, the 11 sheet-s tiles as well as the 7 sheet-d | no: no ruling, and the read does not separate s from d tiles, so it is non-discriminating for this pair at these crops (the bMAT2 shape) |
| T52 (11 tiles) | not ruled (key conflict) | 9 T52 (o and i tiles alike), L13.27 OFF "m-like with descending tail" (as BIRAGO-SMALL's ?), f178r L03.28 unseen | no |

The 8 applied rows went in by `exceptions` (basis named in each row); `ciphertext_f178v.tsv` and the keys are unchanged. Because
these tiles carry conf M, decode_key grades the 7 s values M (not C); the X_8 is U. `decode_key.py --check`: reading up to date.

**True error on no.87 against the clerk sheet** (`lookalike_87/no87_labels/true_error.py`: decoded token value vs
`align87/align_real.tsv` plain_chunk, 843 aligned tokens; the sheet is the known answer):

| | wrong | unvalued (U) | true error | wrong + U |
|---|---|---|---|---|
| before (committed 5517fc38) | 72 | 19 | 0.0854 | 0.1079 |
| after the 8 rows | 64 | 20 | 0.0759 | 0.0996 |

The 7 X_CE tiles move wrong -> right (the value comes from the sheet itself, so this part is circular for the value and not for
the label split); L19.22 moves wrong -> U. Judge (`specs/nevers-birago-fr3251-1572.json`, letters of f.178r+v+f.179r): before FAIL
-1.046 (real_p05 -0.902, null_p99 -1.781, N 926), after FAIL -1.044 (real_p05 -0.904, null_p99 -1.790, N 920): unmoved.
`reading_no87_letters.txt` regenerated.

**Follow-up (true error dropped).** The same shapes can hide under the same labels in the other letters: 26 tiles in
`lookalike_87/no87_labels/followup_71_86_90.tsv` -- no.71 f.139v T50 x3; no.86 T50 x8 and T46 x1 (f174r L04.1, already the
'85' fix in AUDIT.md); no.90 T50 x10 and T46 x4. Second tier, not listed: T92 (no.86 x13, no.90 x41), since the earlier note
named T92 as the other label a "Ce" could sit under. Next: the same value-blind panel read on those 26 tiles (one vision call,
~$1, disk only); a tile read as the curled Ce gets value s by exception, a tall-tailed one stays c.

## NO87-FOLLOW: the no.87 curled-Ce check carried to nos.71/86/90 (3 Oct 2026, for the account-3 orchestrator)

Brief `.claude/briefs/runs/2026-10-03-acct3-no87-follow.md`. Disk only: 0 requests, 1 subagent vision call (Sonnet, no repo
context, value-blind). No class, no novelty wording, no firm count changed. Status stays `partial`.

**Panels.** `harvest/lookalike_87/no87_labels/mk_follow.py` (seed 1004, same protocol as `mk.py`: shuffled panels Q01-Q19 with
ids only, neighbour ids with the target as `[?]`, the same 14-cell candidate-only sheet and the blind sheet; window +-5 signs,
capped at 450 px each side). 19 of the 26 tiles in `followup_71_86_90.tsv` have crops on disk; the 7 on no.90 f.185r L10-L22
(T50 x3, T46 x4) do not (`f185r2/` crops are gitignored; `f185r2/REGEN.sh` re-fetches them, one Gallica request), listed in
`follow_skipped.tsv`. Read: `follow_blind_read.tsv`, joined to `follow_key.tsv` only afterwards. The panel jpgs are not
committed (regenerate with the script).

| tiles | blind read | applied |
|---|---|---|
| 16 T50 tiles located (no.71 f.139v x3; no.86 x8 incl. f.175v V02; no.90 f.184r/f.184v/f.185r L06 x5) | 16/16 T50 "omega with S-tail" (14 H, 2 M); none OFF, none T92 | nothing: the read agrees with the T50 = c label everywhere |
| no.90 f184r L12.19 (T50), no.86 f174r L04.1 (T46) | not located: the window showed italic prose (the pos-to-x estimate fails on these lines) | nothing |
| 7 no.90 f.185r tiles | not read (crops not on disk) | nothing |

**Result.** No "Ce" sign was found under a T50 label outside no.87 in the 16 tiles read: the no.87 relabel does not carry to
nos.71/86/90 on this read, and NEVBIR-87ALIGN's finding that these letters need T50 = c ("per conto", "domestico",
"confusion") is consistent with it. No exceptions rows written; `decode_key.py --check`: reading up to date, no token's value or
grade moved, so each letter's S/M/U stands as committed -- no.71 f.139v S 116 / M 24 / U 21; no.86 S 629 / M 76 / U 54; no.90
S 731 / M 124 / U 111 -- and no letter's control input changed (byte-identical ciphertext and key), so the controls were not
re-run. No new fragment became readable.
**Limit.** The call carried no hidden positive (a no.87 X_CE tile mixed in), so a reader insensitive to the curl would give
the same 16/16. The descriptions (each names a tall S-tail; the no.87 reader named "no tall tail" on the Ce tiles) argue against
that, but it is not tested. Next, if wanted: one call on the 7 f.185r tiles (after `f185r2/REGEN.sh`, 1 Gallica request) plus
Q04/Q06 re-windowed by hand, with 3 no.87 X_CE tiles and 3 T50 tiles hidden among them as known answers, ~$1.

## Remaining gaps (LIKELY-3, 2 Oct 2026; updated GAPS-nevers-birago 04:3x UTC and GAPS3-nevers-birago 05:3x UTC and GAPS4-nevers-birago 06:3x UTC, 2 Oct 2026)
Read so far: all 853 signs of no.87's cipher passage (f.178r foot 3 lines + f.178v 23 + f.179r head 3; joined under the fitted key rank 1/201 z 4.60, power 20/20; judge FAIL -1.046 vs real_p05 -0.902; the clerk's clear decipherment of the passage, found legible on canvas 182 (GAPS4, 2 Oct 2026 06:3x UTC, section above), matches the decode on 0.837 of letters vs 0.114 max for shuffled keys), control-backed; 0 of the 7 target letters ff.138-184. Closed by GAPS4 (2 Oct 2026): the f.178r foot / f.179r head gap (done, 97 + 89 signs, agreement 0.88 / 0.89) and the tipped-in-decipherment gap (resolved: it is the laid-in sheet photographed legibly on canvas 182, read into harvest/f179r_sheet/decipherment_sheet.tsv; canvas 183 shows its blank back; the BnF reproduction batch, REQUEST.md / ASKS row 78, no longer needs it for this item)
- f.184 no.90 -- all its cipher now read (966 signs; NEVBIR-185B, 2 Oct 2026, section at the end): rank 1/201 at 3 seeds, z 4.49-4.59, power 20/20 at err 0.12; judge FAIL -1.069 (shuffled 0/20 PASS); remaining: 19 tiles NEVBIR-185 coded X_NEW that match the sheet's T83 (r) - blocker: open-codes; fit-aware control gain rank 6-9/201 only, grade M; next: confirm the 19 tiles are T83 by a value-blind look-alike pass or the owner's sign sorter (f185r/passC_rest90_ae.tsv), then relabel and re-run decode_key, disk + 1 vision call, ~$1; and a separate verifier pass on the f.184v-f.185v portion (rule 10), ~$3
- f.168r-v no.85 (two runs, 121 signs, NEVBIR-168, 2 Oct 2026) - blocker: too-short; printed 1572 key + T42=m rank 36/201 (z 1.00; seeds 2-3 rank 31, 41), power control 15/20 at err 0.13 (z min 0.22): a miss the right key also gives in about a quarter of windows at this length, so not licensed as a reading and too weak to call a negative; 11 off-sheet signs; pooled test run (NEVBIR-POOL, 2 Oct 2026, section at the end): pool of f.144r + f.168 + f.174r rank 1-4/201, power 15/20 at err 0.15, not licensed, and f.168 is the run that drags the pool down (leave-one-out); next: the off-sheet value-fit shared with f.139v (disk only, ~$1); NEVBIR-LOOKALIKE (2 Oct 2026, section below): look-alike pass lowered the residual reader disagreement to 0.074, printed key + T42=m on passD rank 13-15/201 (z 1.43-1.55) against power 19/20 at 0.074 (z min 2.00) and 14/20 at 0.13: not licensed, not a negative; 7 of the 9 unsettled tiles are one question (T24, the readers, or T83, the look-alike reader; the pre-registered secondary sequence with T83 there ranks 1/201 z 3.49, a pointer only); next: the owner settles the 7 T24/T83 tiles in the sign sorter (sorter/README.md; waiting-on the owner, never blocking), then re-run decode_control.py on the settled sequence, disk only, ~$0.5; NEVBIR-ERRTRUE (3 Oct 2026, section at the end): at the benchmarked err_true power clears the pre-registered gate (17/20 at 0.081, 16/20 at 0.115 and 0.121) and the real key ranks 31-41 (z 0.91-1.00, below every power window's z): a control-backed negative for the printed key on the committed passC read at err_true, marginal at 1.5x (post-hoc seeds 44/60), not robust to counting the 11 off-sheet signs as error (11/20 at 0.17), and contradicted by TX-DECODE's lattice (rank 1/201): treated as a transcription question, not a key exclusion; next: the T24/T83 sorter settlement above, then this same test on the settled sequence; TXD-HOLDOUT (3 Oct 2026, harvest/tx_decode/holdout/RESULTS.md): the TX-DECODE lattice lam-4 rank 1/201 survives the pre-registered held-out control (held-out no.87 lines choose lam 4, 36 vs 37 wrong of 521; printed key beats all 218 same-design wrong keys, z 6.78; rank 1 at lam 1-6), but the wrong-key gate also passes on 4 of 5 position-shuffled f.168 lattices, so it adds little beyond the value-shuffle control; still not a reading (S at best); A1-BIR-EYE (3 Oct 2026, harvest/tx_decode/eye/RESULTS.md): blind eye check PASS, 7/11 changed positions picked key-implied vs 1/11 decoy swaps (p 0.0004); next: a separate verifier on the 5 S candidates (eye/score.json) against the crops, ~$2
- f.144r no.73 (90 signs, NEVBIR-144, 2 Oct 2026) - blocker: too-short; real key rank 4/201 (z 1.77), but the power control finds the right key only 4/20 at the measured 0.24 reader error and 9/20 at 0.12 (20/20 at 0): a non-test at this N and error, not a negative; pooled test run (NEVBIR-POOL, 2 Oct 2026): not licensed at 296 signs (rank 1-4/201, power 5/20 at this run's 0.24 error); next: lower the reader error with the clerk-sheet error map (gap below), ~$2; NEVBIR-LOOKALIKE (2 Oct 2026, section below): look-alike pass lowered the residual reader disagreement from 0.24 to 0.044 (4 tiles unsettled); printed key + T42=m on passD rank 1, 2, 1 of 201 (z 2.27-2.44), power 18/20 at 0.044 (z min 1.78) but 4/20 at the old 0.24: control-backed only if the 2-of-3 residual is accepted as the reader error; next: a verifier pass on the passD reading and the 4 unsettled tiles (sorter focus box), ~$3; NEVBIR-ERRTRUE (3 Oct 2026, section at the end): power re-run at the benchmarked err_true (no.87, 0.081) still fails, 14/20 at 0.081, 8-9/20 at 0.115-0.121 (pre-registered gate 16/20), real key rank 3-6: still too-short on the passC read at the true error; TXD-HOLDOUT (3 Oct 2026, harvest/tx_decode/holdout/RESULTS.md): the TX-DECODE lam-4 rank 1/201 survives the pre-registered held-out control by its stated rule (held-out lines choose lam 4 by one sign; wrong-key gate 0 of 218, z 4.64), but rank 1 holds only at lam 2-4 (rank 2 at lam 1 and 6, 12 at lam 8; "tuned-only" by the pre-stated label) -- the weakest of the three; A1-BIR-EYE (3 Oct 2026, harvest/tx_decode/eye/RESULTS.md): blind eye check PASS, 5/12 key-implied vs 0/12 decoy swaps (p 0.001), the image backs fewer than half the changes; next: a separate verifier on the 4 S candidates (eye/score.json) against the crops, ~$2
- no.71 cipher passage, f.139v foot (161 signs, NEVBIR-138, 2 Oct 2026) - blocker: open-codes; 21 off-sheet signs unkeyed (X_NEW "4", "7", square-with-dot, "t", raised "m" abbreviation and others), the power control is weak at this length (10/20 at err 0.15) and the judge FAILs (-1.159 vs real_p05 -0.955); value-fit of the recurring off-sheet signs run on the pooled 1572 letters (NEVBIR-OFFSHEET, 2 Oct 2026, section at the end): the method failed its own known-answer check on no.87 (untested-by-this-tool, the n-gram fit on note-derived shape classes); the clerk-sheet alignment ran (NEVBIR-87ALIGN, 2 Oct 2026, section at the end): per-tile values for no.87's 25 off-sheet tiles only, the t-shape class is at least two signs, and its transfer variant (T42 m, T95 l, T50 s) changes 4 no.71 tokens and makes none readable (judge -1.159 -> -1.137); next: the owner's sign sorter for the f.139v off-sheet tiles, with the no.87 per-tile C values as labelled examples (sorter/, waiting-on the owner, never blocking)
- f.152r no.77 cipher run (97 signs) read under the 1572 key by NEVBIR-152 (2 Oct 2026, section above): rank 1/201 z 3.1, slip agreement 0.61; the rest of no.77 past f.152v - blocker: not-attempted; f.152v plain per PREMISE-NEVBIR, f.153r onward not opened; next: open canvas 155-156 at 1200 px for a further cipher run (1-2 requests), and a verifier pass on the f.151v slip (whose hand, prior decipherment of this run), ~$3
- the q homophone, T88 and the off-sheet signs (now 25 over 853) - blocker: open-codes; GAPS4 (2 Oct 2026): the t-shaped X_NEW reads m four times against the clerk sheet (grade C, exceptions files) and is probably the printed T17; the fit T42 = m is confirmed by the sheet (0.837 vs 0.816 for the printed key); the value-fit ran (GAPS3, 2 Oct 2026 05:3x UTC, section above): T42 g -> m (S, seven m-words against one g-word; judge -1.074 -> -1.032, z 4.60 -> 4.84), T70 confirmed g, T88 (3 occurrences) undecided (q scores worst, no two-word support; the one q-word 'guecta' also carries a c/s look-alike), X_NEW (7, all at word boundaries) invisible to a letter fit, X_EQ 2 too few; NEVBIR-OFFSHEET (2 Oct 2026, section at the end): the pooled value-fit of 17 note-derived shape classes over nos.71/86/87/90 (2,739 signs) is untested-by-this-tool -- its pre-registered known-answer check on no.87 could not run (no accepted class occurs there) and the control-beating classes read the sheet right on 4 of 10 occurrences; T17 (m) still never occurs -- a sheet-cell or clerk question for an image check; the clerk-sheet alignment ran (NEVBIR-87ALIGN, 2 Oct 2026, section at the end): keys/key_1572_clerk.tsv, C-grade, 0.896 agreement vs shuffled-sheet max 0.376; T42 = m confirmed at C; T95 l 8/8 and T50 s 7/8 conflict with the printed table, T50 = s refuted outside no.87; T88 still undecided (e 2 / q 2, M); the look-alike shape read ran (BIRAGO-SMALL, 2 Oct 2026, section above): T50 = s is a reader-label error (seven "Ce" tiles filed under T50; T50 stays c), three T46 tiles are "8"/"88" not "86", T52 is a key conflict not a label error, T98/T18 a tendency only; true error on the 40 tiles 25 -> 15 if the proposed labels are applied (not applied); next: a value-blind verifier re-read of harvest/lookalike_87/reread.tsv (~$2), then the T98/T18 tiles in the owner's sorter
- no.82 (f.162) cipher, one line on canvas 164 right (25 signs, NEVBIR-162, 2 Oct 2026): run 1 read under the 1572 key, rank 1/201 z 2.6-2.9 (power 2-10/20), 0.74 agreement with a later-hand decipherment slip pasted on f.161v (shuffled max 0.15); run 2 is a 4-sign name code ('M.' + digits 4 7 + u) outside the printed table - blocker: no-key-material for the code beyond the slip's own 'M. di Bellaguarda'; verifier pass done (VERIFY-NEVBIR-82, 2 Oct 2026: N0, the slip is a prior decipherment of the whole line; hand unsettled, same hand as the f.151v slip by eye); next: add code 47 = Bellaguarda to the key at grade C with the slip's provenance beside it (M outside this letter until a second attestation), disk only, ~$1

- no.86 (27 Aug 1572, ff.170r-177r; NEVBIR-170, 2 Oct 2026, section below): its f.174r foot run (85 signs) - blocker: too-short; real key rank 2-4/201 (z 1.8-2.1), power 11/20 at err 0.10 (20/20 at err 0): not rank 1, a non-test at this length, not a negative; the letter's main cipher is the FULL cipher page f.174v (canvas 178 left, ~22 lines, ~600 signs, not yet read) plus f.175r head (1 line) and f.175v (canvas 179 left, ~3 lines); next: read f.174v in two half-leaf jobs (same pipeline, ~$5 each, power 20/20 at that length) and pool with f.174r in one 200-shuffle test (disk only); the short-run pool with f.144r and f.168 (NEVBIR-POOL, 2 Oct 2026) did not license it; f.174v lines 1-11 (285 signs, NEVBIR-174V-A, 2 Oct 2026, section below) read under the printed 1572 key + T42=m: rank 1/201 at 3 seeds (z 3.36-3.49), power 20/20 at err 0.10 and 8/20 at err 0.20 (blind agreement 0.80 before adjudication), 18 off-sheet signs unkeyed (open-codes); next: f.174v lines 12-end + f.175r head + f.175v (NEVBIR-174V-B), then the joint 200-shuffle test of all no.86 cipher (f.174r + f.174v + f.175), disk only, ~$1; f.174v lines 12-22 + f.175r head + f.175v (389 signs, NEVBIR-174V-B, 2 Oct 2026, section below): rank 1/201 at 3 seeds (z 3.42-3.74), power 20/20 at err 0.10; whole no.86 (759 signs) rank 1/201 at 3 seeds (z 3.56-3.83), power 13/20 at err 0.23; judge FAIL -1.161 (shuffled 0/10 PASS); 54 unkeyed signs over the letter (open-codes: lone '8' shapes, X_K, X_A, '?'); verifier pass done (VERIFY-NEVBIR-86, 2 Oct 2026, AUDIT.md section no.86: N3, key published, re-derivation exact, rank 1/201 also at seeds 7 and 11; T15/T11 = the printed digit codes 89/85, confirmed on the crops; '88' on half B L02 is not in the printed table, stays U); next: correct f.174r L04 pos 1-2, which reads T46 + X_S but the crop shows the digit pair '85' = carmagnola (T11): fix harvest/f174r/passC.tsv, re-run join_no86.py, build_decode_inputs.py and decode_key.py --check (disk only, ~$0.5); for N4, vol. 2 of the 1665 Mémoires de Nevers (vol. 1 searched inside on Gallica, no hit)
## Escalation (2 Oct 2026)
- [x] siblings: no.87 is itself the key's own witness leaf and was read first; the six other 1572 letters are the next units
- [x] clear-pages: the clerk's clear decipherment of the whole passage is the laid-in sheet on canvas 182, read by eye (GAPS4, 2 Oct 2026); f.178r and f.179r prose frames the passage
- [x] known-keys: the printed 1572 key applied, rank 1 of 201 shuffled keys, power 20/20
- [ ] print: print_check.py on 2-4 decoded phrases runs once the judge gate is met (whole passage -1.046 against -0.902 after GAPS4; the clerk sheet shows the residual is reader error on named sign pairs, so the sheet alignment then the look-alike pass is the next lift)
- [x] key-rebuild: one-sign value fits, not a rebuild -- run (GAPS3, 2 Oct 2026): T42 g -> m, T70 g, T88 and the off-sheet signs undecided at their counts; the key reads the leaf at rank 1/201 before and after
- [x] image-check: native regions, debug overlays checked by eye (f.178v right edge re-fetched once; f.179r left edge re-fetched once; f.178r re-cut on the slope after both readers reported clipped tails); the canvas 182/183 overviews re-read by eye, which found the decipherment sheet (GAPS4)
- [x] retry: one connection reset on the canvas-183 fetch retried once after a pause (GAPS4); the HTTP 500s were this worker's malformed URLs, not retried
Verdict: keep going: 4 internal gaps (no.86: all its cipher now read, f.174r + f.174v + f.175r/v, 759 signs rank 1/201 (NEVBIR-174V-A/B); its next step is the verifier pass) (f.152r run read by NEVBIR-152, 2 Oct 2026; its next step is the slip verifier pass and canvas 155-156); the value-fit of the off-sheet signs ran (NEVBIR-OFFSHEET, 2 Oct 2026: untested-by-this-tool, it failed its no.87 known-answer check); the clerk-sheet alignment ran (NEVBIR-87ALIGN, 2 Oct 2026: C-grade key keys/key_1572_clerk.tsv, control-backed; the transfer variant improves no other letter); the look-alike shape read on no.87 ran (BIRAGO-SMALL: T50 = s is a reader-label error, a "Ce" sign; labels proposed, not applied); the value-blind re-read and the agreed relabels on no.87 ran (NO87-LABELS, 3 Oct 2026: 8 exceptions rows, true error 0.0854 -> 0.0759); the same read on 19 of the 26 T50/T46 tiles of nos.71/86/90 ran (NO87-FOLLOW, 3 Oct 2026: 16/16 located T50 tiles read the tall-tailed T50, no Ce, nothing applied; 7 f.185r tiles need a crop re-fetch); cheapest next: f.144

## VERIFY-NEVBIR-1572 (2 Oct 2026, account 2): audit 1 -- see AUDIT.md

Verifier class **N0** for the no.87 passage (the period clear decipherment is laid in with the letter, and Tomokiyo
built the printed key from it): our reading is a re-decipherment and a calibration, not a reading of an unread text.
Key `published` (Tomokiyo) + one sign fitted by us. Rule 7 re-derivation reproduces exactly (H0 C4 S681 M146 I1 U21 of
853). Correction: the z 4.84 / S 532 and passage z 4.60 figures are fitted-key (T42 = m), not printed-key, figures.
The seven target letters ff.138-184 remain unread and unclassed.

## Premise check (PREMISE-NEVBIR, 2 Oct 2026)

Brief `.claude/briefs/runs/2026-10-02-acct3-premise-nevbir.md`, the adversarial Premise check of
`.claude/briefs/check-solved.md` run against all seven undeciphered 1572 letters before any first test. Search
only; no transcription, no decoding, no class, no novelty wording. Clock read with `date -u`: box 13:11-13:51 UTC.

**(a) the folder's own NOTES.md / REQUEST.md / AUDIT.md / harvest files.** Every mention of a decipherment, gloss,
interlinear, clear copy, "attached" or "dechiffrement" anywhere in this folder names no.87 only (f.178, out of
scope, N0 per AUDIT.md -- the laid-in sheet on canvas 182). Nothing in NOTES.md, REQUEST.md, AUDIT.md, HYPOTHESES.md
or harvest/ names a decipherment, gloss or attachment for f.138, f.144, f.152, f.160/162, f.168, f.168/170, or f.184
(grepped for each folio number). **Not found, for all seven.**

**(b) the other solvers' working files.** `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` cloned fresh
this session (not re-used from the 2 Oct verifier's clone). Bourdeau's `targets/birago/` (NOTES.md, profile.json,
find_digits.py) is entirely about **f.119** (no.63, 13 Nov 1571, the separate numeric-cipher paragraph), not any of
the seven target letters -- not solved there either ("Final state: not solved"). Bourdeau's own catalogue states it
directly: `SOLVED_CATALOGUE.md` row "Birago and Ceppo to Nevers (about 13 letters)" (checked by him 22 Sept 2026):
"In fr. 3251, ff. 27, 39, 82 and 178 carry contemporary decipherments... ff. 11, 21v, 35, 87, **138-174, 184** ...
have no published reading" -- naming six of our seven folios directly (138-174 spans 138/144/152/160or162/168/170or174
by his own folio citation) plus 184, as unread; this matches Tomokiyo's nevers.htm, which marks none of the seven
"(with decipherment)" (only no.87 is named as the source of the key). Bourdeau's `find_digits.py` sibling sweep
(16 Sept 2026) screened all 118 remaining openings of this same volume (views 88-207) for a *second numeric-cipher*
passage, not for a decipherment sheet; its five flagged candidates (views 99/100/107/109/156) were all confirmed
plain text on inspection (letters of 22 Sept 1571, a relation, a letter of 30 Aug 1571, one of 15 June 1572) -- none
is a decipherment of a 1572 Nevers-Birago letter, and the sweep was not built to find one (it looks for digit runs,
not prose glosses). `aaymeloglu/unsolved-ciphers`'s `catalogue/decode-catalog.csv` has Birago records only for
BnF fr.3619/3621/3623 (1591-92, already Decrypted per DECODE, a different cipher and decade); no fr.3251 record of
any kind. **Not found, for all seven**; Bourdeau's own catalogue line is the strongest and most explicit negative
available and is quoted in full above.

**(c) physical neighbours on Gallica.** Eye-checked (own looks, 1000px overviews, no vision-model calls, no
transcription) for six of the seven folios this session; f.138 reuses HARVEST-D2's existing fetch (canvas 139-140,
28 Sept 2026). None of the pages checked shows an interlinear gloss, a facing decipherment, or a loose/tipped-in
sheet over the *cipher* text, unlike no.87's canvas 182.

| folio | no. | canvas(es) checked this job | ink foliation confirmed | what's on the page(s) | gloss/sheet found? |
|---|---|---|---|---|---|
| f.138 | 71 | 139, 140 (HARVEST-D2, reused) | 138 | clear text only; letter's own cipher insertion not yet located (runs past f.139r) | not checked past f.139r (not this job's scope) |
| f.144 | 73 | 146, 147 | 144, 145 | f.144r: one short inline cipher/nomenclator run mid-prose; f.144v-145r: plain, letter ends 27 Mar 1572 [correction, A3V-VNB1, 4 Oct 2026: f.144v is not plain -- about 24 cipher signs over two lines near the top of the left page of canvas 147 ("Io no so quello [signs] ... [signs] possendone dir male con verità"), a second cipher run of no.73, untranscribed; AUDIT.md AUDIT 12] | **not found** |
| f.152 | 77 | 154, 155 | 152 (+ a second, fainter stamp, two numbering systems overlap from here on) | f.152r: one short inline cipher run mid-prose; f.152v: plain | not found on the pages checked; rest of letter not located [correction, VERIFY-NEVBIR-152, 2 Oct 2026: a decipherment slip IS pasted on canvas 154 left (f.151v), found by NEVBIR-152; AUDIT.md N0] |
| f.160/**162** | 82 | 163, 165, 166 | 161, 162 | f.160 itself belongs to a *different* item (no.81, Requesens to Birago, in Spanish) per the finding aid, not to no.82 -- see folio correction below; two small loose Italian-language slips tipped in nearby (canvas 165, canvas 166) are plain prose (an "avviso"-style note on troop movements, unrelated subject), **not** decipherments of the cipher letter | not found; no.82's own cipher line not located this job [correction, VERIFY-NEVBIR-82, 2 Oct 2026: no.82's cipher line AND a decipherment slip are on canvas 164 (right page and facing f.161v), which this check did not open; found by NEVBIR-162; AUDIT.md N0] |
| f.168 | 85 | 171 | 168 | f.168r: one short inline cipher run mid-prose | not found on the page checked; rest of letter not located [correction pointer, A3V-VNB1, 4 Oct 2026: the second run on f.168v head and the letter's end on f.168v were found by NEVBIR-168; no slip on canvases 171-172, rechecked by eye; AUDIT.md AUDIT 12] |
| f.174/**170** | 86 | 170, 173 | 167, 170 | f.170r: opening/address block only, no cipher visible yet on this one page | not found; cipher line (if on this leaf) not located this job |
| f.184 | 90 | 188, 189, 190 | 184, 185, 187 | f.184r: two dense lines of cipher signs; f.185: whole page of cipher signs (much denser than the other six); f.186v-187r: letter ends 2 Oct 1572, next item (Carolo Birago, 28 Nov) begins directly | **not found** -- nothing laid in between the end of no.90's cipher and the next item, unlike no.87 |

**Folio-citation correction (new this session, from the BnF's own finding aid, not from Tomokiyo).**
`archivesetmanuscrits.bnf.fr/ark:/12148/cc49712p` (fetched and read in full this job) gives, item by item: no.71 =
Fol.138, no.73 = Fol.144, no.77 = Fol.152, no.85 = Fol.168, no.87 = Fol.178, no.90 = Fol.184 -- all matching this
folder's existing table and Tomokiyo exactly -- **but no.82 = Fol.162 (not f.160) and no.86 = Fol.170 (not
f.174)**, confirmed by eye-checked ink foliation this job (canvas 166 right page stamped '162' ends a Birago
letter; canvas 173 right page stamped '170' opens one). Dates match Tomokiyo exactly for both (27 June and 27 Aug
1572), so these are the same two letters, just cited under different folio numbers by the two sources -- not a
second pair of letters. **This folder's own "Undeciphered" table above and `images/manifest.json`'s canvas notes
still read f.160 and f.174**; a worker doing deep work on no.82 or no.86 should eye-check the ink foliation
directly rather than trust either citation (the standing fr.20140/NEV-C1 lesson), and the table should be corrected
before a transcription brief is written against it. Not fixed in the table itself by this job (search-only brief;
the table is load-bearing for other in-flight work and a premise-check worker edits additively, not a structural
rewrite, without flagging it for the owning session first) -- flagged here and in images/manifest.json instead.

**(d) recipient-side print.** `ciphers/nevers-birago-fr3251-1572/AUDIT.md`'s search log (2 Oct 2026, this target's
own verifier, for no.87) already ran Google Books (`country=US`, keyed) and IA full-text for "Lodovico Birago"
Nevers 1572 broadly and found only modern Piedmont/Saluzzo local-history secondary works (Saluzzo e i suoi
valligiani, Dizionario Biografico degli Italiani, local chronicles), never a documentary edition of the
correspondence. Repeated this job with two more queries to extend coverage: IA fts `"Birago" "Nevers" "Saluzzo"`
(2,666 hits, the same handful of Piedmont-history volumes at the top, same as AUDIT.md's prior read, nothing new
opened); Google Books `"Mémoires de Nevers" Gomberville` (46 hits: Revue des questions historiques, Lettres de
Catherine de Médicis, Gomberville's own novels -- the 1665 Mémoires edition itself was not confirmed reachable or
its date-coverage checked this session). **Not found** on the queries run; **unreachable/not independently
confirmed** whether the 1665 Gomberville Mémoires de Nevers edition (focused, by its usual description, on
Nevers's League-era 1580s-90s papers rather than his 1570-72 correspondence as a young man) covers this early
period at all -- a worker with more budget should open that edition's table of contents or index directly rather
than rely on phrase search alone. No Italian/Savoyard documentary edition of Birago's Saluzzo governorship
correspondence was located or ruled out this session (not searched in Italian-language sources this job; English/
French-language IA and Google Books only).

**Verdict, per folio: all seven CLEAR TO TEST**, with the caveats above (f.138's, f.152's, f.168's and f.170's own
cipher passages are not yet located on the image, f.162's not even opened; (d) is not exhaustive). No decipherment,
gloss, or laid-in sheet was found for any of the seven on what was checked -- the no.87 precedent (a decipherment
physically filed with the letter) does not recur here on the pages sampled, and Bourdeau's own catalogue
independently confirms all seven as unread. Nothing here promotes any of the seven to CALIBRATION or FOUND-SOLVED.

Requests: gallica.bnf.fr 17 (see `images/manifest.json` "PREMISE-NEVBIR_2_Oct_2026_canvases"); be-api.us.archive.org
2; googleapis.com 2; archivesetmanuscrits.bnf.fr 1; github.com 2 clones (dbourdeau/cyphersolver, aaymeloglu/
unsolved-ciphers, both fresh, removed from scratch after use). No vision-model calls (own looks only, per brief).
No credentials. No AskUserQuestion.

## NEVBIR-144 (2 Oct 2026, account 2 worker for account 3's queue): f.144r no.73, first test -- a non-test at this length

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-letter.md`, WORK-QUEUE row NEVBIR-144. `tools/intake_gate_check.py`
exit 0 at 15:1x UTC; Premise check above: CLEAR TO TEST for f.144. No class, no novelty wording (rule 10). Status stays `partial`.

**Material.** Canvas 146, right page, ink foliation '144' (PREMISE-NEVBIR). The cipher is one run inside the prose
(27 Mar 1572 letter): from "...delle lre ultimamente mandate et" (L03), all of L04 except the prose "servandosi hora del
mese" (L04.1 / L04.2), all of L05, and L06 up to "tutti questi del stato del Re". Fetched once:
`python3 tools/iiif_lines.py --ark btv1b9060248g --canvas 146 --region 4350,800,3650,760 --out harvest/f144r --prefix f144r
--max-width 1250 --overlap 50 --only-lines 3,4,5,6` (debug overlay `harvest/f144r/f144r_lines_debug.jpg` checked by eye:
L03-L06 one band each), 2x reader copies by `harvest/make_2x.py --folio f144r` (gitignored). A first region at y 1450 missed
the run (it sat 5 lines higher than the 1000 px overview suggested); its source was deleted.

**Passes.** Two value-blind Sonnet readers, `harvest/f144r/blind_pass_brief_f144r.md` (the 1572 brief with the prose/cipher
layout added): `passA.tsv` 90 signs (18 X_NEW), `passB.tsv` 92 (11 X_NEW). `reconcile_blind.py`: **70 of 92 aligned
positions agree (0.76)**, lower than f.178v's 0.88 (this run carries struck-through signs, digits among the signs and
box/slash shapes off the sheet). A third value-blind reader settled the 20 splits (`adjudicate_in.tsv` -> `adjudicate_out.tsv`:
8 to A, 9 to B, 3 X_NEW, 0 NONE). Final `passC.tsv`: **90 signs, 0 '?', 14 X_NEW** (16% off-sheet: the digits 4, 7 and "16"
on L04.1/L05, crossed or struck-through signs, slashed boxes, a Y shape) -- far above no.87's 25 of 853.

**Control (rule 3)**, `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py f144r/passC.tsv --map sign_id_map_1572_fit.json
--corpus it16dip --shuffles 200` (the printed 1572 key + T42=m, the statistic of the f.178v runs):

| run | signs / letters | real key | shuffles mean / max | z | rank of 201 | power control (20 windows, same lengths) |
|---|---|---|---|---|---|---|
| seed 1, err 0.24 | 90 / 94 | -1.256 | -1.538 / -1.222 | 1.77 | 4 | **4/20 rank 1**, z median 1.12 min -2.20 |
| seed 2 | 90 / 94 | -1.256 | -1.525 / -1.180 | 1.79 | 6 | -- |
| seed 3 | 90 / 94 | -1.256 | -1.541 / -1.217 | 1.88 | 3 | -- |
| power only, err 0.12 | | | | | | 9/20, z median 2.00 |
| power only, err 0.00 | | | | | | 20/20, z median 3.57 min 2.13 |

**Verdict on the test: non-test, not a negative.** The real key sits above the shuffled mean (z about 1.8, rank 3-6 of 201)
but not at rank 1; at this letter's length (94 letters) and the measured reader error (0.24) the same test finds a
known-right key at rank 1 in only 4 of 20 windows, so rank 4 is what a right key with this error typically gives, and also
what a wrong one could give. Under rule 3 neither "the key reads f.144" nor "it does not" is licensed. Two limits act
together: length (power is 20/20 only at zero error) and the 14 off-sheet signs.

**Reading (unbacked).** `tools/decode_key.py` job `harvest/ciphertext_f144r.tsv` (built by `harvest/build_decode_inputs.py
f144r --seq f144r/passC.tsv`), `--check` exit 0. The tool prints tokens 90: S 40, M 36, U 14 -- those S grades are the key
file's own (backed on no.87), **not backed on this leaf**: per the brief no per-token grading is claimed here; read every
token as M at best. `harvest/reading_f144r.txt`:

    L03 [quello]··mprima·g | L04.1 eobtatnn··[per][qual] | L04.2 di[quello]ls··rosa· |
    L05 the·ircbodib··a[qual]cosmezodiseu·purato | L06 pmiudicedi·raginero·

**Judge** (secondary; `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f144r/reading_f144r_letters.txt`):

    FAIL language: score=-1.454, null_p99=-1.6, real_p05=-0.955, real_median=-0.828, mode=both, N=94
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

Next (in Remaining gaps): pool f.144r with the sibling letters' sequences in one joint shuffled-key test once they are read,
and/or lower the reader error (clerk-sheet error map, then a look-alike pass). Requests: gallica.bnf.fr 3 (info.json canvas
146; two regions, the first misplaced). Vision calls 3 (two blind passes, one adjudication). No other host. No credentials.
## NEVBIR-138 (2 Oct 2026, account 2): no.71 (f.138, 7 Jan/Feb 1572) cipher located on f.139v and read under the fitted 1572 key

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-letter.md`, WORK-QUEUE row NEVBIR-138. Intake gate exit 0 at 15:1x UTC.
Status stays `partial`. No class, no novelty wording (rule 10); a verifier is a separate session.

**Where the cipher is.** f.138r, f.138v and f.139r are prose (HARVEST-D2, re-checked by eye); bleed-through on f.139r showed
signs, and canvas 141 at 1200 px (`harvest/f138/c141_1200.jpg`) has them: **5 cipher lines at the foot of f.139v** (left page;
the right page, f.140r, opens the next letter). Native region `1850,3560,2550,700` of canvas 141 (8518x5847), cut by
`python3 tools/iiif_lines.py --ark btv1b9060248g --canvas 141 --region 1850,3560,2550,700 --out ciphers/nevers-birago-fr3251-1572/harvest/f139v --prefix f139v --max-width 1250 --overlap 50 --debug`
(6 bands found, pitch 106; band L01 is the prose line "manchera di giustitia; Questo e uno procedere ordinario di chi falle",
L02-L06 the cipher); 2x crops `harvest/make_2x.py --folio f139v --lines 2-6` (gitignored). Gallica requests 4 (1 HTTP 500 on
this worker's own doubled-ark URL, the slip LIKELY-3 and GAPS4 logged; not retried as such, re-issued with the bare id).

**Passes.** Two value-blind Sonnet readers (`blind_pass_brief_1572.md`, the 51-cell sheet, the 15 crops only): `f139v/passA.tsv`
162 signs, `passB.tsv` 160. `reconcile_blind.py`: **138 of 162 aligned agreed (0.85)**, 24 unsettled -- mostly the T60/T86 "#"
pair, T26/T76, and eps-like signs one reader put off-sheet. One value-blind adjudicator (`adjudicate_in.tsv` -> `adjudicate_out.tsv`):
8 to A, 13 to B, 3 to T97 (the loop-ampersand both readers had missed on the sheet). Reader A's lone L02 pos 2 sign (T57, L,
adjudicator also L) is dropped by the reconcile rule. Final `f139v/passC.tsv` **161 signs, 0 '?', 21 off-sheet**.

**Control (rule 3)**, `decode_control.py <seq> --map sign_id_map_1572_fit.json` (printed key + T42 = m), 200 value-shuffled keys:

| sequence | signs / letters | real key | shuffles mean / max | z | rank of 201 | power control |
|---|---|---|---|---|---|---|
| pass A alone | 162 / 152 | -1.017 | -1.573 / -1.191 | 3.33 | 1 | not run |
| pass B alone | 160 / 137 | -0.957 | -1.548 / -1.200 | 3.50 | 1 | not run |
| **passC final** | 161 / 146 | **-0.998** | -1.571 / -1.209 | **3.60** | **1** | 10/20 rank 1 at err 0.15, z median 2.66 min 1.27 |

The real key clears the best of 200 shuffles by 0.21 on every sequence. At ~160 signs the test's power is weak (a true key at
15% reader error ranks first only half the time), so a miss here would have been uninformative; the hit is the informative
direction, and the rank-1 margin is about the size no.87's 853-sign passage showed.

**Reading** (`tools/decode_key.py ciphers/nevers-birago-fr3251-1572`, job written by `harvest/build_decode_inputs.py f139v`;
`harvest/reading_f139v.txt`). Grades (rule 4): **161 tokens: H 0, C 0, S 116, M 24, I 0, U 21** -- a cryptanalytic result (S =
the published key's value where both readers agreed, backed by the rank-1 control; M = settled by the adjudicator or read at
M/L; U = off-sheet signs).

    L02 gc·dandarsiaconsultare[et]cercarn·      L03 ·oreea·iucoda···contraee·arnah·eco
    L04 ··ilcocinatoeinan··apcorpo···pf         L05 tu[per]ocio·luiuose[et]epoi·ipesi·anatur
    L06 h·guantoglifa[che]·selseruitoretengh

This worker's word breaks (not a second transcription): "... d'andarsi a consultare et cercar ... contra ... il Cocinato
[Coconato?] e ... per ocio [pero cio?] lui ... et poi ... quanto gli fa che ... sel servito ..." -- the Conte da Coconato is named in
the letter's clear prose (f.138r), so the name is content-consistent, not independent confirmation.

**Judge** (secondary signal, `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f139v/reading_f139v_letters.txt`):

    FAIL language: score=-1.159, null_p99=-1.662, real_p05=-0.955, real_median=-0.818, mode=both, N=146
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

Shuffled-target control (`harvest/shuffled_judge.py`, 10 seeds, 161 signs): 0 of 10 PASS, mean -1.802, max -1.545. The FAIL
sits between the shuffled decodes and real_p05, the same shape as no.87's near-miss with 13% unkeyed signs here.

**Date.** The endorsement "alli 7 di Gennaro 1572" (images/manifest.json) against Tomokiyo's 7 February: not settled here. Settled 3 Oct 2026: the docket belongs to a preceding attestation on f.137v, not to no.71 (see the Date note above); Tomokiyo's 7 February stands uncontradicted.

Next: value-fit of the recurring off-sheet signs (disk only), then a separate verifier on the f.139v reading (flagged in ROOM).

**Verifier (VERIFY-NEVBIR-139V, 2 Oct 2026): N3, key published; AUDIT.md section "no.71".** No decipherment slip on canvases
140-142 at native size. Every cipher line on f.139v runs into the gutter (canvas 141, x about 4310): line-end signs are
conditional on the image (rule 2). decode_key --check and the control (seeds 7, 11: z 3.60/3.57, rank 1/201) reproduce.
Requests: gallica.bnf.fr 4. Subagents: 3 Sonnet (2 passes + 1 adjudication).

## NEVBIR-170 (2 Oct 2026, account 2 for the account-3 orchestrator): no.86 (27 Aug 1572) located, f.174r run a non-test at 85 signs

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-letter.md`, WORK-QUEUE row NEVBIR-170. `tools/intake_gate_check.py
nevers-birago-fr3251-1572` exit 0 at 16:13 UTC. No class, no novelty wording (rule 10). Status stays `partial`.

**Where no.86 is and where its cipher is.** Whole openings viewed at 1000 px, both pages each (`harvest/f170/ov_c174.jpg` ..
`ov_c180.jpg`, plus `images/f170r_canvas173.jpg`): the letter opens on f.170r (canvas 173 right, ink '170'; the left page is
its address leaf "Al Ill.mo et Ecc.mo Sig.r ... Duca di Nevers") and closes on f.177r (canvas 180 right, ink '177') "Da
Saluzzo li 27 di Agosto 1572", signed Birago. Canvas = ink folio + 3 throughout (171->174, 172->175, 173->176, 174->177,
175->178, 176->179, 177->180, eye-checked at each step). ff.170r-173v are prose. The cipher is: **f.174r foot** (canvas 177
right, 3 full lines after the prose "...nel tempo", then two marks before the prose "et credo chel Volvera" -- this job);
**f.174v, a full page of cipher** (canvas 178 left, about 22 lines, about 600 signs; prose "al pnte, hebbi col mezo del
Facholo" before it); **f.175r head** (canvas 178 right, one line); **f.175v** (canvas 179 left, about 3 lines). This
corrects PREMISE-NEVBIR's row ("f.170r ... no cipher visible yet") and the folder table's "f.174": both citations are right
in a sense -- the letter is BnF Fol.170, its cipher is on ff.174-175.
**Facing pages and slips:** no pasted slip, squared paper, interlinear decipherment or gloss on any of the 16 pages of
canvases 173-180 at 1000 px (checked by eye this job; the f.151v slip shape was looked for). f.174r/f.174v at native
resolution only in the region fetched below; a native-resolution look at f.174v is the next reader's first step.

**Material.** Native region `4950,3380,2700,900` of canvas 177 fetched once
(`harvest/f170/src_ark_12148_btv1b9060248g_f177_4950_3380_2700_900.jpg`), crops cut from the local file:

    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f170/src_ark_12148_btv1b9060248g_f177_4950_3380_2700_900.jpg \
      --out ciphers/nevers-birago-fr3251-1572/harvest/f174r --prefix f174r --centres 145,262,412,548 --max-width 1300 --overlap 60 --debug

(a first cut at centres 150,262,365,470 put L03/L04 off their lines on the debug overlay and was deleted). 2x reader copies
`harvest/make_2x.py --folio f174r` (gitignored). Readers got L01-L03 s1-s3 and L04 s1 (10 crops).

**Passes.** Two value-blind Sonnet readers (`blind_pass_brief_1572.md`, the 51-cell sheet, crops only): `f174r/passA.tsv` 85,
`passB.tsv` 85. `reconcile_blind.py`: **78 of 86 aligned agreed (0.91)**; the splits were five T24/T29 and one T36/T27, plus
the two-mark L04 that the tool mis-aligned. A third value-blind reader (`adjudicate_in.tsv` -> `adjudicate_out.tsv`): T29 at
all five epsilon positions, T27, and L04 = an "8" shape (T46) then a small s/"5" mark (X_S); L04 was hand-set in `passC.tsv`
to those two rows. Final `f174r/passC.tsv` **85 signs, 0 '?', 7 off-sheet** (L03 pos 10-11 are a "4" and a "7": most likely
the clear numeral 47 inside the run -- the letter's prose on f.173r speaks of "47 soldati" -- and L04 "8 5," may likewise be a
clear numeral 85 rather than cipher; not settled here).

**Control (rule 3)**, `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py f174r/passC.tsv --map sign_id_map_1572_fit.json`
(printed key + T42=m; it16dip; 200 value-shuffled keys; err 0.10 ~ the measured 0.09 disagreement):

| sequence | signs / letters | real key | shuffles mean / max | z | rank of 201 | power control |
|---|---|---|---|---|---|---|
| **passC, seed 1** | 85 / 97 | **-1.266** | -1.592 / -1.249 | **2.07** | **4** | 11/20 at err 0.10 (z median 2.40); 20/20 at err 0 |
| passC, seeds 2, 3 | 85 / 97 | -1.266 | -1.610 / -1.155; -1.610 / -1.204 | 1.83; 1.94 | 3; 2 | -- |
| printed key (T42=g), seed 1 | 85 / 97 | -1.266 | -1.599 / -1.249 | 2.11 | 4 | -- |
| variant: L04 dropped as clear numeral | 83 / 91 | -1.272 | -1.595 / -1.249 | 2.03 | 4 (seeds 2, 3: 3, 3) | 15/20 at err 0.10 |

**Verdict on the test: non-test at this length, not a negative.** The real key sits well above the shuffled mean (z about 2)
but at rank 2-4, not 1; the same test finds a known-right key first in only 11-15 of 20 windows at this length and error, so
neither "the key reads f.174r" nor "it does not" is licensed (the NEVBIR-144 shape). No per-token grades are claimed: the
decode_key file below carries the key file's own S grades (backed on no.87, **not on this leaf**); read every token as M at best.

**Decode (unbacked).** `tools/decode_key.py` job `harvest/ciphertext_f174r.tsv` (`harvest/build_decode_inputs.py f174r`),
`--check` "reading up to date". `harvest/reading_f174r.txt`:

    f174r L01 | ·uc[et]pdouipensianui[per]cont·a
    f174r L02 | [et]io[che]eisiiingual[che]p[et]acica[et]fo[et]·i
    f174r L03 | st·etacon··[per]contosisgoun[et]nodi
    f174r L04 | [turino]·

(the L04 "[turino]" is T46's word value applied to the "8" shape; if L04 is the clear numeral 85, it is not cipher at all).

**Judge** (secondary; `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f174r/reading_f174r_letters.txt`):

    FAIL language: score=-1.24, null_p99=-1.616, real_p05=-0.96, real_median=-0.822, mode=both, N=97
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

Shuffled-target control (`harvest/shuffled_judge.py`, fitted map, 10 seeds): 0 of 10 PASS, mean -1.571, max -1.436.

**What this leaves.** No.86's main cipher (the full page f.174v, ~600 signs, plus f.175r head and f.175v) is unread; at that
length the power control is 20/20 (no.87's 853 signs), so it is the decisive unit for this letter, and f.174r pools with it.
Requests: gallica.bnf.fr 8 (7 overview canvases 174-180 at 1000 px, 1 native region), no errors. Subagents: 3 Sonnet (2 blind
passes, 1 adjudication). No credentials.
## NEVBIR-162 (2 Oct 2026, account 2 for the account-3 orchestrator): no.82 (f.162, 27 June 1572) cipher located on the opening leaf, read under the fitted 1572 key; a decipherment slip covers it

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-letter.md`, WORK-QUEUE row NEVBIR-162. `tools/intake_gate_check.py
nevers-birago-fr3251-1572` exit 0 at 16:13 UTC. Box 16:12-17:02 UTC. No class, no novelty wording (rule 10). Status stays `partial`.

**Material, whole canvases viewed first (1200 px: canvases 163, 164, 167; 165 and 166 from PREMISE-NEVBIR's 1000 px files).**
No.82 opens on **canvas 164, right page** (address "Ill.mo et Ecc.mo Sig.re", inner ink stamp "160", top-right stamp "16?" in
the second numbering -- the finding aid's "Fol. 162" and PREMISE-NEVBIR's "canvas 166 right page '162'" are the two systems
overlapping; the letter runs canvas 164 right -> 165 left -> 166 right, ending "Da Saluzzo li .. di Giugno 1572", signed
Lodovico Birago). Canvas 163 is two near-blank pages (bleed-through only); canvas 164's left page is the back of the previous
item (a Spanish address to Birago, no.81) and **carries a pasted slip in a later hand** (see below); canvas 165 left and 166
right are clear prose with no cipher seen at 1000 px; the slips on canvases 165/166 are an "avviso"-style postscript ("Doppo
scritto sono avisato ...", PREMISE-NEVBIR) photographed face up (165) and face down (166), not a decipherment. **The whole
cipher of no.82 is one line on canvas 164 right**: "ho scorto qua che [21 signs], quale e tutta cosa di [4 signs]". Native
region `4700,2200,3050,450` fetched once (`harvest/f162r/src_...f164_4700_2200_3050_450.jpg`); crops cut with:

    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f162r/src_ark_12148_btv1b9060248g_f164_4700_2200_3050_450.jpg \
      --out ciphers/nevers-birago-fr3251-1572/harvest/f162r --prefix f162r --centres 262 --max-width 1300 --overlap 60 --top-margin 40 --debug

(a first cut at `--centres 274` without `--top-margin` clipped the sign tops and was deleted). 1 line x 3 segments, debug overlay
checked by eye, `make_2x.py --folio f162r` for the reader crops.

**A decipherment of this run is pasted on the facing page (f.161v / canvas 164 left)**: a slip in a later, modern-looking hand
(`harvest/f162r/slip_f161v_c164_1400_3450_2100_800.jpg`, read by eye into `harvest/f162r/decipherment_slip.tsv`): "ho scorto
qua che [monsignore di S. Andre], / quale e tutta cosi di [M. di Bellaguarda],". The brackets are the slip writer's own, around
the deciphered parts. Same kind of object as the f.151v slip found by NEVBIR-152; who wrote it and when is not settled here.
**This is a prior decipherment of this item: a fact for the verifier (rule 10). The decode below is a known-answer check
against it, not a reading offered as ours.** PREMISE-NEVBIR (c) checked canvases 163/165/166 but not 164 and so missed it.

**Blind passes** (`blind_pass_brief_1572.md`, 51-cell `sign_sheet_blind_1572.png`, page note: prose page, runs L01.1 and L01.2).
Two value-blind Sonnet readers, `f162r/passA.tsv` and `passB.tsv`, 25 signs each. `reconcile_blind.py`: **22 of 25 agreed
(0.88)**; the 3 splits (L01.1 pos 2, L01.2 pos 1 and 4) are all struck-through signs, settled by a third value-blind Sonnet reader
(`f162r/adjudicate_out.tsv`: T81 M, T54 M, T49 L; it also confirms L01.1 pos 1-2 are cancelled by one long diagonal overstroke,
pos 3 "unsure"). Final `f162r/passC.tsv`: L01.1 21 signs, L01.2 4 signs; off-sheet: X_NEW at L01.1/3 (slashed box), X_EQ at
L01.1/19, and the two digit-like signs "4" "7" at L01.2/2-3.

**Control (rule 3)**, `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py f162r/passC.tsv --map sign_id_map_1572_fit.json
--err 0.12` (printed key + T42=m; corpus it16dip; 200 value-shuffled keys; T42 does not occur, so printed and fitted keys give
the same decode here):

| seed | signs / letters | real key | shuffles mean / max | z | rank of 201 | power control, err 0.12 |
|---|---|---|---|---|---|---|
| 1 | 25 / 21 | **-0.765** | -1.573 / -1.083 | 2.85 | **1** | 5/20, z median 1.13 |
| 2 | 25 / 21 | -0.765 | -1.570 / -0.983 | 2.55 | 1 | 10/20, z median 1.91 |
| 3 | 25 / 21 | -0.765 | -1.583 / -1.016 | 2.55 | 1 | 2/20, z median 0.82 |

Rank 1 of 201 at every seed, 0.22-0.32 above the best shuffle; but at 21 letters the n-gram test's own power is only 2-10 of 20,
so this control alone backs the run weakly. The known-answer check is the instrument that carries weight here.

**Known-answer check against the slip** (`align_sheet.py f162r/passC_L01_1.tsv --sheet f162r/slip_for_align.tsv --sheet-lines
L01-L01`, 200 value-shuffled keys): share of decoded letters in matched blocks >= 3: **fitted key 0.737**, shuffles mean 0.025-
0.031, max 0.120-0.148, **rank 1 of 201, z 18.7-18.9 (seeds 1, 2); printed key 0.737, z 18.7.**

    DECODE: db monsignobedisan_re      (pos 1-2 struck by the writer; _ = X_EQ)
    SLIP  :    monsignoredisandre

The three mismatches: the writer-cancelled false start (T63 T81 = "db", struck), T81 (b) where the slip has r (T81/T83 r
look-alike or a cipher-clerk slip; both readers read T81), and the off-sheet "=" sign where the slip has the d of "Andre".
L01.2 ("M. di Bellaguarda" on the slip) is 4 signs: T54 (m) + two digit-like signs "4" "7" + T49 (u) -- the shape of a
nomenclator name code ("M." + a numbered name), which the printed 1572 table does not carry; not keyed here (3 U tokens).

**Reading** (`tools/decode_key.py ciphers/nevers-birago-fr3251-1572`, job built by `harvest/build_decode_inputs.py f162r`;
`--check` exit 0). `harvest/exceptions_f162r.tsv`: pos 1-2 NULL (struck by the writer, M), X_EQ at pos 19 = d (the slip's d, M).
Grades (rule 4): **25 tokens: H 0, C 0, S 8, M 14, I 0, U 3** -- a cryptanalytic result under the published key + GAPS3 fit, and
the plaintext is the slip's.

    f162r L01.1 | ·monsignobedisandre       slip: monsignore di S. Andre
    f162r L01.2 | m··u                      slip: M. di Bellaguarda

**Judge** (secondary, `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f162r/reading_f162r_letters.txt`,
L01.1 letters without the struck pair):

    ok   language: score=-0.822, null_p99=-1.276, real_p05=-1.051, real_median=-0.846, mode=both, N=20
    PASS - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

Shuffled-target control (`harvest/shuffled_judge.py`, fitted map, 20 seeds, L01.1): 0 of 20 PASS, mean -2.077, max -1.340. At
N=20 and on a name phrase this PASS is weak evidence; reported as is.

**What this settles.** No.82's whole cipher is the one line on f.160r/162 (canvas 164 right); the 1572 key reads its first run as
"monsignore di S. Andre" with 0.74 letter agreement against the pasted slip (shuffled max 0.15), the slip's own reading. The
second run is a name code outside the printed table; the slip gives it as "M. di Bellaguarda" (a C-grade value for the code
"47" if the verifier accepts the slip's authority -- not entered in the key here).

Requests: gallica.bnf.fr 6 attempts (canvases 163, 164 [one connection reset, retried once after 20 s], 167 at 1200 px; info.json
164; two native regions). Subagents: 3 Sonnet (2 passes + 1 adjudication). No credentials.

## NEVBIR-168 (2 Oct 2026, account 2 for the account-3 orchestrator): no.85 (f.168, 29 July 1572), two cipher runs, first test -- not licensed

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-letter.md`, WORK-QUEUE row NEVBIR-168. `tools/intake_gate_check.py` exit 0
at 16:1x UTC. Box 16:12-17:02 UTC. Status stays `partial`. No class, no novelty wording (rule 10).

**Whole openings first (brief step 1).** Canvas 171 (f.167v | f.168r, ink '168') and canvas 172 (f.168v | f.169r, ink '169')
viewed whole at 1000/1600 px. No.85 carries **two** cipher runs: f.168r, 2 lines after "tenendo per certo" (L02 whole, L03 up to
the prose "Il Baron de Sadces"), and **f.168v head, 3 lines** after "potrano considerare" (PREMISE-NEVBIR saw only the f.168r run).
The letter ends on f.168v ("Da Saluzzo li 29 di Luglio 1572", signed); f.169r opens the next item. **No pasted slip, interlinear
gloss or laid-in sheet on either opening.** The only other writing is a three-line note at the foot of f.167v, fetched native
(`harvest/f168r/c171_leftnote.jpg`): "Doppo scritto ho inteso che mons. di Bellag[ard]a ... venuti hieri a Turino" -- a plain-prose
postscript to the preceding letter, not a decipherment. Nothing for a known-answer check.

**Crops** (pasted commands):

    python3 tools/iiif_lines.py --ark btv1b9060248g --canvas 171 --region 4600,2560,3500,480 --out ciphers/nevers-birago-fr3251-1572/harvest/f168r --prefix f168r --max-width 1250 --overlap 50 --debug
    python3 tools/iiif_lines.py --ark btv1b9060248g --canvas 172 --region 1650,700,2750,650 --out ciphers/nevers-birago-fr3251-1572/harvest/f168v --prefix f168v --max-width 1250 --overlap 50 --debug

Debug overlays checked by eye; `make_2x.py` 2x copies (gitignored); prose-only segments withheld; 13 crops per reader. Passage ids
R02, R03 (f.168r) and V01-V03 (f.168v). One reader call covered both pages (13 crops, fewer than f.139v's 15 in one call).

**Passes.** Two value-blind Sonnet readers (`harvest/f168/blind_pass_brief_f168.md`, the 51-cell sheet): passA 122 signs, passB 124.
`reconcile_blind.py`: **109 of 125 aligned agree (0.87)**; 11 '?' settled by a third value-blind reader (`adjudicate_in.tsv` ->
`adjudicate_out.tsv`: one omega straddling the R03 s1/s2 boundary counted once; the K-shape before "Il Baron" judged a prose
flourish, NONE). Final `harvest/f168/passC.tsv`: **121 signs, 11 off-sheet** (digits 4 and 7, t-shapes, a dotted integral, a
dotted square, a slashed B, a bulb with legs).

**Control (rule 3)**, `decode_control.py f168/passC.tsv --map sign_id_map_1572_fit.json` (printed key + T42=m, it16dip, 200
value-shuffled keys, the f.178v statistic):

| sequence | signs / letters | real key | shuffles mean / max | z | rank of 201 | power control |
|---|---|---|---|---|---|---|
| pass A alone | 122 / 117 | -1.381 | -1.580 / -1.245 | 1.34 | 22 | -- |
| pass B alone | 124 / 118 | -1.342 | -1.561 / -1.231 | 1.42 | 20 | -- |
| **passC, seed 1** | 121 / 117 | **-1.414** | -1.566 / -1.247 | **1.00** | **36** | **15/20 rank 1 at err 0.13**, z median 2.75 min 0.22 |
| passC, seeds 2, 3 | 121 / 117 | -1.414 | -1.562 / -1.194; -1.560 / -1.132 | 0.97; 0.91 | 31; 41 | -- |

**Verdict on the test: the key is not shown to read this letter; not a negative either.** The real key is above the shuffled mean
but nowhere near rank 1. The power control (same lengths, measured 13% disagreement, off-sheet signs not modelled) puts a right
key at rank 1 in 15 of 20 windows, with the weakest window at z 0.22 -- so a z of 1.0 is in the tail a right key reaches at this
length, and the 11 off-sheet signs (9%) add error the control does not model. Logged as an unlicensed first test, short-run
class (with f.144r), not as a control-backed negative; no per-token grades are claimed (rule 4) and no reading file is written.
The decode as it stands (`harvest/f168/control_reading.txt`, every token M at best): R02 `cheisisafasuanuato_oltoconlorialtezn`,
R03 `sopfagpafti_solehn`, V01 `guantoilpfoce`, V02 `deresi__sii_tanto_astidiisaamn`, V03 `_ada_osasufefoi_iilifoquello__m`.

**Judge** (secondary; `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f168/reading_f168_letters.txt`):

    FAIL language: score=-1.402, null_p99=-1.601, real_p05=-0.957, real_median=-0.836, mode=both, N=117
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

Next (Remaining gaps): pool f.168 with f.144r in one joint shuffled-key test; value-fit of the shared off-sheet signs.
Requests: gallica.bnf.fr 5 (canvas 172 at 1600 px, the f.167v note region, two cipher regions; one connection reset on canvas 171
retried once after 20 s). Subagents: 3 Sonnet (2 passes + 1 adjudication). No credentials.


## NEVBIR-POOL (2 Oct 2026, owner-account worker for the account-3 orchestrator): joint test of the three short 1572 runs -- not licensed, not a negative

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-pool.md`. Disk only (0 network requests, 0 subagents). Status stays `partial`.
No class, no novelty wording (rule 10).

**Material.** The three runs that were non-tests at their own length, reconciled sequences exactly as committed:
`harvest/f144r/passC.tsv` (no.73, 90 signs, reader disagreement 0.24), `harvest/f168/passC.tsv` (no.85, 121 signs, 0.13),
`harvest/f174r/passC.tsv` (no.86 foot, 85 signs, 0.09). Joined with passage ids prefixed by folio into `harvest/pool/pool_all.tsv`
(296 signs, 308 letters under the key; 32 off-sheet signs, 11%) and the three leave-one-out pairs `harvest/pool/loo_no*.tsv`.
Each passage is scored separately and letter-weighted, as before (runs never join across a passage break). Pooled measured error,
weighted by signs: 0.15; the power control was run at 0.15 and at 0.24 (the worst run's own) to bracket it (rule 3).

**Command** (per run; outputs in `harvest/pool/run_*.txt`):

    python3 ../ceppo-nevers-fr3251-1570s/harvest/decode_control.py harvest/pool/pool_all.tsv --map harvest/sign_id_map_1572_fit.json --seed S --err E [--windows 0]

**Joint test** (printed 1572 key + T42=m, it16dip, 200 value-shuffled keys per seed):

| sequence | signs / letters | real key | shuffles mean / max | z | rank of 201 | power control (20 windows, same passage lengths) |
|---|---|---|---|---|---|---|
| pool, seed 1 | 296 / 308 | -1.318 | -1.557 / -1.283 | 2.13 | 4 | **15/20 rank 1 at err 0.15**, z median 2.95 min 1.40 |
| pool, seed 2 | 296 / 308 | -1.318 | -1.557 / -1.321 | 1.98 | 1 | **5/20 at err 0.24**, z median 1.74 min 0.28 |
| pool, seed 3 | 296 / 308 | -1.318 | -1.560 / -1.317 | 2.04 | 2 | -- |
| pool, seed 4 | 296 / 308 | -1.318 | -1.563 / -1.291 | 2.03 | 2 | -- |

**Leave-one-out** (does one run drag the pool down?):

| dropped | signs / letters | real key | z (seeds) | rank of 201 (seeds) | power control, seed 1 |
|---|---|---|---|---|---|
| f.144r | 206 / 214 | -1.341 | 1.78; 1.68 | 5; 11 | 16/20 at err 0.11 |
| **f.168** | 175 / 191 | **-1.262** | 2.48; 2.27; 2.42 | **1; 1; 1** | 8/20 at err 0.17 (z median 2.20 min 0.62) |
| f.174r | 211 / 211 | -1.348 | 1.63; 1.58 | 10; 12 | 10/20 at err 0.18 |

**Verdict: not licensed, not a negative.** Pooling did not lift the signal: the pooled z (2.0-2.1) is no higher than f.174r's
alone (1.8-2.1), and the real key sits at rank 1 in only one of four seeds (rank 1-4, about the top 1-2% of shuffled keys).
At the pooled error the same test puts a known-right key first in 15 of 20 windows, with a median z of 2.95; the target's 2.1
is inside that range but in its lower quarter, and at the worst run's error (0.24) the power falls to 5/20. So neither "the key
reads these three runs" nor "it does not" is licensed (rule 3). No per-token grades are claimed (rule 4): every token in
`harvest/pool/pool_reading.txt` is M at best.
The leave-one-out says **f.168 (no.85) is the drag**: without it the other two runs reach rank 1 at all three seeds (z 2.3-2.5),
consistent with f.168's own rank 36. That pair is still not licensed -- its power is 8/20 at its error -- and choosing the pair
after seeing the scores is a selection the shuffle test does not correct for. It is a pointer, not a result: f.168's 11
off-sheet signs and its own reading are what to look at next (the value-fit shared with f.139v), and f.144r's 0.24 reader error
is the other lever. The decisive unit for no.86 remains f.174v (~600 signs, power 20/20 at that length).

Requests: none (disk only). Subagents: none. No credentials.

## NEVBIR-174V-A (2 Oct 2026, account 2 for the account-3 orchestrator): no.86 f.174v lines 1-11 read under the printed 1572 key + T42=m, rank 1/201

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-174v.md` (half A). `tools/intake_gate_check.py nevers-birago-fr3251-1572`
exit 0 at 18:12 UTC. Box 18:12-19:07 UTC. No class, no novelty wording (rule 10). Status stays `partial`. A pass here is flagged
for a separate verifier, not described as a reading of record.

**Slip check at native resolution.** Canvas 178 fetched once whole at native size (8515x5853; one connection reset, retried
once after a 20 s pause) and viewed by eye in four quadrant tiles: f.174v (left) is cipher from line 1 (after the prose "di
pnti, habbi col mezo del figliolo" and a bracket) to its foot; f.175r (right) carries one cipher line at its head, then prose
to "Circa al Cavallero Peloia". **No pasted slip, squared paper, interlinear or marginal decipherment on either page**; only
show-through from the facing leaves. At native I count **23 lines** on f.174v (the last at native y ~3960), not 22; half A is
page lines 1-11, half B (NEVBIR-174V-B) starts at the line opening with a phi-Lambda-omega shape (native y ~2400). The
full-canvas image stayed in the session scratchpad and was not committed.

**Material.** Native region `1950,860,2470,1585` of canvas 178 cut from that fetch to
`harvest/f174v/src_ark_12148_btv1b9060248g_f178_1950_860_2470_1585.jpg`, then:

    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f174v/src_ark_12148_btv1b9060248g_f178_1950_860_2470_1585.jpg \
      --out ciphers/nevers-birago-fr3251-1572/harvest/f174v --prefix f174v --max-width 1240 --overlap 60 \
      --centres 93,236,371,514,653,778,912,1071,1219,1359,1491 --debug

(the centres are the tool's own auto-detected ones from a first run; the region was then extended 45 px so L11's descenders are
not cut. Two earlier cuts at a shorter region were deleted). 33 crops (11 lines x 3 segments); 2x reader copies
`harvest/make_2x.py --folio f174v` (gitignored), each under 2500 px.

**Passes.** Two value-blind Sonnet readers (`blind_pass_brief_1572.md`, the 51-cell sheet, crops only, one call each for the
half): `f174v/passA.tsv` 286 signs, `passB.tsv` 290. `../ceppo-nevers-fr3251-1570s/harvest/reconcile_blind.py`: **235 of 292
aligned agreed (0.80)**. Commonest splits were T29/T83 (8 positions, B always reading T83 at H), T13/T64 (3), and the
"-|-" crossed-bar mark, the "c with inner curl" mark and the digit pairs "8 9"/"8 5" (A on-sheet, B X_NEW).
A third value-blind Sonnet reader (`adjudication_sheet.py` -> `f174v/adjudicate_in.tsv` -> `adjudicate_out.tsv`, 51 rows)
settled them: 14 to A, 8 to B, 18 to another cell, 10 X_NEW, 1 NONE. The reader graded the "-|-" mark L and set it to T86,
noting that it may be a separate variant. It read the "8 9"/"8 5" pairs as T15/T11, which carry word values in the printed key.
Final `f174v/passC.tsv` **285 signs, 0 '?', 18 off-sheet (X_NEW)**.

**Control (rule 3)**, `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py f174v/passC.tsv --map sign_id_map_1572_fit.json`
(printed key + T42=m; it16dip; 200 value-shuffled keys):

| sequence | signs / letters | real key | shuffles mean / max | z | rank of 201 | power control (20 windows) |
|---|---|---|---|---|---|---|
| **passC, seed 1** | 285 / 317 | **-1.102** | -1.590 / -1.296 | **3.36** | **1** | 20/20 at err 0; **20/20 at err 0.10** (z median 3.80, min 2.85); 8/20 at err 0.20 (z median 2.40) |
| passC, seeds 2, 3 | 285 / 317 | -1.102 | -1.584 / -1.291; -1.584 / -1.295 | 3.48; 3.49 | 1; 1 | -- |
| pre-adjudication passC (57 '?' dropped), seed 1 | 286 / 252 | -0.994 | -1.549 / -1.222 | 3.27 | 1 | -- |

The real key is first at every seed, well clear of the shuffled maximum. The measured reader disagreement before adjudication
(0.20) is the pessimistic error. At that error the power control finds the right key in 8 of 20 windows; at 0.10 it finds it in
20 of 20. The target ranks 1 either way, so the test is **a pass at this half's length, not a non-test**. It is backed on f.174v
lines 1-11 alone. Pooling with half B and f.174r is the next step.

**Decode** (`tools/decode_key.py` job `harvest/ciphertext_f174vA.tsv` via `harvest/build_decode_inputs.py f174vA --seq
f174v/passC.tsv`; `--check` "reading up to date"). `harvest/reading_f174vA.txt`, **tokens 285: H 0, C 0, S 242, M 25, I 0, U 18**
(S = the key file's grade, now also backed by this half's own control above; M = a reader-conf M/L sign; U = off-sheet,
unkeyed). No H or C: a cryptanalytic result under a published key (rule 4).

    f174vA L01 | edetobaron
    f174vA L02 | anegitiarn·ue·tapraticaiicono
    f174vA L03 | soagenn[che]ei·esauioa·a·tanzape
    f174vA L04 | miagtihominie[carmagnola]nerestanotraua
    f174vA L05 | gliaticontuto[che]lacolerae··gi
    f174vA L06 | taaleattre·uegualitaeingomp
    f174vA L07 | tibile·emenoti[bugonotti]e[carmagnola]·sonotri·t
    f174vA L08 | simiconilme·iodeli·uoicapita
    f174vA L09 | [che]sonota·ambidoisono[bugonotti]hanoem·
    f174vA L10 | nierapraticatoteco·e[che]luire·
    f174vA L11 | domesticoloropsegi[bugonotti]·onipoiu

These Italian stretches read without repair: "pratica", "huomini e [carmagnola] ne restano", "con tuto che la colera",
"egualita", "ambidoi sono [bugonotti]", "domestico loro". The word values are T15 (printed "bugonotti", i.e. ugonotti) and
T11 (carmagnola). Both rest on the adjudicator's T15/T11 calls for the "8 9"/"8 5" pairs. A verifier should re-check those
pairs on the crops, because they are digit-like and one reader called them off-sheet.

**Judge** (secondary; `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/f174v/reading_f174vA_letters.txt`):

    FAIL language: score=-1.164, null_p99=-1.739, real_p05=-0.914, real_median=-0.818, mode=both, N=317
    FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)

A FAIL at the gate, with the score far above the null. This is the same shape as f.139v (-1.159) and f.178v before GAPS4: reader
error on look-alike pairs plus 18 unkeyed signs. The judge is reported as it stands.

**What this leaves.** f.174v lines 12-23, f.175r head and f.175v go to NEVBIR-174V-B. After that, the joint no.86 decode
(f.174r + both f.174v halves + f.175) runs with one 200-shuffle test at 3 seeds (disk only, ~$1). Then a verifier pass
(rule 10), which should also cover the T15/T11 digit-pair calls and the T29/T83 split. Requests: gallica.bnf.fr 3 (1 info.json, 1
reset + 1 retry for the native canvas), no errors otherwise. Subagents: 3 Sonnet (2 blind passes, 1 adjudication). No
credentials.

## NEVBIR-174V-B (2 Oct 2026, account 2 for the account-3 orchestrator): no.86 f.174v lines 12-22 + f.175r head + f.175v read under the printed 1572 key + T42=m; whole no.86 cipher rank 1/201

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-174v.md` (HALF B). `tools/intake_gate_check.py nevers-birago-fr3251-1572`
exit 0 at 18:12 UTC. No class, no novelty wording (rule 10). Status stays `partial`.

**Slip check.** Canvases 178 and 179 at 3000 px (about a third of native 8515 px; both pages each, scratch only) and the four
native regions below: no pasted slip, squared paper, interlinear decipherment or gloss on f.174v, f.175r or f.175v; only
show-through of the recto prose. NEVBIR-174V-A looked at all of canvas 178 at native and found the same.

**Line count.** By row-ink profile f.174v carries 22 cipher lines (line 1 opens with the prose "di pnti, habbi col mezo del
figliolo"). Half A took lines 1-11 (native y 860-2445); this job took lines 12-22, native y 2484-3906 (the line above, at
y 2354, sits inside half A's region and is its L11). Half A's ROOM note counts 23 lines; on these coordinates the two halves
meet with no line skipped, so the count difference is a numbering difference, not a missing line. The folder files call this
half's lines `f174vB L01-L11`; the joined files renumber them `f174v_L12-L22`.

**Material** (gallica.bnf.fr; four region fetches kept, two discarded after mis-placed coordinates, see requests):

    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f174vB/src_ark_12148_btv1b9060248g_f178_1950_2330_2500_1680.jpg \
      --out ciphers/nevers-birago-fr3251-1572/harvest/f174vB --prefix f174vB --centres 154,296,437,572,714,864,1006,1159,1298,1438,1576 --max-width 1300 --overlap 60 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f175r/src_ark_12148_btv1b9060248g_f178_4950_960_2550_200.jpg \
      --out ciphers/nevers-birago-fr3251-1572/harvest/f175r --prefix f175r --centres 70 --max-width 1300 --overlap 60 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f175v/src_ark_12148_btv1b9060248g_f179_1950_2830_2650_460.jpg \
      --out ciphers/nevers-birago-fr3251-1572/harvest/f175v --prefix f175v --centres 92,229,380 --max-width 1300 --overlap 60 --debug

The initial f.175v cut (region y 2900) sat a line low; both readers said so. It was re-fetched at y 2830, re-cut, and read again
by two fresh blind readers. The old V rows in `f174vB/passA/B.tsv` are ignored by `join_no86.py`. 2x reader copies come from
`harvest/make_2x.py --folio f174vB|f175r|f175v` and are gitignored. Every cipher line on f.174v and f.175v runs into the gutter,
so line-end signs are conditional on the image.

**Passes** (value-blind Sonnet readers, `blind_pass_brief_1572.md`, crops only). f.174v 12-22 + f.175r: `f174vB/passA.tsv`,
`passB.tsv`, agreement **230/306 (0.75)** on f.174v and 20/25 (0.80) on f.175r. Most splits came from one reader putting a
frequent joined shape off the sheet (T83 vs X_NEW, 23 positions), plus T86/T60 (11) and T18/T98 (7). A third blind reader settled
78 positions (`f174vB/adjudicate_in.tsv` -> `adjudicate_out.tsv`): 67 to reader A, 9 to reader B, 2 other, 0 dropped. Its
recurring calls were the joined shape = T83, single-bar = T86, loop-on-top = T18, and the blotted omega = T92. f.175v:
`f175v/passA.tsv`, `passB.tsv`, **52/62 (0.84)**; 9 positions were adjudicated, 8 to reader B (T83 x6, T45 x2) and 1 other.
Pooled measured disagreement before adjudication: 302/393, about **0.23**.
Final: **389 signs** (f.174v 12-22: 303; f.175r: 25; f.175v: 61). There are 29 unkeyed signs: X_NEW, X_K, X_A, X_EQ and '?'.
The lone "8" shape (5 times, including an "88" on L13) is off the sheet. It is probably a clear numeral or a code like
half A's T15/T11 "8 9"/"8 5" pairs; this job does not settle it.

**Control (rule 3)**, `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py <seq> --map sign_id_map_1572_fit.json` (printed key +
T42=m; it16dip; 200 value-shuffled keys). Logs are in `harvest/no86/log/`. The sequences come from `harvest/join_no86.py`.

| sequence | signs / letters | real key | shuffles mean / max | z (seeds 1, 2, 3) | rank of 201 | power control (20 windows) |
|---|---|---|---|---|---|---|
| **half B** (`no86/passC_halfB.tsv`) | 389 / 400 | **-1.085** | -1.603 / -1.284 | **3.58, 3.74, 3.42** | **1, 1, 1** | 20/20 at err 0.10 (z min 2.67); 8/20 at err 0.23 |
| **whole no.86** (f.174r + f.174v 1-22 + f.175r + f.175v; `no86/passC_all.tsv`) | 759 / 814 | **-1.113** | -1.593 / -1.331 | **3.69, 3.83, 3.56** | **1, 1, 1** | 13/20 at err 0.23 (z median 2.52) |

The real key takes rank 1 against every shuffled key, at every seed, on both sequences. The power control shows how often a known-right key takes
rank 1 at this length. At the pre-adjudication error (0.23) it does so only 8/20 (half B) and 13/20 (whole letter), so it does
not lower the bar for a miss. Here the target did not miss: it took rank 1. The real key scores above the best of 200 shuffles
by 0.20 on half B and 0.22 on the whole letter. At the post-adjudication error, which is lower, the half-B power control is 20/20
at 0.10.

**Decode.** `tools/decode_key.py` jobs `harvest/ciphertext_no86B.tsv` (half B) and `harvest/ciphertext_no86.tsv` (the per-letter
file: f.174r's 85 signs + half A's 285 + this half's 389 = 759), both built by `harvest/build_decode_inputs.py <folio> --seq
no86/<file>`. `--check`: "reading up to date". Grades come from decode_key with the key file's grades. Half B: **H 0, C 0, S 318,
M 42, I 0, U 29** of 389. Whole letter: H 0, C 0, S 629, M 76, I 0, U 54 of 759. These are cryptanalytic grades; there is no H or C
(no key source or known plaintext on these leaves). `harvest/reading_no86B.txt`:

    no86B f174v_L12 | ticoncostanuocorde·iemsnie
    no86B f174v_L13 | [che]lihuo·iniabeni[et]··nonposino[che]p
    no86B f174v_L14 | tirepalafine··arasiu[per]anooua
    no86B f174v_L15 | geneuraolsra[che]nelepartielo·p
    no86B f174v_L16 | rdiagnome·barondesadrns[per]leco
    no86B f174v_L17 | pasatesirendnsiodioso[che]i··nee
    no86B f174v_L18 | ·a·uolsutoguantoameeisidi·os
    no86B f174v_L19 | tradiltunoa·enionatisi·o·e·
    no86B f174v_L20 | no[quello][che]iodicoe[per]ilserui[quello]ioe·a·co
    no86B f174v_L21 | beneacarolecosedgouernanie·o
    no86B f174v_L22 | [che][per]uolerfare·lserui[quello]io···io·
    no86B f175r_R01 | agubssilamalagratiadaltri
    no86B f175v_V01 | ·praticastreta·ente[per]cont
    no86B f175v_V02 | dilgouernoconilbaroncresoan[che]c
    no86B f175v_V03 | sanfre··

Several stretches read as Italian without repair: "non posino", "alla fine", "le parti", "il servi[tio]", "bene a caro le
cose", "per voler fare", "la mala gratia d'altri", "pratica stretta", "del governo con il baron", and a name "baron de Sadr..."
on L16. The prose of no.86 on f.176r names "il baron de Sadres" ("per il baron de Sadres che la Voluera...", canvas 179 right,
seen by eye in this job's slip check). That ties L16 to the letter's own clear text. It is a consistency observation, not a
known-plaintext crib: the prose is not a decipherment of this run. The f.175v run follows the prose "ho scritto al" and ends
before "Circa alla Carta dil Piemonte".

**Judge** (secondary; `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/no86/reading_no86B_letters.txt`
and `... reading_no86_letters.txt`):

    half B:       FAIL language: score=-1.141, null_p99=-1.739, real_p05=-0.919, real_median=-0.819, mode=both, N=400
    whole no.86:  FAIL language: score=-1.161, null_p99=-1.767, real_p05=-0.905, real_median=-0.828, mode=both, N=814

Shuffled-target control (`harvest/shuffled_judge.py`, fitted map, 10 seeds): half B 0 of 10 PASS (mean -1.637, max -1.539);
whole letter 0 of 10 PASS (mean -1.622, max -1.556). The FAIL has the f.139v/f.174vA/f.178v shape: the score is far above the null
and below real prose, which points to reader error on look-alike pairs plus unkeyed signs. The judge is reported as it stands.

**For the verifier (rule 10).** This reading is flagged for a separate verifier session. Re-check these on the crops: the T83
calls (one reader had all of them off-sheet), the lone "8" shapes, and L20/L22 "[quello]" twice next to "serui". Also check
half A's T15/T11 digit pairs. Requests: gallica.bnf.fr 7 (2 overview canvases at 3000 px, 5 native regions, of which 2 were
discarded and re-fetched after wrong coordinates), 1 info.json; no errors. Subagents: 5 Sonnet (2 blind passes, 2 f.175v
re-read passes, 1 adjudicator used twice). No credentials.

## NEVBIR-LOOKALIKE (2 Oct 2026, owner-account worker for the account-3 orchestrator): look-alike pass on the two short runs, control re-run, sorter package

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-lookalike.md`. Disk only (0 network requests; every crop was already on
disk). Status stays `partial`. No class and no novelty wording (rule 10). No per-token S grades are claimed (see the verdict).

**Step 1, confusion map** (`harvest/confusion_1572.py` -> `harvest/confusion_1572.tsv`). Every two-reader alignment on disk
(`harvest/*/passC*_agreement.tsv`, 15 files: 1572 leaves f139v, f144r, f152r, f162r, f168, f174r, f174v, f174vB, f175v, f178r,
f178v x2, f179r, f184r). That is 2,375 aligned pairs, 299 label swaps, 73 distinct pairs. Top ten: T83/X_NEW 24, T60/T86 21,
T18/T98 18, T29/T83 17, T24/T83 16, T92/X_NEW 16, T24/T29 9, T55/X_NEW 9, T90/X_NEW 9, T50/T92 8.

**Step 2, look-alike pass** (`harvest/lookalike_packet.py`, `harvest/lookalike_reconcile.py`, outputs in `harvest/lookalike/`).
A tile was flagged if its two readers split, or if its passC label sits in a top-ten pair: f.144r 45 of 90 tiles (20 splits),
f.168 47 of 121 (12 splits). There was one value-blind Opus call per run. The reader saw only the 2x line crops, the passC
label sequence and a candidate-only cut of the blind sign sheet (`lookalike/<run>_candidates.png`, ids only). Results:
`f144r_reread.tsv` 22 H / 20 M / 3 L / 0 SPLIT; `f168_reread.tsv` 25 H / 20 M / 2 L / 0 SPLIT. Reconciliation is one more step,
done by script: the rule was fixed before any score was computed and is in the docstring. A firm (H/M) re-read that matches
reader A or B settles the tile 2-of-3. Anything else stays UNSETTLED and keeps the passC label, because a third reader alone
does not overturn two. `passD_alt.tsv` takes every firm re-read label and is a secondary sequence only.

| run | signs | two-reader disagreement before | relabelled (2-of-3) | unsettled | residual disagreement after |
|---|---|---|---|---|---|
| no.73 f.144r | 90 | 0.24 | 3 | 4 | **0.044** |
| no.85 f.168 | 121 | 0.13 | 4 | 9 | **0.074** |

The residual is a 2-of-3 figure on flagged tiles, a different statistic from the old two-reader rate. The power control
below was therefore run at both figures (rule 3 bracket). Seven of the nine f.168 unsettled tiles are one question. All three
earlier reads (A, B and the adjudicator) said T24. The look-alike reader said T83 at M, describing "two halves facing away,
one bar through both", and suggested that the T24 sheet cell may be a poor cut of the same sign. On f.178r/f.179r (GAPS4,
section above) a value-blind third reader settled 19 of 21 splits in this pair to T83.

**Step 3, control** (`python3 ../ceppo-nevers-fr3251-1570s/harvest/decode_control.py harvest/lookalike/<run>_passD.tsv --map
harvest/sign_id_map_1572_fit.json --seed S --err E [--windows 0]`, printed 1572 key + T42=m, it16dip, 200 value-shuffled keys;
outputs `harvest/lookalike/run_*.txt`):

| sequence | signs / letters | real key | shuffles mean / max (seed 1) | z (seeds 1, 2, 3) | rank of 201 (seeds 1, 2, 3) | power control, 20 windows |
|---|---|---|---|---|---|---|
| f.144r passD | 90 / 94 | -1.174 | -1.537 / -1.202 | 2.27, 2.34, 2.44 | **1, 2, 1** | **18/20 at err 0.044** (z median 3.22, min 1.78); 4/20 at 0.24 |
| f.168 passD (primary) | 121 / 119 | -1.342 | -1.577 / -1.224 | 1.55, 1.53, 1.43 | 13, 15, 14 | **19/20 at err 0.074** (z median 3.60, min 2.00); 14/20 at 0.13 (min -0.15) |
| f.168 passD_alt (secondary) | 121 / 119 | -1.078 | -1.582 / -1.261 | 3.49 (seed 1) | 1 | -- |
| f.144r passD_alt (secondary) | 90 / 95 | -1.281 | -1.555 / -1.231 | 1.72 (seed 1) | 5 | -- |

Before this pass: f.144r passC rank 3-6 (z 1.8), f.168 passC rank 31-41 (z 0.9-1.0).

**Verdict (rule 3; report rank, z and power side by side; a non-test is not a negative).**
- **no.73 f.144r:** with three settled relabels the real key moves from rank 3-6 to rank 1-2 (z about 2.3-2.4). At the
  residual figure (0.044), the control puts a right key first in 18 of 20 windows, so the target's result is what a right key
  gives. This is control-backed **only if** the 2-of-3 residual is the true reader error. At the old two-reader 0.24 the same
  result is a non-test (4/20). That condition is not yet checked by an independent read, so no S grades and no firm counts.
  Next: a verifier on the passD reading and its 4 unsettled tiles.
- **no.85 f.168:** the primary sequence improved (rank 36 -> 13-15) but still sits below the weakest power window at the
  residual figure (z 1.5 against a minimum of 2.00 at 0.074). Read at face value, that says the residual underestimates the
  error on this run. It falls inside the 0.13 control's range (min -0.15), so it is **not licensed and not a negative**. The
  pre-registered secondary sequence (T83 at the seven T24/T83 tiles) ranks 1/201 at z 3.49. That is a pointer only: it rests
  on one reader's M calls against two readers plus an adjudicator. The step that settles it is a person's eye on those seven
  tiles (sorter focus box), not a further machine pass (CLAUDE.md Usage 6, "settle the alphabet before reading").
- Judge (secondary; `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/lookalike/<f>_letters.txt`):

      f144r_passD     FAIL language: score=-1.424, null_p99=-1.6,   real_p05=-0.955, real_median=-0.828, mode=both, N=94
      f168_passD      FAIL language: score=-1.371, null_p99=-1.668, real_p05=-0.951, real_median=-0.828, mode=both, N=119
      f168_passD_alt  FAIL language: score=-1.177, null_p99=-1.668, real_p05=-0.951, real_median=-0.828, mode=both, N=119

  Under the alt sequence, f.168 reads R02 `cheisisarasuanuatomoltoconlorialtezn`, R03 `sopragparti_solern`, V01 `guantoilproce`,
  V02 `deresi__sii_tanto_astidiisaamn`, V03 `mada_osasurerui_iiliroquello__m`, every token M at best (rule 4). Under passD it
  differs only at the T24/T83 positions (f/r).

**Step 4, sorter package** (`sorter/`, README there): `signs.tsv`, `labels.tsv`, `focus.tsv` (13 tiles: the 4 f.144r and
9 f.168 unsettled ones), `pages/` (9 line strips cut from the public Gallica region images on disk, 652 KB), and
`build_inputs.py`. Tile boxes are approximate (column-profile blobs fitted to each passage's count). The HTML was built once
into the worker's scratch directory (46 piles, 211 tiles, 1.7 MB) and rendered headless with no script errors. It was **not
published**; the account-3 orchestrator publishes it.

Requests: none (disk only). Subagents: 2 Opus value-blind look-alike reads, 1 per run; the reconciliation was by script.
No credentials. Report of what was found and where it was not found; novelty not classified.

## LOOKALIKE-TOOL (2 Oct 2026, parent worker for the account-3 orchestrator): known-answer test of the look-alike pass on no.87

The look-alike pass is now `tools/lookalike_pass.py`, and the three scripts here point at it. It was run blind on no.87 f.178r (97 signs)
and f.179r (89 signs) with the confusion map, packet and reconcile steps: one value-blind Opus re-read per leaf, 40 + 31 tiles. Each
sequence was then scored against the clerk's clear sheet (canvas 182) with `harvest/lookalike_known/score_known.py`. The scorer
was written and run on passA/B/C before either re-read existed. It decodes with the fitted map without the sheet-derived exceptions,
folds the text the align_sheet.py way, and counts a sign WRONG when its letters fall outside matching blocks of 2 or more.

| leaf | true error passC (before) | flagged | relabelled (2-of-3) | true error passD (after) | residual (2-of-3) | wrong signs flagged / re-read kept wrong |
|---|---|---|---|---|---|---|
| f.178r | 16/90 = 0.178 | 40 | 0 | 0.178 | 0.031 | 9 of 16 / 7 of 9 |
| f.179r | 6/84 = 0.071 | 31 | 0 | 0.071 | 0.000 | 2 of 6 / 2 of 2 |

No correction moved a right label to a wrong one, because the primary rule relabelled nothing. The secondary passD_alt sequence
fixed one sign (f.178r L01.27, T92 -> T50) and harmed none. With a block of 3 the f.178r figures are 0.200 before and after.
**On this leaf pair the pass raises agreement but not accuracy.** Its residual (0.031, 0.000) understates true error
(0.178, 0.071) by 6x or more. One reason is that 11 of 22 wrong signs were never flagged, because both readers agreed on them.
Another is that the re-read confirmed 9 of the 11 flagged wrong labels. Caveat: some WRONG signs may be key-value errors rather
than misreads (GAPS4's c/s pair, the misread opening of f.178r L01). These count the same before and after, so they do not
change the before/after comparison, but they do inflate the absolute error. Both leaves' passC already carried a third-reader
adjudication, as f.144r's and f.168's did.
**Consequence for NEVBIR-LOOKALIKE above:** the f.144r power control run at the 2-of-3 residual (0.044, 18/20) is downgraded. The
residual is not a measure of reader error. The bracket that counts is the two-reader rate (0.24, 4/20), so f.144r stays a
non-test at its length. The f.168 verdict is unchanged (not licensed, not a negative).

## NEVBIR-185 (2 Oct 2026, account 2 for the account-3 orchestrator): no.90 f.184v foot + f.185r lines 1-8 read under the printed 1572 key + T42=m; whole no.90 so far rank 1/201

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-185.md`. `tools/intake_gate_check.py nevers-birago-fr3251-1572` exit 0 at
19:1x UTC. Box 19:10-20:05 UTC, cap USD 5. No class, no novelty wording (rule 10). Status stays `partial`.

**Slip look first.** Canvas 189 (8262x5849) native regions and canvases 188/190 looked at by eye: no laid-in slip, no
interlinear decipherment. The faint marks over f.185r line 19 ("cose sue da di qua, che ...") are show-through from the
facing page (mirror ink), not a gloss.

**Fetch and crops.** Two native regions of canvas 189, fetched once: `1600,3680,2550,600` (f.184v foot) and `4780,980,2850,3420`
(f.185r, whole cipher block). Sources and debug overlays are gitignored (folder at its 30 MB line); `harvest/f185/REGEN.sh`
re-fetches and re-cuts them. Crops:

    python3 tools/iiif_lines.py --image $D/f185/src_f189_1600_3680_2550_600.jpg --out $D/f184v --prefix f184v --centres 80,205,330,465 --follow-slope 300 --slope-margin 15 --max-width 1250 --overlap 50 --debug
    python3 tools/iiif_lines.py --image $D/f185/src_f189_4780_980_2850_3420.jpg --out $D/f185r --prefix f185r --centres 105,215,330,435,550,665,775,890 --follow-slope 300 --slope-margin 15 --max-width 1250 --overlap 50 --debug
    python3 tools/iiif_lines.py --image $D/f185/src_f189_4780_980_2850_3420.jpg --out $D/f185r/l5 --prefix f185r5 --centres 610 --follow-slope 300 --slope-margin 15 --max-width 1250 --overlap 50

(`D=ciphers/nevers-birago-fr3251-1572/harvest`). The slope fit put band L03 back onto manuscript line 2 and missed line 5;
both blind readers flagged the duplicate independently. Line 5 was cut on its own (`f185r/l5/`) and read by both readers;
`f185r/assemble_rest90.py` drops the duplicate band and renumbers so passage ids are manuscript line numbers.

**Blind passes.** Two value-blind Sonnet readers (`blind_pass_brief_1572.md` + page note, crops only): `f185r/passA_rest90.tsv`
+ `passA_l5.tsv`, `passB_rest90.tsv` + `passB_l5.tsv`, 330 signs each after assembly. `reconcile_blind.py`: **318 of 330 agreed
(0.96)**, 12 splits, all settled by one value-blind Sonnet adjudicator (`f185r/adjudicate_in.tsv` -> `adjudicate_out.tsv`, 5 H,
7 M; weakest f184v_L04 pos 1, a struck mark, T81 or NONE). Final `f185r/passC_rest90.tsv`: **330 signs, 0 '?', 49 off-sheet**
(X_NEW 47, X_K 2). Lines: f184v L01 19 (after "a V.E."), L02 28, L03 29, L04 27 (ends in the gutter); f185r L01 30, L02 31,
L03 29, L04 30, L05 30, L06 32, L07 31, L08 14 (to "Mons. di Sanfre"). Reader A wrote one X_K as bare "K"; the assembler
normalises it.

**Whole letter so far** (`harvest/join_no90.py --out no90/passC_all.tsv`: f.184r passC + this portion, 554 signs).
Control (rule 3), `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py SEQ --map sign_id_map_1572_fit.json --err 0.12`
(printed key + T42=m; corpus it16dip; 200 value-shuffled keys; power control 20 windows at 12% injected error, three times
this portion's measured 4% disagreement and twice f.184r's 6%); logs in `harvest/no90/log/`:

| sequence | signs / letters | real key | shuffles mean / max (seeds 1, 2, 3) | z | rank of 201 | power control, err 0.12 |
|---|---|---|---|---|---|---|
| **this portion (f.184v foot + f.185r L01-08)** | 330 / 296 | **-0.889** | -1.518/-1.178; -1.527/-1.123; -1.514/-1.156 | 3.75; 3.88; 4.11 | **1; 1; 1** | 18/20, 17/20, 20/20 (z min 1.72, 1.19, 2.55) |
| **no.90 so far (f.184r + this portion)** | 554 / 521 | **-0.953** | -1.541/-1.246; -1.542/-1.252; -1.540/-1.244 | 4.22; 4.19; 4.20 | **1; 1; 1** | 20/20, 19/20, 20/20 (z min 2.23, 2.68, 2.80) |

T42 does not occur in no.90, so the printed and fitted keys decode it identically.

**Reading** (`tools/decode_key.py ciphers/nevers-birago-fr3251-1572`, job built by `harvest/build_decode_inputs.py no90 --seq
no90/passC_all.tsv`; `--check` exit 0, "reading up to date"; `harvest/reading_no90.txt`). Grades (rule 4): **whole no.90 so far,
554 tokens: H 0, C 0, S 455, M 29, I 0, U 70**; this portion 330: S 265, M 16, U 49 -- a cryptanalytic result (S = the published
key's value where both readers agreed, backed by the rank-1 control; M = settled by the adjudicator or a one-side-H split;
U = off-sheet signs, unkeyed, shown as '·'). This portion:

    no90 f184v_L01 | ···do·olesecutioned
    no90 f184v_L02 | a·i·a·io·haue·eintesoc·lacas
    no90 f184v_L03 | me·oransi·estain[qual]·sos·etoconi
    no90 f184v_L04 | b·stamoltisto·diti[et]dubitant
    no90 f185r_L01 | intensosit·ouinolete·esueaseto
    no90 f185r_L02 | s·iraglioinfauo·ede·i[bugonotti]a[qual]gua·gia
    no90 f185r_L03 | lauisaihaue·esc·iti·f·ancesco
    no90 f185r_L04 | ga·ate·o·ha·aip·esentatole·ete
    no90 f185r_L05 | ·e·sop·aintensentemenouenutone
    no90 f185r_L06 | sc·itomicosaalcuna·sncoha·echies
    no90 f185r_L07 | todana·i·souentione··anie·a·st·
    no90 f185r_L08 | ·tutoa·a·tato·

This worker's word breaks (not a second transcription, not graded): "... [l']esecutione ... ha [ve]d[ut]o ... inteso ... la cas[a]
... molti ... [d]ubitan[o] ... intens[o] ... serraglio in favo[re] de [ugonotti] a qual ... l'avisai haver scritto ... Francesco
... ha presentato le lettere ... sopra intensamente ... venuto ... scritto mi cosa alcuna ... che ... provisione ... danari ...
tutto ... stato". A recurring X_NEW sits where r is expected ("se·raglio", "sc·itti", "f·ancesco", "p·esentatole", "sop·a",
"sc·itto") -- not assigned here (no value-fit run; it would be grade I until a fit or the clerk sheet backs it).

**Judge** (secondary signal, `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/no90/...`):

    no90 so far:  FAIL language: score=-1.134, null_p99=-1.767, real_p05=-0.914, real_median=-0.826, mode=both, N=521
    this portion: FAIL language: score=-1.159, null_p99=-1.721, real_p05=-0.932, real_median=-0.827, mode=both, N=296

Shuffled-target control (`harvest/shuffled_judge.py`, fitted map, no90/passC_all.tsv, 20 seeds): **0 of 20 PASS**, mean -1.687,
min -1.769, max -1.613. The FAIL sits between the shuffled decodes and real_p05, the near-miss shape of the siblings; this
portion has 15% unkeyed signs (49/330), mostly the r-position X_NEW, which the letters file drops.

**What this settles.** The 1572 key reads no.90's f.184v foot and f.185r lines 1-8 (rank 1 of 201 at three seeds, power 17-20/20),
and the 554 signs read so far together (z 4.2). Still unread: f.185r lines 11-14 (after "dal re"; to "che" before "non si sa")
and 17-28 (from "cose sue da di qua, che" to "Chi io non so"), and the f.185v run (canvas 190 left, line 3). Flagged for a
separate verifier (rule 10).

Requests: gallica.bnf.fr 3 (info.json canvas 189; two native regions), 2 s apart, no challenge. Vision calls 5 (two blind
passes, two one-line passes, one adjudication) plus this worker's own looks. No credentials.

## NEVBIR-185B (2 Oct 2026, account 2 for the account-3 orchestrator): no.90 f.185r lines 10-12 and 15-25 + f.185v run read under the printed 1572 key + T42=m; all of no.90's cipher now read, rank 1/201

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-185b.md` (method of NEVBIR-185). Box 20:12-21:02 UTC, cap USD 5. No class, no
novelty wording (rule 10). Status stays `partial`.

**Line numbers.** Counted from the ink rows of the f.185r region, continuing NEVBIR-185's numbering (its L08 ends at "Mons. di
Sanfre"; L09 "qsta settimana" is clear): cipher on **L10** (after "dal re"), **L11**, **L12** (to "che"); L13 "non si sa",
L14 "pensa mai" clear; **L15** (after "cose sue da di qua, che"), **L16** (a short run, then "qste parti", then cipher),
**L17-L24**, **L25** (to "Chi io no so"). The brief's "lines 11-14 and 17-28" were estimates of the same runs: 3 + 11 lines
here, nothing left unread between "dal re" and "Chi io no so". **f.185v**: canvas 190 left, the run after "con tutto ciò".

**Fetch and crops.** Canvas 189 region `4780,980,2850,3420` re-fetched (one HTTP 500, one retry after 20 s: 200); canvas 190
`info.json` and the left page once (native, cropped locally). Crops gitignored (folder over its 30 MB line); `harvest/f185r2/REGEN.sh`
re-fetches and re-cuts both:

    python3 tools/iiif_lines.py --image $D/f185/src_f189_4780_980_2850_3420.jpg --out $D/f185r2 --prefix f185r --centres 1206,1308,1410,1785,1892,2045,2165,2289,2397,2544,2685,2810,2948,3080 --follow-slope 300 --slope-margin 15 --max-width 1250 --overlap 50 --debug
    python3 tools/iiif_lines.py --image $D/f185/src_f190_1850_1240_2350_200.jpg --out $D/f185v --prefix f185v --centres 100 --max-width 1250 --overlap 50 --debug

Debug overlay checked: 14 bands, no duplicated band. The first f.185v cut (centre on the prose line below) clipped the run; both
readers said so, it was re-cut (region above) and re-read by two fresh one-line passes.

**Blind passes.** Two value-blind Sonnet readers (`blind_pass_brief_1572.md` + `f185r2/page_note.md`, crops only; B read the lines
in reverse order): `f185r2/passA.tsv`, `passB.tsv` (f.185r 392 aligned, `reconcile_blind.py` **344 agreed, 0.88**, 48 splits, all
settled by one value-blind Sonnet adjudicator: `adjudicate_in.tsv` -> `adjudicate_out.tsv`, 20 H / 28 M, applied by
`f185r2/apply_adj.py`). f.185v: `passA_v.tsv`, `passB_v.tsv`, 21 aligned, **15 agreed (0.71)**, 6 splits settled by this worker
from the crop (not value-blind; graded M or left '?'): 8+s read as the sheet's "85" cell (T11), the ligature as T83, the
two-upright-on-base as T33; three left unkeyed. Final `f185r2/passC.tsv`: **412 signs** (f.185r 392, f.185v 20), 41 off-sheet or '?'.
Measured disagreement 0.12 (f.185r) / 0.29 (f.185v), 0.13 pooled.

**The r-position sign of NEVBIR-185 is the sheet's T83.** NEVBIR-185's readers coded a recurring "ae/oe ligature (x with e)" shape as
X_NEW 19 times (all where r belongs). The sheet cell T83 is that ligature, and this pass's two readers coded it T83 twenty times each
on f.185r; the printed 1572 table gives T83 = r. `harvest/subtype_xnew.py` relabels those 19 X_NEW rows as X_AE from the readers' own
shape notes (no value read); the test the brief asked for, r as a fitted value under the control:

| no.90 whole (966 signs) | real key | shuffles mean / max (seeds 1, 2, 3) | z | rank of 201 | power, err 0.12 |
|---|---|---|---|---|---|
| without (X_AE unkeyed) | -0.9449 | -1.560/-1.277; -1.560/-1.281; -1.559/-1.268 | 4.49; 4.51; 4.59 | **1; 1; 1** | 20/20 x3 (z min 2.83, 3.04, 3.39) |
| with X_AE = r, shuffled with the map (`--extra`) | -0.9300 | -1.603/-1.281; -1.604/-1.275; -1.615/-1.246 | 4.83; 4.71; 4.89 | **1; 1; 1** | 20/20 x3 |
| fit-aware (`harvest/fit_control_ae.py`: every shuffled key also gets its best letter for X_AE) | best fit **r**, gain +0.0149 | fitted shuffles mean -1.562, max -1.276 | 4.70; 4.71; 4.79 | fitted 1; 1; 1 -- **gain rank 9, 6, 9 of 201** (z 1.89-2.09) | -- |

Read: r is the best single letter for the sign and the key with it still ranks first, but the fit's own gain beats a free one-sign fit
on a wrong key only at about p 0.03-0.045. So the fit alone stays **grade M**; the stronger support is the shape (T83 cell, coded T83 by
this pass's readers), which this worker judged knowing the key, so it is not value-blind -- a verifier or the owner's sign sorter
should confirm the 19 tiles are T83 (`f185r/passC_rest90_ae.tsv` lists them). The committed reading keeps them unkeyed.

**Control (rule 3)**, `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py SEQ --map sign_id_map_1572_fit.json`, it16dip,
200 value-shuffled keys, logs `harvest/no90/log/`:

| sequence | signs / letters | real key | shuffles mean / max (seeds 1, 2, 3) | z | rank of 201 | power control |
|---|---|---|---|---|---|---|
| **this portion (f.185r L10-12, L15-25, f.185v)** | 412 / 456 | **-0.927** | -1.574/-1.235; -1.572/-1.282; -1.574/-1.269 | 4.25; 4.46; 4.53 | **1; 1; 1** | err 0.12 (measured): 19/20, 19/20, 20/20 (z min 2.19, 1.99, 2.87); err 0.26 (twice measured): 3/20, 7/20, 6/20 |
| **no.90 whole (all its cipher)** | 966 / 977 | **-0.945** | see table above | 4.49-4.59 | **1; 1; 1** | err 0.12: 20/20 x3 |

T42 does not occur in this portion either, so the printed and fitted keys decode all of no.90 identically.

**Reading** (`tools/decode_key.py ciphers/nevers-birago-fr3251-1572`, job from `harvest/build_decode_inputs.py no90 --seq
no90/passC_all.tsv`; `--check` exit 0, "reading up to date"; `harvest/reading_no90.txt`). Grades (rule 4): **whole no.90, 966 tokens:
H 0, C 0, S 731, M 124, I 0, U 111**; this portion 412: **S 276, M 95, U 41** -- a cryptanalytic result (S = the published key's value
where both readers agreed, backed by the rank-1 control; M = adjudicated, worker-settled, or one-side-H; U = off-sheet/unread, '·'):

    no90 f185r_L10 | [quello]credopensialgouerno[qual][turino]·[qual]conse
    no90 f185r_L11 | ntimento[qual]··[che]sare·epur·enmale[qual]
    no90 f185r_L12 | lui·han[che]buonosendoso·eno··o··ma·[quello]
    no90 f185r_L15 | nelguinealtridesomha·iatsu
    no90 f185r_L16.1 | ooritain
    no90 f185r_L16.2 | [quello]altra·entet[per]conto[qual]
    no90 f185r_L17 | religione·altrouisaranose·pre
    no90 f185r_L18 | confusioni·di·icultailtutiepre
    no90 f185r_L19 | giuditio···serui·io···[turino]fg[che]facese
    no90 f185r_L20 | intenderealareginafg·[turino][che]·g···tuto
    no90 f185r_L21 | dependealacasa[qual]·emoransi·fauo
    no90 f185r_L22 | risesi[turino]naognisuopoterehdare·e
    no90 f185r_L23 | fuori[qual]eropositoatio[per]unauolta
    no90 f185r_L24 | sedisprgnasinodelao·enione
    no90 f185r_L25 | chano[qual]costui[quello]
    no90 f185v_L01 | ·g[carmagnola]ese·prene·n·u···e

This worker's word breaks (not a second transcription, not graded): "quello credo pensi al governo ... Turino ... consentimento ...
che sar[à] ... pur ... male ... lui han che buono ... altri ... altra ... per conto ... religione altrove saranno se[m]pre confusioni
di[ff]icult[à] ... giuditio ... servi[t]io ... Turino ... che facesse intendere a la regina ... Turino che ... tutto depende a la casa
... favo[re] ... Turino ... ogni suo potere ... dare ... fuori ... proposito ... per una volta ... chi è costui quello"; f.185v
"... Carmagnola e se ...". "fg" twice (L19, L20) is an unread pair, left as decoded.

**Judge** (secondary, `tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file harvest/no90/...`):

    no.90 whole:  FAIL language: score=-1.069, null_p99=-1.794, real_p05=-0.898, real_median=-0.821, mode=both, N=977
    this portion: FAIL language: score=-0.998, null_p99=-1.731, real_p05=-0.911, real_median=-0.834, mode=both, N=456

Shuffled-target control (`harvest/shuffled_judge.py`, fitted map, `f185r2/passC.tsv`, 20 seeds): **0 of 20 PASS**, mean -1.605, min
-1.669, max -1.545. The FAIL sits between the shuffled decodes and real_p05, the near-miss shape of the siblings.

**What this settles.** All of no.90's cipher (f.184r runs, f.184v foot, f.185r, f.185v; 966 signs) is now read under the published
1572 key + T42=m, rank 1 of 201 at three seeds, power 20/20 at the measured error. Not settled: the 19 T83-shaped tiles of NEVBIR-185
(grade M, above), 111 unkeyed signs (digit shapes 4/7/8, square-with-dot, t-shape, raised-a m), and the judge gate. This portion is
flagged for a separate verifier (rule 10); the audits so far (VERIFY-NEVBIR-184, AUDIT2-NEVBIR per PROGRESS.tsv) cover the first 554 signs only.

Requests: gallica.bnf.fr 4 (canvas 189 region twice -- one HTTP 500, one retry; canvas 190 info.json and left page), >= 2 s apart, no
challenge. Vision calls 7 (two blind passes, two one-line f.185v passes, one adjudication; plus this worker's looks at overview and
overlays). No credentials.

English glosses (TRANSLATE-NEVBIR, 2 Oct 2026, grade I interpretation only, no token counts or key changed): harvest/gloss_no71.md, harvest/gloss_no86.md (covers reading_no86B.txt too), harvest/gloss_no90.md -- per line raw decode, word-split Italian with emendations marked, English gloss, 3-line summary.

VERIFY-NEVBIR-90REST (2 Oct 2026, verifier, separate session): rest of no.90 (742 signs) audited -- f.185r L10-25 N4 (first audit), f.184v-185r L01-08 N4 (second audit); f.185v run alone is a non-test (rank 35-38/201, power 0-2/20), its one S graded M; whole-letter control real score is -0.940 (the -0.945 in the NEVBIR-185B table came from a passage-id collision). See AUDIT.md.

## NEVBIR-OFFSHEET (2 Oct 2026, account 2 for the account-3 orchestrator): value-fit of the off-sheet signs on the pooled 1572 letters -- untested-by-this-tool (failed its own no.87 known-answer check)

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-offsheet.md`. Disk only: 0 vision calls, 0 requests to any host. No class,
no novelty wording (rule 10). Status stays `partial`. Box 21:32-21:4x UTC.

**Unit.** The readers coded every off-sheet shape as one id, X_NEW, so X_NEW is a bag of different signs, not one sign.
`harvest/offsheet/subtype_pool.py` (generalises `subtype_xnew.py`, value-blind) gives each X_NEW tile a shape class from the
two blind readers' own notes (21 regex classes: t-shape, ae ligature, digit 4/7/8, square, c-with-curl, t-with-3, m-with-raised-a,
...); A and B disagreeing leaves it X_NEW. 183 X_NEW tiles: 113 classed, 13 A/B disagree, 1 unaligned, 67 left X_NEW. The pooled
sequences it rebuilds (no.87 853, no.71 161, no.86 759, no.90 966 = 2,739 signs) equal the committed passC sequences sign for sign
(script exits 1 otherwise). Counts per class: `harvest/offsheet/subtype_counts.tsv` (X_T 26, X_AE 16, X_EQ 13, X_SQ 11, X_4 10, ...).

**Rule, fixed before any number** (`harvest/offsheet/PREREG.md`, 21:35 UTC): fit each class with >= 3 pooled occurrences to every
single letter and null, rest of the fitted map held (word codes excluded, GAPS3), score = decode_control.py's per-letter 4-gram
mean on it16dip (the spec's judge corpus) over all four letters; accept only if gain over unkeyed >= 0.002 AND gain above the 95th
percentile of 200 controls (the same number of random keyed letter positions relabelled as one pseudo-sign, hidden, refitted).
Method check: per no.87 off-sheet tile, the sheet value = the letter that maximises the decode's matched letters against the clerk
sheet (align_sheet.py statistic); PASS needs >= 70% right over accepted classes with a determinate sheet answer.

**Fits** (`harvest/offsheet/fit_offsheet.py`, seed 1, `fits.tsv`, log `fit_run_seed1.log`):

| class | pooled occ. | best | gain | control mean / p95 / max | rank of 201 | accepted |
|---|---|---|---|---|---|---|
| X_T (t-shape) | 26 | m | -0.0002 | -0.0082 / -0.0043 / -0.0011 | 1 | no (gain floor) |
| X_AE (ae ligature) | 16 | r | +0.0059 | -0.0046 / -0.0014 / +0.0001 | 1 | yes |
| X_EQ | 13 | null | -0.0005 | -0.0035 / -0.0010 / +0.0011 | 7 | no |
| X_SQ (square) | 11 | null | 0.0000 | -0.0028 / -0.0002 / +0.0008 | 6 | no |
| X_4 | 10 | null | -0.0011 | -0.0027 / -0.0001 / +0.0009 | 29 | no |
| X_8 | 8 | null | +0.0005 | -0.0018 / +0.0002 / +0.0014 | 11 | no |
| X_CC (c with curl, all no.86) | 7 | s | +0.0021 | -0.0015 / +0.0004 / +0.0014 | 1 | yes |
| X_7 | 5 | l | +0.0009 | -0.0007 / +0.0006 / +0.0019 | 9 | no |
| 9 others (X_S, X_T3, X_K, X_MA, X_STAR, X_BB, X_A, X_TRI, X_PCT; 3-7 each) | | | | | 41-181 | no |

**Known-answer check on no.87** (`known_no87.tsv`, 25 off-sheet tiles + 1 '?'; 7 with no determinate sheet value): the two accepted
classes (X_AE, X_CC) do not occur in no.87, so the pre-registered check **cannot run -- the brief's stop condition**. Secondary
numbers, not gating: over every fitted class, 4 of 16 tiles right (25%); over the classes that beat their control at rank <= 10
(X_T, X_AE, X_EQ, X_SQ, X_CC, X_7), 4 of 10 (40%). The t-shape class shows why: its fit (m) is right on the four f.178r/f.179r
tiles GAPS4 already entered as C, but the sheet reads h, r, h at its three f.178v tiles -- the readers' word "t-shape" covers at
least two signs, as GAPS4 suspected for the f.178v "8". The X_EQ, X_4, X_7, X_8 classes fit null; the sheet gives them f, n, a, a,
m -- the fit cannot see a letter where the n-gram gain of any one letter is below the noise of a few tiles. Also read off the
table: the 0.002 gain floor was miscalibrated (the controls' mean gain is negative, since filling a hidden tile joins two runs); a
control-only rule would have accepted X_T and still scored 4/7 on no.87, under the 70% bar. Both ways the method does not pass.

**Not applied.** No exceptions file, no key row and no committed reading changed (`decode_key --check` untouched): X_AE = r (16
tiles of no.90, rank 1/201, gain 0.0059 above every control) and X_CC = s (7 tiles of no.86) are pointers only, behind a method
that failed its check. X_AE = r agrees with NEVBIR-185B (the T83 shape, grade M there); this pooled control is stronger than its
fit-aware rank 6-9/201, but it is the same instrument family, so it does not lift the grade.

**Verdict for this step: untested-by-this-tool** (HYPOTHESES.md row). An n-gram value-fit on reader-note shape classes cannot name
off-sheet values at these counts; the off-sheet tiles need the shape settled before any fit (the clerk-sheet alignment of no.87 with
tools/interlinear_align.py, which gives the sheet's value per tile and so which shapes are one sign, then the owner's sign sorter),
not a further fit. Cost: disk only, about 3 minutes CPU.

## NEVBIR-87ALIGN (2 Oct 2026, account 2 for the account-3 orchestrator): C-grade 1572 key from the clerk's clear sheet of no.87

Brief `.claude/briefs/runs/2026-10-02-acct3-nevbir-87align.md`. Disk only: 0 vision calls, 0 requests to any host. No class, no
novelty wording (rule 10). Status stays `partial`. Box 21:49-22:2x UTC.

**Instrument.** `tools/interlinear_align.py align` (no private DP copy), with one new shared option, `--keep-fs` (the f == s fold
is for OCR of a printed long s; a clear sheet read by eye has none, and this cipher has distinct f and s signs; offline test added
to `tools/tests/test_interlinear_align.py`, default unchanged). Input built by `harvest/align87/build_pairs.py`: cipher side the
committed transcription `harvest/ciphertext_f178r/f178v/f179r.tsv` (853 signs); plain side the clerk sheet
(`harvest/f179r_sheet/decipherment_sheet.tsv`, GAPS4) cut into the three spans GAPS4 established and normalised to one convention
first (rule 3): struck words dropped, car.la -> carmagnola, ma.ta -> maesta, the per-sign "p" -> per, j -> i (v -> u is the
tool's fold). Codes: letter signs of the printed table Tnn -> nn (0/1 letter); the 8 word signs (T11 T15 T26 T29 T46 T78 T84
T89, the printed table's one structural fact used) -> 6000+nn (any chunk); every off-sheet tile and '?' its own code 1001-1025
(X_NEW is a bag of shapes, NEVBIR-OFFSHEET), so a tile's value comes from its own context only. Options `--floor 5000 --digits 4
--keep-fs --word-prior --prior harvest/align87/prior.tsv`: the seed is Tomokiyo's table **as printed (T42 = g)**, used for the
first EM iteration only; the counts are the sheet's. A flat start (no seed) does not converge on spans this long (162 of 853
'agrees', the word code 'qual' swallowing "ellaguard") -- the GAPS8 finding again.

**Result.** 764 of 853 signs (0.896) take a chunk that agrees with the sign's own majority over the passage; conflicts 54,
single 25, null/unaligned 10. Key: `keys/key_1572_clerk.tsv` (`harvest/align87/make_key.py`, `--check` exits 0), grade C per
row where agree >= 2 and agree/n >= 0.6, M otherwise; per-tile rows C only where both neighbouring signs agree, else M.

**Shuffled-alignment control (rule 3)**, `harvest/align87/control.py`, same tool, options and seed, `control.tsv`:

| variant | 'agrees' share | letter signs ending at the real run's value (of 41) |
|---|---|---|
| **real sheet** | **0.896** | 41 |
| sheet words permuted within each span, 20 seeds | mean 0.351, max 0.376 (real rank 1 of 21) | 20-30 |
| the three spans rotated over the wrong folios | 0.203 | -- |
| real sheet, seed's letter values permuted (wrong-seed), 20 seeds | mean 0.551, max 0.893 | 9 of 20 seeds reach 39-41 (agrees 0.890-0.893); 11 stay at 1-7 (0.256-0.294) |

The control can fail differently from the target (rule 3's orthogonality paragraph: word order is exactly what an alignment
uses). The seed does not manufacture the agreement (shuffled sheet with the right seed: max 0.376), and the real sheet pulls
nine of twenty wrong seeds back to the same key, to within two signs: the sheet carries the key.

**Against Tomokiyo's printed table** (rule 4: listed, never resolved by majority):

| sign | printed | clerk sheet (agree/n) | grade | note |
|---|---|---|---|---|
| T42 | g | **m** 11/12 (g 1) | C | confirms GAPS3's fit with period plain text; the one g is Guascogna, already exceptions_f178v I |
| T95 | s | **l** 8/8 | C | |
| T50 | c | **s** 7/8 (c 1) | C on no.87 | does NOT transfer: see the decode variant below |
| T52 | i | o 7/11 (i 4) | C (below the transfer rule) | split, left at printed i |
| T88 | g | e 2/4 (q 2) | M | GAPS3 left it undecided; still undecided |
| T46 | turino | 1 of 4 aligned to "turino" (others c, re, a long run) | M | the readers' T46 covers more than the word sign; image question |
| T98 | s | s 10/18 (d 7) | agrees, split | a d look-alike in the readers' T98, the error map's largest pair |
| T76 | n | n 17/22 (e 3) | agrees | |
| T64 | h | h 3/6 (l 2) | agrees, split | |

The other 36 of the 41 letter signs that occur in no.87 agree with the printed value (T17 still never occurs). Off-sheet tiles (25, no.87 only): the four t-shapes GAPS4 entered as m stay
m (two C, two M by the neighbour rule); the three f.178v t-shapes read h, r, h (NEVBIR-OFFSHEET's two-signs-in-one-class finding,
now at grade C for f178v L10/16 h); X_K = p, X_EQ = f and n (two different signs), X_STAR = n, X_S = a (L22), a further 12 per tile
in `keys/key_1572_clerk.tsv`; the f.179r line-end struck pair aligns to nothing (null, M). The f.178r L01 start ("che in di
bellaguarda") stays M throughout: the readers' first eight signs there do not match the sheet (GAPS4).

**Decode variant (pre-registered, `harvest/align87/PREREG.md`, fixed 21:55 UTC before any other letter was decoded).** Transfer
rule: a printed letter sign whose sheet value differs, n >= 3, agree >= 3, agree/n >= 0.75 -> T42 m, T95 l, T50 s
(`harvest/key_1572_clerkvar.tsv`); per-tile values never transfer. `tools/decode_key.py . --config decode_clerkvar.json` (writes
only `harvest/clerkvar/`; the printed-key readings are untouched; `--check` exit 0 on both configs). Per letter
(`harvest/align87/compare_variant.py`, output `compare_variant.txt`):

| letter | signs | printed + T42=m | clerk variant | tokens changed | judge (spec, same file shape) |
|---|---|---|---|---|---|
| no.71 f.139v | 161 | S 116 M 24 U 21 | C 3 S 113 M 24 U 21 | 4 (T50 3, T95 1) | -1.159 -> -1.137 (real_p05 -0.955) |
| no.86 | 759 | S 629 M 76 U 54 | C 10 S 619 M 76 U 54 | 10 (T50 8, T95 2) | -1.161 -> -1.152 (real_p05 -0.905) |
| no.90 | 966 | S 731 M 124 U 111 | C 14 S 717 M 124 U 111 | 15 (T50 10, T95 5) | -1.069 -> -1.073 (real_p05 -0.898) |

S/M/U move only by relabelling S to C; no U becomes readable (the U tokens are off-sheet tiles, which the rule does not transfer).
**T50 = s is wrong outside no.87**: in the three letters T50 sits in "per conto", "domestico", "con costan(za)", "capita",
"confusion", "credo", "carego" -- every one reads c under the printed value and is spoiled by s. So the no.87 T50 tiles are the
readers putting an s sign (most likely one of T57/T92/T98's shapes) under the T50 label, or a no.87-only use: a transcription
question for the image, not a key change. T95 = l is mixed: "accordarlo" (no.90 f184r L02) gains, "mandsto/mandlto",
"alcuna s n/l n" and "fauorise s/l i turino" are no better either way. No newly readable English fragment comes out of the
variant; the honest English summary is "the variant changes 29 letters across three letters and improves none of them clearly".
The committed printed-key readings stay the reference; the variant files are kept as the record of the test.

**What this settles.** (1) The clerk sheet, aligned sign by sign, confirms 36 of the 41 letter-sign values that occur in no.87 and T42
= m at grade C; (2) the two strong conflicts are T95 (l on all 8 no.87 tiles) and T50 (s on 7 of 8), and T50's does not survive
transfer -- it is a reader-label error on no.87, which is what an error map is for; (3) the off-sheet "t-shape" is at least two
signs (m on f.178r/f.179r, h/r on f.178v) at C. The per-sign reader error map is `harvest/align87/align_real.tsv` (status
`conflict:<majority>` per token: T50/s, T98/d, T52/i-o, T76/e, T64/l, T46). Next: the look-alike pass on the no.87 tiles labelled
T50, T98, T52 and T46 against the crops with this map as crib (`tools/lookalike_pass.py`, 1-2 vision calls, ~$2), which decides
whether T50-as-s is a reader label; T95 = l is applied in other letters only after that.

Cost: disk only, ~6 min CPU (control 3m52s). Requests 0.

## NEVBIR-NAMES (3 Oct 2026, account 2 for the account-3 orchestrator): whole-name gap fill -- no fill beats its controls

Brief `.claude/briefs/runs/2026-10-03-acct3-nevbir-names.md`. Disk only: 0 vision calls, 0 requests to any host. No class, no
novelty wording (rule 10). Status stays `partial`. Box 00:22-01:22 UTC.

**Idea tested (owner's, 3 Oct 2026).** Unread spans in nos.71/86/90 may sit where proper nouns belong; fit WHOLE names against the
letters fixed around and inside each gap (distinct from NEVBIR-OFFSHEET, which fitted single signs by n-gram score).

**Gazetteer, pre-registered** (`harvest/names/gazetteer.tsv`, 239 forms of 88 names/offices/places/groups, with
`gazetteer_src.txt` and the rule in `harvest/names/PREREG.md`, pushed in f38910be before any gap was listed). Sources per row:
(a) the no.87 clerk's clear sheet and the names previous workers took from the Birago/Ceppo letters' clear prose (AUDIT.md search
logs); (b) the Mémoires de Nevers 1665 pts 1-2 **only through the Gallica ContentSearch logs already in AUDIT.md** (Hautefort,
Sacremore, Pinerolo, Carmagnolle) -- the full text was not re-fetched; (c) the brief's context list, Italian and French spellings.

**Rule.** Gap = run of U/M tokens >= 3 (word signs and nulls are barriers). A form fits a window overlapping the gap by >= 3
tokens iff every S/C sign in the window agrees; >= 3 fixed letters matched; score = fixed matched + 0.5 x agreeing M. Controls
(rule 3; both change the letters the statistic reads, so both can fail): (i) 200 random gazetteers of it16dip/fr16 words, same
size and length distribution; (ii) 200 shuffles of the fixed letters among the fixed positions. A fill counts only above both
p95. `harvest/names/match_names.py` (seed 1), output `gaps_prereg.tsv`, `fills_prereg.tsv`, `summary_prereg.txt`.

**Result.** 22 gaps in the three letters (no.71 2, no.86 6, no.90 14). A gazetteer name is admissible at only 3 of them --
"gouerno" (no.86 f174v L19, 3.5), "sanfre" (no.90 f185r L17, 3.0), "danuilla" (no.90 f185r L21, 3.0) -- and none clears either
control (per-gap p95 of the random gazetteers 0-3.5, max up to 6.0; flank-shuffle p95 0-3.5). At 19 gaps no name fits at all,
while random words of the same lengths fit most of them. **No surviving fill; nothing graded; bonus check empty (no off-sheet sign
gets a value from a fill).** The three admissible fills read as chance on inspection too: the "danuilla" window is
"tuTo dEPEnDEA la casa" -- ordinary words already readable at M, echoing no.87's own clear "dependendo ... dalla casa de memoransi".

**Why the idea has little room here.** The unread signs are mostly isolated: U runs in the three letters are 125 of length 1, 16 of
length 2, 8 of length 3, 1 of 5+. Where names occur they are already read (Sanfrè, Carego, Geneura, baron des Adrets, Turino and
Carmagnola by word sign). A single off-sheet sign standing for a whole name would admit every name and cannot be tested by pattern;
it needs the sign's identity settled first (owner's sign sorter, NEVBIR-OFFSHEET's verdict) and then its contexts read together.

**English summary.** We fitted a pre-registered list of the people, places and offices Birago could have named into every unread
span of three or more signs in letters 71, 86 and 90; no name fits better than random words of the same lengths, so the
gaps are not, on this evidence, hidden names spelt out letter by letter.

Not done: (b) beyond the logged ContentSearch hits; fr.3252 f.47r (live NEVBIR-47C claim, 0.66 two-reader agreement). Next (not
started): once the sorter settles which off-sheet shapes are one sign, test "this sign = one name" by collecting each recurring
sign's contexts across nos.71/86/87/90 against the gazetteer, ~$1 disk only.

## TX-ATLAS-B72 (3 Oct 2026, account 2 for the account-3 orchestrator): one sign atlas for the 1572 key family

Brief `.claude/briefs/runs/2026-10-03-acct3-tx-atlas-b72.md`; folder `atlas/` (README there has every command). Scored
two ways: the clerk sheet directly (`atlas/score_no87.py`, written before TX-BENCH landed) and `tools/tx_bench.py`
once it landed mid-job (`atlas/tx_bench_atlas.txt`). No
committed reading or transcription was changed; the atlas is an input for TX-DECODE.

- **Segment** (`tools/glyph_atlas.py segment --debug`, 18 native region pages of nos.71-90 + fr.3252 f.117r, disk only):
  4,209 sign boxes, 474 marks. Overlays checked by eye: f.178v is cut cleanly into its 23 lines (675 boxes for 667
  read signs); f.178r's three sloping lines are mixed by the row-profile line split, and pages with prose (f.179r L4,
  f.139v, f.162r) carry prose boxes, which the naming reads as `_`.
- **Cluster** k=140 (over-split). **Naming:** no.87's boxes were mapped to the line-read tokens by a label-blind
  width DP (`atlas/no87_map.py`: 714 one-to-one, 26 two-boxes-to-one, 8 one-box-to-two); a tune tile (f.178v L01-L12)
  whose line-read sign decodes to the clerk's letter is a known answer (309 tiles), and names its cluster by majority
  (76 clusters). The other 64 clusters were named from exemplar sheets, one Sonnet call per sheet (4 calls):
  21 given a code, 9 MIXED, 34 prose/noise.
- **Classify** (`glyph_atlas.py classify`, extended: `--topk 3` writes k1-k3 with distance and vote share, `--holdout`
  keeps boxes out of the vote, `--page all`; test in `tools/tests/test_glyph_atlas.py`). Per-letter lattices in
  `atlas/topk/`.
- **err_true on no.87, held out** (f.178v L13-L23 + f.179r L01-L03, never used to name a cluster or vote; one value
  map `keys/key_1572_clerk.tsv` else the printed sheet, no exceptions; 376 of 398 held-out tokens mapped 1:1 and
  aligned to a clerk letter):

  | reader | err_true | wrong+unvalued |
  |---|---|---|
  | line-read reconciliation (committed ciphertext_*.tsv) | 0.056 | 0.080 |
  | atlas top-1 | 0.322 | 0.348 |
  | atlas top-3 (truth's value not among the three codes) | 0.261 | -- |

  Both wrong on 0.061; atlas top-1 = line-read label on 0.609.
  **tx_bench.py** (item birago1572-no87, eval split, the same 15 held-out lines; atlas boxes in x order, `_` boxes
  dropped, `atlas/topk/no87_heldout_bench.tsv`): **atlas top-1 err_true 0.162 (61/376, 95% 0.128-0.203)** against the
  committed line reads on the same lines **0.040 (15/376, 0.024-0.065)**. tx_bench is kinder to the atlas than the
  label-blind scorer because it aligns by edit distance on the labels and accepts any homophone in the truth set; its
  top atlas confusion is s <- T50 x15. **The atlas is far worse than the line reads on this
  hand**, and its top-3 misses a quarter of signs, so as built it cannot be the lattice that lowers err_true.
- **Why (measured, not tuned further):** leave-one-out kNN accuracy on the 309 known-answer tiles themselves is 0.754;
  nine HOG/size variants (cell 6/8/12, 9/12 orientations, size weight 0-3, PCA unit/shared) all land 0.728-0.754, so
  the limit is the tiles (48 px bitmaps of connected components: touching signs merged, broken strokes split, ~45
  classes from ~7 examples each), not the feature setting. Mapping shifts are a minor part (held-out kNN label matches
  the token's own label 225x, a neighbour's 77x).
- **Next (for TX-DECODE / TX-SORTER, not done here):** use the line-read label as k1 and the atlas k2/k3 as alternates
  only where the line reads split (the lattice is useful as a candidate source, not a reader); a better tile needs
  the line-read box positions (cut per token) rather than connected components; err_true here is on one hand's
  held-out lines only.

## TX-DECODE (3 Oct 2026, account 2 for the account-3 orchestrator): key-constrained lattice decode -- no.87 known answer, then f.144r, f.168 and f.117r re-tested

Brief `.claude/briefs/runs/2026-10-03-acct3-tx-decode.md`. Shared tool `tools/key_decode_lattice.py` (TRANSCRIPTION.md
step 6; test `tools/tests/test_key_decode_lattice.py`). Disk only: 0 requests, 0 vision calls. No reading committed, no
class, status unchanged (`partial`). TX-ATLAS-B72's top-k had not landed, so the brief's fallback ran: the top-k lattice
was built from the two blind line passes (A, B) plus `harvest/confusion_1572.tsv` by the tool's fixed `from-passes` rule
(reader weight H 1 / M 0.6 / L 0.3, alt 0.3x, 0.15x spread over the top-3 confusion neighbours, top 4 kept). The rule
and lam = 1 were committed (0b855b99) before the known-answer run. Printed key `harvest/key_1572_sheet.tsv` throughout (not
the clerk variant). Everything regenerates: `sh tx_decode/run.sh` (from harvest/), `sh .../tx_decode/retest.sh` and
`python3 .../tx_decode/shuffled_target.py` (from ciphers/).

**Known answer, no.87 (853 signs; truth = `align87/align_real.tsv` clerk-sheet value per committed position, 843 aligned).**
The committed ciphertext gives the position skeleton only; its signs are not candidates (8 f178r positions had no reader).

| decode | err_true (wrong) | wrong + U | changed vs top-1 | key rank /201 | z | shuffles mean / max |
|---|---|---|---|---|---|---|
| top-1 of the two passes | 0.0807 | 0.1151 | -- | 1 | 4.57 | -1.635 / -1.275 |
| lattice, lam 1 (pre-registered) | **0.0996** | 0.1507 | 82 | 1 | 2.46 | -1.099 / -0.847 |
| lattice, lam 4 (picked on f178v L01-L11) | 0.0712 | 0.1103 | 29 | 1 | 4.09 | -1.423 / -1.122 |

**The pre-registered setting failed the known-answer gate.** At lam 1 the language model overrides the readers: true error
goes up and z goes down, because the value-shuffled keys gain more from the freedom than the real key does. lam was then
swept on a tune split (f178v L01-L11) and the best value checked on the rest of no.87 (held out): top-1 0.0729 / 0.1267 ->
lam 4 0.0691 / 0.1228 (wrong / wrong+U), about 2 tokens. That is a small gain, chosen after the pre-registered run. **Limit:**
only 27 of the 97 top-1 errors or U positions have the clerk's value anywhere in the two-pass lattice (2.4 candidates per
sign), so 0.0807 -> about 0.08 with U is the most this lattice can give on no.87. The candidate set is the bottleneck; the
atlas top-k (TX-ATLAS-B72) is what can raise it. no.87's two readers disagree on 0.097 of signs (f178r + f179r).

**Synthetic power** (`--power-err`, 20 windows x 50 shuffles, two simulated readers each wrong with probability err, errors
drawn 80% from the confusion table; lam 4 unless stated):

| length, err | top-1 rank 1 (z median) | lattice rank 1 (z median) |
|---|---|---|
| 280, 0.08 | 20/20 (5.19) | 20/20 (5.75); lam 1: 17/20 (3.02) |
| 853, 0.08 | 20/20 (5.58) | 20/20 (6.38); lam 1: 19/20 (3.03) |
| 280, 0.25 | 6/20 (1.66) | **20/20 (4.24)**; lam 1: 8/20 (2.07) |

At err 0.08 top-1 is already at ceiling, so that row has no room to show a gain (rule 3). The gain is at the error level of
the unread letters. The simulation is generous to the lattice: its readers err independently, so the truth is usually in
the lattice. On no.87 the real readers' errors overlap (27/97 recoverable).

**Re-tests at lam 4** (fixed before these runs; printed key; f.144r and f.168 it16dip, f.117r fr16 as in NEVBIR-3252-B;
lattices from each letter's own passA/passB; 200 value-shuffled keys, seed 1; power at the letter's own length):

| letter | signs | A/B agreement (this tool's alignment) | top-1 rank / z | lattice lam 4 rank / z (changed) | lattice lam 1 rank / z | power lam 4, err 0.08 / 0.25 (top-1) | shuffled target, 5 seeds: lattice rank / z | judge (lam 4 text) |
|---|---|---|---|---|---|---|---|---|
| no.73 f.144r | 90 | 0.78 (70/90) | 22 / 1.28 | **1 / 3.10** (12) | 2 / 2.16 | 19/20, 20/20 (19/20, 5/20) | 17-58 / max 1.35 | PASS -0.945 (real_p05 -0.979, N 101) |
| no.85 f.168 | 122 | 0.90 (109/121) | 20 / 1.43 | **1 / 2.77** (11) | 1 / 2.55 | 20/20, 20/20 (19/20, 6/20) | 36-101 / max 0.92 | FAIL -1.019 (real_p05 -0.958) |
| no.77 f.117r (fr.3252) | 279 | 0.77 (210/272) | 10 / 1.63 | **1 / 3.66** (32) | 1 / 3.28 | 20/20, 20/20 (20/20, 16/20) | 4-64 / max 1.91 | FAIL -1.081 (real_p05 -0.903) |

On a position-shuffled lattice the real key never ranks 1 (best rank 4 of 201, z at most 1.91, against 2.77-3.66 on the
real order), so this control could fail and did. f.168's readers agree on 0.90 of signs, yet its top-1 ranked only 20 where the
err-0.08 simulation gives top-1 19/20. Either its reading errors overlap more than the simulation assumes, or the fit is
weaker there. Its rank 1 is the least secure of the three. The judge on the lattice decode of one shuffled target FAILs for all three
(-1.213, -1.301, -1.382), so the ARM-C1 voiding condition is not met at seed 100. The f.144r PASS is a lattice-chosen text:
12 of its 90 signs were chosen by the language model, so the PASS is partly the model's own preference.

**What this licenses.** Three letters that sat at rank 10-22 as reconciled single reads rank 1 of 201 when the decoder may
choose between the two readers' candidates. All keys, real and shuffled, have the same freedom, and the position-shuffled
control fails. That is evidence the printed 1572 key fits f.144r, f.168 and f.117r. It is **not** a reading. Every changed
position (`tx_decode/<letter>_lam4.decode.tsv`, column `changed`) is grade S at best. lam 4 was tuned on no.87, and the
pre-registered lam 1 failed there. Candidates for a verifier, not results:
- f.144r: `quellomprimagiortatenperqualdiquellollrosatheirperbodiaqualcolmezodileurperatopiudicediragineroquello`
- f.168: `cheisisafacuanuatomoltoconlorialtehesopraquellopaftisolechenguantoilprocederesisiitantoastidiisaamemadatosaelfefoiiilifoquellom...`
- f.117r: `mguilamulguenpsenuaardesannintentiondeconueniraunspoursuoisngouerneentdepirceguisestpersoreguiserendroitsusfacile...`

**With TX-ATLAS-B72's top-k (landed during this job; `harvest/tx_decode/atlas_mix.py`, `atlas_mix.json`).** Scored on the
atlas's 388 held-out no.87 signs (`atlas/no87_box_token.tsv` split heldout; the atlas vote excluded them; lam 4; NB those
lines overlap the f178v L01-L11 lines lam was tuned on, so this is not held out from the lam choice):

| lattice | top-1 err / +U | lattice err / +U | truth in lattice | key rank / z (lattice; top-1) |
|---|---|---|---|---|
| two-pass | 0.0722 / 0.1031 | 0.0670 / 0.0979 | 0.933 | 1 / 4.09; 1 / 4.57 |
| atlas only (k1-k3, vote share) | 0.3918 / 0.3918 | 0.3814 / 0.3814 | 0.704 | 1 / 3.03; 1 / 3.06 |
| two-pass 0.8 + atlas 0.2 (weight fixed before the run) | 0.0670 / 0.0979 | 0.0670 / 0.0954 | 0.946 | 1 / 3.88; 1 / 4.55 |

On this hand the atlas adds about 1 point of coverage and about 1 sign in 400 of accuracy. The decoder then recovers about
half a point. Neither is near the 5% target. The rest of the error is signs that neither reader nor atlas offers. Next:
(1) the three re-tests above with the 0.8/0.2 atlas mix (atlas/topk/no73.tsv, no85.tsv, fr3252-no77.tsv; ~$1, disk only),
recording whether rank 1 holds; (2) a verifier pass on the
changed positions of f.144r against the image crops, each graded S or rejected (~$2, one vision call per letter on the
changed tiles only).

## NEVBIR-ERRTRUE (3 Oct 2026, account-1 worker for LANE-A1): f.144r, f.168 and the short-run pool re-powered at the benchmarked true error

Brief `.claude/briefs/runs/2026-10-03-acct1-nevbir-errtrue.md`. `tools/intake_gate_check.py nevers-birago-fr3251-1572` at
09:2x UTC: "partial (line 1) -- edition/page or full-text-search citation found within 6 lines". Disk only: 0 requests, 0
subagents. No reading committed, no class, status stays `partial`.

**Why.** NEVBIR-144/168/POOL ran their power controls at the two-reader *disagreement* (0.24, 0.13, 0.15). TRANSCRIPTION.md:
disagreement is not error. The benchmarked true per-sign error of this hand and pipeline is TX-DECODE's no.87 known-answer row
"top-1 of the two passes": **err_true 0.0807, wrong+U 0.1151** (BENCHMARK-TX.tsv `birago1572-no87`).
**Pre-registered** in `harvest/errtrue/PREREG.md` (commit 7ccfc4c5, pushed before any score): bracket E1 0.081, E2 0.115,
E3 0.121 (1.5x); gate power >= 16/20 at all three; supplementary E4 = err_true + the leaf's own off-sheet fraction (which the
no.87 benchmark, 3% off-sheet, does not carry). Same tool, map, corpus, sequences and seeds as before:
`python3 ../ceppo-nevers-fr3251-1570s/harvest/decode_control.py SEQ --map harvest/sign_id_map_1572_fit.json --corpus it16dip
--shuffles 200 --windows 20 --seed 1 --err E`; outputs `harvest/errtrue/*.txt`.

| letter | signs / letters | real key rank /201 (seeds 1-4) | z | power E1 0.081 | E2 0.115 | E3 0.121 | E4 (leaf) |
|---|---|---|---|---|---|---|---|
| no.73 f.144r | 90 / 94 | 4, 6, 3, 5 | 1.77-1.88 | 14/20 (z med 2.52, min 1.34) | 8/20 (1.85, 1.09) | 9/20 (2.00, 0.38) | 0.24: 4/20 |
| no.85 f.168 | 121 / 117 | 36, 31, 41, 35 | 0.91-1.00 | **17/20** (3.74, 1.92) | **16/20** (3.15, 1.38) | **16/20** (2.92, 1.38) | 0.17: 11/20 (2.31, -0.03) |
| pool f.144r+f.168+f.174r | 296 / 308 | 4, 1, 2, 2 | 1.98-2.13 | **19/20** (3.99, 2.12) | **19/20** (3.39, 2.41) | **19/20** (3.35, 2.51) | 0.19: 8/20 (2.56, 0.90) |

Real-key figures reproduce the committed NEVBIR-144/168/POOL numbers exactly (inputs unchanged). Supplementary, **post hoc**
(not in the pre-registration; power at seeds 2 and 3, `harvest/errtrue/supp_*.txt`): f.168 E1 19/20, 17/20 (all seeds 53/60),
E3 12/20, 16/20 (all seeds 44/60 = 0.73, under the 0.8 gate rate); f.144r E1 14, 15 (43/60), E3 8, 10 (27/60).

**Verdicts under the pre-registered rule.**
- **f.144r (no.73): too-short still.** Power fails at every bracket level (14/20 at err_true). Real key rank 3-6.
- **f.168 (no.85): control-backed negative for the printed 1572 key + T42=m on the committed passC read, at err_true.** Power
  clears 16/20 at E1-E3 (seed 1) and the real key sits at rank 31-41, z 0.91-1.00 -- below the *minimum* z of every one of the
  120 power windows at err <= 0.12 (lowest 1.06). Three limits, stated with it: (i) at the upper bracket the post-hoc seeds put
  power at 44/60, so the negative is firm at err_true and marginal at 1.5x; (ii) at E4 (0.17, counting the 11 off-sheet signs as
  error) power is 11/20 with a window as low as z -0.03, so it holds only if the true error on this leaf is near the no.87
  figure; (iii) rule 2: it is a negative on this transcription, and a different instrument disagrees -- TX-DECODE's
  key-constrained lattice (choosing between the two readers' candidates, lam 4 tuned on no.87) ranks the same key 1/201 on f.168
  (z 2.77, position-shuffled max 0.92). Read together: either f.168's single reconciled read carries well above no.87's error, or
  the printed key does not fit no.85. The lattice result points to the first; this test does not decide between them.
- **Pool: neither.** Power 19/20 at every bracket level, so the test has power; the real key ranks 1 at one seed of four and 2 at
  two (rank 1-2 at a majority, rank 1 at none of the majority), which the pre-registration names "neither". Its z (2.0-2.1) sits at
  or below the lowest power window at E1-E3 (2.12-2.51): the pool scores like a right key read at an error above err_true, which is
  what E4 (8/20, z median 2.56) shows. f.168 is still the drag (NEVBIR-POOL leave-one-out).

No per-token grades (rule 4): nothing is read. No judge run (no new text). Report only: no novelty wording (rule 10).

## TXD-HOLDOUT (3 Oct 2026, account-1 worker for LANE-A1): held-out control for TX-DECODE's lam-4 rank-1 on f.144r, f.168, f.117r

Brief `.claude/briefs/runs/2026-10-03-acct1-txd-holdout.md`; pre-registration `harvest/tx_decode/holdout/PREREG.md` (pushed
0b9a9955 before any score); full tables `harvest/tx_decode/holdout/RESULTS.md`; script `holdout.py` beside it. Disk only.
- (c) Re-tuned on no.87 lines not used for the lam-4 choice (f178v L12-23, f178r, f179r; 521 signs): lam 1/2/3/4/6/8 give
  54/39/38/**36**/37/37 wrong; lam 4 chosen again, by one sign. No re-run needed.
- (a) Printed key vs 200 partition-preserving relabelings + 18 letter rotations at lam 4: 0 of 218 reach it on any letter
  (z vs W1 4.64 / 6.78 / 6.92). Post-hoc (not pre-registered): the same gate also passes on 9 of 15 position-shuffled
  lattices (z there at most 2.87 / 3.64 / 4.65), so its PASS mostly measures letter-frequency fit; the value-shuffle
  control of TX-DECODE (never rank 1 on a shuffled target) stays the discriminating one.
- (b) lam sweep, rank among 200 value shuffles: f.144r 2,1,1,1,2,12 (tuned-only by the pre-stated label); f.168 1,1,1,1,1,5
  (robust); f.117r 1 at all six (robust).
- (d) No re-run text; TX-DECODE's judge figures stand (f.144r PASS -0.945 vs real_p05 -0.979, shuffled -1.213; f.168 FAIL
  -1.019 vs -0.958, shuffled -1.301; f.117r FAIL -1.081 vs -0.903, shuffled -1.382).
Verdict lines: **f.144r: lam-4 rank 1 survives held-out control** (by rule; weakest: rank 1 only at lam 2-4).
**f.168: lam-4 rank 1 survives held-out control.** **f.117r (fr.3252): lam-4 rank 1 survives held-out control.**
This licenses the lam choice for these three re-tests, not any decoded text: no reading committed, every changed position
S at best, no class. Next for all three: the verifier pass on the lam-4 changed positions against the crops (~$2 each).

## A1-POSNULL (3 Oct 2026, account-1 worker for LANE-A1): position-shuffled-lattice null for the printed 1572 key at lam 4
Brief `.claude/briefs/runs/2026-10-03-acct3-a1-wave7.md` job 1; PREREG `harvest/tx_decode/posnull/PREREG.md` (d05de564, before
any score); results `posnull/RESULTS.md`, `posnull.json`. Replaces TXD-HOLDOUT's gate (a), which passed on 9/15 shuffled lattices.
200 position-shuffled lattices per leaf (same per-position candidate sets, positions permuted), printed key, lam 4. Gate: real
rank 1/201 among value-shuffled keys AND real score > shuffled p95.
- f.144r: real -0.945 vs shuffled p95 -1.096 (max -0.956); rank 1; shuffled rank-1 2/200. **PASS** (thin: 0.011 over max).
- f.168: real -1.019 vs shuffled p95 -1.299 (max -1.209); rank 1; shuffled rank-1 0/200. **PASS.**
- f.117r (fr.3252): real -1.081 vs shuffled p95 -1.334 (max -1.297); rank 1; shuffled rank-1 0/200. **PASS.**
Licenses only that the real sign order carries the key's language signal beyond the position-shuffled null; no reading, no
grade change (a separate verifier would be needed), nothing above S, no class. Next as before: the verifier pass on the lam-4
changed positions against the crops (~$2 each).

## A1-BIR-EYE (3 Oct 2026, account-1 worker for LANE-A1): blind eye check of the TX-DECODE lam-4 changed positions

Brief `.claude/briefs/runs/2026-10-03-acct3-a1-wave7.md` job 4. Folder `harvest/tx_decode/eye/`. The pre-registration
(PREREG.md, positions, blind question files, orientation with every question masked) was pushed at 632c8786 before any crop
was shown. One blind Opus reader per leaf saw only line crops (cut by tools/iiif_lines.py from the committed native regions,
in the scratchpad), the value-blind sheet, A/B candidates in random order and masked orientation. It was never told about the
key or which candidate was which. 3 vision calls, 0 requests.
Gate: the key-implied pick rate on changed positions must exceed the decoy-swap rate, with binomial p < 0.05 at
p0 = (d+1)/(n+2).
- f.117r (fr.3252 no.77): 27/32 vs 3/32, p 8.9e-21, **PASS**.
- f.168 (no.85): 7/11 vs 1/11, p 0.0004, **PASS**.
- f.144r (no.73): 5/12 vs 0/12, p 0.001, **PASS** (7 of 12 changes not backed).
- Pooled: 39/55 vs 4/55.

There are 28 S candidates for a verifier (key-implied picks at H/M), listed in `eye/score.json`. No grade was applied, no
reading committed and no novelty classed. Caveats are in RESULTS.md: one reader per leaf; the f.117r bands were tighter than
the original crops, which affects both arms. The decode's lattice changes are supported by the image at these positions. That
is not a reading.


## A1-BIR-VERIFY (3 Oct 2026, account-1 verifier for LANE-A1, a separate session): A1-BIR-EYE's 28 S candidates checked
Full record in `nevers-birago-fr3251-1572/harvest/tx_decode/eye/verify/RESULTS-VERIFY.md` (prereg 594c0f26). The decoy draw
reproduces (same seed, same counts) but was not matched on ambiguity: A1-BIR-EYE's decoys were easy positions. A new blind reader with an
ambiguity-matched decoy arm found: f.117r (re-cut at the original band height) G1 27/32 vs 5/32 PASS, matched 24/26 vs 15/30 PASS, so
19/19 kept; f.168 G1 10/11 vs 1/11, matched 5/5 vs 3/7 PASS, so 5/5 kept; f.144r G1 6/12 vs 0/12 but matched 5/8 vs 6/12 FAIL, so 0/4 kept
(dropped: L05:32, L04.1:7, L05:7, L06:7). The 24 kept positions are applied at S in `decode_verify.json` (decode --check exit 0). Grades:
f.117r H0 C0 S179 M74 I0 U26; f.168 H0 C0 S90 M22 I0 U10; f.144r H0 C0 S40 M36 I0 U14. Judge FAIL on all three (f.117r -1.294 vs
real_p05 -0.907, f.168 -1.238 vs -0.975, f.144r -1.454 vs -0.955). This is a cryptanalytic result, not a reading. Next: a third blind reader on
f.144r's 4 dropped positions plus matched decoys, ~$3, only if new crops (native re-capture) are available.

## BIR-ROUND2 (3 Oct 2026, account-3 worker): round-2 lattice on the M tokens, and the U-token check against the printed key
Full record in `nevers-birago-fr3251-1572/harvest/tx_decode/eye/round2/RESULTS-ROUND2.md` (prereg 923a783f, pushed before any score).
With A1-BIR-VERIFY's 24 S positions pinned, H positions pinned and look-alike partners added at the M positions, the lam-4 lattice
changes 13 / 6 / 13 positions (f.117r / f.168 / f.144r). All of them were already asked in A1-BIR-EYE or A1-BIR-VERIFY and not
kept. There are **0 new positions on every leaf, so the round is untestable at this N** under the pre-registered rule, and no reader call
was made. Nothing changed: decode --check exit 0, grades f.117r H0 C0 S179 M74 I0 U26, f.168 H0 C0 S90 M22 I0 U10, f.144r H0 C0
S40 M36 I0 U14, and the judge lines are as A1-BIR-VERIFY's (FAIL on all three). Position null on the round-2 base: PASS on all three: real key rank 1/201 and real S above every one of 200 shuffled lattices (f.117r -1.081 vs p95 -1.521, z 4.97 vs shuffled p95 1.42; f.168 -1.019 vs -1.425, z 3.61 vs 0.96; f.144r -0.998 vs -1.197, z 3.08 vs 1.56; 111 s). Pinning the 24 S and H positions keeps the key separable from the null (A1-POSNULL z on the unpinned lattices: 3.66 / 2.77 / 3.10), but this gate licenses nothing without reader questions.
The A/B lattice instrument is exhausted on these leaves at lam 4. Next is a different instrument: an open-choice blind re-read of the
M positions against the full sign sheet, which adds candidates, and then the lattice (~3 vision calls, ~$5).
U tokens (`round2/u_tokens.tsv`, report only): the printed key has no null and 8 word or name codes. A digit pair "4 7" recurs on
f.117r L02 and f.144r L04.1 (both readers), and "1 6" appears on f.144r L05. Their shape class is the printed digit name codes
(85/86/89), but they are not in the printed key; values unknown. An "up triangle over cross" resembles quello (T84) in reverse
orientation. No other off-sheet shape matches a printed code. Next: pooled 47/16 count across the 1572 leaves, disk only, ~$1.
Cryptanalytic result only; no reading claimed, no novelty classed.
## BIR-OPEN (3 Oct 2026, account-3 worker): open-choice blind re-read of the M positions, then lattice lam 4
The full record is in `nevers-birago-fr3251-1572/harvest/tx_decode/eye/open/RESULTS-OPEN.md`. The prereg (e5076ee1) was pushed before any crop or score.
This is the different instrument BIR-ROUND2 named. Each reader saw a masked orientation, the native line crops and the whole sign sheet, and
was asked for any sheet id, OTHER or U at each of the 74 f.117r / 22 f.168 M positions. Equal sign-matched H decoys were mixed in. There were 3 fresh blind Opus readers.
- Calibration on the H decoys: f.117r 70/74 (0.95), f.168 22/22 (1.00), both PASS (gate 0.80). T60 decoys read T60 9/10 and 2/2.
- Change rate on M targets: f.117r 41/74, f.168 12/22. The lattice (open answers added as candidates) agrees at H/M on 24 / 6. Posnull PASS on
  both (rank 1/201; z 4.88 / 3.25).
- New S candidates (value changes): f.117r 12 (T60->T86 x5, T65->T51 x5, T95->T51, T98->T18). f.168 4 (T60->T86 x2, T56->T97, T19->T33).
  They are in `open/exceptions_open_<leaf>.tsv` (`open/decode_open.json`), decode --check exit 0.
- The M targets included A1-BIR-VERIFY's 24 exception positions. Open reads replicate 11/19 (f.117r) and 2/5 (f.168). 11 conflict, mainly
  T95 vs T51 (6) and T83 vs T24 (2). The T65/T95/T51 three-way is unsettled, so it goes to the owner's sorter. A1's rows are left unchanged.
- **Grades unchanged** in the tokens file (f.117r H0 C0 S179 M74 U26, f.168 H0 C0 S90 M22 U10). decode_key.py grades an exception on a
  conf-M transcription row as M. So A1's 24 "applied at S" and these 16 are value changes, not S grades. Flagged for the orchestrator.
- Judge: f.117r FAIL -1.224 (before -1.301; real_p05 -0.899). f.168 FAIL -1.150 (before -1.242; real_p05 -0.992). The gain is partly circular.
Cryptanalytic result only. No reading claimed, no novelty classed.
Next: owner sign sorter on T65/T95/T51 and T83/T24 (focus list = the 11 conflicts + 6 T5x survivors). Then decide whether open-read
survivors on conf-M rows may carry grade S (tool/grade policy, orchestrator). Then f.144r with the same instrument (~3 vision calls, ~$5).

## BIR-APPLY (3 Oct 2026, account-3 worker): orchestrator grade policy applied to the f.117r / f.168 lattice corrections
Policy (account-3 orchestrator, 3 Oct 2026, answering BIR-OPEN's flag): a lattice correction is S only where two independent blind
instruments agree on the sign: A1-BIR-VERIFY's two-option check (ambiguity-matched decoys) AND BIR-OPEN's open-choice re-read (H-decoy
calibrated). Everything else stays M.
- Files: `nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/` -- `exceptions_apply_f117.tsv` (S 11, M 20), `exceptions_apply_f168.tsv`
  (S 2, M 7), `decode_apply.json` (`exception_grade_overrides_conf: true` on the f.117r and f.168 jobs; the f.144r job unchanged). The reason
  column names the instrument(s): "A1 and BIR-OPEN agree" (S), "A1 vs BIR-OPEN conflict (owner sorter)" (M, 11 rows), "BIR-OPEN single
  instrument only" (M, 16 rows). Values are BIR-OPEN's (`open/`) unchanged; only grades move, so the reading text is identical to
  `open/reading_<leaf>_open.txt` below its header.
- `python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --config ciphers/nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/decode_apply.json --check`:
  exit 0, "reading up to date". Per leaf (rule 4): **f.117r H 0, C 0, S 190, M 63, I 0, U 26** (was S 179, M 74);
  **f.168 H 0, C 0, S 92, M 20, I 0, U 10** (was S 90, M 22); f.144r unchanged (S 40, M 36, U 14).
- Judge (letters only, brackets and separators stripped, the same extraction as BIR-OPEN; values unchanged, so the scores are BIR-OPEN's):

      $ python3 tools/judge_plaintext.py specs/birago-fr3252-f117.json --file <f117 letters>
      FAIL language: score=-1.224, null_p99=-1.813, real_p05=-0.899, real_median=-0.782, mode=both, N=246
      FAIL - birago-fr3252-f117 (a PASS is a gate for a verifier, not a reading; rule 10)
      $ python3 tools/judge_plaintext.py specs/nevers-birago-fr3251-1572.json --file <f168 letters>
      FAIL language: score=-1.15, null_p99=-1.622, real_p05=-0.992, real_median=-0.824, mode=both, N=111
      FAIL - nevers-birago-fr3251-1572 (a PASS is a gate for a verifier, not a reading; rule 10)
- Sorter focus: `harvest/tx_decode/eye/open/sorter/focus.tsv` (+ README): 17 tiles, the 11 conflicts (T95/T51 x5, T66/T76, X_NEW/T84,
  T13/T64 on f.117r; T83/T24 x2, T51/T95 on f.168) and the 6 f.117r BIR-OPEN-only T65/T95->T51 moves, with crop paths from the two existing
  sorters' signs.tsv. f117 L09 and f168 R03 have one tile fewer than transcribed positions, so those rows may be one tile off and L09.30
  has no tile. Ready for the orchestrator to build and publish; nothing published here.
Cryptanalytic result only (no H or C). No reading claimed; not classed for novelty.
Next: owner sign sorter on the focus list; then f.144r with the BIR-OPEN instrument (~3 vision calls, ~$5).

## BIR-OPEN-144 (3 Oct 2026, account-3 worker): the BIR-OPEN open-choice instrument on f.144r
Brief `.claude/briefs/runs/2026-10-03-acct3-bir-open.md` (section BIR-OPEN-144). Pre-registered at 88df4b16 before any crop or score; details
`harvest/tx_decode/eye/open/RESULTS-OPEN-144.md`. One blind Opus reader (1 vision call) saw 36 M targets and 36 H decoys against the full sign sheet.
- Calibration 35/36 = 0.97 PASS. The one decoy miss is L04.1:7 T60->T86 (H). Target change rate 9/36. Posnull PASS (rank 1/201, S -1.049 vs p95 -1.239).
- 3 survivors (reader + lattice): L05:19 and L05:26 T95->T51, L04.1:12 T78->T86. A1-BIR-EYE did not ask any of them -> **M** (single instrument).
- Grade policy (open read = A1-BIR-EYE pick): **S** at L06:7 T36 and L05:32 T83. These are A1's key-implied picks, already the transcribed sign, so the value is unchanged.
  This applies the policy to positions where the lattice sign equals the transcription sign; the pre-registration did not name that case, logged post-hoc.
  Four open/A1 disagreements and L04.1:7 (both blind reads T86 against the conf-H T60, not applied) go to `harvest/tx_decode/eye/open/sorter/focus.tsv`
  (8 rows appended, kinds conflict/open-only).
- decode_key.py `--config harvest/tx_decode/eye/open/decode_open144.json --check` exit 0: **f.144r H 0, C 0, S 42, M 34, I 0, U 14** (was S 40, M 36).
- Judge (specs/nevers-birago-fr3251-1572.json):
      before FAIL language: score=-1.454, null_p99=-1.6, real_p05=-0.955, real_median=-0.828, mode=both, N=94
      after  FAIL language: score=-1.418, null_p99=-1.614, real_p05=-0.954, real_median=-0.817, mode=both, N=91
  The gain is partly circular (the lattice uses an Italian LM). This is a cryptanalytic result only: no reading, no novelty classed.
Next: owner sign sorter on the appended f.144r rows (the orchestrator republishes); after the decisions, sign_sorter_apply + decode --check, ~$1.

## BIR-OWNER (3 Oct 2026, account-3 worker): the owner's partial sign-sorter picks scored as a third reader on f.117r, f.168, f.144r
Full record: `nevers-birago-fr3251-1572/harvest/tx_decode/eye/open/sorter/RESULTS-OWNER.md` (prereg 8bbb3861, pushed before any score).
The owner's save (partial; the owner's words: "doesn't mean they're right") went through `tools/sign_sorter_apply.py` unchanged: 488 tiles, 68 moved,
58 taken out, 11 bad cuts, 5 set aside. Grade rule: S where the owner's sign equals a blind instrument's read at that position (A1-BIR-VERIFY,
BIR-OPEN, BIR-OPEN-144), M owner-only, U a move into a new pile. Gate: (b) the owner's picks must beat (a) the base and the p95 of (c), 200 random
same-size change sets drawn from the lattice's top-k look-alikes.
- f.117r: 24 changes (S 3, M 11, U 10). (b) is worse than the base and inside the control: FAIL.
      a  FAIL language: score=-1.215, null_p99=-1.797, real_p05=-0.907, real_median=-0.791, mode=both, N=266
      b  FAIL language: score=-1.32, null_p99=-1.776, real_p05=-0.893, real_median=-0.782, mode=both, N=256   (control p95 -1.234; rank 118/201)
- f.168: 14 changes (S 1, M 9, U 4). (b) is worse than 198 of 200 random draws: FAIL.
      a  FAIL language: score=-1.149, null_p99=-1.64, real_p05=-0.975, real_median=-0.821, mode=both, N=114
      b  FAIL language: score=-1.418, null_p99=-1.622, real_p05=-0.992, real_median=-0.824, mode=both, N=111  (control p95 -1.146; rank 199/201)
- f.144r: 17 changes (S 1, M 7, U 9). (b) beats the base and the control: PASS (rank 2/201). Applied in `.../sorter/decode_owner144.json`, decode
  --check exit 0: H 0 C 0 S 39 M 32 I 0 U 19 (was S 42 M 34 U 14).
      a  FAIL language: score=-1.418, null_p99=-1.614, real_p05=-0.954, real_median=-0.817, mode=both, N=91
      b  FAIL language: score=-1.266, null_p99=-1.614, real_p05=-0.954, real_median=-0.817, mode=both, N=91   (control p95 -1.346)
- Pooled: (a) -1.239, (b) -1.333, control p95 -1.255: FAIL. The owner's picks agree with the blind machine reads 1-5 times in 6-24 per leaf and
  instrument. On the T65/T95/T51 conflicts the owner mostly gave a third answer (T65 or a new pile). Of the 25 focus tiles the owner touched 21
  (15 moved, 5 aside, 1 bad cut). Those letter scores are averages over the 4-gram LM. The f.144r gain is on one leaf of three and still far
  below real_p05.
Cryptanalytic result only. No reading claimed, H 0 C 0, no novelty classed.
Next: what to sort next, ranked by score gain in `.../sorter/sort_next.tsv`: f.144r L06.1 (bad cut, recut), L05.7 (aside), L04.1.1, L05.6;
f.168 R03.6, V03.5, V03.23; f.117r gains are small (<=0.02). Also a native re-capture of the 11 bad-cut tiles. Per the README, a fourth look goes to the
owner-only disagreements, the 11 M picks on f.117r and 9 on f.168. Sorting the new piles (T60-c holds 7 tiles across leaves: 4 from T65, 1 each from T95, T36 and T60) against the sheet
would turn U back into values, ~$1 apply after the next save.

## TX-ALTS (4 Oct 2026, account-3 lane A3V parent worker): a/b? alternatives carried into the decode lattice -- not adopted

Brief `.claude/briefs/runs/2026-10-04-acct3-tx-additions.md` (TX-ALTS; research/TRANSCRIPTION-PRACTICE-2026-10-04.md #3).
Gates pre-registered in `harvest/tx_alts/PREREG.md` before any new pass or decode. No reading, no class, status unchanged.
Tool: `--keep-alts` on `tools/key_decode_lattice.py from-passes` and `tools/reconcile_passes.py` (a sign written `a/b?`
is first choice a + alternative b; every reader-written alternative is exempt from the 0.02 floor and the top-4 cut).
Default paths unchanged: `sh tx_decode/run.sh` regenerates TX-DECODE's files byte for byte. Two Sonnet subagent vision
calls (one per page, line crops only, the existing 9 crops each) under the a/b? pass rule (`harvest/tx_alts/pass_brief_alts.md`),
blind, value-blind. Everything regenerates: `python3 tx_alts/test2.py` (from harvest/) -> `tx_alts/test2.json`.

**Test 1 (disk only), existing A/B passes with --keep-alts:** truth in lattice 27/97 (unchanged: the old passes' `alt`
entries were never being cut); lam 4 err_true 0.0712 (60/843, unchanged).

**Test 2, f178r L01-03 + f179r L01-03 (179 truth-aligned signs), pass N under the a/b? rule beside the existing pass B:**

| lattice | top-1 wrong+U | truth in lattice at top-1 errors | lam 4 err_true (wrong / wrong+U) | lam 1 err_true |
|---|---|---|---|---|
| CURRENT (A, B) | 27 | 2 / 27 | 0.045 / 0.151 | 0.084 / 0.196 |
| FIRST (N first choice only, B) | 38 | 13 / 38 | 0.056 / 0.156 | 0.078 / 0.196 |
| ALTS (N with every alternative, B; --keep-alts) | 35 | 12 / 35 (0.34) | 0.061 / 0.156 | 0.089 / 0.196 |

Paired, same signs: ALTS vs FIRST at lam 4 **0 fixed / 0 broken** (p 1.0); at lam 1 3 / 3 (p 0.66). ALTS vs CURRENT at
lam 4 0 / 1. **G1 FAILS** (0.34 < 0.50), **G2 FAILS** (no paired gain): not adopted, per the research note's own rule
("coverage alone with no err_true gain counts as not adopted"). The rule did change what the reader writes: of pass N's
own first-choice errors, the truth sits in N's own written alternatives at 12 of 29 (f178r 7/19, f179r 5/10), against
0 of 18 for the old pass A's `alt` column on the same lines. But N's first choice was worse than A's (29 vs 18 errors),
B's errors carry no alternatives, and the key + language model at lam 4 did not use the extra candidates. Limits, stated
in PREREG before the run: six lines, about 27-38 errors, one pass per page, so a null is low-power, not a negative of the
rule; and the f178r crops cut each line's tail at the bottom edge (the reader read L01/L02 tails from the next line's
crop and lost L03 after pos 24), which inflates N's error on f178r. Cost of the vision step: 2 Sonnet calls.
Next (one line, not done): if retried, read a/b? on both passes (A and B) of a whole letter so both readers' errors carry
alternatives, with f178r re-cut (`tools/iiif_lines.py --debug`, taller region for the slope); same gates.
