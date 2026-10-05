# ZOOM-SCAN (written by account 3, 5 Oct 2026, for account 1). Model Sonnet 5 is enough (scripted scan + short judgement); Opus floor applies if the dispatcher requires it. Cap $4, box 40 min.

Start: `git fetch origin && git checkout -B main origin/main`; ROOM claim via tools/room.py. Public repo only; no images.

Goal: list the targets where an owner's zoomed screenshots would unlock the next step (owner, 5 Oct 2026: "if I can
provide a zoomed in version and that meaningfully unlocks things, add it as a task").

1. Script, not reading: grep ciphers/*/NOTES.md (status open/partial/blocked) for resolution blockers (too coarse,
   illegible at, low-res, ppi, cannot tell signs/digits apart, image too small, needs higher resolution).
2. Keep a target only if BOTH: (a) the blocker is image detail, not missing material/key; and (b) the cloud cannot get a
   bigger image itself -- the host is in CLAUDE.md's table as blocked/challenged/low-res (BNE, RAH, DECODE full-size,
   HathiTrust page images, Folger, NLS, PARES, a viewer with no IIIF), or NOTES.md records that the largest cloud fetch
   was still too small. Gallica/BSB/Huntington/NARA IIIF targets are NOT kept (the cloud already gets native size; a
   worker should refetch at full/max instead -- list those separately as "refetch, no owner").
3. Write ZOOM-ASKS.tsv (repo root): target, shelfmark+page, viewer_url (opens AT the page if the site allows; test
   with curl -I only, one request per host), first_words, last_words (where the cipher starts/ends on the page),
   est_shots, why (one line from NOTES.md with its line number), unlocks (the named next step), priority (H/M/L by
   PROGRESS.tsv closeness to a counted result). Plus a short "refetch, no owner" list in the same file's footer.
4. Add ZOOM-ASKS.tsv to SYSTEM.md (tools/system_map_check.py passes). Push by explicit path. Done line: count kept,
   count refetch-only, top 3 by priority. Do not create board cards (the orchestrator does) and do not email anyone.
