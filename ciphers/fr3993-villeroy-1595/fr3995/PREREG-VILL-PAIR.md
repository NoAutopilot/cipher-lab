# PREREG-VILL-PAIR (A1B-VILL-PAIR, LANE-A1B, account 1, 3 Oct 2026) -- written and pushed before any run

Hypothesis: the target's figures are pair codes (Bourdeau's 1x/2x segmentation, nevers1595/seg.py, as already on disk
in `solver/target_pairs.txt`), each figure group = one homophone of one letter; non-figure signs are their own tokens;
K (f159 null N3, VILL-NOMEN) removed as null.

Cipher: `pair/cipher_pairs_noK.txt`, built from `solver/target_pairs.txt` by dropping the header and every `K` token
(sed, command in NOTES.md). 25 lines (one cipher run per line), **N = 594 tokens, K = 68 types** (146 two-figure groups).

Family: `tools/family_run.py --family homophonic --param profile=target --restarts 8 --corpus tools/data/fr16`
(homophonic_anneal, French order 3), `--tokens space --cipher pair/cipher_pairs_noK.txt`. Why homophonic and not
phased_homophonic or wordcode: the runs are already segmented into figure groups (one token = one group), so the phase
problem phased_homophonic solves does not arise; wordcode tests whole-word codes, a different hypothesis (LANE R4 N's
mixed nomenclator, whose control read 2-6%); this job changes only the one variable A1-VILL-HOMO named -- the token
unit -- with the same solver, so the two rows compare directly.
Pins: the homophonic family takes no pins parameter (only seeded_code does), so the VILL-SIGNS certified values
L=r, w=m, +=x are NOT pinned; disclosed as a deviation from the brief's "if the family accepts pins".

Seeds 3 (control), gate 0.6 on control mean recovery. CONTROL BELOW GATE (exit 3) = "untestable at N=594 by this family",
not a negative; the target is then not run.
If gated: target run (seed 1) and a shuffle-target floor (`--shuffle-target 1`, control seeds 1 to stay in the box).
Pass = judge (`tools/judge_plaintext.py specs/fr3993-villeroy-1595.json --file`, fr16) PASS on the real-target decode
AND judge FAIL on the shuffled decode (a shuffled PASS voids the judge for this family at this N, rule 3).
Negative = control gated AND real-target judge FAIL -> logged as a control-backed negative for the pair-homophone design
over Bourdeau's single unmeasured pass (rule 2 conditional). Any other outcome is reported as "judge cannot decide".
Rule 3 headline check reported: control mean must be < 0.95 to count as able to fail (else noted as near ceiling).
