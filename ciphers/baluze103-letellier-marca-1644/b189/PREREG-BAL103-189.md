# PREREG -- BAL103-189, f.189r cipher vs its f.190r period decipherment (written and pushed before any alignment or score)

Worker BAL103-189 (account 2, LANE DEFAULT-A2-0710), 13 Oct 2026, written 07:3x UTC by `date -u`. Key source under test: published
(Tomokiyo, louisxiv0.htm 1644 table) as this folder names its signs (`key_decode.tsv`, which carries R7C-BAL103K's c = p).

**Material.** BnF Baluze 103 (btv1b9001389d), openapi.bnf.fr canvas 402 = f.189r, cipher with clear words, headed "A Paris ce 9e
Septembre 1644" (foliated 189 by eye); canvas 404 = f.190r, period decipherment headed "Chiffre A Paris ce 9 7bre 1644" (foliated
190). DECODE R2744. f.189r lines 1-21 cut by `tools/iiif_lines.py --ark btv1b9001389d --canvas 402 --iiif-host openapi --region
1100,1350,3250,4750 --follow-slope 400` (overlay checked, 21 bands on 21 lines), crops in `b189/images/f189r_L*_s*.jpg`.
**Disclosure:** both canvases were viewed once at 800 px to identify them; at that size the decipherment's opening ("La despesche
que je vous adresse pour le principat et le memoire ...") and its line shape were legible. The decipherment has NOT been transcribed
or read closely; it is read once (a transcription, not a gloss to be scored) after this file is pushed and after both blind passes
are written. The blind passes are Sonnet subagents given the f.189r line crops, `tx/PASS_INSTRUCTIONS.md` and the key sheet only,
never the decipherment, never told the content.

**Units.** Two blind passes (A, B), one Sonnet call each over all 21 lines; one reconciliation by this worker from the crops
(`tools/reconcile_passes.py`, disagreements settled by eye) -> `b189/f189r_rec.tsv`.

**Decode.** Each sign through key_decode.tsv, first value of an a|b cell; word codes (=N) expand to their words; clear words
written [in brackets] enter as their letters but are flagged clear; `?` and U tokens dropped. Normalisation as calib/PREREG.md
(lowercase, letters only, j->i, v->u, accents stripped). Decipherment span P: the f.190r text from its start to the word "depuis"
that ends f.189r line 21 (struck words omitted, interlinear insertions taken in), plus 200 letters of slack (semi-global DP, free end
gap in P, unit costs; calib.py's DP).

**Statistic A (gate, per blind pass A and B separately, and on the reconciliation, reported all three).** A = matched cipher-derived
letter positions / cipher-derived letters (clear-word letters are aligned but excluded from numerator and denominator).
**Control** (can vary on key correctness): 200 random permutations of the single-letter values across the key's letter cells (seed
1644), same transcription, same clear words, same alignment; mean, p95, p99. Descriptive: wrong-span null (D against an equal-length
span of P shifted by half its length, cyclic).
**Gate:** A >= 0.60 AND A > permutation p99, on BOTH blind passes. Otherwise no key change of any kind.

**Per-sign test of Tomokiyo's table** (reported per sign, cipher-derived letters only, aligned pairs, on the reconciliation, with
each blind pass's counts beside it). For a sign with n >= 2 aligned occurrences:
- *confirmed*: the aligned letter is one of the key cell's values (any of a|b|c) on >= 2/3 of occurrences;
- *contradicted*: every aligned occurrence is the same letter and it is none of the key cell's values (n >= 2), or >= 3/4 with n >= 4;
- *undecided*: otherwise; n < 2 is *unseen/too few*.
Each sign's agreement is also reported against the permutation control (share of the 200 permutations in which that sign's agreement
>= observed), descriptive.
**Licensed key.tsv edits (only if the gate passes):** a sign *contradicted* in the reconciliation AND with the same aligned letter
on >= 2 occurrences in each blind pass separately. An a|b cell may be narrowed to one value only under the same rule (every aligned
occurrence one of its values, n >= 2 in each blind pass, the other value never aligned) -- EXCEPT the ambiguous 9 (i|r|s) and the
f.50 sorter-bound confusable pairs, which are never edited by this job (owner's pass). Every licensed edit: key.tsv + key_decode.tsv
with source "BAL103-189 f.189r calibration", then `tools/decode_key.py . --check` and the fr17 judge on f.50.

**The 9 counts.** Standalone 9 tokens (not =9) in the reconciliation, each with its aligned letter; strict-known as r10/PREREG.md
addendum (aligned letter in {i, r, s} AND the two letters on each side match contiguously); k_i / k_r / k_s strict and loose.
**Decision rule for the 9 shape split (stated in advance):** pool the strict-known 9s of f.189r with f.171r's six (all s,
r10/nines.tsv) -- same correspondence, same September 1644 hand. If the pool reaches N >= 7 with k_i >= 2 (r10/power9.tsv
perfect_can_pass), the shape read runs as registered in r10/PREREG.md (one blind subagent call on a crop around each pooled control 9,
no values, G = long looped g-like descender vs S = short; best {G,S} -> {i, r|s} map accuracy > exact label-permutation null p95 =
PASS). PASS licenses only applying the split to the owner's 9 shape piles on f.50 later (no exceptions.tsv edit by this job);
FAIL or k_i < 2 = NON-TEST/negative logged, f.200 or f.230 (DECODE R2745/R2746) named as the next sibling. If the cap cannot cover
the shape-read call, the counts are reported and the read is the named next step.
