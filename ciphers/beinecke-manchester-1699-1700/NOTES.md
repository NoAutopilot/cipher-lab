# Manchester Papers word-code group, Beinecke OSB MSS fc37 (DECRYPT/DECODE nos. 2859, 2860, 2865, 2866; 1699-1700)

found-solved

HMC 8th Report, Appendix II (1881) read in full by this worker (`Eighth_Report_Historical_MSS_djvu.txt`,
archive.org identifier `EighthReportHistoricalMSS`) and *Memoirs of Affairs of State* (Christian Cole, ed.,
1733; archive.org identifier `10212967bsb`) read in full by this worker for the two Vernon letters; the two
Yard letters were not re-opened by this worker (Bourdeau's own published reading, checked live instead, per
§2 below).

## Summary (read this first)

CS-MANCHESTER (parent worker, 27 Sept 2026). Queued by `SCOUT-OWN-7` (QUEUE.md "SCOUT-OWN-7 key-adjacent
candidates" row 1, `KEY-ADJACENT.tsv` row `glorious.htm`) from Tomokiyo's `glorious.htm`, which quotes the
DECODE catalogue's own status for four Manchester Papers letters as "Non-decrypted. Can be deciphered with
THE=454," and shows an inline partial gloss (code numbers glossed as English words, interspersed with
elisions `....`) for each. The brief asked whether that gloss already amounts to a printed plaintext, per
letter. **All four are found-solved, for two different reasons, and none is a candidate for a campaign here:**

| DECODE no. | Letter | Verdict | Who solved it, when |
|---|---|---|---|
| 2859 | Yard to Manchester, Whitehall, 16 Oct 1699 | found-solved | `dbourdeau/cyphersolver`, 18 Sept 2026 (modern recovery; no prior print) |
| 2860 | Yard to Manchester, Whitehall, 12/24 Oct 1699 | found-solved | `dbourdeau/cyphersolver`, 18 Sept 2026 (modern recovery; no prior print) |
| 2865 | James Vernon to Manchester, Whitehall, 18 Nov 1700 | found-solved | period decipherment on the manuscript's own fly-leaf; printed in Cole's *Memoirs of Affairs of State* (1733) p.248-249 |
| 2866 | James Vernon to Manchester, Whitehall, 12/23 Dec 1700 | found-solved | period decipherment on the manuscript's own fly-leaf; printed in Cole's *Memoirs of Affairs of State* (1733) p.270-271 |

(DECODE no. 2864, George Stepney to Manchester, Vienna, 23 March 1702, is a fifth letter in the same
glorious.htm register but is **not** one of this brief's four targets; it is already `ciphers/stepney-manchester-1702/`
in this repository, verdict `offline-only`, unrelated cipher.)

### 1. Yard letters (2859, 2860) -- Bourdeau's `yard1699`, 18 Sept 2026

`dbourdeau/cyphersolver` was shallow-cloned (depth 1) and grepped for "2859", "2860", "Manchester", "Vernon",
"Yard" before any other step, per this repo's now-standard practice for Tomokiyo-list targets (CS-CLAIR331,
CS-FR3976, same week). `targets/yard1699/NOTES.md` opens: **"Verdict: SOLVED (read in full, 18 Sept 2026)."**
It reads both letters completely with the Manchester papers' own printed key template ("Diplomatic cipher,
contemporary copy", Yale OID 2046948, box 18/47), validated against the contemporary interlinear decipherment
of the sibling 5 Oct 1699 letter, and states explicitly: "Tomokiyo had identified THE=454 and decoded the
first groups... No full reading had been published: HMC calendars both as undeciphered." The full plaintext
of both letters (368 groups, apart from five slips of Yard's pen) is in that file and in the live write-up,
`cyphersolver/README.md` line 168 ("complete", 18 Sept 2026) links
[dbourdeau.github.io/cyphersolver/yard1699.html](https://dbourdeau.github.io/cyphersolver/yard1699.html) --
checked live this session, `HTTP 200` (`curl -sS -o /dev/null -w '%{http_code}'`, 27 Sept 2026). Bourdeau's
Yale OIDs for the two target letters (16601173 = 12 Oct 1699 = DECODE 2860; 16601175 = 16 Oct 1699 = DECODE
2859) were independently reproduced by this worker's own Yale catalogue search (§4). No contribution remains
for us: Bourdeau's reading is the first, and it is his to credit (CLAUDE.md rule 8).

`aaymeloglu/unsolved-ciphers` (shallow clone, same grep): no dedicated target or reading for these two
letters, only raw DECODE catalogue rows (`catalogue/decode-catalog.csv`).

### 2. Vernon letters (2865, 2866) -- a 293-year-old period decipherment, printed in 1733

Neither solver repository has a dedicated target for the Vernon letters. But HMC 8th Report App. II (1881),
read whole (not just an expected page range, per README's "whole volume" rule) for every "Vernon" hit,
calendars both explicitly with a decipherment already noted:

> (lvi.) Nov. 18. Endorsed Nov. [29].--James Vernon to the Earl of Manchester on the Partition Treaty, and
> on the project for placing a French Prince on the throne of Spain. **(Partly in cipher, with decipher on
> fly-leaf. Printed, with some variations, in Cole's Memoirs p. 248.)**--Whitehall.
> (`Eighth_Report_Historical_MSS_djvu.txt` line 232209 area)

> (lxv.) Dec. 12. Endorsed [23].--James Vernon to the Earl of Manchester, giving some particulars of Mons.
> Taillard's interview with the King, and of the movements of Meers and Captain Magrath. **(Partly in
> cipher, deciphered on fly-leaf. Nearly all printed, as deciphered, in Cole's Memoirs, p. 270.)**--Whitehall.
> (line 232287 area)

These are DECODE 2865 (18 Nov 1700) and 2866 (12/23 Dec 1700) exactly, by date, sender, recipient and place.
Cole's *Memoirs of Affairs of State* (1733; identifier `10212967bsb`) was fetched in full
(`10212967bsb_djvu.txt`) and both letters were found and read entire:

- **2865**, p.248-249 of the printed edition (line 20696 area of the OCR text): "To the Earl of Manchester.
  My Lord, Whitehall, Novemb. 18. 1700. O.S. ... but the King has not given me any thing in command at
  present to write to you. Their Resolutions are taken; therefore His Majesty may be allowed to consider a
  little what may be the Consequence of so sudden a Change in that Court, as likewise to expect what are the
  Sentiments of other Princes and States, who are equally concerned in the preservation of the Peace of
  Europe, and the preventing the Balance of Power being broken..." -- this matches Tomokiyo's own inline
  gloss on `glorious.htm` word for word ("...equal ly concern ed in the preser vation of the peace of Europe
  & the preventing the balance of power being ....").
- **2866**, p.270-271 (line 22350 area): "To the Earl of Manchester. My Lord, Whitehall, Decemb. 12/23. 1700.
  [I hope] Mr. Chetwynd is got well to Paris, and that you have forwarded the Letter he brought you, and that
  care has been taken to secure the Letter in case of Accidents. I received your Excellency's Letter of the
  18th on Tuesday last, and sent it immediately to Hampton-Court. I hear from Calais that Meers is come
  thither, and is gone to Dunkirk..." -- again matching Tomokiyo's gloss word for word ("Chetterpind*"/
  "pares*" are Tomokiyo's own OCR-of-code misreadings of "Chetwynd"/"Paris", not a different letter).

So Tomokiyo's inline glosses for these two are not an unfinished key application -- they are Tomokiyo quoting
(with his own added code numbers) a text that a contemporary decipherer already wrote on the manuscript's
fly-leaf and that Cole printed in 1733, 293 years before this session. HMC's own 1881 calendar already links
letter to print (a specialist edition already links the item to its decipherment: README's F0 shape). No
cryptanalysis or key application by us would add anything; the remaining "...." gaps in Tomokiyo's excerpts
are places where he stopped quoting, not places the key fails.

### 3. Correction to KEY-ADJACENT.tsv / QUEUE.md

Both files described this row as "key printed (THE=454), Tomokiyo's page already glosses most code numbers"
and "a worker mainly transcribes/verifies and fills remaining blanks" -- accurate as far as what Tomokiyo's
page alone shows, but wrong about what work remains: two of the four letters were already fully solved by
Bourdeau (a fact not on Tomokiyo's page, dated after it), and the other two were never actually unsolved --
HMC's own 1881 calendar, sitting one click away and already used for the neighbouring Stepney letter in this
same register (`ciphers/stepney-manchester-1702/`), already named the print citation. Both files corrected in
this push (see diff); QUEUE.md row 1 of the SCOUT-OWN-7 table now reads "check-solved found-solved."

### 4. DECODE status change and Beinecke catalogue (secondary checks, per brief)

This repo's own 24 Sept 2026 DECODE crawl (`sources/decode/records-decrypted-2026-09-24.tsv` lines 748, 749,
753, 754) already shows **all four** records as `Decrypted` (Box 02 Folder 51 = 2859; Box 02 Folder 49 =
2860; Box 05 Folder 56 = 2865; Box 05 Folder 65 = 2866) -- a change from the "Non-decrypted" status Tomokiyo
quoted when he wrote `glorious.htm`. Consistent with §1/§2 above (someone updated DECODE's status field after
these were solved/recognised), but DECODE's own "Decrypted" tag is not itself trusted as sufficient evidence
in this repo without independent confirmation (`ciphers/rah9-34-fernandez-1525/NOTES.md`: a DECODE-tagged
"Decrypted" neighbour "carries no decipherment" on inspection) -- the independent confirmation here is
Bourdeau's own repo (§1) and HMC/Cole (§2), not the DECODE tag by itself. DECODE's RecordsView content was not
opened (login-gated; per the CLAUDE.md host table, full-size images and documents are account-wide blocked
even when logged in, so no attempt was made -- would not have answered the question anyway).

Beinecke catalogue: one browser-tool request to `collections.library.yale.edu/catalog?q=%22Manchester+papers%22+cipher+Vernon`
(27 Sept 2026) returned the individual catalog records for all four target letters plus siblings, each
carrying **4 digitised images** (IIIF, IDs recorded in sources.tsv) and, for three of the four, the identical
calendar text already quoted above (Yale's own catalogue evidently draws on the same HMC calendar). Yale OIDs:
16601175 (2859), 16601173 (2860), 16601197 (2865), 16601198 (2866). No further Beinecke requests were needed
(brief allowed up to 4; one sufficed). DECODE listing crawl already covered the status question (see above);
no fresh `decode_list.py` run was needed since the disk crawl already had all four records.

## 5. Search log (rule 1)

- Cryptiana `glorious.htm`: on disk, `sources/cryptiana/web/glorious.htm`, read in full for the "Diplomatic
  Code (c.1699-1701) (THE=454)" section, 27 Sept 2026.
- `dbourdeau/cyphersolver`: shallow clone (depth 1), 27 Sept 2026, grepped for "2859", "2860", "2865", "2866",
  "Manchester", "Vernon", "Yard"; `targets/yard1699/NOTES.md`, `targets/stepney/NOTES.md`, `README.md` read
  in full.
- `aaymeloglu/unsolved-ciphers`: shallow clone (depth 1), 27 Sept 2026, same grep; `catalogue/decode-catalog.csv`
  and `catalogue/decode-records.jsonl` checked for records 2859/2860/2865/2866 (present in the CSV only, same
  status as our own crawl).
- DECODE (de-crypt.org): this repo's own 24 Sept 2026 crawl on disk, `sources/decode/records-decrypted-2026-09-24.tsv`;
  no fresh network request needed (records already present with box/folder identifiers). RecordsView content
  not attempted (login-gated, account-wide document/image block per CLAUDE.md host table).
- Beinecke (collections.library.yale.edu): 1 browser-tool request, 27 Sept 2026 (host is bot-challenged to
  plain curl, confirmed again this session: `HTTP 202` to a direct `catalog.json` curl call).
- Internet Archive full text: `EighthReportHistoricalMSS` (`Eighth_Report_Historical_MSS_djvu.txt`, control
  term "Earl of Manchester" tested via be-api fts first, 1 hit, then the whole volume fetched and grepped for
  "Vernon" -- 60+ hits read, the two target entries found and quoted above) and `10212967bsb` (Cole's
  *Memoirs of Affairs of State*, 1733; full text fetched, both letters located by distinctive phrase and read
  in full). *Court and Society from Elizabeth to Anne* (1864) was not reopened by this worker: Bourdeau's
  `stepney/NOTES.md` already establishes it does not print the neighbouring Stepney letter in the same
  folder, and it is not the edition either Vernon letter cites (both cite Cole 1733 by name and page). *Letters
  illustrative of the reign of William III* (James's edition of Vernon's letters to the **Duke of Shrewsbury**,
  1841) is a different correspondence (Vernon-to-Shrewsbury, not Vernon-to-Manchester) and was not searched
  further once Cole 1733 confirmed both target letters in full.
- Google Books / OpenAlex / Semantic Scholar / print_check.py: not run. Rule 10's novelty question does not
  arise here -- this is a check-solved verdict, not a claimed reading of ours, and CLAUDE.md's pipeline stage
  2 (check-solved) does not require the verifier's rule-10 source sweep. A verifier session, if this target is
  ever cited outward, still runs the full AUDIT.md search log.

## 6. Intake gate

```
$ python3 tools/intake_gate_check.py beinecke-manchester-1699-1700
beinecke-manchester-1699-1700: found-solved (line 3) -- edition/page or full-text-search citation found within 6 lines
EXIT:0
```
