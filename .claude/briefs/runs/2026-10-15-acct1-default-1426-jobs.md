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
