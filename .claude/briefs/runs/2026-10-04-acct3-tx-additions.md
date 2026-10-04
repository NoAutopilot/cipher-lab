# TX additions from research/TRANSCRIPTION-PRACTICE-2026-10-04.md (owner approved 4 Oct 2026; account-3 lane A3V)

Three tool jobs, one worker each, Opus 5.5. Read TRANSCRIPTION.md and the research note's row for your job first. Common rules: the
`.claude/briefs/README.md` common tail (room.py start/claim/push, no dollar figures, no AskUserQuestion). Every job: Usage 8 (an option on
the shared tool + an offline test in tools/tests/, no private copy); pre-register the gate in the job's report before running it;
**measure on BENCHMARK-TX.tsv (no.87) as a paired count on the same signs -- signs fixed vs signs broken against the current pipeline --
plus err_true before/after**; a change is adopted only if fixed > broken with a sign test p < 0.05 or the pre-registered gate says so.
Write results into TRANSCRIPTION.md "Today" column and SYSTEM.md (tools list). Price subagent calls per pass (Usage 6).

## TX-VIEWS -- multi-view voting (cap USD 8; box 75 min)
`tools/iiif_lines.py --views N` writes N altered views per line crop (padding shift, rescale 0.8/1.25, small elastic warp, contrast
stretch); `tools/reconcile_passes.py` accepts N passes and reports per-sign vote share and pairwise error correlation between passes.
Test: no.87 read blind once per view (subagent calls = views x line batches; state the count), majority vote vs the current 2-pass
reconcile, paired fixed/broken; report which views have the least-correlated errors (arXiv 2509.09722 found those help most).

## TX-AGREEAUDIT -- re-check the signs both readers agreed on (cap USD 5; box 50 min)
`tools/lookalike_pass.py audit`: re-reads a random sample of *agreed* signs (both passes identical) blind against the atlas, with 5%
planted known errors as the control (the audit must catch >= 80% of planted errors, else it is a non-test). Test on no.87: how many of the
known agreed-but-wrong signs (LESSONS.md "Look-alike pass") it flags, and its false-flag rate on agreed-and-right signs.

## TX-ALTS -- carry alternatives into the lattice (cap USD 5; box 50 min)
Pass prompts write `a/b?` whenever the reader hesitates (DECRYPT convention, Megyesi HistoCrypt 2020); `tools/reconcile_passes.py
--keep-alts` carries every alternative into the lattice `tools/key_decode_lattice.py` reads. Test: fraction of no.87 errors with the truth
in the lattice (currently 27/97), then key_decode_lattice err_true at the pre-registered lam vs current; paired fixed/broken.
