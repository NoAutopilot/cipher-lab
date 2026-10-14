# LANE DEFAULT-account-1-20261014-1840 jobs (account 1, lane orchestrator session_01STU17qxn3D94dW5wmiCrfE) -- 14 Oct 2026 18:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 18:40 UTC 14 Oct - 04:40 UTC 15 Oct. Gate 0a: SESSION-SWEEP-account-1 stale-claimed
since 5 Oct (the 14 Oct 06:40 and 09:11 lanes proceeded the same way). VERIFY-BACKLOG.tsv (09:16): high rows Birago/ceppo (off limits), low
rows audit2 on N0/N1 items. Backlog = `next_steps.py --hot-only` runnable rows checked against the three 14 Oct lane handoffs' "next" lists.
Excluded: Birago family (birago-*, nevers-birago-*, ceppo-nevers-*), Armstrong, Debosnys, VIV-KEYSTONE (fr16104/fr16106), LANE BNF-FOCUS
holdings (fr3982, fr3985-3990, no.60), clair1161 (Lasry key failed twice: rule 3), fr2933 (waits on a person's look). No other ROOM claim
< 6 h without a done (read 18:4x). Keyed googleapis answered 200 at 18:4x UTC (503 most of 14 Oct): the parked Google Books steps go first.
Intake gate 18:4x UTC (tools/intake_gate_check.py, exit 0 each): thurloe-printed, eckert-1864, baluze167-davaux-1637, fr4712-nevers-duchesse,
clair571-estrades-1645, sforza-duke-1447-f15, fr4735-monluc-lansac-poland-1573, colbert26-lathuillerie-1644, fair-game-2010.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), plus the
"Images" and "Hosts" paragraphs of the "Common rules" section of `.claude/briefs/runs/2026-10-13-acct4-default-2135-jobs.md` and the "Hosts this
wave" paragraph of `.claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md` (openapi.bnf.fr; never gallica.bnf.fr), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A1-1840-14 (account 1)"; export `CIPHERLAB_ACCOUNT=account-1` before any tools/room.py call;
- per-job request limits are the ones stated in your job below; shared hosts carry `<host> take` / `<host> release` ROOM lines
  (openapi.bnf.fr, googleapis, de-crypt.org): if another worker holds one with no release in the last 30 min, work from disk and wait;
- halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before);
- `get_session` is not available to you: say "cost not visible to this session" in the done line;
- Google Books: `www.googleapis.com/books/v1` only, `&country=US&key=$GOOGLE_BOOKS_KEY`, >= 1.5 s apart; on 503/429 one retry after 60 s,
  then stop the host and log it. books.google.com page view is blocked from the cloud (host table): do not try it. Never print the key.
- No image file goes into git (manifest + regen command instead; `git status --short` before the final push).
- A worker reaching `partial` updates Remaining gaps / Escalation / Verdict and runs `tools/gaps_check.py <target>` before its done line.
- Solver jobs: report what was found and where it was not found; do not classify novelty. Never use the words solved, cracked, novel, first or
  new for anything this project did. Never call AskUserQuestion. Stop at 80% of cap or box. Read the clock with `date -u` before writing any time.

## Wave 1 (18:5x UTC 14 Oct)

### GB-PASS (Opus, cap 3, box 60 min, googleapis <= 60): the parked keyed Google Books steps for three folders
googleapis answered 200 at 18:4x after a day of 503. In this order, each with its own NOTES section and Verdict update:
(a) eckert-1864 -- Verdict: "the keyed googleapis pass for Grant Papers vol. 13 with a second-form control first, ~$0.1 (the 5914/2 page waits
on L79)". Read GB-2 and the GP13 sections first; run the second-form control, then GP13 E589-E592 only if it passes. NOTES "## GB-E13".
(b) thurloe-printed -- Verdict: "the Verbael date-phrase snippet queries (`gb2_verbael_snip.py`) on the two full-view ids GB-2 located
(vZzvg46MRdEC / T2JVAAAAYAAJ), ~$0.3": Beverning 27 June / 22 Aug 1653 and No. 37 pp.252-253. NOTES "## GB-VERB"; any snippet that carries
a cipher passage's clear text goes to a reading only through the folder's existing decode script (no new grades in this job beyond C for
tokens the print fills, with the snippet quoted).
(c) fr4735-monluc-lansac-poland-1573 -- MONL-PC (14 Oct) left Google Books 13 of 14 phrases unsearched (503). Re-run `tools/print_check.py`
(or the MONL-PC phrase list) against Google Books only. NOTES "## MONL-PC2"; a print-check "no hits" is a search result, never a novelty
verdict (rule 10). Stop the host for all three if it 503s again.

### SFZ-DEC2 (Opus, cap 3, box 60 min, de-crypt.org: one browser login, <= 50 requests): sforza-duke-1447-f15 DECODE scat. 1597 nos. 12-40
Verdict: "open DECODE scat. 1597 nos. 12-40 by heading (one login, ~45 requests), ~$2". Read SFZ-KEYS, OUT-CHECK-SFZ and SFZ-DEC first (the
heading method; nos. 1-11 and 78 already opened: agent keys). `tools/decode_browser_login.js`; scrub the account name from anything saved.
For each record: heading, date, correspondent, whether a Visconti / Barbavara / Aragon or 1446-47 key; if a 1446-47 key appears, compare its
sign stock with the f.15/f.5/f.8 inventory on disk (an overlap count with a shuffled control at most, no decode). NOTES "## SFZ-DEC2",
known-keys rung + Verdict (next band 41-114, and whether the ASMi request in REQUEST.md is still needed).

### BAL-LOOKS (Opus, cap 3, box 60 min, openapi.bnf.fr <= 20): baluze167-davaux-1637 two image checks
(a) Verdict: "the 167 c275/c283 image check (~$0.8)" -- read BAL167-FIN's section on the unglossed runs; look at both canvases at 1000-1600 px;
say whether each is cipher, what letter it belongs to, and whether a gloss or clear copy exists in the volume. (b) handoff of LANE
DEFAULT-A2-0911-14: "168 f.122 letter -- copy of or same matter as f.110 (image compare, ~1.5)": read BAL168-SWEEP/BAL168-FIN; compare the
f.122 (c258-262) glossed letter with the f.110 letter (sign sequence overlap from crops, gloss wording overlap); answer copy / same matter /
different. Price looks at ~0.15 each (BAL168-FIN). NOTES "## BAL-LOOKS", gaps + Verdict.

### CL571-417 (Opus, cap 2, box 45 min, archivesetmanuscrits.bnf.fr <= 15): clair571-estrades-1645 Clairambault 417 f.236 record
Verdict: "read the BnF catalogue record for Clairambault 417 f.236, ~$1". Read EST-9431 / EST-REG first (why f.236 matters). Use the BnF
archivesetmanuscrits finding aid (host table: page 1 by curl, a browser for more; run twice) and quote the record's wording and availability
flag with its URL/ark; if digitised and the ark is found, map f.236 with `tools/gallica_folio.py --iiif-host openapi` and look at one 1000 px
view (openapi.bnf.fr <= 5). NOTES "## CL571-417", Verdict.

### COL26-SIB (Opus, cap 7, box 120 min, openapi.bnf.fr <= 15): colbert26-lathuillerie-1644 key on one glossed sibling leaf at word grain
Verdict: "apply the f.23/f.24 key and sibling gloss values to one glossed sibling leaf (canvas 51, or 30/32) at word grain, two blind passes,
beside a shuffled-key and a synthetic code+mark control at the leaf's N, ~$6". Read COL26-C33, COL26-C51, COL26-WP, COL26-11B, COL26-42 first
(what is retired and why). Pick the leaf whose crops are already on disk if any; PREREG (statistic, both controls, gate) committed before
scoring; units priced per call: 2 blind passes + 1 reconciliation (~1.2 each) + the scoring. Grades change only if the gate passes. NOTES
"## COL26-SIB", gaps + Verdict, `decode_key.py ciphers/colbert26-lathuillerie-1644 --check` exit 0 if key/reading touched.

### F4712-C83 (Opus, cap 2.5, box 60 min, openapi.bnf.fr <= 16): fr4712-nevers-duchesse sibling census canvases 83-94
Verdict: "census of canvases 83-94 (f.71v onward) at 600 px via openapi.bnf.fr, ~$1.5". Follow F4712-C59/C71's method exactly (sizes, contact
sheet, what counts as a glossed sibling; 1600 px only for a cipher leaf). Census TSV rows, NOTES "## F4712-C83", siblings rung + Verdict
(next block 95-106). The fr4712 images/census/ tracked images are not this job's to remove.

## Wave 2 (as wave 1 reports; filled in below by the lane orchestrator)
