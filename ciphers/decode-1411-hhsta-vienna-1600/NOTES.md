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
Stale-line note (D1411-R21, 9 Oct 2026, account-4): the step above was already run by DEF1-1411 (5 Oct, section below;
`def1411/score1411.py --check` re-run 9 Oct 11:26 UTC: "def1411 current", exit 0), so J6 was stopped before any priced step.
What remains open here is ASKS row 120 and the Remaining gaps below, not this line.

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

## D4-1411P3 step: word-coverage test of frozen T21r (+ h variants) on unread p.3 numerals (6 Oct 2026, account 4)

Step run: DEF1-1411's named next step (Remaining gaps 1 and 3), brief D4-1411P3 (LANE DEFAULT-account-4-20261006-1235).
Pre-registration `d4p3/PREREG-D4-1411P3.md` pushed before any p.3 numeral was read (commit c1f95116f; time line corrected in
the next commit; Addendum A on the f.184 interlinear gloss, 05d174f91, pushed before either pass ran; `d4p3/score_p3.py`
pushed 8eab22eaf, before the passes returned). Tables frozen: T21r (def1411/tables.py), T21r_h12 (residue 12 = h), T21r_h22
(residue 22 = h). Statistic: tools/judge_plaintext.py NgramModel.cover (greedy word coverage), de1600 lexicon (10,487 words).
Calibration on already-scored material was computed before the prereg and is quoted in it (p.2 T21r decode 0.631, its
shuffles p99 0.508, shifts max 0.385; gloss 0.613).

One DECODE browser login (tools/decode_browser_login.js 1411 --fetch IMG_R1411_I6597_P3.png --max-files 1); sha1 509fe691...
matches images/manifest.json; not committed (30 MB rule). Crops (pasted commands; automatic line finding found 0 lines on this
grey scan, as before, so centres came from an adaptive-threshold row profile and were checked on the --debug overlays; a first
left-page cut with centres drifting ~40 px on lines 6-9 was discarded before any pass):
`python3 tools/iiif_lines.py --image IMG_R1411_I6597_P3.png --out images/d4p3_crops --region 760,2040,1720,980 --prefix p3L
--centres 36,134,232,330,428,526,624,722,820 --top-margin 50 --bottom-margin 45 --max-width 2400 --debug` (9 crops, left page
= f.183v, numeral block) and `python3 tools/iiif_lines.py --image IMG_R1411_I6597_P3.png --out images/d4p3_crops --region
2860,360,1600,2980 --prefix p3R --centres 46,131,216,283,351,445,515,589,669,748,818,894,971,1048,1133,1208,1285,1360,1445,
1526,1612,1691,1772,1849,1930,2002,2094,2180,2264,2332,2406,2497,2575,2660,2735,2825 --top-margin 45 --bottom-margin 40
--max-width 2400 --debug` (36 crops, right page = f.184r). All crops under 2500 px.

Two blind Sonnet passes, one call each, crops only, opposite reading orders (`d4p3/passA.tsv` 332 rows, `d4p3/passB.tsv` 324).
tools/reconcile_passes.py (`d4p3/rec/`): 290/328 aligned columns agree (88.4%), 38 splits, gloss columns 4/15. The worker
settled the 38 splits from three stacked crop views (one reconciliation unit; `d4p3/reconcile_notes.tsv`): this hand writes 6
as a looped "δ" (63 not 83 at three line ends, 96 not 90), its "zy" is 29, two one-pass tokens were word strokes and dropped,
two non-numeral marks became signs. Every settled split is M. Reconciled: `d4p3/numbers.tsv`, **311 cipher numbers, 209 M**
(pass B flagged most numbers doubtful), 11 in-text figures (dates "13. oct", "15.", enclosure "lit. 6 n. 3", list numerals)
not decoded, 4 graphic signs not decoded.

**Score (`d4p3/score_p3.py`, `--check` exits 0; de1600 coverage; seed 1411):**

| table | cover | shuffled-target p99 / mean (>= real) | shifted max (>= real) | minus gloss (0.613) | 4-gram | PASS |
|---|---|---|---|---|---|---|
| T21r | 0.563 | 0.463 / 0.386 (0/200) | 0.370 (0/23) | -0.050 | -1.838 | no |
| T21r_h12 | 0.540 | 0.437 / 0.364 (0/200) | 0.376 (0/23) | -0.073 | -1.790 | no |
| T21r_h22 | 0.543 | 0.444 / 0.370 (0/200) | 0.370 (0/23) | -0.070 | -1.911 | no |

de1600 real windows at N=311: coverage p05 0.881, median 0.939. **Pre-registered verdict: CONTROLS BEATEN, COVERAGE BELOW THE
LEAF'S OWN GLOSS, for all three tables** -- the same shape as the 4-gram judge (GAPS146/150, DEF1-1411), now on a second
instrument and on 311 numerals none of the tables was built from. No PASS: no grade moves. No variant is preferred.

**Letter tests (pre-registered):** residue 21 (20 occurrences): **r favoured** -- r ranks 1st of 24 on coverage and on 4-gram
(z 21st and 15th); this confirms DEF1-1411's r on a second fresh page. Residue 12 (18): undecided -- h ranks 1st on 4-gram but
9th on coverage (s 5th on both). Residue 22 (13): undecided -- s 2nd on 4-gram, 7th on coverage; h 22nd and 18th.

**Addendum A, f.184 gloss agreement:** both passes agree on the number and the letter at 10 glossed numbers (p3R_L21 29 p,
69 z, 33 c; p3R_L33 67 p, 72 a; p3R_L36 36 h, 18 o, 87 l, 62 d, 81 e). Matches: T21r 4/10 (control p99 2, 2 of 10,000 draws
>= real), T21r_h12 5/10 (0 of 10,000), T21r_h22 4/10 (4 of 10,000). **Gloss agrees with T21r** on the pre-registered rule
(>= 8 pairs, real > control p99), on a gloss leaf the table was not built from. Mismatches, logged as data, not settled:
69 glossed z where T21r has r (residue 21, the same gloss-hand "z" GAPS141 read on p.1, now opposite to the r the decode
statistic favours on two pages: the gloss hand's r probably looks like z to our readers); 36 glossed h where T21r has s
(residue 12; the h12 variant matches); 29 glossed p where residue 5 = a (7/7 on p.1; the number may be 19, residue 19 = p --
an unsettled transcription question, not tested); 33 c vs e (residue 9; c/e is a common look-alike); 72 a vs u (residue 0,
one gloss pair on p.1); 62 d vs k (residue 14, alphabet-filled, never glossed before). The 10 pairs are recorded as new
known-plaintext pairs at grade M (each letter flagged doubtful by at least one pass); they did not retune any table.

**Post-hoc observation (seen after the score; not tested, licenses nothing):** p3R_L21 decodes "aRePPRATORIE" (with the gloss's
p for 29: "prepparatorie", a Latin-German chancery "praeparatoria"); p3R_L36 "sOLKE" against the gloss "holde"; p3R_L09
"WIRsAZEn", p3L_L08 "ESMIUNGESALL". Hypotheses for a verifier or a person's read, not readings.

Token grades (rule 4): new 311 numbers all M (H 0, C 0 new, S 0, M 311, I 0); 10 new f.184 gloss pairs M; earlier 371 numbers M
and p.1 gloss pairs C 54 / M 8 unchanged. No reading-ready flag. Vision: 2 Sonnet subagent calls (45 crops each) + 1
reconciliation unit (3 stacked crop views) + 4 worker placement views (overview, 3 debug overlays). Requests: de-crypt.org
about 3 (1 login, record page, 1 image). Status unchanged: open.

## R12A-D1411P4 step: frozen T21r (+ h variants) on unread p.4 numerals, coverage test and p.4 interlinear gloss (6 Oct 2026, account 1)

Step run: D4-1411P3's Verdict "cheapest next" (Remaining gaps 3), brief R12A-D1411P4 (LANE LANE-RUN12-account-1). Pre-registration
`d1411p4/PREREG-D1411P4.md` (a copy of d4p3's prereg and its Addendum A, plus a descriptive pooled p.3+p.4 h-vs-s ranking) and the
scoring script `d1411p4/score_p4.py` (a copy of d4p3/score_p3.py) pushed in commit afc9de42d before the p.4 image was opened.
Script check before the prereg: score_p4.py on the p.3 numbers reproduced D4-1411P3's T21r 0.5627 / p99 0.463 exactly.

One DECODE browser login (tools/decode_browser_login.js 1411 --fetch IMG_R1411_I6598_P4.png --max-files 1); sha1 7bbfba3c...
matches images/manifest.json; not committed (30 MB rule). Crops (pasted commands; centres placed by eye on a 1/4 overview and two
1/2 views, checked on the --debug overlays; a first cut with one band per page side made 870-px crops across blank space and a
second over-tall right-page cut were both discarded before any pass), image = the fetched P4 png:
`python3 tools/iiif_lines.py --image IMG_R1411_I6598_P4.png --out images/d1411p4_crops --region 700,200,1580,1060 --prefix p4La
--centres 110,345,435,660,880,990 --top-margin 55 --bottom-margin 15 --max-width 2400 --debug`;
`... --region 700,2470,1580,740 --prefix p4Lb --centres 100,200,556,664 --top-margin 55 --bottom-margin 15`;
`... --region 2480,880,1840,580 --prefix p4Ra --centres 50,120,182,245,358,460,542 --top-margin 15 --bottom-margin 15`;
`... --region 2480,1840,1840,110 --prefix p4Rb --centres 55 --top-margin 10 --bottom-margin 10`;
`... --region 2480,2040,1840,980 --prefix p4Rc --centres 50,114,184,280,356,430,510,596,666,746,820,935 --top-margin 10
--bottom-margin 25` (all with --max-width 2400 --debug). 30 crops (left page = f.184v, 10 numeral lines; right page = f.185r,
"Stralsund 14 octob.", 20 numeral lines), all 1580-1840 px wide.

Two blind Sonnet passes, one call each, crops only, opposite reading orders (`d1411p4/passA.tsv` 254 rows, 84 "?" -- pass A first
skipped crop p4Ra_L03 and read it on a one-crop follow-up; `d1411p4/passB.tsv` 249 rows, 66 "?"). tools/reconcile_passes.py
(`d1411p4/rec/`): 221/254 aligned columns agree (87.0%), 33 splits; gloss agreement on columns both glossed 34/53 raw. The worker
settled the 33 splits from the crops (one reconciliation unit, `d1411p4/reconcile_notes.tsv`). Finding about this hand: the 5 is an
"r"-like form and the 4 a cross "+"; most splits were 4/5 (47/57, 46/56, 93/95/98, 63/65). Four groups dropped (a struck group and a
token inside it on p4La_L05, two graphic signs), the year "zu 1627" on p4Ra_L06 treated as in-text. Every settled token is M.
`d1411p4/make_numbers.py --check` regenerates `d1411p4/numbers.tsv`: **248 cipher numbers, 96 M**. Gloss letters kept only where
both passes wrote one and agree after a fixed shape rule (bare stroke "1" = i, "5"-like = s, the forms GAPS150/D4-1411P3 already
read as i/s), never at a number whose value the worker settled: **42 gloss pairs** (left page, lines p4La_L01-L06, p4Lb_L01-L03).

**Score (`d1411p4/score_p4.py`, `--check` exits 0; de1600 coverage; seed 1411):**

| table | cover | shuffled-target p99 / mean (>= real) | shifted max (>= real) | minus gloss (0.613) | 4-gram | PASS |
|---|---|---|---|---|---|---|
| T21r | 0.581 | 0.452 / 0.391 (0/200) | 0.367 (0/23) | -0.032 | -1.610 | no |
| T21r_h12 | 0.585 | 0.448 / 0.375 (0/200) | 0.359 (0/23) | -0.028 | -1.622 | no |
| T21r_h22 | 0.540 | 0.460 / 0.368 (0/200) | 0.383 (0/23) | -0.073 | -1.715 | no |

de1600 real windows at N=248: coverage p05 0.871, median 0.936. **Pre-registered verdict: CONTROLS BEATEN, COVERAGE BELOW THE
LEAF'S OWN GLOSS, for all three tables** -- the third fresh page with this shape (p.2 4-gram, p.3 and p.4 coverage). No PASS: no grade
moves. No variant is preferred (h12 is 0.004 above T21r but does not PASS).

**Letter tests (pre-registered):** residue 21 (18 occurrences): **r favoured** (r 1st on coverage and on 4-gram; z 20th / 16th), the
third fresh page. Residue 12 (11): undecided (s 1st on 4-gram, 6th on coverage; h 4th / 5th). Residue 22 (16): undecided (s 2nd on
4-gram, 3rd on coverage; h 17th / 8th). Descriptive pooled p.3+p.4 (N=559, decides nothing): residue 12 (29) h 1st on 4-gram but 8th
on coverage, s 3rd / 6th; residue 22 (29) s 2nd on 4-gram and 5th on coverage, h 20th / 13th -- s leans ahead of h at 22, 12 stays open.

**Gloss agreement (Addendum A carried over): 42 pass-agreed gloss pairs; T21r matches 25/42 (0.595) against value-shuffled tables
p99 8 (0 of 10,000 draws >= 25)** -- "gloss agrees with T21r" on the pre-registered rule, on a second gloss leaf the table was not built
from, and with four times the pairs of f.184 (h12 23/42, h22 22/42, both also above p99 8). Mismatches, logged as data, not settled: gloss
n where T21r has u at 96 (twice), 24, 72 (n/u is a minim look-alike in this gloss hand and in our readers); gloss h where T21r has k at
38, 86 (residue 14, alphabet-filled, never glossed before; gloss d at 86 once more); 27 a vs y (residue 3); 73 n vs w (residue 1); 14 n
vs k; 11 y vs g; 26 u vs s (residue 2); 9 c vs e and 29 c vs a; 2 c vs s; 71 f vs t; 69 z vs r (residue 21: the gloss-hand "z" again
where the decode statistic favours r, as on p.1 and f.184). The 42 pairs are recorded as known-plaintext pairs at grade M (a person's
read of the gloss, ASKS row 120, would settle them); they did not retune any table.

**Post-hoc observation (seen after the score; not tested, licenses nothing):** under T21r p4Rc_L01 decodes "DENneMArck" (Dänemarck),
p4Rb_L01 "krIEges...", p4Rc_L08 "propOSet", p4Rc_L09 "AttribuK...", p4Rc_L07 "gesaNdT...", p4Lb_L01 "Danus", p4Lb_L02 "grobEsrucke",
p4Ra_L05 "AnlANGET" (anlanget), p4Rc_L11 "AndTen". The clear text around them is a Stralsund letter of 14 Oct (1628 in the left page's
dating line "15 octob. 1628"). Hypotheses for a verifier or a person's read, not readings.

Token grades (rule 4): new 248 numbers all M (H 0, C 0 new, S 0, M 248, I 0); 42 new p.4 gloss pairs M; earlier 682 numbers M, p.1 gloss
pairs C 54 / M 8 and f.184 pairs M 10 unchanged. No reading-ready flag. Vision: 2 Sonnet subagent calls (30 crops each, plus a one-crop
follow-up) + 1 reconciliation unit (3 stacked crop views + 1 zoom) + 6 worker placement views (overview, 4 half views/sheets, 1 debug).
Requests: de-crypt.org about 3 (1 login, record page, 1 image). Status unchanged: open.

## R12A-D1411LA step: look-alike re-read of the p.4 4/5 forms (6 Oct 2026, account 1)

Step run: R12A-D1411P4's Verdict "cheapest next" (brief R12A-D1411LA, LANE LANE-RUN12-account-1). Rule pinned before any re-read in
`d1411p4/la/PREREG-LA.md` (pushed cafba26e3, time corrected f376b6b96); scoring would re-use PREREG-D1411P4 (afc9de42d) unchanged.
`d1411p4/la/build_tiles.py` lists **83 tiles** (p.4 numbers where pass A, pass B or the committed token has a 4 or 5) on 29 crops and
writes a value-blind prompt (`la/prompt.md`: each 4/5 digit shown as '#', reader names its shape X cross / R r-form / O other / ?).
tools/lookalike_pass.py's packet step needs a sign sheet and sheet map (symbol ciphers) and does not fit a numeral hand, so the tiles
and the same 2-of-3 reconcile rule are applied by the folder script; a numeral mode for the tool is a suggestion, not built here.

**Result: void re-read.** One blind Sonnet call on the 29 line crops (images/d1411p4_crops, native resolution, about 1840 x 112 px)
answered **83 of 83 tiles '?'** (`la/reread.tsv`): the reader reported the masked digits too small to call a shape and could not
match three left-page crops (p4La_L01, p4Lb_L01, p4Lb_L02) to the listed sequences. Under the pinned rule every tile is UNSETTLED
and keeps its committed value, so the corrected numbers equal `numbers.tsv` and the T21r rescore is identical to R12A-D1411P4's
(0.581) by construction: **non-test, not a negative**; no rescore was run, no number, grade or table changed (rule 7 untouched).
Residual 83/83 is reader abstention, not error. Lesson: a whole-line crop given to a shape question about one digit is too coarse;
the re-read needs per-number tiles (each number cut and enlarged on its own, a few hundred px per tile), or the owner's sign sorter.
Vision: 1 Sonnet subagent call. Requests: none (crops on disk). Status unchanged: open.

## D07-D1411 step: per-number tile re-read of the p.4 4/5 forms, T21r rescore (7 Oct 2026, account 1)

Step run: R12A-D1411LA's Verdict "cheapest next" (brief D07-D1411, LANE DEFAULT-account-1-20261007-0042). Instrument pinned before any
read in `d1411p4/la/PREREG-LA2.md` (pushed 67e45081f, 00:52 UTC; time and one framing edit, 12 -> 25 px margin, made before any tile was
read, cf28f1f7d); scoring re-uses PREREG-D1411P4.md (afc9de42d) unchanged, no control or gate moved. `d1411p4/la2/score_la2.py` (score_p4.py
with only the input/output paths changed) reproduced the committed score_p4.json exactly on the unchanged numbers before the re-read.
Tiles: the same 83 numbers as la/tiles.tsv, each cut on its own from its native line crop (images/d1411p4_crops, themselves cut from
IMG_R1411_I6598_P4.png at native resolution in R12A-D1411P4; no re-fetch, no login), x-range in `la2/boxes.tsv`, 25 px margin, full line
height, 4x LANCZOS: `python3 d1411p4/la2/cut_tiles.py` (83 tiles, about 400-600 px wide; regenerable, not committed). Box placement:
first by eye on 50-px ruler overlays, then -- after a contact-sheet check showed about 30 right-page boxes off by one number -- re-placed on
automatic ink-column segments and 1.5-2x ruler zooms, and every tile checked on a contact sheet for a centred target before the full read
(the worker placed boxes; it did not call shapes). Prompt `la2/make_prompt.py`: value-blind, only the mask pattern ('#6', '##') shown.

**Pilot (5 tiles, 1 Sonnet call): 1 of 5 '?'** -- under the pre-registered stop rule (3+ of 5), so the full read ran. **Full read (78 tiles,
2 Sonnet calls of 39): 79 of 83 tiles firm, 4 '?'** (`la2/reread_pilot.tsv`, `la2/reread_full.tsv`) -- the instrument is not void at this
resolution, unlike the line-crop re-read (83/83 '?'). One reader caveat, logged as data: the batch-1 reader said that on its tiles 11-20
(p4Ra_L01_1 to p4Ra_L03_11) the glyphs did not always match the digit patterns and that two were guesses; its answers are used as given.

**Rule applied (`la2/apply_la2.py --check` exits 0; `la2/applied.tsv`, `la2/numbers_la2.tsv`):** settled 58 (57 confirm the committed value,
1 changes it: p4Rc_L07_9 65 -> 64, pass B's value, graded M); unsettled 25 (21 firm re-reads matching neither pass, 4 '?'); residual 25/83 =
30% (2-of-3 agreement, not error). Re-read agreement with pass A 49/79, pass B 54/79, committed 60/79 (76%); on its H-confidence answers 20/22.
Of the 21 firm disagreements, 16 contradict a value both passes and the reconciliation agreed on, 12 of those calling R (5) where all three had
4 and 4 calling X (4) where all three had 5 -- a lean toward "R", so this reader is a third reader of lower agreement, not an arbiter.

**Rescore (`la2/score_la2.py --check` exits 0; seed 1411; same frozen controls): unchanged.** T21r cover 0.5806 (committed 0.581), shuffled
p99 0.452 / mean 0.390 (0/200 >= real), shifted max 0.359 (0/23), minus gloss -0.032, 4-gram -1.620; h12 0.585, h22 0.540; **pre-registered
verdict for all three tables: CONTROLS BEATEN, COVERAGE BELOW THE LEAF'S OWN GLOSS** (same as R12A-D1411P4). Letter tests unchanged (residue
21 r favoured, 18 occurrences; 12 and 22 undecided); gloss agreement unchanged (T21r 25/42 vs control p99 8). The one changed number moves
p4Rc_L07_9 from residue 17 to 16 and no statistic at the reported precision. So the 4/5 look-alike is not what keeps T21r below the gloss:
re-reading it leaves the score where it was. `numbers.tsv` itself is not changed (rule 7: d1411p4/score_p4.py --check still exits 0).

Token grades (rule 4): unchanged -- 248 p.4 numbers M (H 0, C 0, S 0, I 0); one value revised in the la2 copy, still M. No reading-ready flag.
Vision: 3 Sonnet subagent calls (5 + 39 + 39 tiles), no reconciliation unit (the rule is mechanical); worker views: ruler overlays, segment
overlays, zooms and three contact sheets for box placement. Requests: none (all images on disk). Status unchanged: open.

## AM-D1411P5 step: p.5 numerals, two blind passes, frozen T21r (+ h variants) coverage test (7 Oct 2026, account 2)

Step run: D07-D1411's Verdict "cheapest next" (brief AM-D1411P5, LANE LANE-AM-0914). Pre-registration `d1411p5/PREREG-D1411P5.md` and
`d1411p5/score_p5.py` (a copy of d1411p4/score_p4.py, paths changed, pooled descriptive set extended to p.3+p.4+p.5) pushed in 1fbc0c3fc
before the p.5 image was opened; the script reproduced R12A-D1411P4's p.4 T21r score exactly (0.5806) before the prereg. Image: one
DECODE browser login (tools/decode_browser_login.js 1411 --fetch IMG_R1411_I6599_P5.png --max-files 1); sha1 0a102250... matches
images/manifest.json (the full-size files are not on disk in a fresh container: GAPS137 did not commit them); not committed (30 MB rule).

Crops: line centres from an adaptive-threshold row profile per half-page, checked by eye on ruler views and two contact sheets (a first
iiif_lines cut with --deskew and 40 px margins took two lines per crop and was discarded before any pass). The crop step is
`python3 tools/iiif_lines.py --image IMG_R1411_I6599_P5.png --out <scratch> --region 880,340,1420,2700 --columns 0:780 --prefix p5La
--centres 90,172,...,2533 --top-margin 0 --bottom-margin 0 --debug` (and --columns 640:1420 for the right half; placement check only),
then the committed `python3 d1411p5/cut_halves.py IMG_R1411_I6599_P5.png images/d1411p5_crops` reading `d1411p5/lines.tsv` (42 numeral
lines: 23 on the left page, 19 on the right page = f.186; each line split at its least-inked middle column, each half at its own
centre since the lines slope, upscaled 2x LANCZOS, 1170-1850 px wide; 84 crops, pushed ebafac499 before the passes).

Two blind Sonnet passes, one call each, crops only, opposite reading orders (`d1411p5/passA.tsv` 274 numbers, 91 "?"; `passB.tsv` 276,
107 "?"). tools/reconcile_passes.py (`d1411p5/rec/`): 242/276 columns agree (87.7%), 34 splits; gloss agreement 23/37. The worker settled
the 34 splits from crop sheets (one reconciliation unit, `d1411p5/reconcile_notes.tsv`): mostly the r-form 5 vs 1, the looped 6, the hooked 7
vs 2, 9 vs 4; two settled values match neither pass (59, 45); 4 struck or word tokens dropped; 3 dates ("Den 2. dat", "Den 13. huj",
"Das 2") in-text. The passes' "intext?" flag on p5L_L15 "18 60" (twice) was overruled: read as cipher, M (the p.2 copy below aligns them as
cipher). `d1411p5/make_numbers.py --check` regenerates `d1411p5/numbers.tsv`.

**Deviation, after the score (reported, not hidden):** the copy alignment below showed two numbers cut in two by the half-line split
(p5L_L01 "16" read as 1 | 6; p5R_L16 "36" as 3 | 6; both visible whole on the overview). Both were merged in reconcile_notes.tsv after the
first score and the score re-run; the committed numbers.tsv (**266 cipher numbers, 125 M**) and score_p5.json are the merged version.
Both runs are reported below. Lesson for cut_halves.py: the least-ink column can fall in the gap between the digits of one number; a
contact sheet does not catch it -- check each _a/_b boundary pair against the overview.

**Score (`d1411p5/score_p5.py`, `--check` exits 0; de1600 coverage; seed 1411):**

| table | cover (first run, N=268) | cover (merged, N=266) | shuffled p99 / mean | shifted max | minus gloss (0.613) | 4-gram | PASS (first / merged) |
|---|---|---|---|---|---|---|---|
| T21r | 0.612 | 0.617 | 0.511 / 0.430 (0/200) | 0.444 (0/23) | -0.001 / +0.004 | -1.738 | no / yes |
| T21r_h12 | 0.623 | 0.628 | 0.485 / 0.409 (0/200) | 0.440 (0/23) | +0.010 / +0.015 | -1.626 | yes / yes |
| T21r_h22 | 0.541 | 0.545 | 0.481 / 0.404 (0/200) | 0.417 (0/23) | -0.072 / -0.068 | -1.774 | no / no |

de1600 real windows at N=266: coverage p05 0.884, median 0.940. **Pre-registered verdict: T21r_h12 PASS on both runs and preferred
(its coverage exceeds T21r's); T21r "controls beaten, coverage below the leaf's own gloss" on the registered first run (by 0.001), PASS
only after the post-score merges -- report T21r as at the gate, not past it.** The margins are thin (+0.010 to +0.015 for h12).

**Letter tests (pre-registered):** residue 12 (16 occurrences): **h favoured** (h 1st on coverage and on 4-gram; s 4th / 15th) -- the first
page to decide residue 12, in the direction of the f.184 gloss (36 glossed h). Residue 21 (20): undecided on p.5 (r 1st on 4-gram, 3rd on
coverage; z 21st on both). Residue 22 (19): undecided (s 1st on 4-gram, 2nd on coverage; h 7th / 16th). Pooled p.3+p.4+p.5 (N=825,
descriptive): residue 12 h 1st on 4-gram, 7th on coverage; residue 22 s 2nd / 3rd, h 17th / 14th.

**Gloss agreement (Addendum A): 26 pass-agreed gloss pairs on p.5 (mostly f.186); T21r matches 15/26 against value-shuffled tables p99 7
(0 of 10,000 >= 15)** -- agrees, a third gloss leaf (h12, h22 also 15). Mismatches, logged as data: 69 glossed z twice where T21r has r
(residue 21, the gloss-hand "z" again, as on p.1, f.184 and p.4); 81 c and x vs e; 36 b vs s; 63 t vs l; 22 a vs s; 21 u vs r; 89 u vs n
(minim look-alike); 83 e vs g; 51 a vs y. 26 pairs recorded at grade M; they retuned nothing.

**Post-hoc finding (seen after the score; `d1411p5/posthoc_copy.py`, licenses nothing on its own): the p.5 left page is a second copy of
the p.2 left-page cipher text.** p5L_L11_b-L31_a aligns with def1411's p2Lb_L01-p2R_L02 over 95 numbers, 82 equal, 13 differing in 12
substitutions and no insertions (most differences are the look-alikes above: 53/93, 19/29, 7/4, 81/61, 95/45, 46/96), and p5L_L01-L11_a
matches GAPS146's p.2 upper lines (residue/numbers.tsv) in blocks of 45 numbers. Consequences: (1) the p.5 left page is not independent
material -- it re-measures p.2's text, which under coverage already scored 0.631 (DEF1-1411 calibration, above the gloss); the PASS rests
largely on it: p5L alone T21r 0.644 / h12 0.663 (shuffled p99 0.513 / 0.500), p5R (f.186, not a copy) alone 0.576 / 0.576 (p99 0.547 /
0.528), below the gloss; (2) two independent transcriptions of one cipher text agree on 86% of aligned numbers (82/95), a direct
reader-error measure for this hand (about 14% of numbers differ between two reconciled transcriptions), and the 13 differences are each
settleable by comparing the two copies' images -- a cheaper next step than any further page. Which copy is the draft and which the
fair copy (or decipherment working) is not established. Post-hoc words under T21r_h12 (hypotheses for a verifier or a person's read, not
readings): the p.2 runs "konig", "eicsen" (reichsen?), "dani | maris b(altic)" recur on p5L_L24-L31; p5R_L09 "IeIE", p5R_L13 "uPBErn".

Token grades (rule 4, `d1411p5/grades.py --check` exits 0, `d1411p5/grades.tsv`): under the preferred T21r_h12 per the prereg grade rule,
**S 114, M 152** (withdrawn by AM-D1411V below: S 0, M 266) of 266 p.5 numbers (S = both passes agree with no flag and the residue letter is gloss-backed or residue 21; residue 12 = h
stays M, not gloss-backed); H 0, C 0, I 0. **Caveat for the verifier:** the S grades rest on a thin PASS (+0.015) driven mostly by a copy of
already-scored p.2 text; the independent right page alone does not reach the gloss. No reading-ready flag; earlier pages' grades unchanged
(rule 7: the earlier numbers.tsv/decodes are untouched). Vision: 2 Sonnet subagent calls (84 crops each) + 1 reconciliation unit (5 crop
sheets) + worker placement views (overview, 4 ruler views, 3 contact sheets). Requests: de-crypt.org about 3 (1 login, record page, 1 image).
Status unchanged: open.

## AM-D1411V verifier: AM-D1411P5's p.5 PASS and 114 S grades (7 Oct 2026, account 2)

Separate session from AM-D1411P5 and every earlier decode-1411 solver (brief AM-D1411V, LANE LANE-AM-0914). A rule-3/rule-4 check,
not a novelty audit (no reading is claimed; no AUDIT.md). No new page read, nothing re-transcribed.

**(1) Order and deviations.** PREREG-D1411P5.md and score_p5.py: 1fbc0c3fc, 10:20:24 UTC; crops/lines.tsv: ebafac499, 10:25:53;
passes, reconciliation, numbers, score, grades: 570ccd37e, 10:33:44. Neither the PREREG nor score_p5.py was touched after 1fbc0c3fc.
The PREREG predates the scored run. Deviations: (a) **material premise**: the PREREG tests "unread p.5 numerals"; 130 of the 266
(merged) are a second copy of p.2's cipher text (d1411v alignment: five spans p5L_L01_a-L31_a, 120 numbers in difflib blocks >= 4),
and that p.2 text is the material T21r was chosen on -- GAPS146's p2L lines (contaminated for the r question, DEF1-1411) and
def1411's p2Lb/p2R numbers, on which DEF1-1411's letter test fixed residue 21 = r and where "reicsen" first suggested h at 12/22.
On the copy the test is in-sample, not a test on unseen numerals; nobody could know this before the passes, so it is the material's
fault, not the worker's, but it voids the premise. (b) two post-score crop-split merges (16, 36), reported by the worker; they move
T21r from -0.001 to +0.004 against the gloss; h12 passes either way. (c) the crop step used the committed cut_halves.py, not
iiif_lines.py half-line crops as registered (iiif_lines for placement only; first cut discarded before any pass); reported,
immaterial to the statistic. (d) the passes' "intext?" flag on p5L_L15 "18 60" overruled (read as cipher, M); reported. (e) the
PREREG's pooled-set sentence says "p.3 + p.5 (d4p3 + d1411p4)"; the script pools p.3+p.4+p.5 -- wording only, descriptive, decides
nothing. (f) score_p5.py's fail string still says "p.4" -- cosmetic.

**(2) Re-run.** `score_p5.py --check`, `make_numbers.py --check`, `grades.py --check`: all exit 0. `d1411v/rescore_v.py` (statistic,
controls and PASS rule copied from the PREREG unchanged; 200 order shuffles seed 1411, 23 shifted rules, gloss cover 0.6129) reproduces
both registered runs exactly (merged N=266: T21r 0.6165, h12 0.6278; unmerged N=268: T21r 0.6119, h12 0.6231). `--check` exits 0.

**(3) Re-score on the independent material and without the merges** (`d1411v/rescore_v.json`; "indep" = p.5 minus the p.2-copy spans
= 30 left-page numbers + p5R/f.186):

| set | N (merged / unmerged) | T21r cover | T21r_h12 cover | shuffled p99 (T21r / h12) | shifted max | minus gloss (h12) | verdict (all three tables) |
|---|---|---|---|---|---|---|---|
| all p.5, merged (registered after merges) | 266 | 0.617 | 0.628 | 0.511 / 0.485 | 0.444 | +0.015 | T21r, h12 PASS |
| all p.5, unmerged (registered first run) | 268 | 0.612 | 0.623 | 0.493 / 0.466 | 0.440 | +0.010 | h12 PASS; T21r below gloss |
| **indep, merged** | 136 | 0.588 | 0.588 | 0.537 / 0.529 | 0.493 | **-0.025** | controls beaten, below gloss |
| **indep, unmerged** | 137 | 0.584 | 0.584 | 0.555 / 0.526 | 0.489 | **-0.029** | controls beaten, below gloss |
| p5R only, merged / unmerged | 106 / 107 | 0.576 / 0.570 | same | 0.547 / 0.551 (T21r) | 0.481 / 0.477 | -0.037 / -0.043 | controls beaten, below gloss (unmerged T21r: 2/200 shuffles >= real) |
| copy span, merged / unmerged | 130 / 131 | 0.615 / 0.611 | 0.639 / 0.634 | 0.515 / 0.527 (T21r) | 0.392 / 0.389 | +0.026 / +0.021 | h12 PASS (in-sample) |

The PASS lives entirely on the copy of the material T21r was built on. On the independent numerals every table beats its order and
shift controls but stays 0.025-0.029 below the leaf's own gloss -- the same result as p.3 and p.4 (0.03-0.07 below). h12 and T21r
give identical coverage on the independent set: the h12 preference also comes only from the copy (residue 12 letter test was run
on all p.5; not re-run here, but h at 12 has no independent coverage support on p.5). The Addendum A gloss agreement does stand on
independent material: all 26 pass-agreed gloss pairs sit outside the copy spans, T21r 15/26 vs value-shuffled p99 7 (0 of 10,000).

**(4) Grade verdict (PREREG "Grades": "No grade moves unless PASS(T21r) (or a preferred variant)").** The registered PASS is void as a
test of unseen numerals (deviation a); on the independent part, scored under the PREREG's own rule, no table PASSes. **The 114 S
grades drop to M: p.5 is S 0, M 266** (of the 114: 64 on the p.2-copy spans, 50 on independent numerals; H 0, C 0, I 0). They do not
stand even on the independent part, because that part has no PASS of its own. Unchanged: the p.5 letter tests are descriptive at
best (12 = h favoured only with the copy included); the gloss agreement 15/26 stands; the copy finding stands and is the useful
result of the step (two transcriptions of one text, 82/95 equal, a reader-error measure). `d1411p5/grades.tsv` is left as the
worker's registered output (grades.py --check exits 0) and is superseded by this section; status open.
Requests: none (no network). Cost: verifier session only.

## D1A-D1411: p.2/p.5 copy differences, per-number image comparison (8 Oct 2026, account 1)

Brief D1A-D1411 (LANE DEFAULT-account-1-20261008-0540). Pre-registered in d1a/PREREG-D1A-D1411.md (commit 09035fe74, 05:49 UTC;
addendum before the read, 7de9fadb0). Material: the committed line crops (images/def1411_crops, images/d1411p5_crops); no network.
Tiles placed by band-limited ink segmentation (d1a/bandseg.py, d1a/tiles_spec.tsv; d1a/tiles.py checks every tile's (line, pos,
value) against both numbers.tsv and the posthoc alignment: disputed = replace ops, exemplars = equal-block numbers graded ok).
57 tiles (26 disputed, 31 exemplars) shuffled into three montages with neutral ids (d1a/montage/, key d1a/tile_key.tsv); one blind
Opus shape read (d1a/blind_read.tsv, no key, no context, no pairing told); settlement by script (`d1a/settle.py --check`).

**Control: exemplar accuracy 30/31 = 0.968 (gate 0.80) -- PASS** (the one miss: p2Lb_L11 18 read 28, sure).

| op | p.2 tx -> read | p.5 tx -> read | class | settled |
|---|---|---|---|---|
| D01 | 53 -> 53 (unsure, alt 83) | 93 -> 93 (unsure, alt 53) | U | |
| D02 | 19 -> 19 (sure) | 29 -> 69 (unsure, alt 29) | U (p.5 read matches neither) | |
| D03 | 7 -> 7 (unsure, alt 2) | 4 -> 7 (unsure, alt 2) | U (both read 7, neither sure) | |
| D04a | 6 [+ mark] -> 68 (unsure, alt 60) | 60 -> 60 (unsure, alt 68) | U | |
| D04b | 12 -> 12 (sure) | 22 -> 22 (sure) | S3 genuine variant | |
| D05 | 57 -> 57 (sure) | 54 -> 57 (unsure, alt 59) | S1 | 57 |
| D06 | 81 -> 87 (sure) | 61 -> 81 (unsure, alt 84) | U | |
| D07 | 71 -> 71 (unsure, alt 21) | 21 -> 21 (unsure, alt 71) | U | |
| D08 | 19 -> 19 (unsure, alt 17) | 17 -> 17 (sure) | S2 | 17 |
| D09 | 46 -> 40 (unsure, alt 48) | 96 -> 46 (unsure, alt 96) | U | |
| D10 | 81 -> 51 (unsure, alt 91) | 51 -> 51 (unsure, alt 52) | U (both read 51, neither sure) | |
| D11 | 95 -> 95 (sure) | 45 -> 48 (unsure, alt 45) | U (p.5 read matches neither) | |
| D12 | 5 -> 5 (unsure, alt 2) | 51 -> 51 (unsure, alt 81) | U | |

Result: of 13 differences, 2 settled as transcription errors (p.5 "54" is 57 as on p.2; p.2 "19" at p2Lb_L06 is 17 as on p.5), 1
is a genuine copy variant (12 / 22, both read sure), 10 unsettled. Descriptive leanings, not settlements: D03 both tiles read 7
(p.5 transcribed 4); D10 both read 51 (p.2 transcribed 81); D04a both copies carry the same two-sign shape (6 + a mark that p.2's
transcription took as the sign token and p.5's as 0) -- a token-convention difference, not a numeral one. Worker reconciliation (the
same tiles on the placement sheet) moved nothing. The reader agrees with its exemplars but marks most look-alike tiles unsure: the
instrument passes its control and still cannot decide most of this hand's look-alikes at tile scale; a person's read is the remaining
route (the 10 tiles join ASKS row 120). Committed numbers.tsv files are untouched (rule 7); settled values only in d1a/settled.tsv.

**Re-score (descriptive only, in-sample for T21r; AM-D1411V ruling, no grades move; `d1a/rescore.py --check`):** p.2 (def1411) +
p.5 copy span, N=290: T21r 0.635 -> 0.641 settled (shuffled p99 0.510 / 0.517); T21r_h12 0.628 -> 0.635 (p99 0.490 / 0.500). Two
substitutions move coverage by +0.007; nothing licensed. Grades unchanged: S 0 on p.5.
Cost: one blind Opus subagent call + worker reconciliation. Requests: none (no network). Status unchanged: open.

## D1411-P6 step: p.6 numerals -- PREREG and copy mask pushed; image not obtained (10 Oct 2026, account 2)

Brief D1411-P6 (LANE FAMILY-A2n, account 2; .claude/briefs/runs/2026-10-10-ytbiz-family-0209-jobs.md). Status unchanged: open.

Prior work (`tools/prior_work.py decode-1411-hhsta-vienna-1600 --item-spec 'shelfmark=HHStA Wien (DECODE record 1411);folio=p.6'
--step-type transcribe --fetch`, exit 4): 1-own LEAD = this job's own claim (recorded CLEAR; the folder has no earlier read of p.6);
3-tomokiyo and 3-solver UNCHECKED recorded CLEAR at target level from the 24 Sept check-solved and the 3 Oct web check; 2-leaf LOOK
(gloss/clear-copy check on the p.6 leaf) stays **owed**: the image was not obtained (below), so it did not run.

**Done, before any image:** `d1411p6/PREREG-D1411P6.md` and `d1411p6/score_p6.py` pushed in b42c67c7d (02:48 UTC by date -u),
checked on origin/main. score_p6.py = score_p5.py with paths changed plus a copy mask: rescore_v.py's copy_mask (difflib blocks >= 4,
blocks merged across gaps <= 3 on both sides) generalised to every already-read page (p.1, p.1 gloss lines, p.2, p.3, p.4, p.5) and
every p.6 line; masked numbers are excluded before scoring; PASS and grades are on the independent remainder only.
`score_p6.py --reproduce-p5` (mask against p.2 only) reproduces AM-D1411V exactly: p.5 independent N=136, spans 10/7/46/15/52,
T21r 0.5882, h12 0.5882, h22 0.5441 (exit 0).

**Not done: the p.6 image.** The one DECODE browser login succeeded (`loggedIn: true`) but the brief's command
`tools/decode_browser_login.js 1411 --fetch IMG_R1411_I6600_P6.png --max-files 1` passes a relative file name, which the tool
resolves against https://de-crypt.org/decrypt-web/ -> HTTP 404 (128 bytes); the tool's own header says the file server must be
given absolute (`--fetch "https://de-crypt.org/decrypt-custom/filesrv/?file=IMG_R1411_I6600_P6.png"`). One unauthenticated GET of
that absolute URL returns a 986x568 "Insufficient permissions to see the full image" placeholder PNG (HTTP 200), so the full image
needs a session. The brief allows one login; a second was not made. No crops, passes or score: p.6 is untouched.
Fix for the re-brief: pass the absolute filesrv URL (as above). Requests: de-crypt.org 4 (login flow 2, the 404 fetch, 1 anonymous GET).

**Found while calibrating the mask (post-hoc, descriptive, licenses nothing; `d1411p6/posthoc/p4_copy_mask.py --check`):** the
**p.4 right page is a further copy of already-read text**: against p.1 (residue p1L) spans p4Ra_L07-p4Rc_L03 (40 numbers),
p4Rc_L05 (5), p4Rc_L06-L10 (34); against the p.1 gloss lines p4Ra_L02-L03 (25), p4Ra_L04-L06 (24); against p.2 p4Rc_L11-L12 (8);
136 of p.4's 248 numbers masked (p.3 against p.1/p.1 gloss/p.2 masks 0 of 311, so chance blocks are not the cause). T21r was built
on p.1's gloss table and the p.1/p.2 residue rule, so p.4's copy span is in-sample. Split under the AM-D1411V controls:

| p.4 set | N | T21r cover | shuffled p99 | shifted max | verdict (T21r; h12, h22 alike) |
|---|---|---|---|---|---|
| all (registered R12A-D1411P4) | 248 | 0.581 | 0.452 | 0.367 | controls beaten, below gloss 0.613 |
| copy of p.1/p.1 gloss/p.2 | 136 | 0.684 | 0.537 | 0.404 | PASS (in-sample) |
| independent | 112 | 0.429 | 0.473 | 0.384 | **controls not beaten** |

So on p.4 the coverage signal lives on the copy; the independent p.4 numerals do not beat their order shuffle. The 42 p.4 gloss
pairs all sit in the independent part and still agree with T21r (25/42 vs value-shuffled p99 8). Of the independent material so
far, p.3 (no copy found, 0.563 vs p99 0.463) and p.5 independent (0.588 vs p99 0.537) beat their controls and stay below the gloss;
p.4 independent does not beat them. p.4's grades were already all M; nothing is regraded (rule 7: committed files untouched).

## D1411-P6b step: p.6 numerals, two blind passes, frozen T21r (+ h variants), copy mask over p.1-p.5 (10 Oct 2026, account 2)

Brief D1411-P6b (LANE FAMILY-A2n, account 2), resuming D1411-P6. PREREG `d1411p6/PREREG-D1411P6.md` and `d1411p6/score_p6.py` unchanged
since b42c67c7d (checked: no diff against origin/main before the score). `score_p6.py --reproduce-p5` re-run first: p.5 independent N=136,
T21r 0.5882, h12 0.5882, h22 0.5441, "OK" (exit 0).

Image: one DECODE browser login, `tools/decode_browser_login.js 1411 <scratch> --fetch
'https://de-crypt.org/decrypt-custom/filesrv/?file=IMG_R1411_I6600_P6.png' --max-files 1`: a real 4608x3456 PNG, sha1 0f597628...
= images/manifest.json (not the placeholder); not committed (30 MB rule); the saved record page was deleted unread. Requests: de-crypt.org
3 (login flow, record page, 1 image).

The leaf (prior-work 2-leaf, recorded KNOWN-PART): unlike p.5, p.6 is mostly clear German with cipher groups set in the lines. Left
page: numeral groups on lines 1-3 and 5 and two left-margin lines, with **interlinear gloss letters above most of them**; line 4 and
lines 6-7 carry only dates/quantities in the clear text (not cut); the lower left page is show-through. Right page (f.187): groups on
lines 1-6, 10, 12, 14-16, no gloss; plus one strip of the next sheet at the foot (p6X_L01, "... 35 77, 4, 47, 91"). Not cut: the gutter
note beside right line 1 and the other leaves showing at the edges.

Crops: line centres from an adaptive-threshold row profile (ink = pixel < 40-px box-blur - 35, as AM-D1411P5), per quarter-width column
on the right page because its lines slope ~40 px across the page, checked on an overlay and two contact sheets; three placements fixed
before the passes (L05 too high, R03 took R02's numbers in its top margin, L02 cut at the page edge). `iiif_lines.py --image ... --dry-run`
found 0 lines at its default ink threshold on this low-contrast scan, so the committed step is `python3 d1411p6/cut_halves.py
IMG_R1411_I6600_P6.png images/d1411p6_crops` reading `d1411p6/lines.tsv` (18 lines, 36 half-line crops, 2x LANCZOS; pushed 6d7e1257d
before the passes).

Two blind Sonnet passes, one call each, crops only, opposite orders (`d1411p6/passA.tsv` 138 numbers, `passB.tsv` 136, after dropping
the "-" rows for crops without numbers). `tools/reconcile_passes.py` (`d1411p6/rec/`): 123/138 agree (89.1%), 15 splits; gloss agreement
3/12 aligned. One reconciliation unit (`d1411p6/reconcile_notes.tsv`, two crop sheets): 15 splits settled, mostly the r-form 5 (53, 57,
15, 35), 77/72, 11/21, 89 (y-form 9), 85 (or 81) in the margin; **plus a common-mode split both passes made**: p6L_L01_a "88" read 58|88
and "97" read 92|7, p6L_L05_b "53" read 5|3 (or 51|3) -- merged from the crop before the score (the AM-D1411P5 split lesson, here inside
a crop rather than at the _a/_b boundary); "Den 2." (R14) set in-text. `d1411p6/make_numbers.py --check` regenerates
`d1411p6/numbers.tsv`: **133 cipher numbers, 59 M, 12 glossed** (pushed b0b58e6b4 before the score).

**Copy mask: 73 of 133 masked, all against p.2** (8 blocks >= 4, 70 equal inside them): spans p6R_L01_a-L02_a (9), L02_b-L05_a (26),
L06_a (4), L06_b-L14_b (25), L15_a-L15_b (9). So most of the right page (f.187) is a further copy of p.2 text, as the p.5 left page
was (the third copy of already-read text found, after p.5L and p.4R). Nothing aligned to p.1, the p.1 gloss, p.3, p.4 or p.5.
**Independent N = 60** (left page 25, margin 5, foot strip 5, right page 25): exactly the registered floor (N < 60 = NON-TEST), so it
is a test, and a fragile one -- one more merge in the reconciliation would have made it a NON-TEST.

**Score (`d1411p6/score_p6.py`, `--check` exits 0; de1600 coverage; seed 1411), independent N=60:**

| table | cover | shuffled p99 / mean (n >= real of 200) | shifted max (n >=) | minus gloss (0.613) | 4-gram | PASS |
|---|---|---|---|---|---|---|
| T21r | 0.500 | 0.517 / 0.382 (9) | 0.483 (0) | -0.113 | -1.909 | no |
| T21r_h12 | 0.517 | 0.517 / 0.371 (4) | 0.467 (0) | -0.096 | -1.835 | no |
| T21r_h22 | 0.450 | 0.533 / 0.368 (29) | 0.467 (2) | -0.163 | -1.945 | no |

de1600 real windows at N=60: coverage p05 0.800, median 0.917. All 133 (descriptive, copy included): T21r 0.504, h12 0.519, h22 0.429.
**Pre-registered verdict: no PASS; T21r does not beat its order shuffle on p.6's independent numerals (0.500 vs p99 0.517) and sits
0.113 below the leaf's own gloss -- "not supported on p.6", conditional on the transcription.** It does beat every shifted rule.
Letter tests: residues 12 (n=2), 21 (n=4), 22 (n=3) all undecided (too few). 

**Gloss agreement (Addendum A): 11 pass-agreed gloss pairs on the independent set; T21r matches 9/11 against value-shuffled tables
p99 3 (0 of 10,000 >= 9) -- agrees** (h12 8/11, h22 9/11), a fourth gloss leaf. The gloss pairs sit on the left page, so the leaf's
gloss supports T21r letter by letter while the coverage statistic on 60 numbers does not separate from its shuffle.

Token grades (rule 4): no PASS, so **S 0, M 133** of 133 p.6 numbers; H 0, C 0, I 0. Earlier pages' files untouched.
Vision: 2 Sonnet subagent calls (36 crops each) + 1 reconciliation unit (2 crop sheets) + worker placement views (overview, 3 ruler
views, 1 overlay, 3 contact sheets). Status unchanged: open. Report: found as above; not found: any p.6 span aligning to p.1, p.3, p.4
or p.5; no PASS. Novelty not classified.

## Remaining gaps (AM-D1411P5, 7 Oct 2026; D1411-P6b, 10 Oct 2026)
Read so far: 0 cipher numbers at S (AM-D1411V withdrew AM-D1411P5's 114 p.5 S grades: the PASS rests on a copy of the p.2 text T21r was built on; independent p.5 numerals beat controls but stay 0.025 below the gloss); p.1 gloss pairs C 54 of 62; f.184 gloss pairs M 10; p.4 gloss pairs M 42; p.5 gloss pairs M 26; p.6 gloss pairs M 11 (D1411-P6b, no PASS); other numbers M
- p.5 left page = second copy of p.2 (13 of 95 aligned numbers differ) - blocker: waiting-on ASKS row 120 (a person's read); D1A-D1411 (8 Oct) settled 2 of 13 (57, 17) and found 1 genuine copy variant (12/22) by a blind per-number tile read with a passed exemplar control (30/31); the other 10 stay unsettled for this machine instrument (both reads unsure or matching neither candidate) -- the 10 tiles (d1a/settled.tsv, montages d1a/montage/) can join the person's read of ASKS row 120
- unglossed numerals p.3, p.4, p.5 right page, p.6 - blocker: not-attempted; independent material stays below the leaf's own gloss in coverage (p.3 0.563, p.5 independent 0.588) and p.4 independent and p.6 independent (D1411-P6b, 10 Oct: N=60 after 73 of 133 masked as a copy of p.2; T21r 0.500 vs shuffled p99 0.517) do not beat their order shuffle, while p.6's gloss agrees with T21r 9/11 (p99 3); next: read p.7 numerals under a copy of the p.6 PREREG and scorer (copy mask now over p.1-p.6; the measured 60-number pages are at the NON-TEST floor, so pool independent numerals across p.6-p.8 in a registered pooled test rather than another single-page gate), one DECODE login with the absolute filesrv URL, ~$5 per page
- p.4 4/5 residual (25 of 83 tiles unsettled, la2/applied.tsv) - blocker: waiting-on ASKS row 120 (a person's read; the 25 tiles can be added to that read or to a sign-sorter focus list); machine re-reads retired for this question
- gloss letter identities (z/r at 21, n/u, residue 14) - blocker: waiting-on ASKS row 120 (a person's read of the gloss); p.5 adds 26 pairs; residue 12 = h now favoured by p.5's letter test
- pages 7-12 numerals - blocker: not-attempted; full-size images re-fetchable with one DECODE login (absolute filesrv URL works, D1411-P6b); next: p.7 then p.8 the same two-pass step per page, ~$5 each, then the pooled independent test

## Escalation (AM-D1411P5, 7 Oct 2026; D1411-P6b, 10 Oct 2026)
- [x] siblings: GAPS136/GAPS137 checked the Ferdinand III posts and the Kopal Cyffra nova key (inconsistent sign class); p.5 left page found to be a second copy of p.2 (AM-D1411P5); p.6 right page a further copy of p.2 (D1411-P6b)
- [x] clear-pages: clear words around the cipher read in GAPS137; context words used only as post-hoc observation
- [x] known-keys: Cyffra nova ad Poloniam tested in GAPS137, inconsistent at step 1
- [ ] print: no printed edition of this letter located yet; planned print_check of the post-hoc words once a verifier accepts a PASS
- [x] key-rebuild: period gloss table (GAPS141), residue rule (GAPS146), residue 21 = r (DEF1-1411, D4-1411P3, R12A-D1411P4), residue 12 = h favoured on p.5 and T21r_h12 PASS on p.5 (AM-D1411P5) voided by AM-D1411V: in-sample copy of p.2; independent p.5 below gloss
- [x] image-check: D1A-D1411 (8 Oct) per-number tile comparison of the 13 p.2/p.5 copy differences: 2 settled, 1 genuine variant, 10 unsettled (control 30/31); remainder to a person's read (ASKS row 120)
- [retired] retry: the de17/de1600 4-gram language judge as gate, retired by GAPS157 third-attempt clause; also retired for the p.4 4/5 look-alike: machine re-read by a Sonnet shape reader (line crops R12A-D1411LA, then per-number tiles D07-D1411), a person's read is the remaining route
Verdict: keep going: 2 internal gaps; cheapest next: read p.7 (and p.8) numerals under a copy of the p.6 PREREG with the copy mask over p.1-p.6 and register a pooled independent-numeral test across p.6-p.8 (p.6 alone: N=60, at the floor, no PASS; gloss agrees 9/11), ~$5 per page; the p.2/p.5 copy differences go to a person's read (ASKS row 120)
