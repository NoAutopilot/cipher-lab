# H66 pre-registration (DEB-RUN, account 4, 7 Oct 2026 21:4x UTC by date -u; committed before any real-c2 run)

Hypothesis: c2 is a homophonic letter text padded with nulls written in their own sign types (disjoint from the
text's signs), a design DEB-SWARM-D's NULLS-q route (nulls drawn from the text's own curve) did not test.
Instrument: `h66_null_types.py` greedy backward elimination of sign types (count >= 3) maximising
S = z(mi1)+z(bg2)+z(rep3) vs 24 within-line shuffles, dropped share <= 0.65; S_max over the path.
Matched control: FR homophonic letters at c2's line lengths and sign curve, disjoint null types at share q in
{0.35, 0.50}, 15 pct type noise (c2's measured floor 14-18 pct); seeds 1-10 per q.
Search-null: the same greedy on within-line shuffles (controls: seeds 1-10 per q; real c2: seeds 1-20).
Gates, fixed now:
- Control at q passes when control S_max > 95th pct of its own q search-null in >= 8 of 10 seeds.
- Real c2 is scored only against a q whose control passed. Real S_max (median of 3 seeds) > 95th pct of the 20
  real search-null runs -> lead (next: inspect the dropped types, then a solver on the reduced text with the
  same control); otherwise fail for this design at this N and noise.
- If no q passes its control: non-test, logged as 'no passable control at c2 N with this instrument'.
