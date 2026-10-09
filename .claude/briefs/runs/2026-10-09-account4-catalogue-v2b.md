# CATALOGUE-V2b: three-layer reading lines on the three sample pages of the catalogue mock-up (account 4, Opus 5.5, cap USD 4, box 45 min)

Written 9 Oct 2026 22:44 UTC by date -u by the orchestrator (account-4), session_012sGNgiddCpz4QUhQsMyoPU, from CATALOGUE-SITE-1's own proposal
at 22:44 UTC (it stopped at its cap, correctly refusing to invent a French line for Gramont). Private mock-up only (research/mockups/,
never docs/); parent brief .claude/briefs/runs/2026-10-09-account4-catalogue-site.md with Amendments 1-4 and the three-layer addition.

Job: on research/mockups/catalogue-2026-10-09.html (v2, commit 480eb208f) and the generator tools/build_catalogue.py, render each sample
line in three layers -- the crop; the plain text aligned to the signs with the grade marks; "English (translation, interpretation)" with no
grades. (1) Manteuffel f.410 L13-14 and Lodewijk 5797 p.5/p.7: the own-language layer comes from the folder's reading_tokens /
reading_5797 values as they stand (no new reading); add the English line. (2) Gramont: the Montmorency line fr.3040 f.18r L4 decodes
only to letters with gaps and has no line-level alignment to Le Grand (III pp.454-457); do NOT reconstruct it. Either align that line to
Le Grand's text with tools/interlinear_align.py as a C-grade alignment (commit the alignment file, cite the page, show the result with the
grades it earns) or, if that does not fit the cap, swap the Gramont sample to the Villandry letter fr.2980 f.29r (reading in words, H 532
of 568, crops in images/crops_*) and say so on the page. (3) A line that reads as letters with gaps is shown as such, grade marks only,
no English. Rules unchanged: rule-10 wording, nothing restricted, no internal names or costs, every image with source and licence line;
cvd_check PASS; republish nothing (the orchestrator publishes the file to the owner's private artifact). Done line "for orchestrator
(account-4)"; stage by path; never force-push; never AskUserQuestion; never print credentials; no ciphers/ file edited except a new
alignment file under ciphers/fr2980-gramont/ if (2)'s first option is taken, named in the done line.
