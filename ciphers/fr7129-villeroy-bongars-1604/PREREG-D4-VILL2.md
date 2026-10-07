# PREREG D4-VILL2 (7 Oct 2026, written 14:4x UTC before any scored run; account 4, LANE DEFAULT-account-4-20261007-1335)

Job (brief `.claude/briefs/runs/2026-10-07-account4-default1335-jobs.md`, D4-VILL2): the transcription part of
READ2-RELABEL that D4-VILL could not run (Gallica 503). f.260r (canvas f525, `tools/gallica_folio.py` confirmed
'260r' 3725x5914 at 14:45 UTC) lower block fetched native by `tools/iiif_lines.py --ark btv1b8555834s --canvas 525
--region 450,2280,3200,2250` and recut `--image <src> --region 0,105,3200,2145 --lines-per-crop 2 --max-width 1700
--overlap 120` into 13 gloss+cipher line pairs x 2 segments (`sibling/f260r_crops/p260_L01..13_s1|s2.jpg`, overlay
`p260_lines_debug.jpg` checked: each band = one clerk gloss row + its cipher row). L01..L12 are VB-KEY's lines 1-12
(same block, line 1 under "aitreueillez & peutestre"); L13 is one more line VB-KEY did not take.

**Instrument (the one NOTES names, different from the blind passes).** Reader pass with the clerk's gloss in view
(2 Sonnet calls, L01-07 and L08-13, prompt `sibling/passes_r2/READER_PROMPT.md`): per cipher sign, the sign id by
shape (inventory.txt, overbar asked on every number) and the gloss letters written directly above it. Checker pass
(2 Sonnet calls, separate, sees the crops and the reader's TSV, not the key): confirms or corrects each row's sign and
gloss. Reconciliation (one unit): checker corrections taken; rows the checker marks unsure keep the reader's id.
Neither pass sees a key, another pass's files, or NOTES. Output `sibling/passes_r2/`, merged by
`sibling/vill2_align.py` into `sibling/pairs_r2_f260.tsv` (sign-aligned pairs, grade C, the clerk's values).

**Key.** `tools/interlinear_align.py` on the 13 new lines exactly as D4-VILL's `shared_align.py` (--code-prefix: 2+-digit
numerals '%' 0..12 letters, other signs '@' 0..2 letters; --keep-fs; --prior = key v2's single-letter cells; 6 iterations;
cipher side = the reconciled sign sequence, plain side = the line's gloss letters joined, normalized as `kp_key_v3.norm`),
then the unchanged `kp_key_v3.build()` (majority per sign, v2 fallback, null when '-' majority >= 2).

**P1, primary (the brief's test, the M9 hold-out of record).** The same 28 observations VB-KEY and D4-VILL scored
(`kp_key_v3.observations()`: VB-KEY's blind f.260 pass lines 1-12, f.258 lines 2-6). For an f.260 observation of line n
the key is built from the new lines other than n-1, n and n+1 (a conservative window, since VB-KEY's line numbering
may drift by one against ours in the middle of the block); f.258 observations use the key from all 13 new lines.
Statistic: `compare_clerk.score` matched clerk letters / clerk letters, summed over the 28 (VB-KEY 0.340, D4-VILL 0.294).
Control in the same run: 20 class-shuffled copies of each key (`decode_f275.shuffled`, seed of record). **Gate >= 0.70.**

**P2, secondary (same statistic, same control, same 0.70 gate).** Leave-one-line-out inside the new transcription:
new line n's reconciled sign sequence decoded with the key from the other 12 new lines, scored against new line n's
own gloss letters. Caveat fixed now: the reader saw the gloss, so its sign ids may lean toward the letters above them;
P2 tests whether the clerk's values are consistent per sign ACROSS lines under these labels, not shape-blind accuracy.

**Descriptive.** Families g, 9, y, f, u, d, do, Zt, ls, ff, xff, single digits, 99, 18: count, majority, share, vs key v3
and D4-VILL. Reader-vs-checker change rate. The tool's `--shuffle 20` CONSISTENT count on the new pairs.

**Decision.** P1 >= 0.70: decode f.268 with the target's decode script and `--check`, judge fr16 and fr17 (rule 7), report
both. P1 < 0.70 and P2 >= 0.70: the key is consistent under gloss-in-view labels; the limit is the blind transcription
of the held-out lines and of f.268; no f.268 decode; next step = f.268 re-transcribed against the new labelled sign
sheet. Both < 0.70: rule 3 third-attempt clause -- the gloss-in-view instrument is logged [retired] for "the f.275 key
read via the f.260 clerk gloss" at this transcription quality. Status stays `blocked` (Tomokiyo-paper gap) either way.

**Deviation logged before scoring (7 Oct 2026, 14:5x UTC; nothing scored yet).** The first two reader calls (half-page
crops, 1700 px wide) both reported that they did not read the gloss per sign but spread each segment's gloss
proportionally over its signs -- not the instrument. Their files are kept apart in `sibling/passes_r2/v1_proportional/`
and are NOT used for any number. Replacement: each band cut by `sibling/f260r_crops/cut_windows.py` (command `python3
sibling/f260r_crops/cut_windows.py`) into 7 windows of 520 px (80 px overlap, red seam tick) enlarged 2x, at which the
gloss letter over each sign is visible; reader v2 (`READER2_PROMPT.md`, 3 Sonnet calls L01-04, L05-08, L09-13, every
window opened, no proportional spreading), then the checker on the same windows. Everything else above is unchanged
(key rule, P1, P2, gate, control, decision).
