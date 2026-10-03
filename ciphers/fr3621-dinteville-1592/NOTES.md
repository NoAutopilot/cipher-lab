partial
Gomberville, *Mémoires du duc de Nevers* (1665) seconde partie (Google Books H2eV4wAmIr0C) full-text searched by this worker (GF4-BATCH9, 3 Oct 2026) for Dinteville, Dinteuille, Dintevile (0 hits), Langres (10, pp.256-390, none this letter), "deux millions", Strasbourg, "armee lorraine" -- letter absent.

**Hold lifted, LANE N4 scGOM2, 24 Sept 2026:** the genuine seconde partie is Google Books `H2eV4wAmIr0C` (title
page confirmed, distinct from the two Gallica arks which are both Première partie); full-text searched for
"Dinteville"/"Dinteuille" and "Langres" -- letter absent; see the dated section below. fr.3623 sibling letters
(5/13 July 1592) not checked -- needs a Gallica image, out of this pass's host grant.

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

## Edition check, LANE N3 csGOM, 24 September 2026 (Gallica ContentSearch + IIIF)

Brief `.claude/briefs/runs/2026-09-24-lane-n3-csGOM.md`. Same Gomberville pass as the sibling row CS2-06
(`ciphers/fr3625-lauriere-1593/NOTES.md`, same date) -- full method and evidence there; summarized for this
letter's date (3 July 1592) here.

**Both Gallica arks (`bpt6k6435941k`, `bpt6k8717151d`) are two physical exemplars of Gomberville's "Premiere
partie" (BnF shelfmarks FOL-LA23-13 (1) and (A,1)), not a first and second tome.** Confirmed by SRU dc:title
match (only these two results for `dc.title all "memoires duc nevers"` on all of Gallica), continuous 1-937
page-label sequences in both IIIF manifests (no restart consistent with a second bound part), and a read image
of `bpt6k6435941k` f82 (the privilège du roy, dated September 1665, ending "RECVEIL" -- the single collection
that follows).

**Gallica ContentSearch OCR year-counts against `bpt6k6435941k` (1588 -> 17, 1589 -> 2, 1590 -> 2, 1591/1592/1593
-> 0) show this digitized part's content ends before 1591**, one year short of this letter's 3 July 1592 date.
"Dinteville" -> 0 hits in both arks (already checked by csED2 for the title terms; the year-range check is new
this pass and gives the structural reason why). No third, genuine "seconde partie" ark was located on Gallica by
SRU title search this pass -- see the CS2-06 section for the full search (`dc.creator "Gomberville"` 0 hits,
catalogue-record ark 404s, WebSearch turns up Hachette BnF/POD "Partie 2" reprint listings and a second Google
Books id `H2eV4wAmIr0C` as a lead, not opened -- Google Books is out of this lane's host grant).

**CS2-16-specific question (does Gomberville print the f.128 sibling's decipherment, which would make f.130 a
recovery): unanswerable this pass, for the same structural reason.** Neither Gallica ark reaches 1592, so
whether Gomberville prints Dinteville's letter or f.128's interlinear plaintext cannot be checked from what is
digitized on Gallica. This stays open as a question for whoever next gets archive.org, HathiTrust or Google
Books access to the real seconde partie.

**Verdict unchanged: `blocked`.** Same reasoning as CS2-06. No nomination line posted. Unblocks when: the
seconde partie is located outside Gallica (archive.org, HathiTrust, Google Books -- all out of this lane's
grant) and read or searched for "Dinteville," "Langres," 3 July 1592, or the f.128 sibling's decipherment.

A flag about CS2-26 (fr3993-villeroy-1595)'s "Gomberville t.2 Gallica full-text search" claim -- which this
pass's search suggests may actually have hit one of these same Premiere-partie arks -- is posted in the CS2-06
section and in ROOM.md; not this row's target, not otherwise acted on here.

Requests this section: 0 additional gallica.bnf.fr requests beyond the CS2-06 section (same arks, same
ContentSearch/SRU/IIIF calls cover both rows). Credit unchanged. Rule 10: no novelty claim made; this is a
search result.

## Edition check, LANE N4 scGOM2, 24 September 2026 (Google Books, genuine seconde partie found)

Brief `.claude/briefs/runs/2026-09-24-lane-n4-scGOM2.md`. Same Gomberville pass as the sibling row CS2-06
(`ciphers/fr3625-lauriere-1593/NOTES.md`, same date, full method there); summarized for this letter here.

**Google Books `H2eV4wAmIr0C` confirmed as the genuine seconde partie**, distinct from `ztkvMWA_yO0C` (Première
partie, the same part as both Gallica arks csGOM already ruled out). Both `FULL_PUBLIC_DOMAIN`, `ALL_PAGES`.

**Full-text search for this letter's correspondent and place names:**
- "Dinteville": 0 hits. "Dinteuille" (v/u period-spelling variant): 0 hits.
- "Langres": 10 hits, pp. 256-390 — the same dense, on-topic 1592-93 Champagne cluster found for CS2-06's
  "Chaalons" search (e.g. p. 302 "Langres pour les asseurer de la bonne volonté que i'ay de les secourir, & les
  délivrer de l'oppression du Duc de Lorraine"; p. 361 "...ne pouuant d'icy aller droit à Langres..."), none
  naming Dinteville.
- "Balagny": used to positively locate the pp. 719-732 Cambray-crisis letter found for the sibling CS2-26 row
  and confirm it is a different, later (Aug 1595), unrelated piece, addressed "Messieurs" — not this letter
  either (3 July 1592, to Nevers alone).

**fr.3623 sibling letters (5 and 13 July 1592, named in this row's own brief as a lead): not checked.** Whether
they are cipher, and whether Gomberville prints them, needs the Gallica image (or catalogue note) for fr.3623,
which is outside this pass's host grant (no gallica.bnf.fr). The 0-hit Dinteville/Dinteuille search above covers
whether the seconde partie prints *any* Dinteville letter under that name, sibling included, but cannot rule out
an unsigned or differently-attributed print of one.

**Verdict: `open -- Gomberville 1665 seconde partie (Google Books H2eV4wAmIr0C), full-text searched (Dinteville,
Dinteuille, Langres, Balagny), letter absent.`** Stronger than csED2's substitute-source check (Xivrey, Pérot,
both negative, neither reaching Gomberville) and than the original csCS2b/csGOM holds (wrong tome only
available): the correct tome, searched directly in its on-topic 1592-93 Champagne section, gives no hit. Hold
lifted; re-nominated (see ROOM.md and QUEUE.md CS2-16). The f.128 sibling recovery question (DECODE R9450,
Decrypted, alignment inconsistent under simple substitution) is unaffected by this edition check and stands as
csCS2b left it.

Credit: unchanged (D. Bourdeau, cyphersolver). Rule 10: no novelty claim made; this is a search result, not a
verifier's classification.

Requests this section: 0 additional www.googleapis.com/books.google.com requests beyond the CS2-26/CS2-06
sections (same volume; all search terms counted in the CS2-26 section's total, ~15 total for all three rows). No
gallica.bnf.fr, HathiTrust, BSB, ONB or archive.org used.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/dinteville1592/NOTES.md
- Their extent, in their words: attempted, open, not read (R9451)
- Their date: 21 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (GF4-BATCH9, account-4, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `Dinteville Langres Nevers 3 juillet 1592 lettre chiffre` -- BnF catalogue records for fr.3621, fr.3623, fr.3625,
   fr.3631, fr.3617, fr.4718, fr.3974-3995; Wikipedia "Joachim de Dinteville"; OpenEdition, *Noblesse seconde et pouvoir
   en Champagne* ch. IV. No decipherment of f.130.
2. `"fr. 3621" OR "français 3621" Dinteville chiffre` -- BnF fr.3621 record and number-spelling noise only.
3. `"Dinteville" Nevers cipher letter 1592 decipherment` -- Desenclos and Lasry, "An early French digit cipher" (Henri IV
   to Nevers 1592, a different letter); Bourdeau's site index, which lists this letter as not deciphered; cyphersolver
   PR 4 (Lorraine to Vaudemont, fr.3621 no.97), PR 7, PR 9 and issue 13 (Laurière). None of them reads f.130.
4. Folder title / BnF record: the fr.3621 finding aid (archivesetmanuscrits.bnf.fr/ark:/12148/cc50071b), fetched by curl
   and read in full -- see Premise check (a).
Blogs: `Dinteville cipher site:scienceblogs.de OR site:ciphermysteries.com OR site:cryptiana.blogspot.com` -- the 6
Cipher Mysteries hits are unrelated posts (Oak Island, Gentlemen's cipher, van Heeck, Cysquare, La Buse, Beale), with
nothing about Dinteville. There were no Cipherbrain (Klausis Krypto Kolumne) or Cryptiana blog hits. Tomokiyo's pages: the
local mirror `sources/cryptiana/web/` has no "3621"/"Dinteville" (earlier pass, re-confirmed by Bourdeau's own
"Tomokiyo's Nevers catalogue (no Dinteville key)"). No comment thread to open; nothing found.

## Premise check (GF4-BATCH9, account-4, 3 Oct 2026)

(a) **Decipherments the folder mentions: not this item.** The only decipherment named is f.128 (no.114, DECODE R9450
"Decrypted"). The BnF finding aid for fr.3621 (fetched 3 Oct 2026) describes f.128 as "Lettre, avec chiffre et
déchiffrement, du Sr DE DINTEVILLE ... De Langres, ce 1er juillet 1592", a different letter. It describes f.130 (no.116)
as "Lettre chiffrée du Sr DE DINTEVILLE ... De Langres, le IIIIe juillet 1592", with no decipherment. Note: the catalogue
dates the letter 4 July, while Bourdeau read "iij^e" (3 July) on the leaf. The image settles which; the folder keeps
3 July as read. The catalogue also confirms the signer is "JOACHIM DE DINTEVILLE" (f.27, no.19). The bishop of Langres
in the same volume is Charles d'Escars (f.126, no.112), which supports csED2's flag above that "Bishop of Langres" is a
misidentification. Not found.
(b) **Other solvers' working files: not found.** In dbourdeau/cyphersolver (shallow clone, HEAD 4aedb40, 2 Oct 2026),
`targets/dinteville1592/` holds NOTES.md, align.py and profile.json. align.py aligns only f.128's second cipher line
with its interlinear gloss, and no key is applied to f.130. In aaymeloglu/unsolved-ciphers (shallow clone, HEAD d2800bb,
27 Sept 2026), the only matches are catalogue rows (`catalogue/decode-catalog.csv`: R9451 Non-decrypted, R9450 and
R9452 Decrypted). There is no working folder.
(c) **Physical neighbours: no clear copy found.** The finding aid lists ff.127-131 as follows: f.127 (no.113, Dinteville,
1 July 1592, no cipher mentioned); f.128 (the sibling with decipherment); f.129 (Potier de Blancmesnil, 2 July); f.130
(this letter); f.131 (Vergy to Dinteville, 4 July, copy). Bourdeau viewed Gallica views 263-272 (ff.127-131) and f.130v
(address only) at full resolution on 21 Sept 2026, and found no decipherment on or facing f.130. This worker did not
re-view those images; this item rests on Bourdeau's view plus the catalogue.
(d) **Recipient side: not found.** Nevers's printed papers are Gomberville 1665, seconde partie. This worker searched it
(see line 2): no Dinteville letter. Henri IV, *Lettres missives* t.3 (csED2 above) holds only the king's letters to
Dinteville.
New lead for a later recovery, not a find: fr.3623 no.15 (f.23) is a second Dinteville to Nevers letter "avec chiffre
et déchiffrement", from Langres, "il 25 ottobre", in Italian (BnF fr.3623 finding aid, ark:/12148/cc50073t, fetched
3 Oct 2026; DECODE R9452 Decrypted). It is a further crib if it uses the same sign set. The fr.3623 finding aid lists no
Dinteville letters of 5 or 13 July 1592, so the csED2 lead above is not borne out by the catalogue.

Verdict after this pass: `open` stands. The next step, a sign-by-sign transcription of f.128 against its interlinear
(plus fr.3623 f.23), depends on nobody, so no "While waiting" section is needed.
Requests this pass: archivesetmanuscrits.bnf.fr 2, books.google.com 9 (SearchWithinVolume, 2 s apart),
archive.org 1, be-api.us.archive.org 1 (the generic Dinteville full-text query returned only noise), raw.githubusercontent.com 1,
github.com 2 (shallow clones). Rule 10: no novelty claim; these are search results.

## Intake gate (A2-DIN, account 2, 3 Oct 2026)

```
$ python3 tools/intake_gate_check.py fr3621-dinteville-1592
fr3621-dinteville-1592: open (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT 0
```

## f.128r interlinear transcription and alignment (A2-DIN, account 2, 3 Oct 2026)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-din.md` (LANE-A2PUSH2). No live account-4 claim in ROOM.md (GF4-BATCH9
done 02:42). Files: `f128/` (README.md lists them), crops in `images/`.

**Image.** `tools/gallica_folio.py btv1b52524472n --folio 128` -> canvas f265, label '128r', one constant offset
(k=10, ff.1-131). The leaf is no.114 (the BnF finding aid's "avec chiffre et dechiffrement", Langres 1 July 1592): the
date line at the foot ends "...Juillet 1592" (day not read in this step). The cipher passage is 4 lines (L02 right
end after "et"; L03 to L05), each with a period decipherment written word by word above it. Crops (pasted):

```
$ python3 tools/iiif_lines.py --ark btv1b52524472n --canvas 265 --region 200,1800,3700,560 \
    --out ciphers/fr3621-dinteville-1592/images --prefix f128 --top-margin 45 --bottom-margin 25 --only-lines 2,3,4,5 --debug
...src_ark_12148_btv1b52524472n_f265_200_1800_3700_560.jpg (cached): region 3700x560, 5 lines, 5 bands x 2 segments; pitch 100 distance 70 prominence 228.2
  centres (region y): 78 174 271 377 483
  wrote 8 crops and ciphers/fr3621-dinteville-1592/images/manifest.json
```

**Transcription (rule 2: from the image).** Two blind Sonnet passes on the 8 line-segment crops (`f128/passA.tsv`,
`passB.tsv`, raw), then one Opus reconciliation from 1.6x sub-crops of the same region (`images/zoom/`), written to
`f128/gloss_pairs.tsv` and committed (b30b3db2) **before** any alignment. 183 cipher signs in 4 lines, 31 sign labels
(the 25 of `f128/pass_instructions.md` plus D triangle, r curled r, al alpha distinct from a, zh bare z-tail, h, B, n,
div, plus). Error: err_2reader only (no benchmark item for this hand): pass A vs pass B edit distance 26 / 183 signs
(14%), A vs reconciled 33, B vs reconciled 21, all on the instruction label set (so the a/alpha, D/r/4 and 3/zh splits
the reconciliation makes are not counted: a lower bound). Pass B read almost no gloss, and pass A read it only roughly.
The gloss lines in gloss_pairs.tsv are the reconciler's reading, single-reader. Uncertain gloss words are flagged in the
note column: 'dascender' letters 3-5, 'bestiaux', and L05's 'besounasiana' (read literally; Bourdeau reads Besancon).
The gloss writes '+' and '|' for signs it left unexpanded, kept as '+' wildcards.

Gloss as read: L02 "ma dit"; L03 "auoir veu dascender a geneue + deux millions dor despaigne" / clear "Il ha laisse" /
"a"; L04 "bestiaux quarante cinq + + mulets chargez qui doibt aussi passer dans trois"; L05 "iours et + + prendre le
chemin de + besounasiana que + vn chemin de fl[andres]", ending in clear "Cremona"(?).

**Alignment (tools/interlinear_align.py through `f128/align_f128.py`, f and s kept apart, rule 3 control first).**
Control: every rotation (172) of the concatenated gloss letters, re-split into the original words, so each gloss word
keeps its length and place and the letter frequencies are unchanged. Only the sign/letter correspondence moves, so the
control can differ from the target on the statistic. Statistic: consistency, i.e. the share of aligned occurrences of
sign types seen at least twice that carry their type's top letter. My first control re-split without word spaces, which
changed the aligner's word-boundary bonus and gave a null mean of 0.672. That is not a matched control, and I fixed it
before the numbers below.

| variant | params | real | null mean | null p95 | null max | rotations >= real | grades (183 tokens) |
|---|---|---|---|---|---|---|---|
| 1 letter | --code-prefix, 0-1 letter/sign, null-cost 0, seg-bonus 1 | 0.313 (147 occ) | 0.316 | 0.349 | 0.408 | 95/172 | C 38, M 145 |
| 2 syllabic | 0-3 letters/sign, null-cost -1, seg-bonus 0, len-prior 1 | **0.590** (156 occ) | 0.299 | 0.331 | 0.353 | **0/172** | **C 89, M 94** |

Variant 2 was declared after variant 1 failed. Its one run with null-cost 0 was degenerate: every sign went null and
there were no counts. I changed only that one setting (to -1.0), and both runs are logged in the script's docstring.
Variant 1's failure looks like a parameter artifact, not a design result. With free nulls and a word-boundary bonus, the
DP pushes letters onto nulls. Both aligned keys take almost only single letters (variant 2 has two multi-letter chunks,
both M), so the system read here is **a homophonic letter substitution with nulls**, not a syllabary. This is a
cryptanalytic alignment of a period gloss: grade C per sign where it agrees, and no H.

Key (`f128/key_syl.tsv`, sign -> letter, agree/n), the clean ones: al=u 5/5, p=i 5/5, w=r 6/6, z=m 4/4, 4=l 3/3,
y=o 6/8, L=i 4/5, 3=d 4/5, a=q 3/4 (the "qu" of quarante/qui), m=u 5/8, 0=e 9/16, f=n 6/11, sq=s 5/9, #=d 5/13, v=a 5/11,
9=g 2/3, T=h 2/3. Weak or conflicting: 1, ., c, D, r, o, zh, and the singletons II, h, B, n, div, plus. The cleanest
spans are L03 "auoir" (D al y p w; the leading II is unaligned), "veu" (m o al), "deux millions dor despaigne" (# 0 m sq
/ z p 4 plus L y f sq / 3 y w / # 0 sq 0 v L 9 r 0), and L04 "qui" (a m L). The spans that drift (M) are L03 "a geneue +",
the second half of L04 (from "doibt"), and L05 after "de +". Those are where a transcription error or a misread gloss
word is most likely.

**What this adds to Bourdeau** (`targets/dinteville1592/align.py`, MIT, cited, not copied; github.com/dbourdeau/cyphersolver,
21 Sept 2026). His test aligned only L03, about 50 signs against 48 letters, looking for an exact one-to-one map with at
most 3 null types, and found none ("auoir" over II D alpha psi p, but alpha also = d in "dascender"). This pass
transcribes all 4 cipher lines and their gloss (183 signs) and keeps alpha (al) apart from the plain a. Read that way,
al = u 5/5, and the a before "#" in "dascender" is not the "auoir" sign. Hard-EM alignment then tolerates transcription
noise, and the control shows the resulting consistency is not an artifact of the gloss's length structure. It does not
show the key is complete or correct per sign.

`python3 ciphers/fr3621-dinteville-1592/f128/align_f128.py --check` and `... --syl --check` both print "check: committed
outputs match" (rule 7). No spec and no judge for this target (not a reading). Not done in this step: f.130 (the brief
names it as the next step).
Requests: gallica.bnf.fr 3 (manifest via gallica_folio.py, 1 overview at 1000 px, 1 native region), github.com 1 (sparse
clone of Bourdeau's target folder). Vision calls: 2 blind Sonnet passes plus the Opus reconciliation (17 zoom
sub-crops read in this session). Rule 10: no novelty claim. This is an alignment of a period gloss that DECODE R9450
already marks Decrypted.

## f.130r transcription and key_syl decode: PRE-REGISTRATION (A2-DIN2, account 2, 3 Oct 2026, written 05:00 UTC before any scoring)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-din2.md` (LANE-A2PUSH2). Intake gate pasted:
```
$ python3 tools/intake_gate_check.py fr3621-dinteville-1592
fr3621-dinteville-1592: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT 0
```
Fixed before the transcription is reconciled or any decode is scored:
- Ciphertext: `f130/ciphertext.tsv`, reconciled from two blind Sonnet passes (`f130/passA.tsv`, `passB.tsv`) on the
  tools/iiif_lines.py crops `images/f130_L*_s*.jpg`, in the f.128 label set (`f130/pass_instructions.md`). Signs absent
  from the f.128 inventory (`f128/gloss_pairs.tsv`) are flagged in `f130/inventory.tsv`.
- Key: `f128/key_syl.tsv` unchanged (sign -> top letter). Grade per token: C where the key row has agree >= 3 and
  agree/n >= 0.5 AND the sign is settled (both passes agree, or reconciled without doubt); M otherwise (weak key row,
  or a reconciled split); U where the sign is not in the key.
- Statistic: mean log10 4-gram probability per letter (tools/judge_plaintext.py NgramModel, fr16 corpus = the three
  files in tools/data/fr16, n=4, k=0.01) over all 4-letter windows lying wholly inside runs of keyed signs (an unkeyed
  sign or a clear word breaks the run). Secondary, reported but not a gate: greedy word cover (NgramModel.cover) of the
  same runs, letters-weighted.
- Control: 1000 shuffled keys (seed 20261003): the key's letter values permuted among its signs (same letter multiset,
  same keyed positions, same run structure), decoded and scored identically. The statistic depends on which sign carries
  which letter, so the control can differ from the target. Gate: real > shuffled p95 (one-sided). Report real, shuffled
  mean, p95, max and rank. A pass means "the f.128 key reads f.130 better than its own shuffles", not a reading.
- Script: `f130/score_f130.py` (`--check` regenerates the committed outputs).

## f.130r transcription and key_syl decode: RESULT (A2-DIN2, account 2, 3 Oct 2026)

**Crops (pasted, Usage 6).** `tools/gallica_folio.py btv1b52524472n --folio 130` -> canvas f269, label '130r'. The lines
slope up to the right by about 0.04-0.06 px/px, so fixed-y bands mixed neighbouring rows. These are the crops that were used:
```
$ python3 tools/iiif_lines.py --ark btv1b52524472n --canvas 269 --region 280,600,3360,1360 \
    --out ciphers/fr3621-dinteville-1592/images --prefix f130 --debug --centres 125,201,279,387,525,755,891,989,1095,1187,1325 \
    --top-margin 50 --bottom-margin 50 --max-width 1760 --overlap 160 --follow-slope 300 --slope-local
  band L01: slope fit y = 100.7 + -0.03221*x ... band L11: slope fit y = 1302.1 + -0.06327*x
  wrote 22 crops and ciphers/fr3621-dinteville-1592/images/manifest.json
```
The centres are the left-edge y values, so the slope tracker starts on the cipher row. I checked the crops on contact
sheets before any pass. Eleven lines carry cipher: L01 is a tail after "et", L02-L05, L06 is a tail after "dy", and
L07-L11 run to the clear words "pour luy".

**Transcription (rule 2: from the image).** Two blind Sonnet passes read 20 segment crops, using the f.128 label set
(`f130/pass_instructions.md`). Pass B read the crops in reverse order. The raw output is in `f130/passA.tsv` and
`f130/passB.tsv`. I then did one Opus reconciliation (`f130/reconcile_f130.py`). It first normalizes the labels: x -> p, because
the looped-x glyph is the sign f.128 labels p (checked on `images/f128_L03_s1.jpg` against gloss_pairs L03 "deux millions" =
z p 4 plus L); + and t -> plus; and 2 -> z. After that I re-read L02 s1, L10 s1 and L11 s1 from 1.6x zooms (`images/zoom/f130_*_z.jpg`).
That re-read found one systematic pass error. Both passes sometimes wrote a cross label (t, t') for v' (a v with a
crossed stem). Error: err_2reader only, since there is no benchmark item for this hand. Before normalization the A-B
edit distance is 108 on 570 tokens. After it, the distance is 61 on 542 cipher signs (11%). Every sign inside an A/B
disagreement span is conf M (57 of 530). Result: `f130/ciphertext.tsv` has 530 cipher signs (3 of them dots) and 29 labels.

**Inventory against f.128** (`f130/inventory.tsv`). Signs absent from f.128 are flagged there. v' occurs 23 times on f.130
and 0 times on f.128. 0' (an o with a stem) occurs 14 times. The f.128 reconciliation wrote that glyph as 0 ("sq 0 0 f" over "□ o ō ≠"),
so 0' may not be a separate sign. NEW:e-hook and NEW:N-like occur once each. Every other f.130 label occurs on f.128.
The key does not cover v' (23), 0' (14) or the two NEW signs. Together they make the 39 U tokens.

**Test (as pre-registered above, `f130/score_f130.py`, `f130/result.json`, `f130/control.tsv`).**

| statistic | real (key_syl) | shuffled keys (1000) mean | p95 | max | shuffles >= real | gate |
|---|---|---|---|---|---|---|
| fr16 4-gram mean log10 P/letter, keyed runs (385 windows) | **-1.334** | -1.961 | -1.716 | -1.538 | **0/1000** | **PASS** (real > p95) |
| word cover (secondary) | 0.841 | 0.631 | 0.743 | - | - | - |
| variant o_stem (0' read as 0, not pre-registered; 428 windows) | -1.347 | -1.948 | -1.713 | -1.543 | 0/1000 | - |

The control can differ from the target on this statistic: a shuffled key keeps the letter multiset and the keyed
positions, and moves only which sign carries which letter. The f.128 key reads f.130 about 0.2 log10 per letter better
than the best of 1000 shuffles. Grades (decode_key.py, 527 tokens, dots excluded): **C 263, M 225, U 39**. No H. This is
a cryptanalytic result: a period gloss key from a sibling leaf, applied to a leaf with no gloss.

Rule 7: `python3 tools/decode_key.py ciphers/fr3621-dinteville-1592 --check` prints "reading up to date"
(decode.json). `tools/decode_key.py`'s key reader treats a key row whose sign is `#` as a comment line. For that reason
score_f130.py writes two derived copies, `f130/key_dk.tsv` and `f130/ciphertext_dk.tsv`, in which `#` is spelled
`hash`. A tool fix is flagged for the lane. `python3 ciphers/fr3621-dinteville-1592/f130/score_f130.py --check` prints
"check: committed outputs match". There is no spec for this target, so judge_plaintext.py was not run as a spec judge.
Its NgramModel is the statistic above.

**What the decode shows** (`f130/reading.txt`: lower case = C, upper case = M, ? = U). This is not yet a reading. The
runs contain recognisable French: L08 "...dedans ... e bien bas ... quil nes...", L09 "dehors les ...", L10 "...la ville
... le roi ...", L11 "uouruoir de mener ... qui l'... honbeur" (pourvoir? honneur?), and L05 "onserue" (conserve?).
Long stretches drift. The likely causes are the weak key rows (v=a 5/11, #=d 5/13, 1=e 2/11, .=e) and the 39 unkeyed
v'/0' signs. Not done in this step: a word-level reading, key repair from f.130's own runs, and the fr.3623 f.23 sibling.

Requests: gallica.bnf.fr 3 (manifest via gallica_folio.py, 1 overview at 1000 px, 1 native region; later crop runs
read the cached file). Vision calls: 2 blind Sonnet passes plus 1 Opus reconciliation (2 contact sheets, 3 zooms, 1
f.128 reference crop, 4 check crops). Rule 10: no novelty claim.

## f.130r key repair: PRE-REGISTRATION (A2-DIN3, account 2, 3 Oct 2026, written 05:15 UTC before any repair is scored)

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-din3.md` (LANE-A2PUSH2). Intake gate pasted:
```
$ python3 tools/intake_gate_check.py fr3621-dinteville-1592
fr3621-dinteville-1592: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT 0
```
Fixed before any repaired key is scored (script `f130/repair_f130.py`, outputs under `f130/repair/`):
- **Rows that may change (free rows, 17):** the unkeyed f.130 signs v' (23), 0' (14), NEW:e-hook (1), NEW:N-like (1),
  and every key_syl row with agree < 3 (graded M): zh, D, o, 1, c, 9, r, plus, div, T, h, B, n. Every other key_syl row
  (z, v, y, a, p, 3, L, al, w, m, #, ., sq, 0, f, 4) is held at its key_syl value. II (f.128 only, unkeyed) stays unkeyed.
- **Text scored:** f.130 ciphertext.tsv plus the f.128 cipher signs (f128/gloss_pairs.tsv `signs` column), in runs
  broken by CLEAR words and by unkeyed signs, exactly as score_f130.py does. Free rows take one of the 26 letters (no
  null option), so the run structure is the same for every key tried.
- **Statistic:** the same fr16 4-gram mean log10 P/letter (NgramModel, n=4, k=0.01) over all 4-letter windows inside runs.
- **Repair method:** constrained hill-climb (coordinate ascent): sweep the free rows in fixed order, for each try all 26
  letters and keep the best, until a sweep makes no change (max 8 sweeps). Primary run seeded from key_syl (free
  unkeyed rows start at 'e').
- **Held-out check (f.128 period gloss):** for each free row whose sign has at least one aligned gloss letter in
  `f128/align_syl.tsv` (multi-letter chunks contribute their letters), the repaired value must be one of those letters;
  a value that contradicts the gloss is rejected and the row reverts to its key_syl value. v', 0' and the NEW signs have
  no f.128 alignment and are unconstrained. Which rejections rest on a single gloss occurrence is reported, not used.
- **Control:** the same climb + the same held-out rejection run from 1000 shuffled seed keys (key_syl's letter values
  permuted among its keyed signs, seed 20261003, the A2-DIN2 shuffle), free rows climbed, fixed rows left at their
  shuffled values. Gate: repaired-key score > repaired-shuffle p95 (one-sided); report real, mean, p95, max, rank. The
  control can differ from the target on this statistic (its fixed rows carry different letters).
- **Stability:** 20 further climbs of the real key from random free-row starts (seed 20261004); a repaired value counts
  as stable if the primary value is reached in >= 14 of 20.
- **Grades per token:** sign conf M -> M; held key_syl row meeting the A2-DIN2 C rule (agree >= 3, agree/n >= 0.5) -> C;
  free row whose final value is aligned to that sign >= 2 times in f128/align_syl.tsv -> C (gloss-confirmed); free row
  whose value comes from the repair, passes the held-out check, is stable, with the gate PASS -> S; otherwise M; unkeyed U.
- A word-level reading is written from the final key with every token graded; decode.json gets the repaired key as a
  second job and `tools/decode_key.py ... --check` must pass.

## f.130r key repair: RESULT (A2-DIN3, account 2, 3 Oct 2026)

Run as pre-registered above (`f130/repair_f130.py`; outputs `f130/repair/`: result.json, key_repaired.tsv, control.tsv,
stability.tsv, reading.txt, tokens.tsv, reading_words.md). No images and no network in this step.

| statistic (fr16 4-gram mean log10 P/letter, f.130 + f.128 cipher runs, 685 windows) | value |
|---|---|
| key_syl seed (free unkeyed rows at 'e') | -1.449 |
| repaired, before the f.128 held-out check | -1.215 |
| **repaired, after the held-out check (8 rows reverted)** | **-1.271** |
| 1000 shuffled seed keys, before repair: mean | -1.949 |
| 1000 shuffled seed keys, same climb + check: mean / p95 / max | -1.789 / -1.582 / -1.407 |
| shuffles >= real | **0/1000: gate PASS** |

The control can differ from the target here: a shuffled seed key has different letters on the 16 held rows, and the
free rows get the same climb. The climb raises the shuffles by about 0.16 and the real key by about 0.18, so the repair
does not by itself produce the margin.

**Held-out check.** 8 of the 13 free key_syl rows had their repaired value rejected by the f.128 gloss and reverted:
zh (c), D (l), o (l), 9 (l), T (i), h (l), B (a), n (l). Three of these rest on a single gloss occurrence (h, B, n).
Values kept by the repair: 1 = e, plus = l, div = b (unchanged from key_syl); c = r (was a, 1/5), r = n (was b, 1/4).
Unkeyed signs: v' = t, 0' = s, NEW:e-hook = r, NEW:N-like = l. Every free value was reached in 20 of 20 random-start
climbs (stability.tsv).

**Grades** (decode_key.py, 527 tokens, dots excluded): **C 329, S 71, M 127, U 0**, no H (A2-DIN2: C 263, M 225,
U 39). The S tokens are v', 0', c, r, plus, div and the two NEW signs. This is a cryptanalytic result: a period key
from a sibling leaf, repaired by a hill-climb with a matched control.

**Word level** (`f130/repair/reading_words.md`, my word division, graded by its letters). The runs now carry French
phrases: L05 "(c)onseruer ... en l'obeissan(c)e" (before the clear "Messieurs de la ville"), L09 "dehors les ...
seruiront ... leur", L10 "la uille et le roi", L11 "(p)ourvoir de ... retirer d'aultant qu'il i a ... l'honneur"
(before the clear "pour luy"), L08 "...de dans se bien bas ... qu'il ne ... plus". English gist (fragments): keep [the
town] in obedience; outside, the [...] will serve; the town and the king; to provide [for ...], withdraw, inasmuch as
there is [...] the honour [for him]. L01-L04 and L06-L07 are still mostly undivided.

**The words contradict two held-out rejections:** h = p (pourvoir) and D = c (auec, obeissance, conseruer; D = d in
"demeure"). The pre-registered rule kept h = u and D = a, so those tokens stay M and the letters in parentheses are
grade I. The f.128 gloss for h is a single occurrence, and for D it is 2 of 4. A second reader on the f.128 gloss at
those signs would settle whether the rejection or the gloss reading is wrong.

Rule 7: `python3 tools/decode_key.py ciphers/fr3621-dinteville-1592 --check` prints "reading up to date" (decode.json
job 2 = the repaired key). `python3 ciphers/fr3621-dinteville-1592/f130/repair_f130.py --check` prints "check:
committed outputs match". No spec exists for this target, so judge_plaintext.py was not run as a spec judge. Its
NgramModel is the statistic above. Requests: none. Vision calls: none. Rule 10: no novelty claim.

## Verifier (VERIFY-DIN, account 3, 3 Oct 2026, 07:26-07:50 UTC) -- see AUDIT.md

N3 for the f.130 cipher fragments, key source `period`. Re-derived exactly (all four --check pass). Controls at fresh seeds:
key_syl -1.334 vs free-shuffle max -1.537/-1.523/-1.463 and frequency-banded-shuffle max -1.440/-1.526 (0/5000); repaired
-1.271 vs repaired-shuffle p95 -1.583/-1.588 (0/2000). Power at 11% injected error on a same-design synthetic: exact key
5/5 beat all shuffles; real f.130 sits between an exact key and 4 of 33 rows wrong. The repair climb fails its own
known-answer test (4/14 held rows; 40% of freed rows at 11%), so the 71 S are M, and five low-agreement rows the repair
graded C (1, D, T, o, 9) are M: **licensed C 263 S 0 M 264 U 0**. h and D: M; the letters the words want (p, c/d) are I.
Found in print: *Revue de Champagne et de Brie* t.XII (1882) pp.340-341 prints f.128 (1 July) in full and calendars f.130
(4 July, "En chiffres") from its clear text only (`print/revue-champagne-t12-1882-pp340-341.txt`). Script verify/verify_din.py.

## f.128 re-aligned against the 1882 print; f.130r re-decoded (DIN-PRINT, account 3, 3 Oct 2026, 07:43-08:00 UTC)

Brief `.claude/briefs/runs/2026-10-03-acct3-din-print.md`. Pre-registered before any score: `f128/print_align/PREREG.md`
(commit d10eb096). Disk only, no images, no network.

**1. One convention.** `f128/print_align/print_pairs.tsv`: per glossed f.128 segment, the print span (*Revue de Champagne
et de Brie* XII, 1882, p.340) and the gloss, both lowercased, accents folded, punctuation dropped, j/v/y -> i/u/i, numerals
as words, the gloss's '+' marks dropped. Print words are used verbatim (vu, charges), not respelled from the gloss. One
gloss dependency remains: the print's "45 mulets" is OCR-garbled ('îa'), so "quarante cinq" comes from the gloss. Where
they differ, the print reads "besancon" for "bestiaux", "doiuent partir" for "doibt aussi passer", "uesoul naiant" for
"besounasiana", and "cent cheuaux descorte" for "vn chemin de fl". Each of these fits the cipher letter by letter
under the existing key (e.g. `# 0 f v` = cent, `# T 1 m v al sq` = cheuaux, `3 1 . 0 # y c n 1 .` = descorte).

**2. Alignment** (`f128/print_align/align_print.py`, tools/interlinear_align.py with key_syl's exact --syl settings; only
the plain text changed). Consistency, with the key-blind controls (every rotation of the print letters re-split into the
same word lengths, and 1000 letter shuffles, seed 20261003):

| plain text | mode | real | rotations p95 / max (ge) | shuffles p95 / max (ge) | gate |
|---|---|---|---|---|---|
| **print** | **syl (primary)** | **0.831** (160 occ) | 0.327 / 0.803 (0/166) | 0.325 / 0.358 (0/1000) | **PASS** |
| gloss, same convention | syl | 0.468 (158) | 0.333 / 0.352 (0/165) | 0.333 / 0.381 (0/1000) | PASS |
| print | letter (secondary) | 0.389 (144) | 0.372 / 0.417 (3/166) | 0.373 / 0.423 (20/1000) | fail |
| gloss, same convention | letter | 0.349 (149) | 0.361 / 0.390 (18/165) | 0.356 / 0.401 (102/1000) | fail |

The rotation maximum of 0.803 for the print is one near-identity rotation (a shift of a letter or two lets the aligner slide
back into phase); the p95 is 0.327. The letter mode fails for both texts, as it did for the gloss in A2-DIN, so the
primary is the syllabic setting. With the same convention the gloss scores 0.468 (0.590 with its '+' wildcards). Moving to
the print raises it to 0.831, so the gap is the gloss reading, not notation.

**Rows changed vs key_syl.tsv: 7 of 29** (`f128/print_align/diff_vs_key_syl.tsv`): `#` d 5/13 -> c 7/13 (d 6 remains;
it is a c/d polyphone), `c` a 1/5 -> **r 4/4**, `r` b 1/4 -> **n 4/4**, `h` u 1/1 -> **p 1/1**, `zh` e 1/2 -> t 2/2, `B` s -> a
(1/1), `n` e -> r (1/1). Rows whose support rose to a clean C: `.` e 9/9, `f` n 11/11, `y` o 9/9, `D` a 4/4, `9` g 3/3,
`T` h 3/3, `3` d 5/5, `L` i 5/5. `1` e falls to 3/7 (M). The A2-DIN3 hill-climb had already moved c to r and r to n (both
now confirmed by the print). It left h = u, zh = e, B = s and n = e, and the print contradicts all four.

**3. f.130r with the print key, no repair** (`f130/print/score_print.py`, the statistic of score_f130.py, imported
unchanged): fr16 **-1.271** (key_syl -1.334). Free shuffles: mean -1.956, p95 -1.705, max -1.462, 0/1000. Frequency-banded
shuffles (seed 31001): mean -1.675, p95 -1.575, max -1.450, 0/1000. **Gate PASS.** The unrepaired print key matches the
score of the hill-climbed key (-1.271).

**Grades** (decode_key.py, decode.json job 3, 527 tokens, dots excluded; pre-registered rule: key_print agree >= 3 and
>= 0.5 and sign conf H -> C): **C 357, M 131, U 39, S 0, no H.** Caveat (sensitivity, not pre-registered): two of the C rows are
polyphones in the print alignment, `#` (c 7, d 6; 34 C tokens) and `v` (a 8, t 5; 32 C tokens). With both held at M:
**C 291, M 197, U 39.** The conservative figure should be used outside the repository. U = v' 23, 0' 14 and the two NEW signs:
they never occur on f.128, so the print cannot key them. Their repair values (t, s, l, r) stay M at best, in the superseded job 2.
h = p is now print-supported (1/1, so M, not I). D = a 4/4 in the print, so the f.130 words that want D = c/d stay I.

**Superseded:** decode.json job 2 (`f130/repair/key_repaired.tsv`, `f130/repair/tokens.tsv`, C 329 S 71 M 127) is
marked SUPERSEDED in its name and in `f130/repair/SUPERSEDED.md`. Its files are kept unedited, because repair_f130.py
--check regenerates them. The current reading is job 3 (`f130/print/reading.txt`; lower = C, UPPER = M).

**Reading, word level (my division; interpretation, not graded beyond its letters):** L05 "[c]onseruer ces ...
en l'obeissance" (before the clear "Messieurs de la ville"); L08 "...de dans ... bien bas ... qu'il ne s'o.. plus ...";
L09 "dehors les [f]orce[s] seruiront ... leur ..."; L10 "la uille et le roi ..."; L11 "pourvoir de ... [t]irer d'aultant
qu'il i a a per[d]re ... l'honneur" (before the clear "pour luy"). L01-L04 and L06-L07 are still undivided.

**4. Date.** No crop of the f.130 date line is on disk: the f269 source region (280,600,3360,1360) and the line crops cover
only the body as far as L11. Not looked at. The date stays flagged: iij (Bourdeau) or iiij (BnF finding aid, 1882 print, 4 July).

Rule 7: `python3 tools/decode_key.py ciphers/fr3621-dinteville-1592 --check` prints "reading up to date" (3 jobs);
`f128/print_align/align_print.py --check` and `f130/print/score_print.py --check` print "check: committed outputs match".
No spec, so judge_plaintext.py was not run as a spec judge. Requests: none. Vision calls: none. Rule 10: no novelty claim.

## Second verifier (VERIFY-DIN2, account 3, 3 Oct 2026, 08:09-08:25 UTC) -- see AUDIT.md "Second audit"

N3 is kept, with key source `period` (rebuilt from the 1882 print of f.128's plaintext). All three --check scripts pass, and
`verify/verify_din2.py --check` reproduces `verify/result2.json`. At fresh seeds 52001-3 the print key beats 0/3000 free and
0/3000 frequency-banded shuffles (max -1.417). The f.128 alignment beats a fresh shuffle at 0.831 vs max 0.350, 0/300. A
**new wrong-text control** aligns 20 real 16th-century French passages to the f.128 cipher with the same settings. It gives
f.128 consistency max 0.468 and f.130 max -1.440 against the real -1.271 (0/20), so the signal comes from the right
plaintext, not from the aligner.
**Licensed grades: C 177, M 311, U 39.** C needs at least 2 occurrences and no conflicting print alignment. The polyphones
`#` and `v` are M, and so are the conflicted rows `0` (e 11/18), `m` (u 8/10), `sq` (s 7/9) and `a` (q 4/5). For
comparison: pre-registered C 357, DIN-PRINT's conservative figure C 291, agree/n >= 0.75 C 253.
**Date:** the one native crop (`images/src_..._f269_400_3825_2450_175.jpg`) turned out to be a body line, not the date, so
the leaf is still unread at the date. Two print witnesses favour 4 July: the BnF *Catalogue des manuscrits français* (1868),
whose OCR reads "le un' juillet 1592" with u = ii in the same OCR, and the 1882 Revue. Bourdeau's leaf reading is iij.
**New print found:** the *Revue* also prints a different clear letter of the same day, from the Langres town council to
Nevers ("Le Conseil de Ville. Langres, 4 juillet 1592", IA revuedechampagn03unkngoog). Drouot, *Mayenne et la Bourgogne*
(1937), cites deciphered Dinteville letters elsewhere (8 July 1592; BnF fr.4718, fr.4075 f.37). Both ARCSI PDFs are now
read, and neither concerns this letter. Boltanski 2006 is unreachable; it is the N4 blocker together with JSTOR.

## Date line, conflict rows, Drouot siblings (DIN-FIRM, account 3, 3 Oct 2026, 08:27-08:45 UTC)

Brief `.claude/briefs/runs/2026-10-03-acct3-din-firm.md`. Step 2 rule pre-registered before any occurrence was read:
`firm/PREREG.md` (commit 6364b03d).

**1. Date: not settled; the date is not at the foot of f.130r.** One native region per the brief, canvas f269
x 280-3640, y 4180-5340 (`images/src_..._f269_280_4180_3360_1160.jpg`, 8 line crops `images/f130_dateblk_L01..L08`),
plus the rest of the leaf below it, y 5300-5762 (`images/src_..._f269_280_5300_3360_462.jpg`, `images/f130_datefoot_*`;
info.json gives the canvas as 4040 x 5762). Looked at twice (vision calls 2 of 2): the tool's debug overlay of the
4180-5340 block, then the native crops of its last two lines stacked over the foot's one written line. The block holds the
end of the clear body, the closing "V[ost]re tres humble et obeissant serviteur", the signature "Dinteville" and a
postscript at the left ("...Lorraine a laisse ... de Chaumont ... garnisons ... pour faciliter leur volte."). The
postscript ends on the foot line, and below it the row profile is blank to the canvas edge. **No date line in x 280-3640,
y 4180-5762.** Where it was not looked at: the left margin x 0-280 (the postscript is cut off there), the head of the
leaf y 0-600, and y 1960-3825 except the 175 px strip at 3825. The headings keep 3 July as Bourdeau read it, with
iiij (BnF 1868 catalogue, 1882 Revue) as the alternative. Nothing was corrected.

**2. Conflict rows sq and m** (`firm/conflicts.tsv`, `firm/firm_grades.py --check`):

| row | occurrence | print word | class | why |
|---|---|---|---|---|
| sq (s 7/9) | L03.1:30 | deux (`# 0 m sq`) | spelling | 'deus' is in tools/data/fr16 49 times (Catherine de Medicis: 'deus lestres', 'deus ou troys jours') |
| sq | L05.1:51 | cheuaux (`# T 1 m v al sq`) | unexplained | the gloss has other text here; 'cheuaus'/'chevaus' 0 in fr16 (chevaux 46, chevaulx 32); the next sign, 3 = d, starts 'descorte', so it is not a slip |
| m (u 8/10) | L04.1:43 | doiuent (`# y p m o f m h v c`) | unexplained | the t must sit between f = n and h = p, so m reads t here |
| m | L04.1:54 | trois (`sq m w y p sq`) | unexplained | the gloss also reads 'trois', so m reads t again |

**Neither row is promoted.** sq has one unexplained conflict. m reads t twice, in the print and in the gloss of
'trois' alike, so it looks like a real u/t polyphone (or a sign the transcription merges) and stays M. **Strict grades
unchanged: C 177, M 311, U 39.** decode.json job 4 (`f130/print/key_dk_strict.tsv`, `f130/print/reading_strict.txt`) now
carries these grades, so `tools/decode_key.py ciphers/fr3621-dinteville-1592 --check` reproduces them. The values are the
same as job 3, which keeps the pre-registered grades (C 357).

**3. Drouot (1937) siblings: the citations say less than VERIFY-DIN2's summary.** be-api phrase search of
IA41551607_0002 found two citations:
(a) "Dinteville au duc de Nevers, Langres, 8 juill. 1592, B.N., fr. 4718, f. 76", cited as an example of the
"alarme navarriste". It is **not** called deciphered.
(b) "l'intrigue de Chaumont en 1589 : ib., II, 281 ; B.N., fr. 4075, f. 37 (lettre déchiffrée) ; Dinteville au duc de
Nevers, Langres, 3 sept. 1589, ...". This is a deciphered letter on the 1589 Chaumont affair, and the snippet does not
name its writer.
Gallica: SRU `dc.source all "Français 4718"` returns 0, so fr.4718 has no Gallica copy found by this search. That is a
search result: its archivesetmanuscrits record and availability flag were not read. Gallica's **Français 4075** is
btv1b9060550k, "copies ... adressés au marquis de Coeuvres ... de 1613 à 1641, Tome IX" (17th-century copies, 223
canvases, none labelled with a folio). A 1589 deciphered letter does not fit that volume. Either Drouot's shelfmark is
garbled in the OCR or print, or it is another fonds. f.37 was not located (no folio labels and no vision budget to anchor
one). Neither letter was found carrying cipher plus decipherment. Manifest snapshot:
`sources/gallica-manifests/btv1b9060550k.json`.

Rule 7: `decode_key.py --check` (4 jobs) and `firm/firm_grades.py --check` both pass. Requests: gallica.bnf.fr 7 (2 region
fetches, of which 1 was reset and retried once and the first used a malformed ark and returned HTTP 500; 2 info.json, of
which 1 was reset; 5 SRU; 1 manifest), be-api.us.archive.org 9. Vision calls 2. Rule 10: no novelty claim.

## Date line located, not yet read (TWO-LOOKS, account 3, 3 Oct 2026, 08:53-09:10 UTC)

Brief `.claude/briefs/runs/2026-10-03-acct3-two-looks.md` part (A). Gallica requests 3 (one 500 on a doubled ark
prefix in the tool's `--ark` argument, then the whole canvas f269 0,0,4040,5762 native, then one native region that
missed the line), >=2 s apart, no block. Vision calls 3 of 3:
1. `images/f269_overview_808.jpg` (808 px, made locally from `images/src_ark_12148_btv1b52524472n_f269_0_0_4040_5762.jpg`).
   The leaf holds: the cipher-and-clear body to the line "...Lorraine a envoye Florainville du duc de Parme ...", then a
   short line in the same hand, then the stamp of the Bibliotheque royale at the right, then the second, larger-hand
   paragraph ("Monseigneur ce matin ..."), the closing, the signature and the postscript. The head (y 0-600) carries only
   "Monseigneur" and the folio number; the left margin shows no written line. The short line is the only candidate for
   a date line.
2. A native region x 1700-3200, y 3860-4120: placed too high, showed only the stamp (crop deleted).
3. `images/f130_dateline_L01_s2.jpg` (region 300,3800,2900,200 cut from the cached whole canvas with `--image`): this is
   the last clear-body line ("...a envoye Florainville du duc de Parme, ie say pour ... de produire ..."), not the date.
After call 3 the row ink profile of the cached canvas (x 300-1500 and x 1500-2900, 10 px bins) puts the next line at
y about 4060-4160 (right half 4100-4150, densest where the date words sit), with the large-hand paragraph starting at
about 4170. **DIN-FIRM's block began at y 4180, so it missed this line by about 30 px**; its finding that y 4180-5762
holds no date stands. The line is cut at native resolution in `images/f130_dateline2_L01_s1.jpg` and `_s2.jpg` (region
300,4030,2900,170 of the cached canvas) but **was not viewed**: the brief's 3 vision calls were spent. At 808 px the
day numeral is not legible, so **iij vs iiij is not settled; headings unchanged (3 July, Bourdeau; iiij the
alternative)**. Nothing corrected in NOTES/AUDIT; status.json's result title and document_id are the orchestrator's.

## Remaining gaps (DIN-FIRM, 3 Oct 2026; supersedes VERIFY-DIN2's list)
Read so far: f.130 527 of 527 cipher tokens decoded with the print-aligned key; strict C 177 / M 311 / U 39 (decode.json job 4, unchanged by DIN-FIRM's conflict check: sq and m not promoted); f.128 aligned to its 1882 print, consistency 0.831 vs shuffle max 0.358 and wrong-text max 0.468; date line absent from x 280-3640, y 4180-5762 of f269
- f.130 word-level reading (L01-L04, L06-L07 undivided; L05, L08-L11 phrases) - blocker: not-attempted; # (c/d), v (a/t) and m (u/t, DIN-FIRM) are polyphones, v' and 0' unkeyed; next: a word-division pass with #, v and m read in context and graded I, ~$4
- v', 0' and the NEW signs (39 tokens, absent from f.128) - blocker: not-attempted; no f.128 support; next: compare the sign set of fr.3623 f.23 (below), which may carry them with a decipherment, ~$4
- fr.3623 f.23 (no.15, Dinteville to Nevers, Italian, "avec chiffre et dechiffrement", DECODE R9452) - blocker: not-attempted; a further crib if the sign set matches; next: locate the canvas and compare its sign set with f128/gloss_pairs.tsv, ~$4
- Drouot-cited letters: fr.4718 f.76 (Dinteville to Nevers, 8 Jul 1592, not called deciphered) and "fr.4075 f.37" (1589 deciphered letter, writer unnamed, Gallica fr.4075 is a 1613-41 Coeuvres volume so the shelfmark does not fit) - blocker: not-attempted; shelfmark mismatch and no Gallica copy of fr.4718 found; next: read fr.4718's archivesetmanuscrits record and its availability flag, and Drouot's printed page for the 4075 citation (IA lending, a person's read), ~$2
- f.130 date (iij or iiij July) - blocker: not-attempted; line located at f269 y about 4060-4160 (TWO-LOOKS), crops cut but not viewed (vision budget spent); next: one vision call on images/f130_dateline2_L01_s1.jpg + _s2.jpg (disk only, no Gallica request), ~$1.5

## Escalation (DIN-FIRM, 3 Oct 2026; supersedes VERIFY-DIN2's list)
- [x] siblings: f.128r (no.114) transcribed with its interlinear gloss and aligned, consistency 0.590 vs rotated-gloss null max 0.353 (A2-DIN); re-aligned to its 1882 print, 0.831 vs shuffle max 0.358 (DIN-PRINT), wrong-text max 0.468 (VERIFY-DIN2)
- [ ] clear-pages: fr.3623 f.23 decipherment not yet compared; Drouot citations checked (DIN-FIRM): fr.4718 not found on Gallica, fr.4075 shelfmark mismatched (planned steps above)
- [x] known-keys: none in Tomokiyo's Nevers catalogue (Bourdeau; GF4-BATCH9 web check)
- [x] print: Gomberville seconde partie searched, letter absent (scGOM2, GF4-BATCH9); Revue de Champagne XII (1882) p.340 prints f.128, used as the key's plain text (VERIFY-DIN, DIN-PRINT); 1899 reprint, BnF catalogue 1868, Drouot 1937, ARCSI PDFs searched (VERIFY-DIN2)
- [x] key-rebuild: key aligned to the 1882 print of f.128 (7 of 29 rows changed vs key_syl), f.130 fr16 -1.271 vs free-shuffle max -1.462 and banded-shuffle max -1.450 (0/2000), no repair (DIN-PRINT); fresh seeds 0/6000, wrong-text 0/20 (VERIFY-DIN2); conflict rows sq/m checked per occurrence, not promoted (DIN-FIRM)
- [x] image-check: f.130 transcribed from Gallica f269 (2 blind passes + reconciliation, err_2reader 11%, f130/ciphertext.tsv, A2-DIN2); foot of f269 viewed for the date (DIN-FIRM); whole leaf at 808 px, date line located at y 4060-4160 and cut, not yet read (TWO-LOOKS)
- [n/a] retry: no failed instrument on this target to retry yet
Verdict: keep going: 5 internal gaps; cheapest next: one look at the cut date-line crops images/f130_dateline2_L01_s1/s2 (~$1.5, disk only), then fr.3623 f.23's sign set for v' and 0' (~$4)


## Date line read (account-3 orchestrator, 3 Oct 2026 ~09:15 UTC)

One look at TWO-LOOKS' crop images/f130_dateline2_L01_s1.jpg (Gallica f269, y ~4060-4160), zoomed: "... De Langres le iiij^e Juillet 15[92]". After a long lead-in stroke the day numeral has four minims, the last with a j descender, and a superscript e: iiij, i.e. **4 July 1592**. This agrees with the BnF Catalogue (1868) and the 1882 Revue de Champagne; Bourdeau's iij appears to drop one minim. Confidence: fairly high, not certain (minims in a cursive hand). Headings that say 3 July should read 4 July; the status.json result is updated.
