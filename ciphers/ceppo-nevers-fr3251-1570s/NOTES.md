open

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
