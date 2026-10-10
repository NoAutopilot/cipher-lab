# PREREG-DUTCHKEY (LANE FAMILY-A2s, account 2, worker DUTCH-KEY, written 10 Oct 2026 19:2x UTC by date -u, before any score)

Brief: `.claude/briefs/runs/2026-10-10-ytbiz-family-1709-jobs.md` "### DUTCH-KEY". Nothing below has been computed when this file is pushed.

## Inputs (frozen at this commit)
- Key: `key_dewitt_1653.tsv` (codes 1-66, from the printed table in Brieven van Johan de Witt I, ed. Japikse, p.72; built and
  checked by `key_dewitt_1653.py --check`). Codes > 66 are outside the key (name/country codes, edition p.92 n.2) and are not decoded.
- Ciphertext (two passes, reconciled): `ct_p351.tsv` (Birch I p.351, De Witt to Beverning, 24 July 1653; 82 tokens, A = B on all 82),
  `ct_p339.tsv` (Birch I p.340, the cipher of the 18 July letter of Beverning and Nieuport to De Witt that starts on p.339; 223 tokens,
  2 pass disagreements, settled in the `flag` column), `ct_p308.tsv` (Birch I p.308 19 tokens + p.309 67 tokens, Beverning to De Witt
  27 and 30 June 1653; A = B on all 86), `ct_p435.tsv` (Birch I p.435, Beverning and Vande Perre to Boreel, 22 Aug / 1 Sept 1653;
  136 tokens, A = B on all 136).
- Disclosure: while reading the pages and the key I saw that p.351 run 1 visibly spells a word under the key (the transcription passes
  were already independent of the key: pass A is a Sonnet call told nothing about a key; pass B is my eye read, and A = B on p.351).
  The reference spans below were chosen from the English translation's context, not from a decode.

## Gate (known answer, p.351)
Reference: the Dutch of the same letter printed in the edition, pp.100-101 (extract "Ick ben in 't seecker bericht ... te persisteren",
De Witt to Beverning 24 July 1653, the letter the edition's n.3 places at Thurloe I p.351), edition OCR `edition/VAN_DEWITT_01_100.html`,
`_101.html`. Each cipher run is matched to the Dutch word(s) in the place the English translation puts it:

| run | English context in Birch | Dutch reference span (edition) |
|---|---|---|
| 1 | "that men of [1] did censure unjustly" | princessedouariere ("de Princesse Douarière t'onrechte") |
| 2 | "as if they to the business of [2] did incline" | graefwillem ("de saecke van Graef Willem toegenegen") |
| 3 | "that their [3] did suppose the contrary" | haerehoocheyt ("dat Haere Hoocheyt ter contrarie oordeelde") |
| 4 | "that the said [4] was incapable" | grave ("dat gemelten Grave incapabel was") |
| 5 | "That furthermore their [5] were of opinion" | haerehoocheyt ("dat vorders Haere Hoocheyt van opinie was") |
| 6 | "should choose 330" | code > 66, not scored |
| 7 | "or [7] to &c." | designeren ("verkiesen ofte designeren tot etc.") |
| 8 | "that their [8] did desire nothing more" | haerehoocheyt ("dat Haere Hoocheyt niet liever wenschte") |
| 9 | "that their [9] had better declare" | haerehoocheyt ("dat Haere Hoocheyt ... beter metterdaet") |
| 10 | "familiar to their [10]" | haerhoff ("aen haer hoff familiaer") |
| 11 | "by order of [11]" | haerehoocheyt ("door last van Haere Hoocheyt") |

Where the English renders "their" outside the run, the reference still includes "haere"/"haer" so that an abbreviated or a
possessive-included cipher both have their letters available; the statistic below is a subsequence fit, so a shorter cipher form
(an abbreviation) is not penalised and extra reference letters cost nothing.

Statistic S: for each scored run, decode in-key tokens to letters (u/v as u); L = length of the longest common subsequence of the
decoded string and the reference string; S = sum L / sum (decoded letters) over runs 1-5, 7-11. Coverage = share of the 82 tokens <= 66.
Control (can differ): the key's 66 letter values permuted over the 66 codes (keeps each letter's homophone count), 1000 draws, seed
20261010; the same runs, references and statistic; p95 and max reported.
**PASS** iff S >= 0.80 AND S > the control p95. Otherwise FAIL: log in HYPOTHESES.md, do not decode p.435.

## Supporting folds (reported, not gating)
No era-matched 17th-century Dutch corpus is in tools/data (nl16 is 1569-1589 moral prose, nl18 1770-1799, nl20 modern; the judge has no
`nl` 1650s entry). Statistic for p.339 (Birch p.340) and p.308/309: mean per-letter log10 probability under an add-one-smoothed letter
4-gram model (26 letters, word breaks removed, u/v merged, j->i, y kept) trained on the edition's OCR pages on disk EXCEPT pp.099-101 (the gate's answer) and p.108 (the matched control's source)
(`edition/VAN_DEWITT_01_071-073, 091-098, 102-107, 109-112`: De Witt's own 1653 Dutch extracts plus the 1906 editor's notes) together with
`tools/data/nl16` (all files). The model is era-bracketing, not era-matched; say so with any number. Control: the same 1000 key
permutations; report the decode's score, the control p95 and max, and the fraction of control draws above the decode. A fold
"supports" the key iff the decode beats the control max.
Also reported, not scored: p.308's Birch interlinear English gloss "new representatives" beside the decoded run.

## Step 4 (only on PASS): p.435 (Boreel)
- Decode p.435 with the same key; codes > 66 kept as name codes (grade M, unread).
- Shuffled-key control on p.435 itself, computed BEFORE the decoded text is printed or read: the 4-gram statistic above on the
  in-key tokens, decode vs 1000 permuted keys (p95, max).
- Matched control (rule 3): a synthetic Dutch text from the held-out edition page p.108 (the first 128 letters, after the
  normalisation above, of the first double-quoted passage on the page, "Echter vertrouwe ick vastelijck ..."; p.108 is not in the
  4-gram training set), enciphered under the p.72 key with uniformly random
  homophones, with 8 code tokens (> 100) inserted at the same relative positions as in p.435 (8 of 136 = the same code-group share);
  the same statistic and the same 1000-permutation control. Question: does the statistic separate a true-key decode from shuffles at
  this N? Report both numbers (synthetic decode vs its p95; p.435 decode vs its p95).
- Reading p.435: "the key reads it" only if the p.435 decode beats its own control max AND the matched control separates; else the
  result is "the p.72 key does not read p.435" (a negative for this key only, licensed by the matched control), never a negative on the
  letter's cipher as a whole (the letter itself says it uses a new cipher sent by Boreel).

Scripts: `decode_dutch.py` (decodes all four ct files to `reading_*.tsv`, `--check` exits non-zero if stale) and `gate_dutchkey.py`
(computes the gate, the folds and step 4, writes `gate_dutchkey.json`; `--check` re-computes and compares).
