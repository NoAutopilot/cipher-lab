LANE R6 Y9 -- berthier-napoleon-1812: full ciphertext from the Vilcoq plate, then the lead classes in order (Sonnet, cap $6, box 50 minutes).
Common: 2026-09-25-lane-r6-common.md.
Intake gate (live, 25 Sept 17:22 UTC): "berthier-napoleon-1812: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
Read NOTES.md in full (CX2-BERT's found-solved test; Bourdeau's napoleon/NOTES.md is quoted there -- credit him, rule 8).
Job: (1) fetch Vilcoq 1969 p.24's plate at the highest resolution Persée serves (the renderIllustration PNG CX2-BERT found; one fetch, keep a
manifest), cut line crops; two passes of the number groups (you A, ONE blind Sonnet subagent B on the crops, TSVs to disk, committed), reconcile,
settle on the image, write ciphertext_full.tsv and compare with the partial ciphertext.txt already on file (report every difference; never
silently repair ciphertext.txt). (2) Lead classes (COMMON item 4), stop at the first that reads: (a) the same letter in print -- test whether
Chuquet 1912 p.440's two clear 22 Dec letters (XIX, XXIII) fit the cryptogram: group count vs syllable/word count, and whether repeated groups
fall where the clear text repeats words (script it; a matched control = the same test against 20 other Chuquet letters of Dec 1812 of similar
length, so a fit means something only if it beats them); (b) a published key of the office: grep a shallow clone of dbourdeau/cyphersolver
(MIT) and sources/cryptiana/ for Napoleon/Berthier 1812 "petit chiffre" tables; apply any with a random-draw control. No free cryptanalysis.
NOTES.md section "## Y9: full ciphertext and crib test (25 Sept 2026, LANE R6)". Hosts: persee.fr (<=10), archive.org, github.com (one clone).
ROOM done: "for LANE R6: berthier <groups> groups, agreement <x>%, crib fit <target> vs control <c>". Report what was found; do not classify novelty.
