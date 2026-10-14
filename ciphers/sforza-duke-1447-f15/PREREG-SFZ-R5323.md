# PREREG SFZ-R5323 (14 Oct 2026, 19:2x UTC by date -u; account 1, LANE DEFAULT-A1-1840-14) -- pushed before any score

Question: is DECODE scat. 1597 no. 23 (R5323, later fair copy headed "Filippo Maria Duca di Milano") the key of the Duke's slips
italien 1584 f.5/f.8? SFZ-DEC2's 5/7 was one reader who knew the pairs (grade M). This test uses readers who never see them.

Known answers (grade C, ../sforza-italien1584-1447/duke/key.tsv): O=a, Y=o, N8=d, N2=h, N11=r, ce=r, cu=n (7 pairs; labels as
duke_labels.md, which gives shapes only, no values).

Readers: Sonnet subagents given duke_labels.md's label/shape table (no values, no key.tsv, no f.5/f.8 image, no mention of the
Duke's slips or of which labels matter). Task: for each plaintext-letter column of a key sheet, list the cipher signs under it, each
as a duke_labels.md label, or X:<description> if no label fits.
- R5323: two independent blind passes (A, B) on two strip crops of the alphabet block (300 dpi, left a-m, right n-z), all columns.
- Control keys (one blind pass each, same instructions, top half of the sheet at 150 dpi): R5324 (the other "Filipo Maria" sheet) and
  ten other scat. 1597 keys: R5302 R5304 R5305 R5306 R5309 R5310 R5311 R5312 R5313 R5315.

Statistic S(key) = number of the 7 pairs whose label the reader lists in that letter's column (0-7). For R5323 the reported score is
S on the cells both passes agree on (a pair counts only if both A and B list it); S_A and S_B are reported beside it.

Nulls:
1. Other keys: S on each of the 11 control sheets (can differ from R5323: different sheets, different signs).
2. Shuffled-value null: permute the plaintext letters over R5323's agreed columns (10,000 permutations, seed 5323), recompute S; p = share
   of permutations with S >= observed.

Gate (PASS needs all three): S_agreed(R5323) >= 4; S_agreed(R5323) > max S over the 11 control sheets; shuffled p <= 0.01.
On PASS (time permitting, else the named next step): key_r5323.tsv from agreed cells only (grade H only for agreed cells), applied to
f.5/f.8 with decode_key.py against their glosses before f.15. On FAIL: logged, R5323 stays an M-grade lead; no re-tuning of this gate.
Script: score_r5323.py (in this folder). Images and crops stay untracked (regen commands in NOTES "## SFZ-R5323").
