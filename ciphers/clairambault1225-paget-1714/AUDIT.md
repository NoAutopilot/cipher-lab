# AUDIT 1 (A3V-VPAG, 4 Oct 2026): Paget's two cipher letters, Genoa, 8 Apr and 28 Aug 1714 (BnF Clairambault 1225, canvases f60-f66)

Verifier: A3V-VPAG (account 3 worker for LANE-A3V), a session separate from every solver of this item (OX-PAG*, NEXT-PAG,
NEXT2-PAG, PAGET-KEY, A2-PAG*, READ2-PAG, RUN1-PAG, RUN2-PAG) and from A3V-RD7. First audit of this folder. 4 Oct 2026, 03:34-03:43 UTC.

**Gate.** RD7-2026-10-04.md (A3V-RD7) verdict **same** (0 of 505 tokens differ), so the audit proceeds. Caveat: that re-derivation
covers the RUN1-PAG state (H 64 S 31 M 397 I 7 U 6). RUN2-PAG changed the reading after it (4 Oct 03:25, commit 77c79ae1: 7 codes
settled, 40 tokens M->S), and `tools/decode_key.py ciphers/clairambault1225-paget-1714 --check` now reads
`tokens 505: H 64, I 7, M 357, S 71, U 6`, `reading up to date`. The RUN2 state has had no fresh rule-7 re-derivation; it is owed
before stage 9 (found, not applied). It does not move the class below, which rests on the leaves, not on our key.

## 1. Extract

| field | value |
|---|---|
| items | Letter 1, "A Gennes le 8e Avril 1714" (f60R-f65L); Letter 2, "a Genes le 28 aoust 1714" (f65R-f66R) |
| sender | "Paget", signed; Pierre Paget, acting at Genoa for consul Aubert, consul at Cagliari from 1714 (Mézin 1998; Ulbert 2019, per OX-PAGK). **Not Lord Paget** -- see postmortem |
| recipient | unnamed "Monseigneur ... Vostre Excellence"; the Marine B7 calendars (below) file Paget's Genoa letters of 1713-14 as letters received by the Marine, i.e. Pontchartrain's office (inferred, not on the leaves) |
| shelfmark | BnF Clairambault 1225, fol. 48 dossier ("lettres autogr. de Paget, avec chiffre, 1714"), Gallica ark:/12148/btv1b9001034d, canvases f60-f66; old-series stamps 239-281 on the leaves |
| cipher | syllabic nomenclator, 505 cipher tokens, codes 1-~250 |
| on the leaves | a period interlinear decipherment written above the cipher runs: 501 of 505 tokens sit under it (NEXT-PAG, one reader); only f66L `400 4 19 600` is unglossed |
| our reading | key.tsv 114 codes rebuilt from that gloss + homophone/Gibbs/settle passes; per token H 64, S 71, M 357, I 7, U 6 (firm H+C+S 135/505) |
| distinctive plaintext (gloss) | "la Princesse de Parme et ses 2 oncles"; "le Prince Antoine de Parme"; "quoyque ce Dernier Duc n'ait que 36"; "a toujours esté de genie Allemand"; "Labbe Lomeliny"; "a la vente de cette isle" |
| solver searches (from NOTES) | 23 & 25 Sept check-solved (web, RIDA XIX ContentSearch, cryptiana, DECODE cache, both solver repos); OX-PAGK (Mézin, Ulbert, AN Marine B7 identification, LOCAL-QUEUE L11); A2-PAG print_check (16 phrases, IA/GB/OpenAlex/S2/CrossRef, HAL, Persée, GB by hand); NEXT2-PAG web + 3 blogs; PAGET-KEY premise check (repos, neighbours, recipient side). No JSTOR row was ever queued. |

**By eye (this session).** `images/f66R.jpg`, top 17%: "quoyque ce Dernier Duc n'ait que 36" written above
`77.87.45.176.34.45.90.32.41.97.56.38.47.204.36.`, and "le Prince Antoine de Parme" above `146.198.56.41.235.38.175.87.201.156.35.`,
same ink, on the line above each cipher run. The gloss is on the item itself; NEXT-PAG's coverage statement holds on the lines checked.

## 2. Independent searches (4 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical series | AN Marine sous-série B7 calendar: Taillemite, *Inventaire des archives de la marine, B7*, t.2 (arts. 21-47, 1964; IA `inventairedesarc02arch`, be-api fts scoped to the item, 11 queries) and the 1980 volume (GB `yX0iAAAAMAAJ`, snippets) | t.2 calendars Paget's Genoa letters of 16 and 30 Dec 1713, 27 Jan, 3, 9 and 20 Feb, Mar 1714 (Sardinia, the cadi, Peterborough) and Cagliari letters of 1715; summaries of other senders on 8 Apr and 28 Aug 1714, and a Genoa entry on the Tursi galleys carrying "la nouvelle reine" (F° 261v). No entry for Paget 8 Apr or 28 Aug 1714 surfaced in the fts snippets (snippets are capped; not conclusive). The 1980 volume calendars outgoing letters to Paget ("il est nommé consul de France en Sardaigne ... provisions de consul", 3 Oct [1714]). Calendar paraphrase only; no text of the cipher passages. TNA Discovery API: "Paget Genoa" 1714, all holders, 0 records; SP series 0. |
| (b) sender/recipient printed correspondence | no edition of Pierre Paget's letters exists that any search found; Pontchartrain's incoming consular letters for 1714 unprinted (PAGET-KEY premise check, not contradicted); IA fts "Paget" + "princesse de Parme": hits only the B7 inventory and Saint-Simon | none |
| (c) documentary editions | IA fts on the gloss phrases ("quoyque ce dernier duc" 0; "genie allemand" + "duchesse de Parme": Saint-Simon's own text, already logged by A2-PAG as a parallel phrase); RIDA XIX (searched by CX2-MISC2, not repeated) | no print of the letters |
| (d) holding archive | BnF catalogue notice cc137837/cd0e29423 (as logged: "lettres autogr. de Paget, avec chiffre"); GB "Clairambault 1225": 14 vols cite other folios (144, 141, 122-140), none fol. 48 / Paget | catalogue entry only |
| (e) IA / HathiTrust / Google Books | IA fts 6 global queries (Paget+Gênes+1714+chiffre; Paget+princesse de Parme; "quoyque ce dernier duc"; Paget+Cagliari+consul; Lomellini+Paget); GB 7 queries (Paget+Cagliari: 503, not retried; Paget+princesse de Parme; "Clairambault 1225"; Paget+Lomellini; Paget+vente+Sardaigne; Paget+"provisions de consul" + volume record); HathiTrust full text unreachable from the cloud (not tried) | only the B7 calendars, Mézin's dictionary, Saint-Simon |
| (f) solver repos / blogs | fresh shallow clones: dbourdeau/cyphersolver a439937 (3 Oct 2026), aaymeloglu/unsolved-ciphers d2800bb (27 Sept); grep paget / btv1b9001034d / "clairambault 1225" | Bourdeau: catalogue lines only (bnf_candidates.txt, sru_chiffre_desc.json; the research/top50 hits are a JS string "setPageType"); his other Pagets are Charles Paget (sp53, stafford1586). Aymeloglu: false hit. Blogs: NEXT2-PAG's 2 Oct pass accepted, not repeated |
| (g) scholarship | OpenAlex 2 (Paget consul Cagliari: 4 works, none; Elisabeth Farnese consul Genoa 1714: 5 works, none -- nearest "Napoli e Sicilia dopo Utrecht e Rastatt", 2022, not this letter); CrossRef 1 (noise; nearest Lavie, consul in Russia 1714); HAL 1 (0); JSTOR: 4 rows queued below (none existed) | none |

Requests: be-api.us.archive.org 17, archive.org 2 (metadata, djvu 0-byte), www.googleapis.com 8 (1 HTTP 503), api.openalex.org 2,
api.crossref.org 1, api.archives-ouvertes.fr 1, discovery.nationalarchives.gov.uk 2, github.com 2 clones. Subagents 0.

## 3. Classification

**N0** -- plaintext and decipherment of this very item already known: the period interlinear decipherment on the leaves covers
501 of 505 cipher tokens (both letters). Our work re-reads that gloss and rebuilds the code table from it; it adds no plaintext the
leaves do not already carry. The one unglossed run (f66L `400 4 19 600`, 4 tokens, "une complaisance aveugle pour [...]") is U in our
reading too: nothing new is read there.

| field | value |
|---|---|
| prior plaintext | yes -- on the leaves themselves (contemporary, 1714). In print: no text of the cipher passages located; the Marine B7 calendar prints summaries of Paget's neighbouring letters, not these two (fts, conditional) |
| prior decipherment | yes -- the period interlinear decipherment on the leaves |
| evidence quality | gloss placement read from the images by one reader (NEXT-PAG) + this audit's own look at f66R; per-letter alignment controls passed (PAGET-KEY) |
| confidence | high for N0 (the basis is on the item, seen by eye) |
| key source | **period** (rebuilt by us from the period interlinear decipherment: H/C rows); the S values on 13 codes (RUN1-PAG 6: 32 c, 47 t, 145 la, 175 ne, 212 re, 221 se; RUN2-PAG 7: 31 b, 45 r, 48 u, 97 en, 148 lo, 176 ni, 204 que) and the READ2-PAG homophone picks are `ours` (cryptanalytic segmentation of the gloss chunks, control-backed). Text: known (on the leaf, not in print) |
| safe sentence | "Both 1714 Paget letters in Clairambault 1225 carry their own period interlinear decipherment over 501 of 505 cipher tokens; we rebuilt the nomenclator's code table (114 codes) from that gloss, which gives no new text -- N0, a period key reconstruction." |
| unsafe sentence | "We deciphered Lord Paget's 1714 cipher letters" (wrong person; the plaintext is the period clerk's, on the leaf; "deciphered" without that qualifier over-claims) |

## 4. Postmortem

- **Over-claim found in the job brief, not in the folder:** `.claude/briefs/runs/2026-10-04-acct3-a3v-wave2.md` line 41 calls the writer
  "Lord Paget" and names the Paget papers (BL Add MS / Staffordshire RO). The writer is Pierre Paget, French acting consul at Genoa, consul at
  Cagliari from 1714 (Mézin 1998; Ulbert 2019; the Marine B7 calendar's "le s. Paget (Gênes)" / "(Cagliari)"); the English Barons Paget
  (William d. 1713, Henry 7th Baron) are ruled out by the folder since 25 Sept. TNA Discovery was searched anyway (0). Found, not applied
  (a lane brief is the lane's file); repeat it nowhere outward.
- **PROGRESS.tsv row was stale**: it read "period gloss: H 71 M 422 I 7 U 5", firm 71 (the PAGET-KEY state of 2 Oct). Current decode
  (`--check`, this session, after RUN2-PAG): H 64 S 71 M 357 I 7 U 6, firm 135. Row corrected from this file.
- **Rule 7 owed**: RUN2-PAG's change (03:25) post-dates A3V-RD7; a fresh re-derivation of the current state is owed before stage 9.
- Folder sentences checked: NOTES.md uses "read from the period interlinear decipherment" and "nothing here is claimed as new"
  throughout; no over-claiming sentence found to correct. NEAR.md has no row for this target. No SECOND-OPINIONS-QUEUE row (N0).
- Lead for the folder (not acted on): the B7 t.2 calendar entries around F° 261-265 (princesse de Parme marriage, Tursi galleys) and the
  leaves' old-series stamps 239-281 may place these two letters as extracts from AN Marine B7 22; an AN reader (LOCAL-QUEUE L11) could
  confirm whether the register keeps a deciphered copy or a summary of 8 Apr / 28 Aug 1714. That would not change N0.

# AUDIT 1 refresh (A3V3-PAGA, 4 Oct 2026, 06:12-06:3x UTC): the LANE-NEAR4 reading

Verifier: A3V3-PAGA (account 3 worker for LANE-A3V3), a session separate from every solver of this item (list above, plus N4-PAG65,
N4-PAG213, N4-PAG126, N4-RDPAG) and from A3V-VPAG. Gate: `RD7-2026-10-04-near4.md` (N4-RDPAG) rule-7 **SAME** 505/505 on the state
after commits e74d7ba7, 08cfc358, 4f027dd5; this session's `tools/decode_key.py ciphers/clairambault1225-paget-1714 --check`:
`tokens 505: H 50, I 7, M 363, S 79, U 6`, `reading up to date`. The rule-7 debt named in AUDIT 1 section 4 is paid.

## R1. Rule-10 propagation

| | AUDIT 1 (RUN2 state) | now (NEAR4 state) |
|---|---|---|
| per token | H 64, S 71, M 357, I 7, U 6 | **H 50, S 79, M 363, I 7, U 6** |
| firm H+C+S | 135/505 (26.7%) | **129/505 (25.5%)**; Letter 1 42/97 (43.3%), Letter 2 87/408 (21.3%) |
| changed values | -- | 116 g -> ge, 213 ma -> ri, 126 ch -> he, 86 da -> dame (all per token M unless settled S in exceptions.tsv); 84, 77, 158 kept their value, every token M |
| S codes `ours` | 13 (RUN1 6 + RUN2 7) | the same 13, plus per-token S rulings for 116, 158, 86 from `align/settle7_rulings.tsv` (H -> S at f66R:284, f66L:143, f66L:182, f66R:251) |

No changed value adds plaintext: every value still comes from the period gloss over the token, segmented by our alignment. The safe
sentence of AUDIT 1 stays true in every word but the count it does not state; it is re-issued below with the key size unchanged
(key.tsv 114 codes). SECOND-OPINIONS-QUEUE.tsv: no row for this target (N0), none needed. NEAR.md: no row. PROGRESS.tsv row 20 still
carried the RUN2 counts (firm 135, H 64 S 71 M 357): corrected from this file to firm 129, H 50 S 79 M 363.

## R2. The ten H -> M demotions, adjudicated on the leaves

Method: local crops of `images/f61R.jpg`, `f65L.jpg`, `f66L.jpg`, `f66R.jpg` (no network), one reader (this session). **What the leaf
shows first:** the period gloss is written phrase by phrase on the line above each cipher run, often starting left of the first numeral
("Il n'est pas marie et n'a" over `41.96.200.155.213.34.52.174`; "agee de 44 ans" over `30.116.34.87.44.30.41.46`); it does not sit
letter-group over numeral. So no token's "chunk" is read off the leaf by placement; every per-token chunk is an alignment inference
from the phrase plus the firm neighbours. The verdicts below say whether that inference, made by eye with the firm neighbours, gives the
old H value.

| # | line:pos | code | old H -> now | gloss over the run (read on the leaf) | segmentation by eye | old H supported by the gloss? |
|---|---|---|---|---|---|---|
| 1 | f66L:368 | 116 | g -> ge | "agee de 44 ans" | a(30) + ? + ? = "agee": g+ee or ge+e; f66R:99 "Mariage" = ma(155) ri(213) a(30) **ge**(116), word-final, no other token | **no** -- g needs 34 = ee; the only word-final occurrence forces ge. Demotion upheld |
| 2 | f66R:84 | 213 | ma -> ri | "Il n'est pas marie et n'a" | ma(155 H) + 213 + 34 = "marie", et(52 H) na(174 H) follow | **no** -- ma would read "mama..."; the gloss gives ri. Upheld |
| 3 | f66R:99 | 213 | ma -> ri | "pour le Mariage" | po(196 H) le(146) ma(155) **ri**(213) a(30) ge(116) | **no** -- upheld. A third 213 (f66L:276, "son Mari epousa", `41.155.213.`) also reads ri |
| 4 | f61R:34 | 84 | ce -> ce | "a la vente de cette isle" | de(87 H) + 84 + 38 + s(46) + le(146 S) = "de cette isle" | **no** -- the chunk is "cette" (84) with 38 = i; "ce" is only its prefix. Upheld |
| 5 | f66L:257 | 84 | ce -> ce | "cette mere" written directly above `84.156.212.` | **cette**(84) me(156) re(212 S) | **no** -- the gloss over 84 is the whole word "cette". Upheld |
| 6 | f65L:43 | 77 | q -> q | "penetrer ce qui" over `192.175.47.212.45.77.20.` | pe ne t re r + 77 + 20 = "ce qui": ce+qui or ceq+ui | **no** -- "q" alone leaves "ce" on no token. Upheld |
| 7 | f66R:9 | 77 | q -> q | "quoyque ce Dernier Duc n'ait que 36", gloss hand, above `77.87.45.176.34.45.90.32,41.97.56.38.47.204.36` | the clear text of f66L ends "...44 ans quoy que", so the gloss repeats the catchword; then **ce**(77) de(87 H) r(45) ni(176 S) e(34) r(45 S) = "ce Dernier" | **no** -- upheld |
| 8 | f66R:255 | 126 | ch -> he | "Madame la Duchesse qui en de la Maison" | du(90) c(32 S) **he**(126) s(46) se(221 S) = "Duchesse" | **no** -- ch reads "ducchsse". Upheld |
| 9 | f66L:186 | 126 | ch -> he | "Madame la Duchesse sa Mere qui l'a toujours" | same run, `155.86.145.90.32.126.46.221.` | **no** -- upheld |
| 10 | f66L:48 | 158 | mo -> mo | "**née** le meme mois en mil six[cens]" over `175.34.146.165.158.38.46.97.157` | ... **mo**(158) i(38) s(46), en(97) after | **yes** -- right-anchored on s and en, 158 = mo (the second occurrence, "modeste", also mo). The demotion follows settle7's two-instrument rule, not the leaf; the gloss supports the old value |

Result: 9 of 10 demotions are upheld by the leaf (the old H value is not the gloss's chunk); 1 (f66L:48, 158 mo) is a token whose old
value the gloss does support. Grading is the lane's call (this session edits neither key.tsv nor the reading).

**Findings for the lane (not applied):**
1. **77 = "ce", not "q".** Three occurrences, three glosses: "Nopces" over `177.77.46` (f66L:291-293, 177 nop, 46 s) leaves exactly
   "ce"; "ce Dernier" (f66R:9, see row 7); "penetrer ce qui" (f65L:43) reads ce + qui with 20 = qui. The key's q (graded M) fits none
   of them by eye; Gibbs's ceq/p/quoi shares are the drift around this. A one-code settle (77 ce, 20 qui) is the next step.
2. **84 is "cette" on both demoted tokens** (rows 4-5). Its other two occurrences (f65R:68 under "de cette Princesse", f66R:272 under "a
   toujours") do not read cette by eye in the committed segmentation; check whether one of them is a misread numeral before settling.
3. **34 reads "e", not "de", wherever a firm neighbour pins it**: "marie" (f66R:85), "Dernier" (f66R:13), "agee" (f66L:369, with 116 ge),
   "genie" (f66R:286, after ge 116 S, ni 176 S), "née" (f66L:45). All 17 tokens are M at "de" today.
4. **38 reads "i", not "a"**, in "isle" (f61R:35), "mois" (f66L:49) and "n'ait" (f66R:20, before t 47 and que 204 S).
5. **Gloss transcription: `align/pairs.tsv` P23 reads "ne le meme mois"; the leaf has "née le meme mois"** (f66L, gloss over
   `175.34.146...`, accent visible). The pair feeds gibbs_pass/settle7; fix the pair text before the next alignment run.
6. Transcription, not grading: f66L:189 is `20` in ciphertext.tsv; pairs.tsv P28 and the leaf (`221.220.156.212`) read **220** (the
   first 2 is faint). Image check before the next decode.

## R3. Class

**N0, re-confirmed.** The NEAR4 reading adds no plaintext the leaves do not carry, and no firm clause: the longest run of H/S tokens
is 4 (f66L "le du c de"), so there is no newly firm phrase to search. phrases.txt is unchanged since A2-PAG (18 lines), so
print_check.py was not re-run. JSTOR: AUDIT 1 queued 4 rows (2026-10-04), family (i) two ("Paget" + Gênes/Genoa/Cagliari + 1714 +
chiffre/consul; "Paget" + princesse de Parme/Farnese) and family (ii) two (bare quoted phrases "a toujours esté de genie Allemand",
"le Prince Antoine de Parme" "35 ans") -- both families present, none added. No requests to any host this session.

Key source: **period** (rebuilt by us from the leaf's own interlinear decipherment), with the 13 S codes and the settle7 per-token S
rulings `ours`. Text: known (on the leaf, not in print).

Safe sentence (re-issued): "Both 1714 Paget letters in Clairambault 1225 carry their own period interlinear decipherment over 501 of
505 cipher tokens; we rebuilt the nomenclator's code table (114 codes) from that gloss, which gives no new text -- N0, a period key
reconstruction; our key alone reads 129 of 505 tokens firmly (H 50, S 79)."
Unsafe: as AUDIT 1, plus any "deciphered" or percentage that counts the gloss's text as our reading.

## R4. Depth (rule 4a)

| letter | tokens | H | S | M | I | U | firm % | longest firm run | unread name/code vs other |
|---|---|---|---|---|---|---|---|---|---|
| L1, 8 Apr 1714 (f60R-f65L) | 97 | 15 | 27 | 53 | 0 | 2 | 43.3 | 3 | the M/U tokens are syllables and words, not name groups |
| L2, 28 Aug 1714 (f65R-f66R) | 408 | 35 | 52 | 310 | 7 | 4 | 21.3 | 4 | likewise; U = the unglossed `400 4 19 600` (f66L) |

**Depth D1 for both letters** ("fragments read" -- of our key's own reading). Check used: longest run of H/C/S tokens (3 and 4
syllable groups) against the authentication distance for a ~250-code syllabic nomenclator, far above 4 groups; no stretch qualifies,
so D2's clause is not met whatever codes repeat. The plaintext of both letters is fully available from the period gloss (N0); that is
the clerk's reading, not depth of ours. One true sentence about the content, from the gloss (for the record, not a D2 licence): in the
28 Aug 1714 letter the glossed cipher passages describe the Princess of Parma (born in October 1692), her mother the Duchess, aged 44
while the Duke "n'a que 36", and Prince Antoine de Parme, who "n'est pas marié" and has no inclination to marriage.

N0 and D1: not a unique solve; no SECOND-OPINIONS-QUEUE row; **no AUDIT 2 due.**

Postmortem: no over-claiming sentence in the folder. status.json `results` row "Paget from Genoa, 1714: first cryptanalytic attempt
negative" (25 Sept) is stale -- it describes "four interlinear glosses" and a failed crib attack, before NEXT-PAG found the gloss over
501/505 tokens; depth fields added there with a verifier note, title left for the parent to replace.
