# TNA page-copy batch order — six undigitised cipher items

**Status:** backlog (ASKS.md row 73). Not sent. No personal data, no payment details, per CLAUDE.md rule 9.

**Why one order:** six targets from `NEXT-STEPS.tsv`'s needs-image list each already have their own single-item
`REQUEST.md` naming an undigitised The National Archives (TNA) piece, confirmed by TNA Discovery
(`digitised: false` where checked). CLAUDE.md's NX-UNBLOCK brief (26 Sept 2026) asks for these consolidated
into one order rather than six separate ones, since TNA charges a flat £9.92 page-check fee per record
regardless of order size and a single submission is less to track.

**Prices, from TNA's own current fee page** (`nationalarchives.gov.uk/help-with-your-research/record-copying/fees/`,
read 26 Sept 2026 19:01 UTC): Page Check £9.92 per record; Digital copy, up to and including A3, research
quality, £1.52 per copy; Digital copy, greater than A3, £11.95 per copy. A page check is TNA's own prerequisite
step for an undigitised item — it fixes the final page count and the per-page price before the copy order is
placed, and TNA's page states a completed page check is valid six weeks and not normally refunded if the
resulting order can't be fulfilled.

## Items (12 records across 6 pieces, stage 1 only)

| # | Piece/item | Folio(s) | What it is | Target folder | Est. images |
|---|---|---|---|---|---|
| 1 | PRO 30/24/7/505 | — | Shaftesbury to Percivall, Perkins, Fisher, in cipher, 6 June 1682 | pro30-shaftesbury-1682 | 2 |
| 2 | SP 77/32/289 | f.289 | Nicholas to Sir L.R. at St Sebastian, in cipher, 6/16 Aug 1659 | sp77-nicholas-1659 | 2 |
| 3 | SP 78/83/62 | f.147 | Louis XIII to Cesy, partly in cipher, 31 Aug/10 Sept 1628 | sp78-cesy-1628 | 2 |
| 4 | SP 78/69/91 | f.214 | Doncaster to Calvert, in cipher (target letter), 24 Sept 1621 | sp78-doncaster-1621 | 2 |
| 5 | SP 78/69 | f.222 | The cipher enclosure to f.214 ("advertisement in cipher") | sp78-doncaster-1621 | 2 |
| 6 | SP 78/69/56 | f.142 | Directions for the letters sent by Doncaster to France, July 1621 | sp78-doncaster-1621 | 2 |
| 7 | SP 78/69/58 | f.144 | "French titles for the cipher" — candidate key | sp78-doncaster-1621 | 2 |
| 8 | SP 78/69/59 | f.146 | List of French letters for Doncaster, July 1621 | sp78-doncaster-1621 | 2 |
| 9 | SP 78/232/44 | f.103 | Yorke to Bedford, "partly in cipher," 8/20 Mar 1749 | sp78-yorke-1749 | 2 |
| 10 | SP 91/5/108 (C6719621) | — | Whitworth to Harley, 30 Jul/10 Aug 1707, "partly undeciphered" — the target | whitworth-1707 | ~4 |
| 11 | SP 91/5/106 (C6719620) | — | Whitworth to Harley, 23 Jul/3 Aug 1707, deciphered — key source | whitworth-1707 | ~2 |
| 12 | SP 91/5/121 (C6719626) | — | Whitworth to Harley, 16/21 Sept 1707, deciphered — second key source | whitworth-1707 | ~4 |

Row counts: pro30 1 item, sp77 1 item, sp78-cesy 1 item, sp78-doncaster 5 items, sp78-yorke 1 item,
whitworth 3 items (its own REQUEST.md's optional second stage, SP 91/5/294 and /298, is left out of this
batch — order it separately later only if the 1707 key doesn't come through). Total: 12 items, about 28
images at the estimate column above (rough, since none of these have had a page check yet; the real count and
therefore the real digital-copy total come back with the page check).

## Estimated cost

- Page check: 12 records × £9.92 = **£119.04**
- Digital copies (all estimated ≤A3, no oversize pages expected in ordinary letter-sized state papers):
  28 images × £1.52 = **£42.56**
- **Rough total: about £161.60**, before the page checks return the real page counts (could be lower if
  several folios are single-sided single images, or higher if any folio needs more than 2 images).

## One-sentence ask

Please submit one TNA record-copying order (page check first, then digital copies once the counts come back)
for the 12 items listed above, using each item's own TNA Discovery reference; page copies only, digital,
research quality, no oversize.

## Order via

The National Archives' own paid copying service: each Discovery record page ("Order a copy" / "Record
copying"), or the general record-copying request route at
`nationalarchives.gov.uk/help-with-your-research/record-copying/`. Each item is its own Discovery record, so
each goes into the basket separately (per the existing per-item `REQUEST.md` files, which have the full
catalogue descriptions and reasoning for each item and are the fuller reference if any one item is ordered on
its own instead).

## Log

| Date | Action | Result |
|---|---|---|
| 26 Sept 2026 | NX-UNBLOCK: fetched TNA's current fee page, checked TNA Discovery API reachability (500 response on `sps.searchQuery`, not re-tried per the good-citizen single-retry rule — digitisation status for these six items stands as last confirmed in each item's own REQUEST.md/NOTES.md) | Batch order drafted, ASKS row 73 filed at `backlog` |
