# BNF-Q2-TX (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: transcribe the cipher paragraph of BnF fr.3985 f.89 (Nevers to M. de Gièvre, Nevers, 21 Aug 1593;
`ciphers/fr3985-gievre-1593`, status open, intake gate exit 0 at 08:5x UTC 13 Oct) into key no.60 sign tags, nothing
else: no decode, no key work, no test. Purpose: pool these signs with fr.3622 f.91 for a later order-sensitive test at
larger N (see `ciphers/fr3622-nevers-gondi-1594/ITERATE.md`, BNF-K60 row: control power too low at N=135).
Disk only: the native image is on disk; no network at all.

Cap USD 2.5, box 60 min. Units (per pass, CLAUDE.md Usage 6): crop step (~0.2), 2 blind Sonnet subagent passes
(~0.5 each), 1 reconciliation call (~0.5), write-up (~0.4) = ~2.1. Stop before a unit that would cross 80% of either.
Model: Sonnet, subagents Sonnet.

Read first: CLAUDE.md (rules 2, 4, 6; Usage 6 crop paragraph), TRANSCRIPTION.md, `ciphers/fr3985-gievre-1593/NOTES.md`,
`ciphers/fr3986-nevers-revol-1593/sign_guide.md` (the tag set; the same one f.91 used, plus its BNF-K60 notes on the
c60e6dd tags n+, ls+), `ciphers/fr3622-nevers-gondi-1594/passA.tsv` and `reconcile.tsv` (the format to copy), last 30
lines of ROOM.md.

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap.
2. Crop step, mandatory, run and paste before any subagent call:
   `python3 tools/iiif_lines.py --image ciphers/fr3985-gievre-1593/images/f179_native.jpg --out ciphers/fr3985-gievre-1593/images/f89 --debug`
   (add `--region x,y,w,h` around the 4-line cipher paragraph below the dateline "Nevers, 21 aoust 1593"; adjust
   `--distance/--prominence` once if lines merge). Check the debug overlay; one crop per cipher line, order checked.
   Subagents get ONLY the crop paths and sign_guide.md -- never the full page.
3. Two blind passes (passA.tsv, passB.tsv; one line per crop, `f89_L01<TAB>tags...`, `?` suffix for an uncertain sign,
   `[clear: ...]` for words written in clear inside the cipher, e.g. the closing "ma assurer de voir le Roy bientost").
   Then one reconciliation call against the crops: `tools/reconcile_passes.py passA.tsv passB.tsv --crops images/f89`
   first, the call settles only disagreements.tsv; write reconcile.tsv and ciphertext.tsv in f.91's format.
4. Report pass agreement (tokens agreeing / aligned), N tags after reconciliation, tags not in the no.60 key.tsv, and
   per-line counts in NOTES.md section "## BNF-Q2-TX (13 Oct 2026, account 2)". If agreement < 0.65, say the
   transcription is below f.91's and name the tags the passes split on (for the owner's sorter, never blocking).
5. Commit by explicit path (crops under 30 MB folder total), `tools/file_shrink_guard.py` on touched files, push
   (`tools/room.py --push <paths>`), ROOM done line "for LANE BNF-FOCUS (account 2)": N, agreement, unkeyed tags.

Report what was found; do not classify novelty (rule 10) and do not decode. Never print credentials. Never the words
solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If
`tools/room.py --start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
