open
Christie, Life of Anthony Ashley Cooper, First Earl of Shaftesbury vol. 2 (1871; archive.org india.history.resource.85275) full-text search (be-api) by this worker 2 Oct 2026: Percivall 1 hit (a female servant), Perkins 1 (a horse-gelder), Fisher 0, "book of letters" 0, "June 1682" 0; positive control Stringer 1 document hit (his letters as secretary).

# Lord Shaftesbury's drafts of letters in cipher to Percivall, Perkins and Captain Fisher — TNA PRO 30/24/7/505

QUEUE row: N50 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **PRO 30/24/7/505** (Shaftesbury Papers), 1682 June 6. TNA Discovery's own
catalogue description (fetched fresh, 24 Sept 2026, Discovery id C6756450): "Draft of letter from Lord
Shaftesbury to Mr. Percivall, also of one to Mr. Perkins, and another to Captain Fisher, in cypher. Indorsed,
'These to be in my lord's book of letters, entered November 1682.'" `digitised: false`, `note: None`, held
solely by The National Archives, Kew. Anthony Ashley Cooper, 1st Earl of Shaftesbury, died in exile at
Amsterdam in January 1683; this draft falls in the last summer before his flight to Holland (November 1682).
The indorsement implies a fair copy once existed in "my lord's book of letters" — not separately catalogued
under PRO 30/24 by that description; not chased further this pass.

## Check-solved sweep (24 September 2026)

Six sources checked directly by this worker (Sonnet, no subagents spawned — TNA Discovery and archive.org
calls made directly under this run's host list).

1. **TNA Discovery, siblings.** `tools/discovery_items.py "PRO 30/24" "PRO 30/24/7" cipher Shaftesbury
   Percivall Perkins Fisher` returned exactly one item in the whole piece PRO 30/24/7 matching any of those
   terms: this target itself (C6756450). No sibling decipherment or key catalogued in the same piece. (4 API
   calls.)

2. **Editions, printed Shaftesbury correspondence/biography.** W. D. Christie, *A Life of Anthony Ashley
   Cooper, First Earl of Shaftesbury, 1621–1683* (1871), searched via archive.org be-api fts (no login) on
   two identifiers: **vol. 1** (`lifeofanthonyash01chriuoft`, covering pre-1667) and **vol. 2**
   (`india.history.resource.85275`, explicitly labelled covering 1667–1683, i.e. the right years). Vol. 2
   full-text search: `Percivall` → 1 hit, "Mrs. Mary Percivall" at the "Steward's table" — a different person
   (female household servant), not our male addressee "Mr. Percivall". `Perkins` → 1 hit, "old Perkins of
   Hinton Martine" who "gelt" a horse — an agricultural note, not a correspondent. `Fisher` → 0 hits. `cypher`
   → 1 hit: "...that this letter was put into **cypher** by **Stringer**? Mr. Martyn further states that
   Ashley endeavoured [concerning an] alliance..." — quoted verbatim; more context pulled (`Stringer cypher`,
   1 hit, 5-line snippet): this is trial/deposition testimony (a "Mr. Martyn" as witness, the topic "alliance")
   about Thomas **Stringer**, Shaftesbury's secretary from the 1670s until his own death in 1702, who is
   independently confirmed (same page) to have regularly "put into cypher" letters on Shaftesbury's business —
   general evidence that Shaftesbury's household used cipher routinely, but this specific quoted letter is
   about "alliance" testimony (reads as evidence from the 1681 Rye House/Association period), not addressed to
   Percivall, Perkins or Fisher, and the book does not name our three recipients as cipher correspondents
   anywhere in vol. 2. Vol. 1 was also checked for "Percivall" (his own male servant "James Percivall", to
   whom Shaftesbury owed and lent money — an earlier, different context, pre-1667, not a diplomatic/political
   correspondent) — confirms "Percivall" was a real name in Shaftesbury's household across decades, but not
   the cipher letter itself. No printed edition places this specific June 1682 letter or its plaintext.
   (archive.org: 2 advancedsearch + 6 be-api fts calls.)

3. **Community lists.** WebSearch `"Shaftesbury" "Percivall" "Perkins" "Fisher" cipher 1682` returned nothing
   relevant (unrelated Thomas Percival the actor, general Shaftesbury biography pages, NSA cryptologic-museum
   pages unrelated to this letter). No Cryptiana or Cipherbrain hit for this item; local grep of
   `sources/cryptiana/` for "shaftesbury"/"percivall"/"pro 30/24" returned zero hits.

4. **DECODE (de-crypt.org).** No login attempted (known broken; out of this lane's host list regardless).
   `aaymeloglu/unsolved-ciphers`' cached `catalogue/decode-catalog.csv` and `decode-records.jsonl` greped for
   "shaftesbury"/"percivall"/"pro 30/24": zero hits. No DECODE record found for this item in the cache.

5. **Solver repositories.** Fresh shallow clones of both (24 Sept 2026). `dbourdeau/cyphersolver`: grep for
   "shaftesbury"/"percivall"/"perkins" across the tree (excluding images) returns nothing; no target folder,
   no README row. `aaymeloglu/unsolved-ciphers`: grep of `TARGETS.md`, `SHORTLIST.md`, `catalogue/*` for the
   same terms returns nothing. Neither repository has touched this item.

6. **General web search.** `"Shaftesbury" "Percivall" "Perkins" "Fisher" cipher 1682` (above) and a second
   pass restricted to Shaftesbury's biography and the Christie/Christie-cited secondary literature found
   nothing naming this specific draft, its plaintext, or a decipherment.

**Host requests this pass:** discovery.nationalarchives.gov.uk 5 (record search + detail, ≥3 s apart, part of
this worker's shared 27-call total across all four targets), archive.org 8 (2 advancedsearch + 6 be-api fts,
≥3 s apart), WebSearch 1, GitHub 2 shallow clones (grepped, kept for other N-targets this pass).

## Verdict

**Status: open.** No printed edition (Christie's 1871 biography, the only substantial printed source
identified for Shaftesbury's later correspondence), community list, DECODE cache, or either solver repository
names this specific letter, its addressees as a cipher-correspondence trio, or a decipherment. Christie's
book independently confirms Shaftesbury's household used cipher through his secretary Stringer and that a
"Percivall" and a "Perkins" both appear elsewhere in Shaftesbury's papers as unrelated persons (a manservant
decades earlier; a horse-gelder) — worth flagging so a future worker does not mistake either name-hit for this
letter's addressee. Nothing rules out this specific letter appearing in an unindexed part of Christie's book,
or in the Shaftesbury Papers' own finding aids (not checked, out of scope: this pass ran the queries the brief
named, not every possible lead) — a caveat, not a closed question.

**Copy status:** `digitised: false` (Discovery API, confirmed directly, not inferred). **TNA page-copy order**
case — see REQUEST.md. No online image exists to check "in cypher" by eye.

**Recommended next step:** a TNA page-copy order for PRO 30/24/7/505; separately, the indorsement's "my lord's
book of letters, entered November 1682" implies a fair-copy letter-book that may survive elsewhere in PRO
30/24 — worth a targeted Discovery search by a future worker, not chased this pass.

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

Waits on: a TNA page-copy order for PRO 30/24/7/505 (REQUEST.md, since the 24 Sept 2026 check-solved sweep,
now folded into the consolidated TNA batch, ASKS row 73).

- [done 2 Oct 2026, A2-SHA] S: search PRO 30/24 for the indorsement's own 'book of letters, entered November 1682' fair-copy letter-book -- tools/discovery_items.py; no 1st Earl letter-book for 1682 catalogued (see "## PRO 30/24 letter-book search (A2-SHA, 2 Oct 2026)").
- S: re-search Christie's vol. 1/2 (already fetched) for the indorsement's exact phrase 'book of letters'/'November 1682'; only Percivall/Perkins/Fisher/cypher were searched so far.
- S: identify and search another printed Shaftesbury letter collection (e.g. the 1830 Original Letters of Locke, Sidney and Shaftesbury), not yet located this pass.

## Web and blog check (GF-A2-6, 2 Oct 2026)

Plain web searches (WebSearch, 2 Oct 2026):
1. `Shaftesbury 1682 cipher letter Percivall Perkins "Captain Fisher"` -- Notes and Queries no. 67 (8 Feb 1851; opened on gutenberg.org and grepped: its Shaftesbury item is the 3rd Earl's letter to Le Clerc about Locke, no cypher, no Percivall/Perkins/Fisher), Marsh's Library, NLI manuscript records, a TNA record, Grub Street Project 1682 pamphlets. None about this draft.
2. `"PRO 30/24/7" cypher Shaftesbury` -- TNA collection record C11970 and other PRO 30/24 items; nothing on item 505's content.
3. `"These to be in my lord's book of letters"` (the indorsement in quotes) -- no exact hit; unrelated Leeds, Aberdeen, Donne and Huntington records, and the 3rd Earl's letters to Ainsworth.
4. `Shaftesbury drafts of letters in cypher Percivall Perkins Fisher 1682 decipher` -- the same N&Q issue, Eton College records, a Spectator review of 1871 (Christie), Frommann-Holzboog's Standard Edition of the 3rd Earl's correspondence (a different Earl). Nothing on this item.

Blog site searches:
- Cipherbrain (scienceblogs.de), `Shaftesbury cipher 1682`: only unrelated posts (Henry II device, Ferdinand III, Urquhart, Shugborough, a king's letter on Tomokiyo's list); none mentions Shaftesbury.
- Cryptiana (cryptiana.blogspot.com, cryptiana.web.fc2.com), `Shaftesbury cipher`: no results.
- Cipher Mysteries (ciphermysteries.com), `Shaftesbury cipher 1682 Locke`: only La Buse, d'Agapeyeff and an index page; no Shaftesbury post.
No plausible hit for this item, so no comment thread bears on it.

Not found: no decipherment, plaintext or prior attempt for PRO 30/24/7/505 on the open web or in the three blogs.

## Premise check (GF-A2-6, 2 Oct 2026)

(a) Decipherments the folder already mentions: none for this item. The folder names the indorsement "These to be in my lord's book of letters, entered November 1682", which implies a clear fair copy in a letter-book. TNA Discovery (tools/discovery_items.py "PRO 30/24" "PRO 30/24" cypher "book of letters" Percivall, 2 Oct 2026): the only "cypher" item in the whole collection is this one; every "book of letters" / entry-book hit is the 3rd Earl's (PRO 30/24/22/2-7, 23/8-9, from 1689 on); no 1st Earl letter-book for 1682 is catalogued. Christie vol. 2 has no "book of letters" (search above). Not found; the fair copy's survival is unknown.
(b) Other solvers' working files: fresh shallow clones (2 Oct 2026) grepped for `shaftesbury|percivall`, `PRO.?30.?24`: dbourdeau/cyphersolver hits are only incidental text in source dumps (`targets/perwich/camden1903.txt`, `targets/harley1582r8499/lit/harlcat2.txt`, a Napoleon source), not this item; aaymeloglu/unsolved-ciphers none (cited, not copied). Not found.
(c) Physical neighbours: no image online (`digitised: false`) -- leaves either side, facing page and slips unreachable. The same Discovery query shows "Percivall" elsewhere only as Peter Percivall of London, mortgagee with Shaftesbury in 1681 and 1683 (PRO 30/24/46B/101, /103), and "Mr. Percival's note of my exchange at Knowlton" (PRO 30/24/4/172, 1668) -- a possible identification of the addressee, not a decipherment. Not found.
(d) Recipient side: no printed correspondence of a Percivall, Perkins or Captain Fisher of 1682 located in the searches above. Christie vol. 2 (the 1st Earl's printed life and letters) names none of the three as correspondents. Not found in what was read; the 1830 *Original Letters of Locke, Algernon Sidney and Lord Shaftesbury* (T. Forster) was not searched this pass.

## Intake gate (A2-SHA, 2 Oct 2026)

`python3 tools/intake_gate_check.py pro30-shaftesbury-1682`:
```
pro30-shaftesbury-1682: open (line 1) -- edition/page or full-text-search citation found within 6 lines
```
exit 0.

## PRO 30/24 letter-book search (A2-SHA, 2 Oct 2026)

Step: the While-waiting item "search PRO 30/24 for the indorsement's own 'book of letters, entered November 1682'
fair-copy letter-book" (tools/discovery_items.py, series "PRO 30/24", keep prefix "PRO 30/24", one term per call,
2 s apart; Discovery API, 11 calls). Hits per term (item references, whole collection, not only piece 7):

| term | hits | what they are |
|---|---|---|
| "book of letters" | 7 | this item (7/505); the 3rd Earl's entry books 22/2 (1689-1706), 22/4, 22/5, 22/7, 23/8, 23/9 (1703-1713) |
| "entry book" | 7 | the same 3rd Earl books (22/2, 22/4, 22/5, 22/7, 23/9); 40/45 (Parliament speeches 1670-79, 2nd Earl); 49/10 (Council for Plantations 1670-72) |
| "letter book" / "letter-book" | 1 / 1 | 48/55, the Carolina letter book 1670-1675 ("several in the handwriting of Locke") |
| "copies of letters" | 1 | 46A/86A, Admiral Vernon 1746 |
| "entered November" / "my lord's book" | 1 / 1 | this item only |
| Stringer (the 1st Earl's secretary) | 26 | letters to/from Stringer 1676-1701, accounts, deeds; none an entry book |
| Perkins / "Captain Fisher" | 1 / 1 | this item only |
| Percivall | 4 | this item; 4/172 (1668 note); 46B/101, 46B/103 (Peter Percivall of London, mortgagee 1681, 1683) |

Result: no 1st Earl of Shaftesbury letter-book (entry book, copy book) covering 1682 is catalogued at item
level anywhere in PRO 30/24 under these terms; the only 1st Earl letter book catalogued is the Carolina book of
1670-1675 (48/55), which ends seven years before this draft. The fair copy named in the indorsement is not
found in TNA's item-level catalogue; whether it survives uncatalogued, elsewhere (e.g. among Locke's or
Stringer's papers outside TNA) or not at all is unknown. Discovery's keyword search only sees item
descriptions, so a letter-book catalogued under a different wording would be missed: a search result, not
proof of loss. No reading; nothing for a verifier.

Next cheapest step: search T. Forster (ed.), *Original Letters of Locke, Algernon Sidney and Anthony Lord
Shaftesbury* (1830) on archive.org be-api for Percivall/Perkins/Fisher/cypher/"November 1682" (~$1, about 6
requests); the TNA page-copy order (REQUEST.md, ASKS row 73) remains the step that would give the text.
