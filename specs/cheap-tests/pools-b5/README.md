# Census of QUEUE.md re-rank rows 5-9 (LANE B5 job bPOOL0)

26 Sept 2026, 01:33-01:42 UTC. Worker bPOOL0 (Sonnet), LANE B5 (orchestrator session_01A4jfQZGS8SUuDamZK19KZq).
Disk/git-only job (no image fetches, no login): built from the existing on-disk DECODE snapshot
`sources/decode/records-non-decrypted-2026-09-24.tsv` (1187 rows, fetched 24 Sept 2026 via `tools/decode_list.py`,
2 days old, used as-is per CLAUDE.md's "fetch once, keep a manifest" rather than re-crawling the same listing;
DECODE's non-decrypted catalogue does not turn over daily) plus one shallow clone each of `dbourdeau/cyphersolver`
(commit at clone time, MIT code / CC BY 4.0 text, deleted after) and `aaymeloglu/unsolved-ciphers` (no licence,
cited only). `records.tsv` (328 rows, script-generated from the TSV above, not hand-typed) has one row per DECODE
record id in each pool's shelfmark range, with a `has_transcription_or_key_bourdeau` column filled by grepping
Bourdeau's repo for the id ranges his own target folders name.

**Headline finding: none of these five rows is the blank canvas QUEUE.md describes.** Every one of them overlaps
a Bourdeau target folder that already carries a period key, a modern reconstructed key, or a full reading. The
open remainder in each pool is much smaller than QUEUE.md's row 5-9 letter/page counts suggest, because those
counts (traced to the LANE N4 scPOOL pass, 24 Sept 2026) were built by grouping DECODE's `holder_raw` field
alone, which does not see Bourdeau's own target work at all.

## 1. RAH, Signatura 9/23 (+9/24-9/25)

QUEUE row 5 claim: 133 + 38 = 171 letters, ~749 pages, "unmeasured". **What is actually there:** the DECODE
snapshot gives only 68 records across 9/23+9/24+9/25 (30+25+13), 303 pages -- not 171/749; QUEUE's figures do not
reconcile with the DECODE listing under any grouping tried here. **Not unexamined:** Bourdeau's `sanchez1522`
target (`RAH Salazar 9/23-9/26, DECODE R9593-R9657`) is this exact run, opened 20 Sept 2026, status "in progress".
Alonso Sánchez's cipher was already reconstructed by S. Tomokiyo (2025, cryptiana.web.fc2.com), and Bourdeau has
read the opening lines of most records plus two full passages (R9621, R9623 tail); a third of the tail
(R9634, R9644-46, R9648-50, R9652, R9656) is not Sánchez but **Lope Hurtado de Mendoza** -- the same sender LANE
B5's own bLOP job worked this session (R9634/46/49), confirming the overlap. Signs known from transcriptions:
Bourdeau's `sanchez1522/profile.json` documents only 33 tokens over 2 records (most records have no `length.tokens`
entry yet, consistent with "opening lines only"). Signs estimated: 303 pages x ~180 signs/page (this repo's own
Nevers-lane estimate for similar 16th-c. Spanish chancery hands, stated as an estimate) ~= 54,500. **Pool: yes**
against the 2,000-sign threshold on the page estimate, but the real, not-yet-transcribed remainder (excluding what
Bourdeau already read and excluding the Lope Hurtado tail already claimed by bLOP) is unmeasured. **Worked by:**
Bourdeau, in progress (not closed); not found in Aymeloglu's BNE-scoped catalogue (RAH is a different holding
library, no hits). **Image host:** bibliotecadigital.rah.es, Anubis-challenged to curl (probe: HTTP 307), needs
`tools/browser_fetch.js --binary` per the Access playbook row. **Recommendation:** a sampling worker here should
read `sanchez1522/NOTES.md` in full before touching a single page -- most of the cheap win (reading the
already-solved-cipher records Bourdeau has not yet reached) requires no image fetch at all, only applying
Tomokiyo's key to the DECODE ciphertext transcriptions already on file.

## 2. BAV, Barb.lat 6956

QUEUE row 6 claim: 98 letters, 1628-1629, ~542 pages, "unexamined by us". **What is actually there:** Barb.lat
6956 alone is 70 records / 202 pages, all dated 1628 only, in the DECODE snapshot; its sibling volume **Barb.lat
6960** (not named in QUEUE's row) is 29 records / 342 pages, dated 1629. Combined, 99 records / 544 pages --
matching QUEUE's "98 letters, 1628-1629, ~542 pages" almost exactly, so the row's own figure already silently
includes 6960. **Not unexamined -- the key is already published and matched:** Bourdeau's `pallotto1629` target
holds `DOC_R215` from Barb.lat 6956 itself: the reconstructed key (Biermann 2018, Bosbach, a merged version, and
a `codebreaker.py` decryption), a two-digit-homophone + three-digit-nomenclator nuncio cipher. George Lasry
identified that 6960 uses the *same* key as 6956, and Bourdeau applied it to all 28 of 6960's ciphertexts
(R286-R313): "every record decodes to running Italian," confirmed against Kiewning's 1897 printed edition
(*Nuntiaturberichte aus Deutschland* IV/2) word for word. About 2,000 nomenphonic groups resolve; ~1,750
three-digit groups are outside the known 6956 key and stay open. **The key has not yet been applied to 6956's own
69 other records** (only R215 is touched, as the key-document holder) -- this is the single cheapest lead in the
whole census: no sampling, no image fetch, just running the already-published key against the 69 already-
transcribed DECODE ciphertexts of 6956 itself. Signs known: 118,931 "tokens" (unit as given in `pallotto1629/
profile.json`, likely digit-groups not letters -- flagged, not verified) over the 28 read 6960 documents; 6956's
own 69 remaining records have no token count on file. Signs estimated: 202 pages (6956 remainder) x ~250
digits/page ~= 50,500 (estimate). **Pool: yes.** **Worked by:** Bourdeau (key + full 6960 reading); original key
by Biermann & Bosbach (2018, published), matched to 6960 by Lasry; not found in Aymeloglu's repo search.
**Image host:** BAV's IIIF is served by `digi.vatlib.it` (probe: HTTP 200, reachable), a different host from
`api.digitale-sammlungen.de` (that is BSB/Bavarikon, not BAV) -- no prior digi.vatlib.it row exists in CLAUDE.md's
host table; a sampling worker should add one after its first real fetch.

## 3. ARA Brussels, Secretairerie/Carpio-Fuenmayor

QUEUE row 7 claim: 44 letters, 1674-1678, ~186 pages, "one correspondent pair, the cleanest single-key-family
shape of the unmeasured pools". **Correction: it is not one correspondent pair.** DECODE's `inv.nr. 2559` box
(Baltasar de Fuenmayor's incoming correspondence) holds letters from **five** senders to Fuenmayor: Carpio (10),
Doria/Balbases (14), Núñez (4), Ronquillo (12), Salinas (8) = 48 records / 202 pages, 1577-1678 (one 1577 Doria
outlier outside QUEUE's stated range). **Fully read, not unexamined:** Bourdeau has four target folders covering
all five sender groups -- `carpio1677` (read, key reconstructed from the letters + margin decipherments),
`balbases1677` (read, "Balbases 1677 key" -- Pablo Spínola **Doria**, 3rd marqués de los Balbases, is the "Doria"
sender label), `hernannunez1674` (read), `ronquillo1676` (covers both Salinas and Ronquillo, read in part, 88.4%
of 23,463 groups, with four records -- R970, R973, R982, R984 -- being genuinely new readings beyond DECODE's own
transcriber). Signs known: 3,504 (carpio1677) + 23,463 (ronquillo1676, covers Salinas+Ronquillo) + 1,716
(hernannunez1674) = 28,683+ tokens documented in Bourdeau's own profile.json files (balbases1677's profile.json
has no populated token field despite a full prose write-up). **Pool: yes, already the largest confirmed
transcribed pool of the five, and already worked end to end.** **Worked by:** Bourdeau (4 targets, effectively
the whole box); not found in Aymeloglu's repo search. **Image host:** DECODE itself for the ciphertext
transcriptions (already used by Bourdeau); the underlying ARA images would be `search.arch.be` (probe: HTTP 302,
reachable) if a page image beyond DECODE's own scan is ever needed. **Recommendation:** this row should not go to
a sampling worker at all -- the open work, if any, is auditing/extending Bourdeau's readings (R970/973/982/984
margin-check, or the ~11.6% of ronquillo1676 groups still unread), not a first cheap test on an unmeasured pool.

## 4. ASV i1025, Segretario di Stato, Francia (dossiers 17-18 and neighbours)

QUEUE row 8 claim: "ASV i1025 SdS France 17-18", 44 letters, 1580-1589, ~193 pages. **The literal dossiers 17+18
are much smaller than this:** doss.17 (1583-85) + doss.18 (1585-88) = only 5 records / 17 pages in the DECODE
snapshot. The closest match to QUEUE's 44/193 figure is dossiers **17, 18, 22 and 283C together** (1580-1589,
2+3+36+2 = 43 records / 189 pages) -- doss.22 alone (36 records, 168 pages, 1588-89) dominates. Across all ten
France dossiers found in the snapshot (3, 6, 7, 17, 18, 22, 62, 64, 283C, 346; 68 records / 305 pages total),
**Bourdeau has already read every dossier except 346**: doss.3 (`santacroce1552`, closed/already solved and
in print, decifrati bound with the originals), doss.6/7 (`dandini1580`, read), doss.18 (`bergamo1585`, read,
0.990, R15 read before by Lasry), doss.22 (`morosini1588`, read 34 of 36 with Meister's printed key), doss.62/64
(`damiata1624`, read via the Roman office's own decipherment plus the reconstructed key already on DECODE).
**Doss.346 (`bagno1652`, 5 records, 1652) is the one genuine open item:** "the DECODE images were obtained and
checked in full... no decipherment, clear copy or matching key was found. No plaintext is claimed." Doss.17
itself (2 records) has no dedicated Bourdeau target found this pass -- unconfirmed, not excluded. Signs known:
234,005 "tokens" (unit unverified, likely digit-groups) over morosini1588's 2 aggregate document entries; 361
(damiata1624); 1,601 (dandini1580); 3,216 (bergamo1585); 3,933 (santacroce1552). **Pool: yes** on the read
dossiers; doss.346 and doss.17 (7 records, ~21 pages combined) are the only unmeasured/open remainder. **Worked
by:** Bourdeau, extensively (6 of 8 dossiers read or closed); George Lasry's key underlies several (bergamo1585's
R15, damiata1624); Meister's printed key underlies morosini1588; not found in Aymeloglu's repo search. **Image
host:** none named in this listing for ASV directly; DECODE serves the ciphertext transcriptions Bourdeau used
(probe: de-crypt.org HTTP 200); a raw ASV page image route is not established in CLAUDE.md's host table --
probed `www.vatican.va` as a plausible parent domain (HTTP 200) but this is not confirmed to host ASV's own
digitised Segreteria di Stato series. **Recommendation:** if this row is pursued at all, scope it to doss.346
(a genuine open 5-record item, already fully checked by Bourdeau against one candidate key) and doss.17 (2
unconfirmed records), not the 44-letter figure in QUEUE, most of which is already read.

## 5. ASV i1025, Segretario di Stato, Spagna 364C

QUEUE row 9 claim: 45 letters, 1717-1720, ~186 pages. **This reconciles exactly** once 364C (21 records/96 pages,
1717) and its continuation 364D (24 records/90 pages, 1717-1720) are combined: 45 records / 186 pages, matching
QUEUE's figure precisely -- the only one of the five rows whose stated numbers check out directly against the
DECODE snapshot. **Already fully read, not open:** Bourdeau's `nunzio1718` target (scoped to 364D, DECODE
R154-R177) reports that all 24 of its own records, *and the whole of 364C (items 1-32) alongside it*, were
already deciphered by **George Lasry in October 2020** -- a complete reconstructed key plus a 783 KB file of the
whole S364 corpus segmented and aligned line by line with the plaintext, filed as attached documents on the
DECODE records themselves (not visible in DECODE's own "partially decrypted" status label, which understates
this). Signs known: 34,243 tokens documented in `nunzio1718/profile.json` across its 24 records (364D only; 364C's
own count was not separately extracted by Bourdeau's profile but the same corpus file covers it). **Pool: yes**,
already the cleanest closed case of the five. **Worked by:** George Lasry (2020, published/relayed key, per rule
10's key-source vocabulary this reads as a `published` key once cited and verified, not `ours`); Bourdeau
(extended/verified, 21 Sept 2026); not found in Aymeloglu's repo search. **Image host:** DECODE holds the full
segmented reading as an attached document already (no image fetch needed to read it); if a page image is wanted,
same ASV-hosting caveat as row 4 applies (no confirmed route in CLAUDE.md's table; vatican.va probed HTTP 200,
unconfirmed as the right host). **Recommendation:** this is not a sampling-worker row at all -- it is a
verifier-and-write-up row (pull Lasry's segmented file off the DECODE records, grade per rule 4, get an N-class
per rule 10, since the key is `published` and the plaintext already exists).

## Reachability probes (one request per host, this session)

| Host | Probe | Result |
|---|---|---|
| bibliotecadigital.rah.es | `curl -A "Mozilla/5.0"` | HTTP 307 (Anubis challenge redirect, matches CLAUDE.md's documented finding) |
| digi.vatlib.it | `curl -A "Mozilla/5.0"` | HTTP 200 (reachable; not previously in CLAUDE.md's host table) |
| search.arch.be | `curl -A "Mozilla/5.0"` | HTTP 302 (redirect, likely reachable; not previously in CLAUDE.md's host table) |
| www.vatican.va | `curl -A "Mozilla/5.0"` | HTTP 200 (reachable; unconfirmed as ASV's actual image host) |
| de-crypt.org | `curl -A "Mozilla/5.0"` | HTTP 200 (already documented in CLAUDE.md) |

## Method notes / caveats

- "Signs known" figures are taken verbatim from `profile.json`'s `length.tokens` field in Bourdeau's own target
  folders; the field's `unit` (mixed/digits/tokens) was not independently re-verified for every folder in this
  pass -- treat large figures (118,931; 234,005) as order-of-magnitude, not exact sign counts, until re-checked.
- The DECODE snapshot used is 2 days old (24 Sept 2026); it was not re-fetched this pass (good-citizen /
  duplicate-work rules), so a handful of status changes since then (e.g. a record moving from "Non-decrypted" to
  "Decrypted") would not show here.
- `records.tsv`'s `has_transcription_or_key_bourdeau` column is filled by id-range lookup against what each
  Bourdeau NOTES.md/profile.json names for itself, not by opening every one of the 328 individual DECODE records;
  a handful of ids inside a named range (e.g. R23-R26, R50 in the France doss.22 range, which morosini1588's own
  NOTES.md says are non-cipher material) may be mismarked as covered when they are administrative filler --
  documented in NOTES.md line-by-line for anyone who needs the exact set.
- No image was fetched, no login was attempted, no sign was counted by eye. Every number here traces to a file
  already on disk in one of the two solver repositories or this repository's own DECODE snapshot.
