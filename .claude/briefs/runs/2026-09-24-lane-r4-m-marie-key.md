LANE R4 WORKER M -- fr3789 MARIE DE MEDICIS TO BREVES 1610: capture the fr.3642 key and the cipher passages (Sonnet, cap $5).
Target: ciphers/fr3789-mariedemedicis-savary-1610 (kind recovery). Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md (you are
one of the two gallica.bnf.fr fetchers). Read NOTES.md points 3 and the Bourdeau notes it quotes (breves1610/NOTES.md in
github.com/dbourdeau/cyphersolver, MIT: shallow clone and grep only, cite it). DECODE images are permission-blocked (ASKS 42): do not log in.
1. Find BnF fr.3642 on Gallica (SRU `gallica adj "Français 3642"`), locate the key leaf (the one DECODE R2077 and Bourdeau name; walk
   manifest labels, not images, to find it), fetch it at native resolution; manifest.json.
2. Fetch fr.3789 canvases 36-37 (10 Nov 1610, ~45 signs) and the 15 Sept 1610 sibling (~70 signs) at native resolution, crop the cipher runs.
3. Transcribe the key as a table (plain -> code), pass A by you, pass B by one Sonnet subagent blind; reconcile; key.tsv. Transcribe the
   two cipher runs twice the same way; ciphertext.tsv. Commit per step.
4. Apply: decode.json + tools/decode_key.py, grades H for key values, --check exits 0. If the key does not read them, say so with the
   decode and stop (no cryptanalysis). Report what was found and where not; no novelty class. NOTES.md "Key capture and reading
   (24 Sept 2026, LANE R4 M)". ROOM done: grade counts and "for LANE V4: ciphers/fr3789-mariedemedicis-savary-1610 reading ready" if read.
