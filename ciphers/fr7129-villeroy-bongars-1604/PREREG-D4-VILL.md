# PREREG D4-VILL (7 Oct 2026, written before any scored run; account 4, LANE DEFAULT-account-4-20261007-1335)

Job (brief `.claude/briefs/runs/2026-10-07-account4-default1335-jobs.md`, D4-VILL, READ2-RELABEL): re-derive the
f.275 key from the clerk's interlinear decipherment of the sibling f.260r with the shared `tools/interlinear_align.py`
(not the private `sibling/kp_key_v3.py` alignment), score it on the VB-KEY M9 hold-out, compare families with key v3.

**Deviation logged before scoring (13:55 UTC).** The new sign-aligned transcription of f.260r (one reader with the
clerk's gloss in view, one checker) needs f.260r re-fetched from Gallica. At 13:46-13:53 UTC Gallica answered the
manifest with a read timeout, the native image with HTTP 503 and the info.json retry with HTTP 503 ("temporarily
unable to service your request due to maintenance downtime or capacity problems"); per the good-citizen rule the host
was not hit again. So this run uses the pairs already on disk -- VB-KEY's blind f.260 passes (`sibling/passes/
f260_S*[AB].tsv`, 23 line observations) and VB-KP's f.258 lines 2-6 -- i.e. the third "While waiting" bullet. It
changes the alignment instrument only, not the transcription; under rule 3's third-attempt clause it is NOT a
genuinely different instrument for the transcription leg and is reported as such whatever it scores.

**Pairs.** One pair per observation of `kp_key_v3.observations()` (same 28 observations, same letters, same sign
lists as VB-KEY's holdout-em). Cipher tokens written for the shared tool in --code-prefix mode: every 2+-digit numeral
(with or without ^) is a word code (`%` prefix, 0..12 letters, --max-chunk 12); every other sign (letter-like signs,
single digits, ^single digit) is a code (`@` prefix, 0..2 letters, --code-chunk 2). --keep-fs (manuscript gloss, no
long-s OCR confusion). --prior: key v2's single-letter cells (VB-KEY seeded v2 in round 1 the same way). 6 iterations
(tool default). Null cost: tool default.

**Key rule.** The tool's per-token alignment TSV is turned into (sign, chunk or '-', line) pairs and passed to the
unchanged `kp_key_v3.build()` (majority per sign, v2 fallback for unattested signs, null if '-' majority with >= 2) --
the identical key-construction rule and decode as VB-KEY, so only the alignment instrument differs.

**Primary test (brief: "key from f.260 lines").** For each of the 28 observations, a key built from the f.260 pass
lines only, minus both passes of the held-out line when it is an f.260 line; f.258 lines are scored with the key from
all f.260 lines. Statistic: `compare_clerk.score` letter agreement (matched clerk letters / clerk letters), summed over
the 28 observations, the same metric as VB-KEY's 0.340. Control: the same with 20 class-shuffled copies of each key
(`decode_f275.shuffled`, seed of record) -- a control that can vary on this statistic. **Gate: >= 0.70** (the M9 bar).
**Secondary (reported beside, same gate):** VB-KEY's exact scope (key from f.258 + f.260 observations, leaving out only
the held-out observation's own line), so the two instruments are compared like for like (VB-KEY: 0.340, shuffled 0.246).
**Shared-tool rule-3 statistic (descriptive):** the tool's own `--shuffle 20` CONSISTENT count on the full f.260 pairs.
**Family comparison (descriptive):** per sign of g, 9, y, f, u, d, do, Zt, ls, ff, xff, single digits: count, majority
value and share under the shared tool vs key v3.

**If the primary gate passes:** decode f.268 with the target's decode script and `--check`, judge fr16 and fr17. **If it
fails:** no f.268 decode; log under rule 3 that this was the same transcription with a different aligner (not a new
instrument), and keep READ2-RELABEL (re-fetch + reader/checker transcription with the gloss in view) as the open step,
blocked only on Gallica availability. Status stays `blocked` (the Tomokiyo-paper gap, line 3 of NOTES.md).
