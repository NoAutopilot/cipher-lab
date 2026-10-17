# Research director, first wave (17 Oct 2026, 00:5x UTC by date -u; owner's directive "Build an autonomous research organization")

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/prior_work.py` before a priced step on an item, PREREG with a `## Decision` block before any scored run,
`tools/experiment_log.py --check`). Every job below ends its NOTES section with the six research-director questions answered in one line
each: what we learned; what assumptions it depended on; which remain unverified; alternative explanations; the most informative different
experiment; continue / pivot / acquire / reprioritize. A finished brief is not a finished question: name the next question even when the
answer is "nothing cheap moves this".

## JOB VIV-SYNTH (account 4; Opus 5.5; cap USD 6; box 60 minutes; disk only, no network, no readers, no images; Price: vision calls: 0 x USD 0 = 0)

Flagship: ciphers/fr16104-vivonne-spain-1572 (Saint-Gouard to Charles IX, ink pieces 40-70; ink 63 = the 10 Oct 1573 letter without a
period decipherment, N3/D1). About 45 PREREGs, HYPOTHESES.md and a 3,900-line NOTES.md exist; nobody has written the synthesis. Write
`ciphers/fr16104-vivonne-spain-1572/RESEARCH.md` (the living map the flagship survives on; sections fixed):
1. **Question.** What exactly is unread (pieces without a period decipherment, by Gachard's flags and our own table: which letters, how
   many tokens, which key piece each is in) and what reading each would need.
2. **Hypotheses in play** (one row each, with the evidence line that supports or weakens it, by section/PREREG): key-structure hypotheses
   (is key 63 the same family as 67/70 or 40/41; what VIV-ANCHOR, VIVKEY, VIVFKEY, VIV67/70 established), transcription hypotheses (the
   reader-label alphabet; the g/f split; the s1/s2 overlap; deskew), language and AD convention.
3. **Ruled out, with the number that ruled it out** (retired instruments and why; what is consumed, not retired).
4. **Shared assumptions every experiment rested on**, and whether each has been tested: start with transcription error -- BENCHMARK-TX
   err_true on the KNOWN leaves is 0.185-0.232 (f.102r, f.103r, f.201r, PREREG-SORTER-STEP1-INK63 section 3) against the TRANSCRIPTION.md
   standard of <= 0.05: say plainly whether any ink-63 negative can be read as a negative at that input error, which experiments inherit
   it, and what would falsify "the pipeline cannot read this hand below 10%" (a key-constrained decode on a known leaf; a different
   segmentation; a different feature; the owner's sort is one instrument, not the only one). Then the key-family assumption, the language,
   the AD convention (R 3.4 vs corpus; cite the Mercy ruling DV-MERCY2 for how a verifier applied it).
5. **The three most informative next experiments**, ranked by expected information per USD, each with: the assumption it tests, the
   control, the stop criterion, the cap from the nearest ledger row, and what each outcome would change. At least one must not depend on
   the owner's sort. At least one must be a fundamentally different instrument from the g-split/classifier family.
6. **Recommendation**: continue / pivot / acquire / reprioritize, in one paragraph, with the counterfactual.
Read: NOTES.md (grep by section titles first; read "What the sources say", every "Parent reading", the Remaining gaps and Escalation
tails), HYPOTHESES.md whole, PREREG-*.md Decision blocks (`tools/experiment_log.py --family <instrument>` for each family), AUDIT.md,
BENCHMARK-TX.tsv rows, TRANSCRIPTION.md, LESSONS.md "Settle the alphabet before reading". No new experiment in this job; no reading; no
key edit. Report: the file path and the ranked three experiments in five lines.

## JOB MERCY-CEIL (account 4; Opus 5.5; cap USD 3; box 40 minutes; disk only, no network, no readers, no images; Price: vision calls: 0 x USD 0 = 0)

Production: ciphers/espagnol142-mercy-1648 (N4, our key, D1; 529 tokens, S 501 M 28 after the parent applied DV-MERCY2's 13 positions).
DV-MERCY2 ruled the governing authentication distance is es17c 125.9 letters with liberties recounted; the longest H/C/S stretch is 89
(r20:8-r24:13). Question: is a D2 clause reachable at all by settling the remaining M positions, before anyone pays for readers?
1. From ciphertext.tsv and reading_tokens.tsv (or `tools/decode_key.py ciphers/espagnol142-mercy-1648` output), list every M position
   with its row, cluster and why it is M (DV-MERCY2's table: in-range glued clusters, legibility, sense re-cuts).
2. Compute with `mercym33/runs.py` (scratch copy) the longest stretch under three scenarios: (a) as committed; (b) every M whose
   settlement DV-MERCY2's rule could grant S (companion rule: two gated blind readers reading it identically; out-of-range clusters with
   one parse) taken as settled; (c) every M taken as transcribed (the ceiling). Report the three numbers against 125.9.
3. Decision block in `PREREG-MERCY-CEIL.md` (written before step 2's numbers): if (b) >= 126, name the exact positions whose gated re-read
   would license the clause and the per-pass price from MERCY-IMG's ledger row, as the next job (MERCY-IMG2), and stop; if (b) < 126 and
   (c) >= 126, say which in-range clusters stand in the way and whether any instrument other than sense could cut them (the image at
   native resolution was neutral per MERCY-IMG; name what else: spacing statistics across the whole letter with a control, the writer's
   habit on out-of-range clusters); if (c) < 126, the clause route is closed for this item and D2 needs a different route -- say so.
No reading change, no key edit, no AUDIT.md edit. Report: the three stretch numbers and the decision.

## JOB SCOUT-KEYS (account 2; Opus 5.5; cap USD 10; box 90 minutes; network: one host at a time, >= 1.5 s apart, <= 60 requests per host; Price: vision calls: 0 x USD 0 = 0)

Discovery (program C). The readings this project has counted all came from a key beside the ciphertext: Eckert's period key, Clinton's
1778 key on the Haldimand reel, Gachard's "avec le déchiffrement" flags on Saint-Gouard's volumes, the Brederode marginal note, Tomokiyo's
keys. Find ten more of that shape -- a digitised volume, reel or liasse where cipher letters sit beside period decipherments or a key
sheet, copy-free from the cloud -- and for each the pair "deciphered sibling -> undeciphered letter in the same key". Start where the
shape is already known to exist and extend outward: (1) LAC Haldimand Papers reels on heritage.canadiana.ca beyond H-1649 (the B.147/148
pattern: cipher copy + decipherment pages; list reels and the calendar volumes that flag "in cipher"); (2) BnF fr.16104-16106's
neighbours -- other ambassadors' volumes Gachard (1875, IA labibliothquen02gachuoft, on disk at sources/ if fetched before) flags
"avec le déchiffrement" and "sans le déchiffrement" (the pool map: a volume with both flags is a key-recovery pipeline); (3) NA
Staten-Generaal liassen 1.01.02 inv. 6016-6025 and Lias Duitsland for "ontcijfering"/decipherment pairs beyond Brederode (what
HEID-1621B/J and OBRED-6021 already screened is on disk; do not re-screen it); (4) TNA SP 106 key sheets matched to SP 77/81/84/105
letters by date and office (Discovery API, item details); (5) Royal Archives Georgian/Stuart Papers via gpp.rct.uk CalmView for Gualterio-
era ciphers with decipherments (the HMC vol. VI keys are on disk: keys/hmc6_*.tsv). Run `tools/prior_work.py` on every candidate and
`tools/scout_rubric.py` for the score; drop anything DECODE or the solver repositories list as solved; write the ten as QUEUE.md rows
under "## Key-beside-cipher candidates (17 Oct 2026)" with the exact quoted source line for each flag (RETRO-2026-09-26e). Never
promote, never solve. Report: ten rows (holder, item, key evidence, copy-free yes/no, first cheap test and its price), request counts per
host, what was searched with no hit.

## JOB CASES-TX (account 2; Opus 5.5; cap USD 5; box 60 minutes; disk only, no network; Price: vision calls: 0 x USD 0 = 0)

Owner's test (directive 8.5): for each case where the owner had to point out a mistaken foundational assumption -- at least (a) Debosnys
1883: about 28% reader disagreement run through many machine passes before "settle the alphabet before reading" (LESSONS.md, owner 2 Oct);
(b) fr2933-salviati-1525: controls run at 0-7% injected error while the transcription's own pass-to-pass disagreement was 14.6%
(SALV-DIAG, CLAUDE.md rule 3); (c) espagnol142-mercy-1648: four out-of-range clusters that were two glued codes (1 Oct, decode_key
--split-check) and the 15 Oct image check; (d) fr16104-vivonne-spain-1572: the f.191r deskew re-cut and the sorter decision (VIV-F191,
3 Oct; owner 2-3 Oct); (e) any other case LEDGER.md or learning/INTERVENTIONS.tsv records where the owner caught a transcription or
assumption error -- answer from the DATED evidence (LEDGER rows, NOTES sections, PREREGs, BENCHMARK-TX rows that existed at the time):
was the evidence for an autonomous diagnosis already on disk before the owner spoke? Which check, had it been run, would have shown it
(tx_bench err_true, pass-to-pass disagreement, --split-check, a known-answer leaf, a control at the measured error level)? Write
`learning/ASSUMPTION-CASES-2026-10-17.md`: one table (case, date of the owner's intervention, evidence available before it, the check
that would have caught it, verdict: diagnosable / not diagnosable from the record, cost of the check) and a closing list of the two or
three checks that would have caught most cases, each as a one-line rule that `.claude/briefs/README.md`'s common tail could carry (do
not edit the README; the parent decides). No new experiment. Report: the verdict per case and the two or three checks.
