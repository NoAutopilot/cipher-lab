# Checklist for comparing this key with the Brussels register (H17, ASKS 82)

Written 28 Sept 2026 by campaign step H32 (runner session_01K2B2cTCwujqmMqmGYyE6BY) from measurements already in
NOTES.md. Everything here is a feature of `key.tsv` as recovered by cryptanalysis (key `ours`); none is from a period
key. Use it when the Brussels SEE "chiffres 1647-98" register (AGR, Secretairerie d'Etat et de Guerre inv.nr. 2;
DECODE 958-965) or any sibling key is in hand: each line is a yes/no check against the register's own table.

## Design (H2, H16, H21)
- Letters are numbers 2-34; each vowel has three homophones, each consonant one code:
  a 10 (39 occurrences) / 17 (18) / 34 (9); e 18 (57) / 19 (25) / 33 (3); i 31 (11) / 21 (8) / 26 (6);
  o 2 (20) / 29 (8) / 23 (5); u 8 (24) / 27 (4) / 25 (5, M). Check: does the register give the vowels exactly these
  three numbers each, and consonants one each (b 12, c 14, d 16, f 20, g 22, h 24, l 28, m 30, n 32, p 3, q 4, r 5,
  s 6, t 7, y 13, u-consonant as u)?
- Codes 9 (q?), 15 (n?), 25 (u?), 48 (d?), 52 (y?), 65 (s?), 72 (z?) are graded M: a register value decides each.
  48/52/65/72 lie above the letter range (a small numeric nomenclature, H2); H5 and H31 found no local sign that they
  are word codes rather than letters, at low power.
- A boxed numeral **101** (two occurrences: "de la duquesa de Cheureuse y del [101]", "que el [101] uenga con uos")
  is a name-code class (H2). H29: Saint-Ibal and the duke of Lorraine both fit both contexts; the register decides.
- A corrected fraction-like group 14/19 ([MARK:frac], one occurrence, read c, M).

## Scribal habits (not key features unless the register says so)
- Uneven vowel-homophone use (H21): e 57/25/3, a 39/18/9; no context rule behind the choice (H25: preceding letter
  P 0.07, following P 0.70 against within-vowel shuffles). Check: does the register mark one homophone as preferred?
- Dots and one colon after numeral groups (H13, H15, H28): 18 marks in all, not word separators (2 of 16 at word
  ends vs 3.09 expected at random). Code 34 (a) is dotted on 3 of its 9 occurrences, all on the first cipher line r04
  (P 0.003 uncorrected, about 0.04 corrected for 13 codes): a first-line habit cannot be told from a code-specific
  mark on this leaf. Check: does the register mark 34 (or any homophone) with a dot?
- Three clear-text full stops each precede cipher 13 (y) (H13).

## What would change the reading
A register value for any M code above, or for 101, is a period key (grade H) for those tokens; a register that gives
different values for S-graded codes is a data conflict to record before merging (CLAUDE.md rule 4), not a correction.

## Competing values from a word-seeking search (H39, from H36's greedy log)

H36's greedy word-segmentation search on the target (cheap_test_1/h36/greedy.log) chose four values that differ
from key.tsv. On the controls that search picked the right letter for 12 of 25 moves, so these are alternatives
to check, not readings. Context is key.tsv's letters, 6 each side, with the code in brackets (line:position).

| code | key.tsv | greedy | occurrences in context (key.tsv value / greedy value) |
|---|---|---|---|
| 24 | h | n | r06:15 esadec[h]eureus / esadec[n]eureus; r22:17 resmil[h]ombres / resmil[n]ombres |
| 65 | s | r | r24:4 osotre[s]egimie / osotre[r]egimie |
| 25 | u | t | r09:7 queel_[u]engaco / queel_[t]engaco; r10:8 nosinf[u]medeou / nosinf[t]medeou; r16:9 eoneop[u]radlon / eoneop[t]radlon; r17:4 gszrfs[u]cmarey / gszrfs[t]cmarey; r19:10 ciaque[u]ancone / ciaque[t]ancone |
| 48 | d | t | r17:20 orpara[d]iensei / orpara[t]iensei; r20:15 ndreis[d]esisep / ndreis[t]esisep |

Two of these the text itself settles against the search: 24 = h gives "de Cheureuse" and "tres mil hombres" (the H30
blind reader proposed h independently), where n gives neither. The other three are open both ways ("que el [101]
uenga/tenga con uos"; "tres [r]egimient-" wants both an s and an r from one token; "propondreis de/te si"), so the
register decides them.
