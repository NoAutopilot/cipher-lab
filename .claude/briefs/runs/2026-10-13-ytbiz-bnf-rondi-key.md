# BNF-RONDI-KEY (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: transcribe the period partial key blocks on BnF fr.3995 fol.62v-63r (Gallica ark btv1b525085665; canvases f127, f128)
into key files for `ciphers/fr3613-rondinelli-1590` (Hercole Rondinelli to the duc de Nevers, Paris, 11 Nov 1590, fr.3613
f.62r; status open, intake gate exit 0). Nothing else: no transcription of f.62, no decode.
Why: BNF-RONDI3 found on fol.63r a block headed "Rondinelli al S. D. [?] Fiorenza di parigi" with a letter-to-sign list
(a 8, b 7, c 6, d 5, e 3, f m ...) and the French rule "les voyelles s'escrivent dessus les consonantes", matching f.62's
layout by eye (M). Tomokiyo (sources/cryptiana/web/nevers.htm): no.32 (fol.62v) "partial reconstruction of substitution cipher
mainly by figures with some diacritics", Italian annotation "Rafaello"?, "fiorenza", "di parigi"; no.33 (fol.63r) "partial
reconstruction of substitution cipher by figures", "luigi", "fiorenza", "di parigi"; no.34 (fol.63r) "Partial reconstruction of
no.47 ... Notes in French explain vowel indicators placed over a substitution letter, with an example 'di parigi'". These look
like a period decipherer's working keys for Florentine correspondents in Paris; which block belongs to f.62 is the question.

Cap USD 3.5, box 75 min; stop before a unit that would cross 80% of either. Units (per call): fetch + crop (~0.3); TWO blind
Sonnet passes over the crops of all blocks (~0.6 each) + one reconciliation call (~0.6); write-up (~0.5). Model: Sonnet.

Read first: CLAUDE.md (rules 2, 4, 6, 8; Usage 6 crop paragraph), TRANSCRIPTION.md, the folder's NOTES.md (BNF-RONDI3 table
section; images/tables/ already holds 1600 px views of f126-f128 -- use them for orientation only), last 30 lines of ROOM.md.

Route: native images via `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b525085665/f<N>/full/max/0/default.jpg` for
f127 and f128 only (2 requests, 3 s apart; never gallica.bnf.fr). Crops (JPEG) under `images/tables/crops/`; keep the folder
under 30 MB (delete the natives after cropping, keep their URLs in images/tables/manifest.json).

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap.
2. Crop step, mandatory and pasted before any subagent call (`tools/iiif_lines.py --image <native> --out <dir> --debug`, one
   region per block); subagents get only crops plus a short neutral sign-description convention you write first
   (`sign_guide.md`: how to name a figure, a figure with a mark, a letter-like sign, a vowel mark above).
3. Per block, a key file in `keys/`: `block_no32.tsv`, `block_no33.tsv`, `block_no34.tsv` -- columns plain, sign, grade
   (H only where both blind passes and the reconciliation agree; M otherwise), source "BnF fr.3995 f.63r, period partial key
   (numbering Tomokiyo no.34)". Vowel-mark rules and every annotation (Italian and French) verbatim with grades in
   `keys/blocks_rules.md`, with the "di parigi" example sign by sign.
4. NOTES.md section "## BNF-RONDI-KEY (13 Oct 2026, account 2)": rows per block, H share, which plain letters are missing, the
   block whose heading names Rondinelli, and an eye comparison (M) of each block's sign shapes with f.62's (from the BNF-Q13-CS
   / RONDI3 images on disk). Recommend which block a decode should use, with the reason. No decoding.
5. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM done line
   "for LANE BNF-FOCUS (account 2)": blocks, rows, H share, the recommended block, requests per host.

Do not decode; do not classify novelty (rule 10). Never print credentials. Never the words solved, cracked, novel, first, new
for anything this project did. Never call AskUserQuestion. If `tools/room.py --start` fails to push from a detached HEAD:
`git push origin HEAD:main; git checkout -B main HEAD`.
