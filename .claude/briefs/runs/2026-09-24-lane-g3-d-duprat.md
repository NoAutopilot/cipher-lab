# LANE G3 worker D: M30 fr.2967 Duprat, remaining canvases for ciphertext (Sonnet, cap $4, Gallica fetcher)

Target: ciphers/fr2967-duprat (ark btv1b9059840r). Read NOTES.md: five 'Déchiffrement' items, canvases 77, 82, 91, 118 probed are clear-prose
decipherments; about 120 canvases unviewed. Job (LANE G2 handoff priority 3): walk every unviewed canvas at 600-800 px (direct IIIF image
endpoint, >= 1.8 s apart, at most 140 requests), and record per canvas in walk.tsv: canvas, stamped page, content (print / clear letter /
decipherment / ciphertext / blank), date and heading if legible. For any leaf carrying ciphertext (numerals, symbols, nomenclator groups): fetch
its native, note whether a decipherment in the volume matches it (same date, heading), and stop there (no passes; the orchestrator briefs capture).
If none: say the volume carries no ciphertext in N canvases walked. NOTES.md section 'Canvas walk (24 Sept 2026)'; status line unchanged unless
the walk closes it (then 'closed-negative' with the reason: decipherments only, no ciphertext).
