# R2-4 LINE-UNITS -- pre-registration (DEB-SWARM2-R2-4, 29 Sept 2026, written 08:16 UTC before any count below was run)

Brief: DIGEST-1.md "Round-2 prompts", R2-4. CPU only, public-copy transcription only (settled drafts, glyphs/signs.tsv
geometry). No key is scored; nothing here is a reading. Known before writing this: E's 5 of 5 drawn cups/jug line-final
(pict_tests.json) and the digest's 5 of 8 for the broadened class; NOT yet seen: sign widths, the width-matched
counts, the c4 couplet positions of picture-opened lines, any Copiale subsample result.

## Text and units (fixed)
- Units: the 56 cipher lines of the settled drafts (`scripts/settled_lines.py`, prefix `c`), in-line signs only. No page
  drawing enters (portraits, still life, couple, owl are not boxes in the drafts).
- Primary filter: drop H31's punctuation-like classes {BLOB, HOOK-L, DASH-H, `_`, MULTI}; drop the clear digits and
  capitals of clear_spans.tsv (H43: not cipher signs); drop the c2a_L02 pos-28 page-edge artefact (E, PAGEMAP).
  Sensitivity (reported, not decisive): E's filter (clear spans kept).
- Widths: `glyphs/signs.tsv` box width w (1:1 with the drafts, checked 56/56 lines), normalised by the median w of the
  same line's kept signs (removes page scale).

## Classes (fixed by what is drawn, from inventory_settled.tsv ids, before any position is counted)
- CLOSERS (every drawn container): BUCKET, PICT-JUG, BOX-M, PICT-BOTTLE, PICT-BARREL, PICT-GLASS (8 tokens).
- OPENERS (drawn pictures): every PICT-* id not a container, plus SUN, HEART, RAM, CHAIN. STAR is excluded (an asterisk,
  not a drawing: PICTURES.md); a sensitivity row includes it.

## Tests and kill rules (alpha fixed here)
- T1 container line-final: statistic = container tokens in a line's last kept slot; null = 10,000 within-line shuffles
  (each line's multiset fixed). KILL-1 if p_ge >= 0.01.
- T2 width-matched layout control: for each container token, draw one non-container token whose normalised width is
  within +-20 pct of it (any sign; second version: non-picture signs only), 10,000 draws of 8; statistic = how many of
  the 8 are line-final. p_layout = P(draw count >= containers' observed final count). KILL-2 ("wide signs at line ends
  as often") if p_layout >= 0.05 in either version. Also reported: the line-final rate of the whole width-matched pool.
- T3 couplets: among c4's 20 verse lines (c4a0_L01, c4a_L01-14, c4b_L01-05 = verse 1-20; couplets 1-2, 3-4, ...), the
  lines whose first kept sign is an OPENER; statistic = how many are couplet-first (odd) lines; exact null = random
  choice of that many lines out of 20 (10 odd). Supported if p <= 0.05. If the minimum reachable p (all odd) is > 0.05,
  T3 is logged "untestable at this N", not a negative.
- Overall: the vessel rule counts as system only if KILL-1 and KILL-2 are both not met.

## Known-answer controls (run first; the test is read only if they pass)
- K1 Copiale decorative capitals (G-F/data/copiale-transcription.txt, F's capital class: single upper-case Roman letter,
  N excluded) as a known line opener, at Debosnys's size: 1,000 windows of 56 consecutive Copiale lines; in each,
  the class is cut to 8 randomly chosen capital tokens (others stay as ordinary tokens); the T1 statistic on the first
  slot, 2,000 shuffles, alpha 0.01. PASS if detection >= 80 pct of windows. K1r: the same windows with every line
  reversed (a known closer) through the exact T1 final-slot code. PASS if >= 80 pct.
- K2 planted closer on Debosnys's own lines: 8 tokens relabelled PLANT, 5 of them line-final tokens and 3 random
  mid-line tokens (the observed-scale rate), 500 plantings: T1 detection rate (power, gate >= 80 pct). Also 8 random
  tokens (false-positive rate, gate <= 5 pct) and 3 of 8 final (reported power curve point).
- K3 T2 calibration: a fake class of 8 random tokens drawn from the width-matched pool must NOT trip "system" more than
  5 pct of 500 draws; a fake class of 8 line-final tokens of ordinary width must be separated from its own width-matched
  draws (p_layout < 0.05) in >= 80 pct of 500 draws.
