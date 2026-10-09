# PREREG MQS-INTERCEPTOR (LANE MQS-3, account 4) -- written 9 Oct 2026, 10:2x UTC by date -u, pushed before any control runs

Option: `tools/prior_work.py - --interceptor POWER --year YYYY` lists the depots of
`tools/data/interceptor_depots.tsv` whose power matches and whose period covers the year, as families to log as searched.
It prints; it never marks a family searched. Row M45, research/MARY-STUART-TALK-2026-10-09.tsv (Lasry, Biermann and
Tomokiyo 2023, Cryptologia 47:2, pp.108-109, p.188 n.332).

Known answers (statistic: is depot row R in the printed list, yes/no; 3 known cases):
- K1 Mary Stuart: `--interceptor England --year 1586` lists `TNA SP 53` (incl. SP 53/22, keys seized at Chartley) and
  `BL Harley MS 1582` (Phelippes's copy).
- K2 KEYHUNT-2026-10-07.tsv row 464 (Downing's enclosed royalist cipher letters, glossed in the Thurloe papers):
  `--interceptor England --year 1659` lists the Thurloe depot (Bodleian MS. Rawl. A. / Birch 1742).
- K3 KEYHUNT-2026-10-07.tsv row 15 (fr.3977, Bourdeau's nevers1589 = fr.3977 intercepts, with decipherments):
  `--interceptor France --year 1589` lists BnF fr.3977.
Expected: 3/3 listed (4/4 depot rows). Gate: 4/4.

Null (mismatched power/date, 4 cases): `--interceptor Spain --year 1586`, `--interceptor England --year 1700`,
`--interceptor France --year 1659`, `--interceptor England --year 1500`. Expected: none of the four known-answer depot
rows listed in any case (0/16). Gate: 0/16.

Why the null can fail differently (rule 3): the statistic is row membership, which depends on exactly the two inputs the
null changes (power and year); a matcher that ignored either input (lists everything, or matches power only) would list
the K rows under the null and fail it, so the null is not identical to the known answer by construction.

Ceiling note: this is plumbing (a table lookup), not a statistical gain; shelf grade at most `controlled-only`, and only
if both gates pass. A missed gate ships the option `weak` with both numbers; nothing is run on a target from it.
