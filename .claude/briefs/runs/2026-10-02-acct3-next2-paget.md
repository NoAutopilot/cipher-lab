# NEXT2-PAG (2 Oct 2026, written by account 3; runs on account 2): clairambault1225-paget-1714 decode script + intake check

Model: Fable while it answers, else Opus 5.5. Cap USD 4, box 45 min. One job; stop when met.
Context: NEXT-PAG (7d92609c) found the period decipherment written over 501/505 cipher tokens and built key.tsv (21 codes,
12 C, 9 M; held-out 0.649 vs shuffle p95 0.378). intake_gate_check.py exits 1 on this target for the missing web/blog section.
1. `python3 tools/room.py --start`; claim.
2. The open-web and blog comment-thread check (.claude/briefs/check-solved.md CHECK-SOLVED-WEB step) written to NOTES.md;
   `python3 tools/intake_gate_check.py clairambault1225-paget-1714` must exit 0 before step 3.
3. Write decode.json for the target (examples tools/tests/decode_configs/) so `python3 tools/decode_key.py ciphers/clairambault1225-paget-1714`
   regenerates the reading from ciphertext + key.tsv (+ exceptions.tsv), then `--check` exits 0; `--split-check` output pasted.
   Report per-token grades (rule 4) and, separately, how many code tokens the period gloss itself reads (grade H: read from the
   period's own decipherment) vs the key alone. Judge: `python3 tools/judge_plaintext.py` only if a spec exists.
4. Update the finish-or-blocker sections in place; `python3 tools/gaps_check.py clairambault1225-paget-1714`; update the Paget
   row of PROGRESS.tsv from the files (firm = H+C+S tokens); commit by explicit path; done line. Rule 10 wording.
