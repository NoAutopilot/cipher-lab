# PREREG MQS-CVD-AUDIT (account 4), written 09:39 UTC 9 Oct 2026 by date -u, pushed before the control runs

Option: `tools/cvd_check.py --audit FILE...` -- extracts colour literals (hex `#rgb`/`#rrggbb` in any file; 3-int tuples
on cv2 drawing lines read as BGR, other tuples as RGB) from a tool's source or template, keeps the chromatic ones
(CIE LCh chroma >= 15), and flags a pair as CVD-COLLAPSE when it is distinct in normal vision (CIEDE2000 >= 20) but
under COLLAPSE = 10 under protan, deutan or tritan simulation (Machado et al. 2009). Also flags RED-GREEN hue pairs
(the project rule "never red against green"). It is a lead list for a person, not a verdict on the page: it cannot
see which colours co-occur, which carry meaning or what they sit on (contrast stays with --marks/--bg).

## Calibration (seen before this file; NOT the control)
COLLAPSE = 10 was chosen on: Okabe-Ito 7 (21 pairs: minimum simulated dE 11.1, 0 flags at 10; 10 of 21 pairs fall
under the existing gate's 18 WARN floor -- so 18 is too strict to mean "collapse"); and 10 problem pairs (tab10
red/green, blue/purple, orange/green, brown/green; pure red vs three greens; Set1 and Paired red/green; #cc0000/#00cc00),
8 of 10 under 10. Declared tuning, not sourced (M09 still open).

## Control (held out; labels by hue family, not by the simulation)
- Positives, 10 pairs from palettes not designed for CVD, each red-vs-green or blue-vs-purple: ggplot2 (#F8766D,#00BA38),
  (#F8766D,#7CAE00); ColorBrewer Set1 (#377eb8,#984ea3); Dark2 (#d95f02,#1b9e77); Set2 (#fc8d62,#66c2a5); Office 2007
  (#C0504D,#9BBB59), (#4F81BD,#8064A2); Google Charts (#dc3912,#109618), (#3366cc,#990099); Bootstrap (#dc3545,#28a745).
- Negatives, 31 pairs from palettes designed for CVD: Paul Tol bright (#4477AA #EE6677 #228833 #CCBB44 #66CCEE #AA3377,
  15 pairs, grey #BBBBBB dropped as neutral) and IBM design library (#648FFF #785EF0 #DC267F #FE6100 #FFB000, 10 pairs),
  plus Tol vibrant's #0077BB #33BBEE #009988 #EE7733 #CC3311 #EE3377 limited to 6 pairs (0077BB-EE7733, 33BBEE-CC3311,
  009988-EE3377, 0077BB-CC3311, 33BBEE-EE7733, 009988-CC3311).
- Each set is written into three synthetic files (HTML hex, Python RGB tuples, cv2 BGR tuples) with neutral distractors
  (#ffffff #000000 #f3f1ec #24211c) and the audit is run on the files, so extraction is tested with the pair logic.
- Statistic: CVD-COLLAPSE recall on positives (pair counted if flagged in all three formats), false-flag rate on negatives.
- Null: the same files with every colour's channels rotated (RGB -> GBR) before writing. Why it can fail differently:
  rotation moves hues, so a red/green pair becomes green/blue or blue/red and its simulated distance changes; the
  statistic is computed per pair from colour values, so it is not fixed by construction (unlike a pair-order shuffle,
  which cannot change an all-pairs statistic and is therefore not used).
- Extraction check: every planted literal recovered in the right channel order in all three formats (expected 1.000).

## Gates (expected, then pass line)
- Recall on held-out positives: expected ~0.7-0.9; PASS at >= 0.70.
- False flags on negatives: expected 0-3 of 31; PASS at <= 3/31.
- Null recall (rotated): PASS when <= recall - 0.30.
- Headroom: no restarts are involved (deterministic), and recall is not near ceiling by design of the null.
All four pass -> shelf `controlled-only`; any miss -> `weak` with both numbers, not re-briefed.

Then the audit itself runs over tools/build_dashboard.py, tools/glyph_atlas.py, tools/sign_sorter/template.html,
tools/decipher_sheet.py (and any other tool found drawing colour), findings reported, no tool edited by this job.
Credit: Okabe and Ito 2008; Machado, Oliveira and Fernandes 2009; Sharma, Wu and Dalal 2005; W3C WCAG 2.1; Paul Tol
(SRON) colour schemes; IBM Design Library; Wickham (ggplot2); Brewer (ColorBrewer).
