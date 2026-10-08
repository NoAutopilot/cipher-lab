# LANE LEDGER (standing; blast refill brief for account-1). Read `.claude/briefs/lane-common-blast.md` first.

Scope: the Huntington telegraph ledgers with a key in hand -- eckert-1864 (mssEC 19, mssEC 18 = object 10074), eckert-1862 (mssEC 15),
then the next ledgers in LEDGER-SCOUT-2026-10-07.md: object 5952 (Fort Monroe ciphers received and sent, 3 Feb 1864-6 Apr 1865, ~600
unread), object 8472 (USMT cipher messages sent, Aug 1862-Jan 1864), object 6254 (HQ Army of the Potomac cipher book, 1862-63) -- for
8472 and 6254 first establish which code book reads them (a controlled key test on 10 entries), and stop that ledger if none in hand
does. Start from the newest ST-LEDGER-*/LANE LEDGER handoff in STATUS.md.

Per batch of 8-10 entries: (1) the civil-war adapter of prior-work-step.md BEFORE reading -- the Huntington transcription of the same
pointer, OR ser. I/II/III and ORN by date + both correspondents, same-leaf siblings in other codes, the newspaper of the day (Chronicling
America where reachable); an entry clear in its own Huntington transcription is skipped (step 0); (2) Sonnet readers with the book's
decode script and `--check` plus a shuffled-key control; (3) G3 re-search with decoded phrases; (4) a separate Opus first verifier per
batch (LS-V pattern); (5) AUD2 rows per the common rules. Image fetches from hdl.huntington.org / CONTENTdm: one worker at a time, under
300 requests per session, `CISOSEARCHALL` form per CLAUDE.md, manifest in ciphers/<t>/images/manifest.json.
Price per entry read + first audit about USD 1.2-1.5 (ST-LEDGER-2/3); second audit about USD 2.5 per entry.
