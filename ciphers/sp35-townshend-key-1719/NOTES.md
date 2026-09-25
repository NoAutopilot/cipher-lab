open
A report from the Lords committees ... to examine Christopher Layer ... Together with the appendix (1723, archive.org bim_eighteenth-century_a-report-from-the-lords-_great-britain-parliamen_1723, 7086-line djvu.txt) read and grepped in full by this worker: control terms Kelly (14 hits), Plunket (13 hits) and period-spelling cypher (11 hits, incl. "the Ellis Cypher", "writ originally in Cypher") all hit, confirming the volume is genuinely on point and the search functions, but Townshend/Townsend get 0 hits anywhere in the report or its appendix.

## Check-solved (LANE CX2, 25 Sept 2026)

Re-sweep to close the intake-gate citation gap left by the 24 Sept 2026 sweep below (that sweep's line 2 was blank; `tools/intake_gate_check.py` exited 1). Re-clone of both solver repositories (25 Sept 2026, shallow depth 1) confirms the 24 Sept findings still hold; new work this round is items (b) and (a) below.

1. **Web search.** "SP 35/71 Townshend cipher key Atterbury plot solves Claude GPT" and "Papers relating to the Atterbury Plot" — no model-solve announcement (Vals AI, Schneier's coverage of Claude Fable 5.1's Cyphral Distich solve is a different, unrelated 1653 cipher), no source tying this shelfmark pair or the twelve singles to a printed edition or discussion beyond the TNA Discovery catalogue description itself (`discovery.nationalarchives.gov.uk/details/r/C14896200`, the same hierarchy note already quoted below).
2. **Print — read and grepped, not just searched by shelfmark.** Fetched and grepped, this worker, in full: *A report from the Lords committees ... to examine Christopher Layer ... Together with the appendix ... 1723* (archive.org `bim_eighteenth-century_a-report-from-the-lords-_great-britain-parliamen_1723`, djvu.txt, 7086 lines, 1 request, already on disk from the 24 Sept sweep but re-fetched and searched properly this round — the 24 Sept sweep grepped only "Townshend" and wrongly filed this as "the wrong volume... no shelfmark-linkable text" without checking whether the document was actually on-topic). Controls: "Kelly" 14 hits, "Plunket" 13 hits (both named in Cryptiana's H.34-H.37 items), period-spelling "cypher" 11 hits including "the Ellis Cypher" and "in order to being satisfied of [letters] decyphered by them two Months before" — this is a real, substantive, on-topic printed source about the Atterbury-Plot decipherments, not a mismatched volume. Target terms: "Townshend" 0 hits, "Townsend" 0 hits, anywhere in the 7086-line text. This is a genuine controlled full-text negative for the *Layer* report specifically (not yet the *Reports from Committees of the House of Commons* Vol. 1, 1803 reprint that Cryptiana's `atterbury.htm` cites by page for H.34-H.37 — that specific reprint volume was not obtained as a directly-readable OCR text this round either; see Edition risk below). Separately tried Google Books' own full-text-search API (`&country=US&key=$GOOGLE_BOOKS_KEY`) against several different Google-scanned copies titled "Reports from Committees of the House of Commons" (1803): results were inconsistent across scans (a control term like "Kelly"/"cypher" hit one scan id but "Rochester"/"Christopher Layer" hit a *different* scan id of the nominally same title, meaning at least one of the several Google-digitised copies under this generic title is not actually the Atterbury-Plot volume) — not used as evidence either way, abandoned in favour of the directly-grepped archive.org text above, which is unambiguous.
3. **Community lists.** Cryptiana `atterbury.htm` (cached from 24 Sept sweep, re-read): as before, covers B.Y.1/B.Y.10/C.50-52/F.11/H.34-37 by name, none of which the page ties to SP 35/71/61-62 or the twelve singles' shelfmarks. No dedicated Cipherbrain/Cipher Mysteries post found.
4. **DECODE.** Local snapshot (`sources/decode/*.tsv`) and the cached `unsolved-ciphers/catalogue/decode-catalog.csv` (fresh 25 Sept clone) grepped for "townshend", "sp 35", "sp35", "atterbury": no hit in either.
5. **Bourdeau.** Fresh shallow clone (25 Sept 2026, depth 1). Grep for "townshend|sp[ _]?35|atterbury" across the whole repo: one substantive hit, `oldest/scan_2026-09-23/hard_targets.md` line 124, "SP 35/46/59 'Undecyphered paper', c. 1723 (Atterbury plot)" — a different item, same as the 24 Sept finding, confirmed still the only SP 35 Atterbury item in his project. The other "Townshend" hit in this clone (`SOLVED_CATALOGUE.md`/`README.md`) is an unrelated nomenclator code-name ("170 Townshend") in the Visconti 1727 key, not this target.
6. **Aymeloglu.** Fresh shallow clone (25 Sept 2026): zero hits for "townshend", "sp 35", "sp35", "atterbury", "maclean", "sp 54", "sp54" anywhere in the repository (confirms both this target and sp54-maclean-1745 below).

Requests this round: archive.org 1 (djvu.txt re-fetch), googleapis.com/books 11 (Google Books full-text-search API, `&country=US&key=...`, abandoned as unreliable across scans — see item 2), github.com 2 (both solver repos, shallow clone, shared with sp54-maclean-1745), 2 WebSearch queries. No browser-tool use beyond one blocked attempt (Google's own books.google.com/books?...&q= search-in-book endpoint served a bot-challenge "sorry" page to the browser tool; not retried, abandoned per the one-retry rule).

## Original sweep, 24 September 2026

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
   no shelfmark-linkable text. (Corrected LANE CX2 25 Sept 2026: this is not "the wrong volume" in the sense of
   being off-topic — a LANE CX2 re-read confirmed with controls, below, that it is a real, substantive,
   on-topic printed source about these same Atterbury-Plot decipherments, and that "Townshend" is genuinely
   absent from its 7086 lines, not merely unsearched. What remains true and unresolved is that it is a
   different document from the specific *Reports from Committees of the House of Commons* Vol. 1, 1803 reprint
   that Cryptiana's `atterbury.htm` cites by page for H.34-H.37.) The actual Vol. 1, 1803 reprint appendix
   (or the original 1723 Commons committee
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

**Real, softened but not closed (updated LANE CX2 25 Sept 2026).** The same catalogued unit's SP 35/36/34-37
keys are already in print and on Cryptiana (found-solved, `ciphers/sp35-intercepts-1722/`). Cryptiana's
dedicated Atterbury page does not name SP 35/71/61-62 or the twelve singles, which is evidence but not proof
of absence (the printed appendix is organised by topic, not shelfmark). LANE CX2 25 Sept 2026 added a genuine
controlled full-text negative against the 1723 *Report from the Lords committees ... Together with the
appendix*, a real, on-topic, control-confirmed printed source discussing these same decipherments (Kelly,
Plunket, "the Ellis Cypher" all present) that does not mention Townshend anywhere. The specific *Reports from
Committees of the House of Commons* Vol. 1 (1803) reprint that Cryptiana cites by page for H.34-H.37 is still
not obtained as directly-readable OCR text (the only djvu-text archive.org copy found under that title,
`bub_gb_K1n4zoQRhSUC`, is the 1803 General Index, not the report text; several Google-Books-scanned copies
under the same generic title gave inconsistent full-text-search results, see the Check-solved section above,
and were not relied on). The twelve singles (SP 35/19, 31, 33, 37, 39, 45, 49, 50 x2, 53 x2, 56) have not been
individually checked against the 1723/1803 print at all, this sweep or the 24 Sept one.

## Verdict

**Open, stage 2 verified unsolved.** Not "new"; not "unpublished" (rule 10) — a search result, not a
discovery. Closed-negative on DECODE, Bourdeau (this specific pair; a neighbouring item, SP 35/46/59, is his)
and Aymeloglu, confirmed on a fresh 25 Sept 2026 clone of both. Line 2 above now cites a controlled full-text
search actually read by this worker (LANE CX2, 25 Sept 2026), so this verdict passes the intake gate
(`tools/intake_gate_check.py`) for the named item SP 35/71/61-62 specifically. Still open and unresolved: the
twelve singles individually, and the specific 1803 Vol. 1 reprint Cryptiana cites by page — both remain a
real, not merely conditional, gap; treat the odds of prior print for SP 35/71/61-62 as reduced but not zero,
and do not treat this verdict as covering the twelve singles' own print risk.

Requests (24 Sept sweep): cryptiana.web.fc2.com 1, archive.org 4 (Lords-report metadata + text,
Reports-from-Committees index metadata + text), github.com 2 (both solver repos, shallow clone, shared across
that session's four targets), 2 WebSearch queries. Requests (25 Sept LANE CX2 re-sweep): see the Check-solved
section above (archive.org 1, googleapis.com/books 11, github.com 2, 2 WebSearch, 1 blocked browser-tool
attempt).

## Next

Locate and read the actual 1723/1803 Commons-committee appendix (not the Lords' procedural report) by its
topic sections — the "papers relating to the Bishop of Rochester" and "foreign correspondence" sections are
the most likely home for an anonymous letter to Townshend — before any copy order. If the appendix does not
cover SP 35/71/61-62 or the twelve singles, TNA page-copy order is the next route (not digitised, per QUEUE
row N20; none of these fourteen items is known to be online as an image).
