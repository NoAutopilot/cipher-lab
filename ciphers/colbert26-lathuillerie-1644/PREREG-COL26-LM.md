# PREREG-COL26-LM (account 4, LANE DEFAULT-A4-0437-15, 15 Oct 2026)

Job COL26-LM, brief `.claude/briefs/runs/2026-10-15-acct4-default-0437-jobs.md`. Pushed before any score.
Third attempt on the 11 = re / 81 = me hypothesis (COL26-KEY, COL26-1181, this); rule 3 third-attempt clause applies.

Instrument, streams, alternative class, gates and verdict rule: the docstring of `siblings/c_lm_len.py` is the full
registration. In short: score(V) vs the 60 commonest fr17 two-letter pairs in V's place, held-out streams, accept
= above the alternatives' p95. Gate G1 on the five two-letter C codes (16 se, 28 la, 33 ux, 36 ez, 51 de): true
>= 4/5 accepted AND planted false (the other four control values per code, 20) >= 18/20 rejected. Gate G2 at each
target's own held-out n (20 subsample draws, seed 0): mean true acceptance >= 0.8, false <= 0.10.

Outcomes:
- G1 fails -> log "untested-by-this-tool" for 11 = re / 81 = me in HYPOTHESES.md (third attempt), score nothing, stop.
- G1 passes, a target's G2 fails -> that target NON-TEST, same log for it.
- Gates pass: accept -> rev_grade S for that code in key_f23_c50rev.tsv (its own control passed, CLAUDE.md MQS
  crossword line); reject -> rev_value kept, rev_grade stays M with "length-matched reject" noted (a single
  instrument's reject is not a drop). key_f23.tsv, decode.json and readings never written.
