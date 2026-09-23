# Status board

One page, always current. The orchestrator session updates it after every worker reports. If you have lost
track, read this first, then QUEUE.md for what comes next.

Last updated: 23 September 2026, 19:21 UTC

> **the owner is away 21 to 28 September 2026. Read `HANDOFF-WEEK.md` first: it says what he must do before
> leaving, what a teammate can carry alone, and what waits. Anything blocked on a human is in `ASKS.md`.**

## Goal, restated by the owner on 23 September 2026, 17:20 UTC

**Maximise the number of unique solves. Nothing else is sacred.** A unique solve is a reading a separate verifier
classes N3 or better (rule 10). Consequences, applied the same evening:

1. **Recovery is the lane that scales.** The cached DECODE catalogue shows 202 Non-decrypted letters with a Decrypted
   or Partially decrypted sibling in the same shelfmark; 27 survive exclusion against both solver repositories and
   our own queue, in seven clusters (QUEUE.md "Neighbour-record recovery candidates", `tools/decode_neighbours.py`).
   Each is read by opening both records, transcribing, applying the sibling's decipherment as the key. Same-day
   turnaround matters because Bourdeau's project works the same catalogue.
2. **All readable languages count.** The English-only reader profile was discarding most candidates (none of the 27
   survivors is English). QUEUE.md's profile, scout.js and the scout brief now score any language the models read
   at language_fit 3. Existing rows are under-scored for other languages until ASSIGNMENTS row 8 re-scores them.
3. **Cryptanalysis only with a control and a route nobody tried.** Ciphertext-only work on material the two
   solver projects already annealed is the lowest-yield lane (Sforza 1446 today: clean negative).
4. **The archive-order lane stays** (Hamilton, Stair, NLS 20769, Monck) because nobody else pays for copies, but it
   is one solve a month at best; it should never block the pipeline above.
5. **Rules 1, 3, 4 and 10 are unchanged.** "Unique" is the verifier's word, so the pipeline ends in AUDIT.md every time.

Pipeline per cluster: check-solved (editions first: Nuntiaturberichte, CODOIN, calendars) -> DECODE login, open
letter and sibling -> two transcription passes -> key from the sibling, read -> verifier -> board. Blocked at the
second step until ASKS rows 1, 10 and 11 are done.

**18:15 UTC, 23 Sept: the lane that is ours.** The non-DECODE catalogue scout returned 493 items with cipher in TNA
Discovery, BL Archives and Manuscripts and Gallica that neither solver project names (QUEUE.md "Candidates not on
DECODE", N1-N19 scored). The top three carry their key in the same file: Mornington's 1798-1800 despatches with two
copies of the key (BL Mss Eur D623), the 1722 intercepts with cipher-key pairs (TNA SP 35/36), and Courten's diary with
Madden's key (BL Add MS 4956). Check-solved is running on those three; the edition risk is real (the Wellesley
despatches were printed 1836-37). Policy under the unique-solves metric: such items are kept, not dropped as editions,
and the verifier decides. Each will need an imaging order, so the person's card fills once they pass stage 2.

**19:00 UTC, 23 Sept: Bowes 1583, the night's one reading, verified N1.** A solver aligned Tomokiyo's transcription of
eleven cipher fragments with Bowes's letter-book copies printed in 1842 and recovered a sign table that reads 93 of 101
tokens (S 82, M 8, I 3) as the printed names. The verifier found the plaintext in print since 1842 and the leaf itself
calendared in CSP Scotland vi (1910) with every name in clear, so the class is N1, possibly N0 once one calendar page
is read. Not a unique solve; a sign table to hand to Tomokiyo. Two lessons went into the templates: run the HTRC
word-count test on a blocked calendar before setting stage 2, and view the leaf before scoring a catalogue hit.

**19:21 UTC, 23 Sept: wake closed.** The non-DECODE lane delivered the night's stage-2 targets: of fifteen scored
rows, seven are verified unsolved with a copy route (Mornington, Courten, the SP 87 Seven Years War campaign, SP 78
France 1642-57, SP 90/2 1704, SP 87/13 1743, SP 87/23 1747), eight dropped or partial. Four requests are drafted
(Mornington, Courten, SP 78; the SP 87 decision) and six rows sit on the owner's card (ASKS 12-16). 474 survivors of
the catalogue scout are still unscored (ASSIGNMENTS row 13). The DECODE login test and the JSTOR pass wait for a
session that sees the credentials. Nothing was solved; Bowes 1583 is N1. Session usage about 90 for the orchestrator
and nineteen workers.

**Next session on this account, first actions (written 18:02 UTC, 23 Sept 2026).** (1) Presence test of the seven
variables with `test -n`, no values printed. (2) One DECODE login attempt via `tools/decode_fetch.sh 8725 ...`; on
success, ASKS row 1 to done and ASSIGNMENTS row 7 starts (record 8725, then a polite full catalogue pull to
`sources/decode/`, then the neighbour tool on the whole catalogue). (3) One archive.org login attempt via
`tools/ia_borrow.py` on a named page check (ASKS row 2). (4) Read the three worker reports of the night (non-DECODE
scout, Burgess 1912, Bowes 1583) in ROOM.md and the target NOTES, and pick from the new QUEUE sections. The
good-citizen rule in the Access playbook applies to every request.

**Correction, 17:29 UTC.** Re-running the exclusion by volume as well as by id shows Bourdeau's repository already
names 193 of the 202 neighbour pairs in the cached catalogue, and D1 (Pallotto) is found-solved (key broken 2018,
printed edition). Five pairs survive (D8, RAH 9/29), in a volume between two he is reading. So the cached-catalogue
neighbour lane is not ours. What is: (a) the full DECODE catalogue behind the login, which the scrape does not cover;
(b) archives not on DECODE at all, where the two projects do not look (Gallica beyond his BnF picks, BL and TNA
series, NRS, county record offices, dealers), reached by the access playbook and copy orders; (c) the four archive
requests already drafted. The count-maximising plan is therefore a scout on non-DECODE catalogues (TNA Discovery
"cipher" hits, NRS, BL Explore, Gallica full-text for "chiffre" with no DECODE record), which needs the network fix.

## Handoff to the next orchestrator (21 September 2026, 03:00 UTC)

Read this, then CLAUDE.md, then the target table below. Everything you need is in the repository; nothing
important lives only in the previous session's conversation.

**What this project is.** Read old ciphered letters nobody has read. The bottleneck is access, not
cryptanalysis: the online material has been swept by two well-funded AI projects, so our lane is the paper in
archives. README "What counts as a result" defines the three kinds (recovery, cryptanalysis, contribution)
and every board card carries one.

**Where to look.** `STATUS.md` (this file) is the human board. `status.json` feeds `dashboard.html`, published
at https://claude.ai/artifact/Mbveo2jWKwmA7RTqBuCkis (owner's account) and, from the noautopilotytbiz account, at
https://claude.ai/artifact/HzYszSGfSoWPsYXpxvM5zr (published 23 Sept 2026; each account can only republish its own);
rebuild with `python3 tools/build_dashboard.py` and republish to your account's URL after every worker result.
docs/index.html is the same page for GitHub Pages (ASKS row 8). `CLAUDE.md` holds the ten rules, the Pipeline, the Usage
section (model tiering; Sonnet for search and transcription, the top model for reconciliation, verifier and
orchestration), the Access playbook and the Improvement loop. `ROOM.md` is the workers' shared channel.
`LEDGER.md` is one row per worker with cost and outcome. `QUEUE.md` is the ranked queue; `.claude/briefs/`
holds the role templates.

**The two rules that were learned the hard way.** Rule 10: a solver may never call anything new or
unpublished; only a separate verifier, after a logged search, assigns an N-class. And no copy order, payment
or quote request reaches the owner until a check-solved sweep has set that target to stage 2.

**Orchestrator change, 23 September 2026, 15:20 UTC.** The previous orchestrator's account is logged out; a fresh orchestrator on the noautopilotytbiz account took over from this handoff, with nothing unpushed on the old account. That account's environment has no credentials set (ASKS.md row 10), so this orchestrator runs only credential-free jobs: Randolph 1570 native-resolution re-transcription (ASSIGNMENTS row 1) and a check-solved sweep on queue ranks 11, 13, 15, 17, 18 (row 3). The Google Books print checks (row 2) wait for an account with the key.

**23 September 2026, 16:40 UTC, what happened next.** Two workers reported. (1) Check-solved on queue ranks 11, 13, 15, 17, 18: Charles I to Rupert 1645 was read by Bourdeau on 21 Sept with Lasry's King-Queen key (dropped, found-solved); Harley 287 is mostly read by Bourdeau since 21-22 Sept (partial); Catokwacopa 1875 partial with no unique plaintext recoverable; Burgess 1912 and Bowes 1583 open at stage 2. (2) A sibling sweep for Randolph 1570 found that the next leaf, f.278 (DECODE R4932), is a clerk's contemporary decipherment, read by Bourdeau on 21 Sept, and that Boyd's 1903 calendar already says "partly in cipher, deciphered". Randolph is dropped as found-solved; the transcription worker was stopped and its crops are kept for the record. Lesson written to LESSONS.md: open every neighbouring DECODE record with the same shelfmark, and re-clone the solver repositories before every campaign, because Bourdeau's project read three of our queue items in two days.

**Blocked on the owner, new:** this account's environment has no credentials (ASKS row 10) and its network policy denies every archive host: archive.org, bl.digirati.io, hathitrust.org, wikisource.org, gutenberg.org, de-crypt.org, scienceblogs.de (ASKS row 11). From this account only github.com, pypi.org and googleapis.com are reachable, so no access, print-check or image work can run here until the environment's Network access setting is changed. The owner's steer for the week is one cipher solved that a verifier can class N3 or better; with the archive lane closed from this account, the only candidate with material obtainable is Burgess 1912, and its text is on Wikisource and Internet Archive, both blocked.

**15:49 UTC.** The queue was diffed against fresh clones of both solver repositories with the new `tools/solver_repo_diff.py`: four more rows had been solved years ago and are dropped (Boswell 1628 solved 2021, Goring 1645 solved 2020, Sadler 1559 printed 1809, Anne 1711 printed), five are partly read by Bourdeau (ranks 7, 8, 19, 20, 35). The Randolph worker stopped and committed 49 native crops. DECODE record R413 is no longer needed (ASKS row 1 updated).

**15:59 UTC.** The harvest (QUEUE.md "Candidates held on GitHub", 12 rows) gave one genuine cryptanalysis candidate reachable from here: the Sforza-Maino 1446 pair, BnF italien 1583 ff.68 and 70, which Bourdeau closed unread after annealing each letter alone; the joint anneal as one shared key was never tried. Check-solved: open at stage 2, conditional on DECODE, Gallica and Cerioni being unreachable from this account. Lope Hurtado 1522 was left alone as Bourdeau's live target.

**16:46 UTC, end of this orchestrator's wake.** The Sforza-Maino solver finished: four matched synthetic pairs of the same design read at 99% or better, the real pair cleared its shuffled baseline by 0.2-0.4 nats against 1.8-2.0 for the controls, no token claimed. Closed-negative, conditional on Bourdeau's draft transcription, since no image is reachable from this account. Reusable tooling landed in tools/ (joint nomenclator annealer, 15th-century Italian model). Nothing was solved today.

**What the owner's steer needs next.** One cipher solved that a verifier can class N3 or better is not reachable from this account as configured: every archive host is blocked (ASKS row 11) and no credentials are set (row 10). Once either is fixed, the order of attack is: (1) Burgess 1912, text on Wikisource, stage 2, untested acrostic families named in its NOTES; (2) Bowes 1583, search-print in CSP Scotland vi, then BL images; (3) the Sforza pair re-transcribed sign-exact from the Gallica image and rerun through run_target.sh; (4) the harvest rows G1 and G2 only if Bourdeau has stopped on them (re-run tools/solver_repo_diff.py first). Spink lot 1184's question lapsed with today's sale; the images were saved on 19 Sept.

**Running right now (16:46 UTC):** nothing. Erving 1807 was found already printed and dropped; Randolph 1570 has images and a first-pass transcription but no key, and is queued behind the owner's credential fix.

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

**Stops and costs.** All sessions were stopped by the five-hour usage limit from 00:03 to 18:43 UTC. Worker
usage tonight, in dollars of plan usage (not billed): Eckert 1864 reading 189 (over-ran its brief), verifier
28, key test 26, HathiTrust 11, check-solved sweep 18, scout 6, print check 2, access tests 1, plus the free
work in progress. Orchestrator session 2,042 since 17 Sept. **Nothing here is billed:** this runs on a Max subscription, and these figures are the API-equivalent value of the tokens consumed, which is how the session record reports them. What they measure is how fast a session eats the plan's rate-limit window. The orchestrator is one long session with 3.6 billion cached tokens read, so it consumes more of the window than every worker combined, which is what caused the 00:03 to 03:00 UTC lockout on 20 September. See LEDGER.md.

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
| Thomas Randolph to Sussex, 1570 | ciphers/randolph-sussex-1569 | **Found-solved, 23 Sept 2026.** f.278 is a clerk's contemporary decipherment (DECODE R4932), read by Bourdeau 21 Sept; Boyd 1903 no. 339 says 'deciphered'. Images, 49 native crops and two raw passes kept for the record; dropped from the queue | found-solved |
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
