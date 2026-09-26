# Key cross-match

## Calibrated gate and rerun (XMATCH-CAL, 26 Sept 2026, 18:05-18:30 UTC)

**Why.** The 25 Sept verdict needed `pass_real`, which no own-text pair cleared, verified readings included, so
no verdict from the tool was trusted. The gate is now fitted to our own verified readings rather than to a corpus.

**Positive controls.** 18 own-text pairs from the readings status.json and V-GATE2 (26 Sept, 18:03) list at N3/N4
after two audits: Gramont f.29r and f.30, Danzay (two texts), Lodewijk 4610/4611/4612/4616/5797, August of Saxony
53/57/126, Jan van Nassau 5551, Mercy, Linhares, Van Beuningen, Blathwayt, plus Oxenstierna, which the brief names.
Eckert 1864 (route cipher, key in `key.md`, not a code table) and Thurloe P4 (no key identified) could not be used.
A second tier of 11 N0/N1 pairs (plaintext already in print) is scored as a check only. It is never used to fit the gate.

**Null.** 20 shuffled-value keys per pair. Each null draw is scored as if it were a candidate, by its z against the
other 19. The first null shuffled all of a key's values together. It broke the design's own structure (letters on
low codes, words above), and Lodewijk's 1574 table then "read" a 1636 Hessen letter, a 1712 Portuguese appendix and
four more unrelated texts. The null now shuffles values only within their class (single letters among letters,
longer values among longer values). All six of those hits disappeared.

**Statistic.** max(z of the letter 4-gram score, z of the value-frequency score). The value-frequency score is the
mean log corpus frequency of each decoded value: a letter by its letter share, a longer value by its share as a
whole word. The 4-gram z alone left 7 of 18 verified pairs below z 2. A code whose values are all whole words
still reads as words under any shuffle, and only the frequency of the words tells right from wrong.

**Result (KEY-CROSSMATCH-CAL.tsv, tools/data/key_crossmatch_gate.json).** No single gate both admits every verified
pair and rejects 99% of null draws:
- Admit-all: stat >= -0.582 admits all 18 verified pairs but passes 336 of 360 null draws (93%). It is unusable,
  because five verified pairs are too short or too thinly covered for any statistic here: 5551 (32 tokens),
  Linhares (26), Danzay f.36 (67), 5797 (73), and Gramont f.30 (its extension key alone covers 10%).
- **Operating gate: stat >= 3.292 for ciphertexts of >= 100 tokens with coverage >= 0.5.** It admits all 13
  verified pairs in that stratum. The margin is thin: 3 of 260 null draws (1.15%) clear it, just over the 1%
  target. The null 99th percentile is 3.498, 0.206 above the gate, and the lowest verified pair is Lodewijk 4612
  (3.29). A 3.50 gate would meet 1% and drop 4612 (12 of 13). The brief says to admit the verified pairs, so 3.292
  stands and the false-positive rate is flagged here.
- Print tier: 6 of 7 in the stratum are admitted. Gunther 1561 misses at 3.28.
- Rule 3 check on shuffled text (RETRO-APPLY-T): 50 of 65 decodes of token-order-shuffled own texts clear the gate.
  This is expected. Value frequency is order-blind by construction, and a word-valued decode keeps its 4-grams.
  So the gate licenses "this key's code-to-value mapping fits this text's code frequencies". It never licenses
  "this is a reading". Every hit is read by eye before any claim, and the ROOM line says so.
- Multiple comparisons: the sweep scored 465 cross-folder pairs in the stratum. At 1.15%, about 5 false hits are
  expected by chance.

**Rerun (KEY-CROSSMATCH.tsv, rewritten, 99 keys x 186 ciphertexts, 70 s).** Own-text rows: 23 of the 31 in the
stratum clear the gate, all 13 verified pairs among them (Lodewijk 4612 exactly at the floor it sets). The 8 below
it: Gunther 3.28; fr3987 2.79; Jan key_5549 on its own 5549 1.81 (read by Lodewijk's table: J5S);
wvo-hessen-1564 0.85; key_1572 on 5550 and 5557/5552 (0.69, 0.03, both read by Lodewijk's table instead);
colbert26 0.0; malsburg key_519 0.0. Rows whose key fails its own-text positive control keep the TSV verdict
`unusable-key`. Their gated result is still printed and listed below. Negative pairs: 0 of 15 clear the gate.

**Every cross-folder pair that clears the gate:** 33 in all, and none is a new lead.
- 30 are one known relation: the Nassau brothers' shared table. Jan's `key_5549.tsv` is a copy of Lodewijk's 1574
  table, and it reads Lodewijk's 4503/4610/4611/4612/4614/4616/5801/5810/5811(+cut)/7205/7206/sib at
  stat 3.29-28.18. Lodewijk's key, key_full, key_full_v2, key_4614, key_7205 and key_7206 read Jan's
  5549_ps/5550/5557_5552 at 3.43-6.59, and 5551 as `short` (32 tokens) at 3.39. One row (Lodewijk key.tsv
  on 5549_ps, 3.83) is the named KNOWN_PAIRS entry.
- `clair1108-duvergier/key_1696.tsv` on `espagnol142-mercy-1648/ciphertext.tsv`: stat 4.94, coverage 0.649,
  522 tokens. Adjudicated as design kinship, not a lead. Seven of their 22 common codes agree, and six of those
  are the generic a=10, b=12, c=14, d=16, e=18, f=20 run. Mercy is already read by its own key (stat 14.68).
- `clair1108-duvergier/key_1696.tsv` on `bowes-walsingham-1583/ciphertext.txt`: stat 4.06, coverage 0.693,
  101 tokens. Adjudicated as a probable false positive. The two keys share 1 code value. The text is at the
  stratum floor, and it is English scored with the French model because Bowes has no language model here. It is
  one of the ~5 expected.
Both adjudications are in the tool's ADJUDICATED table, so the nightly run does not post them again.

**Nightly.** `python3 tools/key_crossmatch.py --since-hours 25 --post-room` scores only the pairs whose key or
ciphertext changed since the last origin/main commit at least 25 hours old. It deepens a shallow clone once when
it has to. On 26 Sept a 24-hour window held 42 key files and 97 ciphertext files and took 82 s. It posts at most
five ROOM lines, one per `new lead`, in this form:
`key_crossmatch nightly (tools/key_crossmatch.py) | for the parent: xmatch hit (new lead): <key> reads <ciphertext>
stat=<s> (gate 3.292, null p99 3.498) cov=<c> n=<tokens> -- read by eye before any claim`.
Sibling, same-folder, known and adjudicated rows are printed but not posted. Recalibrate with `--calibrate`
whenever a reading reaches N3/N4 after two audits: add it to VERIFIED_PAIRS first.
Tests: `tools/tests/test_key_crossmatch_gate.py` (gate, verdict, value-frequency on a word code, --since selection,
changed_paths on a throwaway git repo) and `tools/tests/test_key_crossmatch.py` (unchanged), all offline.

---

## Repair pass (LANE KX job 1b, 25 Sept 2026) -- superseded by the section above; kept as the record

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
