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
(procurare la restitucione; alchuni lochi in Sauoia). It does not give a continuous text: P1, P3 and P5 are mostly
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
