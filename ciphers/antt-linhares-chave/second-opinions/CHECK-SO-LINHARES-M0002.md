# CHECK: SO-LINHARES-M0002 (PR 10, `chatgpt-2026-09-25.md`)

Citation check by V6-SOCHK (LANE V6), 25 Sept 2026, 16:55-17:10 UTC. Every citation in the answer was traced
to the source itself where it could be reached. "confirmed" says what was read; "not confirmed" means searched
and not found; "unreachable" means the host refused. Repository-file claims were checked against the files on
`main` at a05e018.

| # | Claim in the answer | Result | What was read |
|---|---|---|---|
| 1 | Farias, "Os elos perdidos...", *ex æquo* 40 (2019), pp.15-30, DOI 10.22355/exaequo.2019.40.02 | confirmed | CrossRef record (title, Farias, *ex æquo* issue 40, issued 15 Dec 2019); publisher PDF running head "ex æquo, n.º 40, pp. 15-30. DOI ..." |
| 2 | Farias pp.23-24, nn.7, 8, 10: Bezerra de Seixas to Gabriella de Souza Coutinho, London 7 Mar 1810 and The Hague 27 Mar 1809, both PT/TT/CLNH/0086/02; Isabel Bezerra to the countess of Linhares, 1 May 1817, PT/TT/CLNH/0086/10; English/French channel | confirmed | publisher PDF, PDF pp.9-10 = printed pp.23-24, footnotes 7, 8, 10 read verbatim; "Isabel e Gabriella criaram canal próprio de comunicação em inglês e em francês" (p.24) |
| 3 | "cifra" absent from Farias | confirmed | full text extracted from the PDF, 0 hits |
| 4 | Textos Políticos (1993), Banco de Portugal PDF `ocpep-7_t1.pdf` | unreachable | one request, HTTP 403 (as LX-ED and AUD2 recorded; LOCAL-QUEUE L10) |
| 5 | Vieyra 1809 pocket dictionary, IA `newpocketdiction00viey`, Google Books `0mESAAAAIAAJ` | confirmed (bibliographic) | IA metadata: title "A new pocket dictionary ... abridged from the dictionary of Mr. Vieyra", London, Wingrave, 1809, 830 images; Google Books: same title, F. Wingrave, J. Johnson, 1809, 810 pp. Page-level recount of pp.83/241/255/293/383 not repeated (the answer itself marks it unverified) |
| 6 | ANTT PT/TT/CLNH/0086/11, DigitArq viewer `a03cef08...` | confirmed (repository record) | NOTES.md: same docId, images m0002-m0004 fetched with `tools/digitarq_fetch.py` and committed; not re-fetched |
| 7 | NOTES.md renders the trim rule "do principio, ou do fim da palavra"; the prompt says end-only | confirmed | NOTES.md line 25 (key's own Portuguese: beginning *or* end); PROMPT-chatgpt.md line 30 ("trim from the end"). A real discrepancy between the prompt and the key text |
| 8 | reading.txt now H 24, M 2; 3241315/justa disputed (Jus vs Justa, p.241 col.3 rank 15) | confirmed | reading.txt header lines 2-4; key.tsv row 3241315 (M, LX-QAFIX note) |
| 9 | Carvalho, "Dos 'papéis reservados' do rei ao Gabinete de d. João VI", *Acervo* 36(3) (2023), pp.1-21, p.14: Bezerra de Seixas, Russia, 6 Sept 1812 | confirmed | CrossRef (DOI 10.64729/an.acervo.v36i3.2085, *Acervo* 36(3), pp.1-21); PDF p.14 names "Paulo Bezerra de Seixas, plenipotenciário na Rússia, em 6 de setembro de 1812" and the farewell audiences |
| 10 | web-index search log (quoted phrases, "Vieyra cifra", etc.) | not re-run | the answer's own search log; a search-engine silence, not a source |

Counts: 7 confirmed (1, 2, 3, 5, 7, 8, 9), 1 confirmed from the repository record only (6), 1 unreachable (4),
0 not confirmed, 1 not re-run (10). Nothing invented was found.

**Does any confirmed lead move the class?** No. Farias and Carvalho are context about neighbouring items in the
same maço (0086/02, /10) and a separate collection; neither prints the m0002 fragment, names this key, or
deciphers anything. AUDIT.md's N3/N3 stands on the sources it cites. No flag to the parent.

**Useful corrections the answer raises (for the solver lane, not applied here):** item 7, the key text allows
trimming from the beginning *or* the end, so the prompt's end-only statement is wrong and a both-directions
enumeration on the M tokens is a legitimate literal-rule test.

**Verdict: merge.** A faithful answer: every external citation that could be reached is real and says what the
answer says; the one unreachable item is the known Banco de Portugal block, and the answer marked it unverified
itself.

Requests: api.crossref.org 2, exaequo.apem-estudos.org 1, arquivistica.fci.unb.br 1, archive.org 1,
www.googleapis.com 1, bportugal.pt 1.
