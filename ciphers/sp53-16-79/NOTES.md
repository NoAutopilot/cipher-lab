blocked
CSP Scotland vol.8 (Boyd 1898, HathiTrust `miun.abe1726.0008.001`) pp.211-212 -- HTRC EF word-count test found "tempest", "barret", "cipher" and "paris" co-occurring there (control "phelippes", 122 pages, confirming this is the right correspondence circle) -- a probable calendar entry covering this letter's companion (Tempest) and possibly this one (Barret), but HathiTrust's own page text/images are Cloudflare-blocked from the cloud and could not be read; LOCAL-QUEUE.tsv row L13 filed.

## Check-solved (LANE CX, 25 Sept 2026)

Six-source sweep per `.claude/briefs/check-solved.md`. Worker CX-MARY (session_01WTB2Xohu8ioui6gsRHFF86). Run jointly with `../sp53-16-78` (same hand, same edition, same solver-repo session); see that folder's log for the full method. Differences for this item noted below.

1. **Web search** (a): `"SP53/16" "no. 78" OR "no.78" Mary Queen of Scots cipher Tempest solved` (covers the pair; Barret/no.79 not separately named in any hit) -- no model-solve announcement, no page naming no.79 as solved.
2. **Standard edition** (b): Tomokiyo's own page `sources/cryptiana/web/mary.htm:494-495` (read on disk): "Another anonymous letter in cipher in the same handwriting (copyist's?), addressed to Doctor Barret, President of the English seminary at Rheims. Endorsed by Phelippes." (no "deciphered" note either way, unlike no.78's explicit "Not deciphered" -- both are listed under Tomokiyo's unsolved heading for this section, `mary3.htm:52-53` repeats the same wording). Boyd's CSP Scotland vol.8 (HathiTrust `miun.abe1726.0008.001`) pp.211-212: same HTRC EF hit as no.78 -- "barret" itself hits pp.212 and 749 specifically (`--words tempest,barrett,barret,phelippes,rheims`), consistent with the same calendar entry or an adjacent one covering both letters. Blocked from reading the actual page text (Cloudflare), same as no.78; same LOCAL-QUEUE row L13 covers both targets.
3. **Community lists** (c): same cipherbrain.de/Cryptiana search as no.78 -- no hit naming no.79 specifically.
4. **DECODE** (d): `sources/decode/records-*-2026-09-24.tsv` box 16 rows (7 total, all Decrypted, items 11/15/16/26-29) do not include item 79. **DECODE has no record for SP53/16 no.79.**
5. **Bourdeau** (e): fresh clone (25 Sept 2026) `sp53/NOTES.md`: no.79 (644 tokens +27 illegible, 102 distinct with variants) closed-negative in the same three sessions as no.78. Second session found the pooled 78+79 frequency profile correlates well above chance (Pearson 0.35 vs 0.00+-0.09 for shuffles, P<0.0002) suggesting one shared key, but the third session's stronger solver *retracted* that: "If nos. 78 and 79 shared one clean letter key, the pooled 1151 tokens would solve as the pooled controls did; instead the pooled text scores worse than either letter alone... Either the keys differ, or at least one letter is not a letter cipher with a modest nomenclator." No.79 alone: French with base labels -2.496 after 168 restarts (below any solved control); "variants scoring better than base labels suggests the letter suffixes mark distinct symbols, not glyph variants" -- an open transcription-design question for a future worker with images. No update since 16 Sept.
6. **Aymeloglu** (f): fresh clone (25 Sept 2026, HEAD `2495c45`). No sp53/78/79 folder or TARGETS.md row found. Not attempted there.

Intake verdict: blocked (same specific unreadable edition page as `sp53-16-78`).

Requests this pass: shared with `sp53-16-78` (see that file); no additional network requests specific to no.79 beyond the tsv/repo greps already counted there.

---

# SP53/16 no.79 (1585?)

- **Source:** TNA SP53/16 no.79. Anonymous letter in cipher, same hand as no.78, addressed to Doctor Barret, President of the English seminary at Rheims. Endorsed by Phelippes.
- **Status:** blocked (corrected LANE CX 25 Sept 2026 -- see check-solved verdict at the top of this file).
- **Transcription:** `ciphertext.txt` (Tomokiyo's). Tokens separated by `;`. Includes lettered variants (01a, 01b, 01d, 08b, 08c, 16b-16e, 18b, 18c, 24b, 38b, 39b, 83c, 84f, 88b, 101b) and empty tokens `;;` marking illegible or doubtful symbols.
- **Companion:** `../sp53-16-78`.
- **Background page:** `sources/cryptiana/web/mary.htm`, `mary3.htm`.
- **Ideas:** The lettered variants may be diacritic marks on base numbers, a common device in Mary-era ciphers to extend the table. Work no.78 and no.79 together to pool frequency counts (but see Bourdeau's third-session retraction above: the pooled text scores *worse* than either letter alone under the stronger solver, so a shared key is no longer supported).
- **Solver status (19 Sept 2026):** Closed-negative by Bourdeau (cyphersolver/sp53) and Aymeloglu (TARGETS row 13), 15-16 Sept 2026. Scores at random level; the claim that it shares a key with no. 78 was withdrawn. Needs page images.

## Solver-repo check (aymeloglu, 2 Oct 2026)

Fresh shallow clone of github.com/aaymeloglu/unsolved-ciphers, HEAD d2800bb (27 Sept 2026); the repository has no issues (0 results on the issue tracker, read 2 Oct 2026) and 25 pull requests, all the owner's own, the last on 27 Sept 2026 (cipherkit diagnostics, no target rows). Only one commit since our 25 Sept check (HEAD 2495c45): nothing about this target changed. Their record stands as TARGETS.md row 13: SP 53/16 nos. 78-79 (Phelippes endorsements): closed-negative 16 Sept 2026 (controls at 3 homophones per letter read, 6 -- the real density -- do not; every SP 53/22 key image excluded). Work kept private (no public folder); no licence, cited not copied. Class b (attempted and closed) in sources/solver-diffs/2026-10-02-aymeloglu.tsv. Worker SOLVERDIFF-AYMELOGLU (account 2).

## Solver-repo check (bourdeau, 3 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 2341682 (2 Oct 2026), plus open PR 17 (refs/pull/17/head) and the issue/PR lists read 3 Oct 2026. Their record for this item is unchanged: `targets/sp53/NOTES.md`, "SP 53/16 nos. 78 and 79 (1585?) and SP 53/22 f. 52 -- attempted 2026-09-16 and 2026-09-15 (second session), not solved" (D. Bourdeau; text CC BY 4.0, quoted with credit). No commit, issue or PR since 1 Oct touches SP 53. Class b (attempted, not read) in sources/solver-diffs/2026-10-03-bourdeau.tsv. Worker SOLVERDIFF-BOURDEAU (account 2).

## Solver-repo check (aymeloglu, 3 Oct 2026)

Re-check of https://github.com/aaymeloglu/unsolved-ciphers by SOLVERDIFF-AYMELOGLU (account 2), 3 Oct 2026 00:13-00:50 UTC:
their HEAD is still d2800bb (27 Sept 2026) and PR refs 1-25 are unchanged, so the 2 Oct section above still holds:
TARGETS.md row 13 lists this item closed-negative on 16 Sept 2026, work private (no public folder or ciphertext).
Class b (attempted and closed there). Their issue tracker could not be read from this session (HTTP 403 through the
proxy). Row in sources/solver-diffs/2026-10-03-aymeloglu.tsv. Status line not changed here.

## Web and blog check (CS-BATCH6, 3 Oct 2026 15:44 UTC)
Queries (WebSearch, standard, 1 each): `"SP53/16" Tempest Barret cipher Mary Queen of Scots Phelippes letter deciphered` -- only generic Mary/Phelippes pages (TNA education page, Discovery C13595 series record, popular articles); none names no.78 or no.79. Google Books API (country=US, key): 3 queries on Tempest/Barret/cipher/Phelippes -- hits are the 1858 Thorpe calendar volumes only. Site searches of Cipherbrain, the Cryptiana blog and Cipher Mysteries were not run this pass beyond the standard query above (not logged as searched); the earlier 25 Sept 2026 CX-MARY log (above) searched cipherbrain.de with no hit. Tomokiyo's own pages (on disk, `sources/cryptiana/web/mary.htm:491-495`, `mary3.htm:49-53`): no.78 "Not deciphered."; no.79 no decipherment noted.

## Edition read by this worker (CS-BATCH6, 3 Oct 2026 15:44 UTC)
Thorpe, *Calendar of State Papers relating to Scotland* (1858), Appendix/Mary Queen of Scots in England section, archive.org `calendarstatepa00thorgoog` (djvu text on disk in scratchpad, scan p.562 per be-api): entries read verbatim -- "78. Anonymous letter, in cipher, to Mr. Tempest, an English priest resident at Paris. Fr. [Indorsed by Mr. Phelippes.]" and "79. Another anonymous letter, in cipher, in the same handwriting, addressed to Doctor Barret, President of the English seminary at Rheims. [Indorsed by Mr. Phelippes.]"; both dated "1585?" (between Vol. XVI no.76 and Jan 1586); index gives "Barret, Dr., 980" and "Tempest, Mr., 980". No decipherment, key or plaintext is printed; no.77 (same volume, a cipher letter indorsed by Phelippes "to be written to Pietro [Gilbert Giffard] his father") is likewise calendared as cipher only. Thorpe's two vol.1 copies (`10278864bsb`, `cu31924091754360`) are the 1509-1589 volume and do not carry the entry. Still not read: Boyd's *Calendar* vol. 8 pp.211-212 (the HTRC EF word-count hit): the only archive.org copy found, `calendarofstatep0008vari`, is lending-only (djvu 401) and its be-api index is a different volume (Nicolson, 1590s; "Tempest" 0 hits); `calendarofstatep08grea` is vol. IX (1586-88; "Tempest" occurs only at an Edward Tempest, 15-year-old, and index p.41) -- neither is vol. 8. HathiTrust remains Cloudflare-blocked (LOCAL-QUEUE row L13). Requests: archive.org 9, be-api 12, googleapis 6, github.com 2, WebSearch 1.

## Premise check (CS-BATCH6, 3 Oct 2026 15:44 UTC)
(a) Folder mentions of a decipherment -- not found: NOTES.md says "Not deciphered" (Tomokiyo) and cites no decipherment; the prior CX-MARY pass found none.
(b) Other solvers' working files -- not found: fresh shallow clones 3 Oct 2026, dbourdeau/cyphersolver (HEAD a439937) `targets/sp53/NOTES.md`, SP53_16_78/79.txt, profile.json are attempts at Tomokiyo's transcriptions (not a key); aaymeloglu/unsolved-ciphers (HEAD d2800bb) has no hit for sp53.16 or Tempest. No key applied to these texts by anyone found.
(c) Physical neighbours -- unreachable: no image of SP53/16 ff. for nos.77-79 is on disk. Calendar neighbour no.77 is a cipher letter with Phelippes's indorsement; Tomokiyo's page lists SP53/18 no.76/77 (a different item) as deciphered in Phelippes's hand, so the Phelippes decipher habit is real but no decipher is calendared for no.77-79 in Thorpe.
(d) Recipient-side edition -- partly: Thorpe 1858 read (above); Pollen, *Unpublished documents relating to the English martyrs* (CRS 5) prints a letter naming "Doctor Barret" and "Mr. Tempest here at Parice" (be-api hit on `unpublisheddocum05poll`) -- context for the correspondents, not a decipherment; Boyd vol. 8 unread.

## While waiting
Next action that depends on nobody: be-api full-text search of the other Boyd volume copies and of CRS 5 (Pollen, `unpublisheddocum05poll`) for the letter's own wording is done at the snippet level; the open item is Boyd vol. 8 pp.211-212 -- LOCAL-QUEUE row L13 is the owner-side route; cost about USD 0.5 for a local-runner read.

## Next step (NO-CRACKS, 5 Oct 2026)

next: Boyd, CSP Scotland vol. 8 pp.211-212 read on the local runner (LOCAL-QUEUE row L13, HathiTrust miun.abe1726.0008.001), ~$0.5; then the TNA page copy of SP 53/16 no.79. Who acts: outside. Source: this file's "## While waiting" (LOCAL-QUEUE L13); written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.
