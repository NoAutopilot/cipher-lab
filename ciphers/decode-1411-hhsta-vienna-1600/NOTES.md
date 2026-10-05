# decode-1411-hhsta-vienna-1600

Status: open
Kopal, "Two Encrypted Diplomatic Letters Sent by Jan Chodkiewicz to Emperor Maximilian II in 1574-1575", HistoCrypt 2023 (ecp.ep.liu.se histocrypt article 160), Table 1 and full-text search of the PDF for "182" read by this worker (GF-A2B-1, 3 Oct 2026): its five deciphered Kt. 14 Fasc. 20 letters sit at ff. 174, 194-198, 200-204, 205-208, 210-212, none at f. 182-192.

## What this is

DECODE R1411: Vienna, Österreichisches Staatsarchiv, HHStA, Staatskanzlei Interiora, Chiffrenschlüssel, Kt. 14,
Fasc. 20, f.182-192, 1600-1799, German cleartext/plaintext, Partially decrypted, 18 pages, at least 12 images
seen (free login). QUEUE.md row DC2 flagged an open question the brief repeats: establish first whether this
is a key record or a ciphertext record. Checked as part of LANE N check-solved batch DC1
(`.claude/briefs/runs/2026-09-24-lane-n-csDC1.md`).

## Check-solved sweep, 24 September 2026

1. **Record type.** `sources/decode/records-non-decrypted-2026-09-24-diff.tsv` and aaymeloglu/unsolved-ciphers's
   `catalogue/decode-catalog.csv` both give `record_type: Cipher` for id 1411 (not `Key`) — this answers the
   brief's open question: it is a ciphertext record, cryptanalysis kind, as QUEUE.md's DC2 row already had it.
2. **Aymeloglu.** `unsolved-ciphers/catalogue/decode-ranked.md` row: "| 5 | [1411](.../RecordsView/1411) | 1600
   | Österreichisches Staatsarchiv ... | | German | 18 | inline cleartext; 180 keys from the same collection
   within 20 years |". This id is absent from that file's "Already carrying a deciphered text in DECODE" list
   (checked directly), so per that scrape no "Deciphered text" document is attached. The neighbouring record
   R1410 (same box/fasc.) scores identically with the same "180 keys" signal — Aymeloglu's count of nearby
   DECODE Key records in the Kt.13-21 series within a 20-year window is large but not narrowed to this specific
   f.182-192 span.
3. **Tomokiyo.** `sources/cryptiana/web/habsburg.htm` describes the HHStA Kt.13/Kt.14 Chiffrenschlüssel
   collection at length (Láng 2020's description, ~500 keys across boxes 13-21) and cites several specific
   Kt.14 folio ranges (f.132-135/136-141 printed templates, f.291-302 Carolus Rym 1570, f.311-313) but none
   fall in this record's f.182-192 range — no match found for this specific folio span.
4. **Web.** WebSearch on Benedek Láng's 2020 HistoCrypt description of the Staatskanzlei key collection
   confirms the collection's general scope (boxes 13-21, ~480 keys in the first six boxes per Láng) but
   returned nothing folio-specific to Kt.14 f.182-192.
5. **Bourdeau.** dbourdeau/cyphersolver's `CATALOGUE.md`/`TARGETS.md`: no entry keys on DECODE id 1411. A
   coincidental hit on the bare number "1411" in `CATALOGUE.md` is a different archive's own shelfmark number
   (Hessisches Staatsarchiv Marburg, HStAM 4 h Nr. 1411, an unrelated Hesse-Kassel/Malsburg target) — checked
   and excluded as a false match, not this record.
6. **DECODE.** A prior LANE N pass this session read R1411's RecordsView page directly (QUEUE.md DC2 row): at
   least 12 images, Partially decrypted status, no attached key/transcription/decryption document found on the
   page itself.

## Verdict

**Open.** Partially decrypted status with 18 pages and no attached document on its own RecordsView page
(checked by a prior worker this session) is consistent with only part of the item having been read elsewhere,
not published. "180 keys from the same collection within 20 years" (Aymeloglu's own signal) is a real lead
worth following before any transcription pass: Láng 2020 is the named specialist description of the whole key
collection and should be read in full (not just searched) before deciding whether it, or another Kt.13-21
folio, names a key for this specific fasc./folio range.

Requests this pass: WebSearch 1, github.com 0 (reused shared clones). No fresh DECODE login this pass. No
promotion, no decoding.

## LANE N audit, 24 September 2026

DocumentsList check (`DocumentsList?showmaster=records&fk_id=1411`): **"No records found"** — no attached
key, transcription or decryption document. RecordsView's own field table: `Available Documents:` (empty),
`Inline Cleartext: Yes`, `Inline Plaintext: No`. Read together, this record's "Partially decrypted" DECODE
status is **not backed by any attached document here** — DECODE's own vocabulary most plausibly reflects that
the source pages carry inline cleartext passages around the cipher (a normal diplomatic-letter structure, not
a partial break of the cipher itself), the same distinction QUEUE.md's DC10 note draws for the Modena/Milano
cluster. Nothing here changes the verdict: still **open**, cryptanalysis, transcription is still the next
step. Status word unchanged.

Census diff regenerated this session (normaliser fix): R1411's `held_by` is now
`ours:decode-1411-hhsta-vienna-1600` (was `none`, folder did not exist when the stale diff was made) — pipeline
catching up, not a new finding.

## Web and blog check (GF-A2B-1, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `Chiffrenschlüssel Kt. 14 Fasc. 20 f. 182 Staatskanzlei Interiora cipher letter` -- archivinformationssystem.at
   StK Interiora series record (ID=332, series level only), Busse's Austrian Black Chamber PDF, Kopal's HistoCrypt
   2024 Charles V paper (article 704). Nothing at folio level for f. 182-192.
2. `DECODE record 1411 Haus- Hof- und Staatsarchiv Chiffrenschlüssel partially decrypted German` -- Kopal HistoCrypt
   2023 (article 160, opened, see Premise check (c)), Cipherbrain "unsolved cryptograms from the thirty years war 2"
   (Trauttmansdorff-Volmar dispatches; not this fascicle). No record-level page for R1411.
3. `HHStA Staatskanzlei Interiora Chiffrenschlüssel Karton 14 Fasz. 20 Chiffre Brief entziffert` -- Kopal 2023 and
   2024 again; Hungaricana BecsSeg (Vienna-held Hungarian records, unrelated). No hit.
4. `Láng Benedek Vienna cipher key collection Staatskanzlei Interiora Chiffrenschlüssel HistoCrypt Fasc. 20 letters`
   -- Láng 2020 HistoCrypt description (cited in Kopal 2023's bibliography), Láng's Frank "chiffre indéchiffrable"
   paper (article 400, opened: Tuscany, 18th c., not this item), Real Life Cryptology (Láng 2018). No folio-level hit.
Blog site searches:
5. Cipherbrain (`site:scienceblogs.de klausis-krypto-kolumne` + HHStA/Chiffrenschlüssel/Wien): "unsolved cryptograms
   from the thirty years war 2" (2018-10-21; Trauttmansdorff, a different item), monthly archives. Also surfaced: Top 50
   no. 27 Ferdinand III letters and the 2017-10-07 Thomas Ernst follow-up -- Ferdinand III's own letters, not Kt. 14
   Fasc. 20 f. 182-192. No post or comment naming this fascicle or R1411.
6. Cryptiana (`site:cryptiana.blogspot.com Vienna Staatskanzlei Chiffrenschlüssel`): no cryptiana.blogspot.com hit;
   Tomokiyo's habsburg.htm (on disk, sources/cryptiana/web/) already checked on 24 Sept: no f. 182-192 citation.
7. Cipher Mysteries (`site:ciphermysteries.com Vienna Haus- Hof- und Staatsarchiv cipher letter Habsburg`): no
   ciphermysteries.com hit returned; results were the HistoCrypt papers and Cipherbrain posts above.
No decipherment or plaintext of R1411 found in any post or comment thread. Requests: WebSearch 7, ecp.ep.liu.se 2 (PDFs).

## Premise check (GF-A2B-1, 3 Oct 2026)

(a) Folder's own mentions -- found (signal, not a decipherment): DECODE status "Partially decrypted" with `Inline
Cleartext: Yes` and DocumentsList "No records found" (LANE N audit above); no decipherment document to open.
(b) Other solvers' working files -- not found for R1411. Shallow clones 3 Oct 2026: dbourdeau/cyphersolver (HEAD
e8b4287, 2 Oct): `targets/warsaw/` works R1408 (f. 176) and fetched DECODE images of R1409 (f. 178) and R1410 (f. 181,
"a German letter with inserted code numbers"), plus key records R1392-R1406; R1411 is not fetched or rendered there,
and no apply-key script names it. `targets/chodkiewicz1575/` works R1473 (ff. 210-212). aaymeloglu/unsolved-ciphers
(HEAD d2800bb, 27 Sept): R1411 only in `catalogue/decode-ranked.md`/`decode-catalog.csv` (cited, not copied).
(c) Physical neighbours -- found (context, not this item): Kopal and Waldispühl (Cryptologia 2021) and Kopal
(HistoCrypt 2023) deciphered five letters of this fascicle, Maximilian II's and Chodkiewicz's of 1574-75 on the
Polish election, at ff. 174 (letter C), 194-198, 200-204, 205-208 and 210-212, keys "Cyffra nova ad Poloniam" (1572,
two copies in DECODE) and a Dudith-type key; plaintexts are said to be in DECODE. R1411's f. 182-192 sits inside
that run, between letter C and letter B, so it may belong to the same 1575 Polish correspondence and key family;
not seen at native resolution this pass (DECODE images, no login used). R1410 at f. 181 is German with code numbers
(Bourdeau's description).
(d) Recipient-side editions -- not searched beyond the web pass: Augustynowicz 2001 (Habsburg candidates, second
interregnum) and Dudith, Epistulae 4 (1575, ed. Kotońska 1998) are the editions Kopal names; neither opened here.

## While waiting

Next action that depends on nobody (GAPS157, 3 Oct 2026): pre-register r at residue 21 as an alternative table beside the
frozen one, then cut and read the unused numerals (p.2 left lower half, p.2 right page) in two blind Opus passes and test
both tables against the shuffled-target and shifted-rule controls only (controls-vs-decode, no language-judge gate: the
judge is retired for this leaf, GAPS157). The language reading itself waits on ASKS row 120 (a person's read of the gloss).

## GAPS136 step: Cipherbrain Ferdinand III posts (3 Oct 2026, account-4)

Step run: NEXT-STEPS.tsv row 42 ("27 Ferdinand III letters and the 2017-10-07 Thomas Ernst follow-up"). That row is a
parse artefact: `tools/next_steps.py`'s next-step regex (line 79) matched the word "follow-up" in the Web and blog
check above, whose own sentence already says these are Ferdinand III's own letters, not this fascicle. Run anyway as
a cheap check, since the comment threads had not been read for this item.
- Top 50 no. 27 (scienceblogs.de/klausis-krypto-kolumne/2017/07/07/...-27-ferdinand-iiis-encrypted-letters/): a
  1640-07-20 letter from Ferdinand III to his brother Leopold Wilhelm (supplied by Leopold Auer) and a second of
  1641; numbers plus geometric-symbol pairs. No archive shelfmark given in the post.
- Follow-up 2017-10-07 (.../top-50-crypto-mystery-solved-thomas-ernst-deciphers-fredinand-iiis-encrypted-letters/):
  Ernst's solution (symbol = count of its strokes, AEIOU vowel pattern, "PICCOLOMINEA"). No shelfmark.
- Post body and comment threads of both, searched for Kt. 14 / Fasz. 20 / f. 182-192 / R1411 / Chodkiewicz /
  Maximilian II / Poland 1574-75: **not found**. The letters are 1640-41 private Habsburg correspondence in a
  numbers+symbols design; this record sits inside a run of 1574-75 Polish-election letters (Premise check (c)).
  Not found to be the same item; R1411's images were not seen this pass, so the design comparison is not made.
No decipherment of R1411 found. Requests: WebSearch 1, scienceblogs.de 2. Vision calls 0. No DECODE login.

Next step: one DECODE browser login (`tools/decode_browser_login.js 1411 <dir>`) to fetch R1411's images and check
the leaves against the "Cyffra nova ad Poloniam" key and Kopal's letters A-E (ff. 174-212), per "While waiting" above;
~$2, one login per session.

## GAPS137 step: DECODE images and the "Cyffra nova ad Poloniam" test (3 Oct 2026, account-4)

One DECODE browser login (tools/decode_browser_login.js 1411, --guess-fullsize; account name scrubbed from the saved
record page, 4 occurrences). DECODE served 12 full-size images (3456x4608 PNG, I6595-I6606) of the record's 18 pages;
sha1, size and URL of each are in images/manifest.json. The full-size files (~160 MB) are not committed (30 MB folder
rule); the 200 px thumbnails, the scrubbed record page and two reduced crops of p.1 are. The first browser attempt failed
before reaching the login form (Chromium ERR_CERT_AUTHORITY_INVALID; NSS store lacked the proxy CA in this container,
fixed with the CLAUDE.md certutil step), so only one login was made.

**Pre-registered gate (written before any decode was attempted).** Step 1, inventory: R1411's cipher signs must be of
the same class as the key's -- Kopal 2023 (HistoCrypt art. 160, pp. 2-3, read this session) describes "Cyffra nova ad
Poloniam" (1572) as a homophonic substitution of about 80 graphic signs ("astrological signs, Greek letters, and
esoteric symbols") with Latin clear-word code names ("Benigni", "Ater"). If R1411's cipher is not in graphic signs of
that kind, the key is inconsistent and no transcription, decode or judge is run.

**Result: inconsistent; gate stops at step 1.** R1411 (images/p1_top_gloss.jpg, p1_mid.jpg; contact sheet of all 12
seen) is German cursive with inserted numeral groups separated by commas or dots, values seen on p.1 from 4 to 96
(e.g. "80, 57, 41, 89, 9, 04, 77, 09 ..."), plus a few isolated graphic marks (a circled cross and two other single
signs used like word or name codes). The cipher alphabet is Arabic numerals, not the Kopal graphic-sign set. No decode
was attempted.

**Control.** The brief named a shuffled-key control. For this statistic (sign class: numerals vs graphic signs) a
shuffled key cannot differ from the real one -- permuting the key's plaintext values does not change which sign class
it uses -- so that control is a non-test by construction (rule 3) and was not run. Not needed either: the mismatch is
in the key's own sign set, not in a score.

**What the images show instead (the main finding of the step).**
- Page 1 carries interlinear letters written above many numeral groups, in the same or a near hand: a period
  decipherment of part of the cipher. Read off the crop (unverified, grade M until a transcription pass): over
  "5, 17, 63, 77, 65, 11, 57, 95" the letters "a n l a n g e t" (anlanget); over "35, 81, 73, 13, 70, 22, 9" the letters
  "g e p i s t e"; over "29 41 61 ... 65" a longer run beginning "a n ...". Letter e appears over 81 and 9 and
  n over 41 and 65, so the system is homophonic on about 1-99. This is most plausibly what DECODE's "Partially
  decrypted" refers to.
- Clear words around the cipher: "Herr Reichs Canceler", "mein gnädiger Herr", "Rath und Bürger deputirten",
  "fortification", "Kön. Maij.", "Erb. Rath", "lit. A B C D E F G" (labels of enclosures, "Beylage lit. A ... G"; not a
  key), "Expeditionibus". A Reichskanzler addressed together with a royal Majesty and a town council points to a
  17th-century Swedish or Polish-Prussian context rather than the 1574-75 Maximilian II letters (inference, grade I;
  the date line was not read this pass).
- Several leaves (pp. 4-9) are drafts with heavy corrections and crossings-out; pp. 10-12 include a mostly blank leaf,
  the folio number 192 and an endorsement.

Token grades: no reading claimed. The interlinear letters quoted above are M (read from a reduced crop by this worker,
no second pass). Vision: 3 image reads by the worker itself (contact sheet, two crops of p.1), 0 subagent calls.
Requests: de-crypt.org 26 (1 login, record page, 24 image files), ecp.ep.liu.se 2 (Kopal article page and PDF),
github.com 1 (shallow clone of dbourdeau/cyphersolver to read targets/warsaw/NOTES.md, R1392-R1406 descriptions; cited,
not copied).

Next step: transcribe p.1 (and any other glossed page) as numeral groups with their interlinear letters, using
tools/iiif_lines.py --image on the full-size file, two blind passes; build the (number -> letter) table from the pairs
with tools/interlinear_align.py or a direct pair count, and check each number's letter is consistent across its
occurrences (a shuffled-pairing control can vary here). ~$4-6 at the current per-pass rate (2 passes + 1 reconcile).
Status unchanged: open.

## GAPS141 step: p.1 interlinear gloss -> numeral/letter table, held-out gate (3 Oct 2026, account-4)

Step run: GAPS137's next step. One DECODE browser login re-fetched only p.1 (IMG_R1411_I6595_P1.png, sha1 126a2f4c...
matches images/manifest.json; the first attempt failed at Chromium's certificate check before the login form, fixed with
the CLAUDE.md certutil step, so one login in all). Pre-registration committed before either pass was read:
`gloss/PREREG.md` (b05312da).

Crops (pasted command): `python3 tools/iiif_lines.py --image IMG_R1411_I6595_P1.png --out <dir> --region 380,660,3076,760
--prefix p1g --centres 70,195,310,405,645 --top-margin 45 --bottom-margin 35 --max-width 1600 --overlap 200 --debug`
-> 15 crops (5 glossed numeral lines x 3 segments), committed in `images/p1g_crops/` with their manifest.
Two blind Opus passes (one call each, crops only): `gloss/passA.tsv`, `gloss/passB.tsv`. `tools/reconcile_passes.py`:
numbers 62/62 agree (100%), glosses 60/62 (96.8%); the two gloss splits (L01 pos 8 u-with-ring vs u; L05 pos 9 "a?" vs
"a") settled from the crops by the worker. Reconciled pairs: `gloss/pairs.tsv` (62 numbers, all glossed; 54 grade C, 8
grade M where a pass marked the number or letter doubtful). Table and gate: `gloss/gloss_table.py` (`--check` exits 0),
writing `gloss/table.tsv` and `gloss/heldout.txt`.

**Table (grade C, period gloss; 54 clean pairs, 39 distinct numbers, 14 letters).** Homophones: a=4 (5 29 53 77),
d=3 (8 32 80), e=3 (9 33 81), g=5 (11 35 59 68 92), i=3 (13 61 85), m=3 (16 64 88), n=4 (17 41 56 65), s=5 (12 36 50
70 94), t=3 (22 23 95), z=2 (21 93), o=1 (42), p=1 (19), u=1 (48), ů=1 (66). Conflicts on the page, both passes agreeing
on number and letter: 56 = n (L02) and d (L03); 66 = ů (L01) and o (L03). 22 = t at L01 pos 6 (under a heavy, possibly
corrected "t") against 22 = s at L01 pos 16 (that number marked doubtful by pass B, so excluded). These are logged as data
conflicts (rule 4), not settled by majority.

**Held-out gate (pre-registered): NON-TEST at this N.** Fit on the first 27 clean pairs (23 numbers), test on the last
27: coverage 7/27 = 0.259, accuracy 5/7 = 0.714; value-shuffled fit table (10,000 draws, seed 1411): mean 0.079, p99
0.429, max 0.714, 1 draw >= real. Covered test pairs 7 < the pre-registered 8, so the gate reads NON-TEST (too few
repeats across 5 lines), not a negative and not a PASS. No "reading ready" flag. Secondary (descriptive, no gate):
self-consistency 24/26 = 0.923 over repeated numbers vs position-shuffled glosses mean 0.478, p99 0.577.

**Post-hoc observation (seen after the score, not a tested result; hypothesis for the next step).** Numbers congruent
mod 24 carry the same gloss letter in almost every case: residue 5 = a (7/7), 9 = e (7/7), 13 = i (5/5), 17 = n (6/6),
23 = t (4/4), 8 = d (4 of 5), 11 = g (4/4), 16 = m (3 of 4, the odd one the doubtful "40?" which looks like 70 on the
crop), 15 = l (2/2), 21 = z (2/2). Read as residue -> letter, most values sit on a 24-letter alphabet starting a = 5 (c 7,
d 8, e 9, g 11, i 13, l 15, m 16, n 17, p 19, t 23), with exceptions (12/36 = s, 20 = g, 21 = z, 1 = p, 2 = s). Under
that rule 56 (res 8) is d and 22 (res 22) is s, matching one side of each logged conflict. A mod-24 rule would cover all
of 1-99 from this one page. Because it was found on these same 62 pairs, testing it on them is contaminated; it needs
fresh material.

Token grades (rule 4): no reading claimed; 54 C, 8 M (the gloss pairs themselves). Vision: 2 subagent calls (Opus 5.5,
crops only) + 2 worker image reads for the reconciliation, plus 3 worker reads to place the crops. Requests: de-crypt.org
3 (1 login, record page, 1 image).

Next step: pre-register the mod-24 residue rule (table from these 62 pairs, frozen), then transcribe the unglossed
numerals of p.1's lower block (y 2300-3600, about 9 lines, one blind Opus pass + one check pass on line crops, ~$4)
and score the rule's decode with tools/judge_plaintext.py against a German corpus of the period (check tools/data for an
era-matched de17 corpus first, rule 3) with the shuffled-target decode beside it. Status unchanged: open.

## GAPS146 step: frozen mod-24 residue rule tested on unglossed numerals (3 Oct 2026, account-4)

Step run: GAPS141's next step. Pre-registration `residue/PREREG-GAPS146.md` (commit 78d550f4) pushed before any unglossed
numeral was read: rule `residue/rule.py` -> `residue/frozen_table.tsv`, letter(n) = T[n mod 24], T from the 54 grade-C
glossed pairs only (majority letter per residue; 8 unseen residues from the 24-letter alphabet with a = 5). Conflicts as
declared: 56 n/d -> residue 8 = d (4 vs 1); 66 u-ring/o -> residue 18 = o (2 vs 1); 22 t vs 70/94 s -> residue 22 = s
(2 vs 1). Frozen T has no h and no r (residue 12 = s and 21 = z from the glosses), declared as a weakness before scoring.

One DECODE browser login (tools/decode_browser_login.js 1411, three explicit full-size fetches P1-P3; sha1 of P1 and
sizes of P2/P3 match images/manifest.json). Crops (pasted commands; automatic line finding found 0 lines on this grey
scan, so centres were set from the --debug overlays and checked on them):
`python3 tools/iiif_lines.py --image IMG_R1411_I6595_P1.png --out images/gaps146_crops --region 560,1350,2540,2300
--prefix p1L --centres 115,715,993,1128,1239,1366,1494,1652,1795,1930,2060,2215 --top-margin 60 --bottom-margin 55
--max-width 1400 --overlap 200 --debug` (24 crops, 12 lines) and
`python3 tools/iiif_lines.py --image IMG_R1411_I6596_P2.png --out images/gaps146_crops --region 700,100,1740,1200
--prefix p2L --centres 95,187,301,416,508,622,720,840,949,1041,1134 --top-margin 55 --bottom-margin 55 --max-width 2400
--debug` (11 crops). Deviation from the pre-registration: p.1's unglossed numerals (about 95) were under 150, and only
the upper half of p.2's left page (11 lines) was added, not the whole page, to stay inside the cap.

Two blind Opus 5.5 passes, one call each, crops only (`residue/passA.tsv` 182 rows, `residue/passB.tsv` 183 rows):
identical on 14 of 23 lines. The worker settled the rest from the crops: two "2?" read only by B are letter strokes ("wer",
"zu") and were dropped; A's "20?" on p2L_L03 is a superscript over "die" and was dropped; p1L_L07 positions 2 and 10
(A 29?, B 79) are 79; p1L_L03 position 6 (A 64, B 04) stays unsettled as 64? (M). Reconciled: `residue/numbers.tsv`,
176 cipher numbers, 11 graded M (either pass doubtful), plus 4 graphic signs (#) and one in-text figure (25000), which
were not decoded.

**Score (`residue/score.py`, `--check` exits 0; tools/data/de17, N = 176 letters):** decode -1.551; judge real_p05 -0.854,
real_p01 -0.994, real median -0.747, null_p99 -1.889; shuffled-target decode (200 draws, seed 146) mean -2.225, p99
-2.036, 0 of 200 >= real; shifted rules k = 1..23 best -1.980 (k = 11), 0 of 23 >= real. tools/judge_plaintext.py
residue/judge_spec.json --file residue/decode_letters.txt:
```
FAIL language: score=-1.551, null_p99=-1.889, real_p05=-0.854, real_median=-0.747, mode=both, N=176
FAIL - decode-1411-hhsta-vienna-1600 GAPS146 residue decode (a PASS is a gate for a verifier, not a reading; rule 10)
```
**Pre-registered verdict: CONTROLS BEATEN, JUDGE CANNOT DECIDE.** The frozen rule beats the shuffled target and all 23
shifted rules by a clear margin (0.43 above the best shift) on numerals it was not built from, but stays far below the
real-text 5th percentile (and the 1st). de17's own leave-one-file-out false-negative rate is 38.2 pct at N=300 with per-fold
spread 4.0-97.0 pct (holdout_de17_N300.log) and 41.4 pct at N=1090 (13.0-100.0 pct), so its FAIL is of unknown reliability
(rule 3). Not a negative; no reading-ready flag; status unchanged.

Decode, per line (lower case = number agreed by both passes; upper case = M): p1L_L01 uze; L02 kziegeszatb; L03
denneMazkA; L04 ltezeuez; L05 opensagen; L06 dannen; L07 ScszsfFlicg; L08 lanes; L09 gesandtan; L10 pzopoSet; L11
attzibuezeto; L12 bsIdionges; p2L_L01 andten; L02 zespecceGem; L03 denneMK; L04 adsia; L05 Gescssta; L06 zal; L07 enkonte;
L08 obnigat; L09 so; L10 lgaaesCaabgef; L11 uzetu.

**Post-hoc observation (seen after the score; not tested, not applied):** several runs read as German or Latin chancery
words if the table's z (residue 21) is read r and its b/s at residues 6/12 are read h: "kziegeszatb" ~ kriegesrath,
"pzopoSet" ~ propo(n)et, "attzibuezeto" ~ attribuereto, beside "gesandtan", "dannen", "opensagen". This fits the gloss
writer's r having been read as z by both GAPS141 passes (a common confusion for a period German r), which would also give
the missing r. This is a hypothesis for the next step. Testing it on these 176 numbers would be contaminated.

Token grades (rule 4): the 62 glossed pairs stay C 54 / M 8 (GAPS141). The 176 decoded numbers are graded M (the gate did
not pass, so none are S); no reading is claimed. H 0, C 0 new, S 0, M 176, I 0. Vision: 2 subagent calls (Opus 5.5, crops
only) + 5 worker image reads (two page overviews, two debug overlays, three crops to settle splits, counted as one
reconciliation unit). Requests: de-crypt.org 5 (1 login, record page, 3 images).

Next step: (1) a blind paleographic pass over the GAPS141 gloss crops asking only "is this letter r or z, h or s/b"
(1 Opus call, ~USD 1.5), (2) a corrected table frozen in a new pre-registration from that pass, (3) the numerals not yet
used (p.2 left lower half, p.2 right page = f.183) cut and read in two blind passes, then the same three controls plus de17.
~USD 6. Status unchanged: open.

## GAPS150 step: blind re-read of the r/z and h/s gloss letters; gloss-text calibration (3 Oct 2026, account-4)

Step run: GAPS146's next step (1). Pre-registration `gaps150/PREREG-GAPS150.md` (commit fbb9a7fc) pushed before the re-read
and before any score: probe list, decoy check, and the only rule for changing the frozen table (a residue changes only if
the blind letter is read at H/M confidence at a strict majority of its C positions; L or "?" counts as agreeing).

Blind re-read: one Opus 5.5 subagent call, the 9 existing gloss crops of L01/L03/L05 only, a neutral letter-shape sheet,
15 probes given as line + n-th number + value (9 in question, 6 decoys), no words, table or prior reading shown. Result
`gaps150/reread.tsv`: decoys 6/6 agree with gloss/pairs.tsv (e, d, n, d, a, g). Residue 21 (21, 93): both read **r at L
confidence** ("2"/"z" form, no descender; "z equally possible"). Residues 12 (36, 12), 2 (50), 22 (70, 94, 22?): the
recurring "5"-like form, read **s at M** ("h without its ascender the alternative"); 22 at L01 6th read t (H), as before.
**Under the pre-registered rule no residue changes** (r only at L); the revised table equals the frozen table, so one decode
is reported. Residue 6 (b) has no gloss and was not testable by this step (declared in the prereg). No re-read disagreed
with pairs.tsv at H/M, so the 54 C / 8 M gloss grades stand; the r-vs-z reading of residue 21 is logged as an open
palaeographic question (L-confidence r against the GAPS141 passes' z), not a data conflict.

**Score (`gaps150/score150.py`, `--check` exits 0; de17; the frozen table, controls re-drawn with seed 150):** decode N=176
-1.551; real_p05 -0.854, real_p01 -0.994, null_p99 -1.889; shuffled-target mean -2.218, p99 -2.002, 0/200 >= real; shifted
rules max -1.980, 0/23 >= real. Gate: FAIL on the judge (below real_p05 and p01), controls beaten -- the GAPS146 verdict
reproduces. de17 leave-one-file-out: N=300 false-negative 38.2 pct blended, per fold 4.0-97.0 pct; N=1090 41.4 pct, 13.0-100.0
pct. tools/data has no 16th-c./c.1600 German chancery or newsletter corpus (de16 is a model-composed 8.5 KB text); **the judge
is of unknown reliability here** (rule 3).

**Calibration (rule 3, ZX-DEC349): the leaf's own period gloss text** (`gaps150/gloss_text.txt`, the 62 gloss letters of
L01-L05 as reconciled, u-ring as u) through the same judge:
```
FAIL language: score=-1.524, null_p99=-1.748, real_p05=-0.911, real_median=-0.756, mode=both, N=62
```
Its own letter-shuffled controls: mean -2.195, p99 -1.877. The genuine period plaintext of this leaf, as our passes
transcribe it, scores -1.524 -- essentially where the decode sits (-1.551) and just as far below real_p05. So de17's FAIL
on the decode says nothing about the key: the judge cannot recognise this leaf's own text under our transcription convention
("judge cannot decide", not a negative). Both scores sit well above their shuffled controls.

Exploratory, not pre-registered and not licensing anything (r at residue 21 in place of z, the change the re-read leaned to
at L only): decode -1.308, gloss text -1.463. Both rise together, which is the shape a correct letter value would give, but
the change was chosen after seeing these same 176 decodes; the fresh p.2 numerals are the test.

Token grades (rule 4): no reading claimed; the 176 numbers stay M (H 0, C 0 new, S 0, M 176, I 0); gloss pairs C 54 / M 8
unchanged. No reading-ready flag. Vision: 1 subagent call (Opus 5.5, 9 crops), 0 worker image reads. Requests: none
(all crops on disk).

Next step: pre-register r at residue 21 as an alternative table beside the frozen one (both frozen before reading), then cut
and read the unused numerals (p.2 left lower half, p.2 right page) in two blind Opus passes and score both tables with the
shuffled-target and shifted controls; report the gloss-text calibration beside de17 every time (or build a c.1600 German
chancery corpus, ~12 min, V6-PTCORP pattern, so the judge can decide). ~USD 6. Status unchanged: open.

## CORP-DE16 step: era-matched judge corpus de1600 built; gloss calibration (3 Oct 2026, account-4)

Built `tools/data/de1600` (LANG_CORPORA "de1600"): six archive.org source-edition volumes printing German princely letters
and chancery acts of 1575-1610 in their own spelling (Bezold, Briefe des Pfalzgrafen Johann Casimir I-II; four volumes of
Briefe und Acten zur Geschichte des Dreissigjaehrigen Krieges), period-spelling filtered, 1.15M folded letters. Leave-one-file-
out false-negative rate: N=176 30.5 pct blended, per fold 17.0-56.5 pct; N=62 23.9 pct, 15.0-44.5 pct (de17 at N=176: 38.9 pct,
13.5-91.0 pct). Wide spread: a FAIL/PASS against de1600's real_p05 is of unknown reliability (rule 3). See its README.

Calibration only (no decode scored): the leaf's own 62-letter gloss text scores -1.423 under de1600 (FAIL; real_p05 -0.917,
null_p99 -1.731, letter-shuffled mean -2.111, max -1.773) against -1.524 under de17. Under every leave-one-out model it sits
below 199-200 of 200 genuine held-out 62-letter windows. **The era corpus is not what was keeping the judge from deciding**:
the gloss as transcribed is still far from period prose. The open r/z and h/s letterforms (GAPS150) and abbreviations in the
transcription are the likelier limit. A gate on the decode should compare it with the gloss's own score and with the shuffled
controls under de1600, not with real_p05 alone. Script: `tools/data/de1600/gloss_calibration.py`. Status unchanged: open.

## GAPS157 step: one spelling normalisation on corpus, gloss and decode; registered verdict C (3 Oct 2026, account-4)

Pre-registration `gaps157/PREREG-GAPS157.md` (commit 7c9169ee) pushed before any normalised score. Normalisation N
(`gaps157/score157.py` `norm`): the judge's fold (case, accents, ss, abbreviation marks and all non-letters removed), then
v->u, j->i, y->i, and every run of one letter collapsed to one; applied identically to every corpus file before the 4-gram
model is built, to the gloss (62 -> 61 letters), to the frozen-table decode (176 -> 167), to 200 shuffled-target decodes
(seed 157) and to the 23 shifted-rule decodes. No letter value of the frozen table changed. `--check` exits 0.

| corpus, form | gloss score | gloss real_p05 | real windows <= gloss | gloss letter-shuffled p99 | decode | decode real_p05 | shuffled-target p99 (>= decode) | shifted max (>= decode) |
|---|---|---|---|---|---|---|---|---|
| de1600 raw | -1.423 | -0.917 | 0/200 | -1.803 | -1.635 | -0.876 | -2.008 (0/200) | -2.004 (0/23) |
| de1600 normalised | -1.310 | -0.912 | 0/200 | -1.731 | -1.592 | -0.858 | -1.925 (0/200) | -2.044 (0/23) |
| de17 raw | -1.524 | -0.911 | 0/200 | -1.859 | -1.551 | -0.854 | -2.005 (0/200) | -1.980 (0/23) |
| de17 normalised | -1.473 | -0.907 | 0/200 | -1.786 | -1.546 | -0.885 | -1.937 (0/200) | -2.050 (0/23) |

Normalisation lifts the gloss by 0.11 (de1600) and 0.05 (de17) and the decode by 0.04 and 0.01, but the leaf's own period
gloss still sits below every one of 200 genuine windows of its length under both corpora, about 0.4 below real_p05.
**Registered verdict C: the judge cannot recognise this leaf's text even normalised.** Spelling convention (u/v, i/j, y,
doubled letters, abbreviation marks) is not the gap; the remaining suspects are letter identities in the gloss
transcription itself (r/z, h/s, GAPS150) and the gloss being too short or too abbreviated to be prose to a 4-gram model.
The language judge is retired as a gate for this leaf (rule 3 third-attempt clause: de17, de1600, de1600 normalised, all
on the same gloss, every number moving together but none near the gate) -- untested-by-this-tool, not a negative. The
decode beats its shuffled-target and shifted-rule controls by 0.33-0.45 under all four settings (0/200, 0/23), as in
GAPS146/GAPS150; that licenses only "the frozen table is better than its own permutations", not a reading.

Next instrument: a person's read of the 62-letter gloss (ASKS row 120: what German words the five gloss lines spell, and
whether the letters read z and s are r and h), not a further machine pass. Token grades unchanged: H 0, C 0 new, S 0,
M 176, I 0; gloss pairs C 54 / M 8. No reading-ready flag. Vision: 0. Requests: none. Status unchanged: open.


## DEF1-1411 step: T and T21r (r at residue 21) frozen, tested on unused p.2 numerals (5 Oct 2026, account 1)

Step run: GAPS150's named next step and the brief DEF1-1411 (LANE DEFAULT-account-1-20261005-2039). Pre-registration
`def1411/PREREG-DEF1-1411.md` (commit 6cf4ff3c1) pushed before any new numeral was read: T = residue/frozen_table.tsv
unchanged; T21r = T with residue 21 = r (`def1411/tables.py`). The 176 GAPS146 numbers were not rescored (contaminated for
the r question).

One DECODE browser login (tools/decode_browser_login.js 1411 --fetch IMG_R1411_I6596_P2.png, --max-files 1); sha1
2e022ab8... matches images/manifest.json; not committed (30 MB rule). Crops (pasted commands; automatic line finding found
0 lines on this grey scan, as in GAPS146, so centres were set by eye from --debug overlays; a first cut with misplaced
centres was discarded before any pass):
`python3 tools/iiif_lines.py --image IMG_R1411_I6596_P2.png --out images/def1411_crops --region 700,1270,1740,1650 --prefix
p2Lb --centres 60,266,353,462,663,750,848,1049,1152,1261,1375,1592 --top-margin 45 --bottom-margin 40 --max-width 2400 --debug`
(12 crops, p.2 left page below the GAPS146 p2L lines, numeral-bearing lines only) and
`python3 tools/iiif_lines.py --image IMG_R1411_I6596_P2.png --out images/def1411_crops --region 2600,120,1880,1720 --prefix
p2R --centres 118,217,300,388,511,582,676,776,1099,1187,1275,1475,1569,1675 --top-margin 45 --bottom-margin 40 --max-width
2400 --debug` (14 crops, right page = f.183, numeral-bearing lines; its lower half is clear text). All crops < 2500 px wide.

Two blind Opus passes, one call each, crops only, opposite reading orders (`def1411/passA.tsv` 198 numeral tokens, 14 "?";
`def1411/passB.tsv` 202, 11 "?"): identical on 13 of 26 lines; most splits were a "?" flag on one side only. The worker
settled the rest from the crops (one reconciliation unit; `def1411/reconcile_notes.tsv`): three B-only "10?"/"2." tokens
are words or an enumeration and were dropped; p2Lb_L01 pos 9 = 53 (A 83?); p2R_L06 pos 3 = 19 (A 29?); p2R_L09 pos 5 = 13
(B 17); p2R_L13 pos 1 = 3 (A 7?, B 3?) and pos 5 = 20 (A 70, B 20?). Settled splits and every "?" are graded M. Dates
("9 Octob", "13 huius", "2./5. Octob") are in-text and not decoded. Reconciled: `def1411/numbers.tsv`, **195 cipher numbers,
17 M**, 8 with residue 21.

**Step 0 (ARM-C1), run before the target:** a shuffled copy of the 195 numbers (seed 1411) through tools/judge_plaintext.py:
```
T:    FAIL language: score=-2.218, null_p99=-1.847, real_p05=-0.866, real_median=-0.768, mode=both, N=195
T21r: FAIL language: score=-2.186, null_p99=-1.847, real_p05=-0.866, real_median=-0.768, mode=both, N=195
```
Neither shuffled decode passes, so the judge is not void here.

**Score (`def1411/score1411.py`, `--check` exits 0; de1600 raw; seed 1411):**

| table | decode | shuffled-target p99 (>= decode) | shifted max (>= decode) | gloss (-1.423) minus... | PASS |
|---|---|---|---|---|---|
| T | -1.727 | -1.987 (0/200) | -2.039 (0/23) | decode 0.304 below gloss | no |
| T21r | -1.600 | -1.963 (0/200) | -2.038 (0/23) | decode 0.178 below gloss | no |

Judge at N=195: real_p05 -0.866, real_p01 -0.978, null_p99 -1.847. tools/judge_plaintext.py on the target decodes:
```
T:    FAIL language: score=-1.727, null_p99=-1.847, real_p05=-0.866, real_median=-0.768, mode=both, N=195
T21r: FAIL language: score=-1.6, null_p99=-1.847, real_p05=-0.866, real_median=-0.768, mode=both, N=195
```
**Pre-registered verdict: CONTROLS BEATEN, JUDGE CANNOT DECIDE, for both tables** (each beats its shuffled target and all
23 shifts on numerals neither was built from, but neither reaches the leaf's own gloss score). No PASS: no grade moves.

**Residue-21 letter test (pre-registered, 8 occurrences >= 5): r favoured.** With every other residue fixed, r ranks
1st of 24 letters for residue 21 (top five r, l, i, e, n), z ranks 14th. This settles the GAPS150 open question in favour of
r on fresh material (cryptanalytic, conditional on this transcription); T21r is the preferred table for any later step.
The gloss pairs at 21 and 93 stay graded C as glossed "z" (a letter-identity question about the gloss hand, now answered by
the decode statistic, not by a re-read).

Decode under T21r, per line (lower case = clean; upper case = M): p2Lb_L01 nsersOgDAten; L02 dpniscseR; L03 tros; L04
oBsougcKen; L05 gesTAt; L06 ePzogru; L07 den; L08 uaser; L09 ngEedkonig; L10 reicsen; L11 ostsee; L12 dani; p2R_L01 mar;
L02 isbaltics; L03 sogkecap; L04 itulatIon; L05 gogdacesca; L06 CaPtainuog; L07 ckmacobleute; L08 nundsolken; L09 sesgI;
L10 one; L11 agenren; L12 aommeiss; L13 YfyuGuonasneA; L14 ndenn.

**Post-hoc observation (seen after the score; not tested, licenses nothing):** runs read as words of a Baltic-trade/naval
context: "konig", "ostsee", "dani|mar is baltic(i)" across the page turn (p2Lb_L12 -> p2R_L01), "cap|itulation" across a line
break (p2R_L03 -> L04), "captain", "...leute", "und solchen" (nundsolken). Runs continuing across line and page breaks
support the reading order used. "reicsen" and "isbaltics" fit residue 12 or 22 standing for h (reichsen?/baltichs?) rather
than s, the GAPS150 h/s question, untested here. These words are hypotheses for a verifier or a person's read; the
language judge, retired for this leaf by GAPS157, cannot gate them.

Token grades (rule 4): new 195 numbers all M (H 0, C 0 new, S 0, M 195, I 0); 176 GAPS146 numbers M; gloss pairs C 54 /
M 8 unchanged. No reading-ready flag. Vision: 2 subagent calls (Opus, 26 crops each) + 1 reconciliation unit (2 stacked
crop views) + 4 worker placement views (overview, 2 grids, 1 debug overlay check, 1 crop check). Requests: de-crypt.org
about 3 (1 login, record page, 1 image).

Next step: a different instrument from the retired 4-gram judge -- pre-register a word-coverage test (tools/judge_plaintext.py
NgramModel.cover on a de1600 + Latin chancery lexicon) of T21r against the same shuffled-target/shifted controls, with the
h-at-residue-12/22 alternative frozen beside it, on numerals not yet read (p.3, IMG_R1411_I6597_P3.png, and any later
cipher page), two blind passes; ~USD 6. In parallel, ASKS row 120 (a person's read of the gloss) stands. Status unchanged:
open.

## Remaining gaps (DEF1-1411, 5 Oct 2026)
Read so far: 0 of about 371 cipher numbers at S or better (gloss pairs C 54 of 62; 371 unglossed numbers M)
- unglossed numerals p.1-p.2 (371) - blocker: not-attempted; controls beaten but no gate passed (GAPS146, GAPS150, DEF1-1411); next: pre-registered word-coverage test of T21r (+ h alternative) on p.3 numerals, ~$6
- gloss letter identities h/s at residues 12/22 - blocker: waiting-on ASKS row 120 (a person's read of the gloss); the r/z question is settled by the DEF1-1411 residue-21 test
- pages 3-12 numerals - blocker: not-attempted; full-size images fetched in GAPS137 but no page after p.2 transcribed; next: cut and read p.3 numerals in two blind passes with the step above, ~$6

## Escalation (DEF1-1411, 5 Oct 2026)
- [x] siblings: GAPS136/GAPS137 checked the Ferdinand III posts and the Kopal Cyffra nova key (inconsistent sign class)
- [x] clear-pages: clear words around the cipher read in GAPS137; context words used only as post-hoc observation
- [x] known-keys: Cyffra nova ad Poloniam tested in GAPS137, inconsistent at step 1
- [ ] print: no printed edition of this letter located yet; planned print_check of the post-hoc words once a gate passes
- [x] key-rebuild: period gloss table (GAPS141), residue rule (GAPS146), residue 21 = r settled on fresh numerals (DEF1-1411)
- [x] image-check: full-size DECODE images p.1-p.2 read on native crops (GAPS141, GAPS146, DEF1-1411)
- [retired] retry: the de17/de1600 4-gram language judge as gate, retired by GAPS157 third-attempt clause
Verdict: keep going: 2 internal gaps; cheapest next: pre-registered word-coverage test of T21r on p.3 numerals, ~$6
