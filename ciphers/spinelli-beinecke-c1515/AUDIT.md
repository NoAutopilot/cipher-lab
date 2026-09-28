# AUDIT -- spinelli-beinecke-c1515

## VERIFY-SPINELLI-2 (28 Sept 2026)

Verifier: parent worker VERIFY-SPINELLI-2 (owner account), a session separate from the campaign runners
(session_0189W7KLRRUSFLgi5iPbBYph and successors). Brief: `.claude/briefs/runs/2026-09-28-parent-verify-spinelli-2.md`.
Replaces VERIFY-SPINELLI-1 (session_01SCWXexNRimHBDRaT1SrmX8), which wrote nothing to the repository.
Claim under audit (runner, H35-H40, ROOM 06:15/06:24/06:32): a control-backed PARTIAL decode of the Beinecke letter
(Tommaso Spinelli to Leonardo Spinelli, Barcelona, 7 Sept 1519, OID 10844890) under Domnina's published key, 259
tokens (H 229, M 22, U 8), judge FAIL -1.334 vs real_p05 -0.968, lines 3, 7, 8, 9 continuous Italian.

### 1. Novelty (written first, 14:24 UTC)

| item | answer |
|---|---|
| **Prior decipherment of THIS leaf** | **YES. Class N0.** Klaus Schmeh, "Who can solve this encrypted text from the 16th century?", *Cipherbrain* (scienceblogs.de/klausis-krypto-kolumne), 24 March 2017, https://scienceblogs.de/klausis-krypto-kolumne/2017/03/24/who-can-solve-this-encrypted-text-from-the-16th-century/ -- posts this letter's three pages ("a letter written by some Tommaso from Barcelona, Spain, to an Italian named Leonardo di Guasparri Spinelli ... page #1 (with one paragraph encrypted) ... page #2 (with two encrypted lines)"), the same layout as this folder's p1 8 lines + p2 2 lines. In the comments the same day, commenter #2/#3 (Ellie Velinska) finds Domnina's PDF and key; **#7 (Norbert) and #8-#10 (Thomas) decipher both cipher passages with Domnina's improved 2016 key** (p.27 of the PDF). Snapshot: `verify2/cipherbrain_2017-03-24_tommaso.html` (fetched 28 Sept 2026 14:23 UTC, HTTP 200, sha256 78ba87fd...3d15) and its text `verify2/cipherbrain_2017-03-24_tommaso.txt`. |
| The 2017 reading, verbatim (comment #7, Norbert, p.1) | "et li dite che madama / Marg[h]erita non vole arrettare la gu- / bernatione di Spagnia et che più / d'inclinatione si mos[t]ra al Conte / Palatino che ad altri. / Arrivo caro nelo(?) et trovo la / resolutione di costoro mi[g]liore / di quelo el Papa domandava." |
| (comment #8, Thomas, p.1) | "ET LIDITE CHE MADAMA MARGERITA NON VOLE ACCETTARE LA GUBERNATIONE DI SPAGNIA ET CHE PIU DINCLINATIONE SI MOSTRA AL CONTE PALATINO CHE AD AL TRI? ARRIVO CARZONELO (?) ET .... RESOLUTIONE DE COSTORO (?) MILIORE DI QUE LO EL PAPA DOMANDAVA" |
| (comments #9-#10, Thomas, p.2) | "SE E BISOGNIO EL GUBERNATORE DI BRESSA ANDARAI SUI ??ERI" (two signs unread; #11-#13 discuss "arrettare" vs "accettare" for the %-like cc sign) |
| Domnina 2015/2016 (sources/domnina-2015-2016/) | Prints the key (2015 Fig.1; 2016 Ill.1) and the **2 July 1520 Antwerp letter** (2015 Fig.2; 2016 Ill.2, Beinecke box 126 folder 2583 fol.1r) with Leonardo Spinelli's own decipherment of that fragment (2016 Ill.3, box 127 folder 2611 fol.2r). **That letter is a different item from this leaf**, by layout and opening: the 1520 leaf opens with 9-10 lines of clear text (a large initial, "...poi parti di spagna...") and then 8 lines of cipher at the foot, the first cipher line opening `+ 3 ω ʃ 8 ...`; this leaf opens "Scrissivi un'altra che sarà con questa..." with the cipher starting mid-line 2 ("al R.do fratel mio") and opening `4 7 e 3 8 ...`, 8 cipher lines then the clear "La morte del Cardinal de Rossi...". Leonardo's Ill.3 decipherment ("Passo di qua ... franzesi ... Turchi ...") shares no phrase with this leaf's decode. OCR-layer grep (1519, Barcel, gubern, ispag, Brescia/Bressa, palatin, costoro, 10844890, 3811294): the only hit is "1519" in a Russian footnote on Charles V's reign dates. Domnina prints no reading of this leaf. |
| Tomokiyo, `sources/cryptiana/web/henryvii.htm` (note of January 2024) | Prints only "la gubernation d'ispagnia" and says the letter "can be deciphered" with Domnina's key; `henryviii.htm` and `spanish3.htm` mention Spinelly with no reading. Confirmed by grep this session. |
| Why the campaign missed it | CLAUDE.md rule 1 names "the comment threads of the list posts (Cryptiana blog, Cipherbrain)" as a required pre-campaign check. INTAKE-SPINELLI (27 Sept) and the H-steps logged Tomokiyo, Bourdeau's catalogue, OpenAlex/S2/CORE/Google Books for Domnina, but no Cipherbrain search. A single web search ("Tommaso Spinelli letter Leonardo Barcelona 7 September 1519 cipher deciphered Beinecke") returned the post as its second result. |

**Other families searched this session (a search log; the class is already fixed by the row above):**
`tools/print_check.py` on 7 decoded phrases (`verify2/phrases.txt`, `verify2/print-check.tsv`, `verify2/print-check-hosts.tsv`):
IA full text (ia-global) 7 phrases, Google Books API 7 (one 503), OpenAlex 7 + 2 keyword searches, CrossRef 3 keyword
searches -- no hit for any distinctive phrase (the "resolutione di costoro" IA hit is Caterina Sforza documents, a
generic phrase; "inclinatione" alone was a deliberately broad control word); Semantic Scholar blocked (HTTP 429, not
retried). The tools' blindness is itself a finding: none of them indexes a blog comment thread, which is where the
prior reading was. Archives at Yale finding aid `archives.yale.edu/repositories/11/archival_objects/2787659`: curl 202,
browser 503 -- unreachable, logged. Web search: 2 queries (the Tomokiyo phrase: no hit; the sender/recipient/date query:
the Cipherbrain post). Requests: be-api.us.archive.org 7, www.googleapis.com 7, api.openalex.org 9, api.crossref.org 3,
api.semanticscholar.org 1, archives.yale.edu 2, scienceblogs.de 1.

**Class: N0** -- plaintext and decipherment of this very item already known (Cipherbrain comments #7-#13, 24 March 2017,
under Domnina's 2016 key). **Key source: `published`** (Domnina 2015, corrected 2016). **Text: known.**
Our decode is an independent re-decipherment under the same published key (the runner's notes show no sight of the
Cipherbrain thread), so it is at most a corroboration of the 2017 reading; the rest of this audit grades what, if
anything, is ours beyond it.

(Sections 2-5 follow: key re-derivation, controls, reading against the 2017 text, verdict.)
