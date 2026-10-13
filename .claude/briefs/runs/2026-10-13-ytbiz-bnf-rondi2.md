# BNF-RONDI2 (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: finish the edition check for `ciphers/fr3613-rondinelli-1590` (Hercole Rondinelli to the duc de Nevers, Paris,
11 Nov 1590, BnF Français 3613 no.33, f.62), nothing else. Does Gomberville's *Memoires de M. de Nevers*, seconde partie
(1665, Gallica bpt6k64451005) print this letter (or a deciphered version of it) anywhere in the views BNF-GOMB named?
Do not transcribe, decode or classify the cipher.

Cap USD 2.5 of usage, box 60 min from your claim; stop before starting a step that would cross 80% of either.
Units: 28 views, one image read each, at about USD 0.06 per view from the BNF-RONDI row (0.97 for ~15 reads incl.
overhead) = ~1.7 + one write-up unit. Model: Sonnet.

Read first: CLAUDE.md (rules 1, 5, 6, 10; good-citizen rule), the folder's NOTES.md (BNF-GOMB and BNF-RONDI sections),
the last 30 lines of ROOM.md.

## Route (new; this is the only Gallica route to use)
`gallica.bnf.fr/iiif/` answers Cloudflare 403 to the cloud since 8 Oct. BnF's own API host serves the same images:
`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/bpt6k64451005/f<N>/full/1600,/0/default.jpg` (info.json at
`.../f<N>/info.json` answered 200 on 13 Oct 06:1x UTC; route first logged by D. Bourdeau, cyphersolver
targets/nevers1593/NOTES.md, 12 Oct 2026). Descriptive User-Agent `cipher-lab research script (contact via repository)`,
one request at a time, >= 2 s apart, at most 32 requests in total, fetch each view once to
`ciphers/fr3613-rondinelli-1590/images/gomb/v<N>.jpg` (gitignored or deleted before commit if over 30 MB total; keep a
`images/gomb/manifest.json` with URL, size, sha256). On any 403/429/challenge: stop that host, log it, no loop (one retry
after a pause at most). Never touch gallica.bnf.fr.

## Steps
1. ROOM claim (tools/room.py, single quotes) with box end time and cap.
2. Fetch views 263-273, 387-393, 443-452 (28 views) by a small script, sleep 2 s between requests. Paste the request log
   (view, HTTP code, bytes).
3. Read each view as an image (one image per read; a 1600 px page is enough to see a letter heading and a date). For each
   view record: printed page if visible, letter heading (sender, recipient, place, date), language, and whether anything
   is Rondinelli's 11 Nov 1590 letter or mentions Rondinelli/a "cifra"/a deciphered Italian letter from Paris in Nov 1590.
   One TSV row per view: `ciphers/fr3613-rondinelli-1590/gomb_views.tsv`.
4. NOTES.md: a section "## BNF-RONDI2 (13 Oct 2026, account 2)" with the route, the views read, the result in one line
   (found / not found in the views named, with the edition and pages), requests per host. If not found, update line 1
   only per `.claude/briefs/check-solved.md` (the edition read + pages named; `open` only if the check-solved sources are
   otherwise complete, else keep `blocked` and say what is still unread). Run
   `python3 tools/intake_gate_check.py fr3613-rondinelli-1590` and paste its output.
5. Commit by explicit path, `tools/file_shrink_guard.py` on every touched file, push (`tools/room.py --push <paths>`),
   ROOM done line "for LANE BNF-FOCUS (account 2)" with the result, gate exit code, requests per host.

Report what was found and where it was not found; do not classify novelty (rule 10). Never print credentials. Never the
words solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If
`tools/room.py --start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
