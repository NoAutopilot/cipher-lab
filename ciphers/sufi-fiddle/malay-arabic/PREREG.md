# PREREG -- GAPS93-sufi-fiddle (account-4), 3 Oct 2026 11:2x UTC, committed before any scoring

Step (GAPS90 Verdict): the same `tausug/match.py` design against a Malay word list and an Arabic word list,
separately. Statistic, null, control and gate are exactly those of `../tausug/PREREG.md`; only the lists and the
held-out control text change. Script: `match2.py` in this folder (imports score/permute/read_target/render from
`../tausug/match.py`, so the target skeleton and the C3/C2 statistic are byte-for-byte the same code).

Lists (none committed; manifest.json only):
- L_MS (Malay): Leipzig Corpora Collection `msa_wikipedia_2021_30K` (CC BY 4.0, D. Goldhahn, T. Eckart, U. Quasthoff,
  LREC 2012), sentences file. Sentences split 80/20 by sentence id parity-free rule: the last 20 pct of sentence ids
  are held out for the control and are not in the list. Romanised words -> skeleton with the same `roman_skel` as GAPS90.
  Control rendering: the same `render()` (romanised word -> Jawi-like groups) as GAPS90.
- L_AR (Arabic): Tanzil Quran text, simple-clean (CC BY 3.0, verbatim text, tanzil.net), suras 1-90 as the list,
  suras 91-114 held out (too short? if fewer words than 20 control chunks need, take suras 78-114 held out and 1-77 as
  list; the choice is fixed by word count before scoring and recorded in results.json). Arabic script is mapped letter
  by letter to the same 13 classes as the cipher's own sign map: ب=b; ت ط ة(final, as written: h)… precisely:
  ب b; ت t; ث s; ج j; ح h; خ h; د d; ذ d; ر r; ز s; س s; ش s; ص s; ض d; ط t; ظ d; ع -; غ N; ف p; ق k; ك k; ل l; م m;
  ن n; ه h; ة h; و -; ي -; ى -; ا أ إ آ ء ؤ ئ -. Diacritics stripped. Control rendering: Arabic words split into
  groups after the non-joining letters (ا أ إ آ د ذ ر ز و ؤ ة ء), each group its consonant classes, 20 pct class
  substitution as before.

Gate (unchanged): PASS for a list only if target C3 p < 0.05 (1000 permutations) AND that list's own positive-control
power at 20 pct noise >= 0.8 (20 chunks, 200 permutations each). Power < 0.8 at 20 pct = NON-TEST whatever p is.
A PASS is "worth a reader", never a reading; no token is graded by this test. Seeds 1 and 2 both reported; the gate
uses seed 1. Wiktionary is not used (429 in GAPS90).
