# TXE-I: contrast sweep before cutting (O6, owner's item 6) -- FAIL at the read-free dev gate, no read

LANE TX-ENGINEER round 2, worker TXE-I (account 4, Opus 5.5), 9 Oct 2026 07:38-07:4x UTC by date -u. Brief
`.claude/briefs/runs/2026-10-09-account4-txe-i.md`; pre-registration `benchmark-tx/PREREG-txeng-2.md` (+ p < 0.01 amendment).
Tool `tools/tx_contrast_sweep.py` (sweep / stable / gate / sheet / resolve), test `tools/tests/test_tx_contrast_sweep.py`.

**Verdict: FAIL (read-free dev gate not met).** On dev_tune the `uncertain` flag holds 5 of L's 14 wrong positions (recall
0.357, precision 0.069) at 21.0% of positions flagged; registered gate: recall >= 0.5 at <= 20% flagged. No reader call was
made (0 vision calls), no passQ file exists, no eval look was used (0). tools/tx_taxonomy.py on passQ is therefore not run.

## Method (what the tool does)
Five grey thresholds per page: t_3 = Otsu, step = 0.03 x (p95 - p5), t_k = Otsu + (k - 3) step (f178v: 136.2, 141.6, 147.0,
152.4, 157.8; manifests `manifest_f178v.json`, `manifest_f179r.json`). Rendering k narrows a linear stretch from the page's
p5-p95 (level 1) to a binarisation at t_5 (level 5, "Otsu minus 2 steps" on the ink-intensity scale). Per box grown 50%:
8-connected ink components >= 20 px at each level, assigned to the atlas box they overlap most (an unboxed component to the
target when its x-centre is inside the box: band-cut tails); chains by IoU >= 0.5 to the next level. STABLE = chain at >= 4
levels; APPEARING = chain only at levels 4-5, or new ink >= 20 px attached at the 3->4 / 4->5 step (tails); VANISHING = chain
only at levels 1-2 (a stroke seen apart at soft contrast that merges at harder contrast: a closing gap, a joining speck).
Because the cuts are nested, ink only grows with level; "vanishing" is therefore identity loss, not ink loss (documented in
--help). uncertain = n_appearing + n_vanishing >= 1. Box <-> position map label-blind (tools/tx_compare.box_map, widths only).

Calibration, truth-blind, before the gate (`CALIBRATION.md`): the brief-literal defaults (step 0.06, min area 6) flagged 54.4%
of f178v; the rule "page flag share <= 20% and closest to it" over a 4 x 5 grid chose step 0.03, min area 20 (now the
defaults). The per-box tables were committed (642199517) before truth was opened.

## Per-page flag shares (read-free)
| page | boxes | uncertain | stable-ink box differs > 10% in h or w | appearing > 0 | vanishing > 0 |
|---|---|---|---|---|---|
| f178v | 675 | 135 (20.0%) | 134 (19.9%) | 43 | 99 |
| f179r | 144 | 33 (22.9%) | 32 (22.2%) | 13 | 22 |

## Flag vs wrong positions (gate; `gate_dev_tune.tsv`, `gate_eval_heldout.tsv`, `flags_<unit>.tsv`)
```
gate dev_tune vs L: scored 343, wrong 14; flagged 72 (0.21); wrong flagged 5 -> recall 0.357 precision 0.069; registered gate (recall >= 0.5 at <= 20% flagged, vs L): not met
gate dev_tune vs passA: scored 343, wrong 23; flagged 72 (0.21); wrong flagged 8 -> recall 0.348 precision 0.111
gate eval_heldout vs L: scored 376, wrong 15; flagged 69 (0.184); wrong flagged 3 -> recall 0.2 precision 0.043
gate eval_heldout vs passA: scored 376, wrong 18; flagged 69 (0.184); wrong flagged 4 -> recall 0.222 precision 0.058
```
eval_heldout is read-free (no reader, no output scored): reported as the brief asks, not an eval look. Pass A wrong counts
are position_errors' wrong-or-deleted on the unit (23 and 18; the PREREG table's 24 / 18 count err_true incl. insertions).

Post-hoc breakdown (not gating; p = one-sided binomial chance of holding at least that many of the wrong positions at
that flag share):

| unit | feature | flagged | L wrong held | recall | precision | p (chance) |
|---|---|---|---|---|---|---|
| dev_tune | uncertain | 72 (21.0%) | 5/14 | 0.357 | 0.069 | 0.152 |
| dev_tune | appearing > 0 | 27 (7.9%) | 1/14 | 0.071 | 0.037 | 0.683 |
| dev_tune | vanishing > 0 | 50 (14.6%) | 4/14 | 0.286 | 0.080 | 0.135 |
| dev_tune | stable-ink box change > 10% | 56 (16.3%) | 5/14 | 0.357 | 0.089 | 0.064 |
| eval_heldout | uncertain | 69 (18.4%) | 3/15 | 0.200 | 0.043 | 0.538 |
| eval_heldout | appearing > 0 | 19 (5.1%) | 1/15 | 0.067 | 0.053 | 0.541 |
| eval_heldout | vanishing > 0 | 54 (14.4%) | 2/15 | 0.133 | 0.037 | 0.656 |
| eval_heldout | stable-ink box change > 10% | 82 (21.8%) | 2/15 | 0.133 | 0.024 | 0.871 |

Reading: contrast instability is not where L's errors are. Its rate on wrong positions is at chance on eval and not
distinguishable from chance on dev; the "appearing tail" feature (the d T18 / s T98 mechanism the brief names) holds 1 of
14 and 1 of 15. L's remaining errors are mostly on signs whose ink is stable across the sweep -- consistent with TXE-A's
finding that they are recall/look-alike choices on clean ink, not unseen strokes.

## Reader
None (gate not met). Task text that would have been used (brief step 4): "for each numbered row the five tiles are the same
sign at rising contrast; weigh only strokes present in at least four tiles; give the sheet cell T## that matches, or X_NEW /
?; row, sign_id, conf, strokes used". Calls: 0 vision, 0 subagents.

## Follow-up (one line, not done)
The sweep is a cheap per-box feature (4.5 s a page); it may still serve as one column in a combined selector (round 3), but
alone it adds nothing at p < 0.01.
