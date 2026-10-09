# TXE2-VIVSHEET results (PREREG-txeng2-15 SH-VIV; 9 Oct 2026, 23:33-23:4x UTC by date -u; account 4, Opus 5.5)

Product: a value-blind exemplar sheet for the Saint-Gouard 1572-74 hand, cut from Tomokiyo's published key drawings on
disk (sources/cryptiana/web/henryiii_Vivonne*.png). Zero network. Used by no reader this round.

## What was built
- Labels M = 40: the single-sign tokens of tx/SIGNS.md together with those of tx/f102r_rec.tsv (tokens only; f102r adds
  t, Z, H; SIGNS.md adds r, l, 8). Not one drawable sign, so left out of M: brace descriptors ({flourish} {scribble}
  {curl} {box}), plain-script fragments (Il, non, non], he, he], et], &]), the marker DUP.
- Box-finding: 3 Opus subagent calls, one per drawing, matching by shape only on a gridded 2x copy (scratch):
  Vivonne1 (1574 key) gave 37 of 40 and NONE for c, 2, 8; Vivonne3 (1580) gave c and 2, and its 8 was rejected (a theta-like
  oval the subagent said does not clearly look like an 8); Vivonne6 (1588) gave 8. Vivonne2, 4 and 5 were not called.
  VivonneSig is the signature leaf (no cipher signs) and was not called.
- Boxes unedited after the worker checked each crop by eye. Grades 27 H, 13 M. Tiles carry the token and the key year;
  3 tiles (c, 2: 1580*; 8: 1588*) come from a later Vivonne key, not the 1572-74 hand's own.

## Coverage
40 of 40 committed labels covered: 37 from the hand's own 1574 key, 3 from later Vivonne keys (starred).
Uncovered: none. (Descriptor and plain-script tokens are not counted in M; see above.)

## Files (commit bf459203b; RESULTS.md 99b5e9ced)
| file | sha256 |
|---|---|
| ciphers/fr16104-vivonne-spain-1572/glyphs/sheet_tomokiyo_v1.png | 999812049a2885645fc3f4c78404dbdd6313ac017641425ccc6031a2568b19aa |
| ciphers/fr16104-vivonne-spain-1572/glyphs/sheet_tomokiyo_v1.tsv | 85f5a1a03893a194cc34e0f477910614d1a1c03b8ca2ff0fc13e15002683e246 |
| ciphers/fr16104-vivonne-spain-1572/glyphs/boxes_tomokiyo_v1.tsv | dc91442ef1c58e1d80817a2504cb211c1be522a83ae897935c717a1b69ab7b35 |
| ciphers/fr16104-vivonne-spain-1572/glyphs/build_sheet_tomokiyo.py | 799f4c17e168a333867b1b4efcfb0a7e6577baed122ea9d64e2223f11c3dcef7 |
| ciphers/fr16104-vivonne-spain-1572/glyphs/SHEET-CHANGELOG.md | e39a98a06aa8e9ae7f4d509213df4191364d37479fb5761f658f6b1c958c0ac6 |

`python3 ciphers/fr16104-vivonne-spain-1572/glyphs/build_sheet_tomokiyo.py --check` -> `OK: sheet_tomokiyo_v1 matches a rebuild`.

## Discipline
No truth file, no f.103r crop or output (c106_f103r, outputs/vivonne1573-f103r-confirm2/, txeng2/s2score/) and no
key.tsv opened; SIGNS.md and key.tsv not edited. Subagents saw only their prompt and one drawing. Tokens: 3 subagent
calls, about 315k subagent tokens in total (108k, 104k, 103k). Dollar cost: the lane's get_session reading.

Openings of eval truth: 0

Verdict: measured: sheet built, 40 of 40 committed labels covered; uncovered: none (c, 2, 8 from later Vivonne keys, 1580/1588, starred)
