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

Next action that depends on nobody: transcribe the unglossed numerals of p.1 (lower block) and test the frozen mod-24 residue rule found by GAPS141 against them (see the GAPS141 section); the glossed pairs are harvested (gloss/pairs.tsv).

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
