# Siblings and key search: BL Cotton MS Caligula C II, in and around f.277 (Randolph-Sussex, 9/5 July 1570)

Worker: Archive Lookup / sibling search, 23 September 2026. Scope per brief: `siblings/` only; `NOTES.md`,
`ciphertext.txt` and `images/` belong to the concurrent Transcription worker and were not touched.

## Headline finding: the decipherment exists, on the very next leaf, f.278 — reported by Bourdeau, not
independently confirmed against the images this session (see "What was blocked" below)

`dbourdeau/cyphersolver` (github.com/dbourdeau/cyphersolver, MIT code / CC BY 4.0 text; cloned fresh this
session, commit `2e9ec0165feff163b692453cae5eaa0776c14c65`, dated 2026-09-23 08:37:36 -0500, clean working
tree, remote verified as `https://github.com/dbourdeau/cyphersolver.git`) now carries a solved write-up for
this exact letter at `randolph1570/` (public page:
https://dbourdeau.github.io/cyphersolver/randolph1570.html, title "Randolph to Sussex, 5 July 1570 — Read").
Quoting `randolph1570/NOTES.md` and `randolph1570/profile.json` from that repository:

- **f.278 is a half-leaf, docketed "5 July 1570"**: a clerk re-copied every cipher word from f.277, divided
  by strokes, and wrote the plaintext over each; the short runs are deciphered at the foot in clear. DECODE
  record R4932, status "Decrypted". This is exactly the kind of contemporary interlinear/marginal
  decipherment the brief asked to look for — but it is a sibling *leaf of the same letter* (f.278, the next
  folio after f.277), not a different letter in the same cipher.
- Bourdeau's own account of how it was found: their first pass, like ours, was misdirected by DECODE's R4930
  ("images P3/P5 of R4930 are byte-identical to R4931's; R4930's other pages are Burghley's notes on the
  Norfolk/Ross letters, not a key" — matching our own NOTES.md's conclusion that R4930 is not a verified
  key). Their `profile.json` "solution" log records: "Swept DECODE records of the same volume: R4932 (f.
  278) is the contemporary decipherment of f. 277" (result: worked), then "Transcribed the f. 278 glosses
  and checked them against the f. 277 cipher; all five runs read, three gloss words doubtful" (result:
  worked). Outcome: `"class": "already solved"`, note: "About 70% read by crib attack before the
  contemporary decipherment (f. 278) was found; it agrees with every value recovered. DECODE date 1569
  corrected to 5 July 1570; R4930 is not a key. Catalogue entry 99 removed."
- Their crib for the pre-decipherment 70% pass was the **same** Boyd *CSP Scotland* iii no. 339 abstract our
  own NOTES.md already found and quoted (djvu lines 17866-17935 of `calendarstatepa02boydgoog`); Bourdeau's
  NOTES.md quotes Boyd's citation for the source letter as "Cott. Calig.: Original of the same; partly in
  cipher, **deciphered**" — the word "deciphered" in the 1903 calendar's own citation is the clue that
  pointed them to f.278, and confirms our target's positional match (rule-1 section, this session's read of
  our own NOTES.md) was correctly identified.
- Bourdeau's `randolph1570/transcription.txt` and `NOTES.md` give a full sign-by-sign token transcription of
  the five cipher runs and a full clear-text reading with the deciphered words in italics (both files copied
  in full into `siblings/bourdeau-randolph1570/` in this folder, per rule 8: MIT code / CC BY 4.0 text,
  credited, not claimed as this project's own work).
- Their cipher-system read: word-divided homophonic substitution, Latin letters/figures/invented marks,
  several signs per vowel, four name-codes (boxed sign = "the Scottish Queen's party in Scotland", θθ = "the
  S. Queene", ΠΠ = "the Q. of England", struck-through triple-bar = Earl of Morton).

**This is a search result to report to the orchestrator and to whoever holds NOTES.md, not a decode I
performed.** I did not view the BL images of f.278 myself this session (see next section) and have not
independently checked Bourdeau's sign values against our own transcription; that reconciliation is exactly
what rule 1 and the room need someone to do next, urgently, before further token-by-token cryptanalysis is
spent on a letter whose plaintext may already be established by a contemporary source. Per rule 10, no
novelty class is asserted here — that is the verifier's job, and Bourdeau's own finding, if correct, points
toward N0/N1 territory (decipherment of this very item already known, published by another named project on
2026-09-21/2026-09-23), which is the opposite of a "found" result for us; it does not by itself change our
target's status file, which this worker was not authorised to edit.

Full copies of the relevant Bourdeau files are in `siblings/bourdeau-randolph1570/` (`profile.json`,
`NOTES.md`, `transcription.txt`, and the `CATALOGUE.md` line and `docs/pages.json` entry, extracted
verbatim) for the next worker to check without re-cloning.

## What was blocked (steps 1-3 of the brief could not be executed)

Tested this session, all failed identically as an organisation egress-policy denial (HTTP CONNECT rejected
403 by the proxy, confirmed via `curl -sS http://127.0.0.1:43649/__agentproxy/status` `recentRelayFailures`,
and independently via the `WebFetch` tool returning `EGRESS_BLOCKED`), 23 September 2026, all around
15:23-15:26 UTC:

| Host | Needed for | Result |
|---|---|---|
| `archive.org` | djvu text of CSP Scotland vol. 3 (step 1, calendar index TSV) | `curl`: CONNECT 403; `WebFetch`: `EGRESS_BLOCKED` |
| `bl.digirati.io` | IIIF v3 manifest and image tiles for Caligula C II (steps 2-3, canvas TSV and candidate-folio images) | `curl`: CONNECT 403; `WebFetch`: `EGRESS_BLOCKED` |
| `web.archive.org` | fallback route for a Cloudflare-blocked site (playbook route 2) | `curl`: CONNECT 403 |
| `de-crypt.org` | DECODE record check (R4930/R4931/R4932) | `curl`: CONNECT 403 (also in proxy's own recent-failure log before this worker started) |
| `catalog.hathitrust.org`, `www.google.com`, `en.wikipedia.org` | general reachability check | `curl`: CONNECT 403 |
| `www.googleapis.com` (Google Books) | fallback print search | Reachable (HTTP 429, `rateLimitExceeded`, unauthenticated) — but `GOOGLE_BOOKS_KEY` is **unset** in this account's container (confirmed `test -n` empty), per the orchestrator's 2026-09-23 15:20 ROOM.md note that this account's environment carries none of the seven credentials. Not usable this session. |
| `github.com` | cloning `dbourdeau/cyphersolver` to grep it (Usage rule 2/rule 8) | Reachable, worked (this is how the finding above was made) |

Per `/root/.ccr/README.md`: "do not retry organization policy denials (403/407) — report them instead." This
was not retried beyond the one confirming test per host, and not worked around with `tools/browser_fetch.js`
(same proxy, same policy, would fail identically). **This means `siblings/csp-scotland-3-index.tsv` and
`siblings/caligula-c-ii-canvases.tsv`, both named in the brief, were not produced, and no candidate folio
images were fetched or viewed.** This is an environment-level blocker specific to this session/account (the
2026-09-21 workers in NOTES.md reached both `archive.org` and `bl.digirati.io` without incident from a
different environment), not a finding about the manuscript. Flagged in `ROOM.md` for the orchestrator; the
next worker on an environment that can reach these two hosts should re-run steps 1-3 of the brief as
written — the Bourdeau finding above narrows the priority target to **f.278 specifically** (and, as a
secondary check, f.276 and f.279-280, per the leaf-before/after instruction), rather than a blind sweep of
twelve leaves.

## Step 4: web search and local grep (completed)

- **WebSearch**, 2026-09-23: `"Randolph" "Sussex" 1570 cipher key Caligula` and `"Caligula C II" cipher key
  1570`. No page found describing a Randolph-Sussex key specifically. Both searches surfaced a different,
  unrelated cipher in the *same volume*: **BL Cotton MS Caligula C II f.74r, a 23-line cipher from Mary,
  Queen of Scots to the Duke of Norfolk, "the twentieth of this instant," 1570**, listed as undeciphered on
  Tomokiyo's Cryptiana page (one of the Norfolk-conspiracy series). This is a different correspondence and
  almost certainly a different cipher system (the well-known Mary-Norfolk nomenclator, not Randolph's
  invented signs) — logged for completeness, not proposed as a sibling of f.277's cipher.
- **`sources/cryptiana/web/elizabeth.htm`** (grep, read-only): no hit for "Caligula C II" at all in this
  file. Randolph hits are all the 1559-60 Randolph-Sadler-Croft cipher (Add MS 33591/33592, a different,
  eleven-years-earlier correspondence with Sadler and Croft, not Sussex) — matches what the 21 Sept 2026
  rule-1 search in `NOTES.md` already found. `unsolved.htm` and `henryiii.htm` (false-positive "f.277" from
  an unrelated French cipher) checked too, no hit.
- **`sources/cryptiana/web/mary.htm`** (grep, read-only, not in the brief but found via the WebSearch lead
  above and worth recording): confirms `BL Cotton MS, Caligula C II` also holds the **Mary-to-Norfolk
  cipher** correspondence, ff. c.66-75, four letters dated 31 Jan, 15 Jan, "20th" (undeciphered), and 18 Apr
  1570 — mostly already deciphered by Tomokiyo/Cryptiana, printed in Labanoff iii p.4, credited there. This
  confirms Caligula C II is a composite volume carrying at least two unrelated 1570 cipher correspondences
  (Mary-Norfolk near ff.66-75, Randolph-Sussex at f.277-278); it does not identify any further Randolph
  material or a general key/alphabet sheet for the volume. Not found: any cipher key sheet naming Randolph
  or Sussex, anywhere searched.

## Table (partial — the brief's per-leaf table could not be filled without image access)

| Folio | Calendar entry | What it is | Cipher present | Resembles f.277's symbols | Decipherment/key present |
|---|---|---|---|---|---|
| f.277r-v | Boyd CSP Scotland iii, entry under no. 339 (undated enclosure, filed near 7 July) | Randolph to Sussex, 5 or 9 July 1570 (date read two ways — see NOTES.md) — our target | Yes (5 runs, per Bourdeau's read) | n/a (this is the target) | No, on this leaf |
| **f.278** | Not separately calendared by Boyd (same enclosure) | **Half-leaf docket "5 July 1570": clerk's contemporary re-copy of every cipher word from f.277 with plaintext written above, per Bourdeau** | Yes (copies f.277's signs) | Reported identical (same letter) | **Yes — this is the decipherment**, per Bourdeau (DECODE R4932); not independently viewed by this worker |
| f.276, f.279-280 | Not identified | Unknown — image access blocked | Unknown | Unknown | Unknown |
| f.66-75 (approx.) | n/a | Mary Queen of Scots to Duke of Norfolk correspondence (Cryptiana `mary.htm`) | Yes | Different correspondence/system, not compared | Partially — most already deciphered/published by Tomokiyo (Labanoff iii p.4); f. "20th" 1570 letter flagged undeciphered by Cryptiana |
| f.74r | n/a (per WebSearch snippet, may be within the ff.66-75 Norfolk run above) | Mary to Norfolk?, 23-line cipher, "the twentieth of this instant" | Yes | Not compared | No, per Tomokiyo (undeciphered) |

## Conclusion

**Sibling with decipherment: found — but not by viewing the manuscript.** Bourdeau's `dbourdeau/cyphersolver`
repository (commit `2e9ec016...`, dated 2026-09-23) reports that BL Cotton MS Caligula C II f.278, the leaf
immediately following f.277, is a clerk's contemporary decipherment of the letter on f.277, and gives a full
sign-inventory and reading; it marks its own catalogue entry for this letter "already solved" / "removed" as
of 21 September 2026. **Key sheet: not found** — no general cipher-alphabet or key sheet for Randolph or
Sussex was found anywhere searched (web search, Cryptiana, Bourdeau's repository); the Mary-Norfolk
correspondence elsewhere in the same volume (ff. c.66-75) is a separate, already largely-published cipher,
not a key for Randolph's. **Exact folios worth fetching at native resolution next: f.278 first** (to
independently verify Bourdeau's reading against our own transcription of f.277, per rule 3/rule 10 — this is
now the single highest-priority fetch for this target), then f.276 and f.279-280 as a completeness check,
once a session with unblocked access to `bl.digirati.io` and `archive.org` is available. This was not
reachable this session; say so rather than reporting a negative on the leaves themselves.

## Files in this folder

- `SIBLINGS.md` — this file.
- `bourdeau-randolph1570/` — verbatim copies of `dbourdeau/cyphersolver`'s `randolph1570/profile.json`,
  `randolph1570/NOTES.md`, `randolph1570/transcription.txt`, plus the relevant `CATALOGUE.md` line and
  `docs/pages.json` entry, extracted for the next worker (credited to Bourdeau, MIT code / CC BY 4.0 text,
  not this project's work).
- No `csp-scotland-3-index.tsv`, `caligula-c-ii-canvases.tsv`, or `img/` — not produced, see "What was
  blocked" above.
- `manifest.json` — records what was and was not fetched this session, with reasons.
