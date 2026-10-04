# TX-FABLE (account 3 worker) -- 4 Oct 2026 15:3x UTC (account-3 orchestrator; owner's decision, 4 Oct ~8:30 am PDT)
Owner: "do a test on a few where we've had trouble with transcription and point Fable at them. Then compare to what we had. If
meaningfully better, we'll assign Fable or whatever the latest model is to transcription." Context: every scored full pass so far is
Sonnet (CLAUDE.md Usage 1 tiers transcription to Sonnet); four machine-side additions failed on no.87 today (TRANSCRIPTION.md);
research/MARY-STUART-METHOD-2026-10-04.md says reading quality, not tricks, is what carried their work.
Items: every BENCHMARK-TX.tsv item (all have a known answer): birago1572-no87 (eval), dint-f128-print, ceppo-f21v-S, ceppo-f87-S,
ceppo-f36v-gloss (dev). Baselines = the existing Sonnet outputs in benchmark-tx/outputs/<item>/ (passA, passB; also the reconciled read
where one exists).
1. PREREG first (benchmark-tx/PREREG-txfable.md, pushed before any Fable call): for each item, ONE blind Fable pass with the SAME line
   crops, the SAME sign sheet / label inventory and the SAME prompt text as that item's Sonnet pass A (find them in the item's NOTES or
   brief; if a prompt is not on disk, reconstruct it from the pass-A brief and say so). Readers see crops + sheet only: never truth,
   values, decodes, other passes. The worker must not open any *.truth.tsv until every Fable pass file for that item is committed.
   Gate, fixed now: "meaningfully better" = BOTH (a) pooled over all items, Fable's paired sign test vs the better of each item's two
   Sonnet single passes has fixed > broken with p < 0.05 (tools/tx_bench.py --paired), AND (b) err_true lower than the better Sonnet
   single pass on no.87 (eval) and on at least 3 of the 4 dev items. Also report Fable vs the reconciled two-pass Sonnet read (the
   real pipeline output) -- informative, not the gate. Report cost per 100 signs for Fable vs Sonnet (TRANSCRIPTION.md target 8).
2. Calls: Fable subagents (Agent tool, model fable), one call per leaf or line group exactly as pass A grouped them, line crops only,
   never a full page (Usage 6). State the unit count and per-call estimate after the first call; stop before a call that would cross
   80% of the cap, and score what is done (no.87 first, then dint, f21v, f87, f36v).
3. Score with `python3 tools/tx_bench.py <pass> --bench BENCHMARK-TX.tsv --item <item>` and `--paired`; write benchmark-tx/txfable/
   RESULTS.md (per-item table: Sonnet A, Sonnet B, reconciled, Fable; paired fixed/broken; top confusions before/after; cost), a
   TRANSCRIPTION.md job-table row TX-FABLE ("Today" column), and LESSONS.md one line only if the gate passes. Do not change the model
   rule in CLAUDE.md or any brief yourself: if the gate passes, write the proposed one-line change in RESULTS.md for the parent.
Model: worker Opus 5.5 (scoring, no reading); reads Fable (claude-fable-5-1). Cap USD 30, box 120 min. Disk only (crops on disk; any
missing crop is re-cut from disk sources with tools/iiif_lines.py --image, never refetched). ROOM claim/done via tools/room.py.
Do not touch any target's readings or keys.
