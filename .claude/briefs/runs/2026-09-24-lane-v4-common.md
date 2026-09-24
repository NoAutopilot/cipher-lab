# LANE V4 verifier briefs, 24 Sept 2026 (common rules)

Orchestrator: the parent orchestrator (cipher-lab-7a), session_01EFmUvFAifLKGdBSsW9mjEG, acting as LANE V4. Template: `.claude/briefs/verifier.md` plus the Verifier
brief template in CLAUDE.md. You did not solve this target; you do not protect the solver's conclusions.

1. First action: `python3 tools/room.py --start`; read the last 30 lines of ROOM.md; claim with
   `python3 tools/room.py "<ROLE> (Opus, cap $N, for LANE V4, session <id from get_session or 'unknown'>)" "claim: <target> N-class audit -- files: ciphers/<t>/{AUDIT.md,NOTES.md}, status.json results row, JSTOR-QUEUE.tsv, SECOND-OPINIONS-QUEUE.tsv"`.
   Read `date -u` before writing any date.
2. Read CLAUDE.md rule 10, `.claude/briefs/verifier.md`, and the target's NOTES.md (source, reading, the solver's
   search log). Precedents: `ciphers/eckert-1864/AUDIT.md`, `ciphers/fr2980-gramont/AUDIT.md` (N4 decision table),
   `ciphers/clair1067-brienne-poland-1646/AUDIT.md` (interlinear decipherment on the leaf = N0 without print).
3. Do not decode or re-read the cipher. Do not touch other targets. Never print credentials.
4. Scripts read, models judge: fetch a volume's text once to your scratch dir, grep it, read only the hits. Phrase
   sweeps may go to at most 3 Sonnet subagents at once (`model: sonnet`); verdicts are yours.
5. Hosts, good-citizen rule: one request at a time per host, >=1.5 s apart (Google Books >=3 s, append
   `&key=$GOOGLE_BOOKS_KEY&country=US`, never print the key). Google Books and resources.huygens.knaw.nl may be used by a
   sibling verifier: before a batch on either host, grep the last 20 ROOM lines for a live `host:` claim on it; if
   another worker holds it, do other families first. Post `host: <host> <start|done>` lines. On 429/403/challenge,
   stop that host, log it, one retry after a pause at most. gallica.bnf.fr is LANE G2's: if you need a Gallica page,
   post `for LANE G2: <what>` and log the family as requested. archive.org full text: name the item in your claim line.
6. Output: `ciphers/<t>/AUDIT.md` with verdict table (N-class per item), per-item sections, a principal-families table
   (family / searched or unreachable / what / result), evidence table, "did we first-decipher?", confidence, one safe
   and one unsafe sentence per item, postmortem, corrections to over-claiming sentences in the folder (edit in place).
   JSTOR: one row per query appended to JSTOR-QUEUE.tsv (they never block a class). If any item is N3 or higher:
   write `ciphers/<t>/second-opinions/PROMPT-chatgpt.md` (self-contained: item, plaintext excerpt, what to look for,
   ask for exact citations) and append a `SO-<TAG>` row to SECOND-OPINIONS-QUEUE.tsv (label, folder, prompt, date,
   queued, empty). Update only this target's status.json results row: class and safe sentence in rule 10 wording.
   Set NOTES.md's status word only within the CLAUDE.md vocabulary.
7. Stop at the cap. Commit by explicit path, `git fetch origin main && git rebase FETCH_HEAD && git push origin main`.
   ROOM done line starting `for LANE V4:` with the class per item, commit, and request count per host. Report in five
   lines: first line the class(es). Per rule 10 you assign the class; in ROOM and the report use only the safe sentence.
