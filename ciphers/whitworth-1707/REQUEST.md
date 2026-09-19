# Copy request: The National Archives, SP 91/5, Whitworth's despatches of 1707-08

**The plaintext is already in print.** Sbornik of the Imperial Russian Historical Society vol. 39 (1884) prints
the letter of 30 July/10 Aug 1707 (SP 91/5/108) on pp. 407-411 with one gap marked "(undeciphered)" on p. 410,
and vol. 50 (1886) prints both letters of 22 Sept/3 Oct 1708 (ff. 274 and 294, of which ff. 300 and 298 are the
enciphered duplicates) in full. The private letter of 10/21 March 1708 (f. 163) has its office decipher at
f. 180 and is printed in vol. 39 pp. 470-477. So this order is for the cipher pages only, to recover the key
and read the one unread clause in f. 108. See `NOTES.md` for the checks.

## Before sending

1. Piece identified on Discovery, 19 Sept 2026: **SP 91/5**, State Papers Foreign, Russia, 1707-1708, record
   C3426306, https://discovery.nationalarchives.gov.uk/details/r/C3426306. Not digitised. Items are catalogued
   by folio, so each can be ordered by its own record:
   - **SP 91/5/108**, Whitworth to Harley, Moscow 30 July/10 Aug 1707, "Partly undeciphered":
     https://discovery.nationalarchives.gov.uk/details/r/C6719621. The target.
   - **SP 91/5/106**, Whitworth to Harley, Moscow 23 July/3 Aug 1707, "Partly in cipher" (deciphered):
     https://discovery.nationalarchives.gov.uk/details/r/C6719620. Key source, the letter of the previous
     post.
   - **SP 91/5/121**, Whitworth to Harley, Moscow 16/21 Sept 1707, "Partly in cipher" (deciphered):
     https://discovery.nationalarchives.gov.uk/details/r/C6719626. Second key source, in case the cipher
     passages of f. 106 are short.
   - Optional, second stage, for the 1708 key: **SP 91/5/298** (undeciphered duplicate,
     https://discovery.nationalarchives.gov.uk/details/r/C6719693) with **SP 91/5/294** (its deciphered
     version, https://discovery.nationalarchives.gov.uk/details/r/C6719691), both 22 Sept/3 Oct 1708. A
     whole letter of known plaintext, so it reconstructs that key completely, but no 1708 text is unread.
   - Not needed: SP 91/5/163 and 180 (decipher exists and is printed), SP 91/5/300 (duplicate of the printed
     f. 274).
2. Take the ordering route and prices from nationalarchives.gov.uk ("Order copies" on each record page, or
   "Record copying"), not from here. Each item is a separate record, so each goes in the basket separately.
   The TNA account problem logged in `ciphers/stepney-manchester-1702/REQUEST.md` (confirmation email never
   arrived) applies here too; fix it first.
3. Estimated size: f. 108 runs about three printed pages of English in the Sbornik, so 2 folios, 4 images;
   f. 106 about 2 images; f. 121 about 4 images. First stage about 10 images. The 294/298 pair about 10 more.

## The message

```
Subject: Digital copy request: SP 91/5, three despatches of Charles Whitworth, 1707

Dear Record Copying team,

I would like to order digital copies of three items from SP 91/5 (State
Papers Foreign, Russia, 1707-1708, Discovery reference C3426306), the
despatches of Charles Whitworth, envoy extraordinary at Moscow, to
Secretary Harley:

1. SP 91/5/108, Moscow, 30 July / 10 August 1707 (Discovery C6719621),
   catalogued "Partly undeciphered".
2. SP 91/5/106, Moscow, 23 July / 3 August 1707 (Discovery C6719620),
   catalogued "Partly in cipher".
3. SP 91/5/121, Moscow, 16/21 September 1707 (Discovery C6719626),
   catalogued "Partly in cipher".

Please copy every page of each letter, both sides of every leaf, including
any page that carries only cipher figures or the interlined decipherment,
and any decipher on a separate sheet filed with the letter. The cipher
passages and their contemporary decipherments are the point of the
request, so please do not omit pages that look like numbers only.

The text of item 1 is printed (Sbornik of the Imperial Russian Historical
Society, vol. 39, 1884, pp. 407-411) with one passage left undeciphered;
items 2 and 3 are wanted to recover the key from their deciphered cipher
passages so that the gap can be read.

Purpose: private historical research.

Thank you,
[Your name]
[Postal address]
[Email]
```

## If the copies show no decipher on ff. 106 and 121

- Order the 1708 pair, SP 91/5/298 with SP 91/5/294 (see above): the decipher is certain there, since the
  cataloguer names f. 294 as "deciphered version". If the 1708 cipher differs from the 1707 one, the 1707 key
  still has to come from a 1707 letter; try the next neighbours, ff. 93 (4/15 June 1707) and 133 (29 Oct/9
  Nov 1707), both "Partly in cipher".
- TNA SP 106/7, Queen Anne's cipher keys: 21 sheets are on DECODE (R525-R598), none labelled for Russia or
  Whitworth, but DECODE has not catalogued the whole box. A page check of SP 106/7 for "Mr Whitworth's
  cipher" is the last resort.
- BL Add MSS 37341-37397, the Whitworth Papers (range from memory, unverified), hold his own letter-books and may hold his keys; blocked while
  the British Library is not producing copies.

## Log

| Date | Action | Result |
|---|---|---|
| 2026-09-19 | Discovery API listing of SP 91/5 cipher items; Sbornik vols 39 and 50 checked for the plaintext; DECODE and both solver repositories checked | Only the gap in f. 108 is unread. Request drafted for ff. 108, 106, 121. No order placed. |
