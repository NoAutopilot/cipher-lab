# tools/data: corpora for tools/judge_plaintext.py's language check

Each language in `LANG_CORPORA` (tools/judge_plaintext.py) needs a real period-appropriate prose corpus of
at least ~200k letters that is not a target's own committed reading (scoring a candidate reading against
its own voice is circular). Status as of 25 Sept 2026 (YX-PTJUDGE):

| Language | Folder | Wired? | Why |
|---|---|---|---|
| en | pg1661_holmes.txt, pg2701_mobydick.txt | yes | Gutenberg prose, large, unrelated to any target |
| de | de16/composed_enhg.txt | yes | period German prose (pre-existing) |
| fr | fr16/ | yes | Catherine de Médicis / Marguerite de Valois letters, IA djvu.txt (pre-existing) |
| it | it16/ | yes (25 Sept 2026) | ~1.59M letters, 16th-c. Italian letters (Caro, Tasso, Gonzaga, Aretino), IA djvu.txt; none of it is a target's own reading |
| pt | pt17/ | yes (25 Sept 2026) | ~1.45M letters, António Vieira's own letters 1648-1697, IA djvu.txt; unrelated to the Brochado/Linhares Portuguese cipher targets |
| nl | nl_repo/ (no) / nl20/ (yes, per-spec) | partial | nl_repo/ holds only 3 small files (~12KB total) that are targets' own committed readings -- unusable; nl20/ (25 Sept 2026, GOLD-C) is a real 2.29M-letter Dutch prose corpus (1880-1940, Gutenberg), not yet pointed to by any spec's `judge.corpora` (no `nl`-language target spec exists yet) and not added to `LANG_CORPORA` (brief: do not edit that file's defaults) |
| es | es_repo/ | **no** | holds only rah-canada-1869's own reading.txt (1.3KB) -- both too small and circular |
| la | la_repo/ | **no** | holds only dupuy468-anhalt's own reading.txt (5.2KB) -- both too small and circular |
| de (20th-c.) | de20/ | per-spec (25 Sept 2026) | 2.49M letters, 1880-1940 German prose (Fontane, Hesse, Döblin, Wassermann), Gutenberg; `LANG_CORPORA["de"]` still points to de16 (Early New High German, wrong period for a 1944 target) per the brief's "do not edit tools/judge_plaintext.py's defaults" -- `specs/koehler-1944.json`'s `judge.corpora` points here directly |
| fr (19th-c.) | fr19/ | per-spec (25 Sept 2026) | 2.66M letters, 1830-1888 French prose (Stendhal, Balzac, Flaubert, Maupassant), Gutenberg; `LANG_CORPORA["fr"]` still points to fr16 (16th-c.) -- `specs/debosnys-1883.json`'s `judge.corpora` points here directly |

To wire nl/es/la later: fetch a real period corpus (Internet Archive `_djvu.txt` full text, or a Google
Books full-view volume with GOOGLE_BOOKS_KEY) of the right language and century, at least ~200k letters,
never the target's own material, name it in a MANIFEST.tsv the way pt17/MANIFEST.tsv and fr16/MANIFEST.tsv
do, and add the files to `LANG_CORPORA` in tools/judge_plaintext.py.
