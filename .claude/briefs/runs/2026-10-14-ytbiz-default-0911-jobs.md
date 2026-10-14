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

Wave 1 sessions (spawned 09:18-09:19 UTC): VER-C1161 session_016GoR3EqtEdxzfmHoRRt2c7; BAL22-SHAPE session_019SaTMkgRiMG8k7SSuRE41q;
BAL168-SWEEP session_011uwbJK2BBjfS7U3PXzkdfe; EST-REG session_01MRywkZ3DWozgcPvosR6STm; GB-2 session_011LgUEf4G3FrFsLQrofwrYE;
SALV-TRY20 session_019bAX6RALYPv2Z6t4PvSQio.

## Wave 2 (09:5x UTC 14 Oct)
Wave 1 results: VER-C1161 AUDIT 3 (clair1161 N3 -> N0, status.json/NEAR updated by the lane); BAL22-SHAPE (f.22r H 4 S 5 I 2 M 13);
EST-REG (9431 registered; vs Clair 421 0 same-code); GB-2 (Verbael located in full view, unread after 503; eckert control 503);
SALV-TRY20 (0 of 31 accepted, --try route retired). Many `parallel` actions in next_steps are stale (already run): check 1 first.

### PW-FIX (Opus, cap 3, box 60 min, disk only): tools/prior_work.py check 3 false CLEAR on a solver snapshot that names the shelfmark
VER-C1161's ROOM flag (09:29 UTC): check 3-solver printed CLEAR for clair1161 (BnF Clairambault 1161 ff.162r-164v) although
sources/cyphersolver/2026-10-14-lasry/clair1161/ names the shelfmark. Reproduce first (paste the command and the CLEAR row), find why the
snapshot is not matched (cache_paths in tools/data/prior_portals.tsv, the term list, the per-target subfolder layout of the 2026-10-14-lasry
snapshot), fix it in the tool, and add offline tests in tools/tests/test_prior_work.py: must-catch = this case (a dated Lasry snapshot
folder naming the shelfmark -> LEAD or CONTEXT, never CLEAR); must-not-block = a same-volume different-folio snapshot (e.g. a Lasry folder
for another item of the same volume) stays at most CONTEXT. Update the docstring's must-catch/must-not-block kinds (CLAUDE.md 8a). Run the
full tools/tests/test_prior_work.py and paste the count. Then re-run prior_work.py on the other Lasry same-volume folders listed in
sources/cyphersolver/2026-10-14-lasry/ours_same_volume.tsv (read-only, no --record) and list any CLEAR that now flips, in the done line.
Not a solver job; SYSTEM.md only if a new file is added.

### COL26-C33 (Opus, cap 5, box 90 min): colbert26-lathuillerie-1644, word-grain pairing of c33 for 20 = i (D2-COL26's named next)
The folder's escalation line "word-grain pairing of c33 (9 lines) to firm 20 = i at word grain (line grain missed the gate narrowly);
~$4.5; source: D2-COL26". Read D2-COL26, COL26-WP and COL26-11B first: the word-pairing instrument failed its instrument check twice for
11 = le on canvases 20-21; run the same instrument check on c33 FIRST (PREREG pushed before), and if it fails, stop there and log
"non-test at this N" -- a third failure of the same instrument check retires word pairing for this folder (rule 3 third-attempt clause).
Units: crop step (tools/iiif_lines.py, pasted), two blind reads of the c33 gloss/cipher words (~1.2 each), reconciliation (~0.8), pairing +
control (~0.8). Gallica IIIF only if c33 crops are not on disk (<= 20 requests, >= 2 s, browser UA). No key.tsv edit; --try for 20 = i.

### SALV-MAP3 (Opus, cap 4.5, box 90 min, disk only): fr2933-salviati-1525, third blind mapping pass of the 20 disagreement types
The folder's gap line: "a third blind mapping pass of the 20 disagreement types (and nt^, eps^7) against his key sheet, image-only ...
next: one Opus subagent call per atlas part with the two earlier passes withheld, then decode and score_lasry.py, ~$4". Image-only, the
earlier passes withheld from the subagent; per-type 2-of-3 majority with the earlier passes; PREREG first (what counts as a settled type,
the score gate as SALV-LKEY: word hits and 4-gram vs the same 300 permuted keys). key_lasry.tsv updated only for 2-of-3 types, dated note;
our key.tsv untouched. NEAR numbers before/after in the done line. If the gate still misses, the published-key step is [retired] with the
instrument named (rule 3) -- say so in the gap line and Escalation.

### F3975-PC (Sonnet, cap 1, box 30 min): fr3975-vieuville-1587, print_check on the letter's clear phrases
The folder's "While waiting" action: `tools/print_check.py ciphers/fr3975-vieuville-1587` with the readable clear phrases ("eschevins et
maire de ville", "St Aignen", 30 Sept 1587) in phrases.txt (create or extend it; keep existing lines), against IA full text, Google Books
(country=US, key; on 503 one retry after 60 s, then log unreachable) and OpenAlex (key). Paste the summary in a dated NOTES section;
'no hits' is a search result, never a novelty verdict. Status stays `blocked`.

Wave 2 sessions (spawned 09:40 UTC): PW-FIX session_01Hf212v6xmX38n1YDCggzeK; COL26-C33 session_014jfMUt7CUyscq8Me7FDKP5;
SALV-MAP3 session_01TbESZH67oRC4ekVXV6WsfV; F3975-PC (Sonnet) session_01G7dWAzhhEQnu8Lg4zKxxvi.

## Wave 3 (10:0x UTC 14 Oct) -- at most two in flight (orchestrator check-in 98)
Wave 2 results: PW-FIX (prior_work.py fixed, 137 PASS); COL26-C33 (instrument CLEARS, 20 = i FAIL-LOWPOWER); SALV-MAP3 (4-gram PREREG gate
PASS, 0/300); F3975-PC (stale step, stopped at check 1); BAL168-SWEEP (168 c1-250, no unlisted letter beyond f.110r/c237).

### SALV-EYE (Opus, cap 3.5, box 75 min, disk only): fr2933-salviati-1525, eye check of the SALV-MAP3 settled and unsettled types
SALV-MAP3's named next ("eye check of settled/unsettled types ~3"; ablation: S^=m and Lx^=u lower the score). Image-only, crops from disk
(glyphs/atlas + Lasry sheet), one subagent call per type group, blind to the three earlier passes' values; record agree/disagree per type
against the 2-of-3 value; no key_lasry edit beyond marking a type `eye-confirmed` or `eye-contested` in a dated column; re-score only if a
type flips (same 300 permuted keys, PREREG gate). Then a fresh `--check` re-derivation of the reading under key_lasry. NEAR numbers in the
done line; no novelty words; the verifier comes after (lane's call).

### BAL171-SWEEP (Opus, cap 4, box 80 min, openapi.bnf.fr <= 300 at >= 3 s): baluze167-davaux-1637, Baluze 171 canvases 1-250
Exactly BAL168-SWEEP's method (300 px contact sheets, <= 15 looks at 1000 px, controls = listed 171 cipher canvases in range); then, in
the same session if under 80% of cap and box, the 167 c275/c283 image check (two looks at 1000 px; BAL167-FIN's named unglossed runs:
glossed, bare, or not cipher). Take/release ROOM lines for openapi.bnf.fr (account 4's lane also uses it: wait for its release). New
survey.tsv rows only; volumes gap line; Verdict; gaps_check. No transcription.
