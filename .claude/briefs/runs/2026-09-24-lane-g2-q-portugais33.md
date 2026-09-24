# LANE G2 worker Q: M29 Portugais 33, viceroy of India (São Vicente) to Afonso VI, 1667, "carta que foi por çifra": capture + passes (Sonnet, cap $6, Gallica fetcher)

ONE target, strict cap. Direct image endpoint only; one retry per URL, then stop that URL and report.
Target: ciphers/portugais33-saovicente-1667 (ark btv1b104629623, item pinned at canvas f263 = fol.129r by the digitisation check). Read NOTES.md.
1. Fetch 1000 px views of canvases ~258-270 to find the whole item (cipher leaves, any clear text, any decipherment, the other two letters
   of the 1667-68 series); record per canvas in NOTES.md. Then natives of the cipher leaves only (images/manifest.json, under 30 MB).
2. Crops with tools/iiif_lines.py --debug (check the overlay) and two blind Sonnet passes (passA.tsv, passB.tsv; the second never sees the
   first); agreement with tools/reconcile_passes.py. Describe the cipher system (numerals? symbols? nomenclator range?) in two lines.
3. If a decipherment or a clear duplicate is present, transcribe it (dechiffre.txt) and say so first: that makes it a recovery.
NOTES.md section "Capture and passes (24 Sept 2026)". No decoding.

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
