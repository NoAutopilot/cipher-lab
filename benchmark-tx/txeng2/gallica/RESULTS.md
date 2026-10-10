# TXE2-GALLICA -- PREREG-txeng2-15 GP1 Gallica probe (10 Oct 2026)

Worker TXE2-GALLICA (account 4, Opus) for LANE TX-ENGINEER-2 incarnation 3. Times by `date -u`.

## Requests (one host: gallica.bnf.fr)

| # | time UTC | URL | UA | HTTP | body |
|---|---|---|---|---|---|
| 1 | 00:08:13 | https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060248g/manifest.json | browser (Chrome 124) | 403 | not saved |
| 2 | 00:08:39 (single retry, 20 s pause) | same | same | 403 | `server: cloudflare`, text/html, 5488 bytes, `<title>Attention Required! \| Cloudflare</title>`, "you have been blocked" (sha256 prefix ff5100d5c50b6820; kept out of the repo, it carries a Ray ID) |

Request count per host: gallica.bnf.fr 2. No other host.

## What landed

Nothing. Steps (2) N1 colour master btv1b9060248g canvases 182-184, (3) fr.16105 ff.104r-108v line crops (btv1b9009663p)
and (4) the five CANDIDATES.md "Other solvers' items" crops were not attempted: the brief stops at the first non-200
after one retry. No `probe 10 Oct` column added to benchmark-tx/txpool/CANDIDATES.md (nothing to record per row beyond
"host 403", which this file holds).

## What failed

The reachability test: HTTP 403 twice, a Cloudflare "you have been blocked" page (an IP/WAF block, not an
altcha challenge and not a 429). Same status as every 9 Oct call, so the block has not lifted with the UTC day change.
Not retried further (good-citizen rule). Next: a probe from a different egress (the owner's desk runner, LOCAL-QUEUE)
or a later cloud probe at a lane's choosing; nothing in this session will call Gallica again.

## Commits

- ROOM claim 9fac12b79
- this file: see the ROOM done line

Openings of eval truth: 0

Verdict: measured: Gallica answered 0 of 2 fetches (both HTTP 403, Cloudflare block page, 00:08 UTC 10 Oct 2026); nothing fetched, read or scored.
