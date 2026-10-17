# PREREG VIV-KSPLIT (17 Oct 2026, worker VIV-KSPLIT, account 4)

Brief: .claude/briefs/runs/2026-10-17-acct4-research-director-6.md "## JOB VIV-KSPLIT". Written and pushed before any scored run.

## Material (counted before any read)
tx/kcells2/packet.tsv: 214 rows; 95 with a line crop (f102r/f102v/f103r, ink 40 leaves). By label and clerk letter, rows with a crop:
label c: 38 p, 9 q, 7 e (54); label 2: 41 m, 0 other. Label 2 therefore has NO contrast tile with a crop: on the cropped leaves the
alignment never puts label 2 at a non-m letter. A 2-way model read of label 2 cannot be scored (one truth class; the shuffled-truth
null is degenerate) and its exemplar sheet cannot be seeded (no u tile). Registered now: the model read runs on label c only; label 2
goes to the owner's sorter page (where a person may still see two shapes) and is reported as "not machine-testable at this material".

## Step 1: frequency-matched null (disk, seconds)
tx/ksplit/null_fm.py re-runs tx/kcells2/kcells2.py's measure() on ink 63 with 20 draws in which c takes a letter whose fr16 corpus
frequency lies within a factor 2 of p's, and 2 a letter within a factor 2 of m's (pool a-z less j, w, k; p and m themselves excluded;
seeded 'VIV-KSPLIT-fm-<i>'). Real (c=p, 2=m) passes iff its s and hrunV both exceed the matched draws' p99. Report only, no key edit.
Reading: if real passes the matched null, the VIV-KCELLS2 (c) verdict was the mean-score bias and is reported as such; if not, (c) stands.

## Step 2: tiles
Per leaf, the line crops are segmented with tools/glyph_atlas.py segment (--median-h pool, the s1/s2 overlap deduped at its midpoint,
as tx/vivgsplit/gsplit.py leaf_units), and tools/box_token_align.build_map (width DP, no labels, lam 0) maps the committed reading
tx/<leaf>_rec.tsv tokens (kcells's row_tokens, pos = its index) to boxes. A packet row gets a tile only when its (line, pos) is mapped
1:1 to one box. tiles.tsv carries id, page, line, pos, label; clerk letters only in truth.tsv. A contact sheet is eye-checked before
the sorter page or the read; a tile showing no whole sign is dropped and counted (truth-blind check: the eye does not see truth.tsv).

## Step 4: model read (label c)
Exemplar sheet: shape A = the 3 p tiles, shape B = 3 e/q tiles, chosen as the first 3 of each by tile id (no purity score exists per
tile; "highest purity" cannot be computed per tile, declared deviation). Exemplars are excluded from scoring. The remaining tiles are
shuffled (seed 20261017) into batches of about 12; one strongest-model subagent call per batch, 8 calls at most, each sees the exemplar
sheet + its batch tiles under neutral ids, answers A/B per tile, no letters named.
Score: accuracy (A on p, B on e/q); null: truth labels shuffled 200 times over the scored tiles (seed 20261017), p99.
Gate: accuracy > null p99 AND >= 0.80. (The brief's "both labels" gate cannot apply; label 2 is untestable, see Material.)

## Decision branches (registered before any run)
(a) label c passes the gate: the split works by machine for c -- name a KEYCELL-READ of ink 63 scoped to label c, priced per page from
this job's per-call rate; the owner's sort is held as the cross-check.
(b) label c fails: the owner's sort is the instrument; the parent scores it against truth.tsv when it lands.
(c) under 30 usable tiles for label c after the box check: say so, no read.
Label 2 in every branch: not machine-testable here (no contrast tile with a crop); the owner's sort is its only instrument now.

## Decision
Belief: the readers' labels c and 2 each merge two clerk signs (p into c, m into 2), and the packet tiles carry enough of both shapes to split them.
Would change it: under 30 usable tiles for label c after the box check (branch c), or a 2-way read at or below the shuffled-truth p99.
Observed: frequency-matched null on ink 63: real c=p, 2=m s -1.5289 rank 1/21 vs matched p99 -1.5344 (pass), hrunV 26 vs p99 26 (tie): FAIL by the registered both-stats rule. Tiles: 95 rows with a crop -> 46 mapped 1:1 (label-aware) -> 36 pass the box check: label c 15 (truth 12 p, 2 q, 1 e), label 2 21 (all m).
Decision: change -- branch (c): label c has 15 usable tiles and 3 contrast tiles, no model read (0 vision calls); the owner's blind sorter page is the only instrument now; more tiles need the ink-67/70 line crops (cut in scratchpads, never committed) or label-aware maps of more ink-40 leaves.
Lesson: the width-only box DP put only ~18 of 66 tiles on the sign their own reader label names on these leaves; use the label-aware map (classify top-3 + --loo) and eye the contact sheet before pricing any per-tile read -- packet rows are not tiles.
