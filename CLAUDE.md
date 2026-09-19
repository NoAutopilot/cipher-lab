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

## Network

Cloud sessions in this project's environment may be unable to reach anything but GitHub. Test with
`curl -sS -o /dev/null -w "%{http_code}" <url>` before planning web work; a `000` means blocked. Web search
(the WebSearch tool) usually still works. Anything that needs a browser, a login, or a copy order is the
person's job; write the exact request into `REQUEST.md` and stop.

## Git

Commit directly to `main`. No pull requests unless asked. Stage by explicit path when several sessions share
the repo. Never rewrite history.
