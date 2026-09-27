# Nevers neighbouring-volume sweep, 27 Sept 2026 (parent worker NEV-SWEEP)

Brief: `.claude/briefs/runs/2026-09-27-parent-nev-sweep.md`. Reviewer's bet 1 (CODEX-REVIEW-2026-09-27b.md,
"search neighbouring volumes around one strong existing family"), accepted by the owner on the SOLVE parent's
14:38 line: a bounded experiment using `tools/cipher_page_detector.py` (the 24 Sept 2026 image layout
pre-filter, weights unchanged) over the BnF Nevers volumes fr.3976-3985 that neighbour fr.4715's known
Vieuville-Nevers cipher family, to measure whether the detector finds material the catalogue searches missed.

## Method

U1: chose fr.4715 (btv1b52509819x, 202 canvases) as the calibration set -- its known cipher folios are listed
in `ciphers/fr4715-montholon-1589/POOL.md`'s item table (from `nevers.htm`'s "Vieuville-Nevers Cipher" list
and `bnf4715.htm`'s undeciphered items). Candidate sweep volumes from the Nevers series with no register row
yet (fr.3976 and fr.3979 already have rows -- CS-FR3976 found-solved, INTAKE-3979 found-solved): resolved
Gallica arks by SRU search (`gallica.bnf.fr/SRU`, host still gallica.bnf.fr) restricted to `dc.type=manuscrit`
and the "Collection Memoires de la Ligue" series title shared with fr.3976/fr.3979/fr.4715's own volume family:
fr.3977 = btv1b9060546p (715 canvases), fr.3980 = btv1b90605458 (682 canvases), fr.3982 = btv1b9060543f
(561 canvases); fr.3978 and fr.3981's arks did not resolve by this query within the job's time. All three
resolve via `tools/gallica_folio.py --list` (manifest fetch only, cached).

U2 (calibration): scored the 22 known cipher folios of fr.4715 (recto side of each item in POOL.md's table:
ff. 3, 24, 28, 30, 44, 50, 51, 58, 60, 62, 64, 65, 67, 70, 71, 73, 75, 77, 78, 80, 81, 83) at 400px thumbnail
width with the detector's own scorer and its unchanged weights/threshold (0.5), plus 4 unambiguous non-cipher
negatives (the volume's own binding leaves: plat sup., contreplat sup., page de garde recto/verso).

## Result: detector gate FAILS on fr.4715 -- stopped after U2, no sweep run

**Recall on fr.4715's known cipher folios: 4/22 = 0.182** (scores: f.24=0.51, f.64=0.54, f.67=0.75, f.75=0.52
scored cipher; the other 18, including the target folder's own f.58/f.81, scored plain, 0.29-0.41 range).
**False positives on the 4 binding-leaf negatives: 1/4 = 0.25** (the front cover, "plat sup.", scored 0.53).

Per the brief's own stop condition ("if recall on fr.4715 is under 0.7, stop after U2 and say the detector is
not fit for the sweep at this width"): **stopped here. U3 (sweep of fr.3977/fr.3980) and U4 (manual sample)
were not run.** This is consistent with, and sharper than, the detector's own documented 24 Sept 2026 held-out
figure (holdout n=27: precision 0.750, recall 0.692, fpr 0.214, gate recall>=0.85/fpr<=0.15 FAIL) -- fr.4715's
own letters score noticeably worse than the general holdout set, not better, so this specific neighbourhood is
not a case where the detector's known weakness happens not to matter.

## Answer to the reviewer's question

Did the sweep find cipher material the catalogue searches missed? **Not tested.** The calibration step that
the brief gates the sweep on failed decisively (0.182 vs. the 0.7 floor), so no canvas in fr.3977, fr.3980 or
fr.3982 was scored or viewed. This is a negative on the detector's fitness for this task at this image width and
this threshold, not a negative on whether the neighbouring volumes hold undiscovered cipher letters -- that
question is untested by this method. The named next step, if this bet is retried, is a different instrument (a
higher-resolution scan with the `--autocrop` feature retested at this specific volume's scale, or a completely
different cheap filter such as a plain full-text/finding-aid sweep of fr.3977/fr.3980/fr.3982 for "chiffre"
rather than an image classifier) -- not a further run of this same detector at this same width.

## Counts

- Volumes: fr.4715 (calibration, 202 canvases; not swept, only 26 canvases scored for calibration), fr.3977
  (715 canvases, resolved, not swept), fr.3980 (682 canvases, resolved, not swept), fr.3982 (561 canvases,
  resolved, not swept; a third candidate kept in reserve if the gate had passed).
- Canvases scored: 26 (22 positive calibration + 4 negative calibration).
- Network requests: 3 manifest fetches (fr.3977/fr.3980/fr.3982, cached from `--list` calls also used by U1) +
  1 manifest fetch (fr.4715, already cached from an earlier worker) + 26 thumbnail image fetches (one
  transient connection reset on the first fetch, one retry per the good-citizen rule, then all succeeded) +
  5 Gallica SRU catalogue-search queries (still gallica.bnf.fr host) to resolve the three candidate arks. All
  gallica.bnf.fr, well under the brief's 400-request thumbnail allowance and its 12-fetch manual-sample
  allowance (0 of the 12 used -- U4 not reached).
- No vision subagent calls used (U4 not reached).
- No KEY-ADJACENT.tsv rows added (no confirmed new cipher letters -- the sweep that would have found them did
  not run).

## For parent 7m -- sweep verdict

**Detector not fit for the sweep at this width: fr.4715 calibration recall 0.182 (4/22), well under the 0.7
floor. No sweep of fr.3977/fr.3980/fr.3982 was run; nothing found or ruled out in those volumes by this
method.**
