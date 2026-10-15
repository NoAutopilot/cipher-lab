# PREREG-AVS-153 (15 Oct 2026, 14:5x UTC by date -u; worker AVS-153, account 2, for LANE DEFAULT-A2-1410-15)

Job: WVO 153 p6 (f.4) cipher lines 10-20 (crops L11-L21 of `tools/iiif_lines.py --image <scratch>/r/nat-005.jpg --out <scratch>/c6 --debug`,
21 bands, same banding as WVO-153-KEY), two blind Sonnet passes per band (band 10-15, band 16-20; pass A given WVO-153-KEY's labels,
pass B its own inventory), reconciled by this worker on the crops, aligned by hand to the period decipherments (W2 p8/f.6, W1 p7/f.5).
Registered before any token is valued:
1. Values come only from the aligned witness text (grade C); a token whose cipher spelling departs from both witnesses, or whose class
   the passes split on and the crop does not settle, is M; a new class seen in one token only is M.
2. Gate G1 (rule 3, same statistic as w153/controls_153.py (a)): shuffle-consistency of all valued tokens of lines 1-20 under key_153
   must exceed its shuffled p95 (2000 shuffles, seed fixed), and lines 10-20 alone must also exceed their own shuffled p95. Withheld
   tokens are reported as misses on a second line.
3. Gate G2: key_153 vs key_98 on the pre-fixed map (digits + key_98 readers' own labels) must stay above permuted p95; any class whose
   lines 10-20 value contradicts key_98 is listed, not folded silently.
4. A class whose lines 10-20 value differs from its lines 1-9 value is a conflict: it goes to M and is listed, never settled by count.
5. Stop rule: stop before a unit that would cross 80% of cap (USD 6) or box (90 min, end 16:16 UTC).
The plaintext is known from the leaf (key source): this builds key_153 for the unread letters of this key family (System B / key_98:
WVO 126's key-level M tokens, WVO 58, WVO 175 pp.3-8), not a reading of an unread text.
