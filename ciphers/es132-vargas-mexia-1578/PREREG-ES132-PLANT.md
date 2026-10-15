# PREREG-ES132-PLANT (15 Oct 2026, ES132-PLANT, LANE DEFAULT-A1-1140-15 account 1), written and pushed before any re-read call
Question: is the ES132-LOOK re-read's preference for reader A on f.51v L11-L25 (95 of 105 tiles) reading or echo? ES132-AUDIT (9 Oct) ran the
label-showing prompt with 9 plants (7/9 = 0.778, NON-TEST) and could not speak to the hide-passc re-read. This run uses the hide-passc prompt,
the mode the ES132-LOOK re-read used (tile's own label never shown), with enough plants for the gate to bite.
Instrument: `tools/lookalike_pass.py audit --hide-passc`, inputs `lookalike/audit/f51v_pass{A,B,C}.tsv` (ES132-AUDIT's make_inputs.py, unchanged),
confusion `lookalike/confusion.tsv`, `--lines 'L(1[1-9]|2[0-5])' --sample 90 --plant 0.30 --seed 15102026 --k 3`, committed RUN5-ES51 half-line crops
`images/f51v_L??_s?.jpg` (30 crops), empty sheet + the notation legend (as ES132-AUDIT). Dry run: 200 agreed signs in the pool, 90 items, 27 planted.
In hide mode a plant is an item whose candidate set is built around its top confusion partner (the partner, the partner's partner, and the original);
the reader sees no label at any audited position. One value-blind Sonnet vision call (f51v_p). f.52r not run: one call is what the 2.5 cap allows.
Statistic and gate (the tool's own `audit-score`, unchanged): planted catch = conf H/M AND label == original; pooled over the 27 plants, gate >= 0.80,
i.e. >= 22 of 27. Also reported, no gate: agreement with the original on the 63 unplanted (real) tiles at H/M, and flags on them.
Rule: PASS = this re-read instrument picks the A=B=C-agreed shape against its top look-alike on f.51v at >= 0.80, so the 95/105 A preference is
"consistent with reading at the look-alike level" -- still not told apart from correlated readers on the disputed tiles themselves (agreed tiles are
easier). FAIL = the A preference stays "not told apart from an echo" and the hide-passc re-read is not licensed for settling f.51v.
Either way: no change to key.tsv, grades, the committed reading, passD, focus.tsv or any earlier PREREG; this tests an instrument, not tokens.
Caveat fixed now: the truth is the agreement of two passes and the committed reading, not an image check.

## Addendum f.52r (15 Oct 2026, ES132-P52, LANE DEFAULT-A1-1140-15 account 1), written and pushed before the f.52r re-read call
Same question, instrument, statistic, gate, rule and "either way" clause as above, applied to f.52r L01-L21 (L22 is the clear dating line). Nothing above
is changed by this addendum; the f.51v PASS (26/27, 147bf0785) is not re-scored.
Instrument: `tools/lookalike_pass.py audit --hide-passc`, inputs `lookalike/audit/f52r_pass{A,B,C}.tsv` (ES132-AUDIT's make_inputs.py, unchanged), confusion
`lookalike/confusion.tsv`, `--lines 'L(0[1-9]|1[0-9]|2[01])' --sample 90 --plant 0.30 --seed 15102026 --k 3`, committed RUN5-ES51 half-line crops
`images/f52r_L??_s?.jpg` (42 crops, 21 lines). Dry run (disk only): 400 signs, 293 agreed in the pool, 90 items, 27 planted, 0 forced. Files
`lookalike/plant/f52r_p_audit_{items.tsv,prompt.md}` committed with this addendum; the prompt carries the same two edits as f51v_p (halves, not thirds;
the notation legend + "no candidate sheet" line in place of the empty sheet), diff against f51v_p_audit_prompt.md = the crop list and the item lines only.
One value-blind Sonnet vision call (f52r_p), no retry unless the call returns no parseable TSV (then one retry, logged).
Statistic and gate (unchanged `audit-score`): planted catch = conf H/M AND label == original, over the 27 plants; gate >= 0.80, i.e. >= 22 of 27.
Also reported, no gate: agreement with the original on the 63 unplanted tiles at H/M, and flags on them; and the pooled f.51v+f.52r catch (descriptive only).
Rule: PASS = the hide-passc re-read picks the A=B=C-agreed shape against its top look-alike on f.52r at >= 0.80, so the ES132-LOOK f.52r re-read
(150 A / 27 B / 9 other) is "consistent with reading at the look-alike level"; still not told apart from correlated readers on the disputed tiles
themselves. FAIL = the f.52r re-read stays "not told apart from an echo" and is not licensed for settling f.52r.
Either way: no change to key.tsv, grades, the committed reading, passD, focus.tsv or any earlier PREREG.
