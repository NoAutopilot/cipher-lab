# PREREG-PISA-T475 (11 Oct 2026, written 18:5x UTC by date -u, before any tile is shown to a reader)

Job: PISA-T475, brief .claude/briefs/runs/2026-10-11-acct1-default-1840-jobs.md (LANE DEFAULT-A1-1840, account 1). Disk only. Cap 2.
Target: the f.275r key86 T45/T47/T57 tokens PISA-275R left UNSETTLED: L10 p12 (T57; PISA-275R best T57, second T32, low),
L11 p19 (T47; best T42, second T19, low), L15 p27 (T45; best T19, second T27, low). Centres are PISA-275R's eye-located
x_centre_strip (una_pisa/tokens_pos.tsv: 660, 975, 1670). L08 p35 (T47) stays not located.
f.244r scope cut (stated before any read): f.244r's 26 T45/T47/T57 tokens have never been located; una_pisa/windows.py's predict with
R9-PIS2's anchors misplaces most of them by one sign or more (pisa_t475/locate.py montage, worker's eye), and an eye re-centring of 26
tokens plus a second reader call does not fit the cap. f.244r is logged as the next step with the locating aid, not run.

## Instrument (UNA-PISA, unchanged; GK passed 4/5, 5/5, 5/5, 5/5, 5/5, 5/5 on 9-11 Oct 2026)
- Sheet una_pisa/blind/cells_sheet.png (22 cells, map una_pisa/cells_map.tsv, seed 20261009), the 5 known-answer tiles, prompt and parser
  of una_pisa.py verbatim except file paths. Token tiles: PIL crop x +/- 60 px (120 px, as PISA-275R) of the una_pisa/strips.py strip, full
  strip height, 2x, committed in pisa_t475/tok/ and pisa_t475/blind/f275r/. Shuffle seed 20261011 + 75.
- Reader: ONE blind Opus subagent call (3 targets + 5 controls). No key values, copy, labels or earlier answers. Reply verbatim in
  pisa_t475/blind/reply_f275r.txt; scored by pisa_t475/pisa_t475.py score -> pisa_t475/result.tsv (--check).

## Gates and rules (fixed now)
- GK: known-answer tiles whose best is their own cell >= 4 of 5; below that the call is a NON-TEST.
- This reader SETTLES a token on <cell> at medium or high confidence. SETTLED-BY-TWO <cell> when <cell> is also PISA-275R's best or
  second for that token; otherwise UNSETTLED for this job (both reads logged).
- SETTLED-BY-TWO on the token's own label, or on a cell of the same value (T47/T31/T11 = m): no edit, logged.
- SETTLED-BY-TWO on a cell of another value: a relabel candidate, re-scored under the UNA2-PISA / PISA-T32 / UNA3-PISA / PISA-T31 gates
  (G1 reconciled nw_score strictly rises and stays above key-shuffle p99 and order p99, f.275r err 0.215, copy kp86d; G2 control >= 4/5;
  G3 relabelled tokens identical to the aligned copy letter >= ceil(n/2) and > the same tokens identical under the old value), key86.tsv
  unchanged, pis1key/una2_pisa imported unchanged. All pass -> committed (pre-edit bytes kept as *_preT475.tsv, reading regenerated,
  decode_key --check). Any fail -> nothing applied. The re-score runs only if it can finish before 80% of the box (19:44 UTC) and the cap.
- Nothing in key86.tsv changes in this job.
