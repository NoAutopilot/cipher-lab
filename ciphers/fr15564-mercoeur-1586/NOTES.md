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
