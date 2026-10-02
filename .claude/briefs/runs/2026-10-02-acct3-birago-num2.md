# BIRAGO-NUM2 (account-3 orchestrator, 2 Oct 2026): read the Nov 1571 numerical key -- cribs first, then a controlled anneal

Targets ciphers/birago-nevers-1571 (f.119) + ciphers/birago-fr3252-1571-72 (f.100r). BIRAGO-NUM (5e7479ad) established:
same key in both letters (21 shared 6-mers vs shuffled max 5; shared 10-mer 1503985803), dots mark two-figure code
groups, phase.py pairs 476 / 64 types; the homophonic family control falls below gate at the measured noise, so a
blind family run is a non-test. Credit Bourdeau (cyphersolver targets/birago, f.119 transcription and exclusions).
Model Opus 5.5. Cap $8, box 70 min. Disk only.
1. Cribs first (cheap, strong): the clear text of both letters and the neighbouring 1571-72 Birago letters name
   Carmagnola, Bellagarda (Bellegarde), Valletta, Savoia, Turino, the Duke, the Queen, Ugonotti. Pre-register (before
   scoring) which cribs to try where: drag each crib over the 476-pair stream of both letters jointly, accept a
   placement only if it is consistent at every repeat in both letters and beats the same crib dragged over a shuffled
   pair stream (200 shuffles). Write accepted pair values to a key file read by decode_key (grade S, crib-backed).
2. If >= 8 pair types are fixed by accepted cribs, run the joint phase+key anneal named by BIRAGO-NUM seeded with them,
   with its own matched control at N=476, K=64 and the measured noise; never report a target number whose control is
   below gate. Otherwise stop after step 1 and write the design note.
3. NOTES both folders, HYPOTHESES rows (both numbers), gaps_check, PROGRESS "Birago numerical (f.119 + f.100)" note.
   English gist of any words read. Report what was found and where it was not found; do not classify novelty.
   Done line "for the account-3 orchestrator".
