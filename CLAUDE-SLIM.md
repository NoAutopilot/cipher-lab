# cipher-lab (agent rules)

[R0] Every rule change edits CLAUDE.md AND RULEBOOK-FULL.md in the same commit; tools/rules_sync_check.py enforces it.
Story and full wording of any `[id]`: RULEBOOK-FULL.md, search the id.

[INTRO] Unsolved historical ciphers; one person plus agents. Read LANDSCAPE.md and LESSONS.md. Binds every session.

## Layout
- [L.1] `ciphers/<name>/`: `ciphertext.txt` (as transcribed, never silently repaired), `NOTES.md`, `REQUEST.md`, scripts, keys.
- [L.2] `sources/`: others' pages, never edit. [L.3] `tools/`: anything a second target could reuse.
- [L.4] `CATALOG.md` Cryptiana's list; `LANDSCAPE.md` the corrected picture.

## Conventions (non-negotiable)
1. [R1] Before any campaign confirm unsolved: search engine; sender's printed correspondence (IA); calendars/state
   papers; Cryptiana/Cipherbrain comments; DECODE; dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers. Log + date in NOTES.md.
2. [R2] Prefer the image; from a transcription only, say so; negatives are conditional on it.
3. [R3] No negative without a matched control (same length, symbol count, design, language); report both numbers.
   A control must be able to fail:
   [R3.a] gain gate: control's blind baseline not near ceiling (>=95%); match the design, not only N and K.
   [R3.b] normalize both texts to one convention before diffing. [R3.c] judge corpus must match era/register.
   [R3.d] report per-fold spread; <~5 files or wide spread = reliability unknown (`en` is). [R3.e] judge FAIL near gate:
   score the document's own period gloss too; gloss near shuffled = "cannot decide". [R3.f] score the family's decode of
   the shuffled target first; a PASS there voids the judge gate. [R3.g] unbalanced classes: per-class or known-answer
   gate. [R3.h] a control orthogonal to the statistic is a non-test. [R3.i] each unit clears its own control before its
   glosses merge into a shared key. [R3.j] same approach, one knob changed, still failing: log "untested-by-this-tool",
   need a new instrument or material. [R3.k] injected error must bracket the target's measured transcription error.
   [R3.l] calibration out of tolerance: stop before scoring candidates. [R3.m] subsample positive controls to target N.
4. [R4] Grade per token: H key source, C known plaintext, S cryptanalytic with a control, M uncertain, I inferred or
   repaired. Give counts. No H or C = "cryptanalytic result". [R4.a] Two H witnesses disagreeing = data conflict: record
   sender/recipient/direction/date for each, grade M off-witness, log in HYPOTHESES.md, never settle by majority.
4a. [R4a] Unique solve = N3+ AND D2+. D0 a key ranks first, nothing reads; D1 scattered words, no stretch above the
   authentication distance (~1.5 x unicity, every liberty counted), no code reading in two contexts; D2 one such clause
   and one true, specific content sentence by the verifier; D3 >=80% tokens H/C/S, gaps mostly names/codes, plus external
   check or AD + matched control; D4 every cipher-letter token H/C/S, residue only listed name/code groups, non-statistical
   external check, fresh rule-7 re-derivation. Words: D1 "fragments read", D2 "partially deciphered (about N%)", D3
   "largely deciphered (about N%)", D4 "deciphered" ("; N name codes unidentified"); "key identified" only for a period or
   published key. Lower depth on any revision. Gate: `tools/depth_check.py`.
5. [R5] NOTES.md status, first lines: `open`, `partial`, `solved`, `closed-negative`, `found-solved`, `blocked`,
   `offline-only`. Nothing else. [R5.a] Beat a control, or control voided the negative: `partial` + NEAR.md row, never
   `closed-negative` (needs every ladder family with a passed control); `tools/near_check.py`. [R5.b] `partial` parks only
   when every gap is blocked from outside (no-key-material, too-short, illegible, needs-physical-access, waiting-on a named
   row/party); else escalate within brief and cap. Stopping worker appends "## Remaining gaps" + "## Escalation" with
   Verdict "keep going"/"parked"; `tools/gaps_check.py <target>` passes before done.
6. [R6] Absolute dates only; run `date -u` before writing any date/time, never estimate.
   [R6.a] Order cross-session events by `git log origin/main`, not ROOM.md stamps.
7. [R7] Every reading has a script that regenerates it and exits non-zero when stale. [R7.a] With a spec, paste
   `tools/judge_plaintext.py <spec> --file <reading>` output into NOTES.md; before stage 9 a fresh session re-derives with
   `--check` (diff beyond M tokens sends it back). Judge = "worth a verifier", never "right".
8. [R8] Credit solvers and Tomokiyo. Aymeloglu's repo: cite, never copy code. Bourdeau: code MIT, text CC BY 4.0.
9. [R9] Repo is public: log archive requests by date and archive, never sender name, address or payment details.
9a. [R9a] "Stays out of this repo" briefs name the destination; never push it here, not even as a placeholder; no
   destination = stop and say so.
10. [R10] Novelty is a verifier's verdict. Solvers say "read at grade H" / "not found in <source>, searched by <method> on
   <date>", never new, unpublished, unread, first, never printed. A separate verifier writes AUDIT.md: N0 plaintext and
   decipherment of this item known; N1 plaintext published anywhere; N2 plaintext known, no prior mapping of this
   ciphertext; N3 none found after logged search; N4 N3 + principal editions, catalogues, project pages; N5 confirmed by
   archive or specialist. "First decipherment" etc. only at N4 with "no prior decipherment located", or N5. Example:
   ciphers/eckert-1864/AUDIT.md. [R10.a] Record key source `ours`/`period`/`published` -> status.json `key` (`text:
   known` if in print); never say "first". [R10.b] Propagate later revisions into AUDIT.md and SO-queue rows first.

## Outreach
[OUT.0] Issues (never PRs) to the two solver repos and DECODE need every gate; from the cloud draft in
`outreach/bourdeau-issues.md` for the owner. Emails are the person's: draft in `outreach/`. Gates: [OUT.1] (1) AUDIT.md
class; [OUT.2] (2) above N1: second adversarial audit, open-index pass (OpenAlex, S2, Persée, HAL, CrossRef), Google
Books, JSTOR rows answered/waived; [OUT.3] (3) audit's safe sentence, prior print stated, AUDIT.md linked; [OUT.4] (4)
rule 10 wording; [OUT.5] (5) CONTRIBUTIONS.md row before sending; [OUT.6] (6) links: repo folder, source image at the
leaf, printed edition at the page; [OUT.7] (7) a non-drafter session falsifies every fact and the address and writes a
`checked:` header line; none, no send; [OUT.7.a] same pass checks voice (outreach/README.md 1a). [OUT.draft] Blank
subject/recipient/sign-off for the person; recipient = institution's public address from its contact page, dated; never
a private individual's address. [OUT.8] (8) Agents may send from cipherlab.research@gmail.com only with a CONTRIBUTIONS
row, passed gate 7, AI-disclosure sentence in paragraph one; one sender (owning parent); log before sending.

## Operating model
[OPS.1] Parent per account opens lanes; Opus lane orchestrators brief Sonnet workers; verifiers separate. Claim/done in
ROOM.md; send_later check-ins, no polling; read all of STATUS.md; `allowed_warning` anywhere = no new workers.
[OPS.2] Idle-standing lane: one ROOM line naming the ASKS rows, no check-in; exit only on an answer or new material.
[OPS.3] External loops: [OPS.3.a] SECOND-OPINIONS-QUEUE.tsv -> `[SO-]` PRs; [OPS.3.b] JSTOR/LOCAL-QUEUE runners;
[OPS.3.c] SEND-QUEUE.tsv only after `checked:` (`tools/send_queue_check.py`); [OPS.3.d] retrospective and breakthrough routines.
[OPS.4] Only a parent commits `tools/*_runner_prompt.md`; grep "Paste this" for relative paths and credential tokens.
[OPS.5] Verifier giving N3+ appends the SO-queue row in the same session. [OPS.6] Never take the other account's targets.

## Pipeline
[PIPE.1] Scout -> QUEUE.md, never solves. [PIPE.2] Check-solved verdict alone sets stage 2; no copy order, payment or
quote before it. [PIPE.2.a] Paste `tools/intake_gate_check.py <target>` before a deep-work brief; nonzero blocks.
[PIPE.3] Promote a handful; keep >=1 recovery and >=1 cryptanalysis. [PIPE.3.a] Prefer sign pools (>=2,000 signs).
[PIPE.3.b] Rank by EV = P(cheap test moves it) x value / cost. [PIPE.3.c] Famous items only with a named untried cheap test.
[PIPE.3a] Before a campaign (> $10): spec + one $3 Sonnet first test with control in `cheap_test_done`.
[PIPE.4] Access workers stage 2->7 or REQUEST.md. [PIPE.5] Solver stage 8. [PIPE.6] Verifier stage 9.
[PIPE.7] Orchestrator sets kind (recovery/cryptanalysis/contribution) and "Result so far".

## Collaborators
[COL.0] Several accounts, full access. [COL.1] Claim in ROOM.md first, `done` after; use `tools/room.py` or single
quotes; costs from `get_session`. [COL.2] Claims go stale after 6 h. [COL.3] Human blockers go in ASKS.md.
[COL.4] Fetch/rebase right before editing QUEUE.md, QUEUE-scores.json, status.json, STATUS.md, ROOM.md; keep both facts.
[COL.5] Run-brief filenames carry `CIPHERLAB_ACCOUNT`; never overwrite a recent other-session file.
[COL.6] Outside agents only append to ROOM.md. [COL.7] Newcomers: ONBOARDING.md; limits in BUDGETS.md.

## Workers
[WRK.1] One job, push, short report, stop; nothing the brief did not name. [WRK.2] Read last 30 ROOM lines first; flag
lines are answered before the next assignment. [WRK.3] Solver and verifier never one session; solver briefs end "report
what was found and where it was not found; do not classify novelty". [WRK.4] Verifier brief: copy the template at
RULEBOOK-FULL.md#WRK.4 verbatim.

## Usage (tokens are the budget)
[USE.0] Every brief has a dollar cap; stop at it. [USE.1] Sonnet for searches/transcription; strongest model for keys,
reasoning, verdicts. [USE.2] Scripts read, models judge. [USE.3] Digests, not repos. [USE.4] Fetch once, manifest.
[USE.5] TSV/JSON + five-line report. [USE.6] <=4 subagents; two transcription passes unless >10% disagree.
[USE.6.a] >~5 jobs = separate sessions. [USE.6.b] TRANSCRIPTION.md (<=5% true per-sign error). [USE.6.c] split >10% or
unsettled alphabet: owner's sign sorter next. [USE.6.d] `tools/lookalike_pass.py` before a third pass. [USE.6.e] one
page per visual subagent call; `get_session` every 15 min. [USE.6.f] cap = units x per-unit rate + 1; stop before a unit
crossing 80%. [USE.6.g] background compute is its own box. [USE.6.h] rate per pass, not per page. [USE.6.i] crop with
`tools/iiif_lines.py` first, never send a full page. [USE.6.j] reconciliation is one more unit.
[USE.7] Stop when the brief is met. [USE.8a] Rule broken twice -> tool + offline test. [USE.8a.a] gate docstrings state
what they must NOT block. [USE.8a.b] Gate list (file_shrink_guard before landing pushes): RULEBOOK-FULL.md#USE.8a.b.
[USE.8] Shared scripts with `--help` + test; add options, no private copies: [USE.8.a] gallica_folio, [USE.8.b]
iiif_lines, [USE.8.c] reconcile_passes, [USE.8.d] decode_key `--check`, [USE.8.e] print_check, [USE.8.f] family_run,
[USE.8.g] interlinear_align.

## Access playbook
[ACC.0] Run `python3 tools/key_livecheck.py` first; no access ASKS/LOCAL-QUEUE row unless it shows the key failing.
[ACC.cat] Quote the holding catalogue's availability flag first; a portal's "no items" is not a digitisation verdict.
[ACC.1] curl/API first: [ACC.1.a] Huntington, [ACC.1.b] CalmView, [ACC.1.c] RAH recipes. [ACC.2] Then
`tools/browser_fetch.js`; [ACC.2.a] never `ignoreHTTPSErrors`, Wayback for Cloudflare; [ACC.2.b] HathiTrust via APIs.
[ACC.3] Credentials from the environment. Never print them, never write them to the repo. [ACC.3.a] Google Books:
`&key=$GOOGLE_BOOKS_KEY&country=US`. [ACC.3.b] OpenAlex `Authorization: Bearer $OPENALEX_KEY`; S2 `x-api-key: $S2_KEY`,
1.1 s apart. [ACC.3.c] IA: one book, one named check, return it, never bulk; cookie responses to file, read, delete.
[ACC.3.d] Loan images are obfuscated: page reads go to the person. [ACC.3.e] be-api fts `page_num` is not a page.
[ACC.3.f] No loan -> page-number route. [ACC.3.g] JSTOR: owner's machine, online reading, never PDFs; log in AUDIT.md.
[ACC.3.h] DECODE: `tools/decode_browser_login.js`, one login per session, scrub account name; never retry a failed login.
[ACC.3.i] Never run `env`, `printenv`, `set`, `export -p` or `cat /proc/*/environ` unfiltered; never `curl -v`,
`--trace` or `set -x` with a credential; credentials only via `--netrc-file` (mode 600, deleted after), cookie jar or
library config; test with `test -n`. A password in a transcript must be rotated: say so in ROOM.md.
[ACC.3.j] [ACC.3.k] [ACC.3.l] see ACC.3.a-b. [ACC.3.m] Env vars arrive intact; site rejections go to the owner.
[ACC.4] Person-only (paywalls, orders, payments, emails, captchas): batch in REQUEST.md, stop.
[ACC.5] Good citizen: official APIs; one request at a time per host, >=1.5 s apart, a few hundred per session; on
429/403/challenge stop that host, log it, one retry max; descriptive UA unless needed; never bypass a challenge or
automate a login beyond one attempt; report per-host counts. [ACC.6] `000` from curl = egress-blocked, stop.
[ACC.7] Fetch a series once with a manifest; <=30 MB images per folder. [ACC.hosts] Host table: docs/HOSTS.md.
[ACC.8] Owner-machine hosts go to LOCAL-QUEUE.tsv. [ACC.9] [ACC.10] Optional keys: absent = keyless route, say so.
[ACC.11] KEYS.md register; request with `tools/key_request.py`. [ACC.12] Never use AWS_* or CLOUDSDK_AUTH_ACCESS_TOKEN
(purpose unrecorded). [ACC.13] Europeana/DPLA keys work.

## Improvement loop
[IMP.1] LEDGER.md row per archived worker. [IMP.2] `tools/ledger_check.py` before a self-row; edit duplicates in place.
[IMP.3] Cross-account jobs ledgered once, by the runner. [IMP.4] Lessons become template edits; retrospective every 12
rows or $60, or after X/F, <=5 diffs. [IMP.5] Port lane-local fixes to `.claude/briefs/README.md`.

## Git
[GIT.1] Commit directly to `main`. No pull requests unless asked. Stage by explicit path. Never rewrite history.
[GIT.2] GitHub writes via a short-lived worker. [GIT.3] Nobody force-pushes `main`; a committed credential: rotate
first, tell the owner in ROOM.md, he decides.
