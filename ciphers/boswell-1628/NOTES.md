# Charles I to William Boswell (TNA SP 106/5, box 5, ff.20-21)

found-solved

- **Source:** The National Archives, State Papers, inv.nr. 106 box 5. DECODE record 413 ("TNA_SP106/5_CharlesI_(0020-0021)"),
  author King Charles I, receiver William Boswell (1585-1650), 2 pages, cleartext English and Latin.
- **Found-solved:** Woodard 2021 published a decipherment of this letter (per `ASKS.md` row 1 and the LANE DX
  orchestrator's 25 Sept 2026 00:44 UTC ROOM.md note); a solver reading here would be a re-derivation of known
  plaintext, so no cryptanalytic campaign is planned. This folder exists to hold the DECODE fetch below; the
  Woodard 2021 citation itself has not been independently verified from this account (no full text read, no
  page/edition pinned) — flagged as the next step if anyone wants to cite it precisely.

## DECODE fetch, 25 Sept 2026

LANE DX job 2 (the one DECODE login worker), one login shared with `ciphers/intercepted-royalist-1646` (record
8725) and `ciphers/randolph-sussex-1569`/`ciphers/bne20211-ferdinand-1478` (records 4930, 1172, 1180) —
`tools/decode_browser_login.js`, `--fetch-page /decrypt-web/RecordsView/413`, `--guess-fullsize`. Files saved
here (moved from the shared OUT_DIR after the run, since the script writes one directory per invocation),
account name scrubbed from the HTML.

**RecordsView/413 fields (real content):** ID 413, Name `TNA_SP106/5_CharlesI_(0020-0021)`, Country UK, City Kew
/ "The National Archives, State Papers, inv.nr. 106 box 5.", Author King Charles I, Receiver William Boswell
(1585-1650), Type Cipher, **Status: Non-decrypted** (DECODE's own project field — this is DECODE's internal
status, not a claim about whether the plaintext is known anywhere; Woodard 2021's decipherment, if confirmed,
would make this an N1/N2-class item per rule 10, not N3), Cipher Type Unknown, Symbol Sets Graphic signs, Pages 2,
Creation Date 2018-10-08, Access mode Authentication required, Cleartext English and Latin, Plaintext "probably
English too, but strictly speaking unknown" (DECODE's own field text).

| file | bytes | sha1 | content |
|---|---|---|---|
| record_413.html | 121569 | 98010e746365d01ab9b165f4d36a71d0cb0b2aec | real (RecordsView metadata, scrubbed) |
| TH_IMG_R413_I3496_P1.png | 82483 | 3e96cb4a564cfaa1bf6e3ad4d98800ac4b67913a | real thumbnail |
| TH_IMG_R413_I3497_P2.png | 82576 | b8dea00c8c9170c24ae73ee0a7dd4ce12c6799fa | real thumbnail |
| IMG_R413_I3496_P1.png, IMG_R413_I3497_P2.png | 17947 each | 035489a0605851154ab88372216354b63596ca22 | **placeholder** ("Insufficient permissions to see the full image") |
| DOC_413_2021-Nov-09-13-40-59_26606.pdf, DOC_413_2021-Nov-09-13-41-19_88471.pdf | 17947 each | 035489a0605851154ab88372216354b63596ca22 | **placeholder**, same sha1 — two attached documents exist (uploaded Nov 2021, consistent with the Woodard 2021 date) but this account cannot open them |

The Nov 2021 upload date on both attached documents is consistent with — but not proof of — the Woodard 2021
decipherment being the attachment; nobody has read the attachment's actual title or content from this account.
No novelty classification here (rule 10); this target is not a cryptanalysis candidate.
