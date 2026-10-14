# PREREG-VIVFKEY (14 Oct 2026, VIV-FKEY, account-4 worker for LANE VIV-KEYSTONE)

Committed and pushed before any pooled tally, key change, gate or score. Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md
"Wave 6" / "VIV-FKEY". Disk only; no network, no vision call. Instrument: VIV-KEY's (PREREG-VIVKEY.md) restricted to the plaintext letter f,
pooled over every truth leaf of this hand. Script: tx/vivfkey.py (written after this file), outputs under tx/viv63_fkey/.
What is already known before this file (read from summaries, not tallied by this job): the truth files mark every truth-f position
`excluded:letter-off-key` (or key-M / off-key) because no key row carries f; their `ref_sign` column at those positions shows labels g, p, P,
x, m, L, :, o, y, tz, s, b among others (read while locating the files). VIV-KEYV (AUDIT 7) saw an f-like sign (Tomokiyo col f row 1, large
looped g-like) inside label e. VIV-67B's labels put o (single) -> f 2, y -> f 1, b -> f 1 on f.201v. The rule below is written with that in view.

## (i) Material (committed, read as is)
Five truth leaves, one file each (benchmark-tx/): f.102r `vivonne1573-f102r-dev2.truth.tsv` (dev2, the re-anchored item, control 0.721; dev is
NOT used, it covers the same leaf); f.103r `vivonne1573-f103r-confirm2.truth.tsv`; f.201r `vivonne1573-f201r-dev.truth.tsv`; f.201v
`vivonne1573-f201v-dev.truth.tsv`; f.211r `vivonne1573-f211r-dev.truth.tsv`. Ink groups for the conflict and spread rules: ink 40 = f.102r + f.103r;
ink 67 = f.201r + f.201v; ink 70 = f.211r. The label used is `ref_sign` (the committed reconciled label, the label key.tsv is applied to). Reading the
plain column of the confirm2 file is a key tally, not a transcription score; no transcription is scored by this job.
Report-only beside it: tx/vivanchor_result.json, tx/viv67_labels.tsv, tx/viv70_labels.tsv, tx/viv67b_labels.tsv rows with aligned letter f.

## (ii) Counting positions
A row is ALIGNED when `plain` is a single letter a-z. The truth builds apply the local alignment check (>= half of the keyed neighbours within 8
positions either side decode to their aligned letter) only to `scored` candidates, not to off-key / letter-off-key / key-M rows. This job applies
the same check uniformly to EVERY aligned row: neighbours = the rows within 8 file positions either side (file order = stream order) whose ref_sign
is a forcing code (key.tsv row with grade C, source "published key", meaning equal to key_tomokiyo.tsv) and whose plain is a letter; a neighbour is
ok when the forcing meaning equals its plain. A row COUNTS when it has >= 1 keyed neighbour and ok share >= 0.5 (WIN 8, WMIN 0.5, the builds'
values). Brace tokens ({curl}, {blot}, ...) are nulls and never candidates. F = the counting rows whose plain is f.

## (iii) Decision rule
For each label L: f_L = |F with ref_sign L|; n_L = counting rows with ref_sign L; share_L = f_L / n_L.
- **ROW** for L iff L has NO key.tsv row, f_L >= 3, share_L >= 2/3, and no CONFLICT (two ink groups each with >= 2 counting rows of L, each with a
  unique top plain letter, tops differ). A tie for the top letter is no ROW.
- **SPLIT** for L iff f_L >= 3 and the ROW test fails only because L is keyed to another letter or share_L < 2/3, AND f occurs at L on >= 2 of the 3
  ink groups, AND L is enriched at f: base rate b_L = (counting rows with ref_sign L whose plain is neither f nor L's top letter) / (counting rows whose
  plain is neither f nor L's top letter); enrichment f_L / |F| >= 3 x b_L and one-sided binomial P(X >= f_L | |F|, b_L) < 0.01. A SPLIT means the
  f-sign sits inside label L as a sub-shape; it is not a key row.
- **NEITHER** otherwise (f scattered over labels at reader-error rates, or too few).
Several labels may each be ROW or SPLIT; each is reported. The headline is ROW if any label is ROW, else SPLIT if any is SPLIT, else NEITHER.

## (iv) If a ROW
Each ROW label -> one key.tsv row: code L, meaning f, grade C, source "clerk decipherments ink 41 / ink 68 / ink 71 on the five truth leaves, pooled;
VIV-FKEY", n_aligned = n_L, n_match = f_L, top_aligned from the tally, per-leaf counts in the note. Then every decode script that reads key.tsv and has
--check (tx/viv63_decode.py, viv53G, viv54L, viv53L, viv53, viv54, viv52) regenerated, each --check 0. `tools/decode_key.py ... --try L=f` report-only
as VIV-KEY ran it (scratch ciphertext, key before), pasted, not a gate.
Gates: tx/vivanchor_gates.py unchanged, `--seed 20261014VF-<ink> --tag vivfkey` on inks 63, 53, 54 (tx/vivfkey_gates_<ink>.json). Per ink PASS iff
verdict_b2 PASS AND verdict_wrong_keys PASS; positive controls failing = NON-TEST = fail. Any ink fails -> every row this job added is removed,
decodes regenerated back (each --check 0), logged "rows held: gate FAIL on ink N". Known limit (VIV-KEY): these gates show a row did not break the
decode, they cannot tell f from another letter; the row rests on the clerk anchors. A verifier follows any edit.

## (v) If a SPLIT (and no ROW)
No key.tsv edit, no relabelling: applying a split needs per-tile shape relabelling on ink 63, which a disk-only job cannot do. Write
tx/viv63_fkey/f_tiles.tsv: every row of F (leaf, line, pos, ref_sign, ink group, clerk context +-4 letters, SPLIT label yes/no), the input the
VIV-PACKET3 packet needs to show the f-shape against its host label. Report the tally and the split labels.

## (vi) If NEITHER
No edit; the tally and per-label numbers logged in NOTES.md.

## (vii) Reported, not gated
Per-label table for every label with f_L >= 1 (f_L, n_L, share_L, top letter, per-ink-group f counts, b_L, enrichment, binomial p); |F| per leaf;
truth-f rows lost to the alignment check; the report-only label-file hits. No depth, N-class or reading change (rule 10, rule 4a).

## (viii) Stop rule
Cap USD 6 or 80% of the box (box 03:29-04:44 UTC 14 Oct by date -u; 80% at 04:29), whichever first; no gate run is started that cannot finish
before it; if a ROW's gates cannot finish, the row is reverted (no untested row stays in key.tsv).
