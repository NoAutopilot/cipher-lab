# PREREG HAR-39V2 (15 Oct 2026, written 11:4x UTC by date -u, before any image fetch, any read or any score)

Target: BL Harley MS 287 f.39v (DECODE R8479 image 4), line G word 3. HAR-39V (d5d3c580a, one reader, not blind to
Bourdeau's strings) read 10 signs `U U: J: D J: O: ? F. O C` = b-u-t-i-t-y-?-p-e-d, sign 7 blotted; word M.
Key: Bourdeau's closed three-grid pigpen (needham1587/decode.py, MIT): shapes J U L / C O F / N 7 D = a-i plain,
dot below = k-s, dot inside = t-z. Not changed by this job.

## Part 1: second blind reader
Image: R8479 f.39v full size, re-fetched in this session's one DECODE browser login (scratchpad only, never in git).
Crops: PIL crops at native resolution of line G words 1, 2, 3, 4, 5, 8 (word boxes from tx/f39v_lineG_har39v.tsv
x_native, y band 3170-3330, re-located on the image if the band is off), each enlarged 3x, saved with neutral labels
in a shuffled order fixed by `random.Random(39)` over the six words. Reader: ONE fresh Opus subagent vision call,
given only the six crops and the alphabet description (nine shapes by grid cell, three mark states), told that some
words are checks and not told which, never shown Bourdeau's strings, HAR-39V's table, the letter's subject or any
plaintext. It returns, per crop, the sign count and shape+mark per sign (or `?` with a note). I do not read the crops
myself before its answer is saved to tx/f39v_lineG_har39v2.tsv.

Gate C2 (controls = words 1, 5, 8, Bourdeau's strings `L 7 J C. O U.`, `7 O. O: O D.`, `F J D. J: O C. O C`, 19 signs):
PASS if >= 18/19 signs equal in shape and mark and all three sign counts right; else CONTROL FAIL -> the target
read is a non-test and nothing below is scored. Words 2 and 4 (`L: J D.` was, `L: D J: 7` with) are reported, not gated.

Target outcomes (compare reader 2 with HAR-39V sign by sign, sign 7 excluded since HAR-39V left it `?`):
- A: reader 2 also counts 10 signs and agrees on >= 8 of the 9 signs 1-6, 8-10 -> those agreed signs are a two-reader
  read (still M as a word: the string decodes to no English word under the key; no slip hypothesis tested here).
- B: reader 2 counts a different number of signs, or agrees on < 8 of 9 -> reader conflict, logged sign by sign, word M.
- In either case, if reader 2's string decodes under the key to an English word that fits line G's sense, it is
  reported as one reader's candidate (M), not adopted.
No grade upgrade beyond "two-reader agreed sign" in this job; word stays M under both outcomes unless both readers
agree AND the agreed string decodes to an English word (brief: "Word stays M unless both readers agree and the
controls pass").

## Part 2: R8478 / R8480 (Decrypted, ff.37-38 and ff.41-42, 1587, flanking Needham's ff.39-40)
Same login: record pages, thumbnails and --guess-fullsize images, <= 30 requests total for the session, >= 1.5 s apart.
Look (by eye on downscaled copies, then native crops where needed) for: (i) the hand and alphabet (same three-grid
pigpen or not); (ii) interlinear or marginal gloss; (iii) any word whose signs match HAR-39V's word-3 string or its
-?-p-e-d ending (`? F. O C`), or the b-u-t opening (`U U: J:`), with its gloss if glossed. Outcomes:
- R1: a glossed occurrence of the same sign group is found -> reported with its gloss (grade C for that occurrence
  only; f.39v word stays M until a later job tests it at the f.39v position).
- R2: same alphabet, glossed, no matching group -> reported as a negative for this word; the gloss pairs are noted
  as material for a later alignment job (not aligned here).
- R3: different system, unglossed, or images refused (forbidden.png) -> reported as such.
Report found / not found; no novelty class.
