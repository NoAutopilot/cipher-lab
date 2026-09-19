# cipher-lab

Working area for attacking unsolved historical ciphers. One person plus AI agents. Read `LANDSCAPE.md` for who
else is working and what is left, `LESSONS.md` for how the successful solvers work. These rules apply to every
session and every subagent, cloud or local.

## Layout

- `ciphers/<name>/` one folder per target: `ciphertext.txt` (as transcribed, never silently repaired),
  `NOTES.md` (sources, status, what is established vs inferred, failure log), `REQUEST.md` when an archive
  request is involved, scripts and keys beside them.
- `sources/` unmodified snapshots of other people's pages. Never edit.
- `tools/` shared scripts. Anything a second target could reuse goes here, not in a target folder.
- `CATALOG.md` every item from Cryptiana's list; `LANDSCAPE.md` the corrected picture.

## Conventions (non-negotiable)

1. **Search before solving.** Before any campaign on a target, establish that it is still unsolved, in this
   order: the cipher's name in a search engine; the sender's printed Lettres or Correspondance on the Internet
   Archive; the calendars and state-paper series; the comment threads of the list posts (Cryptiana blog,
   Cipherbrain); DECODE at de-crypt.org; and the two solver repositories, github.com/dbourdeau/cyphersolver
   and github.com/aaymeloglu/unsolved-ciphers. Record what was checked and the date in NOTES.md.
2. **Image over transcription.** Prefer the page image. When only a transcription exists, say so, and treat a
   negative as conditional on it.
3. **No negative without a matched control.** A solver's failure on a target means nothing unless the same
   solver reads a synthetic cipher of the same length, symbol count, design and language. Report both numbers.
4. **Grade every claimed reading per token:** H read from a key source, C from known plaintext, S cryptanalytic
   with a control, M uncertain, I inferred or repaired. Give the counts. No H or C means "cryptanalytic result".
5. **Status vocabulary** in the first lines of every NOTES.md: `open`, `partial`, `solved`, `closed-negative`,
   `found-solved`, `blocked`, `offline-only`. Nothing else.
6. **Absolute dates.** "19 Sept 2026", never "recently" or "yesterday".
7. **Reproducible readings.** Any claimed reading has a script that regenerates it from the transcription and
   the key, and exits non-zero if the committed reading is stale.
8. **Credit.** Name who solved what and when. Cite the solver repositories and Tomokiyo. Aymeloglu's repository
   has no licence: cite it, do not copy code from it. Bourdeau's code is MIT, text CC BY 4.0.
9. **Personal data stays out of the repo.** It is public. Log archive requests by date and archive, never with
   the sender's name, address or payment details.

## Workers

A worker session does one job, pushes, reports in a short paragraph, and stops. It never starts a new target,
a cryptanalytic attempt, or a write-up that its brief did not name. The orchestrator updates `status.json`,
`STATUS.md` and the published board after every worker report.

## Access playbook

Getting the material is most of the work. Try routes in this order and record which one worked in NOTES.md:

1. **A JSON API or plain URL with curl**, with a browser User-Agent (`-A "Mozilla/5.0"`). Gallica IIIF, TNA
   Discovery's API, the Huntington's CONTENTdm API and the Internet Archive all serve this way.
2. **A real browser.** Sites that answer curl with 403, 202, a JavaScript challenge or a Cloudflare page
   (HathiTrust, PARES, Spink, TNA Discovery record pages, Yale) usually serve headless Chromium. Use
   `NODE_PATH=$(npm root -g) node tools/browser_fetch.js URL out.html --shot out.png`, which drives the
   Chromium bundled in this environment. It fills a search box with `--type "css=text"` and waits for
   `--selector`. Read the saved HTML with `python3 tools/html2text.py` or the screenshot with the image reader.
3. **Credentials from the environment.** Logins the person has set up are exposed as environment variables
   (`DECODE_USER` and `DECODE_PASS` for de-crypt.org). Use them through the browser tool or a curl login flow.
   Never print them, never write them to the repo.
4. **The person.** Paywalls (State Papers Online, Gale), copy orders, payments, emails to archives and dealers,
   and captchas the browser cannot pass. Write the exact request into the target's `REQUEST.md`, mark the
   target "waiting on you" in the report, and stop. Batch several asks into one REQUEST.md rather than
   stopping at the first.

Test reachability before planning: `curl -sS -o /dev/null -w "%{http_code}" <url>`; `000` means the egress
policy blocks it, in which case say so and stop, since no route above will help.

Once a series is identified as useful (a ledger, a volume, a cipher book), fetch all of it once and record the
manifest (URLs, ids, sizes) in the target folder, so later workers do not refetch. Keep committed images under
30 MB per folder; for more, keep the manifest and a sample and note where the rest can be re-fetched.

## Git

Commit directly to `main`. No pull requests unless asked. Stage by explicit path when several sessions share
the repo. Never rewrite history.
