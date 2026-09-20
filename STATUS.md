# Status board

One page, always current. The orchestrator session updates it after every worker reports. If you have lost
track, read this first, then QUEUE.md for what comes next.

Last updated: 20 September 2026, 03:48 UTC

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
| Stepney to Manchester, 1702 | ciphers/stepney-manchester-1702 | TNA page check ordered and paid 19 Sept 2026, order 3660178, SP 105/65 | Wait for TNA's quote for the copy; pay; when the copy arrives, commit it or paste it to the orchestrator | TNA, then you |
| Wellington to Maitland, 1812 | ciphers/wellington-maitland-1812 | Transcribed 19 Sept 2026. Dictionary search: 57 editions tested, none matches (DICTIONARY.md). HathiTrust pass running from a real browser since 20 Sept 00:02 UTC | Worker: HathiTrust searches. You, before 23 Sept: email Spink asking whether lot 1184 includes a pocket dictionary | Worker, then you |
| Whitworth to Harley, 1707-08 | ciphers/whitworth-1707 | Verified 19 Sept 2026: plaintext of the SP 91/5 'undeciphered' items is in print (Sbornik IRIO 39 and 50) except one clause of f. 108. Copy request drafted for ff. 108, 106, 121 | Order the three items from REQUEST.md (about 10 images) | You |
| Eckert Papers, US Military Telegraph 1862-67 | ciphers/eckert-1862, ciphers/eckert-1864 | Pilot 1 done 19 Sept: Zooniverse transcribed; its decoding phase never ran (single entries were read on the project blog, AUDIT.md); ten 1862 telegrams read at grade C. Pilot 2 done 20 Sept 00:00 UTC: cipher book mssEC 41 transcribed in full; twenty 1864 entries of mssEC 19 read at grade H (296 H, 8 C, 1 M). Verifier audit done 20 Sept (ciphers/eckert-1864/AUDIT.md): E6 and E12 were already in print (N1: OR I/32 pt 3 p.498; Basler CW 7:479), E4 and E5 are N3 (no prior plaintext located in the sources searched; not 'unpublished'). Nothing in the folder may be called a first decipherment. About 550 more entries readable the same way | Key test of Cipher No. 2 (mssEC 47-48) on the Beckwith/Kimber entries | Worker |
| Everything else | QUEUE.md | First scout run done 19 Sept 2026: 40 scored, 163 kept unscored, 40 dropped | Work down the queue | Orchestrator |

## Worker sessions

| Session title | Job | Result | State |
|---|---|---|---|
| Archive Lookup: Stepney 1702 (blocked, done) | Find the 1702 volume | Blocked by the old "Trusted" network policy; logged | Done, archive |
| Archive Lookup: Stepney 1702 (done) | Same, after the policy change | Found SP 105/65, record C3609655; REQUEST.md updated | Done, archive |
| Scout: queue builder (done) | Refresh the snapshot; build the ranked queue | Cryptiana unchanged. QUEUE.md written: 40 scored, 163 unscored, 40 dropped. Interrupted 22:15 UTC after it began attempting ciphers beyond its brief | Done, archive |
| Image Capture + Transcription: Wellington 1812 | Capture auction images before 23 Sept sale; transcribe | 17 images, full transcription, pass A log pushed | Done, archived |
| Research: Wellington 1812 dictionary edition | Test pocket dictionaries against the 57 code groups | 57 tested, not found, three near misses; pushed 466cf27 | Done, archived |
| Archive Lookup + Transcription: Eckert Papers 1862 | Zooniverse coverage check; read ten telegrams | Pushed 2d54f06: never decoded by Zooniverse; ten 1862 entries read at grade C | Done, archived |
| Key Test: Eckert 1864 headquarters cipher (mssEC 47-48) | Test Cipher No. 2 on the Beckwith/Kimber entries; A read at grade H, B genuine target | | Running (started 03:15 UTC) |
| Verifier: prior-art audit of four Eckert 1864 telegrams | Disprove the "not printed" claim; N0-N5 class per message; correct wording; CLAUDE.md rule 10 | Pushed: E6 N1 (OR I/32 pt 3 p.498), E12 N1 (in print since 1864; Basler CW 7:479), E4 N3, E5 N3; AUDIT.md written; over-claims corrected; verifier template added to CLAUDE.md | Done |
| Transcription + Reading: Eckert 1864 ledger with Cipher No. 1 | Twenty 1864 entries at grade H | Pushed 045fbe2: all twenty read cleanly (296 H, 8 C, 1 M, 0 I); four not found in the OR volumes checked | Interrupted 03:06 UTC, archived 03:15 (result pushed; it had started a duplicate audit, $189 of usage) | Archived |
| Access: HathiTrust dictionary search via browser (Wellington 1812) | Test tools/browser_fetch.js; run the DICTIONARY.md section 6 searches | Chromium blocked by proxy CA; HathiTrust APIs used; 19 editions, none match | Done, archived ($11) |
| Archive Lookup: Whitworth 1707 | Search-print check; list items; REQUEST.md | Only one clause of SP 91/5/108 unread; ciphers/whitworth-1707 committed | Done, archive |

## Environment

- Cloud environment "Default" now has full network access (changed 19 Sept 2026). New sessions can reach
  archives and Cryptiana. The original orchestrator container predates the change and cannot; it delegates.
- Repo conventions: CLAUDE.md. Workflows: .claude/workflows/check-solved.js and scout.js.
