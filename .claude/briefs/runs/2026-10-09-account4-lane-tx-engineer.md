# LANE TX-ENGINEER (campaign; owner's decision 9 Oct 2026 06:4x UTC): a Fable lane that engineers the transcription pipeline

Written by orchestrator (account-4) session_013CM4Sw1JBAhc5a2KspaERr. Lane orchestrator model: Fable (`claude-fable-5-1`);
workers Fable or Opus 5.5 (never below; Sonnet only where the thing measured IS the Sonnet reader, and the Sonnet numbers are
already on file). Cap 60 of usage for the lane, box 600 min, three gated rounds. Address every ROOM line "for orchestrator
(account-4)". Lane rules: `.claude/briefs/parent.md` "Keep slots full", `.claude/briefs/README.md` common tail,
`.claude/briefs/transcription.md`, `TRANSCRIPTION.md` (the standard), CLAUDE.md Usage 6 (crop step mandatory and pasted, one
page per subagent call, price per pass, reconciliation is a priced unit) and rule 3 (controls; a gate is pre-registered before
any score). Keep a "LANE TX-ENGINEER handoff" section in STATUS.md current from the first result.

## The owner's question, in his words made precise
Transcription is the bottleneck (TRANSCRIPTION.md "Why"). He asks: point a Fable session at the items whose signs are known
precisely, iterate, build tools, think outside the box, and find what an AI working inside Claude Code can do to raise
per-sign accuracy. The decisive fact already on file: a plain model swap is NOT it -- TX-FABLE (4 Oct 2026,
benchmark-tx/txfable/RESULTS.md, LEDGER 34.03 N) read every BENCHMARK-TX item WORSE with Fable than with Sonnet under the same
crops, sheet and prompt (no.87 0.093 vs 0.069, p 0.025; dev 0 of 4 lower). So this lane does not re-run that test. It changes
the protocol, the inputs and the tools, and measures each change on the held-out set.

## Ground truth and measurement (fixed)
BENCHMARK-TX.tsv (eval: birago1572-no87, 803 scored signs; dev: dint-f128-print, ceppo-f21v-S, ceppo-f87-S, ceppo-f36v-gloss) scored
by `tools/tx_bench.py` (err_true with CI, `--paired` fixed/broken + exact sign test). Tune on dev, report on eval; a round's gate
is written in benchmark-tx/PREREG-txeng-<round>.md and pushed BEFORE any read or score; readers never see truth, decodes or other
passes. Never edit a *.truth.tsv. Today's lines to beat: single Sonnet pass A 0.069 (0.053-0.088), reconciled 0.053, reconciled +
relabels 0.045 on no.87; dint single pass 0.188-0.247 mapped. A third hand is added if one exists on disk with a published or
period key, H/C-graded tokens, a symbol (not digit) cipher and two raw reader passes (prior_work.py + the folder's NOTES decide;
candidates to check first: fr2980-gramont f.29r, lodewijk WVO letters are digits so no, Birago fr.3252 f.117); if none, say so.

## Round 1 (cap 10): error taxonomy, no reads
From the error lists already on disk (benchmark-tx/outputs/*, tx-views-2026-10-04.md, agreeaudit_no87_include.tsv, txfable/raw):
one table per item of every wrong sign by (true, read) pair, position in line (first/last/inner), crop edge (within 5% of the
crop border or not), glued pair, stroke-weight class, and whether pass A, B, the five views and Fable all made the same error
(correlated) or not. Output research/TX-TAXONOMY-2026-10-09.md with the three error classes that carry the most mass per hand, and
for each the mechanism you believe (cut-off tail, look-alike pair, inventory split, fatigue by call position). This round
decides what rounds 2-3 build. ROOM line with the top three classes.

## Round 2 (cap 25): build and test two or three instruments, each a tool in tools/ with --help and an offline test
Pick from this list and your own ideas, by the taxonomy's mass, pre-register each on dev, report on eval:
- Compare, don't recall: per-sign tiles presented beside the atlas's nearest exemplars (glyph_atlas.py top-3) so the reader
  picks among shown candidates ("which of these three, or none") instead of naming a sign from memory. The lattice decode
  (tools/key_decode_lattice.py) then resolves with the key. Line reads are 0.040 where atlas top-1 alone is 0.162; the
  combination has never been scored.
- Crop geometry: overlap tails (the f.178r L03 class), adaptive line bands by ink profile, a second crop set that shifts
  boundaries half a line, read only where the two crop sets disagree.
- Targeted re-read: a second look ONLY at the look-alike pairs the taxonomy names, shown as a pair of exemplar rows, with the
  question "is this A or B" -- not a whole re-pass (TX-VIEWS showed whole re-passes repeat A's errors, phi 0.71-0.76).
- Image preprocessing measured, not assumed: binarisation, deskew, stroke-width normalisation, 2x/4x upscaling, contrast on
  faint ink; each as a flag on tools/iiif_lines.py or a new tools/tx_prep.py, scored on dev.
- Re-render check: draw the transcription back as exemplar tiles in line order and ask a fresh reader whether the drawn line
  matches the image line, flagging positions; the flags go to the sorter's "Check these first" box (TRANSCRIPTION.md item 7).
- Sequence constraints: bigram plausibility of the decoded values under the folder's key and corpus as a per-position
  confidence, merged into the lattice (grade S, never H).
- Position effects: if the taxonomy shows errors rising with call position, cap signs per call and interleave hands.
Fable as a reader is tried again ONLY under a changed protocol (compare-don't-recall or targeted re-read), as one arm beside Opus,
never as a plain re-pass. Each instrument's result: err_true on dev with CI, then eval once, with `--paired` vs the current
reconciled read; a gain is a gain only on eval. A shelf row in tools/data/tool_shelf.tsv (proven / controlled-only / weak /
untested) and a SYSTEM.md row for every tool (system_map_check.py must pass).

## Round 3 (cap 20): combine and re-score, then the sorter
Combine the instruments that moved eval into the standard pipeline (TRANSCRIPTION.md "Pipeline"), score the whole pipeline on
eval against today's 0.045 (reconciled + relabels), and feed what still splits to the owner's sorter through focus.tsv with the
taxonomy's question per tile. Update TRANSCRIPTION.md's "Today" column only when the held-out figure improves. Third-attempt
clause (rule 3): an instrument that fails its own gate three times with every fix is retired, named, not re-run.

## Stop and report
Stop at the cap, at 80% of the box, or when three consecutive instruments move eval by nothing. Final: STATUS.md handoff with the
table instrument | dev err_true | eval err_true | paired fixed/broken p | verdict; RESULTS in research/TX-ENGINEER-2026-10-09.md;
one plain-language paragraph for the owner (what moved the needle, what did not, what he should do at the sorter). Ledger every
worker (cost from get_session), archive each; never AskUserQuestion; never print credentials.

## Amendment 1 (owner, 9 Oct 2026 06:5x UTC): test everything that could give an edge; list twenty ideas and go after them
The owner widened the mandate: every idea that seems possible gets a pre-registered test; the lane may use the whole of account
4's usage window on this (cap raised to 150; the only stop is the window itself -- five_hour `allowed_warning` past one check-in
or `rejected` pauses spawning until the reset, BUDGETS.md). Round 1 now ends with an IDEAS register,
research/TX-IDEAS-2026-10-09.md: at least twenty ideas, each with the mechanism it attacks (from the taxonomy), the cheapest test
(dev item, cost, gate), and an order by expected gain per cost; the lane works down the list, one PREREG per idea, and marks each
tested / moved eval / did not move / retired. The owner's own ideas go on the list first, each as a tool with a flag and a test:
1. Delete white space: tight per-sign and per-line crops with margins measured in ink, not pixels (tools/iiif_lines.py or
   tools/tx_prep.py flag), scored against today's crops.
2. Darkening: gamma / contrast / stroke thickening on faint ink, measured per setting, never assumed.
3. Cut symbols, then a quality gate per cut: a classifier (ink mass, aspect, component count, edge contact) that labels a tile
   good / bad crop / two signs joined / blot or noise before any reader sees it; the joined and bad-crop tiles are re-cut, the
   blots dropped with the decision logged; gate measured on the benchmark truth (which tiles it flags are in fact wrong reads).
4. Alter the colours: per-channel and false-colour renderings (red channel to drop iron-gall bleed-through, ink-paper
   separation, inverted), each scored as its own reading arm.
5. What expert document-recovery teams do: a short literature pass (forensic document examination, digital palaeography and
   document image analysis practice -- binarisation families, multispectral and pseudo-multispectral tricks on RGB scans,
   super-resolution, bleed-through removal, HTR pipelines such as Transkribus and eScriptorium, ICDAR competition methods);
   write research/TX-RECOVERY-PRACTICE-2026-10-09.md naming the three methods applicable to an RGB scan in Claude Code, then
   test them; sources cited, nothing copied from an unlicensed repository.
6. Contrast sweep before cutting: for an uncertain sign, render the tile at five contrast levels and let a reader (or a script
   on component stability) watch which strokes persist and which appear, cut and label from the stable strokes, and log the
   sweep as the evidence for the cut.
7. Symbol library across targets: an atlas of clean exemplars of every sign from every target in the same key family and from
   published sign tables (Tomokiyo's and the period keys on disk), so a poor tile is matched to a clean high-resolution
   exemplar of the same sign and the reader sees the pair ("compare, don't recall" generalised across targets).
8. High-resolution alternatives from the time: for a damaged or low-resolution leaf, find another leaf in the same hand and key
   with a better image (siblings, the same scribe's other letters, a contemporary copy) and use its exemplars as the reference
   sheet, or read the sibling where it carries the same word; prior_work.py and the folder's SIBLINGS rows first.
Add your own to reach twenty and beyond (examples the lane may take or discard: stroke-width normalisation, deskew and
line-straightening, super-resolution 2x/4x, reading at two scales and reconciling, sign-level majority over small crop
perturbations, a confusion matrix learnt from the benchmark that re-weights the lattice, per-scribe fatigue and call-position
caps, a second reader that sees only the first reader's doubtful tiles, reading the line backwards, a "same sign elsewhere on the
page" retrieval that shows every other occurrence of the candidate sign, ink-density profiles to split glued pairs, page-level
deskew from ruling lines). Every result, including every negative, goes in the IDEAS register with its numbers; TRANSCRIPTION.md's
"Today" column moves only on a held-out gain. The lane's other duty: tell the orchestrator at each check-in which idea is
running, which moved eval, and the running cost against the window.
