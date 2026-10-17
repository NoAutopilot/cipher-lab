# Research director, wave 6 (17 Oct 2026, 05:3x UTC by date -u): the ink 67/70 tiles; program C moves to Aitzema

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, PREREG with a `## Decision` block pushed before any scored run, `tools/experiment_log.py --check`). Each job ends
its NOTES section with the six research-director questions in one line each. Report what was found and where it was not found; no
novelty class (rule 10).

## JOB VIV-TILES6770 (account 4; Opus 5.5; cap USD 6; box 45 minutes; hosts: openapi.bnf.fr / gallica.bnf.fr only, <= 8 image requests, >= 1.5 s apart; Price: vision calls: 2 x USD 1.3 = 2.6)

Flagship ciphers/fr16104-vivonne-spain-1572. VIV-KSPLIT (NOTES "## VIV-KSPLIT (17 Oct 2026)") could not run the model split: the 95
packet rows with crops gave 36 usable tiles and only 3 contrast tiles, because the 120 packet rows on inks 67 and 70 (ff.201r-v, 211r-v of
fr.16105; 44 of them contrast tiles) have no line crops on disk. images/ is already 39 MB (over the 30 MB line), so no new page images or
line crops are committed: regenerate them into a scratch directory and commit only the small tiles.
1. Regenerate the four leaves' line crops with the exact `tools/iiif_lines.py` commands recorded in images/manifest.json for c206_f201r
   (and the f.201v, f.211r, f.211v entries; `--ark btv1b9009663p --iiif-host openapi`, regions as recorded), output under a scratch
   directory outside the repository; <= 8 requests. Check the debug overlay before cutting (Usage 8).
2. Re-run tx/ksplit/tiles.py on the packet rows for inks 67 and 70 against those crops (extend the label-aware map to those leaves with
   their own reader outputs tx/f201r_rec.tsv etc.; the f.102r/f.103r atlas does not cover them -- say what you used). Box check by eye
   on one contact sheet per label (reader labels only, the clerk letter never on the sheet; that is the vision line). Write
   tx/ksplit/tiles_6770.tsv, append to truth.tsv (clerk letter), tiles under tx/ksplit/tiles/ (PNG, small). Target: >= 30 usable tiles
   for label c with >= 15 contrast (e/q), and label 2 with its u contrast tiles.
3. No model read in this job and no sorter change (the owner's page stays as published). Report the counts per label and contrast,
   and whether VIV-KSPLIT's model read (8 calls at most) can now run; "## VIV-TILES6770 (17 Oct 2026)" in NOTES.md; RESEARCH.md s.5
   one line. Report: tiles per label and contrast per leaf, the read go/no-go, five lines.

## JOB CHECK-AITZEMA (account 4; Sonnet 5; cap USD 5; box 45 minutes; hosts: resources.huygens.knaw.nl (the cited pages and one search per term, not whole volumes), www.nationaalarchief.nl (the item page only), github.com (two shallow clones), de-crypt.org listing, web search; Price: vision calls: 0 x USD 0 = 0)

Program C, SCOUT-KEYS row K2 (harvest/SCOUT-KEYS-2026-10-17.tsv): Foppe van Aitzema, agent at the Hanse towns, to the States General,
NA 1.01.02 inv. 6025 "Liassen Agent Aitzema" (1617-1625, 589 scans, digitised). Key evidence: the griffier filed Aitzema's own code
(Resolutien SG NR 3 res. 1178, p.188, July 1617); letters read "ontcijferd" on 5 Dec 1617 (res. 1789, p.289), 6 Jan 1618 (res. 1923,
p.307), Feb 1618 (res. 2305 + note a, p.351: orig. dd. Lubeck 17 Feb 1618 in inv. 6025). Job = check-solved per
.claude/briefs/check-solved.md only (no leaf hunt: CHECK-HAGA ran 1.41x its cap by doing both). Lesson of HAGA-LEAF/LEAF2: the lias
interleaves correspondents, so no date projection; this job locates nothing, it only establishes status and the premise.
1. Create ciphers/aitzema-sg6025-1618/ with NOTES.md (status word alone on line 1; line 2 the edition sentence naming the Resolutien
   pages THIS worker read via retroboeken, quoted).
2. Six sources: web (four plain searches + the three blogs' comment threads, "## Web and blog check"), print (the four cited Resolutien
   pages and one retroboeken search each for "Aitzema" + "cijfer"/"ontcijfer"; Rowen or any edition of Aitzema's letters if a web
   search names one), DECODE listing (cache), Bourdeau (grep for aitzema), Aymeloglu (grep), Cryptiana (grep). "## Premise check": is the
   code the griffier filed in 1617 extant (inv. 12578.1 key leaf, or elsewhere), and which letters are cited as deciphered (those are
   the known-plaintext pairs; the undeciphered ones are the targets).
3. Verdict sentence, `tools/intake_gate_check.py aitzema-sg6025-1618` pasted, and the next cheap test named with its price (a contact
   sheet of inv. 6025 for cipher lines, or the key leaf first). No images fetched in this job.
Report: verdict, the deciphered-letter list, the next test and price, five lines.
