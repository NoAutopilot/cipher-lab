open

# Anonymous letter to Lord Townshend enclosing a cipher key, and 12 further SP 35 singles — Atterbury-Plot series (1719-1725)

QUEUE row: N20 (`QUEUE.md`, "Candidates not on DECODE").

## Source

TNA, Secretaries of State: State Papers Domestic, George I, catalogue text as quoted in QUEUE.md's N20 row
(TNA Discovery, not independently re-fetched this sweep per the LANE S brief, which holds no Discovery slot
for this batch):

> **SP 35/71/61**: anonymous letter to Townshend "enclosing cipher key". **SP 35/71/62**: that key itself.

Plus 12 further SP 35 domestic intercepts from the same 1719-1725 Jacobite-correspondence sweep, none
individually noting a key or decipherment: SP 35/19, 31, 33, 37, 39, 45, 49, 50 (x2), 53 (x2), 56.

TNA's own hierarchy note (quoted in the QUEUE row) ties SP 35/71/61-62 to "Papers relating to the Atterbury
Plot (SP 35/35-39 and SP 35/71-72)" — the same catalogued unit as `ciphers/sp35-intercepts-1722/` (QUEUE row
N2, SP 35/36/34-37), which that folder's check-solved sweep (23 Sept 2026) found **found-solved**: the key
material for that cluster (Cryptiana's "H.34-H.37") was printed as Appendix H of the 1723 House of Commons
committee report on the Atterbury Plot, reprinted in *Reports from Committees of the House of Commons*, Vol.
1 (1803), and is transcribed, imaged and analysed on Cryptiana (`cryptiana.web.fc2.com/code/atterbury.htm`).
N20's own "Next" note (QUEUE.md) already flagged "high prior odds it is already printed, per N2's finding" —
this sweep tests that inference against SP 35/71/61-62 and the twelve singles specifically, rather than
assuming it.

## Check-solved sweep, 24 September 2026

1. **Print — the decisive question, only partly resolved.** Fetched Cryptiana's `atterbury.htm` live
   (1 request, WebFetch): the page's own text states it covers appendix letters/items **B.Y.1, B.Y.10, C.50,
   C.51, C.52, F.11, H.34, H.35, H.36, H.37** from the 1723/1803 printed report, with page images and analysis
   for each — but **it does not name or cite SP 35/71/61, SP 35/71/62, or any of the twelve singles (SP
   35/19, 31, 33, 37, 39, 45, 49, 50, 53, 56) anywhere on the page.** This is a genuine gap, not a confirmed
   negative: Tomokiyo's page may simply not have reached this item, or the printed appendix may cover it
   under a lettering this sweep did not identify (the appendix's sections run alphabetically by *topic*, not
   by shelfmark — e.g. "papers relating to the Bishop of Rochester", "papers relating to George Kelly" — so a
   plain shelfmark search cannot confirm absence from the print).
2. Fetched the archive.org text of *A report from the Lords committees ... to examine Christopher Layer ...
   Together with the appendix* (1723; identifier
   `bim_eighteenth-century_a-report-from-the-lords-_great-britain-parliamen_1723`, 152 KB djvu text, 2
   requests: metadata + text). This is the Lords' own procedural report (narrative discussion of the
   decipherers' testimony, the "Ellis Cipher", numeric aliases for Kelly/Plunket/etc.), **not** the Commons
   committee's document appendix that Cryptiana cites by letter — it contains no occurrence of "Townshend" and
   no shelfmark-linkable text. It is the wrong volume for confirming or excluding SP 35/71/61-62; the actual
   appendix (via Vol. 1 of the 1803 *Reports from Committees* reprint, or the original 1723 Commons committee
   report with its lettered appendix) was not located and read this sweep — a different archive.org item
   (`bub_gb_K1n4zoQRhSUC`, "Reports from Committees ... 1715-1801") that matches the title was fetched (1
   request) and found to be only the 1803 *General Index* volume, not the report text itself.
3. **Web search.** "anonymous letter Townshend cipher key Jacobite SP 35/71" and variants: no source ties
   this specific shelfmark pair to a named printed edition or a modern discussion. General Jacobite-cipher
   background only (Corbière as decipherer 1719-43, NLS's "Secret Codes" 1715-rising page, an unrelated 1724
   Brougham-archive cipher).
4. **Community lists.** Cryptiana: see (1). Cipherbrain, Cipher Mysteries: no dedicated post found by web
   search.
5. **DECODE.** Cached catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`, from the Aymeloglu clone)
   grepped for "SP 35", "Townshend", "Atterbury": no record.
6. **Bourdeau.** Fresh shallow clone (`dbourdeau/cyphersolver`, depth 1, 24 Sept 2026) grepped for "Townshend",
   "SP 35", "SP35": one hit, `oldest/scan_2026-09-23/hard_targets.md` line 123, naming **SP 35/46/59**
   "Undecyphered paper", c. 1723 (Atterbury plot) — a different piece and item from this row's SP 35/71/61-62
   and the twelve singles, confirming Bourdeau's project is independently working SP 35 Atterbury material but
   has not (in this clone) named this row's specific items.
7. **Aymeloglu.** Same clone pass (`aaymeloglu/unsolved-ciphers`, commit as cloned 24 Sept 2026): no hit for
   "Townshend", "SP 35" or "SP35" anywhere in the repository's markdown.

## Edition risk

**Real, not resolved.** The same catalogued unit's SP 35/36/34-37 keys are already in print and on Cryptiana
(found-solved, `ciphers/sp35-intercepts-1722/`). Cryptiana's dedicated Atterbury page does not name SP
35/71/61-62 or the twelve singles, which is evidence but not proof of absence, since the printed appendix is
organised by topic, not shelfmark, and this sweep did not obtain and read that appendix directly (only the
Lords' procedural report, a different document). The twelve singles (SP 35/19, 31, 33, 37, 39, 45, 49, 50 x2,
53 x2, 56) have not been individually checked against the 1723/1803 print at all this sweep.

## Verdict

**Open, stage 2 verified unsolved (conditional).** Not "new"; not "unpublished" (rule 10) — a search result,
not a discovery. Closed-negative on DECODE, Bourdeau (this specific pair; a neighbouring item is his), and
Aymeloglu. The print check is incomplete: the actual 1723 Commons committee appendix (not the Lords' report,
and not the 1803 index-only volume fetched this sweep) still needs to be obtained and checked by topic-section
for "Townshend", "cipher key", and each of the twelve singles' correspondents before this can move past
conditional. Given N2's precedent, treat the odds of prior print as elevated, not resolved.

Requests: cryptiana.web.fc2.com 1, archive.org 4 (Lords-report metadata + text, Reports-from-Committees index
metadata + text), github.com 2 (both solver repos, shallow clone, shared across this session's four targets).
2 WebSearch queries this target.

## Next

Locate and read the actual 1723/1803 Commons-committee appendix (not the Lords' procedural report) by its
topic sections — the "papers relating to the Bishop of Rochester" and "foreign correspondence" sections are
the most likely home for an anonymous letter to Townshend — before any copy order. If the appendix does not
cover SP 35/71/61-62 or the twelve singles, TNA page-copy order is the next route (not digitised, per QUEUE
row N20; none of these fourteen items is known to be online as an image).
