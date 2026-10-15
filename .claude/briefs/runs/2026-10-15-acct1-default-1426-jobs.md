# LANE DEFAULT-account-1-20261015-1426 jobs (account 1, lane orchestrator session_01WUxMjbN8ZBwyMbRJvwrjsQ) -- 15 Oct 2026 14:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 14:27 UTC 15 Oct - 00:27 UTC 16 Oct. Gate 0a: SESSION-SWEEP-account-1 stale-claimed
since 5 Oct 22:40, proceeded (as every account-1 lane since 14 Oct).
Backlog: VERIFY-BACKLOG has no actionable row in scope (Birago/ceppo `counted` high rows off limits; the rest `none` or audit2 on N0/N1 items
that need Google Books, 503 all day). Step b: `next_steps.py --hot-only` runnable rows, each checked against the folder's latest NOTES
section; then cold runnable rows from plain `next_steps.py` (hot list spent after exclusions; said in the ROOM claim).
Excluded: live LANE DEFAULT-A2-1410-15 holdings (decode-1162/1168, fr3151, bne20211, fr16045, fr16144, pro3055, harley-287, august-van-saksen,
na-suriname, willem-van-hessen), VIV-KEYSTONE (fr16104, fr16106, lodewijk, oldenbarnevelt, mercy, thurloe), BNF-FOCUS (fr3982, fr3985-3990,
fr3985-gievre), Birago family / ceppo / nevers-birago, Armstrong, Debosnys, cipher-lab-private. LANE DEFAULT-A4-1236-15 closed 14:24 UTC, so
its folders (fr5761, fr4735, baluze167, clair1161) are free; each worker still checks the last 60 ROOM lines for its folder.
Intake gate 14:4x UTC (tools/intake_gate_check.py, each PASS): fr5761-election-1519, colbert26-lathuillerie-1644,
fr4735-monluc-lansac-poland-1573, baluze167-davaux-1637, na-janssens-java-1811. fr3198-labbe-1577 is `blocked` (catalogue search only).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-15-acct1-default-0740-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A1-1426-15 (account 1)"; export `CIPHERLAB_ACCOUNT=account-1` before any tools/room.py call;
- a worker pays ~1-2 of start-up before its first unit: stop before a unit that would cross 80% of cap or box;
- no www.googleapis.com; no gallica.bnf.fr (openapi.bnf.fr only, where a job names it), >= 3 s apart, take/release ROOM lines;
- each job edits only its own folder (plus a tools/ option and its offline test where the job says so); never key.tsv beyond what a passed,
  pre-registered gate licenses; never status.json, STATUS.md, NEAR.md or the owner's published pages;
- never the words solved, cracked, novel, first, new for anything this project did; never name the owner; never AskUserQuestion.

## Wave 1 (14:4x UTC 15 Oct)

### ELEC-R3 (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 3): fr5761-election-1519 third reader on Phi, Hbar, "Orval"
ELEC-R2's Next (1): "native-resolution crops of the f.51r Brandebourg/Treves rows and the note's second line (openapi.bnf.fr c105 regions, 2
requests, ~0.8) for a third reader on Phi, Hbar and 'Orval'". Read ELEC-VERSO and ELEC-R2 and `elecr2/PREREG-ELEC-R2.md` first. PREREG
addendum (commit before the fetch): the registered rule and decoys stay exactly as ELEC-R2's; only the crops change (native resolution).
One blind Sonnet reader on the crops (crops in scratchpad, never git), score by the registered rule, report agree/disagree with R1 and R2 per
target and decoy. Lead grade M at most; no key edit. NOTES "## ELEC-R3", Next updated.

### COL26-LEN (Opus, cap 2, box 45 min, disk only): colbert26-lathuillerie-1644 11 = re and 81 = me under a length-matched score
Verdict: "cheapest next: the same two codes under a length-matched score gated on the 5 known 2-letter codes, ~$1". Read COL26-KEY and
COL26-1181 (and their PREREGs) first. PREREG (commit before any score): the length-matched score, the value-class control on the 5 known
2-letter C codes and its pass gate, and the accept rule for each of 11 and 81. Control first: if the 5 known codes do not pass, stop and log
"non-test" (both stay M). Use `tools/decode_key.py --try` / existing folder scripts with an option, no private copy. key_f23 and readings
unchanged unless the registered rule licenses an M -> S, which goes to key_f23_c50rev.tsv only. NOTES "## COL26-LEN", gaps + Verdict,
gaps_check.

### MONL-R0S (Opus, cap 2, box 45 min, disk only): fr4735-monluc-lansac-poland-1573 positional null for K14 = s
Verdict: "cheapest next: the R0s positional null for K14=s (~$1)". Read MONL-K14TRY and MONL-SORT2 (and the R0s text near NOTES l.1598) first.
PREREG (commit before scoring): how the positional null is built (what is permuted, draws >= 200, what it must be able to do differently
from the target: CLAUDE.md rule 3 orthogonal-control clause), and the rule under which R0s licenses K14 = s at S, stays M, or is refused.
Scripts only, no vision. A licensed value is written only as the registered rule says (lead or key file named in the PREREG). NOTES
"## MONL-R0S", gaps + Verdict, gaps_check.

### BAL-65C (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 4): baluze167-davaux-1637 glossed plain 65 on Chavigny canvases
Verdict: "a glossed plain 65 is not turning up by canvas sweep ... either more 168/170 Chavigny canvases (survey.tsv rows 168 f.166 c346/c348,
f.212 c438/c440, f.158 c330-332; ~$1.5 per two canvases) or accept L04 pos 0 as 65 without its acute". BAL-65L's method exactly: fetch 168
c346 and c348 at 2400 px (scratchpad, never git), zoom every 65 under a gloss, classify acute/plain by BAL-65L's registered features. Only two
canvases; if a glossed plain 65 is found, add the row to f22mk/glossed_pairs_169c.tsv and re-run the scorer per its PREREG. NOTES
"## BAL-65C", gaps + Verdict, gaps_check.

### JAV-200 (Opus, cap 1.5, box 40 min, the folder manifest's IIIF host <= 3): na-janssens-java-1811 leaf 200 cell 119 (and 6)
JAV-198's Next: "read leaf 200 cell 119 (and 6) at native size (1 IIIF request, ~$0.7); if it reads 420, key row 120 is a misread of 420 and
goes to the key owner's next regrade, not edited by a cross-check job." Do exactly that: one region request at native size, one blind look at
each cell (Opus eye or one Sonnet call, say which), record the reading and what it implies. No key change: write the finding to the folder's
HYPOTHESES.md / corrections note as JAV-198 did. NOTES "## JAV-200", gaps + Verdict, gaps_check.

### F3198-PL (Sonnet, cap 1.5, box 45 min, archivesetmanuscrits.bnf.fr <= 25, >= 3 s apart): fr3198-labbe-1577 piece lists for l'Abbé letters
NOTES "Next steps": "(b) of D2-F3198 stands -- search the archivesetmanuscrits piece lists of the other Nevers volumes (fr.3198-3200,
fr.4696-4715) for l'Abbé letters of Feb-Apr ..." (read the line in full for the date window and what is sought). Plain search form, page 1 via
curl, pagination via tools/browser_fetch.js if needed (run twice, CLAUDE.md host table). Record every volume searched, query, hit / no hit,
with the finding-aid ids. Catalogue search only: no images, no status change; add a dated NOTES section "## F3198-PL" and a one-line Next.

Wave 1 sessions (14:37 UTC): ELEC-R3 session_01ACfVYHLwfKCoeFre8z1PXb; COL26-LEN session_01A1vrd2rCD9NPMkA6e9ib9G; MONL-R0S
session_01RJKdEakDQZh2dnz2SJUYx1; BAL-65C session_01VEJCwnzeNAGbK2qZxoiVX9; JAV-200 session_012rvR2A8T4ps2wQ7VxfyRcf; F3198-PL
session_0144vRi7ysA48FZ6muHuAvt5 (Sonnet).

Wave 1 results (15:1x UTC): ELEC-R3 1.80 N, COL26-LEN 1.78 D (stood down: duplicated COL26-LM; orchestrator's brief error, read below the
Verdict line before briefing), MONL-R0S 2.00 N, BAL-65C 2.91 D-, JAV-200 1.84 D, F3198-PL 1.01 N; all ledgered and archived.
Seven-day `allowed_warning` on every session: not a stop (BUDGETS.md 27 Sept amendment); five_hour not reporting.

## Wave 2 (15:2x UTC 15 Oct)
Excluded in addition: LANE DEFAULT-A4-1441-15 (matignon, clair1161, lodewijk). Each brief's step was checked against the folder's latest
sections (not only the Verdict line) before writing it.

### ELEC-REC (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 5): fr5761-election-1519 rectos ff.161r-164r
ELEC-VERSO next (2), repeated by ELEC-R2 and ELEC-R3: "with the f.51r block as the key, search fr.5761 rectos ff.161r-164r (c325-c331, 4
canvases at 1000 px, ~1.5) ... for further occurrences of its signs, which a third oXo would need for C". Read ELEC-VERSO, ELEC-R2, ELEC-R3.
PREREG (commit before the fetch): what counts as an occurrence of each f.51r sign (oXo, Lfo, Phi, Hbar and the rest of the block) and the
decoy rule (ELEC-R3's decoy fired: say how this pass avoids that). 4 canvases at 1000 px (scratchpad, never git); one Opus look per canvas,
native region only for a candidate sign (<= 1 extra request). Lead grade M; a third independent oXo is reported, not keyed. No fourth reader
on the f.51r images. NOTES "## ELEC-REC", Next updated.

### BAL-65D (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 4): baluze167-davaux-1637 glossed plain 65 on 168 c438/c440
BAL-65C's Verdict: "the call rule needs >= 3 glossed plain 65, so it stays M; next: two more glossed plain 65 from the same letters (survey.tsv
rows 168 f.212 c438/c440, f.158 c330-332)". BAL-65C's method and PREREG exactly, on 168 c438 and c440 only (2400 px, every 65 under a gloss
zoomed). Add any glossed plain 65 to the pair file and re-run the scorer per the PREREG; L04 pos 0 moves only as the call rule says. NOTES
"## BAL-65D", gaps + Verdict, gaps_check.

### F3198-72 (Opus, cap 2, box 45 min, openapi.bnf.fr <= 3): fr3198-labbe-1577 f.72 nos.34/35 native view
F3198-PL's Next: "the 17 Apr pair f.72 nos.34/35 in fr.3198 (own volume, native view for inserted numeral groups, ~USD 1)". Locate f.72's
canvas with tools/gallica_folio.py (manifest only; openapi.bnf.fr for the image), view at 1000 px then one native region if numeral groups
appear. Report: are there cipher groups, how many, in which hand, and do they share the target letter's sign set (list signs seen; no
decoding). No status change unless it is the folder's blocker, which F3198-PL says it is not; dated NOTES section "## F3198-72" and Next.

### JAV-KEY (Opus, cap 1.5, box 30 min, disk only): na-janssens-java-1811 key row 120 regrade
JAV-200's Next: "key owner's regrade drops/annotates key row 120 (Fin.) as a misread of 420 at 200:119". Apply it the way GAPS3's regrades.tsv
does (one decision row naming JAV-198 and JAV-200 as witnesses), annotate or retire key row 120 per the folder's convention, then
`tools/decode_key.py ciphers/na-janssens-java-1811 --check` (update the committed reading only if 120 occurs and the script says it is
stale). HYPOTHESES.md conflict entry closed with witnesses. NOTES "## JAV-KEY", gaps + Verdict, gaps_check.

Wave 2 results (15:4x UTC): ELEC-REC 2.11 N, BAL-65D 3.22 N (1.29x), F3198-72 1.96 N, JAV-KEY 1.73 D; ledgered and archived.

## Wave 3 (15:5x UTC 15 Oct)

### JAV-420C (Opus, cap 1.5, box 30 min, disk only): na-janssens-java-1811 re-apply GAPS3's 420 M -> C
JAV-KEY found: "key.tsv's 420 row still carries grade M ... Next: re-apply GAPS3's 420 M -> C to key.tsv (scripts/apply_regrades.py, then
--check; leaf 188 C 84 -> 85 ...)". Read GAPS3's regrades.tsv decision for 420 and JAV-KEY first; re-apply exactly that decision (no new
evidence), `tools/decode_key.py ciphers/na-janssens-java-1811 --check`, regenerate the committed reading only through the folder's script.
Rule 10 propagation: if the reading's counts change, carry the change into AUDIT.md (one dated line, no class change) and into any
SECOND-OPINIONS-QUEUE.tsv row for this folder. The keysource passes' 120 cells: note in NOTES only (transcription records are not edited
without the image). NOTES "## JAV-420C", gaps + Verdict, gaps_check.

### ELEC-3897 (Opus, cap 3, box 60 min, openapi.bnf.fr <= 6): fr5761-election-1519 fr.3897 items 36-38, 62, 64-65, 73 for second witnesses
ELEC-REC Verdict Next (1): "fr.3897 items 36-38, 62, 64-65, 73 (ELEC-PAIR next 3) for second witnesses". Read ELEC-PAIR (its next 3) and
ELEC-REC first. PREREG (commit before the fetch) with ELEC-REC's occurrence and decoy rules. Locate the items' canvases with
tools/gallica_folio.py (manifest only), 1000 px views (scratchpad), one Opus look per canvas, at most one native region per candidate within
the request cap. Report per item: name signs present or not, and any occurrence of an f.51r-block sign. Lead grade M; no key edit. Stop before
a canvas that would cross 80% of cap. NOTES "## ELEC-3897", Next updated.

### BAL-65E (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 4): baluze167-davaux-1637 168 c330-332, the last listed Chavigny source
BAL-65D's Next: "168 c330-332 (f.158 letter), last listed Chavigny source (~1.5)". BAL-65C/65D method and PREREG exactly, those canvases only.
After it, the Verdict must name the outcome for L04 pos 0 in one line: rule met (S), or every listed source spent and the token parked as M
with "no further listed source" (no further canvas sweep proposed without a new source). NOTES "## BAL-65E", gaps + Verdict, gaps_check.

Wave 3 results (16:1x UTC): JAV-420C 1.59 D (420 -> C, leaf 188 C 85 M 22), ELEC-3897 2.74 N (items 36, 38, 62-65: names in letters),
BAL-65E 2.90 D (plain 65 2/2 = ra, rule needs 3, L04 pos 0 parked M, no further listed source); ledgered and archived.

## Wave 4 (16:1x UTC 15 Oct; last wave)

### JAV-RG (Opus, cap 1.5, box 30 min, disk only): na-janssens-java-1811 make apply_regrades.py --check pass again
JAV-420C found: "`apply_regrades.py --check` on the full regrades.tsv fails (row 120 retired; 102 and 1096 superseded by GAPS17), so the
script's own rule-7 check no longer describes key.tsv. Next: a regrades.tsv `superseded_by` column or a skip for retired / later-decided rows,
with the pass-correction for 200:119, disk only, ~$1." Do that: add the column (or skip rule) so the script reproduces the current key.tsv
exactly, without changing any key value or grade; `apply_regrades.py --check` and `tools/decode_key.py ciphers/na-janssens-java-1811 --check`
both exit 0. The 200:119 pass-correction goes to corrections.tsv per the folder's convention (keysource passes stay as transcribed, rule
"never silently repaired"). NOTES "## JAV-RG", gaps + Verdict, gaps_check.

### ELEC-39 (Opus, cap 2.5, box 50 min, openapi.bnf.fr <= 5): fr5761-election-1519 fr.3897 items 37 and 39
ELEC-3897's Next: "fr.3897 item 39 (Joachim to Bonnivet, Kluckhohn nr. 356) between f.82 and f.103, ~2"; item 37 was not located (f.74-81v).
ELEC-3897's PREREG and rules exactly; locate by canvas label first (tools/gallica_folio.py, manifest on disk if saved), then 1000-2000 px views.
Report per item: name signs present or not, any occurrence of an nr. 357 / f.51r-block sign. Lead grade M; no key edit. NOTES "## ELEC-39",
Next updated (if both items are clear, say the fr.3897 route for a second witness is spent).

Wave 4 results (16:4x UTC): JAV-RG 1.95 D (apply_regrades --check passes, key.tsv byte-identical), ELEC-39 1.72 D (fr.3897 item 39 f.84r
carries name signs barI x5, Zheavy x3, 4 x1, M, one reader); ledgered and archived.

## Wave 5 (16:4x UTC 15 Oct; one job, then close)

### ELEC-356 (Opus, cap 3, box 60 min, archive.org <= 2, openapi.bnf.fr <= 2): fr5761-election-1519 pair f.84r-v against Kluckhohn nr. 356
ELEC-39's Next (1): "pair f.84r-v against Kluckhohn nr. 356 (p.813, archive.org `bub_gb_0gFoAAAAMAAJ` leaf n821, 1 request) plus c107 (f.84v)
at 2000 px, under ELEC-PAIR's pre-registered rule; barI, Zheavy and 4 could reach >= 2 pairs each, ~2.5." Read ELEC-PAIR (its PREREG and
pairing rule) and ELEC-39 first; PREREG addendum committed before the fetch, rule unchanged. Pair each sign position with the print's name at
the same place; report pairs per sign, agree/conflict with nr. 357 / f.51r values, and what grade the registered rule licenses (a key value
only if the rule licenses it; conflicts to HYPOTHESES.md with witnesses). Item 37 is not part of this job. NOTES "## ELEC-356", Next updated.

Wave 5 result (17:0x UTC): ELEC-356 2.34 D (f.84r-v = Kluckhohn nr. 356 word for word but the signs; 12 pairs, 0 conflicts; pooled with nr.
357 under ELEC-PAIR's unchanged rule barI = Boheme and Zheavy = Saxe reach C; Kluckhohn names his nr. 316 as the source of the name-cipher
resolution); ledgered and archived.

## Wave 6 (17:1x UTC 15 Oct; one job, then close)

### ELEC-316 (Opus, cap 2.5, box 50 min, archive.org <= 4, openapi.bnf.fr <= 1): fr5761-election-1519 read Kluckhohn nr. 316
ELEC-356's Next (1) and (2): "read Kluckhohn nr. 316 (same volume, archive.org `bub_gb_0gFoAAAAMAAJ`, locate by the 'No. 3xx' running heads;
~1-2 requests) and its own source line: if 316 is the key or a decipherment, it is a key source for this name-sign set (grade H) and for
checking every C/M above, ~1.5; (2) settle the l.27 4|flag slot image-to-image against f.116r l.11/l.29/l.32 (openapi.bnf.fr f142 at 2400, 1
request), ~1". Do (1) first: transcribe what nr. 316 prints about the signs (quote it, with page/leaf), name its manuscript source, and check
every C/M name-sign value in this folder against it (agree / conflict per sign; conflicts to HYPOTHESES.md with witnesses, rule 4). A key
value goes to key.tsv at H only if the print gives the sign-to-name table itself (an edited key, credited to Kluckhohn 1893 as a published
source), otherwise as a lead. Then (2) only if under 60% of cap. NOTES "## ELEC-316", Next updated. Report what was found and where it was not
found; do not classify novelty.
