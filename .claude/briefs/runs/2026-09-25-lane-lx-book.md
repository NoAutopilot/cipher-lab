LX-BOOK (Sonnet, cap $8, at most 2 subagents). Target: ciphers/antt-linhares-chave. Job: identify the dictionary this code uses. Kind: recovery (the key system is read; only the book is missing).

Read CLAUDE.md (rules 1, 3, 7, 10, the Access playbook) and ciphers/antt-linhares-chave/NOTES.md in full first.

The key sheet (DigitArq docId a03cef08d3c04758aa148f5be56d3401, images m0003-m0004, CC BY-SA, no login) says: digit 1 of a group = how many following digits are the page; the next digit = column 1, 2 or 3; the rest = the word's rank in that column; a small number under a group = letters to trim from the front or the end of the word; groups starting 4-9 are nulls, and a message starting with nulls uses "o Diccionario Inglez". Pages run 1 to at most 999.

The orchestrator's parse of the worked example (CHECK IT against the image before relying on it; the key text itself confirms rows 1 and 2):
| group | page | col | rank | trim | gloss on the sheet |
| 1131 (/2) | 1 | 3 | 1 | 2? | a |
| 322212 | 222 | 1 | 2 | - | guerra |
| 313312 | 133 | 3 | 12 | - | de |
| 321118 | 211 | 1 | 8 | 1 | Franc[a] |
| 23312 | 33 | 1 | 2 | 3 | a |
| 311021 | 110 | 2 | 1 | - | com |
| 1412 | 4 | 1 | 2 | 5 | a |
| 3344325 | 344 | 3 | 25 | 4 | Rus[sia] |
| 335422 | 354 | 2 | 2 | 5 | si |
| 1811 | 8 | 1 | 1 | 4 | a |
| 3290219 | 290 | 2 | 19 | 1 | parece (so the headword is probably "parecer") |
| 3234124 | 234 | 1 | 24 | - | inevitavel |
Strongest tests (no trim): guerra p.222 col 1 no.2; de p.133 col 3 no.12; com p.110 col 2 no.1; inevitavel p.234 col 1 no.24; parecer p.290 col 2 no.19. The profile implies a Portuguese headword list of roughly 400-430 pages set in THREE columns (com ~110, de ~133, F ~211, gu ~222, in ~234, pa ~290, Rus ~344, si ~354). Allow +-2 on rank for counting conventions (sub-entries, run-ons); the page and column must match exactly.

Leads, context only and UNVERIFIED (do not repeat them as facts): the Linhares fonds spans 1780-1827; D. Rodrigo de Sousa Coutinho (Turin 1779-96) and D. Domingos de Sousa Coutinho (London 1803-14); a "Diccionario Inglez" alongside suggests a pair, e.g. the two halves of a Portuguese-English dictionary (Vieyra, London 1773, and its abridged/later editions), or a Portuguese dictionary plus a separate English one; the sample sentence fits 1805-07 or 1811-12. Also consider Portuguese-French pocket dictionaries, Morais (1789, 1813) and orthographic word lists printed before 1827.

Method: (1) list candidate editions with a free scan (BNP Biblioteca Nacional Digital purl.pt, Internet Archive, Google Books full view with &country=US and the GOOGLE_BOOKS_KEY per the playbook, HathiTrust); first filter on page count and column count, then test p.222 col 1, and only for survivors the other four pages. Where a scan has OCR, locate the page that carries "guerra" before fetching images. (2) Record every candidate tested in ciphers/antt-linhares-chave/BOOK.md: title, edition, scan URL, pages checked, pass/fail per test pair. Commit and push after each batch of candidates. (3) If one edition passes all five strong tests, save the page images you used under images/book/ with a manifest, decode ALL twelve worked-example groups from it as the proof, and, if ciphers/antt-linhares-chave/ciphertext.tsv exists by then (a parallel worker, LX-TR, is transcribing m0002), decode that too with per-token grades (H from the book, M uncertain) and put the Portuguese reading in reading.txt. If no candidate passes, stop at the budget with BOOK.md as the negative (candidates and the test numbers side by side).

Touch only ciphers/antt-linhares-chave/** and ROOM.md. Do not edit QUEUE.md, STATUS.md, status.json or any other target.

First action: `tools/room.py --start` (fetches, force-checks-out `main` onto `origin/main`, and refuses a
ROOM.md under 50 lines rather than a shrunk stub; replaces raw `git fetch`/`git reset` for this step,
RETRO-2026-09-24b — the prose fix alone let the identical stale-clone/detached-HEAD failure recur at least
twice more the same day). If ROOM.md says 'retrospective starting' or 'swap starting', push what you hold and
stop until 'retrospective done' or 'swap done', then re-run `tools/room.py --start`. If ROOM.md
says 'swap starting', push what you hold and stop until 'swap done', then `git fetch origin && git reset --hard
origin/main`. Read the last 30 lines of ROOM.md first; append a line before editing a shared file and a `done` line when you stop; use `flag` for anything the orchestrator must see. Cap: about $8 of usage; at most 2 subagents, on Sonnet unless the brief says otherwise. Commit, `git fetch
origin main && git rebase FETCH_HEAD && git push -u origin main`, report in a short paragraph (first line:
the answer), stop. Per rule 10, report what was found and where it was not found; never new, unpublished,
first. Per rule 7, a claimed reading on a target with a spec is reported only with `tools/judge_plaintext.py`'s
output pasted in, and stands only after a fresh-instance re-derivation from the spec and key. Do not start other
targets. Never print or commit credentials, and never echo a credential into your own transcript: no unfiltered `env`, no `curl -v` or `set -x` on a call that carries one (Access playbook item 3). A negative's done line carries
target and control numbers side by side, or it is not a negative (rule 3).
