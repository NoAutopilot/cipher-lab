# LANE G2 worker N: M32 fr.2751 De Diou to Mayenne (League era), cipher with its own decipherment: pin, capture, passes (Sonnet, cap $6, Gallica fetcher)

ONE target, strict cap. Gallica on 24 Sept: manifest/services endpoints reset often; the direct image endpoint
(/iiif/ark:/12148/<ark>/f<N>/full/<size>/0/default.jpg) works. After one retry per URL stop that endpoint and report; do not route around.
Target: ciphers/fr2751-dediou-mayenne. Read its NOTES.md and sources/cryptiana/web/mayenne.htm (two published Mayenne-De Diou tables in
other volumes, fr.3982-3984/3995/4715: type them into key_mayenne_*.tsv with the citation, for a later trial).
0. First establish that fr.2751 is digitised (finding aid DAO link or SRU); if not, write REQUEST.md, set status blocked, and stop.
1. Pin the item to canvases (tools/gallica_folio.py or the finding aid folio + label check), fetch 1000 px views to find the cipher and the
   decipherment, then natives of those leaves only (images/manifest.json, under 30 MB). Record folio, canvas, layout, date line in NOTES.md.
2. Crops (tools/iiif_lines.py --debug) and two blind Sonnet passes of the cipher (passA.tsv, passB.tsv); one pass of the decipherment
   (dechiffre.txt). Then a mechanical trial of each published Mayenne table on pass A with a shuffled-key control (trial.tsv).
NOTES.md section "Capture and passes (24 Sept 2026)". No alignment; an Opus aligner follows.

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
