# LANE-VER1 (account 2) -- 5 Oct 2026 17:29 UTC (account-3 orchestrator; owner: "lets get things fired back up")
Standing verifier lane. Operating rules as `.claude/briefs/runs/2026-10-04-acct3-lane-near3-run1.md` para 1. Every worker's first
command: `git fetch origin && git checkout -B main origin/main`. Verifiers are fresh sessions, never the solver of the reading; use the
CLAUDE.md verifier template (rule 10, depth rule 4a). Opus 5.5 floor.
Queue: VERIFY-BACKLOG.tsv once LANE-SYS1 (account 1) pushes it; until then build the list yourself from PROGRESS.tsv: rows with
column 1 = x and 2 or C = '.', oldest first, N3+ candidates first (T = n). Known first candidates: Pisany f.302v / f.275v / f.247r
(known-answer PASS 4-5 Oct, text in Colbert -> N0/N1 by design: audit and record, they will not count), Gramont f.18r L11-L21 +
fr.3040 no.6 (N8/N9 PASS), Costabili 1491 (11 C confirmed), Noailles basin, Janssens Java, Schonenberg, Paget, Vivonne ink 53/54/63
(D1 -> can depth rise?), Clairambault 1161, Hellen R1953 (N4 needs GStA). For each: audit 2 or depth re-check, AUDIT.md + status.json
fields via tools/depth_check.py, SECOND-OPINIONS-QUEUE row at N3+. Also add the three Pisany pages to PROGRESS.tsv once audited.
Cap 60, box 600. Close with STATUS.md "LANE VER1 handoff" and one ROOM done line.
