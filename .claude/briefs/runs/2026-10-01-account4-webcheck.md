# WEBCHECK-<target>: the open-web and blog comment-thread check the intake gate now requires (one target per worker)

Written 1 Oct 2026 23:5x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme). One session per
target; the session's prompt names the target. Role field for ROOM.md lines: `WEBCHECK-<target> (account-4)`.
Model: Fable 5.1 (Opus 5.5 if Fable fails). Cap: USD 3. Box: 30 minutes. Hosts: web search plus the three blogs and
whatever a hit links to; one request at a time, >= 1.5 s apart; stop on any 403/429/challenge and log it.

## Why

`python3 tools/intake_gate_check.py <target>` exits 1 on these folders only because their check-solved verdict predates
the 28 Sept 2026 CHECK-SOLVED-WEB rule (`.claude/briefs/check-solved.md`, "Required step: Open web and blog comment
threads"): spinelli-beinecke-c1515 was closed N0 because its letter had been read in a Cipherbrain comment thread. No
deep work may be briefed on these targets until the gate passes.

## The job

Do exactly the required step, for the one target named in your prompt, and nothing else:
(a) at least four plain web searches -- sender + recipient + date; shelfmark + "cipher"/"chiffre"/"cifra"/"Chiffre"
    (the document's language); the most distinctive clear-text or decoded phrase in quotes (take it from the folder's
    ciphertext/reading/NOTES files); the folder's own descriptive title;
(b) a site search of each of the three blogs by name: Cipherbrain (scienceblogs.de/klausis-krypto-kolumne), the
    Cryptiana blog (cryptiana.blogspot.com, and Tomokiyo's cryptiana.web.fc2.com pages -- grep the on-disk snapshot
    `sources/cryptiana/` first, zero requests), and Cipher Mysteries (ciphermysteries.com);
(c) open every plausible hit and read its comment thread, not only the post.
Also (check-solved.md): search the cipher's name with "solves" and "Claude" or "GPT" (model-solve announcements).

Log every query and every hit (URL, date, what it says about THIS letter) in a section at the end of NOTES.md headed
exactly `## Web and blog check (WEBCHECK-<target>, 1 Oct 2026)`. If any hit carries a decipherment or plaintext of the
item: the status word on line 1 becomes `found-solved`, line 2 names the source and date, and you say in the done line
that any later reading is N0 -- quote the hit's own sentence about this letter verbatim (check-solved.md's rule). If
nothing is found, the status word stays as it is and you write "no decipherment or plaintext of this item located
by these queries on 1 Oct 2026" (a search result, never a novelty verdict, rule 10). Then re-run
`python3 tools/intake_gate_check.py <target>` and paste its output under the section; if it still exits 1 for a reason
other than the blog check, state the reason and leave the status word alone.

Commit by explicit path (the NOTES.md only), rebase on origin/main, `python3 tools/restricted_guard.py --outgoing`,
push to main. ROOM.md: claim line first, done line with the hit count, the gate's exit code and the request count per
host. Do not transcribe, decode, or touch any other folder. The common tail of `.claude/briefs/README.md` applies.
