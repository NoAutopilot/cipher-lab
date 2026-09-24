# LANE G2 worker A: fr5160 1653 band, reconcile folio 9, then trial the Brienne-family keys with a matched control (Opus, cap $10, disk only)

Target: ciphers/fr5160-letellier-1653 (Brienne to Servien). Read NOTES.md sections "Folio 1-2 letter reconciled" and "1653 band: natives
and folio 9 passes". Also read ciphers/clair1067-brienne-poland-1646/NOTES.md "Interlinear decipherment and key" (key_1646.tsv, same design
family, a different table).

1. Reconcile passA_f9.tsv and passB_f9.tsv (canvas 24/25, 27 lines, 77.7% agreement) against the crops already on disk
   (images/f9r_L*.jpg, f9v_L*.jpg), the way reconcile_f1.py did for folio 1-2, with the same sign spellings. Output ciphertext_f9.tsv,
   inventory_f9.tsv, reconcile_f9.py with --check (rule 7). Commit.
2. Key trial. Apply key_1646.tsv (clair1067 folder), key_brienne_1647.tsv and key_brienne_1651.tsv to ciphertext_f1.tsv and ciphertext_f9.tsv
   (and key_1659.tsv for completeness). Score each by a French-language measure (e.g. quadgram or word-hit rate on the output) and compare with
   a matched control: the same key with its values shuffled over its codes (at least 20 derangements), and the true key on a synthetic
   ciphertext of the same length and sign mix. Report true vs control numbers per key per letter, in NOTES.md and trial_1653.tsv, with the
   script (trial_1653.py). If any key beats its control, list the stretches it reads and grade them S; if none does, say which signs the
   1653 table must differ on (overlap counts) and stop there. Do not attempt a full cryptanalytic solve; name it as the next step if the
   numbers justify it.
3. Report: a NOTES.md section "1653 band: folio 9 reconciled and key trial (24 Sept 2026)".
No network at all. Sign-level judgement from the crops is yours; use a Sonnet subagent only for mechanical counting if at all.

COMMON (every LANE G2 worker, 24 Sept 2026). Parent: LANE G2 orchestrator session_015NqJ9uu5Ef3Bo6QaRiGcGp.
- Read CLAUDE.md in full, then this brief, then the target's NOTES.md sections named below; the last 30 lines of ROOM.md.
- First action: `python3 tools/room.py --start`, then a claim line with `python3 tools/room.py "<role> (<model>, cap $N, for LANE G2)" "claim: <target> -- files: ..."`.
  Last action: a `done:` line with the commit hash and a two-line result. Push with `python3 tools/room.py --push <paths>`; stage by explicit path.
- Run every long job in the FOREGROUND (never background a solver or a fetch loop; two workers went idle that way). Commit and push after each
  pass or step, so a rate-limit stop loses nothing.
- Stop at your cap (the session metadata's cost figure). At the cap, push what you have, write a 'progress' paragraph in NOTES.md, post done.
- Rule 4 grades per token, rule 7 a script that regenerates any reading (prefer tools/decode_key.py with decode.json), rule 3 matched controls for
  any negative. Rule 10: no "new", "first", "unpublished", "previously unread"; say "read at grade X" and "not found in <source>, searched <date>".
  Absolute dates; read `date -u` before writing any time.
- Good-citizen rule: one request at a time per host, >= 1.5 s apart, UA `cipher-lab research script (contact via repository)`, IIIF images only on
  gallica.bnf.fr (.texteBrut is altcha-walled), stop a host on 429/403/challenge and log it. Report requests per host in your done line.
- Keep committed images under 30 MB per folder; above that, keep a manifest and put working copies in your scratchpad.
- End: a short report paragraph in the target's NOTES.md (what was found, where it was not found); do not classify novelty.
