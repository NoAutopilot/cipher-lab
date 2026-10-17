# Research director, wave 3 (17 Oct 2026, 02:2x UTC by date -u): the flagship's key cells; program C's first candidate

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, PREREG with a `## Decision` block pushed before any scored run, `tools/experiment_log.py --check`). Each job ends its
NOTES section with the six research-director questions answered in one line each. Report what was found and where it was not found; do
not classify novelty (rule 10).

## JOB VIV-KCELLS (account 4; Opus 5.5; cap USD 4; box 45 minutes; disk only, no network, no readers, no images; Price: vision calls: 0 x USD 0 = 0)

Flagship ciphers/fr16104-vivonne-spain-1572. ERR-SIM (NOTES "## ERR-SIM (17 Oct 2026)", RESEARCH.md s.4.1 and s.5) showed the key, not
the readers, caps every ink-63 clause: key.tsv has no H/C code for p, m, f, k, x, y and only M rows for b, h, z; the zero-error control
reads 54 letters against an AD of 94.6, and 143 once p and m have codes. VIV-ANCHOR (8 Oct 2026, NOTES l.1819) tried word-window anchors
and found under 3 decided positions for m, p and qu, because a window anchors only when every other letter already decodes. Question: with
a whole-stream alignment instead of word windows, which reader labels carry p, m and f on the deciphered sibling pairs, and at what share?
1. PREREG first (`PREREG-VIV-KCELLS.md`, Decision block below, pushed before any run). Instrument: `tools/interlinear_align.py stream
   SYMBOLS.txt TEXT.txt OUT_KEY.tsv` (DP hard-EM, one letter per cipher sign; read its --help and the HEID-1623CAL lesson in
   ciphers/brederode-heidelberg-1621/NOTES.md: the tool is untested below N 200, so use only pages with N >= 500), a different instrument
   from VIV-ANCHOR's windows (rule 3 third-attempt clause respected: windows, n-gram rank and the f-split are the retired ones).
2. Pairs on disk: ink 40 (ff.102r-103r reader output, as VIV-ANCHOR used it, tx/vivanchor.py names the files) against the clerk's ink-41
   decipherment (tx/dec_f105v-f108v merged); ink 67 (tx/f201r_rec.tsv, f201v passes) against tx/dec67_norm.txt; ink 70 (f.211r-v passes)
   against tx/dec70_norm.txt. Drop brace nulls as VIV-ANCHOR did. Run each pair separately, then pooled.
3. Known-answer control, run first: the alignment must recover the 14 letters already C in key.tsv (a, c, d, e, g, i, l, n, o, q, r, s,
   t, u) at the same top label with share >= 2/3 for at least 10 of them; a shuffled-decipherment control (the decipherment's lines
   permuted, 20 shuffles) must recover fewer than 4. Gate fails -> non-test, stop, log.
4. After the gate: for p, m, f (and k, x, y, b, h, z) report every label's share and count at the aligned positions, per pair and pooled,
   with the label's own purity (what else it carries). A cell is proposed only at share >= 2/3 and n >= 10 on the pooled stream and
   >= 1/2 on each pair that has n >= 5.
5. Decision (pre-registered): (a) p and/or m cells meet the rule: add them to key.tsv at grade C with the counts (source: this job),
   re-decode with the committed decode scripts (`--check`, rule 7; grades before/after), report ink 63's longest all-H run and rerun
   `tx/err_sim/err_sim.py` on the extended key (seconds) for the reader-error crossover ERR-SIM could not measure; (b) the p or m
   positions scatter across labels with no label above 1/2 -> T1 confirmed for that letter (the readers' labels merge the sign): write
   the aligned positions to tx/kcells/<letter>_positions.tsv (page, line, pos, label) so an exemplar-tile reader can be briefed on those
   exact tiles; no key edit; (c) gate fail -> non-test.
6. "## VIV-KCELLS (17 Oct 2026)" in NOTES.md; RESEARCH.md s.2 (K2), s.4.1 and s.5 updated in place; HYPOTHESES.md row via
   tools/experiment_log.py. Scripts under tx/kcells/. Report: gate numbers, the p/m/f label table, the decision, the new ceiling, five lines.

## JOB CHECK-HAGA (account 4; Sonnet 5; cap USD 4; box 60 minutes; hosts: resources.huygens.knaw.nl, www.nationaalarchief.nl and service.archief.nl (one at a time, >= 1.5 s apart, <= 60 each), github.com (two shallow clones), de-crypt.org listing, web search; Price: vision calls: 2 contact sheets x USD 0.5 = 1.0)

Program C, SCOUT-KEYS row K1 (QUEUE.md "## Key-beside-cipher candidates (17 Oct 2026)", harvest/SCOUT-KEYS-2026-10-17.tsv row K1): Cornelis
Haga, Constantinople, to the States General; NA 1.01.02 inv. 6896 holds a duplicate of his 30 April 1622 letter "met onopgeloste
cijfercode" (Resolutien SG NR 5 p.536, res. 3504a); the 1620 key is DECODE R2118 and Bourdeau read R2113/R2115 with it (targets/haga1620,
credited); Haga sent a NEW code in 1621 (NR 5 p.260, res. 1644a). Job = check-solved per .claude/briefs/check-solved.md, then the material
step, no decode.
1. Create ciphers/haga-sg6896-1622/ with NOTES.md (status word alone on line 1; the edition sentence on line 2 naming what THIS worker
   read: the Resolutien SG NR 5 pages for res. 3504a and 1644a and NR 4 p.482 via resources.huygens.knaw.nl retroboeken, quoted).
2. Six sources: web (four plain searches + the three blogs' comment threads, "## Web and blog check"), print (the Resolutien; Heeringa's
   Bronnen tot de geschiedenis van den Levantschen handel via IA full text if reachable; a print_check phrase run once a clear phrase is
   on disk), DECODE listing (tools/decode_list.py cache: every Haga record, any 1621-1626 one), Bourdeau's haga1620 (what his key covers,
   whether he names 1622), Aymeloglu (grep), Cryptiana. "## Premise check" per the intake brief (the 1620 key vs the 1621 new code: the
   30 Apr 1622 duplicate may be in the new code, which is why it stayed unsolved -- say which, if the resolution or Bourdeau says).
3. Material step only if the verdict is open: find the 30 Apr 1622 duplicate in inv. 6896 through the NA item page's drupal-settings
   JSON and service.archief.nl IIIF (CLAUDE.md host table; ciphers/oldenbarnevelt-brederode-1605/screen_tools/na_fetch.py is the
   pattern): one 700 px contact sheet of the April-June 1622 run (<= 2 sheets, that is the vision line), identify the leaf, fetch its
   native image once into images/ with manifest.json, count cipher lines and whether a decipherment sits beside it. No transcription.
4. Verdict sentence, `tools/intake_gate_check.py haga-sg6896-1622` pasted, the next cheap test named with its price (key application of
   R2118 with a shuffled-key control if the 1620 key; else the 1621 key hunt: NA inv. 12578.1 and the resolution's own words).
Report: verdict, the leaf found or not, the next test and price, five lines.
