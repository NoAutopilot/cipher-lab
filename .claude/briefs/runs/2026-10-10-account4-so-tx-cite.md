# SO-TX-CITE: citation and claim check of the outside transcription review (account 4, Sonnet, cap USD 3, box 45 min)

Written 10 Oct 2026 00:3x UTC by date -u by the orchestrator (account-4). The owner's ChatGPT runner answered
second-opinions/prompt-2026-10-10-tx-external-opinion.md as PR 71 ([SO-TX-TRANSCRIPTION-2026-10-10]); its file is landed at
research/SO-TX-TRANSCRIPTION-2026-10-10.md. The second-opinions loop (CLAUDE.md "Operating model") requires a verifier to check every
citation. Job, read-only on the benchmark (open no truth file, no crop):
1. For each of R1-R7, fetch the cited page (arxiv, aclanthology, jmlr, dspace.ut.ee, github; one request each, 2 s apart, browser UA
   only where CLAUDE.md's host table says so) and check the specific figures the review attributes to it (R1: Copiale SER 11.4%, Borg
   23.6% at confidence 0.4 with five support examples; R2: Copiale 2.2% with 711 training lines, Borg 8.5% with 195; R3: Borg 6.6% at
   2,500 symbols, 4.26% at 10,000, Copiale 4.46% at 2,500, 90-95% location precision/recall; R4-R7 existence and relevance). Write a
   row per citation to research/SO-TX-TRANSCRIPTION-2026-10-10-CITES.tsv: ref, url, reachable (HTTP code), claim, verdict
   (confirmed / differs: <what the source says> / unreachable), where in the source.
2. Reproduce the review's three scorer findings on the current tools/tx_bench.py with its own synthetic snippet (section "Reproduction
   snippet"; the orchestrator already ran it at 00:3x UTC: missing line not charged (scored 1, lines_missing ['L2']); paired() ignores
   flags (fixed 1 vs 0 after drop_flagged); an insertion repair scores fixed 0 broken 0) and record the output in the TSV's last rows
   as claim/verdict pairs. Also test the review's case 5 (homophone credited) and case 6 (Wilson interval on rate 4.0) and record them.
3. Append one line to the landed file's head: "Citations checked <date -u> by SO-TX-CITE: <n confirmed, n differ, n unreachable>;
   see ...-CITES.tsv". No other edit to the review. Close PR 71 with a one-line comment naming the landed path (your token is fresh;
   the orchestrator's is not) -- only after the file is on main. ROOM claim/done lines "for orchestrator (account-4)"; stage by path;
   never force-push; never AskUserQuestion; never print credentials; requests per host in the done line.
