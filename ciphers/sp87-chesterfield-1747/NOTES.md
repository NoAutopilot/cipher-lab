open
Full-text search read by this worker (be-api fts on Dobrée's 1932 *Letters* vol.2, archive.org id lettersofphilipd0002bona, control phrase "Chesterfield" confirmed present) plus a fresh Google Books full-text search (key+country=US, 25 Sept 2026) both surfaced real, dated snippets narrating the same Waldeck/Cronstrom/Ginckel affair (Chesterfield's own 1845 printed *Letters* and the 1831 Marchmont Papers, diary of 17 Sept 1747) but neither shows the cipher despatch SP 87/23/41 or /70 itself reproduced anywhere. Recipient side opened by GF4-BATCH8 (account-4), 3 Oct 2026: Charteris, *William Augustus, Duke of Cumberland* (1913, IA `williamaugustusd00charuoft`, grepped whole) narrates Waldeck (p. 305) and Cronstrom (pp. 331-332, Aug 1747) from the Cumberland Papers without printing either despatch.

## Check-solved (LANE CX2, 25 Sept 2026)

Six-source sweep per .claude/briefs/check-solved.md, worker CX2-SP87A, re-run fresh (not just re-cited) on all six families:

1. **Web search.** "SP 87/23 Chesterfield Cumberland cipher 1747 Waldeck Cronstrom solved" and "Chesterfield Cumberland Waldeck Cronstrom 1747 cipher 'solves' Claude OR GPT" (2 queries): no model-solve announcement (Vals AI or otherwise), no claimed decipherment anywhere online; hits are only TNA Discovery catalogue pages for the same three items and dbourdeau.github.io's index page.
2. **Standard edition/calendar, read by this worker.**
   a. TNA Discovery item-details re-fetched today for all three items (C9040584, C9040876, C9046270): `digitised: false` for all three, unchanged from 23 Sept 2026.
   b. be-api full-text search on Dobrée's *Letters of ... Chesterfield* (1932) vol.2 (archive.org id `lettersofphilipd0002bona`, lending-restricted so opened only via the no-login fts route): "Cronstrom", "Waldeck", "Cumberland" all return real quoted snippets on the identical Waldeck-removed/Cronstrom-appointed/Cumberland-not-offended affair; control query "Chesterfield" also hits (confirming the search index is live on this volume, not returning spurious results). Still cannot determine from snippets alone whether Dobrée quotes SP 87/23/41 or /70 verbatim or only narrates the same events from SP 84 (Holland) — unresolved, lending-restricted, no login used (brief: no logins).
   c. **New this pass:** a Google Books full-text search (`googleapis.com/books/v1/volumes`, key+country=US) for `"Chesterfield" "Cronstrom"` surfaced two full-view (ALL_PAGES) editions of Chesterfield's own printed letters — Lord Mahon's 1845 edition (id `X5gHAQAAIAAJ`) and another 1845 printing (id `H59fQ0ZxzygC`) — both quoting "...Cronstrom said beforehand that he would quit, but has since begged to be employed: Ginkel talks in the same way, but I dare say will act..." This is Chesterfield narrating the same affair in a different, private letter of his own (his usual society correspondence), not the SP 87/23 official despatch to Cumberland. A follow-up query `"Cronstrom" "Waldeck"` surfaced *A Selection from the Papers of the Earls of Marchmont* (1831, ids `88ugXhe4sPMC`/`q88LAAAAYAAJ`, ALL_PAGES) with a longer passage — "Cronstrom and Ginckel refused to serve under Prince Waldeck, and that he had told Prince Waldeck to make no steps towards them... Ginckel, Lord Chesterfield said, being bashful; but that Cronstrom got in so well with Prince Waldeck, that he took him, and soon in the campaign Prince Waldeck found him out, and they quarrelled; and it was on the Prince of Orange giving Cronstrom the command in the lines..." A Dutch scholarly source found independently, *De Gids* (1885, id `-x_SAAAAMAAJ`), cites the same episode to "Diary of Marchmont, 17 Sept. 1747" — confirming this is Marchmont's diary record of a conversation with (or report from) Chesterfield about the affair, dated seven weeks after SP 87/23/70, not a copy of the cipher despatch itself. Attempted to pin an exact page by downloading and grepping five separately-OCR'd archive.org copies of the Marchmont Papers (`selectionfrompap01/02/03roseuoft`, `selectionfrompv31831rose`, `aselectionfromp03marcgoog`) for "Cronstrom"/"Waldeck"/"Ginckel": **zero hits in every copy** (both djvu-text grep and be-api fts) — most likely a scanno/OCR gap on that specific page common to every IA-side scan (Google's own scan/OCR of the same edition does show it in its snippet index), not evidence the passage doesn't exist; flagged as an open loose end, not pursued further this pass (a human with the physical/Google Play reader could pin the page in minutes). Basil Williams and the Cumberland Papers (Windsor) were not searched this pass — that edition risk belongs to the newcastle target and this target's own "Next" section respectively.
3. **Community lists.** `sources/cryptiana/` regrepped for "SP 87/23", "Cronstrom", "Waldeck", "Chesterfield ... Cumberland": the only Chesterfield hit anywhere in the cached snapshot is an unrelated, already-solved 1659 item (2nd Earl of Chesterfield, Princess Henriette, solved instantly by Lasry in 2022 per Tomokiyo's page) — a different Chesterfield (2nd Earl, not 4th), a different century, confirmed by name and date, not our target's 1747 despatch.
4. **DECODE.** `sources/decode/` TSVs (fetched 24 Sept 2026: dc11-20-documents, florence-dieci, records-decrypted, records-non-decrypted[+diff]) regrepped for "SP 87", "Chesterfield", "Cronstrom", "Waldeck", "Munchberg", "Hyndford", "Harrington", "Clavering", "Holdernesse": no record for any term.
5. **Bourdeau.** Fresh shallow clone of `github.com/dbourdeau/cyphersolver` (25 Sept 2026, git protocol; plain HTTPS to github.com 403s from this container, `git clone` over HTTPS works) grepped for "SP 87", "Chesterfield", "Cronstrom", "Waldeck": no target folder or catalogue row matches. The only "Waldeck" hit (`CATALOGUE.md` item 2.9) is a different, unrelated 1744 three-digit military code to Prince Carl August Friedrich of Waldeck, Hessisches Staatsarchiv Marburg (HStAM 118 a Nr. 3954) — a different correspondent, archive and cipher design.
6. **Aymeloglu.** Fresh shallow clone of `github.com/aaymeloglu/unsolved-ciphers` (25 Sept 2026): 8 target folders total (forster-1644, ferdinand-1634, starhemberg-1758, and five others), none named SP 87 or matching any correspondent name in this cluster.

**Sibling decipherment re-check.** TNA Discovery class-wide phrase search for "deciphered" restricted to record series "SP 87" re-run today: 8 hits total (SP 87/2/70, 5/62, 40/121, 40/77, 24/35, 36/13, 32/45, 40/76), unchanged from 23 Sept 2026 and none in piece 23 (1747) — no sibling decipherment for this cluster.

**Verdict: open, unchanged.** The edition risk is narrower than 23 Sept (three independent printed sources — Dobrée 1932, Chesterfield's own 1845 letters, and the Marchmont Papers diary — all discuss the identical Waldeck/Cronstrom/Cumberland affair) but every one of them reads as narration by a third party or by Chesterfield in a different letter, not as a printed decipherment of SP 87/23/41 or /70's own ciphertext; none is confirmed to close this target. No model-solve announcement, no DECODE record, no Bourdeau or Aymeloglu match. Not "new"; not "unpublished" — a search result, not a discovery (rule 10).

**Requests today (25 Sept 2026):** discovery.nationalarchives.gov.uk 3 (item-details re-fetch, >=1.6s apart); archive.org-family 9 (5 Marchmont-volume djvu fetches, 1 Mahon vol.4 djvu, 1 Chesterfield-1892-edition djvu, 2 be-api fts, all >=1.5s apart); googleapis.com/books 6 (key+country=US); github.com 2 (git-protocol shallow clones of both solver repos — plain HTTPS 403s to this container, `git clone` succeeds). WebSearch: 2 queries. No logins, no credentials printed.

---

# Chesterfield and Cumberland, ciphers on the Anglo-Dutch/Orange succession question — TNA SP 87/23/41, 51, 70 (1747)

QUEUE row: N15 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

TNA, State Papers Foreign, Military Expeditions, **SP 87/23**, The National Archives, Kew. Catalogue text
quoted verbatim from the Discovery API (`discovery.nationalarchives.gov.uk/API/search/records`, fetched 24
September 2026):

> **SP 87/23/41** (21 July 1747, id C9040584): "**Chesterfield to Cumberland, partly in cipher**: the king's
> surprise that the prince of Orange has taken the command from Waldeck and given it to Cronstrom. Cumberland
> was correct not to show dissatisfaction. The king awaits a detailed peace proposal from the French court.
> His disappointment at the weakness of the Austrian contingent."
> **SP 87/23/51** (28 July 1747, id C9040876): "**Chesterfield to Cumberland, partly in cipher**: the king's
> decision on Saxe's letter will be delayed until the next post. A copy of the letter has been sent to
> Sandwich to show to the prince of Orange. Cumberland is not to release any French prisoners while M
> Seigneur continues to make difficulties."
> **SP 87/23/70** (14 August 1747, id C9046270): "**Cumberland to Chesterfield, partly in cipher**, enclosing
> a letter of his to the prince of Orange [SP 87/23/71] to demonstrate that he has not shown any offence at
> the Waldeck affair. He has ordered all officers to obey Cronstrom..."

## Check-solved sweep (23 September 2026)

1. **TNA Discovery, full-piece sweep for a sibling decipherment.** `tools/discovery_items.py` against
   series "SP 87" piece "SP 87/23" with terms cipher/decipher/undeciphered/duplicate (4 requests) returned
   exactly these 3 items — no other item in the piece is cipher-flagged. A class-wide phrase search for
   "deciphered" restricted to record series "SP 87" (1 request, 8 hits across the whole class, shared with
   the N14 sweep — see ciphers/sp87-newcastle-1743/NOTES.md) returned **zero** hits from piece 23 (1747):
   the nearest are SP 87/24/35 (1748, a different piece, Newcastle to Cumberland) and SP 87/32/45 (1758).
   No sibling decipherment exists in this piece. Item-details fetches (3 requests, ids
   C9040584/C9040876/C9046270; the first two needed one retry each after HTTP 202 "still processing"
   responses, both succeeded on retry, no further retries needed) confirm `note: null` (nothing beyond the
   search description) and **`digitised: false`** for all three.
2. **Print (the decisive finding for this cluster).** As the brief anticipated, Bonamy Dobrée's standard
   edition, *The Letters of Philip Dormer Stanhope, 4th Earl of Chesterfield* (1932, 6 vols), is **not** on
   archive.org in a directly matching edition search for "Letters of Lord Chesterfield" + Dobrée, but a
   broader search (creator:Dobree AND Chesterfield) found it under its full title: vols. 1-2 only
   (`lettersofphilipd0001bona`, `lettersofphilipd0002bona`), both **lending-only**
   (`access-restricted-item: true`) — not opened this sweep (brief: no logins). Vols. 3-6 not found on
   archive.org at all. Used the no-login full-text search API instead
   (`be-api.us.archive.org/fts/v1/search`, 4 requests: "Cronstrom", "Waldeck", "Cumberland", "\"Chesterfield
   to Cumberland\"" against vol. 2) per the access playbook's allowed no-login route. Result: **vol. 2 of
   Dobrée's edition discusses the exact same episode as SP 87/23/41 and /70** — the same names in the same
   context: "The Prince of Waldeck was put in command of the Dutch troops..."/"the appointing of the Prince
   of Waldeck to command in chief the Dutch..."/"General Cronstrom said beforehand that he would quit, but
   has since..."/"the English offered the Duke of Cumberland [command]... Cumberland was held to be in
   command with Königsegg ad latus" — and one highlighted snippet is explicitly sourced "**(S.P. Holland**"
   (State Papers Holland, SP 84, a different but related series), showing Dobrée's editorial apparatus cites
   official State Papers directly for this affair. No exact-phrase hit for "Chesterfield to Cumberland" (0
   results) — the fts phrase-search syntax may not be reliable, not evidence of absence. **The `page_num`
   field returned by this API (618) equals the item's own `imagecount` (618, confirmed via
   `archive.org/metadata`) for every hit** — the known finding recorded in CLAUDE.md (be-api's page_num is
   not a real locator) reproduces exactly here, so this cannot be cited as a page number, only as "the term
   is present somewhere in vol. 2." Whether Dobrée reproduces or merely narrates/footnotes the Waldeck-
   Cronstrom-Cumberland affair — and whether he draws on SP 87/23 specifically as opposed to SP 84 (Holland)
   or Cumberland's own Cabinet papers — cannot be determined from search snippets alone.
3. **Community lists.** `sources/cryptiana/` grepped for "SP 87/23"/"Cronstrom"/"Chesterfield ...
   Cumberland": no hit anywhere in the cached snapshot.
4. **DECODE.** `ay/catalogue/decode-catalog.csv` grepped for "SP 87/23"/"Chesterfield"/"Cronstrom": no
   record.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md` and `SOLVED_CATALOGUE.md` grepped for the same terms: no hit.
6. **Aymeloglu.** `ay/CATALOGUE.md` grepped for the same terms: no hit.

Requests: discovery.nationalarchives.gov.uk 9 (4 term-searches on the piece, 3 item-details fetches with 2
retries after HTTP 202, 1 class-level "deciphered" phrase search shared with N14), archive.org 2
(advancedsearch for the Dobrée edition, 2 queries counted as 1 request pair; metadata fetch for imagecount),
be-api.us.archive.org (fts) 4.

## Edition risk

**Real and unresolved, not moot.** Unlike N9/N10/N4/N5 in earlier sweeps, this is not a case of a scout
conflating two unrelated items: Dobrée's edition genuinely discusses the identical episode (Waldeck's
removal, Cronstrom's appointment, Cumberland's non-reaction) that SP 87/23/41 and /70 report, in the same
volume, with at least one State Papers citation nearby. Whether that amounts to *printing the cipher
letters themselves* (which would close this target) or *narrating the same events from other sources*
(which would leave it open) cannot be settled without reading vol. 2 around the Waldeck/Cronstrom passage —
blocked behind archive.org's lending restriction this session.

## Verdict

**Open, stage 2 verified unsolved (conditional: Dobrée vol. 2 pp. near the Waldeck/Cronstrom passage
unread, lending-restricted; vols. 3-6 of the same edition not located; HMC/Cumberland Cabinet papers not
searched).** Three items, "partly in cipher" per the catalogue's own wording for all three, none digitised,
no sibling decipherment in the piece or the wider SP 87 class for 1747, no match on DECODE, Bourdeau's or
Aymeloglu's working lists, or Tomokiyo's cached pages — but a live, specific print-edition lead not yet
closed. Not "new"; not "unpublished" — a search result, not a discovery (rule 10).

## Next

Before any TNA copy order: get inside Dobrée vol. 2 (archive.org loan, if IA credentials are fixed, or a
library copy) at the Waldeck/Cronstrom passage to determine whether it quotes SP 87/23/41 or /70 verbatim
or only narrates the same events from SP 84/other sources — the cheapest possible resolution of this
target, per rule 2 and the access playbook's edition-first instruction, and cheaper than a copy order for
all three items. If Dobrée turns out not to print the cipher text itself, then TNA page copies for all
three (`digitised: false`, no other route). Not batched into REQUEST.md this session (brief scope: record
findings and stage only).

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: (a) a TNA page-copy order for SP 87/23/41, 51, 70 (REQUEST.md, ASKS row 57, since 25 Sept 2026);
(b) before that, an IA loan read of Dobrée vol. 2 near the Waldeck/Cronstrom passage (NOTES.md's own "Next"
section) -- IA login/borrow now works (access playbook, resolved 23 Sept 2026) but the page images are
served obfuscated for scripts, so a person still has to read the held loan in the reader.

- S: pin the exact Marchmont Papers page for the Cronstrom/Waldeck passage via a sixth OCR source or a different archive.org scan -- five copies all have an OCR gap on this page, though Google's own snippet shows it.
- S: search Basil Williams and the Cumberland Papers (Windsor) editions, this target's own named unsearched edition risk, via archive.org/HathiTrust.
- S: full-text search Dobrée vol. 2 (already fts-searchable, no login) for 'S.P.' or 'State Papers' near the Waldeck passage, to see whether it cites SP 87/23 directly rather than SP 84 -- without needing to borrow the book.

## Web and blog check (GF4-BATCH8 (account-4), 3 Oct 2026)

WebSearch, 3 Oct 2026: (1) `Chesterfield Cumberland 1747 cipher Waldeck Cronstrom despatch deciphered` -- TNA Discovery/beta catalogue
pages for SP 87/23/41 (C9040584) and a neighbour, Bourdeau's index page, Wikipedia (Fontenoy, Lauffeldt); no decipherment named.
(2) site-restricted to the three blogs, `Chesterfield 1747 cipher` on **Cipherbrain** (scienceblogs.de/klausis-krypto-kolumne: musical
cryptogram, Urquhart, Henry II device, Ferdinand III, an 1897 newspaper ad), **Cipher Mysteries** (ciphermysteries.com: Gentlemen's
Cipher 1748, early American ciphers, Blitz) and the **Cryptiana blog** (cryptiana.blogspot.com: no hit; Tomokiyo's only Chesterfield
item is the 2nd Earl's 1659 letter, already noted above); no post or comment thread names SP 87/23. Solver repositories re-cloned
shallow 3 Oct 2026 and grepped (`SP ?87/23|cronstrom`): zero hits in Bourdeau's and Aymeloglu's.

## Premise check (GF4-BATCH8 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment: **not found** -- NOTES.md and REQUEST.md name no decipherment, gloss or clear copy of
/41, /51 or /70; the SP 87 class-wide "deciphered" sweep (8 hits) has none in piece 23. (b) Other solvers' working files: **not
found** -- no SP 87 folder or rendering in either solver repository. (c) Physical neighbours: **unreachable** -- all three items and
/71 (Cumberland's enclosed letter to the Prince of Orange) are `digitised: false`; the piece sweep found no other cipher-flagged item.
(d) Recipient's side: **not found** -- Cumberland's papers (Royal Archives, Windsor) are printed only in extract by Charteris,
*William Augustus, Duke of Cumberland: his early life and times* (1913; IA `williamaugustusd00charuoft`, grepped whole 3 Oct 2026):
Waldeck at p. 305 ("difficulties with"), Cronstrom at Bergen-op-Zoom, Aug 1747, pp. 331-332 -- narration, no despatch of Chesterfield's
printed. Mahon's 1845 *Letters* (IA BSB scans 10402489bsb, 10402490bsb, 10402492bsb, vol. I and IV among them) grepped: no Waldeck or
Cronstrom in their OCR (the passage Google's own scan shows is in a private letter, as the 25 Sept sweep found). Item stays `open`.

## While waiting (3 Oct 2026, GF4-BATCH8)

Waits on: the TNA page copy of SP 87/23/41, 51, 70 (ASKS row 57) and a person reading Dobrée vol. 2 in an IA loan.

- S: grep the Newcastle-side printed sources (Coxe, *Pelham Administration*, 1829, on archive.org) for July-Aug 1747 Waldeck/Cronstrom despatches to Cumberland -- a free crib source for the cipher passages, no person needed.

## Next step (NO-CRACKS, 5 Oct 2026)

next: grep Coxe, Pelham Administration (1829, archive.org) for July-Aug 1747 Waldeck/Cronstrom despatches to Cumberland, a free crib source for the cipher passages, ~$0.5; the page copy of SP 87/23/41, 51, 70 is ASKS 57 (not yet in outreach/tna-page-copy-batch.md as of 5 Oct 2026). Who acts: agent. Source: this file's "## While waiting (3 Oct 2026, GF4-BATCH8)"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.

## Coxe, Pelham Administration grep (R7-CHEST, 6 Oct 2026)

Job: grep Coxe, *Memoirs of the Administration of ... Henry Pelham* (1829) for July-Aug 1747 Waldeck/Cronstrom despatches to Cumberland as a crib source.
Method: archive.org `_djvu.txt` of `memoirsofadminis01coxe` (1,543,073 bytes) and `memoirsofadminis02coxe` (1,806,167 bytes), grep for cronstrom|waldeck|ginkel|ginckel|cronstr, then context reads. 4 requests to archive.org (2 advancedsearch/download pairs), >=2 s apart; no login.

Found (OCR text, not page image): vol. 1 names Cronstrom twice, both narration: the siege of Bergen-op-Zoom, trenches opened 15 July, town taken 15 Sept 1747, governor "in the eighty-first year of his age" (index: i 361), and a Pelham letter of August 1747 to Horace Walpole ("Cronstrom himself says, it is impossible to save the town"). Waldeck appears only in 1745-46 contexts (Fontenoy, command of the Dutch army, his 100,000-man plan; index i 231). Ginkel appears once, 1745 (Newcastle/Carteret-era letter). One Cumberland-to-Chesterfield despatch is quoted, dated 3 July 1747 (Lauffeldt, vol. 1 ch. XII footnote), a different despatch from SP 87/23/41, /51, /70; the quote concerns Bathiany and the right wing and names neither Waldeck nor Cronstrom. Vol. 2: index entries only (Cronstrom i 361; Waldeck i 231).
Not found: any July-Aug 1747 Waldeck/Cronstrom despatch to Cumberland, any passage reading as a clear copy or paraphrase of the cipher items' content, any decipherment. As a crib source this is a negative; at most a dating anchor (Bergen-op-Zoom fell 15 Sept 1747, after SP 87/23/70's date). Read from OCR, so a scanno could hide a hit; the "Ginkel"/"Waldeck" spellings were tried, "Waldek"/"Waldec" were not. No grades: no reading was produced (H/C/S/M/I counts 0).
Search result for the log, not a novelty verdict.

Remaining gap closed: the Coxe grep step. Still waiting on the TNA page copy (ASKS 57) and the Dobrée vol. 2 read.
