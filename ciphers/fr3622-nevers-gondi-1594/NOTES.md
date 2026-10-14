found-solved
BnF fr.3622, Nevers to M. de Gondi, 27 Mar 1594 (our f.91): deciphered in part by George Lasry ("BnF cipher research", 10 Oct 2026), published in cyphersolver 13 Oct 2026 (targets/nevers1594gondi, commit dde5b0ea): 3/3 pages transcribed in part, key of 54 symbols, 230 of 245 elements identified (93.9%), method "read after matching with key from external sources", extent partial. Snapshot: sources/cyphersolver/2026-10-14-lasry/nevers1594gondi/ (LANE BNF-FOCUS, 14 Oct 2026). Was `open` before 14 Oct.
Gomberville 1665 seconde partie (Gallica bpt6k64451005) views 754-763 (printed pp.691-700, Feb-Apr 1594) read as images by this worker, letter absent; whole-volume ContentSearch Veze 0 hits, Gondy hits all other contexts.

# Nevers to M. de Gondy, "De Veze", 27 March 1594 -- BnF Français 3622 no.45, fol. 91

Job BNF-Q13-CS for LANE BNF-FOCUS (account 2), 8 Oct 2026 (status then `blocked`; superseded by BNF-GOMB below), not a negative.
BnF notice (cc50072k/cc504266 listing): "Lettre, avec chiffre, de L[ODOVICO] G[ONZAGA, duc DE NEVERS] ... à Mr de Gondy ... De Veze, ce XXVIIe mars 1594." No decipherment flag. Same period, other Nevers cipher letters of March 1594 exist (no.76 to Revol 12 Mar, in the fr.3989 folder).

## Leaf look (Gallica btv1b9058938q, canvas 100 = f.90v/91r, 900 px)
Right page numbered 91: French letter, "Monsieur de Gondy ...", with about five lines of symbol/numeral cipher embedded in the body (a mid-page block of ~6 lines plus shorter runs), clear French around it. Left page is the address/endorsement leaf (show-through). No interlinear decipherment, no clear copy at 900 px. Mixed clear + embedded symbol cipher, short: probably a nomenclator-style use; key unknown (Nevers office key no.60 untested here; KEYHUNT-2026-10-07.tsv lists no.60 for neighbouring Nevers letters of 1593-94, not this one).

## Prior-art search (8 Oct 2026)
Bourdeau: no hit Gondi/Gondy 3622. Tomokiyo nevers.htm: Gondy to Nevers letters in fr.3983/3986/3988 only, not this one. Desenclos and Lasry 2024: Henri IV 1592 only. WebSearch (Nevers Gondy 27 mars 1594 Veze): nothing on the letter.

## Web and blog check (BNF-Q13-CS, 8 Oct 2026)
Query "Nevers Gondy 27 mars 1594 Veze lettre chiffre Français 3622": no hit. Blog site searches not run individually.

## Premise check (BNF-Q13-CS, 8 Oct 2026)
(a) none: not found. (b) fr3985-3989 key work: not checked against this letter: not found. (c) f.90v-91r viewed at 900 px: no gloss, not found. (d) Gondy-side editions: unreached.

## While waiting
Run the sibling Nevers key (tools/keys/key60.tsv) against the f.91 symbols as a known-key test only after a transcription; first action: crop with tools/iiif_lines.py (canvas 100).

## BNF-GOMB (8 Oct 2026, account 2)
Edition: Gomberville 1665 seconde partie, Gallica bpt6k64451005. ContentSearch whole volume: Veze 0, Veze(acute) 0, Beze 0; Gondy/Gondi 7 hits at views 395, 475, 516, 559, 668, 669, 853 (snippets: Cardinal de Gondy in 1590/1593 Rome and Ligue contexts, none a Nevers letter of 27 Mar 1594); "1594" 11 hits (views 15, 471, 482, 538, 540, 554, 754, 755, 758, 767, 773).
Images read: views 754-763 (printed pp.691-700): Arret of Parlement 30 Mar 1594, Plaisance-La Chastre letters, Orleans 27 Jan 1594, Lyon reduction 7-9 Feb 1594, a Huguenot writ to the king. No Nevers letter to Gondy, clear or deciphered, in the Feb-Apr 1594 block. Views 764-773 (to Aug 1594) not read as images; OCR name hits there: none for Gondy.
Premise (d): Gondy-side edition not located; Gomberville is Nevers's own side. Premise (a)-(c) unchanged from BNF-Q13-CS.
Gallica requests this job: about 39 incl. 1 reset+1 retry.

## Gate
```
ciphers/fr3622-nevers-gondi-1594: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## BNF-G41 (8 Oct 2026, account 2, first cheap test)
Gate on fr.3983 f.178 passed in modified form (ITERATE.md: real -1.40 vs shuffled max -1.59, rank 0/200, both passes). Target f.91 (canvas 100 of btv1b9058938q, native 8004x6167, `images/f91/f100_native.jpg`): the cipher lines (about 5, mid-page) are written in a symbol alphabet, not in digits, so key no.41 (numeric codes) has no entry for them; target decode not run, `decode_key.py --check` n/a (no reading). Grades for a reading: none (0 H, 0 C, 0 S tokens on f.91). Where it was not found: no.41 does not read f.91's glyphs. Calls made: 4 Sonnet blind passes (key A/B, gate digits A/B), no reconciliation call for the gate digits (the gate used both passes separately). Requests: Gallica 11 (manifest cached earlier, canvases 150/151/306-310 thumbnails, f151/f310/f100 native).

## BNF-G60E, f.91 under the G60D instrument (8 Oct 2026)
Key no.60: Bourdeau's transcription (fr3986 key.tsv, CC BY 4.0), credit D. Bourdeau; numbering S. Tomokiyo. Crops: image `images/f91/block.jpg`
cut by hand into sloped bands (`images/f91/v2/`; the tool's default cut `images/f91/f91_L0*` truncated the right-hand ends and its
passes were discarded). Gallica IIIF returned HTTP 500 twice, a local copy was used. Result (numbers only, registered rule, no classification):
N=134 tags, (a) -1.344 vs p95 -1.403 / p99 -1.272, (b) 0.870 vs p99 0.844 (rank 198/200); pass agreement 0.65. Per-token grades (H = in key and both passes agree;
M otherwise; U = tag not in key): H 75, M 35, U 24; no H/C period reading, so this is a cryptanalytic result at most. Viterbi text is a draft
(`scripts/g60e_result.txt`), no translation claim. No reading file written, so decode_key.py --check not applicable. Verifier next.

## Robustness check (BNF-G60R)

8 Oct 2026, account 2, independent Opus session for LANE BNF-FOCUS (did not see G60E's reasoning before the numbers).
Script `scripts/g60r_robust.py` (instrument `scripts/g60d_instrument.py` unchanged), output `scripts/g60r_result.txt`.

- Re-derivation: real (a) 4-gram -1.344, (b) word cover 0.870 -- reproduces G60E to 3 dp (135 tokens read, 110 keyed).
- Null A, 1000 class-preserving shuffled keys (seed 7001): (a) p99 -1.308, 21/1000 at or above real; (b) p99 0.847, 4/1000 at or above real.
- Null B, shuffled target (rule 3, ARM-C1), 200 permutations of tag order (seed 7002), real key: (a) p95 -1.217, p99 -1.194, 63.0% at or above real; (b) p95 0.892, p99 0.916, 16.5% above real.
- Registered verdict: **does not hold.** Real (b) clears Null A but not Null B (0.870 < p99 0.916; 16.5% >= 5%). The word cover comes from no.60's word and syllable values (la, de, les, et, bien, nostre) on any ordering of these tags; the real order of f.91 is no better than a random order under this key. Not a negative of no.60 on f.91 either: this instrument cannot decide at N=135 (rule 3 non-test). Step 5 (depth) not run, per the brief.
- Agreement with G60E: G60E's own row already flagged the thin margin and asked for the shuffled-target decode; that check fails, so "no.60 fits f.91" should not go to a verifier on these numbers. A discriminating test needs an order-sensitive statistic (e.g. a run of readable clause) or more ciphertext.

## BNF-K60 (13 Oct 2026, account 2)
Intake gate before B: `python3 tools/intake_gate_check.py fr3622-nevers-gondi-1594` -> "open (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0.

**A. Key sync.** `ciphers/fr3986-nevers-revol-1593/key.tsv` brought to D. Bourdeau's key60.txt/decode60.py @c60e6dd (cyphersolver, 12 Oct 2026; corrections from issue #32 by R. Weglarek, checked by D. Bourdeau on the fr.3995 images; text CC BY 4.0, numbering S. Tomokiyo). Changed 3 (`++` u -> u|i|d M; `2+` p|i -> u|i M; `4+` bien -> i|bien M, since our tags do not separate his shapes), added 2 (`n+` = p H, `ls+` = l H), 7 checked unchanged, 14 of his shapes unmapped (no tag in sign_guide.md: o–, –o–, –o, o–o, c~, ·x, ‡o, ♀, ⱶⱶ, ɱ, Δ|, \, ∩, 8++), not guessed. Log: `ciphers/fr3986-nevers-revol-1593/key_changes_c60e6dd.tsv`.
Rule 7: `decode_key.py ciphers/fr3986-nevers-revol-1593 --check` and `ciphers/fr3987-nevers-revol-1593 --check` both "reading up to date" (fr3986 ciphertext.tsv carries none of the changed tags). Readers of this key.tsv in this folder: `scripts/g60c_control.py`, `g60d_instrument.py` (and g60e/g60r over it) -- committed outputs g60e_result.txt/g60r_result.txt were made under the old key; f.91 carries one changed tag (L02 `4+`), no regen script exists, not re-generated. Not read from this key.tsv and so not synced (follow-ups for their owners): `ciphers/fr3987-nevers-revol-1593/key.tsv` (own copy; its ciphertext has ++ x1, 2+ x2, 4+ x6), `tools/keys/key60.tsv` (fr3986 v2 job: ++ x2; fr3990 decode). matignon-mayenne-1586 only cites the path in NOTES.md; it does not decode with it.

**B. Order-sensitive test** (PREREG-K60.md, committed b8b88694 before any score; `scripts/k60_order_test.py`, outputs `scripts/k60_negative.txt`, `k60_control.txt`, `k60_target.txt`). Shape ported from Bourdeau's `targets/nevers1593/f88/shuffle_control.py` (MIT).
- Negative control (200 random tag strings, f.91 frequencies): false positives 0/200.
- Positive control (N=135, 18% unkeyed, held-out lexicon file), power at p <= 0.01: 0% 0.390, 15% 0.085, 25% 0.055, 35% 0.015.
- Target L02-L05 (134 tokens, 110 keyed): S = 7 (`+ c` = nostre + s|a, "nostres", L05), 899/5000 shuffles >= 7, p = 0.180.
- Verdict (registered): **non-test (control power 0.015 at 35%)**. Not a negative of no.60 on f.91; nothing graded (0 H, 0 C, 0 S on f.91; the run is M at most).
- Where it was not found: no order-dependent word longer than the shuffles' typical 6-7 letters under the corrected key.
Requests this job: github.com (cyphersolver clone/fetch) 3; Gallica 0; BnF hosts 0.
Status unchanged: open. Next: more no.60 ciphertext of the same office and month to pool (ITERATE.md "Next best attempt").


## Found solved elsewhere (LANE BNF-FOCUS, 14 Oct 2026 06:3x UTC by date -u)
BnF fr.3622, Nevers to M. de Gondi, 27 Mar 1594 (our f.91) is deciphered in part by George Lasry ("BnF cipher research", 10 Oct 2026), published in cyphersolver 13 Oct 2026 (targets/nevers1594gondi, commit dde5b0ea): 3/3 pages transcribed in part, key of 54 symbols, 230 of 245 elements identified (93.9%), method "read after matching with key from external sources", extent partial. The lane found it at the daily re-screen of Bourdeau's repository at HEAD b0af20a (14 Oct). Our work on this item stops here: no further transcription, key test or ASKS row. What we have on disk (transcriptions, key blocks, sorter, controls) stays as a record; any comparison with his reading is a separate, later job and is not run by this lane. Credit: George Lasry (result), D. Bourdeau (publication; text CC BY 4.0), S. Tomokiyo (key numbering).
