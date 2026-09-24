# Beltrame Costabili (Esztergom) to Eleonora d'Aragona, 20 March 1492, State Archives of Modena, Amb. Ung. b.2/21 no.8

**Status: partial** (per DECODE's own status field — see below; extent of the existing partial decipherment
not confirmed this pass).

## Item

DECODE R1168. Metadata (Aymeloglu `decode-records.jsonl`): author Beltrame Costabili, receiver Eleonora
d'Aragona (Duchess of Ferrara, Modena and Reggio, consort of Ercole I d'Este), origin Esztergom, Hungary,
20 March 1492, 4 pages, cleartext Italian, cipher type "Homophonic or simple substitution", symbol set
graphic signs. **DECODE's own `Status` field for this record is "Partially decrypted", not "Non-decrypted".**

QUEUE.md row **DC10** placed this in the "DECODE non-decrypted records with images" section (which pools both
Non-decrypted and Partially-decrypted rows from the underlying crawl, per `sources/decode/NOTES.md`'s "What
was fetched" section) and scored it `held_by: none`, next step "transcription", framed only by its membership
in the same Este/Sforza envoy-report cluster as R1162 (an attached-`[transc]` record, DC4, handled by another
worker this session). The "partially decrypted" status itself was not surfaced or acted on at the ranking
stage.

Brief: `.claude/briefs/runs/2026-09-24-lane-n-csDC2.md`. de-crypt.org and archive.org not queried directly by
this worker (held by other LANE N workers this session); this verdict rests on the census-diff TSV's own
`status` column plus two WebSearches and a check of the local Cryptiana snapshot, since DocumentsList (the
DECODE page that would show what, if anything, is attached as a partial reading) could not be checked under
this brief's host restrictions.

## Check-solved sweep, 24 September 2026

- **Editions first.** Este ambassador editions for Hungary in this period (the brief names these for the
  Ferrara/Modena 1492 cluster): not located or checked this pass. Two WebSearches
  (`Beltrame Costabili Eleonora d'Aragona 1492 cifra Modena ambasciatori Ungheria`; `"Costabili" Modena
  archivio cifrario Ungheria 1492 decifrato`) surfaced general context (Costabili was one of several agents
  reporting from Hungary to the Este court in this period; a 26 Sept 1489 letter of his from Buda is
  documented) and a general Modena-archive page on "Lettere e cifrari" at the Este court, but **no specific
  mention of this letter (20 March 1492) or its cipher, solved or not**, and no confirmation either way.
- **Web / lists (Cryptiana).** No page in the local `sources/cryptiana/` snapshot mentions "Costabili",
  "Eleonora" (in this Hungarian-ambassador sense) or this shelfmark (checked by grep across `web/`, `blog/`,
  `PAPERS.tsv`, `READABLE.tsv`); not separately searched live beyond the two WebSearches above.
- **Bourdeau (github.com/dbourdeau/cyphersolver).** No file matches "Costabili", "b.2/21" or "R1168"
  specifically (broad substring greps on "1168" alone returned only unrelated false positives — numeric
  substrings inside unrelated JSON/TSV files, checked and dismissed). The repo's Este/Sforza-cluster work
  (`sadoleto1482/`, `buda1489/`) covers a different correspondent (Nicolo Sadoleto) and different box
  (Ambasciatori b.1/9), not b.2/21.
- **Aymeloglu (github.com/aaymeloglu/unsolved-ciphers).** R1168 appears in `catalogue/decode-ranked.md`,
  `decode-records.jsonl` and `decode-catalog.csv` — raw catalogue-harvest presence only, matching this
  project's own census-diff finding; no independent write-up or attempt found.
- **DECODE.** Not queried live (per brief). The census diff's own `status` column, already committed to this
  repo (`records-non-decrypted-2026-09-24-diff.tsv`), reads **"Partially decrypted"** for id 1168 — this is
  DECODE's own catalogue signal that some prior work exists on this record (a partial key, a partial reading,
  or a partially-completed transcription attached via DocumentsList), which none of this pass's other five
  sources independently corroborated or could explain further. This is the single most important fact this
  check-solved pass surfaced and it was not checked by anyone assembling QUEUE.md's DC10 row.

**Verdict: partial**, called directly from DECODE's own status field, not independently confirmed. This is
**not** the same as "open" and this record should not be nominated to the board as an open cryptanalysis or
recovery lead until a worker with DECODE access (a) confirms what "Partially decrypted" refers to via
DocumentsList / RecordsView, and (b) reports what portion is already read and by whom. No novelty claim made
(rule 10).

## Correction to QUEUE.md

DC10 (and, by the same logic, any other row in that section whose underlying `status` column in
`records-non-decrypted-2026-09-24-diff.tsv` reads "Partially decrypted" rather than "Non-decrypted") should
carry an explicit flag distinguishing the two statuses; the ranking pass pooled them without surfacing which
rows already carry DECODE's own partial-work signal. Flagged in ROOM.md, 24 Sept 2026, for the LANE N
orchestrator to re-check the rest of the DC1-DC20 list against the `status` column for the same issue.
