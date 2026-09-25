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
| nl | nl_repo/ | **no** | holds only 3 small files (~12KB total) that are targets' own committed readings/plaintext-print copies (breda-statengeneraal-1624-25, vanbeuningen-dewitt-1657) -- far under the ~200k floor, and using a target's own reading as its corpus would be circular anyway |
| es | es_repo/ | **no** | holds only rah-canada-1869's own reading.txt (1.3KB) -- both too small and circular |
| la | la_repo/ | **no** | holds only dupuy468-anhalt's own reading.txt (5.2KB) -- both too small and circular |

To wire nl/es/la later: fetch a real period corpus (Internet Archive `_djvu.txt` full text, or a Google
Books full-view volume with GOOGLE_BOOKS_KEY) of the right language and century, at least ~200k letters,
never the target's own material, name it in a MANIFEST.tsv the way pt17/MANIFEST.tsv and fr16/MANIFEST.tsv
do, and add the files to `LANG_CORPORA` in tools/judge_plaintext.py.
