# C-FOLLOW question 3: Heathcote (Conington Castle) / Fanshaw papers, current holder

Status: **open**. One sentence that decided it: TNA Discovery's own catalogue record for part of this exact
collection states in its own scope-content note that the Conington/Heathcote Fanshaw papers reviewed by the HMC
in 1899 have since split in two, with part now at Huntingdonshire Archives and "the rest ... apparently now at
the Librarian's Dept. of the London Borough of Barking" -- so there is a traced holder, but not a confirmed
location for the specific two 1659 Hyde-to-Fanshaw cipher items LEAD-AO2 names.

Worker: worker C-FOLLOW (account 4, session_01Cn31pRut6ApxWhp14eBiz2), for the account-4 parent. 24 Oct 2026,
05:3x UTC.

## What was found

`discovery.nationalarchives.gov.uk` record **CON 7/10/2** (Huntingdonshire Archives, catalogue reference `CON`,
series "LETTERS", a 9 Aug. 1663 letter from Thomas Maynard, British Consul at Lisbon, to Sir Richard Fanshaw)
carries this note verbatim: "N.B. This is part of a collection of Fanshaw documents, originally at Conington &
reviewed by R.C.H.M. in 1899 - see report p.128. The rest of this collection is apparently now at the Librarian's
Dept. of the London Borough of Barking." (`source: A2A`; `digitised: false`; no `legalStatus`/`accessConditions`
recorded on this item.) This is the HMC 1899 report LEAD-AO2 rests on (*Manuscripts of J.M. Heathcote, Esq.,
Conington Castle*) -- the Discovery record quotes that report's own page 128, inside the same page range (pp.
107-180-ish, per the 1899 report's Fanshaw correspondence section) that holds the two 1659 Hyde-to-Fanshaw items
at pp.155-156.

- **Huntingdonshire Archives** (`heldBy` xReferenceCode 11, xReferenceId A13532500) holds at least the `CON`
  accession (confirmed separately: Discovery record `N13695801`, "Accession 5282, diary of John Moyer Heathcote
  (1800-1892)", same `heldBy` entry -- John Moyer Heathcote is the "J.M. Heathcote, Esq." of the 1899 report's
  own title). `CON 7` is titled plainly "LETTERS." (no further scope note at that level); its one searchable
  child item found this session, CON 7/10/2, is dated 1663, inside Fanshaw's Lisbon embassy (1661-66) -- i.e.
  the *later*, already-partly-resolved stratum of the collection (the 1664 Bennet-to-Fanshaw items the 1899
  editors themselves matched to the printed 1724 edition), not demonstrably the 1659 pre-embassy exile-period
  letters LEAD-AO2 names. A Discovery search for `"CON 7" Hyde` returned 0 hits -- inconclusive (could mean the
  1659 items are catalogued without "Hyde" as a searchable term, or that they are not in this sub-series at
  all, possibly having gone to the Barking portion instead).
- **London Borough of Barking and Dagenham Archives** (today's formal holder name, confirmed from an earlier
  web search this session: Discovery record-creator entries for "Fanshawe family of Parsloes" and "Lady Ann
  Fanshawe (1625-1680)" both cite reference **M51-286** there) is the other half, per the CON 7/10/2 note. Ann
  Fanshawe (Sir Richard's wife) and the Fanshawe family of Parsloes, Barking, are the documented link between
  the ambassador's own papers and this specific archive -- consistent with, not independently re-confirmed
  beyond, the Discovery note's own claim.
- No separate catalogue record, sale record or museum acquisition was found for the Heathcote/Conington
  collection as a whole; the family's own Conington Castle estate archive (the `CON` reference) is the
  Huntingdonshire Archives accession, per the diary record above.

## What was not checked (time/cost budget; next step if reopened)

Which of the two archives (or neither) holds the specific 1659 items has not been confirmed -- that needs
either the Huntingdonshire Archives online catalogue (not fetched this session; Huntingdonshire Archives'
own search interface was not tried directly, only the Discovery-API mirror of its A2A records) searched for
"1659" + "Hyde" within the `CON` reference, or the Barking and Dagenham Archives catalogue for `M51-286`
searched the same way. Neither holder's own availability flag (digitised / viewable / requires appointment)
was read from their own site; only Discovery's `digitised: false` on the one CON 7/10/2 record was read.

## Requests (this item)

`discovery.nationalarchives.gov.uk`: 2 record-details fetches (N13695801, CON 7/10/2 and its two parents, 213b...,
becc..., a4f0...) plus the 2 search queries ("Heathcote Conington", "CON 7" Hyde) already counted in this job's
total below. WebSearch: 2 queries (counted in the job total below).

## While waiting

The one action that depends on nobody: search Huntingdonshire Archives' own online catalogue (not yet tried)
and the Barking and Dagenham Archives catalogue for `M51-286`, both for "1659" and "Fanshaw"/"Hyde", to settle
which holder (if either) has the two specific items -- a cheap web/catalogue check, no archive visit needed.

Never promoted, never created a `ciphers/<slug>/` folder, never decoded.
