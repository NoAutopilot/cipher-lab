## NEAR3-C1RD rule-7 re-derivation (4 Oct 2026)
Fresh session, read only the brief, CLAUDE.md rules 4 and 7, spec, ciphertext.tsv, key.tsv, decode_key.py --help (no decode.json exists; NOTES.md, HYPOTHESES.md, reading*, glossctl/ not opened before step 2 was written).
Convention used (from spec/key/decode_key help alone): clear words ([PLAIN:..]) and '/' are not cipher tokens; value and grade from key.tsv; conf != H downgrades to M; unkeyed = '?'/U.
Script: `rederive/rederive_c1rd.py` -> `rederive/rederive_c1rd.txt` (924 cipher tokens: C 97, S 675, M 152, U 0).

`python3 tools/decode_key.py ciphers/clair1161-avis-flandre-1688 --check`:
```
ciphertext.tsv: tokens 939: C 97, M 152, S 675, U 15
reading up to date
exit=0
```
(939 = 924 cipher tokens + 15 non-cipher rows graded U by the tool: the clear words and '/'.)

Diff against `reading_tokens.tsv` (opened after step 2), token by token on line, pos, sign, value and grade: 924 agree, 0 differ. Grades C 97 / S 675 / M 152 match the committed header.
Verdict: PASS (rule 7). This checks that the committed reading regenerates from ciphertext.tsv + key.tsv; it says nothing about whether the key is right (rule 10). key.tsv and the reading were not edited. Subagent calls: 0; requests: 0 (disk only).
