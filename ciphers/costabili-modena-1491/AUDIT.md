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

## Verification of the N8-COS C values (N9-COSV, 5 Oct 2026)

Independent verifier session (account 2 worker for LANE-NEAR9; not N8-COS, not VER-GRACOS), 05:18-05:2x UTC by `date -u`. Claim under audit:
"R1166 P1-P2 key: 10 sign values at C (N8-COS)". No reading claimed, no novelty class (there is no running decode).

**(1) Reproduction.** `python3 ciphers/costabili-modena-1491/align/run_align.py <scratch> align/n8cos_passA_norm.tsv align/n8cos_passB_norm.tsv`
-> `{"A": {"pairs": 17, "real": 0.575, "sh_mean": 0.211, "sh_p95": 0.244, "gate": true}, "B": {"pairs": 18, "real": 0.459, "sh_mean": 0.192,
"sh_p95": 0.219, "gate": true}}`. Both keys and both alignment files byte-identical to the committed `n8cos_key_pass{A,B}.tsv` /
`n8cos_align_pass{A,B}.tsv`. No drift.

**(2) Per-group support.** `align/n9cosv_pergroup.py` -> `align/n9cosv_pergroup.tsv` (every group where each value's sign is aligned, with both
passes' gloss read, sign read and aligned chunk). Then one DECODE browser login (05:20 UTC, `tools/decode_browser_login.js 1166 <scratch> --fetch
<P1,P2 absolute filesrv URLs> --max-files 2 --delay 1800`), P1/P2 sha1 = `images_manifest.tsv` (7ea51a6f..., 2560751b...), scratch only, nothing
committed; crops re-cut with the committed cutter (`cd <scratch>; python3 .../align/n8cos_cut.py` -> 32 crops, `n8cos_boxes.tsv` byte-identical to
the committed one), and this verifier eye-checked 20 of the 32 crops plus wider page views for p1_u03/p1_u04/p1_u18 (sign shape under the gloss
letter, gloss letter itself). Groups = distinct crops; "both" = the value aligned in that group in both blind passes.

| sign | value | groups A / B / both | both-pass groups | eye check (gloss letter over the sign, this session) | verdict |
|---|---|---|---|---|---|
| + | a | 7 / 5 / 5 | p1_u02, p2_u04, p2_u07, p2_u09, p2_u13 | tradu-, dal, patrio | CONFIRMED C |
| T | d | 3 / 3 / 2 | p1_u02, p2_u04 (+ p1_u16 B only, p2_u02 A only) | tradu-, dal: T under d, both passes read T | CONFIRMED C (thin: 4 groups, 2 in both) |
| a | i | 5 / 5 / 4 | p1_u03, p1_u05, p2_u07, p2_u09 | nocie, patrio | CONFIRMED C |
| b | o | 8 / 8 / 6 | p1_u04, p1_u05, p1_u13, p1_u17, p1_u18, p2_u05 | non, honore, nocie (p1_u18) | CONFIRMED C |
| c | p | 6 / 2 / 2 | p2_u07, p2_u09 | Compagnie, patrio, padre, por/per, p1_u21: c under p in 5 groups; B reads c there too, its pairs were lost to the 0.8-1.25 ratio filter or a gloss misread, not to a different sign read | CONFIRMED C |
| d | r | 8 / 7 / 5 | p1_u02, p1_u04, p1_u05, p2_u05, p2_u09 | honore, patrio, Loro, padre | CONFIRMED C (see crop error below) |
| g | l | 2 / 5 / 2 | p2_u04, p2_u05 | dal, Loro, and p1_u03/p1_u18 "Le" (below) | CONFIRMED C |
| o | e | 5 / 3 / 1 | p1_u03 (x2) | nocie (x2), honore (gloss is "honore", A misread "honorv"), p1_u18 "Le", padre, per/por: plain dash+o under e in 5 groups | CONFIRMED C, conditional on the Ω split below |
| y | n | 9 / 9 / 8 | p1_u03, p1_u04, p1_u13, p1_u17, p1_u18, p2_u05, p2_u07, p2_u16 | non (y b y), honore, nocie | CONFIRMED C |
| z | o | 4 / 4 / 4 | p1_u03, p1_u04, p2_u05, p2_u07 | zigzag z under o in all four (nocie, honore, Loro x2, Compagnie) | CONFIRMED C for the zigzag shape only (below) |

Findings the committed tables could not show:
- **N8-COS crop error, p1_u03 and p1_u18.** The box's left edge cuts the first sign; on the full page it is the g shape (bowl with a long looped
  descender, as in p2_u04 "dal" and p2_u05 "Loro"), under gloss "Le". The readers saw only the bowl and wrote d (both passes p1_u03, pass A p1_u18),
  which is the whole of the apparent d = l conflict. It is a box error, not a d/l homophone: d = r stands, and g = l gains two eye-checked groups.
- **A third shape, Ω (lead dash + open loop), behind every z/o split.** Every A-z / B-o disagreement, in the nine crops eye-checked for it (p1_u02, p1_u07, p1_u11,
  p1_u12, p1_u15, p1_u19, p1_u20, p2_u02, p2_u09), is this one shape, not the zigzag z and not the small o. Under a legible gloss it stands at t
  (tradu-, ritrou-, tradutta x2, patrio); once (p2_u15 "padre") at d. The label convention (z, dash+z `Z`, o) has no slot for it, so pass A filed it
  under z and pass B under o; that is the source of A's z scatter (6/13) and B's o scatter (4/20), and of VER-GRACOS's "t-sign" note. It matches
  decode-1168's `~` = t (C) and probably its z = t (M) as the same collision there. This verifier records the shape and the gloss letters only; no
  key row is written for it (not a decode job).
- So z = o and o = e are C on their own shapes (zigzag z; small dash+o), and a transcription that does not keep Ω apart from both must not apply
  either at C. This is a condition on use, not a lowering: on the shapes themselves the gloss fixes the value in 4 and 5 groups.

**(3) decode-1168 key as a witness.** `ciphers/decode-1168-modena-costabili-1492/key.tsv` is built from a different letter (b.2/21 no.8, 20 Mar
1492), different images (R1168 f.12r, 2592x3888 DECODE scans) and that letter's own period interlinear gloss: an independent known-plaintext
witness of the key, not derived from the R1166 images. It is not independent in instrument: same project, same blind-pass + `interlinear_align.py`
method, and the N8-COS readers were given the decode-1168 sign label list, so a label collision (q; Ω filed as z or o) is shared, not
cross-checked. "9 agree / z differs" holds by value; at C on both sides it is 7 (+, T, a, b, d, g, y): c = p and o = e are M in decode-1168, and
its z = t is most likely the Ω shape. VER-GRACOS kept +, b, y at C "by corroboration only" from decode-1168; this session adds direct eye checks of
the gloss over each (3 or more groups each), so they no longer rest on that corroboration alone.

**(4) Verdicts.** 10 CONFIRMED C (z and o conditional on keeping Ω apart), 0 LOWERED. `align/key_r1166p12_n8cos.tsv` grades unchanged; its z and
o notes now name the Ω condition. Requests: de-crypt.org 1 login + 2 image fetches (1.8 s apart). Subagent calls: 0. Cost: see the lane ledger.
Suggested next step (not run): a group-crop re-pass with Ω as its own label and the p1_u03/p1_u18 boxes widened to the left, before any P4 decode.
