# MQS-TX-CROSSWORD result on Birago no.87 (9 Oct 2026, 06:49-06:58 UTC by date -u; LANE MQS-2, account 4)

Pre-registration tools/tests/PREREG-MQS-TX-CROSSWORD.md, pushed at d0de36fe with flag.py, score.py, positions.tsv and the blind
packets **before any crop was shown and before any score**. 2 Sonnet vision calls (G1 59 questions / 48 crops, G2 51 / 39 crops),
1 eye-check unit (me, 5 crops), 0 network requests. Fourth attempt on no.87 (rule 3 third-attempt clause): different instrument
on both ends -- flags from the decipherment (LM gain under the printed key, not reader disagreement) and an open-choice per-sign
re-read against the whole sign sheet (no candidate list, current sign masked), so a value no reader proposed was reachable.

Crop commands (run before the first call; crops in the session scratchpad only; boxes equal the committed manifests after the
region offset):

    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f178r/src_ark_12148_btv1b9060248g_f181_4700_3720_3050_620.jpg --out $S/f178r --prefix f178r --centres 95,215,355 --max-width 1250 --overlap 350 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f179r/src_ark_12148_btv1b9060248g_f183_4800_1000_3000_620.jpg --out $S/f179r --prefix f179r --centres 96,245,380 --max-width 1250 --overlap 375 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f178v/src_ark_12148_btv1b9060248g_f182_1703_848_2900_3452.jpg --out $S/f178v --prefix f178v --distance 95 --prominence 150 --max-width 1250 --overlap 425 --debug

| gate (pre-registered) | result |
|---|---|
| G0 calibration, D decoys answered = current sign >= 0.80 | 30/30 = 1.000 PASS |
| changes proposed (T arm, reader H/M differs AND LM prefers it) | 5 of 60 (reader kept the current sign at 52/60, OTHER/U 1) |
| G3 eye check of every changed sign (eye_check.tsv) | agree 3 (qids 29, 33, 79), disagree 2 (qids 11, 80: upright box on a stem, T49 shape, read T57) -> reverted |
| G1 err_true(applied_T_eye) < 0.045 | 0.045 (36/803, 0.033-0.061) **FAIL** (= base labels.tsv 36/803) |
| G2 paired vs labels.tsv, fixed > broken, p < 0.05 | fixed 1, broken 1, p 1.000 **FAIL** |
| G4 second held-out item | none on disk (only eval item is no.87) -- not met by construction |

Reported, not gated: before the eye check applied_T 0.047 (38/803), fixed 1 broken 3 (the eye check removed both extra breaks);
image-only applied_Timg (6 changes) 0.047, fixed 1 broken 3; null arm R 0 changes, 0/0.

Verdict (pre-registered rule): **FAIL; logged untested-by-this-tool / not supported on no.87** at this reader. Not re-briefed against
no.87. Shelf: weak.

What it says (descriptive, my own (line,pos) join against the truth file, not tx_bench, so approximate): the LM flags do reach
agreed-wrong signs -- about 16 of the 60 T positions sit on a base error, against 0/30 in D and 0/20 in R -- but the open-choice
reader, not shown the current sign, re-read the same shape as the base at 52/60 flags. The limit is now the reader's eye on those
signs, not the lattice: the flagger finds them, the Sonnet reader does not see them differently. Next step (one line, not run):
route the T positions where the LM gain is high and the reader agreed with the base to the owner's sign sorter focus list
(sorter_preflight, blind mode) rather than a fifth machine re-read; the flag list is positions.tsv arm T.
