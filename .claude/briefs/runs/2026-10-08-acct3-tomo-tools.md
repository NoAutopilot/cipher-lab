# TOOLS-TOMO (account-4 lane, queued by the account-3 orchestrator, 8 Oct 2026 22:2x UTC by date -u)

Owner, 8 Oct 2026: our method matches Tomokiyo's (period keys carried to siblings), but his ciphertext-only breaks use
instruments we lack -- "add those tools to our toolbox so we use them as needed in the future". Source of every spec:
LESSONS-TOMOKIYO.md Section 2 (his numbered practices, page cited) and Section 3 (c) C1-C7 and (b) B5.
Lane orchestrator, Opus 5.5, cap $60, box 480; operating rules as `.claude/briefs/lane-common-blast.md` (workers on your own
account, about 6 live, ledger from get_session, stop on `rejected`). One worker per tool; each tool is extended into the
EXISTING script named below (CLAUDE.md Usage 8: an option on the shared tool, not a private copy) unless the spec says new.

## The instruments (one worker each, Opus for C6/C7/consistency, Sonnet acceptable for C1/C4/C5)
1. **C4 contacts + KWIC** -- `tools/freq.py --contacts K` (contact table of the K most frequent groups: left/right neighbours
   with counts) and `--kwic GROUP --width W --sort left|right` (every occurrence of one group in context). Practice 5.
2. **C5 long repeats** -- `tools/freq.py --repeats N` (every recurring token n-gram of length >= N with all positions and
   the gaps between them, suffix-array or rolling hash, no O(N^2) limit). Practice 6.
3. **C6 two encipherments** -- `tools/interlinear_align.py --cipher-pair A B` (DP alignment of two ciphertexts of ONE text,
   e.g. a letter and its duplicata in another key or with other homophones; emits symbol-equivalence classes (homophone
   groups), alignment confidence, and clear-word anchors where either copy has clear words). Practice 7.
4. **C3 matrix regularity** -- `tools/key_design.py --matrix` (print a key's letter values as a vowel-headed matrix, flag
   paired first digits / reversed rows / blockwise runs, label one-part / two-part / two-dimensional / blockwise). Practice 4.
5. **C1 spelling part first** -- `tools/freq.py --split-at N` (unigram stats separately below/above N, with the gap search
   that proposes N: where the letter-code band of a nomenclator ends and the word codes begin). Practice 1.
6. **C7 long-word drag** -- `tools/running_key.py --drag MINLEN --corpus DICT` (drag every dictionary word >= MINLEN at every
   offset, quadgram-score the revealed fragment, list top fragments for manual extension). Practice 11.
7. **Consistency across unrelated words** (B5 as a tool) -- `tools/decode_key.py <t> --consistency` (for every S-graded or
   proposed value, list the distinct words of the reading it appears in; a value attested in one word only is reported as
   M-only; a summary line per target). Practice 16. Do NOT change CLAUDE.md rule 4 (the owner's); the tool reports.

## Gates for every instrument (CLAUDE.md rule 3 and Usage 8a)
- `--help` documents the option; an offline test in tools/tests/ covers it, including at least one case it must NOT flag.
- **Known-answer control on a case Tomokiyo actually solved** (LESSONS-TOMOKIYO.md Section 1 table names the page): run the
  instrument on that case's ciphertext as if unsolved and show it surfaces what broke it (e.g. C6 on Servien 1632's two
  encipherments, servien.htm; C4/C1 on a Nevers-collection nomenclator; C3 on a matrix.htm key; C7 against hessen-1824's
  existing control; C5 on a case where long repeats gave the break). Report the control's number beside a shuffled/null
  run that can fail differently (rule 3's "a control that cannot vary" paragraph). A tool whose control does not surface the
  answer is shipped as `controlled-only: failed` on the shelf, not withdrawn.
- Then ONE live run on a target we hold where Section 3 (d) names that practice as an untried step (destaing-gerard-1779,
  berthier-napoleon-1812, hessen-1824, ...), after `tools/intake_gate_check.py` and `tools/prior_work.py` on that target;
  report what was found and where it was not found; do not classify novelty.

## Toolbox registration (the point of the job; the lane's close checks every item)
- `tools/data/tool_shelf.tsv`: one row per instrument (tool+option, kind instrument, grade from its control: proven /
  controlled-only / failed, `use_when` written in the words a future brief would use: "code with 300 groups and no key",
  "two copies of the same letter", "nomenclator letter band", "long repeated runs", "a value read in one word only"...,
  evidence = the control numbers with file path, last_outcome = the live run). `python3 tools/tool_shelf.py "<problem>"`
  must return the new row for three test phrasings per tool (paste them).
- `SYSTEM.md`: each new option named on its tool's row (`tools/system_map_check.py` passes).
- `LESSONS-TOMOKIYO.md` Section 3 table: column (a) updated for each practice now covered, with the tool+option.
- `CLAUDE.md` Usage 8 ("Shared scripts before new ones"): ONE added line naming the seven options as "Tomokiyo's ciphertext-
  only instruments" and pointing to tool_shelf.tsv; no other CLAUDE.md edit.
- `.claude/briefs/README.md` common tail: one line -- "a code or nomenclator with no key in hand: run tools/tool_shelf.py on the
  problem and use the Tomokiyo instruments it returns before any family run".
- Close: LEDGER rows, STATUS.md "LANE TOOLS-TOMO handoff" (per tool: option, control result, live-run result, shelf grade),
  `work_queue.py --done TOOLS-TOMO`, ROOM done line for acct3-orchestrator; `tools/file_shrink_guard.py` on every touched file.
