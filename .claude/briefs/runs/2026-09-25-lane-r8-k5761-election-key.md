LANE R8 K5761 -- BnF Français 5761 item 3, "Chiffres desquelz l'on a usé durant le voiage d'Allemagne" (1519 election embassy key):
intake gate repair and sign inventory (Sonnet, cap $4, box 40 minutes; disk only -- the seven leaf images f104-f110 are already in
ciphers/fr5761-election-1519/images; archive.org full-text search and general web search allowed; no Gallica, no subagents).
Authority: LANE R8 brief job 2; CLAUDE.md Pipeline 2 intake gate (RETRO-2026-09-25h proposal 4). Common: 2026-09-25-lane-r8-common.md.
Live gate (25 Sept 22:22 UTC): "fr5761-election-1519: open (line 1) with no standard-edition citation (page number or full-text-search phrase)
within 6 lines -- CLAUDE.md's Pipeline intake gate says this must read `blocked` instead" (exit 1).
Job:
(1) The folder already carries a six-source check-solved (NOTES "Check-solved sweep (24 September 2026)", Mignet 1886 vol.1). Re-verify the
    edition citation (open Mignet on archive.org, give the page) and add Desjardins' and any 1519-election document edition you can open
    (e.g. Le Glay, Négociations diplomatiques entre la France et l'Autriche, 1845, for 1519); Tomokiyo (sources/cryptiana/ first); both
    solver repos (grep). Rewrite NOTES lines 1-6 so the status word has the edition and page within 6 lines; run
    `python3 tools/intake_gate_check.py fr5761-election-1519` and paste the output (exit 0, or `blocked` honestly if the edition cannot be read).
(2) Sign inventory from key.tsv, key_pass*.tsv and the images: per correspondent block (f104 Cordier/La Motheaugroing, f110 Bourdeaulx, and
    each of f105-f109), the number of alphabet signs, code/name signs, nulls, and whether blocks share signs. One table, sign_inventory.tsv,
    and a NOTES section "## Sign inventory (25 Sept 2026, LANE R8)". State the design class (per-correspondent substitution alphabet + small
    nomenclator, or other).
(3) Pools: grep QUEUE.md, CATALOG.md, sources/solver-diffs/*.tsv and ciphers/*/NOTES.md for any catalogued cipher letter of 1519-1520 from the
    named correspondents (Bonnivet, d'Orval, Guillart, Cordier, La Motheaugroing, Bourdeaulx, Joachim de Moltzau). If a candidate
    ciphertext is on disk or catalogued, post "for the parent: fr5761 key <n> signs; candidate letter <shelfmark>" in ROOM and stop.
Do not decode or apply the key. ROOM done: "done: for LANE R8: fr5761-election-1519 gate <exit>, <n> blocks, <signs> signs, pool <none|shelfmark>",
requests per host.
