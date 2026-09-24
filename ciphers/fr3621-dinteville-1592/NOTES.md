blocked

**Edition check (LANE N3 csED2, 24 Sept 2026 16:17 UTC):** hold not lifted -- Gomberville not reached (same
result as CS2-06). Substitute sources read; one flags a probable catalogue misidentification of the
correspondent (see section 2 below). Brief `.claude/briefs/runs/2026-09-24-lane-n3-csED2.md`.

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

## Edition check, LANE N3 csED2, 24 September 2026 (IA + Gallica SRU slots)

**Gomberville, *Mémoires du duc de Nevers* (1665) -- not reached.** Same result as the sibling row CS2-06
(fr3625-lauriere-1593): located on Gallica (`bpt6k6435941k`, `bpt6k8717151d`) via SRU, absent from archive.org
under Gomberville's creator field or a Nevers-title 1600-1700 date search, Google-Books-only otherwise
(out of route), and Gallica SRU cannot search full OCR text. **Row stays `blocked` on this alone.**

**Substitute 1: Berger de Xivrey, *Recueil des lettres missives de Henri IV*, tome 3 (1589-1593), archive.org,
read in full.** `grep -i Dinteville`: 16 hits, all Henri IV's own outgoing letters *to* "Mons. de Dinteville" as a
royal military lieutenant (e.g. pp. cited in the OCR near "A MONS. DE DINTEVILLE... Jay destiné deux cens
chevaux à Langres"), plus an editorial footnote identifying him: "Joachim, baron de Dinteville et de ...,
fils de Jean de Dinteville et de Gabrielle ..., mourut à Dinteville le 1er octobre 1607." No cipher content, no
decipherment, and this is Henri IV's side of the correspondence, not Dinteville's letters to Nevers -- but it
independently establishes the correspondent's identity and dates.

**Substitute 2: *Les luttes religieuses en Champagne au XVIe siècle: la Ligue* (Pérot, 1911), archive.org,
read in full.** Extensive coverage of "M. de Dinteville, lieutenant général" at Troyes and Langres through the
1580s-90s, sourced throughout from "Correspondance inédite de M. de Dinteville" (cited as unpublished, apud
*Revue de Champagne et de Brie*) -- i.e. a manuscript source this historian read and quoted from, not this
edition's own text, and no passage matches the 3 July 1592 letter to Nevers or names a decipherment. No hit for
"évêque"/"bishop" near "Langres" or "Dinteville" anywhere in the volume.

**Flag for whoever next touches this target: the correspondent may be misidentified in this target's own
NOTES.md.** Line 3 of this file (above) calls the signer "Dinteville (Bishop of Langres -- see catalogue and BnF
record)". Both sources read this pass, plus a WebSearch check (`en.wikipedia.org/wiki/Joachim_de_Dinteville`,
found 24 Sept 2026), identify the "M. de Dinteville" active at Langres in exactly this period as **Joachim,
baron de Dinteville**, the king's lieutenant-général holding Langres and Troyes for Henri IV -- a layman and
soldier, not a bishop. Langres was a duchy-peerage held by its bishop ("duc et évêque de Langres"), a distinct
office and (so far as found this pass) a different person. No source read this pass supports "Bishop of Langres"
for this letter's signer; whoever set that in the catalogue check should re-verify it against the BnF record
before it is repeated. Also worth a look, not pursued further this pass (out of scope, a lead not a finding):
WebSearch surfaced BnF fr. 3623 as holding letters from "J., baron de Dinteville" to Nevers dated Langres,
5 July and 13 July 1592 -- a sibling correspondence in the same month, days after this letter, in a different
volume from fr.3621. Worth checking for a decipherment or a key before this row's next escalation.

Credit: unchanged from the check-solved pass (D. Bourdeau, cyphersolver, `dinteville1592/`). Rule 10: no novelty
claim made.
