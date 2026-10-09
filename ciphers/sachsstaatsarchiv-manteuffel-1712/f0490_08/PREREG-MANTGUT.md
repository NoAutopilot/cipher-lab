# PREREG-MANTGUT (9 Oct 2026, 20:2x UTC by date -u; written before either blind rendering pass is run and before any score; LANE FAMILY-A2l account 2)

Leaf: HStA Dresden 10026 Loc. 694/08, film frame 0490, vertical two-line code run in the gutter margin (MANT-0490L; 38 tokens incl. a
leading '7' that may be an insertion mark) and, on the same two margin lines after a stroke, a clear rendering in the same hand
(V-MANT0490L eye check: 'et a la satisfaction des deux parti / belligerents'). Named next of AUDIT "AUDIT (V-MANT0490L)": gate (a) on the
gutter with the clear rendering as one span. A key test, not a reading; the plaintext is on the leaf (N0 by construction).
Question: does key.tsv (origin/main at be573943b; unchanged since a768bc651's key commit chain as used by MANT-0490L) read the BLIND-pass
gutter digits the way the leaf's own clear rendering reads, above what permuted keys give?

Disclosure: this worker has seen key.tsv, MANT-0490L's decode of the gutter, V-MANT0490L's eye reading of the rendering, and the rendering
itself on gutter_rot.jpg while cutting the crop. For that reason the rendering text is NOT read by this worker: it comes only from two blind
Sonnet passes that see the rendering crop alone (no digits, no key, no decode, no prior reading in the prompt).

Inputs (all committed; no fetch):
- Rendering crop: f0490_08/crops/r0490G01_L01.jpg, cut from committed f0490_08/gutter_rot.jpg with
  `tools/iiif_lines.py --image f0490_08/gutter_rot.jpg --region 735,55,505,75 --centres 37 --out f0490_08/crops --prefix r0490G01`
  (clear words only; no code digit in the crop).
- Rendering passes: R1 and R2, two independent blind Sonnet calls on that crop (R2 told to read word by word right-to-left then write it
  in order) -> f0490_08/render_R1.txt, render_R2.txt, used exactly as written: letters only, accents stripped, '?' letters dropped; this
  worker never corrects, completes or settles a rendering letter.
- Digits: the blind code passes' gutter tokens exactly as committed, passA_L.tsv and passB_L.tsv rows crop c0490G01 (38 tokens each, '?'
  stripped); NOT the reconciled ciphertext_L.tsv (V-MANT0490L found reconciler departures from both passes made with key values in view).
- Span: ONE span = the whole rendering (both margin lines, in order) over all 38 gutter tokens in order (r1 then r2), the '7' included as read.

Statistic S: exactly f0490_08/gloss_gate_L.py's alignment (copied unchanged into f0490_08/gutter_gate.py): a code whose key value (any '|'
alternative, letters only) equals the next rendering letters scores 1; a code may consume 1-3 letters unmatched (0) or none (-0.25); a
rendering letter may be skipped (-0.25). Name/word codes match only when the rendering spells the whole value (356 'deux', 1000 'et').
Control (rule 3): key.tsv values permuted over its codes, 1000 draws, seed 491, same span and alignment. The control CAN differ from the
target on S (S depends on which value each code carries; the permutation changes exactly that). Reported with it: the control's own blind
level (mean, p99) so a near-ceiling control would be visible.

Gate (a), deciding: four rows = digits {passA, passB} x rendering {R1, R2}. Each row PASSes if S > p99 AND S >= 0.5 x keyed tokens.
**Gate PASS = all four rows PASS.** Any row FAIL = gate FAIL (logged, no grade moves). Fewer than 10 keyed tokens in a row = too short.
Reported only (no gate): reconciled ciphertext_L.tsv x R1 and x R2.
Per-class breakdown (rule 3, unbalanced classes), each deciding row: tokens split by key value class -- 'letter' (every alternative is one
letter), 'multi' (any alternative of 2+ letters: et, deux, s|sa, r|re|ro, b|[a], o|a counts as letter), 'unkeyed' -- real matched/keyed per
class beside the control's per-class mean and p99. Read: if the PASS rests on one class only, say so.

Grades if PASS: a gutter token matched on all four deciding rows -> C (matched to the leaf's clear rendering under a passing gate); matched
on some rows -> M; unmatched -> M. If FAIL: all 38 stay M (V-MANT0490L's grading). key.tsv: unchanged unless PASS; then only rows graded M in
key.tsv whose code is matched at >= 2 distinct gutter positions on all four deciding rows move M -> C (source 'leaf 0490 clear rendering,
MANT-GUT'); no new code, no value change, no C -> anything. `tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712 --check` after.
Outputs: f0490_08/gutter_gate.py (--check), f0490_08/gutter_gate.out, NOTES "## MANT-GUT".
