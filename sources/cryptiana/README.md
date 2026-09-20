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
