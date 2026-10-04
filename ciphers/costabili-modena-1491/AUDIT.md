# costabili-modena-1491 AUDIT

## Key-grade verification VER-GRACOS (account 3 verifier, 4 Oct 2026, 17:3x UTC)

Independent session (not N8-COS). Disk only, no network. No N-class assigned here: there is no running reading yet. Nothing in
`align/key_r1166p12_n8cos.tsv` changed.

**Reproduction.** `align/run_align.py` re-run on the committed `n8cos_pass{A,B}_norm.tsv` gives the same result: A 0.575 (17 pairs, shuffle
mean 0.211, p95 0.244), B 0.459 (18 pairs, 0.192, 0.219). Both clear the PREREG gate, and both per-pass keys are byte-identical to the committed
ones. The gloss-shuffle control re-pairs gloss and group, so it can change the statistic (rule 3). C means known plaintext here: the period
interlinear decipherment on R1166 (rule 4).

**Limits.** The R1166 page images were never committed. They are scratch-only, and the manifest holds only sha1s. So no crop or image
position could be checked on disk in this session. These verdicts rest on the committed blind reads only. An eye check of the group crops
waits on the next DECODE login.

**Per-sign null (new; `align/ver_gracos_persign.py`, 100 shuffles).** This measures how often a gloss shuffle meets the PREREG C rule for the
same sign and value: same value in both passes with at least 2 agreeing each.

| sign | value | A | B | per-sign null | decode-1168 (other letter, period gloss) | verdict |
|---|---|---|---|---|---|---|
| T | d | 3/3 | 3/3 | 0.00 | d C | CONFIRMED |
| c | p | 6/6 | 2/4 | 0.00 | p M | CONFIRMED (B thin) |
| g | l | 2/5 | 5/8 | 0.00 | l C | CONFIRMED |
| d | r | 8/14 | 8/10 | 0.01 | r C | CONFIRMED |
| a | i | 6/9 | 6/14 | 0.02 | i C | CONFIRMED |
| o | e | 6/11 | 4/20 | 0.02 | e M | CONFIRMED (B scatter partly from the t-sign misread as o, below) |
| z | o | 6/13 | 5/7 | 0.05 | t M | CONFIRMED for the bare-z shape only (below) |
| b | o | 9/9 | 8/13 | 0.13 | o C | CONFIRMED, by corroboration only |
| + | a | 8/11 | 6/11 | 0.16 | a C | CONFIRMED, by corroboration only |
| y | n | 10/13 | 10/16 | 0.23 | n C | CONFIRMED, by corroboration only |

- +, b and y are frequent signs mapped to frequent letters. At this N (17-18 pairs), the C rule alone is met by chance 13-23% of the time,
  so it does not separate these three from noise. Each stays C only because an independent known-plaintext witness, decode-1168's period
  gloss (f.12r, C there at 16/20, 4/7 and 7/7), gives the same value. Any future revision of decode-1168 on these signs reopens them.
- z/Z: at the gloss-t positions (p1_u02 "tradu..ta", p2_u02, p2_u09 "patri") pass A writes `z` and pass B writes `o`. At the gloss-o positions
  (p1_u03, p1_u04, p2_u05 x2, p2_u07) both passes write `z`. So the value o rests on 5 positions both readers agree on. The t-sign is a third
  shape (the convention's dash+z `Z`) that neither reader separated reliably. A transcription that does not keep z and Z apart must not use
  z = o at C. This label-collision risk is the same one N8-COS used to hold q at M.
- q held at M (N8-COS downgrade): **CONFIRMED**. The label q takes c (7/14, 7/20), u (5/14, 6/20) and, in decode-1168, e at C, so it covers
  at least two shapes.

Verdicts: 10 CONFIRMED, 0 KEEP-AS-S, 0 REJECT. key.tsv unchanged. No count or depth change: there is no running decode yet.
