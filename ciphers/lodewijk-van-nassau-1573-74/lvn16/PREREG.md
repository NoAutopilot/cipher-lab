# R12-LVN16 pre-registration (6 Oct 2026, written before any blind read is opened)

Material: WVO 4616 p1, rendered at 300 dpi (pdftoppm -r 300, 2481x3508, sha1 4f47b490f28e2cfeebaf5352c34f64af87636148),
cipher block = ciphertext_4616.tsv lines p1_L05-p1_L17 = crop lines L01-L13 of
`tools/iiif_lines.py --image 04616-1.png --out crops --prefix 04616_p1 --region 0,320,2481,880 --distance 45 --prominence 20`.
Targets: lvn16/targets.tsv (50 rows: 34 non-H rows of the block, plus the 19 slash groups, 3 overlapping).

Reads: two independent blind Sonnet passes (A3, B3), each transcribing every token of every crop line, never shown
pass A/B, the key, or each other. Tokens are aligned to ciphertext_4616.tsv per line by difflib on the token sequence.

Control (known answer, can fail differently from the targets): every H row of the block that is not a slash group
(the rows both 150-dpi passes agreed on). Per blind pass, exact-match rate on aligned H rows. Gate: each pass >= 0.90.
If either pass is below gate, no target row is changed (non-test at this reader accuracy); results logged only.

Settle rule, applied only if the gate passes:
- a non-H row is settled (confidence H, why "image300 lvn16") when A3 and B3 read the same token there; the value may
  equal pass A, pass B or neither (the 300-dpi image outranks the 150-dpi passes);
- if A3 and B3 differ, the row stays M, both reads logged in the alt column; no reconciler override is applied.
- slash groups: if A3 and B3 both read the stroke as a separator between digit groups and agree on every group, the
  token is split into its codes (consecutive rows, positions renumbered within the line, note "split lvn16"); each part
  is decoded from key_full; a part outside key_full stays U. Otherwise the row stays as it is.
Counts reported: C/H/M/U for 4616 before and after, and the four-letter 57.5% figure recomputed.
