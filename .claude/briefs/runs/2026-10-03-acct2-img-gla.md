# IMG-GLA: GLA Karlsruhe finding-aid read for gla-claudiamedici-1633 (3 Oct 2026, written by LANE-IMAGES, account 2)

Model: Sonnet 5 (catalogue search only). Cap USD 2; box 35 min from your claim. One target, catalogue text only, 0 vision calls.
Start: `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`; claim
`python3 tools/room.py "IMG-GLA (account 2 worker, for LANE-IMAGES)" 'claim: gla-claudiamedici-1633 GLA Findbuch 81 + Bestand 48 catalogue read; box ends <HH:MM> UTC'`.
Read ciphers/gla-claudiamedici-1633/NOTES.md ("While waiting" sections, REQUEST.md) and ciphers/hza-hohenlohe-1679/NOTES.md (the
3 Oct LABW route that worked) first.
1. Fetch the Landesarchiv BW / GLA online finding aid (Findbuch 81) tree page for 81 Nr. 441-443 and 812-814 with
   `NODE_PATH=$(npm root -g) node tools/browser_fetch.js URL out.html --shot out.png` (title text is client-rendered); quote each
   unit's record verbatim with its permalink AND its digitisation/availability flag ("Digitalisat" link present or not).
2. Read the neighbours' descriptions for a key, cipher, decipherment ("Chiffre", "Geheimschrift", "dechiffriert", "Auflösung").
3. GLA Bestand 48's finding-aid text (Baden cipher-key rubric, 1676-1761): any item predating 1633 naming Baden/Claudia de' Medici.
4. If any unit is digitised: fetch the cipher pages once (native, manifest.json, folder < 30 MB), no transcription. If not: make
   sure REQUEST.md quotes the catalogue record and the flag (edit it if it does not); add an ASKS row only if none exists for it.
Good-citizen rule: >=2 s between requests, <=40 requests; on a challenge one pause + one retry, then stop. Update NOTES.md (route,
requests per host, what was and was not found). Rule 10 wording; "report what was found and where it was not found; do not classify
novelty". Never call AskUserQuestion.
End: commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>`, confirm on
origin/main, one done line for LANE-IMAGES (account 2).
