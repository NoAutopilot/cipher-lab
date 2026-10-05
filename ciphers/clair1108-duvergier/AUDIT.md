# AUDIT: Vergier to Jérôme de Pontchartrain, March 1696 (BnF Clairambault 1108, fol.249-250 and fol.261v-262)

Verifier V1 for LANE V2 (Opus, cap $10), 24 Sept 2026, 08:51-09:10 UTC by `date -u`. Adversarial audit under CLAUDE.md
rule 10. No decoding done; no reading, key, ciphertext or grade changed.

Claim under audit (LANE G2, 08:27-08:38 UTC, 24 Sept 2026): "Du Vergier to Pontchartrain, 26 Mar 1696, BnF Clairambault
1108 fol.249v-250r and fol.262; the clear words written above the cipher groups are an interlinear decipherment (second
hand); key_1696.tsv built from it; reading C 584 M 82 U 1. fol.249r has no cipher (show-through of 249v)."

## 1. Verdict

| item | leaves (canvas) | cipher groups | class | prior plaintext | prior decipherment of this item | confidence |
|---|---|---|---|---|---|---|
| A. Letter dated Boulogne, 26 Mar 1696 | fol.249r (clear), 249v-250r (cipher) (canvases 252-253) | f253L + f253R, every run | **N0** | yes, in manuscript: the interlinear gloss over every cipher run; not found in print | yes, the gloss on the leaf | high |
| B. Undated letter, Boulogne (content dates it to about 20-27 Mar 1696, see s.3) | fol.261v-262r (canvas 265) | f265L + f265R except the nine groups below | **N0** | yes, in manuscript: the interlinear gloss; not found in print | yes, the gloss on the leaf | high |
| B'. The first nine groups of f265R R01 (`117 33 289 178 224 30 289 8 289`) | fol.262r | 9 | **not classified**: no reading | no gloss over them | none located | - |
| (not in the claim) fol.247v, tail of an earlier letter | canvas 251 | not transcribed | not classified | the probe image shows glosses over its cipher rows | - | - |

(a) **Coverage.** The interlinear decipherment covers every cipher run of letter A and every run of letter B except the
first nine groups of f265R R01, where the gloss begins at "M de Pontchartrain" (NOTES "Reconciliation", confirmed in
rows.tsv and reading_tokens_1696.tsv: those nine tokens are graded M 8, U 1, all other tokens C or M against the gloss).
The key's values for the nine groups spell "ce t te [178] ne s te te" (with 8 read as null "0"), which is not French; there is
no reading here to classify. The single U token in the whole reading (178) is in this span.

(b) **Print.** The item is known in print at folio level since 1879 (Boislisle), and was used, with its folio range
cited, by Mancel (1903) and La Roncière (1909); Pontchartrain's side of the same exchange is printed (Depping 1855, Mancel
1903). No printing of the deciphered text of letter A or B was found: the distinctive words of the glosses (Kent, York,
haras, Giraudin, coterie, desbauche, Myddleton) are absent from the searchable text of the two works that cite the item.
Not N1, because the plaintext was not found in print; N0 already applies because the decipherment is on the leaf.

## 2. Parties (identity check, which widened the search)

- **Sender: Jacques Vergier** (1655 or 1657-1720), poet, *commissaire de la marine*, posted to Dunkerque. He signs
  "Vergier" (no "Du"); the folder name follows the BnF finding aid's "Du Vergier". Pontchartrain sent him to Calais in
  Feb-Mar 1696 to watch James II and his court during the planned Jacobite invasion (Depping IV p.772 n.1: "Vergier, envoyé
  à Calais pour la surveiller"; Mancel 1903 pp.130-134; La Roncière VI p.216).
- **Recipient: Jérôme Phélypeaux de Pontchartrain** (1674-1747), then working in the Marine secretariat beside his father
  Louis, comte de Pontchartrain, secretary of state for the Navy. Evidence: letter B's gloss "[j'avois demandé il y a
  quelque temps] a M vostre Pere la permission de m'en retourner a Dunkerque" (f265L R13-R14), and the son's reply of 12 Mar
  1696 to Vergier, "de quelle importance il est que mon père et moy soyons informés" (Depping IV p.773 n.). The claim's
  "Pontchartrain" is right; the person is the son.
- **Context.** The Jacobite invasion attempt of Feb-Mar 1696 (James II at Calais; Middleton his secretary of state; Berwick
  sent to England). Letter A reports Middleton's view that a landing in Kent is impracticable and his plan for landings in
  Yorkshire and the West from Calais and Brest. Letter B reports Vergier's request to return to Dunkerque and his standing
  with James II.

## 3. Search log (principal families)

All on 24 Sept 2026, 08:51-09:05 UTC.

| family | searched / unreachable | what | result |
|---|---|---|---|
| Pontchartrain correspondence: Depping, *Correspondance administrative sous Louis XIV* (1850-55) | searched | IA djvu text of t.1, 3, 4 (`correspondancead01depp`, `03depp`, `04depp`) and t.2 (`correspondancead0002depp`; `correspondancead02depp` djvu returned 500), grep vergier/giraudin/middleton/"coste de Kent"/haras/coterie | **t.4 pp.772-773:** Pontchartrain to the abbé de la Trémoille 19 Feb 1696, with a footnote printing Pontchartrain (the son) to Vergier, 12 Mar 1696, which answers Vergier's letter of **7 March** (not A or B) about Middleton's "refroidissemens et irrésolutions", and a letter to Middleton. None of A's or B's plaintext. |
| Boislisle, *Correspondance des contrôleurs généraux* t.1 (1683-1699) | searched | IA `correspondancede01franuoft` djvu, same grep | 0 |
| Clément, *Lettres de Colbert* | not applicable | Colbert d. 1683; the Marine run stops before 1696 | - |
| Boislisle ed., *Mémoires de Saint-Simon* t.3 (1879) | searched | IA `memoiresdesaints03sain` djvu, grep 1108/vergier | **p.57 n.1:** "On trouvera aussi des rapports et des correspondances secrètes sur les projets de débarquement dans le ms. Clairambault 1108, fol. 245-264." Folio citation only, no text. |
| Sender-specific: Émile Mancel, "Vergier (Jacques) (1655-1720)", *Bulletin de l'Union Faulconnier* (Dunkerque), 1903, pp.109-177 (Google Books `X3M2AAAAMAAJ`, full view; offprint "Jacques Vergier, 1655-1720", Dunkerque 1903) | searched by search-inside (57 terms); page view unreachable | `books.google.com/books?id=...&jscmd=SearchWithinVolume`; the one `pg=PA130&output=text` page fetch got Google's "automated queries" 403 and was not retried | **p.130 n.3 cites "Clairambault, 1108, folios 245-264"**; pp.131-134 print Pontchartrain's letters to Vergier of 25 Feb, 12 Mar and 28 Mar 1696 (the 28 Mar one answers B: "votre séjour à Boulogne ne paraisse trop affecté ... je suis d'avis que vous retourniez à Dunkerque"); p.177 prints the instruction to Vergier of 27 Feb 1696. Terms from A's and B's glosses: Kent 2 hits (pp.533, 536, unrelated), York 0, haras 0, Giraudin 0, coterie 0, desbauche 0, honnesteté 0, Myddleton 0, "26 mars 1696" 0, "Middleton impraticable" 0. The plaintext is not quoted, as far as OCR search can show; the pages were not read in full. |
| Sender's works: *Œuvres diverses de M. Vergier* (1726-1742) | searched (Google Books API) | titles surfaced; verse, not dispatches | not relevant to the dispatches |
| Marine history: La Roncière, *Histoire de la marine française* VI (1909 `1LhVAAAAYAAJ`, 1932 `7_VpJRy1EkkC`) | searched by snippet and search-inside | "Clairambault 1108", Vergier, Kent, York, haras, Giraudin, coterie, Middleton+York/Kent/Brest | **p.216** cites "Clairambault 1108, fol. 245" and "Vergier, 25 février et 28 mars 1696; à Vergier, 27 février (Mancel ... p.25, 28, 71)"; narrative summary only; A's and B's distinctive words 0 |
| Marine series inventories (AN Marine B2/B3/B7) | partly unreachable | earlier passes (NOTES "Marine key search"): Neuville/Buche B2 inventories searched on Google Books and HTRC; SIV and archivesnationales.culture.gouv.fr egress-blocked; FranceArchives bot-blocked | no mention of Vergier's letters located; the B3 (lettres reçues) inventory was not reached |
| Recueil des instructions aux ambassadeurs | not applicable | France had no embassy in England in 1696 (war); the letters are internal Marine correspondence | - |
| BnF catalogue (archivesetmanuscrits) | from the check-solved fetch | "Fol. 245 • Du Vergier (Lettres orig., dont plusieurs avec chiffres)" | no decipherment mentioned in the entry; gallica.bnf.fr is LANE G2's host, not fetched |
| Google Books full text | searched | 19 API queries (14 on decoded phrases in 17th-c. and modern spelling, 5 on names), key + country=US | phrase queries 0 hits each: "impraticable sur la coste/côte de Kent", "haras d'Angleterre" 1696, Giraudin irlandois Dunkerque, "coterie journaliere", "l'armement de Dunkerque regarde la descente", "conduite de Calais a Dunkerque", "chevalier Giraudin" (only unrelated 1839/1886 hits); name queries led to Mancel, La Roncière, Saint-Simon, Studi francesi |
| *Studi francesi* 1979 (`stknAAAAYAAJ`, no preview), an article on Vergier's contes citing Mancel | searched inside | Clairambault 0, Kent 0, Middleton 1 (p.273: Vergier's mission to "milord Middleton, tâche dont il s'acquitte très honorablement") | biographical mention, no text |
| Internet Archive full text | searched | be-api fts: "coste de Kent" AND Vergier 0; Giraudin AND Dunkerque 0; Vergier+Middleton+Dunkerque 27 unrelated (encyclopaedias); advancedsearch for the Union Faulconnier *Bulletin* found only `bulletinvolume00dunkgoog` (1898), not 1903 | 0 relevant |
| HathiTrust | not searched this pass | Cloudflare-challenged (NOTES, 24 Sept) | - |
| Tomokiyo / Cryptiana, both solver repos, DECODE | searched (local) | `sources/cryptiana` and `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped vergier/"Clairambault 1108"/btv1b90009665; repos: fresh clones grepped earlier today by check-solved and key-search passes (NOTES), not re-cloned | 0 (DECODE's two Clairambault rows are Clair 325 and 328, 1526-28) |
| Scholarship indexes | searched / partly unreachable | CrossRef "Vergier commissaire marine Dunkerque" (nothing relevant in top 8); HAL `"Vergier" AND (Pontchartrain OR Dunkerque)` 0; OpenAlex errored twice (no `meta`, as LANE W saw a 429 at 08:50); Semantic Scholar returned no data (rate limit) | nothing |
| JSTOR | queued | 2 rows in JSTOR-QUEUE.tsv | never blocks the class |

## 4. Evidence table

| evidence | what it shows | where |
|---|---|---|
| Second-hand interlinear gloss over every cipher run of A and B, darker ink on f.265, self-corrections, consistent code values | the leaf carries a decipherment of this very item | NOTES "Reconciliation"; rows.tsv; dechiffre.tsv (51 gloss rows) |
| Nine groups at the head of f265R R01 without a gloss | the only uncovered span in A and B | rows.tsv l.112; reading_tokens_1696.tsv (8 M, 1 U) |
| Glosses on fol.247v | the earlier letter is glossed too | images/probe_f251.jpg (thumbnail, left page) |
| Boislisle, Saint-Simon III (1879) p.57 n.1 | the item cited by folio as secret reports on the landing plans | IA memoiresdesaints03sain |
| Mancel 1903 p.130 n.3, pp.131-134 | the item cited by folio; Pontchartrain's replies printed; no plaintext of A/B found | Google Books X3M2AAAAMAAJ (search-inside) |
| Depping IV (1855) pp.772-773 n. | Pontchartrain (son) to Vergier 12 Mar 1696, reply to Vergier's 7 Mar letter | IA correspondancead04depp |
| La Roncière VI (1909) p.216 | the item cited; Vergier's letters of 25 Feb and 28 Mar 1696 cited | Google Books 1LhVAAAAYAAJ |

## 5. Did we first-decipher?

**No.** Both letters were deciphered on the leaf, by the second hand that wrote the glosses. This project added the
sign-by-sign key (key_1696.tsv, 129 codes, grade C from the letter's own known plaintext), the reproducible reading
(`tools/decode_key.py ... --check`), the settlement of fol.249r as show-through, and the identification of the parties.
That is a recovery from the document, as with clair1067, not a decipherment.

Whether the gloss is contemporary is probable, not established: it uses the period's spelling (desbarquement, honnesteté,
Irlandois, estably), and a fluent reading of a 129-code syllabic nomenclator implies the key was at hand, which fits the
recipient's office. The hand has not been compared with a Marine secretariat clerk's.

## 6. Why N0, not N1 or higher

Rule 10's N0: "plaintext and decipherment of this very item already known". Precedent: clair1067-brienne-poland-1646/AUDIT.md
s.2 (an interlinear decipherment on the leaf is N0 without print), fr5160-letellier-1653, thurloe-printed P3. This item
is stronger than clair1067 on one point: the folios have been cited in print since 1879 as secret correspondence on the
landing plans, and since 1903 as Vergier's letters. N1 would need the plaintext in print; not found. N3/N4 would be false
on its own terms, because a decipherment of the item exists on the leaf.

Qualifier, to be carried wherever the class is repeated: *the known decipherment is a manuscript interlinear gloss on the
leaf; the item is cited in print (Boislisle 1879, Mancel 1903, La Roncière 1909) but its deciphered text was not found in
print; Mancel's pp.129-135 were searched by OCR, not read in full.*

## 7. Confidence

High for N0 on A and B: it rests on the leaf, and nothing found in print could move it lower than N0. Medium for "not
found in print": Mancel pp.129-135 are the one place a paraphrase could sit, and they were searched, not read; they do not
change the class either way.

## 8. Safe and unsafe sentences

**A, 26 Mar 1696.** Safe: "Vergier's cipher letter to Jérôme de Pontchartrain from Boulogne, 26 March 1696 (BnF
Clairambault 1108, fol.249-250), carries an interlinear decipherment on the leaf (N0); aligning it with the groups gives a
129-code key (grade C) that regenerates the reading. The folios are cited in print since 1879; the deciphered text was not
found in print." Unsafe: "We deciphered Vergier's letter"; "first reading of Vergier's cipher"; "unpublished intelligence
on the 1696 invasion plan".

**B, undated (c. 20-27 Mar 1696).** Safe: "A second Vergier letter from Boulogne (fol.261v-262r) is deciphered on the leaf
in the same hand (N0) except nine groups, which neither the gloss nor the key reads." Unsafe: "the whole letter is read"; "a
newly recovered letter"; "dated 26 March 1696" (it is undated; its date is inferred from Pontchartrain's reply of 28 Mar).

**B'.** Safe: "Nine groups at the head of fol.262r have no gloss and no reading." Unsafe: any reading of them.

## 9. Postmortem

The failure was a search gap, not an over-claim: no file claimed novelty. But the check-solved and key-lead passes said
"no printed edition found anywhere" and "Depping ... no volume covers Marine-department internal correspondence of the
1690s", while Depping IV prints Pontchartrain to Vergier (12 Mar 1696) in a footnote and Boislisle (1879), Mancel (1903)
and La Roncière (1909) cite this very item by folio. Those passes searched by topic and title; the item was found only by
searching the sender's name and the shelfmark in quotes ("Clairambault 1108"), and by grepping the edition's full text.
Lesson for the brief: search the shelfmark in quotes in Google Books and IA full text before calling an item uncited.

Other corrections made in place (each marked "Verifier V1, 24 Sept 2026"):
- NOTES.md, check-solved "Verdict" and "Key leads and print check": the "none found anywhere" and Depping sentences
  annotated with the citations above.
- NOTES.md, "Recipient's printed material": the heading was the sender's own printed works; annotated.
- NOTES.md, sender identification: confirmed by Depping IV and Mancel (print sources, not a web search); recipient
  specified as Jérôme de Pontchartrain.
- status.json results row: class N0, the safe sentence, and "fol.249r not yet transcribed" replaced (it was settled as
  show-through at 08:38); "contemporary decipherment" softened to "probably contemporary".

Not done (one line each): read Mancel pp.129-135 in full (Gallica or a person; the class does not depend on it); B3
(lettres reçues) inventory for a ministry copy of A or B; the nine groups of B' and fol.247v, for a solver.

Requests: www.googleapis.com 20 (19 volume queries, 1 volume record), books.google.com 78 (77 SearchWithinVolume, 1 page
fetch refused 403, not retried), archive.org 11 (4 advancedsearch, 7 djvu downloads, one 500), be-api.us.archive.org 3,
api.openalex.org 2 (errors), api.crossref.org 1, api.semanticscholar.org 1, api.archives-ouvertes.fr 1. No gallica.bnf.fr,
no logins, no subagents.

Desenclos check, 4 Oct 2026 (DESENCLOS-PREMISE, account 3): no hit. Searched 17 open full texts of the 36 items in sources/desenclos/2026-10-04/bibliography.tsv (HAL PDFs, DSpace Tartu HistoCrypt 2024/2025 PDFs, OpenEdition HTML; built from HAL, theses.fr, OpenAlex, Semantic Scholar, CrossRef, Google Books) for this item's shelfmark, sender/recipient, place and date (terms.tsv, search-log.tsv, search.py); none names this item, its key or its plaintext. Not read: her 2014 thesis (theses.fr: not online) and 2017/2021 cryptography chapters (not open; JSTOR-QUEUE rows of 4 Oct 2026).

---

## AUDIT 2 (VER1-LOWA, 5 Oct 2026)

Verifier VER1-LOWA (account 2 worker for LANE-VER1, brief `.claude/briefs/runs/2026-10-05-ytbiz-ver1-jobs.md`), 5 Oct 2026,
from 19:03 UTC by `date -u`; a session separate from the LANE G2 solver and from Audit 1 (24 Sept 2026, 08:51-09:05 UTC).
Claim under audit: Audit 1's **N0** for letters A (26 Mar 1696, fol.249v-250r) and B (undated, fol.261v-262r), B' (nine
unglossed groups) not classified; C 584, M 82, U 1 of 667; key period. No decoding.

### Rule-7 check
`python3 tools/decode_key.py ciphers/clair1108-duvergier --check` (5 Oct 2026): "signs.tsv: tokens 667: C 584, M 82, U 1 /
reading up to date". Unchanged since Audit 1.

### Search (5 Oct 2026)
The folder had no `phrases.txt`; this audit wrote one (10 runs from the gloss and the clear text of A and B, 17th-c. spelling
folded by the tool) and ran the scripted pass.

| family | searched | result |
|---|---|---|
| scripted pass | `tools/print_check.py ciphers/clair1108-duvergier --only ia-global,gbooks,openalex,crossref` (output in the session scratchpad): be-api 10, Google Books 10 (key, country=US), OpenAlex 10, CrossRef 10 | IA global 0 for every phrase. Google Books and CrossRef: loose-match counts only (dictionaries, Maintenon's letters for "voila monseigneur son projet", Grimoard's Turenne collection 1781 for the Giraudin run -- word overlap, not the phrase). No print of A's or B's gloss text. |
| (e) IA full text, by hand | be-api fts: "giraudin irlandois" (10 items: La Rochelle, Agenais bibliography, masonic, Revue d'histoire de l'Église -- none Vergier), `"coste de kent"` (3, Spanish newspapers, numismatics), "vergier middleton calais 1696" (4,220 loose; top hits La Roncière VI, already read by Audit 1, and a *Corsaires dunkerquois* title, generic) | nothing on these letters |
| Google Books, by hand | `"chevalier Giraudin"` (7: an 1839 play, Agenais bibliography -- unrelated); `"Myddleton" Vergier Boulogne 1696` 0 | 0 |
| (g) OpenAlex (errored for Audit 1) | "Vergier Pontchartrain 1696 Middleton Calais" 0; "Jacques Vergier commissaire de la marine Dunkerque" 27 (review notices, unrelated) | 0 relevant |
| (g) Semantic Scholar (rate-limited for Audit 1) | same two queries | **HTTP 429** on both, host stopped |
| (g) HAL | `"Clairambault 1108"` 0; `Vergier AND Middleton` 0 | 0 |
| (g) Persée | HTML search | not usable for a phrase test (same generic count for unrelated quoted strings) |
| sender-specific: Mancel 1903 (*Bulletin de l'Union Faulconnier*) | IA advancedsearch `title:faulconnier` and "Mancel Vergier" | **0 items on IA**; the volume remains readable only through Google Books search-inside (Audit 1: 57 terms, the gloss words absent). The pages pp.130-134 were still not read in full: a gap, not a hit. |
| JSTOR | family (ii) row appended (bare quoted phrase, no cipher keyword): "impraticable sur la coste de Kent" | queued; family (i) rows 50-51 answered, no hit on these letters |
| HathiTrust full text | not tried (Cloudflare from the cloud, standing finding) | unreachable |

### Classification (Audit 2)
- **A (fol.249v-250r, Boulogne 26 Mar 1696): N0 -- Audit 1 endorsed.** Prior decipherment: the interlinear gloss on the leaf;
  no print of the plaintext located (folio-level citations only: Boislisle 1879, Mancel 1903, La Roncière 1909).
- **B (fol.261v-262r): N0 -- Audit 1 endorsed**, except **B'** (the first nine groups of f265R R01, no gloss, no reading):
  still not classified.
- Key source **period** (rebuilt by us from the gloss); `text: known` (on the leaf).

**Depth (rule 4a), A+B as one result: D2, 87.6%** of cipher tokens C (584 of 667; no H/S; M 82, U 1). Not D3: the residue is
mostly ordinary syllable groups where the key value and the gloss part company (e.g. `143` et, `277` en, `290` ti), plus the
nine unread B' groups, not names or codes. External check: the gloss (non-statistical). Depth sentence (true, specific, from
the gloss and the C reading of A): Vergier reports Lord Middleton's view that a landing on the Kent coast had become almost
impracticable because of the forces placed there, and his plan to land instead in the province of York, "ou sont presque tous
les haras d'Angleterre", or in the West, or in both at once, embarking at Brest the troops for the West and at Calais those for
York. Outward words: "partially deciphered (about 88%)" -- by the period gloss; the safe sentences of Audit 1 s.8 govern.

**Unsafe** (added to Audit 1's): "largely deciphered" (D3 not met); any reading of B'.

### Postmortem
No over-claim found. The results row lacked depth fields and still said one audit; updated. No SECOND-OPINIONS-QUEUE row (N0).

Requests: be-api.us.archive.org 10 + 3, archive.org 2, www.googleapis.com 10 + 2, api.openalex.org 10 + 2, api.crossref.org 10,
api.semanticscholar.org 2 (429), api.archives-ouvertes.fr 2. No logins, no credentials printed.

`python3 tools/depth_check.py` (5 Oct 2026, after this audit; the item is N0, not counted): `unique solves (N3+ and D2+): 16 -- D4 1, D3 2, D2 13; not counted D0/D1: 13; legacy ungraded: 0` exit 0
