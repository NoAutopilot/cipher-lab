# PREMISE-NEVBIR (2 Oct 2026, written by account 3; runs on account 2). Owner: keep everything moving.

Model: Sonnet (owner, for premise checks), else Opus 5.5. Cap USD 3, box 40 min. Search only; no decoding.
Target: ciphers/nevers-birago-fr3251-1572, the SEVEN undeciphered 1572 letters in BnF fr.3251 (ff.138 no.71, 144 no.73,
152 no.77, 160 no.82, 168 no.85, 174 no.86, 184 no.90; NOTES.md "Undeciphered"). no.87 (f.178) is the key's own source
and is N0 (AUDIT.md) -- not in scope.
1. `python3 tools/room.py --start`; claim.
2. Run the Premise check of .claude/briefs/check-solved.md for EACH of the seven letters: (a) every decipherment, gloss,
   clear copy or "dechiffrement" the folder's own NOTES/REQUEST/AUDIT/harvest files mention for that folio -- open it;
   (b) Tomokiyo's nevers.htm / Cryptiana pages and both solver repos' WORKING files (not status lists) for any rendering of
   these folios; (c) the leaves and canvases on each side of each letter on Gallica (manifest already on disk under
   images/ or harvest/) for a clear copy or decipherment laid in, as at canvas 182; (d) recipient-side print: the Nevers
   papers' editions (Mémoires de Nevers 1665, Gomberville), Italian/Savoyard documentary editions for Birago 1572.
3. Write "## Premise check (PREMISE-NEVBIR, 2 Oct 2026)" in NOTES.md with a per-folio table: (a)-(d) found / not found /
   unreachable, and a per-folio verdict: CLEAR TO TEST, CALIBRATION (decipherment exists), or FOUND-SOLVED.
   `python3 tools/intake_gate_check.py nevers-birago-fr3251-1572` must exit 0 afterwards (paste it).
4. Commit by explicit path; done line listing the folios that are CLEAR TO TEST. Rule 10 wording.
