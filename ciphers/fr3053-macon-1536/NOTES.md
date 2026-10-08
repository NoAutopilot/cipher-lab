found-solved
D. Bourdeau, cyphersolver `targets/rome1536/` (NOTES.md, README.md row, `pass5/gallica_views.md`; fresh clone 1fb3c46, 7 Oct 2026) read by this worker: DECODE R4233 (fr.3053 f.6ff., "Rome le xxvi^e jour de Janvier 1536" o.s.) read ~95 % and R4234 (f.16ff., Feb 1536 o.s., view 34 = f.17r) ~94 % on 21-22 Sept 2026; Ribier, Lettres et mémoires d'Estat i (archive.org bub_gb_Tbs9UbObcPUC, bub_gb_bOnmNv2ZLVoC, djvu grep "Mascon"/"1536") and Correspondance du cardinal Jean du Bellay ii (correspondancedu0002dube, be-api full-text search "Mascon") also searched, no printing of these dispatches.

# BnF fr.3053 (Gallica btv1b90601432) canvases 16 and 34: Charles Hémard de Denonville, cardinal of Mâcon, Rome, to Anne de Montmorency, Jan-Feb 1537 (n.s.)

- Checked by KH-CS3 (account 2, session_01NaTaidASRG7Yz1ytE9HkMT), 02:2x-02:3x UTC 8 Oct 2026 by date -u, brief
  `.claude/briefs/runs/2026-10-08-acct3-scout-jobs.md` section KH-CS3 (c), following `.claude/briefs/check-solved.md`.
  This is not Gramont; SA-G3's line in `ciphers/fr2980-gramont/NOTES.md` is corrected to match.
- **Foliation.** The manifest's canvas labels are all "NP" (`sources/gallica-manifests/btv1b90601432.json`, 162
  canvases), so they give no folio. The mapping below comes from SA-G3's leaf stamps (c16 = "7", c34 = "17") and
  Bourdeau's view map (`pass5/gallica_views.md`: f.16r = view 32, f.17r = view 34). No image was viewed this pass.
  - Canvas 34 = f.17r, inside R4234: BnF item 5, f.16, "A Rome, le IXe jour de febvrier 1536". DECODE dates it to
    February 1536 o.s., which is 1537 n.s.
  - Canvas 16 = f.7, inside R4233: BnF item 3, f.6, "A Rome, le XXIXe jour de janvier 1536". Bourdeau reads the date
    on the leaf as "xxvi^e"; the two dates disagree and are logged here, not settled.
- **BnF finding aid** (archivesetmanuscrits.bnf.fr ark cc49513k, FRBNFEAD000049513, one request 8 Oct 2026): "Dépêche,
  avec chiffre, de CHARLES, « cardinal de Mascon... à monseigneur de Montmorency,... A Rome, le XXIXe jour de janvier
  1536 »" (Fol. 6, item 3); "Dépêche, avec chiffre, de CHARLES, « cardinal de Mascon », à monseigneur de Montmorency.
  « A Rome, le IXe jour de febvrier 1536 »" (Fol. 16, item 5).

## Verdict (KH-CS3, 8 Oct 2026): found-solved

Both canvases sit inside letters that Daniel Bourdeau has already read. The key is "Mascon's cipher" (S. Tomokiyo,
reconstructed from fr.3053; re-tabulated by G. Lasry 2023, table for fr.3071 f.9).

Bourdeau's README row, quoted verbatim: "Charles Hémard de Denonville, bishop and then cardinal of Mâcon (Rome,
Orvieto) → Anne de Montmorency, eight ciphered letters, BnF Français 3053 ff. 6, 16, 21, 32, 35, 40, 77, 85 (DECODE
R4233, R4234, R4235, R4238, R4239, R4240, R4247, R4248; catalogue 180, class A) | Sept 1536 – 6 Apr 1537 |
21 Sept 2026 | partial | ... **Pass 5 (22 Sept)**: ... ~95 % of all cipher letters read, CER 3-8 % vs contemporary
clear texts".

His pass-5 table gives R4233 at ~95 % (1,904/2,006 letters, four contemporary glosses) and R4234 at ~94 % (5,369
letters, an f.18bis clear copy and an f.18v margin). DECODE R4233/R4234 read "Partially decrypted".

Who did not know (F-class per README): our SA-G3 screen of 7 Oct 2026 flagged c16/c34 as "unread sibling" with "key
unknown". Neither Tomokiyo (francis.htm l.290: "contains many letters (1535-1537) partially in cipher from Charles de
Hémard de Denonville, Bishop (Cardinal) of Mâcon [Mascon] ... ambassador in Rome, to Montmorency") nor the DECODE
listing gives plaintext; Bourdeau's repository does.

What this leaves to hand on: nothing to read on c16/c34. Any later reading of these leaves would be N0. Bourdeau's
own "Open" line names ~5 % ambiguous sign runs, some names, and "the f. 85 key not tabulated". Those are his and are
not taken here (CLAUDE.md, Accounts / credit rule 8).

One-line suggestion (not started, rule 7). The finding aid lists further "avec chiffre" dispatches from Mâcon to
Montmorency that are not among Bourdeau's eight records: ff.26 (1 Apr 1537), 29 (14 Apr 1537), 51 (18 Nov 1536),
58 (28 Oct 1536), 62 (9 Nov 1536), 64 (11 Nov 1536), 75 (23 Mar 1535) and 67 (Rodez and Lavaur copy, 9 Feb 1536).
Some may be among DECODE R4236/R4237/R4241-R4246, which Bourdeau's eight do not include. A check-solved of those
folios against DECODE and Bourdeau's catalogue (catalogue_additions.md) would cost about USD 1.5; next step only if the
orchestrator wants it.

## Premise check (KH-CS3, 8 Oct 2026)
- (a) folder's own mentions: no prior folder. SA-G3's line (fr2980-gramont NOTES) said "no decipherment seen on c34,
  marginal/inline text on c16 unchecked". Bourdeau names six contemporary marginal or interlinear decipherments in the
  volume (f.18v margin, f.18bis clear copy, glosses on R4233). **Found:** the "inline text" SA-G3 left unchecked is
  plausibly one of these. Not viewed this pass (brief: no image views).
- (b) other solvers' working files: **found**, Bourdeau `targets/rome1536/` R4233.md, R4234*.md, pass5/R4233_pass5.md,
  pass5/R4234_pass5.md, shapedec.py (key run on this very text). Aymeloglu: no fr.3053 row (grep of the clone at d2800bb).
- (c) physical neighbours: per Bourdeau, f.18bis is a bound clear copy of R4234 P15 and f.18v carries a margin
  gloss (views 37-38). Not re-viewed.
- (d) recipient's side: Ribier i and Du Bellay ii (above) do not print these dispatches. They only mention Mâcon
  (Ribier's "Mascon" hits are later letters co-signed with de Selve).

## Intake gate
`python3 tools/intake_gate_check.py fr3053-macon-1536` (KH-CS3, 8 Oct 2026):
```
fr3053-macon-1536: found-solved (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## Web and blog check (KH-CS3, 8 Oct 2026)
1. `cardinal de Mâcon Montmorency 1537 lettres chiffrées BnF fr. 3053 déchiffrement`: CCFr records, Desenclos and Lasry
   2024 (1592 Nevers letter), Biblissima fr.3021, an ARCSI bulletin. Nothing on fr.3053.
2. `"Mascon's cipher" Tomokiyo fr.3053 Denonville Rome 1536`: HistoCrypt papers (Lasry, Sennecey), Cipherbrain posts
   on Louis XIII and Biermann, a TNA blog. Nothing on fr.3053; the Cipherbrain hits are other letters.
3. Tomokiyo's francis.htm read on disk (`sources/cryptiana/web/francis.htm` l.288-290). Bourdeau's write-up
   (dbourdeau.github.io/cyphersolver/rome1536.html) is the public reading, read via the repository clone.
4. Desenclos open texts on disk (grep `3053|Denonville|cardinal de M[aâ]con|Mascon`): 0 hits.
Cipher Mysteries and the Cryptiana blog: no hit from the site-restricted searches run for fr.3988 the same session.
No separate site search was run for this target, because the found-solved verdict rests on Bourdeau's repository,
not on absence.

Requests (fr.3053 part): archivesetmanuscrits.bnf.fr 1; archive.org 7 (advancedsearch 2, djvu 3, be-api fts 2,
plus 3 malformed fts calls that returned non-JSON); no Gallica image requests.
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0); S. Tomokiyo; G. Lasry. No classification of novelty here (rule 10).
