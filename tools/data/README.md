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
| es | es_repo/ (no, unused) / es17/ (yes, 25 Sept 2026) | yes | es17/: ~1.92M letters, early-17th-c. Spanish prose (Cervantes' Don Quijote, Quevedo's Buscón), IA djvu.txt, built for espagnol142-mercy-1648 (1648); wired straight into `LANG_CORPORA["es"]` since no `es` default previously existed (nothing to preserve, unlike de/fr above); es_repo/ (rah-canada-1869's own reading, 1.3KB) stays unused and unwired |
| la | la_repo/ | **no** | holds only dupuy468-anhalt's own reading.txt (5.2KB) -- both too small and circular |
| de (20th-c.) | de20/ | per-spec (25 Sept 2026) | 2.49M letters, 1880-1940 German prose (Fontane, Hesse, Döblin, Wassermann), Gutenberg; `LANG_CORPORA["de"]` still points to de16 (Early New High German, wrong period for a 1944 target) per the brief's "do not edit tools/judge_plaintext.py's defaults" -- `specs/koehler-1944.json`'s `judge.corpora` points here directly |
| fr (1800-1811, official/military) | fr1810/ | yes, as its own key `fr1810` (1 Oct 2026, BER-FRCORP) | 4.85M letters, Correspondance de Napoléon Ier tomes XI/XVI/XX (1805-10), Correspondance du maréchal Davout tomes II/III cut before 1812 (Mazade 1885), Lettres inédites de Napoléon Ier tome I (an VIII-1809, Lecestre 1897), IA djvu.txt; built for berthier-napoleon-1812 (22 Dec 1812); nothing from Dec 1812; leave-one-file-out false-negative rate and per-fold spread at N=325 beside fr18's in fr1810/README.md -- read before trusting a FAIL/PASS; `LANG_CORPORA["fr"]` still fr16 |
| fr (1835-1850, diplomatic) | fr1840/ | yes, as its own key `fr1840` (6 Oct 2026, R11-ZESCORP) | 3.17M letters, Nesselrode Lettres et papiers VIII-IX (1840-50), Metternich Mémoires VI (1835-48, French ed.), Guizot Mémoires VI-VII (1840-47), IA djvu.txt; built for zeschau-seebach-1841; leave-one-file-out FN 22.7% at N=325, per-fold 10.0-49.5% in fr1840/README.md -- read before trusting a FAIL/PASS |
| fr (19th-c.) | fr19/ | per-spec (25 Sept 2026) | 2.66M letters, 1830-1888 French prose (Stendhal, Balzac, Flaubert, Maupassant), Gutenberg; `LANG_CORPORA["fr"]` still points to fr16 (16th-c.) -- `specs/debosnys-1883.json`'s `judge.corpora` points here directly |

To wire nl/la later: fetch a real period corpus (Internet Archive `_djvu.txt` full text, or a Google
Books full-view volume with GOOGLE_BOOKS_KEY) of the right language and century, at least ~200k letters,
never the target's own material, name it in a MANIFEST.tsv the way pt17/MANIFEST.tsv and fr16/MANIFEST.tsv
do, and add the files to `LANG_CORPORA` in tools/judge_plaintext.py.
