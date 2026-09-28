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


### 2. Key re-derivation, blind (one Opus vision subagent, 2 image reads; the verifier's own 2 image reads were for section 1)

The subagent saw only the 2016 plate's key table (`verify2/plate_key_table.png`, a crop of Ill. 1), `glyphs/atlas_v2.png`
and the atlas code list, told to ignore the atlas's "(key: ...)" hints from the superseded Tomokiyo key, and never
opened `keys/` or `passes/`. Output `verify2/blind_keymatch.tsv` (34 codes: 18 H, 11 M, 5 L); comparison with the
runner's H35 map (`keys/key_domnina_2016_atlasmap.tsv`) in `verify2/keymap_compare.tsv`.

| comparison | count |
|---|---|
| runner-valued codes the blind pass also matched | **22 of 23 agree** (21 first choice, THREE l as second choice after P) |
| disagreement | 1: OMEGA2 (runner a, M; blind G, M) -- both at M; 2 signs in the letter |
| codes the runner left open (lumped) | 7: blind picks one of the runner's own candidates for NINE (e/null), TEE (p), EIGHTBAR (cc); SEVEN blind l/i vs runner e/i (the i half agrees); TWOFLAT, UCURL, CARET no comparison |
| in one list only (naming drift between atlas_v2 and the H35 map) | 8 (CIRCLE, EPSILON, HOOK, JHOOK; ECAP, ELOOP, RHO, TLOOP) |

The runner's key map is reproduced blind at the atlas-code level. The H38/H40 sub-code shape splits were not
re-derived (budget: they take per-sign crops, 116 + 43 signs); section 4 tests them against the known answer instead.

### 3. Controls re-run from the scripts on disk

| test | runner (NOTES H40/H39) | this session | files |
|---|---|---|---|
| `passes/key_domnina_test.py` v6 map, 200 shuffles, seed 7 | unigram -2.710 (0/200), bigram -2.593 (0/200), phrase distance 2 at 41 (0/200; shuffled mean 14.68) | **identical, every figure** | `verify2/rerun_v6_seed7.txt` |
| same, seed 101 (a fresh seed) | -- | unigram 0/200 (mean -3.018), bigram 0/200 (mean -3.701), phrase 0/200 (mean 14.71) | `verify2/rerun_v6_seed101.txt` |
| `tools/judge_plaintext.py specs/spinelli-beinecke-c1515.json --file reading_letters_v6.txt` | FAIL -1.334 vs real_p05 -0.968, null_p99 -1.752, N 224 | **identical** (FAIL) | `verify2/judge_rerun.json` |
| `tools/decode_key.py ... --check` | exit 0 | exit 0 ("reading up to date", H 229 M 22 U 8) | -- |

**Reproduced.** The ten-shuffle judge family control was not re-run; the known-answer control below is stronger.

### 4. The reading, line by line, against the 2017 known answer

`verify2/compare_2017.py` (regenerates `verify2/compare_2017.tsv`): the committed v6 decode against the 2017 Cipherbrain
reading (Norbert #7 p.1, Thomas #10 p.2), with the 2017 text's [bracketed] insertions and ?? dropped and u/v, i/j folded
to the decode's convention (rule 3, PX-BRODEC: one convention before diffing). Agreement = 1 - edit distance / reference
length. Control: the same statistic on 200 decodes under the values permuted among the mapped codes (seed 5). This
replaces the brief's 20-permutation model judgement: once a published plaintext exists, a scripted known-answer
diff is the stronger instrument (logged as a deviation from the brief).

| line | v6 decode | 2017 reading (normalised) | agree | shuffled mean / max | verdict |
|---|---|---|---|---|---|
| p1 1 | etlgdmitmethemadaa | et li dite che madama | 0.71 | 0.03 / 0.35 | patchy |
| p1 2 | arge?itanonuolea?e?arehlagu | Margerita non uole a(cc/rr)ettare la gu- | 0.76 | 0.11 / 0.28 | patchy |
| p1 3 | bmernat?onedispagnialthepim | -bernatione di Spagnia et che piu | 0.81 | 0.07 / 0.26 | continuous (one intruding m; "lthe" for "etche") |
| p1 4 | dintlinationesmmosraalcon?e | d'inclinatione si mos[t]ra al conte | 0.89 | 0.09 / 0.30 | continuous |
| p1 5 | palat?noteatal?trch | Palatino che ad altri | 0.61 | 0.02 / 0.28 | patchy |
| p1 6 | aciuocaroneoettrouola | arriuo caro nelo et trouo la | 0.87 | 0.12 / 0.30 | continuous |
| p1 7 | resolutionedcostoromiiore | resolutione di costoro mi[g]liore | 0.93 | 0.12 / 0.26 | continuous |
| p1 8 | dique?oelpaladomanaauua | di quelo el Papa domandaua | 0.82 | 0.08 / 0.27 | continuous letters, mis-segmented by the runner |
| p2 1 | seebisognioelguernatoredibre | se e bisognio el gubernatore di Bressa | 0.88 | 0.14 / 0.25 | continuous |
| p2 2 | uaandahaisuioreri | andarai sui ??eri | 0.62 | -0.16 / 0.15 | patchy |
| all | | | **0.809** | 0.081 / 0.183 | 0/200 shuffles at or above |

Every line beats every one of its 200 shuffles. The runner's "continuous" list (3, 7, 8, 9) is confirmed and lines 4
and 6 (0.89, 0.87) belong in it at the letter level; 1, 2, 5 and 10 are patchy, as the runner said. The Italian is
period Tuscan-Italian of the 1510s (gubernatione, bisognio, costoro, quelo) and consistent with the leaf's own clear
text, which names "il gobernatore di Brescia mio signore et amico": the cipher's p2 "el gubernatore di Bressa" is the
same office. The runner's and H42's word-level interpretations are wrong where the 2017 reading is fuller: p1 8
"el pala[tino] doman[d]a" / H42 "el pala domana (tomorrow)" is **"el Papa domandava"** (the decoded l in "pala" is
the key's p misread); p1 5 "palat[i]no te a tal" is **"Palatino che ad altri"**; p1 1 "et ... the ma" is **"et li dite
che madama"**; p2 2 "anda ha" is **"andarai"**. The subject the runner did not reach -- **Madama Margherita** (Margaret of
Austria) not accepting the governance of Spain, and more inclination shown to the Count Palatine -- is in the 2017 text.

### 5. Verdict

| field | value |
|---|---|
| Claim scope | **recovered-passages**, as an independent re-decipherment of an already-published reading; nothing outward-facing |
| Key source | **published** (Domnina 2015 Fig. 1, corrected 2016 Ill. 1); the atlas-to-cell map is ours and reproduced blind 22/23 |
| Novelty class | **N0** -- this leaf's cipher passages were deciphered with the same key in the Cipherbrain comments of 24 March 2017 (Norbert #7, Thomas #8-#13); text: **known** |
| Token grades endorsed | H 229 / M 22 / U 8 as a grading of **provenance** (the value is read from the published key via two blind passes), not of correctness: against the 2017 text the decode's letters agree 0.81 overall, so some H letters are wrong (e.g. p1 8 "pala" for "papa", p1 1 "lgdmit" for "lidite"). No C: the 2017 reading is a modern decipherment, not a period key source; it may be used as C-grade known plaintext only with that stated. |
| Reproducibility | `tools/decode_key.py --check` exit 0; the controls reproduce exactly (section 3) |
| **Safe sentence** | "Using Ekaterina Domnina's published key (2015, corrected 2016), we independently re-deciphered the two cipher passages of Tommaso Spinelli's letter of 7 September 1519 (Beinecke GEN MSS 109); they had already been deciphered with the same key by readers of Klaus Schmeh's Cipherbrain blog on 24 March 2017, and our letter-level decode agrees with that reading at 81% (200 shuffled-key decodes: mean 8%, best 18%)." |
| **Unsafe sentence** | "We have read the Spinelli cipher letter for the first time" / "a previously unread passage" / "the rest of the letter has no published reading" (Bourdeau's catalogue sentence, and INTAKE-SPINELLI's "Not found-solved", are both overtaken by the 2017 thread). |

**Postmortem.** Failure: rule 1's named family "the comment threads of the list posts (Cryptiana blog, Cipherbrain)"
was never searched for this target; INTAKE-SPINELLI's gate and 40-odd campaign steps rested on Tomokiyo's one phrase and
Bourdeau's "read in part", both of which postdate or omit the 2017 thread. One web search on sender, recipient and date
found it. Files that over-claim and need correcting by their owners (not edited here, per the brief): NOTES.md
"Gate verdict (Job 0)" ("Not found-solved"; "Tomokiyo does not print any reading ... The rest of Gen. MSS 109 has no
published reading" is true of Tomokiyo/Bourdeau but not of the leaf), the reading.txt header (should cite the 2017
reading), `reading_words.tsv` glosses "domana = tomorrow" and "pala" (the 2017 text reads "el Papa domandava").
No SECOND-OPINIONS-QUEUE row (N0). A contribution remains possible and is the orchestrator's to decide: Bourdeau's
catalogue entry for GEN MSS 109 says "Read in part"; the Cipherbrain 2017 thread is a fuller prior reading it could cite.
Requests this session are listed in section 1; vision: 2 image reads by the verifier, 2 by the blind subagent.
