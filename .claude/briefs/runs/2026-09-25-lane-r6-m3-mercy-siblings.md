LANE R6 M3 -- espagnol142-mercy-1648: pools first -- find sibling letters under the same code in BnF Espagnol 142 (Sonnet, cap $6, box 50 minutes).
Common: 2026-09-25-lane-r6-common.md. NEAR.md row "espagnol142-mercy-1648", next step (1).
Intake gate (live, 25 Sept 18:52 UTC): "espagnol142-mercy-1648: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
You are this lane's only Gallica fetcher. State: the target is f.22r-v (canvases 58-59) of ark btv1b10035717h (605 canvases, canvas = 2 x folio
+ 14 in this run, NOTES.md Y5); key.tsv (38 values) reads it (M2). Job: (1) read the finding aid (archivesetmanuscrits cc... for Espagnol 142, the
item list with dates; <= 5 requests) and list every item that is ciphered, in Spanish, or addressed to or from Mercy, Castel-Rodrigo, Peñaranda or
the Brussels secretariat 1640-1650; (2) probe those items' canvases at /full/600,/0/ (one at a time, >= 2 s, <= 60 image requests) and keep only
leaves carrying 2-3 digit code groups; (3) for each, fetch native resolution (images/siblings/ with manifest.json, folder under 30 MB),
transcribe the code groups (you, one pass; plus a second pass by ONE blind Sonnet subagent only if the leaf has more than 150 groups), and
apply key.tsv with a script and a random-draw control (same code range, 1000 draws): report per sibling the share of its codes that are in the
38-value set and whether the decode reads as Spanish. A sibling whose codes fall inside the set and read is pooled (siblings.tsv + pooled
ciphertext file); report the pooled N. NOTES.md section "## M3: sibling sweep (25 Sept 2026, LANE R6)". Hosts: gallica.bnf.fr,
archivesetmanuscrits.bnf.fr. ROOM done: "for LANE R6: mercy siblings <k> found, pooled N <n>, key coverage <x>% vs control <c>%". Report what
was found and where it was not found; do not classify novelty.
