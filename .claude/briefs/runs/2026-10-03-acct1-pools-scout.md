# LANE-POOLS scout (account 1), 3 Oct 2026 21:5x UTC -- four source-partitioned scout workers

Why: the account-3 orchestrator's LANE-POOLS brief (`.claude/briefs/runs/2026-10-03-acct3-lane-pools-images.md`) asks for
new POOLS -- one sender + one office + one key family with >= 2,000 cipher signs across its letters, digitised (copy-free share
> 0), no published reading -- because every reading on the board so far came from a period key or a pool of siblings, and our
solvers read code+mark only at pooled lengths (CLAUDE.md Pipeline 3, "Selection rule, pools first").

Template: `.claude/briefs/scout.md` + the common tail in `.claude/briefs/README.md`. Scout only: never promote, never solve,
never transcribe, never classify novelty. Model Sonnet. Cap USD 6, box 50 minutes from your own `date -u` at start: stop and
push at the cap or at 50 minutes, whichever first; at 40 minutes push what you have. At most 2 subagents (Sonnet).

## Read first (all four parts) -- do not re-find what is already on file

- `QUEUE.md` section "Cipher letter pools by key (LANE N4 scPOOL, 24 Sept 2026)" (line ~5555) and
  `specs/cheap-tests/pools-b5/README.md` (bPOOL0, 26 Sept): the big DECODE pools (RAH 9/23-25, BAV Barb.lat 6956/6960,
  ARA Carpio-Fuenmayor, ASV SdS France 17-18, ASV SdS Spain 364C) all overlap Bourdeau targets (sanchez1522, pallotto1629, ...).
  Do not re-nominate them as new; a row on them is allowed only if you name a *sub-pool* bPOOL0 shows is untouched, with its
  record ids.
- `POOLS.tsv` (604 rows) -- existing groups; `KEY-ADJACENT.tsv`, `KEY-OFFICES.tsv` -- keys we hold and their offices.
- Already pools, excluded: fr.4715 Vieuville-Nevers (CS-4715-POOL), Birago/Nevers/Ceppo anything (account-3 campaign),
  armstrong-madison-1808, debosnys-1883, mercy/espagnol142, malsburg-hessen-1636, lodewijk/jan-van-nassau (in hand),
  and any `ciphers/<t>` with a ROOM.md claim younger than 6 h or an account-4 GAPS*/FT4* line.
- For every candidate: `ls ciphers | grep -i <sender/shelfmark>` and grep ROOM.md -- if we already have a folder, the row says
  so and counts only letters *outside* that folder.

## Parts (one worker each; your prompt names your part)

- **P1 Tomokiyo keys.** `sources/cryptiana/` (CRYPTO-INDEX.tsv 279 rows, READABLE.tsv, keys/, web/, blog/): every key Tomokiyo
  reconstructed or prints whose *other* letters (same sender, same office, same years) he lists as unread or does not mention.
  Group by key; count the letters he names; locate them (Gallica ark/canvas where he gives the shelfmark).
- **P2 Gallica / BnF one-sender volumes.** BnF fr.3xxx-4xxx, Clairambault, Colbert (500 and Cinq-cents), Dupuy, n.a.fr.: volumes
  that are mostly one ambassador's dispatches with many cipher letters (archivesetmanuscrits.bnf.fr dépouillement; Gallica SRU
  with adjacency phrases, never "chiffré" alone -- scout.md). Excluding Nevers/Birago/Vieuville. Estimate signs from 2-4 sampled
  canvases per volume (thumbnail or low-res IIIF, `full/600,/0/default.jpg`; one vision look each, no transcription).
- **P3 Low Countries + Iberia.** Huygens WVO (`sources/wvo/`, `resources.huygens.knaw.nl/wvo`), Huygens retroboeken, Nationaal
  Archief scans (drupal-settings-json route), DigitArq/ANTT (`tools/digitarq_fetch.py`), BNP purl.pt; Europeana/DPLA with the keys.
  One-sender runs of cipher letters (an ambassador's or governor's dispatches), with an image route.
- **P4 DECODE by sender + QUEUE unpromoted.** `sources/decode/records-non-decrypted-*.tsv` (or one fresh login-free
  `tools/decode_list.py` pass if the snapshot is older than 7 days) grouped by *sender parsed from the record title*, not by
  holder fonds (bPOOL0's lesson), plus QUEUE.md rows never promoted to `ciphers/` that share a sender. For each group, grep a
  fresh shallow clone of github.com/dbourdeau/cyphersolver and github.com/aaymeloglu/unsolved-ciphers for the record ids
  (`tools/solver_repo_diff.py` / `tools/decode_neighbours.py` where they fit; cite Aymeloglu, never copy his code).

## Every candidate row needs

Pool = >= 2 letters, one sender, one office, one key family (or plausibly one: same years, same token shape), estimated >= 2,000
signs in total. Below 2,000 or one letter: list it in a "near misses" table, do not score it.

Write `sources/pools-scout/2026-10-03/P<n>.tsv` (tab-separated, one row per pool) with exactly these columns:
`pool_id  sender  office_recipient  key_family  letters  years  shelfmarks_or_records  est_signs  sign_basis  image_route
availability_quote  key_status  prior_reading  solver_repo_overlap  language  corpus  first_cheap_test  test_quote  p_move  value
cost_usd  ev  notes`
- `est_signs` with `sign_basis` (measured from N sampled canvases x lines x signs/line, or a stated per-page estimate -- say which).
- `image_route` (host + tool from the CLAUDE.md host table) and `availability_quote`: the holding catalogue's own flag, quoted,
  with URL/ark (CLAUDE.md Access playbook preamble). An image portal's "no items" is not a flag.
- `key_status`: none / period key on file (where) / published modern key (who) / sibling with interlinear decipherment (where).
- `prior_reading`: who read what, with the source sentence. `solver_repo_overlap`: grep result for both repos, with the hit or
  "no hit for <terms>".
- `corpus`: the tools/data corpus that matches the language *and era* (CLAUDE.md rule 3 pt17/pt18 lesson), or "none".
- `first_cheap_test`: one test a breadth worker can run at USD 3 with a matched control (rule 3a), and `test_quote`: the exact
  sentence from the source that makes it possible (scout.md "Quote the source").
- `ev` = p_move x value / cost_usd (value 1-5, p_move 0-1). Score a solver repo's own stated next step down (scout.md).

Also write `sources/pools-scout/2026-10-03/P<n>.md`: five-line report (raw, kept, digitised count; what was searched with
counts per host; near misses; what was unreachable). Do NOT edit QUEUE.md or POOLS.tsv -- the lane orchestrator merges the four
parts (avoids four writers on one shared file).

Good-citizen rule: one request at a time per host, >= 1.5 s apart (DigitArq 3 s, Bavarikon 3 s), a few hundred per host at most;
stop a host on 429/403/challenge. Report request count per host in your done line. Never print credentials.

Done line (tools/room.py): `done (<start>-<end> UTC, brief met|box|cap): commit <sha>. P<n>: <k> pools kept (top: <id> est
<signs>), <m> near misses; requests per host ...; cost: see the lane ledger`. Report what was found and where it was not found;
do not classify novelty.
