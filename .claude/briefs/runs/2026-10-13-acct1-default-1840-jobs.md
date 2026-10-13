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
