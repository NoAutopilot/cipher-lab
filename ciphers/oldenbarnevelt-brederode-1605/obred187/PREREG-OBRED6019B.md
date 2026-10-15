# PREREG-OBRED6019B (addendum to PREREG-OBRED6019), 15 Oct 2026, written 06:2x UTC by date -u, before any scan is fetched

Job OBRED-6019B (LANE DEFAULT-A2-0509-15, account 2). Scope: the six OBRED-6019 sheets not read, sheets 20-25 = inv. 6019 stride-3
scans 514, 517, ..., 649 (46 scans). Method, controls, hit definition and the non-test rule are exactly PREREG-OBRED6019's.

Rebuild: the 700 px scans were not committed, so `screen_tools/regen_6019b.sh` re-fetches the 46 scans (+ METS: 47 requests to
service.archief.nl, >= 2.1 s apart) and rebuilds all 25 sheets with blank placeholders for scans 1-511, so the seed-6019 shuffle is
unchanged; the rebuilt key is compared with `cmp` against the committed `images/6019_screen_sheetkey.json` without either being opened.
If cmp fails, the sheets are not the pre-registered ones and the job stops. Only sheets 20-25 are read.

Calls: tile letters of the three controls and any hit tile for sheets 20-25 are appended to `images/6019_screen_sheetcalls.txt` and
pushed before the key is opened. Re-looks at 1200 px: at most 6 requests, scratchpad only. Requests: at most 53 to service.archief.nl.
Stop rule: cap 2 (80% = 1.6), box 40 min from the claim (06:25 UTC; 80% at 06:57 UTC); sheets read in order 20..25; any sheet not read
is reported as unscreened by scan range.
