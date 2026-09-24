LANE R4 WORKER A -- POSTHIUS 1614/1618 CAPTURE: crops and two blind passes of the cipher lines and key blocks (Sonnet, cap $4).
Target: ciphers/trew-posthius-1614-18 (stage 2, kind recovery). Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md.
Read .claude/briefs/transcription.md and the target's NOTES.md "What is on the leaves" first.
Images are ON DISK (images/, manifest.json: 1614_p1 2000 px + native key crop; 1618_p2 2000 px + native key crop2). Work from
disk. Host, only if a crop needs native resolution the disk copies lack: api.digitale-sammlungen.de IIIF image API v2 (ids in
manifest.json), at most 6 requests, >= 1.5 s apart, add each fetch to manifest.json. No other host.

Material (small, a few lines each):
 (1) 1614 recto: the 4-line cipher block (Latin letters), the two-line key "Salutembcdfg / hiknopqrwxyz", the clear note above it
     ("Eandem descriptionem ... Camerario") and the clear line below it ("Fridericus Henricus vocat[ur] recens natus Princeps").
 (2) 1618 address side: LEFT key block (plaintext letters + drawn glyphs, struck through), RIGHT key block ("Conradbefgbi" /
     "Klm.pqstuwxyz" as eyeballed -- do not trust this reading), and the worked specimen lines under it (German + cipher letters).
Steps:
1. Cut line crops of (1) and (2) with tools/iiif_lines.py (or its --image/local-file mode; if it lacks one, add a --image option
   with --help and a test in tools/tests/ rather than a private crop script). Check the --debug overlay. Commit crops+manifest, push.
2. The left 1618 block has drawn glyphs: build a small atlas first (tools/glyph_atlas.py; codes G1..Gn, contact sheet), then passes
   use its codes. The Latin-letter lines need no atlas.
3. Two BLIND Sonnet subagent passes (they are not shown NOTES.md's eyeball readings): letter by letter per line, one row per
   character position, columns line, pos, char, conf; keys written as the two rows exactly as they stand on the leaf (column
   alignment kept: which top letter sits over which bottom letter). Commit and push each pass as it lands (passA.tsv, passB.tsv).
4. tools/reconcile_passes.py passA.tsv passB.tsv --crops <crop dir>; settle only disagreements.tsv rows from the crops; write
   ciphertext.tsv (cipher lines), key_leaf_1614.tsv and key_leaf_1618_left.tsv / key_leaf_1618_right.tsv (top, bottom, pos,
   agreement), specimen_1618.tsv, and clear_lines.tsv (the clear notes as transcribed). Report agreement per block.
No decoding, no key application, no identification of the prince (the solver does that). NOTES.md section "Capture and passes
(24 Sept 2026, LANE R4 A)". ROOM done line ends "for LANE R4: posthius capture ready".
