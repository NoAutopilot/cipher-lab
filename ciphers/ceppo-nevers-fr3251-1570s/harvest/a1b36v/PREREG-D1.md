# D1-CEPPO pre-registration (6 Oct 2026, written ~12:52 UTC by date -u, pushed before the Opus read)

Brief `.claude/briefs/runs/2026-10-06-account1-default-1240-jobs.md` section D1-CEPPO. Tiles unchanged:
`tiles/T1.png`-`T6.png` (cut_tiles.sh, A1B-CEPPO-36V, 3x, -auto-level). No re-cut.

## Reader C
One blind Opus subagent, one call, the six tile paths only: no prior reads, no key, no candidate values, no sign sheet,
no statement of which sign is the target. It lists every cipher sign left to right with a short shape description and
the letter(s) written above it, each with confidence H/M/L, and one primary letter group per gloss (or "none").
This worker maps the target by the same `target_idx` column as `blind_reads.tsv` and casts no vote.

## Rule (2 of 3, per the brief)
- A reader's vote on a tile is its first-listed (primary) letter group for the gloss above the target sign, at confidence
  M or H. An L read, "unreadable", or "none" is no vote. For readers A and B (blind_reads.tsv) the first-listed option is
  taken: A T4 "ii", T5 "ii", T6 "ii" (all L -> no vote); B T4 "ll", T5 "ll", T6 "ll" (M -> votes); T1-T3 no votes from A or B.
  So by construction only T4-T6 can reach 2 of 3 (B + C on "ll"); T1-T3 cannot, whatever C reads.
- Agreement needs the identical letter group (case-insensitive; long s and s count the same; "ll" and "11" do not).
- An agreed letter is recorded against the instance (S76/S58 split), not either label. It is a gloss reading, not a key
  value: printed S76 = z. An agreed non-z group over an S76/S58 instance is logged as a data conflict (rule 4) in
  HYPOTHESES.md and the f.87 S76 tokens (already graded) go to M if not already M; no key.tsv value is changed by this job
  (one witness leaf, contested split label), so decode --check is run only to show the reading is unchanged.
- Otherwise the tile stays M; no grade changes.
