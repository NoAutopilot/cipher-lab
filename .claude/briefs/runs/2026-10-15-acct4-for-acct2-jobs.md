# Jobs queued by the account-4 parent (LANE VIV-KEYSTONE, session_01D7XWmthshMVqxumdDvitPh) for account 2's dispatcher, 15 Oct 2026 01:5x UTC

All three report to the account-4 parent (ROOM.md lines "for LANE VIV-KEYSTONE (account 4)"); the account that runs them ledgers them. Each
worker: CLAUDE.md first, `python3 tools/room.py --start`, last 30 ROOM.md lines, claim before any edit, PREREG file pushed before any
measurement, done line when stopping, commit by explicit path, pull --rebase, push to main, five-line report. None touches key.tsv, any
committed reading, status.json or an owner page; none starts another job. Target folder: ciphers/fr16104-vivonne-spain-1572 (NOTES.md sections
VIV-67, VIV-67B, VIV-70, VIV-70B, VIV-DECH3 are the worked examples; openapi.bnf.fr: take/release lines in ROOM.md, one request at a time >= 3 s
apart, disk first; a canvas already on disk is never refetched).

## JOB VIV-67C (Opus 5.5 worker, Sonnet readers; cap USD 10; box 120 minutes; openapi.bnf.fr <= 8; Price: vision calls: 6 x USD 1.4 = 8.4)
Exactly VIV-67B's method (NOTES "VIV-67B": two blind passes per leaf, reconcile, key-constrained alignment under the registered trim rule,
200 value-shuffled keys as the null) on **f.202r** (canvas 207 right, about 30 cipher lines with marginal notes; the remainder of ink 67)
against the continuation of ink 68's decipherment: f.206v's tail and **f.207r** (canvas 212 right; VIV-67B says f.202r "should open on f.206v and
run into f.207r"), read in two blind passes each. Crops: `tools/iiif_lines.py --image <leaf> --out <dir>` pasted before the first reader call;
one line crop (or its halves) per Sonnet call, readers return text only. PREREG-VIV67C.md first (gate: the registered alignment statistic vs the
shuffled-key p95, as VIV-67B). Outputs with the 67C names (tx/f202r_*, tx/dec_f207r_*, tx/dec67c_norm.txt, tx/vivk67c_result.json); the
benchmark item vivonne1573-f202r-dev registered only if the gate passes (BENCHMARK-TX.tsv row, as VIV-67B did for f.201v); label table counts
only. NOTES.md "## VIV-67C (<date -u>)": leaves by eye, requests per host, the gate table, what the leaf adds (a sixth truth leaf of this hand:
more known-answer positions for the g-split and the other label splits), cost not visible.

## JOB VIV-70C (Opus 5.5 worker, Sonnet readers; cap USD 12; box 150 minutes; openapi.bnf.fr <= 10; Price: vision calls: 8 x USD 1.4 = 11.2)
VIV-70B's "Next" line: **f.211v and the following cipher page of ink 70** against the rest of ink 71's decipherment under the registered trim rule
(PREREG-VIV70B.md; this is the rule's first blind use, say so in PREREG-VIV70C.md and report the rule's pass/fail as a result of its own,
beside the alignment gate). Same method and outputs as VIV-70B with the 70C names (tx/f211v_*, tx/dec71*_, tx/vivk70c_result.json); the
benchmark item vivonne1573-f211v-dev only if the gate passes. Start with 600 px overviews to confirm which canvases carry f.211v and the end of
ink 71 (VIV-70's NOTES give the offset), then native crops of only those. Stop before a unit (a leaf, a pass) that would cross 80% of cap or box.

## JOB VIV-LOOKALIKE (Opus 5.5; cap USD 4; box 60 minutes; disk only, no network, no readers; Price: vision calls: 0 x USD 0 = 0)
STATUS.md's parked gap "ink 63 label splits and overlap duplication": run `tools/lookalike_pass.py` on the named pairs (r/z, 2/z on f.193v; c/e and
6/b on f.192r) across the ink-63 passes on disk (tx/f19*_pass*.tsv and tx/viv63_f191/*pass*.tsv), and add a PRE-REGISTERED overlap-dedup step to
tx/viv63_clean.py for the s1/s2 half-line overlaps readers wrote twice (f.192r L06, L34; f.193r L07): PREREG-VIVLOOKALIKE.md first (the rule, the
known-answer check on the three truth leaves where the same overlap shape exists, the gate: dedup must not remove any position the truth leaves
keep, and err_2reader on f.193r must not rise). Re-decode ink 63 with tx/viv63_decode.py into a scratch copy (never reading_piece63.tsv), report
err_2reader per leaf before/after and the longest all-H run per leaf before/after; the lookalike pass's 2-of-3 residual is agreement, not accuracy
(CLAUDE.md Usage 6). HYPOTHESES.md one row with the control. NOTES.md "## VIV-LOOKALIKE (<date -u>)". No committed reading changes; the parent
decides whether the dedup rule enters the build.
