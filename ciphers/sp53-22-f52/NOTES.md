open
Tomokiyo's own page `sources/cryptiana/web/mary.htm:879-887` read directly by this worker (not quoted from another source), and CSP Scotland vol.9 (Boyd, archive.org `calendarofstatep08grea`, A.D. 1586-1588, the volume covering the Chartley/Babington seizure this item belongs to) full-text searched with a control ("Chartley", 19 hits) for "spanish sp[yi]" and "f. 52" -- no hit; SP53/22 is TNA's own key/cipher-table volume and is not itself calendared letter-by-letter the way correspondence is, so this negative is consistent, not surprising.

## Check-solved (LANE CX, 25 Sept 2026)

Six-source sweep per `.claude/briefs/check-solved.md`. Worker CX-MARY (session_01WTB2Xohu8ioui6gsRHFF86).

1. **Web search** (a): `"SP53/22" "Spanish spy" cipher Mary Queen of Scots solved` -- no hit naming this specific folio; general Mary-cipher literature only (Lasry/Biermann/Tomokiyo 2023 Cryptologia, on the 1578-84 Castelnau letters, a different cipher family). No model-solve announcement.
2. **Standard edition** (b): Tomokiyo's page read directly, `sources/cryptiana/web/mary.htm:879-887`: "**SP53/22 f.52** ... 'Cifer with\* Spanish Spye:' 'Spanish spy' ... A short ciphertext." with the transcription given inline (matches this folder's `ciphertext.txt`). No decipherment or key given on the page. CSP Scotland vol.9 (archive.org `calendarofstatep08grea`, downloaded and full-text searched this pass, control "Chartley" 19 hits confirming this is the right volume for the 1586 Chartley seizure that SP53/22 belongs to): no hit for "spanish spy"/"f. 52". SP53/22 itself is described by Tomokiyo (`mary.htm:646`) as "a collection of 'Ciphers, including those for papers seized at Chartley Castle...'" -- i.e. TNA's own key-table volume, which CSP Scotland calendars as a class, not folio by folio the way it calendars correspondence; a negative full-text search here is the expected result, not evidence of anything missed.
3. **Community lists** (c): Cryptiana read above; cipherbrain.de -- WebSearch `cipherbrain.de Mary Queen of Scots SP53/16 OR SP53/22 OR Moray Wood cipher` returns nothing from that site. No list-post comment thread found for this item.
4. **DECODE** (d): `sources/decode/records-*-2026-09-24.tsv` (24 Sept full crawl, on disk) grepped for "box 22" -- **zero rows in either the Decrypted or Non-decrypted files.** DECODE's catalogue has no record at all for TNA SP53 box 22, so no record for f.52 specifically.
5. **Bourdeau** (e): fresh shallow clone (25 Sept 2026) `sp53/NOTES.md`: f.52 attacked first session (15-16 Sept 2026) alongside nos.78/79. Quote: "**f. 52**: 84 tokens over 22 symbols. Homophonic annealing in Spanish, French, English and Italian gives fluent nonsense at -2.1 to -2.4 nats/letter; matched 84-token controls in the same four languages are **not solved** either (-2.0 to -2.3 against -1.26 to -1.32 for the truth). Below unicity; no reading claimed." Not revisited in the second or third sessions (those focus on 78/79 only) -- "f. 52 is unchanged (84 tokens, below unicity)" per the third session's closing summary. No update since 16 Sept.
6. **Aymeloglu** (f): fresh shallow clone (25 Sept 2026, HEAD `2495c45`). No sp53/f52 folder found by name; the existing NOTES.md's "All 61 SP53/22 key images tried (Aymeloglu)" claim (19 Sept) could not be independently re-verified from folder names alone in this pass (no `sp53` folder exists in this repo to grep) -- likely refers to Aymeloglu's DECODE/catalogue harvest rather than a dedicated target folder; flagging that this specific claim rests on the prior worker's citation, not this worker's own read, since I found no `sp53`-named path here to check directly.

Intake verdict: open (both editions on the target's own claim -- Tomokiyo's page and the CSP Scotland volume -- were opened and read by this worker, with a control for the full-text search).

Requests this pass: archive.org 2 (metadata + download for `calendarofstatep08grea`, reused from the sp53-16-78/79 pass, >=1.5s apart), github.com 2 (fresh shallow clones, shared with 78/79/moray passes), WebSearch x2.

---

# SP53/22 f.52, "Cifer with Spanish Spye"

- **Source:** TNA SP53/22, a collection of ciphers related to Mary, Queen of Scots. f.52 is a short undeciphered ciphertext endorsed "Cifer with[?] Spanish Spye". The verso of the cipher key at f.40 also carries a short undeciphered ciphertext.
- **Status:** Open.
- **Transcription:** `ciphertext.txt` (Tomokiyo's, from unsolved.htm). Tokens separated by `;`. Base numbers 0-13, with a `b` variant on many.
- **Background page:** `sources/cryptiana/web/mary.htm`.
- **Ideas:** Very short (about 90 tokens) with only 0-13 plus `b` variants, so about 28 symbols. That's alphabet-sized. Likely a simple substitution for Spanish or English. Short enough that a key among the SP53/22 ciphers may apply directly; try f.40's key first.
- **Solver status (19 Sept 2026):** Closed-negative by both, 15-16 Sept 2026. Below unicity: matched 84-letter controls solve in six languages, the target does not. All 61 SP53/22 key images tried (Aymeloglu).

## Solver-repo check (aymeloglu, 2 Oct 2026)

Fresh shallow clone of github.com/aaymeloglu/unsolved-ciphers, HEAD d2800bb (27 Sept 2026); the repository has no issues (0 results on the issue tracker, read 2 Oct 2026) and 25 pull requests, all the owner's own, the last on 27 Sept 2026 (cipherkit diagnostics, no target rows). Only one commit since our 25 Sept check (HEAD 2495c45): nothing about this target changed. Their record stands as TARGETS.md row 14: SP 53/22 f.52, "Cifer with Spanish Spye": closed-negative 16 Sept 2026 (matched 84-letter controls solve in six languages, the target a full gram worse under every hypothesis; all 61 key images negative). Work kept private (no public folder); no licence, cited not copied. Class b (attempted and closed) in sources/solver-diffs/2026-10-02-aymeloglu.tsv. Worker SOLVERDIFF-AYMELOGLU (account 2).

## Solver-repo check (bourdeau, 3 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 2341682 (2 Oct 2026), plus open PR 17 (refs/pull/17/head) and the issue/PR lists read 3 Oct 2026. Their record for this item is unchanged: `targets/sp53/NOTES.md`, "SP 53/16 nos. 78 and 79 (1585?) and SP 53/22 f. 52 -- attempted 2026-09-16 and 2026-09-15 (second session), not solved" (D. Bourdeau; text CC BY 4.0, quoted with credit). No commit, issue or PR since 1 Oct touches SP 53. Class b (attempted, not read) in sources/solver-diffs/2026-10-03-bourdeau.tsv. Worker SOLVERDIFF-BOURDEAU (account 2).

## Solver-repo check (aymeloglu, 3 Oct 2026)

Re-check of https://github.com/aaymeloglu/unsolved-ciphers by SOLVERDIFF-AYMELOGLU (account 2), 3 Oct 2026 00:13-00:50 UTC:
their HEAD is still d2800bb (27 Sept 2026) and PR refs 1-25 are unchanged, so the 2 Oct section above still holds:
TARGETS.md row 14 lists this item closed-negative on 16 Sept 2026, work private (no public folder or ciphertext).
Class b (attempted and closed there). Their issue tracker could not be read from this session (HTTP 403 through the
proxy). Row in sources/solver-diffs/2026-10-03-aymeloglu.tsv. Status line not changed here.

## Web and blog check (GF4-BATCH20 (account-4), 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026): (1) `"Spanish Spye" cipher SP 53/22 Mary Queen of Scots` -- TNA education page for SP 53/22 f.1, the Glasgow MQS project, Lasry/Biermann/Tomokiyo 2023 (the 1578-84 letters, a different set), Babington Plot pages; nothing on f.52; (2) `"Cifer with Spanish Spye" OR "Spanish spy" cipher Tomokiyo Chartley solved` -- Phelippes/Babington pages and the 1930s Spanish strip cipher (unrelated); nothing on f.52; (3) shelfmark + "cipher" is query 1; the item's own descriptive title is query 2's quoted phrase. The ciphertext is numerals only, so there is no distinctive clear-text phrase to search.
Blog site searches: Cipherbrain (scienceblogs.de/klausis-krypto-kolumne `?s=Maria Stuart`): 5 posts, none about this item; klausschmeh.net (Schmeh's blog since 2026) `?s=Mary Stuart` and the "Solved cryptogram" category page (4 posts, 21 Sept-1 Oct 2026: ADFGVX, WWII Enigma, Copenhagen, Koehler): nothing on Mary Stuart ciphers; Cryptiana blog (cryptiana.blogspot.com `search?q=Mary Queen of Scots`): 19 posts 2019-2026, none naming SP53/22 or a "Spanish spy" cipher; Tomokiyo's on-disk pages (`sources/cryptiana/web/mary.htm:879-887`, `sources/cryptiana/web/unsolved-2026-09-24.htm:96-97`, zero requests): f.52 still listed as "a short undeciphered ciphertext" on the 24 Sept 2026 snapshot of his unsolved page; Cipher Mysteries (`?s=Mary Queen of Scots`): Nothing Found.
Comment threads: no post about this item was found, so no thread to read.
Model-solve and new-publication check: Apeiron (apeiron.re front page: no listing of solved items is served; nothing on this item); the Cabinet Noir repository (github.com/el-descifrador/cabinet-noir, shallow clone HEAD 47b6db9, 2 Oct 2026, 26 target folders, all French/Spanish/German 1568-1824 nomenclators) grepped for `sp ?53`, `spanish spy`, `spye`: no hit.
Result: no decipherment or plaintext of this item located by these queries on 3 Oct 2026 (a search result, not a novelty verdict, rule 10). Status word unchanged.
Requests: WebSearch 2, scienceblogs.de 1, klausschmeh.net 2, cryptiana.blogspot.com 1, ciphermysteries.com 1, apeiron.re 1, github.com 1 clone (shared with goldbar-1933 and eckert-1864); all >=1.5 s apart.

## Premise check (GF4-BATCH20 (account-4), 3 Oct 2026)

(a) Folder's own mentions: **not found** -- no decipherment, gloss or clear copy of f.52 is mentioned anywhere in NOTES.md, REQUEST.md or `specs/`. One premise flag, from Tomokiyo's own page: in this volume the other leaves are keys endorsed "Alphabet with <correspondent>" (f.50 "Alphabet with the B. of Rosse", f.54 "Alphabet with Tho. Throgmorton"), and f.52 is endorsed "Cifer with* Spanish Spye". Tomokiyo transcribes it as a short ciphertext, and both solvers attacked it as one; whether the leaf also carries a plain line or key (which would make it a key sheet, not a message) cannot be settled without the image (REQUEST.md item 1).
(b) Other solvers' working files: **not found** -- Bourdeau's `targets/sp53/NOTES.md` (public) records homophonic annealing in four languages with matched 84-token controls also unsolved, no reading; Aymeloglu keeps the work private (TARGETS.md row 14: 61 key images tried, all negative). No rendering of f.52 under any key exists in either repository.
(c) Physical neighbours: **unreachable** -- SP 53/22 is not digitised (REQUEST.md). From Tomokiyo's descriptions only: f.50 Bishop of Ross alphabet, f.51 a skipped number, f.53 a French nomenclator (Paget 83, Arundel 84, Morgan 85, Fontenay 86), f.54 Throckmorton's alphabet; none is described as a decipherment of f.52. The verso of f.52 is not described.
(d) Recipient's side: **not found / not applicable** -- no correspondent is named beyond "Spanish spy"; CSP Scotland vol. 9 was full-text searched on 25 Sept 2026 (section above, no hit). A CSP Spain (Simancas) vol. 3 search would need a name to search for; none is known.
Verdict: the premise holds as far as can be checked without the image; the item stays `open`.

## While waiting

The one action that depends on nobody: re-read Tomokiyo's live `unsolved.htm` and `mary.htm` entries for f.52 against the 24 Sept snapshots on disk (zero-cost diff), and check whether either page now gives an image reference for 092.jpg/093.jpg (the HTML comment on both entries), which would show what the leaf holds before the TNA copy order (REQUEST.md) is placed.

Gate after this pass (3 Oct 2026, GF4-BATCH20): `python3 tools/intake_gate_check.py sp53-22-f52`
```
sp53-22-f52: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```
`python3 tools/next_steps.py --wait-only | grep sp53-22-f52`: no line.

## Next step (NO-CRACKS, 5 Oct 2026)

next: diff Tomokiyo's live unsolved.htm and mary.htm entries for f.52 against the 24 Sept snapshots on disk and check for an image reference (092.jpg/093.jpg), ~$0.2, before the TNA copy order (REQUEST.md; not yet in outreach/tna-page-copy-batch.md as of 5 Oct 2026). Who acts: agent. Source: this file's "## While waiting"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.
