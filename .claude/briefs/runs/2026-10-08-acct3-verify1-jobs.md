# LANE-VERIFY-1 job briefs (account 3, session_01RQfe5hVN5keS2RuSSifTnf), 8 Oct 2026 from 15:59 UTC
Lane brief: .claude/briefs/lane-verify.md (+ lane-common-blast.md). Every job here: Opus 5.5 verifier, a session separate from every
solver and first auditor of its items, not protecting their conclusions. Common tail for every job:
- Start: `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`; read the last 30 ROOM lines;
  `python3 tools/work_queue.py --claim <JOB> --session <your session id>` if your row is queued; one ROOM claim line (cap, box end).
- Prior work: run `.claude/briefs/prior-work-step.md` (if `tools/prior_work.py` exists use it, else checks 1, 3, 4 and 5 by hand) per
  item, and log every check (route, query, result, or "unchecked") in your AUDIT.md section under "Prior-work checks 3-5" -- this is
  the search-family log later gates will read. Check 5 (G3, the decoded-phrase re-search incl. same-day replies, other
  correspondents' versions and the press of the day) is mandatory before any N3+ sentence.
- Verifier template: CLAUDE.md "Verifier brief (template)" verbatim; depth under .claude/briefs/runs/2026-10-08-acct3-depth-bar.md
  (keep or lower; never raise without the check). Rule 10 and 4a wording only.
- Write your section into the target's AUDIT.md, update status.json rows (rebase first; `audit_status`, class, depth fields), any
  SECOND-OPINIONS-QUEUE.tsv row already filed for the item (correct it if a class or count changed; a verifier giving N3+ appends one).
- Good-citizen rule and the CLAUDE.md host table; one request at a time per host, >=1.5 s apart; report requests per host.
- Before the push: `python3 tools/file_shrink_guard.py <every file touched>`; push with `python3 tools/room.py --push <paths>`;
  `python3 tools/work_queue.py --done <JOB>`; one ROOM done line "for LANE-VERIFY-1 / acct3-orchestrator" with what changed.
- Stop at 80% of cap or box before starting a new item. Do not decode, do not touch other targets or other items.

## V1-KNOWN (account 3), cap $8, box 90 min. Second audits of the 16 VERIFY-BACKLOG audit2 rows already at N0/N1
Units: 16 items, about $0.45 each (print citation open + one holder check), plus one reconciliation unit. These are record
corrections, not novelty work: confirm or correct the class and cite the print at the page.
- eckert-1864 N2-L (first audit AM-ECKV, account 2), N2-N N2-O N2-P N2-Q N2-S N2-U (ECK64-NO2 verifier, account 1), N2-AZ N2-BA
  N2-BB N2-BC N2-BD N2-BE N2-BF (D4-VP2, account 4): open the cited OR / PUSG page (IA djvu text, fetched once to scratch) and diff
  the print against reading-no2.md's derived text; check the Huntington CONTENTdm `transc` field for the pointer (a public
  transcription carrying the clear body makes it N0 for that body). N2-AZ: establish the PUSG vol. 11 page if possible. N2-Q: confirm
  the "Ann Apple is" correction was applied in reading-no2.md, else name it as still pending. One section "## AUDIT 2 (second
  adversarial, V1-KNOWN)" covering all 14.
- nla-heinrich-braunschweig-1519 (R9-NLAV, N0, key archival): confirm N0 basis (Grein's key sheets / transcription) and depth D2 under
  the depth bar.
- colbert26-lathuillerie-1644 (DA1-COLV + addendum D2V-COL26, N0, D1): confirm N0 (period gloss on the leaf) and D1 with the
  D2V-COL26 grade change carried.
- Set each status.json row's `audit_status` to "two audits" and PROGRESS.tsv `2` where a row exists (Birago rows are off limits:
  skip birago-fr3252-1571-72 entirely).

## Second wave (16:1x UTC): one-audit N3 items from the lane's inventory (every N3 D2+ item already has two audits)
Per item: a second adversarial audit with the common tail, section "## AUDIT 2 (second adversarial, <JOB>)" (or "AUDIT 4" where the
folder numbers them), the families the first audit did NOT cover searched first, then prior-work check 5 (G3) on the decoded text
itself -- "a search section exists" is not G3; log the phrases actually run. Units about $2.5 per item + one reconciliation unit.

## V1-OLD (account 3), cap $6, box 75 min: na-oldenbarnevelt-2442-1605 leaves 4/5/7 (ff.59v-62r, 729 cipher words)
First audit: AUDIT 3 (OLD-SIBS-V, account 2); reader OLD-SIBS (account 4). N3 D1. Check the Oldenbarnevelt retroboek (Huygens,
toc1 + full-text search, CLAUDE.md host table) and the recipient side; re-derive with the folder's --check; depth under the bar.

## V1-O9 (account 3), cap $6, box 75 min: eckert-1864 O9-AI, O9-AJ
First audit LS-V6 (account 1); reader LS-R6 (account 1). N3 D1; the press of the day was NOT read (gold/coin shipment orders: read
Chronicling America for the dates +-3 days, OR ser. I/III and the Treasury side). Also, a record fix only: status.json row for E70
still says N3 while AUD2-LS-H lowered it to N2 -- correct that row (cite AUD2-LS-H), nothing else on E70. File a status.json result
row for O9-AI/O9-AJ only if the class stays N3+ and depth reaches D2 (else none, as now).

## V1-1862 (account 3), cap $6, box 75 min: eckert-1862 4982.1 and 4992.3 (code word "Sermon = Bowling Green")
First audits LS3-V62 (account 2) and VERIFY-ECK (account 4). 4992.3 G3 unclear: run it. Correct the queued SECOND-OPINIONS-QUEUE row
for 4992.3 if the class moves.

## V1-F4712 (account 3), cap $5, box 60 min: fr4712-nevers-duchesse f.10r (six tokens carried from the f.13r gloss)
First audit D2V-F4712 (account 2); reader D2-F4712 (account 2). G3 was not run (shelfmark/subject searches only): run it on the six
tokens' phrase context, the Nevers printed correspondence and Tomokiyo's cached pages. Correct the queued SO row if the class moves.

## Re-addressed (not run on account 3): AUD2-ES132 -- es132-vargas-mexia-1578 f.89 and f.119 unprinted paragraphs (N3 D1) were
first-audited on account 3 (A3V2-ES132A1, 4 Oct), so their second audit goes to account 4 under this same common tail.

## V1-LS4A (account 3, 16:2x UTC), cap $11, box 95 min: eckert-1864 E90, E92, N2-BZ part 2 (LS4-V1a, account 1) and N2-BY (LS4-V2a, account 1)
Readers LS4-R1a / LS4-R2a, first audits LS4-V1a ("## AUDIT" section, commit b74a0a41) and LS4-V2a (commit 911d41da), all account 1;
classes N3 weak, depths E90 D3, E92 D2, N2-BZ pt 2 D2, N2-BY D3. Shape: .claude/briefs/runs/2026-10-08-acct3-aud2-ls.md (per-entry
steps) plus this file's common tail. Families the first audits named as unread go first: the Grant Papers footnotes (Google Books
snippet search reaches PUSG vol. 13, LS4-V2a's lesson; msstate is Cloudflare), the Huntington's own transcription of each pointer and of
same-leaf siblings, and the press of the day (Chronicling America, +-3 days). G3 on each decoded body. Units 4 x $2.5 + 1 reconciliation.
Update the four status.json rows (`audit_status` "two audits" or the lowered class) and SO-ECKERT-E90/E92/N2BZ2/N2BY rows if a class moves.

## Third wave (16:4x UTC): G3 checks (prior-work-step.md check 5) on two-audit eckert-1864 N3/N4 items whose audits log no
item-level decoded-phrase re-search (lane inventory, keyword-level). A G3 job is not a full third audit: per item, take the decoded body
from reading*.md, run tools/print_check.py with its distinctive phrases plus same-day replies/antecedents (OR ser. I-III and ORN by date
+ both correspondents, Grant/Lincoln papers incl. PUSG notes via Google Books snippets with country=US), the Huntington transcription of
same-leaf siblings, and the press of the day (Chronicling America +-3 days; loc.gov answered 403 to V1-1862 at 16:2x -- one try, log it
unreachable if so). SUBSTANCE (two rare entities or numbers shared within +-3 days) is diffed; a print hit lowers the class. Write one
section "## G3 check (<JOB>)" in AUDIT.md: per item, phrases run, hosts, result, class kept/lowered; update status.json and SO rows only
where a class moves. Skip (and say so) any item whose reading or audit ran on account 3. Units about $1.2 per item + 1 reconciliation.

## V1-G3A (account 3), cap $9, box 80 min: E5, N2-M, N2-T (the N4s: outward wording rests on them), N2-R, N2-AI, N2-AJ
## V1-G3B (account 3), cap $5, box 55 min: N2-BM, E78, O9-BB

## Fourth wave (16:5x UTC): G3 checks (Third wave paragraph applies, minus the eckert-specific routes) on non-eckert two-audit items:
the N4s first (outward wording rests on them; their audits predate the 8 Oct G3 rule), then N3 at D2+. Per item use the folder's
reading file and the family adapter in prior-work-step.md (Dutch: WVO print codes + Huygens retroboeken; French embassies: Négociations/
Correspondance + Tomokiyo; German: Acta Borussica etc.; Spanish/Flemish: Gachard, CSP Spain). Section "## G3 check (<JOB>)" in each
AUDIT.md. Skip any item whose reading or an audit ran on account 3 (say so). Units about $1.3 per item + 1 reconciliation.

## V1-G3C (account 3), cap $7, box 75 min: august-van-saksen-1561-64 WVO 126 postscript, WVO 53 postscript, WVO 57 enclosure (N4);
lodewijk-van-nassau-1573-74 WVO 4610/4611/4616 and WVO 5797 p5/p7 (N4)
## V1-G3D (account 3), cap $7, box 75 min: fr20140-danzay-1557 f.35r-36r (N4); fr2980-gramont f.29r no.21 and f.30r-v no.22 (N4);
fr3416-nevers-fils-1589 f.35r (N4); sachsstaatsarchiv-manteuffel-1712 694/08 f.410 lower block (N4)
## V1-G3E (account 3), cap $7, box 75 min: huntington-blathwayt-madrid-1728 BLA 186 (N4); antt-linhares-chave m0002 (N3 D2);
jan-van-nassau-1572-75 WVO 5551 (N3 D2); decode-2678-bnf-colbert127-gravel-1665 (N3 D2); vanbeuningen-dewitt-1657 item 2 (N3, no depth:
rule its depth under the bar as part of this check)

## Re-addressed (not run on account 3): G3-FR3416 -- fr3416-nevers-fils-1589 f.35r (N4) G3 check per the Fourth wave paragraph; its
reading (NV02-READ) and audit (VERIFY-NV02) ran on account 3, so the check goes to account 4. Cap $2.5, box 35 min.
