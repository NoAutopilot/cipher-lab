blocked
Read (26 Sept 2026, bZES): Bourdeau's `zeschau1841/` folder and CATALOGUE.md #53 in full at HEAD fc0c9e8
(25 Sept 2026, `github.com/dbourdeau/cyphersolver`, shallow clone, deleted after); Aymeloglu's
`catalogue/decode-records.jsonl` at HEAD (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone, deleted
after, no per-item solve, catalogue mirror only); DECODE's own RecordsList cache
(`sources/decode/records-non-decrypted-2026-09-24.tsv` rows 849-852) plus one live `RecordsView/5006` fetch
(200, "Access mode: Authentication required", thumbnail template unfilled without a session); one OpenAlex
query (`search=Zeschau Seebach cipher`, 0 results) and one Semantic Scholar query (same terms, 0 results).

## Who, what

Heinrich Anton von Zeschau (Saxon foreign minister, Dresden) to Albin Leo von Seebach (Saxon minister resident,
St Petersburg). Saxon Main State Archive Dresden, HStAD 10731 Sächsische Gesandtschaft in Russland, Nr. 12.
DECODE R5005 (18 Jan 1841, French), R5006 (6 Apr 1842, French), R5007 (13 Jun 1842, German; DECODE's own record
mistypes the year as 1846), R5008 (26 Oct 1843, German). Bourdeau CATALOGUE.md #53.

## Established (H/C-grade facts, not our cryptanalysis)

- R5005 is fully transcribed by Bourdeau: 3,969 digits, unseparated two-digit groups (96 of 100 pairs occur),
  about 70 lines across 6 images / 5 written spreads. Source: `zeschau1841/ct_R5005.txt`,
  `zeschau1841/ct_R5005.digits.txt` (Bourdeau, MIT code / CC BY 4.0 text, credited).
- The cipher is a syllabary, not a letter substitution (Bourdeau's own diagnosis from a faintly-visible pencil
  decipherment still on R5005 p.5 right, line a5_03: `11 70 82 34 29 40` glossed "la pre m i er e").
- Seven values recovered from that gloss: **11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que** (46 from the end of
  line a8_05). Grade **I** (inferred from a rubbed, partially-legible pencil trace, not a clean key source) --
  Bourdeau's own NOTES.md does not claim these as certain.
- Bourdeau tried these values on R5005 only (homophonic/syllabary annealers seeded with the glosses, all
  failed to produce French) and explicitly did **not** try them against R5006-R5008 ("R5006-R5008 are not
  transcribed yet" -- his own NOTES.md, "What would move it" item 3).
- R5006/R5007/R5008 have no ciphertext transcription anywhere found: not in Bourdeau's `zeschau1841/` folder
  (only `ct_R5005.*` exist), not in Aymeloglu's catalogue mirror (metadata only, `Available Documents: ""` for
  all four ids), not on DECODE without login (see below).
- DECODE's own status for all four records is "Partially decrypted" ("interlinear decrypted, but unfortunately
  rubbed out"), page counts R5005=9, R5006=2, R5007=3, R5008=3 (`sources/decode/records-non-decrypted-2026-09-24.tsv`).
- No printed edition of this correspondence found by Bourdeau or by this pass's OpenAlex/S2 queries (0 hits
  each); not searched further per the intake step's minimal scope.

## The test this job was assigned, and why it stopped

Brief: apply the 7 recovered syllabary values to R5006-R5008 as a crib wherever their ciphertext is on disk,
with a random-digit-string coverage control and an order-scrambled German-bigram control (CLAUDE.md rule 3,
order-sensitive statistic since a coverage figure alone cannot distinguish a real crib from noise -- see
CLAUDE.md's "bCAS"/"AX-5799" lesson on non-tests, 26 Sept 2026).

**Blocked before the test could run: no ciphertext for R5006, R5007 or R5008 exists on any disk this account can
read.** Checked, in the Access playbook's order:
1. Bourdeau's own folder -- absent (confirmed above).
2. A DECODE attachment readable without login -- absent. `RecordsView/5006` (live fetch, 26 Sept 2026, 200 OK,
   one request) shows the record's own "Access mode: Authentication required" field, and the page's image
   slots are an unfilled `{{>thumbnailUrl}}` template with only a 1x1 placeholder GIF as the actual `src` --
   no image URL is exposed to an unauthenticated fetch, consistent with the Access playbook's account-wide
   DECODE image block (confirmed on 25 other records across 6 institutions, ASKS.md row 42) and with
   Aymeloglu's mirrored `"Paper Access Mode": "Authentication required"` for all four ids.
3. The holding archive itself -- QUEUE.md's own CS2-09 entry (LANE N4 scARCH2, 24 Sept 2026) already resolved
   this exact shelfmark (`archiv.sachsen.de`, guid `fb8ee3d8-3829-4665-8b8f-45c2574196d7`) to
   `digitalisatExists: false`: the whole Nr. 12 dispatch file is not digitised at all, so no route through the
   archive's own site gets an image either. Not re-fetched this pass (already on file, dated).

No browser login was spent (the Access playbook already establishes the DECODE image block holds even when
logged in, so a login would not clear it); no image or archive host was newly hit beyond the one `RecordsView`
GET above.

Per CLAUDE.md's rule 9a/ASKS.md convention, the only route left is a physical copy order from HStAD Dresden for
10731 Sächsische Gesandtschaft in Russland, Nr. 12 (a mixed ministerial-dispatch file, not letter-specific --
the exact leaves for R5006/R5007/R5008 within it are not known from any metadata read this pass). Not written
as a fresh REQUEST.md this job (out of the brief's scope and cap); ASKS.md row 42 already covers the general
DECODE account-wide image block this finding rests on.

## Credit

Bourdeau, `dbourdeau/cyphersolver`, `zeschau1841/` folder and CATALOGUE.md #53, read 26 Sept 2026 at commit
fc0c9e8 (25 Sept 2026 18:14 CDT). MIT code, CC BY 4.0 text. The 7 syllabary values above are his recovery, not
ours.

## GAPS173-zeschau-seebach-1841 (3 Oct 2026, account-4)

Step run: Next step 1 (the HStAD Dresden copy order) needs a person, but its purpose -- images of R5006-R5008 --
has a cloud route since 28 Sept 2026: DECODE serves full-size scans after a browser login (sources/decode/NOTES.md
"Full-size images: access after the PI's extension", DECODE-OPEN, which fetched only the first image of each of
these records). This pass ran that route for all six images.

- One login (`tools/decode_browser_login.js 5006 <scratch> --fetch-page RecordsView/5007,5008 --guess-fullsize`,
  `loggedIn: true`, 3 Oct 2026 16:59-17:00 UTC). Six full-size JPEGs, all 7214x5412, none the `forbidden.png`
  placeholder. Images stay in the session scratchpad only, never in this repository (the PI's reminder: the holding
  archive's permission may be needed before any image is published); a later worker refetches them the same way.

| file | sha1 (12) |
|---|---|
| IMG_R5006_I28865_P1.jpg | 483bbb1d719f (matches DECODE-OPEN) |
| IMG_R5006_I28865_P2.jpg | 27186d7b5d48 |
| IMG_R5007_I28868_P1.jpg | b5ec8e9e93cd (matches DECODE-OPEN) |
| IMG_R5007_I28868_P2.jpg | c081766ef775 |
| IMG_R5008_I28871_P1.jpg | 86e6105b60fe (matches DECODE-OPEN) |
| IMG_R5008_I28871_P2.jpg | 17a51f08bf33 |

- Vision call 1 (downscaled overview of R5006 p.1): heading "No. 13", "Dresde, ce 6 Avril 1842", clear French
  opening "J'accuse la réception de Vos rapports inclus le n° 17 du 22 Mars", then 9 lines of unseparated digits
  on the leaf, which takes about a third of the image width (the rest is the copy-stand background). A red archival
  foliation note sits at the foot (not read).
- Vision call 2 (one native-resolution line crop, `tools/iiif_lines.py --image` on a local crop of the page body, 8
  lines found): the first cipher line is fully legible, about 68 digits, written in the same unseparated style as
  R5005. Faint pencil traces show above the digits, which fits DECODE's own note "interlinear decrypted, but
  unfortunately rubbed out". No digit string is committed here: one unchecked read is not a transcription (rule 2/4).
- Estimate, from 9 lines x ~68 digits on R5006 p.1: about 600 digits a page, roughly 3,000-3,600 digits over the
  six pages, nearly doubling the 3,969 digits of R5005 now on disk (Bourdeau).
- Not done: no transcription, no crib test, no reading. Status word left `blocked` for the parent to change: the
  outside blocker it named (no images anywhere reachable) no longer holds.

Requests: de-crypt.org 1 login + 3 RecordsView + 12 filesrv (6 thumbnails, 6 full-size) = about 17, 2 s apart, one
at a time. No other host.

## Next step (refreshed 3 Oct 2026, GAPS173)

1. Transcribe R5006-R5008 (6 pages) from the DECODE scans: refetch them with one login as above, crop with
   `tools/iiif_lines.py --image`, two blind passes a page on line crops (one page per subagent call), then
   `tools/reconcile_passes.py`. That is 12 pass-calls + 1 reconciliation at the 3 Oct ledger's Opus native-vision
   rate (USD 3.5-10 a pass), about USD 45-65 in total.
   Mark the rubbed pencil traces above the digits as they are found: they may give more gloss values (grade I).
2. Then apply Bourdeau's 7 values as a crib with the coverage + order-scrambled controls the bZES brief specified.
3. The HStAD copy order (ASKS 64, SEND-QUEUE S5, still `queued` on 3 Oct) is no longer needed to get images; the
   parent decides whether to hold S5 or reword it as a permission/quality request. Multispectral/UV imaging of
   R5005 (Bourdeau's suggestion) stays a person/archive step.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/zeschau1841/NOTES.md
- Their extent, in their words: attempted, open: system identified, a few code values from the erased decipherment, letters not read
- Their date: by 25 Sept 2026 (undated in NOTES)
- Note: already cited in our NOTES.md (bZES, 26 Sept)
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.
