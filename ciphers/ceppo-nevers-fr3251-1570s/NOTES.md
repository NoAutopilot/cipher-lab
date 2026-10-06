partial

INTAKE-3251, 27 Sept 2026: solver-ready intake only (Layout, no reading, no decoding, no class). Built from
KEY-ADJACENT.tsv row 2 (SCOUT-OWN-6, 27 Sept 2026) and `sources/cryptiana/web/nevers.htm` (local mirror,
read in full by this worker, not re-fetched, section id=BnFfr3251). Tomokiyo, verbatim:

> "BnF fr.3251 contains letters partially in cipher from Lodovico Birago to Duke of Nevers (1570-1572)."
> "From September 1570 to May 1571, they used the Ceppo-Nevers Cipher below (reconstructed from BnF fr.4702)."

# Ceppo-Nevers Cipher letters (BnF fr.3251), Lodovico Birago to Duke of Nevers, Sept 1570-May 1571

All from Saluzzo. Digits, per Tomokiyo (KEY-ADJACENT.tsv row 2, `token_shape` column).

## Undeciphered (this folder's targets, no "(with decipherment)" marking on nevers.htm)

| folio | no. | date |
|---|---|---|
| f.11 | no.6 | 14 September 1570 |
| f.21v | no.11 | 12 October 1570 |
| f.35 | no.18 | 15 November 1570 |
| f.87 | no.45 | 9 May 1571 |

(f.87 no.45 is not in KEY-ADJACENT.tsv row 2's own three-folio summary or the SCOUT-OWN-6 ROOM line, but the
brief for this job named it explicitly as a fourth target: nevers.htm lists the whole September 1570-May 1571
run as ff.11, 21v, 27, 35, 39, 82, 87, and only 27/39/82 carry "(with decipherment)" -- f.87 is not one of them.)

## Witnesses (known-plaintext siblings -- carry a period decipherment, the calibration set per the fr7129 lesson)

| folio | no. | date |
|---|---|---|
| f.27 | no.14 | 6 November 1570 (with decipherment) |
| f.39 | no.20 | 30 November 1570 (with decipherment) |
| f.82 | no.42 | 20 March 1571 (with decipherment) |

## Excepted (already in this repository, a DIFFERENT cipher, not part of this folder)

f.119 no.63, Saluzzo, 13 November 1571: nevers.htm says "In November 1571, they used a numerical cipher (not
deciphered)" -- a distinct, third cipher from the Ceppo-Nevers one above, already covered by
`ciphers/birago-nevers-1571` (status: open, no key found). Not duplicated here.

## The key

> "In 1572, the year of Birago's death, they used a new cipher, which can be reconstructed from the
> decipherment attached to no.87 is called the Nevers-Birago Cipher (1572) herein."

(That sentence names the OTHER cipher, covered by the sibling folder `ciphers/nevers-birago-fr3251-1572`.) This
folder's own key, the Ceppo-Nevers Cipher, is reconstructed by Tomokiyo from a different volume, BnF fr.4702:

> "(BnF fr.4702) Fols.36-37 are letters from Cesare Ceppo to the Duke of Nevers. One has interlined
> deciphering, which allows reconstruction of the cipher as follows (called "Ceppo-Nevers Cipher" herein).
> This in turn allows reading of the undeciphered letter "io sono avisato via di Milano et ..." but not quite."

The printed table itself is the image `nevers_add1.png`, embedded in nevers.htm immediately after that
paragraph -- see "Key blocker" below; it was not transcribed this session.

## Check-solved header (not a formal check-solved pass -- see "What remains" below)

What has been checked, by whom, when:
- **Community list.** Tomokiyo's `nevers.htm` names all four target folios above and does not mark any of them
  "(with decipherment)" -- read in full by this worker, 27 Sept 2026, local mirror, not re-fetched.
- **Sibling correspondence, same shelfmark.** `ciphers/birago-nevers-1571/NOTES.md` (LANE CX, 25 Sept 2026) ran a
  full six-source check-solved sweep on this exact sender-recipient pair (Birago to Nevers) and its finding on
  point 1 applies here without change: *"no published edition of Birago's letters to Nevers exists"*, confirmed
  by two web searches, not merely assumed. That file also confirms DECODE has no record for fr.3251 at all
  (`records-non-decrypted-2026-09-24.tsv` and Aymeloglu's DECODE mirror grepped for "birago"/"3251", zero hits),
  and that Bourdeau's own `birago/NOTES.md` and `profile.json` (`prior_solution.exists: "no"`) found no sibling
  solution either, after sweeping all 118 remaining fr.3251 openings for a matching cipher design.
- **Solver-repository cross-check.** `sources/cryptiana/READABLE.tsv`'s own row for `unsolved.htm` quotes
  Bourdeau's `SOLVED_CATALOGUE.md` directly: *"Birago and Ceppo to Nevers (about 13 letters)... catalogue
  318... Read in part... ff. 11, 21v, 35, 87, 138-174, 184... have no published reading"* -- Bourdeau
  independently lists this exact set of folios (both this folder's four and the sibling folder's seven) as his
  own open, unread work, which corroborates Tomokiyo's own "not deciphered" wording rather than merely repeating
  it (a second, independent source naming the identical folio list as unsolved).

What remains before any class (rule 10) or any deep-work brief:
- A formal `.claude/briefs/check-solved.md` pass proper (this intake job is Layout only, not check-solved) --
  `tools/intake_gate_check.py ceppo-nevers-fr3251-1570s` should be run before any deep-work brief; the citation
  above (full-text read of nevers.htm, no printed edition to open) is written to satisfy that gate's shape, not
  as a substitute for the formal pass.
- The catalogue's own record for BnF fr.3251 (`archivesetmanuscrits.bnf.fr/ark:/12148/cc49712p`) has not been
  read by this worker for a fuller description or availability flag beyond the ark already used by
  `ciphers/birago-nevers-1571`.
- Once a reading exists: `tools/print_check.py` on the decoded phrases (rule 10; CLAUDE.md README common tail).

## Key blocker: resolved (KEY-IMG-3251, 27 Sept 2026)

`keys/key_ceppo_nevers.tsv` is transcribed and on disk: 55 hand-drawn symbol cells (48 letter homophones across
19 of 22 letter columns -- b, x, y carry none -- plus 1 "et" word-sign and 6 null signs), from `nevers_add1.png`
(fetched from `cryptiana.web.fc2.com/code/nevers_add1.png`, manifest in
`sources/cryptiana/web/manifest_2026-09-27-keyimg.tsv`). Two independent blind Sonnet subagent reads, mechanically
merged: 56 of 58 rows agreed cell-for-cell (grade AB); 2 rows (both in column s, rows 2 and 3) had the position
agreed but the exact hand-drawn shape not fully resolved between the two passes (grade M). No column/row
placement disagreement on this table (contrast the sibling folder's y/z mix-up). `tools/key_design.py` reads it
as `usable=yes`, design_family `homophonic` (20 distinct letters, ~2.5 homophones mean) -- consistent with
Tomokiyo's own description of the system. KEY-OFFICES.tsv and KEY-DESIGN.tsv both carry rows for this key;
`tools/key_design.py --check` passes.

**Next step:** transcribe the cipher passages of the four target folios (two blind passes) and apply
`keys/key_ceppo_nevers.tsv` with a 20-shuffled-key control (rule 3); reading to a verifier.

**Next step:** transcribe the cipher passages of the listed folios (two blind passes) and apply
keys/key_<name>.tsv with a 20-shuffled-key control; reading to a verifier. (Blocked on the key-table fetch
above until then.)

## NEV-C2 witness calibration (27 Sept 2026)

Per `.claude/briefs/runs/2026-09-27-lane-nev-owner-c2-calibrate-ceppo.md`. **FAIL at the pass bar** (agreement
0.70 / z>=4 not reached), on the only witness that yielded any clerk plaintext at all. Status stays `open`.
No target folio (f.11, f.21v, f.35, f.87) touched; no class, no novelty wording, no grades assigned.

**f.27 (no.14, 6 Nov 1570).** Canvas 28 confirmed by eye (ink foliation '27' on the right page; offset +1
holds, consistent with the four points already established elsewhere in the volume). The cipher passage is
about 1.5 manuscript lines, ending "...come feci intendere all'Ecc.a V.ra" and continuing onto the next line
before "il che si può assai credere" resumes. Unlike the sibling group's f.178 (NEV-C1, no gloss found at
all), f.27 genuinely does carry a clerk decipherment: a small, cramped interlinear gloss squeezed into the
line space below the second cipher line's signs, covering the WHOLE passage in one run rather than one gloss
line per cipher line. Confirmed present by this worker directly (contrast-enhanced native-resolution crops,
`images/f27/f27_L03_s1.jpg`/`f27_L03_s2.jpg`) and independently by the plaintext subagent -- but even at
Gallica's maximum native resolution for this canvas (8424x5832), the gloss's individual letterforms mostly
blur together: the plaintext subagent read only "?? [s]pe? i[t]o ??????" at confidence L
(`witness/witness_f27_plain.tsv`), which normalizes to 6 legible letters ("speito") out of an estimated
25-39 signs' worth of gloss. A second independent zoom/contrast pass by this worker (not a subagent call)
did not improve on this; the interlinear hand is simply drawn far smaller than either the ordinary prose or
the cipher signs, at the limit of what the source image can resolve.

Sign read (subagent b, `witness/witness_f27_signs.tsv`): lineA (the cipher tail on the "V.ra" line) 16 signs,
lineB (the following line's cipher) 22 signs, 38 signs total after the reconciliation fix below. Blind check
(subagent c, per the fixed-seed 30 percent line sample -- `random.seed(1)` over `['lineA','lineB']` picked
`lineA`): 17 signs on lineA (`witness/witness_f27_blind_lineA.tsv`).

**Key-row indexing bug caught and fixed before scoring.** Both subagent (b) and subagent (c) independently
numbered `key_row` by the key file's absolute line number (counting the 12 leading `#` comment lines and the
header row) instead of the 1-based DATA-row number the brief and `tools/decode_witness.py --help` specify --
a shared, mechanical off-by-13 error, not a real disagreement. Caught by this worker cross-checking every
numeric `key_row` value's `shape_note` text against the key file's own sign description at
`raw_row - 13`: all 33 numeric entries across both files matched their shape description word-for-word once
shifted, confirming the pattern rather than a coincidence, and none of the shifted values fell outside the
valid 1-58 range. Both files corrected in place (subtract 13 from every non-`?`/non-`nNN` `key_row`) before
any scoring; worth a line in a future brief or in `tools/decode_witness.py`'s own docstring, since this is
the second time a 1-based "data row, not file row" convention has needed an explicit worked example (the key
file's own header/comment-line count is easy for a subagent given only the file, not the convention, to
miscount).

**Reconciliation** (`witness/reconcile_f27.tsv`): after the indexing fix, (b) and (c) agreed on 12 of 15
one-to-one sign comparisons on lineA (excluding the one 2-vs-1 segmentation split below) --
**80.0% sign-level agreement**, the honest reader-error measure this step exists to produce. Four points
settled by this worker looking directly at the native crop (not a subagent call):
1. **Segmentation** (b's pos 4, a single "36"-look mark b called "plain arabic numerals... unlike the
   surrounding cursive homophones"): direct inspection (`images/f27/recon_pos4b.png`) shows the "3" and "6"
   shapes drawn in the *same* cursive ink weight as every other homophone sign, not a distinct numeral hand --
   resolved as **two** signs, agreeing with (c)'s independent read (key rows 12/e and 17/h).
2. **b:9(d) vs c:?** -- resolved for **9/d** (b), a clean single-bar oval distinguishable from the two-bar
   mark next to it (`images/f27/recon_pos7_10.png`).
3. **b:? vs c:45(t)** -- resolved for **45/t** (c); the same "oval loop, long diagonal tail" shape recurs
   later in the line at a position both passes already agreed was row 45 (`images/f27/recon_pos10_11.png`).
4. **b:48(u, "stacked figure-8") vs c:33(q, "two connected humps")** -- resolved for **33/q** (c); the mark
   is two loops connected side by side opening upward ("w"-like), not stacked vertically
   (`images/f27/recon_pos16.png`).
One mark (both passes' position 9, "oval crossed by two close parallel bars") stays genuinely unmatched --
both independently punted on it and direct inspection confirms it is a real two-bar variant, distinct from
the one-bar row-9/d shape next to it, with no confident match in the 58-row table.

**Score** (`witness/witness_f27_signs_final.tsv`, the reconciled 39-sign pooled reading, against the single
6-letter clerk gloss, no `--sample-lines` since the gloss run cannot be honestly split by cipher line):

```
full passage: real key 0.5000 (3/6 aligned letters); 20 shuffled keys mean 0.5833 sd 0.1118 min 0.3333 max 0.8333; z -0.75; rank 11 of 21
```

**FAIL, decisively, on both bar conditions** (agreement 0.50 < 0.70; z -0.75, nowhere near +4; the real key
ranks 11th of 21, indistinguishable from the shuffled floor). This is not a finding against the key: with
only 6 clerk letters to align against, the test has essentially no power either way (rule 3's own headline
paragraph, applied to the clerk-letter count rather than the shuffle-control's N) -- the honest statement is
that f.27 could not calibrate this key, not that the key is contradicted. `witness/key_rows_ceppo.tsv` (58
rows) shows the same: every row's confirmed/contradicted count is a handful at most, too small to grade any
individual homophone.

**Rows confirmed / contradicted at this sample size** (from `key_rows_ceppo.tsv`, informational only given
n=6 clerk letters): row 19 (i) and row 30 (o) each confirmed once; rows 6(c), 9(d), 12(e), 13(e), 17(h),
23(l), 26(n), 27(n), 28(o), 30(o), 31(p), 33(q), 42(s), 43(s), 45(t), 47(u), 48(u) each contradicted 1-4
times. None of this is a usable per-row grade at n=6 aligned letters -- listed per step 8's "either way, list
the rows confirmed and contradicted", not as a claim about any row's correctness.

**f.39 (no.20, 30 Nov 1570).** Canvas 40 (f.39r) and canvas 41 (f.39v left page) confirmed by eye (ink
foliation '39' on canvas 40's right page; offset +1 holds here too). The letter closes on f.39v, "Da Saluzzo
il 30 novembre 1570", signed Lodovico Birago -- matching no.20 exactly, confirming this is the whole letter.
Its cipher passage is much longer than f.27's: about 7 lines at the foot of f.39r continuing about 5 more
lines onto f.39v, a dense, evenly-spaced block (some sign-groups underlined, plausibly a name/word-code
convention) with **no interlinear gloss anywhere** -- checked directly and by a contrast-enhanced zoom; the
line pitch is uniform throughout with no extra half-line gap a squeezed-in gloss would need, unlike f.27's
visibly taller/messier third line. Also checked f.40r (the following leaf) at contrast-enhanced zoom for a
loose/tipped-in decipherment sheet, on the sibling folder's f.178/179 precedent (`nevers-birago-fr3251-1572`
NOTES.md, NEV-C1): none found, only scattered ink dots, a later pencil-style X, and bleed-through from the
facing leaf's own prose. **FAIL at the plaintext read (a)** for this witness, same shape as NEV-C1's finding
for the sibling group's f.178 -- subagents (b)/(c) were not run for f.39 since there is nothing to align a
sign transcription against (brief step 8, "either way").

**f.82 (no.42, 20 March 1571) -- overview only, not conclusive.** Canvas 83 confirmed by eye (ink foliation
'82'; the facing left page f.81v carries a dated note "Da Salluzzo li 20 marzo 1571", matching no.42's date).
f.82r's own cipher passage (about 2 lines, mid-page) shows the same uniform, tightly-spaced-line signature as
f.39 at this 1000px overview -- no obvious extra interlinear row, unlike f.27 where the extra row was visible
even at 1000px once looked for. This is **not** a confirmed negative: this job's whole 8-request gallica
budget was spent locating and reading f.27 and f.39 before reaching f.82, so no native-resolution crop was
fetched here, and the 1000px overview is exactly the resolution at which f.27's own gloss was nearly
invisible before a native crop revealed it. Named next step for a follow-up worker with a fresh request
budget: one native-resolution crop of f.82r's cipher block (`tools/iiif_lines.py --ark btv1b9060248g --canvas
83 --region ... --out ciphers/ceppo-nevers-fr3251-1570s/images/f82 --prefix f82 --debug`) before concluding
no decipherment exists on this witness either.

**Verdict.** The Ceppo-Nevers key (`keys/key_ceppo_nevers.tsv`) is **neither confirmed nor contradicted** by
this job: the one witness that yielded any clerk plaintext (f.27) yielded too little (6 letters) to test
anything, and the other two witnesses named "with decipherment" by Tomokiyo either show no decipherment on
their accessible leaves (f.39, checked thoroughly) or were not reachable at native resolution within this
job's request budget (f.82, checked only at overview). This mirrors the sibling group's NEV-C1 finding
(no legible witness on Gallica for `key_nevers_birago_1572.tsv` either) closely enough that both keys in this
BnF fr.3251 pair may simply be harder to calibrate from Gallica alone than the fr7129 precedent this lane's
brief was built from. `tools/decode_witness.py` itself is now exercised end-to-end on real data for the
first time (NEV-C1 could not run it at all); no bug found beyond the key-row indexing convention noted above.

**Named next steps, in order of expected value:** (1) a native-resolution crop of f.82r per the note above --
cheapest, and the only remaining "with decipherment" witness untried at full resolution; (2) if f.82 also
fails, treat both fr.3251 keys as uncalibratable from the surviving Gallica witnesses and consider a
control-backed decode of a target passage itself as the fallback (the same fallback NEV-C1's orchestrator
follow-up named for the 1572 key: "the key of record against 20 shuffled keys, with the language judge, run
as a target-style test and labelled as such") -- appropriate here only after (1) is exhausted, since it
substitutes a weaker test for a witness-backed one and should not be reached for by default; (3) a specialist
or higher-zoom re-shoot of f.27's own gloss (the BnF's own reading room, or a different exposure/angle) is the
only way to recover more than 6 letters from the one witness that is known to carry a real decipherment, but
is outside this job's access (a REQUEST.md/ASKS.md matter for the person, not a repeated cloud fetch against
the same source image).

**Requests:** gallica.bnf.fr 8 in this job (the full allowance): canvas 28 at 1000px (1 connection reset,
retried once per the good-citizen rule), canvas 28 info.json, one malformed-URL request (this worker's own
typo, a doubled `ark:/12148/` prefix -- HTTP 500, fixed on this worker's side, no retry needed since the
fault was not the server's), canvas 28 native-resolution region crop via `tools/iiif_lines.py`, canvas 40 at
1000px, canvas 41 at 1000px, canvas 83 at 1000px (8th and last). All >=2s apart, descriptive script
User-Agent, one at a time. Subagents: 3 (plaintext read, careful sign read, blind check), all image-review
only, no credentials, no AskUserQuestion, no novelty wording, owner not named.

## NEV-C3 witness calibration, f.82 (27 Sept 2026)

Per `.claude/briefs/runs/2026-09-27-lane-nev-owner-c3-calibrate-f82.md`. **FAIL at the pass bar** (agreement
0.70 / z>=4 not reached on either the f.82-alone or the f.82+f.27-pooled run), but this witness IS legible --
the first "with decipherment" witness in either fr3251 group (NEV-C1's f.178, NEV-C2's f.27/f.39) that yields
a real interlinear gloss AND lets the full calibration pipeline run end to end without a plaintext-read dead
end. Status stays `open`. No target folio (f.11, f.21v, f.35, f.87) touched; no class, no novelty wording.

**Fetch and crops.** One Gallica IIIF region fetch (`f83/pct:55,25,43,7.5`, canvas 83 = f.82r, confirmed by eye:
ink foliation '82'; facing f.81v carries "Da Salluzzo li 20 marzo 1571", matching no.42's date), HTTP 200 on
the first try, no retry needed -- 1 of the job's 3-request allowance. `tools/iiif_lines.py --debug` located 4
manuscript-line bands but its own auto-cut crops split each cipher line's gloss row from its sign row (the
gloss sits in the *trough* between two detected line-centres, not as its own peak) -- confirmed by eye against
the debug overlay, and per the brief's own fallback the gloss+cipher pairs were hand-cut with PIL instead: for
each of the 3 cipher-bearing manuscript lines (line1 = "...per il S. Biagio" then cipher signs to the end of
the line; line2 = a full line of pure cipher; line3 = a second full line of pure cipher, running to the page's
right margin with no prose resuming on that line -- prose resumes only on the next full line), one y-range
covering that line's own gloss + sign rows, split into 4 overlapping x-segments at 2x zoom
(`images/f82/f82_pairN_sN.jpg`). The auto-cut `f82_L01..L04` files were deleted as superseded (not usable,
gloss split in half); `images/f82/manifest.json` documents both the detection and the hand-cut boxes.

**Gloss read (subagent a), two attempts.** First pass on the gloss+cipher pair crops came back **all
illegible** (0 confident letters, confidence L on all 3 lines) -- the tiny interlinear marks read as
ambiguous ink strokes, distinguishable from the clearly-legible ordinary prose on the same page. Rather than
accept this as this witness's final word (per rule 3's caution against a negative from under-tried material,
and the direct precedent of NEV-C2's f.27, where a first-pass framing initially missed a gloss later
confirmed present), this worker cut a second, tighter set of crops isolating ONLY the gloss row (excluding
the cipher-sign row below it) in narrower ~620px source slices at 3x zoom (`images/f82/gloss_retry/`, 21
files) and resumed the SAME subagent (not a new one -- still within the 3-subagent cap) with the new material.
The retry recovered **6 confident letters total** (line1: 0; line2: "m" + 2 "o"s; line3: 3 "o"s), up from 0,
confirming the framing/resolution of the first crops had genuinely understated legibility -- but the subagent
kept confidence L throughout ("most marks... remain tick/caret/numeral-like flecks rather than resolvable
cursive letters... I did not bump to M/H just to match the expectation that the new crops would read much
better"), and separately flagged that several ambiguous marks look more like small numerals than letters,
raising an open question (not resolved by this job) about whether this interlinear layer is a full
letter-by-letter plaintext gloss or partly a reference/position annotation. `witness/witness_f82_plain.tsv`
holds the second-pass reading.

**Sign read (subagent b).** 114 signs across the three lines (34 H-confidence), matched against
`keys/key_ceppo_nevers_numbered.txt`'s 58 rows, gloss row explicitly excluded from this pass.
`witness/witness_f82_signs.tsv`.

**Blind check (subagent c) and reconciliation.** `random.seed(1)` over `['line1','line2','line3']` picked
**line1**. (c) transcribed 22 signs for line1 (7 H); (b) transcribed only 15 for the same line -- a genuine
segmentation/completeness disagreement, not merely a shape disagreement. Direct inspection of the source
crops by this worker (`witness/reconcile_f82.tsv`) confirms: (1) both readers agree on the two anchor signs
this worker could verify by eye -- the line's first cipher sign (a three-hump cursive "m", key row 11) and a
large "X" cross roughly two-thirds through the line (key row 47); (2) (b)'s very first entry (a "plain round
closed loop") has no counterpart in (c) and is most likely (b) mis-splitting the m-sign's own first hump into
a spurious extra sign, not a real cipher sign; (3) **(b)'s line1 pass is confirmed incomplete**: the page
continues for 3-4 more cipher signs after the X-cross, all the way to the leaf's right margin (confirmed by
this worker looking directly at `images/f82/f82_pair1_s4.jpg`), which (b) did not transcribe at all (its
transcription ends at the X, its last entry) while (c) did continue and catch them. The dense cursive
stretch between the m-sign and the X-cross could not be settled sign-for-sign against either reader's count
within this job's box (a genuine segmentation disagreement in a cramped hand, the same shape NEV-C2's f.27
reconciliation hit once already). This confirmed incompleteness in (b) does not change any of the scores
below, since line1's own gloss read has 0 confident letters either way -- nothing on line1 enters the
letter-alignment at all.

**Score** (`tools/decode_witness.py`, key=`key_ceppo_nevers.tsv`, signs=`witness_f82_signs.tsv`,
plain=`witness_f82_plain.tsv`, 20 shuffled keys, seed 1):

```
f.82 alone:        real key 0.8333 (5/6 aligned letters); shuffled mean 0.7750 sd 0.2852 min 0.1667 max 1.0000; z 0.20; rank 11 of 21
f.82 + f.27 pooled: real key 0.9167 (11/12 aligned letters); shuffled mean 0.7708 sd 0.1511 min 0.4167 max 1.0000; z 0.97; rank 2 of 21
```

(`--sample-lines line1` could not run: line1's own gloss read has zero legible letters, so the tool correctly
exits on "no clerk letters in scope" for that subset -- expected, not a bug, given the gloss-read finding
above.)

**FAIL on both bar conditions** (z nowhere near +4 either alone or pooled), but **not a contradiction of the
key** in the way a low raw agreement would be: the real key's raw agreement (0.83 alone, 0.92 pooled) is
comfortably above the 0.70 threshold both times, and pooled it ranks 2nd of 21 keys (only one shuffled key
scored higher) -- the z-score stays low only because n is so small (6 then 12 aligned letters) that the
shuffled-key distribution itself is extremely wide (sd 0.29 alone, 0.15 pooled) and sometimes scores just as
high by chance. This is the same "no power at this n" shape rule 3's headline paragraph describes, one step
better than NEV-C2's f.27-alone result (which ranked 11th of 21, indistinguishable from the shuffled floor;
f.82 alone also ranks 11th, but pooling with f.27 pushes the real key to 2nd). Read alongside the confirmed
per-row breakdown below, this is best described as an encouraging but statistically inconclusive signal, not
a pass and not a negative.

**Rows confirmed / contradicted** (`witness/key_rows_ceppo_f82.tsv`, f.82-alone run; informational only at
n=6): row 29 (o) confirmed 1x, row 30 (o) confirmed 4x -- together accounting for all 5 of the run's aligned
matches (both of the key's two homophones for "o" are individually confirmed by this witness, the strongest
per-row signal either NEV-C2 or NEV-C3 has produced so far); every other row shows 0 confirmations and 0-13
contradictions at this sample size, not a usable per-row grade (rule 3). The single miss among f.82's 6 gloss
letters is the "m" (line2's first legible letter) against whatever the aligner matched it to.

**Verdict.** The Ceppo-Nevers key is **not confirmed to the pass bar, but is not contradicted either**, and
this witness is the first of the group's three "with decipherment" witnesses to produce a full, scoreable
signs+plaintext pair (f.178 and f.39 had no gloss at all; f.27 alone was a non-test at n=6, rank 11/21). Two
of its two "o"-homophone rows are individually confirmed by every aligned occurrence.

**Named next steps, in order of expected value:** (1) a further, more patient gloss-reading pass on
`images/f82/gloss_retry/` (or a fresh, even-tighter re-crop of just line2 and line3, which carry all 6 of the
letters recovered so far) -- the two-attempt escalation in this job already found real signal by narrowing
the crop; a worker with a dedicated budget for this one step alone (not split across fetch+3 subagents+
scoring, as this job was) may recover enough letters to reach the z>=4 bar, especially pooled with f.27; (2)
resolve whether the interlinear marks are letters or a numeral/reference annotation (subagent (a)'s open
flag) before spending further budget on letter-by-letter reading -- if numerals, the calibration strategy for
this key needs to change; (3) settle the mid-line1 segmentation disagreement between (b) and (c) with a
slower, sign-by-sign pixel measurement, lower priority since it does not affect the letter-alignment score;
(4) if no further gloss legibility is recoverable, the lane's own named fallback applies: a control-backed
decode of a target passage itself, labelled as a target-style test, not a witness calibration.

**Requests:** gallica.bnf.fr 1 (well under the 3-request allowance: one fetch, HTTP 200 first try, no retry
needed). Subagents: 3 (gloss read -- resumed once with better crops, still 1 subagent; careful sign read;
blind check), all image-review only, no credentials, no AskUserQuestion, no novelty wording, owner not named.

### LANE NEV close-out (27 Sept 2026)

Calibration of `keys/key_ceppo_nevers.tsv` is still pending. NEV-C2 (f.27) and NEV-C3 (f.82) are non-tests: they
aligned 6 and 12 clerk letters, too few for any control to have power. The shuffled-key means are 0.58 and 0.77,
so the control is degenerate at this n. That is a lack of letters, not evidence against the key. Before a z test
means anything, the calibration needs at least 30 aligned gloss letters. The source for them is f.82r: the LANE NEV
orchestrator looked at the native crop (canvas 83, `pct:56,25.5,42,6.5`) and could see a gloss of roughly one
letter over each of about 90 signs, but the Sonnet subagent passes recovered only 6. The next step is to read that
gloss alone, one segment at a time, upscaled 2x, with the strongest model, and to gate on 30 or more letters before
any sign read is paid for. Job 2 (reading f.11, about USD 8) comes after that gate. Any control whose shuffled mean
is above 0.5 is reported as degenerate.

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

## HARVEST-A: f.11r (no.6, Saluzzo 14 Sept 1570) decoded with the printed key (28 Sept 2026)

Brief `.claude/briefs/runs/2026-09-28-parent-harvest-A.md` (KEY-ADJACENT rank 3). Intake gate: web and blog check
above, `tools/intake_gate_check.py ceppo-nevers-fr3251-1570s` exit 0. No class, no status change here (the
orchestrator's); rule 10 wording only.

**Material.** Gallica btv1b9060248g canvas 12 (f.11r, foliation '11' confirmed on the 27 Sept overview), one native
region `pct:51,36,48,10` (`images/f11/src_f11r_cipherband.jpg`, 4040x583) after two mis-aimed regions of the same
canvas. Five cipher insertions on three lines: P1 after "Dete auiso per l'altre mie a V.Ecc.a di l'andata" to
"quali molti attribuiscano fra l'altre occ.ni"; P2 to "Con la gionta."; P3 after it to the line end; P4 after
"Proponendo" to "al che da assai credenza l'intendersi"; P5 after it to the line end. 11 line crops
(`images/f11/manifest.json`, hand-boxed around an ink-profile line centre).

**Blind transcription.** A value-blind sign sheet (`harvest/sign_sheet_blind.png`): the 55 cells of Tomokiyo's
nevers_add1.png cut out and relabelled S10-S97 by a seeded shuffle, letter headers removed; the id-to-value map
(`harvest/sign_id_map.json`) was not given to the readers. Two independent Sonnet subagent passes on the crops only:
`harvest/passA.tsv` (132 signs), `harvest/passB.tsv` (133). Agreement by alignment 83/134 = 0.62. Both passes
missed three sheet signs this worker found on the image (barred theta S69, barred 8 S80, the 't3' ligature S56 --
each read as two signs or as a look-alike) and split on the look-alike pairs S30/S49 (r/n, a stroke between two
dots), S24/S88 (o/t, crossed strokes) and S37/S74 (c/m, a 6 with and without a tick). Reconciled by this worker by
shape against the sheet, one pass over native crops: `harvest/passC_reconciled.tsv` (135 signs).
**Bias caveat:** the reconciler had already seen the two passes' decodes when reconciling, so the reconciled
sequence is not blind; the blind pass B number below is the one without that bias.

**Control (rule 3), `harvest/decode_control.py`.** Real key (as printed) against 200 keys made by shuffling the
value column of the same 55-sign sheet; mean log10 4-gram per letter, it16dip corpus, contiguous runs only.
Power control: 20 it16dip windows at the target's own passage lengths, enciphered with the same key and null rate,
20% of signs replaced at random, same 200-shuffle test.

| transcription | letters | real key | shuffles mean / max | z | rank of 201 | power control (rank 1) |
|---|---|---|---|---|---|---|
| reconciled (not blind) | 127 | -1.290 | -2.063 / -1.605 | 5.09 | 1 | 20/20 |
| pass B (blind) | 132 | -1.534 | -2.065 / -1.499 | 3.03 | 2 | 20/20 |
| pass A (blind) | 136 | -1.885 | -2.067 / -1.659 | 1.11 | 36 | 20/20 |
| consensus only (60 signs where A, B and reconciled agree) | 60 | -0.912 | -2.144 / -0.400 | 1.22 | 6 | 4/20 -- non-test, too few contiguous runs |

**Reading** (`tools/decode_key.py ciphers/ceppo-nevers-fr3251-1570s`, `decode.json` -> `harvest/reading_f11.txt`,
`--check` passes; tokens 135: H 0, C 0, S 53, M 68, I 12, U 2):

```
P1 | inmofedilpremisenteconfortcandaooal
P2 | nprocurarelaresoitucionesi·hecg
P3 | ancodilprchemaoodi·[et]
P4 | ncauioalchunilochiinsauoia
P5 | [et]uoiuinolomequc
```

Words read: P2 "...procurare la res[t]itucione..." (the o at P2 pos 16 is the S24/S88 crossed-stroke pair; t
fits); P4 "[Proponendo i]n cau(i)o [= cambio?] alchuni lochi in Sauoia"; P1 "...di l-... con fort-...". Grades:
S where the sign's printed value is used and both blind passes agree with the reconciliation, M where they do not,
I for 12 positions where the printed value is overridden (`harvest/exceptions_f11.tsv`): (a) the pound-shaped sign
(printed under m, row 2) reads l in la, di l-, alchuni, lochi -- 7 positions; (b) a double-barred theta, not in the
printed table (its single-barred theta is f), reads r in procurare, restitucione -- 4 positions; (c) the ticked 6
(printed m, row 1) read s once in re-s-titucione. Tomokiyo's own note on this key ("allows reading of the
undeciphered letter ... but not quite") already signals that the table is incomplete.

**Judge** (`python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file
ciphers/ceppo-nevers-fr3251-1570s/harvest/reading_f11_letters.txt`, pasted):

```
FAIL language: score=-1.289, null_p99=-1.623, real_p05=-0.958, real_median=-0.822, mode=both, N=127
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```

Far above the shuffled null, below real prose: a partial reading with 68 M tokens, as the grades say.

**What this shows and does not.** The Ceppo-Nevers key as printed reads Birago's f.11r insertions better than 200 of
200 shuffles on the reconciled transcription and 199 of 200 on a fully blind pass, with Italian words recoverable
(procurare la restitucione; alchuni lochi in Sauoia). [VERIFY-CEPPO-1 correction, 28 Sept 2026: of these, only "curare", "estitucio", "chuni", "ochi" and "sauoia" are forced by the printed key; "pro-", "la r-" and both l's are I overrides. See AUDIT.md.] It does not give a continuous text: P1, P3 and P5 are mostly
unread. Searched for a prior reading as logged in the web and blog section above; not found there. No novelty
claim (rule 10).

**Next step (named):** a fresh session re-reconciles passA/passB blind to values (the bias caveat above) and runs
`harvest/decode_control.py`; then the other three targets (f.21v canvas 23 left page, f.35 canvas 36 -- about three
cipher lines at the foot of the recto, overview fetched 28 Sept, foliation '35' confirmed --, f.87 canvas 88) the
same way, which would also test the three variant values. Suggested status for the orchestrator: `partial`
(rule 5, control beaten), not set here.

Requests: gallica.bnf.fr 4 (three native regions of canvas 12, one 1000px overview of canvas 36), all >=2s apart,
browser UA; archive.org 2 (advancedsearch, one _djvu.txt for rank 8); web search 7; cryptiana.blogspot.com 2;
github.com 1 clone. Subagents: 2 (the blind passes).

## VERIFY-CEPPO-1 (verifier, 28 Sept 2026)

See `AUDIT.md`. Novelty N3 for the fragments (key published, Tomokiyo). A value-blind Opus re-reconciliation
(`harvest/passD_blind_verify.tsv`, graded in `harvest/passD_blind_verify_graded.tsv`) ranks the printed key 1 of
201 shuffles (z 5.54, and 5.38-5.82 on three seeds; power control 20/20). A blind reader of 21 decodes picked
only the real-key one as Italian and found 0 words in the 20 shuffles. Recovered fragments: P1 presidente,
mandato (blind sequence only; HARVEST-A's P1 "premisente ... candaoo" not endorsed); P2 [pro]curare
[la r]estitucio[ne]; P4 [al]chuni [l]ochi in Sauoia. Judge FAIL -1.267 (real_p05 -0.957). Next step: test the
three variant signs against the ff.27/39/82 period glosses.

## HARVEST-C intake: f.21v, f.35, f.87 (PARENT WORKER HARVEST-C, 28 Sept 2026)

Brief `.claude/briefs/runs/2026-09-28-parent-harvest-c.md`. Rule 10 wording only; no class, no status change here.

**Intake gate** (`tools/intake_gate_check.py ceppo-nevers-fr3251-1570s`: exit 0, "open (line 1) -- edition/page or
full-text-search citation found within 6 lines"). The web and blog step is HARVEST-A's section above (same day, both
fr.3251 folders), plus three folio-specific web searches this session, 28 Sept 2026: `Birago Nevers "12 ottobre 1570"
OR "12 octobre 1570" Saluzzo cifra` (f.21v), `Birago Nevers "15 novembre 1570" Saluzzo lettera cifra` (f.35),
`Lodovico Birago Nevers "9 maggio 1571" OR "9 mai 1571" Saluzzo chiffre` (f.87). Hits: only the BnF finding aid of
fr.3251 (cc49712p), fr.4702 (cc57752b) and other Nevers volumes, and Bourdeau's index page, which lists these folios
as having no published reading. No reading found.

**DECODE.** (a) Local mirrors `sources/decode/records-*-2026-09-24.tsv` and `keys-all-2026-09-28-merged.tsv` grepped
for 3251 / birago / ceppo / nevers: no fr.3251 record (the Nevers hits are fr.3975/3976, 1587-88). (b) Aymeloglu's
`catalogue/decode-catalog.csv` (10,106 rows, cloned fresh 28 Sept 2026) grepped the same way: its five "Lodovico Birago"
records are BnF fr.3619 f.73, fr.3621 ff.42/48/49 and fr.3623 f.41 (1591-92, French or Italian, all Decrypted), in
other volumes, twenty years later, and none is in fr.3251; the only "3251" hit is DECODE record id 3251, a 1911
postcard. (c) Live DECODE catalogue (de-crypt.org RecordsList, no login, 28 Sept 2026): holder field
`x_c_holder LIKE 3251` returned "No records found"; the same query with 3621 returned records 9444-9451 (the positive
control, so the negative is a working search). A sender search (`x_sender LIKE Birago`) also returned none, but
records with Birago as sender exist, so that field is not searchable this way. It is not a test. Result: no DECODE
record for fr.3251 f.21v, f.35 or f.87, so none is found-solved.

Requests so far: de-crypt.org 5 (1.5-2 s apart), web search 3, github.com 1 clone (Aymeloglu, read only).

VERIFY-CEPPO-2, 28 Sept 2026 (second, adversarial audit; AUDIT.md "Second audit"): held in part. N3 upheld; 0 of
2,000 chance decodes (1,000 shuffled keys, 1,000 sign-order shuffles) give two words; blind reader rates only the
real decode above one isolated word. Endorsed fragments, printed key only: presidente, mandato, curare, estitucio,
chuni, ochi, sauoia. The pound sign (l) and double-barred oval (r) stay I; the ticked 6 is printed s row 2 on the
blind transcription. Next step: fr.3252 f.36 (Gallica btv1b9060232m), Birago to Nevers 5 April 1571, "avec chiffre
et déchiffrement" per the BnF catalogue -- a possible Ceppo-Nevers witness to settle the two I signs.

**Images: blocked, all three folios held (18:20-18:34 UTC, 28 Sept 2026).** Gallica refused this container for
fr.3251 (btv1b9060248g): canvas 23 (f.21v, left page) `full/1600,` and `full/1000,` both HTTP 403 with Gallica's own
JSON body `{"httpStatus":403,"error":"You are not authorized to access this resource."}`, `f23/info.json` HTTP 503
"maintenance downtime or capacity problems", and a `pct:0,0,50,100/800,` region 403. After a 10-minute pause, one
retry (18:32 UTC, `f23/full/1000,`) returned the same 403. Per the good-citizen rule the host was not hit again, so
canvases 36 (f.35) and 88 (f.87) were never requested. HARVEST-A read canvas 12 from the same ark earlier the same day
without trouble, so this looks like a host-side or per-address refusal, not a rights change on the volume. That is an
inference, not tested. Fallbacks tried: the Wayback CDX API at web.archive.org (connection reset by the proxy relay on
all four calls, `ws_closed_mid_exchange`), this repository (no image of ff.21v, 35 or 87 in the working tree or in
git history), and Bourdeau's repository (cloned 28 Sept 2026: `targets/birago` holds only f.119's `cipher_full.png`
and the three key images). No image means no blind passes, no decode and no controls. Nothing was read, and no
finding either way.

**Next step (named):** a fresh session, preferably after 29 Sept 2026 00:00 UTC, fetches canvas 23 once at 1000px
(1 request) to test whether the refusal has lifted. If it has, it runs this section's steps unchanged: native
region crops of the cipher lines (canvas 23 left page, f.21v; canvas 36 recto foot, about three lines, f.35;
canvas 88, f.87), two value-blind passes against `harvest/sign_sheet_blind.png`, value-blind reconciliation,
`harvest/decode_control.py` (200 shuffles and the power control), and a `harvest/verify_mk_blind.py` blind reader,
with at most 20 Gallica requests per folio. The same block applies to the 1572 group
(`ciphers/nevers-birago-fr3251-1572`, same ark). That group is also written in a different key: Tomokiyo reconstructs
the 1572 letters from the f.178 decipherment (`keys/key_nevers_birago_1572.tsv`), not the Ceppo-Nevers table, so a
blind sign sheet has to be cut from `NeversBirago.png` first, and the Ceppo key is not applied there.

Requests this job: gallica.bnf.fr 5 (4 refused plus 1 retry, all refused); web.archive.org 4 (reset); de-crypt.org 5;
github.com 2 clones (Aymeloglu, Bourdeau, read only, deleted after); web search 3. Subagents: 0.

## HARVEST-D witness: BnF fr.3252 f.36-37, Birago to Nevers, Saluzzo 5 April 1571 (PARENT WORKER HARVEST-D, 28 Sept 2026)

Brief `.claude/briefs/runs/2026-09-28-parent-harvest-d.md`. A key source, not a counted reading. No class, no status
change here; rule 10 wording only.

**Intake.** Web search, 28 Sept 2026: `Birago Nevers "5 aprile 1571" OR "5 avril 1571" Saluzzo chiffre "3252"` and
`"Duca di Ferrara" Mirandola 1571 guarnigione trattato "Duca di Fiorenza" Birago Saluzzo`. Hits: BnF finding aids
(fr.4702, fr.3623), the Treccani DBI life of Ludovico Birago (cites fr.3252 among its manuscript sources; no text of
this letter), Wikipedia pages. No reading of this letter found. DECODE: live RecordsList `x_c_holder LIKE 3252`
returned no records; the same query with 3621 returned records 9444ff (positive control). Aymeloglu's
`catalogue/decode-catalog.csv` (cloned 28 Sept 2026): the only "3252" is DECODE record id 3252, a 1911 postcard.
Tomokiyo's nevers.htm does not list fr.3252. Not found-solved.

**Material.** Gallica btv1b9060232m (manifest: 184 canvases, every label NP). Canvas 37 right page carries foliation
'36' (f.36r); canvas 38 is f.36v / f.37r; canvas 39 shows f.37v (address "Ill.mo mio oss.mo il sig. Duca di Nevers
Pari di Francia ... a la Corte", endorsement '5 aprile 1571') and f.38r. The letter is in Italian with five cipher
passages: f.36r foot (about 13 lines), f.36v top (6 lines), f.36v middle (3 lines plus 2 lines after
"gentil'huomo"), f.37r (2 lines, after "come che Iddio è Iddio"). A small pasted slip at the foot of f.37r (left)
carries a clear-text passage ("[Il] sig. Duca di Ferrara è andato [con] diligenza alla Mirandola et [per fa]rli
mutare la guarnigione [a] causa d'un trattato quale se [...] li haveua il S. Duca di [F]iorenza. Mons. di [...]
[...]garda quale veneva [a] giornate giunse hieri a [T]orino per le poste"); its left edge is in the gutter and it
was not matched to a cipher passage. Every cipher passage carries the clerk's letter-by-letter decipherment: small
letters written above each sign. At 1x these are too faint to read, but a 2x upscale of the native region makes them
legible. Files: `harvest/witness_f36/` (overviews c36-c39, five native regions, the slip, `manifest.json`),
`cut_lines.py` (regenerates `lines/` and `lines2x/`; only the five cited crops are committed, in `cited/`).

**Same key.** On f.36v line 1 the 18 signs carry 18 gloss letters, "parlandone il signor", and every sheet sign in it
takes its printed Ceppo-Nevers value: S16 p, S45 a, S84 l (twice), S80 a, S89 d, S62 o, S17 i, S26 s, S13 g, S70 o,
S75 e, and the dotted slash (S30/S49) n. Pairs on f.36r agree (S17 i, S84 l, S16 p, S24 o, S31 m, S57 p, S26 s).
So this letter is in the Ceppo-Nevers key, and its interlinear glosses are a period decipherment of it.
Table: `harvest/witness_f36/alignment_pairs.tsv` (25 pairs, conf H/M/L per pair).

**The double-barred oval (no cell in the printed table) = r.** It is glossed r twice on f.36v line 1: pa-r-landone
(idx 3, conf H) and signo-r (idx 18, conf M). It has the same form as the sign on fr.3251 f.11r
(`harvest/witness_f36/f11r_double_barred_oval_x4.png`). So the four f.11r positions HARVEST-A read r "from context"
(procurare, restitucione) now have a period decipherment of the same key behind the value. Whether to regrade them
is for the orchestrator and verifier; this section does not edit the f.11r files.

**The pound-shaped sign: not settled, but the evidence moves.** No sign of that exact form turned up in the witness
lines read (f.36v lines 1-5, f.36r lines 1-3 and 9-13, f.37r line 1; the rest not scanned). Two nearby observations:
(a) S31, the cell the pound sign was assigned to on f.11r (printed m row 2), appears once on f.36r (upper line of
crop r36_L12, a loop with a long tail sweeping right) and is glossed **m**, its printed value, not l. (b) S84 (printed
l row 1) is glossed **l** three times. On f.36r it sits in the run z-sign / S84 / triangle, and f.11r P1 has the same
run with the pound sign in S84's place. Side by side (`harvest/witness_f36/compare_f11pound_vs_witness_S84_S31.png`),
the f.11r pound sign has S84's structure: a lower-left loop, a crossing stroke, and an upper-right loop, drawn
upright instead of leaning. The likelier explanation is that the f.11r pound sign is S84 in a more upright hand, read
at its printed value l. That would be a transcription look-alike (S84 taken for S31), not a variant sign outside the
table. This is an inference (M), not a gloss on an f.11r sign. If it holds, the seven f.11r pound positions read l at the
printed value of S84, and the override in `exceptions_f11.tsv` becomes a transcription relabel.
**Counter-evidence, found later the same session:** fr.3251 f.21v cipher line 5 (`harvest/f21v/lines/f21v_L05_s1.png`)
has a crossed-loop sign like S84 *and* a pound-shaped sign a few signs apart in one line. In Birago's own letters,
then, the two forms may be distinct signs, and the upright-S84 explanation is weaker than stated above. The pound
sign's value stays open between l (f.11r context, I grade) and whatever a gloss on the sign itself says. No witness
gloss on that exact form has been read yet.

**What was not done.** Four Sonnet blind passes on the 1x crops (A/B x two leaves) returned all glosses "?" and
guessed sign ids. They were rejected unused (`harvest/witness_f36/passes/README.md`). No full alignment of the
witness's several hundred glossed signs was made; the pairs above are the ones read to answer the brief's two
questions. The slip was not matched to a passage.

**Next step (named):** a full two-pass alignment of the witness (sign id + gloss per sign) on the 2x crops, one
f.36v block or four f.36r lines per call, gives the complete period key for this letter. It also tests the other
f.11r look-alike pairs (S30/S49, S24/S88, S37/S74). Then re-run `harvest/decode_control.py` on f.11r with S84 in the
seven pound-sign positions and r for the double-barred oval.

Requests (witness): gallica.bnf.fr 11 (manifest 1, four overviews, six regions), 2 s apart; de-crypt.org 2; web
search 2; github.com 1 clone (read only). Subagents: 4 (rejected).

## HARVEST-D: fr.3251 f.21v, f.35, f.87 and the 1572 group -- images in hand, held before the blind passes (28 Sept 2026)

**Intake.** HARVEST-C's section above covers these three folios, run the same day (28 Sept 2026): the web and blog
step with three folio-specific searches, DECODE local and live (holder LIKE 3251: none, with the 3621 positive
control), and Aymeloglu's decode-catalog.csv (no fr.3251 record). No prior reading, so none is found-solved.
`tools/intake_gate_check.py ceppo-nevers-fr3251-1570s`: exit 0.

**Images (the block HARVEST-C hit has lifted).** Gallica btv1b9060248g served again at 20:16-20:28 UTC, 28 Sept 2026.
One 1400 px overview and one native region per folio, plus one wider re-fetch per folio after the first regions clipped
the line starts (9 requests). The images confirm the layout. f.21v is the left page of canvas 23 (canvas 23's right
page is foliated 22 and is blank); about 11 lines of cipher mixed with prose run from "quattro motti" to "Io Resto in
pena". f.35 (canvas 36, recto, foliated 35) has two cipher lines near the foot, after "a questo particolare". f.87
(canvas 88, recto, foliated 87) has six cipher lines at the foot, after "mandatome qua dal sig. Cornelio Benti-voglio
per alcuni suoi particolari". None of the three has an interlinear gloss. Files: `harvest/f21v/`, `harvest/f35/`,
`harvest/f87/` (overview, `c*_cipher_w.jpg` native region, `manifest.json`). `harvest/cut_folio_lines.py` cuts the
1x line crops (f.21v 33 segments, f.35 6, f.87 18; crops are not committed, one command regenerates them). The line
centres were checked by eye on one crop per folio.

**Held: no blind passes, decode or controls run.** At 20:27 UTC, this worker's own session metadata read rate-limit
status `allowed_warning`. Under BUDGETS.md's scaling rule that means no new workers anywhere, so the four subagent
blind passes these folios need were not started. The only subagents this job ran were the four witness passes,
launched before the warning was seen. The folios are held, not negative: nothing was read.

**Next step (named):** once the rate-limit status reads `allowed`, a fresh session runs `python3
harvest/cut_folio_lines.py` and gives two Sonnet passes per folio the crops and `harvest/sign_sheet_blind.png`. The
passes must add a NEW row for signs not on the sheet: the double-barred oval, and the pound-shaped sign, which appears
on f.21v line 5 next to an S84-like sign. Then comes a value-blind reconciliation, then `harvest/decode_control.py`
(200 shuffles plus the power control) with r for the double-barred oval (witness f.36v, above), then
`harvest/verify_mk_blind.py`. Order by size: f.87 (six lines), f.21v, f.35 (two lines, probably under the control's
power floor). The 1572 group (`ciphers/nevers-birago-fr3251-1572`, key `keys/key_nevers_birago_1572.tsv` on disk)
first needs a value-blind sign sheet cut from `NeversBirago.png`, then the same passes. It is held on the same
warning.

Requests (folios): gallica.bnf.fr 6 (three overviews, three regions) + 3 (wider regions). Total Gallica this job: 20
(11 for fr.3252, 9 for fr.3251), all 2 s apart, browser UA, no refusals.

## HARVEST-D2: f.35 (no.18, Saluzzo 15 Nov 1570) decoded with the printed key (PARENT WORKER HARVEST-D2, 28 Sept 2026)

Brief `.claude/briefs/runs/2026-09-28-harvest-d2-3.md` (account 3, continues HARVEST-D). No class, no status change here;
rule 10 wording only. Intake: HARVEST-C's section above (28 Sept 2026: folio-specific web search, DECODE local and live
with the 3621 positive control, Aymeloglu's decode-catalog.csv) -- no prior reading, not found-solved;
`tools/intake_gate_check.py ceppo-nevers-fr3251-1570s` exit 0 at 22:14 UTC. Rate limit on this account at start:
`allowed` (the warning that held HARVEST-D was the owner account's).

**Material.** HARVEST-D's native region `harvest/f35/c36_cipher_w.jpg` (canvas 36, f.35r foot, foliation '35'), no
new Gallica request. Two cipher lines after "a questo particolare,"; the prose resumes "che sarebbe tanto come a dire".
Crops: `harvest/cut_folio_lines.py` now also writes `lines2x/` -- segments of about 1150 px cut at the column-ink
minimum nearest the nominal boundary (no overlap, no sign split) and upscaled 2x, since HARVEST-D's witness passes had
shown 1x crops too small for a reader (3 + 4 crops here).

**Blind transcription** (`harvest/blind_pass_brief.md`): two Sonnet passes on the crops and `sign_sheet_blind.png`
only, with three off-sheet ids allowed (X_THETA2 double-barred oval, X_POUND, X_NEW). `f35/passA.tsv` 76 signs,
`f35/passB.tsv` 76 signs (both 37 + 39 per line). **Value-blind reconciliation** by `harvest/reconcile_blind.py`
(alignment by sign id; agreements kept, a split with one H side takes the H side, the rest go to a third eye):
69 of 76 aligned positions agreed (0.91), 7 splits, none settled by confidence. A third Sonnet reader, blind to
values, settled the 7 from the crops with the neighbours' ids as landmarks (`f35/adjudicate_in.tsv`,
`f35/adjudicate_out.tsv`: S49, S24, S91 x3, S53, S26, all M). This worker saw no sign value while reconciling
-- the merge is mechanical and the disputes went to a subagent that had not seen the map -- which answers HARVEST-A's
bias caveat for this folio. Final `f35/passC.tsv`: 76 signs, 2 X_POUND, 1 X_NEW (L01 pos 2, a P-like loop with a
stem, both readers), 0 X_THETA2, 0 '?'.

**Decode** (`tools/decode_key.py ciphers/ceppo-nevers-fr3251-1570s`, job f35 in `decode.json`: key = `key_f11.tsv`
(the printed table) + `key_extra.tsv` (X_THETA2 = r, S, from the fr.3252 f.36v period gloss; not used on this folio);
`--check` passes). Tokens 76: H 0, C 0, S 35, M 38, I 0, U 3 (the two pound signs and the X_NEW, unkeyed):

```
f35 L01 | c·enonaosensohauefiuremidsiuihafino·e
f35 L02 | sntfateetmiuongano·irficsalitomeein[et]st
```

S where the printed value is used and both blind passes agreed at M or better, M where a pass was L or the position was
adjudicated (`reading_f35_tokens.tsv`). Word-like runs: "non", "haue", "fino" (L01), "fate", "et mi" (L02); nothing
continuous. No exception, no override: the pound sign is left unkeyed here (its two f.35 occurrences cannot rank a value,
see the fit line below).

**Control (rule 3), `harvest/decode_control.py f35/passC.tsv --extra X_THETA2=r --seed 1`:** real key -1.306 (mean
log10 4-gram per letter, it16dip, 73 letters) against 200 keys with the value column shuffled: mean -2.075, sd 0.173,
max -1.579; **z 4.46, rank 1 of 201**. Preliminary runs on the two blind passes before any reconciliation: pass A
rank 1 (z 4.64), pass B rank 1 (z 4.10). Power control (20 it16dip windows at the same passage lengths, same key,
20% signs replaced): real key rank 1 in **19/20**, z median 4.25. Value fit for X_POUND (2 occurrences): n and d
-1.293, t and r -1.303 -- no separation, not a test at this count.

**Blind reader** (`harvest/verify_mk_blind.py f35/passC.tsv f35/blind 35 X_THETA2=r`: the real-key decode and 20
shuffled-key decodes of the same signs, shuffled order; a Sonnet reader saw only `f35/blind/blind_decodes.txt`): it
picked TEXT 09 as the one Italian text ("non, haue, fino, fate, -ano, mi", LANG; five others SOME with isolated
fragments, the rest NONE), moderate-to-high confidence, no competitor. TEXT 09 is the real key
(`f35/blind/blind_answer.json`, `blind_judgment.tsv`).

**Judge** (`python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file
ciphers/ceppo-nevers-fr3251-1570s/harvest/reading_f35_letters.txt`, pasted):

```
FAIL language: score=-1.402, null_p99=-1.604, real_p05=-0.985, real_median=-0.829, mode=both, N=73
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```

Above the shuffled null, below real prose, as on f.11r: a partial reading with 38 M tokens on two lines.

**Verifier correction (VERIFY-CEPPO-D2-1, 29 Sept 2026, AUDIT.md "f.35"):** on the verifier's value-blind D (71/76 =
passC) the key test is stronger (rank 1/201, z 5.0-6.0, power 17-19/20), but a blind reader on D rated no decode LANG
and saw only "fino" and "come" in the real one. Claim scope none; no passage is endorsed; the words above are scraps.

**What this shows and does not.** On f.35 the printed Ceppo-Nevers key beats 200 shuffles on both blind passes and on
the reconciled sequence, at a power the same control reads 19/20, and a blind reader picks its decode out of 21. It gives
word fragments, not a continuous text: 73 letters is short, and the M grades say where the readers were unsure. No
prior reading located (HARVEST-C's search log); no novelty claim (rule 10). Not run: `tools/print_check.py` -- no
phrase longer than a common word is read here to search for.

Files: `harvest/f35/` (passA, passB, passC + agreement/disagreements, adjudicate_in/out, blind/),
`harvest/ciphertext_f35.tsv`, `reading_f35.txt`, `reading_f35_tokens.tsv`, `reading_f35_letters.txt`,
`harvest/key_extra.tsv`, `decode.json` (job f35). Requests: gallica.bnf.fr 0 (HARVEST-D's images). Subagents: 4
(two blind passes, one adjudication, one blind reader), all Sonnet, no credentials, no AskUserQuestion.

## HARVEST-D2: f.21v (no.11, Saluzzo 12 Oct 1570) decoded with the printed key (PARENT WORKER HARVEST-D2, 28 Sept 2026)

> VERIFY-CEPPO-D2-2 (29 Sept 2026, second audit): held, N3. "in diuerse" dropped (its r is the double-barred oval, its s D's alone); the letter itself is cited and its clear text (f.21r) quoted in Pascal, *Il Marchesato di Saluzzo e la Riforma protestante* (1960), fn. 6 -- say "no prior reading of its cipher passages", not "of this letter". See AUDIT.md.

Same brief, same intake as the f.35 section above (HARVEST-C's search log, 28 Sept 2026; not found-solved). No class, no
status change here; rule 10 wording only.

**Material.** HARVEST-D's native region `harvest/f21v/c23_cipher_w.jpg` (canvas 23, left page = f.21v), no new Gallica
request. Eleven lines from the line after "quattro motti ... alla sua uenuta" to the line ending "Io Resto in pena per";
prose and cipher alternate on six of them, so the passages are L01, L02.1, L02.2, L03, L04, L05, L06.1, L06.2, L07, L08.1,
L08.2, L09, L10, L11 (the prose between runs is named in `blind_pass_brief.md`'s per-line layout given to the readers).
Crops: `lines2x/`, flat bands (this page's lines are straight; 33 crops), read at 2x.

**Blind transcription.** Two Sonnet passes per half (L01-L06: `f21v/passA_L01-06.tsv`, `passB_L01-06.tsv`, 160 signs
each; L07-L11: `passA_L07-11.tsv`, `passB_L07-11.tsv`, 107 each), value-blind, off-sheet ids allowed. **Value-blind
reconciliation** (`reconcile_blind.py`): 133 of 160 aligned positions agreed on the first half (0.83), 94 of 107 on
the second (0.88); 40 splits, none settled by confidence, all sent to a third blind Sonnet reader per half
(`adjudicate_in/out_L01-06.tsv`, `_L07-11.tsv`). The splits were systematic look-alike pairs, and the adjudicator
decided them from the ink: the barred 8 (14 positions, all S80 -- the bar is there), the L-with-dot (5, all S10), the
slash between dots (4, S49, no crossing bar), the small dotted caret against the plain lambda (5, S23), theta with one
bar or two (S69 x3, S13, X_THETA2), and single cases. Final `f21v/passC.tsv`: 267 signs, of which 8 X_THETA2
(double-barred oval), 7 X_POUND, 5 X_NEW (an "L-like 1 with a dot" three times, a reversed 3 with a dot, a barred u), 0
'?'. This worker saw no value during the merge.

**Decode** (`tools/decode_key.py`, job f21v: `key_f11.tsv` + `key_extra.tsv` [X_THETA2 = r, S, fr.3252 witness] +
`exceptions_f21v.tsv` [X_POUND = l at the 7 positions, grade I]; `--check` passes). Tokens 267: H 0, C 0, S 179, M 76,
I 7, U 5. S = printed value with both blind passes at H and agreeing; M = a pass at M/L or an adjudicated position; I =
the pound sign; U = X_NEW.

```
f21v L01   | lesacardahenensedeltuttodaemee[et]etcinre
f21v L02.1 | uptnedilort
f21v L02.2 | ha
f21v L03   | ranseintencionemoptaquestacaricasadiqua
f21v L04   | credolenesinersuad
f21v L05   | ciolnoserlimlcederuiuendoetseruend
f21v L06.1 | io
f21v L06.2 | auanfarminoraog
f21v L07   | ranoreauantiqualchenartitonleuarms
f21v L08.1 | iqua
f21v L08.2 | a
f21v L09   | nf·tantodinarleindiuercect·e
f21v L10   | aciofemti·e
f21v L11   | t·mfatto[et]l·eramefadificulta
```

Runs read as Italian: "del tutto da ... et" (L01), "intencione ... questa carica ... di qua" (L03), "credo le ne ...
[p]ersuad[e]" (L04; the prose before it is "Et spinto dalla passione ... con più persone"), "ceder uiuendo et seruend[o]"
(L05), "auanti qualche ..." (L07), "tanto dinar[i] ... in diuer[s]e" (L09), "fatto [et] ... fa dificulta" (L11, before
"Io Resto in pena"). The rest is fragments with M tokens in them.

**Verifier correction (VERIFY-CEPPO-D2-1, 29 Sept 2026, AUDIT.md "f.21v"):** on the verifier's value-blind
re-reconciliation D (250/267 signs = passC) the key test holds (rank 1/201, z 5.7-6.6, three seeds), but "intencione"
(L03, three S49/S73 n/null splits) and "auanti" (L07, S23/S97 split) are not forced on D and are not endorsed; the
pound-sign l stays I. Endorsed passages: tutto da; questa carica ... di qua; credo le ne; ceder uiuendo et seruend;
tanto di ... in diuerse; fatto; fa dificu-. Class N3, key published.

**The two off-sheet signs.** `decode_control.py --fit-sign` scores the whole folio with one sign set to each value in
turn: X_POUND (7 occurrences) ranks **l first** (-1.099; null -1.122, r -1.127, i -1.129), and X_THETA2 (8 occurrences)
ranks **r first** (-1.111; n -1.113, l -1.128) -- r is the value the fr.3252 f.36v period gloss gives it (HARVEST-D),
found here from the text alone. The pound-sign l is what HARVEST-A read from f.11r context; it is graded I here, as
there, since no gloss on the sign exists yet.

**Control (rule 3), `harvest/decode_control.py f21v/passC.tsv --extra X_THETA2=r --seed 1`** (X_POUND unkeyed in the
control): real key -1.111 (254 letters) against 200 value-shuffled keys: mean -2.053, sd 0.147, max -1.583; **z 6.40,
rank 1 of 201**. Power control (20 it16dip windows at the same passage lengths, same key, 20% signs replaced): real key
rank 1 in **20/20**, z median 6.76, min 5.46.

**Blind reader** (`verify_mk_blind.py f21v/passC.tsv f21v/blind 21 X_THETA2=r X_POUND=l`; a Sonnet reader saw only
`f21v/blind/blind_decodes.txt`): picked TEXT 15 with high confidence as the only text reading as Italian prose ("tutto,
questa, casa, credo, tanto, fatto, difficulta, qualche, intencione, di qua, uiuendo, che"); one other text SOME ("che"
twice), nineteen NONE. TEXT 15 is the real key (`blind_answer.json`, `blind_judgment.tsv`).

**Judge** (`python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file
ciphers/ceppo-nevers-fr3251-1570s/harvest/reading_f21v_letters.txt`, pasted):

```
FAIL language: score=-1.136, null_p99=-1.702, real_p05=-0.931, real_median=-0.824, mode=both, N=261
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```

Closer to real prose than f.11r (-1.267) or f.35 (-1.402), still short of the p05 gate: 76 M and 5 U tokens on 267.

**Print check** (`tools/print_check.py ciphers/ceppo-nevers-fr3251-1570s`, `phrases.txt`: uiuendo et seruendo, questa
carica, intencione, fa dificulta, tanto dinari; `print-check.tsv`): IA full text, Google Books and OpenAlex answer the
common phrases with unrelated texts (Notitia Dignitatum, Atti e memorie, a 1687 Guerras de Flandes); "uiuendo et
seruendo" has no hit anywhere; Semantic Scholar answered 429 once and was not retried. A search result, not a novelty
verdict (rule 10). Requests: be-api 5, googleapis 5, openalex 6, crossref 2, s2 1.

**What this shows and does not.** The printed key reads f.21v far better than chance (z 6.4, 20/20 power, a blind
reader's unprompted pick), the two variant signs take the values the witness and f.11r gave them by the text's own
statistics, and several phrases are continuous Italian. It is not a full reading: the judge fails, and about a third of
the tokens are M or unkeyed. No prior reading located (HARVEST-C's search log and the print check above); no novelty
claim.

Files: `harvest/f21v/` (passes, passC + agreement/disagreements per half and merged, adjudicate_in/out per half,
blind/), `harvest/ciphertext_f21v.tsv`, `exceptions_f21v.tsv`, `reading_f21v.txt`, `reading_f21v_tokens.tsv`,
`reading_f21v_letters.txt`, `phrases.txt`, `sources.tsv`, `print-check*.tsv`. Requests: gallica.bnf.fr 0. Subagents: 7
(four blind passes, two adjudications, one blind reader), all Sonnet.

## HARVEST-D2: f.87 (no.45, Saluzzo 9 May 1571) -- key clears its controls, the merged reading is the weakest of the three (PARENT WORKER HARVEST-D2, 28 Sept 2026)

> VERIFY-CEPPO-D2-2 (29 Sept 2026, second audit): held in part, N3. The r of "giorno" and of "secre" are both the double-barred oval (M, period-gloss backed); "auanti" is D's. Crib lead: f.89 (no.46), Birago to Nevers the same day, no cipher. See AUDIT.md.

Same brief, same intake as the f.35 section above (HARVEST-C's search log, 28 Sept 2026; not found-solved). No class, no
status change here; rule 10 wording only.

**Material and a correction.** f.87 (canvas 88, recto) carries **five** cipher lines at the foot, not six: the cipher
begins after "mandatome quà dal sig. Cornellio Benti-uoglio per alcuni suoi particolari" on that line (L01) and fills
the next four (L02-L05). The lines fall to the right by 95-135 px across the region (a bowed page; the last line ends at
the right margin about a line-height lower than it starts), and HARVEST-D's sixth nominal centre was that fallen right
end of L05. Two reader pairs found this the hard way before it was measured: the first pair on flat crops and the
second on crops sheared by one global slope of the wrong sign both reported the target line cut at the crop bottom from
the second segment on and "L06" empty (`f87/rejected_flat_crops/`, `f87/rejected_sheared_crops/`, with READMEs; not
used). The third cut (`cut_folio_lines.py`, `follow=True`) tracks every line's centre window by window from the joint
row peaks of a smoothed ink profile and shears each segment flat between its two local centres, on a taller native
region fetched this job (`f87/c88_cipher_wt.jpg`, pct:52,67,43,18; the 13%-high regions clipped L05's right end). The
tracks were checked on an overlay before the readers ran. Gallica: 2 requests (one narrow tall fetch discarded).

**Blind transcription.** Third pair, on the tracked crops (18 crops, 2x): `f87/passA.tsv` 204 signs, `f87/passB.tsv`
214 (L01 27 both; L02-L05 44/47, 46/48, 45/48, 42/44). **Value-blind reconciliation:** 156 of 217 aligned positions
agreed (**0.72**, against 0.91 on f.35 and 0.83/0.88 on f.21v -- this is the hardest hand of the four folios), 45
splits and 16 one-reader signs. Two blind Sonnet adjudicators (L01-L03, L04-L05; `adjudicate_in/out_L01-03.tsv`,
`_L04-05.tsv`, 48 rows) settled every split from the crops, siding with pass A 29 times and pass B 18; 13 one-reader
signs at M or below were dropped, 3 at H were adjudicated. Their own confidence was low: the splits are the same
look-alike pairs throughout (a 6/b with a tick, dot or bar: S54 null / S74 m / S77 s / S37 c; an 8 with a bar or a
dot: S80 a / S65 et; the crossed sign with one or two bars: S24 o / S88 t; the loop with an ij flourish: S31 m / S32 r /
S76 z), and on this hand the ink often does not decide them at 2x. Final `f87/passC.tsv`: 204 signs, 7 X_THETA2, 1
X_POUND, 3 X_NEW, 0 '?'.

**Decode** (`tools/decode_key.py`, job f87: `key_f11.tsv` + `key_extra.tsv`; no exceptions; `--check` passes).
Tokens 204: H 0, C 0, S 134, M 66, I 0, U 4.

```
f87 L01 | l[et]immmgnorduasilgd··ea
f87 L02 | ·usimr[et]ndizcmeneazimmhecenmrmtilpfoincpidam
f87 L03 | aamem[et]gnaet[et]imsirnorestnalgenmochauendouazt
f87 L04 | uaetirem[et]sqeacaeoc·i[et]ungiorntauantieim[et]ntzeme
f87 L05 | neandosecrezamentecontzoorteondeciamlhunt
```

Runs read as Italian: "...mo ch'auendo..." (L03), "un giorn[o] ... auanti" (L04), "ne ando secre[t]amente cont[r]o
... onde ..." (L05); the rest is not continuous. X_THETA2 (7 occurrences) again ranks **r first** by value fit (-1.735;
i -1.739, a -1.751), the witness value; the single pound sign cannot be ranked.

**Control (rule 3), `decode_control.py f87/... --extra X_THETA2=r --seed 1`:**

| sequence | signs | real key | shuffles mean / max | z | rank of 201 | power (rank 1) |
|---|---|---|---|---|---|---|
| pass A (blind) | 204 | -1.634 | -2.069 / -1.736 | 3.49 | 1 | 10/10 |
| pass B (blind) | 214 | -1.617 | -2.072 / -1.691 | 3.47 | 1 | 10/10 |
| passC, all splits adjudicated | 204 | -1.735 | -2.065 / -1.695 | 2.48 | 2 | 20/20 (z median 7.5) |
| passC, confidence rule only (H side wins, 20 splits not adjudicated) | 204 | -1.753 | -2.064 / -1.687 | 2.33 | 4 | 20/20 |

The key beats 200 shuffles on each blind pass taken alone, at a power the same control reads 10/10, but the merged
sequence scores *below* both passes: adjudication on this hand replaced two readers' independent errors with a third
reader's, at the pairs above, rather than removing them. That is a transcription limit, not a key result.

**Judge** (`python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file
ciphers/ceppo-nevers-fr3251-1570s/harvest/reading_f87_letters.txt`, pasted):

```
FAIL language: score=-1.723, null_p99=-1.669, real_p05=-0.942, real_median=-0.816, mode=both, N=197
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```

At the null ceiling (0.05 above null_p99), far from real prose.

**Blind reader** (`verify_mk_blind.py f87/passC.tsv f87/blind 87 X_THETA2=r`; a Sonnet reader saw only
`f87/blind/blind_decodes.txt`): picked TEXT 04 with high confidence as the only text reading as Italian in several places
("secre[t]amente, auanti, giorn[o], [ch']auendo, che"); three texts SOME with one scrap each, seventeen NONE. TEXT 04 is
the real key (`blind_answer.json`, `blind_judgment.tsv`).

**Verifier correction (VERIFY-CEPPO-D2-1, 29 Sept 2026, AUDIT.md "f.87"):** a whole-line value-blind
re-reconciliation (split signs merged, the double-barred oval matched to printed S60 = r) ranks the key 1/201 at
z 5.1-5.3 on three seeds (power 20/20), above both raw passes; the merge above, not the hand, was the limit. Endorsed:
"un giorno auanti", "ne ando secre-amente" (the t is not read: the sign gives z). N3, key published.

**Verdict for this folio: reading ready with the caveat above, the weakest of the three.** The printed key is supported
on f.87 as on the other folios (each blind pass rank 1 of 201; a blind reader picks the real decode of 21; the
double-barred oval fits r), but the reconciled transcription is poor: 66 M tokens on 204, the judge at the null, a
merge that scores below its own inputs. What it gives is word-level fragments (secre[t]amente, un giorn[o], auanti,
ch'auendo), not text. **Next step (named):** per-sign crops (one sign per image at 3-4x, cut at the column-ink gaps
`cut_folio_lines.py` already finds) for the four look-alike pairs on this folio, read by two fresh blind passes on those
crops only, then the same control; and, since the S24/S88 and S80/S65 splits recur on every folio, a witness check of
those four pairs against the fr.3252 f.36 glosses (HARVEST-D's named next step) would settle them for all four letters
at once.

Files: `harvest/f87/` (three pass pairs, two rejected with READMEs; passC + agreement/disagreements; adjudicate_in/out
whole and per half; blind/; `c88_cipher_wt.jpg`, `manifest.json`), `ciphertext_f87.tsv`, `reading_f87.txt`,
`reading_f87_tokens.tsv`, `reading_f87_letters.txt`. Requests: gallica.bnf.fr 2. Subagents: 9 (six blind passes over
three crop cuts, two adjudications, one blind reader), all Sonnet.

## LIKELY-2 (2 Oct 2026, account-4)

Brief `.claude/briefs/runs/2026-10-02-account4-likely-phase2.md`, row rank 2 of `ciphers/_triage/likely-solves-2026-10-02.tsv`
(f.21v no.11, f.35 no.18, f.87 no.45; `first_cheap_test`: "f.21v: locate the cipher passage, iiif_lines crops, 2 blind
passes + reconcile, decode_key.py with the key vs 200 shuffled-key controls, judge it16; per-sign crops only if the
shuffle gate is marginal"). Clock read 03:34-03:5x UTC. Intake gate `tools/intake_gate_check.py ceppo-nevers-fr3251-1570s`:
exit 0 ("open (line 1) -- edition/page or full-text-search citation found within 6 lines"), run before the status word
below was changed.

**Non-job: everything the row names is already read, controlled and audited.** The row's cell is, step for step, what
HARVEST-D2 ran on 28 Sept 2026 (the three sections above) and VERIFY-CEPPO-D2-1 / D2-2 re-derived on 29 Sept (AUDIT.md):

| folio | blind passes | key vs 200 value-shuffled keys (HARVEST-D2) | verifier's blind D, three seeds | judge it16 | class |
|---|---|---|---|---|---|
| f.21v no.11 | 2 + adjudication, 267 signs | rank 1/201, z 6.40, power 20/20 | rank 1/201, z 5.7-6.6, power 20/20 | FAIL -1.136 (real_p05 -0.931) | N3, two audits, recovered-passages; status.json row 29 Sept; NEAR.md row |
| f.35 no.18 | 2 + adjudication, 76 signs | rank 1/201, z 4.46, power 19/20 | rank 1/201, z 5.0-6.0, power 17-19/20 | FAIL -1.402 (real_p05 -0.985) | none (key fits, no passage read); NEAR.md "read no language" |
| f.87 no.45 | 3 pairs + adjudication, 204 signs | rank 1/201 on each blind pass (z 3.5), merge rank 2 (z 2.48) | rank 1/201, z 5.1-5.3, power 20/20 | FAIL -1.723 (null_p99 -1.669) | N3, two audits, recovered-passages; status.json row; NEAR.md row |

The shuffle gate on f.21v is not marginal (z 6.4 and 5.7-6.6), so the row's conditional step (per-sign crops for the
look-alike pairs) does not fire from this row either; it stays the folder's named next step (AUDIT.md "For the
orchestrator (VERIFY-CEPPO-D2-1)"). No test was run here, no image fetched, no subagent called: gallica.bnf.fr 0
requests, vision calls 0, HYPOTHESES.md unchanged (no new pair of numbers to record). Not a negative. The row entered
the shortlist because line 1 of this file still read `open` while the two audits of 29 Sept wrote "target stays
`partial`" and NEAR.md carries its rows: the shortlist's scope excludes `partial` folders, so the status word, not the
reading, let it through. Fixed here under rule 5 (a target that beat its matched control is `partial`): line 1 now
reads `partial`, with the finish-or-blocker sections below; the spec's `cheap_test_done` now names all four folios.

## CEPPO-SPLITS: f.21v look-alike pairs S49/S73 and S23/S97 settled by shape against the fr.3252 period gloss (2 Oct 2026, account 2 for the account-3 orchestrator)

Brief `.claude/briefs/runs/2026-10-02-acct3-ceppo-splits.md`. Clock read 21:32 UTC at start. No class, no novelty wording.

**Crops (command, pasted).** `python3 tools/iiif_lines.py --image ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/c23_cipher_w.jpg
--out <scratchpad>/f21v_sp --prefix f21v --debug --groups 8 --group-upscale 3` (13 bands, 580 ink pieces; band n+1 =
passage Ln, checked on the overlay). The per-sign tiles kept are cut from the same native region at 4x
(`harvest/f21v/lookalike/crops/`, `f21v_L07_7_vs_10.jpg`, `f21v_L09_1_6_17.jpg`). No Gallica request; no subagent.

**Known answer: which shape is which value.** The brief named the glossed leaves ff.27, 39 and 82, but their glosses
cannot be read at Gallica's native resolution (NEV-C2: six letters legible on f.27). The legible period decipherment in
the same key and hand is fr.3252 f.36-37 (HARVEST-D, images on disk), so it served as the known answer
(`harvest/f21v/lookalike/witness_crops/`; the gloss letters were read by this worker, grade M):
- diagonal slash with one dot on each side: glossed **n** 5 times (f.36v L1 x3, f.36v L1 s2, f.36r L4). The printed
  sheet has two horizontal forms, S30 (r) and S49 (n), and S73 (null). Birago's diagonal form takes S49's value, n.
- caret with a dot between or under the legs (the A-form, sheet S23): glossed **n** 3 times (f.36v L4, f.36r L4 x2).
- lambda with a curled top and no dot (sheet S97): glossed **a** once (f.36r L4, in the run "lambda, dotted slash"
  glossed "a n").

**The f.21v tiles.** All four S49/S73 splits (L01.15, L03.7, L03.10, L03.14) are the diagonal dotted slash; all five
S23/S97 splits (L07.10, L07.27, L09.1, L09.6, L09.17) carry the dot inside the caret (L07.27 is the A-form with a dot
beside it). L07.7, which both readers had already labelled S97, is the curled-top lambda with no dot, and it sits three
signs from L07.10, the dotted caret, in one line. The dot is the feature that tells them apart.
`tools/lookalike_pass.py` was run as confusion (the f.21v and f.87 alignments: `harvest/f21v/lookalike/confusion.tsv`),
then packet (`--top 0`, the 40 splits; filtered to the 9 tiles of the two named pairs in `*_tiles_pairs.tsv`), then
reconcile with this re-read (`reread_*.tsv`, H, basis column = the witness shape). Result: 9 of 9 settled 2-of-3, 0
relabelled, 0 unsettled. The adjudicator's passC labels stand. In all nine, reader A matched the settled label and
reader B did not. `harvest/f21v/passD.tsv` = passC with these 9 tokens at H; `ciphertext_f21v.tsv` was rebuilt from
it (`build_decode_inputs.py f21v --seq f21v/passD.tsv`).

**True error (brief's requirement): not measured.** No blind reader was run on a glossed leaf in this job, so there is
no before/after reader-error figure. What was measured: the shape rule against the glossed witness, 9 of 9 consistent
(5 n, 3 n, 1 a), on gloss letters read by one worker (M). On f.21v itself, reader B's error at these 9 tiles was 9/9
before the settlement and 0 after (these figures are against the gloss-shape rule, not against a gloss on f.21v).

**Decode** (`tools/decode_key.py ciphers/ceppo-nevers-fr3251-1570s`, `--check`: "reading up to date"). f.21v tokens 267:
S 179 -> **188**, M 76 -> **67**, I 7, U 5 (unchanged). f.11r, f.35 and f.87 are unchanged. The letters are identical, so
no word changes. What changes is that "intencione" (L03, three dotted slashes = n) and "auanti" (L07.10, dotted caret
= n, beside L07.7 curled lambda = a) now rest on a shape the period clerk glossed. The verifier had left both
unendorsed because they were not forced on D (VERIFY-CEPPO-D2-1). They are cryptanalytic (S) with this shape evidence.
The verifier decides whether to endorse them. English: "intention", "before (avanti)"; L09 "tanto dinar[i] ... in
diuer[s]e" = "so much money ... in divers[e]" (its n's now S).

**Control (rule 3) at the measured two-reader error** (f.21v disagreement 40/267 = 0.15; `decode_control.py
f21v/passD.tsv --shuffles 200 --windows 20 --err 0.15 --extra X_THETA2=r`): real key -1.111. Seed 1: z 6.40, rank 1/201,
power 20/20 (z median 8.37). Seed 2: z 7.01, rank 1, 20/20. Seed 3: z 6.96, rank 1, 20/20.

**Judge** (`python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file
ciphers/ceppo-nevers-fr3251-1570s/harvest/reading_f21v_letters.txt`, pasted):
```
FAIL language: score=-1.136, null_p99=-1.702, real_p05=-0.931, real_median=-0.824, mode=both, N=261
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```
Unchanged, as expected, because the letters did not change.

**f.87: not done here.** 27 split tiles of the four named pairs went to `sorter/focus.tsv` for the owner. These are
not blocking. No sorter page exists for this target yet; the file is ready for `tools/sign_sorter.py --focus`. The
fr.3252 witness has glossed instances of S24 (o), S31 (m) and S80 (a). A per-pair witness read like the one above is
the next step. The f.21v S65/S80 pair (20 splits, the largest on f.21v by the confusion table) is outside this brief
and is named below.

## BIRAGO-SMALL: f.21v L11.17 dotted slash settled by the same shape rule (2 Oct 2026, account 2 for the account-3 orchestrator)

Brief `.claude/briefs/runs/2026-10-02-acct3-birago-small.md`, item 1. Clock 22:27 UTC at start. Disk only: 0 requests, 0 subagents.
No class, no novelty wording.

**Tile.** `harvest/f21v/lookalike/verify/f21v_L11_17_dottedslash.jpg` (VERIFY-CEPPO-SPLITS section 4): a diagonal slash with one dot
above-left and one below-right, no crossbar. Compared by eye with `witness_crops/f36r_L4_curledlambda_a_dottedslash_n.jpg`, the
glossed fr.3252 form (n, 5 glossed instances, CEPPO-SPLITS), and with the four f.21v tiles CEPPO-SPLITS settled
(`crops/f21v_L03_band_pos1-18.jpg`). It is the same form. Both raw passes read S73 (A: alt S49, conf L; B: alt S30, conf M), so
this is a both-agree tile that the 2-of-3 rule could not touch (the LESSONS.md "Look-alike pass" shape: half the wrong signs had
two readers agreeing). Relabelled S73 -> **S49 (n), H**, basis written to `harvest/f21v/lookalike/reread_L07-11.tsv`; passD.tsv and
`passD_L07-11.tsv` carry it; `ciphertext_f21v.tsv` rebuilt (`build_decode_inputs.py f21v --seq f21v/passD.tsv`).

**Second check, not done.** VERIFY-CEPPO-SPLITS asked also for an *unglossed* diagonal dotted slash in the fr.3252 witness, which would
show Birago also writes the null S73 in this form. One look at four regenerated 2x lines of f.36v top (`witness_f36/cut_lines.py`)
did not settle it: the band centres sit between lines on those crops, so the glosses above each slash cannot be paired by eye at
that cut. The rule therefore rests, as for the nine CEPPO-SPLITS tiles, on glossed instances only. That check is still open.

**Decode** (`tools/decode_key.py ciphers/ceppo-nevers-fr3251-1570s`, then `--check`: "reading up to date"). f.21v tokens 267:
S 188 -> **189**, M 67 -> **66**, I 7, U 5. L11 reads `t·mfatto[et]l·eramenfadificulta` (was `...l·eramefadificulta`). One letter is
added before the endorsed "fa dificu[l]ta", and that passage is unchanged. No new word is claimed: "eramen" is not read as a word
here. `reading_f21v_letters.txt` regenerated from reading_f21v.txt.

**Control (rule 3; the label changed, so the control can now differ)**, `decode_control.py f21v/passD.tsv --shuffles 200 --windows
20 --err 0.15 --extra X_THETA2=r`: real key -1.1096 (was -1.111). Seed 1: z 6.43, rank 1/201, power 20/20 (z median 8.34).
Seed 2: z 6.95, rank 1/201, 20/20 (z median 7.98). The key score moves by +0.0014. That is too small to tell null from n by
score: the decision rests on the shape.

**Judge**, pasted:
```
FAIL language: score=-1.135, null_p99=-1.721, real_p05=-0.93, real_median=-0.829, mode=both, N=262
FAIL - ceppo-nevers-fr3251-1570s (a PASS is a gate for a verifier, not a reading; rule 10)
```

**Endorsed count: pending a verifier.** Solver rule 188 -> 189. The verifier rule (AUDIT.md VERIFY-CEPPO-SPLITS, 155) is the
verifier's to move, not this worker's: L11.17 is one more tile that, if endorsed, would make it 156.

## Remaining gaps (finish-or-blocker pass, 2 Oct 2026)

Read so far: 411 of 682 tokens at S across the four letters (f.11r 53/135, f.21v 189/267 after CEPPO-SPLITS and BIRAGO-SMALL, f.35 35/76, f.87 134/204, the
HARVEST-A/D2 decode grades; `reading_f*_tokens.tsv`), word fragments and short passages, no continuous text; judge FAIL
on every folio.
- f.21v, 66 M + 5 U + 7 I tokens of 267 - blocker: not-attempted; the S49/S73 and S23/S97 pairs are settled (CEPPO-SPLITS above; L11.17 by BIRAGO-SMALL, endorsed by VERIFY-BIRAGO-SMALL 3 Oct 2026, verifier count 156), and the largest remaining split is S65/S80 (et/a, 20 tiles, `harvest/f21v/lookalike/confusion.tsv`); next: the same witness-shape settle for S65/S80 (fr.3252 f.36v glosses S80 a; find a glossed plain 8) on 4x tiles, then reconcile and decode_control, ~$4.
- f.87, 62 M + 4 U tokens of 204 (S 138) - blocker: not-attempted; hash and 8 pairs judged by the f.36 witness rules (CEPPO-WITNESS-PAIRS, VERIFY-CEPPO-WP, 3 Oct 2026: 7 applied, L04.41/L05.42 t at M contested, L02.35 rejected); L04.39 read barred by both blind readers but gate (iii) fails, S65 kept at M (A1B-CEPPO-87); S31/S32/S76 still have no witness rule (no agreed gloss on f.36r S31 x2, f.37r S76 (A1B-CEPPO-87), nor on f.36v S32 x1 and S76/S58 x5 (A1B-CEPPO-36V, 3 Oct 2026, 2 blind Sonnet reads each); f.36v S76/S58 x3 carry a two-stroke gloss both readers see (ii/ll/11, not z) but name no letter); D1-CEPPO (6 Oct 2026): a third, blind Opus reader on a1b36v T1-T6 gives 2-of-3 agreement on one tile only (T4, "ll" over S76/S58, against printed z; logged as a data conflict in HYPOTHESES.md); the same reader reads the same looped sign as "ss" on T5/T6, so no shape rule; f.87's six S76 tokens were already M, no grade change; next: the owner's sign sorter for the S31/S32/S76 looped family (sorter/), or a further glossed Birago/Ceppo leaf with the looped sign -- blind model reads of the a1b36v tiles are [retired] (three readers, A1B-CEPPO-36V + D1-CEPPO)
- f.11r, 12 I tokens (the pound sign read l from context) - blocker: no-key-material; every witness on disk or one fetch away is now searched: ff.27/39/82 (A1B-CEPPO-POUND), fr.3252 f.36r/f.36v/f.37r + slip (A1B-CEPPO-36: one occurrence, gloss not legible blind), fr.3252 f.47r (A1B-CEPPO-11V, 3 Oct 2026: 0 X_POUND labels in passA/passB/recon, and the leaf carries no interlinear gloss, so no glossed occurrence is possible), f.11v (A1B-CEPPO-11V: show-through of f.11r and a docket only, no cipher, no decipherment); stays I under PREREG c5412f90. f.117r is not a gloss source either (no slip or clear copy, birago Premise check (c)) and waits on the owner's sorter; reopens only with a new glossed Birago/Ceppo leaf.
- f.35, 38 M tokens of 76 on two lines - blocker: too-short; 73 letters, at the control's power floor, and the verifier's blind reader rated no decode of it LANG (AUDIT.md f.35); more letters cannot come from this leaf.

## Escalation (2 Oct 2026)

- [x] siblings: ff.27, 39, 82 (period decipherments) read as the calibration set (NEV-C2, NEV-C3, 27 Sept); fr.3252 f.36v (5 Apr 1571, with decipherment) gave the double-barred oval = r (HARVEST-D, 28 Sept).
- [x] clear-pages: f.89r (no.46, same day as f.87, read by two blind Sonnet passes) and f.21r (the clear text on disk from Pascal 1960 fn. 6 / VERIFY-CEPPO-D2-2) used as context cribs for the f.87 / f.21v runs (A1B-CEPPO-CRIB, 3 Oct 2026): 0 of 12 crib words matched in either run (shuffle p95 0, swap 0; planted-word power 0.69-0.70), no grade changes. f.89v (the letter's continuation) not read.
- [x] known-keys: Tomokiyo's printed Ceppo-Nevers key (`keys/key_ceppo_nevers.tsv`, from fr.4702) applied to all four folios, rank 1/201 on each blind transcription.
- [x] print: `tools/print_check.py` on the f.21v phrases (HARVEST-D2, `print-check.tsv`), no hit; two novelty audits per letter (AUDIT.md), N3.
- [x] key-rebuild: the printed key holds on every folio; the two off-sheet signs were added from the fr.3252 witness (r) and the value fit (l, grade I), nothing else to rebuild.
- [x] image-check: native Gallica regions for all four folios on disk (`harvest/f*/manifest.json`), line centres and tracks checked on overlays; f.87's crops were re-cut three times before the readers ran (HARVEST-D2).
- [x] retry: f.21v's S49/S73 and S23/S97 splits settled from the shapes in the fr.3252 period gloss (CEPPO-SPLITS, 2 Oct 2026; the both-agree tile L11.17 by the same rule, BIRAGO-SMALL); f.87's reconciliation was redone whole-line and value-blind by the verifier, lifting the merge from rank 2 (z 2.48) to rank 1 (z 5.1-5.3) (AUDIT.md VERIFY-CEPPO-D2-1, f.87).
Verdict: keep going: 2 internal gaps (f.21v, f.87; f.11r now no-key-material); cheapest next: f.21v S65/S80 witness-shape settle on 4x tiles (~$4); f.36v S76/S58 gloss tiles read by three blind readers (A1B-CEPPO-36V 2 Sonnet, D1-CEPPO 1 Opus, 6 Oct 2026): one tile agrees on "ll" (data conflict with printed z), no rule -- [retired] instrument: blind model reads of the a1b36v tiles; L04.39 and f.36r/f.37r S31/S76 tried 3 Oct 2026 (A1B-CEPPO-87), L04.39 to M, no gloss; clear-page cribs (f.89r, f.21r) tried 3 Oct 2026, no match

## CEPPO-WITNESS-PAIRS: f.87 look-alike pairs by the fr.3252 f.36 witness shape rules (3 Oct 2026, account 2 for the account-3 orchestrator)

Brief `.claude/briefs/runs/2026-10-03-acct3-ceppo-witness-pairs.md`. Disk only, 0 requests, 0 subagents. No class, no novelty
wording. Rules pre-registered from the f.36v glosses before any tile was opened:
`../birago-fr3252-1571-72/harvest/witness_pairs/PREREG.md` (e1760f2e). In short: barred 8 = a (S80, glossed x6), plain 8 = et
(S65, x1); upright hash = o (S24, x4), slanted hash = t (S88, x2); crossbar-6 = null (S54, unglossed x2), blob-6 = m (S74, by
elimination). No rule for S31/S32/S76 or S24-vs-others outside these shapes. Files: that folder, `f87_*`.

**Application.** `harvest/f87/c88_cipher_w.jpg` was cut into 6 strips at 2x. Each hash and each S65 8 in passC was located by
its passC neighbours (one eye, this worker; a positional slip is possible, so grade M) and then judged by the rule. Note that
`sorter/focus.tsv` positions follow a different alignment from passC, so tiles were located by neighbour triplets, not by
those numbers.
- Hash, rule disagrees with passC (7): L03.25, L03.46, L04.29, L04.41, L05.23, L05.42 are upright, so S88 -> S24 (o). L02.35 is
  slanted, so S24 -> S88 (t). The rule agrees with passC at L03.12, L04.34, L02.30 (slanted, S88) and L05.30 (upright, S24).
  L05.28 is UNDECIDED.
- 8 (3): L02.7, L03.6, L04.21 are barred, so S65 -> S80 (a). L03.13 and L04.39 are plain, so S65 stays. L04.9 is unclear.
- 6: no crossbar-6 found among the passC S74 positions checked by eye. Not tallied tile by tile (cap).
- **Conflicts with endorsed S tokens:** L02.35 (S24 o, H, S), L04.41 (S88 t, H, S) and L05.42 (S88 t, H, S) are already graded S
  in `reading_f87_tokens.tsv`, and the rule reads them the other way. This is a data conflict for the verifier, not settled
  here. The committed reading files are NOT edited. The proposed sequences are `f87_passE_hash.tsv` (7 changes) and
  `f87_passE_hash8.tsv` (10).

**Controls** (TWO-READER error 0.28 = 1 - 0.72 agreement; `decode_control.py ... --shuffles 200 --windows 20 --err 0.28 --extra
X_THETA2=r`):
| sequence | real key | z (seeds) | rank | power |
|---|---|---|---|---|
| passC (as committed) | -1.7352 | 2.48 / 2.83 | 2 / 2 | 20/20 |
| passE hash (7) | -1.6814 | 3.03 / 3.23 / 3.25 | 1 / 2 / 1 | 20/20 |
| passE hash+8 (10) | -1.6372 | 3.29 / 3.54 / 3.57 | 1 / 1 / 1 | 20/20 |

Relabel controls (`relabel_null.py`, `f87_relabel_null.txt`):
- hash+8 vs random signs at the same 10 positions: 0/300 reach it (p 0.003). Random positions: 0/300 (p 0.003).
- **In-family flips** (the same number of random S88->S24, S24->S88 and S65->S80 flips; the value set is the same, only which
  tiles flip changes): 20/500 reach it (**p 0.042**, mean -1.6884).
- hash only: random signs 1/300 (p 0.007). In-family flips: 45/500 (**p 0.092**, fails).
So much of the gain comes from adding o and a anywhere. The specific tiles the rule picks beat random in-family flips only for
hash+8, and only just.

**Verifier (VERIFY-CEPPO-WP, 3 Oct 2026, `AUDIT.md` last section).** The 7 S candidates are accepted and applied to
`harvest/ciphertext_f87.tsv`: solver S 134 -> 139, endorsed 113 -> 120, judge -1.655 FAIL. L04.41 and L05.42 keep t but drop
to M: the shape says o, but o lowers the score, so gate (iii) fails. L02.35 is rejected: the verifier and blind reconciler D
see no slant, so o stays S. Fresh-seed in-family flips: p 0.033-0.034 for the 7.

**Judge** (pasted, `python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file ...`):
```
passC (= reading_f87_letters.txt): FAIL language: score=-1.723, null_p99=-1.669, real_p05=-0.942, real_median=-0.816, mode=both, N=197
passE hash:                        FAIL language: score=-1.685, null_p99=-1.669, real_p05=-0.942, real_median=-0.816, mode=both, N=197
passE hash+8:                      FAIL language: score=-1.642, null_p99=-1.623, real_p05=-0.947, real_median=-0.833, mode=both, N=194
```
**Grades (proposed, hash+8):** all three pre-registered gates are met: the rule settles each tile, the key ranks 1/201 with
power 20/20 in every seed, and the judge is better. That gives 7 M -> S candidates (L03.25, L03.46, L04.29, L05.23 o; L02.7,
L03.6, L04.21 a) and 3 S tokens contested. **VERIFIER WANTED** (the in-family control passes only at p 0.042; the gloss reads
and the tile locations are one eye each). Fragments (M, English gist only): L04 "...un giorno..." ("one day"; was "ungiornt"),
L03 "...avendo..." ("having"), L05 "secre[t]amente" ("secretly", unchanged).

## Premise check (A1B-CEPPO-POUND, 3 Oct 2026)

Adversarial pass per `.claude/briefs/check-solved.md` "## Premise check", run 16:4x UTC, disk and two read-only clones.
- **(a) Decipherments the folder already mentions -- found, none of the four targets.** Tomokiyo's printed Ceppo-Nevers key
  (fr.4702 ff.36-37, `nevers_add1.png`) is a key, not a reading of fr.3251; his own note says it reads the fr.4702 letter
  "but not quite". The three "(with decipherment)" witnesses ff.27, 39, 82 were opened (NEV-C2/C3, `images/manifest.json`):
  f.27's gloss covers f.27's own passage only (illegible past ~6 letters); f.39 carries no gloss at all (f.39r-39v and the
  facing f.40r checked at zoom); f.82's gloss covers f.82 only. fr.3252 f.36-37 (HARVEST-D) glosses its own letter.
  Pascal 1960 (VERIFY-CEPPO-D2-2) quotes f.21r's clear text, not a reading of any cipher. No mentioned decipherment
  covers f.11r, f.21v, f.35 or f.87.
- **(b) Other solvers' working files -- not found.** Fresh read-only clones 3 Oct 2026: dbourdeau/cyphersolver a439937
  (3 Oct 2026): `SOLVED_CATALOGUE.md` l.243 still lists "ff. 11, 21v, 35, 87 ... have no published reading";
  `targets/birago/` works f.119 only and names ff.27/39/82 as siblings with decipherment; no apply-key script or rendering
  for any Ceppo-Nevers folio (grep ceppo / 3251 / btv1b9060248g: only nevers.htm mirrors and the Gallica sweep index).
  aaymeloglu/unsolved-ciphers d2800bb: grep ceppo / 3251 hits only DECODE record id 3251 (an unrelated 1911 postcard).
- **(c) Physical neighbours -- not found (for f.11r).** Canvas 12 is the opening f.10v | f.11r (`images/f11r_canvas12.jpg`,
  1000 px, INTAKE-3251; HARVEST-A's three native regions of canvas 12). No slip or clear copy was recorded on either page.
  f.11v (canvas 13) has never been fetched: not checked here (brief is disk-only for this step); logged as a gap, not a find.
  ff.21v/35/87 neighbours were viewed by HARVEST-C/D (overviews in `harvest/f*/manifest.json`); no decipherment recorded.
- **(d) Recipient side -- not found.** Nevers' papers are the recipient's own archive (fr.3251 is in the Nevers collection);
  no printed edition of Birago-Nevers letters exists (birago-nevers-1571 check-solved, two web searches); the recipient-side
  print found so far is Pascal 1960 (clear text only) and Boltanski 2006 (unread in full, AUDIT.md). Nothing new located.
Premise result: no find on (a)-(d); the item is not calibration or found-solved. The f.11r pound sign's value is not published
in any source above.

## A1B-CEPPO-POUND: pre-registration (3 Oct 2026, written before any gloss is read)

Question: the interlinear value of the pound-shaped sign (f.11r, 7 positions, exceptions_f11.tsv: script-L / pound form,
a lower-left loop, a crossbar, an upper loop rising to the right; `harvest/witness_f36/compare_f11pound_vs_witness_S84_S31.png`
left panel) on the witnesses ff.27, 39, 82.
- **Shape rule (what counts as the sign):** an upright script-L/£ form: closed lower loop at the baseline, a stem rising
  to an upper loop or hook, and a horizontal crossing stroke through the stem. NOT the sign: the leaning S84 crossed-loop
  (closed loops at both ends of a long horizontal), the S31 flourished-g (loop on top, tail curling back under), the hash
  (#, S24/S88), the crossed d-oval.
- **Script locate first:** no witness transcription carries a pound description; the one witness sign labelled m row 2
  (the cell the pound sign was assigned to) is f.82 line2 pos23 ("small loop at top with a long tail sweeping right and
  curling back under" = S31's printed shape, not the pound by its own note). Candidates are therefore located by eye on
  the on-disk bands, crops cut, then two blind readers (no candidate value given) read the gloss above/below each crop.
- **Promotion threshold:** the 7 f.11r pound positions (and the 5 other f.11r I tokens are NOT touched by this step) go
  from I to C only if >=2 distinct witness occurrences of the sign each carry a legible gloss letter and both blind readers
  give the same letter for each, all occurrences agreeing on one value. One glossed occurrence agreeing = stays I, noted as
  support. Readers split, or occurrences disagree = stays I, logged as a split. Zero located occurrences = stays I; the
  gap's next step moves to a different witness (fr.3252 f.36r/37r unscanned lines) or f.11v.
- **Stop rule:** no vision call would cross 80 pct of the USD 4 cap.

## A1B-CEPPO-POUND: result -- the pound sign does not occur on ff.27, 39 or 82 (3 Oct 2026)

Pre-registration above (commit c5412f90, pushed before any band was viewed). Disk only, 0 requests, 0 subagents,
0 blind vision calls (the pre-registered rule runs readers only on located occurrences, and there were none).
- **Script locate.** No witness sign table (`witness/witness_f27_signs*.tsv`, `witness_f82_signs.tsv`,
  `witness_f82_blind_line1.tsv`) describes a pound form. The one witness sign labelled m row 2 (f.82 line2 pos23) is
  described as S31's own printed shape (flourished g), not the pound.
- **Eye scan, this worker, one eye.** Bands cut in scratchpad from `images/f82/src_f82r_band.jpg` (3 strips) and
  `images/f27/src_ark_12148_btv1b9060248g_f28_4717_3412_3285_463.jpg` (3 strips), viewed at native size; local PIL crops
  of regions of the iiif_lines.py source bands (the tool's own output, NEV-C2/C3), no new fetch.
  f.82: no upright pound form in the three cipher lines; the crossed-loop forms present are the leaning S84 type (closed
  loops at both ends of a horizontal stroke). f.27: two upright L-shaped signs, at x 330-640 ("+ L D +", the same run
  shape as f.11r P1 "z / pound / triangle / +") and x 880-1150 ("b b L . 2 9"); kept as
  `images/f27/f27_plainL_x330_1x2.jpg` and `f27_plainL_x880_1x2.jpg`. Both are a plain right-angle L in the crisp
  ruled-stroke style of the triangle beside it -- no lower loop, no upper loop, no crossbar -- so they fail the shape
  rule. They match key row 42 (s, "crisp (ruled-line) angular corner-bracket"), and the gloss letter under the first looks
  like s (one eye, M; not read by blind readers, not used for any grade). f.39: no interlinear gloss on f.39r, f.39v or the
  facing f.40r (NEV-C2), so it cannot give a value whatever signs it carries; its 1000 px images were not re-scanned.
- **Outcome under the pre-registration:** zero located occurrences -> the 7 pound positions on f.11r stay I (the other
  5 f.11r I tokens untouched). No decode re-run, no AUDIT.md or SECOND-OPINIONS-QUEUE.tsv change (nothing promoted).
  One side note for the next reader: f.27's "+ L D +" run parallels f.11r's "z pound D +" run, but the f.27 L reads s
  and f.11r's context reads l there (s gives "sa restitucione", "aschuni", "sochi"), so the parallel does not transfer
  a value; the two forms are distinct signs.
- **Where not found:** fr.3251 ff.27r (both cipher lines), 82r (three cipher lines) on the native bands; f.39r-v by
  NEV-C2's record. Not searched: fr.3252 f.36r lines 4-8, f.36v lines 6 on, f.37r after line 1, the f.37r slip
  (the named next step), and f.11v (never fetched).

## A1B-CEPPO-36: the pound form on fr.3252 f.36r/f.36v/f.37r -- one occurrence, gloss not read blind (3 Oct 2026)

Pre-registration unchanged: A1B-CEPPO-POUND's shape rule and promotion threshold (commit c5412f90). Disk only, 0 requests.
- **Script locate.** The birago folder's existing passes (read only) carry X_POUND only in F36R-REREAD pass B at r36n_L09 pos 2,
  19 and L10 pos 41; adjudicated S94 (female sign, H) and S53 -- a circle on top with a stem, not the pound form.
- **Crops** (scratchpad, not committed): `python3 tools/iiif_lines.py --image ciphers/ceppo-nevers-fr3251-1570s/harvest/witness_f36/<f>.jpg --out <scratch>/lines/<f> --prefix <f> --debug`
  for f in c37_f36r_cipher (17 bands), c38_f36v_top (8), c38_f36v_mid (7), c38_f37r_cipher (3); eye scan on 12 native tiles
  of those regions plus `c38_slip_wide.jpg`, one eye (this worker).
- **Found:** one upright script-L/pound form, f.36r r36_L03 pos 30 (region x ~2150, y ~350), in the run "+ Z [pound] ng-sign",
  the same "z / pound" run as f.11r P1. Crop kept: `harvest/witness_f36/f36r_L03pos30_pound_3x.jpg` (region 1990,255-2310,415, 3x).
  Both earlier passes in the birago folder (f36/recon.tsv, ciphertext_f36_v2.tsv) label this sign **S84** (printed l), and
  the same page also has the leaning S84 in "Z [S84] triangle" -- so in this hand an upright pound form sits where readers
  put S84, which supports the upright-S84 explanation above (inference, M).
- **Blind readers (2 Sonnet calls, no value given):** A: shape "script L/2-like, loop top right, second loop at bottom", gloss ?,
  conf L. B: shape "looped cursive L/ell, open loop top right, lower hook with curl", gloss "none clearly above it; a faint
  slanted l-like stroke up-left, probably a neighbour's gloss", conf L. This worker's own eye reads a small l above the sign (M,
  not used for any grade).
- **Outcome under the pre-registration:** 1 located occurrence, readers give no letter -> stays I; logged as a located
  occurrence with unread gloss, not as support. The 7 f.11r pound positions stay I; no decode re-run, no AUDIT.md or
  SECOND-OPINIONS-QUEUE.tsv change.
- **Where not found:** f.36r all 17 bands of `c37_f36r_cipher.jpg` (only the one above), f.36v `c38_f36v_top`/`c38_f36v_mid`
  (the "2."/underlined angular signs present are the corner form, glossed s at least once, "il s[i]gnor"), f.37r
  `c38_f37r_cipher` (none), the slip (clear text only, no cipher). Not on disk: the parts of f.36v outside the two regions.

## A1B-CEPPO-11V: f.11v fetched (show-through only) and fr.3252 f.47r searched for the pound form (3 Oct 2026)

Pre-registration unchanged (PREREG c5412f90: promote the pound form only on >=2 glossed occurrences agreeing).
- **f.11v.** `python3 tools/gallica_folio.py btv1b9060248g --folio 11 --side v --anchor 12=11r --anchor 36=35r --anchor 88=87r`
  (fit canvas = folio + 1, residuals 0; one canvas per opening, f.11v = canvas 13 left page). Overview `f13/full/1600,`, then
  `python3 tools/iiif_lines.py --ark btv1b9060248g --canvas 13 --region 660,2350,3500,380 --out <scratch>/f11v --prefix f11v --debug`
  (native band over the cipher-looking lines; source and a mirrored, contrast-stretched crop kept in `harvest/f11v/`).
  Found: the page carries mirrored show-through of f.11r -- the band reads correctly only when flipped ("Con la guerra",
  "intendesi", the f.11r cipher runs) -- plus the f.11r signature flourish show-through, a BnF stamp and a faint docket at the
  foot. No cipher of its own, no decipherment, no slip; the pound form cannot occur with an interlinear value here. One eye
  (this worker), no subagent.
- **fr.3252 f.47r.** Script locate on the birago folder's passes (read only): `harvest/f47/passA.tsv`, `passB.tsv`, `recon.tsv`
  and `la/`, `ref/` carry 0 X_POUND labels although the blind brief offered it as an off-sheet id; recon has 23 S84 cells.
  More decisive: f.47r has no interlinear gloss (birago NOTES.md Premise check (c), checked on the native line crops), so any
  occurrence there would be unglossed and could not count toward the promotion rule. No crops cut, no vision call spent.
  f.117r, f.144r, f.168 not touched (sorter).
- **Result:** the 7 f.11r pound positions stay I; no decode, AUDIT.md or SECOND-OPINIONS-QUEUE change due. Gap line moved to
  no-key-material: only a new glossed Birago/Ceppo leaf reopens it.
Requests: gallica.bnf.fr 2 (overview + one native region), 0 subagents, 0 blind vision calls; own looks 3.

## A1B-CEPPO-CRIB: pre-registration (3 Oct 2026, written and pushed before any crib list exists or is read against a run)

Step: Escalation "clear-pages" -- f.89 (no.46, Birago to Nevers, 9 May 1571, clear) and f.21r (clear first page of no.11)
as context cribs for the M tokens of f.87 and f.21v. Tool: `harvest/crib/crib_match.py` (docstring gives the exact
matching rule; positive check before this section: on `reading_f87_tokens.tsv` it finds the verifier-endorsed
"giorno", "auanti" and "secre-amente" at cost 0-1, 0 of 50 shuffles).

- **Candidate runs:** f.87 L01-L05 (`reading_f87_tokens.tsv`, as committed now) and f.21v L01-L11 (`reading_f21v_tokens.tsv`).
- **Crib lists, extraction rule fixed now:** `crib/cribs_f89.txt` = every proper noun (person, place, office-holder's
  name), month name and number written as a word in the reconciled f.89r clear text, >= 5 letters after folding; no
  other words, chosen without looking at any run. `crib/cribs_f21r.txt` = every word of >= 5 letters in the f.21r clear
  text on disk (AUDIT.md VERIFY-CEPPO-D2-2: "con le pratiche che tiene, maxime con Vgonotti, hauendoli per aderenti, et
  intrinseche amici, oltra l'esser temuto da i principali ... di Carmagnola") -- no vision on f.21r.
- **Match:** crib_match.py's rule: S letters fixed, only M/U/I tokens may be substituted, filled or dropped; cost <= 0
  (5 letters), 1 (6-8), 2 (9+).
- **Statistic and controls (rule 3):** T = distinct crib words matched in the run. Control 1: 1000 within-line shuffles
  of token order (seed 1), p95 and p(>=T). Control 2 (swap): f.21r list against f.87, f.89 list against f.21v.
  Positive control: the f.87 endorsed words above (already run, 3 of 3 found).
- **Gate:** a run's crib support counts only if T > shuffle p95 AND T > the swap count for that run. Then, and only
  then, a matched word with its own shuffle match rate < 0.05 moves the M tokens it uses (kept or edited) to S, recorded
  in an exceptions/notes file and decode re-run with `--check`; edits to sign values are not made by this step unless the
  matched letter is a value of a look-alike partner already named in NOTES.md (else logged as a lead, grade unchanged).
  Fail either arm: no grade changes, logged as a control-backed negative with both numbers.

## A1B-CEPPO-CRIB: result -- no crib word from f.89r or f.21r is found in the f.87 or f.21v runs (3 Oct 2026)

Pre-registration above (commit 44b7f901, pushed before any crib list existed).

**f.89r read.** Gallica btv1b9060248g canvas 90 (right page = f.89r; the left page is f.88v, f.87's address leaf, with
cipher show-through only). Crops: `python3 tools/iiif_lines.py --ark btv1b9060248g --canvas 90 --region
4560,700,3560,4480 --out ciphers/ceppo-nevers-fr3251-1570s/harvest/f89 --prefix f89 --max-width 2400 --debug` (35
lines x 2 segments; a first region clipped the right margin and was deleted unused). Two blind Sonnet passes
(`harvest/f89/passA.tsv`, `passB.tsv`, each with a `_names.tsv`), reconciled by this worker for names only, against the
debug overlay. The letter (dated by the finding aid 9 May 1571) answers Nevers's of 26 April, mentions Birago's packets
from Pinerolo of 13 and 16 [April], and complains that the fortresses are left unpaid: money from Auvergne and Provence,
the Tesoriere's account, the fortification of Carmagnola, the munitions, the garrisons at Revello ("Rauello"),
Dragonero in Paesana, Perosa and Verzuolo, the Swiss guard. Clear text, grade as read by two passes; this worker did not
reconcile the full text word by word (only the names, which is what the registered crib rule uses).

**Crib lists** (`harvest/crib/cribs_f89.txt`: Aprile, Pinarolo, Francia, Auuergna, Prouenza, Carmagnola, Rauello,
Dragonero, Paesana, Perosa, Verzolo, Suiceri; numbers are digits on the page, so none enter. `cribs_f21r.txt`: the 12
words of >= 5 letters in the f.21r quotation, among them Vgonotti and Carmagnola).

**Result** (`harvest/crib/crib_match.py`, seed 1, 1000 within-line shuffles):

| run | crib list | T (words matched) | shuffle mean / p95 / max | swap list | swap T | gate |
|---|---|---|---|---|---|---|
| f.87 L01-L05 (204 tokens, 61 M, 4 U) | f.89r, 12 | **0** | 0.00 / 0 / 0 | f.21r | 0 | FAIL (T not > p95) |
| f.21v L01-L11 (267 tokens) | f.21r, 12 | **0** | 0.00 / 0 / 1 | f.89r | 0 | FAIL |

**Power (unregistered, added before reporting; `harvest/crib/plant_power.py`, 100 plants per word):** each crib word
planted into the run at the run's own M fraction (0.32 f.87, 0.29 f.21v), with half the M letters wrong, is found
**0.70** (f.87, 841/1200; per word 0.58-0.86) and **0.69** (f.21v, 826/1200) of the time. The plant leaves S tokens
correct, so real power is lower wherever an S token is misread or the cipher spells a name differently.

**Reading.** No name or place from the same-day clear letter, and no word of the f.21r passage, sits in the cipher runs
within one or two M-token edits. With power about 0.7 per occurrence the test excludes the case of several of these
words in the runs, not a single one. The cipher on f.87 may also carry what the clear letter does not (that is
what cipher is for). **No token changes grade; no reading, AUDIT.md or SECOND-OPINIONS-QUEUE.tsv change**
(rule 10 propagation not triggered). Rule 4 counts unchanged: f.87 S 139 / M 61 / U 4; f.21v as in Remaining gaps.

Not done: f.89v (the letter continues: "quale due partite con-") not fetched; its names could enter a second crib list
under the same rule, ~USD 2 (one region + 2 passes). Requests: gallica.bnf.fr 3 (1 overview to scratchpad, 2 regions).
Vision: 2 Sonnet subagent passes (70 crops each), 2 own looks (overview, debug overlay).

## A1B-CEPPO-87: f.87 L04.39 and glossed S31/S76 on fr.3252 f.36r/f.37r (3 Oct 2026, account 1)

Brief `.claude/briefs/runs/2026-10-03-acct1-a1b-ceppo-87.md`. Pre-registration `harvest/a1b87/PREREG.md` (6334b236), pushed before
any read. Crops: `python3 tools/iiif_lines.py --image ciphers/ceppo-nevers-fr3251-1570s/harvest/f87/c88_cipher_wt.jpg --out <scratch> --debug`
(7 bands; cipher line 4 located by its passC neighbours "...ℒ 8 ∴ ≠ ꝯij 3 6 +"), fr.3252 bands from birago `cut_f36r.py` /
`cut_gloss.py`; tight tiles `harvest/a1b87/cut_tiles.py` (T1-T4, 3x). Two blind Sonnet passes, one batch each, tiles only,
no candidate values (`harvest/a1b87/blind_reads.tsv`). 0 network requests.

**Unit 1, f.87 L04.39 (passC S65 H).** Both readers: a single stroke crosses the waist of the 8 and runs out past both sides,
so R-8 reads S80 (a), agreeing with blind reconciler D. Gates (`harvest/a1b87/controls.txt`, decode_control.py, err 0.28,
seeds 1-3, side by side):
| sequence | real key | z (seeds 1/2/3) | rank | power |
|---|---|---|---|---|
| current (S65) | -1.6516 | 3.15 / 3.48 / 3.47 | 1/201 x3 | 20, 20, 19 /20 |
| L04.39 = S80 | -1.6536 | 3.07 / 3.44 / 3.37 | 1/201 x3 | 20, 20, 19 /20 |
Judge (`python3 tools/judge_plaintext.py specs/ceppo-nevers-fr3251-1570s.json --file ...`):
```
current:      FAIL language: score=-1.655, null_p99=-1.623, real_p05=-0.947, real_median=-0.833, mode=both, N=194
L04.39 = a:   FAIL language: score=-1.657, null_p99=-1.699, real_p05=-0.944, real_median=-0.828, mode=both, N=193
```
Gate (ii) passes, gate (iii) fails (both scores drop slightly: "...auantieimetntzeme" -> "...auantieimantzeme"). Per the prereg,
and as VERIFY-CEPPO-WP did for L04.41/L05.42, the value stays S65 (et) and the token drops H -> M; the shape reading S80 is
recorded here. Data conflict noted: the shape rule and the language score point opposite ways on this tile. decode_key
--check exit 0; f.87 now S 138 / M 62 / U 4 (was 139 / 61 / 4). The letters are unchanged, so the SO-CEPPO-F87 prompt and
AUDIT.md's reading text need no edit; AUDIT.md f.87 gets a one-line grade note.

**Unit 2, glossed S31/S76.** Located by script: S31 at f.36r r36n_L11 pos 3 and r36n_L13 pos 30 (`ciphertext_f36_v2.tsv`), S76
at f.37r r37_L01 pos 14 (`f36/recon.tsv`); no S32 on f.36r. Each target was matched by its neighbours in both readers' sign
lists. No gloss letter met the both-agree rule: T2 (L11 S31) "m-like, unreadable" / "m-like or in, uncertain"; T3 (L13 S31)
"?" / none; T4 (S76) "ff or tt" / "ff or ss", both uncertain. So no witness count and no shape rule for S31/S32/S76; f.87's
S31/S32/S76 tokens (e.g. L04.38, L04.42) keep their grades. The f.36r S31 L11 gloss "m" read by HARVEST-D (alignment_pairs.tsv,
one eye, M) is not confirmed by blind readers at 3x. Not looked at: f.36v S76 instances (outside this brief), f.117r/f.144r/f.168.

Grades: no H or C change; 1 token H -> M on f.87. Report: what was found and where it was not found; no novelty class.

## A1B-CEPPO-36V: glossed S32/S76 on fr.3252 f.36v (3 Oct 2026, account 1)

Brief `.claude/briefs/runs/2026-10-03-acct1-a1b-ceppo-36v.md`. Pre-registration `harvest/a1b36v/PREREG.md` (0bfa53c2, rule copied
unchanged from 6334b236), pushed before any read. Located by script in birago `harvest/f36/recon.tsv`: S32 at v36mid_L03 pos 22 (pass B
only, not tiled) and v36mid_L05 pos 10 (A=B); S76 (pass A) / S58 (pass B) split at v36top_L02 pos 7, 32, v36mid_L01 pos 2, v36mid_L02
pos 11, v36mid_L06 pos 9, 15, 28. Crops: PIL is absent in this container, so `tools/iiif_lines.py` could not run; line bands for locating
were cut to scratch with `convert c38_f36v_{top,mid}.jpg -crop Wx185+X+(centre-120) +repage -auto-level` (centres from
`harvest/witness_f36/cut_lines.py`), and tight tiles with `sh harvest/a1b36v/cut_tiles.sh` (6 tiles, 3x; T3-T6 re-cut once after this
worker's placement check found the target outside the first boxes). Tiled: S32 x1 (T1), S76/S58 x5 (T2-T6); not tiled: v36mid_L03 S32
(contested label), v36top_L02 pos 32, v36mid_L06 pos 28 (box). Two blind Sonnet reads, one batch each, tiles only, no candidate
(`harvest/a1b36v/blind_reads.tsv`). 0 network requests.

Result: no tile meets the both-agree rule. S32 (T1): "k-like" / "k/r-like", both L. S76/S58: T2 unreadable both; T3 "k/h-like" both,
uncommitted; T4, T5, T6: both readers see two tall strokes over the looped-tail sign ("ii or 11" / "ll, ii, 11"), A at L, B at M --
consistent with A1B-CEPPO-87's f.37r T4 read ("ff or tt" / "ff or ss"), a two-letter group, not the printed z, but no letter is named
by both, so under the prereg it is neither a witness count nor a contradiction. No rule established; f.87's S31/S32/S76 tokens keep
their grades; decode and judge not re-run (nothing changed); AUDIT.md and SO-CEPPO-F87 need no edit (no reading or grade change).
Next: tiles T3-T6 to one blind Opus reader at higher magnification (~$4), or the owner's sign sorter.

Grades: no change. Report: what was found and where it was not found; no novelty class.

## D1-CEPPO: f.36v gloss tiles to a third, blind Opus reader (6 Oct 2026, account 1)

Brief `.claude/briefs/runs/2026-10-06-account1-default-1240-jobs.md` (D1-CEPPO). Pre-registration `harvest/a1b36v/PREREG-D1.md`
(pushed b8298e03e before the read): 2 of 3 readers agree on a primary letter group at M/H over the target sign, or the tile stays M.
Crop step: none new -- the committed tiles from `sh harvest/a1b36v/cut_tiles.sh` (ImageMagick, 3x; PIL still absent, so
`tools/iiif_lines.py` cannot run here). One Opus subagent call, six tile paths only, no prior reads, no key, no target named.
Result `harvest/a1b36v/blind_reads_D1.tsv`:

| tile | target | A (Sonnet) | B (Sonnet) | C (Opus) | 2 of 3 |
|---|---|---|---|---|---|
| T1 | S32 | k-like L | k/r-like L | n L | none |
| T2 | S76/S58 | unreadable | unreadable | ii L | none |
| T3 | S76/S58 | k/h-like L | k/h-like L | tt M | none |
| T4 | S76/S58 | ii L | ll M | ll M | **ll** |
| T5 | S76/S58 | ii L | ll M | ss M | none |
| T6 | S76/S58 | ii L | ll M | ss M | none |

One tile (T4, v36mid_L06 pos 9) meets the rule, with "ll" over an S76/S58 instance; printed S76 = z, S58 = t. Per the prereg this is
logged as a data conflict (rule 4) in HYPOTHESES.md, not a key value. It is weak: reader C reads the same looped sign family as "ss"
on T5 and T6 (long s and l are near-identical at this size), and A read "ii" at L throughout; all three readers agree only that the
gloss over this looped sign is a two-stroke group, never a single z. No key change; f.87's six S76 tokens were already M (no grade
change); `tools/decode_key.py . --check` exit 0 ("reading up to date": f.87 S 138 / M 62 / U 4). AUDIT.md and SO rows need no edit
(no reading change). The S32 tile (T1) has no agreed gloss. Blind model reads of these tiles have now run three readers: the
instrument is retired for these tiles; the next step is the owner's sign sorter or a further glossed leaf.

Grades: no change. Vision: 1 Opus subagent call (6 tiles). Hosts: none (0 network requests). Report: what was found and where it was
not found; no novelty class.

