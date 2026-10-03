# SEURE-KP pre-registration (3 Oct 2026, committed before any read or score)

Worker SEURE-KP (LANE-A2PUSH3, account 2), brief `.claude/briefs/runs/2026-10-03-acct2-seure-kp.md`.

## Span hypothesis (H-span)

From GAPS102: items 43 and 44 carry the same closing formula and date (M) and share recurring cipher groups
(`40 n R`, `n R ∆`, `13 30`) but are not sign-identical copies. Survey views f81 and f85 (500 px, on disk) show
item 43's f81R as a short clear opener followed by dense cipher to the foot of the page, and item 44's f85R as
about 13-14 lines of clear prose followed by a cipher block.

**H-span:** item 44's opening clear paragraph on f85R (every clear line after the address/opener line, up to the
first cipher sign) is the plaintext of item 43's cipher that begins immediately after 43's clear opener on f81R,
in the same order, start-anchored (first enciphered sign of 43 <-> first letter of 44's clear paragraph after the
shared opener words). If 44's opener words also appear in clear on 43's line 1, they are dropped from P so both
spans start at the same point of the text.

The end of 43's matching cipher span is unknown, so three cipher-span lengths are fixed in advance as ratios of
cipher signs to plain letters: r = 0.70, 0.85, 1.00 (C_r = the first round(r x |P|) cipher signs after the
opener; 43's cipher is read on f81R only, enough lines to cover r = 1.00 plus one line).

## Statistic

`tools/interlinear_align.py`'s `run_align` (imported, no private DP), one pair (P, C_r), every sign token
marked as a code (`--code-prefix @`, each code takes 0 or 1 letters: a letter-substitution reading; numerals
and invented signs treated alike), `--null-cost 0`. Consistency S = share of code tokens whose aligned
chunk equals the code's modal meaning with count >= 2 (status `agrees`) over all code tokens.
The test statistic is S* = max over the three r of S_r.

## Controls (run before the target)

1. **Positive (power) control, matched:** P enciphered with a random homophonic substitution whose sign
   inventory K and length match C_1.00 (K = distinct signs read in C_1.00), at 0% and at 15% sign substitution
   error; S* computed the same way. If the positive control at 15% error does not clear its own null p95 the
   test is logged a non-test at this N (rule 3), not a negative.
2. **Nulls, 200 draws each, computed with the same max-over-r:** (a) shuffled gloss: P's letters permuted
   uniformly; (b) rotated gloss: P rotated cyclically by a uniform offset in [|P|/10, 9|P|/10]. Both keep P's
   letter counts, and both can move S (they destroy the alignment of repeats between P and C), so they can
   differ from the target.

## Gate

H-span **licensed** (a key fragment may be drafted, grade C only where the clear text is read H) iff S*(real)
> p95 AND > max of BOTH null distributions. Otherwise logged as a negative conditional on H-span and on the
reads (not a design-family negative; rule 3's third-attempt clause does not apply to a first attempt).

## Reads

f85R clear lines: one Opus subagent read of line crops (`tools/iiif_lines.py`, command pasted in NOTES.md),
letters only, abbreviations expanded only where the hand writes them out, unread letters `?`. f81R cipher: one
Opus subagent sign-count/segment pass of line crops with the existing f75L glyph conventions where they fit
(`glyphs/`), unknown signs given ad-hoc labels consistently. Then one reconciliation by the worker. Signs read
and cost per 100 signs recorded.

## Amendment A1 (3 Oct 2026, committed after crops were cut, before any read or score)

Crops (`images/kp/`, debug overlays checked) show f85R's clear prose runs the whole top of the page (23+ lines,
~1,500 letters), longer than one leaf of 43's cipher at any r. To fit the cap, P is fixed to the clear text of
f85R crop lines L01-L08 from "(que je donnay ..." (the words 43 also writes in clear on f81R line 1, "Sire, Je
vous escrivis par mes dernieres ... doctobre", are dropped, per H-span's start anchor; f81R's clear opener ends at
"doctobre" and its cipher begins on the same line). C is read from f81R line 1 (cipher part) through as many
lines as C_1.00 + one line needs (~L01-L20). A prefix of the H-span pair is still an instance of H-span.
The positive control is also run at 40% sign error, because this folder's earlier two-reader passes on f75L
agreed at only 38-52% (rule 3: the control's injected error must bracket the target's reader error); if the
control fails at 40% but passes at 15%, a target miss is logged "non-test above ~15% reader error", not a negative.

## Amendment A2 (3 Oct 2026, after both reads, before any score on them)

`--null-cost 0` is degenerate in `align_pair` (a letter on a code costs -0.5 and a trailing unaligned plain letter
-0.3, so with free nulls the first iteration aligns nothing and S = 0 for every input; found by reading the code,
no score computed on the reads). The tool's default null cost (-3.0) is used instead, for target, nulls and
control alike. Draw counts cut to fit the box: nulls 200 each (unchanged); positive control 3 synthetic keys per
error level x 30 shuffled-gloss draws each. No reconciliation vision unit is run (one reader per side, confidence
0.6 clear / 0.55 cipher, as self-reported); the 40% control level stands in for the unmeasured reader error.
