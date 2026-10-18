- **Status:** found-solved -- no ciphertext at Haldimand Papers B.149 pp.286-288 (BL Add MS 21809, LAC reel H-1650 Images 304-306, read 18 Oct 2026); the cypher Brymner's entry mentions is an enclosure Paterson forwarded, most probably Carleton's re-sent 25 Sept 1782 cipher copies at B.148 p.123/pp.126-8, whose period decipherment (B.148 p.102) is already read at H in ciphers/pro3055-clinton-1779 (GAPS7); that link is grade I.
- **Brymner page read:** *Report on Canadian Archives* 1888 (archive.org `reportoncanadian1888publuoft`, full djvu text, B.149 section, about lines 10760-10850): "Paterson to Haldimand. Sends letter in cypher from Carleton, who has given orders to send to New York the clothing for the foreign troops." -- the two-column OCR reflow prints "Page 286" in front of "in cypher from Carleton"; on the page images 286 is the *preceding* Studholme entry and the Paterson letter is p.287.

# hald149-carleton-1783: Haldimand B.149 p.286 "in cypher from Carleton"

Worker HALD149 (account 4, 18 Oct 2026, 14:08-14:2x UTC by `date -u`), brief `.claude/briefs/runs/2026-10-18-acct4-research-director-22.md`.
Pool row: QUEUE.md "Haldimand-service cypher pool (18 Oct 2026)" rank 1; harvest/HALD-POOL-2026-10-18.tsv row 66.

## Check-solved and premise check (18 Oct 2026)

- Repository: no folder, NOTES.md, AUDIT.md or print check names B.149 / Add MS 21809 / H-1650 (grep of every *.md, *.tsv, *.json,
  *.py except ROOM.md); pro3055-clinton-1779's scope is B.147/B.148 = Add MS 21807/21808 on H-1649.
- Tomokiyo, `sources/cryptiana/web/haldimand.htm`: scoped to 21807/21808; lists Carleton cipher letters of 1782 (f.31A, f.49,
  f.65A, f.93, f.123) in B.148, none in 21809.
- Solver repositories and DECODE: local snapshots under sources/cyphersolver, sources/bourdeau, sources/decode have no "Haldimand"
  hit (only sources/solver-diffs/2026-09-23-non-decode-hits.tsv, an earlier scout list). Aymeloglu's repository not cloned (the job
  ended before a key test was possible; see below).
- Print: Brymner 1888 B.149 calendar (above) read in full text; Brymner 1887 B.148 calendar (`reportoncanadian1887publuoft` djvu)
  read for Oct 1782-Feb 1783: the only Carleton cipher item in that window is "Carleton to Haldimand. Copies of letters in cypher.
  123" (26 Oct 1782), and Haldimand's reply calendared at p.132 says he "has received his (Carleton's) letters by way of Halifax".

## Web and blog check

18 Oct 2026, two web searches ("Paterson Haldimand Halifax November 1782 cypher Carleton Jason"; "Haldimand Carleton cipher 1782
cipherbrain OR cryptiana Halifax enclosure"): only TNA PRO 30/55 catalogue items (Paterson to Carleton 22 Nov 1782, item 6236;
Carleton to Haldimand 12 Nov 1782, item 6142) and BL catalogue rows for Add MS 21806/21808/21809; no Cipherbrain, Cryptiana-blog or
forum post on this letter and no published decipherment of a B.149 item. A search result, not a novelty verdict (rule 10).

## The pages (LAC reel H-1650, heritage.canadiana.ca `oocihm.lac_reel_h1650`, 1367 images)

Route as pro3055 (viewer page lists IIIF ids, saved to `images/h1650_seq.tsv`; image-uab.canadiana.ca with browser UA + Referer).
H-1650 begins with B.149 = Add MS 21809 (LAC label strip "Letters from Governors of Nova Scotia and Officers Commanding at Halifax
etc., n.d., 1777-1784, MG 21, Add. Mss. 21809, (B-149)"), and B.150 = 21810 is already running at Image 400 (p.35).
Probes at 1000 px: Image 120 = p.107, 260 = p.244 (Fort Howe 3 May 1782), so about 0.98 pages per image; then Images 302-306:

| Image | page | BL fo. | letter | cipher? |
|---|---|---|---|---|
| 302 | 284 | 276 | Studholme to Mathews, Fort Howe 13 Oct 1782 | no |
| 303 | 285 | 278 | Connor to Mathews, Fort Hughes 18 Oct 1782 (Higginbottom carrying dispatches from Carleton) | no |
| 304 | 286 | 280 | Studholme to Mathews, Fort Howe 3 Nov 1782 (newspapers; Gibraltar; Lord Howe's fleet) | no |
| 305 | 287 | 282 | **Paterson to Haldimand, Halifax 11 Nov 1782**: "I have the honor to enclose Your Excellency a letter in Cypher from His Excellency Sir Guy Carleton, received this day by His Majesty's Ship Jason. Sir Guy has further directed me to send all the Clothing for the Foreign Troops to New York, except what may be wanted for those who are to remain here, and at Penobscot." Endorsed "Recd by Mercure the 10th Jany 83". ff.282v endorsement only | no (covering letter) |
| 306 | 288 | 283 | Studholme to Mathews, Fort Howe 20 Nov 1782 | no |

Committed at 1000 px: `images/h1650_304.jpg`, `h1650_305.jpg`, `h1650_306.jpg`. Read by eye on two montages (vision 2 + one crop =
3 image reads). Paterson's text above is the worker's reading of a 1000-px frame (grade H for the sense; spelling not collated).

**Corrections to the pool row.** (1) Date: November 1782, not 1783-84. (2) "Page 286" is Brymner's page number for the preceding
entry; the Paterson letter is p.287. (3) There is no cipher on B.149 pp.284-288: the cypher was an enclosure, not bound with the
covering letter in 21809.

## Where the enclosure is (grade I)

Carleton's cipher reached Halifax on HMS Jason on 11 Nov 1782 and Haldimand on 10 Jan 1783. The B.148 calendar's only Carleton
cipher item between 25 Sept 1782 and Feb 1783 is p.123 (26 Oct 1782, "Copies of letters in cypher"), which pro3055 GAPS6/GAPS7
identified as copies of Carleton's 25 Sept 1782 cipher letter (another copy pp.126-8; period decipherment p.102, read at H, 218
words; cells match the 1778 title-page key 19/19 against a shuffled-plaintext control mean 1.25, p95 3). Haldimand's p.132 reply
acknowledges Carleton's letters "by way of Halifax". So Paterson's enclosure is most probably the p.123 or pp.126-8 copy -- a
dated-route inference, not a matched endorsement (grade I).

## Key test

Not run: the page carries no ciphertext, so neither the 1778 title-page key nor the Entick page.column.line code had anything to
be applied to, and no control was built. This is not a negative about either key.

## Remaining gaps

- The I-grade link above could be raised to H by reading the endorsements on B.148 pp.124/128 (H-1649, Images ~1206/~1210; 1206 is
  already in pro3055's images) for "via Halifax" / "by the Jason" / "Recd 10 Jan 1783"; owned by pro3055-clinton-1779, ~USD 1.

## While waiting

Nothing here is waiting; the pool's rank 2 (1884 report, Add MS 21704/21715/21720 cypher duplicates) is the next fresh item.

## Six questions (research director)

1. Learned: the pool's rank-1 "cypher" entry is a covering letter; the cipher was an enclosure filed in B.148.
2. Assumed: that Brymner's "Page N" precedes its own entry (false under two-column reflow) -- the pool's page numbers need image checks.
3. Unverified: which B.148 copy Paterson enclosed (endorsement not read).
4. Alternative: the enclosure is lost or filed elsewhere (B.146 p.54 holds a further copy per the B.148 p.123 pencil note).
5. Most informative next: read the pp.124/128 endorsements; for the pool, check every "in cypher" row's page against its neighbour before fetching.
6. Pivot: rank 1 is consumed; move to rank 2 after locating its reel.

Requests: heritage.canadiana.ca 1 (viewer page), image-uab.canadiana.ca 11 (Images 2, 120, 260, 400, 540, 680, 302-306 at 1000 px),
archive.org 2 (Brymner 1888 and 1887 djvu text), each 1.6 s apart.
