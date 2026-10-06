# PREREG R15-OLDUV -- u/v notation pass on blocks B/C1 (step (n)), 6 Oct 2026

Written and pushed before any score is computed. Brief: .claude/briefs/runs/2026-10-06-account2-run15-jobs.md, job R15-OLDUV.

1. **Naming rule (the reading).** In blocks B and C1 the open u/v cup shape is one cipher sign. It is written as sign `2`
   (digit key 2 -> u) in every B/C1 token. The four B tokens whose committed raw_token names it as a letter `v` are renamed
   through overrides.tsv (ciphertext.tsv stays as transcribed): B37 `bv8n4s` -> `b28n4s`; B49 and B76 `4tr8v8n` -> `4tr828n`;
   B55 `v8r4s,` -> `28r4s,`. Grades are not changed by this step (B37 stays M; B49/B55/B76 keep their default S). The
   reading therefore writes `u` for this shape everywhere in B/C1 (period orthography; the cipher does not distinguish u
   from v). Blocks A and C2 are not touched (they wait on the owner's sorter, step (a'')).
   Known side fact, not changed here: scripts/apply_key.py's docstring says letter v folds to u, but decode_token applies
   fold() only to digit characters, so a raw letter v passes through unchanged. Fixing the function would also change A/C2.
2. **Judge normalisation.** The es1600 corpus (CODOIN printings) spells u/v the modern way (verdad 283 vs uerdad 4, servir
   520 vs seruir 0); the reading keeps period u for consonantal v (uer, ueces, seruir, uerdad). Per CLAUDE.md rule 3
   (PX-BRODEC: normalize both renderings to one convention before a gate), the re-judge folds v -> u in every text the
   judge sees: the four target windows, the corpus model and its word list, the held-out real windows, the null samples,
   and the shuffled-decode controls. Implemented as a `--uv-fold` option of scripts/segment_judge.py that extends
   tools/judge_plaintext.FOLD with v->u for that run only (default off, so the R13/R14 logs still reproduce).
   Consequence stated in advance: under this fold the item-1 renaming changes nothing the judge sees, so any score
   movement comes from the fold, not from the renaming.
3. **Windows, controls, gate (unchanged from PREREG_R13-OLDSEG / R14-OLDF2).** Same four token-boundary windows, es1600,
   400 control samples, 200 held-out windows per fold, shuffled-decode seeds 1-3, min word cover 0.5. PASS/FAIL is the
   judge's own per-window verdict (score >= real_p05); no threshold is changed. Each window is reported beside its
   R14-OLDF2 score. The controls can move under the fold (held-out real windows and shuffled decodes are folded too), so
   the comparison is not identical by construction.
4. **Reading of the result.** If a window flips FAIL -> PASS under the fold while its held-out real-prose controls stay
   at or near their R14-OLDF2 level, the R14-OLDF2 FAIL in that window is logged as partly a notation gap, not a key
   negative. If all four still FAIL, the notation gap is ruled out as the cause of the FAIL at this N. Either way no
   status changes from this step alone (stays open).
