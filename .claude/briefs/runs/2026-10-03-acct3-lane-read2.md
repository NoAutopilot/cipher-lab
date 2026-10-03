# LANE-READ2 (account 2) -- 3 Oct 2026 22:3x UTC (account-3 orchestrator)

Follows LANE-IMAGES (STATUS.md "LANE IMAGES handoff"): images are now on disk or in reach; this lane reads them.
Operating rules exactly as `.claude/briefs/runs/2026-10-03-acct3-lane-pools-images.md` paragraph 1 (lane orchestrator on your own account,
Opus 5.5, workers via create_session, ~6 live, ledger every worker from get_session, stop on allowed_warning or backlog spent; then
"LANE READ2 handoff" in STATUS.md and one done ROOM line). Birago, Armstrong, Debosnys off limits; no folder with a ROOM claim < 6 h.
DECODE images are never committed (manifests + sha1 only). TRANSCRIPTION.md governs every transcription job (crops via tools/iiif_lines.py,
pasted, before any subagent call; per-pass pricing, N reads + 1 reconciliation).

Jobs, in order (one worker each; tools/intake_gate_check.py pasted before each brief):
1. hellen-frederick-1752: transcribe the R4369 key (1751 "Hellen avec le Roy de Prusse") into key.tsv (grade H source), then a known-key
   test on R1953 with a matched control (same key on a shuffled-cipher letter of equal N); decode_key.py --check. Re-fetch per manifest.
2. clair1161-avis-flandre-1688: two blind passes + reconciliation of Gallica btv1b90010063 c185-c188 (46 crops exist for c186R); then
   tools/design_prior.py and the first cheap test with control (breadth rule 3a).
3. siena-concistoro-2308: list which of the 11 records / 24 images carry open (unglossed) cipher vs key tables; for a key + open letter
   pair, a known-key test as in job 1. Re-fetch per manifest, one DECODE login per worker.
4. Mislabelled needs-image folders (images already on disk): clairambault1225-paget-1714, fr5160-letellier-1653,
   fr7129-villeroy-bongars-1604, vanspaen-vandergoes-1808 (+ partly moray-wood-1568, roell-vandedem-1809): one Sonnet worker rewrites
   each folder's last next-step paragraph to the real next step and re-runs tools/next_steps.py; no solving.
5. If backlog left: the highest-EV `partial` rows in NEXT-STEPS.tsv whose blocker is not owner-side (keep going rows), one worker each.
Every worker brief: per-unit cap and box (Usage 6), "report what was found and where it was not found; do not classify novelty".
