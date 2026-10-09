# PREREG-MANT-0176 (MANT-0176, 9 Oct 2026, LANE FAMILY-A2h account 2; written and pushed in its own commit BEFORE the leaf is fetched, any pass read or any score computed)

Leaf: HStA Dresden 10026 Loc. 694/08, file 0176 (stamp 135, "Berl. 2 Juil 1712" per MANT-INV08B, eye estimate 30-40 tokens in the right page's lower
third, unglossed at 1600 px). URL from mant0608/fetch_b.tsv (.../3a83f921-9a43-485f-874b-34653ed59b68/fullsize/0176.jpg); at most 2 GETs (0176, and
0175 only if 0176 lacks the letter's head/date). Key: key.tsv at origin/main as of this commit, unchanged by this job.

Design = PREREG-MANT-0109 (f0109_08/), itself PREREG-MANT-0454's design; scripts copied into f0176_08/ with the leaf id changed (f0109_08/ and
f0454_08/ not edited). No other change: same crops rule, same two blind Sonnet passes (A crop order, B reversed; crop paths only; readers report
every number with its neighbouring clear words and any interlinear/sub-linear letters), same worker reconciliation unit -> f0176_08/ciphertext.tsv.

Gate (a): only if a pass or the worker's look finds interlinear letters on a run; exactly as PREREG-MANT-0109. Else n/a.
Name-abbreviation rule: as PREREG-MANT-0109 (maximal run of exactly 2-3 codes recurring as a whole run >= 3 times leaves the stream, graded M).
Gate (b) (f0176_08/judge_gate.py = f0109_08/judge_gate.py with F/leaf id changed): letter values of key.tsv's letter codes (first alternative,
1-3 letters), word/name codes and codes absent from key.tsv dropped; tools/judge_plaintext.py NgramModel, corpus fr18; control = letter values
permuted among key.tsv's letter-valued codes, same token sequence. L <= 52: scored whole vs 1000 permuted keys, seed 176 (the one change from
0109: the seed, fixed here); L > 52: consecutive 52-letter blocks, seed 176+k, tail reported only. Power at the scored length from the
positive-control streams (694/09 0085 runs 9+10; 694/09 0136 unglossed), 200 permuted (seed 7) per window, pass if real > 190th of 200;
gate (b) is a TEST only if power >= 0.80, else "too-short" (neither PASS nor negative; every unglossed letter token M). Block PASS = real >
p95 (p99 reported). Leaf PASS / MIXED / FAIL as PREREG-MANT-0109. L < 4: too-short, unscored.
Grades: f0176_08/grade_0176.py = f0109_08/grade_0109.py (S only for unglossed letter tokens in a PASSing block with power; name/word codes M;
abbreviation groups M; low-conf M; not in key U). No key.tsv change; candidates as rule-4 slots in HYPOTHESES.md.
Decode: tools/decode_key.py f0176_08 (decode.json as f0454_08's), --check. Check 5: tools/print_check.py on decoded and clear phrases.
