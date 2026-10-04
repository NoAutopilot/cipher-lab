# Camille Desenclos: bibliography and premise search (DESENCLOS-PREMISE, 4 Oct 2026)

Why: the BnF Département des Manuscrits (reply of 3-4 Oct 2026 on Espagnol 144 f.22) pointed us to Dr Camille Desenclos
(UPJV / CHSSC; Centre Jean-Mabillon associate; research axis "Naissance et essor de la cryptographie française, années
1520 - années 1680", begun on a BnF Mark Pigott grant). Her work is a premise source (CLAUDE.md rules 1, 10).

- `bibliography.tsv`: 36 items (2013-2026) from HAL (30 records), theses.fr (thesis 2014ENCP0002), OpenAlex (author
  A5019875910), Semantic Scholar, CrossRef (filtered to Camille Desenclos; the name also matches an epidemiologist),
  DSpace Tartu (HistoCrypt 2024, 2025). Google Books `inauthor:` returned 0 volumes. No monograph on cryptography found.
- `raw/ft/`: the 17 open full texts read (10 HAL PDFs, 2 DSpace Tartu PDFs, 7 OpenEdition pages kept as text), with
  `pdftotext -layout` / html2text extractions. Unmodified downloads; open access.
- `terms.tsv`, `search.py`, `search-log.tsv`: per target, the shelfmark, sender/recipient, place, date and key-name regex,
  run over every text. Raw matches: fr3416 1 (Rethel as a place in the 1592 paper), dupuy468 10 (the year 1518 in
  unrelated citations and page furniture), clair349 2 ("Este" inside "esté"/"assemblee"), fr15575 2 ("Syllabus"); all
  read by eye and none about the item. **No hit for any of the 15 targets.**
- Not read: the 2014 thesis (theses.fr: "accessible: non"; its 2015 Trajectoires summary was read); "Transposer pour
  mieux transporter" (2017, Cairn), "Écrire le secret quotidien", "L'espionnage espagnol..." and "Francés de Álava"
  (2021, Spies volume; HAL records with no file); Revue de la BnF 2014 (Cairn PDF link served HTML). JSTOR-QUEUE.tsv rows
  added 4 Oct 2026 (three titles, one shelfmark family, one Mercy row). No LOCAL-QUEUE row: no item has an online copy a
  local browser could reach that the cloud could not.
- Context worth keeping (not a hit): Desenclos and Lasry 2024 (the 1592 digit cipher) say BnF fr. 3995 holds 68 cipher
  tables all belonging to Nevers, and list fr. 3422, 3614, 3616, 3623, 3633, 3634, 3646, 3976, 3977 as holding at least
  23 digit-cipher letters to Nevers of 1589-1591; Desenclos and Lasry 2025 treat unidentified cipher letters in fr. 2988,
  3158, 20506, 2961, 3029, 3092 and 6632 -- none is one of our items.

Requests: api.archives-ouvertes.fr 1, hal.science 10, theses.fr 1, api.openalex.org 6, api.semanticscholar.org 2 (one
429), api.crossref.org 1, www.googleapis.com 1, dspace.ut.ee 9, books/journals.openedition.org + doi.org 7, cairn.info 1,
www.chartes.psl.eu 1, chssc.u-picardie.fr 4.
