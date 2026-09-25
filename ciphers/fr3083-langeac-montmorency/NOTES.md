found-solved

# Jean de Langeac, bishop of Avranches (French ambassador at Venice), to Anne de Montmorency — BnF fr. 3083 (QUEUE.md row D7)

DECODE record cluster: R3694 ("Non-decrypted", fr. 3083 fol. 20-21) beside R3695 ("Decrypted", fr. 3083 fol.
55). Source: QUEUE.md "Neighbour-record recovery candidates" row D7. Checked 25 Sept 2026 by LANE DX worker
NB-FI, per the neighbour check-solved brief, before any DECODE login this session (worker never logged in).

## 1. Bourdeau (dbourdeau/cyphersolver, shallow clone, 25 Sept 2026)

`grep -rli "fr\.?3083\|avranches"` over the whole clone hits `cyphersolver/gramont1529/`, dated **18 September
2026** (a week before this check), which contains `fr3083_no8_langeac.md` — a full transcription of
**exactly this letter**: "BnF fr. 3083 no. 8, f. 20-21 — Jean de Langeac, bishop of Avranches, Venice, to
Montmorency, 14 January [1529]", read off the Gallica image (ark btv1b90601328, canvas 36). Sender, receiver,
shelfmark and folio (20-21) match the cached DECODE catalogue's fields for **R3694** exactly (see §2).

Bourdeau's NOTES.md for the folder ("Gramont, Mâcon and Langeac to Montmorency, 1529-1537"):

> "Verify-first answer: four letters, four keys, all broken by Lasry in 2023 ... `fr3083_no8_langeac.md`: read
> in full apart from two short groups. Saint-Pol asks Langeac to seek his leave (congé) from the Signoria;
> Venice refuses and protests it would ruin the enterprises (Milan, Spanish money arriving, spring coming);
> Langeac has written to dissuade him. January 1529, five months before Landriano."

The key is **"Avranches' cipher 1"**, reconstructed by **George Lasry** (table dated 5 Nov 2023, on
Tomokiyo's Cryptiana page cryptiana.web.fc2.com/code/GL.htm) from other Avranches letters, refined further
in Bourdeau's own file for signs specific to this leaf (y-shaped C, ɤ = S, 9-shaped A/V, ɓ = P/I, ₠ = LL, 8∞ =
LE, macron = en). The reading gives the full text (Latin-script capitals for cipher, lower case for the
letter's own clear passages), a modern-French rendering, and dates the letter to 14 January 1529 from
internal content (Saint-Pol's command in Lombardy, the retaking of Aquila, five months before his defeat at
Landriano). Two short sign-groups remain unread; everything else is settled.

Tomokiyo's own page (`sources/cryptiana/web/francis.htm`, on disk, mirrored from cryptiana.web.fc2.com) is the
prior public source for the cipher and for this letter's existence — quoting it directly (line 183, not inside
an HTML comment, confirmed by grepping for unclosed `<!--` around it):

> "It was used in two letters from Avranches in Venice to Montmorency in BnF fr.3083 (Gallica), f.20 (no.8),
> f.55 (no.22) (the latter is with interlinear decipherment)."

f.20 (no.8) is R3694 (this row's "letter"); f.55 (no.22), "with interlinear decipherment" on the leaf itself,
is R3695 (this row's "Decrypted" neighbour) — DECODE's own status field for R3695 matches Tomokiyo's
description exactly. Tomokiyo attributes the Bishop-of-Avranches authorship of the *sister* letter used to
build the cipher table (fr. 20506, f. 96v) to Robert Cenalis, not Jean de Langeac; Cenalis held the see of
Avranches only from 1532, so for a letter of January 1529 the see's holder — and DECODE's own Sender field —
is correctly Langeac (bishop of Avranches 1526-33, per Wikipedia, ambassador at Venice in this period). This
is a naming wrinkle in Tomokiyo's page, not a doubt about the record: same shelfmark, same correspondent pair,
same cipher family.

Tomokiyo's page also notes: "The same cipher was rediscovered by George Lasry's codebreaking in 2023" —
i.e. an independent second confirmation of the key, on top of Tomokiyo's own partial table from the fr.20506
sister letter.

## 2. DECODE catalogue fields (cached, `ay/catalogue/decode-records.jsonl` and `decode-catalog.csv`, no login)

| id | status | holder | sender | receiver |
|---|---|---|---|---|
| R3694 | Non-decrypted | "Bibliotheque nationale de France (BnF), Français 3083 fol. 20-21." | Jean de Langeac, bishop of Avranches | Anne de Montmorency |
| R3695 | Decrypted | "Français 3083 fol. 55" | (not separately re-fetched; matches Tomokiyo's f.55/no.22, "with interlinear decipherment") |  |

R3694's holder string (fol. 20-21) matches Bourdeau's read folder exactly, confirming this is the same
physical item, not merely the same shelfmark.

## 3. Aymeloglu (aaymeloglu/unsolved-ciphers, no licence, cited not copied)

`grep -rli "fr\.?3083\|avranches\|langeac\|cenalis"` over the whole clone hits only the cached DECODE
catalogue files used in §2. `TARGETS.md`/`SHORTLIST.md` do not name this shelfmark or either correspondent —
untracked there.

## 4. Editions

WebSearch, 25 Sept 2026: "Jean de Langeac évêque Avranches ambassadeur Venise Montmorency 1529 lettre
chiffre" — confirms from Wikipedia/genealogical sources that Langeac was bishop of Avranches from 1526,
bishop of Limoges from 1533, and held an embassy to Venice (sources differ 1529 vs 1530 for the exact
posting), with Étienne Dolet as his secretary during a later (1530s) mission; no edition or transcription of
this specific letter or of BnF fr. 3083 was found. Ribier's *Lettres et mémoires d'estat* and Decrue's *Anne
de Montmorency* (named in the brief) not opened this pass — not needed for the verdict below, since Bourdeau
already read the leaf itself from the manuscript image, not from a print.

## 5. Community

Tomokiyo's Cryptiana page (`sources/cryptiana/web/francis.htm`) is the prior public source, covered in §1.
Cipherbrain and model-solve announcements not separately queried this pass (a dated, named repository entry
already settles the record; see check-solved.md's steer to stop once a named source states the specific
letter).

## Verdict

**found-solved, Bourdeau's lane.** R3694 (fr. 3083 f. 20-21, Langeac to Montmorency, 14 Jan 1529) is already
read in full apart from two short sign-groups, in a folder dated 18 September 2026 — a week before this
check — using George Lasry's 2023 "Avranches' cipher 1" table, itself built from the interlinear
decipherment on the sibling leaf f. 55 (= R3695, DECODE's own "Decrypted" record) and other Avranches
letters, and cited on Tomokiyo's Cryptiana page since before that. DECODE's "Non-decrypted" status on R3694
is stale. No fresh recovery or cryptanalysis work is owed here; the QUEUE row's own suggested next step
("read R3695's decipherment for the cipher's scheme/key, apply to R3694") has already been done, by Bourdeau,
independently of this DECODE cluster. Per rule 10, this is reported as a search result (a dated repository
entry and a public cipher-key page), not a novelty claim.

Nothing here needs the DECODE login. No record ids owed to the LANE DX login worker for this cluster.
