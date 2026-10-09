# S2-NOTE: notation audit of the S2 look, read-free (TXE2-S2NOTE, 9 Oct 2026 22:28-22:3x UTC by date -u)

For LANE TX-ENGINEER-2 (account 4, incarnation 3). PREREG benchmark-tx/PREREG-txeng2-12.md section S2-NOTE.
**The S2 number of record stays the look as taken: passZ_S2b flagged-excluded 0.150 (75/500), as measured 0.296 (316/1068)**
(benchmark-tx/txeng2/s2score/tx_bench_S2.txt). Everything below is a notation-corrected companion reported beside it,
never a replacement. No crop was re-read; no truth, benchmark, pass, PREREG or s2score file was edited. Input hashes
re-checked against s2score/SHA256SUMS.prescore before scoring: all seven match.

## 1. The map (built and committed before any truth or error was opened)

`norm_map.tsv`, commit **4eb1753af**, sha256 `73e2f205df11a53a026c34c183394e1aa317ad83889c6538ca23471f71112af9`
(SHA256SUMS.map). Sources: sheet_SIGNS.md and committed.tsv's label inventory only.

| from | to | reason |
|---|---|---|
| s | S | committed has 0 lowercase s and S x141; the sheet's two s-forms collapse to the committed's single s-class label |
| H | # | sheet: "# the double-crossed sign like # / H / ‡"; committed H x1 beside # x107 |
| X? -> X | (36 rows, every sheet token) | sheet: "? after a token you are unsure of" |

Considered and not mapped (comment lines in the file): z vs 3 (sheet: "write z only for a flat-topped z"; committed uses
both, 3 x68 / z x12), y vs V (sheet describes two different strokes; committed y x57 / V x61), ':' (one sign on both sides,
committed x156; nothing to map, never dropped), l/L, p/P, a/@ (separate sheet tokens, both used in committed); Z, J, t, i, w
(the sheet does not say which token they are).

## 2. Classification of the errors (tools/tx_bench.py's own align(), map applied per position, classify.py)

notation = the error vanishes when the read sign and the truth set are both put through the map; segmentation = deleted
or inserted; read = a different sign, split into "agrees with the committed reference sign" (the committed reading
itself is wrong there by the truth) and "other".

| file | figure | total | notation | segmentation (del + ins) | read (= committed ref) | read (other) |
|---|---|---|---|---|---|---|
| passZ_S2b | flagged excluded | 75 | **0** | 42 (21 + 21) | 14 | 19 |
| passZ_S2b | as measured | 316 | **0** | 77 (56 + 21) | 191 | 48 |
| passA_S2 | flagged excluded | 74 | 0 | 42 (24 + 18) | 13 | 19 |
| passA_S2 | as measured | 312 | 0 | 79 (61 + 18) | 189 | 44 |
| passB_S2 | flagged excluded | 77 | 0 | 41 (21 + 20) | 13 | 23 |
| passB_S2 | as measured | 323 | 0 | 78 (58 + 20) | 182 | 63 |
| passA | flagged excluded | 24 | 0 | 8 (8 + 0) | 16 | 0 |
| passA | as measured | 248 | 0 | 17 (17 + 0) | 231 | 0 |
| passB | flagged excluded | 37 | 0 | 10 (7 + 3) | 14 | 13 |
| passB | as measured | 263 | 0 | 15 (12 + 3) | 219 | 29 |
| committed | flagged excluded | 16 | 0 | 0 | 16 | 0 |
| committed | as measured | 236 | 0 | 0 | 236 | 0 |

passZ_S2b's 19 flagged-excluded "read (other)" (truth set / ref <- read): {@|to}/@ <- {curl} x2; {P|s|z}/z <- r; {:}/: <- o,
{dot}, s; {p}/p <- y, g; {L|g}/g <- e, y; {L|g}/L <- 2; {7|m}/m <- {loop}; {3|h|k}/3 <- tz, z; {6|f|j}/f <- tz; {tz}/tz <- z;
{tz}/3 <- z; {Zu|a|oo}/a <- y; {4}/4 <- f.

## 3. Normalised figures beside the look (tx_bench_norm.txt, same arguments as tx_bench_S2.txt plus --label-map)

| file | look: flagged excl. | normalised: flagged excl. | look: as measured | normalised: as measured | paired fixed/broken look -> norm |
|---|---|---|---|---|---|
| passZ_S2b | 0.150 (75/500) | 0.154 (77/500) | 0.296 (316/1068) | 0.301 (322/1068) | 7/66 -> 3/67 |
| passA_S2 | 0.148 (74/500) | 0.152 (76/500) | 0.292 (312/1068) | 0.298 (318/1068) | 7/65 -> 3/66 |
| passB_S2 | 0.154 (77/500) | 0.158 (79/500) | 0.302 (323/1068) | 0.308 (329/1068) | 9/76 -> 5/78 |
| passA | 0.048 (24/500) | 0.048 (24/500) | 0.232 (248/1068) | 0.232 | 0/12 -> 0/12 |
| passB | 0.074 (37/500) | 0.074 (37/500) | 0.246 (263/1068) | 0.246 | 2/26 -> 2/26 |
| committed | 0.032 (16/500) | 0.032 (16/500) | 0.221 (236/1068) | 0.221 | 0/0 |

The map removes no error and moves the S2 files up by 2 flagged-excluded errors each: on passZ_S2b three positions change,
all by re-alignment (f103r_L21 pos 38 ':' and pos 39 {P|s|z} become wrong, f103r_L36 pos 37 ':' becomes right; inserted
21 -> 22, wrong 33 -> 34).

## 4. Committed labels absent from the S2 sheet (by count in committed.tsv, 2,033 signs)

t 4, Z 4, i 2, J 1, w 1, H 1 (named in the sheet only as a look of #, not a token) -- 13 signs (0.6%); plus three
committed tokenisation fragments, 'non]' 1, '{flourish' 1 + 'cross}' 1 (one sign split in two). Brace descriptors
({curl} 3, {cross} 2, {scribble} 1) are covered by the sheet's {word} rule. Reverse direction (sheet tokens unused in
committed): s (0) and r (0). The vocabulary gap is small; it does not explain the S2 baseline.

## Findings (seen after the map was committed; none applied to the map)

1. **The s -> S entry is not neutral against the truth.** The truth sets themselves carry lowercase 's' as a member
   distinct from 'S' (e.g. {P|s|z}); the readers' 81 's' reads were therefore already scored against the truth's own s,
   and merging s into S changes no error, only re-alignment. The PREREG's premise that 'S' 0 vs 141 / 's' 81 might be
   notation is answered: it is not, on scored positions.
2. **z-for-3 and y-for-V were not mapped** because the sheet distinguishes them in so many words; the S2 reads carry no
   '3' and no 'V' at all (z 54, y 60, per the look's line). Only 4 of passZ_S2b's 75 errors involve a read z on a
   3/tz truth and 3 a read y; a z->3 / y->V map was not tested and is not added here (rule: no entry after an error is
   seen). That the readers never once used '3' or 'V' though the sheet defines both is a reader-instruction defect for
   the next confirm item's brief, not a correction of this look.
3. **Segmentation is the largest single class** of the S2 flagged-excluded errors (42 of 75: 21 deleted, 21 inserted),
   against 8 and 10 for the builder's passA/passB; the S2 reads carry 1,890-1,907 signs vs the committed 2,033.
4. Every read error class "= committed ref" (14 of 75) is a position where the S2 reader agrees with the committed
   reading and the truth disagrees with both: these are scored errors of the reference stream itself, the same 16
   that make committed.tsv's own 0.032 floor.

## Hashes

| file | commit | sha256 |
|---|---|---|
| norm_map.tsv | 4eb1753af | 73e2f205df11a53a026c34c183394e1aa317ad83889c6538ca23471f71112af9 |
| tx_bench_norm.txt | (this commit) | ded2a7a4317e26b556f7825c8bf39e89553d2179db5120d4a6c9ceeeb0863d12 |
| classify.py | (this commit) | cce879cc94415fe7a067b4ac940e53515174a0764c7bf88dc8cd46b29186aae4 |
| classify_out.txt | (this commit) | 6ae2f981f27d371e2bfacd1ba6ccfcea21e1d704650df24a2e6947ee9fabda4d |

No tool change: classify.py imports tools/tx_bench.py's align/read_tsv/drop_flagged/load_label_map and changes no score.
classify.py's first version wrongly counted "read equals the committed reference sign" as notation (191/14 for passZ_S2b);
corrected before any figure was written here to "vanishes only if the mapped read is in the mapped truth set".

Openings of eval truth: 1 (the classification opening, all after commit 4eb1753af: classify.py twice over the six files,
one diagnostic of the read-other confusions and of the three re-aligned positions, and the tx_bench_norm.txt run).

Verdict: measured: notation 0, segmentation 42, read 33 (14 = committed ref, 19 other) of passZ_S2b's 75 flagged-excluded
errors (as measured 316: 0 / 77 / 239); under the read-free map passZ_S2b reads 0.154 (77/500) flagged excluded and 0.301
(322/1068) as measured, beside the look's 0.150 / 0.296, which stays the S2 number; the S2 baseline is not a notation artefact.
