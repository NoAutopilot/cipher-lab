# ra-ud-chiffer-handlingar

Status: closed-negative

## What this is

"Handlingar ang. chiffer" — 18th/19th-century cipher-system descriptions, including F. Gripenstierna's 1786
proposal for a cipher machine. Riksarkivet i Stockholm/Täby, "Utrikesdepartementet med föregångare /
Kabinettet för utrikes brevväxlingen Huvudarkivet / Handlingar ordnade efter ämne / Övriga ämnesordnade
handlingar / Samlingsserie", reference code `SE/RA/221/2210.01.1/F/F 5/F 5 C/7`. Catalogue note (verbatim):
"Handlingar ang. chiffer, med bl.a. skrivelser från F. Gripenstierna 1786 ang. en chiffermaskin, beskrivningar
av chiffersystem under 1700- och 1800-tal, kvitton på mottagna chiffernycklar. Jfr. vidare samlingen
Chifferklaver, över vilken det finns ett kortregister i forskarexpeditionen." Date range on the record:
1700-tal - 1800-tal. QUEUE.md row R9, flagged there as "contribution (caution)" — a collection of cipher-system
*descriptions*, not a specific enciphered text to read.

This brief's specific question was: (1) is the Gripenstierna cipher-machine material already published
(Swedish cryptologic history), and (2) does the folder hold keys usable for other rows in this batch. No
ciphertext transcription applies to this item at all — it is a collection about cipher systems, not itself an
uncracked cipher — so `ciphertext.txt` is not created and no cryptanalytic search log applies.

## Check-solved sweep, 24 September 2026

1. **Web — is Gripenstierna's machine already published?** WebSearch `"Gripenstierna 1786 chiffermaskin cipher
   machine proposal Sweden"`. **Found, published, twice over:**
   - Bengt Beckman, *"The world's first encryption machine – Gripenstiernas cipher-Machine 1786"*, National
     Defense Radio Establishment (FRA), Bromma, 1999.
   - Bengt Beckman, *"An Early Cipher Device: Fredrik Gripenstierna's Machine"*, **Cryptologia**, vol. 26, no. 2
     (2002), doi/publisher page `tandfonline.com/doi/abs/10.1080/0161-110291890821` (abstract page returned
     HTTP 403 to WebFetch — paywalled journal article, not re-fetched past that block, per the good-citizen
     rule; the title, author, journal, volume and issue are confirmed from the search result itself and from
     multiple independent citing pages below).
   - The search snippet itself states the mechanism: 57 disks substituting letters (entered by a cleared
     official) for numbers (visible to a clerk) — a description consistent with, and evidently drawn from, the
     same archival material this Riksarkivet record holds.
   - Corroborating mentions found in the same pass: Wikipedia's "Cryptograph" and "Jefferson disk" articles both
     credit Gripenstierna's 1786 device as an early/first prototype of the disk-cipher principle; a July 2026
     Hackaday post "Encryption In The 1790s" also covers it.
   - Hans Högman's Swedish-military-history page (`hhogman.se/crypto-dept.htm`) and Bengt Beckman's own
     Wikipedia page were not read in full this pass but were surfaced as further citing sources; not needed to
     establish the core finding (published) at the confidence this check-solved pass requires.
2. **Print.** Covered by (1): the machine itself is the subject of a specialist report (FRA, 1999) and a
   peer-reviewed journal article (Cryptologia, 2002), both squarely "Swedish cryptologic history" in the sense
   the brief asked about. No further print search run.
3. **Lists.** `sources/cryptiana/` grepped for `gripenstierna|chiffermaskin`: no hits (Cryptiana's list is
   built around unsolved diplomatic/private ciphers, not published cipher-machine history, so this is expected
   and not informative either way).
4. **DECODE.** `sources/decode/` grepped for the same terms: no hits. Live de-crypt.org not queried (this item
   is not a ciphertext DECODE would catalogue).
5. **Bourdeau/Aymeloglu.** Fresh shallow clones (shared with the rest of this batch). `grep -n -i -E
   "gripenstierna|chiffermaskin"` against both repos, full-repo: zero matches anywhere, catalogue files or data
   files. Neither project references this material.

**Riksarkivet digitisation check** (`data.riksarkivet.se/api/records`, `text=Gripenstierna chiffermaskin`, one
request): confirms `SE/RA/221/2210.01.1/F/F 5/F 5 C/7` with `"onlyDigitisedMaterials":false` and reproduces the
catalogue note verbatim, including its own cross-reference: "Jfr. vidare samlingen Chifferklaver" (compare
further the Chifferklaver collection) — the same collection QUEUE.md's own scout note already identifies as
Bourdeau's/DECODE's ground (`riksarkivet1628`, `goertz1717`, `baner1640`), reinforcing that this folder sits
administratively adjacent to already-worked territory. Not digitised.

## Whether this folder holds keys usable for other R rows (R5, R6, R8)

Not established, and unlikely on the evidence available. This is a Utrikesdepartementet (Foreign Ministry)
collection of cipher-system *descriptions and key receipts* ("kvitton på mottagna chiffernycklar"), i.e. UD's
own administrative record of cipher-key issuance to its own diplomatic posts — the same institutional lineage as
QUEUE.md's own R1/R2 rows (Celsing family, Beskickningsarkivet, each already noted as carrying "chiffernyckel"
in their own folder). R5 (Mörner/Esplunda, a private family archive with unsigned letters) and R6 (Crusenstolpe/
Ericsbergsarkivet, a private collector's papers about 1809) are both outside the UD fonds entirely and have no
plausible institutional link to this folder. R8 (Karl XI's 1677 full power, Kungl. Majestäts kansli /
originaltraktater) predates the Utrikesdepartementet as an institution by over 150 years (UD's own record here
gives its provenance as 1840-, with a Kabinettet för utrikes brevväxlingen predecessor from 1791) and is
likewise institutionally unconnected. No key-sharing relationship established; this remains a Gripenstierna-era
UD administrative folder only, not a resource for the other three targets in this batch.

## Verdict

**Closed-negative — not a cryptanalysis or recovery candidate, confirmed.** QUEUE.md's own caution
("not a cryptanalysis/recovery candidate... flagged for the contribution lane only") is correct and now
verified: the one specific, nameable item in this folder (Gripenstierna's 1786 cipher machine) already has a
dedicated published treatment, both a specialist report (Beckman/FRA 1999) and a peer-reviewed article (Beckman,
Cryptologia 2002). The remaining contents of the folder ("beskrivningar av chiffersystem under 1700- och
1800-tal, kvitton på mottagna chiffernycklar") are administrative UD records, the same class QUEUE.md's own R4
row excludes elsewhere in this batch as already covered by Beckman's and Åsebo's published historiography of
Swedish 20th-century cryptology — the 18th/19th-century version of the same pattern. No ROOM `nomination:` line
is appropriate for this row (it does not verify "unsolved" because it is not a cipher-to-solve in the first
place); left off the board.

Not digitised (would need a copy order if anyone wants the Gripenstierna correspondence itself for a
history-of-technology write-up, not for cryptanalysis — REQUEST.md is not drafted, since no one asked for this
material and rule 10 wording does not apply to a target that is not being claimed as unpublished).

Requests this pass: data.riksarkivet.se 1 (shared batch count), WebSearch 1, WebFetch 1 (403, not retried),
github.com clones shared with batch. No Google Books, no TNA, no DECODE login.
