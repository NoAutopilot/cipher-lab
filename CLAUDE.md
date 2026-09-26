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
   The same holds for a *gain* gate (a crib loop, a model-in-the-loop step, any technique judged by how many
   points it adds over blind): before wiring a numeric threshold to a control, check the control's own blind
   baseline is not already near ceiling (roughly >=95%) or already matched by more restarts alone -- a control
   that already solves blind has no headroom to show a gain regardless of the technique. Lesson of 24 Sept 2026
   (solvEX): the brief gated the Salviati target's run on a control at "N=720, K=36 (Salviati's own N and K)"
   but used a simple-substitution design at that N, which reads 99.7% blind on 3 seeds -- already on file before
   the brief was written. Salviati's own cipher is code+mark (cm), which at the same N reads 22-67% blind (LANE
   R4 P's curve): match the *design*, not only the length and symbol count, when the question is whether a
   technique adds anything.
   A matched design is not enough if the two texts being diffed use different transcription conventions.
   Lesson of 25 Sept 2026 (PX-BRODEC): a leave-one-out control diffed a fresh body decode against the
   appendix's own period gloss and returned 50-68% against an 80% gate, apparently a failure -- but the gloss
   abbreviates ("S.d±" for "Snr D.") while the decode spells the word out, so most of the gap was notation, not
   error. Before diffing two renderings of the same underlying text for a gate, normalize both to one
   convention (expand abbreviations, one case, one punctuation set) or the gate measures whichever side
   transcribes more literally, not correctness.
   A language corpus can be the wrong *era* even when it is the right language. Lesson of 25 Sept 2026
   (V6-PTCORP, antt-linhares-chave): `tools/judge_plaintext.py`'s `pt17` corpus is Vieira, 17th-century Portuguese;
   the target is an 1808-1819 letter. Under pt17 the reading FAILed (-1.145 vs real_p05 -1.101) and real prose
   itself false-negatived 8.5% of the time; swapping to a corpus built from the letter's own period and register
   (pt18: Correio Braziliense and O Investigador Portuguez, 1808-1819) PASSed the same reading (-1.051 vs real_p05
   -1.122) and dropped the real-prose false-negative rate to 4.0% -- both sides of the gate moved together, which
   is what a calibration fix looks like, not threshold-shopping. Before running a language judge on a target with a
   specific date and register, check whether tools/data's corpus for that language is era-matched; if not, building
   one is a cheap job (about 12 minutes, V6-PTCORP) worth doing before trusting a FAIL or a PASS
   (RETRO-2026-09-25i proposal 2).
   A corpus's held-out false-negative rate is only as trustworthy as its fold count. Lesson of 25 Sept 2026
   (MJ, espagnol142-mercy-1648): `tools/data/es17c` matched the target's era and genre (1643-47 Spanish
   court-newsletter *Cartas*, not Cervantes) exactly the way pt18 matched Linhares, and the FAIL did not flip --
   register-matching alone does not always rescue a judge the way it did once. Its leave-one-file-out
   false-negative rate (23.5%, N=519) is a blend of only three folds that disagree by 4x (10.0%, 21.0%, 39.5%
   per volume); a blended rate from so few folds says more about which volume was held out than about the
   corpus as a whole. Report the per-fold spread alongside the blended rate, and treat a corpus with under
   ~5 source files and a wide per-fold spread as a FAIL/PASS of unknown reliability rather than trusting the
   single number, the same way a control below its own gate cannot license a target reading (rule 3's
   headline paragraph). Lesson of 25 Sept 2026 (EN-FOLDS): `LANG_CORPORA["en"]` (the default English judge
   corpus, `pg1661_holmes.txt` + `pg2701_mobydick.txt`) had never had this check run at all; run at N=200/500
   it spreads 0.44-0.64 even after adding three more gutenberg.org sources (Huck Finn, Gatsby, Pride and
   Prejudice) in `tools/data/en/` -- more sources made the spread *worse*, because Moby-Dick's own register
   is the outlier, not the file count. A FAIL/PASS against `en` is of unknown reliability; see
   `tools/data/en/README.md`.
   When a judge FAILs a candidate reading close to the gate and the document itself carries an independent
   period gloss or annotation (a marginal or interlinear note, known-genuine and not the candidate), score that
   text through the same judge alongside the candidate and the shuffled-null controls. Lesson of 25 Sept 2026
   (ZX-DEC349, clair349-este-guise-1556): the fr16 judge FAILed the decode (-1.109 vs real_p05 -0.882), a clean
   negative on its own -- but the leaf's own contemporary interlinear gloss scored -1.545 through the identical
   judge, *worse* than the candidate and only marginally above the shuffled-null controls (-1.62 to -1.65). That
   places the candidate much closer to genuine prose than to noise despite missing the p05 gate: a gloss score
   near the shuffled controls, not near real_p05, means a FAIL close to the gate reflects the corpus/threshold at
   this document's length and register, not necessarily the key -- "judge cannot decide," not a negative. This is
   conditional (few documents carry their own period gloss) and distinct from the pt18/es17c lessons above, which
   calibrate the corpus in general; this calibrates against a real text from the same leaf.
4. **Grade every claimed reading per token:** H read from a key source, C from known plaintext, S cryptanalytic
   with a control, M uncertain, I inferred or repaired. Give the counts. No H or C means "cryptanalytic result".
5. **Status vocabulary** in the first lines of every NOTES.md: `open`, `partial`, `solved`, `closed-negative`,
   `found-solved`, `blocked`, `offline-only`. Nothing else.
   Near solves (25 Sept 2026, UPDATES.md): a target where a solver beat its matched control by a reproducible margin, or
   where a control showed the negative was not a real test, is `partial`, never `closed-negative`, and gets a row in
   `NEAR.md` with the numbers and the named next step; `closed-negative` needs every family in the target's ladder logged
   with a passed control. Both parents read NEAR.md at every check-in and every retrospective reviews it.
6. **Absolute dates.** "19 Sept 2026", never "recently" or "yesterday". Read the clock (`date -u`) before writing
   any date or time; never estimate it, and never tell a worker the date without checking. Lesson of 23 Sept 2026:
   an orchestrator wrote times that ran eight hours ahead of the clock and dated a whole evening's files 23 Sept.
   `tools/room.py`'s timestamp is machine-generated (`time.gmtime()`), not typed by a model, but that only
   guarantees it matches *that session's own container clock* -- not that two sessions' containers agree with each
   other. Lesson of 24 Sept 2026: the parent's ROOM.md line at 18:49 said "Retro-apply e archived" seven minutes
   before retro-apply e's own auto-stamped done line (18:56) exists; both stamps are machine-generated, so this is
   container clock skew between two sessions, not a model estimating a time. Don't use two different sessions'
   ROOM.md timestamps to decide which of their actions happened first; where the order matters (an audit, a
   postmortem), use the single shared history's push order (`git log origin/main`) instead, which is one clock,
   not many. This window's retrospective also found that isn't always available either: `tools/room.py --push`'s
   rebase can fold several sessions' commits into one generically-titled "update" commit on whichever session
   happens to run the merge, which erases the per-session commit trail along with any independent time check --
   flagged here, not fixed; the retrospective ran out of budget to design the fix.
7. **Reproducible readings.** Any claimed reading has a script that regenerates it from the transcription and
   the key, and exits non-zero if the committed reading is stale.
   A reading on a target that has a spec is reported only with the output of `tools/judge_plaintext.py <spec>
   --file <reading>` pasted into NOTES.md (a FAIL may still be reported, as a FAIL). Before the orchestrator moves
   the target to stage 9, a fresh session that has seen only the spec and the key re-derives the reading with the
   target's decode script and `--check`; a re-derivation that differs by more than the M-graded tokens sends the
   reading back. The judge and the re-derivation are the Lean of this repository: they say "worth a verifier",
   never "right" (rule 10).
8. **Credit.** Name who solved what and when. Cite the solver repositories and Tomokiyo. Aymeloglu's repository
   has no licence: cite it, do not copy code from it. Bourdeau's code is MIT, text CC BY 4.0.
9. **Personal data stays out of the repo.** It is public. Log archive requests by date and archive, never with
   the sender's name, address or payment details.
9a. **A brief that says material stays out of this repository must name the destination, and the worker must not
   push here at all** -- not even as a placeholder "to be removed later." If the named destination (a private
   repository, an artifact) does not exist yet, the worker stops and says so; it does not commit the material to
   this repository in the meantime. Lesson of 24 Sept 2026: two workers (grants scout, grants applications),
   briefed only that the material "stays out of this repository," both pushed it here anyway; both fixes now sit
   in this repository's history pending the owner's purge (`tools/purge_history.sh`).

10. **Novelty is a verifier's verdict, not a solver's.** A solver session may say "read at grade H" and "not
   found in <named source>, searched by <method> on <date>". It may not say new, unpublished, unread, first or
   never printed, and neither may the orchestrator when it reports to the person. Absence from one source is a
   search result, not a discovery. A separate verifier session, working from the plaintext and the ciphertext
   and trying to disprove novelty, assigns one class after a logged search and writes it to the target's AUDIT.md:
   N0 plaintext and decipherment of this very item already known; N1 plaintext already published anywhere (our
   reading is an independent re-decipherment); N2 plaintext known elsewhere but no prior mapping of this
   ciphertext to it found; N3 no prior plaintext or decipherment located after the logged search; N4 N3 with the
   principal editions, catalogues and project pages covered, internal or unpublished work not excluded; N5
   confirmed by the holding archive or a specialist. Wording such as "first decipherment", "previously unread",
   "newly recovered" or "unpublished plaintext" is allowed only at N4, with the qualifier "no prior decipherment
   located", or at N5. The board's stage "Novelty verified" is set only from AUDIT.md. Lesson of 20 Sept 2026:
   four Eckert 1864 readings were called "never printed" because they were absent from Official Records ser. I
   vols 32-45; the sender-specific editions (Butler Correspondence, Lincoln Collected Works, ORN) had not been
   searched and no phrase search was run after decoding.
   Precedent and worked example: ciphers/eckert-1864/AUDIT.md.
   Key source (25 Sept 2026, owner's request): every AUDIT.md verdict also records whose key read the item -- `ours` (recovered by us: cryptanalysis, a plain-copy alignment, or identifying the codebook), `period` (rebuilt by us from a decipherment, key sheet or cipher book of the time) or `published` (someone else's modern key, credited) -- and the parent copies it to the result's `key` field in status.json, with `text: known` when the plaintext was already in print. An `ours` key at N3 or better is the nearest honest equivalent of a first; say it in those words, never 'first'.
   A reading revised after AUDIT.md is written (a blind-pass correction, a re-derivation fix under rule 7) is
   propagated into AUDIT.md and into any row already filed for that target in `SECOND-OPINIONS-QUEUE.tsv` before
   either is treated as current, not left for the next session to notice. Lesson of 25 Sept 2026 (V6-MERCY2):
   a downstream reading change (R7-MREV: "Cleues" -> "Eleues") was not carried back into AUDIT.md or the already-
   queued SO prompt, so an outward-facing sentence kept a word the blind read had dropped.


## Outreach (owner's directive, 23 September 2026)

The orchestrator may post contributions to the solver repositories on GitHub (an issue, never a pull request, on
dbourdeau/cyphersolver or aaymeloglu/unsolved-ciphers) and to DECODE once its login works, without asking, when
every gate below is met. (24 Sept 2026: a cloud session's GitHub access is scoped to the owner's own repositories, so
the issue text is drafted in `outreach/bourdeau-issues.md` and the owner posts it from their account, like an email.) Emails to researchers, archives and dealers stay the person's: the orchestrator drafts
them in `outreach/` and the person sends them and records the date. Gates for any post: (1) the target's
AUDIT.md carries a verifier's class; (2) for anything above N1, a second adversarial audit by a separate session
has tried to find it in print and failed, the open-index scholarship pass (OpenAlex, Semantic Scholar, Persée, HAL, CrossRef) and the Google Books queries are done, and the target's rows in `JSTOR-QUEUE.tsv` are answered or waived by the owner;
(3) the message is the audit's safe sentence, states any prior print it rests on, and links AUDIT.md so the
recipient can check the search log; (4) rule 10 wording only; (5) the post is logged in `CONTRIBUTIONS.md` with
date, recipient, class and link, before it is sent; (6) every outward note carries the links a recipient can verify
from their desk without asking us: the repository folder (AUDIT.md, key, reading), the primary source image (the
Gallica or IIIF ark at the leaf), and the printed edition it rests on, at the page cited, on archive.org or HathiTrust.
A subject line, a recipient line and a sign-off left blank for the person are part of every draft. The recipient line
carries the institution's public contact address (read from its own contact page, with the date) so the person can send
without looking it up; a private individual's address never goes in the file (24 Sept 2026, owner: "I gotta have an email address"). A negative with a matched control is a contribution too.

## Operating model (read before orchestrating)

Roles: one **parent orchestrator** per account (the session the owner talks to; `.claude/briefs/parent.md`) opens
**lanes**; each lane has an Opus **lane orchestrator** that writes job briefs to `.claude/briefs/runs/` and runs
Sonnet **workers**, which use subagents for independent passes; **verifiers** are always separate sessions from
solvers. Every session coordinates through `ROOM.md` (claim before work, done when stopping) and schedules its own
check-ins with send_later; nothing polls. State lives in git: `STATUS.md` holds the "Parent handoff" section, the
"Lane structure" table and one "LANE <X> handoff" per closed lane, below the results log, so read the whole file,
not the first screen. The rate-limit rule is BUDGETS.md's scaling rule (`allowed_warning` anywhere: no new workers
anywhere). Nothing is billed on the owner's Max plan; dollar figures measure the rate-limit window.

Loops that run outside this repository and write back into it:
- **Second opinions**: a scheduled ChatGPT task reads `SECOND-OPINIONS-QUEUE.tsv` and answers each queued prompt as an
  `[SO-<label>]` pull request (`tools/second_opinion_runner_prompt.md`). Lanes queue a reading after the verifier
  gives N3 or better; the parent marks it posted; a verifier checks every citation.
- **Local runners** on the owner's computer answer `JSTOR-QUEUE.tsv` and `LOCAL-QUEUE.tsv` through his logged-in
  browser (`tools/jstor_runner_brief.md`, `tools/local_runner_brief.md`).
- **Routines**: the weekly retrospective, and "Cipher Lab: breakthrough alert (email)", which the parent fires for a
  real result.
Accounts: no account sees another's sessions or triggers; each parent reads the other's handoff and ROOM lines, and
takes none of its targets.

## Pipeline (who hands what to whom)

1. **Scout** (`.claude/workflows/scout.js`, or a worker with the same brief) finds candidates, checks status at
   the sources, scores them and sets `kind` (cryptanalysis, recovery, contribution; editions are dropped). It
   writes QUEUE.md. It never promotes to the board and never solves.
2. **Check-solved** (`.claude/workflows/check-solved.js`) runs blind, six sources, on any queue item before it
   goes on the board, and again whenever a catalogue row may be stale. Its verdict goes into the target's
   NOTES.md and sets stage 2, "Verified unsolved". Stage 2 is set only by a check-solved verdict, and no copy
   order, payment or quote request goes on the person's card until the target is at stage 2 (20 Sept 2026). Intake gate (25 Sept 2026): before any deep work (transcription, key application, cryptanalysis) on a target, read its check-solved verdict against .claude/briefs/check-solved.md: an `open` whose sentence does not name the standard edition and the pages or full-text search actually read, or that names an edition it could not open, is `blocked`, whatever word it uses. Send a check-solved worker first. (Linhares, 25 Sept: an `open` with the sender-family edition unread went to deep work; the verifier held it at N3 for that reason.) A prose rule a lane orchestrator has to remember to apply by eye did not stop that breach, so run `tools/intake_gate_check.py <target>` and paste its output before briefing any deep-work worker; a nonzero exit blocks the brief (RETRO-2026-09-25h proposal 4).
3. **Orchestrator** promotes to the board only after check-solved, at most a handful at a time, choosing by
   score and by the three kinds together, so the board always carries at least one recovery and one
   cryptanalysis candidate and never fills with editions.
   Selection rule, pools first (25 Sept 2026, UPDATES.md): between two candidates of equal expected value, take the one that
   belongs to a sign pool -- one sender, office and key family with 2,000 or more signs across its letters -- over a single
   short letter; every reading on the board so far came from a period key or a pool of siblings, and the controls say our
   solvers read code+mark only at pooled lengths. Famous short items enter only through the standing gold lane.
   Selection rule (24 Sept 2026): rank by expected value = P(the first cheap test moves it) x value / cost, not by
   fame or by scout score alone. Prefer items with a transcription on disk, a formal constraint (a known key family,
   a crib, a host text, a form), a language with a corpus in tools/data, and no published matched-control negative.
   Famous items (Voynich, Kryptos K4, Zodiac Z13/Z32, Beale, Rohonc, Dorabella) enter only with a named untried
   cheap test; `UNSOLVED-SURVEY.md` is the reference ranking for the public list and is re-ranked when a row's
   status changes.
3a. **Breadth lane.** Before any target gets a campaign (a cap above $10), it gets a spec (`specs/<slug>.json`:
    ciphertext as transcribed with source and date, alphabet, constraints, cheap tests in order, a `judge` block) and
    one Sonnet worker runs its first cheap test at a cap of $3, with the matched control, and writes the two numbers
    into the spec's `cheap_test_done`. A breadth worker takes the next spec whose first test is unrun, never a second
    test on the same spec, and never a campaign. The orchestrator promotes to a campaign only a spec whose first test
    moved it (judge PASS, found-solved, or a control-backed negative that names the next test). Ten first tests at $3
    beat one campaign at $30: the mathematics results resolved 4 of 700 and 9 of 353 by trying everything cheaply.
4. **Access workers** (lookup, print check, image capture, transcription) move a target from stage 2 to stage
   7 without the person where the playbook allows, and write REQUEST.md when it does not.
5. **Solver** reads (stage 8), grades per token, reports what was found and where it was not found.
6. **Verifier** assigns the N-class (stage 9) and corrects any over-claim.
7. **Result label**: the orchestrator sets the card's kind from what actually happened (a key that opened it
   is recovery, a reading without the key is cryptanalysis, a correction or a dataset handed on is
   contribution) and writes the "Result so far" line. README "What counts as a result" is the reference.

## Collaborators

Several people work in this repository, each from their own account, with full access and no fixed lanes.
Two things make that safe, and they are not optional.

**Claim before you start.** Append a line to `ROOM.md` naming you, the role and the target before any work
begins, and a `done` line when you stop. If a live claim already covers what you wanted, take the next
thing. Nothing else stops two agents transcribing the same folio. Write ROOM lines with `tools/room.py` or inside single quotes / a quoted heredoc: inside double quotes a figure like `$8` is a shell variable and vanishes (QA 25 Sept 2026 08:30 found four done lines reading "well under  stall alarm"). A cost figure comes from the orchestrator's `get_session`, never from the worker's own sense of it.

**A claim goes stale after six hours.** If a claim in `ROOM.md` has no `done` line and no further activity from that agent for six hours, anyone may take the target after appending a line saying so. Otherwise one idle agent parks a target indefinitely and nobody can tell, because no account can see another account's sessions.

**Anything blocked on a human goes in `ASKS.md`,** not only into a report. A blocker that lives only in a session transcript is invisible to everyone else.

**Rebase before you write to a shared file.** `QUEUE.md`, `QUEUE-scores.json`, `status.json`, `STATUS.md`
and `ROOM.md` are written by everybody. Fetch and rebase immediately before editing, and when a row
conflicts, keep both facts rather than overwriting someone else's finding.

New people and their agents start at `ONBOARDING.md`. Everyone records their own plan limits in
`BUDGETS.md`, because no account can see another account's rate limits.

## Workers

A worker session does one job, pushes, reports in a short paragraph, and stops. It never starts a new target,
a cryptanalytic attempt, or a write-up that its brief did not name. The orchestrator updates `status.json`,
`STATUS.md` and the published board after every worker report.

The room: `ROOM.md` is the second channel. A worker reads its last 30 lines before its first action and
appends one line when it learns something another worker might need, before it edits a shared file, and
when it stops (`done`). A `flag` line is an interjection: the orchestrator reads every flag before the next
assignment and answers it in the brief or in the room. Lines are signals, not reports; reports go in the
worker's final paragraph and NOTES.md. Duplicate work (two sessions auditing the same claim on 20 Sept 2026)
is what the room prevents.

Two hats, never one session: the **solver** produces readings and the search log of what it checked; the
**verifier** receives the plaintext, the ciphertext and that log, and searches to disprove novelty (rule 10).
A solver brief ends "report what was found and where it was not found; do not classify novelty". A verifier
brief lists the source families to cover (canonical editions, sender- and recipient-specific edited
correspondence, the holding archive's catalogue and blog, the transcription project's pages, Google Books,
HathiTrust, Internet Archive, GitHub cipher projects, scholarship), requires a phrase search on the decoded
text, requires a log of every family searched and every one unreachable, and ends with an N-class per item in
AUDIT.md plus corrections to any over-claiming sentence in the target's files. The orchestrator moves a target
to "Novelty verified" only from AUDIT.md, and repeats to the person only the class and its safe sentence.

**Verifier brief (template).** Used before any reading is described outside the repo as new. The verifier is
a session other than the solver's and does not protect the solver's conclusions.

```
VERIFIER: <target folder>. Claim under audit: <the sentence as the repo states it>.
1. Extract from the repo, per item: date, sender, recipient, place, plaintext as read, ciphertext,
   distinctive phrases, archive identifiers, and exactly what the solver searched (sources, identifiers,
   method, date).
2. Search independently: by date, sender+recipient, quoted phrases, ciphertext words and identifiers, in
   (a) the canonical series, its index and its supplements; (b) the sender's and the recipient's printed
   correspondence; (c) the documentary editions for the period; (d) the holding archive's catalogue,
   blog and project pages; (e) full-text search on Internet Archive, HathiTrust and Google Books;
   (f) the solver repositories and cipher blogs; (g) scholarship through the open indexes (OpenAlex API and Semantic
   Scholar API with the keys of access playbook item 3, Persée, HAL, CrossRef, Google Scholar when reachable) and, for JSTOR, a row per query appended to
   `JSTOR-QUEUE.tsv` for the owner's local runner; a queued JSTOR row never blocks N3 or N4 on its own (24 Sept 2026,
   the owner is not the bottleneck at fifty sessions). Log each family
   as searched or unreachable, with what was searched.
3. Classify each item N0-N5 (rule 10) with: prior plaintext (yes/no, where, earliest citation), prior
   decipherment (yes/no), evidence quality, confidence, one safe sentence, one unsafe sentence.
4. Postmortem: name the failure, the files and sentences that over-claim, and correct them. If the reading itself
   was revised after this AUDIT.md (or an earlier one) was written, carry the revision into AUDIT.md and into any
   `SECOND-OPINIONS-QUEUE.tsv` row already filed for this target before writing the safe sentence (25 Sept 2026,
   V6-MERCY2).
5. Write <folder>/AUDIT.md; commit and push; report the classifications and the one-line postmortem.
Do not decode, do not touch other targets, do not print or commit credentials.
```

## Usage (tokens are the budget)

The person's plan is a fixed window of usage, not a bill. A worker that burns it stops every other session.
Every brief states a cap in dollars of usage (the session metadata's cost figure) and the worker stops at it.

1. **Tier the model to the job.** Blind searches, catalogue sweeps, harvesting, transcription passes and any
   job whose output is checked by another agent run on Sonnet (`claude-sonnet-5`). Reconciliation of passes,
   key reading, cipher reasoning and verifier verdicts run on the strongest model. The orchestrator sets the
   model when it creates the session; a worker sets it when it spawns subagents.
2. **Scripts read, models judge.** Never have a model read an Official Records volume, a 400-page dictionary
   or a 2,000-row key to find one thing. Fetch the text once, grep or parse it with a script, and give the
   model the hits. decode.py, check.py and freq.py are the pattern.
3. **Digests, not repositories.** Workers read LESSONS.md and LANDSCAPE.md, not the solver repositories in
   full. Clone a repository only to grep it for a named target.
4. **Fetch once, keep a manifest.** Images and page text go to disk with images/manifest.json on the first
   fetch; later passes read the disk.
5. **Compact outputs.** Worker results are TSV, JSON or a short markdown table with a five-line report; prose
   is for NOTES.md sections the person will read. The person has said machine-shaped files are fine.
6. **Fan-out limits.** At most four subagents at once per worker; two transcription passes, not three, unless
   the two disagree on more than a tenth of the rows.
   A subagent's transcription job is priced by signs matched x reference-sheet size, not by elapsed minutes or
   page count: GOLD-4D (25 Sept 2026) gave one Sonnet subagent all four Debosnys cryptograms (about 1,300 signs)
   against a 160-sign inventory in a single call and was stopped at 3.3x its $7 cap, 38 minutes into a 60-minute
   box, because the wall-clock box is checked between tool calls and cannot interrupt one call that is still
   running -- a call sized to outlive the box defeats it regardless of the box's length. Scope a subagent's
   visual-transcription call to one page or one cryptogram against the reference sheet, never the whole
   inventory in one call, and have the orchestrator read `get_session` on that worker at a fixed short interval
   (15 minutes, GOLD's own fix) rather than trusting the box alone when a job includes a large-inventory match.
   The same mispricing recurs at the primary worker's own level, not only inside a subagent call, whenever a
   brief's job loops over discrete same-shaped visual or multi-variant units: LANE R7's native-crop atlas
   re-pass (AT55V, 25 Sept, 13 Gallica native crops) ran 1.23x its $6 cap, its blind eye-bisection pass (MEYE,
   same day, 122 tokens) ran 1.86x its $2.50 cap, and LANE GOLD's family-variant sweep (GOLD-K2, same day)
   crossed from about 56% to 89% of its 75-minute box in the single step of starting a second ~25-minute
   control+target variant, landing 9% over its $6 cap. In each case the worker correctly did not stop mid-unit
   (the box is a minimum too, per this section's own rule); the brief's box was sized as a round number of
   minutes, not as (planned unit count x a per-unit cost/time estimate drawn from the nearest comparable ledger
   row) plus one unit of margin. Size a unit-loop brief's cap and box from the per-unit rate, state the unit
   count and the per-unit estimate in the brief itself, and have the worker stop before starting a unit that
   would cross 80% of either figure -- not only after aggregate elapsed time crosses 80%, which one large unit
   can jump past in a single step.
   A well-sized per-unit box can still run over if a background computation shares the same box's CPU (25-26 Sept
   2026, GOLD-K3): two family_run.py variants estimated at about 24 minutes each (48 of a 75-minute box) actually
   took 59 minutes and landed 23 percent over the $6 cap, because a ten-text noise-band computation was run
   concurrently in the same box to save a second one, and "a background band of ten decoder runs competes for
   CPU with the family runs" (GOLD-K3's own lesson). Price a background/reference computation that runs alongside
   foreground per-unit work as its own separate box, or serialize it before or after the foreground units --
   never assume concurrent CPU-bound work is free just because it does not add a unit to the count the per-unit
   rate was built from.
7. **Stop when the brief is met.** A worker does not continue into follow-ups (a sweep of sister copies, an
   audit of its own) that its brief did not name; it writes the follow-up as a one-line suggestion in NOTES.md.
8a. **Rules become tools (25 Sept 2026, UPDATES.md).** A rule that the ledger shows broken twice gets a mechanical check in
   tools/ with an offline test, and its prose shrinks to one line naming the tool. Precedents: `tools/intake_gate_check.py`
   (the intake gate), `tools/room.py` (ROOM.md hygiene), `tools/ledger_check.py` (outcome codes), `tools/family_run.py`
   (rule 3: a hypothesis family runs on a target only after its matched control has run and read; both numbers are written
   side by side to `ciphers/<t>/HYPOTHESES.md`), `tools/near_check.py` (rule 5's near-solve amendment: a NEAR.md/status.json
   `near` target must never read `closed-negative`, the two registers must agree, and a row stale past 48 hours is flagged).
8. **Shared scripts before new ones (24 Sept 2026).** Each has `--help` and an offline test in `tools/tests/`; a
   target that needs something they lack gets an option added to the tool, not a private copy.
   `tools/gallica_folio.py ARK --folio 35` reads the manifest's canvas labels once, gives the canvas and native image
   URL, and reports every offset change and duplicate label (fr.20140 changes offset at f.50v; fr.16092 is all 'NP',
   so give it eye-checked `--anchor canvas=folio` pairs and it tests them for one offset).
   `tools/iiif_lines.py --ark ARK --canvas N --region x,y,w,h --out ciphers/<t>/images --debug` fetches the region
   once at native resolution, finds lines by row ink profile (`--distance`, `--prominence`), cuts crops under
   2500 px wide, writes images/manifest.json entries, and keeps the folder under 30 MB by shrinking only its own
   reference copies. Check the debug overlay before handing crops to a pass.
   `tools/reconcile_passes.py passA.tsv passB.tsv [passC.tsv] --crops images/crops` aligns the passes per line and
   writes disagreements.tsv (only what the reconciler must settle from the image), ciphertext_draft.tsv and
   agreement.tsv; `--halves` joins a/b half-line crops, `--split-chars` splits unsegmented digit groups.
   `tools/decode_key.py ciphers/<t> [--check]` applies key.tsv (and exceptions.tsv) to the ciphertext, grades every
   token and fails when the committed reading is stale (rule 7); a target describes its layout in decode.json
   instead of writing a decode.py (examples: tools/tests/decode_configs/, which reproduce Gramont, Danzay and Anhalt).
   `tools/print_check.py ciphers/<t>` runs phrases.txt against sources.tsv and, unasked, against the whole of IA
   full text, Google Books and OpenAlex; writes print-check.tsv and print-check-hosts.tsv. Its 'no hits' is a
   search result for the log, never a novelty verdict (rule 10).
   `tools/family_run.py SPEC --family F` (masc, homophonic, periodic_vigenere, running_key; 25 Sept 2026) runs rule 3 in
   order: the matched control first (spec N, K, corpus, `--seeds`), the target only if the control mean meets `--gate`
   (else CONTROL BELOW GATE, exit 3), one row per run with both numbers in ciphers/<t>/HYPOTHESES.md.

## Access playbook

**Key livecheck (25 Sept 2026, KEYPROBE-TOOL).** `python3 tools/key_livecheck.py` is the first command of every
parent check-in and of every worker whose brief names an external host -- not the same tool as `tools/key_probe.py`
below (that one is name-presence and cross-account sync, no network call; this one makes the actual documented
call). It reports presence (`os.environ`, never a value) and, for the API-key hosts below, one live documented test
call each; DECODE, JSTOR and Internet Archive logins are presence-only by default (see the tool's own docstring for
why -- automating a login on every check-in would itself be the repeated-login the good-citizen rule below forbids).
A worker may not write an ASKS.md row asking the owner for access, nor a LOCAL-QUEUE.tsv row, until the probe shows
the relevant key absent or failing, and the row must quote the probe's line for that credential. Why this exists:
GOOGLE_BOOKS_KEY sat unused from 20 to 25 Sept 2026 (a `country=US` parameter was all it needed), IA_USER/IA_PASS
worked from 23 Sept with no borrow attempted until 25 Sept, and CORE_API_KEY was probed only when the owner asked --
work sat in ASKS.md all day waiting on access already in hand. `tools/room.py --start` prints the last probe's
summary line; a stale or missing KEYS-STATUS.md means the probe has not been run recently, re-run it.

Getting the material is most of the work. Try routes in this order and record which one worked in NOTES.md:

1. **A JSON API or plain URL with curl**, with a browser User-Agent (`-A "Mozilla/5.0"`). Gallica IIIF, TNA
   Discovery's API, the Huntington's CONTENTdm API and the Internet Archive all serve this way.
   **Huntington CONTENTdm, confirmed 24 Sept 2026:** the naive `dmQuery/ALIAS/TERM/fields!list/sort/maxrecs/
   start/0/0/0/0/json` form silently ignores the search term and returns a fixed title-sorted listing (caught by
   testing "cipher", a quoted phrase, and no term at all, all returning the identical 77 rows) -- always use the
   documented `CISOSEARCHALL^TERM^all^and` clause instead, and set the sixth path segment (suppressfulltextsearch)
   to `1` to search page-level OCR/notes text, not `0`. The Stowe Papers collection (`/p16003coll20`) genuinely
   has no "cipher"/"cypher" hits this way; the Manuscripts collection (`/p15150coll7`) does. `dmGetItemInfo/
   ALIAS/POINTER/json` gives the full catalogue note per item (the search endpoint truncates `descri` to empty
   for many records).
   **Lambeth Palace Library and the Georgian Papers Programme / Royal Archives, confirmed 24 Sept 2026:** both
   run CalmView (same ASP.NET WebForms software; GPP redirects `www.gpp.rct.uk` -> blocked, but the bare
   `gpp.rct.uk` serves). The bare Lambeth hostname 403s at the root; the real catalogue is under `/CalmView/`.
   The search box itself is a WebForms postback (needs `__VIEWSTATE`), but submitting it once yields a plain,
   repeatable GET URL for the results page that needs no session or postback replay:
   `/CalmView/Overview.aspx?src=CalmView.Catalog&r=((((text)='TERM')))` (URL-encode the parentheses and quotes).
   Paging past the default 20 rows needs one POST setting the page-size dropdown (`ctl00$main$TopPager$ctl15`)
   to `0` ("All"), with `__VIEWSTATE`/`__EVENTVALIDATION` copied from that same results page. CalmView's text
   search tokenises "cipher" and "cypher" as distinct terms -- query both spellings.
   **bibliotecadigital.rah.es (Real Academia de la Historia), confirmed 24 Sept 2026:** every plain path
   (`registro.do`, `catalogo_imagenes/grupo.do`, `resultados_busqueda.do`, and the image endpoint
   `imagen_id.do` itself) sits behind the site's Anubis JS proof-of-work bot-challenge -- curl always gets a
   307 to `/.within.website/`, never solves it. The site's own OAI-PMH endpoint (`/oai/oai.do`) is not behind
   Anubis and answers plain curl. `verb=GetRecord&metadataPrefix=didl` (not the default `oai_dc`, which only
   gives the `grupo.do` group-viewer link) returns a `didl:Resource` per page image, each `ref` a direct
   `.../i18n/catalogo_imagenes/imagen_id.do?idImagen=NNNNNNNN` URL -- but that URL is still behind Anubis for
   curl. A real headless Chromium (`tools/browser_fetch.js`) clears the challenge, but only intermittently
   (of ~8 attempts one pass, most returned Anubis's own unsolved challenge page, "Anubis could not load its
   JavaScript. The server may be overloaded."); `tools/browser_fetch.js --binary` (added 24 Sept 2026) retries
   the navigation, default 3x, until the response's content-type isn't `text/html`, which made five image
   fetches reliable: `node tools/browser_fetch.js "<imagen_id.do URL>" OUT.jpg --profile DIR --binary`. See
   `ciphers/rah-canada-1869/NOTES.md` for the worked example.
2. **A real browser.** Sites that answer curl with 403, 202, a JavaScript challenge or a Cloudflare page
   (HathiTrust, PARES, Spink, TNA Discovery record pages, Yale) usually serve headless Chromium. Use
   `NODE_PATH=$(npm root -g) node tools/browser_fetch.js URL out.html --shot out.png`, which drives the
   Chromium bundled in this environment. It fills a search box with `--type "css=text"` and waits for
   `--selector`. Read the saved HTML with `python3 tools/html2text.py` or the screenshot with the image reader.
   Known on 20 Sept 2026: in cloud containers Chromium fails every HTTPS page with `ERR_CERT_AUTHORITY_INVALID`
   because it does not trust the container's TLS-intercepting proxy CA (curl and Node do, through environment
   variables). The fix is `apt-get install -y libnss3-tools && certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n
   ccr-agent-proxy -i /root/.ccr/agent-proxy-ca.crt` once per container (the script prints this hint); a worker's
   permission policy may refuse it, in which case say so and use the APIs below. Never use `ignoreHTTPSErrors`.
   Confirmed 20 Sept 2026: the setup script now runs this fix automatically in a fresh container, and it works —
   `certutil -L` lists `ccr-agent-proxy` at session start and `tools/browser_fetch.js` renders ordinary HTTPS
   pages (e.g. archive.org) with no `ERR_CERT_AUTHORITY_INVALID`, confirming the cert problem itself is fixed.
   It does not, on its own, get past a site's own Cloudflare bot challenge: HathiTrust and manuscripts.nls.uk
   both still served a "Performing security verification" Cloudflare interstitial to the tool after the fix,
   confirmed by screenshot, unrelated to the certificate. For a Cloudflare-blocked site, try the Internet
   Archive Wayback Machine instead (`web.archive.org` is not Cloudflare-protected here): find the archived URL
   with the CDX API, `https://web.archive.org/cdx/search/cdx?url=<site>&output=json`, then fetch
   `https://web.archive.org/web/<timestamp>if_/<original-url>` with `tools/browser_fetch.js` (the `if_` suffix
   avoids the wayback toolbar frame breaking `--selector`/`--type`; a bare fetch without it can return a stub
   `upstream request failed` — retry once before concluding the capture is unreachable).
   **HathiTrust without a browser:** the site itself is Cloudflare-challenged for curl, but the Bibliographic API
   (`catalog.hathitrust.org/api/volumes/brief/recordnumber/N.json`, `oclc/N.json`; needs a full Chrome User-Agent
   string) gives volume ids, and the HTRC Extracted Features API
   (`data.htrc.illinois.edu/ef-api/volumes/HTID/pages?pos=false`) gives per-page word counts for every volume;
   `tools/htrc_ef_headwords.py` uses both to place headwords. Record numbers come from web search restricted to
   catalog.hathitrust.org, the Online Books Page, or OCLC numbers from Open Library's search API.
3. **Credentials from the environment.** Logins the person has set up are exposed as environment variables
   (`DECODE_USER` and `DECODE_PASS` for de-crypt.org). Use them through the browser tool or a curl login flow.
   Never print them, never write them to the repo.
   Google Books: the API answers unauthenticated requests with HTTP 429 after a few dozen calls. The person
   has set GOOGLE_BOOKS_KEY in the environment (20 Sept 2026): append `&key=$GOOGLE_BOOKS_KEY` to every
   `www.googleapis.com/books/v1/volumes` call. Full-text hits still need the volume to be full view; use
   `filter=full` and read pages through the volume's `accessInfo` links. Never print the key. **Cloud fix (25 Sept 2026, 22:55 UTC, parent probe):** from this container the keyed call returns HTTP 403 `unknownLocation` ("Cannot determine user location for geographically restricted operation"); adding `&country=US` to the same call clears it (full-view search and `searchInfo.textSnippet` on PARTIAL volumes both answered). Every Google Books API call from the cloud carries `country=US`; a `NO_PAGES` verdict recorded before this date without it is not a test.
   **OpenAlex and Semantic Scholar keys (24 Sept 2026).** OpenAlex retired its mailto "polite pool" in February 2026
   and meters a daily credit budget per caller; keyless callers are counted per IP, and every cloud session shares one
   egress IP, which is why all of them saw 429 on 24 Sept 2026. The person has set `OPENALEX_KEY` (a free key from
   openalex.org/settings/api, ten times the keyless budget, a `search=` call costs 10 credits, a single-record lookup 0).
   Send it as a header, never in the URL: `curl -H "Authorization: Bearer $OPENALEX_KEY" "https://api.openalex.org/works?search=..."`;
   check what is left with `curl "https://api.openalex.org/rate-limit?api_key=$OPENALEX_KEY"` (resets at midnight UTC;
   429 also on more than 100 requests/s). Semantic Scholar: unauthenticated traffic shares one pool and 429s; the person
   has set `S2_KEY` (24 Sept 2026, a free key from the form at semanticscholar.org/product/api), sent as `-H "x-api-key: $S2_KEY"`, 1 request per second, no Retry-After on 429, so sleep 1.1 s between
   calls and back off. `tools/print_check.py` reads both variables and adds the headers itself (and runs its `s2`
   check only when the key is present). With the keys, a session runs the open-index pass itself; no owner-machine row
   is needed for OpenAlex or Semantic Scholar. Test presence with `test -n`; never print or commit either key.
   Internet Archive: IA_USER and IA_PASS (set 20 Sept 2026) let a worker borrow a lending-only book for one
   hour and read its pages (the `internetarchive` Python library's `ia configure` flow, or the web login with
   a cookie jar; the loan endpoint is /services/loans/loan/ with action browse_book, then the page images
   through the BookReader endpoints). Rules: one book at a time, for a named page check, returned when done,
   never bulk; the account is for the person's own reading. Search-inside and the full-text API need no login.
   First use, 20 Sept 2026: login failed both ways -- the `internetarchive` library's `ia configure`
   (`services/xauthn/?op=login`) and archive.org's current `/login` page both require an email address, and
   IA_USER as set is not one (`account_not_found` from the API; the login page renders only an "Email
   address" field, no username field). Borrowing could not be tested; `tools/ia_borrow.py` implements the
   flow (xauthn login, loan/browse_book, BookReaderJSIA.php for page images, loan/return_loan) but its image
   step is unverified pending a corrected IA_USER.
   Retried 21 Sept 2026 after the person rotated IA_USER to an email-format value and the password: login
   still failed, same `{"success": false, "values": {"reason": "account_not_found"}}` from the xauthn API
   (HTTP 401), but now because archive.org had no account under that email at all, not a format problem.
   **Resolved 23 Sept 2026**: the person registered the account, and `services/xauthn/?op=login` now returns
   `{"success": true}` with session cookies for the address in IA_USER. Login is no longer a blocker. The
   borrow and page-image steps of `tools/ia_borrow.py` are still unverified -- nothing has held a loan yet --
   so the first worker to use it should expect to debug that path and should record what it finds here. The
   response body carries live session cookies: write it to a file, read what you need, delete the file, and
   never print it.
   **Borrow findings, 23-24 Sept 2026:** a held CDL loan serves page images obfuscated for the archive.org reader,
   which `tools/ia_borrow.py` correctly refuses to decode (ASKS row 18), so a loan gives a person a readable page, not a
   worker. Items in the print-disabled tier (`is_lendable: false`, `max_borrowable_copies: 0` on the no-login
   availability check) cannot be borrowed by this account at all (ASKS row 26, Daussy 2001). Check availability and
   be-api fts first; a page read in a lending-only book goes to the person as an ASKS row.
   Without login: `be-api.us.archive.org/fts/v1/search?q=<term>&identifier=<id>` full-text-searches even
   lending-only items and returns snippet highlights, but its `page_num` field is not a real page locator --
   it equals the item's total `imagecount` (confirmed on two different items) -- so this route can confirm a
   term is present/absent and show the surrounding sentence, but cannot cite a page number; page images and
   raw OCR files (`_djvu.txt`, `_hocr_searchtext.txt.gz`, `_page_numbers.json`) all 403 without a valid loan.
   **IA-BORROW job, 25 Sept 2026 (parent worker IA-BORROW, session_01DzmCQYEVbNRHz3etXbHcrV):** `tools/ia_borrow.py`'s
   `browse_book` had a live bug -- it only checked the HTTP status, not the response JSON's `success` field, so a
   200 response carrying `{"success": false, ...}` was logged and treated as a successful borrow; fixed (now
   `die()`s on `success` false, whatever the field's own docstring, message says). Confirmed on real loans this
   session: (1) `correspondancede0006jose` (Correspondance de la Cour d'Espagne VI, collections `inlibrary` +
   `internetarchivebooks` + `printdisabled`) borrows fine (`browse_book` returns `{"success": true}`), but even
   with an active loan and a valid `loan-<id>` token, `<id>_page_numbers.json` still answers 403 -- there is no
   script route from a held loan to a printed-page-to-leaf mapping, only to the leaf-indexed BookReaderJSIA
   manifest; a leaf fetched anyway (leaf 300 of 944, arbitrary) came back with an `X-Obfuscate` header and no
   JPEG magic bytes, confirming the 23-24 Sept obfuscation finding holds for this item too. (2) A `sim_*`
   microfilm/journal item carrying only the `printdisabled` collection (no `inlibrary`/`internetarchivebooks`) --
   `sim_cryptologia_1981-04_5_2` -- hard-fails `browse_book` itself: HTTP 400, body
   `{"error":"This book is not available to borrow at this time. Please try again later."}`, reproduced on one
   retry after a 20 s pause. This is a second, independent confirmation of the print-disabled-tier finding above
   (ASKS row 26, Daussy 2001): a `printdisabled`-only item cannot be borrowed by this account regardless of
   retries. Per this job's brief, the whole job stopped here (first hard failure of the borrow step) rather than
   attempting items 3-5.
   JSTOR: JSTOR_USER and JSTOR_PASS (set 20 Sept 2026) are the owner's JSTOR account, on JPASS monthly from 24 Sept 2026 (unlimited online reading,
   10 PDF downloads a month), used only from the owner's machine (Cloudflare blocks the cloud), online reading only, never PDF downloads; log the article and date in AUDIT.md and never print the credentials.
   **DECODE (de-crypt.org) login, confirmed 20 Sept 2026:** plain CSRF-protected form POST, no client-side
   password encryption despite the site's `ENCRYPTED_PASSWORD` flag (that flag is server-side hashing only;
   checked the unminified `ewcore.js` behind its source map, no JS touches the password field). GET
   `/decrypt-web/login`, read the `csrf_name`/`csrf_value` hidden-input pair, POST them plus `username` and
   `password` back to the same URL with a cookie jar (`-c`/`-b`). A failed login re-renders the same login page
   at HTTP 200 with `"IS_LOGGEDIN":false` embedded in the page's JSON, not a distinct status code or redirect
   — that string is the only reliable success/failure signal. `tools/decode_fetch.sh RECORD_ID OUT_DIR`
   implements this and then fetches `/decrypt-web/RecordsView/RECORD_ID` plus its attachments; it reads
   `DECODE_USER`/`DECODE_PASS` from the environment and never echoes them. As of that date the credentials in
   this environment were rejected ("Incorrect user name or password", confirmed by screenshot) — this is a
   working flow, not a working login; do not retry it repeatedly against the live account (risk of lockout).
   Update, 21 Sept 2026: the person rotated the password and reset `DECODE_USER`/`DECODE_PASS`; a single test
   login with the new pair was also rejected (same `IS_LOGGEDIN:false` signal). One attempt only, per the
   handling rule below — do not retry further without the person confirming the account again (ASKS.md row 1).
   **Resolved 24 Sept 2026, 04:40 UTC:** DECODE_USER is the site's plain user name, not an email (the owner logs in
   with user name and password). The curl form POST is never evaluated by the server, even with every hidden field,
   the submit button and Origin/Referer posted (`tools/decode_fetch.sh` repaired 7401f94, run once: re-rendered,
   IS_LOGGEDIN:false, no 'incorrect' message). A real browser submission works first time:
   `NODE_PATH=$(npm root -g) node tools/decode_browser_login.js RECORD_ID OUT_DIR` logs in headless, lands on
   RecordsList and saves RecordsView/RECORD_ID; cookies stay in the in-memory context. Use it, one login per
   session, fetch everything in that session, and scrub the account name from any saved page before committing.
   Record 8725 (BL Add MS 72438 f.104) carries Status: Decrypted with two documents and two images (fetch pending).
   Handling rule (20 Sept 2026, after two workers echoed a password into their own transcripts): never run
   `env`, `printenv`, `set`, `export -p` or `cat /proc/*/environ` unfiltered; never `curl -v`, `--trace` or
   `set -x` on a command that carries a credential; pass credentials only through `--netrc-file` (mode 600,
   deleted after), a cookie jar, or a library's own config, and test presence with `test -n`. A transcript is
   the person's private log, but a password in it must still be rotated, so say so at once in ROOM.md.
   OpenAlex: the owner set OPENALEX_KEY (24 Sept 2026); append `&api_key=$OPENALEX_KEY` (URL-encoded) to every
   api.openalex.org call, which lifts the per-address daily budget that returned 429 to every cloud session that day. Test
   presence with `test -n`, never print it.
   Semantic Scholar: the owner set S2_KEY (24 Sept 2026); send it as the `x-api-key` header on every
   api.semanticscholar.org call (the unkeyed API answered 429 from the cloud all day on 24 Sept; keyed it answers 200).
   Test presence with `test -n`, never print it.
   Google Books also needs `&country=US` on every call (the API otherwise answers 403 "Cannot determine user
   location" from cloud containers).
   **Credential diagnostic, 21 September 2026:** after DECODE and IA both rejected freshly rotated
   credentials, checked whether `DECODE_USER`, `DECODE_PASS`, `IA_USER`, `IA_PASS`, `GOOGLE_BOOKS_KEY`,
   `JSTOR_USER`, `JSTOR_PASS` are reaching this container intact, using only length/character-class tests
   (`wc -c`, `case` glob tests, per-character `printf '%d'` ordinal checks) — no value or substring of one was
   ever printed, logged, or echoed. Confirmed for all seven: each is set (none unset or empty); no leading or
   trailing whitespace; not wrapped in a leading+trailing quote mark (`'` or `"`); every character is printable
   ASCII (no non-printable byte found at any position); `DECODE_USER` and `IA_USER` each contain an `@`,
   consistent with the person's account being (or being rotated to) an email address. Lengths were recorded
   but are not reported here since a length alone can narrow a value; they were consistent with non-empty,
   plausible credentials for all seven and are in the worker's ROOM.md note for anyone re-running this check.
   Not tested: whether the value matches what the person intended to set (would require revealing it), and
   whether a copy-paste artifact invisible to character-class tests (e.g. a Unicode look-alike character that
   is still "printable ASCII" by this test, or a value truncated by the shell that set it before it reached
   this container) is present — this diagnostic only rules out the specific classes checked above.
   Conclusion: most consistent with **(b)** — the variables are reaching the container intact (correct length
   class, no whitespace padding, no quote-wrapping, no non-printable corruption, `@` present where expected)
   and the rejections seen on 20-21 Sept 2026 are the sites declining the credentials themselves, not a
   transport or quoting fault in this environment. (a) unset/not-reaching is ruled out — all seven are set.
   (c) mangling by quoting or whitespace is ruled out for the specific forms tested (wrapping quotes, leading/
   trailing whitespace, non-ASCII/non-printable bytes). Next step is for the person to confirm the DECODE and
   archive.org accounts and passwords directly with each site (e.g. a password reset flow), not to re-type the
   same values into this environment's variables again.
4. **The person.** Paywalls (State Papers Online, Gale), copy orders, payments, emails to archives and dealers,
   and captchas the browser cannot pass. Write the exact request into the target's `REQUEST.md`, mark the
   target "waiting on you" in the report, and stop. Batch several asks into one REQUEST.md rather than
   stopping at the first.

**Good-citizen rule (owner, 23 September 2026): never get flagged as a bot or spam.** Use each site's official
API where one exists (TNA Discovery API, Gallica SRU, Internet Archive advancedsearch/metadata/download, IIIF
manifests and image API, MediaWiki API with `maxlag=5`) rather than scraping HTML search pages. One request at a time
per host, at least 1.5 seconds apart, never parallel workers against the same host; a few hundred requests per host
per session at most. Fetch once and read from disk after (Usage item 4). On a 429, 403, or a Cloudflare or other
challenge page, stop hitting that host, log it in NOTES.md and ROOM.md, and never retry in a loop; a single retry after
a pause is the limit. Use the browser-style User-Agent only where this playbook says the site needs it; otherwise a
descriptive one, `cipher-lab research script (contact via repository)`. Never automate a login beyond the single
attempt rule above, never bypass a challenge, never use `ignoreHTTPSErrors`. Workers report their request count per
host in the final paragraph.

Test reachability before planning: `curl -sS -o /dev/null -w "%{http_code}" <url>`; `000` means the egress
policy blocks it, in which case say so and stop, since no route above will help.

Once a series is identified as useful (a ledger, a volume, a cipher book), fetch all of it once and record the
manifest (URLs, ids, sizes) in the target folder, so later workers do not refetch. Keep committed images under
30 MB per folder; for more, keep the manifest and a sample and note where the rest can be re-fetched.

### Image and catalogue hosts (table, 25 Sept 2026)

One row per host, from what workers have actually recorded in the repo -- read before rediscovering a route.
"not recorded" means a real search of QUEUE.md, ROOM.md, STATUS.md, sources/, tools/ and LESSONS.md turned up
nothing, not that the host is untried.

| Host | Serves | Auth / key | Works from cloud? | Route or tool | Rate rule | Documented |
|---|---|---|---|---|---|---|
| Gallica (gallica.bnf.fr) | IIIF v2 manifest + native-res image API; SRU search; texteBrut OCR | none | yes (24-25 Sept 2026) with a browser UA; intermittent altcha/SSL-reset; texteBrut endpoint needs a real local browser | `tools/gallica_folio.py`, `tools/iiif_lines.py` | 1-2s apart | LESSONS.md; STATUS.md (Gallica lane) |
| BnF archivesetmanuscrits (archivesetmanuscrits.bnf.fr) | finding-aid search, no images | none | page 1 works via curl; pagination needs a real browser and varies run to run (run twice) | plain POST search form | not specified | LEDGER.md; images not public domain -- permission via manuscrits@bnf.fr or the SINDBAD form |
| British Library IIIF (iiif.bl.uk / bl.digirati.io) | IIIF manifests for BL digitised mss | none | dead since the 2023 cyberattack; access.bl.uk is DNS-dead | none for images; `searcharchives.bl.uk?format=json` works for catalogue only | >=2s, <=120 calls | LESSONS.md; HANDOFF-WEEK.md; QUEUE.md; brief scUK |
| e-codices (e-codices.unifr.ch) | server-rendered full-text search, medieval mss | none | yes (24 Sept), but 0 cipher yield on two full sweeps -- drop from future sweeps | plain search URL | <=15/session | QUEUE.md; ROOM.md; brief scCH |
| e-manuscripta (e-manuscripta.ch) | OAI-PMH (harvest only, no search verb); HTML `/search` | none | partial: OAI reachable; HTML search Cloudflare-challenged once, not retried | `/oai` (harvest only, ~16,400 requests for a full harvest) | <=60/session, >=3s | QUEUE.md; brief scCH |
| Bavarikon / BSB (bavarikon.de + api.digitale-sammlungen.de) | search/object pages + IIIF image API v2 (separate host) | none | yes via the browser tool (Anubis-challenges curl); confirmed working 24 Sept 2026 across 30-45-request rounds | `www.bavarikon.de/search?terms=...` (wildcards -- whole-word tokenizer) then `api.digitale-sammlungen.de/iiif/image/v2/{id}/full/{size},/0/default.jpg` | bavarikon >=3s, <=60-80/session; image API <=15-30/session | QUEUE.md; LEDGER.md; ciphers/trew-schellhammer-1653/NOTES.md; briefs scBAV/scBAV2/scTREW |
| ONB (Austrian National Library, onb.ac.at) | catalogue only, no image API found | none | no usable route -- search.onb.ac.at is a Primo Explore Angular shell, no server-rendered results, not yet tried with the browser tool | none found | n/a | QUEUE.md; LEDGER.md; STATUS.md |
| Europeana (api.europeana.eu) | JSON search (TYPE:TEXT/TYPE:IMAGE), aggregated copy-free IIIF images from hundreds of holdings | `wskey=api2demo` (public shared demo key; EUROPEANA_API_KEY not yet set, ASKS row 47) | yes, reliably, no 403/429/challenge ever logged | `api.europeana.eu/record/v2/search.json?wskey=api2demo&query=...` | <=80/session | QUEUE.md; ASKS.md row 47; ROOM.md |
| DigitArq / ANTT (digitarq.arquivos.pt) | full working-res JPEG images, catalogue full-text search, item detail (reverse-engineered public JSON API) | none | yes, reliable, HTTP 200 | `tools/digitarq_fetch.py` -- the search/advancedSearch endpoints ignore their own query/pagination params; use `/api/rdigital/{docId}?fromIndex=&max=` for the real page list and `/api/rdigital/dissemination?fileId=` for full-size images | >=3s (stricter than the general 1.5s floor), <=150/session | `tools/digitarq_fetch.py` docstring; QUEUE.md ("PARES / DigitArq cipher letters", "Portuguese holdings" sections) |
| BNP / purl.pt (bndigital.bnportugal.gov.pt) | catalogue search, quoted-phrase respected | none | yes | `bndigital.bnportugal.gov.pt/records?...` (NOT `digital.bnportugal.gov.pt`, a proxy CONNECT failure) | 5 queries/session logged, no issues | QUEUE.md; briefs scPT, lane-px-scdict |
| PARES (pares.mcu.es / pares.cultura.gob.es) | dead | n/a | **no** -- dead host, 24 Sept 2026: the origin server's own TLS cert chain is incomplete (not a proxy/trust issue), and even the Wayback CDX index for this host failed the same way once | none; grep the `aaymeloglu/unsolved-ciphers` repo's cached PARES sweep (`catalogue/pares-*.jsonl`) instead | n/a | QUEUE.md ("PARES: blocked, not a bot challenge in the usual sense") |
| Huygens WVO (resources.huygens.knaw.nl/wvo) | advanced-search HTML + CSV export (CSV omits the useful `opmerkingen` field); per-letter detail page has it | none | yes, reliable, no blocks logged | `wvo/app/brieven?opmerkingen=<term>&opmerkingenBool=AND&geavanceerd=1`; `wvo/app/brief?nr=<n>` for detail | >=2s apart, descriptive UA | sources/wvo/NOTES.md |
| Huygens retroboeken -- Heinsius, De Witt, Oldenbarnevelt, Willem III-Bentinck, Staten-Generaal (resources.huygens.knaw.nl) | full-text OCR search across each printed edition (hits letter text AND editorial footnotes) + page images | none | yes, reliable | `retroboeken/<book>/<accessor_id>/index_html?search_term:ustring:utf-8=<term>&batch_start=N` (accessor varies by book); `retroboeken/<book>/pages.json?source=<m>` for the real image URL; `toc1` accessor gives a chronological letter index | >=2-2.1s apart, descriptive UA, ~95-128/session | sources/huygens/NOTES.md (Grotius is a *different* app, grotius.huygens.knaw.nl, covered via the ePistolarium/tc13 backend instead) |
| Nationaal Archief (nationaalarchief.nl / service.archief.nl) | item metadata + full-res JPEG scans + a real IIIF endpoint (service.archief.nl) | none | intermittent -- site-wide maintenance 503 seen once, worked fine other sessions same day; `data.nationaalarchief.nl` does not resolve through the proxy at all, permanently, use `www.nationaalarchief.nl`/`service.archief.nl` instead | read the item page's embedded `drupal-settings-json` -> `viewer.response.availability`/`scans` (the visible "Scan"/"Viewer" boilerplate text is identical whether or not an item is actually digitised -- not a per-item signal), then `service.archief.nl` IIIF `info.json` | >=1.5s, descriptive UA, <=25/host | sources/huygens/NOTES.md; QUEUE.md |
| archieven.nl | intended Dutch-archives cross-search | none | query-form-unverified, not a tested negative -- results load client-side against `mifiles.archieven.nl`, not reverse-engineered; a headless-Chromium fetch also rendered no result list | none confirmed | n/a | QUEUE.md (openarch.nl/openarchieven.nl is a different, unrelated genealogy site) |
| Internet Archive full-text API (archive.org, be-api.us.archive.org) | `_djvu.txt` OCR, `advancedsearch.php` metadata, `be-api.../fts/v1/search` full-text search that works even on lending-only items (its `page_num` field equals the item's total `imagecount`, not a real page locator) | none | yes, extensively used | `tools/ia_numeral_runs.py`, `tools/ia_djvu_headwords.py`, `tools/print_check.py` | 1.5s apart, one at a time | tools/ia_numeral_runs.py docstring; sources/ia-fulltext/NOTES.md; CLAUDE.md item 3 |
| Internet Archive lending/borrow (archive.org) | controlled digital lending, one-hour session loan | IA_USER/IA_PASS (must be an email address; resolved 23 Sept 2026 -- owner registered the account) | login/loan/return all work, but the page image itself is served obfuscated for scripts (`X-Obfuscate` header) -- `tools/ia_borrow.py` detects this and stops rather than decode it; pages must be read by a person in the reader, or via be-api full-text search (no page numbers) | `tools/ia_borrow.py IDENTIFIER --pages N-M --out DIR` | one book at a time, for one named check, returned when done, never bulk | tools/ia_borrow.py docstring; CLAUDE.md item 3 |
| HathiTrust bibliographic API (catalog.hathitrust.org/api/volumes) | volume ids/htids from a record or OCLC number | none (needs a full Chrome UA string) | yes | chained through Open Library search -> OCLC -> this API in `tools/htrc_series_harvest.py` | not specified | CLAUDE.md item 3; tools/htrc_series_harvest.py |
| HathiTrust HTRC Extracted Features API (data.htrc.illinois.edu/ef-api) | per-page token counts only (bag-of-words, no order, no image) for every volume including in-copyright ones | none | yes, reliable, no Cloudflare (a different host from HathiTrust's own site) | `tools/htrc_ef_headwords.py` (headword-location), `tools/htrc_numeral_pages.py` (numeral-density cipher-page detector) | >=1.5-1.6s | tools/htrc_ef_headwords.py, tools/htrc_numeral_pages.py docstrings; sources/htrc/NOTES.md |
| HathiTrust full text / page images (babel.hathitrust.org, catalog.hathitrust.org's own search UI) | full text, page images | none | **no** -- Cloudflare-challenged, does not work from the cloud even with the browser tool, even after the container's TLS-proxy cert fix | none from the cloud | n/a | CLAUDE.md item 2; tools/local_runner_brief.md; LOCAL-QUEUE.tsv rows L3/L4 |
| Google Books (www.googleapis.com/books/v1) | JSON volume search, snippet/full-view text via `accessInfo` links | GOOGLE_BOOKS_KEY (set 20 Sept 2026) | yes, with key + `&country=US` (or 403 "cannot determine user location" from cloud containers); unauthenticated 429s after a few dozen calls | `?q=...&country=US&key=$GOOGLE_BOOKS_KEY`, `filter=full` for full-view only | not specified | CLAUDE.md items 3, 2 (Google Books key notes); tools/print_check.py |
| JSTOR (jstor.org) | article search/read | JSTOR_USER/JSTOR_PASS (owner's JPASS account) | **no** -- Cloudflare blocks the cloud entirely | none from the cloud; online reading only, never PDF downloads, from the owner's machine | n/a | CLAUDE.md item 3; tools/local_runner_brief.md; LOCAL-QUEUE.tsv row L2 / JSTOR-QUEUE.tsv |
| OpenAlex (api.openalex.org) | scholarship search (`works?search=`) | OPENALEX_KEY (header `Authorization: Bearer $OPENALEX_KEY`, not the URL) | yes with the key (10x the keyless per-IP daily budget, which 429'd every cloud session on 24 Sept); still 429s if a pass doesn't send it | `tools/print_check.py`; `api.openalex.org/rate-limit?api_key=` to check budget | <=100 requests/s, budget resets midnight UTC | CLAUDE.md item 3; tools/print_check.py |
| Semantic Scholar (api.semanticscholar.org) | `graph/v1/paper/search` | S2_KEY (header `x-api-key`) | yes with the key; some passes still show 429s, suggesting inconsistent key usage | `tools/print_check.py` (reads S2_KEY/S2_API_KEY/SEMANTIC_SCHOLAR_API_KEY, runs the check only when present) | 1 request/s, no Retry-After -- sleep 1.1s and back off manually | CLAUDE.md item 3; tools/print_check.py |
| DECODE (de-crypt.org) | record metadata/listing (login-free), thumbnails, documents, full-size images (account-gated) | DECODE_USER/DECODE_PASS | listing works with no login at all; login itself works via a real browser (resolved 24 Sept 2026, DECODE_USER is a plain username not an email); full-size images and non-image documents are **account-wide blocked even when logged in**, confirmed from the owner's own browser session -- a role/permission gate, not a route problem | `tools/decode_list.py` (login-free catalogue paging); `tools/decode_browser_login.js` (real-browser login + fetch); `tools/decode_fetch.sh` confirmed broken (its curl POST is never evaluated server-side) | 1.5-2s apart, one login per session | sources/decode/NOTES.md; CLAUDE.md item 3; ASKS.md row 1 |
| Library of Congress (loc.gov) | JSON search/item API (`?fo=json`); `tile.loc.gov` IIIF image tiles; `crowd.loc.gov` By the People transcriptions | none | `www.loc.gov` and `tile.loc.gov` yes, reliable, 200; `crowd.loc.gov` 403 to curl with both descriptive and browser UA | `www.loc.gov/search/?fo=json&q=...` | not specified | QUEUE.md ("Library of Congress digitised manuscripts", LANE N, 24 Sept 2026) |
| NARA (catalog.archives.gov) | catalog search JSON, API v2 | requires an `x-api-key`, requested by email per NARA's own GitHub README; not set in this environment | HTTP-reachable (200) but functionally unusable without the key -- the plain search UI returns huge unfiltered, noise-dominated result counts | none effective | n/a | QUEUE.md (free-key gap) |
| Bodleian (digital.bodleian.ox.ac.uk) | IIIF/search for digitised manuscripts | none | yes, 200 direct | search/IIIF at digital.bodleian.ox.ac.uk | not specified | QUEUE.md; STATUS.md (`archives.bodleian.ox.ac.uk` is the separate Archives & Manuscripts catalogue, copy-order only) |
| CUDL (cudl.lib.cam.ac.uk) | search JSON + IIIF manifests | none | inconsistent -- 403 to plain curl in one pass, answered real queries via the browser tool in an earlier pass the same day; zero cipher-yielding rows found either way | browser tool | not specified | QUEUE.md; STATUS.md; sources/solver-diffs/2026-09-24-lane-n-oxbridge-digital.tsv |
| Beinecke (Yale, collections.library.yale.edu) | IIIF images | none | catalogue search is bot-challenged to plain curl; item-level IIIF fetch works via the browser tool once the item is identified (confirmed on two targets) | browser tool, item ID known first; `dataverse.yale.edu` hosts some material openly (CC0, no login) | <=15-40/session | QUEUE.md; ROOM.md; STATUS.md |
| Folger (catalog.folger.edu, luna.folger.edu) | catalogue, LUNA image repository | none | **no** -- "Human Verification" bot-check page, 403/202-challenge/503 across every attempt, 24 Sept 2026 | none found -- email Folger reference for a digital image or LUNA link | n/a | QUEUE.md; QUEUE-scores.json; STATUS.md |
| Leiden (Universiteit Leiden / UBL) | not recorded beyond a one-line grouping | none | grouped in STATUS.md's "seven catalogues answer curl with bot challenges" list, but no host-specific URL, route or result logged anywhere else | not recorded | not recorded | STATUS.md (grouped only, no dedicated section found) |
| KB (Koninklijke Bibliotheek, kb.nl) | `jsru.kb.nl/sru/sru` real SRU endpoint, GGC (printed-book catalogue) collection only, no manuscripts collection found; `manuscripts.kb.nl/search` ignores its own `?query=` param; `collecties.kb.nl/zoeken` is Cloudflare-challenged | none | jsru.kb.nl yes, but GGC-only yields pure noise for cipher terms (`cijferschrift` = sheet-music notation, not cryptography); manuscripts.kb.nl reachable but non-functional search; collecties.kb.nl blocked | `jsru.kb.nl/sru/sru?query=...&x-collection=GGC` | >=1.5-2s, <=40/session | QUEUE.md; STATUS.md; sources/solver-diffs/2026-09-24-lane-n3-nl.tsv |
| TCD (Trinity College Dublin, digitalcollections.tcd.ie) | digital collections search | none | **no** -- Cloudflare/hCaptcha "One More Step" challenge, confirmed twice, query form unverified beyond that | none working | n/a | QUEUE.md; sources/solver-diffs/2026-09-24-lane-n-ireland.tsv; STATUS.md |
| NLS (National Library of Scotland, manuscripts.nls.uk) | manuscript catalogue | none | **no** -- Cloudflare "Performing security verification" interstitial, confirmed even after the container's TLS-proxy cert fix (named alongside HathiTrust as the two sites that still block post-fix) | none direct; Wayback CDX (`web.archive.org/cdx/search/cdx?url=manuscripts.nls.uk...`) works as a fallback; email manuscripts@nls.uk / the copy-enquiry form | n/a | CLAUDE.md item 2; ciphers/nls-20769/REQUEST.md |
| Antenati (antenati.cultura.gov.it) | Italian vital-records genealogy | none | **no** -- 403 on first attempt and the one permitted retry | none | n/a | QUEUE.md; sources/solver-diffs/2026-09-24-lane-n-italy-a.tsv; LEDGER.md |
| academia.edu | scholars' published papers (key bibliography, e.g. Tomokiyo) | none | **no** -- 403 login wall, every attempt, no exceptions found | none from the cloud; a related (not identical) article sometimes on Tomokiyo's own mirror, cryptiana.web.fc2.com | n/a | sources/cryptiana/README.md; tools/local_runner_brief.md; LOCAL-QUEUE.tsv row L8 |
| Banco de Portugal (bportugal.pt) | the bank's own historical-publications PDFs (OCPEP series) | none | **no** -- 403/connection-rejected on every route, confirmed again 25 Sept 2026, even via headless Chromium | none from the cloud | n/a | ciphers/antt-linhares-chave/AUDIT.md, NOTES.md; LOCAL-QUEUE.tsv row L10 |

Hosts that need the owner's own machine (queued in `LOCAL-QUEUE.tsv`): JSTOR; HathiTrust full text/page images;
Gallica's texteBrut text endpoint specifically (its IIIF image API works fine from the cloud); the actual page
images inside a held Internet Archive loan (obfuscated for scripts, a person must read them in the reader);
academia.edu; Banco de Portugal (bportugal.pt); and narrower cases -- some Google Books full-view volumes, and
archivesnationales.culture.gouv.fr/francearchives.gouv.fr, which do not load from the cloud at all.

Free keys the record shows would help, not yet set: **EUROPEANA_API_KEY** (free at pro.europeana.eu/page/get-api;
lifts the shared `api2demo` throttle on what is already the widest free-image source the scouts use -- ASKS row
47); **DPLA_API_KEY** (free at pro.dp.la/developers/api-codex; no DPLA usage found anywhere in the repo yet,
would add digitised US collections -- ASKS row 47); **a NARA API key** (`x-api-key` for catalog.archives.gov,
requested by email per NARA's own `usnationalarchives/Catalog-API` GitHub README; without it catalog.archives.gov
search is reachable but functionally unusable, drowned in unfiltered noise).



   **Optional discovery keys (listed 25 Sept 2026; the owner adds them in the environment settings, fresh workers pick
   them up; test presence with `test -n`, never print):** `EUROPEANA_API_KEY` (set 25 Sept 2026, answers HTTP 200)
   (Europeana Search/Record API, `wskey=`
   parameter; replaces the shared public `api2demo` key, which is throttled; aggregates IIIF images from hundreds of
   European holdings), `DPLA_API_KEY` (set 25 Sept 2026, answers HTTP 200) (Digital Public Library of America, `api_key=` parameter; digitised US
   collections), `DDB_API_KEY` (not visible as of 25 Sept 2026 22:58 UTC; the owner believes it was added -- re-probe from a fresh session, and check the variable name) (Deutsche Digitale Bibliothek: German archives, libraries and the Archivportal-D;
   authentication as its API documentation at api.deutsche-digitale-bibliothek.de says), `APE_API_KEY` (not set as of 25 Sept 2026) (Archives Portal
   Europe: archival finding aids across Europe, only from institutions that allow API access; per its API page),
   `CORE_API_KEY` (set 25 Sept 2026, probe 22:58 UTC: HTTP 200 with `Authorization: Bearer`, path `v3/search/works/` with the trailing slash -- without it the API answers 301 to an HTML redirect; keyless calls get 429) (CORE open-access full text, `Authorization: Bearer`; for verifiers' scholarship searches). Where a key
   is absent, fall back to the keyless route and say so in NOTES.md; a missing key never blocks a job.

   **Keys are a register, a request tool and an announcement (owner's ask, 25 Sept 2026, about 22:45 UTC).** `KEYS.md` is the
   one list of credential names, their purpose, the tool that reads them and which account has seen them. An agent that needs a
   key runs `tools/key_request.py NAME --purpose "..." --tool tools/x.py --by "<lane/worker>"` (writes the KEYS.md row as
   `requested`, the ASKS.md row for the owner's desk and a ROOM.md flag); the owner adds the variable in the environment
   settings of BOTH accounts (a session started before the change never sees it); the next fresh session on each account
   runs `tools/key_probe.py --sync` inside `tools/room.py --start`, which flips the row to `set`, records the account and
   time in `seen`, and appends "key NAME now set on account X" to ROOM.md, so both parents learn of it at their next
   check-in with no message from the owner. A `set` row seen by one account only is a key the other still lacks; a row
   whose purpose reads "undocumented" is not used until a brief names the service. Accounts label themselves with
   `CIPHERLAB_ACCOUNT` (`ytbiz`, `owner`; ASKS row 63). The prose lists above stay as the how-to per host; KEYS.md is
   the presence record.

   **Key probe, 25 Sept 2026, 22:44 UTC (parent 7d, after the owner reported that keys added on one account for a worker there were
   missed by the other).** `python3 tools/key_probe.py` lists, by name only, every credential variable this container carries
   against the list documented here, and `tools/room.py --start` prints its one-line summary at every session start; a name it
   reports as "set but not in CLAUDE.md" is documented here (what it is for, which tool reads it) before any worker uses it.
   Present on this account at 22:44: the eleven above plus REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET (24 Sept, tools/reddit fetch
   briefs), and three the repository had not recorded: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY (no region variable set) and
   CLOUDSDK_AUTH_ACCESS_TOKEN (Google Cloud SDK access token; no project variable set). Their purpose is not recorded anywhere in
   the repository as of 22:44 (ASKS row: the owner names the service and the job they were added for); until then no worker calls
   AWS or Google Cloud with them. Unset: DDB_API_KEY, APE_API_KEY, CORE_API_KEY, NARA_API_KEY. The two accounts' environments are
   configured separately: a key added for one account is added on the other too, and each parent runs the probe at start.

   **Key probe, 25 Sept 2026.** Presence check (name only, no values printed): `EUROPEANA_API_KEY` set, `DPLA_API_KEY`
   set, `DDB_API_KEY` unset, `APE_API_KEY` unset, `CORE_API_KEY` unset. One test query per set key, key passed only via
   its environment variable: Europeana Search API (`query=cipher&rows=1`) returned HTTP 200, `success: true`,
   `totalResults: 1668`; DPLA (`q=cipher&page_size=1`) returned HTTP 200, `count: 805`. Both keys work from this
   container. Fresh worker sessions started after this point pick up both variables automatically; sessions already
   running before this point do not see newly-added environment variables and should not be assumed to have them.

## Improvement loop

The orchestrator writes a LEDGER.md row when it archives a worker (role, model, cost, outcome code, lesson).
Briefs are copies of the templates in `.claude/briefs/`; a lesson becomes a template edit, not a note. A
retrospective session (`.claude/briefs/retrospective.md`) runs after every 12 ledger rows or $60 of worker
usage, whichever comes first (the orchestrator checks after every worker report), and after any worker scored X
or F; it reads the ledger and the period's log and proposes at most five concrete changes as diffs in
RETRO-<date>.md (approved by the owner 24 Sept 2026, ASKS row 23). The orchestrator applies changes that only touch briefs, tools or workflows, records them in
the ledger, and puts anything that changes the goal, the spend or the person's asks to the person with a
recommendation. Success is measured as cost per delivered result by role, share of workers that stop on
brief, over-claims caught before the person sees them, and whether the top of the queue produces results.
A fix a retrospective finds in one lane's dated COMMON.md and not in the others' is ported into the shared
`.claude/briefs/README.md` common tail in the same pass, not left lane-local (RETRO-2026-09-25h: the wall-clock
cost box and the AskUserQuestion ban each landed in only the one lane that discovered them, twice the same day,
before this rule existed).

## Git

Commit directly to `main`. No pull requests unless asked. Stage by explicit path when several sessions share
the repo. Never rewrite history.
A long-lived orchestrator's GitHub MCP token can go stale mid-session without an error the orchestrator notices
(confirmed 24 Sept 2026: closing eight second-opinion pull requests failed silently against the parent's token
after several hours; a fresh $0.24 Sonnet worker closed them on the first try). Route any GitHub pull-request or
issue write through a short-lived worker rather than a parent that has been running for hours, whether the write
is a second-opinion PR close or an outreach issue post.
The history purge planned on 23 Sept 2026 (`tools/purge_history.sh`, branches `purged-main`, `purged-main-2`) was
dropped on 25 Sept 2026: the owner is fine with his name, email addresses and the images staying in history, and a
scan of every commit that day found no secret. So there is no pending swap, and nobody force-pushes `main`. The one
case that would justify a rewrite is a real credential committed by mistake: then rotate it first, tell the owner in
ROOM.md, and let him decide; never force-push on a session's own judgement.
