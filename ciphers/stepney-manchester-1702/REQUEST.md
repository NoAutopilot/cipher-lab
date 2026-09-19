# Copy request: The National Archives, Stepney's letter-book, SP 105

This route needs no key. Stepney's letter-books hold copies of his out-letters in clear, so the entry for
23 March 1702 should give the plaintext of the 24 code groups directly.

## Before sending

1. Piece identified on Discovery, 19 Sept 2026: **SP 105/65**, "Letter book(s) of George Stepney, envoy
   extraordinary to the Holy Roman emperor", 1702 Jan-1702 Aug. Discovery record C3609655:
   https://discovery.nationalarchives.gov.uk/details/r/C3609655 (open it and use "Order copies" / "Record
   copying"; the piece is not digitised and has no item-level catalogue, so no folio can be quoted). The
   neighbours, all with the same title, are SP 105/64 (1701 Oct-Dec) and SP 105/66 (1702 Sept-Dec). SP 105/61
   (1701-1705) is a memoranda book on Sweden and Poland, not a letter-book. SP 105/60 is the only Stepney volume
   catalogued to item level, and it stops in 1694.
2. Take the ordering route and prices from nationalarchives.gov.uk ("Order copies" or "Record copying"), not
   from here. Because the volume is not itemised, the request below asks for a paid search by date and
   addressee if the copying team cannot find the entry from the description.
3. Secondary TNA volume for the same period: SP 80/18, "George Stepney (Envoy Extraordinary)", 1702 Jan-June
   (Discovery C5909986), the despatches as received in London. Manchester was Secretary of State from January
   1702, so a copy or decipher of the letter may sit there if it was treated as official.

## The message

```
Subject: Digital copy request: SP 105/65, Stepney letter-book, entry of 23 March 1702

Dear Record Copying team,

I would like to order a digital copy of one entry from George Stepney's
Vienna letter-book in SP 105 (Archives of British Legations), piece
SP 105/65, "Letter book(s) of George Stepney, envoy extraordinary to the
Holy Roman emperor", 1702 Jan-1702 Aug (Discovery reference C3609655).

The entry I need is Stepney's letter to Charles Montagu, Earl of
Manchester, dated Vienna, 23 March 1702 (New Style; 12 March 1702 Old Style, so the
letter-book may head it 12/23 March). The original received
letter, now at Yale (Osborn MSS fc37, Manchester papers, box 8 folder 40),
contains two short passages in cipher that were never deciphered; the
letter-book copy should carry them in clear. Please also copy the facing
or adjacent pages if the entry runs over.

If the folio cannot be identified from this description, please treat this
as a request for a paid search of the March 1702 entries of SP 105/65 for
a letter to the Earl of Manchester, and let me know the cost before
proceeding.

Purpose: private historical research.

Thank you,
[Your name]
[Postal address]
[Email]
```

## If the letter-book has no copy

- BL Add MSS 7058-7078, the Stepney Papers, reportedly include his own copies and his cipher keys. Blocked
  while the British Library is not producing copies.
- TNA SP 106, the office's cipher templates of the period. "Mr. Stepney's cipher" was sent to Manchester in
  August 1701 (HMC 8th Report, App. II, p. 85), so a copy of it may also sit in the Manchester papers at Yale
  or Huntingdonshire Archives, though not among the two keys Yale has digitised.

## Log

| Date | Action | Result |
|---|---|---|
| 2026-09-19 | Tried to browse SP 105 on TNA Discovery to fill in the piece reference | Not done: this session is network-restricted (discovery.nationalarchives.gov.uk and www.nationalarchives.gov.uk both blocked by the egress proxy, HTTP 403 on CONNECT), so the `[SP 105/xx, from Discovery]` placeholder remains and the lookup must be repeated from a session with web access |
| 2026-09-19 | Browsed SP 105 on Discovery via the JSON API (series C13644, subseries "Correspondence and papers of Sir George Stepney" C69924, pieces SP 105/48-77 listed; details fetched for SP 105/61-67; children endpoint queried for SP 105/65) | Piece found: **SP 105/65**, "Letter book(s) of George Stepney, envoy extraordinary to the Holy Roman emperor", 1702 Jan-1702 Aug, record C3609655, not digitised, no item-level entries, so no folio for 23 March 1702 can be quoted. Placeholder in the draft replaced. SP 105/61 (1701-1705) is a memoranda book on Sweden and Poland; SP 105/62-64 cover Mar-Dec 1701, SP 105/66 Sept-Dec 1702. Also noted SP 80/18 (Stepney's despatches, 1702 Jan-June). The Discovery HTML page answered HTTP 202 (JavaScript challenge) to curl, so the "Order copies" button was not verified from here. No order placed. |
| 2026-09-19 | Order started on TNA Discovery: SP 105/65 page check (£9.92) form reached, details text prepared (see below) | Not completed: the TNA account confirmation email did not arrive. To resume: check spam, resend verification, verify the address, then paste the text and add to basket |

## Text for the page-check form

```
Please locate and copy the entry for George Stepney's letter to Charles
Montagu, Earl of Manchester, dated Vienna, 23 March 1702 (New Style; the
letter-book may head it 12 March or 12/23 March 1702, Old Style). This is
SP 105/65, Stepney's letter-book as envoy extraordinary at Vienna, January
to August 1702. The letter opens "I am honoured with your letter of the
10th past. This will come to the Hague by a courier of Count Wratislaw's"
and mentions the Emperor's ratification of the article against the
pretended Prince of Wales, and the expedition of Naples being laid aside.
The received original at Yale has two short passages in cipher; the
letter-book copy should carry them in clear. Please copy the whole entry
and the facing or adjacent page if it runs over. Purpose: private
historical research.
```
