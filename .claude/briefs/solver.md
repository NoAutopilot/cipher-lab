# Solver (Fable, cap $40)
Best case: N<k> (filled in by the orchestrator from check-solved and print-check notes before the session starts:
N1 if this letter's plaintext is in print, including when that print is the crib; N2 if the plaintext is known
elsewhere; N3 otherwise). Under the unique-solves goal a best case below N3 runs on Sonnet with a $5 cap as a
contribution (a key or sign table to hand on), and its verifier is a Sonnet phrase check, not a full audit.
Read CLAUDE.md (rules 3, 4, 7, 10). Target: <folder>. Input: ciphertext.txt and the key source or known
plaintext named here. Produce readings with per-token grades and a script (decode.py --check) that
regenerates them. Report what was read and what was not found, with the search log of any print check you
ran. Paste the judge output. Do not describe a reading the judge failed as a reading; describe it as a
candidate that failed check X. Do not classify novelty; do not continue into sweeps or audits the brief did
not name. + common tail.
Scripts (24 Sept 2026; CLAUDE.md Usage 8): regenerate readings with `tools/decode_key.py <folder> [--check]` and a
decode.json in the folder (examples in tools/tests/decode_configs/) rather than a new decode.py; when you run a print
check, put the distinctive decoded phrases in phrases.txt and the editions in sources.tsv and run
`tools/print_check.py <folder>`; cite print-check.tsv and print-check-hosts.tsv in the search log. Its results are
search results only; novelty stays the verifier's.
