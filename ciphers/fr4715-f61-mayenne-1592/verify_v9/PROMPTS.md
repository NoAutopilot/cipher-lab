# VERIFY-F61-V9 prompts and disclosures (29 Sept 2026)

- Design, categories, gates and read-outs committed 17ccf1ea before any tile existed or any look. One amendment before the tiles were cut, after the
  three placement helpers' rows came back (in the script's docstring): one-letter 'a' words that coincide with a CA position are dropped from the text
  pool (the helpers, asked only for clear words, listed seven CA as the word 'a'); the three other one-letter a's are tiled as EDGE_A, descriptive only.
- No Gallica request: the tiles are cut from the native region already on disk (images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg,
  the one request of 27 Sept 2026), not from any sheet or tile the runner made.
- Placement helpers: three Sonnet calls (lines L01-L04, L05-L08, L09-L11) read ruler strips cut by the verifier from the native image and listed
  clear words and letter x's; they were not told the question. The L09-L11 call listed no letter a; its four a's are interpolated (v9_text_letters.tsv).
- Verifier's one look before the calls: the placement strip of the TEXT and EDGE_A tiles only (22 tiles; no CA, no cipher tile). The markers sit on
  an a-shaped letter in 8 of the 9 text a's; the ninth (a:affaires, L08 x 2662, the word's second a by the helper's index) shows an e-like letter under
  the marker and may be misplaced -- kept as sampled, since gate 1 exists to catch it. The non-a markers sit on the named letters.
- Key v9_items.tsv committed before the calls. Three fresh Opus subagents in parallel, each told to open only its own three sheets.

## setP and setQ (same text, different sheets, shuffles and ids)
Each tile on these three sheets shows one handwritten mark from a 16th-century French letter, marked by a red triangle above and below. Classify
ONLY the mark between the two triangles, by its shape alone: ignore ink weight, size, slant, neighbours and any connecting strokes to neighbours.
Categories:
A = a closed round or oval bowl with one upright stroke on its RIGHT side (the stroke may rise above the bowl or stop at the bowl's top).
O = a closed ring alone, with no stem.
U = two uprights joined by a curve at the bottom, or an n-like arch; no closed bowl.
E = a small closed loop with an open tongue or a crossbar (e-like or c-like).
S = a sign with a hash or bars, a loop crossed by a long vertical (phi-like), a 43-like figure, a 6-like figure, a bracket, a double loop on a line,
    or any other shape not listed above.
X = cannot tell.
Do not guess what letters or values these marks mean; shape only. Answer every tile id.
Output only a TSV with the header id<TAB>answer, one row per tile, then one line "tiles: N". Nothing else.

## setR (free sort, the runner's H235/H256 format)
Each tile on these three sheets shows one handwritten mark from a 16th-century French letter, marked by a red triangle above and below. Look ONLY
at the mark between the two triangles. Sort all the marks into 2 to 6 groups by letterform alone (the shape of the strokes), ignoring ink weight,
size, slant, neighbours and any connecting strokes to neighbours. Name the groups A, B, C ... and give each group 2 to 8 words describing the shape.
Do not guess what letters or values the marks mean. Every tile goes in exactly one group; use a group named "unclear" only if you truly cannot see
the mark. Output only a TSV with the header id<TAB>group, one row per tile, then one line per group "group X: <description>", then "tiles: N".
Nothing else.
