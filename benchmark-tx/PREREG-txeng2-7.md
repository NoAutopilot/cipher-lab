# PREREG TX-ENGINEER-2 round 7 (lane incarnation 2, session_011EV9AKeJ4YuU9jjghdUy6F, 9 Oct 2026 19:5x UTC by date -u; pushed BEFORE any read or score; gate per PREREG-txeng2-0 Amendments 2-5: pool 29 pending B1's recount; no eval look this round)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check` passes on this file before any spawn. B1 runs under
PREREG-txeng2-6's own declared section (spawned this round).

## O1 Overlap-zone audit of the baselines' indels, read-free (TXE2-OVERLAP; Opus 5.5; cap 3; TX-RED F23)
Nearest prior: X21 / X21b deviations (the typed s1/s2 overlap sentence wrong on dev_tune and dint; readers measured 425 and
1,100-1,300 px), M16 (`iiif_lines.py --overlap-note`, the manifest-generated sentence that is the rule for new briefs),
X12 / X19 (deletion detectors: retired as instruments -- this is not an instrument, it is an audit of the baselines).
What is different: no reader, no instrument -- for every pool item whose baseline passes were read under a typed overlap
sentence (dev_tune/eval_heldout/f178r: harvest/f178v and f178r crops, blind_pass_brief_1572.md; dint-f128-print:
pass_instructions.md; f152r: its own brief; Spinelli: txeng/confirm reader_task.txt; ceppo items: harvest/f87 brief),
measure the true s1/s2 overlap per line from the crop manifests or the crop images themselves (pixel match of the shared
strip), and then locate every deletion and insertion of the baseline (tx_bench --json per item: dint A 2 deleted / B 5
inserted, no.87 L and A/B, f152r's 1 inserted, Spinelli's 2 deleted / 3 inserted, f87's) relative to the overlap zones:
inside / at the seam (within 1 sign width) / outside. Dev items are read-free; eval items' error POSITIONS are opened
read-free and counted (openings: eval_heldout, f178r, f152r, Spinelli = 4). Declared reading rule: if >= half of an item's
indels sit inside or at the seam of its overlap zones, that item's baseline is marked "overlap-sentence-suspect" in
units/README and BENCHMARK-TX notes, and its re-read under the manifest `--overlap-note` is declared a baseline change
(never a gain) in the next Amendment; below half, the typed sentence is corrected for future briefs only. No gate, no
instrument, no reads. Output: benchmark-tx/txeng2/overlap/RESULTS.md with the per-item table (overlap stated / measured
per line, indels in/seam/out), sha256 beside every commit hash, and "Openings of eval truth: 4 (positions only)".

Costs this round: O1 3 + B1 6 (PREREG-6) + H1 housekeeping 4 (brief only, not an experiment). Eval looks this round: 0.
