# LANE TOOLS-TOMO jobs (account 4, lane orchestrator session_01SMKmyCZXCV6TQpjRUdoPWg) -- 8 Oct 2026 22:4x UTC by date -u

Lane brief: .claude/briefs/runs/2026-10-08-acct3-tomo-tools.md (read it in full; its "Gates for every instrument" apply to every job).
Cap 60, box 22:35 UTC 8 Oct - 06:35 UTC 9 Oct. Source of every spec: LESSONS-TOMOKIYO.md Section 2 (practice numbers) and Section 3 (c).
Tomokiyo's pages are on disk under sources/cryptiana/web/ (read with `python3 tools/html2text.py <file>`; never edit sources/). Credit
Tomokiyo by page in every docstring, NOTES section and shelf row (CLAUDE.md rule 8). No code from a repository without a licence
(aaymeloglu/unsolved-ciphers: cite only); Tomokiyo's Perl on polygram.htm is described, not copied.

Orchestrator findings before briefing (22:4x):
- `tools/freq.py` ALREADY has `--contacts K`, `--kwic`, `--width`, `--sort`, `--repeats N`, `--split-at N` (BER-KWIC, 27 Sept 2026,
  LEDGER row "parent worker BER-KWIC"), tested in tools/tests/test_freq.py and run live on berthier-napoleon-1812 against a
  shuffled-order control. What it lacks against the spec: the gap search that PROPOSES N for --split-at, the gaps between repeat
  positions, and any known-answer control on a case Tomokiyo solved. LESSONS-TOMOKIYO Section 3 was never updated for it.
- `--cipher-pair`, `--matrix`, `--drag`, `--consistency` do not exist yet.
- `tools/tool_shelf.py` now accepts option rows: tool cell `freq.py --contacts` (commit 8210cbe1). --check requires the option string
  in the tool's source. `--check` on main already fails on 17 MISSING rows from other sessions' tools: not yours; your rows must not
  add to that list. `python3 tools/tests/test_tool_shelf.py` has the same one pre-existing FAIL ("real shelf"), nothing else.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, the tool file(s), cap and box end time, addressed "for LANE TOOLS-TOMO (account 4)". If --start
  fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- You own exactly the tool file(s) named in your job and their test file. Do not edit another job's tool. Extend the existing script
  (CLAUDE.md Usage 8): an option and its functions, existing behaviour and tests unchanged (run the tool's existing tests before and after).
- Each option: `--help` text naming Tomokiyo practice + page; an offline test in tools/tests/ (synthetic fixtures) covering the
  option, including at least one case it must NOT flag (CLAUDE.md Usage 8a: state in the docstring what it is meant to catch and one
  kind it must not).
- Known-answer control on a case Tomokiyo actually solved (LESSONS-TOMOKIYO.md Section 1 table names the page; cipher material from
  sources/cryptiana/web/ or a ciphers/ folder that holds a period/published key for the case): run the instrument on that ciphertext as
  if unsolved and say whether it surfaces what broke it, with a number. Beside it, a null/shuffled run whose statistic CAN differ from the
  target's (rule 3, "a control that cannot vary" paragraph: say in one line why your null can fail differently). If no Tomokiyo-solved
  case with ciphertext on disk exists for your instrument, use the nearest case in the repo with a period key (H-graded) and say so; if
  that fails too, a synthetic matched control, and the shelf grade is then `controlled-only`, never `proven`. A control that does not
  surface the answer ships as grade `weak` with evidence "controlled-only: failed ..." -- not withdrawn.
- Pre-register the control's pass line in `tools/tests/PREREG-<JOB>.md` (or the target folder) pushed BEFORE the control runs.
- ONE live run on a target we hold where the instrument names an untried step: first `python3 tools/intake_gate_check.py <target>` and
  `python3 tools/prior_work.py <target> --step-type <type>` (paste both, exit codes; exit 4 rows are owed by you per
  .claude/briefs/prior-work-step.md, `--record` them). Exclusions: any folder with a ROOM claim < 6 h old and no done line (grep the last
  600 ROOM lines); eckert-*, Birago, Armstrong, Debosnys, every folder in a live 8 Oct jobs file under .claude/briefs/runs/. Write a dated
  NOTES.md section "<JOB> (8 Oct 2026)" in that target with the command, its head, what it found and where it found nothing. Report what
  was found and where it was not found; do not classify novelty; no status-line change unless rule 5 requires one; if the target is
  partial, keep `python3 tools/gaps_check.py <target>` passing.
- Registration (yours): one row per option in `tools/data/tool_shelf.tsv` (columns tool, kind=instrument, grade, use_when in a briefer's
  words, evidence = control numbers + file path, last_outcome = the live run, date); then paste
  `python3 tools/tool_shelf.py "<phrasing>"` for THREE phrasings per option showing your row in the top 3. Name the option on its tool's
  row in SYSTEM.md (one parenthesis, like freq.py's BER-KWIC note) and keep `python3 tools/system_map_check.py` passing. Do NOT edit
  CLAUDE.md, LESSONS-TOMOKIYO.md or .claude/briefs/README.md: the orchestrator does those once at close.
- Good-citizen rule if you touch a host (you should not need one). Rebase before writing shared files (tool_shelf.tsv, SYSTEM.md, ROOM.md);
  keep both facts on conflict. Commit only your own paths. `python3 tools/file_shrink_guard.py <every file you touched>` before the final
  push; push with `python3 tools/room.py --push <paths>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did. Never name the owner; never print credentials;
  never call AskUserQuestion.
- Stop at the cap or at 80% of the box, whichever first; do not start a step that would cross 80% of either. Opus session floor ~1.5.
  No subagents unless the job says so (these are script jobs).
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <option: control number vs null; live run; shelf
  grade; commit>` "for LANE TOOLS-TOMO (account 4)", then a five-line final report giving per option: control case + number, null number,
  live-run target + finding, shelf grade, the three tool_shelf phrasings.

## Wave 1 (22:4x UTC 8 Oct)

### TT-FREQ (Opus, cap 10, box 180 min): tools/freq.py C4 + C5 + C1 (practices 5, 6, 1)
Options exist (see findings). Do: (a) audit each against the lane brief items 1, 2, 5 and add only what is missing: `--split-at auto`
(or `--split-gap`) gap search that proposes N -- the value where the low letter band of a nomenclator ends (largest gap / frequency-profile
break in the sorted numeric values, reported with the low block's size and IC beside the high block's); `--repeats` must print the gaps
between successive positions and must not be O(N^2) in the ngram length (rolling hash or suffix array; test on 20,000 tokens under a few
seconds); `--contacts` must give left/right neighbour counts. (b) Known-answer controls on Tomokiyo-solved cases: C4 on a case where a
contact chart broke it (ormonde.htm, Clanricarde to Ormonde, or a Nevers-collection nomenclator with key in ciphers/fr*-nevers* --
show the contact table makes the key-known suffix/prefix or vowel groups stand out); C5 on a case where long repeats appear in the
ciphertext (Section 1 "frequency or repeats" rows; or a monoalphabetic letter in the repo with a period key) -- show the recurring n-grams
fall on a repeated plaintext word; C1 on a nomenclator with a period key whose letter band is known (e.g. a Nevers-collection or
wallisdecipher.htm "numbers up to about 64 reserved for letters") -- does the proposed N land at the true band edge (report |error|),
and on a shuffled-VALUE null (values redrawn uniformly over the range -- this can move the gap, unlike a shuffled-order null).
(c) Live run: berthier-napoleon-1812 already has C4 and C5 (BER-KWIC); run the proposed-split (C1) there or on destaing-gerard-1779 if
berthier's NOTES show C1 already run with an N. Shelf rows: `freq.py --contacts`, `freq.py --kwic`, `freq.py --repeats`,
`freq.py --split-at`.

### TT-PAIR (Opus, cap 10, box 180 min): tools/interlinear_align.py --cipher-pair A B (C6, practice 7)
Build `--cipher-pair A B` (two token files of ONE text in two encipherments, or a letter and its duplicata): DP (Needleman-Wunsch with
affine gaps or the tool's existing DP) over the two token streams, iterating align -> symbol-equivalence update -> realign (servien.htm:
"align -> identify -> realign"); a contradiction is a one-place shift; tokens marked clear in both copies are anchors (plaintext, not
nulls); a clear word in one copy against cipher in the other is emitted as a crib. Output: equivalence classes (A-symbol <-> B-symbol
with counts, merged into homophone groups when two A-symbols map to one B-symbol), per-position alignment confidence, the crib list.
Control: Servien-Sabran 1632 (servien.htm): the page gives both PLAINTEXTS in parallel lines (a)-(h)... and the cipher symbols only as
images. If no transcription of the two ciphertexts is on disk (grep sources/ and ciphers/ for Baluze 155 / servien), build the control as:
the two real Servien plaintexts (as printed on servien.htm, with their real wording differences) each enciphered by an independent random
homophonic key of the period shape (about 2-3 homophones per frequent letter, a few nulls), clear words left clear where the page says they
were clear; score = fraction of recovered A<->B equivalences that are correct (same plaintext letter) and fraction of true homophone pairs
recovered. Null: the same but with copy B a DIFFERENT text of the same length (another passage from servien.htm or a fr17 corpus passage),
which the alignment can fail on. This is semi-synthetic: shelf grade `controlled-only` unless a real two-copy ciphertext with known answer
exists in the repo (search: "duplicata", "duplicate", "two copies", "second copy", "register copy" in ciphers/*/NOTES.md; LESSONS-TOMOKIYO
Section 1 "two encipherments compared" rows) -- if one does, run it too and grade from it. Live run: a target in ciphers/ that holds two
encipherments of one text (from that grep); if none qualifies, say so and log the live run as "no eligible target". Shelf row:
`interlinear_align.py --cipher-pair`.

### TT-MATRIX (Opus, cap 7, box 150 min): tools/key_design.py --matrix (C3, practices 3 and 4)
Build `--matrix KEY.tsv` (a key's letter values, from a target's key.tsv or a two-column file): lay the letter cipher values out as a
vowel-headed matrix (matrix.htm "Why Matrix?": rows/columns by digits), flag paired first digits (1=2, 3=4), reversed rows, alphabetical
runs (one-part), blockwise one-part (alphabetical blocks in shuffled order), two-dimensional (alphabetical down a column, across a row) and
none (two-part/random), with the evidence counts; and from a PARTIAL key (a few letters identified), predict the rest when a regular
arrangement fits ("once a couple of letters are identified, the whole cipher alphabet may be inferred"). Control: keys printed on
matrix.htm (papal 1550s-60s, Spanish 1585-1590 blocked-square) and any repo key Tomokiyo describes as regular (ormonde, schiner):
label each correctly, and from 2-3 given letters predict the rest -- report letters predicted correct / total. Null: the same keys with
values randomly permuted over letters (labels must fall to "none", prediction must fail). Live run: the tool over every key.tsv in
ciphers/*/ with a recovered or period key (or a sample of 20 if more), writing ciphers/_triage/key-matrix-2026-10-08.tsv; name any key
flagged regular whose target still has unread siblings. Shelf row: `key_design.py --matrix`.

### TT-DRAG (Opus, cap 9, box 180 min): tools/running_key.py --drag MINLEN --corpus DICT (C7, practice 11)
Build `--drag`: for every dictionary word of length >= MINLEN (from DICT: a word list, or a tools/data corpus's word types) at every
offset of the ciphertext, derive the other side's fragment (running key: plain = cipher - key, both sides symmetric -- any fragment may
belong to plaintext or key, runningkey.htm "Tips"), score it with the tool's existing quadgram model for the language, and list the top
fragments with offset, word, fragment, score and a z-score against the fragment-score distribution; option to restrict to words from a
crib list. Control: hessen-1824's existing running-key control (ciphers/hessen-1824/HYPOTHESES.md and NOTES bHCP/bHCP2/bHCP3 rows: the
matched control at N=164, the de19 corpus) -- a synthetic running-key cipher of the same N, language and key-source design: does the drag
put a true key or plaintext word at its true offset in the top 10? Report hits@10 over >= 5 seeds. If a Tomokiyo-described running key
(runningkey.htm: Brown's 2026 challenge, plaintext and key given?) is on disk with its ciphertext, run it too and grade from it. Null: the
same drag on a ciphertext enciphered with a RANDOM (non-language) key, where true-word hits must collapse. Live run: hessen-1824 (Section
3 (d): rule 3 "untested-by-this-tool" names a different instrument -- this is it), MINLEN 10 then 8, de19 word types; write the top 20
fragments to NOTES and say whether any extends by hand. Shelf row: `running_key.py --drag`.

### TT-CONS (Opus, cap 6, box 150 min): tools/decode_key.py <t> --consistency (practice 16, B5 as a tool)
Build `--consistency`: for every key value used in the target's reading (decode_key.py's own grading output), list the distinct words of
the reading it appears in (word = run between the reading's word separators; for a reading without word separation, use the decode's
word segmentation if decode.json gives one, else say "no word segmentation" and stop for that target); a value attested in only one
distinct word is reported "M-only (one word)"; per-grade counts and one summary line per target ("values: N; in >=2 unrelated words: K;
one-word only: M"). "Unrelated" = different words, not inflections of one stem (a 4-letter shared prefix counts as related; say so in
--help). The tool REPORTS; it does not regrade (CLAUDE.md rule 4 is the owner's, unchanged). Control: breaking.htm (Tomokiyo's own
"Occurrences of 9(W) in 'wards' and 'with' and those of 24(O) in 'cooperate' and 'you' are consistent") -- if that ciphertext and key are
on the page, rebuild the case as a decode_key target fixture and show 9 and 24 come out as multi-word; also a repo target with an H-graded
period key (e.g. a tools/tests/decode_configs/ example). Null: the same reading with a deliberately wrong value injected for one
mid-frequency code (it must come out in fewer unrelated words, or the reading breaks) and a random key (most values one-word or none).
Live run: `--consistency` over every target whose decode_key output carries S-graded tokens (grep reading/grades files), summary TSV at
ciphers/_triage/consistency-2026-10-08.tsv, and name the S values attested in one word only. Shelf row: `decode_key.py --consistency`.
