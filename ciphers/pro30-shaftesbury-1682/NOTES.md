open

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
