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
