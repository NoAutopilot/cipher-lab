# SIG-B228B pre-registration (LANE SIG-1, account 1), written 8 Oct 2026 23:27 UTC by date -u, committed before any tile is cut or read

Target: Baluze 170 f.228v (same letter as f.229, Chavigny to d'Avaux, Amiens 25 Aug 1640). Brief: .claude/briefs/runs/2026-10-08-acct1-sig1-jobs.md "## SIG-B228B".

## u4/4u signs (unit 1)
1. Targets: the four f.228v signs D1-BAL170B settled as s:u4 from an A u4 / B 4u split (d1bal170b/rec_f228v/disagreements.tsv):
   v a_L02 col4, v b_L01 col10, v b_L05 col8 ("la l[?]ngrave"), v b_L06 col6. Currently decoded t (the f.229 u4 value), grade M.
   The f.228r a_L02 ll|u4 vs u4|4u row is NOT a target: SIG-B228 already valued it l (Tomokiyo fragment agrees); it stays.
2. Method: SIG-B228's tile-sheet method (b167228/sig_tiles.py tile() geometry, centres placed by eye on gridded copies, shape location
   only). One unknown sheet: the 4 targets + 3 decoys + 2 anchors, shuffled to blind ids U1..U9 (key held back in key_private2.tsv),
   against the unchanged f.229 exemplar sheet (sheet_f229_exemplars.png: E-a = 4u, E-t = u4 among 11). Two independent blind Sonnet reads.
3. Decoys (known right answer, the gate): three already-valued f.228v tiles of three distinct shapes not used as SIG-B228 decoys at the
   same position: h = n (E-n), y+ = r (E-r), gam = u (E-u). Decoy gate: >= 2 of 3 matched to their right exemplar by BOTH reads.
   If it fails, no target changes.
4. Anchors (reported, not gating): one f.228v sign both D1-BAL170B passes read 4u (v a_L01 col5) and one both read u4 (v b_L04 col1).
   They show whether the readers can separate E-a from E-t on this hand at all; reported beside the targets.
5. Adoption per target tile: both reads name E-a -> value a (4u); both name E-t -> stays t (u4, now exemplar-confirmed);
   anything else -> stays as it is (t, M). Values enter only via b167228/sig2_shape_map.tsv read by to_pipe.py (per-token override), grade M.

## The two v a_L01 71' marks (unit 2)
6. One tight crop per numeral (numeral centred, about one line high), shuffled with 6 control crops to blind ids N1..N8, two blind
   Sonnet reads naming acute / diaeresis / bar / none / unsure. Controls: 4 transcribed with an acute (r b_L02 40',
   v b_L04 90', v b_L02 44', v b_L02 65') and 2 transcribed unmarked that SIG-B228's both reads saw unmarked (v a_L01 16, v b_L02 13).
   Gate: >= 3 of 4 acute controls read acute by both reads AND >= 1 of 2 unmarked controls read none by both. Gate fails -> no change.
7. A 71 mark changes only if both reads agree: both "none" -> the token is transcribed unmarked (71, decoded with the supplied acute
   value, grade I instead of H; the reading word is unchanged); both "acute" -> stays 71' (H); otherwise stays 71' as transcribed.

## Re-judge
8. b167228/judge_null.py run UNCHANGED (fr17, 40 shuffled nulls, seed 20261008, 3-segment f.229 positive control); report beside
   SIG-B228's -0.971 vs real_p05 -0.935. The gate is not moved.
9. ZX-DEC349 check (rule 3): if a period gloss text of the same hand exists on disk (gloss.tsv / survey.tsv / f.229 gloss), score it through
   the same judge spec and report it beside the reading; if none exists, say so.

Caps: USD 3.5, box to 00:17 UTC 9 Oct 2026. Units: 2 tile reads + 2 mark reads + 1 reconciliation, ~USD 0.6 each; stop before a unit crossing 80%.
