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
