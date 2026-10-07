# armstrong-madison-1808 -- ITERATE.md (standing lane TOMO-ARM)

Framework: `.claude/briefs/runs/2026-10-07-acct3-standing.md`. One table, appended, never rewritten. Read this and
HYPOTHESES.md before every attempt. Credit: S. Tomokiyo (Cryptiana) recommended this letter to the project and published
the WE028 transcription and the shorthand comparison it starts from.

## Starting position (7 Oct 2026, 21:45 UTC, from NOTES.md / HYPOTHESES.md / CAMPAIGN.md H1-H76)

What the data say the cipher is NOT, or what this project's tools cannot test without new material:
- Not THE=972 (the Armstrong-Madison office code), not WE027/WE028, not the Madrid legation cipher, not Livingston's
  1801-04 code, not a printed dictionary code (ARM-A2, ARM3-DICT, ARM3-LIVCODE, H38, H46-H50, H68): screens MISS.
- Nomenclator / vocabulary-prior solvers: retired under rule 3's third-attempt clause (ARM-C1, H27, H73; best matched
  control 0.153 vs gate 0.6 at N=369; the en18 objective prefers wrong decodes over the truth). Reopens only with new
  material: a second letter in this code, a key, or a gloss.
- Shorthand: plate-only model reader retired (H24, H28: chance on three systems' own specimens); model glyph readers
  retired (H54/H55, kappa 0.36); crop flags untested at near-ceiling baseline (SLANT-CROP). Open: the owner's sorter
  (ASKS 128; read its db only when the owner says "done"), the dot-position test (Mavor vs Taylor), connected specimens.
- Best lead on file: Madison's "must be one concerted with another correspondent" (15 May 1808) plus the 1805 precedent
  (Armstrong's private cipher with Monroe, copies sent to Madison by mistake). Specimens of that cipher were not located.

## Attempts

| date (UTC) | hypothesis | instrument | matched control | result (both numbers) | verdict | what it taught |
|---|---|---|---|---|---|---|
| 7 Oct 2026 21:50-21:58 | W1. The 1805 Armstrong-Monroe private cipher survives on Monroe's side, and the Monroe Catalogue Online (UMW Papers of James Monroe, ~39,600 entries) says where (ASKS 97/142, LOCAL-QUEUE L54: the desk runner stopped at the sign-in) | Headless Chromium on the catalogue's FileMaker WebDirect app with the public guest sign-in printed on the project's own page (one sign-in); find by sender, by recipient, and by "code" in the repository field | not applicable (a catalogue search, not a statistic); positive check: the search returns the known LOC items (Armstrong to Monroe 24 Dec 1804, LOC Monroe Papers ALS -- found) | sender = Armstrong, John: 33 records; recipient = Armstrong, John: 33; repository contains "code": 274 found, 209 unique captured (paging in date order; 65 missed clicks show as duplicates, all from 1811 on, so 1800-1810 is complete) | pass (search ran, new locations) | The RCs exist and are catalogued: **NYPL Monroe Papers, Armstrong to Monroe 22 Jan 1805 (ALS), 5 Apr 1805 (LS) and 4 May 1805 (LS), each "partially in code and deciphered"**; Monroe to Armstrong 14 Nov 1805 (NYPL copy, "partially in code"); Bowdoin to Monroe 25 Nov 1805-10 Aug 1806, six NYPL ALS "partially in code and deciphered" (Armstrong to Bowdoin 22 July 1806: no cypher for Monroe, "recollecting that you have ..."); Armstrong to Monroe 7 July 1807 (LOC Monroe Papers ALS) says he could not read Monroe's last letter "because the cipher is incorrect". Files: `keyhunt/monroe-catalogue-2026-10-07/` |
| 7 Oct 2026 22:01-22:07 | W1b. The Armstrong-Monroe cipher was still in use nearer 1808 than 1805 | LOC Monroe Papers reel 4 frame 0302 (Armstrong to Monroe, Paris 7 July 1807, P.S. 10 July; sheet filmed mirror-reversed), tile.loc.gov IIIF full size, mirrored and rotated locally, one reader (this session) | not applicable (a document read) | P.S. read: "10 July. I regret exceedingly that from some change in your cypher or in mine, or from the use of one with which I am altogether unacquainted, your last letter by Mr R[ussell?] is altogether unintelligible to me." (H for the sense; M for the bearer's name and two words, one reader) | pass (read) | A private Armstrong-Monroe cipher was live in mid-1807, seven months before the 20 Feb 1808 letter, and the two men's copies had already drifted apart. Monroe was back in Virginia by Dec 1807, so a letter to him in that cipher could plausibly travel in the State Department pouch (I, not shown). Raises the value of W2. |

Next best attempt and why: **W2 -- get page images of the three NYPL Armstrong-to-Monroe RCs (22 Jan, 5 Apr, 4 May 1805)
and screen their coded passages against the target** (value range, units-digit skew, 900-1099 gap, shared values, the
`keyhunt/screen_*` battery). They carry Monroe's own decipherment, so if they share the target's code they are grade-H
key material and reopen the retired nomenclator instrument with a gloss; if they do not, the private-Monroe-cipher lead is
closed with a real witness. Route: NYPL (the 5 Oct email to manuscripts@nypl.org is awaiting reply -- the orchestrator
adds the exact items and catalogue IDs to any reply) and, faster, the UMW Papers of James Monroe editors, whose catalogue
marks 5 Apr and 4 May 1805 "Digital image" (they hold scans). Both are outward contacts: the orchestrator's (gates 1-8);
the lane hands up the item list only. While that is pending, W3 = the secondary target (birago-nevers-1571 f.119).

W3 checked (7 Oct 2026 21:59-22:01 UTC): birago-nevers-1571's named next step (a third letter in the Nov 1571 number system in another
Nevers volume) -- `tools/bnf_findingaid.py` over fr.3253-3256, fr.4688, fr.4712-4715: the only 1571-72 cipher items are fr.4688
nos.7-8 (Guazzo, 25 Mar 1571) and nos.24-33 (Guazzo, Casale, 12 Dec 1571-28 Apr 1572, "Chiffres"), already the target
`ciphers/guazzo-nevers-fr4688-1571-72` (blocked: fr.4688 not digitised, BnF copy order). fr.3256 no.21 (Louis de Birague
memoir, Bologna 15 Feb 1571) carries no cipher mark. Tomokiyo's 2024/07 and 2024/09 blog posts snapshotted
(`sources/cryptiana/blog/2024_0{7,9}_*.html`): no key, only the Desenclos-Lasry 1592 parse rule (3-figure codes start with 1),
which BIRAGO-NUM-TOOLS's prefix-code test already covers in kind. So Birago's new material = the fr.4688 Guazzo copy order
(ST-ACCESS's COPY-ORDERS list should carry ff.15-18 and ff.65-86).

## Retrospective after wave 1 (2 attempts + 1 check)
Moved something: catalogue/document instruments (Monroe Catalogue, LOC reel read). Never moved anything on this target since
26 Sept: in-house solvers and model glyph readers at N=369 (retired). The data now point at one witness family -- the
Armstrong-Monroe private cipher, 1805-1807 -- whose specimens with period decipherment sit at NYPL. Standing state after this
wave: waiting on W2 images (NYPL reply / UMW editors), the owner's sorter "done" (ASKS 128), and the fr.4688 copy order.
