# Brussels "chiffres 1647-98" register vs key.tsv (campaign row H17)

DECODE-OPEN (parent worker, owner account, session_015RJ8kumxcx2XKtHHU1zzsU), 28 Sept 2026, after DECODE's PI
extended the project account's image rights. Source: DECODE records 958-965, AGR Brussels, Secretairerie d'Etat et
de Guerre inv.nr. 2 ("chiffres 1647-98"; R964's record gives inv.nr. 2559). All 17 full-size page images were
fetched and viewed; they stay in the worker's scratchpad. The holding archive's permission may be needed before any
image is published (DECODE PI, 28 Sept 2026), so none is committed.

## What the eight records hold

| record | DECODE name / receiver | pages | content | numeric letter table? |
|---|---|---|---|---|
| R958 | key1, "Dug. de Nienburg" (Neuburg) | 1 | vowels a e i o u = 10/11, 20/12, 30/13, 40/14, 50/15; consonants b-z = 16-35 (no 20, 30); 23 names as capital letters A-Z | yes: `decode_958.tsv` |
| R959 | key2, "Conde de Cantecroy" | 2 | French: letters as graphic signs; word codes (au, de, du, ...) 12-89; names 300-379 | no (sign alphabet) |
| R960 | key3 | 1 | A18 B20 C19 D17 E14 ... Z39, one code per letter (letter marks as variants); syllabary; DECODE transcription D2756 | yes: `decode_960.tsv` |
| R961 | key4 | 1 | syllabary/nomenclature 35-468; first part (alphabet) missing from the photograph (DECODE D2770) | no |
| R962 | key5 (Latin) | 1 | syllabary 1-666 (R/S syllables in 4-80); DECODE D2618 | no letter table |
| R963 | key6 | 2 | letters as numbers 15, 26, 37, 40, 59 ... with signs; word and name codes 120-239+ (DECODE D3025) | letters spaced 11 apart, not 2-34 |
| R964 | key7 | 2 | court names 300+ (DECODE D3023) | no |
| R965 | key8 | 7 images | several keys: p1 a dictionary 200-1011 with letter superscripts; p2 a homophonic dictionary; p3 "Cifra de Gouernadores y Cauos Principales del Ex.to por el año 1658", scrambled alphabet 1-23; p4 cover leaf (1691); p5 faint scrambled multi-homophone alphabet; p6 and p7 alphabets A..M then N..Z from 1 | yes: `decode_965.tsv` (p3, p5, p6, p7) |

## Comparison with key.tsv

`compare_decode.py` (writes `comparison.tsv`; `--check` fails when stale). For every numeric code key.tsv carries
that a table also carries:

| record | table | codes both carry | agree | which |
|---|---|---|---|---|
| R958 | key1 | 24 | 1 | 10 (a) |
| R960 | key3 | 19 | 1 | 27 (u) |
| R965 | p3 (1658) | 21 | 1 | 29 |
| R965 | p5 | 17 | 0 | |
| R965 | p6 | 18 | 6 | 2-7 (o p q r s t) |
| R965 | p7 | 28 | 7 | 2-8 (o p q r s t u) |

DECODE's own transcriptions of R961-R964 were checked the same way (script-parsed, not committed): R961 and R964
share no code with key.tsv, R962 shares 36 (syllables; 2 agree, 5 and 65 by the letter r/s, chance), R963 shares 6 (0 agree).

**No table reaches the brief's gate (20 agreements among shared codes): no candidate period key in this
register.** The best, R965 p7 at 7/28, agrees only on the run o p q r s t u = 2-8, which key.tsv shares with the
p6 and p7 alphabets of the same register (N..Z counted up from 1 or 2). key.tsv's own layout differs from every
table here: three homophones per vowel (a 10/17/34, e 18/19/33, i 21/26/31, o 2/23/29, u 8/25/27) and consonants on
even numbers (b 12, c 14, d 16, f 20, g 22, h 24, l 28, m 30, n 32); R958 (the H16 design sibling) has two
homophones per vowel on tens/teens and consecutive consonants 16-35. No table gives a value for key.tsv's M codes
(9, 15, 25, 48, 52, 65, 72) or for the boxed 101 (R958's names are capital letters, not boxed numerals).

What the register does show: the o-u = 2-8 run is a house habit of this Brussels office (R965 p6, p7), so key.tsv's
2-8 is consistent with the Secretaria's practice, a design point, not a period key.

## Grades and passes

Pass A: DECODE-OPEN's own read of crops cut from the full-size images. Pass B: a blind Sonnet subagent read the
same 11 crops without pass A. H = both passes agree on a clear cell; S = one pass unsure, or the passes place a
value on different letters (the second-row homophones of R965 p7 and most of p5/p6, which are faint at the
1616x2309 scan size); U = unread (R960 K, L, M under the archive stamp). Counts: R958 24 H / 4 S; R960 19 H / 2 S /
3 U; R965 30 H / 64 S. The comparison counts H and S cells; restricting to H cells does not change any verdict
(p7's seven agreements are all H).

## The M codes and the H41/H42 syllable reading

In DECODE's own transcriptions the codes above key.tsv's letter range are syllables where they occur at all:
R960 48 = no, 65 = ba; R962 (Latin) 52 = re, 65 = s, 72 = san, 101 = vu; R963 101 = ay. These are other keys, so
they neither confirm nor refute H41/H42's syllable reading (72 = do, 52 = ro). Only the design point carries over:
in this office, codes just above the alphabet are syllables. No table gives 72 = do or 52 = ro.
