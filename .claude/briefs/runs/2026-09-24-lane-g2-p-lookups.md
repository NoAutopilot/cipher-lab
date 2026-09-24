# LANE G2 worker P: three small Gallica lookups (Sonnet, cap $4, Gallica fetcher, about 12 requests)

Direct image endpoint only (/iiif/ark:/12148/<ark>/f<N>/full/<size>/0/default.jpg); one retry per URL after a pause, then stop that URL.
1. fr5160-letellier-1653 (LANE V2 verifier V5 asks, ROOM 09:55): fetch canvas 131 (f.68r) and canvas 127 (f.66r) at native or 2000 px to your
   scratchpad. Is f.68 a clear duplicate or a decipherment of the f.67 letter (10 Oct 1659), or a separate letter? Compare with
   reading_f67 (NOTES.md 'Folio 67: reconciled and read'); quote the opening lines. Then Gallica full-text search (SRU / ContentSearch service
   on btv1b9060495t, and globally) for 'maniement des affaires' Servien 1659 and 'mesintelligence' 'Altesses Royalles' 1659; log hits or none.
   Write the answer into NOTES 'Folio 67' as a sub-section and post 'for LANE V2' in ROOM.
2. fr2751-dediou-mayenne: fetch f.116r (the cipher leaf; the last worker got two resets). If it comes, cut crops with tools/iiif_lines.py
   --debug and run ONE blind Sonnet pass (passA.tsv) only; report the extent. If it fails after one retry, stop and note it.
3. clairambault296-paget-1713 (M26, ark btv1b9000759b): pin the Paget letter's canvas (finding aid folio + label check or thumbnails), and
   record it in NOTES.md. Note that clairambault1225-paget-1714 (M4) is the same correspondent a year later: say whether the hands and cipher
   look alike from the images (one line). No passes.

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
