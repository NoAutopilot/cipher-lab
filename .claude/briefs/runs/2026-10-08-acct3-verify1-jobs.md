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
