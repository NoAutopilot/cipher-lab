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

Next action that depends on nobody: one DECODE browser login (`tools/decode_browser_login.js 1411 ...`) to fetch
R1411's images, check the leaves against the "Cyffra nova ad Poloniam" key and Kopal's letters A-E (same fascicle,
ff. 174-212), and confirm whether R1411 is one of their letters' copies or drafts before any transcription.

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
