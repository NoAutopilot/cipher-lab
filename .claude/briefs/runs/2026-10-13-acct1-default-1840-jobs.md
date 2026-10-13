# LANE DEFAULT-account-1-20261013-1840 jobs (account 1, lane orchestrator session_01TYyr52anK6nZcz4LqA98TL) -- 13 Oct 2026 18:5x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 18:40 UTC 13 Oct - 04:40 UTC 14 Oct. Gate 0a: SESSION-SWEEP-account-1 stale-claimed
since 5 Oct, proceeded as prior incarnations. VERIFY-BACKLOG regenerated 18:45: high rows Birago/ceppo (off limits), low rows audit2 on
N0/N1, counted rows priority none. Backlog: `next_steps.py --hot-only` runnable rows minus the 13 Oct A1-0640/A2-0710/A4-0935 lanes' done
steps and LANE BNF-FOCUS (account 2) holdings (fr3982, fr3985-3987, fr3622, fr3613). Probes 18:4x UTC: keyed googleapis 503 (eckert-1864,
thurloe Verbael stay parked). Intake gate 18:5x UTC (tools/intake_gate_check.py, exit 0 each): fr16104-vivonne-spain-1572,
fr4712-nevers-duchesse, na-suriname-map-1781, la-garde-1577.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A1-1840 (account 1)"; the hosts bullet below replaces "No Gallica" and that
file's "Hosts this wave". Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session`
is not available to you: say "cost not visible to this session" in the done line. Export `CIPHERLAB_ACCOUNT=account-1` before any
tools/room.py call.
**Hosts: openapi.bnf.fr** (IIIF Image API v3), exactly as `.claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md` "Hosts this wave"
(descriptive User-Agent; one request at a time, >= 3 s apart; per-job limit below; `openapi.bnf.fr take` / `release` ROOM lines around each
batch -- if anyone holds it with no release in the last 30 min, wait; on 403/429/5xx or a challenge: one retry after 60 s, then stop the
host). `tools/iiif_lines.py` and `tools/gallica_folio.py` take `--iiif-host openapi`. Never gallica.bnf.fr (403). **resources.huygens.knaw.nl**
("huygens" take/release, >= 2 s, descriptive UA). Images stay under the folder's `images/` (folder < 30 MB); crops a later eye check needs
are committed.

## Wave 1 (18:5x UTC 13 Oct)

### VIV-HEADS (Opus, cap 2, box 45 min, openapi.bnf.fr <= 8): fr16104-vivonne-spain-1572, heads of inks 78, 97, 101
NOTES.md Verdict / gap line "ink 52 misplaced-decipherment residual": VIV-DECH and VIV-DECH2 (13 Oct) viewed the dechiffre heads of inks
56, 60, 62, 83, 89, 91 and the ink 78 close; the heads of 78, 97 and 101 are unviewed. Same method and table as VIV-DECH (NOTES.md
"## VIV-DECH"): head region (first 6-8 lines at `1600,` or one native region) of each, canvas from the folder's ink/leaf table, compared
with ink 52 f.164r's decoded opening and three named distinctive decoded phrases. One line per leaf: canvas, folio, ink, head as written,
matches ink 52 yes/no and why. A decipherment of the 5 Sept letter would be prior plaintext: if found, stop, write it plainly in NOTES.md
and a ROOM flag line, and do not touch AUDIT.md. Update the gap line (the residual is closed when these three are viewed) and gaps_check.
Do not start ff.165r-168v (a campaign decision). Report what was found and where it was not found.

### F4712-C59 (Opus, cap 2, box 45 min, openapi.bnf.fr <= 14): fr4712-nevers-duchesse, census canvases 59-70
Finishes the sibling census (F4712-C39, F4712-C47, 13 Oct: ff.28v-48r, no glossed sibling of f.10r). Same method and table as F4712-C39
(NOTES.md "## F4712-C39"): one overview per canvas at `600,` (1600 for any cipher leaf, to look for an interlinear gloss), name each file by
canvas before the next fetch and check it exists. Stop at the first glossed cipher leaf in the f.10r/f.13r system (name it, two native
regions at most, no transcription). If canvas 70 is not the volume's end, say how many canvases remain and do not continue. Update the
siblings line and the Verdict (if the census is complete and empty, say so and mark the siblings rung accordingly); gaps_check.

### SUR-LEGK (Opus, cap 2.5, box 60 min, disk only): na-suriname-map-1781, 2039 legend k positions 1-2 and 5, two-pass blind re-read
NOTES.md gap line for 4.VEL 2039 "legend k pos 1-2 and 5 (R15-SURV's look was not fully blind; its two-pass re-read was not run) -
not-attempted". Distinct from the Remarque K/O/&/[J-rev] tokens (two instruments failed their controls on 13 Oct; do not touch them).
Crop step pasted (`tools/iiif_lines.py --image <the 2039 native image on disk> --out ...` or the folder's existing legend crops), then two
blind Sonnet subagent passes on the legend-k line crop only (each told the sign inventory/sheet, not the current reading or R15-SURV's
call), plus your reconciliation (3 units at ~0.7). Settle a position only where both passes agree with each other; disagreement stays M
(or U). Apply through the folder's decode/--check scripts (rule 7), grade per rule 4, update the gap line and Verdict; gaps_check.
Report what was found and where it was not found.

### LAG-SIB (Sonnet, cap 2.5, box 60 min, huygens <= 40, archive.org <= 20): la-garde-1577, same-system sibling sweep for pooling
NOTES.md Verdict (LAG-HIRES, 13 Oct): "cheapest next: the open siblings step (a same-system pooling sweep for more ciphertext)". Read the
ZX2-LAG2 and LAG-* sections first and list every route already searched; search only routes NOT in that list, e.g. Huygens WVO
(`opmerkingen` = cijfer / chiffre / gecijferd, sender or recipient La Garde and his named correspondents, 1575-1579), the Huygens
retroboeken editions that cover the period, Groen van Prinsterer's Archives ser. 1 vols 5-6 and Gachard's Correspondance de Guillaume le
Taciturne on archive.org full text (be-api fts / djvu grep for "chiffre" near the correspondent's names), DECODE login-free listing. For
each candidate: holder, shelfmark/letter number, date, sender -> recipient, whether cipher is stated, whether an image is online, and
whether it is the same system (same sign stock/numbers as 6179/6467) when an image is viewable (overview only; no transcription). Write a
`## LAG-SIB` section with a candidates table and the routes searched/unreachable, update the siblings rung and Verdict; gaps_check. No
cryptanalysis. Report request counts per host.

Wave 1 (all ledgered + archived, 19:0x UTC): VIV-HEADS 2.61 D (inks 78, 97 not ink 52; 101 not reached), F4712-C59 2.38 N (c59-70 empty;
71-142 remain, not pursued: three empty runs), SUR-LEGK 2.92 D (legend k pos 1-2/5 settled M; pos 6 split 7|r), LAG-SIB 1.80 N (0 siblings;
Marnix Aug 1577 alphabet lead, Groen VI p.129). Lesson: Opus floor puts $2 jobs at 1.2-1.3x; size small Opus jobs at 2.5.

## Wave 2 (19:1x UTC 13 Oct)

### VIV-101 (Opus, cap 2, box 30 min, openapi.bnf.fr <= 4): fr16104-vivonne-spain-1572, head of ink 101
VIV-HEADS (NOTES.md "## VIV-HEADS", commit 6e1330003) left ink 101's dechiffre head unviewed: ink 100 cipher still on f.299r c321, ink 101
at c322-c324. Same method and table as VIV-HEADS: the head region of ink 101's dechiffre leaf at `1600,`, compared with ink 52 f.164r's
decoded opening and the same three named phrases VIV-HEADS used. One table line. If it matches ink 52: stop, NOTES.md + ROOM flag, no
AUDIT.md edit. Otherwise close the "misplaced-decipherment residual" gap line (all post-19 Sept dechiffre heads viewed) and gaps_check.

### SUR-POS6 (Opus, cap 2, box 40 min, disk only): na-suriname-map-1781, 2039 legend k position 6 (7 vs r)
SUR-LEGK (NOTES.md "## SUR-LEGK", commit e20173ec5): both blind passes read legend k pos 6 as 7, the committed value is r (held M). Using
SUR-LEGK's crops (no new crop unless needed, then pasted iiif_lines.py command): one blind Sonnet call comparing pos 6 against the sheet's
7 and r tiles plus two known-answer controls (a settled 7 and a settled r elsewhere on 2039, unlabelled, order shuffled) -- the controls
must be read right for the target call to count. Apply only if the controls pass and the call is clear; otherwise stays M with the split
recorded. --check, grade counts, gap line and Verdict; gaps_check. Do not touch the Remarque K/O/&/[J-rev] tokens or 2046.

### COL26-WP (Opus, cap 5, box 80 min, disk first, openapi.bnf.fr <= 6): colbert26-lathuillerie-1644, word-level pairing c20-21 for 42, 11, 6
NOTES.md Verdict "cheapest next: the word-level pairing on canvas 20-21 for 42, 11, 6, ~$6 (D07-COL26K)". Rule 3 third-attempt check FIRST
(CLAUDE.md rule 3, last paragraphs): c20-21 has had A4-COLALN (interlinear_align, per-unit gate FAIL) and D07-COL26K (positional known-answer:
42 underpowered, 11 FAIL); COL26-42 (13 Oct) found 42 = s(ieur) a non-test on held-out units. Write in your section whether a word-level
pairing is a genuinely different instrument from both (what statistic, what unit) and whether new material enters; if it is the same
instrument with a changed knob, log "untested-by-this-tool" and stop. If different: PREREG-COL26-WP.md pushed first (statistic, a control
that can differ from the target on that statistic, a power check on known-answer codes 83 de / 31 que with the held-out code masked, gate);
run the power check BEFORE scoring 42/11/6 and stop at a non-test. No key.tsv edit unless the gate passes, and then via decode_key.py --try
(M unless --try's own control passed). Update gap line, Verdict; gaps_check. Report what was found and where it was not found.

### LAG-MARNIX (Sonnet, cap 1.5, box 45 min, huygens <= 20, archive.org <= 15): la-garde-1577, locate Marnix's Aug 1577 cipher alphabet
LAG-SIB (NOTES.md "## LAG-SIB") found Groen van Prinsterer, Archives ser.1 vol. VI p.129 (letter DCCXLII) naming Marnix's cipher alphabet of
August 1577. Read that page and its footnotes in the archive.org full text: who sent the alphabet to whom, whether Groen saw it and where
(KHA/A?? shelfmark), whether any period cipher table of Marnix/La Garde/William of Orange 1576-78 is catalogued (Huygens WVO detail pages for
the letters around it; the KHA inventory if a public finding aid answers). Also LAG-SIB's two untried routes: a Huygens retroboeken phrase
search for the correspondent names with "chiffre"/"cijfer", and a grep of the two solver repositories for La Garde/Marnix (clone only to
grep). Output: a `## LAG-MARNIX` section (holder, shelfmark, digitised y/n, image URL if any, whether it can be the 6179/6467 system and why),
siblings/known-keys rungs and Verdict updated; gaps_check. No cryptanalysis; if an image of the alphabet is online, fetch it once and stop
(name the key-test as the next step).
