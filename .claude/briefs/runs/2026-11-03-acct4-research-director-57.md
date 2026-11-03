# Research director, wave 57 (3 Nov 2026, 03:0x UTC by date -u): first two hot runnable rows after the 30 Oct-3 Nov gap

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Owner's directive 3 Nov 2026: all purchases on hold -- no copy order,
quote or paid request of any kind; free routes only. Read CLAUDE.md rules 3, 4, 6, 7 and Usage 6 before starting. Stop at 80% of the
box or the cap, whichever comes first; a unit that would cross either is not started.

## JOB ELEC-KLUCK (account 4; Sonnet 5; cap USD 3; box 40 minutes; hosts: archive.org, at most 12 requests, >= 1.5 s apart; Price: vision calls: 4 x USD 0.30 = 1.20)

Target ciphers/fr5761-election-1519 (status `open`). Read NOTES.md from "## Remaining gaps (SUP-ELECTION, 20 Oct 2026)" to the end,
and the SUP-ELECTION six-question block just above it (the Lbar Palatin/Treves conflict on f.116r l.29). Paste the output of
`python3 tools/intake_gate_check.py fr5761-election-1519` first; a nonzero exit stops the job.
1. **Kluckhohn pp.813-814 page images.** archive.org item `bub_gb_0gFoAAAAMAAJ` (Kluckhohn, Deutsche Reichstagsakten unter Karl V,
   Bd. 1): find the leaf numbers for printed pp.813-814 from the item's `_djvu.txt` (already used for the OCR read; fetch it once if
   not on disk under ciphers/fr5761-election-1519/images/ or sources/ia-fulltext/) and fetch the two page images at a readable size
   (the BookReader page endpoint, or `https://archive.org/download/<id>/page/n<leaf>_w1200.jpg` style; record which worked in
   images/manifest.json). Read each page image yourself (2 vision calls) against the OCR lines quoted in NOTES.md: does the print
   read "Palatin" at p.814 l.14 as the OCR has it, and what does the printed sentence say around it (quote it, with the page and
   line). Then compare with the two l.29 signs on the committed crops (elec356/ or elec2r/ crops named in NOTES.md; 2 vision calls
   at most): which sign position does the printed name fall on, counting the clear words before and after. Write the answer as a
   dated section "## ELEC-KLUCK (3 Nov 2026)" in NOTES.md: print confirmed or not, which l.29 sign carries Palatin, grade (C only if
   the print and the position agree; else M), and whether the Lbar = Treves pair stands. Update the "Lbar Palatin/Treves conflict"
   gap line in "## Remaining gaps" and the clear-pages escalation box; never edit key.tsv -- propose the change as a `--try` line.
2. **Lisch V pp.323-347 (the third Lbar/flag/4 slot).** Only if step 1 finished under 60% of the box: locate Lisch, Jahrbuecher des
   Vereins fuer meklenburgische Geschichte, Bd. 5 on archive.org by advancedsearch (<= 4 requests), fetch its `_djvu.txt` once, grep
   pp.323-347 for the 1519 election letters and the names Palatin/Pfalz, Trier, Mainz, Coeln, Sachsen, Brandenburg, and record hits as
   a table (columns: page, line, name, sentence) in the same NOTES.md section. No page images for Lisch in this job.
3. Six questions (learned; assumptions; unverified; alternatives; most informative next; continue/pivot) in five lines at the end of
   the section; `python3 tools/gaps_check.py fr5761-election-1519` must pass; file_shrink_guard on NOTES.md and images/manifest.json;
   commit, push. Report: five lines (print verdict, l.29 sign, Lisch hits, requests per host, files).

## JOB NEVREVOL-PREREG (account 4; Opus 5.5; cap USD 4; box 60 minutes; hosts: none (disk only); Price: vision calls: 12 x USD 0.15 + 1 reconciliation = 1.95)

Target ciphers/fr3987-nevers-revol-1593 (status `blocked` internally, SUP-NEVREVOL 20 Oct 2026: the value-shuffled-key control
failed its positive control, so the atlas passes were never run). Read NOTES.md from "**Control first, and it failed its gate.**" to
the end, PREREG-SUP-NEVREVOL.md, controls_sup.py (note: its target branch expects ciphertext_v2.tsv, which does not exist yet; the
positive-control branch does not need it), controls_pos.txt, images/v2/crops_note.md and manifest.json, sign_guide.md, and
tools/keys/key60_atlas (the 264ext atlas). Paste `python3 tools/intake_gate_check.py fr3987-nevers-revol-1593` (a `blocked` head is
"already terminal, nothing to gate" -- that is the expected line, proceed; the block is internal, SUP-NEVREVOL's own next step).
1. **Re-PREREG.** Write PREREG-NEVREVOL-2.md before any pass: hypothesis (the 264ext atlas fits the f.66 hand well enough that a
   key-no.60 decode of the six densest lines scores above chance); gate = real S ranks <= 10/201 against BOTH (a) 200 length-class
   value shuffles of key no.60 (values permuted only within a value-length class) and (b) 200 shuffled-order nulls of the transcript;
   positive control first, on synthetic passages that mix letter, syllable and word signs in no.60's own proportions (extend
   controls_sup.py --positive with a `--mixed` option rather than a private script), at 0%, 10% and 20% injected sign error, 10
   passages each; the job continues only if the positive control passes its own gate in >= 8/10 passages at 0% AND >= 6/10 at 10%
   (rule 3: the injected-error level must bracket the hand's own disagreement, 51% pass agreement on the 24 Sept draft is the
   warning sign -- if the control dies by 10%, stop, log "control below gate at the hand's error band" in HYPOTHESES.md and
   NOTES.md, and do not run the passes). Decision block with the stop criterion written before the control runs.
2. **Two blind atlas passes**, only if the control passed. Unit = one crop (images/v2 holds 12: six lines, two halves each).
   Pass A: you read each of the 12 crops yourself (strongest model, this session), one crop per look, labelling every sign with the
   atlas labels in sign_guide.md. Pass B: one subagent call per line pair (6 calls, Opus 5.5, crops only, no key, no pass A). That is
   12 counted vision calls plus your reconciliation of the disagreements against the crops (the +1 unit). Write ciphertext_v2.tsv
   (line, pos, sign, pass agreement), reconcile_v2.tsv (disagreements settled from the image, never from the key), then run
   controls_sup.py's target branch for the gate against both nulls and write the row to HYPOTHESES.md with both numbers. Decode with
   `python3 tools/decode_key.py ciphers/fr3987-nevers-revol-1593 --check` only if the gate passed; grade per token (rule 4); no
   reading is claimed unless the gate passed and the judge output is pasted.
3. Six questions in five lines in NOTES.md "## NEVREVOL-PREREG (3 Nov 2026)"; update "## Remaining gaps" and the retry box;
   `python3 tools/gaps_check.py fr3987-nevers-revol-1593` must pass; file_shrink_guard on every touched file; commit, push.
   Report: five lines (positive control numbers at 0/10/20%, gate result with both null ranks or "not run", pass agreement,
   files, commit).
