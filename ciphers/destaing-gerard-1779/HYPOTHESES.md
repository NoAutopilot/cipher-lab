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
