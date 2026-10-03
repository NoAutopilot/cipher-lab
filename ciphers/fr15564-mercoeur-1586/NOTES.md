blocked

# Anonymous cipher to the Duc de Mercœur, "ce xxvj juin" c.1586 — BnF fr. 15564 f.151

QUEUE row: CS2-03 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 13 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026
by LANE N3 csCS2c (session_0113dPptSGXZiBF5uwvtKmtc), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2c.md`.

## What it is

Bourdeau's catalogue: "Anonymous to the Duke of Mercoeur, c.1586 ('ce xxvj juin'), attempted, open (too short
for ciphertext-only; not Lasry/Mayenne-Forget/Clair.357 keys)." Prior scout pass (24 Sept 2026, scCS2) marked
the image route "not captured this pass... ark not confirmed" and the row "copy-order (unconfirmed)."

## Image route (confirmed copy-free, this pass)

Gallica SRU (`dc.type all "manuscrit"` scoped to "Français 15564") returns one manuscript record: ark
`btv1b9064027v`, 154 feuillets, creator field "Catherine de Médicis... Auteur de lettres" (a cataloguing
artifact — the volume is a recueil of many hands, not letters by her). IIIF manifest confirms 171 canvases, all
labelled "NP" (no per-canvas foliation in the manifest — this volume needs eye-checked anchors like fr.16092,
CLAUDE.md's Access playbook). Canvas index 150 (`@id .../canvas/f151`) serves at full resolution (info.json:
8936×6606, level2 profile) — **image is online now**, full size. Canvas-to-manuscript-foliation offset for this
volume is **not** independently verified (the "f151" in the IIIF id is Gallica's own sequential view number, not
confirmed against the catalogue's own foliation) — flagged for whoever fetches the actual leaf.

The BnF catalogue's own description of fr.15564 (read via the same SRU record) names, among the volume's
contents: "Dépêches orig. chiffrées, non signées, adressées à Mr de Mercoeur probablement par le duc Henri de
Guise (**f. 27, 78, 119 et 142**)." **This list does not include f.151.** The catalogue note is introductory
("on remarque..."), not necessarily exhaustive, so this is not a contradiction of Bourdeau's f.151 citation, but
it is not a confirmation either — no source read this pass names a ciphered item at f.151 specifically.

## Six-source search log (24 September 2026)

1. **Standard printed edition / calendar for the date.** Searched for a printed edition of (a) the Duc de
   Mercœur's correspondence and (b) Henri de Guise's correspondence (the catalogue's probable-sender guess).
   Located Gaston de Carné, *Documents sur la Ligue en Bretagne: Correspondance du duc de Mercœur et des
   ligueurs bretons avec l'Espagne* (Archives de Bretagne t. XI-XII, 1899, on Gallica: `bpt6k109957t`,
   `bpt6k1099586`) — but this edition's own correspondence run is **1589-1598**, after this target's c.1586
   date; it does not cover the window. No printed edition of Henri de Guise's own letters was located (only
   scattered manuscript-collection catalogue entries and auction-house single-letter listings). **No standard
   edition or calendar covering a June 1586 letter to Mercœur was found or read.**
2. **Tomokiyo / Cryptiana.** Not checked directly this pass (WebSearch of `cryptiana.web.fc2.com` + "Mercoeur"
   / "Mercœur" returned no relevant hit; not independently fetched from the live site).
3. **DECODE.** No local `sources/decode/` file for this item; not checked (DECODE login is the DECODE worker's
   alone per COMMON rules).
4. **Solver repositories.** Bourdeau's own catalogue entry (above) is the only source read; his own note says
   "attempted, open" and lists three tried keys that do not fit (Lasry, Mayenne-Forget, Clairambault 357) — no
   claim of a solution. Aymeloglu's repository not checked this pass (budget).
5. **Comment threads / general web.** One WebSearch ("duc de Mercoeur" 1586 lettre chiffre déchiffrée Guise
   correspondance) surfaced only the Carné edition (above, wrong date range) and unrelated manuscript catalogue
   entries; no decipherment or key claim found for this letter.

## Verdict: `blocked`

Per the LANE N3 addition of 24 Sept 2026 (csCS2a lesson) and the widened rule of the same date: an `open`
verdict requires NOTES.md to name the edition volume and pages actually read for the date, and "not located
this pass" is `blocked`, never `open`. No standard edition covering June 1586 correspondence to Mercœur or from
Guise was located despite a genuine search (item 1 above). **No nomination line posted for this row.** The image
route is copy-free (confirmed, ark and full-resolution canvas above) should this target be revisited once an
edition is found, or for a recovery-lane worker checking whether f.151 is even genuinely one of the ciphered
items (the catalogue's own list of ciphered Mercœur dispatches does not include it).

Rule 10: no novelty claim made. Not decoded, not transcribed (out of scope for check-solved).

Requests this pass: gallica.bnf.fr SRU 2, manifest 1, info.json 1 (4 total, well under this brief's <=25 cap;
see `fr3984-sega-1593/NOTES.md` for this session's full Gallica request accounting, since the same worker's
Part B leaf check used most of the remaining budget). WebSearch 2. No DECODE, no solver-repo clone this pass.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/mercoeur1586/NOTES.md
- Their extent, in their words: attempted, closed unread; clear frame transcribed, cipher not read (catalogue 13)
- Their date: 21 Sept 2026
- Note: their target folder not cited in our NOTES.md (catalogue item 13 is)
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (CS-BATCH1, 3 Oct 2026)

Queries (WebSearch, standard, 3 Oct 2026): (1) `Mercoeur 1586 lettre chiffrée Guise "15564" déchiffrement` -> Loria 2023 PDF, HistoCrypt papers, Morgan, museeprotestant Guise genealogy: no reading of f.151; (2) `Nevers/Mercoeur/... cryptiana.blogspot.com` variants (four searches): no hit on the Cryptiana blog itself via the search engine. Local snapshots read instead by this worker: `sources/cryptiana/web/henryiii.htm` (section "BnF fr. 15564", "f.151"), `unsolved.htm`, `GL.htm` ("Duke of Guise? in BnF fr.15564 and fr.15565"), `blog/2018_12_undeciphered-letters-from-duke-of-guise.html`. Tomokiyo, unsolved.htm: "In 2022, George Lasry solved it ... He also found there is a short ciphertext in f.151 ... He says it does not decipher with the same key and is probably too short for cryptanalysis." henryiii.htm, f.151: "Undeciphered. Dated \"ce xxvje juin.\" Endorsed \"A Monseigneur / Monseigneur le Duc de Mercoeur\"". Cipherbrain, Cipher Mysteries and the live Cryptiana blog comment threads: not opened this pass (search engine returned no page for them; no live fetch run). Not found: any decipherment of f.151.

## Premise check (CS-BATCH1, 3 Oct 2026)

(a) Folder's own files: NOTES.md named only Bourdeau's "attempted, open" and the catalogue's ciphered list (f.27, 78, 119, 142); no decipherment mentioned. Not found.
(b) Other solvers' working files: Tomokiyo/Lasry solved f.27, f.78, f.119, f.142 of this volume (and fr.15565 ff.105, 122, same key; solution printed on GL.htm, "nomenclature symbols appear to be Roman numerals") -- that key is on hand and Lasry reports f.151 does NOT decipher under it. Bourdeau (`targets/mercoeur1586`, 21 Sept 2026): clear frame transcribed, cipher not read, Lasry/Mayenne-Forget/Clair.357 keys tried. Found for the neighbouring letters, not found for f.151.
(c) Physical neighbours/facing page/slips: not viewed (no vision calls in this brief). Unreachable-by-brief; image is online (ark btv1b9064027v, canvas f151, 8936x6606).
(d) Recipient side: Carne, Documents sur la Ligue en Bretagne (1899) covers 1589-1598 only (no date overlap). Not found.
Open point: the earlier note that the catalogue lists no f.151 is answered by Tomokiyo/Lasry, who do record a short ciphertext at f.151.

## While waiting

The one action that depends on nobody: count the f.151 cipher signs from the Gallica canvas (one native crop, one vision call, ~USD 2.5) to see whether it is long enough for any test, and list its sign inventory against the Lasry fr.15564 key's inventory (GL.htm). Status stays `blocked` (no printed edition exists for an anonymous letter; Tomokiyo is the nearest index).

## f.151 sign count and inventory against Lasry's key (MERC151, 3 Oct 2026)

Intake gate (3 Oct 2026, 14:58 UTC): `python3 tools/intake_gate_check.py fr15564-mercoeur-1586` ->
`fr15564-mercoeur-1586: blocked (line 1) -- already terminal, nothing to gate`, exit 0. Status stays `blocked`; this
is an image check (sign count and inventory), no decoding was attempted.

**Leaf located.** f.151 is canvas **f164** of ark `btv1b9064027v` (each canvas is an opening; the leaf is a narrow
slip pasted on the right page, ink foliation "151" at its top right, a later number "226" below the text, monogram
"MR" under it). Anchors read by eye this pass: canvas f157 = f.144 (right page, foliation "144"/"222"), f163 = f.150
("150"/"224"). The earlier guess "canvas index 150 / f151" in this file and Tomokiyo's HTML comment "p.166" both miss
it in the current manifest. Region and crops:

    python3 tools/iiif_lines.py --ark btv1b9064027v --canvas 164 --region 4800,2950,4135,1100 \
      --out ciphers/fr15564-mercoeur-1586/images --prefix f151 \
      --centres 225,307,389,471,553,635,717,799,881 --lines-per-crop 3 --top-margin 50 --bottom-margin 60 --debug

(6 crops, 3 lines each; the autocorrelation centres missed lines, so centres were set by eye from the row profile.)

**What the leaf is.** Not a wholly enciphered letter: nine short cipher spans set inside clear French ("Tout a esté
[cipher] ... Toutes choses y estans disposées et preparées ainsi que i'estime que vous aurez esté advertys [cipher]
... Je regrette infiniment nre malheur [cipher] ... Je ne faudray de vous tenir advertys de tout plus tost [par]
homme exprès [cipher] ... Mais nous avons depuis estimé qu'il viendra plus à propos d'attendre encores un peu ...
Ce xxvj(e) Juin"). The clear words are a reading of one pass, grade M, recorded only as context for the spans.

**Count (one Opus read, grade M, no second pass).** `f151_read1.tsv`: **220 cipher signs in 9 spans (9-43 signs
each), 41 distinct sign labels, 5 singletons**; commonest y 16, '#' (double-barred cross) 12, o 12, L 11, v 11,
3 (z-tail) 11, 4 10, r 10. Read once: the count is +/- about 10%, and labels are this reader's ad-hoc names.
Cost per 100 signs: the orchestrator's `get_session` figure / 2.2.

**Lasry's key on disk.** `sources/cryptiana/web/GL/GL_BnFfr15564.png` (fetched 3 Oct 2026, the image GL.htm embeds;
README row added) transcribed to `key_lasry_gl.tsv`: 22 letters with 66 homophones, 17 nomenclator values (18 glyphs,
DE AU LA ET DES QUE LES MON LE QUI POUR PAR VOUS ILS/NOUS NOUS LEUR SON, most of them 'ff'/'7'-headed groups, the
"Roman numerals" Tomokiyo mentions), 13 "Unknown" signs. Values H as printed (Lasry 29 May 2022, published by Tomokiyo);
glyph descriptions M (600 px image).

**Inventory comparison (by eye, not by a shared sign atlas).** About 12 of f.151's 41 types have a look-alike in the
key (digit and letter shapes 2 3 4 6 7 8, y, v, '#', 'ff', a 'pi'/'P'-like sign, an 'S'-like sign). About 15 have no
evident counterpart in the key image: Greek-letter shapes (delta, open square, beta, omega, phi, lambda, mu, epsilon),
capitals T R X M N G, '=', dotted 'i' separators. 'ff' occurs 4 times on f.151 (S2, S3), and 'ff'-headed groups are the
key's nomenclator form -- the one shared feature of design visible at this resolution. Taken with Lasry's report that
f.151 does not read under this key, the inventory looks partly or wholly different; a same-scale glyph sheet is what
would settle the overlap, not this description.

**Long enough for a test?** N = 220, K about 41, French, mixed clear/cipher with a probable small nomenclator. Rule 3:
any solver run needs first a matched control -- `tools/family_run.py` homophonic at N=220, K=41, fr16 corpus, signs
split into 9 spans of the same lengths, injected error bracketing a one-pass read (10-15%, rule 3 SALV-DIAG clause).
Prior curves (CLAUDE.md rule 3: simple substitution reads 99.7% at N=720; code+mark 22-67% at N=720) make a pass at
N=220/K=41 unlikely; the clear frame is the better lever (cribs at known positions: e.g. S5 follows "nre malheur",
S9 precedes "en qui nous esperons beaucoup"), but a crib loop needs its own matched control too.

## While waiting (updated MERC151, 3 Oct 2026)

Next step that depends on nobody: a second blind read of the six f.151 crops and a reconcile against
`f151_read1.tsv` (2 Opus calls, ~USD 3), then the rule-3 control above (`family_run.py` homophonic, N=220, K=41,
fr16, offline, ~USD 1) before any target run; a control below gate logs f.151 as too-short for that family.
