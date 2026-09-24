Status: blocked

# Bodleian MS. e Musaeo 203 — the four letters Wallis left undeciphered

Check-solved pass, LANE N2 worker csEM, 24 Sept 2026 (`date -u` read at session start: 2026-09-24 10:48 UTC).
Six-source sweep per `.claude/briefs/check-solved.md` and CLAUDE.md rule 1/9. Brief:
`.claude/briefs/runs/2026-09-24-lane-n2-csEM.md`. Source row: QUEUE.md EM4 (from
`sources/emlo/cipher-letters-2026-09-24.tsv`, LANE N2 scout scEM2, 24 Sept 2026).

## The four items

Bodleian **MS. e Musaeo 203** (= MS. Eng. misc. e. 475 in one EMLO manifestation, "MS. 19336" in another —
same physical volume), John Wallis's own master copy, "A Collection of Letters and other Papers, which were
at severall times intercepted, written in Cipher. Deciphered by John Wallis... 1653." Per the EMLO abstracts
(quoted in QUEUE.md EM4), four of its ~52-53 letters carry the placeholder "[Abstract is unavailable because
the letter is not deciphered...]" instead of Wallis's usual deciphered abstract:

1. Henri Brasset → Antoine de Bordeaux-Neufville, 4 Apr 1653 (French)
2. Unknown, Scotland, 16 Jan 1651
3. George Villiers, 2nd Duke of Buckingham, undated
4. Peter Townesend, Flanders, 5 May 1658 (with a blank page titled "A Key to the Cipher foregoing")

## 1. Search log

**a. Name/target in a search engine (WebSearch).** Four queries: `"MS. e Mus. 203" Wallis Bodleian cipher`;
`"e Musaeo 203" Wallis deciphered letters Bodleian`; `digital.bodleian.ox.ac.uk "MS. e Mus. 203"`; `Beeley
"Correspondence of John Wallis" ... "e Mus. 203"`. Confirms the collection is Wallis's 1653 gift, 52 (some
sources say 53, see below) Royalist letters 1640-53, each normally with cipher + Wallis's deciphered copy +
key. No page names any of the four "not deciphered" letters as since solved. Two further queries (`Thurloe
"Brasset" "Bordeaux" cipher 1653 deciphered`, `Duke of Buckingham cipher letter Wallis Bodleian`) returned
this repo's own Bourdeau-clone summary (see 1c) and the Dominic Winter 2020 auction listing (Lot 375, "53
letters... deciphered by John Wallis... £29,000") for the whole collection, not any one letter. One search
result's own summary claimed "the Peter Townesend letter [is] a fifty-third letter evidently added later" and
that the auction lot describes "fifty-three coded letters... all accompanied by the deciphered text" — this is
a WebSearch-engine paraphrase, not a quotation I could verify against the primary page (the Dominic Winter
lot page 403'd my WebFetch as a bot-check page, one attempt, not retried per the good-citizen rule); it
contradicts EMLO's own "not deciphered" abstract for this same letter, so **do not repeat it** until read from
the actual lot description or the Bodleian's own catalogue record.

**b. Sender's/recipient's printed Correspondance.** Beeley & Scriba's *Correspondence of John Wallis* (OUP,
4 vols to date, covering Wallis's own letters, not this deciphering collection) is the modern edition of the
general editor named in EMLO's source note (Philip Beeley). No open-web page from it addressing MS e Mus. 203
specifically was found this pass — the volumes are not on an open host in my list (archive.org copies of vols
2 were seen only as third-party PDF-scrape sites, not archive.org itself, so not used).

**c. Solver repositories.** Bourdeau's clone (`dbourdeau/cyphersolver`, shallow clone, grepped only, not
committed) has a `bordeaux/` target: Antoine de Bordeaux → Brienne, **30 May 1653**, BL Add MS 4200 f.88 —
read 2026-09-18 from the English Deciphering Branch's own worksheet, DECODE R7537 (BL Add MS 32263 f.1). This
is a **different letter and a different correspondence direction** from EM4's item 1 (Brasset → Bordeaux-
Neufville, 4 Apr 1653): different sender, different recipient, different date, different holding shelfmark.
Bourdeau's own NOTES.md states as an aside: "Wallis's Bodleian collection of decipherments ends with a French
letter of 4 April 1653, so he did not do this one" — **this is almost certainly EM4 item 1** (same date,
same language, same collection), independently confirming from the solver side that Wallis left it
undeciphered. It does **not** establish that item 1 uses the same cipher design as R7537 (Bordeaux→Brienne);
R7537 is keyed to "Mr. Bordeaux" as receiver in London, the opposite direction and a different sender to
item 1's Brasset→Bordeaux-Neufville. **Unresolved**, would need the actual R7537 worksheet or item 1's own
cipher inventory to compare. Aymeloglu's clone (shallow, grepped) has no `wallis`/`musaeo`/`brasset` hits;
its DECODE catalogue dump (`catalogue/decode-catalog.csv`, `decode-records.jsonl`) has two unrelated Brasset
records (id 9431, Clairambault 574 pp.4-5, 1645-49, key type; id 9429, Clairambault 417 f.236, 1648,
**Decrypted**) — different shelfmarks (BnF, not Bodleian), different dates, not this letter; they do establish
Brasset corresponded in cipher elsewhere and some of it is already broken, which is context, not evidence
about this item.

**d. DECODE.** Not queried directly (host reserved to the DECODE-login worker this run, per COMMON RULES);
neither Bourdeau's nor Aymeloglu's DECODE-catalogue mirrors show a record for MS. e Musaeo 203, "Brasset ...
Bordeaux-Neufville", "Buckingham" (Wallis-era), "Townesend ... Flanders 1658", or "Scotland 1651" under this
shelfmark.

**e. Thurloe State Papers (Birch 1742), archive.org, be-api full-text search.** Identifier map built via
`advancedsearch.php` (`collectionofstat01thur`..`07thur`, 7 vols). Item 1 (Brasset→Bordeaux-Neufville, 4 Apr
1653) falls in vol. 1's date range. `be-api.us.archive.org/fts/v1/search` hits for "Brasset", "Bordeaux",
"Neufville", "Buckingham" (with "cipher") in `collectionofstat01thur` **all return the same single page, 838**,
with fragments of many different, topically unrelated sentences (a 1625 Denmark embassy, a sick "lord of
Buckingham" in an army, property "formerly belonging to the duke of Buckingham") — the pattern of many
alphabetically-adjacent B-names and no coherent narrative on one page is the signature of an **index page**,
not body text; p.838 is very likely Thurloe vol. 1's own name-index (B section), not the letter itself. I did
not get past this to the letter's actual page (the fts snippet API gives ~10-word fragments, not full pages,
and I ran out of budget reading OCR fragments blind — see Usage below). **This is not a negative and not a
positive**: Thurloe vol. 1 (the standard edition covering intercepted correspondence of this exact period,
including other Bordeaux/Brasset material) has not actually been read for this letter, only index-adjacent
snippets. Per the common-tail quality rule, this keeps items 1 (and by extension the volume overall, since
Buckingham and Scotland 1651 items would fall in the same or an adjacent Thurloe volume) at **blocked**, not
open. No hits at all for "Townesend" in vol. 1 (wrong volume — 1658 falls in a later vol., not checked this
pass) or for a Scotland/16 Jan 1651 search (no named correspondent to query on).

**f. Digital Bodleian (images).** Browser-rendered searches (`tools/browser_fetch.js`, JS SPA, curl alone
returns an empty shell) for `"e Mus. 203"` and separately for the shelfmark string: **"No items found"**
both times (site banner also noted "Technical issues are affecting Digital Bodleian" at fetch time, so a
false negative from an outage cannot be fully excluded). `archives.bodleian.ox.ac.uk` (Bodleian Archives &
Manuscripts, the finding-aid site, not in this brief's host list but read via WebFetch as a search-result
page per COMMON RULES) 503'd twice on the two records WebSearch surfaced for this collection
(`/repositories/2/resources/5805` "A Collection of Letters and other Papers"; `/repositories/2/resources/3901`,
a *different*, later Wallis deciphering volume covering 1669-1703 — WebSearch's own summary calls this MS
"Eng. misc. e. 382" (e, not c) — not queried further (out of host list, and 503 twice already, one retry
limit reached).

## 2. Verdict

**No image found; not established as solved; not established as safely open either — blocked.** All four
items stay off the board pending: (i) a real read of Thurloe vol. 1 (and the correct volume for the 1658
Townesend and undated Buckingham items) past the index, by page number rather than blind fts snippets; (ii)
a retry of `archives.bodleian.ox.ac.uk`'s two records once the 503s clear, to settle whether "53 letters...
all... deciphered" is the auction house's loose description of the whole lot (52 read + Townesend's blank-
key page bound in after) or a real claim about item 4; (iii) Digital Bodleian once its "technical issues"
banner clears, in case the two negative searches were a platform outage rather than a true absence.

**REQUEST.md written** for a Bodleian imaging order (MS. e Musaeo 203, the four undeciphered items' page
ranges) since no route to a full-size image was confirmed this pass.

## Requests (this pass)

digital.bodleian.ox.ac.uk: 2 browser_fetch (search pages) + 2 curl (SPA shell only, no data) = 4.
archive.org: advancedsearch 1, be-api fts 6. github.com: 2 shallow clones (bordeaux/, unsolved-ciphers/,
grepped only, not committed). WebSearch: 8. WebFetch: 4 (2 archives.bodleian 503, 1 Dominic Winter bot-page,
1 blogs.bodleian 503). No subagents.

## Files

None (no image, no ciphertext transcribed — this brief is check-solved only, never transcribe).
