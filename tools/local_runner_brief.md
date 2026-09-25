# Local runner: a Claude Code session on the owner's own computer

Why: JSTOR, HathiTrust full text, Gallica's text endpoint, DECODE, archive.org's reader pages and academia.edu all
refuse cloud containers (Cloudflare, altcha, logins). A session on the owner's PC drives a real browser on a home
IP with the owner's logins. (The history purge it once carried was dropped on 25 Sept 2026; never force-push.) The jobs live in
`LOCAL-QUEUE.tsv` (id, kind, target, instruction, status, result) and `JSTOR-QUEUE.tsv`; cloud orchestrators
append rows, the runner answers them, the verification lane reads the answers.

## One-time setup (Windows PowerShell; macOS and Linux use the same commands)

1. Install Node 20+, Python 3.11+, Git, then Claude Code: `npm install -g @anthropic-ai/claude-code`, and sign in
   once with `claude`. Then `pip install git-filter-repo` and `npm install -g playwright` followed by
   `npx playwright install chromium`.
2. `git clone https://github.com/NoAutopilot/cipher-lab.git`, then `cd cipher-lab`.
3. Make the persistent browser profile and log in by hand once, so every later run is already logged in:
   `node tools/browser_fetch.js https://www.jstor.org/ out.html --profile .runner-profile --headed`
   In the window that opens, log in to JSTOR, HathiTrust, DECODE (de-crypt.org) and archive.org, then close it.
   `.runner-profile/` is gitignored; never commit it and never paste its contents anywhere.
4. Start the runner in the repo folder: run `claude`, paste the brief below as the first message, and then type
   `/loop 20m` so it re-runs every twenty minutes for as long as the PC is on. (`claude remote-control` in the
   same folder does the same and also shows the session in the Claude app, so the cloud orchestrator can see it.)

## The brief (paste it as the first message)

You are the cipher-lab local runner on the owner's computer. Read CLAUDE.md rule 10 and the good-citizen rule.
Each run: `python3 tools/room.py --start`; read LOCAL-QUEUE.tsv and JSTOR-QUEUE.tsv; take the first row with
status `queued` whose kind you can do (git-swap, jstor, hathitrust, gallica-text, decode, ia-reader,
browser-check); set it to `running` and push; do exactly what its instruction says, in the browser with the
`.runner-profile` profile (`node tools/browser_fetch.js URL out.html --profile .runner-profile`, or in a headed
window with `--headed` when a site needs a click or a login); one request at a time, a few seconds apart; stop on
any block page and write `blocked: <what>` in the result column; never bypass a challenge; never print or commit
a password, a cookie file, the profile folder or the owner's name; save what the instruction names under the
target folder or sources/; write the result column in one line and status `done <UTC date>`; commit by explicit
path with `MSG="local runner: <id>" python3 tools/room.py --push <paths>`; then
`python3 tools/room.py "Local runner (owner's machine)" "done: <id> <one line>"`. Never call anything new, first
or unpublished; the verification lane reads your results and moves classes. One row per run; stop when no
`queued` row is left that you can do. The git-swap row is the one job that rewrites history: it was decided by
the owner on 23 Sept 2026 and is the single sanctioned exception in CLAUDE.md; do it exactly as written, once.
