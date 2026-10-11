# PREREG-PISA-T31 (11 Oct 2026, written 17:26 UTC by date -u, before any tile is shown to a reader)

Job: PISA-T31, brief .claude/briefs/runs/2026-10-11-ytbiz-default-1709-jobs.md (LANE DEFAULT-A2-1709, account 2). Disk only.
Target: the 14 key86 T31 (m) tokens R9-PIS2 left UNSETTLED (pis2/t31_tokens.tsv): f.244r L03 i5, L06 i44, L07 i33, L07 i45,
L09 i20; f.275r L03 i31, L04 i7, L05 i0, L07 i11, L08 i0, L10 i13, L13 i11, L15 i9, L15 i33. A crop compare says which table
cell a page sign looks like (a label slip); it cannot show that the table gives a cell the wrong value.

## Instrument (the UNA-PISA instrument, unchanged; it passed its known-answer gate 4/5, 5/5, 5/5, 5/5 on 9 Oct 2026)
- Table sheet: una_pisa/blind/cells_sheet.png (22 cells of the 688 px table copy under letters A-V, map una_pisa/cells_map.tsv, seed
  20261009), unchanged. It holds T31 and T47 (m, bare x), T36 (s, x+o), T45 (o), T49/T17 (s), T42, T11 and the rest of UNA-PISA's set.
  T30 (in R9-PIS2's 8-cell set) is not on the sheet; a token whose true cell is T30 can only come out UNSETTLED or as a look-alike.
- Token tiles: the committed R9-PIS2 crops pis2/tok/<leaf>_<line>_i<idx>.jpg (x +/- 75 px, full strip height), 2x upscaled, under
  shuffled ids. Known-answer tiles: UNA-PISA's five (K-T36a f.275r L09 i3, K-T36b L14 i28, K-T17, K-T16, K-T46), re-shuffled in.
- Reader: one blind Opus subagent call per leaf (2 calls). The reader gets the sheet and tiles only: no key values, no copy text, no
  transcription labels, no earlier reader's answers, and is not told any tile has a known answer. Prompt = UNA-PISA's, verbatim
  except file paths. Seeds 20261011 + 1 (f244r), + 2 (f275r). Replies saved verbatim in pisa_t31/blind/reply_<leaf>.txt.
- Scorer: pisa_t31/pisa_t31.py score (UNA-PISA's parser) -> pisa_t31/result.tsv; --check exits non-zero if stale.

## Gates and rules (fixed now)
- GK per call: known-answer tiles whose best cell is the tile's own cell >= 4 of 5; a call below GK is a NON-TEST for its leaf.
- Per token (this reader): SETTLED-<cell> when best is given at medium or high confidence, else UNSETTLED.
- Third-reader rule: a token is SETTLED-BY-TWO <cell> when this reader SETTLES it on <cell> and <cell> is R9-PIS2's reader_top or
  reader_second for the same token. Otherwise it stays UNSETTLED for this job (logged with both reads).
- SETTLED-BY-TWO on T31 itself: first per-token support for the table's bare x cell; no change (label already T31).
  On T47 or T11 (value m): value-neutral, logged, no edit.
- SETTLED-BY-TWO on a cell of another value: a relabel candidate. Candidates are re-scored per page under the UNA2-PISA / PISA-T32 /
  UNA3-PISA gates, key86.tsv unchanged, with pis1key's run_files/control and una2_pisa's per_token imported unchanged:
  G1 reconciled nw_score strictly rises and stays above both the key-shuffle p99 and the order p99 (f.244r err 0.284, f.275r 0.215,
  copies as kp86/kp86d); G2 positive control >= 4/5; G3 pooled over the job, relabelled tokens whose new value is identical to the
  aligned copy letter >= ceil(n/2) and > the same tokens identical under m. All three pass -> relabel committed on that page
  (pre-edit bytes kept as *_preT31.tsv, readings regenerated, decode_key --check and kp86 --check run). Any fail -> nothing applied.
  Known conflict, stated now: on f.244r the T36 shape decodes s where the copy has o (R9-PIS2, D4-PISRS identical 0/6), so f.244r T36
  candidates are expected to fail G3; that is logged as rule-4 data, not overridden.
- Time rule: the re-score runs only if it can finish before 80% of the box (18:10 UTC); else it is logged as the next step, not run.
- Nothing in key86.tsv changes in this job.
