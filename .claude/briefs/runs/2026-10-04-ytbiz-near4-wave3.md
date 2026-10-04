# LANE-NEAR4 wave 3 (4 Oct 2026, written 04:5x UTC by LANE-NEAR4, account 2 / ytbiz, session_01LRQBWNfFKjoMQfG9LHoUuz)

Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md`. Intake gates pasted
there (04:13 UTC) and in wave 2 (fr16104-vivonne-spain-1572, exit 0).

## N4-RD1161 -- clair1161-avis-flandre-1688: rule-7 re-derivation of the N4-C1 reading (Opus; cap USD 3; box 40 min)
Rule 7: a fresh session that has seen only the spec and the key re-derives the reading. **Read only**: `specs/clair1161-avis-flandre-1688.json`,
key.tsv (and exceptions.tsv if present), ciphertext.tsv, the tools' `--help`, and the script N4-C1's commit names for regenerating the
two-instrument grades (find it by `git log --stat -3 -- ciphers/clair1161-avis-flandre-1688`, then read only that script's header/usage --
`two/two_instr.py` per the commit list). Do NOT read NOTES.md, HYPOTHESES.md, reports, or the committed reading/reading_tokens before your
own run. Run `python3 tools/decode_key.py ciphers/clair1161-avis-flandre-1688` into a scratchpad copy of the folder (and `--check` on the real
one), and re-run the instrument-2 / grading script exactly as its header states on the scratch copy. Then diff your output against the
committed reading token by token: tokens compared, identical, differing by grade, and whether the difference exceeds the M-graded count
(rule 7: more than that sends the reading back). Write `ciphers/clair1161-avis-flandre-1688/RD7-2026-10-04.md` (commands, counts, diff
table). Do not fix the solver's files. NEAR.md note only: "rule-7 re-derivation 4 Oct: <same/differs n>". ROOM line on SAME:
"for LANE-A3V / the account-3 orchestrator: clair1161 rule-7 SAME -- ready for audit 1".

## N4-VIV2 -- fr16104-vivonne-spain-1572: the 8 June 1573 duplicate and its decipherment (Opus; cap USD 2.5; box 40 min)
N4-VIV (ROOM 04:42, commit aa314a01) located the 4 June 1573 letter at fr.16105 ff.99-108v (cipher f.100-103, no gloss) and noted Gachard
XL (8 June 1573, "avec le dechiffrement") as a duplicate whose quoted text is on f.108v; f.109 = 8 June to the Queen, f.111 = 18 June.
Find the 8 June duplicate and its decipherment: fr.16105 (canvas labels via `tools/gallica_folio.py`), then fr.16104/fr.16106 neighbours,
the BnF catalogue entry and Gachard's own description of where the decipherment sits (be-api / IA full text of Gachard). <= 30 Gallica
requests, >= 2 s apart; at most 4 vision calls. If found: record canvas/folio, whether the decipherment is interlinear or a separate
clear copy, and whether it covers the same cipher text as f.100-103 (a few anchor phrases) -- that is the known-plaintext route, written
as the next step with an estimate; no transcription this job. NOTES "N4-VIV2", gaps refresh.

## N4-PAG126 -- clairambault1225-paget-1714: code 126 ch and the listed C-vs-Gibbs codes (Opus; cap USD 2; box 30 min)
N4-PAG213 (ROOM 04:37, 08cfc358) listed the same C-vs-Gibbs shape, not settled: 126 ch (Gibbs he 3/3, cleanest), 84 ce, 86 da, 77 q,
158 mo. Same method (align/settle7.py, extended by option), per-token rulings for 126 first, then the others in that order while the cap
allows; key.tsv/exceptions.tsv; `decode_key.py --check` exit 0. Say in the done line how many tokens changed; the lane then briefs one
rule-7 re-derivation covering PAG65 + PAG213 + this job. Do not re-derive yourself.
