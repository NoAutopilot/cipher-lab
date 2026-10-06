# R11-SURTV pre-registration (6 Oct 2026, account 2; written and pushed before any tile is cut or scored)

Question: is the map readers' code `y` (4.VEL 2039 legend, 2061 battery block; key_period_codes_nieuw.tsv y = d, M) the same
written sign as the inv. 373 letter's y-family (Texier, 29 Oct 1781; gloss m|n 21/21, R11-SURY)?

Tile classes (fixed now; a token that cannot be located on its crop is dropped and reported, never replaced):
- MAPY (11): every reader-code `y` in ciphertext_2039_legend.tsv lines head/a/g that this worker can place (head:0, head:9,
  a:2, a:8, g:0) and every `y` in ciphertext_2061_battery.tsv (L02:10, L04:10, L06:18, L06:22, L07:0, L09:36, L10:11).
  [12 listed; head:9 is dropped in advance if its segmentation (y vs [psi]) cannot be placed on the crop.]
- LETY (21): R11-SURY tokens.tsv t01-t21 (letter y-family, gloss m 12 / n 9), same centres.
- DREF (d reference): the map's d-signs (2061 L06:5 [v-tall], L08:27, L08:45, L08:50, L10:0 v; 2039 c:0 v) and the letter's
  d by gloss (den L01, den L07, omstandigheeden L02 both d, versuymd L06 final d, omstandigheeden M02 both d, versuimd M01 final d).

Crops: map tiles from images/2039_legend_native.jpg and images/2061_battery_legend_native.jpg (native; line bands by
tools/iiif_lines.py, commands in crops.txt); letter tiles as R11-SURY (inv373_0693_r10/crops, inv373_yfam_r11/c93n). Each tile is
cut +-70 px (map 2061: +-45 px, smaller hand) around the sign centre, scaled to a common height, anonymised and shuffled (seed 1781)
on contact sheets with no class or sheet label visible; the worker scores from the sheets before joining the key.

Features (binary, per tile, the marked sign only):
- F1 tail: a stroke continues clearly below the baseline (a descender) from the sign's right arm.
- F2 tall: an arm rises clearly above x-height or ends in a loop above it (tall/looped v).
- F3 dots: two dots (or a diaeresis-like pair) above the sign.
Shape call: Y-form = F1 and not F2; V-form = not F1; other = F1 and F2.

Statistic and gate: A = share of MAPY tiles called Y-form; B = share of DREF tiles called Y-form; T = A - B.
Control: 10,000 permutations (seed 1781) of the MAPY/DREF labels over those tiles, recompute T; p99.
- SAME SIGN (as LETY) if T > p99 AND A >= 0.8 AND LETY's Y-form share >= 0.8.
- DIFFERENT (map y is a v-form like the d-signs) if A <= 0.2.
- Otherwise UNDECIDED.
The control can vary on T (it moves tiles between the two groups whose Y-form shares are compared).
F3 (dots) is reported per class, descriptive only.

Consequence fixed in advance: no key change either way. SAME SIGN -> the map's y = d (context) and the letter's y-family = m|n
(gloss) become a rule-4 conflict on one sign: a row in conflicts.tsv with both witnesses, y stays M. DIFFERENT -> the letter is
no witness on the map's y; y = d stays M as is. UNDECIDED -> logged, y stays M.
