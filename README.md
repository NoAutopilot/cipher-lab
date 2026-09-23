# cipher-lab

Working area for attacking unsolved historical ciphers, starting from the list maintained on
S. Tomokiyo's site Cryptiana.


## What counts as a result

**The metric, restated by the owner on 23 September 2026: the number of unique solves.** A unique solve is a
reading a separate verifier has classed N3 or better (CLAUDE.md rule 10). Nothing else is sacred: language, period,
holder and historical weight only matter as far as they change how many such readings the project produces. In
practice that makes recovery the lane that scales (the DECODE catalogue holds thousands of letters whose key or
decipherment sits in a neighbouring record) and cryptanalysis the exception.

Three kinds, all wanted, always labelled as which they are (CLAUDE.md rule 10):

1. **Recovery.** A key found in another box reads a text nobody has read. Hamilton 1650 and Stepney 1702 are
   this lane.
2. **Cryptanalysis.** A text read without its key. Rare; needs size (NLS MS 20769 if it is a cipher) or a key
   that fails to fit (Hamilton if the NRS sheets do not cover it).
3. **Contribution.** Work handed to the people who hold or study the material: machine-readable keys, verified
   readings, catalogue corrections, and honest negatives, offered to the archive, to Tomokiyo's list, to DECODE
   and to the solver repositories. The Eckert keys and audit are this lane.

## Layout

    STATUS.md             the status board: every target, its state, the next action and whose it is
    status.json           the same data, machine-readable; source for the published dashboard
    dashboard.html        one-page board rendered from status.json by tools/build_dashboard.py
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
2. Read `ONBOARDING.md` (start here if you are new), `BUDGETS.md` (per-person plan limits), `LESSONS.md`, `LEDGER.md` (one row per worker, outcome and cost), `ROOM.md` (the workers' shared channel: one-line signals and flags), `.claude/briefs/` (role templates, edited by the weekly retrospective) before writing any solver. The short version: search for a printed solution,
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
