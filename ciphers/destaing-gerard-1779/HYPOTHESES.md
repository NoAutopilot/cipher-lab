# destaing-gerard-1779 -- hypothesis families

Append-only. Rows below normally come from `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number
sits beside the TARGET number in every row). The rows here are hand-written in the tool's own row format
because the family tested (period-code numeric overlap) is not one of `tools/family_run.py`'s families
(masc, homophonic, periodic_vigenere, running_key, keyed_running_key) -- see `period_code_test.py` for the
script that produced them. Prose sections may be added above this table by workers.

<!-- period_code_test.py table: one row per run, appended by hand in the family_run.py row format -->

| date (UTC) | family | parameters | seeds | CONTROL mean (5-95pct) | TARGET hits | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 | period_code_overlap (hand-run, not in tools/family_run.py) | marbois Code A/B specimen (Marbois-to-Vergennes 13 Mar 1782, 160 distinct keys, range 9-1195) vs d'Estaing's N=104 distinct codes, draws in range 2-597 | 1 (1000 Monte Carlo draws, seed=1) | 14.51 (10-20) | 17 | n/a (overlap count, not a plaintext candidate) | no -- inside control band, not a match | for LANE ZX2: destaing period code test |
| 25 Sept 2026 | period_code_overlap | marbois Code C specimen (Marbois-to-Castries 17 Mar 1782, 45 distinct keys, range 8-1154) vs d'Estaing's N=104 distinct codes, draws in range 2-597 | 1 (1000 Monte Carlo draws, seed=1) | 4.41 (2-8) | 6 | n/a | no -- inside control band, not a match | for LANE ZX2: destaing period code test |
| 25 Sept 2026 | period_code_overlap | marbois Code A/B + Code C combined (200 distinct keys) vs d'Estaing's N=104 distinct codes, draws in range 2-597 | 1 (1000 Monte Carlo draws, seed=1) | 18.17 (13-24) | 22 | n/a | no -- inside control band, not a match | for LANE ZX2: destaing period code test |

**Reading (rule 3/4, S-grade, control-backed negative):** d'Estaing's 30 April 1779 code does not overlap
sources/cryptiana/web/marbois.htm's four reconstructed 1780-82 French diplomatic codes (Codes A, B, C, D --
Vergennes/Luzerne/Montmorin/Castries correspondence) any more than chance predicts, for every specimen tested
individually and combined. Consistent with these being different codebooks: different correspondents, and
three years later than this letter. Even a real hit would only be numeric coincidence, not a shared decode --
two-part codes assign numbers to entries independently per book (marbois.htm's own description of Codes A-D).
No period code tested this session reads d'Estaing's letter.

| date (UTC) | family | parameters | seeds | CONTROL mean (5-95pct) | TARGET hits | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 27 Sept 2026 | onepart_dict_position (hand-run via `onepart_test.py`, not in tools/family_run.py) | top 12 distinct codes vs fr18 word-type initial-letter bands (66,291 types), consistent initials = {a,d,e,i,l,n,p,q,v} (folded initials of de/la/le/les/que/et/a/en/il/ne/pour/vous), range 2-597 | 1 (1000 Monte Carlo draws, seed=1) | 5.76 (5-95pct 3-9) | 6 | n/a (band-consistency count, not a plaintext candidate) | no -- inside control band | for DES-PART: destaing one-part dictionary-position test |

**Reading (rule 3/4, S-grade, non-test at this N):** the 12 most frequent code groups' relative positions in
the 2-597 range are no more consistent with a one-part-alphabetical placement of common French function words
than 1000 uniform random draws of 12 values in the same range (6 of 12 vs control mean 5.76, 5-95pct [3,9]).
The same control also stands for the two-part null (position uninformative), since the null model for
"two-part" is exactly the uniform-random draw already used. Per CLAUDE.md rule 3, a target inside the
control's band is "no support for one-part at this N", not a negative on the code's design -- the test does
not distinguish one-part from two-part at N=12 against 26 letter-bands. See NOTES.md "DES-PART (27 Sept
2026)" for the full run and next-step discussion.

| date (UTC) | family | parameters | seeds | CONTROL mean (5-95pct) | TARGET hits | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 3 Oct 2026 | known_key (hand-run via `known_key_test.py`) | La Luzerne-Destouches 1781 key.tsv (281 codes, 1-1199) on N=216; fr18 4-gram of keyed runs vs 1000 value-shuffled keys | 1 | -1.003 (p95 -0.732, p99 -0.658) | -0.842 (coverage 44/216) | n/a | no -- and positive control 1/5 windows at matched coverage: NON-TEST | for FT4 (account-4) |
| 3 Oct 2026 | known_key overlap | same key, distinct-code overlap vs uniform draws 2-597 | 1 (1000 draws) | 22.7 (17-29) | 25 | n/a | no -- inside band; no out-of-sample positive control | for FT4 (account-4) |
