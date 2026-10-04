# f.228 batch B2 (L05-L08) pre-registration ADDENDUM (N8-NV05B, account-2 worker for LANE-NEAR8), 4 Oct 2026, 16:43 UTC by `date -u`

Pushed before any crop of L05-L08 is cut, any pass is run or any score computed. What this worker has seen of L05-L08
before this file: nothing on the image (the native region below L04 has been fetched to disk by a `--dry-run` for
geometry only and not yet looked at); in NOTES.md, N8-NV05 pass GB's misplaced read of the faint line below L04's cipher
("mi salu[..]on manda ... por talas sus cartas que tenga ..."), which N8-NV05 identified as L05's gloss. Disclosed; that
is why the gloss passes below are blind and the reconciler adds no word neither pass read.

## Unchanged (PREREG.md + PREREG-ADDENDUM-N8.md)
- Statistic S: `../control_fr3641/score_control.py` `score()` (imported), its norm() and abbreviation table, plus the
  N8 addendum's fixed extra rule (`build_gloss_v2.py` `clean()`, imported: [..] spans removed, ? and ^ dropped,
  qe/ql/dho/dha/V.Md expanded, nothing else).
- Key: `key_syllabary.tsv` (the 95 coded rows of ../key_no54.tsv, unedited). Tokeniser: `build_ciphertext.py` `toks()`
  (digit runs split into 2-digit codes from the left, odd final digit single, letter runs one token, other signs one each).
- Control: values shuffled among the 95 coded rows, 1000 draws, seed 1, scored against the same gloss.
- Gate: PASS iff S > control p99 AND S >= 0.60.

## Scope and what is gated
- B2 = the four bold cipher lines after L04 (L05 = the first bold cipher line below L04's "80.17c 73 92 ..." line),
  their four glosses. Nothing from L09 on is read.
- **Gated number: S on L05-L08 alone** with its own control (seed 1). Reported beside it, not gated: pooled L01-L08
  (ciphertext.tsv + the B2 ciphertext, gloss_v2.tsv + the B2 gloss) with its own control (seed 1, 1000 draws).

## Crops and the line-placement rule (from crop geometry, the fix GB needed)
- One native region of canvas 235 covering L05-L08 and their glosses, fetched once by `tools/iiif_lines.py`; one crop
  set, one band per line, each band holding Ln's bold cipher line in its lower part and the faint gloss line above it
  (band edges a little below each cipher line's descenders), segments <= 1900 px with overlap; `--follow-slope` if the
  debug overlay shows the lines leave a fixed-y strip. Command and overlay check pasted in NOTES.md before the first read.
- **Rule:** a gloss word belongs to Ln iff, on the crop, it lies above Ln's bold cipher line and below L(n-1)'s bold
  cipher line, within the same column span. Gloss readers are given each segment's bold-line opening signs (from cipher
  pass A, the anchor only, no decode) and told to read only the faint cursive line directly above that bold line,
  nothing below it. A placement disagreement between GA and GB is settled by this rule on the crop, never by the decode;
  text read below the bold line is dropped.

## Passes, reconciliation, units
- Cipher A and cipher B: two blind Sonnet passes, one call each on all B2 crops, NV05E's cipher prompt (tokens left to
  right, digits as written, dots/colons/letter signs kept, '?' for doubt).
- Gloss GA and GB: two blind Sonnet passes, one call each on the same crops, the N8 gloss prompt plus the anchor; neither
  sees the decode, the other pass, gloss.tsv/gloss_v2.tsv or NOTES.md.
- Reconciliation (1 unit, this worker, on the crops): cipher A/B disagreements settled from glyph shape and graded M; gloss
  disagreements settled only where the glyph shape decides, otherwise the span becomes [..] (dropped). No word or token
  neither pass read is added. err_2reader reported for cipher tokens and gloss words (agreement, not accuracy).
- Units: 5 (A, B, GA, GB, reconciliation) at ~USD 1.5 each against the USD 8 cap and the 75-minute box; no unit started
  past 80% of either.

## Reporting
L05-L08 S, p99, mean, max, count >= real, gate; pooled L01-L08 the same, ungated; per-line counts. PASS or FAIL written
as is. Grades per VERIFY-NV05 (syllables from the period sheet H; letter signs and code words U). AUDIT.md (N0) gets a
dated revision note if the reading grows. Decode via `tools/decode_key.py` (second job in decode.json), `--check` exit 0.
