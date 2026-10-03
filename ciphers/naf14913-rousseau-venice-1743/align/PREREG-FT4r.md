# FT4r pre-registration (account-4, 3 Oct 2026, written ~12:25 UTC by the clock, pushed before any registered score)

Pair: numerals f.266r (`ciphertext_f266r.txt`, 171 groups, first readings of the a|b alternatives, 98 distinct codes, one 722 at
group 49, "180 722 180") <-> slip f.265r (`slip_f265r.txt`, the expanded line fixed by FT4q at grade I, 493 letters).
Instrument: `align/ft4r_pair.py` = the FT4l one-edit model and gate (PREREG-FT4i.md + amendment FT4l: MAXLEN 12, every
repeated code one identical chunk, free groups 1..12 letters, <= 1 edit (W release / D dropped group), E by decomposition per
edit class, sublimit 10 s, Pool(4), early exit on a fit), with the single 722 occurrence pinned to chunk X (ft4q_poly.solve_pinned,
the FT4q part-2 model: the pinned group is never released or dropped). No other pins (the f.206 C values are not imposed, as FT4l).
Run once with X = 'i' and once with X = 'ti'. Nothing else differs between the two runs.

- Statistic per X: E_real(X) in {1, 0, unresolved}.
- Controls per X (can vary on E's axis: E depends on both sides' order), as one_edit_seg.draws: seed 3, n 40, (s) slip words
  shuffled / real groups, (g) group order shuffled / real slip; the pin moves with the 722 token. Unresolved counted E = 1 (high).
- Gate per X (unchanged from FT4l): PASS iff E_real(X) = 1 AND each control's E=1 share <= 0.05 (<= 2 of 40).
  E_real(X) = 1 with a share > 0.05 from resolved fits > 2: NON-INFORMATIVE (one edit fits wrong pairings);
  from unresolved draws only: NON-INFORMATIVE (power). E_real(X) = 0 (every class proved infeasible): FAIL for X under the
  one-edit model -- needs no control (a proof, not a score), but it is a fact about this pair with this slip expansion, not a
  negative for the f.206 key. E_real(X) unresolved: NOT SCORED for X.
- Sizing done before this commit, on an UNREGISTERED draw only (seed 99, (g), X = ti): unresolved at 63 s wall. So 160 control
  draws are about 2.5-3 h; they do not fit this 45-min box. Run order therefore: (1) REAL X = ti, (2) REAL X = i (no controls
  yet); (3) controls only for an X with E_real(X) = 1, (s) then (g), in blocks of 5 draws, each block committed and pushed.
  Stop before a block that would cross 80 pct of the box (box 12:22-13:07 UTC; line 12:58). A control not completed to n 40 is
  reported as NOT SCORED with its draw count, never as a partial gate; the remaining blocks are the next step.

What each outcome means for the 722 polyvalence question (f.206 needs 722 = ti at two occurrences, grade C; f.213 minus group 73
fits only with 722 = i, FT4q part 1; f.249 cannot decide):
- O1  E_real(i) = 1, E_real(ti) = 0: this pair, like f.213, admits i and excludes ti within one edit. Two independent passages
  against f.206: 722 is then best described as polyvalent (ti / i), or the f.206 segmentation at 722 is the thing to re-check.
  If the i controls later PASS, an independent pair supports 722 = i: a result for a separate verifier (rule 4 data conflict
  stays logged with the witnesses; no majority settlement).
- O2  E_real(ti) = 1, E_real(i) = 0: this pair sides with f.206; f.213's i is then isolated (its extra-368 edit region is the
  place to look). Same verifier note if the ti controls PASS.
- O3  both 1: this pair does not decide 722 at this model's resolution; with controls it can still PASS as a pair (pairing I ->
  a control-backed slip/cipher match), which says nothing on 722.
- O4  both 0: the pair needs >= 2 edits (or the slip is a paraphrase / the expansion is off) under either value; no 722 info.
- Any unresolved real: not scored for that value; next step is a different instrument, not a longer timeout (rule 3, FT4j).
- Key rule: nothing enters or moves in key.tsv this step whatever the result; a PASS goes to a separate verifier, and any later
  key change goes through decode_key.py --check.
