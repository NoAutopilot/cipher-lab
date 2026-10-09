# EXHIBIT-2: pick the displays by what the audited reading itself says, then rebuild three (account 4, Opus 5.5, cap USD 12, box 100 min)

Written 9 Oct 2026 22:5x UTC by date -u (clock 22:58) by the orchestrator (account-4), session_012sGNgiddCpz4QUhQsMyoPU, on the owner's
review of EXHIBIT-1 at 22:5x UTC: "we don't want to make stuff up; if it's not interesting, don't act like it's interesting; if it's
genuinely interesting, the interesting bit isn't landing -- perhaps because of the three examples chosen." The orchestrator's diagnosis:
the Gramont display's hook (the divorce suit) belongs to the Montmorency letter, printed in 1688 (N0 key check); our N4 reading there is
the Villandry letter, a courier's note. The display borrowed the printed letter's interest. Parent brief: .claude/briefs/runs/2026-10-09-
account4-exhibit-1.md (its curatorial brief, display anatomy, three-layer lines, image and licence rules, portrait rules all stand);
its output and CURATOR.md are the starting point (research/mockups/exhibit/, build_exhibit.py). Private mock-up only, never docs/.

Step 1, SELECTION (write it first, research/mockups/exhibit/SELECTION.md, before any page): for every status.json result at N3 or
better and D2 or better (not superseded), score one question with evidence quoted: "what does the audited reading itself tell a reader
that is not in print?" -- using the item's depth_sentence and AUDIT.md safe sentence only, never the letter's context. Columns: item,
class, depth, % read, key source, the one thing the reading says (quoted), whether it names people/places/dates, whether the content is
already known from print (then it does not count), a 0-3 interest score with one line of reason, and "thin" where the reading is a
courier note, a salutation or a fragment. Candidates the orchestrator expects to rank high, to be scored not assumed: Orange-August
1561-64 (WVO 53/57, N4 D3, key ours: Maximilian's election, the Queen of Spain, Vendome and Navarre); Manteuffel frame 0391 (N3: Oxford,
Bolingbroke, the Elector and the Queen); Canada 1869 (N3 D3: the restoration plot); Du Vergier (the Jacobite landing plan) if its class
holds; Chavigny-d'Avaux 1640; the Suriname fort map (a cipher legend on a plan: the object itself). Gramont stays only if its own
reading scores; otherwise it is dropped and SELECTION.md says why in one line.
Step 2, BUILD the top three as displays per the parent brief's anatomy, with these changes: the HEADLINE and THE SECRET rest on the
audited reading's own words (the three-layer lines show exactly those words); context (events, faces, map) is labelled context and never
supplies the hook; where a display's reading is modest, the headline says what it is ("a courier's note", "two names an editor could not
read") and claims no more; the "How we know" badges unchanged. Portraits: retry the Commons API once per person with the documented
User-Agent "cipher-lab research script (contact via repository)", 2 s apart, stop at the first 429 and keep placeholders; do not loop.
Gallica not before 10 Oct 00:00 UTC. Output: research/mockups/exhibit-2026-10-09b.html (single file) + per-display pages; the old
exhibit file untouched. Done line "for orchestrator (account-4)": SELECTION.md's top five with scores, the three built, portraits
fetched, what is left; stage by path; never force-push; never AskUserQuestion; never print credentials; no ciphers/ edit.

## Addition (orchestrator, clock 22:59 UTC 9 Oct): portraits are a desk job, not a cloud fetch
The orchestrator's own test at 22:59 UTC: commons.wikimedia.org answers 429 to a compliant User-Agent at two requests two seconds apart --
the shared cloud egress address is throttled. Do NOT call Wikimedia at all. Instead write research/mockups/exhibit/portraits/manifest.tsv
for the three selected displays (person, role in five words, the Commons file title or a search phrase, why that painting, expected
licence PD-Art/PD-old, output filename) and leave labelled placeholders; LOCAL-QUEUE row L73 has the owner's desk runner fetch the files
from the manifest and commit them. Build the pages so that dropping the files into portraits/ with the manifest's filenames fills every
face without a rebuild (the <img> src points at the manifest filename; the placeholder is the CSS fallback).
