# Research director, wave 60 (3 Nov 2026, 05:3x UTC by date -u): fr3987 premise check (the gate's last missing section)

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Owner's directive 3 Nov 2026: all purchases on hold -- free routes
only. Stop before starting any unit that would cross 80% of the box or the cap. Intake gate as run by the parent at 05:2x UTC 3 Nov:
`fr3987-nevers-revol-1593: open (line 1) passes the citation and web/blog checks but has no '## Premise check' section -- run check-solved.md's adversarial Premise check (mentioned decipherments opened, other solvers' working files, neighbouring leaves, recipient-side editions) before any first test`
-- the citation and web/blog checks pass; only the premise check is missing. This job writes it and nothing else.

## JOB PREMISE-3987 (account 4; Sonnet 5; cap USD 3; box 40 minutes; hosts: openapi.bnf.fr / gallica.bnf.fr at most 8 requests, github.com (solver repositories, grep) at most 6, archive.org at most 4, >= 1.5 s apart; Price: vision calls: 3 x USD 0.30 = 0.90)

Target ciphers/fr3987-nevers-revol-1593 (status open; BnF fr.3987 f.66 = canvas 121 per NOTES.md, Revol / Nevers correspondence,
10 Nov 1593, key no.60). Read .claude/briefs/check-solved.md "## Premise check" (the (a)-(d) list, 2 Oct 2026) and the folder's
NOTES.md head, "## Item" or equivalent, the "## Web and blog check" section and the two parent-notes blocks. Your stance is the
verifier's moved forward: try to PROVE the leaf is already read.
(a) The folder's own mentions: grep NOTES.md, HYPOTHESES.md and the PREREG files for every mention of a decipherment, gloss,
    interlinear, clear copy, "dechiffrement", "en clair", "Tomokiyo gives", "attached"; open each referenced thing that is on disk
    and say what it is. Record found / not found.
(b) Other solvers' working files for THIS leaf: in dbourdeau/cyphersolver grep for fr.3987, f.66, "Revol", "nevers1593",
    "key60" and open any file that renders or decodes this leaf (not status lists); aaymeloglu/unsolved-ciphers likewise (cite, do
    not copy code). Say whether key no.60 has already been applied by anyone to f.66's text.
(c) The physical neighbours at native resolution: canvases 119, 120, 122, 123 of the fr.3987 ark named in NOTES.md and the facing
    page of canvas 121 itself, fetched once each with tools/iiif_lines.py --ark/--canvas (or the recorded native URL form) at a
    size that shows a clerk's hand, looked at by you (3 vision calls at most: the two neighbours on each side as one look each,
    the facing page as one), for a clear copy, a decipherment, a slip pasted or laid in, or interlinear words above runs. Record
    what each canvas is (a different letter, a blank, a continuation) as a TSV-style list of 5 rows (one per canvas): canvas, folio,
    what it holds, cipher present, clear copy present.
(d) The recipient's side: the Nevers papers' printed editions and the Revol side (French diplomatic editions for 1593, Lettres
    missives de Henri IV, Mémoires de la Ligue vols 5-6 already read per NOTES.md -- cite that, do not re-read), one archive.org
    advancedsearch and one full-text check each at most.
Write "## Premise check (PREMISE-3987, 3 Nov 2026)" in NOTES.md directly after the Web and blog check section, with (a)-(d) each as
found / not found / unreachable and the evidence, then paste `python3 tools/intake_gate_check.py fr3987-nevers-revol-1593` (it must
exit 0; if it still fails, paste the message and stop). A find makes the item calibration or found-solved before any pass runs: set
the head accordingly and stop. Also write "## While waiting" if the head ends up blocked. file_shrink_guard, commit, push.
Report: five lines ((a), (b), (c) neighbour listing, (d), gate output).
