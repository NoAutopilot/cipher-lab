blocked

# Dinteville (Langres) to the Duke of Nevers, 3 July 1592 — BnF Français 3621 no. 116 (f. 130), DECODE R9451

QUEUE row: CS2-16 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 183 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September
2026 by LANE N3 csCS2b (session_01711qcbvcwvGDsSAtVXwfJB), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2b.md`.

## What it is

A letter signed by Dinteville (Bishop of Langres — see catalogue and BnF record), to the duc de Nevers, dated
"de Langres le iij^e juillet 1592," in clear French with two inline cipher passages (roughly 400–450 signs:
letters, digits and marks — `# 4 1 0 o v w m ψ α Δ □ ¢ ∇ π ƒ z +`). D. Bourdeau's own working folder
(`dinteville1592/` in his repository, session of 21 September 2026) confirms **there is no decipherment on
f. 130 itself**. A different letter in the same hand and sign set, f. 128r (no. 114, DECODE R9450, status
**Decrypted** in the local DECODE snapshot), carries a genuine contemporary interlinear decipherment over
~150 signs. Bourdeau tried a one-sign-one-letter alignment of f. 130's second cipher line against f. 128's
crib and found **no consistent mapping**: "auoir" sits over `II Δ α ψ p`, but the same `α` would then also have
to be `d` in "d'ascendre" — a contradiction. He reads this as evidence the system mixes a letter cipher with
code signs (nomenclator words for names/places such as Genève, Espagne), not a pure substitution his crib can
key by itself.

## Sibling f. 128 as a key source (per brief instruction)

**Not usable as a direct key for f. 130 this pass.** f. 128's interlinear decipherment is real (DECODE marks
R9450 "Decrypted", and the Gallica image below shows small interlinear glosses above the cipher lines), so it
is the correct crib to try — but the alignment Bourdeau ran shows the sign-to-letter mapping it would imply is
inconsistent under a simple substitution, which points to code signs/homophones rather than a clean one-part
cipher a short crib can unlock unaided. A reading of f. 130 from this material is possible in principle (a
nomenclator-plus-crib method, as used on Pelissier 1592/Lorraine 1592) but needs a verified sign-by-sign
transcription of both leaves first, which was not done this session by Bourdeau or by this check-solved pass.
If pursued, this is a **recovery** candidate (the key/crib already exists in the archive), not cryptanalysis —
but not yet at the "key found, apply it" stage.

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk).** No sentence in the local snapshot names fr. 3621, Dinteville, or
   Langres-to-Nevers 1592 specifically (grep across `sources/cryptiana/web/*.htm`: no hit for "3621" or
   "Dinteville"). Bourdeau's own note records the same: "Tomokiyo's Nevers catalogue (no Dinteville key)."
2. **Standard printed edition.** Not located or read for this letter's date this pass. Bourdeau's working
   folder does not record any Mémoires-de-Nevers or calendar check for this item at all (unlike CS2-26, where he
   ran an actual Gallica full-text search of tome 2). archive.org is held by csED this pass; WebSearch/WebFetch
   located only the BnF catalogue record (`archivesetmanuscrits.bnf.fr/ark:/12148/cc50071b`) and a web snippet
   confirming the item's date and sender, no printed text.
3. **DECODE (sources/decode/) + both solver-repo clones.** Local DECODE snapshot: **R9451** (f. 130, no. 116,
   1592–, Non-decrypted) and its sibling **R9450** (f. 128, no. 114, 1592–, **Decrypted**) both present, matching
   Bourdeau's account exactly (confirmed via `sources/decode/records-non-decrypted-2026-09-24.tsv` line 228 and
   `records-decrypted-2026-09-24.tsv` line 81). dbourdeau/cyphersolver (shallow clone, 24 Sept 2026):
   `dinteville1592/NOTES.md` gives the fullest account (above), verdict "attempted, open... Not read," escalation
   checklist shows siblings/clear-pages/known-keys done, key-rebuild not done. aaymeloglu/unsolved-ciphers:
   fresh shallow clone, no hit for "3621" or "Dinteville".
4. **Web search** (Dinteville Langres duc de Nevers 1592 lettre chiffre BnF fr.3621): only the BnF catalogue
   record and a snippet naming the correspondents/date surface; no solution or key found.
5. **Ciphertext and sibling decipherment confirmed present on the Gallica leaves.** IIIF fetches, gallica.bnf.fr,
   24 Sept 2026, 2 requests: `.../btv1b52524472n/f269/full/500,/0/native.jpg` (view 269, f.130r) shows clear
   French with two blocks of inline cipher signs matching Bourdeau's description; `.../f265/...` (view 265,
   f.128r, sibling no. 114) shows the same hand and sign family with small interlinear glosses visible above
   several cipher lines, consistent with DECODE's "Decrypted" status. Leaves:
   https://gallica.bnf.fr/ark:/12148/btv1b52524472n/f269.item and f265.item

## Verdict

**Blocked, not open.** No source claims a decipherment of f. 130 itself, and the sibling's crib (f. 128,
DECODE R9450 Decrypted) does not yet close it — Bourdeau's own alignment test found no consistent mapping. But
the standard printed edition for the date was not located or read this pass at all (not even a secondary-index
check, unlike CS2-06/CS2-26), and archive.org is not available to this worker this pass. Per the lane rule that
is `blocked`, not `open`: no nomination line posted. Unblocks when: archive.org or another edition route lets
Gomberville's *Mémoires du duc de Nevers* (1665) and a 1592 Ligue-period calendar be checked for Dinteville, and
(separately, for a future recovery attempt) f. 128 and f. 130 are both re-transcribed sign-by-sign against the
Gallica images.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 183;
`dinteville1592/` working folder), CC BY 4.0 — prior attempt, not a solution.

Not decoded, not transcribed here (out of scope for check-solved). Rule 10: no novelty claim made; this is a
search result, not a verifier's classification.
