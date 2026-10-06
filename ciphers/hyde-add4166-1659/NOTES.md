open
Thurloe State Papers vol. 7 (Birch 1742; British History Online pp.771-781, letter on printed pp.775-776) and Calendar of the Clarendon State Papers vol. IV 1657-1660 (Routledge, 1932; full text, whole-volume grep, IA calendarofclaren04bodluoft) read by this worker; the 1 Nov 1659 letter's numerals are printed without any decipherment in Thurloe and the letter is absent from the Calendar.

# hyde-add4166-1659: Hyde to "Mr Milles", 1 Nov 1659, BL Add MS 4166 ff.92-93 (DECODE R4886)

Check-solved by worker NB-HYDE for LANE NEWT-B-account-2, 6 Oct 2026 (date -u 23:19-23:5x UTC). No transcription, key application or cryptanalysis done. No ciphertext.txt: only a print transcription exists (Birch 1742 via BHO, and Tomokiyo's copy of it), and it is quoted below as a source, not adopted as a transcription of the leaf (rule 2: image not seen; a negative or any later test is conditional on it).

## Item
- Letter of Sir Edward Hyde to Mr Milles (a cover name), 1 Nov 1659, a copy. f.92 is clear English (answer to a chancery bill = cover story; "Edmundson"/"Ch. Stuart"; "I pray direct 966 232 to 925 794 920 932"). f.93 carries the numerals: two lines of numbers with a few clear words ("am", "you may use", "or the", "that", "as"), then about 45 lines of short number groups each followed by a cover name ("220 101 25 12 741 8 Mr. Perkins", "670 333 159 Mr. Tush", "9 20 23 12 772 25 Mr. Holt" ...), then a clear closing paragraph ("Sir, The fear I apprehend of interception for this letter (wherein I send you a cypher) ...").
- Printed text (Birch 1742 vol. 7, headed "An intercepted letter. 1st of Nov. 1659. In the possession of Joseph Jekyll, esq;" pp.775-776): numerals printed bare, no gloss, no interlinear decipherment, no editorial note. BHO copy saved in the scratchpad during this check (not committed).
- BL catalogue record (searcharchives.bl.uk/catalog/040-002109623, read 6 Oct 2026): "ff. 92r-93*v: Letter of Sir Edward Hyde to Mr Milles, 1 Nov 1659. With cipher key. A copy." Availability flag quoted: "http://access.bl.uk/item/viewer/ark:/81055/vdc_100165336989.0x000001 (digital images currently unavailable)". So the leaf cannot be viewed from the BL; ff.94r-v is a spy's letter to Thurloe "enclosing a cipher-key, 1659" and the BL note says "the cipher-key may be that at f. 95r" (DECODE R4887, f.95, type Key, N/A).
- DECODE R4886 (login-free record page fetched 6 Oct 2026, 1 request): Status Non-decrypted, Author Sir Edward Hyde, Receiver Mr Milles, Symbol set Numerical, 2 pages, no documents attached, access mode "Authentication required". No login attempted.

## Sources checked (6 Oct 2026)
1. Web: queries in the Web and blog check section. No decipherment, plaintext or model-solve announcement found.
2. Print: Thurloe vol. 7 (read, as above; Google Books API volume search with country=US returns the same bare numerals in two Birch volumes, ALL_PAGES snippets: "Mr. Perkins . 670 333 159 Mr. Tush"). Calendar of Clarendon State Papers vol. IV 1657-1660: whole-volume grep of 2.28 MB OCR for Milles/Mills, Perkins, Tush, Knots, Jekyll, Edmundson (3 hits, all other letters: "Edmundson [the King]" in Brodrick correspondence), the numeral groups 966/925/794/920/932/953/774 (no hit as a cipher group), and the 1 Nov 1659 date (nearest entries: Mordaunt 31 Oct, Huone 1/11 Nov, p.429; none is this letter). The Calendar covers Clarendon MSS, so absence is expected: the BL copy is Thurloe's intercept.
3. Community lists: Tomokiyo unsolved.htm (sources/cryptiana/web/unsolved.htm line 522-523): "An intercepted letter of Edward Hyde dated 1 November 1659 (Add MS 4166, f.92-93 (DECODE R4886)) has some undeciphered portions." and thurloe.htm "f.92-93 (DECODE R4886)": "F.93 is full of undecoded code numbers"; CATALOG.md row "Open". Cipherbrain, Cryptiana blog and Cipher Mysteries site searches: nothing on this letter.
4. DECODE: as above.
5. Bourdeau (dbourdeau/cyphersolver, fresh shallow clone 6 Oct 2026): no folder for this letter. targets/hyde/ is a different item (Hyde's ciphered superscriptions to Barwick, 1659-60, printed in the 1721 Vita; verdict "dummy numbers"); the only other hits are Tomokiyo mirrors under targets/napoleon/ and the DECODE id list. targets/hyde/NOTES.md applies the Hyde-Barwick key (THE=370, numbers 1-692) to those superscriptions only. His text on this letter: none found.
6. Aymeloglu (aaymeloglu/unsolved-ciphers, fresh shallow clone 6 Oct 2026): catalogue/decode-records.jsonl line 468 and decode-catalog.csv row 4886 list the record as Non-decrypted, nothing else; no folder, no working file.

Stated-next-step check (check-solved.md): no planning line in either repository names this letter, so no duplicate-effort risk found.

## Verdict
`open`, conditional on the BL leaf not having been seen (images unavailable, DECODE image needs login) and on the printed transcription. What would change it: a decipherment in Birch's note, a Thurloe-office decipher copy, or a published key at f.95r. None found in what was read.

Observations for whoever briefs a first test (not tested here):
- The group values run to 966; the Hyde-Barwick key (Bourdeau, barwick_key.py, numbers 1-692, Vita 1721 plate) cannot cover the high groups, and Bourdeau found it did not decode the superscriptions either. Whether it applies to the low groups is untested.
- f.93 looks like a table, not running cipher text: number groups followed by cover names, with 670 and 101 each occurring six times and 25 four times. The closing clear paragraph says the letter sends a cypher. The names may be the key's cover-name list, giving cribs; this is a reading of the print, not a result.
- Census of the BHO print from "I pray direct" to the clear closing paragraph (script run inline, no key applied): 133 numerals, 103 distinct, min 5, max 966. Unicity and any matched control belong to the spec step.

## Premise check (NB-HYDE, 6 Oct 2026)
(a) Folder's own mentions: no prior folder. Related folders: ciphers/monck-1660/NOTES.md lines 56-60 describe Tomokiyo's f.92-93 row as a separate 1 Nov 1659 intercept and point at Bourdeau's hyde/ (a different item); thurloe-printed has nothing for it (its P1-P28 do not include this letter, grep "4886" and "1659" found only Fauconberg rows). Found: no decipherment mentioned anywhere.
(b) Other solvers' working files: not found. Bourdeau's only run of the Hyde-Barwick key is on the superscriptions; Aymeloglu has only the catalogue row.
(c) Physical neighbours: unreachable. BL images "currently unavailable"; DECODE full images need an authenticated account and no login was attempted. ff.94r-v (spy letter with cipher-key) and f.95r (key, DECODE R4887) are described in the BL record only. Left open as the first action for a person or a later session with image access.
(d) Recipient side / Hyde side editions: Calendar of Clarendon State Papers vol. IV: not found. Birch's Thurloe vol. 7: found, undeciphered. Barwick's Vita 1721 / Life 1724: not searched for this date (the Mills letter is not to Barwick; the Barwick OCR is not on disk here). Not found does not mean absent.

## Web and blog check (NB-HYDE, 6 Oct 2026)
Plain searches (WebSearch, standard): (1) Hyde "intercepted letter" 1 November 1659 "Mr. Mills" cipher Thurloe deciphered; (2) Add MS 4166 f.93 Hyde 1659 cipher "Edmundson" Charles Stuart decipherment; (3) "I pray direct" "966" Hyde Mills Perkins Tush Craft Knots cipher 1659; (4) Hyde intercepted letter 1659 Thurloe cipher solves Claude. Hits opened: BL catalogue record (read), BHO Thurloe vol. 7 (read); the rest (Yale Manchester papers, Barwick superscription notes, Harper's "Spycraft") are other items. No model-solve announcement found.
Blog site searches: cryptiana.blogspot.com / cryptiana.web.fc2.com (allowed_domains search, 1 hit page cryptiana.blogspot.com/2026/, nothing on Hyde 1659); ciphermysteries.com (search returned unrelated posts only); scienceblogs.de/klausis-krypto-kolumne (nothing on Hyde 1659). Comment threads of these hits not opened because no hit concerns this letter.
Requests (approximate, counted from the session): DECODE 1, BL catalogue 1, BHO 1, archive.org 7 (advancedsearch 1, metadata 2, fts 7 incl. be-api, download 1), Google Books 3, GitHub clones 2, web searches 7.

## While waiting
One action that depends on nobody: transcribe nothing yet; first compare the print's numeral groups on pp.775-776 (BHO) with the groups available from the DECODE thumbnail strip if a login-free thumbnail exists, otherwise do a grep-level census of the printed groups (count, distinct, max value, groups preceding cover names) in a script, no key applied.

## Intake gate output (6 Oct 2026)
```
hyde-add4166-1659: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```
`tools/next_steps.py --wait-only | grep hyde-add4166` printed no line.
