# NEWT-C follow-ups (LANE NEWT-C-account-4, written 7 Oct 2026 00:3x UTC by date -u)

Parent: LANE NEWT-C-account-4 (session_01XXcLqsU7GkbYZoN7rPaBzx). Why: two of the six NEWT-C check-solved verdicts
(.claude/briefs/runs/2026-10-07-account4-newtc-checks.md) stopped with their own named next step undone. Each step below is
that worker's own "While waiting"/"Remaining next step" line. Model Sonnet. Cap USD 7, box 60 min from your own `date -u`; the box
is a minimum (README common tail): the wave-2 workers stopped after 6-10 minutes with steps undone -- do not. Stop at 80% of either.
Units: up to 6 Gallica volumes or leaves anchored, ~1 USD each (S4 scout and NC-CROI ledger rows), plus one look per leaf.
No transcription, no key application to a target leaf, no cryptanalysis, no DECODE login, no paid orders. Gallica: >=1.5 s apart,
low-res IIIF (`full/700,/0/default.jpg`), one look each; `tools/gallica_folio.py ARK --anchor canvas=folio` for unlabelled manifests.

## Jobs

| job | target folder (exists) | step |
|---|---|---|
| NC-CROI2 | colbert-croissy-london-1668-74 | The verdict `found-solved` covers 25 of 72 folios (DECODE Decrypted); 47 residue folios have no reading located anywhere (NOTES.md "Residue"). Classify each residue folio, volume by volume (Colbert 149, 159, 160, 164, 165bis, 166; arks in NOTES.md or via the BnF catalogue), as: (a) copy/duplicate of a Decrypted letter (say which), (b) cipher with a contemporary decipherment on the leaf, (c) cipher with no decipherment (residue proper), (d) not cipher / mislocated. Estimate cipher signs for (c) from the leaf look (lines x groups/line). Then set line 1: `partial` if (c) holds >= 2 letters or >= 1,500 groups, else keep `found-solved`, and say why in one sentence. If `partial`: append "## Remaining gaps" / "## Escalation" (tools/gaps_check.py format; pass it), and write specs/colbert-croissy-london-1668-74.json (follow specs/README.md and specs/rayburn-2004.json): test 1 = `tools/decode_key.py` with ciphers/colbert155-beziers-1670/keys/key_colbert_croissy_1668.tsv on one (b) leaf as known answer (its decipherment = the answer), matched control = the same key on the same leaf's groups shuffled; test 2 = the same key on one (c) letter; judge block fr17 if tools/data has it (check era; CLAUDE.md rule 3). Do NOT run either test. |
| NC-MONL2 | fr4735-monluc-lansac-poland-1573 | NOTES.md "Remaining next step": pull the BnF dépouillement of fr.4735 (archivesetmanuscrits.bnf.fr, items 16-93; page 1 by curl, run twice if paginated), list Monluc's cipher letters with dates, map Tomokiyo's folios (Cipher 1 ff. 84, 87, 132, 136, 138; Cipher 2 f. 209) to canvases by eye-anchors, check each for a marginal decipherment, estimate cipher signs; check Noailles 1867 vol. III by date for each listed Monluc letter; then do the undone check-solved items named in "Not done" (three blog site searches with comment threads; Google Books editor's-note sweep with country=US and the key). Update line 1 (open / partial / found-solved / blocked) per the result. If the residue (unglossed, unprinted Monluc cipher) is >= 1,500 signs or >= 2 letters and the gate exits 0: write specs/fr4735-monluc-lansac-poland-1573.json, test 1 = Tomokiyo's Monluc Cipher 1 table (henryiii.htm; fetch the PNG once, credit) applied to one glossed leaf as known answer vs shuffled control, test 2 = one unglossed leaf. Do NOT run either test. |

## Steps (each worker, its own job only)
0. `python3 tools/room.py --start`; `date -u`; ROOM claim via tools/room.py: "<job> <folder>, cap 7, box end <time>, for LANE NEWT-C-account-4".
1. Read CLAUDE.md, the folder's NOTES.md, .claude/briefs/check-solved.md (for MONL2's undone items).
2. Do the step. Write the results into the folder's NOTES.md as "## <job> (<date>)" with a per-folio/per-letter table.
3. `python3 tools/intake_gate_check.py <folder>`; paste output. If `partial`: `python3 tools/gaps_check.py <folder>`; paste OK.
4. Commit only that folder (and the spec if written) by explicit path; `git fetch origin main && git rebase FETCH_HEAD && git push origin HEAD:main`.
5. ROOM done line via tools/room.py: verdict line 1, counts (a/b/c/d or glossed/unglossed), est. residue signs, spec written or not, gate exit,
   requests per host, "cost: see the lane ledger, for LANE NEWT-C-account-4". Report in five lines; stop.
Never call AskUserQuestion; never print credentials; never name the owner; never the words new, first, novel, solved, cracked for anything this
project did. Report what was found and where it was not found; do not classify novelty.
