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

## Verification of W = t at C (N9-COSVW, 5 Oct 2026)

Account 2 verifier for LANE-NEAR9, 06:02-06:1x UTC by `date -u`; not the solver (N9-COS2, 0c150c16). Claim under audit: "W (dash + open loop,
own label in align/labels.tsv) = t at C (A 3/5, B 3/4, 3 groups each); A 0.614 / B 0.521 vs p95 0.260/0.233" (NOTES N9-COS2, PREREG-N9-COS2
d2fd89bd). **Verdict: CONFIRMED at C.** No grade change; `align/key_n9cos2.tsv` left as committed.

**(1) Re-run.** `python3 ciphers/costabili-modena-1491/align/run_align.py <scratch> align/n9cos2_passA_W.tsv align/n9cos2_passB_W.tsv` ->
`{"A": {"pairs": 17, "real": 0.614, "sh_mean": 0.213, "sh_p95": 0.26, "gate": true}, "B": {"pairs": 18, "real": 0.521, "sh_mean": 0.191,
"sh_p95": 0.233, "gate": true}}` -- identical to the claim. W in the real alignments: A t 3/5 (agree p1_u02, p2_u02, p2_u09; conflict p1_u21 at
"v" from the misread gloss "prevento", p2_u15 at d), B t 3/4 (agree p1_u02, p1_u20, p2_u09; conflict p1_u11 at n). (The key file's n for other
signs follows the aligner's key output, e.g. d A 8/12 there vs 8/14 rows in the alignment file; agree counts are the same.)

**(2) The 12 mechanical relabels against the image.** One DECODE browser login (06:03 UTC, `tools/decode_browser_login.js 1166 <scratch>
--guess-fullsize --max-files 2 --delay 1800`): only P1 arrived under the file cap (the thumbnail counted as a file), sha1 7ea51a6f... =
`images_manifest.tsv`; one plain-curl try for P2 returned a 17 KB placeholder (account-gated), so no second login. Scratch only, nothing
committed. P1 crops cut from `align/n8cos_boxes.tsv` (x0-60 for p1_u03/p1_u18 per `n9cos2_boxes_fix.tsv`), read by this verifier's own eye.

| crop | pos | eye: shape | gloss over it (eye) | slot in gloss |
|---|---|---|---|---|
| p1_u02 | 0 | dash + open loop (left edge clipped) | tradu(c)ta | t |
| p1_u07 | 1 | dash + open loop | tuti | t (2nd t of "tuti") |
| p1_u07 | 5 | dash + open loop | termini | t |
| p1_u11 | 1 | dash + open loop | "ob no era primo" (gloss not over the group's start) | ambiguous |
| p1_u12 | 2 | dash + open loop | satiffacto (= satisfacto) | t (s a t i s f a) |
| p1_u15 | 6 | dash + open loop | facto | t (f a c t o) |
| p1_u19 | 4 | dash + open loop | nanti | t (n a n t i) |
| p1_u20 | 2 | dash + open loop | ritrouar | t (r i t r o) |
| p1_u21 | 3 | dash + open loop | partito (both passes misread the gloss) | t (p a r t i t o) |
| p2_u02 | 0 | not re-seen (P2 not fetched); N9-COSV eye-checked it as this shape | tradutta | t |
| p2_u09 | 2 | not re-seen; N9-COSV eye-checked it as this shape | patria | t |
| p2_u15 | 7 | not re-seen by this verifier or by N9-COSV | padre | d (contrary) |

All 9 P1 relabels are the dash + open-loop shape, distinct from the zigzag z and the small dash+o (o = e) in the same crops (p1_u03 "Le nocie":
g o y z q a o; p1_u19 "...re-": d o). No relabel is a different sign. Under-count confirmed on the image: p1_u21 position 5 (A z, B o) is the
same shape at the second t of "partito", missed by the rule because difflib aligned the two rows off by one there; p1_u07's clipped first sign
may be one more (initial t of "tuti"), not visible in the crop.

**(3) W groups with the gloss chunk.** Aligner-counted agreeing groups: tradu- (p1_u02), tradutta (p2_u02), patria (p2_u09), ritrovar (p1_u20) --
three distinct words, the W sign at a slot the C values around it fix (W d + T = t r a d; c + W d a = p a t r i; d a W d b = r i t r o). Eye-only
(pairs lost to the 0.8-1.25 ratio filter or a gloss misread, not counted in the grade): termini, tuti, satisfacto, facto, nanti, partito (x2).
So the gloss fixes t unambiguously on >= 2 independent groups (the brief's test) and the prereg C rule is met in both passes. Against: one
token, p2_u15 under "padre" at the d slot, image unchecked (the sign may be misread, or the writer spelled "patre"); p1_u11 is not placeable.
11 of 12 placeable W tokens (with the extra p1_u21 one) stand at t. Outside corroboration: decode-1168's `~` = t (C).

**(4) The p1_u03/p1_u18 re-cut.** Diff of `n8cos_pass{A,B}_norm.tsv` -> `n9cos2_pass{A,B}_W.tsv`: the only non-W edits are the first token of
p1_u03 (A, B) and p1_u18 (A; B already read g), d -> g. Both widened crops read g o y z/b q a o under "Le nocie": g = l at the head, consistent.
Re-scoring with the W relabel but without the re-cut gives A 0.598 / p95 0.236, B 0.514 / 0.233; per-sign majority values identical with and
without the re-cut for every sign; only d (A 8/16 -> 8/14, B 8/10 -> 8/9, the l-conflicts removed) and g (A l 2/5 -> 4/7, B 5/8 -> 6/9) counts
move. No other sign's value moved.

Requests: de-crypt.org 1 browser login + 1 image (1.8 s apart), 1 plain curl (placeholder). Subagent calls: 0. Cost: see the lane ledger.
Suggestion (not run): eye-check p2_u15 at the next DECODE login (W at "padre"'s d), and relabel p1_u21 pos 5 as W in any re-pass.

## AUDIT 1 (VER1-COS, 5 Oct 2026)

Novelty audit (rule 10) by an account 2 verifier for LANE-VER1, 18:17-18:4x UTC by `date -u`. This session is not N8-COS, N9-COS2,
VER-GRACOS, N9-COSV or N9-COSVW, and it does not decode. No earlier section of this file assigns an N-class, so this is Audit 1.
**Claim under audit:** "R1166 P1-P2 key: 11 sign values at C" (NOTES "Remaining gaps"; N8-COS 10 values, W = t added by N9-COS2;
key-grade checks VER-GRACOS 4 Oct and N9-COSV / N9-COSVW 5 Oct). On disk, `align/key_n9cos2.tsv` gives 11 C (+ a, T d, a i, b o, c p,
d r, g l, o e, y n, z o, W t) and 7 M. That matches the claim.
**decode-1168-modena-costabili-1492 is not the same reading.** It is a different letter (b.2/21 no.8, 20 Mar 1492, R1168), already
`found-solved`: Berzeviczy 1914 no. CLV prints it in clear. Here it appears only as a key witness and is not audited.

### 1. Item extracted from the repository

| field | value |
|---|---|
| item | DECODE R1166 = ASMo, Amb. Ung. b.2/20 no.16 = Vestigia 2977 = MNL DL-DF 295935 (same photograph, N8-COS) |
| date, place | 21 Jun 1491 (archive date card "1491 ev 06 ho 21 nap"), Esztergom |
| sender, recipient | Beltrame Costabili to Eleonora d'Aragona, Duchess of Ferrara |
| cipher | graphic-sign substitution, dash lead-in strokes; P1 ~35 lines ~50% cipher, P2 ~20 lines ~40%, P4 ~10 lines ~50% (COS-M; ~1,140 signs, measured-estimate) |
| what was read | no running decode. Only the sign-to-letter key, aligned to the **period interlinear decipherment written over the cipher groups on P1-P2** (grade C = known plaintext from that gloss) |
| gloss phrases (eye-read) | "a la traductione", "Lo Re de Hungaria", "tuti Li termini sono [passati]", "Le nocie", "conveneria", "nanti la recu[peratione]", "cum pegiore satisfactione", "suo padre", "patria" |
| solver searches (from NOTES) | CS-4: Berzeviczy 1914 whole volume (no 1491 Costabili letter printed). RUN3-COST: IA advancedsearch 10, be-api 17 (Ulaszlo series, Szazadok/Fraknoi, clear-slip phrases), Vestigia 2949-3008 (catalogue records only, no transcription). Earlier: decode-1162/1168 web, blog and Tomokiyo checks |

### 2. Independent search (5 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical series | Berzeviczy, *Acta vitam Beatricis* (MHH Dipl. 39, 1914; IA `aragoniaibeatrix00berz`, `monumentahungari0039unse`, `beatrixkirlyn14500berz`) via `tools/print_check.py` listed sources, 9 phrases | no hit for any gloss phrase. CS-4's whole-volume read stands: no 1491 Costabili letter is printed there |
| (b) sender/recipient correspondence | Magyar diplomacziai emlekek Matyas kiraly korabol (ends 1490: out of range); Szazadok 50 (Fraknoi, `szzadok50trgoog`) as a listed source | no gloss phrase found. Láng 2018 (below) cites MDE III pp. 13-17, 90-91, 166-168 for Beatrix-Eleonora cipher letters of 1482-86, not 1491. MDE III was not read page by page |
| (c) documentary editions / archive inventories | Google Books API for the ASMo Cancelleria "Cifrario" series. "Cifre con Ambasciatori e Agenti estensi all'estero, Sec. XV" is listed in *Atti e memorie* (Deputazione di storia patria, Modena) 1924 (`TNMNAQAAIAAJ`) and 1927 (`cuqWamxfE00C`), snippet only. Ilardi, *Studies in the Renaissance* 9 (1962) (IA `studiesinrenaiss0009vari`) gives "Cifre con Ambasciatori e Agenti Estensi all'Estero, B. 4 (XV century)" | **lead, not examined:** ASMo holds a 15th-century series of Este embassy cipher tables. A period key sheet for Costabili's cipher may survive there. No printed copy of one was found. "Dispacci degli ambasciatori estensi" as a printed series for Hungary 1491 was not located |
| (d) holding archive / project pages | DECODE RecordsView/1166, login-free, 1 request: Status "Partially decrypted", **Available Documents empty**, no key fields. Aymeloglu `catalogue/decode-catalog.csv`: no DECODE key record for Costabili / Modena / Ferrara. Vestigia 2977 (N8-COS, RUN3-COST): catalogue incipit/explicit and images, no transcription | no transcription or key attached to the record; no DECODE key record |
| (e) IA / HathiTrust / Google Books full text | `print_check.py`: 9 gloss and clear-text phrases x ia-global, gbooks, 4 listed IA items, openalex, crossref (79 rows). Plus 8 be-api queries ("Beltrame Costabili" cifra; Costabili zifra; Costabili "in cifra" Ungheria; ambasciatori estensi cifra Ungheria; cifrari estensi; "Cifre con Ambasciatori"; Costabili 1491 inside `oapen-20.500.12657-53633`). Plus 5 Google Books queries (Costabili cifrario; Costabili rejtjel; "Beltrame Costabili" 1491 Strigonio; the Cifrario series title; Costabili cifra Eleonora Esztergom) | no verbatim hit for any phrase. Google Books "hits" are keyword matches in unrelated volumes (Li reali di Francia, Sanuto, Documenti di storia italiana 1836); none prints a 1491 Costabili text. be-api hits for Costabili + cifra/zifra are Berzeviczy's 1482-90 queen's-cipher passages, Lucrezia Borgia (Antonio Costabili, 1503) and Ariosto's letters: none is this letter. ia-global was not searched for 2 phrases (be-api HTTP 502) |
| (f) solver repositories, cipher blogs | dbourdeau/cyphersolver (clone of 3 Oct 2026, grep): CANDIDATES.md B2 lists the Costabili records as "Valentini and Costabili not checked"; `targets/buda1489/vestigia/search_rows.json` has catalogue rows only; no key or decode. aaymeloglu/unsolved-ciphers (27 Sept 2026): catalogue rows only. Tomokiyo (`sources/cryptiana/`), Cipherbrain, Cipher Mysteries: none (decode-1168/CS-4 logs, not re-run) | no decipherment, key or working file for R1166 |
| (g) scholarship | OpenAlex (Bearer key; 11 calls by print_check + 6 here): "Costabili Ferrara Hungary 1491", "Este ambassadors Hungary cipher", "Ferrara Hungary ambassadors cipher 1491", "Beatrice of Aragon Hungary cipher letters Este", "titkosiras Matyas kiraly Ferrara", "Lang Benedek cipher Hungary". CrossRef 3. HAL: "Costabili" 0, "Beatrice d'Aragona" cifra 0. Persée: "Costabili" 283 and "Costabili Ungheria" 966, first pages about art and horses, none on this cipher | **Láng, *Real Life Cryptology* (AUP 2018, open access, IA `oapen-20.500.12657-28452`, full text read by grep).** p.137 and p.156: Beatrix and Eleonora "used a simple monoalphabetic cipher with graphic signs"; the Modena letters include "the one in which Beatrix is sending Eleanor the code key". Appendix 10.2 (p.192): "50 letters related to Hungarian history in the Modena State Archives (Vestigia), 1482-1519, Beatrix, Eleonora, Ippolito d'Este and others, Latin and Italian, solved: y and n". Appendix 10.1 (cipher tables): no Ferrara-Hungary graphic-sign table. Costabili is not named. Pastrnak 2025 (*En la España Medieval*, Pecchinoli 1488-90): abstract has no cipher content. Vértesy, "Titkos írás egy Corvinában", *Magyar Könyvszemle* 77 (1961) 167-169 (a 1491 Beatrix note in a Corvina, mono graphic signs, solved per Láng): **unreachable** (epa.oszk.hu HTTP 403, not retried) |
| Semantic Scholar | print_check s2 | **unreachable**: HTTP 429 on the first call, stopped (good-citizen rule) |
| JSTOR | 3 rows appended to `JSTOR-QUEUE.tsv`: family (i) names + date + cipher keyword; family (ii) two bare quoted gloss phrases | queued; does not block the class |

Requests this session: archive.org 7, be-api.us.archive.org 20 (2 HTTP 502), www.googleapis.com 19, api.openalex.org 19, api.crossref.org 3,
api.semanticscholar.org 1 (429), de-crypt.org 1, api.archives-ouvertes.fr 2, www.persee.fr 2, epa.oszk.hu 1 (403), real-j.mtak.hu 1 (404),
www.degruyter.com 2 (202 challenge, 0 bytes), github clone 2. No subagent calls.

### 3. Classification

| item | class | key | text | prior plaintext | prior decipherment | confidence |
|---|---|---|---|---|---|---|
| R1166 P1-P2 (b.2/20 no.16, 21 Jun 1491): sign key, 11 values C / 7 M, rebuilt from the leaf's interlinear decipherment | **N0** | `period` (rebuilt by us from the period interlinear decipherment on the same leaf) | known (on the leaf, as a period decipherment; not found in print) | yes: the period decipherer's interlinear gloss on P1-P2 (1491) | yes: the same gloss is the decipherment of these passages | high |

- Why N0 and not higher. The plaintext and its decipherment are on the item itself, as in the decode-1162 (R1162, N0), Clairambault 1067
  and RAH Canada precedents. Our work maps the period decipherment back onto the signs. It reads no passage that the period decipherer had
  not already read.
- Mapping. No printed or published sign-value table for this cipher was found: none in Láng 2018's table list, none on DECODE, none in
  either solver repository. Two things are **not excluded**: (1) a period key sheet in ASMo Cancelleria, Cifrario ("Cifre con
  Ambasciatori e Agenti estensi all'estero, sec. XV", B.4); (2) the key Beatrix sent Eleonora (Láng p.156; MDE III). Whether Costabili's
  cipher is the queen's cipher is not established. Vértesy 1961 may print a sign table of a related 1491 Beatrix cipher and was not
  reached. None of this changes the class, which rests on the plaintext.
- The ~100 unglossed signs of R1166 P4 are not part of this item. Nothing has read them. If a later decode reads them, that is a separate
  item for a separate audit.

### 3a. Depth (rule 4a)

| item | % cipher tokens H/C/S in a running reading | unread | depth | check |
|---|---|---|---|---|
| R1166 | 0% (no running decode; 0 of ~1,140 measured-estimate signs read by us as text) | all | **D0** | key-only: 11 sign values C from gloss alignment (N8-COS/N9-COS2 passes, re-verified VER-GRACOS, N9-COSV, N9-COSVW). No clause or sentence is read by us from the cipher, so no D2 content sentence is written |

Outward words: none ("a key ranks first; nothing reads"). D0 here means no running reading exists. It is not a judgment on the 11 C
values, which the earlier verifier sections confirm.

**Safe sentence:** "Costabili's cipher report to Eleonora d'Aragona of 21 June 1491 (ASMo, Amb. Ung. b.2/20 no.16; DECODE R1166)
carries a period interlinear decipherment on the leaf. Aligning it with the cipher groups gives 11 sign values at grade C. This is a key
rebuilt from the period decipherment (N0, key period, text known on the leaf); nothing beyond what the period decipherer read has been
read."
**Unsafe sentence:** "We deciphered Costabili's 1491 letter" / "the first key of the Ferrara-Hungary cipher" / "previously unread
passages". The plaintext is on the leaf; a period key sheet in ASMo is not excluded; and no running reading exists.

### 4. Postmortem

No over-claim found in this folder. NOTES.md calls the result a "key rebuild from the period decipherments, not cryptanalysis" (COS-M)
and says "Read so far: 0 of ~5,060". The earlier verifier sections assign no class. One wording to watch: NOTES' Premise check (c) says
a gloss means "found-solved for that leaf". That is correct for the plaintext, and it means any outward note must keep this item at N0.
The open lead goes into the folder's next steps as a suggestion, not run: ASMo Cifrario B.4 (sec. XV) and MDE III pp. 13-17 for a period
Ferrara-Hungary key sheet. Finding one would give an H-grade witness for the 7 M values.
SECOND-OPINIONS-QUEUE.tsv: no row (N0, below N3). Search phrases and sources: `phrases.txt`, `sources.tsv`; results `print-check.tsv`,
`print-check-hosts.tsv`.

depth_check (VER1-COS, 5 Oct 2026, exit 0; this item is D0, not counted, so it is not listed by name):
```
unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 12; legacy ungraded: 0
```

## AUDIT 2 (DEF1-GRACOS, 5 Oct 2026)

Verifier DEF1-GRACOS (account 1, for LANE DEFAULT-account-1-20261005-2039), 20:47-21:1x UTC by `date -u`. Not N8-COS, N9-COS2,
VER-GRACOS, N9-COSV, N9-COSVW or VER1-COS. Brief `.claude/briefs/runs/2026-10-05-account1-default-2039-jobs.md`, DEF1-GRACOS.
Nothing decoded. Task: try to break Audit 1's N0 / D0 / key period, and log the families searched.
**Revision check:** no NOTES.md section dated after Audit 1 (18:4x UTC); `align/key_n9cos2.tsv` unchanged (11 C, 7 M). No
SECOND-OPINIONS-QUEUE.tsv row exists. Nothing to carry forward.

### Result: N0, key period, D0 endorsed; one lead sharpened

1. **Berzeviczy 1914 does not print this letter.** Read from the volume's own table of contents (IA `aragoniaibeatrix00berz`,
   `_djvu.txt` fetched once; OCR lines 1271-1393). Every 1491 item, CXXVII-CL, is listed. The June 1491 items are CXXXIV (13 June,
   Beatrix to Eleonora), CXXXV (17 June, unsigned, Pavia), CXXXVI (20 June, Ippolito to his father) and CXXXVII (24 June, Beatrix to
   the Duke). None is a Costabili report of 21 June. The Costabili reports printed are XCIV (Antonio, 1489), CLV (20/22 Mar 1492 =
   R1168, already `found-solved`), CLXII (3 May 1492), CLXXXVIII, CXCV (1493), CCXCII (1502) and appendix IX (16 Jul 1490). This
   confirms CS-4's whole-volume read.
2. **Lead sharpened, not resolved: the period key was sent to Ferrara eight days earlier.** Berzeviczy **CXXXIV**, Beatrix to Eleonora,
   Esztergom, 13 June 1491 (ASMo Canc. Duc., Cart. di Princ. Est., B.a 2, Ungheria; printed pp.190-191). The editor's summary reads
   "új titkos jegyeket küld" ("sends new secret signs for their correspondence"). The text says: "io ho una cifra con la S. V. antiqua
   ... per essere cifra multo vechia ... pertanto mando una copia d'essa ... et con questa scriverimo quando será bisogno". The same
   letter names "el dicto Messer Beltramo [Costabili] scrive al presente" and says she has charged him "che scriva de omne cosa
   copiosamente". Berzeviczy prints the letter, **not the cipher copy** (no sign table in the item, none in the volume's contents). So
   a period key sheet for the queen's cipher went to Eleonora in June 1491, and Costabili was writing to her in the same week. Whether
   R1166 uses that cipher is **not established**. If the copy survives in ASMo (Audit 1's Cifrario B.4 lead; Láng 2018 p.156, "the one
   in which Beatrix is sending Eleanor the code key"), it would be an H-grade witness for the 7 M values. This is a suggestion for the
   folder's next steps, not run. It does not change the class, which rests on the plaintext glossed on the leaf.
3. **Nothing found that prints the R1166 plaintext or a sign table for it.** See the log below. *Nel segno del corvo* (Modena exhibition
   catalogue, 2002) mentions in a note that a Costabili letter "è inserita tra quelle di Beatrice" (ASMo, Cancelleria ducale). Google
   Books gives only that snippet. No query (`cifra`, `zifra`, `Strigonio giugno`) surfaced a transcription of a 21 June 1491 letter, and
   the catalogue was not reached in full. Logged as not excluded.

| item | class | key | text | depth | % H/C/S | check |
|---|---|---|---|---|---|---|
| R1166 P1-P2 sign key (11 C / 7 M) | **N0** (endorsed) | `period` (rebuilt by us from the leaf's period interlinear decipherment) | known (on the leaf; not found in print) | **D0** (endorsed) | 0% running text (0 of ~1,140 measured-estimate signs) | key-only: gloss alignment; no clause read by us, so no D2 sentence |

**Safe sentence** (Audit 1's, unchanged): "Costabili's cipher report to Eleonora d'Aragona of 21 June 1491 (ASMo, Amb. Ung. b.2/20 no.16;
DECODE R1166) carries a period interlinear decipherment on the leaf. Aligning it with the cipher groups gives 11 sign values at grade C.
This is a key rebuilt from the period decipherment (N0, key period, text known on the leaf); nothing beyond what the period decipherer read
has been read."
**Unsafe:** "we deciphered Costabili's letter", "the first key of the Ferrara-Hungary cipher", "the key Beatrix sent in June 1491" (the
identity of R1166's cipher with the queen's June 1491 copy is unproven), "previously unread", "printed by Berzeviczy" (it is not).

### Search log (5 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical series | Berzeviczy 1914, `aragoniaibeatrix00berz`: be-api fts "Costabili" 1, "Beltrame" 1, "Strigonii" 1; full TOC read from `_djvu.txt`; CXXXIV text read | not printed (point 1); CXXXIV key-copy letter (point 2) |
| (b) Nyáry | Nyáry Albert, "A modenai kir. levéltár magyar történelmi szempontból", *Századok* 1868: located by bibliography (Google Books snippets: *Magyar könyvészet* 1885, *Századok* 1868, *Párhuzamok* 2000); IA advancedsearch for Századok 1868 0 items | **unreachable** in full text; it is an archive survey from 1868, and Berzeviczy 1914 supersedes it as the edition. Not read |
| (c) Dispacci estensi | Google Books `"dispacci" estensi Ungheria Costabili` 1 (*Savonarola da Ferrara all'Europa* 2001, unrelated); no printed "Dispacci degli ambasciatori estensi" series for Hungary 1491 located (as Audit 1) | none |
| (e) Google Books API | `"Beltramo Costabili" 1491 cifra` 0; `"Costabili" "Strigonio" 1491 Eleonora` 1 (*Nel segno del corvo* 2002, point 3); `"tuti li termini sono passati"` 346, top 6 unrelated (keyword matches: Sanuto, 1611/1628 tracts); `"Nel segno del corvo" Costabili` x3 variants 0/1/1 snippets only; `Costabili 1491 "in cifra" Beatrice Eleonora` 0 | no transcription |
| (g) scholarship | OpenAlex (Bearer) "Beltramo Costabili Esztergom" 0, "Beatrice of Aragon Eleonora cipher Modena" 0; Semantic Scholar 1 (HTTP 429, stopped); CrossRef "Beltramo Costabili Hungary" (top 5 unrelated); CORE `"Costabili" Ungheria cifra 1491` (top 5 unrelated); HAL "Costabili Ungheria" 0 | nothing on this cipher |
| (f) solver repositories | aaymeloglu/unsolved-ciphers HEAD d2800bb (shallow clone, grep "costabili"/"1166"): DECODE catalogue rows R1162-R1168, R1095-R1097 only (the "1166" hit in starhemberg-1758 is a number, not this record); dbourdeau/cyphersolver HEAD a439937, unchanged since Audit 1's grep | no reading or key |
| JSTOR | 2 rows appended: (i) Beatrix/Beatrice + Eleonora + 1491 + cipher keyword; (ii) bare phrase "una cifra con la S. V. antiqua" | queued; Audit 1's 3 rows still queued; neither blocks the class |
| not searched | Vértesy 1961 (Audit 1: epa.oszk.hu 403; not retried, good-citizen rule); MDE III page by page (out of date range per Láng's citations) | |

Requests this session for this item: archive.org 3 (advancedsearch 2, `_djvu.txt` 1), be-api.us.archive.org 3, www.googleapis.com 9,
api.openalex.org 2, api.semanticscholar.org 1 (429), api.crossref.org 1, api.core.ac.uk 1, api.archives-ouvertes.fr 1; github shared with
the fr2980-gramont audit. All >= 1.5 s apart.

### Postmortem

No over-claim found: the registers say "key rebuilt from the period decipherment, not a reading". One suggestion goes into the next steps
(not run): look in ASMo for the cipher copy Beatrix sent with Berzeviczy CXXXIV (13 June 1491) and compare its signs with key_n9cos2.tsv.
status.json results[115] and the PROGRESS.tsv R1166 row are updated (two audits). No SECOND-OPINIONS row (N0).

depth_check (DEF1-GRACOS, 05 Oct 2026 21:00 UTC, exit 0, 0 FAIL; both items N0, not counted, so not listed by name):
```
unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 13; legacy ungraded: 0
```
