# Cryptiana source snapshot

Unmodified copies of pages from S. Tomokiyo's site *Cryptiana: Articles on Historical Cryptography*
and its companion blog, downloaded on 19 September 2026. Copyright remains with the author.

- `web/` — pages from https://cryptiana.web.fc2.com/code/ under their original filenames.
  `unsolved.htm` is the index page ("Unsolved Historical Ciphers", last modified 19 September 2026)
  and every other file here is something it links to. Pages are Shift_JIS encoded; the `.txt` files
  are Tomokiyo's transcriptions of specific ciphertexts.
- `blog/` — posts from https://cryptiana.blogspot.com/ linked from the index page. UTF-8.

Do not edit these files. Working notes and transcriptions belong under `ciphers/`.

To read a page as text:

    python3 tools/html2text.py sources/cryptiana/web/unsolved.htm | less

## Additions, 24 September 2026 (ASSIGNMENTS row 26, Tomokiyo bibliography check)

`bongars.htm`, `spanish3C.htm`, `eleanor1476.htm` fetched from cryptiana.web.fc2.com (one request at a
time, 1.5s apart, descriptive UA, all HTTP 200) as reference for the academia.edu papers listed in
`PAPERS.tsv` -- none is an exact mirror of an academia.edu paper's own text, only a related article by
the same author on a nearby subject; see PAPERS.tsv for the distinction. Tomokiyo's academia.edu profile
(https://independent.academia.edu/SatoshiTomokiyo) itself returned HTTP 403 on the one permitted fetch;
per the good-citizen rule that host was not retried, and the paper list in `PAPERS.tsv` was built instead
from `web/crypto.htm`'s own table of contents (which links out to academia.edu for papers with no htm
counterpart) plus web search snippets of academia.edu's own listing pages. See `PAPERS.tsv` and
`READABLE.tsv`.
