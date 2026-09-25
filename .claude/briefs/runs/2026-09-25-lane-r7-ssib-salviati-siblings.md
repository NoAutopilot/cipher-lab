LANE R7 SSIB -- fr2933-salviati-1525: pools-first search for sibling letters in the same invented-sign cipher (Sonnet, cap $4, box 45 minutes).
Common: 2026-09-25-lane-r7-common.md. NEAR.md row "fr2933-salviati-1525". No solving, no transcription beyond a 5-sign shape check.
Intake gate (live, 25 Sept 20:00 UTC): "fr2933-salviati-1525: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
Why: the atlas re-pass (R7-AT55V/AT57V) cut the pooled type count only 223 -> 204-198 against a gate of 178, so the transcription lever is spent;
CM2's own suggestion and the pools-first rule say more observations per type is the next lever. NOTES.md already logs period-key searches
(Meister 1906, Carte Strozziane inventory, Bourdeau's keys, AAV): do not repeat them.
Job:
(1) BnF finding aids (archivesetmanuscrits.bnf.fr, plain POST search, page 1 only per the host table; run twice if paging): "Salviati" with
    "chiffre"/"chiffres"/"en chiffre", 1524-1530, in Français, Dupuy, Béthune, Clairambault, Italien; also "lettre en chiffres" + "italien" for 1524-1528.
    List each hit: shelfmark, folio, date, sender, recipient, digitised (Gallica ark) yes/no.
(2) For each digitised hit (at most 6), fetch ONE reference image at 1600 px (Gallica IIIF, <=20 requests total, >=2 s apart, browser UA) and compare
    five of its cipher signs with glyphs/atlas_part1.png / atlas_part2.png: same invented-sign repertoire (the cursive a, e, g, y, m, w, wd, nt, bh, ch
    forms with superscript marks) or a different design. Record matches only by named sign pairs you can see on both.
(3) Write ciphers/fr2933-salviati-1525/siblings.tsv (shelfmark, folio, date, sender, recipient, ark, design_match yes/no/unclear, signs compared, est.
    sign count) and a short leafnotes/siblings.md. A same-design sibling is a pool lead for the orchestrator; do not transcribe it.
ROOM done: "done: for LANE R7: salviati siblings -- <k> catalogue hits, <d> digitised, <m> same design (est. <n> more signs)".
Hosts: archivesetmanuscrits.bnf.fr (<=30), gallica.bnf.fr (<=20). Report what was found and where it was not found.
