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

## Remaining gaps (LIKELY-3, 2 Oct 2026; updated GAPS-nevers-birago 04:3x UTC and GAPS3-nevers-birago 05:3x UTC, 2 Oct 2026)
Read so far: 667 of roughly 800 signs of no.87 f.178 (all 23 lines of f.178v: L01-L10 LIKELY-3, L11-L23 GAPS-nevers-birago 04:3x UTC; the joined leaf under the fitted key (GAPS3, 05:3x UTC, section above) rank 1/201 z 4.84, judge FAIL -1.032 vs real_p05 -0.905; f.178r's 2 and f.179r's 3 cipher lines not cut), control-backed; 0 of the 7 target letters ff.138-184
- f.178r foot (2 cipher lines) and f.179r head (3 lines) - blocker: not-attempted; canvases 181 and 182 right page need a native region each (2 gallica requests); next: iiif_lines regions + the same pipeline, ~$3
- ff.138, 144, 152, 160, 168, 174, 184 (nos. 71-93) - blocker: not-attempted; HARVEST-D2's recipe (1200 px per canvas until the cipher is found, 2-4 requests a letter, offset drifts +1 to +3) then the same pipeline per leaf; next: locate and read f.144 (the fullest page of signs per the row), ~$8 a letter
- the q homophone, T88 and the 13 off-sheet signs - blocker: open-codes; the value-fit ran (GAPS3, 2 Oct 2026 05:3x UTC, section above): T42 g -> m (S, seven m-words against one g-word; judge -1.074 -> -1.032, z 4.60 -> 4.84), T70 confirmed g, T88 (3 occurrences) undecided (q scores worst, no two-word support; the one q-word 'guecta' also carries a c/s look-alike), X_NEW (7, all at word boundaries) invisible to a letter fit, X_EQ 2 too few; T17 (m) still never occurs -- a sheet-cell or clerk question for an image check; next: a transcription pass on the logged look-alike pairs (T50/T92 c/s, T42/T17, T18/T98, T51/T95) with the fitted key's reading as the crib, 1 vision call per half-leaf, ~$3
- the tipped-in decipherment (canvas 183) - blocker: needs-physical-access; written face not photographed (NEV-C1, LANE NEV follow-up); REQUEST.md / ASKS row 78 BnF reproduction batch covers it

## Escalation (2 Oct 2026)
- [x] siblings: no.87 is itself the key's own witness leaf and was read first; the six other 1572 letters are the next units
- [n/a] clear-pages: f.178v is cipher throughout; the prose of f.178r and f.179r frames the passage and was used only to confirm content
- [x] known-keys: the printed 1572 key applied, rank 1 of 201 shuffled keys, power 20/20
- [ ] print: print_check.py on 2-4 decoded phrases runs once the judge gate is met (the g-sign fit lifted the leaf from -1.074 to -1.032 against -0.905; the look-alike transcription pass or more text is the next lift)
- [x] key-rebuild: one-sign value fits, not a rebuild -- run (GAPS3, 2 Oct 2026): T42 g -> m, T70 g, T88 and the off-sheet signs undecided at their counts; the key reads the leaf at rank 1/201 before and after
- [x] image-check: native region, debug overlay checked by eye, right edge re-fetched once when L07-L10 were clipped
- [n/a] retry: no reset, challenge or failed fetch to retry (the one 500 was this worker's malformed URL)
Verdict: keep going: 3 internal gaps; cheapest next: f.178r foot + f.179r head (2 gallica requests, same pipeline under the fitted key, ~$3), then the look-alike transcription pass on f.178v with the reading as crib (~$3), then f.144
