# Standing prompt: an outside experimenter on the transcription benchmark (written 10 Oct 2026 00:5x UTC by date -u by the orchestrator (account-4), at the owner's decision that his ChatGPT runner may run its own experiments, collated with ours)

Collation rule (added to research/TX-PROGRAM.md the same minute): every outside experiment lands as a `[SO-TX-EXP-<id>]` pull request
carrying its own pre-registration, scripts, outputs and exposure ledger; a PR-LAND worker copies the files to `benchmark-tx/ext/<id>/`,
TX-RED grades it in its next pass, and the lane adds one row to `research/TX-REGISTER.tsv` with `campaign=external`. Its eval or
confirm items are scored only by the lane, once, under the lane's own look budget; the outside experimenter never scores them.

Paste everything below the line.

---

You reviewed our transcription measurement yesterday (your report is at
https://github.com/NoAutopilot/cipher-lab/blob/main/research/SO-TX-TRANSCRIPTION-2026-10-10.md; we adopted it: the scorer is fixed with
tests, the "bracket" wording is withdrawn, the f.102r truth is re-anchored as vivonne1573-f102r-dev2, your oracle-location diagnostic is
pre-registered as a candidate). I now want you to run your own experiments on the same benchmark, in your own sandbox, as a separate
line of work that we will collate with ours. Rules, which protect the benchmark rather than you:

1. **Dev items only.** BENCHMARK-TX.tsv column `split`: you may read truth files, crops and build scripts for `dev` items (the
   ceppo-*, dint-*-gloss*, dint-f128-print and vivonne1573-f102r-dev2 rows). Never open, download or score a truth file, crop folder
   or output of any `eval`, `confirm` or `confirm2` item (birago1572-no87, birago1572-f152r, bir1591-f23r-gloss*, gunther8246-p2,
   luzerne108a-p1, spinelli-c1519-confirm, vivonne1573-f103r-confirm2). If you need an eval score, say so in your PR and we run it once.
   vivonne1573-f102r-dev (without the 2) is withdrawn: do not use it.
2. **Pre-register before you read.** Your PR's first file is `benchmark-tx/ext/<id>/PREREG.md`: question, items, method, exact pass
   condition, what you will and will not open. Commit it before any experiment output. Our format: benchmark-tx/PREREG-txeng2-17.md.
3. **Score with our tool, fixed.** `python3 tools/tx_bench.py <output.tsv> --bench BENCHMARK-TX.tsv` (current main, after commit
   6896cf0e7): report standard SER with S/D/I separately, the flagged-excluded figure beside the as-measured one, and for any
   "improvement" claim the paired per-line edit-total test the tool now prints, not a sign-level count. Reader abstention counts as wrong.
4. **Exposure ledger.** Every file you opened, by path, in `EXPOSURE.md` in your folder; every model call's prompt and the crop paths it
   received, in `calls/`. A result without the ledger is not collated.
5. **No truth edits, no key values.** You may not change any truth, flags or build script; propose a correction in the PR text instead.
   Do not pass plaintext values, key tables or glosses to a reader; readers see images and a value-blind sign sheet only.
6. **Reproducible.** Scripts and outputs in your folder; one command regenerates the score. Model names and versions stated.
7. **Deliver as a pull request** titled `[SO-TX-EXP-<id>] <one line>` adding only files under `benchmark-tx/ext/<id>/`, body ending
   "Do not merge" (we copy and close, as with your review). One experiment per PR. Say what was found and where it was not found; do not
   call anything "first" or "solved".

Good first questions, pick one or propose your own: (a) your oracle-location diagnostic's arm B on dev items only, with boxes from our
existing crops' ink components as a stand-in for human boxes, to estimate the effect size before the human step; (b) a line-level CTC or
detection reader (HTRbyMatching checkpoints, your R7) run cold on dint-f89-gloss and vivonne1573-f102r-dev2 against our passZ baselines;
(c) a segmentation-only study: from the fixed scorer's S/D/I, which merges and splits recur across the dev hands, with image evidence.

Start by reading, in this order: research/TX-PROGRAM.md, TRANSCRIPTION.md, BENCHMARK-TX.tsv, tools/tx_bench.py --help, your own
report, research/TX-RED-2026-10-09.md (our adversarial reviewer's open findings F47-F63), research/TX-REGISTER.tsv (what we tried).
