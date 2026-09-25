# te-wood-1950 cheap test 1: Gillogly dictionary attack

Written 25 Sept 2026 by LANE B2 worker bWOO (Sonnet, session_01JgaFwLL9NQAT23xpr59ZZh).

## Method

Cipherbrain post 35 (`sources/schmeh/posts/35-thouless.txt`) describes Thouless's running-sum keyed
cipher: a key is a sequence of distinct words drawn from a book (duplicates of earlier words in the
sequence dropped), each word's letters summed A=1..Z=26 and reduced mod 26 to give one key number
per plaintext letter, `ciphertext = plaintext + key (mod 26)`. Jim Gillogly solved Thouless's message
C in 1995 by a dictionary attack over candidate key texts, finding the key BLACK BEAUTY. Wood's own
1950 cryptogram (spec `specs/te-wood-1950.json`) uses the same method with an explicitly
**non-English** key text and a plaintext "authored in several different languages" (per Schmeh) --
Wood's own words, not English either.

`gillogly_attack.py` replicates this: for a candidate key text and every start offset `s`, it walks
forward from `s` collecting the first N=21 distinct words (case/accent-normalised), sums each word's
letters mod 26 to get the key stream, decrypts, and scores the putative plaintext with
`tools/english_score.py`'s `EnglishModel.cover()` -- the longest stretch of the (space-free) decrypted
string that splits wholly into real dictionary words -- once against an English model (the tool's
default Holmes/Moby-Dick corpora) and once against a model built from the key text's own language
(the key text itself, per the brief: "a word list in the plaintext's language; English first, then the
key text's language"). Own code; nothing copied from the solver repositories (CLAUDE.md rule 8).

At N=21 this is far too short for a score-based PASS (spec `cheap_tests_in_order[0]`, CLAUDE.md rule
3): the highest-scoring offset for any key text is reported only as a candidate for a person's manual
inspection, never a solve.

## Key texts (Internet Archive, archive.org, not gutenberg.org)

| file | archive.org identifier | language | bytes |
|---|---|---|---|
| `keytexts/fr_bible.txt` | bub_gb_kMCnTLhx90cC (La Sainte Bible de Carrières) | French | 584,201 |
| `keytexts/la_vulgate.txt` | biblia-sacra-vulgata (Biblia Sacra Vulgata) | Latin | 5,435,270 |
| `keytexts/fr_novel.txt` | bub_gb_ZJtKqLCEAFQC (Les Misérables, Victor Hugo) | French | 437,746 |
| `keytexts/de_novel_faust.txt` | fausteinetragdi09goetgoog (Faust, Goethe) | German | 571,229 |

A fifth candidate, the 1912 Luther Bible (`die-bibel-...-lord-henfield-edition-2025`), 404'd on its
listed `_djvu.txt` derivative despite the metadata API listing it (checked once, not retried); Faust
was substituted as the German-language candidate instead, so German is covered by a classic novel
rather than a Bible, matching the spec's "Bibles ... or a classic novel" wording. Each key text scanned
to its first 20,000 raw words (a practical cap, not the whole book; see Limitations).

## Control (matched, 3 seeds, `control_de_novel_faust.txt`)

A synthetic N=21 cryptogram built from a real English sentence (from `tools/data/pg1661_holmes.txt`,
independent of the target) and the true running-sum key at a random offset in `de_novel_faust.txt`,
searched over the *same* 0..20,000-word range the real attack scans (so the control matches the real
search conditions, not an easier forward-only window):

| seed | true offset | rank of true offset (of ~19,980 candidates) | true-offset score (max/en/lang) | next-best score |
|---|---|---|---|---|
| 0 | 1625 | **1** | 19 / 18 / 19 | 16 |
| 1 | 710 | **1** | 20 / 20 / 20 | 16 |
| 2 | 13 | **1** | 20 / 19 / 20 | 17 |

The true offset ranks 1st of ~20,000 candidates in all 3 seeds, with a clean score gap (19-20 vs
16-17 runner-up) -- the method and scoring function work as intended.

## Target result (Wood's cryptogram, `FVAMINTKFXXWATBOIZVVX`, N=21)

Top-1 candidate per key text, full top-10 tables in `attack_<keytext>.txt`:

| key text | lang | top score (max/en/lang) | offset | plaintext |
|---|---|---|---|---|
| fr_bible | french | 12 / 12 / 12 | 5981 | OFQTHDFEWMOODWEEAMPJH |
| la_vulgate | latin | 12 / 8 / 12 | 5631 | EDENYTUTIHRECMFUMDSND |
| fr_novel | french | 12 / 4 / 12 | 12245 | QMNUPRHATEUXBOWDUCNQD |
| de_novel_faust | german | 16 / 5 / 16 | 18131 | RFLHHXOAWAXTIMILLEBYE |

None of these reach the control's true-positive band (18-20/21); the best of the four
(de_novel_faust, score 16) still sits below the control's *runner-up* scores (16-17) and none of the
top-10 candidates in any of the four `attack_*.txt` files read as a real sentence in any language on
inspection. **No candidate found** among these 4 key texts and their first 20,000 words: negative, not
a solve, not even a lead worth a person's manual inspection.

## Limitations (read before extending)

- Each key text is scanned only to its first 20,000 raw words (about the first third to two-thirds of
  a Bible-length book at this OCR word rate). Wood may have started later; a next worker could raise
  `--max-words` at increased runtime cost (roughly linear).
- Only 4 key texts tried, all well-known European classics/Bibles. Wood said the key text is "a book,
  which is not written in English" -- no narrower constraint than that from Schmeh's account; a huge
  space of candidate books remains untried.
- The English/key-language `cover()` score cannot detect a hit in a *third* language (e.g. if the
  plaintext segment sampled by chance is Italian or Spanish, neither dictionary would score it well).
  Given Wood's plaintext is described as multilingual, a true hit could score low here even with the
  right key text, if the particular 21-letter stretch happens to fall in a language neither model
  knows.
- OCR noise in the Google Books-derived `_djvu.txt` files (visible in the raw text, e.g. stray
  characters, misrecognized letters) will occasionally corrupt a word's letter-sum, shifting the key
  stream at and after that word; not corrected for.

## Reproduce

```
python3 gillogly_attack.py control --keytext keytexts/de_novel_faust.txt --lang-name german \
    --n 21 --seeds 3 --topn 10 --max-words 20000
python3 gillogly_attack.py attack --cipher FVAMINTKFXXWATBOIZVVX --keytext keytexts/fr_bible.txt \
    --lang-name french --max-words 20000 --topn 10
# (repeat attack for la_vulgate/latin, fr_novel/french, de_novel_faust/german)
```
