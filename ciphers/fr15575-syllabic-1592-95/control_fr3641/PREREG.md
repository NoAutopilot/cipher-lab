# NV05C pre-registration (committed before any pass is read or scored), 3 Oct 2026

Control letter: BnF fr.3641 f.111r (Gallica btv1b52508089f canvas f239, label '111r'), don Diego de Ibarra to Philip II,
Paris, 1 Dec 1592 (Tomokiyo, phelippes.htm no.51: "In the 1592 syllabic numerical cipher. Interlined deciphering.").
Chosen because it is fully interlined on the recto and has a second, cleaned decipherment elsewhere (league.htm no.80).
Scope: line pairs L01-L12 of the body (crops images/f111r_L01..L12_s1-3, region 400,1800,3500,1900), fixed before reading.
The worker looked at line L01 once while checking the crop (saw that 45 16 67 / 73 56 40 / 65:55 read as la co pi / que me ha / par ma);
no other line was read before this file was committed.

Key: ../key_no54.tsv as committed by NV05B (d4a3a4b4), 95 coded syllable rows (codes 10-99); nothing edited.

Tokenisation (fixed now): a run of digits is split into 2-digit codes from the left; an odd final digit is a single-digit
token (header letter sign, not a syllable code). Every non-digit sign (. : n f p x and other letter-shaped signs, clear
3-letter groups such as 'pal', 'xel') is its own token. Only 2-digit tokens whose code has a row in key_no54.tsv are
scored ("scored tokens"). Other tokens decode to one '_' (cannot match) in the alignment.

Normalisation (CLAUDE.md rule 3, PX-BRODEC): both the decoded stream and the clerk's gloss are lower-cased, accents
stripped, letters only, j->i, v->u, y->i. Clerk abbreviations are expanded before scoring by this fixed table only:
'duq'/'duqz' -> duque, 'q'/'q~' (alone) -> que, 'qs' -> ques, 'VM'/'V.M.'/'vm' -> vuestramagestad, 'S.M.'/'sm' -> sumagestad.
Nothing else is expanded or corrected.

Statistic S: per line, the decoded stream (key values in token order) and the normalised gloss of that line are aligned
by longest common subsequence (tools/decode_witness.py lcs_align). A scored token counts as a match when every letter of
its decoded value is in a matched pair. S = matches / scored tokens, pooled over L01-L12.
Secondary (reported, not gated): decode_witness-style letter agreement = LCS matches / gloss letters, pooled per line.

Control: the same S with the key's values shuffled among the 95 coded syllable rows (codes fixed, values permuted),
1000 draws, seed 1. A per-code value permutation changes which syllable each scored token decodes to, so S can differ.

Gate: PASS iff S_real > p99 of the 1000 shuffled S AND S_real >= 0.60. Otherwise FAIL, diagnosed by key row grade (H/M/I),
convention, and key family.

Transcription: 2 blind Sonnet passes of the cipher line tokens (A, B) on the same crops; 1 Sonnet read of the gloss (G);
reconciliation by the worker on the crops (disagreeing tokens only). err_2reader = tokens where A != B / aligned tokens.
