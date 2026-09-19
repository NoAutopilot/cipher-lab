# Status board

One page, always current. The orchestrator session updates it after every worker reports. If you have lost
track, read this first, then QUEUE.md for what comes next.

Last updated: 19 September 2026, 22:25 UTC.

## How the sessions work

- **Orchestrator:** the Claude Code session titled "Orchestrator". Talk there and only there.
- **Workers:** sessions the orchestrator spawns for one job each, tagged `cipher-lab`, grouped under
  "Cypher Cracking" in the sidebar. Their titles are role first, then the target: "Archive Lookup: ...",
  "Scout: ...", "Image Capture + Transcription: ...". They push their result to this repo and report to the
  orchestrator. You never need to open them. Archive them once their row below says done.

## Targets

| Target | Folder | State | Next action | Whose |
|---|---|---|---|---|
| Charles II to Hamilton, 1650 | ciphers/hamilton-1650 | Copy request emailed to NRS 19 Sept 2026 for GD406/1/2197 (5 key sheets) | Wait for NRS quote; pay; when images arrive, commit them or paste them to the orchestrator for transcription and decoding | NRS, then you, then orchestrator |
| Stepney to Manchester, 1702 | ciphers/stepney-manchester-1702 | Volume identified: TNA SP 105/65. Page-check order (£9.92) reached the form but TNA's account confirmation email never arrived | Fix the TNA account (spam, resend, check address), paste the text in REQUEST.md, add to basket, pay | You |
| Wellington to Maitland, 1812 | ciphers/wellington-maitland-1812 (being created) | QUEUE rank 4. Auction lot at Spink, sale 23 Sept 2026; images may vanish after | Worker saving images and transcribing now | Worker |
| Whitworth to Harley, 1707-08 | ciphers/whitworth-1707 (being created) | QUEUE rank 2. TNA SP 91/5 items catalogued undeciphered | Worker verifying items and drafting the copy request | Worker |
| Eckert Papers, US Military Telegraph 1862-67 | none yet | QUEUE rank 1 (38/39). Huntington ledgers of coded telegrams with the cipher book online | Pull one ledger and the cipher book, read ten messages | Orchestrator, next |
| Everything else | QUEUE.md | First scout run done 19 Sept 2026: 40 scored, 163 kept unscored, 40 dropped | Work down the queue | Orchestrator |

## Worker sessions

| Session title | Job | Result | State |
|---|---|---|---|
| Archive Lookup: Stepney 1702 (blocked, done) | Find the 1702 volume | Blocked by the old "Trusted" network policy; logged | Done, archive |
| Archive Lookup: Stepney 1702 (done) | Same, after the policy change | Found SP 105/65, record C3609655; REQUEST.md updated | Done, archive |
| Scout: queue builder (done) | Refresh the snapshot; build the ranked queue | Cryptiana unchanged. QUEUE.md written: 40 scored, 163 unscored, 40 dropped. Interrupted 22:15 UTC after it began attempting ciphers beyond its brief | Done, archive |
| Image Capture + Transcription: Wellington 1812 | Capture auction images before 23 Sept sale; transcribe | | Running |
| Archive Lookup: Whitworth 1707 | Search-print check; list items; REQUEST.md | | Running |

## Environment

- Cloud environment "Default" now has full network access (changed 19 Sept 2026). New sessions can reach
  archives and Cryptiana. The original orchestrator container predates the change and cannot; it delegates.
- Repo conventions: CLAUDE.md. Workflows: .claude/workflows/check-solved.js and scout.js.
