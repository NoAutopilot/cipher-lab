# PREREG-PISA-275R (9 Oct 2026, written 13:5x UTC by date -u, pushed before any tile is shown to a reader)

Job: PISA-275R, brief .claude/briefs/runs/2026-10-09-account4-default-1340-jobs.md J2 (LANE DEFAULT-account-4-20261009-1340).
Amendment to PREREG-UNA-PISA.md: its stage 2 run on the third page it named, f.275r, which UNA-PISA did not reach (call budget).
Everything not stated here is PREREG-UNA-PISA.md unchanged: the 22-cell sheet (una_pisa/blind/cells_sheet.png, cells_map.tsv,
seed 20261009), the 5 known-answer tiles, the prompt text (una_pisa.py build), the reply format and una_pisa.py score.

## Material (disk only, no network)
- Target tiles: the f.275r T45/T47/T57 tokens of reading_f275r_tokens.tsv (17), located by eye on line strips from the committed
  images/f275rL_* crops (una_pisa/strips.py), with una_pisa/windows.py (now anchored on R9-PIS2's eye-located f.275r tokens,
  pis2/tokens_pos.tsv) and a 120 px re-centring montage, recorded in una_pisa/tokens_pos.tsv (rows page=f275r).
  Not located with confidence, excluded: f.275r L08 pos35 (T47; the sign sequence fits two neighbouring signs, ~2450 or ~2510).
  So 16 target tiles: T57 11, T47 3, T45 2.
- Caveat as in UNA-PISA: the worker looked at the lines to locate the tokens; the reader sees no labels, key values or copy.
- Images (strip crops, tiles) are cut into the worker's scratch directory and are not committed (brief common item 5);
  una_pisa.py takes UNA_IMG=<dir> for the f275r tiles; tiles_map.tsv and prompt.md are committed.

## Reader and staging
- Reader: one blind Opus call (the UNA-PISA instrument; the blind Sonnet crop compare is [retired] for these table cells after
  D07-PIST40's 1/5 control, so a Sonnet reader would be a different and already-failed instrument). 16 target tiles + the 5
  known-answer tiles re-shuffled (seed 20261009 + 1, the index UNA-PISA's script already reserves for f275r), same sheet.
- Gate GK on this call: known-answer best cell = own cell >= 4 of 5. If GK FAILs the call is a NON-TEST for f.275r: logged, no
  per-token result used. No second call to rescue a failed GK (a second call is allowed only if the first reply is unparseable).

## Rule per token (unchanged)
SETTLED-<cell> when best cell is given at medium or high confidence; else UNSETTLED. A key-cell correction is a candidate only if
>= 3 tokens of one label settle on one other cell of the hypothesised value (T45 -> a u cell, T47 -> an f cell, T57 -> an n cell)
and none settle on the labelled cell. A transcription-label slip (T57 -> T32 as on f.301v/f.302v) is a candidate when >= 3 T57
tokens settle on T32; it is then tested as its own pre-registered re-score with UNA2-PISA's three gates (G1 rise above key-shuffle
p99 and order p99 on f.275r, G2 positive control >= 4/5, G3 per-token alignment >= half and above the old label), in a separate
step; nothing is relabelled in this job.
Nothing in key86.tsv, the transcriptions, readings or grades changes in this job.
