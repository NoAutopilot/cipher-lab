# TXE2-BASE-SPIN2: Spinelli confirm baseline re-read under atlas_v5 (PREREG-txeng2-9 B2)

9 Oct 2026, 21:33-21:4x UTC by date -u. Worker TXE2-BASE-SPIN2 (account 4, Opus 5.5) for LANE TX-ENGINEER-2 incarnation 2;
brief `.claude/briefs/runs/2026-10-09-account4-txe2-round9.md`. **A baseline change, never a gain (Amendment 7).** This job
has no instrument and makes no paired instrument claim. The old-vs-new paired line below compares two baselines and
nothing else.

Openings of eval truth: 1 (the baseline score)

## Disclosure (logged in ROOM.md at 21:3x, before step 1)
My grep of `txe2-sheet3/RESULTS.md` for the shape names printed its lines 47-57. Those lines carry the positions and the
truth letters beside the three NEW shapes. The brief said to read the shape names only. Mitigations: (a) the table lookup
was done by a separate blind Opus subagent that saw only the published table image and the three shape names, and I took
its cell choice as given; (b) the collapse-map rule was taken from evidence that predates the truth file (the 28 Sept
H35 keymatch passes), applied mechanically: a cell is mapped only where both passes agree; (c) the readers and the
adjudicator saw only the sheet, the crops and the brief. The lane may judge whether (b) was still open to bias.

## Step 1: table lookup
Domnina 2016 Ill. 1 (`sources/domnina-2015-2016/p27_2016_plate_key_letter_decipherment.jpg`), cropped to
`lookup/domnina2016_ill1_table.png`. Blind subagent output (`lookup/lookup.tsv`, verbatim):

| shape | best cell | conf | runners-up |
|---|---|---|---|
| circle-on-stem | G sign 1 (phi-like loop on a stem, foot turned left) | M | FF (L), D sign 2 (L) |
| long-s-crossbar | U/V sign 2 (tall f / long s with a crossbar) | H | P sign 1 (L) |
| looped-H | SS sign 1 (large looped H flourish) | H | -- |

The table carries all three shapes, so the sheet changes. atlas_v5 = atlas_v4 + three rows, `KEY_G1`, `KEY_U_V2` and
`KEY_SS`, named after the published cells in the v7 KEY_* style. Each row's one exemplar is the published drawing, cut at
the subagent's box and fitted to a 72 px tile. No row uses a manuscript tile, so none was chosen through an eval position.
Built by `ciphers/spinelli-beinecke-c1515/glyphs/build_atlas_v5.py` (`--check` ok); see `SHEET-CHANGELOG.md`.

Collapse map (`benchmark-tx/txeng/confirm/collapse_map.tsv`, the rule is in its comment lines): a published cell maps to
the atlas code that BOTH H35 keymatch passes (`passes/keymatch_pass{K,L}.tsv`, 28 Sept) gave that cell. Published values
(Domnina 2016) are G1 g, U/V2 u, SS ss.
- `KEY_G1 -> PHI`: K PHI M, L PHI M.
- `KEY_U_V2`: unmapped (K NONE/TEE, L TEE/PHI).
- `KEY_SS`: unmapped (K JHOOK, L NONE).

An unmapped name scores as itself.

## Step 2: brief diff (B1's brief, the sheet the only change)
```
reader_task_v5.diff:  3c3  ...glyphs/atlas_v4.png  ->  ...glyphs/atlas_v5.png
adjud_task_v5.diff:   sheet atlas_v4 -> atlas_v5; queue/output paths basespin -> basespin2
```
The "do not resize" wording is kept from v4. The crops are the same committed `benchmark-tx/txeng/confirm/crops/` (20).
The call split is one call per pass with all 20 crops.

## Steps 3-4: passes, reconcile, adjudication
- passA_v5 has 254 signs and passB_v5 has 252. `reconcile_passes.py --keep-alts` gives agreement 240/254 = 94.5%:
  152 agreed-H, 88 agreed-uncertain, 14 disagreements, so the queue has 102 rows (`build_queue.py`, B1's copy).
- Adjudication was one Sonnet call with no resume. Its output covers 102/102 rows in queue order: 94 M and 8 L.
  `apply` changed 3 positions vs the draft, giving passZ_v5 with 254 signs.
- New-sheet names used in passZ_v5: KEY_G1 at p1c_L02.27 and p2c_L01.17; KEY_U_V2 at p1c_L02.28 and p1c_L06.21; KEY_SS at
  p2c_L02.1. Two NEW: signs remain (p1c_L02.20 gamma-with-crossstroke, p1c_L08.3 epsilon-with-ring-above).

## Calls and tokens
| call | model | tokens | tool uses |
|---|---|---|---|
| table lookup (subagent) | Opus 5.5 | 108,504 | 10 |
| passA_v5 (20 crops + sheet) | Opus 5.5 | 134,010 | 24 |
| passB_v5 (20 crops + sheet) | Opus 5.5 | 135,885 | 24 |
| adjudicator | Sonnet | 132,802 | 25 |

Dollar cost: the orchestrator's get_session reading.

## Step 5: the one score (label-mapped; spinelli-c1519-confirm only)
```
passZ_v5  err_true 0.067 (13/193) 95% 0.040-0.112 | wrong 10 deleted 0 inserted 3 | excluded 66
          flagged excluded 0.058 (11/191) 95% 0.033-0.100 [2 flagged]
          top confusions: i<-HOOK x3, u<-KEY_U_V2 x2, t<-TEE, i<-EIGHT, p<-THREE, s<-KEY_SS, n<-EIGHT
passA_v5  err_true 0.098 (19/193) 0.064-0.149 | wrong 16 deleted 0 inserted 3 | flagged excluded 0.089 (17/191)
passB_v5  err_true 0.057 (11/193) 0.032-0.099 | wrong 9 deleted 0 inserted 2 | flagged excluded 0.047 (9/191)
```
| file | position errors (wrong+deleted), as measured | flagged-excluded |
|---|---|---|
| passZ_v4.tsv (old baseline, atlas_v4) | 8/193 | 6/191 |
| passZ_v5.tsv (new baseline, atlas_v5) | 10/193 | **8**/191 |
| passA_v5 alone | 16/193 | 14/191 |
| passB_v5 alone | 9/193 | 7/191 |

### Baseline change, old -> new (paired, 193 common positions; a baseline change, not a gain)
`paired passZ_v5.tsv vs passZ_v4.tsv: base wrong 8, output wrong 10; fixed 2, broken 4; sign test p = 0.6875`
- Fixed: p1c_L02.26 and p2c_L01.17. p2c_L01.17 was an adjudicated NEW:circle-on-stem in v4 and is read KEY_G1 here.
- Broken: p1c_L01.3, p1c_L04.2, p1c_L04.11 and p2c_L02.13. None of these is read with a v5 row; they are reader/adjudicator
  variation at signs the sheet change did not touch.
- Wrong in both: p1c_L01.5 [flagged], p1c_L03.16 [flagged], p1c_L02.27, p1c_L06.21, p2c_L02.3, p2c_L02.7. p1c_L02.27 and
  p1c_L06.21 are read KEY_U_V2, which stays unmapped under the pre-set rule, so they score wrong as v4's NEW: did.
- Sheet-defect positions p1c_L01.14, .15 and p1c_L03.25 are right in both baselines.
- Full table: `score/positions.tsv`; raw output: `score/tx_bench.txt`, `score/detail.txt`.

## Pool arithmetic
Eval pool = 10 + 6 + <Spinelli's new flagged-excluded position errors> + 1 + 5 = 10 + 6 + **8** + 1 + 5 = **30**
(under Amendment 7 with B1's 6 the pool was 28). The lane makes the BENCHMARK-TX.tsv and pool change in Amendment 8. This job
touched neither.

## Commits and sha256 (all before the score unless marked)
| commit | file | sha256 |
|---|---|---|
| 1facfffd5 | ciphers/spinelli-beinecke-c1515/glyphs/atlas_v5.png | ad952c30f6a8f73676be22f02e86061c23b9710ea448a4a474e7ce689c68326c |
| 1facfffd5 | ciphers/spinelli-beinecke-c1515/glyphs/atlas_v5.tsv | 05aa05dfa74cb2bd5728db44f4a628526e16dfdf3b03c725a7465ca4322f724e |
| 1facfffd5 | ciphers/spinelli-beinecke-c1515/glyphs/build_atlas_v5.py | b5bd49b76b7c692548ac8cef60bb732861f0d41f04b371f2bbbc38d0cd523573 |
| 1facfffd5 | benchmark-tx/txeng2/basespin2/lookup/lookup.tsv | 38ab82f81f81b80f401df3975d1c15663bbdb66934906b6ecac3d05194131da6 |
| 1facfffd5 | benchmark-tx/txeng/confirm/collapse_map.tsv | da677b0dd44cdf70c12083ad53bab93cb5f2f6c5c31a698ccb73d4a50d43f793 |
| 1facfffd5 | benchmark-tx/txeng2/basespin2/reader_task_v5.txt | a7844b7d7f076312a3b2008954023fa30ba7a7989d870fe73abdc27f84531016 |
| 1facfffd5 | benchmark-tx/txeng2/basespin2/adjud_task_v5.txt | e04122149b6937ac2b1f4bd34036b3c3ff743606047197059c6e999a8c3070e5 |
| 24c54c0db | benchmark-tx/outputs/spinelli-c1519-confirm/passA_v5.tsv | 33575343134189a7bbec060e8916d3a2d769d942e2debe84a6d385300f9b4e39 |
| 24c54c0db | benchmark-tx/outputs/spinelli-c1519-confirm/passB_v5.tsv | e5ac48dbd84813f99abf89578f8088e58dce9754f2e42501bea78330764230a6 |
| 8f84e6261 | benchmark-tx/txeng2/basespin2/rec/*, adjud_queue.tsv | (in git) |
| fb2738dad | benchmark-tx/txeng2/basespin2/adjud_out.tsv | 0fc6f3653be7ab4487a824c7748723f74a570a43bea03b46d208f8c2e832bf8c |
| fb2738dad | benchmark-tx/outputs/spinelli-c1519-confirm/passZ_v5.tsv | b238c10e288370ea4f6536e0ad160288de81c15939658fcad9eef3fe197bcbb5 |
| this commit (after the score) | score/*, score_detail.py, RESULTS.md | -- |

No *.truth.tsv and no BENCHMARK-TX.tsv was edited. Nothing was re-read or re-adjudicated after scoring.

## Notation fold (LANE TX-ENGINEER-2 incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5, 9 Oct 2026 22:2x UTC by date -u; PREREG-txeng2-0 Amendment 8, TX-RED F36; read-free)
Declared in Amendment 8 before this score: the collapse map folds the new cell names to the published cells' key codes from
`ciphers/spinelli-beinecke-c1515/key.tsv`'s Domnina rows, never from the truth. Applied as `fold/collapse_map_fold.tsv`
(B2's map + the fold rows, rule in its comment lines; the truth file was not opened, no reader or adjudicator re-run):
- KEY_U_V2 (U/V sign 2, value u) -> HOOK: key.tsv's u codes are EM (U/V sign 1) and HOOK_U_V; the atlas map's HOOK row
  (28 Sept) places U/V sign 2 in the merged hook family, so the cell's key code is HOOK_U_V, already collapsed to HOOK
  (tx_bench applies the map as one lookup, so the row is written to the collapsed form).
- KEY_SS (SS sign 1, value ss): key.tsv carries no row with value ss (the keymatch passes gave K JHOOK L / L NONE L, so no
  code was ever assigned), so the declared rule yields no fold; KEY_SS stays unmapped and scores as itself. Amendment 8's
  "expected 5" assumed both names fold; under the rule as declared only one does.
```
passZ_v5 (fold)  err_true 0.057 (11/193) 95% 0.032-0.099 | wrong 8 deleted 0 inserted 3 | flagged excluded 0.047 (9/191) [2 flagged]
                 top confusions: i<-HOOK x3, t<-TEE, i<-EIGHT, p<-THREE, s<-KEY_SS, n<-EIGHT
                 paired vs passZ_v4: base wrong 8, output wrong 8; fixed 4, broken 4; p 1.0000
passA_v5 (fold)  err_true 0.088 (17/193) | wrong 14 | flagged excluded 0.079 (15/191)
passB_v5 (fold)  err_true 0.047 (9/193)  | wrong 7  | flagged excluded 0.037 (7/191)
```
| file | position errors (wrong+deleted), as measured | flagged-excluded |
|---|---|---|
| passZ_v4.tsv (old baseline) | 8/193 | 6/191 |
| passZ_v5.tsv under B2's map | 10/193 | 8/191 |
| **passZ_v5.tsv under the fold** | **8/193** | **6/191** |
Spinelli's pool count after the fold: **6** flagged-excluded (Amendment 8 expected 5; the KEY_SS position, p2c_L02.1 read KEY_SS
against an s-code truth, stays an error under the declared rule). v4 -> v5 under the fold: fixed 4 / broken 4, p 1.0, a
baseline change either way. Full output: `fold/tx_bench_fold.txt`. Openings of eval truth by this fold: 1 (the re-score; TX-RED F40 -- B1 counted its own).
sha256 of the inputs scored: passZ_v5 b238c10e288370ea4f6536e0ad160288de81c15939658fcad9eef3fe197bcbb5, passZ_v4
a641e2614b7e9931d22d1885d011a70fd7c3aeb1e25160e7b78534afbc756a70 (both as committed by B1/B2, unchanged).
