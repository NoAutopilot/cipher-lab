# PREREG TX-ENGINEER round 3 -- DRAFT (lane, 9 Oct 2026 08:0x UTC by date -u; frozen, with a commit hash named here, before any round-3 read)

Status: DRAFT while TXE-L, TXE-M, TXE-N, TXE-O are live. The fixed parts below do not change; the "instruments combined" list
is completed from the Results log of research/TX-IDEAS-2026-10-09.md when the last round-2 worker reports, and the file is
then marked FROZEN with the commit hash. No round-3 read is made before that line exists.

## What round 2 established (Results log, 12 instruments by 08:00 UTC)
Moved: crop geometry (M2: `iiif_lines.py --band-extent 0.1 --mask-neighbours`, `--follow-slope` on the sloping line,
`--overlap-note` for the brief; geo unit pooled 27/8 p 0.0019, correlated reads; the gain is the f178r L03 tail, the band-cut
lines unmoved). Failed, retired for this hand: compare-don't-recall and its variants (M1, M1b), thin pair re-read (M3),
confusion-matrix lattice (M5), rendering sweep (O1 O2 M4; the 4x read D2), Sauvola/CLAHE/SWN (O5), per-cut gate (O3), pair
hints (M17), contrast sweep (O6), jitter prior (M11), adjudication by Fable or Opus (M19: a non-test for gain, 1 of 14
errors on split items). Non-test: colour (O4; greyscale sources). Pending: M7 shuffled order (L), M24 feature-first (M),
M20 shifted crop set (N), the doubt detector (O).

## The combined pipeline (fixed)
1. Crops: `iiif_lines.py --image <src> --band-extent 0.1 --mask-neighbours --max-width 1250 --overlap 425 --overlap-note
   [--follow-slope WIN --only-lines N for any line whose --check-boxes report or debug overlay shows a slope]`; the
   generated crops_note.md replaces the brief's typed overlap sentence. Nothing else from the rendering family (D, D2, G
   failed).
2. Two blind passes, Opus 5.5 subagents, the unchanged `blind_pass_brief_1572.md` + `sign_sheet_blind_1572.png` + crops_note,
   pass-A call grouping; plus any pending instrument whose dev gate passes (M, N) as the brief or crop variant it defines.
3. `tools/reconcile_passes.py` on the two passes; disagreements and uncertain.tsv settled by the Sonnet third-reader protocol
   of the folder (TXE-K showed a stronger adjudicator does not help), then the NO87-LABELS relabel map (a key-family
   decision, not a no.87 read) applied as today's L applies it.
4. The doubt detector (TXE-O's chosen combination, if it meets its gate) lists the positions still doubtful -> the sorter's
   focus.tsv with the taxonomy's question per tile (TRANSCRIPTION.md item 7); the pipeline's reading is reported WITH the
   number of doubtful positions, never resolved by the lane.

## The single eval look (fixed)
Unit: eval_heldout (f178v L13-23 + f179r L01-03, 376 scored; no sloped line there, so the crop step's predicted gain is
small -- stated now). Output `benchmark-tx/outputs/birago1572-no87/passZ_pipeline_eval_heldout.tsv`, scored once:
`tools/tx_bench.py ... --paired benchmark-tx/txeng/units/labels_eval_heldout.tsv` (L, today's 0.040 there) and
`--paired passA_eval_heldout.tsv`. Gate: fixed > broken, p < 0.05 (Amendment 2, combined pipeline). This look is counted in
the register ("Eval looks taken: 1 (pipeline)"). The whole-no.87 figure against TRANSCRIPTION.md's 0.045 is reported as the
union of the geo reads (f178r, already taken) + eval_heldout (this look) + the dev_tune lines (re-read by the pipeline too,
as a dev number), with the three parts named, never as a single new held-out number.

## The confirm item (fixed; Amendment 2 guard 2)
`spinelli-c1519-confirm` (BENCHMARK-TX.tsv row, split=confirm, built by TX-CONFIRM-SET on account 1, commit 74934b71; a
different hand, 259 signs). The lane and its workers have not opened it and do not until this step. The pipeline above is
run on its crops exactly as on no.87 (its own sheet and brief from its folder), scored ONCE with tx_bench --item
spinelli-c1519-confirm, paired against the folder's existing best read if one exists in the outputs, else err_true alone.
That number is the campaign's headline beside no.87's; it is reported whatever it is.

## The live letter (fixed; Amendment 2 guard 3)
fr.3252 f.117r (ciphers/birago-fr3252-1571-72/images/f117, 11 reader-split M tokens, the most of f.117/f.144/f.168): the
pipeline's crops and two passes, reconcile, decode with the folder's key under its own PREREG and power control
(`family_run.py` / `key_decode_lattice.py` as the folder's NOTES prescribe), `prior_work.py` step first; reported as "the
key now licenses N more tokens at grade S" (or not), then a verifier session audits it. No grade above S from this lane.

## Costs
Pipeline on eval_heldout: 2 passes x 2 calls + reconciliation 1-2 calls = about 6 Opus calls (~9); confirm item: about 6
(~9); live letter: about 8 (~12) + verifier (~6). Round-3 total about 40 of the lane's remaining window.
