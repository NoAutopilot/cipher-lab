# PREREG-VIVKEY (14 Oct 2026, VIV-KEY, account-4 worker for LANE VIV-KEYSTONE)

Committed and pushed before any pooled tally, key change, gate or score. Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md
"Wave 2" / "VIV-KEY". Disk only; no network, no vision call. Rule 3 third-attempt clause: VIV-ANCHOR's instrument re-run on NEW material
(the ink-67 clerk anchors of VIV-67), not a re-tuning on the same material. Script: tx/vivkey.py (written after this file).

## (i) Material (all committed, read as is)
- Ink 40 anchors: tx/vivanchor_result.json `target.label_centric` (VIV-ANCHOR, word-anchored against the ink-41 decipherment; every
  position counts at confidence 1.0, since a window anchors only when every other letter of a >= 7-letter word decodes exactly).
  Only per-label value counts are used (`values`); positions are cited as listed.
- Ink 67 anchors: tx/viv67_labels.tsv (VIV-67, banded-DP alignment of f.201r to the ink-68 decipherment under key_tomokiyo.tsv).
  An occurrence is ALIGNED when `aligned_letter` is a single letter a-z (not '-'); it COUNTS when also `dp_conf` >= 0.5.
- Brace tokens ({curl}, {scribble}, {blot}, ...) are nulls (VIV-ANCHOR (i)) and are not candidates.

## (ii) Candidates
Every label NOT in key.tsv with >= 3 aligned positions pooled (ink 40 positions + ink 67 aligned occurrences, any confidence).
Expected from the committed summaries (not yet tallied by this job): c, o, 2, e, t, r, i. Keyed labels (V = n C; y = h M; S = b M;
b = z M) are REPORT-ONLY: their pooled top letter is printed beside the key value; a disagreement is logged as a CONFLICT and
nothing in key.tsv changes for them (no grade change either; that is a later job).

## (iii) Decision rule (VIV-ANCHOR's, pooled)
For a candidate L, pooled counting positions P = ink-40 positions + ink-67 occurrences that count (conf >= 0.5).
- Top letter X of P. L -> X iff count(X) >= 3 AND count(X) / |P| >= 2/3. A tie for top is no assignment.
- CONFLICT: if ink 40 and ink 67 each have >= 1 counting position for L and each has a unique top letter, and the two tops differ,
  L is a CONFLICT: logged with both tallies, no row, whatever the pooled share.
- X must be a plaintext letter; if X equals a letter the key already carries, L becomes a homophone of it (allowed, as V -> n was).
- Everything else: "under rule" (n < 3 or share < 2/3), logged.

## (iv) Key change and re-decode (only if (iii) assigns anything)
Each assignment -> one key.tsv row: code L, meaning X, grade C, source "clerk decipherments ink 41 (fr.16105 ff.105v-108v, word-anchored on
ink 40, VIV-ANCHOR) + ink 68 (fr.16105 ff.205r-205v, DP-aligned on ink 67 f.201r, VIV-67), pooled; VIV-KEY", n_aligned/n_match and the
top letters filled from the pooled tally, positions or counts per ink in the note. Then tx/viv63_decode.py, tx/viv53G_decode.py,
tx/viv54L_decode.py and every other decode script that reads key.tsv and has --check (viv53L, viv53, viv54, viv52 if present)
regenerated and each --check exits 0.
Also run, for each assignment, `python3 tools/decode_key.py ciphers/fr16104-vivonne-spain-1572 --try L=X` (MQS-CROSSWORD; controlled-only on
letter codes) if the folder's layout lets it run; its output is pasted, REPORT-ONLY (not a gate); if it cannot read this folder, say so.

## (v) Gates (each ink, after the change; NEW seeds)
tx/vivanchor_gates.py's code path unchanged (b2 order gate with C1 f.103r and C2 positive controls + 200 value-permuted wrong keys),
with seeds '20261014VK-63', '20261014VK-53', '20261014VK-54' (option --seed added to the script, default unchanged) and results written
to tx/vivkey_gates_{63,53,54}.json (registered vivanchor_gates_*.json untouched). Per ink PASS iff verdict_b2 PASS AND
verdict_wrong_keys PASS. If the positive controls fail ("not a gate"), that ink is a NON-TEST, logged, and counts as a fail for the
revert rule.
Revert rule: if any ink fails, every row added by this job is removed, the decodes regenerated back (each --check 0), and the result
logged as "rows held: gate FAIL on ink N". If more than one row was added and an ink fails, each row is then tried alone ONCE
through the same gates (seeds '...-<label>' appended) if the box allows; otherwise all stay out.

## (vi) Reported, not gated
Before/after per ink: H/M/U counts from the reading TSVs; longest consecutive H run (vivanchor_gates.runs(), AUDIT 2's measure: every
M/U breaks it, across line ends) with the five longest H stretches as text for ink 63; the fr16 judge mean log-prob of the ink-63
decode letters (tools/judge_plaintext.py NgramModel on t.FR16, the corpus of the b2 gate) before/after. Per-token grade counts for the
verifier. No depth or N-class is set (rule 10, rule 4a).

## (vii) Stop rule
Stop at the cap (7) or 80% of the box (01:48 UTC 14 Oct), whichever first; do not start a gate run that cannot finish before it. If the
gates cannot be run in the box, every added row is reverted (no untested row stays in key.tsv).
