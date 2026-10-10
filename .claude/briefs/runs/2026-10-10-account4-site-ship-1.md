# SITE-SHIP-1: one private preview site -- exhibit front door, full catalogue behind it, real navigation (account 4, Opus 5.5, cap USD 12, box 120 min)

Written 10 Oct 2026 01:1x UTC by date -u by the orchestrator (account-4), session_012sGNgiddCpz4QUhQsMyoPU, on the owner's words at
01:0x UTC: "I think the site is sufficient as is. Let us ship the rest, along with useful navigation." The two mock-ups he approved:
research/mockups/exhibit-2026-10-09b.html (EXHIBIT-2: three displays, research/mockups/exhibit/build_exhibit2.py, CURATOR.md,
SELECTION.md) and research/mockups/catalogue-2026-10-09.html (CATALOGUE-SITE-1 v3 + CATALOGUE-V2b: tools/build_catalogue.py, 164 item
pages under research/mockups/catalogue/). Read both briefs (.claude/briefs/runs/2026-10-09-account4-exhibit-1.md, -exhibit-2.md,
-catalogue-site.md with its Amendments, -catalogue-v2b.md) before touching anything: every rule there stands (private only, never docs/,
rule-10 wording, "we don't make stuff up", three-layer reading lines, image and licence rules, portraits from the manifest only, no
Wikimedia calls, no network except what the catalogue builder already fetches from disk).

"Ship the rest" = every audited item, not only the three displays, in ONE site under research/mockups/site/ built by ONE script
(research/mockups/site/build_site.py, which imports or calls the two existing builders rather than copying their code; a tools/tests/
test_build_site.py that builds into a temp dir and checks every internal link resolves, exit 0). Still a private mock-up: the owner
decides later whether and where it goes public; the script refuses any --out under docs/ like build_catalogue.py does.

Structure and navigation (the owner's one ask):
1. Front door = the exhibit index (the three displays, each with its three-layer lines), then "All readings" below the fold.
2. Every page carries the same top bar: Exhibit | All readings | By century | By archive | By language | How to read | Credits;
   a breadcrumb (Home > All readings > <item>); on item pages prev/next in the catalogue order and a "Back to the display" link where the
   item belongs to one of the three displays; on display pages a "See the evidence" link to each item page it rests on.
3. "All readings" = the catalogue index as it is (counts by class, one row per item) plus a client-side filter box (plain JS, no
   library) over sender, recipient, year, archive, language, class and depth -- the data is already in the rows.
4. Three browse pages generated from status.json fields: by century, by holding archive, by language; each a list of item links with the
   one-line "what the reading says" from SELECTION.md where it exists, else the depth_sentence.
5. Portraits: placeholders as EXHIBIT-2 left them, filled from research/mockups/exhibit/portraits/ when the desk runner drops files (L73).
6. A sitemap.html listing every page, and a footer line on every page: "Private preview, <date -u>. Readings graded per CLAUDE.md rule 4;
   novelty classes per rule 10 (verifier's verdict). Nothing here is called first, new or unpublished." (rule 10 wording; a class N4 item
   may say "no prior decipherment located", nothing stronger.)

Outputs: research/mockups/site/ (index.html, exhibit/, items/, browse/, how-to-read.html, credits.html, sitemap.html, assets/), the
build script and its test, and ONE self-contained preview file research/mockups/site-2026-10-10.html (the front door with the three
displays and the All-readings index inline, item pages linked relatively) -- the orchestrator publishes the whole folder as a private
multi-file artifact, so keep paths relative, no leading slash, total under 16 MB (shrink images as build_catalogue.py does). Run
tools/restricted_guard.py --outgoing and tools/file_shrink_guard.py on every touched path before the final push; paste both lines.
Done line "for orchestrator (account-4)" with: page count, link-check result, size, what is still placeholder; cost by get_session is the
orchestrator's. Stage by path; never force-push; never AskUserQuestion; never print credentials; ROOM claim before the first write.
