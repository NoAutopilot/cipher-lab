# READ2-RELABEL: fix the next-step paragraph of six folders mislabelled needs-image (3 Oct 2026, written by LANE-READ2, account 2)

Why: LANE-IMAGES (STATUS.md "LANE IMAGES handoff") found six NEXT-STEPS.tsv rows with blocker `needs-image` whose images are already on
disk; the label is tools/next_steps.py's keyword guess from each folder's LAST next-step paragraph. Fix the paragraph, not NEXT-STEPS.tsv.
Folders: clairambault1225-paget-1714, fr5160-letellier-1653, fr7129-villeroy-bongars-1604, vanspaen-vandergoes-1808, and (partly)
moray-wood-1568, roell-vandedem-1809. No solving, no fetching, no transcription.

Model: Sonnet. Cap USD 5; box 45 min from your claim, whichever first. Units: 6 folders, disk-only, ~USD 0.5 each. Before starting a
folder, stop if it would take you past 80% of the cap or the box.

Start: read `.claude/briefs/README.md` "Common tail" and follow it. `python3 tools/room.py --start` (detached HEAD: `git push origin
HEAD:main; git checkout -B main HEAD`); `date -u`; check ROOM.md for a claim younger than 6 h on any of the six folders (skip that
folder if so); claim with `python3 tools/room.py "READ2-RELABEL (account 2 worker, for LANE-READ2)" 'claim: next-step paragraph fix, 6 mislabelled needs-image folders (clairambault1225-paget-1714, fr5160-letellier-1653, fr7129-villeroy-bongars-1604, vanspaen-vandergoes-1808, moray-wood-1568, roell-vandedem-1809); box ends <HH:MM> UTC'`.
Read `tools/next_steps.py`'s docstring (how it picks the paragraph and the blocker keywords) and IMAGES-AUDIT-2026-10-03.tsv rows for the six.

Per folder:
1. `ls ciphers/<t>/images` and read images/manifest.json: which leaves are on disk (with crops?), which are not.
2. Read NOTES.md's last sections (Remaining gaps / Escalation / While waiting / Next step). Find the paragraph next_steps.py reads.
3. Append (never rewrite earlier sections) a short dated section "## Next step (READ2-RELABEL, 3 Oct 2026)" naming the real next step
   given what is on disk -- e.g. "images on disk at images/<files>; next: two blind passes + reconciliation per TRANSCRIPTION.md, ~$<n>"
   -- and, where only part of the material is on disk (moray-wood, roell-vandedem), name both: the step for what is on disk, and the
   copy order still needed for the rest (quote its existing REQUEST.md/ASKS row; file nothing new). For a `partial` folder keep the
   Remaining gaps / Escalation format and run `python3 tools/gaps_check.py <t>`, pasting its line.
4. After all folders: `python3 tools/next_steps.py` and check each of the six now shows the intended blocker/step (paste the six rows).
   If next_steps.py still misreads a folder, change only the wording of your own paragraph; do not edit the tool.

Rule 10 wording; no novelty claims. Never call AskUserQuestion. End: commit by explicit path (the six NOTES.md files + NEXT-STEPS.tsv if the
tool rewrote it), `python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>`, confirm on origin/main, one done line
for LANE-READ2 (account 2) listing per folder old -> new blocker, "cost: see the lane ledger".
