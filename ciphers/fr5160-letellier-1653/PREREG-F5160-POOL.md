# PREREG-F5160-POOL: pooled 1653-band nomenclator control (9 Oct 2026, written 13:5x UTC by date -u, before any score)

Worker F5160-POOL (account 4, Opus), LANE DEFAULT-account-4-20261009-1340, job J1. Second attempt of the same instrument
(tools/nomenclator_anneal.py) on the 1653 table; the first (24 Sept 2026, NOTES "1653 band: constrained solve") read the
752-token control at 25.7% against a ~60% bar. The one knob changed is N: all four 1653 pieces pooled.

**Inputs** (`pool_inputs.py --check`): pattern `real_pool.txt` = f1 + f9 + c11 + c32, 972 cipher tokens, 134 types, 40
singletons, top-8 shares 7.8 5.9 4.9 4.7 3.9 3.7 3.5 3.5 %. Control `control_pool.txt` / `control_pool.truth.json`:
`synth control_pool_plain.txt --design control_1653_design.json --pattern real_pool.txt --seed 1653` (the 24 Sept design
unchanged), 972 tokens, 120 types, 21 singletons, top-8 7.7 5.5 4.6 3.7 3.3 3.1 3.0 3.0 %. Plaintext = the 24 Sept control
plaintext unchanged + f.68r clear text (this volume) + Marguerite de Valois letter XIX (25 Apr 1581). Model: tools/data/fr16
with every paragraph containing a control sentence removed (`FR_MODEL_DIR=... pool_inputs.py --model`), not committed.

**Solver settings, identical to the 24 Sept best schedule (t5)**: `solve --context clear --syl cv --extra-syl
"$(cat control_1653_syl.txt)" --words "<the design's 16 word values>" --max-syl 100 --max-word 16 --max-null 3
--max-homo 4 --p-syl 0.45 --T0 2 --T1 0.02 --iters 10000000 --restarts 4 --seed 7`, fixes S8=de S91=ques S32=le S43=se
(the control's true signs for the four values the real run would seed from key_1659). If the measured speed makes 10M x 4
impossible inside the box, iterations are cut and the cut is reported; the gate is not moved.

**Gate (control)**: token accuracy (`nomenclator_anneal.py eval`) of the **highest-scoring** restart >= **0.60**. Also
reported: max token accuracy over restarts, letter accuracy, best score vs the true key's score under the same model.
- PASS -> run the target `real_pool.txt` with the same settings, fixes = key_1659's signs for de/ques/le/se where the 1653
  pieces carry them; any output is a candidate only (rule 4 grades S at most, rule 7 judge before any reading is reported).
- FAIL -> no target run. Logged in HYPOTHESES.md as the second attempt of nomenclator_anneal.py on this table (rule 3
  third-attempt clause: one more failure without every number moving together retires the instrument); next step named:
  a word-level (dictionary-constrained) solver between the clear frames with its own matched control.
