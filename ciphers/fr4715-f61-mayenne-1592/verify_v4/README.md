# verify_v4 -- VERIFY-F61-V4 working files (verifier, 28 Sept 2026; separate session from every solver)

Brief: `.claude/briefs/runs/2026-09-28-parent-verify-f61-v4.md`. Verdict: AUDIT.md section "VERIFY-F61-V4 (28 Sept 2026)".

## Step 1, reproduce (16:2x UTC)
- `family/decode_period.py --key key_period_v4.tsv --frac 0.1 --sbs --check` -> fresh; `family/test_period_key.py --key
  key_period_v4.tsv --collapse-ebr --min 2 --frac 0.1 --sbs --perms 200 --check` -> fresh; `family/recode_split.py score
  --check` -> fresh; `merge_period_keys.py` re-run into scratch from the three per-leaf v4 files: identical to key_period_v4.tsv.
- `repro.py` (fresh seeds, the committed scorer's own functions): 48/55 = 0.873 reproduced; seed 20260928, 2000 permuted keys
  mean 0.324 p95 0.455 p99 0.545 max 0.618, 0/2000 >= key; seed 7331 mean 0.320 p95 0.455 max 0.618, 0/2000. The committed
  200-key p95 0.436 is slightly low against 2000 keys (0.455); max 0.527 vs 0.618. Conclusion unchanged.

## Step 2, leakage (`leak.py`)
- Every one of the 459 v4 rows carries leaf fr.3982 f.101r (267), fr.3984 f.188r/f.184r (169) or fr.3984 f.274r (23); no f.61
  or f.108r row. Every anchor tile of recode_split.py's PRIOR list (H65/H67 SBS, H69 4TRI, H70 VBAR, H77 LOOPS) is on f.101r or
  f.188r (tile files' leaf column); group->class names on the anchors were set by the sister leaf's period letter, not Tomokiyo's.
- Where Tomokiyo's letters DO enter: not the key, but the f.61 side's class boundaries. H13/H15 (VBAR_A/B) and H26 (SBS) were
  blind shape sorts of f.61's signs whose group->cell naming was scored against his letters. The +5 of v4 over v3 comes entirely
  from the --sbs relabel (L03/13-15, L05/5, L08/5, L11/10 gained; L03/14 'e' lost). Ablations, 2000 fresh permutations each:
  without --sbs 42/55 = 0.764 (0/2000); SBS without its sort-artefact e 48/55 (unchanged); VBAR merged 48/55; the three
  Tomokiyo-validated cells (VBAR_A, VBAR_B, SBS) removed from the key 36/55 = 0.655 vs p95 0.400 (0/2000).
- The SBS boundary is independently backed on the sister leaves (H65: the period gloss writes o under the side-by-side glyph,
  blind sort), so it is not a leak of letters; it is a class decision first found on the known spans, and the conservative
  figure for "the period key reads f.61 with no Tomokiyo information at all" is the no-relabel 42/55 = 0.764.
- Scorer note: Tomokiyo's 'v' (avec, avance) is scored as a miss against INF = u; with u = v the key reads 50/55.

## Steps 3-5 (16:1x-16:2x UTC)
- Step 3, `split_sample.py` (5 Opus vision calls, prompts in PROMPTS.md pushed 08e31a63 before the calls): `split_result.txt` --
  SBS 10/10, PHI 10/10, INF 10/10, 4TRI/4HOOK 14/14, f.61 G2/G1 against sister-leaf forms 12/12; decoys 15/15.
- Step 4, `meter.py`, `c6_check.py`: 20/59/20 recounted; the 6 moves are INF u/e -> u (threshold: f.188r INF total 38 -> 50);
  C6 = e (8 firm tokens, 3 gloss tokens) falls on Tomokiyo's dash or is skipped at all 6 span positions -> regraded I;
  meter as graded 12 / 59 / 28.
- Step 5, `twoway.py` -> `f61r_v4_twoway.txt` (no run of >= 3 firm letters on the leaf); `phrase_ctl.py` (1 Opus text call,
  prompt pushed ce288ec1 before it) -> `phrase_result.txt`: true key 9th of 21, the rule passes 3-7 items on permuted keys too
  (mean 4.7): nothing recovered outside the spans.
