open
*Calendar of State Papers, Domestic, James I, 1619-1623* (Green; archive.org `sim_great-britain-public-record-mary-elizabeth-i-and-james-i_1619-1623`, full text grepped whole by GF4-BATCH8 (account-4), 3 Oct 2026): read at its Sept 1621 entries, pp. 287-295 -- no Doncaster-to-Calvert letter, no cipher item; its index lists Doncaster's French embassy at pp. 276, 346, 362, 394, 425, 434, none this letter; its only 'partly in cipher' Doncaster item is at pp. 173-174 (Woodford to Nethersole, 1620). Birch, *Court and Times of James I* vol. 2 (IA `courttimesofjame02bircuoft`), read at July-Sept 1621, pp. 270-288: newsletters only (Doncaster leaves for France 3 Aug 1621, p. 272). No CSP Foreign calendar covers 1621. No printing of SP 78/69/91 or its f.222 cipher advertisement found.

# Doncaster (Viscount Doncaster, later Earl of Carlisle) to Calvert, with an advertisement in cipher enclosed — TNA SP 78/69/91

QUEUE row: N53 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 78/69/91** (State Papers Foreign, France), folio 214, 1621 Sept 24. TNA
Discovery record detail (fetched fresh, 24 Sept 2026, Discovery id C7322858): scope description "Folio 214:
Doncaster to Calvert - and duplicate, with advertisement in cipher (f.222)." `digitised: false`. James Hay,
Viscount Doncaster (created Earl of Carlisle in Sept 1622), was on a special embassy to France in 1621; Sir
George Calvert was Secretary of State in London. "Advertisement" here means an intelligence report/notice,
enclosed in cipher with the duplicate of this letter.

## Check-solved sweep (24 September 2026) — includes a candidate key sibling

Six sources checked directly by this worker (Sonnet, no subagents — TNA Discovery and archive.org calls made
directly under this run's host list).

1. **TNA Discovery, siblings — candidate key found.** `tools/discovery_items.py "SP 78" "SP 78/69" cipher
   advertisement Calvert Doncaster` returned the whole run of the piece's Doncaster/Calvert correspondence for
   1621. Three items stand out as directly cipher-related, all close to the target in foliation and all from
   the same July 1621 preparation for Doncaster's embassy:
   - **SP 78/69/56** (f.142, C7322823, 20 July 1621): "Directions for the letters sent by Viscount Doncaster
     to France."
   - **SP 78/69/58** (f.144, C7322825, [July 1621]): **"French titles for the cipher."** Full record detail
     fetched (`digitised: false`, `note: None`, held by TNA only) — this is the strongest candidate for a
     **key catalogued right beside the letters it was issued for**: a cipher-titles sheet, filed two folios
     after the "Directions" item and 70 folios before this target's f.214, all within the same July–September
     1621 sequence covering Doncaster's outgoing embassy. Not confirmed as *the* key for f.214/222 specifically
     (no image seen; "French titles" could be a set of code-names/titles for correspondents rather than a full
     substitution table) — a lead for an access worker to check first, before any transcription or copy order
     is placed for f.214/222 alone.
   - **SP 78/69/59** (f.146, C7322826, [July 1621]): "List of French letters for Doncaster" — likely a related
     administrative list, not itself a key, but filed in the same short run.
   All three of f.142/144/146 are `digitised: false` (confirmed by fetching f.144's full record; f.142/146 not
   individually re-confirmed but same piece, same digitisation regime). No other item in the piece's ~150
   entries matched "cipher" in its description besides these and the target itself. (10 API calls: 5-term
   `discovery_items.py` search + one record-detail fetch for f.144 + one record-detail fetch for the target
   f.214, C7322858.)

2. **Editions.** No specialist printed edition of Doncaster/Carlisle's or Calvert's 1621 correspondence was
   identified by search this pass (Calvert's own papers are not in a single printed edition comparable to
   Christie's Shaftesbury or the Camden Nicholas Papers). *Calendar of State Papers, Domestic, James I,
   1619–1623* (archive.org `calendarofstatep0000mary_l0t0`) searched via be-api fts (no login): `Doncaster` →
   1 hit with several snippets, all about **domestic** matters (his embassy preparations generally, honours,
   a Treasurer/Chamberlain appointment rumour) — none mentions Calvert, an advertisement, or cipher.
   `advertisement in cipher` (exact phrase) → **0 hits**. CSPD does not calendar SP 78 (Foreign, France)
   content directly, so this negative is expected rather than informative; there is no continuously published
   CSP Foreign series for James I's reign covering 1621 (unlike CSPD), so no Foreign-series calendar exists to
   check by the same method. Google Books is out of this lane's host list.

3. **Community lists.** WebSearch `Doncaster Calvert 1621 cipher "advertisement" "SP 78/69"` surfaced only
   TNA Discovery's own catalogue page for a neighbouring item (SP 78/69/136, a different Doncaster-to-Calvert
   letter later the same year) and unrelated results (British History Online's CSP Venice index, an unrelated
   pipe-maker's list, a Springer chapter on "Cipher Mysteries" with no specific match). No Cryptiana or
   Cipherbrain hit; local grep of `sources/cryptiana/` for "doncaster"/"calvert"/"sp 78/69" returned zero
   hits.

4. **DECODE (de-crypt.org).** No login attempted (known broken; out of this lane's host list regardless).
   `aaymeloglu/unsolved-ciphers`'s cached `catalogue/decode-catalog.csv` and `decode-records.jsonl` greped for
   "doncaster"/"calvert"/"carlisle"/"sp 78/69": zero hits. No DECODE record found for this item.

5. **Solver repositories.** Fresh shallow clones of both (24 Sept 2026, shared with the other three targets
   this pass). `dbourdeau/cyphersolver`: grep for "doncaster"/"calvert"/"carlisle" across the tree (excluding
   images) returns nothing; no target folder, no README row. `aaymeloglu/unsolved-ciphers`: grep of
   `TARGETS.md`, `SHORTLIST.md`, `catalogue/*` for the same terms returns nothing. Neither repository has
   touched this item or its candidate key sibling.

6. **General web search.** The query in item 3 above is the general web search; a second pass
   (`"Viscount Doncaster" cipher France 1621`, `"French titles for the cipher" 1621 SP 78`) found nothing
   naming this letter, its enclosure, or the f.144 titles sheet.

**Host requests this pass:** discovery.nationalarchives.gov.uk 12 (shared running total with the other three
targets, ≥3 s apart; the highest of the four targets, owing to the sibling search), archive.org 2 (fts only,
no advancedsearch needed — the CSPD identifier was already known from the N53 row's own suggestion),
WebSearch 2, GitHub 2 shallow clones (shared with the other three targets).

## Verdict

**Status: open.** No printed edition, community list, DECODE cache, or either solver repository names this
letter, its cipher enclosure, or a decipherment. The one substantive finding is the **candidate key sibling
at SP 78/69/58 (f.144, "French titles for the cipher")**, filed in the same piece within the same July–
September 1621 sequence that produced this letter's enclosure — this is exactly the "the key was in the
archive beside the letter" pattern LESSONS.md flags as the single most productive route to a real break, and
it should be the first thing an access worker checks (by copy or image) before assuming this is a
ciphertext-only target. Nothing here confirms f.144 *is* the operative key for f.214/222 specifically; that
can only be settled by looking at both.

**Copy status:** target and all three candidate-sibling items `digitised: false` (Discovery API, confirmed
directly for f.214 and f.144; f.142/f.146 same piece, same regime, not individually re-confirmed).
**TNA page-copy order** case — see REQUEST.md, which asks for f.214/222 (the letter and its cipher enclosure)
**and** f.142/144/146 (the candidate key run) together, since ordering them separately would double the
archive's per-item handling for what is very likely one research question.

**Recommended next step:** a single TNA page-copy order covering f.142, f.144, f.146, f.214 and f.222; if
f.144's "French titles" turns out to be a real substitution/nomenclator key, this converts from a
cryptanalysis candidate to a recovery (key-in-archive) target immediately on receipt of the copy.

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

Waits on: a single TNA page-copy order covering f.142, f.144, f.146, f.214 and f.222 (REQUEST.md, since 24
Sept 2026, now folded into the consolidated TNA batch, ASKS row 73).

- S: fetch full record detail (note field) for SP 78/69/56 (f.142) and /59 (f.146) individually -- only f.144's note was checked this pass -- tools/discovery_items.py.
- S: search TNA Discovery broadly for other 'French titles for the cipher'-style key sheets from the same 1621 embassy-preparation clerks, to gauge what such a sheet typically contains before assuming f.144 is the operative key.
- S: search Calvert's later CSPD entries for a retrospective mention of this cipher/advertisement; only the pre-embassy hits were searched this pass.

## Web and blog check (GF4-BATCH8 (account-4), 3 Oct 2026)

WebSearch, 3 Oct 2026: (1) `Doncaster Calvert 1621 cipher advertisement "French titles" Hay embassy France` -- the SSNE biography of
James Hay, Wikipedia, a Folger ambassadors list, BHO's CSP Venice vol. 17 index page, the TNA blog post on an undeciphered Louis XIV
letter (a different item); nothing on this letter or f.144/f.222. (2) site-restricted to the three blogs, `Doncaster 1621 cipher` on
**Cipherbrain** (scienceblogs.de/klausis-krypto-kolumne), the **Cryptiana blog** (cryptiana.blogspot.com) and **Cipher Mysteries**
(ciphermysteries.com): only those blogs' front pages and unrelated posts (Blitz ciphers, Dorabella); no post or comment thread names
Doncaster, Calvert or SP 78/69. Solver repositories re-cloned shallow 3 Oct 2026 and grepped (`doncaster|SP ?78/69`): zero hits in
Bourdeau's and in Aymeloglu's repository.

## Premise check (GF4-BATCH8 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment: **found, not a decipherment** -- NOTES.md names SP 78/69/58 (f.144, July 1621) "French
titles for the cipher", a candidate key sheet in the same piece, and /56 "Directions for the letters", /59 "List of French letters";
all `digitised: false`, so none could be opened; none is described as a decipherment of f.222. (b) Other solvers' working files:
**not found** -- no Doncaster folder, key or rendering in either solver repository. (c) Physical neighbours: **unreachable** -- f.214
and its duplicate with the f.222 enclosure are `digitised: false` (Discovery C7322858); the piece-wide term sweep (24 Sept) found no
decipher item beside f.214-222. (d) Recipient's side: **not found** -- Calvert's office papers are what CSPD calendars, and its Sept
1621 entries (pp. 287-295) hold no copy or decipherment of the advertisement; the sender's own papers (BL Egerton, Hay/Carlisle)
sit at the British Library, offline since 2023 (LESSONS.md), so are unreachable from here. Item stays `open`.

## While waiting (3 Oct 2026, GF4-BATCH8)

Waits on: the TNA page copy of f.142/144/146/214/222 (ASKS row 73, batch order).

- S: grep CSP Venice vol. 17 (1621-1623; BHO or archive.org full text) for the Venetian ambassador's reports of Doncaster's Sept 1621 audiences, a free crib source for the advertisement's subject -- no person needed.

## CSP Venice vol. 17 grep (R7-DONC, 6 Oct 2026, for LANE LANE-RUN7-account-2)

Source: *Calendar of State Papers ... Venice*, vol. 17, 1621-1623, ed. Hinds (1911), BHO full text (index page + four chapters: Aug 1-14 pp. 96-110,
Aug 16-30 pp. 110-120, Sept pp. 120-139, Oct pp. 139-156; archive.org has no vol. 17 item in advancedsearch -- 3 queries, identifier guesses returned empty metadata).
Grep: doncaster|hay|cipher|cypher|advertis|calvert. Requests: british-history.ac.uk 5, archive.org 7 (search + metadata), all >= 1.5 s apart, no 4xx/challenge.

Found (calendar summaries only; none of them a report of an audience on or near 24 Sept 1621, none mentions a cipher advertisement):
- 7 Aug (no. 126, Priuli, Paris): Doncaster arrived, visited by Priuli; says he comes to bring peace in France.
- 7 Sept (no. 160, Priuli): Doncaster assured the king and the constable that, if matters go further, James could not restrain his subjects from helping those of the religion, esp. La Rochelle.
- 10 Sept (London): Doncaster detained fifteen days in Paris; Calvert to the Rochelle commissioners, afraid the king can do little while engaged for his son-in-law.
- 14 Sept (no. 168, Priuli): Doncaster has taken the sickness, near death, recovering.
- 17 Sept (London): Doncaster ill on the way, business delayed. 24 Sept (London): per latest advices Doncaster, owing to sickness, had not begun his negotiations; king would let Rochelle commissioners levy troops if they fail.
- Oct pp. 139-156: no Doncaster hit.

Where it was not found: no Venetian report of an audience of Doncaster in the second half of Sept 1621 in this volume's Aug-Oct chapters as calendared; no mention of the advertisement. Use as crib: context only
(Doncaster ill, negotiations stalled around 14-24 Sept; Rochelle/Huguenot subjects, possible levies of troops; Calvert as London recipient) -- subject words for a future crib list, ungraded. Not read: the Italian originals; later
chapters (Oct-Dec) not grepped beyond October. Item stays `open`; wait line unchanged (TNA batch, ASKS 73).
