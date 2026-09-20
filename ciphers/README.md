# Working folders

One folder per cipher being worked on. Convention:

- `ciphertext.txt` — the transcription being attacked. Keep the tokeniser in mind: Cryptiana's
  transcriptions use `;` between tokens; inline quotations from unsolved.htm use spaces.
- `NOTES.md` — source, status, what is already known, and ideas. Update the status line when
  anything changes.
- Anything else (scripts, partial keys, candidate plaintexts) goes in the same folder.

Folder names are `<who-or-what>-<year>` or the archive shelfmark. Before starting on a cipher,
check `CATALOG.md` and Daniel Bourdeau's site (https://dbourdeau.github.io/cyphersolver/) to make
sure it has not been solved since the snapshot was taken.

Quick frequency count of any folder's ciphertext:

    python3 tools/freq.py ciphers/sp53-16-78/ciphertext.txt
