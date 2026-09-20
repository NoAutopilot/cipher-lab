# Letter partly in cipher relating to Gen. Monck, 1659-1660 (BL Add MS 32093 f.423, Malet collection)

- **Status:** open.
- **Plaintext language:** English, near-certain. The catalogue's own item description is in English with
  English names ("Gen. Monck"), the volume is otherwise English state papers by this date, and the adjacent
  items (ff. 421-424+) are English-language letters among Hyde, Sydney, Whitelocke and Winchilsea.
- **Ciphertext:** none transcribed. No digital image is online (BL's manuscript viewer has been offline since
  the 2023 cyber attack; this record's own "Digitised Content" facet is "No"). A copy must be requested; see
  `REQUEST.md`.

## What the catalogue says (BL Archives and Manuscripts Catalogue, checked 20 Sept 2026)

Source: https://searcharchives.bl.uk/catalog/040-002025830 (item record); parent
https://searcharchives.bl.uk/catalog/032-002025827. This is the BL's beta "interim" catalogue, which the site's
own banner says "contains catalogue records created before October 2023" and cannot list newly catalogued
items for now — it was reachable directly by curl with a browser user-agent, unlike the manuscripts viewer.

Parent collection, shelfmark Add MS 32091-32096, title verbatim: "STATE PAPERS, historical documents, and
official and private letters from 1086-7 to 1760; formerly belonging to the family of Malet, Baronets, of
Wilbury, co. Wilts., and chiefly collected by Sir John Malet, M.P. temp. Chas. II. Interspersed are also papers
collected by George Harbin... In six volumes. Vol. I. (ff. 279); 1087-1575. Vol. II. (ff. 333); 1576-1624.
Vol. III. (ff. 423); 1625-May, 1660. Vol. IV. (ff. 420) July, 1660-1676. Vol. V. (ff. 415) 1677-1697.
Vol. VI. (ff. 364); 1700-1762. The collection was described for the Historical MSS. Commission, 1876, 1879
(App. 5th Report pp.308-320; App. 7th Report pp.428-433)." Add MS 32093 = Vol. III (ff. 423, dated 1625-May
1660): one continuous volume, French religious/diplomatic material at the start, English state correspondence
later. (A stray web snippet calling this "1635-40" is unreliable and contradicted by the catalogue record.)

Item entry, quoted verbatim: **"113. Letter partly in cipher, undeciphered, relating, apparently to
Gen. Monck and his movements in 1659 and 1660. Imperfect. f. 423."** — immediately preceded by item 112, "Sir
Edw[ard] Hyde [Lord Chancellor, afterwards 1st Earl of Clarendon], to [Heneage Finch, 2nd] Earl of Winchilsea;
Breda, 23 May, 1660... f. 421." The index confirms both "Monck, George, 1st Duke of Albemarle, army officer,
1608-1670" and "Malet, John, alias Mallet; of Poynington, county Somerset" as names on this volume. "Imperfect"
suggests possible physical damage worth seeing before transcription starts.

BL access (checked 20 Sept 2026, bl.libguides.com): a Reader Pass issued after 21 March 2024 is needed to
consult the item in person; requests go through an online form (max 4 Western-MS requests active at once,
submit up to 28 days ahead). For a reproduction without a visit, bl.libguides.com/copyright/copying-at-the-british-library
says readers "may order hi-resolution digitisations from" BL Imaging Services with "a service fee to cover the
costs," but no fixed price is published online — expect an email/quote-based request. See `REQUEST.md`.

## Search before solving (CLAUDE.md rule 1), 20 Sept 2026

1. **Search engine.** "Add MS 32093" Malet Monck cipher, "32093" Malet Monck cipher undeciphered, "Add. 32093"
   Monck cipher: no hits referencing this item outside the BL catalogue itself. Nothing found.
2. **Printed correspondence.** Thurloe State Papers vol. 7 (british-history.ac.uk, Feb-Nov 1659) contains
   Monck/Clarges correspondence of this period and is fully digitised/searchable; the Calendar of Clarendon
   State Papers (Bodleian, ed. Macray), vol. 4 covers 1657-1660. Neither was searched page-by-page or
   full-text for a decipherment of this specific item — only a keyword web search was run, which is weak for
   19th-century-printed calendar text that is not fully OCR'd/indexed. **Not checked**: the Historical MSS
   Commission's own 1876/1879 description of this collection (5th Report pp.308-320, 7th Report pp.428-433) —
   an 1870s report predates modern digitisation and, per rule 10's Eckert 1864 lesson, is exactly the kind of
   sender/collection-specific edition that a plain web search misses. This is the first thing to check before
   treating this as unsolved for solving purposes.
3. **Community lists.** Grepped `sources/cryptiana/web/unsolved.htm` for "32093" and "Malet": zero matches;
   this item is not on Tomokiyo's list under either name. The same file lists a related but distinct item,
   "Undeciphered Superscription by Hyde (1659-1660)" (marked "Solved (as Nulls)"), citing BL Add MS 4166
   ff.92-93, a separate 1 Nov 1659 Hyde intercept with clear superscriptions "For the Lord General Monk" — this
   confirms Monck material of the same period circulated in cipher/code contexts elsewhere, but is not this
   item. See `ciphers/whitworth-1707/` for the adjacent period's other cipher work, and
   Bourdeau's `hyde/` folder below.
4. **Cipherbrain / Cipher Mysteries.** No relevant hits for "Monck cipher letter" beyond generic top-50 lists.
5. **DECODE.** de-crypt.org is reachable but a web search "site:de-crypt.org Monck" and "\"Add. 32093\" Monck
   cipher" returned no relevant record IDs. **Not logged in or browsed directly** — out of scope for this
   scouting pass; a future worker with a DECODE login should check.
6. **Solver repositories.** Grepped `/tmp/cyphersolver` and `/tmp/unsolved-ciphers` (shallow clones, 20 Sept
   2026) for monck|monk|32093|malet|clarges: no hit for this item in either repository. Bourdeau's repo does
   have an adjacent, already-solved target, `hyde/` ("Hyde's undeciphered superscriptions," Brussels
   1659-1660, solved as nulls per the 1724 Barwick-Life editor's note) — a different letter, different
   shelfmark (not BL: sourced from Peter Barwick's *Vita Johannis Barwick*, 1721/1724), same correspondent
   (Hyde) and years, whose key names both Monck and Clarges (see Key leads below).

**Confidence that this is not already published: moderate, not high** — three checks remain: the HMC 5th/7th
Report pages, a full-text pass of Thurloe vol. 7 and the Clarendon calendar, and a direct DECODE login/browse.
Per rule 10, "not found by the searches logged above" is the only claim this sweep supports.

## Key leads

- **Hyde-Barwick cipher key** ("THE=370"), a full 643-entry nomenclator (numbers 1-692: letters, syllables,
  words), transcribed from the engraved "Tabula Cryptographica" facing p.316 of Peter Barwick's *Vita Johannis
  Barwick* (London 1721; archive.org id `bim_eighteenth-century_vita-johannis-barwick-s_barwick-peter_1721`),
  reproduced at `/tmp/cyphersolver/hyde/barwick_key.py` (Bourdeau, MIT). Relevant entries: 589 "Hyde Lord
  Chancellor", 600 "Monke Lieutenant Gen.", 637 "Clarges Dr", 572 "Barwick", 573 "Council", 608 "Parliament",
  579/580 "England"/"English". This key was used between Hyde and Barwick in exactly 1659-60 and names both
  Monck and Clarges; Bourdeau's own tests show it does **not** decode the four Hyde superscriptions (those are
  deliberate nulls per contemporary editorial testimony), but it has **not** been tried against this letter.
  Once a transcription exists, this is the first key to test — a same-correspondent, same-period key already
  built is exactly the "sibling in the same circle" pattern `LESSONS.md` calls the most productive single move.
- Thurloe State Papers vol. 7 (british-history.ac.uk/thurloe-papers/vol7): fully digitised, worth a targeted
  phrase/date search once the plaintext or ciphertext content gives something to search on.
- Calendar of the Clarendon State Papers (Bodleian, ed. Macray), vol. 4 (1657-1660): available on archive.org;
  not yet checked page-by-page for a Monck cipher/key entry.
- Bodleian Archives & Manuscripts "Clarendon State Papers" collection page
  (archives.bodleian.ox.ac.uk/repositories/2/resources/7567): not yet fetched; may hold a key alongside Hyde's
  outgoing letters of this period.

## Ideas

This is a Restoration-crux document: Monck's "movements in 1659 and 1660" cover his march from Scotland to
London (Jan-Feb 1660) that precipitated the Restoration of Charles II, so the content is a decision-of-state
letter, not a routine dispatch. Get the image first (catalogue says "Imperfect" — check what survives), then
test the Hyde-Barwick key before any fresh cryptanalysis.

## Print check, 20 Sept 2026

Free-source check of the four sources NOTES.md flagged as "not yet checked page-by-page": HMC 5th/7th Reports,
Calendar of Clarendon State Papers vol.4, Thurloe vol.7, and Nicholas Papers vol.4.

1. **HMC 5th Report (1876) pp.308-320, Malet MSS section.** Checked page-by-page from Internet Archive OCR
   (`FifthReportHMC1876`). One candidate co-occurrence: "[16--], Elsinore, Nov. 13. Algernon Sydney to my Lord
   [Whitlocke]... P.S. Monk is marching into Eng[land]... partly in cypher... about the landing of Charles II"
   — a letter *by* Sydney *to* Whitelocke, not the anonymous "relating to Gen. Monck" item 113 describes; the
   1876 report's internal volume numbering does not obviously line up with the modern Add MS 32091-6 split, so
   this is not a confirmed match. No other Monck+cipher item in pp.308-320. No relevant match.
2. **HMC 7th Report (1879) pp.428-433, "Additional Manuscripts of Sir Alexander Malet, Bart."** Checked
   page-by-page (`reportofroyalcom07grea`). Covers only 16th-century items and one 1676 speech; nothing from
   1659-60, no mention of Monck, cipher, or item 113. No relevant match.
3. **Calendar of Clarendon State Papers vol.4 (Macray/Routledge, 1932, 1657-1660).** Located on Internet Archive
   (`calendarofclaren04bodluoft`), full text grepped: 115 Monck+cipher co-occurrences out of 693 Monck mentions,
   e.g. "two copies (one in the former cipher, and another in a new one sent to Sir J. Greenville) of the power
   proposed for treating with Monck" and "cipher, deciphered by H. Hyde... uncertainty of the Presbyterians'
   attitude towards Monck." Confirms the same Hyde circle used cipher heavily for Monck news in this period, but
   all entries are Bodleian Clarendon Papers correspondence (a different archive from the BL Malet collection);
   none references Add MS 32093, Malet, or an item matching "undeciphered... imperfect." No relevant match.
4. **Thurloe State Papers vol.7, Jan-Feb 1660 pages (pp.805-825, british-history.ac.uk).** No "cipher"/"cypher"
   string on any of these pages; the two Monck mentions present are plain continental-intelligence newsletters,
   not cipher. A follow-up search for cipher content across the whole volume found only 1658 items (Monck's
   Spain/Flanders campaign correspondence), none from Jan-Feb 1660. No relevant match.
5. **Nicholas Papers vol.4 (Camden Society, 1657-1660).** Located on Internet Archive (`nicholaspapers04nich`),
   full text grepped for cipher terms (40 hits) and for Monck co-occurring with any of them. Documents cipher
   keys used in the Nicholas/Hyde circle of this period (a Hyde cipher and a Whitley/Mompesson cipher, both
   Egerton MS 2550 — a different shelfmark from the Hyde-Barwick key already in this file), but zero
   co-occurrences of Monck with any cipher term out of 47 Monck mentions, and no hit for "32093" or
   "Malet"/"Mallet". No relevant match.

**Verdict:** Not found in the sources checked here — neither a decipherment nor a more detailed description of
item 113 (Add MS 32093 f.423) turned up in the HMC 5th or 7th Report's Malet-collection pages, the Calendar of
Clarendon State Papers vol.4, Thurloe vol.7's Jan-Feb 1660 pages, or Nicholas Papers vol.4. This does not
change REQUEST.md; the BL Imaging Services order for f.423 remains the only route to a transcription.

## Check-solved sweep, date unknown

Six independent searchers were run against the claim already on file (scout check, 20 Sept 2026: web search,
Cryptiana snapshot, solver repos — no relevant hit; DECODE checked only by an indirect web search, not logged
in; print check, 20 Sept 2026: full-text grep of HMC 5th Report pp.308-320, HMC 7th Report pp.428-433,
Calendar of Clarendon State Papers vol.4, Thurloe vol.7 Jan-Feb 1660, Nicholas Papers vol.4 — no match). This
sweep both confirms those two prior checks and closes gaps they left open (HMC print sources, solver-repo
verbatim grep, and a direct DECODE record search).

1. **Open-web search** (WebSearch/WebFetch for any solution, decipherment, key or attempt). Eleven search-engine
   queries against the shelfmark, "Malet"+"Monck", and generic "Monck cipher solved" phrasing, plus a direct
   fetch of Bourdeau's `dbourdeau.github.io/cyphersolver` index page, found no page describing a solution, key,
   plaintext or stated attempt on this item. A Google-indexed snippet of the CELM (Catalogue of English Literary
   Manuscripts) page for BL Add 30000-34999 mentions only folio 421 (item 112, Hyde-to-Winchilsea), not f.423
   (item 113, the target). **Unchecked** (not negative): the full CELM page itself (403 to both WebFetch and a
   direct browser-UA curl) and the BL Untold Lives blog post on ciphers in BL manuscripts (301 to
   blogs-archive.bl.uk, then 404 on that URL) — neither could be read in full, only via search-engine snippets
   or an unreachable archived copy. **Verdict: no relevant hit found; two secondary pages unreachable.**

2. **Print check via Internet Archive/HathiTrust, plus DECODE and solver-repo cross-check.** Independently
   downloaded and full-text grepped five period sources not on the prior print-check list: Clarke Papers vol. I
   and vol. IV (Camden Society, ed. Firth, 1891/1901 — vol. IV covers exactly Monck's 1659-60 march), Skinner's
   *Life of General Monk* (1724 ed.), Gumble's *Life of General Monck* (1671), and Guizot's *Monk: chute de la
   république...* (French). None contains "Malet" or "32093"; the Clarke Papers' own "[cypher]" tags are
   editorial markers for Clarke's shorthand newsletters, unrelated to a Malet-collection item, and Skinner's one
   cipher letter (Sir John Greenvil to Hyde) is a different sender/recipient/collection. Independently
   re-downloaded and re-grepped the Calendar of Clarendon State Papers vol.4 already checked in the prior print
   pass, confirming zero "Malet"/"32093" hits. Both solver repositories were shallow-cloned and grepped
   case-insensitively for monck|monk|32093|malet across every file: no match for this item in either (Bourdeau's
   repo has an unrelated `hyde/` folder, sourced from Barwick's *Vita Johannis Barwick*, not this shelfmark;
   Aymeloglu's repo returned zero matches for all four terms). **DECODE**: one login attempt via the documented
   csrf-token flow (`tools/decode_fetch.sh`) was rejected (`IS_LOGGEDIN:false`); no second attempt was made,
   per the script's own lockout warning, so no DECODE record search was completed by this searcher.
   **HathiTrust's** own full-text search (babel.hathitrust.org) returned HTTP 403 to curl; substituted with
   WebSearch restricted to catalog.hathitrust.org, weaker than a direct query. **Verdict: no relevant hit in
   five newly-checked period sources or either solver repo; DECODE and HathiTrust full-text search unchecked
   (blocked), not negative.**

3. **Community-list check** (Cryptiana web+blog snapshot and live search, Cipherbrain/klausis-krypto-kolumne,
   Cipher Mysteries, MysteryTwister C3, r/codes). The local Cryptiana snapshot (`sources/cryptiana/`) has zero
   occurrences of "32093" or "Malet"; the two files mentioning Monck (`thurloe.htm`, `charlesii.htm`) cover
   different shelfmarks (DECODE R4902-R4908, Add MS 4166 nulls). Cryptiana's own unsolved-list page has no entry
   for this item; it lists the Moray-Wood cipher (Add MS 32091, a different volume in the same six-volume Malet
   series, still undeciphered — see `ciphers/moray-wood-1568/`) and the Add MS 4166 Hyde superscription item
   (solved as nulls), confirming both are distinct from the target. Site-restricted web searches against
   Cipherbrain, Cipher Mysteries and MysteryTwister C3 found nothing; two tangential Cipher Mysteries/BL posts
   were opened directly and confirmed not to mention this item. **Unchecked**: r/codes could not be browsed or
   searched directly (WebFetch refuses reddit.com and old.reddit.com in this environment); coverage rests only
   on search-engine site: queries. **Verdict: no relevant hit found in any reachable community list; r/codes
   itself unchecked (blocked), not negative.**

4. **DECODE (de-crypt.org) direct check**, run independently of searcher 2's single attempt. Confirmed the site
   and the decrypt-web app are reachable (HTTP 200, not blocked by egress policy or Cloudflare) and that
   `LANDSCAPE.md`/`CATALOG.md` record no DECODE id for this item. Five separate login attempts — the JSON API,
   the form-encoded API, the form-encoded API with a CSRF header, a manual replication of the documented
   GET-csrf/POST-login flow, and the repo's own `tools/decode_fetch.sh` — were all rejected (HTTP 401, or
   HTTP 200 with the embedded state `IS_LOGGEDIN:false`), using the `DECODE_USER`/`DECODE_PASS` environment
   credentials (never printed). The anonymous/guest session can load the record list but it always reports "No
   records found" regardless of query, so no record search by shelfmark, sender or year was possible. Stopped
   at five failed attempts per the lockout warning; did not retry a sixth time. **Verdict: DECODE itself
   reachable, but authenticated record search blocked — two independent searchers (this one and searcher 2),
   six login attempts total, all rejected. This is an unresolved gap requiring a fixed credential or a working
   browser-based login, not a completed negative check.**

5. **Bourdeau's cyphersolver repository**, cloned and grepped directly (not just via web search as in the prior
   scout check). No folder, target directory or catalogue-file entry for Monck, Malet or Add MS 32093; the two
   numeric/string coincidences found (`32093` in unrelated OCR/data files; `malet` in unrelated corpora) are
   false positives. The two closest folders were read in full: `moray/NOTES.md` (Regent Moray to John Wood, Add
   MS 32091 — a different item, volume, and century, in the same six-volume Malet series) and `hyde/NOTES.md`
   (Hyde's undeciphered superscriptions, Brussels 1659-60 — solved as nulls; a different, non-BL letter, though
   it does name "Monck" in clear-text cover addresses and its key includes an entry "Monke Lieutenant Gen.",
   already recorded in this file's Key leads section). **Verdict: no relevant hit; both near-miss folders
   confirmed distinct from this item.**

6. **Aymeloglu's unsolved-ciphers repository**, cloned and grepped, plus a GitHub search of Robert Pitt's public
   repositories (cited in `LESSONS.md`/`LANDSCAPE.md` as a third source family). No folder, README/TARGETS/
   SHORTLIST/CATALOGUE row for Monck, Malet or Add MS 32093; the only string matches (`32093` in a `uv.lock`
   dependency hash, `malet` in a DECODE catalogue CSV row for an unrelated 15th-century "Francisco Maletta" item
   at the Austrian National Library) are false positives. Robert Pitt's 40 public repos include no match by
   name/description, and GitHub code search scoped to his account returned zero hits for all three terms.
   **Unchecked**: Pitt's repos were checked by name/description and indexed code search, not by cloning and
   full-text grepping all 40 individually. **Verdict: no relevant hit found.**

**Reconciled verdict.** All six searchers agree: no solution, decipherment, key, plaintext or even a more
detailed description of item 113 (BL Add MS 32093 f.423) has been found in any reachable source — search
engines, Cryptiana/Cipherbrain/Cipher Mysteries/MysteryTwister, five newly-checked printed editions (Clarke
Papers I & IV, Skinner, Gumble, Guizot) plus a re-confirmed Calendar of Clarendon State Papers vol.4, and both
named solver repositories (including a full clone-and-grep, not just web search, of each). This both confirms
the prior scout check and print check on file and extends their coverage. No prior work by any named solver
exists to credit for this item; the only prior work on file is this repository's own scout check and print
check (20 Sept 2026, unattributed worker sessions) and the BL catalogue's own item description. One gap is not
closed: DECODE (de-crypt.org) could not be searched at all — six login attempts across two independent
searchers, using the environment's `DECODE_USER`/`DECODE_PASS` credentials via every documented and undocumented
flow, were all rejected (`IS_LOGGEDIN:false`/HTTP 401), leaving DECODE's own record database unchecked rather
than negative; this should be flagged to whoever maintains those credentials before it is reported as checked.
Other sources marked unchecked (not negative) above: the full CELM page and the BL Untold Lives blog post (both
unreachable), HathiTrust's own full-text search (403), and r/codes (unbrowsable, search-engine-only coverage).

**Verdict: open — verified unsolved by every reachable source (rule 5 vocabulary); status unchanged from the
existing "open," since no ciphertext has yet been transcribed and this sweep is a pre-transcription
not-already-solved check, not a reading. The DECODE record database remains an open gap, not a closed one.**
