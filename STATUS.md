# Status board

One page, always current. The orchestrator session updates it after every worker reports. If you have lost
track, read this first, then QUEUE.md for what comes next.

Last updated: 20 September 2026, 04:12 UTC

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
| Wellington to Maitland, 1812 | ciphers/wellington-maitland-1812 | Transcribed 19 Sept 2026. Dictionary search closed on 20 Sept 03:37 UTC: 76 editions tested (57 Google/IA, 19 HathiTrust via APIs), none matches; Scott, Jones 1800, London Perry, Walker 1810, Dublin Entick not in HathiTrust | You, before 23 Sept: email Spink asking whether lot 1184 includes a pocket dictionary. Library leads: Urban pp. 232-233, Bentinck papers, WO 37 | You |
| Whitworth to Harley, 1707-08 | ciphers/whitworth-1707 | Verified 19 Sept 2026: plaintext of the SP 91/5 'undeciphered' items is in print (Sbornik IRIO 39 and 50) except one clause of f. 108. Copy request drafted for ff. 108, 106, 121 | Order the three items from REQUEST.md (about 10 images) | You |
| Eckert Papers, US Military Telegraph 1862-67 | ciphers/eckert-1862, ciphers/eckert-1864 | Parked 20 Sept 2026. 1862: ten entries read at grade C. 1864: twenty entries read at grade H from Cipher No. 1 and three from Cipher No. 2, both surviving books; audit (AUDIT.md): E6, E12 already in print (N1), E4, E5 no prior print located (N3). No cryptanalysis left. Enquiry sent to the Huntington curator 20 Sept about a corpus dataset; reply decides the corpus pass | Wait for the reply | Archive |
| Earl of Stair to Townshend, 1710 | ciphers/stair-townshend-1710 | Verified 20 Sept 2026 (KU catalogue, six-source sweep): open, English | Not in print (checked 20 Sept). You: order four scans from Kansas per REQUEST.md, about $20 | You |
| Letter relating to Gen. Monck, 1659-60 | ciphers/monck-1660 | Verified 20 Sept 2026 (BL catalogue, sweep): open, English | You: ask BL Imaging Services for a quote for Add MS 32093 f.423 (REQUEST.md) | You |
| NLS MS 20769, 18th-c. cipher manuscript | ciphers/nls-20769 | Record known from snippets only; extent unverified | You: read the live catalogue record at manuscripts.nls.uk and paste it; then decide on scans | You |
| Everything else | QUEUE.md | First scout run done 19 Sept 2026: 40 scored, 163 kept unscored, 40 dropped | Work down the queue | Orchestrator |

## Results so far (labelled per README "What counts as a result")

| Target | Kind | Result |
|---|---|---|
| Eckert Papers 1862-67 | Contribution | Machine-readable Cipher No. 1 and No. 2 keys, 23 readings checked against print, AUDIT.md with N-classes, corpus-status finding; offered to the Huntington 20 Sept 2026 |
| Whitworth 1707 | Contribution | Four of five catalogue "undeciphered" items shown to be already in print (Sbornik 39, 50); one clause of f.108 open |
| Hamilton 1650, Stepney 1702, Wellington 1812, 1646 intercepts | Recovery (in progress) | Key hunts; nothing read yet |
| NLS MS 20769 | Cryptanalysis (candidate) | Pending catalogue confirmation |
| Stair 1710, Monck 1660 | Undecided | Depends on what the scans show |

## Worker sessions

| Session title | Job | Result | State |
|---|---|---|---|
| Archive Lookup: Stepney 1702 (blocked, done) | Find the 1702 volume | Blocked by the old "Trusted" network policy; logged | Done, archive |
| Archive Lookup: Stepney 1702 (done) | Same, after the policy change | Found SP 105/65, record C3609655; REQUEST.md updated | Done, archive |
| Scout: queue builder (done) | Refresh the snapshot; build the ranked queue | Cryptiana unchanged. QUEUE.md written: 40 scored, 163 unscored, 40 dropped. Interrupted 22:15 UTC after it began attempting ciphers beyond its brief | Done, archive |
| Image Capture + Transcription: Wellington 1812 | Capture auction images before 23 Sept sale; transcribe | 17 images, full transcription, pass A log pushed | Done, archived |
| Research: Wellington 1812 dictionary edition | Test pocket dictionaries against the 57 code groups | 57 tested, not found, three near misses; pushed 466cf27 | Done, archived |
| Archive Lookup + Transcription: Eckert Papers 1862 | Zooniverse coverage check; read ten telegrams | Pushed 2d54f06: never decoded by Zooniverse; ten 1862 entries read at grade C | Done, archived |
| Scout: verify and file four proposed targets | Stair 1710, Monck 1660, NLS 20769, 72438 f.104 | Stair and Monck open (English); NLS unverified; f.104 marked Decrypted on DECODE | Done, archived ($6) |
| Print Check: Stair 1710 in Graham's Annals | Free check before the Kansas order | Not in Graham 1875, HMC 11th Report or Marlborough despatches | Done, archived ($2) |
| Check Solved: blind six-source sweep of five targets | check-solved workflow, Sonnet | Hamilton: offline-only confirmed, no solution anywhere | Running (started 03:21 UTC) |
| Key Test: Eckert 1864 headquarters cipher (mssEC 47-48) | Test Cipher No. 2 on the Beckwith/Kimber entries | Outcome A: mssEC 47 reads them at grade H; key-no2.md, reading-no2.md | Done, archived ($26) |
| Verifier: prior-art audit of four Eckert 1864 telegrams | Disprove the "not printed" claim; N0-N5 class per message; correct wording; CLAUDE.md rule 10 | Pushed: E6 N1 (OR I/32 pt 3 p.498), E12 N1 (in print since 1864; Basler CW 7:479), E4 N3, E5 N3; AUDIT.md written; over-claims corrected; verifier template added to CLAUDE.md | Done |
| Transcription + Reading: Eckert 1864 ledger with Cipher No. 1 | Twenty 1864 entries at grade H | Pushed 045fbe2: all twenty read cleanly (296 H, 8 C, 1 M, 0 I); four not found in the OR volumes checked | Interrupted 03:06 UTC, archived 03:15 (result pushed; it had started a duplicate audit, $189 of usage) | Archived |
| Access: HathiTrust dictionary search via browser (Wellington 1812) | Test tools/browser_fetch.js; run the DICTIONARY.md section 6 searches | Chromium blocked by proxy CA; HathiTrust APIs used; 19 editions, none match | Done, archived ($11) |
| Archive Lookup: Whitworth 1707 | Search-print check; list items; REQUEST.md | Only one clause of SP 91/5/108 unread; ciphers/whitworth-1707 committed | Done, archive |

## Environment

- Cloud environment "Default" now has full network access (changed 19 Sept 2026). New sessions can reach
  archives and Cryptiana. The original orchestrator container predates the change and cannot; it delegates.
- Repo conventions: CLAUDE.md. Workflows: .claude/workflows/check-solved.js and scout.js.
