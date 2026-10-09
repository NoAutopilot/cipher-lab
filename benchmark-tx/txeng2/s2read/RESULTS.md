# TXE2-S2READ: the frozen S2 pipeline's reads on vivonne1573-f103r-confirm2, steps 1-4 (no score)

LANE TX-ENGINEER-2 (account 4, incarnation 2), Opus 5.5 worker; 9 Oct 2026, 21:3x-21:5x UTC by date -u. Binding: PREREG-txeng2-S2.md
"FROZEN" (steps 1-4 exactly, step 5 empty) and PREREG-txeng2-9.md S2-READ; brief .claude/briefs/runs/2026-10-09-account4-txe2-round9.md.

**No score was run; the lane's single look follows TXV-VIV.** Openings of eval truth: 0. Not opened: the truth TSV, the builder's
committed/passA/passB.tsv, any decode, alignment or clerk decipherment of f.103r, key values. Disclosure: I listed the file names
in ciphers/fr16104-vivonne-spain-1572/tx/ (names only) while looking for the sign list, and opened exactly one file there,
tx/SIGNS.md (the N5-VIVK readers' sign inventory: shape descriptions only, no values; read in full and judged value-blind),
copied verbatim to `sheet_SIGNS.md`. The folder's NOTES.md was grepped for "SIGNS.md / reader brief / DUP" lines only.
Hosts: 0 requests.

## Step 1: crops and overlap (crops checked, never re-cut)
- Crops: the folder's committed `images/c106_f103r_L01..L37_s{1,2}.jpg` (N5-VIVK, --follow-slope 400), 1600 px wide, scale 1.0.
- Overlap measured per line by `tools/overlap_audit.pixel_overlap` (O1's NCC method; `overlap_measure.py`, table `overlap.tsv`):
  **150 px on all 37 lines, NCC 0.998-0.999, equal to the manifest boxes (150 native px)**. Sign width 43 px (iiif_lines.ink_run_width,
  median over the 74 crops). Brief sentence written by `iiif_lines.overlap_sentence` (`overlap_note.md`), not typed.
- Overlay (`overlay/ov0-3.jpg`, s1+s2 stitched at the measured overlap, seam dashed blue): seamless on every line; **no sign cut
  at the s1/s2 seam**. Notes: L26 and L27 are the same written line (a DUP band, as BENCHMARK-TX says; both passes wrote DUP);
  L01 opens with plain words; the last sign of L23 and of L37 touches the crop's right edge (page edge, possibly clipped; noted,
  not re-cut); neighbouring-line ascenders/descenders intrude at the top/bottom edges of most crops.
- Brief (`reader_task.txt`, "do not resize") + sheet committed with sha256 in 339d561ef before any read.

| file | sha256 | commit |
|---|---|---|
| reader_task.txt | a0f706649ee29b41d4429484b600c704e48fe83bd4c393a91c3b32ca9664bbca | 339d561ef |
| sheet_SIGNS.md | 5e5090094fa51de7498885c647374f6192312b5d2ff931679f1db743533df41e | 339d561ef |
| overlap_note.md | 50766e674ad55a47ba7439bc2214e9eb5be44d44943870591662572f3174c32c | 339d561ef |

## Step 2: two blind Opus 5.5 passes (5 calls each, <= 8 lines per call)
Chunks L01-08, L09-16, L17-24, L25-32, L33-37; each call saw only its task text (`reads/task_<P><k>.txt`), the sheet and its
crops. Raw chunk reads in `reads/`; `assemble.py` drops DUP rows, strips a trailing '?' (conf capped at M) and renumbers.

| call | tokens | call | tokens |
|---|---|---|---|
| A1 | 108,794 | B1 | 111,280 |
| A2 | 110,025 | B2 | 111,448 |
| A3 | 112,666 | B3 | 110,694 |
| A4 | 109,109 | B4 | 110,127 |
| A5 | 105,932 | B5 | 107,278 |

| output | signs | sha256 | commit |
|---|---|---|---|
| outputs/vivonne1573-f103r-confirm2/passA_S2.tsv | 1,890 on 36 lines (L27 DUP) | 930e68ca640ef7b66ed90d929b2962826936cb9d057b58b659e3c01394a4d515 | c87a023e2 |
| outputs/vivonne1573-f103r-confirm2/passB_S2.tsv | 1,900 on 36 lines (L27 DUP) | 7ee3977507c8f507462a6b0ab36d4473d12dbf2195d96ef708ee57e6c11e9ece | 5e85d9da7 |

Chunk sha256s: SHA256SUMS_passA.txt, SHA256SUMS_passB.txt.

## Step 3: reconcile + one Sonnet adjudication
`tools/reconcile_passes.py passA_S2 passB_S2 --keep-alts` (rec/, 340ea0218): **agreement 1710/1918 = 89.2%** (per line 0.789
L04 to 1.000 L34); agreed-H 1,543, agreed-uncertain 167, disagree 208. Queue (`adjud_queue.tsv`, TXE-Q format): 375 rows.

Adjudication: one Sonnet subagent (`adjud_task.txt`, TXE-Q's worked example adapted to the text sheet), tokens 137,396; then one
resume of the same subagent (TXE-Q's precedent: one adjudication, one resume), tokens 139,999.
- Initial hand-back (kept as `adjud_out_first.tsv`, 41b39c8c0): **settled every row by rule (top-listed candidate), by its own
  report a pass-through, not an image adjudication**, though it marked viewed = yes on all 375.
- Resume (disagree rows only, from the image): **9 of 208 disagree rows settled from the image** (L01 cols 19, 20, 23, 32, 42;
  L03 cols 5, 11, 12, 13), 7 of them differing from the top-listed candidate; the other 199 kept pass A's reading at conf L, viewed = no.
  The 167 uncertain rows kept the agreed reading (their viewed = yes comes from the rule-based initial hand-back).
- Applied (`apply_adjud.py`): passZ 1,891 signs; 18 positions changed vs the reconciler's draft; 27 positions dropped (NONE: pass A
  had no sign there). **passZ is therefore essentially pass A at the disagreements, not an adjudicated read.** Not re-run: the
  frozen pipeline allows one adjudication.

| output | sha256 | commit |
|---|---|---|
| adjud_out.tsv | 0352864811647bbb205d97cac61d4366859eac59c95bccbadd0ac40c75cefc92 | 6ff5fb060 |
| outputs/vivonne1573-f103r-confirm2/passZ_S2.tsv | b5e6ab9f847fadb2175253e4aa0de8edf7743c14fe8fa9491130d393691ec928 | 6ff5fb060 |

## Step 4: doubt feed (never resolved)
`outputs/vivonne1573-f103r-confirm2/doubt_S2.tsv` (sha256 2cb696d350df88fa88f243b9c06d4c0df3f3f0bdf98da7a237bde4df2ebae99c,
6ff5fb060): per passZ position, disagree / uncertain / adjlow (adjudicator conf M/L or viewed = no) / latt / n_signals; 348 of
1,891 positions (18.4%) carry at least one signal. **latt has no input (NA):** it is a key-lattice decode of the read, i.e. a decode
of f.103r, outside this worker's rules, and `tools/tx_doubt.py signals` has no unit for this item ("unit vivonne1573-f103r-confirm2
not in benchmark-tx/txeng/units/README.md").

## For the lane
- The single score uses passZ_S2.tsv as the pipeline output; given the adjudication result, passA_S2/passB_S2 beside it carry most
  of the information. Vocabulary = SIGNS.md labels as read (no --label-map); `{words}` tokens are possible in the passes.
- Cost: the orchestrator get_session reading (12 subagent calls: 10 Opus reads + 1 Sonnet adjudication + 1 resume).
