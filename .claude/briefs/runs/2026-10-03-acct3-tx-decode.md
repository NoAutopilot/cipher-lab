# TX-DECODE (account-3 orchestrator, 3 Oct 2026): key-constrained decoding over per-sign candidates

Read TRANSCRIPTION.md (pipeline step 6). Model Opus 5.5. Cap USD 10, box 75 min. Disk only: vision calls: 0 x USD 1.5 = 0.
Build tools/key_decode_lattice.py: input a top-k TSV (sign position, candidates, scores), a key (tools/decode_key.py
key.tsv format) and a language model (tools/judge_plaintext.py corpora); output the most probable sign sequence and its
plaintext by Viterbi/beam over the lattice with a per-candidate prior from the reader scores, and the list of every
position where the choice differs from top-1 (to be graded S, never H). Built-in controls (rule 3): the same decode under
200 shuffled keys (the real key must beat them by rank/z, else the gain is the language model inventing text), and a
known-answer run: Birago no.87 top-k (from TX-ATLAS-B72, or synthesize top-k from the two line passes + lookalike
confusions if that has not landed) must move toward the clerk sheet, err_true reported before/after. Only if the
known-answer run improves and the shuffled-key control holds: re-test f.117, f.144, f.168 (rank/z, power at err_true)
and report; no reading is committed by this job, results go to NOTES.md as candidates for a verifier.
Shared files: ROOM claim/done via tools/room.py; update the TRANSCRIPTION.md "Today" column and SYSTEM.md (system_map_check ok) for any new tool, with --help and an offline test in tools/tests/ (Usage 8). gaps_check/file_shrink_guard before the final push. Never print credentials, never name the owner, never AskUserQuestion. Done line "for the account-3 orchestrator" with the headline number.
