Status: found-solved
Verifier KHF-1 verifier, 7 Oct 2026 (AUDIT.md): **N0**, key `published`, text known, depth D3 (about 85%). The passage was deciphered and printed by Irving Brant, *James Madison: Secretary of State, 1800-1809* (1953), at his chapter note 12: "Monroe received from George Erving in cipher and placed in his papers without an interlining. Deciphered a century and a half later, it reads: 'It is said that Randolph asked when Mr. Monroe would return home. The President answered, not until his successor arrives. The other bluntly observed that he, Mr. Monroe, would be the next President.'" Our reading is an independent re-decipherment that agrees with it word for word. The check-solved verdict `open` below was wrong (AUDIT.md section 4); the line that follows is the check-solved worker's, kept as written.
1904 LOC *Papers of James Monroe* calendar (IA cu31924029594037) p.39 and the 1891 Dept of State *Calendar of the Correspondence of James Monroe* (IA cu31924032751665) p.70 read by this worker (both list the letter, the 1891 one says "Remarks about Randolph in cipher", neither prints or deciphers it); Preston, *Papers of James Monroe* vol. 5 (2014) table of contents (1806 section, every entry) read by this worker, letter absent; Hamilton, *Writings of James Monroe* vol. IV (IA writingsjamesmo03monrgoog) full-text grep for Erving/Lisbon/successor, letter absent.

# George W. Erving to James Monroe, Lisbon 23 May 1806 -- coded passage in WE028

Check-solved verdict `open`, premise check clean and intake gate exit 0 (KHF-1, 7 Oct 2026; sections at the end). Found 7 Oct 2026 by KH4-D (LANE KH-4, account 4, KEYHUNT row 68, key `tools/data/uscodes-1800/WE028.tsv`).

## Source (image over transcription: read from the image)
- Library of Congress, James Monroe Papers (mss33217), Series 1, reel 3 (item mss33217003), frames 0828-0830:
  `https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0800:0828` (p.1, headed "Lisbon 23 May 1806"),
  `...:0829` (pp.2-3; signed "George W Erving"; coded lines 1-5 of the right page), `...:0830` (not looked at beyond the
  contact sheet). Native 4234x2824 for frame 0829.
- 1904 LOC *Calendar of the Papers of James Monroe* (IA cu31924029594037, OCR line "23. George William Erving to Monroe."
  under May 1806) lists it; the calendar does not flag cipher.
- Context (from the clear text, read by this worker at pct:30, not transcribed): Erving had embarked at Falmouth on the
  13th and reached Lisbon on the 21st; news from the United States to 3 April; the Randolph schism; the Massachusetts
  election (Sullivan, Strong, district of Maine).

## Ciphertext and reading
`ciphertext.txt` (34 groups, five lines), two blind Sonnet passes on the line crops in `images/` (`tools/iiif_lines.py`
command below), `passA.tsv`/`passB.tsv`, agreement 33/33 on the groups both read (`tools/reconcile_passes.py`,
`agreement.tsv`). `decode.py [--check]` (rule 7) writes `reading.txt` and `reading_letters.txt`. Grades (regraded by KHF-1,
7 Oct 2026, see "## Grading" at the end): **H 29, C 0, S 0, M 4, I 1 of 34** (KH4-D's first grading was S 29 M 4 I 1).

Clear words in the manuscript between the runs are given in brackets; the decoded groups are in capitals:
> [Randolph asked] WHEN MISTER MONROE WOULD RETURN HOME -- THE PRESIDENT [answered] NOT UNTIL HIS SUCCESSOR ARRIVES.
> [the other bluntly observed that he] MISTER MON[ROE] WOULD BE THE NEXT PRESIDENT.

(L04's middle group is overwritten in the manuscript with "137" interlined; read 1379 = ter, grade I. Its last group 146
is at the crop edge, grade M. L05 runs on from L04: "mon | ro E would be ...".) The left page of frame 0829 carries two more
groups in running text, "a conversation of Randolph with 78" with "1385" interlined above (= "with the president", M, one
reader) -- not transcribed by the passes, not counted.

Crop command (pasted, Usage 6):
`python3 tools/iiif_lines.py 'https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0800:0829' --out <scratch>/crop --region 2120,80,2060,580 --prefix f829 --debug`
-> 6 lines, pitch 97; L01-L05 used.

## Matched control (rule 3) and judge (rule 7)
`control.py` (output `control.json`): the same 34 groups under 200 shuffled WE028 keys (plaintext values permuted over the
1600 codes). A shuffled key changes both statistics, so the control can fail differently from the target.
- en18 4-gram score: **real -0.723 vs shuffle mean -1.296, p95 -1.087, max -0.971** (0 of 200 reach the real score).
- greedy word cover: real 0.971 vs shuffle mean 0.865, p95 0.941, max 0.972 -- this statistic barely separates at 105
  letters (1 of 200 shuffles reaches it); reported, not relied on.

`python3 tools/judge_plaintext.py specs/erving-monroe-1806.json --file ciphers/erving-monroe-1806/reading_letters.txt`:
```
ok   length: got=105, min=50, max=400
ok   language: score=-0.723, null_p99=-1.986, real_p05=-0.877, real_median=-0.738, mode=both, N=105
PASS - erving-monroe-1806 (a PASS is a gate for a verifier, not a reading; rule 10)
```
en18's fold spread was measured at N=1000/1500, not at 105 letters: a PASS of unknown reliability at this length (rule 3);
the shuffled-key control above is the stronger evidence.

## What was searched (7 Oct 2026) and where it was not found -- not a check-solved verdict
- Founders Online (headless Chromium): the Madison Papers print the WE028 passages of Erving's and Monroe's letters **to
  Madison** decoded by the editors; this letter is to Monroe and is not in the Madison Papers. Not searched: Founders for
  this letter's date by name (it would only appear in a Monroe edition).
- `sources/cryptiana/web/state.htm` (Tomokiyo's WE028 page): lists Madison-Monroe letters only; no Erving-Monroe item.
- `sources/cyphersolver/`, `sources/decode/`, `sources/solver-diffs/`: no Erving item (grep "erving").
- Not reached by KH4-D (covered by KHF-1's check-solved below, table of contents read): *The Papers of James Monroe* vol. 5 (Preston, 2014; Google Books NO_PAGES and Rotunda subscription per
  armstrong-madison-1808 ARM-KEYHUNT-2) -- the edition most likely to print or calendar this letter; Aymeloglu's
  repository (not cloned here); a phrase search. These are check-solved's job.
- Related known item: Erving to Monroe, Madrid 5 Feb 1806 (reel 3 frames 740-744, WE028 with a period interlinear
  decode), read in ciphers/armstrong-madison-1808 H25/H29 -- the same channel; not this letter.

Report what was found and where it was not found; novelty is a verifier's call (rule 10).
Verifier, 7 Oct 2026: N0 -- Brant (1953) printed this passage's decipherment; see AUDIT.md.

## Check-solved (KHF-1, 7 Oct 2026)
Verdict: **open** (KHF-1, account 1, 20:42-21:0x UTC by date -u). **Overturned by the verifier, 7 Oct 2026: printed decipherment in Brant 1953, see AUDIT.md -- `found-solved`.** Edition by edition:
- **1904 LOC calendar** (*Papers of James Monroe, listed in chronological order*, IA cu31924029594037, `_djvu.txt`, whole
  volume grepped for "Erving" -- 40 hits -- and every 1806 heading): p.39, May 1806, "23. George William Erving to Monroe."
  No summary, no cipher flag.
- **1891 Dept of State calendar** (*Calendar of the Correspondence of James Monroe*, Bureau of Rolls and Library Bulletin 2,
  IA cu31924032751665, whole volume grepped for "Lisbon", "1806, May" and "cipher"): p.70, Erving, George W.: "1806, May 23.
  Announces his arrival in Lisbon. News from United States. Yrujo left Washington after his insolent letter to Madison.
  Miranda's expedition. Sullivan to be governor of Massachusetts. Randolph's dissatisfaction causes a schism in the
  administration which may enable the appointment of Mr. King. Remarks about Randolph in cipher. Recommends Mr. Bankhead as
  consul to St. Andre. 4deg. 4 pages." -- the calendar **flags the cipher and does not read it**. (Found through a Google Books
  API hit, id 1IGQp018n7YC, full view; read from the IA copy.)
- **Preston, ed., *The Papers of James Monroe* vol. 5, Selected Correspondence and Papers, Jan 1803-Apr 1811** (ABC-CLIO 2014):
  the volume's own table of contents, published by the Papers of James Monroe project at
  academics.umw.edu/jamesmonroepapers/publications/publishedcorrespondence/volume-5-table-of-contents/ (fetched with
  tools/browser_fetch.js; curl 403), 1806 section read entry by entry: Monroe's letters to/from Madison, Jefferson,
  Nicholson, Skipwith, Wirt, Randolph (16 June), Vincent ... -- **no Erving item in 1806**; the volume's only Erving item is
  "From George Erving, 5 November" 1803. Not checked: the volume's annotation (a footnote to "To John Randolph, 16 June" 1806
  could cite this letter); Google Books id VhPHEAAAQBAJ is PARTIAL but its search-inside page answered a captcha redirect
  (one attempt, stopped), the 2003-dated record d_vCEAAAQBAJ is NO_PAGES, not on IA, not in HathiTrust (record 005232597
  carries v.1-3 only). The project's full catalogue of correspondence (summaries) is login-gated; not searched.
- **Hamilton, ed., *Writings of James Monroe* vol. IV, 1803-1806** (IA writingsjamesmo03monrgoog, "VOLUME IV" checked):
  prints Monroe's own letters only; whole-volume grep for Erving (49 hits), Lisbon, "successor", "May 23": no Erving letter
  of 23 May 1806, no quotation of its cipher passage.
- **PJM-SS (Founders Online, Madison Papers)**: search Lisbon + Author "Erving, George W." (25 hits): Erving to Madison 17 Apr
  1806 (London, planning the Lisbon route), then 17 June 1806 (Madrid) -- no Erving letter to Madison from Lisbon in May 1806,
  so no sibling copy of this passage on the Madison side. Founders carries no Monroe edition.
- **LOC Monroe reels 3-4**: the item itself (reel 3 frames 0828-0830) viewed; neighbours under Premise check below.
- **DECODE**: `sources/decode/` (listing dumps, keys-all 28 Sept, h18/h20) grep "Monroe", "Erving": none.
- **Bourdeau** (github.com/dbourdeau/cyphersolver, shallow clone at its 7 Oct 2026 09:05 commit, grep -w Erving/mss33217/
  WE028/Lisbon): only Erving -> Madison, Madrid 24 Mar 1807 (targets/erving1807) and its README row naming Erving -> Madison
  10 Aug 1807 as the next step; nothing for Erving -> Monroe or 1806. Not a stated next step for this letter.
- **Aymeloglu** (github.com/aaymeloglu/unsolved-ciphers, shallow clone at its 27 Sept 2026 commit, same grep): no hit.
- Tomokiyo's WE028 page (`sources/cryptiana/web/state.htm`): Madison-Monroe letters only (KH4-D, re-confirmed by grep).

## Web and blog check (KHF-1, 7 Oct 2026)
Queries (WebSearch, standard) and what came back:
1. `Erving to Monroe Lisbon "23 May 1806"` -- Founders Madison abstracts (Erving to Madison 17 Apr 1806, 21 Jan 1806), W&M
   Swem dspace Erving-Monroe items of 1804-05; nothing for this letter.
2. `"Erving" Monroe 1806 Lisbon cipher Randolph "next President"` -- Founders (Erving to Madison 22 June 1807 on "Mr Monroes
   Cypher"), RR Auction lot (a 1807 Madison letter), W&M Jay Johns collection, UMW publishedcorrespondence page; no reading.
3. `"Papers of James Monroe" volume 5 1806 Erving Lisbon letter` -- Founders, Swem dspace, Mass. Hist. slip file; nothing.
4. `"George W. Erving" "James Monroe" 1806 cipher decoded` -- Founders (editors' decodes of Erving/Monroe letters *to
   Madison*), DPLA (Monroe to Washington 1796); nothing for this letter.
5. `"Monroe Papers" mss33217 reel 3 Erving 1806 cipher` -- loc.gov reel pages, NYPL Monroe papers; nothing.
6. Model-solve check: `Erving Monroe 1806 cipher letter solves Claude OR GPT decoded` -- only the Marmont 1809 / Cryptiana
   item (a different letter); nothing for this one.
Blogs by name: `site:scienceblogs.de/klausis-krypto-kolumne Erving Monroe cipher` (**Cipherbrain**: index pages only, no
Erving post); `site:cryptiana.blogspot.com Erving Monroe` (**Cryptiana blog**: no result from the blog) plus Tomokiyo's WE028
page on disk (above); `site:ciphermysteries.com Erving Monroe cipher 1806` (**Cipher Mysteries**: no result from the site).
No comment thread to read: no hit on any of the three blogs touched this letter.
Google Books API (`country=US`, keyed): `"Monroe would be the next President"` and `"until his successor arrives" Monroe`
-- no result; `"Erving" "Lisbon" "23 May 1806"` -- the 1891 calendar (above) and Weber, *United States Diplomatic Codes and
Ciphers* (WE028 background, not this letter). [Verifier correction, 7 Oct 2026: Weber's note cites **this very letter** -- "Erving to Monroe, Madrid, February 5, 1806 and Lisbon, May 23, 1806, in JMP, R 3" -- as a use of the code; and the query "Monroe would be the next President" returns seven hits when re-run, two of them Brant's printed decipherment. See AUDIT.md.]

## Premise check (KHF-1, 7 Oct 2026)
- (a) Folder's own mentions: the only gloss-like marks are two **code numbers interlined by the writer** -- "1385" above "78"
  on the left page of frame 0829 (a code group, not a decipherment) and "137" over L04's second group. Viewed on frame 0829
  (1800 px) and the native line crops: no plaintext written over or under any of the five coded lines. **Not found.**
- (b) Other solvers' working files: Bourdeau's erving1807 (Erving to Madison 1807, Pinckney's legation code) and Aymeloglu's
  repo: no file for this letter, no run of a WE028 key on it. **Not found.**
- (c) Physical neighbours, LOC reel 3, all at 1800 px: 0828 (p.1 of this letter, clear), 0829 (pp.2-3, coded lines on the
  right page, no gloss), 0830 (p.4: P.S. continued, signature initials, docket "23 May 1806 ... Erving"; nothing else on the
  page but bleed-through), 0831 (a separate item headed "[1806 May 28]", notes "America"/Spain, calendar's "Monroe. Notes
  respecting Spain and Great Britain"), 0827 fetched. No decipherment, clear copy or slip bound beside it. **Not found.**
- (d) Recipient side: Monroe is the recipient; his editions (1904 and 1891 calendars, Preston vol. 5 TOC, Writings vol. IV)
  above; the Department side (PJM-SS / Founders, Madison) has no Erving letter from Lisbon in May 1806. **Not found.**

## Grading (KHF-1, 7 Oct 2026)
`decode.py` regenerates `reading.txt` (`--check` current). Per token: **H 29, M 4, I 1 of 34** (C 0, S 0).
- H: both blind passes agree on the group and its value is read straight from WE028. WE028 is a key source: Tomokiyo's
  transcription of the period Monroe-Madison table, graded H in `tools/data/uscodes-1800/README.md`, and the same table is
  attested on this very channel by the period interlinear decipherment on Erving to Monroe, Madrid 5 Feb 1806 (reel 3 frames
  740-744; 12 values agree, ciphers/armstrong-madison-1808 H25/H29). No cryptanalysis is involved, so KH4-D's S grade was
  under-stated; the shuffled-key control (`control.json`) stays as evidence that the key is the right one for this letter.
- M: 401 (N), 680 (ar), 651 (X) -- one pass marked the group doubtful; 146 (mon) on L04 -- at the crop edge.
- I: L04's overwritten second group, read 1379 (ter) from "137" interlined.
- Not counted: the left page's "with 78" with "1385" interlined (= "with the president"), read by one eye only.
Key source for AUDIT.md: `published` (Tomokiyo's modern transcription of the period table, credited).
Judge, re-run after regrading (letters unchanged):
```
ok   length: got=105, min=50, max=400
ok   language: score=-0.723, null_p99=-1.986, real_p05=-0.877, real_median=-0.738, mode=both, N=105
PASS - erving-monroe-1806 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Next: a separate verifier session (rule 10, N-class and depth, AUDIT.md).
