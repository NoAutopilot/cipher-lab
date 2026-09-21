# Status board

One page, always current. The orchestrator session updates it after every worker reports. If you have lost
track, read this first, then QUEUE.md for what comes next.

Last updated: 21 September 2026, 03:00 UTC

## Handoff to the next orchestrator (21 September 2026, 03:00 UTC)

Read this, then CLAUDE.md, then the target table below. Everything you need is in the repository; nothing
important lives only in the previous session's conversation.

**What this project is.** Read old ciphered letters nobody has read. The bottleneck is access, not
cryptanalysis: the online material has been swept by two well-funded AI projects, so our lane is the paper in
archives. README "What counts as a result" defines the three kinds (recovery, cryptanalysis, contribution)
and every board card carries one.

**Where to look.** `STATUS.md` (this file) is the human board. `status.json` feeds `dashboard.html`, published
at https://claude.ai/artifact/Mbveo2jWKwmA7RTqBuCkis; rebuild with `python3 tools/build_dashboard.py` and
republish to that same URL after every worker result. `CLAUDE.md` holds the ten rules, the Pipeline, the Usage
section (model tiering; Sonnet for search and transcription, the top model for reconciliation, verifier and
orchestration), the Access playbook and the Improvement loop. `ROOM.md` is the workers' shared channel.
`LEDGER.md` is one row per worker with cost and outcome. `QUEUE.md` is the ranked queue; `.claude/briefs/`
holds the role templates.

**The two rules that were learned the hard way.** Rule 10: a solver may never call anything new or
unpublished; only a separate verifier, after a logged search, assigns an N-class. And no copy order, payment
or quote request reaches the owner until a check-solved sweep has set that target to stage 2.

**Running right now** (independent sessions; collect them with get_session, then fetch main and read what they
pushed): Erving to Madison 1807, session_01823ERYCU9Fy2t858YsWL11. Randolph to Sussex 1569,
session_01F6AEdCy2oGSwrJX2Pa4rPH. Both Sonnet, capped about $12, started 02:58 UTC.

**Waiting on the owner:** rotate the DECODE and archive.org passwords (both were printed into worker
transcripts on 20 Sept) and set IA_USER to the account email; email Spink before the 23 Sept sale; the Kansas
order for Stair; an NLS quote and five-leaf sample for MS 20769; a British Library quote for Monck.

**Waiting on archives:** National Records of Scotland (Hamilton key sheets), The National Archives (Stepney
page check, order 3660178), the Huntington (corpus enquiry sent 20 Sept).

**Standing routines:** weekly retrospective, Mondays 06:00 UTC, emails five proposed changes and a
cost-per-result verdict. Breakthrough alert, fired on demand. Morning summary, as scheduled.

**Cost note.** The previous orchestrator ran from 17 to 21 September and reached $2,042 of plan usage, more
than every worker combined, because one long session re-reads its whole history. Prefer a fresh orchestrator
session every few days over one that runs for ever.

## Overnight summary, 19-20 September 2026 (written 05:15 UTC, completed 06:12 UTC)

**Nothing was cracked.** One over-claim was caught and turned into a rule; two archive orders are out; three new
targets are filed with requests drafted; the browser fix works in every new container.

**Done tonight**

- Eckert 1864: twenty entries read at grade H from the surviving Cipher No. 1 book; the "four not printed" claim
  was audited by a separate verifier and withdrawn (E6 and E12 were in print, N1; E4 and E5 no prior print
  located, N3; AUDIT.md). A key test then showed the headquarters entries are Cipher No. 2 and the Huntington's
  copy reads them (outcome A). Every cipher in the ledger reads from a surviving book: Eckert is parked as an
  edition, and an enquiry went to the Huntington curator about a corpus dataset.
- Process: CLAUDE.md rule 10 (novelty is a verifier's verdict, N0-N5), a Usage section (model tiering, scripts
  over reading, caps), a Pipeline section (scout, check-solved, board, access, solver, verifier, result
  label), an improvement loop (LEDGER.md, brief templates in .claude/briefs/, weekly retrospective every
  Monday 06:00 UTC), a board stage "Novelty verified", kind labels on every card, and the scout rubric's
  new "unread" axis so editions never top the queue again.
- Wellington 1812: HathiTrust half of the dictionary hunt closed negative through the Bibliographic and
  Extracted Features APIs (19 more editions, 76 in all). Blind sweep set the status to partial (Hayes, Lasry,
  Tomokiyo published a partial solution of the system).
- Blind six-source sweep of the board: Hamilton and Stepney offline-only, Whitworth and the 1646 intercepts
  open, nothing already solved anywhere.
- Three new targets verified and filed with REQUEST.md: Stair to Townshend 1710 (Kansas; not in print, so the
  order stands), Monck 1660 (BL), NLS MS 20769 (catalogue record confirmed: 57 leaves, "written in cipher",
  language undetermined, deposited 1949). BL Add MS 72438 f.104 folded into the 1646 target; DECODE marks it
  Decrypted, to be read with the DECODE login.
- Access: the environment setup script now adds the proxy CA to Chromium in every new container (tested);
  NLS is Cloudflare-challenged even so, read via a Wayback capture.
- Free work, 05:02-05:20 UTC, all on Sonnet for about $13 together: (1) print checks found no printed decipher
  or key for Hamilton, the 1646 intercepts or Monck (Burnet 1677 and Google Books were unreachable, so those
  are unchecked, not negative); the archive orders stay the route. (2) A search-print sweep showed three queue
  items already in print in clear (Moray regency 1568-69 in CSP Scotland ii; Throckmorton 1559-63 in Forbes
  1740-41; Sadler 1543 in Clifford 1809): dropped as found-solved, which is a contribution. Rupert 1645 and
  Cornwallis not found; Wotton 1585 and Bowes 1583 sit behind the British History Online paywall; Cobham 1588
  half checked. (3) The queue was re-scored with the unread axis: 39 rows tiered, Eckert dropped as an edition,
  top ten now 1646 intercepts (40), Wellington (40), Hamilton (39), Whitworth (37), Boswell 1628 (36),
  Cornwallis (36), Cecil correspondents (36), Walsingham-Wotton (36), Erving 1807 (35), Randolph 1569 (35);
  every one recovery except Whitworth (contribution). Three of the ten need only the DECODE login to start.

**Waiting on you**

1. Email Spink before 23 Sept: does lot 1184 include a pocket dictionary?
2. Kansas order for Stair MS P556, four scans, about $20 (ciphers/stair-townshend-1710/REQUEST.md).
3. BL Imaging Services quote for Add MS 32093 f.423 (ciphers/monck-1660/REQUEST.md).
4. NLS quote and a five-leaf sample of MS 20769 (ciphers/nls-20769/REQUEST.md).
5. Environment variables DECODE_USER and DECODE_PASS; optionally GOOGLE_BOOKS_KEY; the Gmail connector.

**Waiting on archives:** NRS (Hamilton key sheets), TNA (Stepney page check, order 3660178), the Huntington
(corpus enquiry).

**Stops and costs.** All sessions were stopped by the five-hour usage limit from 00:03 to 03:00 UTC. Worker
usage tonight, in dollars of plan usage (not billed): Eckert 1864 reading 189 (over-ran its brief), verifier
28, key test 26, HathiTrust 11, check-solved sweep 18, scout 6, print check 2, access tests 1, plus the free
work in progress. Orchestrator session 2,042 since 17 Sept (corrected 20 Sept 18:30 UTC; the earlier figure of 250 in this file was wrong). It is one long-running session with 3.6 billion cached tokens read, so it costs more than every worker combined. See LEDGER.md.

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
| NLS MS 20769, 18th-c. cipher manuscript | ciphers/nls-20769 | Record read 20 Sept 2026: 57 leaves, "written in cipher", genre Ciphers. Codes., language undetermined, deposited 1949 | You: ask NLS for a quote and a five-leaf sample (REQUEST.md) | You |
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
| Access Test: browser tool after the setup-script fix | Prove the fix in a fresh container; read the NLS record | Fix works; NLS record read via Wayback (live site Cloudflare-challenged) | Done, archived ($1) |
| Check Solved: blind six-source sweep of five targets | check-solved workflow, Sonnet | Hamilton, Stepney offline-only; Whitworth, 1646 open; Wellington partial. Nothing found solved | Done, archived ($18) |
| Key Test: Eckert 1864 headquarters cipher (mssEC 47-48) | Test Cipher No. 2 on the Beckwith/Kimber entries | Outcome A: mssEC 47 reads them at grade H; key-no2.md, reading-no2.md | Done, archived ($26) |
| Verifier: prior-art audit of four Eckert 1864 telegrams | Disprove the "not printed" claim; N0-N5 class per message; correct wording; CLAUDE.md rule 10 | Pushed: E6 N1 (OR I/32 pt 3 p.498), E12 N1 (in print since 1864; Basler CW 7:479), E4 N3, E5 N3; AUDIT.md written; over-claims corrected; verifier template added to CLAUDE.md | Done |
| Transcription + Reading: Eckert 1864 ledger with Cipher No. 1 | Twenty 1864 entries at grade H | Pushed 045fbe2: all twenty read cleanly (296 H, 8 C, 1 M, 0 I); four not found in the OR volumes checked | Interrupted 03:06 UTC, archived 03:15 (result pushed; it had started a duplicate audit, $189 of usage) | Archived |
| Access: HathiTrust dictionary search via browser (Wellington 1812) | Test tools/browser_fetch.js; run the DICTIONARY.md section 6 searches | Chromium blocked by proxy CA; HathiTrust APIs used; 19 editions, none match | Done, archived ($11) |
| Archive Lookup: Whitworth 1707 | Search-print check; list items; REQUEST.md | Only one clause of SP 91/5/108 unread; ciphers/whitworth-1707 committed | Done, archive |

## Environment

- Cloud environment "Default" now has full network access (changed 19 Sept 2026). New sessions can reach
  archives and Cryptiana. The original orchestrator container predates the change and cannot; it delegates.
- Repo conventions: CLAUDE.md. Workflows: .claude/workflows/check-solved.js and scout.js.
