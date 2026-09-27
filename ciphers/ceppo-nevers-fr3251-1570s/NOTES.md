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
