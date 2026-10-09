# PREREG-B2: replication read of the TXE-B geo unit (LANE TX-ENGINEER, idea M2-rep; 9 Oct 2026, written 07:46 UTC by date -u, before any read)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-b2.md`; parent pre-registration `benchmark-tx/PREREG-txeng-2.md` (Amendment: p < 0.01).
Why: TXE-B's one read (pass H) vs pass A was fixed 12 / broken 4, p 0.0768 -- a near-miss. One more independent read on the SAME crops
either reproduces it or shows it was luck. Nothing about the crops or the task changes.

## Crops (unchanged)
- `crops/` exactly as TXE-B committed them (no diff since their first commit 11f72a4ae; manifest.json carries no sha1 field, so the
  sha1s below are recorded now and re-checked before scoring).
- The reader sees `crops2x/` (gitignored), regenerated now with the same 2x LANCZOS -> PNG step as `harvest/make_2x.py`; their sha1s
  are recorded below (TXE-B's own 2x files were not committed, so the 2x step is the same code, not a byte check against theirs).

## Reader
- ONE blind Opus 5.5 subagent call (`model: opus`), a fresh subagent, the 18 crops in one call.
- Task text: `reader_task_H2.md` = TXE-B's `reader_task.md` verbatim except the output path (`passH2_raw.tsv`). The reader opens only
  the sheet and the 18 crops; no truth file, no other pass, no decode.
- Raw read -> `passH2_raw.tsv`, committed and pushed before scoring. Normalised as TXE-B did (passage L01-L03 -> f178r_Lnn, L05/L10/L22
  -> f178v_Lnn; columns line, pos, sign = sign_id; every row kept, including X_ rows; checked: this map reproduces passH_geo.tsv from
  passH_raw.tsv exactly, 187/187 rows) -> `benchmark-tx/outputs/birago1572-no87/passH2_geo.tsv`.

## Gate (fixed now)
1. Replication alone: `tools/tx_bench.py passH2_geo.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired
   benchmark-tx/txeng/units/passA_geo.tsv`: fixed > broken.
2. Pooled over H and H2: fixed = 12 + F2, broken = 4 + B2, two-sided exact sign test, p < 0.01.
3. Reported (not gating): per-position agreement H == H2 on the scored geo positions, beside pass A/B's agreement on the same lines
   (from `benchmark-tx/txeng/units/passA_geo.tsv` and the pass B file on disk for the same lines, if any).
Adopt (`--band-extent 0.1 --mask-neighbours` -> controlled-only on the no.87 geo unit) only if (1) holds AND (2) clears. Both H and H2
also reported vs `labels_geo.tsv` (L). No eval_heldout look is spent: this is the geo unit only.
Pre-registered prediction: the L03 tail (pos 24-34, the positions A deleted) is read again, with >= 5 of 8 right as in H.

## Crop sha1s (native, then 2x read copies)
```
4b4a5e4f82c81cabd98e758e59be42ec8fac3750  crops/f178r_L01_s1.jpg
90d3e94587ceb6f699da041a6d1fb11f78423b8c  crops/f178r_L01_s2.jpg
18e303277837c72db5bce0e1dd685a259429ebfa  crops/f178r_L01_s3.jpg
9a98fdcfd6abb9af90fde9a5a08e46cc10dd099e  crops/f178r_L02_s1.jpg
76a1371aa3842dc8ba3b88874246824f9c9adb62  crops/f178r_L02_s2.jpg
a5e39ab44a342cdae2c65ae6340997c5b4ed9e9d  crops/f178r_L02_s3.jpg
d721ef055322b58cf9cb83d8a1c023f96b8460c1  crops/f178r_L03_s1.jpg
a63d6389679d23b4b08801e3aea370fd82ed08de  crops/f178r_L03_s2.jpg
8159ab1922342740b09932a3661fae808207c8cb  crops/f178r_L03_s3.jpg
68e1903c4bf5ea3a7564772cb19d2d050381b086  crops/f178v_L05_s1.jpg
0b1c114c6351643a5fd64b6ba75082e7930fa6e6  crops/f178v_L05_s2.jpg
deb4d64b00087528112a32881560bc3abb7d5789  crops/f178v_L05_s3.jpg
9bd5309f9100708def665bdfafcaa1387666613a  crops/f178v_L10_s1.jpg
241d867b391307753ffab76a1faab0ae57fee67c  crops/f178v_L10_s2.jpg
e5221eacad48b02918086ff17d5681865bb92469  crops/f178v_L10_s3.jpg
41bf2bf608a00ecc60f02bf889ddd370197916aa  crops/f178v_L22_s1.jpg
442ae73095edcbcd3a65f5828bd20767507c71dc  crops/f178v_L22_s2.jpg
007af30df881ace872b9747393ab12ce0c996dd8  crops/f178v_L22_s3.jpg
3b4af853e6a947473c19bab218385e96b0718728  crops2x/f178r_L01_s1_2x.png
aee771518bcc84e32ccf57eae0d8ce5e16631d9e  crops2x/f178r_L01_s2_2x.png
ffa77c0242501f455ae331aa50616d2cea43da82  crops2x/f178r_L01_s3_2x.png
bec480f556867567e0296c4ebd3079b3462e422d  crops2x/f178r_L02_s1_2x.png
49270a2e47a1be1c3048ff327c0b24f7cbd047cb  crops2x/f178r_L02_s2_2x.png
3b225ea4a5c40dbf698d082c370a878e79f6628f  crops2x/f178r_L02_s3_2x.png
3187a85f510f46e1313a2d98e970d2c7d9027bb8  crops2x/f178r_L03_s1_2x.png
42c2b639a6fea74ec11c524e8cd090e90817ef8b  crops2x/f178r_L03_s2_2x.png
7ab3b46fb9638fe104de3cba9d12357c014500c9  crops2x/f178r_L03_s3_2x.png
90e54acad8daa0cc35e3b8ea43b3dc8d7435e0f2  crops2x/f178v_L05_s1_2x.png
4c81c739046a5060986d66355a0f41b3d469fe50  crops2x/f178v_L05_s2_2x.png
79dd9fb208d05d1fb69d04abb4db3297996f6b92  crops2x/f178v_L05_s3_2x.png
3f0bbce1c80fedad29e30158198d27fdaaca9ac1  crops2x/f178v_L10_s1_2x.png
79f1e92f461dc9df7824c949aec4758d30375f76  crops2x/f178v_L10_s2_2x.png
6c726c3779e00c65b81b0adc55f7ddc503a3940d  crops2x/f178v_L10_s3_2x.png
e9835275b47e90848aff5b5d42364022ad21634a  crops2x/f178v_L22_s1_2x.png
f7d04cf118d4b589d62aceb8c6e01f7899be0bfb  crops2x/f178v_L22_s2_2x.png
3587c94e72aa2f14cb60a9607d9031a864d2aa80  crops2x/f178v_L22_s3_2x.png
```
