# LANE DEFAULT-account-4-20261013-0935 jobs (account 4, lane orchestrator session_01Fof6DzsQ6Uah6Lw7sC1Lfb) -- 13 Oct 2026 09:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 09:35-19:35 UTC 13 Oct (80% line 17:35). Gate 0a: no SESSION-SWEEP-account-4 row.
Backlog read 09:4x UTC: VERIFY-BACKLOG.tsv regenerated 09:41 -- high rows Birago/ceppo (off limits) plus fr16104 ink 52 audit2 (held for
wave 2, after the f.191v view below, since that view may bear on prior plaintext); low rows audit2 on N0/N1. Then `next_steps.py --hot-only`
runnable rows minus the 13 Oct A1/A2 lanes' completed jobs and LANE BNF-FOCUS (account 2) holdings (fr3982, fr3985, fr3986, fr3987, fr3622,
fr3613). Probes 09:4x UTC: openapi.bnf.fr 200, keyed googleapis 503 (eckert-1864 / thurloe Verbael stay parked).
Intake gate 09:4x UTC (tools/intake_gate_check.py, exit 0 each): baluze167-davaux-1637 partial, fr4712-nevers-duchesse partial,
fr15575-syllabic-1592-95 partial, fr16104-vivonne-spain-1572 partial; colbert26-lathuillerie-1644 and na-suriname-map-1781 checked by
each worker as its first command (paste the output).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A4-0935 (account 4)"; the hosts bullet below replaces "No Gallica".
Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session` is not available to
you: say "cost not visible to this session" in the done line. Export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call.
**Hosts: openapi.bnf.fr** (IIIF Image API v3), exactly as `.claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md` "Hosts this wave"
(descriptive User-Agent; one request at a time, >= 3 s apart; per-job request limit stated below; `openapi.bnf.fr take` / `release` ROOM
lines around each batch -- other lanes (BNF-FOCUS) use the host too, so if anyone holds it with no release in the last 30 min, wait;
on 403/429/5xx or a challenge: one retry after 60 s, then stop the host). `tools/iiif_lines.py` and `tools/gallica_folio.py` take
`--iiif-host openapi` (IIIF-HOST, 13 Oct). Never gallica.bnf.fr (403). Images stay under the folder's `images/` (folder < 30 MB);
crops a later eye check needs are committed.

## Wave 1 (09:4x UTC 13 Oct)

### VIV-191V (Opus, cap 1.5, box 35 min, openapi.bnf.fr <= 5): fr16104-vivonne-spain-1572, view f.191v and its docket
NOTES.md Remaining gaps line "ink 52 La Ferriere f.191v lead (V-VIV52, AUDIT 5)": La Ferriere, Catherine IV intro p.cxx, quotes a
Saint-Gouard letter to the Queen (Anjou/England/Infante, early Sept 1572) citing fr.16104 f.191v. Find the canvas for f.191v (about c207;
confirm with `tools/gallica_folio.py --iiif-host openapi` or the cached manifest and by the folio number on the leaf), fetch an overview
(size `1600,`) of f.191v and the leaf carrying its docket/address. Answer, from the image only, in a NOTES.md section "## VIV-191V":
(a) is f.191v in cipher, clear, or a clear copy/decipherment; (b) its date, sender, addressee as written; (c) whether its text is the
same letter as ink 52 f.164r-v (compare the decoded f.164r-v phrases in the folder against what is legible -- name three phrases checked
and the result); (d) whether it is the passage La Ferriere quotes. No transcription beyond what (a)-(d) need; one vision call at most on
line crops if the overview is not legible. Update the Remaining gaps line (done, with the answer) and pass gaps_check. This answer feeds a
second verifier audit (wave 2): write it plainly, with the canvas number and the image file.

### V-BAL167 (Opus, verifier, cap 4, box 70 min, disk only): baluze167-davaux-1637, re-audit of the BAL-WL regrade and the f.228 depth
You are a verifier, not the solver (BAL-CROP/BAL-WL were other sessions). CLAUDE.md "Verifier brief (template)" steps 1, 3a and 4 only
(the N-class is not in question; no novelty search): read PREREG-BAL-SHAPE / PREREG of BAL-WL (commit 418e47a36), the balshape/ tiles,
the blind pass output and the 31 f.228 letter tokens regraded M -> S (H 56 S 31 M 39 I 27 U 1 of 154). Check: (1) the PREREG was pushed
before the read (git log order); (2) the positive control (0.917) and the same-key wrong-label negative (0.000) can each differ from the
target on the statistic scored (CLAUDE.md rule 3 "a control that cannot vary on the same axis"); (3) the 31 regrades are exactly the ones
the gate licenses, no more; (4) re-derive with the folder's decode script `--check` (rule 7); (5) depth per rule 4a for f.228 with
`tools/depth_check.py` -- D1 or D2, one true sentence if D2. Write the verdict as a dated section in AUDIT.md (and status.json depth fields
only if depth changes, via the documented fields); revert any regrade the gate does not license. One eye-look subagent call on tiles at most
(~1.5), only if (3) cannot be settled from the files.

### F4712-C39 (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 10): fr4712-nevers-duchesse, census canvases 39-45
NOTES.md Verdict "census of canvases 39-45 (ff.28v-35r) at 600 px via openapi.bnf.fr, ~$1.5" (F4712-71 lost these overviews to a filename
bug in its loop: name each file by canvas before the next fetch and check it exists). Ark from NOTES.md (F4712-CENSUS / F4712-71
sections). One overview per canvas at size `600,`; for each, one line in a table: canvas, folio as written, clear/cipher/blank/mixed, any
interlinear gloss, hand, date/addressee if legible. If a cipher leaf with an interlinear gloss in the f.10r/f.13r system appears, fetch at
most two native regions of it and stop there (name it as the next step; do not transcribe). Update Remaining gaps (siblings line) and the
Verdict; gaps_check.

### SYL54-LEG (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 4): fr15575-syllabic-1592-95, the no.54 mark legend
NOTES.md Remaining gaps "no.54 mark legend (f.97r right, 8 French lines) - not-attempted; next: one crop of canvas f188 f.97r right, 2 blind
passes + reconcile, ~$1.5". Ark btv1b525085665 (fr.3995). info.json for f188, one native region of the right-hand legend, line crops with
iiif_lines.py, two blind Sonnet passes (one call each, line crops only) + your reconciliation (3 units at ~0.7). Write
`key_no54_legend.tsv` (line, text, grade) and a NOTES.md section; say what the legend says each mark does, and whether that changes any
row of key_no54 (if it would, list the rows, do not edit the key -- a later job applies it with `decode_key.py --try`). Folder is at
29.75 MB: keep only the region file and crops you cite, shrink reference copies, and check `du -sh` before pushing.

### COL26-42 (Opus, cap 2.5, box 50 min, disk only): colbert26-lathuillerie-1644, pre-registered per-code test of 42 = s(ieur)
NOTES.md Remaining gaps "[ ] 42 = s(ieur) per-code test on canvas 20-21 + f.24 + canvas 29, pre-registered, rotation control, scripts only;
~$1.5; source: COL26-C29 post hoc lead". The lead is post hoc on canvas 29 (all three occurrences under "S."), so canvas 29 cannot be the
test set: PREREG-COL26-42.md pushed before scoring must name the held-out occurrences (canvas 20-21 interlinear units, f.24), the
statistic (gloss agreement of 42 with s/sieur/Sr vs the competing value si), the rotation/value-shuffle control and its gate, and the
power at that N (if the held-out N is too small for the control to reject, say non-test and stop before scoring). Scripts only, using the
existing interlinear/*.tsv and key files; no image work. Record in HYPOTHESES.md; key edit only if the gate passes, through
`decode_key.py --try 42=...` first. gaps_check.

### SUR-2039R (Opus, cap 2.5, box 50 min, disk only unless the crops are missing): na-suriname-map-1781, 2039 Remarque K/O/&/[J-rev] blind call
NOTES.md Verdict (SUR-GAPS list, 13 Oct update): "the 2039 Remarque K/O/&/[J-rev] blind call, ~$1.5". Follow the folder's own blind-call
pattern (SUR-2046, PREREG 6b9676d75): PREREG-SUR-2039R.md pushed first with a control built from already-keyed signs of the same sheet
whose answer the subagent does not see, and a gate the control must meet before any target call is accepted; one blind subagent call on
crops already on disk (or regenerated from the folder's regen script; NA host only if neither exists, <= 4 requests, `NA take/release`);
relabels enter as exceptions at the grade the gate licenses (M unless the control clears its bar with margin). decode `--check`; gaps_check.

## Wave 2 (10:0x UTC 13 Oct)
Wave 1 results (all ledgered): VIV-191V f.191v = clear decipherment of the 19 Sept 1572 letter, not ink 52; V-BAL167 upheld all 31 regrades,
f.228 D2, depth_pct 56.5; F4712-C39 no glossed sibling ff.28v-35r; SYL54-LEG legend 11 rows; COL26-42 non-test (0 held-out S.); SUR-2039R
non-test (controls 13/20 vs 14). Pricing lesson from wave 1 (3 of 6 over 1.4x): the Opus session floor is ~1.5 and a tile-sheet or
folder-shrink step is its own unit -- caps below are sized with that.

### V2-VIV52 (Opus, verifier, cap 5, box 80 min): fr16104-vivonne-spain-1572 ink 52 f.164r-v, second adversarial audit (Outreach gate 2)
VERIFY-BACKLOG.tsv row "Saint-Gouard to Catherine de Medicis, 5 Sept 1572 (BnF fr.16104 f.164r-v): French fragment" (priority high, audit2).
You are a session other than the solver (VIVPAN/VIV52-O) and the first verifier (V-VIV52, AUDIT 5); do not protect either. CLAUDE.md
"Verifier brief (template)" in full, steps 1-5, with these specifics: (a) the claim under audit is AUDIT.md section 5's safe sentence and its
N3 class; (b) VIV-191V (NOTES.md "## VIV-191V", 13 Oct) found f.191v is a clerk decipherment of a different letter (19 Sept 1572) -- verify
that reading of the leaf from its image on disk, since a clear copy of ink 52 anywhere in fr.16104 would make the item N1; check the
volume's other "dechiffre" leaves named in NOTES.md for a copy of the 5 Sept letter; (c) La Ferriere, Lettres de Catherine de Medicis IV
(and its intro, pp. cxx ff.) and the Saint-Gouard/Vivonne material in print (the French and Spanish editions the folder's
check-solved names; CODOIN / Simancas K. calendars if listed) by phrase search of the decoded fragments on IA full text (be-api) and the
keyed Google Books API (it answered 503 at 09:4x UTC: probe once, log unreachable if still 503); (d) open indexes (OpenAlex, Semantic
Scholar, CORE with keys per CLAUDE.md), Persee/HAL; (e) JSTOR-QUEUE.tsv rows in both families (i) and (ii) (CLAUDE.md verifier brief 2g)
appended for the owner's runner -- a queued row never blocks the class. Write AUDIT.md section 6 (N-class, key source, depth per 3a,
safe and unsafe sentence, every family searched/unreachable with counts), propagate to status.json via the documented fields and to any
SECOND-OPINIONS-QUEUE.tsv row already filed (SO-VIV52). IA (be-api, archive.org) take/release ROOM lines. Report the class and the
one-line postmortem.

### BAL167-SHRINK (Opus, cap 2.5, box 45 min, disk only): baluze167-davaux-1637 images/ from 31 MB to under 30 MB
CLAUDE.md Access playbook, last paragraph (the AX2-SHRINK pattern): `images_manifest_full.tsv` with a `cited_by` column (which NOTES/AUDIT/
HYPOTHESES line or script uses each file -- grep, do not guess), a `regen_images.sh` that re-derives every full page and recorded crop from
openapi.bnf.fr (use `--iiif-host openapi` URLs), a byte-identical regen test on ONE sample crop (<= 2 openapi.bnf.fr requests, take/release
lines), then delete uncited full pages / convert cited ones to JPEG at the same dimensions. Never delete a file cited by AUDIT.md or a PREREG,
or a balshape/ tile (V-BAL167 just audited them). `du -sh` before/after; decode `--check` and any balshape scorer still run after. Paste
`tools/file_shrink_guard.py` output in the done line.

### F4712-C47 (Opus, cap 2.5, box 45 min, openapi.bnf.fr <= 14): fr4712-nevers-duchesse, census canvases 47-58
Same method and table as F4712-C39 (NOTES.md "## F4712-C39", 13 Oct): one overview per canvas at `600,` (1600 for any cipher leaf, to look
for an interlinear gloss), name each file by canvas before the next fetch. Stop at the first glossed cipher leaf in the f.10r/f.13r system
(name it, two native regions at most). Update the siblings line and Verdict; gaps_check.

### SYL54-TRY (Opus, cap 3, box 60 min, openapi.bnf.fr <= 2): fr15575-syllabic-1592-95, legend mark pairs + --try of the 16 marked rows
NOTES.md Remaining gaps "no.54 legend mark pairs and the mark rule in decoding ... next: one native crop of the left-hand marks (canvas f188
x 5750-6100, y 2400-3400) eye-checked, then `decode_key.py --try` of the 9 circumflex and 7 plus-after nomenclator rows as code + modifier at
their f.228 occurrences, ~$1.5". Step 1: the crop (1 request; reuse SYL54-LEG's region file if it covers it) and one blind subagent call
settling the caret (s|l) and dotted-n (en|l) pairs -- the subagent does not see SYL54-LEG's two readings. Step 2: PREREG-SYL54-TRY.md
pushed first (statistic, the --try control, the gate), then `decode_key.py <t> --try` for each of the 16 rows at every occurrence; record
in HYPOTHESES.md; no key.tsv edit unless --try's own control passed for that value class (CLAUDE.md MQS-CROSSWORD line), and then M.
The 8/9 circumflex "-s" pattern is post hoc: it may motivate the PREREG, it cannot be its evidence. gaps_check.

### SUR-CTX (Opus, cap 3.5, box 70 min, disk only): na-suriname-map-1781, 2039 Remarque K/O/&/[J-rev] pre-registered context test
NOTES.md l.4168 and the Verdict: "pre-registered context test (value- and letter-shuffle controls, as SUR-ALIGN) is the instrument for
these classes, not a second tile call". Read SUR-ALIGN's PREREG and script (13 Oct) and reuse its machinery (tools/ first; no private copy
of a shared tool). PREREG-SUR-CTX.md pushed before scoring: per class (K x4, O x2, & x2, [J-rev] x2), the candidate values, the Dutch
vocabulary/corpus used, the statistic, both controls, the gate, and a power check at this N (10 tokens) -- if the controls cannot reject at
this N, write non-test and stop before scoring (COL26-42 did exactly this today). Relabels only where the gate licenses, as exceptions, M
unless the control clears with margin. decode `--check`; gaps_check.

## Wave 3 (10:3x UTC 13 Oct)
Wave 2 (all ledgered): V2-VIV52 N3 upheld, misplaced-decipherment residual named; BAL167-SHRINK 31 -> 29 MB; F4712-C47 empty census
(fr4712 census paused: two empty runs, canvases 59-70 left as a named step, not run here); SYL54-TRY and SUR-CTX non-tests at their own
controls (na-suriname 2039 Remarque: two instruments failed their controls today -- not re-briefed without new material).

### VIV-DECH (Opus, cap 2.5, box 45 min, openapi.bnf.fr <= 10): fr16104 ink 52 misplaced-decipherment residual
NOTES.md Remaining gaps line "ink 52 misplaced-decipherment residual (V2-VIV52, AUDIT 6)": view the head region (first 6-8 lines, at
`1600,` or a native region) of each post-19 Sept "dechiffre" leaf in fr.16104 -- inks 56, 60, 62 and the Oct-Dec 1572 pairs, canvases from
the folder's ink/leaf table -- and compare each opening with ink 52 f.164r's decoded opening and its distinctive decoded phrases (name the
three phrases you use). One line per leaf: canvas, folio, ink, head as written (date/addressee), matches ink 52 yes/no and why. A
decipherment of the 5 Sept letter anywhere would be prior plaintext: if found, stop, write it plainly in NOTES.md and ROOM.md (flag line),
and do not touch AUDIT.md (a verifier's file). Update the gap line and gaps_check. Report what was found and where it was not found.

### BAL167-GHV (Opus, cap 4, box 70 min, openapi.bnf.fr <= 12): baluze167-davaux-1637 g+/hook/v image check
NOTES.md Remaining gaps "170 f.228r-v g+/hook/v classes (HYPOTHESES.md) - not-attempted; next: an image check of the g+, hook and v forms
against glossed Baluze 170 leaves that carry those shapes (survey.tsv glossed leaves ff.63-322, crops via openapi.bnf.fr), ~$3", and the
Verdict's V-BAL167 lesson: the negative arm carries within-key look-alike wrong labels. Method as BAL-WL (PREREG pushed before any read;
gloss-fixed exemplar tiles from 2-3 glossed leaves as positive control; within-key look-alike wrong-label negative whose score can differ
from the target's; one blind Sonnet tile pass, a second only if the first is under gate; regrade only what the gate licenses; decode
`--check`). Units: survey.tsv pick + <= 3 region fetches + crops (~1), 1-2 vision calls + 1 reconciliation at ~0.8 each. Folder is at
29.1 MB: add only cited tiles, add them to images_manifest_full.tsv and regen_images.sh (BAL167-SHRINK), `du -sh` before pushing.

## Wave 4 (10:5x UTC 13 Oct; last wave)
Wave 3 (ledgered): VIV-DECH Sept dechiffre heads (inks 56/60/62) are not ink 52, Oct-Dec pairs bracketed (c288, c296) not viewed;
BAL167-GHV hook 7 + v 1 M -> S after read 1 FAIL / read 2 PASS (PREREG c60720e55), g+ stays M, re-audit owed.

### V-GHV (Opus, verifier, cap 3, box 50 min, disk only): baluze167-davaux-1637, re-audit of BAL167-GHV's 8 regrades
As V-BAL167 (wave 1) for BAL167-GHV (NOTES.md "## BAL167-GHV", PREREG c60720e55, commit ccdff89ef). Check: (1) PREREG pushed before
either read (git log order) and it allowed a second read when the first was under gate, in those words -- a second read not provided for
in the PREREG voids the regrade; (2) the within-key look-alike negative can differ from the target on the statistic; (3) what read 1's
FAIL means for read 2's PASS (is the pass a retry of the same instrument that the first read failed? say so plainly); (4) the 8 regrades
are exactly what the gate licenses; (5) decode `--check`; depth per rule 4a with `tools/depth_check.py`. Write AUDIT.md section "AUDIT 5"
(next number); revert any regrade not licensed; status.json depth fields only if depth changes.

### VIV-DECH2 (Opus, cap 2.5, box 40 min, openapi.bnf.fr <= 8): fr16104 Oct-Dec dechiffre heads
NOTES.md gap line as updated by VIV-DECH (commits 1441e930a, 69b7d6521): the Oct-Dec 1572 dechiffre/cipher pairs between c219 and c296,
bracketed but unviewed. Same method and table as VIV-DECH: head region of each dechiffre leaf, compared with ink 52's decoded opening and
three named phrases. Stop at the first leaf that matches (flag line, NOTES.md, no AUDIT.md edit). Update the gap line; gaps_check.
