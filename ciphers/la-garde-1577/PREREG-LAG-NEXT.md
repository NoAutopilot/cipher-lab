# PREREG-LAG-NEXT: the next family on the base codes at N=229 (9 Oct 2026, account 2, LANE FAMILY-A2d)

Written and pushed before any control or target score of this job is computed. CPU only, no network beyond git.

**Family choice.** `tools/design_prior.py families/basecode_cipher.txt` (pasted in NOTES "LAG-NEXT"): operative class tier
multi-sign d=0.11, letter-for-letter d=0.25 (both "plausible"); advisory fine ranking homophonic 0.11, alphabet substitution
0.25, nomenclator 0.27, syllabary 0.56, mixed 0.97, code 1.75. Homophonic and masc (= alphabet substitution) are closed by
LAG-GAP; syllabary and wordcode already have rows. The highest-ranked family with no row, nomenclator, is not taken: the fine
tier is advisory only by the tool's own docstring (it does not separate homophonic from nomenclator), and the repository's
`nomenclator` family is a two-level numeric word code (particle block 1-99, family book >= 100) whose control cannot match a
target whose 26 codes all lie in 1-29 (rule 3: match the design). So, per the brief, **running_key** (book-key Vigenere,
`tools/families/running_key.py`, `running_key.py` two-stream beam decoder, defaults order 6, beam 3000, per_hyp 10).

**Control (step 1, the only scored step unless it gates).** `tools/family_run.py specs/la-garde-1577.json --family running_key
--cipher ciphers/la-garde-1577/families/basecode_cipher.txt --tokens space --seeds 3 --gate 0.6 --control-only
--measured-error p --param noise=p`, p = 0.055 (LAG-ERR's measured base-code error) and p = 0.084 (its 95% upper bound, the
rule-3 error-band bracket). Corpora: the three fr16 texts in tools/data/fr16 (the family needs >= 3: plain book, key book,
training; the spec's two judge corpora plus lettresindites00marg). The control is laid on the target's own 15 message lengths
(22 25 9 8 28 20 19 16 22 15 9 14 4 6 12, N=229). Noise: the `noise` param added to the family for this job (a share p of
control cipher letters redrawn at the control ciphertext's own letter frequencies; offline test
tools/tests/test_running_key_noise.py). Recovery = share of plaintext letters read correctly. Gate 0.60 on the 3-seed mean.

**Read-out, fixed now.**
- Control below gate at BOTH 0.055 and 0.084 -> running_key is **untestable by this tool at N=229 with these message lengths**
  ("untested-by-this-tool", not a negative, rule 3); the target is not run and the LAG-GAP score-gap gate is not reached.
  Logged in HYPOTHESES.md (family_run rows) and NOTES.
- Control gates at 0.055 (or both) -> stop scoring; write Amendment 1 here fixing (i) the code-to-tableau-letter map for the
  target (the plain running_key family assumes the codes are the standard tableau's letters in order; any map is itself a
  hypothesis) and (ii) the LAG-GAP score-gap design (PREREG-LAG-GAP.md) with its power check on held-out controls first, push
  it, and only then run the target. If the gate's power check fails for this family -> "non-test", no gate swap.
- The target stays `open` (rule 5) whatever the result. No reading is claimed by this job.
