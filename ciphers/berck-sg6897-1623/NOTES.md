open
Resolutien der Staten-Generaal Nieuwe Reeks Deel 6 (1623 - juni 1624, GS 208) pp.22, 28, 99, 405, 549, 561, 637 (res. 122/122b, 171/171a, 174, 636/636a, 637/637a, 2531/2531a, 3358/3358a, index p.637) and Deel 7 (juli 1624-1625, GS 223) p.29 (res. 177/177a) read in full by this worker via resources.huygens.knaw.nl/retroboeken/statengeneraal (`searchText` accessor, terms "Berck", "ontcijferd", "code", "sleutel", each run once per volume per CLAUDE.md's print-check convention; `pages.json` lookup, pages fetched directly).

QUEUE row: SCOUT-KEYS K3 (QUEUE.md "## Key-beside-cipher candidates (17 Oct 2026)"; harvest/SCOUT-KEYS-2026-10-17.tsv).

## Target

Johan Berck, Heer van Goidschalkoord, pensionary of Dordrecht, sent by the States General to Venice in 1622 to
press the Republic of Venice for overdue subsidy payments and, from early 1623, to report on the Valtellina
negotiations. Nationaal Archief 1.01.02 (Staten-Generaal), inv. nrs. 6897 (648 scans) and 6898 (712 scans),
both confirmed `availability: DIGITALIZED` via the item pages' own `drupal-settings-json` (`www.nationaalarchief.nl/onderzoeken/archief/1.01.02/invnr/6897` and `/invnr/6898`, fetched this session). No leaf images were opened (brief scope: check-solved only).

## Premise check (this worker, 17 Oct 2026)

(a) Folder's own prior mentions: none -- folder created this session.
(b) Other solvers' working files: Bourdeau's cyphersolver (shallow clone, full grep) and Aymeloglu's
    unsolved-ciphers (shallow clone, full grep) both searched for `-w "berck"` (word-boundary) and for
    "6897"/"6898": zero genuine hits in either (the raw substring "berck" matched only unrelated strings
    inside other words/filenames, e.g. "napoleon", confirmed false positives by re-grepping with `-w`).
    Matches SCOUT-KEYS K3's own "Bourdeau, Aymeloglu, DECODE, repo: no hit" line.
(c) Physical neighbours / same-lias mixing (**correction to SCOUT-KEYS K3's framing, see below**): the printed
    Resolutien calendar shows inv. 6897 is NOT a Berck-exclusive Venice lias -- it also holds at least two
    cipher items belonging to Cornelis Haga, the States' resident at Constantinople, filed by *date received*
    alongside Berck's Venice letters rather than by correspondent (see "Cross-correspondent mixing" below).
(d) Recipient-side editions: the recipient here *is* the States General (the holding body itself), so there is
    no separate "recipient's own edition" to check beyond the Resolutien series already read; no other state's
    documentary series would hold Berck's own despatches.

## Resolutions read (this worker, 17 Oct 2026)

- **Res. 122 (p.22, 19 jan. 1623):** "De Amsterdamse koopman Balthazar Coymans stuurt dd. 18 jan. een schrijven
  dd. Venetië 30 dec. 1622 van Berck door. H.H.M. geven de ambassadeur opdracht berichten die wel of niet voor
  mededeling geschikt zijn in aparte brieven te zetten, de laatste in een geheime code waarvan hij de sleutel
  moet opzenden (1622 no. 4752; 171, 234)." -- the founding instruction: Berck is to split his despatches, and
  anything secret goes in a separate letter in a secret code whose key he must send to The Hague. Footnote
  "122b": "S.G. 6897 (orig.). Berck schrijft in verband met de Valtellina niet te geloven ,,dat op Vranckrijck
  vast fondament te maecken is...''" -- this cited letter (30 Dec 1622) is itself in clear Dutch/quoted prose,
  not ciphered; the order to start using cipher comes *in reply* to it.
- **Res. 171 (p.28, in the entries for 25 jan. 1623, replying to Berck's letters of 15 Dec. 1622):** "...Wat
  betreft de correspondentie wordt opdracht gegeven alles aan de Staten-Generaal te richten, geheime
  mededelingen afzonderlijk in code (45, 122, 560, 2653)." Footnote "171a": "S.G. 6897 (minuut dd. 28 jan.)" --
  the States' own draft reply repeating/confirming the cipher instruction. (The brief's own citation named this
  as "res. 172"; p.28's actual res. 172 is an unrelated Kettler-regiment payment matter -- the cipher-relevant
  text on this page is res. 171, correctly identified and read here.)
- **Res. 636 (p.99, dated by position ~early April 1623, received from Haga not Berck):** "Haga schrijft dd.
  Constantinopel 5 febr. Besloten wordt de cijfercode op te bergen." Footnote "636a": "S.G. 6897 (orig.,
  grotendeels in cijfer; zonder code)" -- an original letter, mostly in cipher, *without* its code/key, filed
  in the same inv. 6897 as Berck's letters. This is **Haga's**, not Berck's.
- **Res. 637 (p.99, same date window, 17 maart 1623):** "Berck zet dd. Venetië 17 maart uiteen hoe men van de
  diensten van Luz gebruik kan maken..." Footnote "637a": "S.G. 6897 (orig.)" -- a Berck letter, no cipher flag
  on this one.
- **Res. 2531 (p.405, 12 jan. 1624):** "Berck schrijft dd. Venetië 22 dec. 1623." Footnote "2531a": "S.G. 6897
  (orig.). Met een door Duyck ontcijferd bericht inzake de onderhandelingen over de Valtellina." -- **the one
  confirmed Berck cipher item**: an original letter of 22 Dec. 1623 carrying a message that the States'
  griffier Duyck deciphered, concerning the Valtellina negotiations. This is a known-plaintext pair if the
  cipher text and Duyck's decipherment both survive together in the inv. 6897 file (not confirmed by image;
  no leaf opened this job).
- **Res. 3358 (p.549, 28/29 mei 1624):** "Ontvangen een brief dd. Constantinopel 30 maart van Haga." Footnote
  "3358a": "S.G. 6897 (orig.). Bij het duplicaat een in code gestelde mededeling." -- another **Haga**
  (Constantinople) item in inv. 6897, a duplicate carrying a message set in code; no decipherment mentioned.
- **Res. 177 (Deel 7, p.29, 22 juli 1624):** "Ontvangen een brief dd. Constantinopel 25 mei van Haga." Footnote
  "177a": "S.G. 6897 (orig.). A.v. een orig., geheel in code gestelde brief met het zegel van Haga en een
  receptum van 2 aug." -- a third **Haga** item, an original letter *entirely* in code, sealed, received 2
  Aug.; no decipherment is noted in the apparatus. If still unread, this is an undeciphered Haga cipher letter
  physically in inv. 6897.
- Register (index) check: p.637 (printed) is the "R" section of Deel 6's index; "sleutel" search hits there are
  false positives (the inn "De Sleutel" at res. 3427, and the index entry for that inn) -- no register entry
  for a Berck cipher key was found by the terms searched.
- `ontcijferd` (source 6): 1 hit total, = res. 2531 above (already read). `ontcijferd` (source 7): 0 hits.
  `code` (source 6): 5 hits = res. 122/171 (p.22/28, Berck, already read), res. 636/3358 (p.99/549, Haga,
  already read), and p.32 (res. 207, Langerack's cipher instruction -- a third, unrelated ambassador, not
  pursued further, out of scope). `code` (source 7): 1 hit = res. 177 above.

## Cross-correspondent mixing (finding, 17 Oct 2026, relevant to ciphers/haga-sg6896-1622)

S.G. inv. 6897 is a chronological "Lias Secrete Brieven 1623-1624" bundle, not a Berck-dedicated Venice lias as
SCOUT-KEYS K3 characterised it: it holds original cipher/code material from at least **two** correspondents --
Berck at Venice (the 22 Dec. 1623 Duyck-deciphered letter) and **Cornelis Haga at Constantinople** (three
items: 5 Feb. 1623 "grotendeels in cijfer; zonder code", a 30 Mar. 1624 duplicate "in code gestelde mededeling",
and a 25 May 1624 letter "geheel in code gestelde brief met het zegel van Haga", none noted as deciphered in
the printed apparatus). This matches ROOM.md's HAGA-LEAF2 finding (17 Oct, 04:38 UTC) that NA inv. **6896**
(the adjacent inventory number, orders ~320-328) interleaves a Venice-based correspondent into what was assumed
to be Haga's own run -- the same archival pattern (these 1623-24 "secreet" lias bundles mix ambassadors by
received-date, not by sender) seen from the other direction. Flagged in ROOM.md for whoever next picks up
either haga-sg6896-1622 or this target: a leaf hunt in 6896-6898 for either ambassador should expect interleaving, not a clean per-correspondent run, and the three Haga cipher citations above are a lead for that
target's own NOTES.md, not claimed or read further here (out of this job's scope -- no leaf hunt, no images).

## Web and blog check (CHECK-BERCK, 17 Oct 2026)

Four plain web searches: (1) "Johan Berck Venetië ambassadeur gedeciphreerd Duyck 1623" -- background on
Berck's 1622 Venice mission (DBNL, Ecartico) and the unrelated Huygens Suriano/Contarini Venetian-side letter
editions; no Duyck/decipherment hit. (2) "\"Johan Berck\" Venice States General cipher decipher" -- general
Venetian-cryptography scholarship (Soro, Histocrypt papers), no Berck-specific hit. (3) "\"6897\" OR \"6898\"
Nationaal Archief Berck Venetië sleutel cijfer" -- no matching result (UK National Archives and an unrelated NA
handwriting-recognition index). (4) "Johan Berck resident Venetië Staten-Generaal Valtellina 1623 1624 1625" --
DBNL/Ecartico biography only, no Valtellina-specific or cipher hit. Plus one targeted query, "\"Berck\" \"Duyck\"
cipher decrypted 1623 States General Venice" -- Huygens Suriano/Contarini pages and Histocrypt Venetian-cipher
papers, no Berck/Duyck hit.
Three blog site searches: `site:scienceblogs.de klausis-krypto-kolumne Berck Venedig` -- zero matching posts.
`site:cryptiana.blogspot.com Berck` -- zero matches (search engine returned only unrelated "Berck, France" town
hits). `site:ciphermysteries.com Berck Venice` -- zero matches (one irrelevant hit, an unrelated manuscript
post). No comment thread anywhere named this item.

## Six sources

1. **Web + 3 blogs:** see above, no prior decipherment or solve found.
2. **Print (editions):** Resolutien SG NR 6 pp.22, 28, 99, 405, 549, 561 and NR 7 p.29 read directly via
   Huygens retroboeken (see "Resolutions read" above) -- the printed calendar's own apparatus is the only
   edition found that discusses Berck's cipher correspondence; no separate edition of Berck's Venetian
   despatches was found by web search (none exists as far as searched).
3. **DECODE listing (cache):** `sources/decode/records-decrypted-2026-09-24.tsv` and
   `records-non-decrypted-2026-09-24.tsv` grepped for "berck" (0 hits) and "venic|venez|venet" (hits are all
   Archivio di Stato di Venezia Italian-language items, unrelated to the Dutch NA 1.01.02 series) -- no DECODE
   record for this item.
4. **Bourdeau (cyphersolver):** shallow clone, grepped for "berck" (word-boundary: 0 genuine hits) and
   "6897"/"6898" (0 genuine hits).
5. **Aymeloglu (unsolved-ciphers):** shallow clone, grepped for "berck" (0 hits) and "6897"/"6898" (0 hits
   outside an unrelated ottobon-1589/catalogue file).
6. **Cryptiana:** grepped `sources/cryptiana/`, `CATALOG.md`, `LANDSCAPE.md` for "berck" -- 0 hits.

## Verdict

**open**, confirmed unsolved by six sources (web x4, 3 blogs, Resolutien SG NR 6 pp.22/28/99/405/549/561 and
NR 7 p.29 read directly by this worker, DECODE cache, Bourdeau grep, Aymeloglu grep, Cryptiana grep): no source
reports a prior decipherment, key publication or solve of any Berck cipher passage beyond the one the editors
themselves already note as contemporaneously deciphered (res. 2531a).

**Deciphered-letter list (known-plaintext pairs):**
- Berck's letter of **22 Dec. 1623** (Venice), original in S.G. 6897, "met een door Duyck ontcijferd bericht
  inzake de onderhandelingen over de Valtellina" (res. 2531a) -- the one confirmed pair. Whether the cipher
  text and Duyck's decipherment physically survive together in the file is unconfirmed (no image opened).
- No other Berck letter is flagged "ontcijferd" (deciphered) anywhere in NR Deel 6 or Deel 7's apparatus; the
  only other Berck-cipher-adjacent entries are the Jan. 1623 instructions (res. 122, 171) to begin using a
  secret code, which name no specific letter.
- (Not Berck's own, but found in the same inv. 6897 and relevant to ciphers/haga-sg6896-1622: three Haga
  cipher items, res. 636/3358/Deel-7-177, none noted as deciphered -- see "Cross-correspondent mixing" above.)

**Key extant:** not found. No key sheet, codebook or "Sleutel" entry for Berck's Venice cipher was located --
not in the Resolutien register, not via a targeted web search for NA 1.01.02 inv. 12578 (the brief's named
candidate series; the search returned nothing relating to inv. 12578 at all, so neither confirmed nor ruled
out by this method), and not elsewhere. The States' own order (res. 122) that Berck "de sleutel moet opzenden"
(must send the key) establishes that a key was *supposed* to exist in The Hague from early 1623, but no
resolution or footnote in the two volumes read records its arrival, filing location or survival.

`python3 tools/intake_gate_check.py berck-sg6897-1623` output:
```
berck-sg6897-1623: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit: 0
```

## While waiting

The one named next step (the 22 Dec. 1623 original + Duyck's decipherment, located by docket date in inv.
6897) depends on nobody outside this project -- a dateline-strip or docket-date image pass on inv. 6897's
scans, same method as AITZEMA-SHEET/AITZEMA-RUN1618 used on inv. 6025. Not blocked on a person, key, or
archive reply.

## Next test and price

1. **First choice (cheap, ~USD 1-1.5):** a dateline-strip contact-sheet pass over inv. 6897 (648 scans)
   targeting late-Dec. 1623/early-Jan. 1624 dockets, to locate the 22 Dec. 1623 original and confirm whether
   Duyck's decipherment is filed with it (the known-plaintext pair) or separately -- same method as
   AITZEMA-SHEET (stride-10 thumbnails, then native-res on hits), scoped to a ~60-80-scan date window rather
   than the full lias.
2. **If that pair is confirmed and other Berck cipher passages are wanted:** a second pass over inv. 6898
   (712 scans, 1624-1626) for further "in code"/"ontcijferd" dockets, since Deel 7 (the only printed Resolutien
   volume covering part of that span, July 1624-1625) showed only Haga cipher material, not Berck's, in this
   job's search.
3. **Flagged, not this job's to run:** the three Haga cipher citations in inv. 6897 (res. 636, 3358, Deel-7-177)
   are a direct lead for ciphers/haga-sg6896-1622's own next step, given HAGA-LEAF2's finding that the
   1623-24 lias bundles interleave correspondents by date.

## Research-director questions (owner's loop, 17 Oct 2026)

- **What was learned:** inv. 6897 is a mixed 1623-24 secret-letter lias holding cipher material from both
  Berck (Venice) and Haga (Constantinople), not a Berck-exclusive series; only one Berck cipher passage (22
  Dec. 1623) is attested in the printed Resolutien apparatus, and it was already deciphered at the time by
  Duyck.
- **Assumptions the result depended on:** that the printed Resolutien SG NR 6/7 calendar's editorial footnotes
  reliably flag every cipher-related passage in the underlying archive (they may not catch a cipher passage the
  19th/20th-century editors judged unremarkable, or one in inv. 6898 falling after Deel 7's July 1625 end).
- **Which remain unverified:** whether the 22 Dec. 1623 cipher text and Duyck's decipherment survive together
  as a physical pair in inv. 6897 (no image opened this job); whether Berck's key was ever actually sent and
  filed (inv. 12578 unconfirmed either way); whether inv. 6898 (1624-1626, no printed calendar yet covering
  most of it) holds further undeciphered Berck cipher passages.
- **Alternative explanations:** the apparent absence of a second Berck cipher passage could reflect that Berck
  mostly complied with carrying secrets in clear once the Venetian political moment passed (res. 637, 17 Mar.
  1623, is already back to ordinary clear prose about Luz's employment), rather than a real gap in the record.
- **Most informative different experiment:** the dateline-strip image pass on inv. 6897 named above, which
  would directly confirm or refute whether the known-plaintext pair survives as a physical unit -- more
  informative than further text-search on the printed calendar, which has now been exhausted for the terms
  that would surface a cipher flag.
- **Continue / pivot / acquire / reprioritize:** continue on this target with the named image pass if program C
  wants a third key-beside-cipher candidate progressed to a cheap test; otherwise reprioritize to K4-K9 (TNA
  rows), which are untested and may offer a higher per-letter deciphered-pair yield for the same image-pass cost.
