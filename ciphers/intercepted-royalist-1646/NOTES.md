# Intercepted royalist letter (21 May 1646)

- **Source:** BL Add MS 72438, f.9r. DECODE record R8623. Tomokiyo believes it is undeciphered.
- **Status:** Open.
- **Transcription:** `ciphertext.txt` holds only the opening, as quoted on unsolved.htm. The full text must be transcribed from the DECODE image (R8623).
- **Related:** BL Add MS 72438 f.10 (DECODE R8624), an intercepted letter to Charles I of 13 May 1646, is also undeciphered and may share the cipher.
- **Ideas:** Mixed cleartext and one- to three-digit code groups. Highest seen so far 333. Cleartext anchors ("beholding to 309 for", "Messenger", "communicate") give word-class hints for the adjacent groups.
- **Solver status (19 Sept 2026):** Partial by Aymeloglu (unsolved-ciphers/royalist-1646), 16 Sept 2026. Note the folder covers two letters: f.10 (13 May, to Charles I) is Digby key no. 129 with about 45 values fixed; f.9 (21 May, the opening quoted here) uses a smaller key in which 226 = London. Needs the rest of key 129 or the contemporary decipher.

## Scout addition: f.104 and the volume's keys, 20 Sept 2026

A proposed fourth candidate (a separate letter, BL Add MS 72438 f.104, "almost wholly in undeciphered cipher")
was checked against this folder rather than filed as a new target, since it is the same volume. Findings, not
yet acted on:

- **The volume is Weckherlin's, not "Nicholas Papers":** BL catalogue title (searcharchives.bl.uk/catalog/040-001967027,
  checked 20 Sept 2026) is "Cipher-keys and intercepted royalist correspondence from the papers of Georg
  Rudolph Weckherlin, government official, 1625-1647." Digital images: "currently unavailable" (BL viewer
  offline since the 2023 cyber attack).
- **f.104 entry (verbatim, matching /tmp/cyphersolver/rupert/NOTES.md's own quote):** "f. 104r: Royalist
  intercepted letter almost wholly in undecoded cipher, n.d." No sender/date/recipient given in the catalogue,
  so no print-edition search was possible (nothing to search on). A second item, f.171r, is in the same
  state ("undecoded") per the same source but has no DECODE record in the harvested set below, so its coverage
  is unclear.
- **DECODE status conflict — do not treat f.104 as an open target without resolving this.** f.104 has its own
  DECODE record, **no. 8725** (https://de-crypt.org/decrypt-web/RecordsView/8725), confirmed by raw HTML:
  "Type: Cipher | Status: **Decrypted** | Cipher Type: Unknown | Symbol Sets: Numerical | Pages: 1 |
  Author/Sender/Receiver: blank | Access mode: Authentication required." This is the opposite of f.9 and f.10
  (DECODE records R8623/R8624), both explicitly "Non-decrypted" in the same harvested catalogue
  (`/tmp/unsolved-ciphers/catalogue/decode-catalog.csv`). Tomokiyo's unsolved.htm does not list f.104 at all
  (grepped `sources/cryptiana/web/unsolved.htm` for "72438" and "104": only f.9/R8623 and f.10/R8624 appear),
  which is consistent with DECODE marking it already solved rather than with Tomokiyo having simply missed a
  live target. Neither solver repository flags this DECODE status (Aymeloglu's `royalist-1646` folder never
  engaged with f.104 at all; Bourdeau's `rupert/NOTES.md` names the folio only from the archival "no
  contemporary decipherment survives" sense, not DECODE's project-status sense). **No DECODE credentials are
  available in this environment** (checked; `DECODE_USER`/`DECODE_PASS` unset), so record 8725's actual
  plaintext/decipherer could not be read. Resolve this — with a DECODE login — before requesting a physical
  copy of f.104 or including it in any campaign.
- **Keys in the volume**, extending the "49 captured Digby keys" figure already in `LANDSCAPE.md` (sourced from
  `/tmp/cyphersolver/TARGETS.md`): the index leaf f.25, "Cyphers taken in the Lord Digby's cabinet" (Sherburn,
  Oct 1645), numbers the captured keys roughly 80-139; surviving key pages run across ff.25/27-99 (not all 60
  numbered slots survive as separate leaves, which is where "49" comes from). Cross-checked independently in
  both the BL catalogue and Aymeloglu's own from-the-record research (`/tmp/unsolved-ciphers/royalist-1646/README.md`):
  f.27 = key no.84 (Bennet); f.52 = no.113 (Digby & Vavasour); f.70 = no.125 (Mr Browne, ~700-entry key);
  f.77 = no.129 (unnamed, "from the Queen's Court" — the key already in partial use on f.10 above); f.78 =
  no.130 (Col. Hurliston, syllabary); f.82 = no.132 (Sir Kenelm Digby). Beyond ff.25-99, the catalogue also
  lists cipher-key items at ff.100-101 (King & Queen), 102-103 (Digby/Walsingham), 105-106, 108-109
  (unidentified royalist keys — not yet matched to a name), then Weckherlin's own diplomatic cipher-books
  ff.110-170 (a different, unrelated haul: Latin cipher-book ff.124-141, Augier ff.151-158, Waller ff.162-163).
  f.104 itself is not catalogued as a key; it sits as the one non-key "intercepted letter" leaf between the
  f.102-103 and f.105-106 key items.
- Any of ff.100-101, 102-103, 105-106 or 108-109 ("unidentified royalist keys") could in principle be the rest
  of key no. 129 that f.10's reading still needs, or the key for f.9's smaller cipher — worth requesting
  alongside f.11 (already planned) once a DECODE login clarifies whether f.104 is actually open. See
  `REQUEST.md`.
