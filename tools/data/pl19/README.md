# tools/data/pl19: Polish prose, Project Gutenberg

Fetched 26 Sept 2026 (GOLD-KAL3, `.claude/briefs/runs/2026-09-26-lane-gold-c5-kaliningrad-polish.md`) for the
kaliningrad-2015 Polish-homophonic cheap test (rank 4 in `ciphers/kaliningrad-2015/HYPOTHESES.md`'s cycle-4
decision table). No Polish corpus existed on disk before this job.

## What's here

Four Project Gutenberg Polish-language prose texts, header/footer stripped at the PG START/END markers (as
`de20`/`nl20`), gzip-compressed. See `MANIFEST.tsv` for ids, authors, titles, years, URLs, sha1 of the stripped
body (before the ł-fix below), and letter count after `tools/homophonic_anneal.py`'s `fold()`.

| id | author | title | year |
|---|---|---|---|
| 34635 | Zapolska, Gabriela | Menazerya ludzka | 1911 |
| 6000 | Łubieński, Maciej | Ironia Pozorów | unknown (Gutendex gives none) |
| 27178 | Gnatowski, Jan | Na śmierć, 1863 | 1888 |
| 8119 | Schulz, Bruno | Sklepy cynamonowe | 1934 |

None of the named example authors in the brief (Sienkiewicz, Prus, Żeromski, Reymont, Orzeszkowa, Konopnicka)
appear in Gutendex's Polish-language fiction catalogue as queried (`languages=pl&topic=fiction`, 7 results
total, 26 Sept 2026) -- those names were the brief's suggestions, not a catalogue check; this is what the
catalogue actually holds under that query. The two titles left out of the 7: 28168 (Mickiewicz, "Żywila", a
short "powiastka"/short-story, and a poet better known for verse) and 38459 (Niewiadomska, "Bez przewodnika",
category "Adventure", an author known for children's/school books) -- left out for register fit, not fetched
(no extra request spent testing them).

## Letter counts (before/after fold)

Total across the 4 texts, **before** `fold()` (own Polish alphabet, ą ę ó ł ż ś ć ń ź kept distinct, case
folded to lowercase, everything non-alphabetic dropped): 840,756 letters.

**Short of the 1.5M-letter aim** stated in the brief: Gutendex's Polish-fiction catalogue under this query is
thin (7 hits total; the two largest, 6000 and 34635, are 434,601 and 232,954 folded letters respectively) and
the brief capped this job at 4 texts, so no 5th/6th fetch was made to chase the aim once the four largest
fiction hits were in hand. Reported as found, not padded (rule 10: a catalogue result is a catalogue result).

ł-fix (brief step 1): `homophonic_anneal.fold()` NFKD-normalizes and strips *combining* marks, but ł (U+0142)
is not built from a base letter plus a combining mark -- it is its own code point -- so `fold()`'s final
`[^a-z]` filter drops it outright rather than folding it to `l`. Checked directly: `fold()` on the 4 raw
bodies (before any fix) drops 24,138 letters to ł/Ł alone (2.87% of the 840,756-letter total), against under
0.1% for every other non-a-z alphabetic character combined (a handful, under 30 total, of stray Cyrillic
letters from quoted phrases/footnotes across the 4 texts -- left alone, genuinely not Polish, and far under
the 0.1% bar). The `.txt.gz` files in this folder have ł/Ł already replaced with l/L, so `fold()` run on them
drops only those ~30 stray Cyrillic letters: `len(fold(text))` vs the raw own-alphabet letter count differs
by 0.004%, well under the 0.1% check in the brief.

Folded (a-z only, ł already fixed) total: 840,725 letters.

## IC, own alphabet vs folded (brief step 9)

Measured on the fetched corpus itself (concatenated in manifest order), N=978, 20 windows, seed 42, matching
the target's own N (convention A):

| view | IC min-max (20 windows) | IC mean |
|---|---|---|
| own Polish alphabet (ą ę ó ł ż ś ć ń ź kept distinct as separate signs, no fold at all) | 0.0472-0.0534 | 0.0506 |
| folded to a-z (ł fixed to l first, then `fold()`) | 0.0618-0.0660 | 0.0642 |

The brief's prior estimate ("Polish plain IC is about 0.061 on its own alphabet") was higher than what this
corpus measures unfolded (0.0506); folded IC (0.0642) sits close to and brackets the target's convention-A IC
(0.0657, K=36) inside its own 20-window range's upper half. This is a profile observation, not a control
result -- see `ciphers/kaliningrad-2015/HYPOTHESES.md` for the `family_run.py` unit that actually tests it.

## Licence

Each source is Project Gutenberg public-domain text; `LICENSE-gutenberg.txt` is the PG licence footer (one
copy, per its own redistribution terms), taken from book 34635's fetch (all four carry the identical text).

## Requests

Discovery (gutendex.com, `https://gutendex.com/books?...`): more than intended -- see
`ciphers/kaliningrad-2015/NOTES.md` "GOLD-KAL3" section for the honest count and the lesson (a `-L` follow
of a redirecting query counts as 2 requests, not 1, and a mid-job verification re-query is pure waste; this
job made both mistakes). Text fetches (gutenberg.org, `https://www.gutenberg.org/ebooks/<id>.txt.utf-8`): 4,
one per text, 1.5s apart, descriptive User-Agent, no retries needed (all 200 on first attempt).
