# SIG-B228 pre-registration (LANE SIG-1, account 1), written 8 Oct 2026 22:52 UTC by date -u, committed before any f.228 tile is cut or read

Target: Baluze 170 f.228r-v (same letter as f.229, Chavigny to d'Avaux, Amiens 25 Aug 1640). Brief: .claude/briefs/runs/2026-10-08-acct1-sig1-jobs.md "## SIG-B228".

## Shape values (gaps: q 6, ll 4, g+ 3, ff_crossed 2, ll|u4 1, v 1, wave 1 = 18 U tokens)
1. A shape gets a letter value ONLY from an external exemplar: (a) Tomokiyo's letter block, images/louisxiii_davaux.png, or
   (b) a glossed f.229 occurrence, i.e. a shape class already valued in passes/reconciled_b170f229{r,v}.tsv (crops on disk).
   Never from f.228's own context (ARM-C1 shape; B167-228's refusal of q = c on context stands as the rule).
2. Procedure: one tile sheet per shape group (f.228 tiles of the unvalued shapes + 3 decoy tiles of already-valued f.229 shapes,
   all unlabelled and shuffled) plus one exemplar sheet (Tomokiyo letter block + labelled f.229 shape tiles). Two independent blind
   Sonnet subagent reads per sheet pair; each read names, per tile, the best exemplar label or NONE.
3. Adoption gate per shape: both reads name the SAME exemplar for a majority of that shape's tiles (for a 1-token shape: the one tile).
   Otherwise the shape stays U.
4. Decoy gate (the control; it can fail differently from the target because decoy tiles have a known right answer): across the
   decoy tiles (hook s, gam u, y+ r, three distinct already-valued f.229 shapes), >= 2 of 3 must be matched to their right
   exemplar by BOTH reads. If the decoy gate fails, NO shape value is adopted, whatever rule 3 says.
5. Adopted values enter only through b167228/to_pipe.py (an external-exemplar map, grade M like every letter sign); no hand edit of a reading.

## Unmarked numerals (27 tokens read with a supplied acute, grade I)
6. Each of the 27 unmarked numeral tokens is re-checked for a mark on the native line crops by two blind Sonnet reads (mark: acute ',
   diaeresis :, bar =, none). A token's mark changes only where both reads agree on a mark AND it differs from "none"; a token
   both reads see unmarked keeps grade I with the supplied acute; disagreement keeps the status quo.
   A numeral both reads see with an acute is regraded H (the key's acute row). Control: 4 already-marked (H) f.228 numerals
   are mixed in unlabelled; if fewer than 3 of 4 are read with their transcribed mark by both reads, no regrade is adopted.

## Re-judge
7. b167228/judge_null.py run UNCHANGED (fr17, same 40 shuffled nulls, seed 20261008, same 3-segment f.229 positive control).
   Report beside B167-228's -0.993 vs real_p05 -0.887. PASS/FAIL as the script prints; the gate is not moved.
8. External check (not a gate): Tomokiyo's fragment "sont mal satisfaits de" (louisxiii.htm l.361) against f.228r a_L02.

Caps: USD 6, box to 00:20 UTC 9 Oct 2026. Units ~9 subagent calls at ~USD 0.6 + 1 reconciliation; stop before a unit crossing 80%.
