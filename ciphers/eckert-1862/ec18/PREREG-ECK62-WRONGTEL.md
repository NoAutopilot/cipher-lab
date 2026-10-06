# PREREG-ECK62-WRONGTEL (R7B-ECK62, 6 Oct 2026 02:1x UTC, written and pushed before any number)

Question: D2-ECK62R left 18 aligned mssEC 18 entries (`align_flip_entries.tsv` minus the accepted flip 9991.571) that agree
with the print under neither book. Is the dated OR match the wrong telegram (the match carried by a few shared clear words),
or the right telegram read with a table the keys do not cover / a transcription fault?

Why not the brief's sender/recipient heading check: the ledger header names the telegraph operator (S. H. Beckwith,
Emerick), and the addressee is usually a code word, so a heading-name statistic cannot separate right from wrong telegrams
(checked on 9985.563, 9985.564, 9974.549, 9991.571 headers before any number). The statistic below uses what the ledger
does carry in clear.

Statistic (per entry): clear-word coverage = LCS(entry clear words, OR window words) / number of entry clear words. Entry
clear words = the committed reading under the entry's aligned book (`decode_all`, possessive on, guard off, as
`ec18_align.py`), brackets removed, lower-cased words of >= 3 letters that are in ec18.vocab(). OR window = words
[anchor - 2n, anchor + 2n) of the matched volume (n = number of entry words), from the same 48 `_djvu.txt` (sha256 of
`or_volumes.tsv`). Entries with < 6 clear words are reported but not classified.

Controls (rule 3; each can differ from the target on this statistic):
- positive: the 14 entries of `align_free_entries.tsv` with scored >= 5 and agree_rate >= 0.75 (right telegram, right book),
  same statistic, same window rule;
- negative: the same 14 plus the 18 targets, window moved to each entry's own committed control window (ctl_vol,
  anchor + ctl_offset), i.e. a same-week telegram that is not the match.

Gate (the instrument): positive-control median >= 0.50 and negative-control median <= 0.25 and positive p10 > negative p90.
If it fails: no entry is classified, the step is logged untested-by-this-tool.

Per target entry (only if the gate passes): coverage >= positive p10 -> "right telegram" (cause left: table change or
transcription); coverage <= negative p90 -> "wrong telegram" (the dated match is not this entry's print); between ->
"undecided". Selection bias stated in advance: every target window was chosen by a 5-gram clear-word match and no negative
window was, so the target sits above the negative control by construction; "wrong telegram" is therefore conservative.

Also reported, descriptive, not gated: entries whose body carries a second date line (two telegrams merged by the volunteer
text's blank-line split), entries sharing one OR anchor page, and the classes by month against the key files' table-change
dates. Nothing in key.md, key-no2.md, the readings or the books is changed by this test.
Script: `ec18_wrongtel.py DATA ORDIR --write|--check` -> wrongtel_entries.tsv, wrongtel_summary.tsv.
