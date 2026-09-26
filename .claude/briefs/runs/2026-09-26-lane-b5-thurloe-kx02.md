JOB bTHU (LANE B5, Sonnet worker). One line: QUEUE.md KX-02 / "Scored backlog for LANE B6" rank 1 -- extract the four further Thurloe State Papers cipher letters with printed glosses (Lockhart from Chauny 19 June 1656, vol.5 p.101; Nutley; Attorney General Prideaux; Sir Benjamin Wright, vol.3) from the djvu text on disk, align cipher groups to gloss with tools/interlinear_align.py, and add them to ciphers/thurloe-printed/ in the existing format.

Read first: `.claude/briefs/runs/2026-09-26-lane-b5-common.md`, QUEUE.md KX-02 row and the Scored backlog section, ciphers/thurloe-printed/NOTES.md and index.tsv (the P-row format), `tools/interlinear_align.py --help`. Intake: `python3 tools/intake_gate_check.py thurloe-printed` (paste; if nonzero, stop and say why).

Cap and box: $2 or 30 minutes from your first `date -u`, whichever first. Disk only: `sources/ia-fulltext/collectionofstat0{3,5}thur_djvu.txt` (if absent, one archive.org download of each _djvu.txt, >= 1.5 s apart, and record it).

Steps:
0. `date -u`; `python3 tools/room.py --start`; ROOM claim (tools/room.py) naming ciphers/thurloe-printed/.
1. Script-extract each letter's cipher-numeral runs and the printed gloss spans (grep, not reading the volume). Record page, letter, sender, date, N groups.
2. Align with tools/interlinear_align.py; grade C (plaintext from the print). Report groups aligned, conflicts with values already in the thurloe-printed key (agree / disagree counts: agreement with the existing key is the control -- a disagreement rate above about 10 percent means the alignment or the key family is wrong; say which).
3. Add rows to index.tsv in the existing P-row format; NOTES.md section with the four letters. The plaintext is Birch's own print: this is a contribution (key values from a printed gloss), not a decipherment; say so. Push; done line with aligned count and agreement vs conflict counts; report in five lines. Do not classify novelty.
