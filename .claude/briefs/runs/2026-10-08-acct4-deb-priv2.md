# DEB-PRIV1D / DEB-PRIV2A / DEB-PRIV2B -- Debosnys private-repo steps (run IN the account-4 standing session)

Written by LANE DEB-RUN (account 4, session_01KBx2V5yEGzw3yFXtCMgaAz), 8 Oct 2026 00:5x UTC by date -u, on the
account-3 orchestrator's ROOM flag of 8 Oct 00:40 UTC (PRIV1 part (d) approved ~$7.5; PRIV2 "the bigger lever").
RESTRICTED.md (ciphers/debosnys-1883/) binds every step: no image, crop, transcription, quotation or description of a
museum scan enters the PUBLIC repository, a ROOM line, an artifact or any prompt outside the private repo. Public side,
per row: one ROOM line and one ITERATE.md row "<ROW>: done / not applicable / stopped at gate, held per RESTRICTED.md"
plus the numbers that describe only the PUBLIC transcription or a synthetic control (never a scan's content).
Rows run in order; each is its own WORK-QUEUE row; a row whose gate fails stops the rows after it.
Crop step for every vision call (CLAUDE.md Usage 6): `tools/iiif_lines.py --image <scan> --out <private scratch dir>`,
output pasted before the first subagent call; a full-page image argument to a subagent is the brief's error.

## DEB-PRIV1D -- letter-form habits (cap USD 7.5, box 60 min; Opus 5.5 orchestrating, Sonnet subagents)
Part (d) of .claude/briefs/runs/2026-10-07-acct4-deb-priv1.md (parts a-c already done in the private repo, 1 Oct):
does a frequent cipher sign (X, PCT, O-TILDE, Y-CURL, A-LOOP, and the pictograms) share its form with a letter-form
habit of his clear hand? Units: one Sonnet call per clear-hand scan on line crops, ~0.15 USD; stop before a unit that
crosses 80 pct of cap or box. Control: the same question on two public non-Debosnys 19th-c. hands in the same calls;
a decoy "yes" voids that call's yes. Output: a sign -> letter-form candidate table, private only.

## DEB-PRIV2A -- is the museum material a better transcription source? (cap USD 6, box 45 min)
Gate step, cheap. (1) Do the scans in hand include the cryptogram sheets themselves (the museum's reply of 7 Oct says its
26 original foolscap sheets were all sent on 28 Sept; numbered pages end at 10)? If none shows a cryptogram: write
"DEB-PRIV2: not applicable" and stop all PRIV2 rows. (2) If yes: pixels per sign on each cryptogram page vs the public
images (public: 15-30 px per sign, swarm/DIGEST-2 s2). (3) Known-answer control, as DIGEST-2 requires before any re-read:
rebuild swarm/R2/R2-2's synthetic known-answer page (t_low.py recipe: tiles cut from the NEW images, boxes with a settled
id, same class mix, fresh seed) and have two blind readers (Opus 5.5 calls, as R2-2/H63) read it. Gate to run PRIV2B:
two-reader error on the new-image known-answer page <= 8 pct (public pixels read 15.6-17.7 pct; H63 coarse-folded 7.3).
Above 8 pct: log "museum images do not lower the floor enough" with the number, stop.

## DEB-PRIV2B -- two blind passes + reconcile, then the solvers (cap USD 22, box 150 min; runs only on a PRIV2A pass)
Units (per pass, not per page; Usage 6 AX-COMP2/bMALS): 6 page images (c1, c2a, c2b, c3, c4a, c4b) x 2 blind passes =
12 reader calls + 6 reconciliation units = 18 units at ~1.2 USD (nearest ledger rate: H21b/H23 Fable calls) = ~21.6.
Order: c4 (verse, cleanest) and c2 first, c1 and c3 last; stop before a unit crossing 80 pct of cap or box.
(1) Passes on line crops, in the 160-id inventory (glyphs/inventory.tsv, public), `tools/reconcile_passes.py` to merge.
(2) Measure: per-sign disagreement between the two new passes, and between the new reconciled reading and the public
settled drafts (ciphertext_c1/c2/c34_draft.tsv). Public side may carry these percentages (they describe the cipher
transcription's agreement, not the scans' content) -- but the new reading itself stays private until the museum's
written permission.
(3) Only if the new-image error estimate is < ~8 pct: re-run, privately, the automatic solvers whose controls failed
only on noise, each control FIRST at the new measured noise and at the pooled N (family_run.py homophonic, DIGEST-1's
syllabic C method, H's Copiale pipeline `pipeline.py copiale --noise <new>`); target only if its control passes.
Report what was found and where it was not found; do not classify novelty. A pass of any solver goes to a separate
verifier session; nothing about a reading is published before the museum's permission (RESTRICTED.md rule 2).
