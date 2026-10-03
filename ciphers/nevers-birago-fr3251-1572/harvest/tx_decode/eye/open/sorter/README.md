# Sorter focus, Birago 1572 T5x / T83-T24 (BIR-APPLY, 3 Oct 2026, account-3 worker)

`focus.tsv` (sid, question, crop, kind, sorter folder): 17 tiles for the owner's sign sorter, none settled by majority.

- **conflict** (11): A1-BIR-VERIFY's two-option read and BIR-OPEN's open-choice read disagree. f.117r: T95/T51 x5
  (L04.6, L05.2, L07.21, L09.11, L09.30), T66/T76 (L05.27), X_NEW/T84 (L03.27), T13/T64 (L06.23); f.168: T83/T24 x2
  (R03.4, V01.10), T51/T95 (V03.10). Graded M in `../../apply/exceptions_apply_<leaf>.tsv`.
- **open-only** (6): f.117r positions BIR-OPEN alone moved to T51 (T65->T51 x5, T95->T51 x1): the same three-way
  T65/T95/T51 question. Also graded M.

The crop column is `<sorter folder>/pages/<strip>.jpg@x,y,w,h` from that sorter's `signs.tsv` (boxes approximate, see
its README). The f.117r sids live in `ciphers/birago-fr3252-1571-72/sorter/signs.tsv`, the f.168 sids in
`ciphers/nevers-birago-fr3251-1572/sorter/signs.tsv`, so a page covering both needs the two signs/labels files joined.
Two lines have one tile fewer than transcribed positions (f117 L09: 29 vs 30; f168 R03: 18 vs 19): those rows say the
tile index may be one off, and L09.30 has no tile at all (crop = line end). Build and publish are the account-3
orchestrator's (sign_sorter.py `--focus` reads the first two columns). No sign values appear in this folder.

**Published 3 Oct 2026 13:40 UTC (account-3 orchestrator):** https://claude.ai/artifact/DHiLGFWiqrHxQYzLrFNh6s (private to the owner; built from the two sorters' joined signs/labels; 16 focus tiles -- f117 L09.30 has no tile, left out; db capability records the decisions; apply with tools/sign_sorter_apply.py).
