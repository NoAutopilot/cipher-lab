# LANE DEFAULT-account-2-20261014-0911 jobs (account 2, lane orchestrator session_019GFKerGc4HE6YqTNNSX8vk) -- 14 Oct 2026 09:2x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 09:11-19:11 UTC 14 Oct. Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct,
proceeded as prior incarnations. VERIFY-BACKLOG regenerated 09:16: high rows Birago/ceppo (off limits), rest audit2 on N0/N1. Backlog:
`next_steps.py --hot-only` runnable rows minus the 13-14 Oct lanes' done steps, plus the clair1161 AUDIT re-class the A1-0640 lane owed a
verifier. Probe 09:2x UTC: keyed googleapis (country=US) 200 again -- eckert-1864 and thurloe Verbael unparked.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A2-0911-14 (account 2)"; the hosts named in your job replace that file's
hosts lines. Export `CIPHERLAB_ACCOUNT=ytbiz` before any tools/room.py call. `get_session` is not available to you: say "cost not visible
to this session" in the done line. Never the words solved, cracked, novel, first, new for anything this project did. Do not touch
status.json, NEAR.md, STATUS.md or the board (the lane orchestrator does). Birago, Armstrong and Debosnys folders are off limits.
Report what was found and where it was not found; do not classify novelty (solver jobs).

## Wave 1 (09:2x UTC 14 Oct)

### VER-C1161 (Opus, cap 4, box 75 min): verifier, clair1161-avis-flandre-1688 AUDIT re-class after the Lasry prior-work notice
CLAUDE.md "Verifier brief (template)" in full. Claim under audit: AUDIT.md's current N-class/depth for the items of ff.162r-164v (N3 per
the A1-0640 handoff) against the prior-work notice of 14 Oct 2026 (AUDIT.md line ~347, LQ-C1161; George Lasry's "BnF cipher research",
published by D. Bourdeau, cyphersolver `targets/clair1161`, commit dde5b0ea; snapshot at sources/cyphersolver/2026-10-14-lasry/clair1161/).
Per item (face): is his transcription/decipherment prior work for our reading (N0/N1/N2 per rule 10), at what extent (his "in part"), and
does any face stay N3 (not covered by him)? Depth (rule 4a) per item; record `key` (ours/period/published) per rule 10. Append a dated
section; do not rewrite earlier sections; correct over-claims in NOTES/AUDIT wording. The C1161-LKEY/C1161-V2 key conflicts (16 agree /
10 disagree) are a data conflict (rule 4) -- record, do not settle. SECOND-OPINIONS-QUEUE row only if any item stays N3+ and has none.
Hosts: github.com (one shallow sparse clone of dbourdeau/cyphersolver if the snapshot lacks a file), archive.org be-api/advancedsearch,
Google Books API (country=US, key), OpenAlex/S2 with keys, 1.5 s apart. You are not any solver session of this folder.

### BAL22-SHAPE (Opus, cap 3, box 60 min, disk only): baluze167-davaux-1637, 169 f.22r letter-sign blind shape check + rule-7 re-derivation
The folder's gap line "169 f.22r letter signs and name ... next: a blind shape check of the six letter signs against Tomokiyo's table and
glossed exemplars (BAL-WL method) plus a fresh rule-7 re-derivation, ~$2.5". Units: two blind shape passes (one call each on crops of the six
signs + exemplar strip, ~0.8 each), reconciliation (~0.5), control as BAL-WL (same-key wrong-label negative) and re-derivation with
`tools/decode_key.py ciphers/baluze167-davaux-1637 --check` (~0.5). PREREG before scoring. M -> S only where both passes agree and the
control passes; f and a context fits stay I unless the shape check licenses them. Update the f.22r grades in NOTES (rule 4 counts), the gap
line, Verdict, gaps_check. AUDIT.md: append one line pointing to your section; no class change (verifier's job).

### BAL168-SWEEP (Opus, cap 5, box 80 min, openapi.bnf.fr <= 300 at >= 3 s): baluze167-davaux-1637, Baluze 168 canvases 1-250 at 300 px
Exactly BAL167-SWEEP's method (its NOTES section; contact sheets at 300 px, priced ~0.35 per sheet + fetch loop), <= 15 looks at 1000 px;
controls = the listed 168 cipher canvases in range (f.110r unlisted per N9-BAL; f.246-247 is beyond 250 -- note the canvas if reached).
Take/release ROOM lines for "openapi.bnf.fr"; one request at a time >= 3 s; one retry after 60 s on 403/429/5xx then stop; never
gallica.bnf.fr. images/ stays under 30 MB (contact sheets in scratch; commit only the looks a later eye check needs, or a regen script).
New survey.tsv rows only; volumes gap line; Verdict; gaps_check. No transcription. If 168 has fewer than 250 canvases, finish it.
Coordinate with BAL22-SHAPE on NOTES.md (same folder): rebase before writing, keep both sections.

### EST-REG (Opus, cap 3, box 60 min): clair571-estrades-1645, register 9431 + diff vs the Brasset keys
The folder's two not-attempted gaps: (1) "Register 9431 in KEY-OFFICES/KEY-DESIGN - next: loader option or a key*.tsv copy, ~$1": prefer a
loader option on tools/key_design.py (with an offline test in tools/tests/) over a private copy (CLAUDE.md Usage 8); add the 9431 rows to
KEY-OFFICES.tsv / KEY-DESIGN.tsv. (2) "Diff 9431 against the Clair 417 (1648) and Clair 421 (1649) Brasset keys - next: read the published
Clair 421 table (Tomokiyo/Lasry) and diff by code and series, ~$1.5": find the published table on disk first (sources/cryptiana,
sources/cyphersolver/2026-10-14-lasry/, KEYHUNT-2026-10-07.tsv), then cryptiana.web.fc2.com (<= 10 requests) or one shallow sparse clone of
dbourdeau/cyphersolver; diff by code and series; report shared-design evidence (counts), never a claim the letter reads. Gaps/Escalation
(known-keys rung), Verdict, gaps_check.

### GB-2 (Opus, cap 2, box 45 min): keyed googleapis pass for two parked steps, eckert-1864 then thurloe-printed
Host: www.googleapis.com/books/v1 only, `&country=US&key=$GOOGLE_BOOKS_KEY` (never print it), one call at a time >= 1.5 s, control first in
each folder; on 503/429, one retry after 60 s, then log unreachable and stop that folder. (a) eckert-1864: the gap line "Grant Papers vol.
13 (2-20 Feb 1865) for E590 E591 E592, and a looser E589 query (`Monohansett Monroe`)" -- re-run the same sliced list as ECK-GP13B/C
(`fortmonroe/eck_gp13c_gb.out` and its script) once the control answers 200; record hits/non-hits per entry with the volume id; no
novelty language. (b) thurloe-printed: "the 1725 Verbael ... next: Google Books API (country=US) 'Verbael gehouden door de Heeren'"; if a
full-view or snippet volume is found, check whether it holds Beverning's 27 June / 22 Aug 1653 letters and No. 37 pp.252-253 (snippet
search on distinctive words); record the volume id and what it does/does not show. Gaps/Escalation/Verdict and gaps_check in both folders.

### SALV-TRY20 (Opus, cap 3, box 60 min, disk only): fr2933-salviati-1525, --try the 20 pass-disagreement types + eps^7 under Lasry's key
The folder's gap line: "testing the 20 pass-disagreement types (each pass's cell from lkey/pass*_part*.tsv) and eps^7 = ti/tu at every
occurrence with `tools/decode_key.py --try` and the same permuted-key control ... next: --try both candidate cells per disagreement type,
re-score with lkey/score_lasry.py --set, ~$2". PREREG first (the acceptance rule per type and the whole-key re-score gate as SALV-TRY used).
Read SALV-LKEY and SALV-TRY sections first. Accepted values M unless --try's control passed for that value class; no key.tsv edit
(key_lasry.tsv only, with a dated note). Report the word-hit and 4-gram numbers before/after vs the same 300 permuted keys. This is the
last pass at this instrument (rule 3's third-attempt clause applies to any further whole-key re-score): say so in the gap line. NEAR
numbers in the done line.
