# PREREG -- R12-RJM42, rah-juan-manuel-1521: both letter alphabets held out on R9502 f.40 vs its period decipherment f.42
Written 6 Oct 2026 12:1x UTC; committed and pushed BEFORE `python3 scripts/test42.py` is run for the first time. At this point the
worker has seen the three subagent reports (row counts, ?n descriptions) but not the token contents of passes/f40_A.tsv,
passes/f40_B.tsv or passes/gloss_f42.tsv, and no alignment of f.40.

Material: R9502 (Juan Manuel to Charles V, Rome, 8 Mar 1522), DECODE image P1 right page = f.40 (cipher, 30 crop lines: 1-20 cipher,
21-24 clear, 25-30 cipher), P3 right page = f.42 (the clerk's decipherment, 27 crop lines, heading on L01, "Claro" before L21's text).
Passes: A forward, B reverse, shared inventory passes/inventory.md, Sonnet, crops only; gloss: one Sonnet read of f.42 crops.

Method (scripts/test42.py, fixed now): test 1's reconcile and alignment code unchanged (tools/interlinear_align.py run_align, code
prefix @, symbols take 0-2 letters, word codes %, null cost -1.0, max chunk 10, clear-consumes, prior-free). Cipher lines that are
all-bracketed in pass A are dropped; gloss rows marked `heading` are dropped and a leading "claro" is stripped from any gloss row.
?n normalisation, from each pass's own description only: A ?1 (numeral-7 sign) -> 7; B ?3 (small raised co-like sign) -> R;
B ?4 (small hatched sign after ott) -> T (test 1's f194 B precedent: hatched stroke = T). Every other ?n stays unmapped (not scored).

Gate 0, calibration (checked first; rule-3 control-before-target): share of nomenclator code tokens whose aligned chunk equals their
own table word must be >= 0.50 (in-sample f.194 had 0.65; the failed held-out f.199 had 0.38). Below it, neither key is scored and
the run is logged "non-test at this alignment".

Statistic, per key: S = share of scored symbol tokens whose aligned chunk equals the key's value for that label (null = empty
chunk). Keys: alphabet.tsv (13 labels, top value per sign, from f.194/f.197) and key_tomokiyo_alpha.tsv (firm rows with an
our_label, 12 labels). Control: 200 keys with the same values permuted among the same labels, seeds 1..200 (the alignment is fixed
and the values move, so the control can differ from the target on S). Gate per key (unchanged from witness/gate_alpha.txt):
PASS iff S > control max AND S >= 0.24.

Held-out cleanliness: Tomokiyo prints this letter's first decipherment line ("Esta otra letra se cerro anoche y no pudo").
Scored set = symbol tokens NOT on cipher crop line 1 and whose aligned chunk does not start within the first 32 gloss letters (the
incipit's letters). The excluded tokens are scored separately with the same control and reported, never used for the gate.

A PASS licenses no key, grade or reading change in this job (the brief: no change unless a key passes; any change goes to a verifier
first). A FAIL with gate 0 passed is a held-out FAIL for that key at this transcription error (err_2reader reported beside it).
