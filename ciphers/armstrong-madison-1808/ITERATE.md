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

Next best attempt and why: **W2 -- get page images of the three NYPL Armstrong-to-Monroe RCs (22 Jan, 5 Apr, 4 May 1805)
and screen their coded passages against the target** (value range, units-digit skew, 900-1099 gap, shared values, the
`keyhunt/screen_*` battery). They carry Monroe's own decipherment, so if they share the target's code they are grade-H
key material and reopen the retired nomenclator instrument with a gloss; if they do not, the private-Monroe-cipher lead is
closed with a real witness. Route: NYPL (the 5 Oct email to manuscripts@nypl.org is awaiting reply -- the orchestrator
adds the exact items and catalogue IDs to any reply) and, faster, the UMW Papers of James Monroe editors, whose catalogue
marks 5 Apr and 4 May 1805 "Digital image" (they hold scans). Both are outward contacts: the orchestrator's (gates 1-8);
the lane hands up the item list only. While that is pending, W3 = the secondary target (birago-nevers-1571 f.119).
