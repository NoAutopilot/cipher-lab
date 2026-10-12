# PREREG-PISA-244 (12 Oct 2026, written 07:1x UTC by date -u, before any tile is shown to a reader)

Job: PISA-244, brief .claude/briefs/runs/2026-10-12-acct1-default-0640-jobs.md (LANE DEFAULT-A1-0640, account 1). Disk only. Cap 3.5.
Target: the 26 f.244r tokens that tx86/ciphertext_f244r.tsv labels T45 (o), T47 (m) or T57 (la), never compared before (PISA-T475 cut them).

## Locating (done before this file; the worker saw the signs, not any reader)
- Centres are pisa_244/locate.tsv: eye-located on 2x ruler views of the una_pisa/strips.py f.244r strips (s2 at x 1360, as R9-PIS2),
  counting from slashes and R9-PIS2's eye-located T31 anchors, then re-centred once on a tile montage. pisa_t475/locate.py's predictions
  were not used (off by one sign or more on most). 24 located, 2 not located:
  L06 p29 (T45; tx86 p27-p30 repeat the p22-p26 group inside the s1/s2 overlap, no sign of its own on the strip) and
  L07 p41 (T47; written over p42 T19 as one cluster). Locating notes found by the way, logged as leads, not tested here:
  tx86 reads one crossed-p sign as ?[tcross] + T45 twice (L02 p11-12, L04 p44-45) and as T45 + ?[tcross] once (L06 p24-25); one sign at
  L05 1635 carries two labels (T35 p29, T57 p30); L06 p27-p30 repeat p22-p26 within the overlap.

## Instrument (UNA-PISA, unchanged; GK passed 4/5, 5/5, 5/5, 5/5, 5/5, 5/5, 5/5 on 9-11 Oct 2026)
- Sheet una_pisa/blind/cells_sheet.png (22 cells, map una_pisa/cells_map.tsv, seed 20261009), the 5 known-answer tiles (UP.CONTROLS),
  prompt text and parser of una_pisa.py verbatim except file paths. Token tiles: PIL crop x +/- 60 px (120 px) of the strip at the
  locate.tsv centre, full strip height, 2x, committed in pisa_244/tok/ and pisa_244/blind/f244r/. Shuffle seed 20261012 + 244.
- Reader: ONE blind Opus subagent call (24 targets + 5 controls). No key values, copy, labels, locate notes or earlier answers.
  Reply verbatim in pisa_244/blind/reply_f244r.txt; scored by pisa_244/pisa_244.py score -> pisa_244/result.tsv (--check).

## Gates and rules (fixed now; UNA-PISA's stage-2 rules)
- GK: known-answer tiles whose best is their own cell >= 4 of 5; below that the call is a NON-TEST and nothing below is read.
- Per target token: SETTLED-<cell> when the reader's best cell is given at medium or high confidence; else UNSETTLED.
  SETTLED on the label, or on a cell of the same key86 value: no edit, logged. SETTLED on a cell of another value: a label-slip
  (relabel) candidate only.
- Key-cell rule: a key-cell correction is a candidate only if >= 3 tokens of one label settle on one other cell of another value and
  none settle on the labelled cell; even then it is a separate PREREG, never applied here.
- Relabel candidates are NOT re-scored in this job (no f.244r UNA2-style re-score is pre-registered here, and the cap does not hold one);
  any candidates are named as the next step (UNA2-PISA / PISA-T32 gates G1-G3 against the f.244r copy).
- Nothing in key86.tsv, tx86, readings or grades changes in this job.
