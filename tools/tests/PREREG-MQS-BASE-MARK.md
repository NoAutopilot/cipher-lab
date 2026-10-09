# PREREG-MQS-BASE-MARK (written 9 Oct 2026, 07:49 UTC by date -u, by MQS-BASE-MARK, before any control below was run)

Source of the gap: research/MARY-STUART-TALK-2026-10-09.tsv row M11 ("Diacritic variants as separate types; base+mark
labels so a mark can be reclassified without re-boxing"; Lasry, Biermann and Tomokiyo 2023, Cryptologia 47:2, p.112 n.48,
Figs 3-4 p.113). Gap as recorded: a label is one opaque code, so reclassifying a mark means relabelling every token by hand.

## Feature

1. `tools/sign_sorter_apply.py --split-marks MARKS.tsv [--mark-labels F]` adds two columns to the settled export, `base`
   (the settled sign, before any ':' it already carries) and `mark` (the tile's attached marks from marks.tsv, one label per
   mark, ordered left to right and joined by '+'; '' for a plain tile). A mark's label is, in order: the `--mark-labels`
   table (mid or mark cluster -> label), the marks.tsv's own `mark`/`kind` column, else the mark's cluster from
   `--clusters` (`m<cluster>`), else `m` (marked, unclassified). A settled sign already of the form `base:mark` is split
   on its last ':' and its mark is kept. `new_sign` is unchanged (existing behaviour and tests unchanged).
2. `tools/decode_key.py`: a tsv ciphertext with `base` and `mark` columns (and no sign column) reads its sign as
   `base` or `base:mark`. `--merge-mark SPEC` (decode.json `merge_marks`) reclassifies marks for the whole text with one
   edit: `X` = mark X is not distinctive (the token is read as its base), `X=Y` = mark X is mark Y, `*` = every mark is
   dropped. Applied to `base:mark` signs (split on the last ':') whichever ciphertext form carried them. Default (no
   option): behaviour unchanged. Must-NOT guard: a merge that collapses a key distinction (key has both `B` and `B:X`, or
   `B:X` and `B:Y`, with different values) is reported on stderr as `merge-mark collapses` with the codes, every time.

## Controls (offline script `tools/tests/mqs_base_mark_control.py`; results to tools/tests/RESULTS-MQS-BASE-MARK.tsv)

**K1 round trip, Birago 1572 atlas (structure only, no key value read or written; ASKS 118).** From
ciphers/nevers-birago-fr3251-1572/atlas signs.tsv + marks.tsv + clusters.tsv: truth label per sign = `S<sign cluster>`
plus `:` + its marks' `m<mark cluster>` joined '+' when it carries marks. Write a settled labels file holding the compound
truth labels, run `--split-marks`, then rebuild `base[:mark]` from the two columns. Statistic: share of signs whose rebuilt
label equals truth. Expected 1.000; **gate 1.000** (every sign; 348 marked of 4209). Null N1: marks.tsv with its `sid`
column permuted (seed 1), same run; can differ because the statistic depends on which sign each mark is attached to.
Expected about 1 - 2x348/4209 ~ 0.85 or lower; **null gate <= 0.95**.

**K2 one-edit reclassification, synthetic French (design of the intended use: a homophonic letter cipher whose variants
are told apart only by a mark; length of Birago no.87's scale).** 20 seeds; per seed 1,500 letters of tools/data fr16
text (folded a-z); key: 22 bases, letters split into plain base and base:dot variants (6 letters have a dotted homophone
on a base of another letter), plus a non-distinctive `flourish` mark put on 10% of tokens at random. Transcription error
injected: every `dot` recorded as `tick` (a mark misclassified page-wide). Statistic: decode accuracy (letter equal to
truth, unkeyed = wrong) after the single edit `--merge-mark tick=dot,flourish`. Before the edit: expected <= 0.85; after:
expected 1.000; **gate mean >= 0.99**. Null N2: the same edit applied to a ciphertext whose marks were permuted across
tokens (seed-matched); can differ because the statistic depends on which tokens carry the dot. Expected well below the
known answer; **null gate mean <= 0.95**. Ceiling check: the before-edit accuracy is reported, so the gain is read against
a baseline not at ceiling (rule 3).

**K3 must-NOT (guard).** On the K2 key, `--merge-mark dot` (dot is distinctive) must print `merge-mark collapses` naming
each of the 6 bases; `--merge-mark flourish` must print nothing. Gate: 6/6 named and 0 false alarms, all 20 seeds.

A control that misses its gate ships the option at shelf grade `weak` with both numbers (no re-brief). No target status,
key, reading or AUDIT.md change; nothing value-bearing from the Birago 1572 family is written.
