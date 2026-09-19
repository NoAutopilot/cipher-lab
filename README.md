# cipher-lab

Working area for attacking unsolved historical ciphers, starting from the list maintained on
S. Tomokiyo's site Cryptiana.

## Layout

    CATALOG.md            every item from Cryptiana's index with status, shelfmark and source page
    LANDSCAPE.md          who is solving what (Sept 2026), corrected statuses, where the open ground is
    LESSONS.md            how the current solvers work, distilled from their repositories
    CLAUDE.md             the rules every session and agent follows here
    QUEUE.md              ranked list of what to attempt next, refreshed by the scout workflow
    .claude/workflows/    named workflows: check-solved (six-source sweep before any campaign),
                          scout (harvest, filter out the solved, score, file into QUEUE.md)
    ciphers/<name>/       one folder per cipher being worked on: ciphertext.txt + NOTES.md
    sources/cryptiana/    unmodified snapshot of the Cryptiana pages (19 September 2026)
    tools/html2text.py    render a saved page as plain text
    tools/freq.py         token frequency, index of coincidence, bigrams for a ciphertext
    tools/refresh-sources.ps1  re-download the index page and show what changed (PowerShell)

## Start here

1. Read `LANDSCAPE.md`. Most of Cryptiana's list was swept by two AI-driven projects in the week
   before this snapshot, and the section "Where the open ground is" says what is left.
2. Read `LESSONS.md` before writing any solver. The short version: search for a printed solution,
   get the page image, look for a sibling letter with a decipherment, find the structure by hand,
   and never report a negative without a matched control.
3. `CATALOG.md` keeps every item from the index page with Tomokiyo's status and the corrections.
3. Read the background page named in the catalogue:

       python3 tools/html2text.py sources/cryptiana/web/mary.htm | less

4. Make a folder under `ciphers/` following `ciphers/README.md`, or use one that already exists.
5. Get a feel for the ciphertext:

       python3 tools/freq.py ciphers/sp53-16-78/ciphertext.txt

## Ready-made starting points

These folders already hold a transcription and notes:

| Folder | What |
|---|---|
| sp53-16-78, sp53-16-79 | Two 1585 letters in the same hand, numeric nomenclator, Mary Queen of Scots circle |
| sp53-22-f52 | Very short "Spanish spy" cipher, alphabet-sized symbol set |
| moray-wood-1568 | Short Scottish diplomatic cipher, said to look simple |
| birago-nevers-1571 | Italian numerical cipher with diacritics, needs tokenising first |
| maurice-rupert-1645 | Royalist code after Naseby |
| intercepted-royalist-1646 | Opening only; full text needs transcribing from DECODE R8623 |
| ormond-arran-1678 | About 20 groups, explicitly written as a test of the recipient |
| stepney-manchester-1702 | Two short runs; archival route more promising than cryptanalysis |
| destaing-gerard-1779 | French naval code, about 600 entries, with cleartext context |
| berthier-napoleon-1812 | Large Napoleonic code, opening only |

## Sources and credit

All pages under `sources/` are copyright S. Tomokiyo and are kept only as a working reference.
Cite the site (https://cryptiana.web.fc2.com/code/) and the named solvers when using anything from it.
