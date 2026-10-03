# LANE-POOLS (account 1) and LANE-IMAGES (account 2) -- 3 Oct 2026 20:3x UTC (account-3 orchestrator; owner: "sounds good")

Operating rules for both, exactly as `.claude/briefs/runs/2026-10-03-acct3-lane-a1.md` "Pace": lane orchestrator on your own account,
Opus 5.5 (Sonnet only for pure catalogue search/check-solved passes), workers via create_session on your own account (source_url
https://github.com/NoAutopilot/cipher-lab), ~6 live, refill within 15 min via send_later, ledger every worker from get_session, stop on
five_hour allowed_warning/rejected or when your backlog is spent; then "LANE <name> handoff" in STATUS.md and one done ROOM line.
Never take a folder with a ROOM claim younger than 6 h or one the account-4 parent holds (its GAPS*/FT4* lines). Birago, Armstrong and
Debosnys are off limits (owner sorters / private). Good-citizen rule and the CLAUDE.md host table for every request.

LANE-POOLS (account 1) -- new candidates, pools first (CLAUDE.md Pipeline 3 "Selection rule, pools first").
1. Scout (`.claude/workflows/scout.js` brief, or workers with the same brief) for POOLS: one sender + office + key family with >= 2,000
   cipher signs across its letters, digitised (copy-free share > 0), no published reading. Start from POOLS.tsv (existing groups),
   QUEUE.md unpromoted rows, Tomokiyo's key pages (sources/cryptiana) for keys whose letters are unread, DECODE listings
   (tools/decode_list.py) grouped by sender, Gallica/BnF fr.3xxx-4xxx volumes of one sender, NA/Huygens WVO, DigitArq. Score by expected
   value (P(first cheap test moves it) x value / cost). Write QUEUE.md rows + POOLS.tsv rows; never promote, never solve.
2. Check-solved (`.claude/workflows/check-solved.js` / .claude/briefs/check-solved.md, premise check included) on the top 6 pools, one
   worker each; tools/intake_gate_check.py must pass before anything is called stage 2.
3. For each pool that passes: a spec (specs/<slug>.json) and its FIRST cheap test with a matched control (breadth lane rule 3a, cap $3),
   two numbers into cheap_test_done. Stop there -- the orchestrator promotes.
LANE-IMAGES (account 2) -- unblock image-blocked targets.
1. `python3 tools/next_steps.py`; take NEXT-STEPS.tsv rows with blocker `needs-image` (about 50) whose holding host has a working route in
   the CLAUDE.md host table (Gallica IIIF, NARA IIIF v3, DigitArq, Bavarikon/BSB, Nationaal Archief, Huygens, LOC, Europeana/DPLA keyed,
   DECODE with one login per session). Skip hosts marked "no" (BL, HathiTrust page images, Folger, TCD, NLS, PARES, Antenati, ONB).
2. Per target, one worker: read the holding catalogue record first and quote its availability flag; locate the leaf (tools/gallica_folio.py
   etc.); fetch once at native resolution into ciphers/<t>/images with images/manifest.json; keep the folder under 30 MB; cut line crops
   with tools/iiif_lines.py (debug overlay checked); update NOTES.md (route that worked, request count per host) and flip the blocker.
   No transcription, no decoding -- the next lane does that.
3. Where the image is genuinely not online: REQUEST.md row (copy order) and ASKS row, quoting the catalogue record -- never a guess.
Every brief: per-unit cap and box (Usage 6), "report what was found and where it was not found; do not classify novelty".
