# PREREG-MQS-BNF-S2B (written 9 Oct 2026, 07:2x UTC by date -u, before any notice was fetched or scored)

Job: MQS-BNF-S2B (LANE MQS-2, account 4), the second half of S2 of MQS-BNFPILE's "Later sessions": score with
`tools/bnf_findingaid.py --pile` (scorer unchanged, PILE_MIN 5) the non-Français finding aids (NAF, Clairambault,
Dupuy, Cinq Cents de Colbert, plus the other diplomatic fonds the census hit) that are not yet on disk. Builds on
MQS-BNF-S2A (PREREG-MQS-BNF-S2A.md, commit d30fe002): its cache `sources/bnf-findingaids/2026-10-09/` and
`sources/bnf-findingaids/2026-10-07/` are read, never refetched; its `--permute` null is reused unchanged.
Fetch once to `sources/bnf-findingaids/2026-10-09/` (same folder, new files only), 2 s apart, descriptive UA, hard ceiling
**190 requests** to archivesetmanuscrits.bnf.fr; stop the host on any 403/429/challenge. No Gallica. No reading, no
decoding, no status/key/AUDIT change. --pile stays shelf `weak` whatever happens (PREREG-MQS-BNFPILE C5).

## Target set (fixed now)
(a) Census first-page arks (`sources/bnf-census/2026-10-09/html/q*.html.gz`, titles read from the saved result pages)
not on disk, in early-modern diplomatic/correspondence fonds -- 25 arks:
NAF 23094 cc120521; Cinq cents de Colbert 483 cc918111, 338 cc91720t; Clairambault 460 cc13829m, 531 cc138775,
296-299 cc138146, 312-452 cc13826w, 873-890 cc139674, 1111-1239 cc137837; Dupuy 263 cc88429b, 269 cc88435k;
Français 5160 cc58150z, 5176 cc58166m (S2A could not match fr.5160 by title; the census gives its ark); Baluze 178
cc34105c; Lorraine 14 cc95609z, 15 cc95625d, 367-372 cc34620f, 953-955 cc340362; Espagnol 132 cc34747q, 174 cc34782b,
336 cc34944b; italien 2242 cc11190d; Arsenal Ms-4738 cc850219, Ms-6334 cc86298x, Ms-6516 cc86455q.
Excluded by title, not fetched (logged in the results): BnF administrative archives (20xx/ series), Arsenal medieval,
liturgical and literary Ms, Arsenal Bastille groups 10330-12471 (police archive, not diplomatic), Arts du spectacle
fonds, Arabe, Pelliot chinois, Latin 8777-8780 (Tironian notes), NAL 2507, Nîmes, Ms-8596 (one Venetian ducal letter),
Mélanges de Colbert 121 (already on disk, dev set).
(b) Shelfmarks the 23-25 Sept passes (`sources/solver-diffs/2026-09-2[345]-*.tsv`) name in these fonds, by `--cote`
search (POST, exact-title match, page 2 at 100 only if needed): Dupuy 44, 63, 111, 155, 265, 869; Clairambault 296,
325, 328, 348, 349, 351, 357, 360, 361, 813, 1067, 1108, 1111, 1225; NAF 1619, 1628, 1643, 1660, 4206, 6972, 13349,
28930 (NAF titled either "NAF N" or "Nouvelle acquisition française N"; both prefixes accepted). A cote whose
exact title is not matched is logged "no exact-title match", never a negative. A cote already covered by a fetched
group notice (e.g. Clairambault 325-361 inside 312-452) is still searched once for its own volume notice.
Order: (a) then (b); if the ceiling is near, (b) is cut from the end of the list, logged.

Statistic: per notice, `bare` and `open_bare`; class `pile` = open_bare >= 5. A multi-volume group notice is scored as
one row (as S2A did for fr.3974-3995); a group row reaching `pile` is checked by hand for whether its bare items sit in
one volume before it is called a pile (recorded either way).

## K1 Known answer (reproduction, same design)
fr.2988 (`2026-10-09/cc49442s.html`) scored inside the S2B set. Expected: bare 26, open_bare 0, rank 1 of the set by
`bare`. Gate: all three exact (rank 1 fails only if an S2B notice has bare >= 26 -- then reported, gate failed).

## K2 Planted pile in a fresh notice (same design, length and language as the intended use)
`planted()` from tools/tests/test_bnf_findingaid_pile.py (10 bare "Pièce en chiffre." items) and a 5-item variant,
into ONE fresh S2B notice with an item list chosen with `random.Random(20261009)` over the sorted ark list. Portals
on. Expected: both planted volumes in the top 5 of the S2B set by open_bare; 5-item plant reaches class `pile`.
Gate: 10-item rank <= 5 AND 5-item rank <= 5. Why it can fail: the base notice's own Présentation/Bibliographie marks
the plants known (non-Français notices are often richer in Bibliographie), a portal hit, or real S2B volumes with
more open bare items push the plant down. Not at ceiling: the base notice is real and unseen.

## N1 Across-volume permutation null (reused from S2A: `--permute 200`, seed 20261009)
Statistic = max `bare` in any one volume; item texts permuted across volumes, per-volume counts kept.
(i) S2B set + fr.2988: expected real 26 > null p95 (S2A's own null p95 was 6). Gate: real > p95.
(ii) S2B set + the 10-item plant, fr.2988 removed: gate real > p95.
Why it can differ: max-per-volume depends on which volume holds which item, exactly what the permutation changes.
A within-volume order shuffle cannot change `bare` and is not used (rule 3, "control that cannot vary").
Reported descriptively, no gate: S2B set alone (real max vs its null) -- the question this session asks.

## Ceiling check
Deterministic scorer, no restarts; K1/K2 are reproduction and plant checks, not rates.

## Reporting
Both numbers for every gate; every notice with open_bare >= 1 listed with digitised flag; a `pile`-class notice not
digitised goes into ONE batched REQUEST.md (ASKS 38 pattern) covering S2A and S2B together (S2A handed over none);
if none clears, no REQUEST.md is written and that is said. A notice with no item list is `image-triage`, never a
negative. Requests per host reported.
