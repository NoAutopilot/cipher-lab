# pt17: 17th-c. Portuguese prose for the judge's language check

Internet Archive OCR full text (`_djvu.txt`) of two editions of António Vieira's letters (written
1648-1697, well inside the 1650-1750 window this repo's Portuguese ciphers fall in), fetched once on
25 Sept 2026 (see MANIFEST.tsv). Front matter (Google's boilerplate and each edition's 19th/20th-century
editorial preface) is trimmed off each file before saving, so the corpus is period letter prose only.

Combined: 1,974,460 + 263,331 raw bytes, 1,275,080 + 169,939 letters after `fold()` -- about 1.45M
period-Portuguese letters, well over the ~300k floor tools/judge_plaintext.py's language check needs.

Never add Brochado's own letters (antt-msliv0638-brochado-1712), any text from the MSLIV 0638 volume,
or Dória 1944 to this folder -- those are the targets the judge scores, and scoring a target against its
own voice is circular (see tools/data/pt_repo, which holds exactly that and must not be wired into
LANG_CORPORA for this reason).
