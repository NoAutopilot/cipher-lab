# PREREG: commit the 4 f.275r shape-settled T36 labels into tx86e (R12A-PISRS, 6 Oct 2026, written before any edit)

Job: .claude/briefs/runs/2026-10-06-account1-run12-jobs.md "R12A-PISRS" (b). Named by D4-PISRS / RUN6-PIS Remaining gaps ("commit the 4 f.275r T36 labels
(shape and copy both s) into tx86e with the downstream regeneration ... f.244r left M pending the conflict").

Edit (fixed now, not chosen after looking at any score): in the reconciled file tx86e/ciphertext_f275r.tsv only, the four tokens that
pis2/t31_tokens.tsv marks SETTLED-T36 on f275r -- L04 i39, L09 i3, L12 i5, L14 i28 (index over non-'/' tokens, 0-based, as pisrs.py) --
change T31 -> T36. Evidence: R9-PIS2 blind shape compare (medium confidence, my eye agreeing) and the copy's s at these places (RUN5-PIS4 / D4-PISRS).
Not edited: tx86e/passA.tsv, passB.tsv, ciphertext_draft.tsv (raw passes); f.244r (tx86) -- its T36 shape conflicts with the copy's o (rule 4);
the 9 other f.275r T31 tokens (UNSETTLED); key86.tsv.
Mechanism: the pre-edit file is kept byte-identical as tx86e/ciphertext_f275r_preT36.tsv; tx86e/apply_t36.py derives the edited file from it and
pis2/t31_tokens.tsv, asserting each target is T31 and its context matches pis2/tokens_pos.tsv; `--check` exits non-zero if the committed file is stale.
Downstream regeneration: reading_f275r_M.txt / reading_f275r_tokens.tsv by tools/decode_key.py (as RUN5-PIS3's command), `--check` exit 0;
kp86e/t31_grades.py (t31_witness.tsv) and `--grade` (grades_f275r.tsv). Rule 4 grading is the existing kp86e rule unchanged: a T36 token is C only
if its decoded letter aligns identically to the copy, else M. No gate and no score is claimed from this edit (it is not a test); the
supporting scores are D4-PISRS's and R12A-PISRS (a)'s, reported separately. Expected reading change: 4 letters m -> s on f.275r; reported in
NOTES.md and flagged in ROOM.md for a verifier (AUDIT.md predates it).
Scripts that read the pre-edit file for their committed results (kp86e.py, pis1key.py, relabel_f275r.py, pisrs.py) are noted; pisrs.py's input
path points at the _preT36 copy so its committed result stays reproducible.
