# Glyph atlas: the z / 7 / 2 dispute (PX-BROGLYPH, 25 Sept 2026)

PX-BROPASSB's pass-A/pass-B reconciliation (NOTES.md "PX-BROPASSB") found the appendix's 90% agreement gate
failed at 85.84%, with `z<->7` (58 of 87) and `2<->7` (29 of 87) replace-disagreements making up 87 of 183
replace-disagreements (47.5%) -- one recurring glyph shape read differently by the two passes across many
entries and leaves. This section settles it from the page images, per this job's brief (`.claude/briefs/runs/
2026-09-25-lane-px-broglyph.md` step 2), using `tools/glyph_atlas.py crop` (added this job) to cut individual
crops from the plain DigitArq JPEGs already on disk in `images/`.

## Method

For each of the 87 disputed positions, I read `ciphertext_appendix.tsv`'s position index to locate the token
in its entry's cipher line, found the corresponding printed line on the full-resolution leaf image, and cut a
crop (`tools/glyph_atlas.py crop --image ... --box x0,y0,x1,y1:label --dest images/crops`) at 3-6x upscale.
Rather than crop all 87 individually (most are the identical shape once one is confirmed on a leaf), I spot-
checked across every leaf that contributes to the dispute -- m0280, m0281, m0282, m0289, m0290, m0291, m0292,
m0293, m0294, 9 of the ~12 leaves involved (m0283, m0286, m0287, m0288 not individually re-checked this pass;
their disputed tokens are graded M below, not H, per the brief's grading rule) -- and additionally checked
**undisputed** `z` and `2` instances on the same leaves as a control, so the comparison is never "does the
disputed shape look like itself" but "does the disputed shape look like the undisputed exemplars of each
candidate reading". 20 individual glyph instances are shown in the 15 crops in `images/crops/` (listed below).

## What the crops show

**One recurring glyph, not two or three.** Every instance currently transcribed `z` (agreed *or* disputed)
and every instance currently transcribed `7` in the disputed set is the same shape: a horizontal top stroke,
a diagonal descender, and a small mid-stroke hook/crossbar -- the classic 18th-century "barred 7" used across
Portuguese and French secretary hands of this period to keep a numeral 7 from being read as a 1. It is
completely uniform across all 9 leaves checked, in both `Carta` entries and `Passage` entries, whether the
transcriber who wrote the pass called it `z`, `7`, or (twice) `2`:

- `images/crops/m0280_carta13_line1_pos4.png` -- Carta 13 pos 1/4/14 (leaf m0280): three instances of the
  shape in one line, positions 1 and (agreed, per pass B) `7`, positions 4 and 14 disputed (`7` pass A / `z`
  pass B) -- identical shape to each other and to the agreed instance.
- `images/crops/m0280_carta13_line2.png` -- Carta 13 pos 29/32 (leaf m0280): two **undisputed** `z` instances
  (both passes agree). Same shape as the disputed ones above -- the control that matters most: if agreed-z
  looked different from disputed-z/7, that would argue for two real signs. It does not.
- `images/crops/m0282_carta61_line2.png` -- Carta 61 (leaf m0282), a `26.12.z.8.12.15.` run: same shape again,
  on a leaf where pass A calls it `7` throughout and pass B calls it `z` (the opposite convention from
  m0290-294, see "Two passes, two conventions" below).
- `images/crops/m0290_carta93_line1.png`, `m0290_passage2a_line1b.png` -- Carta 93 / Passage 2a (leaf m0290):
  same shape, disputed positions read `z` by pass A and `7` by pass B.
- `images/crops/m0291_carta96_line1.png`, `m0291_carta96_line3.png` -- Carta 96 (leaf m0291): line 3
  (`2.ff.15.c.12.z.8.12.25.`) has a genuine loop-`2` and the crossbar shape in the same short crop -- side by
  side, the two are visibly different signs.
- `images/crops/m0292_carta105_line1_left.png`, `m0292_carta105_line1.png`, `m0292_carta105_block.png` --
  Carta 105 (leaf m0292): the crossbar shape three times in one line (disputed, pass A `z` / pass B `7`) and,
  immediately after, a genuine loop-`2` (pos 6, pass A `2` / pass B `7` -- pass B's error, not a second
  reading of the crossbar shape).
- `images/crops/m0293_carta106_line1.png`, `m0293_carta106_line2.png` -- Carta 106 (leaf m0293): the crossbar
  shape (pos 10, disputed) and, on the next line, two genuine loop-`2`s side by side (pos 12/15-16, disputed
  the same way as m0292's).
- `images/crops/m0294_carta110_line2.png` -- Carta 110 (leaf m0294): two crossbar instances flanking a genuine
  loop-`2` in the same short run (`e.z.2.z.18.`) -- again, plainly two different shapes next to each other.

**Genuine `2` is a different, distinguishable sign.** Every `2`-side instance checked (Carta 105 pos 6, Carta
96 pos 3/16, Carta 106 pos 12/15-16, Carta 110 pos 30) is a plain loop-shaped numeral 2, clearly not the
crossbar shape, in both disputed and undisputed positions. Pass B's `7` reading at these 29 positions looks
like pass B over-applying its own "read the ambiguous shape as 7" convention to an unrelated, unambiguous
digit -- a separate, ordinary digit-legibility slip, not evidence of a third sign.

**The disputed shape does not match this scribe's plain-hand cursive z.** `images/crops/m0280_plain_naofaz3.png`
crops the Deciffrada line "não faz nenhum caro[so]" (m0280, running Portuguese prose, not cipher) -- the
plain-hand `z` in "faz" is a simple flowing loop/descender with no top stroke and no crossbar, visibly
unlike the cipher glyph. This is the check the job brief asks for ("decide ... from letterforms, not from the
key"): if the cipher's code-letter `z` were meant to be read as the ordinary letter z, it has no reason to be
written in a completely different hand from the same scribe's own plain-text z on the same page.

**Two passes, two conventions, not two shapes.** Pass A never once transcribed `7` on leaves m0290-294 (0 of
1364 numeric tokens) despite transcribing it 49 times on m0280-289 -- and within m0280-289, pass A's own `7`
readings are themselves disputed by pass B, which called the identical shape `z` there (m0281 Carta15/23,
m0282 Carta61, m0283 Carta70, m0286 Carta73/74/Passage3a, m0287 Carta79/80, m0288 Carta81/85/Passage2a -- 25
of the 87). Pass B's two transcription subagents (`passB_cipher_1.tsv` = m0280-288, `passB_cipher_2.tsv` =
m0289-296, PX-BROPASSB) each picked one convention -- `z` for the first batch, `7` for the second -- and
applied it consistently within their own half. That is the signature of one graphically ambiguous sign that
different transcribers resolve differently and consistently, not of two really-different letterforms that
happen to get confused at the boundaries.

## Decision

**One sign.** The crossbar shape is a single recurring code symbol, correctly read as **numeral 7** (the
period "barred 7"), not letter z. Every token currently transcribed `z` anywhere in the appendix (70 tokens:
agreed and disputed alike) and every token currently transcribed `7` in the 58 z/7-disputed positions is this
same shape and is settled to `7`. The 29 `2`-vs-`7` disputes are settled the other way: pass A's `2` reading
stands (a genuine, distinguishable loop-shaped digit); pass B's `7` was a misread of an unrelated glyph.
Letter-code `z` accordingly drops out of this cipher's active alphabet -- nothing checked in this pass shows
a real instance of it (see "Not done this pass" in NOTES.md for the four leaves not individually re-checked).

## Consistency check against the period decipherment (secondary test, not the basis for the decision above)

`key.tsv` already grades `z -> e` at C (11/12 = 92% before this job; 18 raw z-observations feed the anchored
sample) and the pre-settlement `7` at M (`e` still the largest single value, 6/11 = 55%) -- both point the
same direction the letterform evidence does. `2 -> d` was M (10/18 = 56%, `e` second at 5/18) -- consistent
with code `2`'s pre-settlement tally being a mix of genuine loop-2 (which should tally mostly to one letter)
and misfiled crossbar-shape instances (which should tally toward `e`, like z and 7 do). The actual before/
after counts, run mechanically from the settled `ciphertext_appendix.tsv` through `scripts/01-04` and
`tools/decode_key.py --check`, are reported in NOTES.md "## PX-BROGLYPH" (this job's closing section), not
estimated here -- per CLAUDE.md rule 7, a reading (or a settlement that changes one) is reported from the
script's output, not from a hand count.
