open

Read by this worker, 25 Sept 2026: the item's own three images (m0112 the plaintext cover letter; m0113-m0114 the
cipher draft, with the plaintext syllable written directly above almost every number) -- no printed edition or
calendar applies, since this is an unpublished archival draft, not a letter in a print series. Full-text search
(be-api.us.archive.org/fts/v1/search, 0 hits for `"Costa Cabral" "Conde d'Avila" 1865 cifrada`; advancedsearch.php
by title+date range, 0 items) and Google Books (`GOOGLE_BOOKS_KEY`, 0/300 relevant hits across `"Costa Cabral"
"Conde d'Ávila" 1865 carta cifrada`, `"Caetano de Magalhães" 1865 Padroado`, `"Costa Cabral" correspondencia 1865`;
the 300-hit query returned only unrelated catalogues and an unrelated Fonseca Magalhães correspondence volume)
found no prior print or decipherment. BNP bndigital's `?q=` search parameter does not restrict results (every
query, including this one, returned "51732 Resultados" -- the whole catalogue, the same non-functional-search-box
shape CLAUDE.md's Access playbook already logs for the Huntington CONTENTdm naive query -- so this route is logged
as unreachable, not read as a negative). DECODE's public RecordsList crawled in full and login-free
(`tools/decode_list.py --status non-decrypted,partially-decrypted,decrypted,n/a --record-type cipher`, 2897 cipher
records to `/tmp/decode-costacabral-check.tsv`, not committed since it is a general catalogue snapshot not specific
to this item) has no Costa Cabral or FCC row. Web search (Portuguese and English) for the letter, the correspondents
(Caetano de Magalhães, Conde d'Ávila) and the 1865 Padroado/Santa Sé negotiation found nothing specific to this item
-- only unrelated Costa Cabral family letters and 20th-century ambassador lists. Cryptiana and Cipherbrain checked
by web search (`cryptiana OR cipherbrain "Costa Cabral" OR "FCC" Torre do Tombo cipher`), no hit. Both solver
repositories grepped (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`, depth-1 clones 25 Sept 2026,
`grep -ril -i "costa cabral\|FCC/001/0021\|costacabral"`), zero hits in either. No calendar or state-paper series
applies to a private family-fonds draft with no independent print history, so this check-solved sweep is over the
item and its correspondents, not a datable letter in a numbered series.

## The unit

ANTT `PT/TT/FCC/001/0021/00026` -- fonds Família Costa Cabral, sub-fonds "Documentação pertencente a António
Bernardo da Costa Cabral -- correspondência de várias pessoas sobre assuntos políticos". Viewer:
`https://digitarq.arquivos.pt/fileViewer/b482fac086d54e2bae791264bb78b79f` (docId
`b482fac086d54e2bae791264bb78b79f`), CC BY-SA 4.0, no login. Catalogue note: "Inclui um rascunho de uma cópia de
carta cifrada: (...) pa-pa (419-419), di-ga-mo (926-923-1212) [...]". Scouted by scDIGI2 (LANE N4, 24 Sept 2026,
ROOM.md 21:26) via DigitArq unit-description search; re-fetched full-resolution here with `tools/digitarq_fetch.py`
(3 requests, `--list` + `--full`, >=3 s apart, no retries needed).

3-image item, all now on disk at `images/full_PT-TT-FCC-001-0021-00026_m01{12,13,14}.jpg.jpg` with
`images/filelist.json` (ids 13958080-13958082, one `representationID`):

- **m0112**: plaintext (Portuguese, H grade -- read directly off the image), headed "Reservadíssimo" and "1865",
  addressed "Meo Caro Conde". Body: the Secretaria writes on behalf of the ill Foreign Minister, the Conde d'Ávila,
  about a matter needing "grande segredo e reserva". It refers to a letter from "Sua Santidade" (the Pope) whose
  reply goes with the official dispatch; that reply had been left with the former minister, the Duque de Loulé, and
  never reached the Secretaria. The recipient ("Conde") is asked to obtain, with the greatest discretion and
  without the Pontifical government suspecting the reason, a copy of the Pope's letter, and to forward it to the
  Minister as "um bom serviço e um obséquio especial" -- an unrelated-to-cipher but historically dense item: a
  covert Portugal-Vatican channel over what appears to be a stalled or missing papal communication during the
  Padroado dispute, 8 July 1865, signed "Secretaria, 8 Julho 1865, Caetano de Magalhães" (the sender), self-
  described as a friend "dos bellos tempos de Coimbra" (of the old Coimbra days) -- i.e. an old university friend
  of the addressee, not a formal diplomatic register between strangers.
- **m0113-m0114**: the cipher draft itself (H grade for the plaintext syllables, read directly off the image; the
  numeric groups are the ciphertext, transcription not attempted this pass -- out of this brief's scope). A
  4-digit-max nomenclator worksheet: the plaintext syllable or short word is written directly above almost every
  number, e.g. "con-fi-dev-ci-ar" / "99-629-737-20-428", "el-Rei-de-se-ja" / "903-342-456-103-870",
  "pa-dri-nho-do-prin-ci" / "419-135-151-25-204-20" (m0113), "sou-ber-al-ge-ma" / "618-323-428-2111-742",
  "as-elo-pa-pa-di-ga-mo" / "12-25-419-619-926-923-1212" (m0114, matching the catalogue's quoted
  "di-ga-mo (926-923-1212)" and "pa-pa (419-419)" fragments). This is a self-glossed encoding worksheet -- the
  clerk's own scratch copy while enciphering, not a later, independent decipherment -- so it hands over roughly
  four to five dozen syllable/word-to-number pairs directly, several numbers repeating across lines (419, 617,
  988, 1087 each appear more than once, consistent with a fixed nomenclator rather than a one-time pad). Numbers
  observed range from two digits (e.g. 11, 12, 20, 25, 60) to four digits (max seen 2111, on "ge"); most syllables
  are 1-3 letters, with a few full short words ("Rei", "que", "de"). No independent ciphertext (a version without
  the interlined gloss) is visible on these three images -- the draft itself, gloss and numbers together, is all
  that was fetched. Two faint crosses ("+") mark two of the number groups on m0113, cause not established this
  pass.

## Next step (not this brief)

Per the brief, no key extraction this pass. The natural next step is a transcription of every syllable-number pair
into a `key.tsv` (recovery kind, key source `ours`: rebuilt from the clerk's own contemporary worksheet, not a
later or published key) -- this is a straightforward reading task, not cryptanalysis, since the plaintext is
already interlined; the harder part is confirming trim/joining rules where syllables run together across a line
break, and locating (or accepting the absence of) a "live" ciphertext-only copy of the same letter elsewhere in
this fonds to check the key against.
