LANE R5 WORKER G -- KEY NO.60 SIGN ATLAS from interlined leaves, then re-run F1's two leaves (Opus, cap $8; recovery calibration).
Parent 7b's 20:45 instruction, with one correction: fr.3983 f.169 (KS-04) is under key no.46 (two-digit figures), not no.60, so it cannot
calibrate no.60's symbols. Use instead the two interlined leaves of the SAME copyist that F1 and F2 named (every sign there has a
contemporary value written over it): the Instruction of 31 Aug 1593, BnF fr.3985 f.126-130 (ark btv1b90606498, canvases 264-268), and
Henri IV's interlined letter fr.3986 f.151/152 (ark btv1b9060631k; canvas by Bourdeau's ratio c = 118 + 2.058*(folio-64), eye-check).
Common rules: .claude/briefs/runs/2026-09-24-lane-r5-common.md. Read: ciphers/fr3985-nevers-revol-1593/NOTES.md (F1 section), the F2 and F3
sections in fr3986/fr3987/fr3990 NOTES, tools/keys/key60.tsv, key60_atoms.md, key60_segment.py (F3's shared files; extend, do not fork).
1. Fetch (gallica.bnf.fr IIIF image API, >= 2 s apart, <= 15 requests; you are this lane's only Gallica fetcher): the interlined cipher
   runs of c.264-268 (start with two canvases; add more only if the sign inventory is not yet covered) and of fr.3986 f.151/152.
2. Build the atlas: for each cipher sign with its interlined value, a crop (tools/glyph_atlas.py or tools/iiif_lines.py), the value
   written above it, and the key60.tsv entry it matches; tools/keys/key60_atlas/ with atlas.tsv (sign_id, this-hand form description,
   interlined value, key60 code, agreement yes/no) and a contact sheet. List every place where Bourdeau's key60 value and the
   interlined value disagree (F3 found some key values conflict with his enciphering-sheet column).
3. Calibrated re-run on F1's leaves (ciphers/fr3985-nevers-revol-1593, images on disk): pass A by you against the atlas, one blind
   Sonnet pass-B subagent given the atlas contact sheet; reconcile. Gate 80%. Pass -> settle, decode_key.py, --check exit 0, grades,
   and report whether it reads as French. Fail -> report agreement and stop.
Price: ROOM progress line after step 2 with cost. At 80% push; at $8 stop.
NOTES: tools/keys/key60_atoms.md gets an "Atlas from interlined leaves (LANE R5 G)" section; fr3985 NOTES.md "Calibrated re-run (24 Sept 2026,
LANE R5 G)". ROOM done: "for LANE V5: ... reading ready (H h M m I i)" only if it reads as French; else "for LANE R5: key60 atlas <n> signs,
F1 re-run agreement <x>%, cost $c". Rule 10 wording.
