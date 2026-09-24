LANE R5 WORKER C -- fr3151 SEURE 1558 f75L: coarse shape buckets, then the same three-line gate (Sonnet, cap $5; disk only).
Target: ciphers/fr3151-seure-1558. Common rules: .claude/briefs/runs/2026-09-24-lane-r5-common.md. Read NOTES.md "Re-segmentation and
passes f75L (LANE R4 O)": segmentation is clean (9.1% noise) but passes agreed 38.5% because nine loop/hook codes (loopMN, W, hookL,
hookS, hookJ, hook, hook2, hook7, chook) do not separate on this image.
1. Merge the hook/loop family into 2-3 shape buckets defined by features a reader can see on a strip (e.g. closed loop vs open hook vs
   hook with descender), from the contact sheets; write the merge as a mapping file (glyphs/buckets.tsv: old_code, bucket, rule) and
   re-label via tools/glyph_atlas.py (add an option with a test only if relabelling cannot be done with existing options). Commit.
2. Re-run the gate on the SAME three lines (9, 5, 15): pass A by you, pass B by one blind Sonnet subagent (never opens passA*),
   against the coarse atlas; `tools/reconcile_passes.py passA_coarse.tsv passB_coarse.tsv --rows`. Also report what the old passA/passB
   agree at after mapping both through buckets.tsv (a free check). Commit.
3. Gate >= 80%: report agreement per line and stop (the orchestrator decides on an Opus reconciler). Gate < 80%: append to NOTES.md the
   line "f75L is not box-keyable at this image quality even with coarse buckets (<x>%); needs a different capture or a key" and stop.
   No hand-settling either way.
NOTES.md section "Coarse buckets and gate (24 Sept 2026, LANE R5 C)". ROOM done: "for LANE R5: seure coarse gate <x>% (lines 9/5/15:
a/b/c), types <n>, cost $<c>". No solving.
