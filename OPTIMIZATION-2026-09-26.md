# Optimisation review, 26 Sept 2026 (owner-account parent, at the owner's request, about 18:00 UTC)

The owner's four concerns, each with the measurement that bears on it and the change proposed. Both parents
read this; the other account's parent (7i) replies in ROOM.md "for the owner-account parent".

## Measurements (26 Sept, LEDGER.md rows dated 26 Sep, and ciphers/ at 18:00 UTC)

| What | Number |
|---|---|
| Spend today, all rows | about USD 1,457 over 241 ledger rows |
| of which target work (readings, transcriptions, alignments, check-solved on a target) | about 792 (54 percent) |
| of which meta: LEARN passes, retrospectives, applies, QA, out-checks, PR landing, tools, system map | about 406 (28 percent) |
| of which lane orchestrators | about 147 (10 percent) |
| of which scouts | about 46; verifiers about 66 |
| New letters on the board today | 0 (count flat since 06:20; the one N-class change was a dataset row) |
| Target folders | 255: 85 open, 24 partial, 24 blocked, 32 found-solved, 9 closed-negative, 5 solved |
| Open or partial folders whose NOTES.md ends with a written "next step" nobody has run | 63 of 111 |
| Near-solve rows | 13 |
| Key tables on disk | 142 files; KEY-CROSSMATCH: 57 usable keys, 35 with an own text, judge control miscalibrated since 25 Sept (verified readings fail its pass_real gate) and not rerun since |
| Items waiting on the owner | 46 open or waiting ASKS rows, 11 LOCAL-QUEUE rows, 6 OUTBOX sections |

## (a) The human in the loop

Finding: 46 open asks on one person is not a queue, it is a wall; the person cannot rank it, so nothing on it
moves and each parent keeps adding. Drops today came from three shapes: a hand-over gap on one account (no
verifier for three hours), silent write failures (PR-LAND-3, twice), and a parent's own spawn error
(SCOUT-OWN-2). Each now has a mechanical guard; none had one this morning.

Change: (1) a desk cap -- the parents keep at most five items on the owner's desk at any time, each one action,
one sentence, with a paste-ready text; everything else lives in a ranked backlog (ASKS.md stays the ledger, the
board's "Your desk" shows only the five); the parents re-rank daily and say what they demoted. (2) A
dropped-item detector in tools/orphan_check.py: any ROOM line addressed "for <role>" with no reply from that
role within two hours is a finding at every check-in, so nothing waits silently (the Japikse question waited
three and a half hours today). (3) The owner does nothing that needs reading the repository: if an ask needs
context, the ask is wrong.

## (b) Two accounts with mirrored roles

Finding: the mirror costs money and causes collisions. Today: nine LEARN passes across both accounts, five
retrospectives and applies, two landing workers on the same pull requests, and two verifier arrangements.
About a quarter of the day's spend was accounts learning from and checking each other.

Change: specialise instead of mirror, without moving anything in progress (the owner's condition, 26 Sept
18:1x). Every lane keeps its targets to completion on the account that started it. From now on the other
account is SOLVE (it holds the deep target work and the verifier lineage) and the owner account is SUPPLY
(scouting capped at one new index a day, check-solved filters, runner PR landing, QA, retrospectives, tools,
out-checks, partner outreach); LANE WC and LANE VO1, opened on the owner account tonight, run to completion as
exceptions. New target lanes from partner lists go to SOLVE by default. One LEARN pass and one retrospective a
day, both on SUPPLY. Shared files stay shared; the parents keep hourly check-ins with distinct duty lists.
Proposed to parent 7i in ROOM; applied to parent.md when both parents agree.

## (c) Quitting too early

Finding: 63 open or partial folders end with a written next step that no worker has run. Lanes are opened from
scout picks, not from that backlog, so the backlog is invisible and the same money buys a fifth scout of the
same tables. "Control below gate, not a test" is often where a folder stops, though the fix (crops, an atlas, a
second pass) is named in the same paragraph.

Change: (1) tools/next_steps.py builds NEXT-STEPS.tsv from every open or partial NOTES.md: folder, the next-step
sentence, blocker type (needs image / needs key / needs person / runnable now), estimated cost from the pricing
precedents; the board shows it. (2) Every lane's job 1 is the top runnable row of that list; a scout is spawned
only when the runnable rows are exhausted. (3) A folder is not left "open" with a runnable next step for more
than a day without a ledger row saying why.

## (d) Keys as an attack corpus

Finding: the corpus exists (142 key tables, KEY-OFFICES.tsv with office, correspondents, years, language;
tools/key_crossmatch.py; tools/family_run.py; tools/glyph_atlas.py), but it is used once per lane, not
continuously, and its judge control was left miscalibrated on 25 Sept, so its verdicts are not trusted.

Change: (1) recalibrate key_crossmatch's gate on the verified readings as positive controls, then run it
nightly (a routine) against every new ciphertext on disk, posting hits to ROOM. (2) Build KEY-DESIGN.tsv: for
each key, its structural signature (alphabet size, homophones per letter, nomenclator size, numeral ranges,
syllable tables, nulls, office, decade, language) and tools/design_prior.py, which scores an unread
ciphertext's sign statistics against those signatures with a shuffled control, so the design family of an
unread letter is predicted before any attack is chosen -- the owner's intuition, made mechanical: a's
structure narrows b's hypothesis. (3) Every solved or recovered key is added to both tables at the lane's
close-out, as a ledger rule.

## Order of work (owner-account parent, tonight)

1. NEXT-STEPS.tsv tool and list (Sonnet, cap 4), then LANE WC and every later lane takes its job 1 from it.
2. key_crossmatch recalibration + nightly routine (Opus design, cap 8).
3. Desk cap and dropped-item detector (Sonnet, cap 4: parent.md rule, orphan_check change, board "Your desk").
4. KEY-DESIGN.tsv and design_prior.py (Opus, cap 10), after 1-3.
5. Account specialisation: proposed to 7i now; parent.md edited when agreed; the owner decides if the parents
   do not.
