# HYPOTHESES -- na-janssens-java-1811

| date | hypothesis / family | instrument | control | target / real | verdict | source |
|---|---|---|---|---|---|---|
| 6 Oct 2026 | LM-context fill of the 56 unkeyed leaf-188 codes from the key's value vocabulary | GAPS17 letter 5-gram, fr1810, window 3 (`lmfill/heldout_188.py`) | held-out: 20% of 76 foldable C tokens masked x10 seeds; shuffled-context control 20 seeds/mask: top-1 max 0.040, confident precision 0.020 | top-1 0.153 (gate >= 0.30 FAIL); confident precision 0.161 on 31 (gate >= 0.80 FAIL, dominated by 'l') | untestable by this method at this N (rule 3); not run on the unkeyed codes | lmfill/PREREG-R11-JANSLM.md (2a454d193); NOTES.md R11-JANSLM |
