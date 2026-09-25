# Key cross-match (LANE KX job 1b, repair pass, 25 Sept 2026)

**Fix A (coverage).** 60 key files found; 4 are not code->value tables and are excluded with a one-line reason,
not guessed: `huntington-blathwayt-madrid-1728/key_items.tsv` is a per-item coverage STATISTICS table;
`trew-posthius-1614-18/key_leaf_{1614,1618_left,1618_right}.tsv` are two-row structural tables with no value
column. Of 57 usable keys, 35 now have an identifiable own ciphertext (was 1 of 56 able to even score its own
text). Own-text pairing now reads a folder's `decode.json` job list when one exists (fixes
august-van-saksen-1561-64's key_53/74/98, each tied to one specific ciphertext, previously all "own" to all
three); else a shared digit run or the key's office name in the ciphertext's "Cipher system:" header, with
process-of-elimination for one key left over (fixes thurloe-printed's 8 offices x ~23 letters, previously all
cross-called "own"; jan-van-nassau-1572-75's key_1572 vs key_5549). A header-word detector plus name-based
column aliasing (`robust_load_key`) fixed keys whose header (`system`, `row`, `sign_desc`, `item`, `figure`,
`plaintext`, `plain`/`sign_code`) dk.load_key's own sniffing missed, including the two previously-crashing
`key_brienne_1647/1651.tsv` (`code`+`plaintext`, the job's named positive control). A sign-column-by-name
fallback (`robust_tsv_signs`) and a `=`-prefix clear-word filter (jan-van-nassau's documented convention) fixed
several ciphertext tokenisations. 22 keys still have no own ciphertext: ambiguous multi-key folders with no
decode.json (fr5160-letellier-1653's key_1659/key_1659_ext -- see Weak below), or a format not attempted here
(dupuy452-carpi-1520: concatenated glyphs, no separator; orange-nassau-1572/key_nepveu.tsv: mostly clear French
under the 4-letter clear-word floor; thurloe-printed/key_blake.tsv's P9: needs its own bespoke decode.py).

**Fix B (control).** The unrelated-key null is replaced with judge_plaintext.py's calibrated controls:
pass_null (beats 200 shuffled same-length windows' 99th pct) and pass_real (beats 200 real-corpus windows' 5th
pct). pass_null clears broadly; **pass_real cleared for none of the 35 own-text pairs**, including two
independently-verified readings (august-van-saksen-1561-64/key_53, z_sh 6.86, dictword_share 0.52;
oxenstierna-gustav-adolf-1632/key.tsv, z_sh 9.26, dictword_share 0.74) -- both score below even the worst 5% of
their own reference corpus, because fr16/de16 are cleaner edited text than a real decoded period letter. A
corpus-register gap, not a wrong decode -- read z_shuffled/pass_null/dictword_share together, not pass_real alone.

**Positive control, mechanical bar (rank 1, z_shuffled>=4, pass_null): 8 of 35** with own-text, up from 1 of 56
clearing both controls before: august-van-saksen-1561-64/key_53.tsv, key_98.tsv;
clair1067-brienne-poland-1646/key_1646.tsv; fr20140-danzay-1557/key.tsv; fr2980-gramont/key.tsv;
fr5160-letellier-1653/key_1659_f86only.tsv; huntington-luzerne-destouches-1781/key.tsv;
oxenstierna-gustav-adolf-1632/key.tsv. Strict own-quality (also pass_real): 0 of 35, per the finding above.

**Hits: 0. Weak: 8** (excludes `own`/known-pair rows) -- all fr5160-letellier-1653/key_1659(_ext).tsv against
its own f1/f67/f86/f88 (cov 0.51-0.96, z_sh 3.6-5.9): 4 keys, no decode.json, so elimination could not assign a
single own-text, but the numbers make key_1659(_ext) near-certain as this folder's real key. Plus
clair1108-duvergier/key_1696.tsv on its own ciphertext.tsv (cov 0.997, z_sh 4.57): its decode.json names a
`signs.tsv` not on disk, so own-pairing still misses it though tokenising now works.

**Known pairs.** Lodewijk's 1574 table on Jan's 5549 postscript (J5S): cov 0.814, z_sh 2.45. key_5549 (a copy of
Lodewijk's table) on Jan's own 5549 letters: cov 0.797-0.834. Brienne's key_brienne_1647/1651.tsv, same file in
both folders, cross-folder: cov 0.21-0.46 each way -- under the 0.5 gate, so it does not cross-decode.

**Negative pairs: 0 false positives of 13 named, 8 scored** (5 untestable: rah-morillo-1817 has no committed
ciphertext; rah-canada-1869/la-garde-1577 -> Nevers have no key of their own yet). Willem-van-Hessen's
nomenclator vs Nassau 1572-75, Nassau 1572 key vs Willem-van-Hessen 1069, and vs rah-canada-1869 /
huntington-luzerne-destouches-1781 (century gaps): none hit or weak.
**Next, not run here:** a decode.json for fr5160-letellier-1653; a period-spelling corpus for pass_real; Swedish
support (oxenstierna's own reading is Swedish, scored here against French for lack of one).
