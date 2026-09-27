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
