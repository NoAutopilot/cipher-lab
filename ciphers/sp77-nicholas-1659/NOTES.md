open
*The Nicholas Papers* vol. 4 (Camden 3rd ser. 31, IA `publications31royauoft`), CSP Domestic 1659-60 (Green, IA `sim_great-britain-public-record-papers-domestic-commonwealth_1659-1660`) and *Calendar of the Clarendon State Papers* vol. 4 (IA `calendarofclaren04bodluoft`), each grepped whole by this worker 3 Oct 2026 for Sebastian/Fuentarabia, 'L. R.' and 6/16 Aug 1659 and read at the August 1659 entries (Nicholas Papers iv pp. 175-181; CSPD 1659-60 pp. 78-82; Cal. Clar. iv pp. 309-322): no Nicholas letter to St Sebastian of 6/16 Aug 1659 is printed or calendared; the nearest is CSPD's '[Sec. Nicholas] to M. de Marces' of [6-7 Aug.], a different addressee (an earlier CSPD 1659-60 entry addresses him '[Sec. Nicholas] to M. de Marces, Palais Royal, Paris').

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

## NX-UNBLOCK (26 Sept 2026)

Free-route pass per CLAUDE.md's NX-UNBLOCK brief: checked TNA's current record-copying fee page
(`nationalarchives.gov.uk/help-with-your-research/record-copying/fees/`, read 19:01 UTC 26 Sept 2026 --
page check £9.92/record, digital copy up to A3 £1.52/copy) and tried the TNA Discovery search API for a
fresh digitisation check (`discovery.nationalarchives.gov.uk/API/search/records?sps.searchQuery=...`); it
returned HTTP 500, not retried per the good-citizen single-retry rule. No new free scan or edition found for
this item this pass; digitisation status stands as already recorded in this folder's REQUEST.md. This item
is now item in the consolidated order `outreach/tna-page-copy-batch.md` (ASKS row 73, status backlog) rather
than a standalone TNA order.

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: a TNA page-copy order for SP 77/32/289 (REQUEST.md, since 24 Sept 2026, now folded into the
consolidated TNA batch, ASKS row 73).

- S: search BL's catalogue (searcharchives.bl.uk?format=json, live per the playbook even though BL's IIIF images are dead) for Egerton MS 2550's full contents list, for a key entry under 'Sir L.R.'/'San Sebastian'.
- S: re-search Nicholas Papers vol. 4 (already fetched) for 'Flanders' or another correspondent term, beyond only 'Sebastian'/'L.R.'/'cipher' tried so far.
- S: re-verify sp105-paget-1693's 'no Interregnum cipher table in SP 106' finding against SP 77/32's own siblings for a companion key filed elsewhere, not independently re-checked this pass.

## Web and blog check (GF4-BATCH7 (account-4), 3 Oct 2026)

Plain web searches (WebSearch): `Edward Nicholas 1659 cipher Flanders`, domain-restricted to the three blogs --
**Cipherbrain** (scienceblogs.de/klausis-krypto-kolumne): no hit; **Cipher Mysteries** (ciphermysteries.com): only the
fifteenth-century-cryptography and Dorabella pages; **Cryptiana blog** (cryptiana.blogspot.com and Tomokiyo's
cryptiana.web.fc2.com): no hit. A combined query naming the blogs (`site:cryptiana.blogspot.com Lockhart OR Roe OR
Nicholas OR Thurloe cipher 1638 1657 1659`) returned Wikipedia (Sealed Knot, Thurloe), a Camden Third Series preface on
Cambridge Core and TNA catalogue pages, none naming SP 77/32/289. Earlier sweep (24 Sept 2026): `Nicholas "San Sebastian"
cipher 1659 "SP 77/32"`, `"Nicholas cipher" "Sir L.R."`, `"St. Sebastian" cipher Nicholas 1659 Flanders` -- Bourdeau's
Boswell 1643 page (a different letter) and nothing on this item. No comment thread found that discusses it. Solver
repositories re-cloned shallow 3 Oct 2026 and grepped (`SP ?77/3[0-9]`, `Nicholas`): Bourdeau's `targets/ormonde/NOTES.md`
cites a Nicholas-to-Ormond 1644 letter with interlinear decipherment (different letter, different year), Aymeloglu's
`royalist-1646/README.md` cites the King's 1646 letters to Nicholas -- neither is this item.

## Premise check (GF4-BATCH7 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment or key: **found, not this item** -- Warner's note (Nicholas Papers iv
introduction) that keys survive in BL Egerton MS 2550 (ff. 24, 78) for other correspondents; no decipherment of f.289 is
mentioned anywhere in the folder. (b) Other solvers' working files: **not found** (the Ormond 1644 and royalist 1646
folders above concern other letters; no key run on this text). (c) Physical neighbours: **unreachable** -- SP 77/32/289
is `digitised: false` (Discovery C7970624); the piece's term-sweep (24 Sept) found no other cipher or decipher item in
SP 77/32. (d) Recipient side: **not found** -- the St Sebastian end (Bennet at Fuentarabia, Holder at St Sebastian,
writing to Hyde) is calendared in Cal. Clar. iv pp. 309-322 for Aug 1659 with no Nicholas letter of 6/16 Aug and no "L.R.";
the intercepted royalist "French correspondence" in CSPD 1659-60 (SP 18/204) carries Nicholas's and Hyde's letters to
Marces for the same week (pp. 80-82; Hyde's has "Italics in cypher, undecyphered"), not this one. Status unchanged: open.

## While waiting (3 Oct 2026, GF4-BATCH7)

Waits on: the TNA page copy of SP 77/32/289 (REQUEST.md; consolidated TNA batch, ASKS row 73).

- S: grep CSPD 1659-60's index and Cal. Clar. iv's index (both already fetchable from IA) for royalist aliases and agents at St Sebastian in Aug 1659 (Holder, Bennet, Peter Wilson's house) to identify "Sir L.R.", ~$1.

Requests this pass (shared with the sibling targets where noted): archive.org 5 (advancedsearch 2, djvu.txt 3),
github.com 2 shallow clones (shared), WebSearch 2 for this target.

## Index grep for St Sebastian agents and aliases (R7-NICH, 6 Oct 2026)

Step run: the 3 Oct "While waiting" item. Texts fetched once from IA (`_djvu.txt`) and grepped by script: Cal. Clar. iv (`calendarofclaren04bodluoft`) and CSPD 1659-60 (`sim_great-britain-public-record-papers-domestic-commonwealth_1659-1660`). Search terms: Sebastian, Fuentarabia/Fontarabia, Holder, Wilson, Talbot, Marces, "L. R."/"Sir L.", Nicholas (Aug 1659 window).

Found (none is a plaintext of f.289, so no crib):
- CSPD 1659-60 SP 18/204 (Aug 1659): Col. Bamfield writes to "M. D'Arquibol, alias Father Talbot, at Peter Wilson's, St. Sebastian's" and to "Peter Wilson, alias Father Talbot" (Wilson is a cover name for Peter Talbot; the house is a royalist forwarding address at St Sebastian). The index lists "St. Sebastian's, Spain" at pp. 57, 65, 126, 446, 457, 558; "News of letters from" pp. 82, 126.
- Cal. Clar. iv: Thomas Holder is the agent at St Sebastian forwarding Bennet's letters (Sept-Oct 1659 entries); Bennet to Hyde from Fuentarabia nos. 3-8 (2/12-27 Aug/6 Sept), Bennet's no. 4 of 5/15 Aug says Talbot arrived at Fuentarabia two days before. Nicholas to Marces 13/23 Aug is cited in Cal. Clar. iv's introduction (p. xxxvi region, line 461 of the djvu text).
- Candidate recipients for "Sir L.R." at St Sebastian: none located. No "Sir L.R.", "L. R." or a knight with those initials appears in either index or the Aug 1659 entries; the St Sebastian residents named are Holder, Talbot (alias Wilson/D'Arquibol), Bennet (at Fuentarabia). "L.R." may be a cipher alias or the catalogue's own initialism; unresolved.

Not found: any Nicholas letter to St Sebastian dated 6/16 Aug in either calendar; any named "Sir L.R."; any key naming him. Status unchanged: open. Next step stays the TNA page copy of SP 77/32/289 (ASKS row 73); a cheap further step is reading Bennet's own Aug 1659 letters (Cal. Clar. iv pp. 310-316) for "Sir L." as a cover name, not run here.

Requests this pass: archive.org 2 (djvu.txt), no other host.
