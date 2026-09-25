# pt18: Portuguese prose of about 1780-1830 for the judge's language check

Built 25 Sept 2026 (V6-PTCORP, `.claude/briefs/runs/2026-09-25-lane-v6-ptcorp.md`) because `tools/data/pt17`
is António Vieira's own letters (1648-1697) -- roughly 120-160 years before this repo's c.1780-1830
targets (antt-linhares-chave, c.1811-12) -- an era mismatch LX-JUDGE's discrimination check (25 Sept 2026,
`ciphers/antt-linhares-chave/NOTES.md`) flagged as adding an 8.5 pct false-negative rate to that gate at
N=98 letters, from corpus mismatch alone.

Internet Archive OCR full text (`_djvu.txt`) of four Google Books scans of two London-published,
Portuguese-language emigre periodicals of the Peninsular War / early Rio court years:

- **Correio Braziliense, ou, Armazem Literario** (Hipólito José da Costa, London, monthly, 1808-1822;
  identifiers `correiobrazilie00unkngoog`, `correiobrazilie02unkngoog`)
- **O Investigador Portuguez em Inglaterra, ou Jornal literário, político &c.** (London, monthly,
  1811-1819; identifiers `oinvestigadorpo03unkngoog`, `oinvestigadorpo05unkngoog`)

See MANIFEST.tsv for per-file identifier, title, date, URL, byte/letter counts, fetch date and why each
was chosen. Fetched once, one request at a time, >=1.5 s apart (4 archive.org requests total this pass,
plus the advancedsearch.php candidate searches).

Each file has Google's boilerplate ("This is a digital copy of a book...", repeated in a Portuguese
machine translation in three of the four scans) trimmed off before saving -- that boilerplate is modern
English/Portuguese, not period text, and would otherwise sit inside the corpus the judge scores against.
The cut line for each file is recorded in MANIFEST.tsv; a handful of garbled library-stamp OCR lines
("STANFORD UNIVERSITY LIBRARY" etc.) remain just after each cut point and at scattered "Digitized by
Google" watermarks through the text -- normal, low-volume front/back-matter noise, not stripped further
given the size of the surrounding real text (see the cross-corpus word-coverage check below).

Combined: 970865 + 1006657 + 633178 + 615402 = **3,226,102 letters after fold()** -- well over the
1,000,000-letter floor this brief set, and over triple pt17's ~1.45M. No single source is more than
31.2 pct of the total (correiobrazilie02unkngoog); the smallest is 19.1 pct.

**OCR-quality check** (per this brief's "share of folded letters in words found in the others"): for each
file, `tools/judge_plaintext.py`'s own `NgramModel.cover()` word list was built from the *other three*
files only, then used to score that file's own folded letters. All four land at 90.5-95.6 pct cross-corpus
word coverage -- consistent, clean period-Portuguese OCR across two different periodicals and two Google
Books scanning passes, not heavy junk or Latin/French drift. (For comparison, LX-JUDGE's controls table
shows genuine real-text word-cover medians around 0.88-0.95 for period Portuguese scored against pt17's
corpus, so this is the expected range for real prose, not an anomaly.)

**Excluded, per this brief:** anything by or about Vieira (that is pt17), anything by or about
Linhares/Sousa Coutinho or this repo's own antt-linhares-chave material (that would be circular), the
Vieyra dictionary the target's key uses (circular for a different reason -- it is headword salad, not
prose), translations from English/French, and verse. All four sources here are original Portuguese prose
periodical text, not translations, not verse, not dictionaries, and have no connection to the Linhares
target or its key source.

Never add Brochado's own letters, MSLIV 0638 material, or Dória 1944 to this folder either -- same
circularity concern as pt17's own warning, extended to any future pt18-era target from that fonds.
