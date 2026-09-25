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
