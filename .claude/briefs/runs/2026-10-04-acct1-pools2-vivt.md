# LANE-POOLS2 VIV-T -- fr16106-vivonne-longlee-1579: spec + first cheap test with a matched control (account 1), 4 Oct 2026 07:0x UTC

Why: LANE-POOLS2 item 2 (`.claude/briefs/runs/2026-10-04-acct3-lane-pools2-a3v2.md`): the pool passed the bar on a point estimate
(VIV-M, 6accb244: ~225 dense cipher canvases, ~90 unglossed, interval reaching 0). Breadth rule 3a: spec + ONE first cheap test,
two numbers in `cheap_test_done`; account 3 promotes. Read `ciphers/fr16106-vivonne-longlee-1579/NOTES.md` in full first.
Off limits: `ciphers/fr16104-vivonne-spain-1572` (read only; its 1572-74 table is a different key).

Model Opus 5.5 (you), Sonnet subagents for passes, at most 2 at once. Cap USD 10, box 80 min. Unit pricing per pass (Usage 6):
~USD 1.5 per page-pass; plan = 1 cipher page x 2 blind passes + 1 reconciliation + 1 plain-copy page read = 4 units ~6, plus
bisection and scripting ~2. Stop before a unit that would cross 80% of cap or box. Gallica: browser UA, >= 2 s apart, <= 50 requests,
each canvas once; you are the only LANE-POOLS2 worker on Gallica.

1. Gate: `python3 tools/intake_gate_check.py fr16106-vivonne-longlee-1579` (paste). Write `specs/fr16106-vivonne-longlee-1579.json`
   (Pipeline 3a fields: ciphertext source + date, alphabet (two systems seen: letter-form marks in fr.16107/16108 c80/c102, digit-and-
   mark in fr.16108 c256/c322/c388/c432 -- say which your pair uses), constraints, cheap tests in order, `judge` block; check
   tools/data for an era-matched 16th-c French corpus (fr16) and name it).
2. Pair: locate the clerk's plain copy ("Dechifre de la precedente") of fr.16107 c107-c108 by bisecting c109-c126 at 600 px (or take
   another dense letter whose plain copy you locate first, whichever is cheaper). Record both canvases and the date.
3. Crops then passes (TRANSCRIPTION.md): paste `python3 tools/iiif_lines.py --ark btv1b9009661v --canvas <N> --region <x,y,w,h>
   --out ciphers/fr16106-vivonne-longlee-1579/images --prefix c<N> --debug`, check the overlay, 2 blind Sonnet passes on crop paths
   only (no plaintext), `tools/reconcile_passes.py`, reconcile from the crops; err_2reader reported. Read the plain copy for the
   same span (one unit; transcribe as written, rule 2).
4. PRE-REGISTER (commit + push `PREREG_test1.md` before any key is fitted): split the pair into a fit half and a held-out half by line
   (state the split). Fit a key on the fit half with `tools/interlinear_align.py` (grade C). Statistic: held-out known-answer
   character/token agreement of the fitted key's decode against the plain copy. Nulls computed first: (a) the same fitted key with its
   values shuffled (>= 1000), (b) the fitted key applied to the held-out cipher against a wrong plain window of the same length from
   the same copy (>= 200). Gate: real > both p99. State in one line why each null can differ from the target on this statistic (rule 3
   orthogonality). A held-out half too short for the key's own sign count is a NON-TEST, say so rather than run it.
5. Write `key.tsv` (fit-half values, grade C, counts), the held-out decode, a script with `--check` (rule 7). Grade tokens per rule 4.
   Spec `cheap_test_done` = target real vs null p99s. Refresh Remaining gaps / Escalation (gaps_check passes); if PASS, name the next
   test (the fitted key on one unglossed letter, judge fr16 vs shuffled-key null). Do not touch status.json / NEAR.md / QUEUE.md.

Done line (tools/room.py, role "LANE-POOLS2 VIV-T (account-1 worker)"): `done (<start>-<end> UTC, brief met|box|cap): commit <sha>.
fr16106 pair <canvases> (<date>): <n> cipher signs, err_2reader <x>; key <k> values C; held-out agreement <real> vs value-shuffle p99
<a> / wrong-window p99 <b> -> PASS|FAIL|NON-TEST; gaps_check <r>; requests ...; cost: see the lane ledger`. Report what was found and
where it was not found; do not classify novelty.
