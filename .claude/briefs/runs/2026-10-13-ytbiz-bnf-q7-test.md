# BNF-Q7-TEST (Opus worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: one pre-registered, controlled test of "BnF fr.3982 f.25 (Nevers to the Grand Duke of Tuscany, 26 Aug 1592) is
enciphered in Nevers key no.62" (`ciphers/fr3982-nevers-toscana-1592`, status open, intake gate exit 0). Disk only,
no network. Nothing above grade M; a pass goes to a separate verifier, never to an outward sentence.
Cap USD 6, box 120 min; stop before a unit that would cross 80% of either. Units: read + key audit (~1), PREREG (~0.5),
control (~1.5), target + nulls (~1), write-up (~1). Model: Opus.

Inputs (BNF-Q7-KEY, 13 Oct): `key_no62.tsv` (114 rows, 99 H / 15 M: names and words 201-297, nulls 227/294/295, and a
letter section with single digits and 31-39, some polyphonic e.g. 34 = b|c, 35 = f|g), `ciphertext.tsv` (f.25, 6 lines,
260 digits written continuously, `?` = uncertain digit, passes agree 0.905; no digit 8 occurs). Tomokiyo (nevers.htm,
fr.3995 section): no.62 is "Substitution by figures. Polyphonic. Nulls. Figures 201-297 represent names and words (in
Italian)"; the fol.115v note gives 263227 = Nivers (227 null), 297295 = Gran duca (295 null).

Read first: CLAUDE.md rule 3 in full (matched design, error band bracketing the transcription's, the orthogonality check,
calibration-as-gate), rules 4 and 7, the folder's NOTES.md (BNF-Q7-ID and BNF-Q7-KEY sections), last 30 lines of ROOM.md.
Paste `python3 tools/intake_gate_check.py fr3982-nevers-toscana-1592` first.

Steps
0. ROOM claim (tools/room.py, single quotes) with box end and cap.
1. Key audit, before anything is scored: is the letter section complete enough to encipher Italian (list the letters with
   no figure)? Are f.25's digit pairs/triples inside the key's code set at all -- the share of the string that a DP over
   the key's code lengths can parse with no leftover, versus the same DP on 1000 digit-shuffled copies of the string (a
   STRUCTURAL check, reported as a number, not a reading). If the key's letter section cannot cover Italian, or the parse
   share is not above the shuffle p95, stop: log "key no.62 does not fit f.25 at this transcription (structural)" with
   both numbers, and say whether the fit failure could be the table transcription (M rows) rather than the letter.
2. PREREG (`ciphers/fr3982-nevers-toscana-1592/PREREG-Q7.md`, committed before any score): the decoder (DP segmentation
   over the key's code lengths, polyphonic values expanded, scored by an Italian 4-gram model built from tools/data/it16dip
   -- name the files, held out from any control windows), the statistic (a length-normalised in-order log-likelihood, or
   the count of it16dip lexicon words >= 5 letters in the best decode -- pick one that GROWS with N, unlike BNF-K60's
   longest-word statistic), the null (decode of the target under 1000 value-shuffled keys that keep the key's code-length
   classes, AND under 1000 digit-order shuffles of the target -- the statistic must be able to differ under both), and the
   gate: control power >= 0.8 at p <= 0.01 at the target's measured error band, else NON-TEST.
3. Control: 200 synthetic texts, it16dip windows (held out) of f.25's plaintext length, enciphered with key_no62.tsv
   itself (polyphonic choices uniform, names/words where the window has them, nulls at a share you state), written as one
   continuous digit string, with digit errors injected at 0%, 5%, 10% and 15% (the passes disagree on ~9.5%: the band must
   bracket it). Power per error level, negative control (random digit strings of the same length and digit frequencies).
4. Target: one run on ciphertext.tsv as committed (uncertain digits: state the rule, e.g. first reading). Report the
   statistic, both null p-values, and the best decode only as a draft in NOTES.md, every token graded M at most.
5. ITERATE-style row in NOTES.md (date | hypothesis | instrument | matched control | result | verdict | what it taught) and
   a "next best attempt" line; `tools/gaps_check.py` if the folder becomes partial.
6. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM done
   line "for LANE BNF-FOCUS (account 2)": structural fit numbers, control power per error level, target statistic and p.

Report what was found and where it was not found; do not classify novelty (rule 10). Never print credentials. Never the
words solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If
`tools/room.py --start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
