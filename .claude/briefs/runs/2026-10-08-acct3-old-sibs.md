# Oldenbarnevelt 2442 siblings (account-3 orchestrator, 8 Oct 2026 03:5x UTC, on the owner's question "anything more from these
people or this period we could do the same way?"). default-lane common tail; Opus 5.5 orchestrating, Sonnet passes.
Method precedent: ciphers/na-oldenbarnevelt-2442-1605 (blocks B/C1 N3 D2, two audits, key ours: vowels written as digits inside
otherwise clear Spanish, solved with every clear letter fixed as a crib -- scripts/solve_digit_subst.py over tools/homophonic_anneal.py;
matched control solve_digit_subst 100% at N=372/262/95).

## OLD-SIBS (account 4), cap $16, box 120 min: leaves 4, 5, 7 of inv. 2442 (a different letter or letters in the same file, unread)
NOTES.md section 1: leaves 4, 5 and 7 (images/004_*, 005_*, 007_*, on disk, two-page openings) carry heavy letter+digit cipher of
a different correspondence; leaf 7 has clear text naming "la Abadia de Lerma donde el Duque funda ... collegial" and cipher groups
like the target's (orchestrator eye-check of a crop, 8 Oct 03:5x). Scans 9-11 were never fetched.
0. Fetch scans 9-11 once (service.archief.nl, manifest per NOTES access log; >=1.5 s apart); note any cipher. Decide which leaves
   form which letter(s) (folio stamps, hands, salutations, dates) and write a short "## Leaves 4/5/7/9-11" section first. If any
   leaf is a copy of an already-read block (same text as A/B/C1/C2), say so and drop it.
1. Check-solved light (the item is already at stage 2 as one file; for each NEW letter identified, run the premise check: the
   folder's own search log + a phrase search on its clear text in Lonchay & Cuvelier OCR and the Huygens Oldenbarnevelt
   retroboeken) and paste tools/intake_gate_check.py na-oldenbarnevelt-2442-1605.
2. Crops: `python3 tools/iiif_lines.py --image ciphers/na-oldenbarnevelt-2442-1605/images/<leaf>.jpg --out
   ciphers/na-oldenbarnevelt-2442-1605/images/crops_L457 --debug` (paste the command; check the overlay); cipher lines only.
3. Two blind Sonnet passes per leaf on crops only (never the full leaf), then one reconciliation per leaf (Usage 6: price
   ~$1.5 per pass; 3 leaves x 2 passes + 3 reconciliations = 9 units). Split >10% -> record it, do not run a third pass.
4. Solve: first test the B/C1 key (a=4 e=8 i=3 o=7 u=2) as a fixed key; then the free solve (solve_digit_subst.py) with a matched
   control at the leaves' own N, K and noise. Both numbers side by side (rule 3). A different key is a finding, not a failure.
5. Grade per token (H none; S only where the decode is a real word and the image agrees; M otherwise); reading file + decode
   script with --check (rule 7); judge es1600 reported (FAIL allowed, as for B/C1). NOTES.md section per letter.
Stop before a unit that would cross 80% of cap or box. Report what was found and where it was not found; do not classify novelty.
A separate verifier session (queue it as a WORK-QUEUE row for account 2 when you finish) classifies and sets depth under
.claude/briefs/runs/2026-10-08-acct3-depth-bar.md.

## OLD-CAT (account 2), cap $4, box 50 min: more letters of this kind in the Nationaal Archief
The neighbour check (NOTES section 2) read only unittitles of invnrs 2435-2450. Pull the whole finding aid of toegang 3.01.14
once (the Nationaal Archief EAD/open-data export or the item pages' drupal-settings-json; never data.nationaalarchief.nl, which
does not resolve) and grep every description for cijfer/cijferschrift/gecijferd/sleutel/onderschept/Spaans/Spaanse brief, 1595-1619;
then the same for the Staten-Generaal's Spanish/"Lias Spanje" and intercepted-letter series if an export is reachable. For each
hit: invnr, title, scans count, digitised yes/no, a one-crop eye-check of whether it is letter+digit Spanish like 2442. Output
ciphers/na-oldenbarnevelt-2442-1605/siblings_catalogue.tsv + a short NOTES section. No decoding. >=1.5 s per request, <=60 requests.
