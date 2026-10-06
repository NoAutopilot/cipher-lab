# R12-LVN10 pre-registration (6 Oct 2026, written before any blind read is opened)

Material: WVO 4610 p3, rendered at 300 dpi (`pdftoppm -png -r 300 -f 3 -l 3 04610.pdf`, 2481x3508,
sha1 a41b5df838e49cefb71e30cdfbe0803f3947d591; scratchpad, not committed; `./regen_images.sh page300 4610 3` route).
Crops: `python3 tools/iiif_lines.py --image 04610-3.png --out crops --prefix 04610_p3 --region 120,1150,2350,1950
--distance 65 --prominence 20 --top-margin 12 --bottom-margin 12 --debug` -> 22 single-segment physical-line crops
(2350 px wide), covering ciphertext_4610.tsv lines p3_L12-p3_L31 (the transcription's line breaks do not match the
physical lines here: p3_L31 is two physical lines), checked on a montage.
Scope: p3 only (60 of 4610's 131 M reading tokens; p3_L12-L31 carries 49); the cap allows one page. p1/p2 handed on.
Targets: lvn10/targets.tsv (63 non-H numeral rows of p3_L12-L31: 62 M, 1 S).

Reads: two independent blind Sonnet passes (A4, B4), each transcribing every numeral of every crop in order, each
run of plain-script words written as one '|' token, never shown the earlier passes, the key or each other.
Alignment: the numeral rows of ciphertext_4610.tsv p3_L12-L31 (clear '=' rows dropped) against each pass's numeral
tokens ('|' dropped), as one page sequence, difflib (autojunk off); equal blocks and equal-length replace blocks map
1:1; anything else is unaligned ('-').

Control (known answer, can fail differently from the targets): the 230 H numeral rows of the range. Per pass,
exact-match rate. Gate: each pass >= 0.90. If either pass is below gate, no row is changed (non-test at this reader
accuracy); results logged only.

Settle rule, applied only if the gate passes:
- a non-H row is settled (confidence H, why "image300 lvn10") when A4 and B4 read the same token there, with no '?'
  mark and both aligned; the value may equal the row's sign, pass A, pass B or neither;
- if A4 and B4 differ or either is unaligned, the row stays as it is, both reads logged in alt;
- no row is inserted or deleted (segmentation gaps are logged only).
Counts reported: C/H/M/U for 4610 before and after, and the four-letter 58.3% figure recomputed.
