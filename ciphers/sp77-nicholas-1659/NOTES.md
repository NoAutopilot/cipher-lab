open

# Secretary of State Nicholas to Sir L.R. at San Sebastián, in cipher — TNA SP 77/32/289

QUEUE row: N52 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 77/32/289** (State Papers Foreign, Flanders), folio 289, 1659 Aug 6/16.
TNA Discovery record detail (fetched fresh, 24 Sept 2026, Discovery id C7970624): scope description "Folio
289: Nicholas to Sir L.R. at St. Sebastian - in cipher." `digitised: false`. Sir Edward Nicholas was Secretary
of State to the exiled Charles II at this date, corresponding on the eve of the Restoration. "Sir L.R." is
not otherwise identified in the catalogue text; not run to ground this pass (out of scope for a check-solved
sweep).

## Check-solved sweep (24 September 2026)

Six sources checked directly by this worker (Sonnet, no subagents — TNA Discovery and archive.org calls made
directly under this run's host list).

1. **TNA Discovery, siblings.** `tools/discovery_items.py "SP 77" "SP 77/32" cipher decipher key Nicholas
   Sebastian` returned one item matching "in cipher" in its description across the whole piece SP 77/32
   (which runs Dec 1657–Dec 1659, ~150 letters, nearly all to/from Nicholas): this target itself (C7970624).
   No sibling decipherment or key catalogued in the same piece. (9 API calls.)

2. **Editions.** *The Nicholas Papers* (Camden Society; identified on archive.org as vol. 4, `id
   publications31royauoft`, Camden 3rd series no. 31, covering the correspondence up to 1660) searched via
   archive.org be-api fts (no login): `Sebastian` → **0 hits**; `L.R.` → 0 hits (too short/common a token for
   fts to be meaningful, treated as a negative result only, not a clearance); `cipher` → 1 hit, quoted
   verbatim: "...and the **cipher** used (Egert. MS. 2550, f. 78) is endorsed by Nicholas 'Cipher with
   Col[...]'... adopted fictitious names and wrote largely in cipher. Nicholas calls his two principal
   correspondents... signed 'Tristram Thomas' or with the cipher 866... The key to the **cipher** used is in
   Egerton MS. 2550, f. 24." This is the editor's (G. F. Warner's) introductory note describing Nicholas's
   ciphering habits with *other* named correspondents in the 1650s and the location of surviving keys at the
   British Library, **Egerton MS. 2550** (ff. 24, 78) — background confirming Nicholas routinely used cipher
   and that some of his keys survive at the BL, but the volume does not name "Sir L.R." or "San Sebastian" or
   quote this specific letter's plaintext. A companion WebSearch hit (`dbourdeau.github.io/cyphersolver`)
   independently corroborates the same Egerton MS. 2550 material: it describes a *different*, already-solved
   Nicholas cipher letter (Charles I and Nicholas to Boswell, 1643, TNA SP 84/157, alphabet solved by R. Pitt
   Sept 2026, in `dbourdeau/cyphersolver`'s `boswell/` folder — see item 5) whose key is likewise cross-
   referenced to Egerton MS. 2550, f. 24, confirming this is a real, reusable key location for Nicholas's
   correspondence generally, but for a different addressee (the Duke of Courland's envoy, not "Sir L.R.") and
   a different year (1643, not 1659). **BL Egerton MS. 2550 is out of this lane's host list (no BL) — flagged
   as a lead for a BL-capable worker, not checked further this pass.**

3. **Community lists.** WebSearch `Nicholas "San Sebastian" cipher 1659 "SP 77/32"` surfaced Bourdeau's
   `cyphersolver` site (the Boswell item above, a different letter) and a Cambridge Core abstract page for
   "Correspondence of Sir Edward Nicholas" (Camden series listing, no full text) but nothing naming this
   specific item. No Cryptiana or Cipherbrain hit; local grep of `sources/cryptiana/` for "nicholas"/"san
   sebastian"/"sp 77/32" returned zero hits.

4. **DECODE (de-crypt.org).** No login attempted (known broken; out of this lane's host list regardless).
   `aaymeloglu/unsolved-ciphers`'s cached `catalogue/decode-catalog.csv` and `decode-records.jsonl` greped for
   "nicholas"/"sp 77/32"/"san sebastian": all "Nicholas" hits are unrelated BL Add MS 4136 (Throckmorton,
   1559–63) and BL Add MS 18982/32256 (1644–45) items — a different Nicholas correspondence altogether, none
   at TNA SP 77/32 or dated 1659. No DECODE record found for this item.

5. **Solver repositories.** Fresh shallow clones of both (24 Sept 2026, shared with the other three targets
   this pass). `dbourdeau/cyphersolver`: grep for "nicholas" finds the `boswell/` folder (Charles I and
   Nicholas to Boswell, 1643, TNA SP 84/157 — solved by R. Pitt Sept 2026, read in `boswell/NOTES.md`: a
   **different letter, different year, different addressee** — the folder's own README table (line 132) also
   lists a separate "Hyde's ciphered superscriptions, 1659–60" item, again a different correspondent
   (Hyde, not Nicholas) and different content (dummy numbers on superscriptions, not this letter's body).
   Neither is our target. No folder or README row for "SP 77/32" or "Sir L.R." `aaymeloglu/unsolved-ciphers`:
   grep of `TARGETS.md`, `SHORTLIST.md`, `catalogue/*` for "nicholas"/"sebastian"/"sp 77" returns nothing
   beyond the unrelated BL catalogue rows in item 4.

6. **General web search.** The query in item 3 above is the general web search; a second pass
   (`"Nicholas cipher" "Sir L.R."`, `"St. Sebastian" cipher Nicholas 1659 Flanders`) found nothing naming
   this letter's plaintext or key.

**Host requests this pass:** discovery.nationalarchives.gov.uk 10 (shared running total with the other three
targets, ≥3 s apart), archive.org 5 (1 advancedsearch + 4 be-api fts, ≥3 s apart), WebSearch 2, GitHub 2
shallow clones (shared with the other three targets).

## Verdict

**Status: open.** No printed edition of Nicholas's correspondence (the Camden Society's *Nicholas Papers*,
the standard source, checked for this exact date range) quotes this letter or names "Sir L.R." or "San
Sebastian"; no community list, DECODE cache, or either solver repository has this item. The editor's own note
that some of Nicholas's 1640s–50s cipher keys survive at BL Egerton MS. 2550 is a genuine lead (his household
evidently kept several distinct keys for different correspondents across the decade) but is **unverified for
this specific letter** — it names other correspondents (an unidentified "Col[...]", and separately the Duke of
Courland's envoy via Boswell) and is out of this lane's reach (no BL host). Separately: this letter predates
the Restoration (Aug 1659), and SP 106 (the Miscellaneous Ciphers class) is already established elsewhere in
this project (ciphers/sp105-paget-1693/NOTES.md, 24 Sept 2026 TNA sweep) to have **no cipher/decipher table
for the Interregnum/exile period at all** — its Charles II item (SP 106/6) begins only at the Restoration,
1660 May 29 — so a key for this 1659 letter, if it survives in a comparable series, would not be in SP 106
either; not independently re-verified this pass, cited from the prior sweep.

**Copy status:** `digitised: false` (Discovery API, confirmed directly). **TNA page-copy order** case for
f.289 — see REQUEST.md.

**Recommended next step:** a TNA page-copy order for f.289; separately, a BL-capable worker should check
Egerton MS. 2550 (ff. 24, 78 and its full contents list) for a key catalogued under "Sir L.R." or "San
Sebastian" specifically, since the manuscript is already established as a repository of Nicholas's cipher
keys for other correspondents — not chased this pass (no BL access on this lane).
