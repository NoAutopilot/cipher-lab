# R2-4 LINE-UNITS -- result (DEB-SWARM2-R2-4, 29 Sept 2026, 08:20 UTC)

Pre-registration: `PREREG.md` (commit 572aa02d, pushed before any count). Script: `line_units.py` -> `line_units.json`
(CPU, about 20 s; reproduces exactly: every random step is seeded). Public-copy transcription only. No key, no value,
no plaintext: nothing here is a reading. Grade S throughout.

## Verdict first

**Control FAIL at the registered gates, so the target numbers below are held as unlicensed** (PREREG: "the test is read
only if they pass"; no gate was moved and no second attempt was made, CLAUDE.md rule 3). The numerical kill tests were
**not met**: the broadened container class sits at line ends far beyond within-line shuffles and far beyond wide signs of
the same drawn width. But the effect rests entirely on the three ids E named after seeing positions (cups and jug, 5 of 5);
the three containers added by the digest (bottle, barrel, glass) are 0 of 3 line-final. The couplet prediction fails.

## Known-answer controls (run first)

| control | registered gate | result | pass |
|---|---|---|---|
| K1 Copiale decorative capitals as a line opener, 56-line windows, class cut to 8 tokens, alpha 0.01 | >= 0.80 detection | 0.310 (310 usable windows; 690 of 1,000 had < 8 capitals) | **FAIL** |
| K1r the same, lines reversed (a known closer) | >= 0.80 | 0.297 (317 windows) | **FAIL** |
| K2 planted closer on Debosnys's own lines, 5 of 8 final | >= 0.80 power | 1.000 (500 plantings) | pass |
| K2 planted closer, 3 of 8 final (power curve point) | reported | 0.868 | -- |
| K2 8 random tokens (false positive) | <= 0.05 | 0.006 | pass |
| K3 width test, random fake class of 8: falsely "system" | <= 0.05 | 0.054 (500 draws) | **FAIL (marginal)** |
| K3 width test, 8 line-final tokens of ordinary width separated from width-matched draws | >= 0.80 | 1.000 | pass |

Why K1 fails (diagnostic, not a re-gate): the Copiale capital class as F defined it (single upper-case Roman letter, N
excluded) has 196 tokens in 1,768 lines (6.2 per 56 lines, so most windows are unusable), 95 line-initial overall (48
pct), and in the windows dense enough to hold 8 capitals only 24 pct of them are line-initial (877 of 3,716); many are
mid-line. At 8 tokens and Copiale's 42-sign lines, a marker that opens a line a quarter of the time is not reliably seen
at alpha 0.01. So K1 measures the test's power for a diffuse marker, and says the test would miss one of Copiale's
strength at Debosnys's size -- a limit on any *negative* this test gives, which is not the direction of the target
result. K3's miss is a design flaw in the registration itself: a gate at the nominal alpha (0.05) is met or missed by
sampling error (500 draws, SE about 0.01). Both are reported as FAIL anyway; the registered rule is all six gates.

## Target tests (held as unlicensed; reported because they are the numbers)

**T1, containers line-final** (8 tokens, primary filter): 5 of 8 in the last kept slot; within-line shuffle mean 0.33,
p_ge 0 of 10,000, exact p 3.4e-6. KILL-1 (p >= 0.01) not met. Sensitivity with clear spans kept: 5, mean 0.31, p 0.

| token | line | pos / of | wnorm | final |
|---|---|---|---|---|
| BUCKET | c2a_L02 | 22/22 | 1.30 | yes |
| PICT-JUG | c2a_L12 | 30/30 | 1.85 | yes |
| BUCKET | c2a_L13 | 30/30 | 1.76 | yes |
| BUCKET | c2b_L04 | 26/26 | 0.98 | yes |
| BOX-M | c3_L02 | 33/33 | 1.50 | yes |
| PICT-BOTTLE | c2a_L02 | 9/22 | 1.30 | no |
| PICT-BARREL | c2a_L10 | 17/29 | 1.13 | no |
| PICT-GLASS | c4b_L05 | 11/14 | 1.11 | no |

Selection note: BUCKET, PICT-JUG and BOX-M are the ids E tested after H33 had flagged line-final classes (E's own
E1b showed PICT-JUG and BOX-M were below H33's floor, so 2 of the 5 were not position-selected). The three containers
named only by drawing are 0 of 3 final. So the pre-registered broad class passes on the strength of the cups and jug;
"containers close lines" is not supported for bottle, barrel or glass, and the cup rule is the part that holds.

**T2, width-matched layout control**: for each container, a non-container token within +-20 pct of its line-normalised
width (candidate pools 104-576 tokens each). Expected finals if width drove position: 0.37 (any sign) and 0.36
(non-picture signs); p_layout 0 of 10,000 in both. KILL-2 not met. Across all non-container tokens the line-final share
rises only mildly with width: < 0.8: 3.4 pct; 0.8-1.25: 3.9; 1.25-1.6: 6.8; 1.6-2.2: 6.8; > 2.2: 8.3 pct (24 tokens) --
a small layout effect, an order of magnitude below the cups' 5 of 5.

**T3, picture-opened verse lines vs couplet starts**: 4 of c4's 20 verse lines open with a drawn picture: verse lines 2,
4, 13, 14 (PICT-HEART, SUN, PICT-LEAF, PICT-ANCHOR); 1 of 4 is a couplet's first line; exact p_ge 0.957 (minimum
reachable 0.043, so testable). **Not supported.** (Post hoc, not a test: 3 of 4 are couplet-second lines, P about 0.29.)
Same with STAR included (no change).

Sanity: drawn-picture openers on all 56 lines, 11 line-initial vs shuffle mean 2.36, p 0 of 10,000 (H31 reproduced with
the pre-registered class, STAR out, clear spans out).

## For the orchestrator

- What would license T1/T2: a known-answer marker control that passes at Debosnys's size. The Copiale capital class is
  too diffuse for 8 tokens; a registered replacement (e.g. Copiale's line-initial capitals only, or a period cipher with
  a known terminal mark) is a new instrument, which rule 3 allows; re-gating this one is not.
- Whatever the licence, the pre-registered broad container class adds no support beyond E's cups: 0 of 3 new containers
  close a line. If the cup rule is used downstream, it is "BUCKET/PICT-JUG/BOX-M close lines", not "containers do".
- Pictures do not mark couplet starts in the verse (1 of 4).
