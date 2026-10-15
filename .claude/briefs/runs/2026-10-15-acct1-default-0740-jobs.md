# LANE DEFAULT-account-1-20261015-0740 jobs (account 1, lane orchestrator session_017cqzjbis9FztzHDDPLyGbm) -- 15 Oct 2026 08:0x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 07:40-17:40 UTC 15 Oct. Gate 0a: SESSION-SWEEP-account-1 stale-claimed since 5 Oct
22:40, proceeded. VERIFY-BACKLOG.tsv (02:40 15 Oct): high rows Birago/ceppo (off limits), rest audit2 on N0/N1 items (known text; googleapis
503 since 12 Oct). Backlog = the A1-0447 handoff next list (STATUS.md) + `next_steps.py --hot-only` runnable rows. Excluded: folders held by
the live DEFAULT-A4-0645-15 lane (lodewijk-van-nassau-1573-74, clair1161-avis-flandre-1688, baluze167-davaux-1637, na-suriname-map-1781) and
by DEFAULT-A2-0509-15 (harley-287-1587, matignon-mayenne-1586, august-van-saksen-1561-64, es132-vargas-mexia-1578,
oldenbarnevelt-brederode-1605); Birago family, Armstrong, Debosnys, VIV-KEYSTONE (fr16104/fr16105/fr16106), BNF-FOCUS folders and holdings,
cipher-lab-private.
Intake gate 07:5x UTC (tools/intake_gate_check.py, exit 0 each): pro3055-clinton-1779, fr4712-nevers-duchesse, mccormick-1999,
fr5761-election-1519, fr4735-monluc-lansac-poland-1573.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-14-acct1-default-1840-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A1-0740-15 (account 1)"; export `CIPHERLAB_ACCOUNT=account-1` before any tools/room.py call;
- first actions: `git fetch origin && git checkout -B main origin/main`, `date -u`, read the last 60 ROOM.md lines (if another session
  claimed your folder in the last 6 h with no done line, post a "stood down" line and stop), post a claim line with your box end time;
  fetch and rebase immediately before every push (`python3 tools/room.py --push <paths>`; if it reports a failure, fetch, rebase, keep both
  sides of any ROOM.md or NOTES.md conflict, and push once more); a file new to git is pushed with plain `git add` + commit + push and checked
  with `git cat-file -e origin/main:<path>`;
- every claim/halfway/done ROOM line ends with "usage: not readable here" (get_session is not available to workers);
- price every look: a vision call is a unit (~0.5-1.0); an Opus session has a floor of ~2 before any look; state units x rate in your claim
  line; stop before a unit that would cross 80% of cap or box. The orchestrator reads get_session at 30 min and interrupts at 1.3x cap.
- solver jobs: report what was found and where it was not found; do not classify novelty.
- no www.googleapis.com in this wave.
- every other rule there holds unchanged (shared-host take/release lines, halfway line, no images in git, gaps_check on `partial`, no
  novelty words, no AskUserQuestion, `date -u` before any time, "cost not visible to this session").

## Wave 1 (08:0x UTC 15 Oct)

### CLIN-3004 (Opus, cap 5, box 75 min, image-uab.canadiana.ca <= 20): pro3055-clinton-1779 letter 3004 reel cipher page(s)
A1-0447 next 1: "sibling reel ciphers 3004, 3502, 3537, 4152, 4216 (~4-5 a page, same method)". 3004 only (printed 1920 doc 196 pp.170-171,
B.147 pp.234-5). Exactly CLIN-247/CLIN-2962's method (read their NOTES sections and PREREGs): locate the cipher page(s) on the reel, register
the B2 gate and the page-permuted-key control before decoding, iiif_lines.py crops (command pasted before the first subagent call), two blind
passes + one reconciliation unit. If 3004's cipher runs over more than one page, do the first page only and name the rest. No images in git.
NOTES "## CLIN-3004", gaps + Verdict, gaps_check. Text-known item: this tests the reel key on a printed sibling (lane guardrail share).

### F4712-8R (Opus, cap 4, box 60 min, openapi.bnf.fr <= 8): fr4712-nevers-duchesse F4712-8 resumed
Verdict: "finish F4712-8's N tiles and run its one pre-registered blind call, ~$1.5". PREREG ea57e0de7 stands: do not change it. Read
F4712-HAND and F4712-8 first; place the 2 more control 8s the PREREG asks for (value-free tiles), run the one scored call exactly as registered,
score it by the registered rule. Result is a same-writer lead graded M at most. NOTES "## F4712-8R", gaps + Verdict, gaps_check.

### MCC-JUDGE (Opus, cap 3, box 60 min, disk only): mccormick-1999 judge + NCBE-stem-keeping null on the MCC-SUFX candidate
Verdict: "judge_plaintext on the MCC-SUFX decode and an NCBE-stem-keeping null to size the single-type share of the margin, ~$3". Read MCC-SUFX
and its PREREG (335740320). Pre-register the null (keep NCBE-stem tokens fixed, shuffle the rest by type, >= 200 draws) and the margin rule in
NOTES before running. Run `tools/judge_plaintext.py` on the candidate (paste the output; the `en` corpus caveat in tools/data/en/README.md
applies: a PASS/FAIL there is of unknown reliability, say so) and the null. No vision calls. NOTES "## MCC-JUDGE", gaps + Verdict, gaps_check.

### ELEC-SRC (Opus, cap 3, box 45 min, archive.org <= 6, openapi.bnf.fr/gallica <= 6): fr5761-election-1519 Kluckhohn source line
ELEC-5756's next (1): read Kluckhohn's own source line for nr. 357 and nr. 383 on the RTA J.R. I page image (archive.org `bub_gb_0gFoAAAAMAAJ`,
1-2 page requests), not the OCR, to get the real shelfmark. If it names a BnF volume, look up that volume's Gallica ark only (one SRU or
catalogue request) and, only if digitised, read the folio Kluckhohn cites at 600 px (<= 4 canvases) for the cipher name groups. Do not start
a census of the volume. Status stays as written unless a pair is found (>= 2 occurrences per sign before any C grade). NOTES "## ELEC-SRC",
Verdict.

### MONL-L16 (Opus, cap 6, box 90 min, disk only): fr4735-monluc-lansac-poland-1573 c268 L16-L20
Verdict: "c268 L16-L20 two blind passes + reconciliation, then align_c268.py (~$3); the L15:9/L15:18/L11:14 eye re-check (~$1) can ride with
it". Exactly MONL-L11's method (read MONL-SORT, MONL-ALIGN, MONL-VB, MONL-L11, MONL-ADH first): <= 12 crops per call, ~0.5 per call; 5 lines x 2
blind passes + 1 reconciliation + 1 eye re-check = 12 units -- state the count in your claim and stop before the unit that would cross 80% of the
cap. No key value, machine label or decode in a blind call. Then align_c268.py --check and the shuffled-clear control (200). NOTES
"## MONL-L16", gaps + Verdict, gaps_check.

## Wave 1 result (08:3x UTC): CLIN-3004 4.66 D, F4712-8R 2.45 N (NON-TEST, instrument retired, folder parked), MCC-JUDGE 2.57 D, ELEC-SRC 2.29 D; MONL-L16 running.
Parallel lane DEFAULT-A2-0810-15 (account 2) holds matignon-mayenne-1586, oldenbarnevelt-brederode-1605, harley-287-1587, kaliningrad-2015: not picked.

## Wave 2 (08:3x UTC 15 Oct)

### CLIN-3004B (Opus, cap 6, box 75 min, image-uab.canadiana.ca <= 16): pro3055-clinton-1779 letter 3004 pp.230-231
CLIN-3004's named rest: B.147 pp.230-233. Pages 230 and 231 only, CLIN-3004's method and the same PREREG design (append a PREREG addendum
naming the two pages before any pass): crops command pasted, two blind passes + one reconciliation per page (6 units at ~0.7 = ~4.2; stop
before a unit that would cross 80% of cap), the B2 gate and page-permuted-key control per page. No images in git. NOTES "## CLIN-3004B",
gaps + Verdict, gaps_check. Text-known item (guardrail share).

### ELEC-357 (Opus, cap 4, box 60 min, openapi.bnf.fr/gallica <= 10): fr5761-election-1519 fr.3897 item 56 and fr.5761 nr. 383 position
ELEC-SRC's next: locate fr.3897 item 56 ("Double des lettres de Joachim ... a l admiral, XVIIIe jung 1519", btv1b90096539) from the f.146 = item 73
anchor (~3-4 canvases at 600 px), then read item 56's canvases for cipher name groups (<= 4 canvases); then the fr.5761 manifest/notice Description
for where nr. 383 sits (1-2 requests, no canvas census). Status stays as written unless a pair is found (>= 2 occurrences per sign before any C
grade). NOTES "## ELEC-357", Verdict.

### MCC-GREGG (Opus, cap 6, box 90 min, disk; gutenberg.org or archive.org <= 6 only to fetch a public-domain Gregg shorthand dictionary/word list): mccormick-1999 Gregg-lexicon variant of the suffix-mark model
Verdict: "the Gregg-lexicon variant of the suffix-mark model with its matched control, ~$6". Rule 3 check first, in NOTES: this is a different
lexicon (new material), not a re-tune of the MCC-SUFX knob; if you cannot get a public-domain Gregg word list in <= 6 requests, stop and log
"not run: no corpus", do not substitute. PREREG (control at the target's N=132 / K / ending profile, the MCC-JUDGE NCBE-fixed and type nulls,
>= 200 draws, the margin rule) before scoring the target. `tools/token_anneal.py` option, not a private copy; offline test in tools/tests/.
No vision calls. NOTES "## MCC-GREGG", gaps + Verdict, gaps_check.

## Wave 2 result (09:0x UTC): MONL-L16 7.87 D (1.31x), CLIN-3004B 5.59 D, ELEC-357 2.77 D; MCC-GREGG running. pro3055 stops here this lane
(text-known share ~10.3 of ~36 spent, over the fifth guardrail); pp.232-233 go to the handoff.

## Wave 3 (09:1x UTC 15 Oct)

### MONL-K04 (Opus, cap 6, box 90 min, disk only): fr4735-monluc-lansac-poland-1573 K04|K12 value-blind sort, then c268 L21-L25
Verdict: "the value-blind K04|K12 sort of the L16-L20 tiles with L11:14 (~$1.5), then c268 L21-L25 (~$3)". MONL-L16 ran 1.31x: price per call,
<= 12 crops per call, ~0.5 per call. Units: sort 2 + L21-L25 (5 lines x 2 blind passes) 10 + reconciliation 1 = 13; state them in the claim and
stop before the unit that would cross 80% of the cap (if the sort alone reaches that, stop after it). Same rules as MONL-ADH's value-blind sort
(controls first) and MONL-L16's blind passes. Then align_c268.py --check and the shuffled-clear control (200). NOTES "## MONL-K04", gaps + Verdict,
gaps_check.

### ELEC-PAIR (Opus, cap 4, box 60 min, archive.org <= 6, openapi.bnf.fr <= 4): fr5761-election-1519 nr. 357 name signs vs Kluckhohn's print
ELEC-357's next: Kluckhohn RTA J.R. I nr. 357 printed text (pp.813-814 and the n.821-822 reference ELEC-357 names; `bub_gb_0gFoAAAAMAAJ` page
images, not the OCR) against the ~7-8 name signs on fr.3897 ff.116r-117r (c142 right, c143). Pre-register in NOTES the pairing rule (a sign
pairs with a printed name only where the clear context on both sides matches; >= 2 occurrences per sign before any C grade; a shuffled-name
control). Value-free crops. Do not start the nr. 383 bisection. NOTES "## ELEC-PAIR", Verdict.
