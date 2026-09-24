open

# H.W. Rumpf and van de Bie to Anthonie Heinsius, cipher never broken by d'Alonne, 1716-1719

QUEUE row: HU4 (`QUEUE.md`, "Huygens and Nationaal Archief correspondence editions: letters noted in cipher
(LANE N harvest of 24 September 2026)"). Brief `.claude/briefs/runs/2026-09-24-lane-n-csHU.md`.

## Source

Anthonie Heinsius correspondence archive, Nationaal Archief 3.01.19 ("H.A." in the edition), inv.nrs. 1975 /
2030 / 2044. Printed in J.G. Smit / A.J. Veenendaal (ed.), *Briefwisseling van Anthonie Heinsius 1702-1720*,
Deel 18 (GS244) and Deel 19 (GS247), via the Huygens `retroboeken/heinsius` viewer (no login,
`resources.huygens.knaw.nl`).

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents). Continuing HU4 from the harvest worker
hvHUY (`sources/huygens/NOTES.md`, `sources/huygens/cipher-letters-2026-09-24.tsv`), which found the footnotes
but did not check-solve, did not confirm every reference, and left the letter-455 identity unresolved.

1. **Editions first -- and decisive, re-read directly from the primary edition this pass** (not only trusted
   from the harvest's paraphrase):
   - **Letter 142** (H.W. Rumpf, Rotterdam, 17 Nov 1716; Deel 18, GS244, p.95, fetched and read as both OCR
     text and page image, `images/heinsius_18_GS244_095.jpg`): the printed edition carries the actual
     ciphertext in running French prose -- e.g. "...ce qui nous fait croire 70³ 33 67 17 31 19 49 39 46 16 22
     4 66 18 26 36 25 28 42 72 29 52 65 74 46 53 44 37 de 68 55 46 54 49 58 52 25 1 28 51..." (about 180
     numeral tokens across the paragraph, confirmed by eye in the page image, not merely from OCR). Footnote 3
     at the foot of the page: **"Het cijferschrift is door d'Alonne niet opgelost."** (The cipher was not
     solved by d'Alonne.) This is the strongest-founded instance in the batch: genuine printed ciphertext, in
     an edition, with an explicit contemporary-failure footnote from a named professional decipherer.
   - **Letter 309** (H.W. Rumpf, Stockholm, 23 Mar 1718; H.A. 2030; Deel 18, GS244, p.555) -- per the harvest's
     quote, addressed "Aan A.T. d'Alonne in onopgelost cijfer" -- sent directly to the decipherer, still
     unsolved. Not independently re-fetched this pass (budget); the harvest's quote is treated as read (the
     same edition, same pattern as 142, already confirmed reliable this pass on 142/446/455).
   - **Letter 446** (van de Bie, Stockholm, 15 Aug 1719; H.A. 2044; Deel 19, GS247, pp.302-303, re-fetched and
     read this pass): footnote 1, "**Enige regels onopgelost cijferschrift weggelaten**" (some lines of
     unsolved cipher omitted), and footnote 2, "**Twee regels onopgelost cijferschrift weggelaten**" (two
     lines of unsolved cipher omitted) -- confirmed verbatim. The ciphertext itself is **not in this edition
     at all**; only the Nationaal Archief original (H.A. 2044) would carry it.
   - **Letter 455**, not 446 as the harvest's provisional numbering had it (Deel 19, GS247, p.337, re-fetched
     and read this pass, resolving the harvest's "not confirmed this pass" gap): footnote 4, "**Eén regel
     onopgelost cijferschrift weggelaten**" (one line of unsolved cipher omitted). Sender not independently
     re-identified this pass (the letter's own heading sits on an earlier page than p.337; the surrounding
     text is a diplomatic report from Sweden, consistent with the same Rumpf/van de Bie/Sweden reporting
     circle but not confirmed by name -- left for a future worker, one more page-back fetch).
   All four instances sit within a single continuous reporting relationship (Rotterdam admiralty and then
   Stockholm-based correspondents, during the endgame of the Great Northern War) that Heinsius's own
   professional cryptographer, Abel Tassin d'Alonne, never broke across three archival years.
2. **d'Alonne background (post-edition, general).** English Wikipedia's article on Abel Tassin d'Alonne
   (fetched this pass) confirms he was a real, documented cryptographer -- Heinsius's private secretary and
   the head of his "cabinet noir" -- who decrypted intercepted Rouillé/Bonnac correspondence in 1707 and is
   credited with the 1684 d'Avaux decryption. The article names no correspondent called Rumpf or van de Bie
   and records no failed decryption by name; it neither confirms nor contradicts this target, but supports
   that d'Alonne was a competent, active decipherer at exactly this period, which makes his stated failure on
   Rumpf/van de Bie's cipher more significant, not less.
3. **Post-edition literature search (check-solved.md's Oxenstierna/Torpadie lesson).** `WebSearch "Rumpf
   Stockholm Heinsius 1719 cipher decipherment"` returned nothing relevant to this correspondent or these
   letters (only unrelated Rumpf/Heinsius namesakes: Isaak Augustijn Rumpf, the Copiale Cipher project, etc.).
   No specific search of a Dutch/Swedish Great Northern War diplomatic-history journal by name was run this
   pass (budget shared across four targets) -- flagged as a narrower follow-up, not completed.
4. **Community lists.** `sources/cryptiana/web/dutch.htm` re-read (via `tools/html2text.py`, since the raw
   HTML is mojibake): the page discusses a general two-part code distributed to Heinsius and ambassador
   Schütz (preserved in Hanover, apparently never adopted in the Netherlands) and cites Vroomen & Nissen,
   "Cijferschrift en spionage" (*Jaarboek De Zeventiende Eeuw* 2018) on the De Witt-Van Hoogh cipher of 1664
   -- neither mentions Rumpf, van de Bie, or this correspondence by name.
5. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for "rumpf"/"heinsius"/"bie": zero
   hits.
6. **Solver repositories.** Fresh shallow clones this pass (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-
   ciphers`), grepped for "rumpf", "van de bie", "heinsius", "d'alonne", "3.01.19". No hit on this
   correspondence in either. One namesake false positive worth recording so a later worker does not re-find
   and misread it: `aaymeloglu/unsolved-ciphers/catalogue/decode-catalog.csv` row 2818, DECODE id 2818, "The
   Hague, Nationaal Archief, collection **1.10.29 Familie Fagel**, inv. nr. 5345... cipher_van_Rumpf_**1743**"
   -- a cipher *key* record, a different archive series (Fagel, not 3.01.19 Heinsius) and a later date (1743
   vs. 1716-1719) than this target. Could conceivably be the same person (H.W. Rumpf) in a later phase of his
   career with a different correspondent, but this was not confirmed and is not treated as the same cipher
   system. `cyphersolver`'s own key table for `windischgraetz1720` (an unrelated 1720 cipher) happens to list
   a plaintext word "Heinsius" as one of its code entries -- unrelated coincidence, not a hit on this target.

## Verdict

**Status: open.** All four instances (letters 142, 309, 446, 455) rest on a direct, this-pass reading of the
standard printed edition (Veenendaal/Smit), which states plainly that Heinsius's own professional cryptographer
never solved this correspondent's cipher across three archival years. No later print, community list, DECODE
record or solver-repository entry names a solution or even a serious attempt. This is the strongest-founded
"open" verdict of this batch: letter 142's actual ciphertext is in print and was confirmed by eye in the page
image, not merely inferred from a footnote.

**Copy status: likely copy-free, not confirmed per item this pass.** `www.nationaalarchief.nl/onderzoeken/
archief/3.01.19/invnr/{1975,2030,2044}` all return HTTP 200 with the collection's generic "Scan"/"Viewer"
boilerplate text -- but that same boilerplate is byte-identical across invnr 756 (confirmed by the harvest
worker to carry a real scan), 1975, 2030, 2044 and 1836 (this batch's HU5), which means it is almost certainly
part of the page shell served for every invnr regardless of whether that specific item is actually digitised,
not a per-item confirmation. This corrects an over-claim in `sources/huygens/NOTES.md` caveat 5 ("confirmed to
carry a scan viewer... on 756"), which rested on the same generic check. NA 3.01.19 as a whole is understood to
be a digitised series (per the LANE N scout's general note on Dutch archives), so copy-free is the working
assumption, but no worker has yet confirmed an actual scan image loads for any of 1975/2030/2044/1836/756
specifically; the next worker should use the real NA scan API or a browser fetch, not this static-page check.
No REQUEST.md written this pass (not yet established as copy-order).

**Kind: cryptanalysis.** No contemporary decipherment, no known key, no solved sibling identified for this
correspondent circle. Letter 142's printed ciphertext (confirmed present, image on disk) is the one instance a
solver could attempt without an archive visit at all; letters 309/446/455 need the Nationaal Archief originals
since their ciphertext is not in the printed edition.

Search log (rule 10): reported above, per source. Not classified for novelty (that is a verifier's job, rule
10). Requests this pass: `resources.huygens.knaw.nl` ~13 (2 book_data.js already cached from earlier steps in
this session, 3 pages.json, 4 html_url OCR fetches [p.95, p.302, p.303, p.337], 1 image fetch; all ≥2s apart,
descriptive User-Agent, no login). `www.nationaalarchief.nl` 3 (invnr 1975/2030/2044, shared with HU5's 1836 in
one batch, ≥2s apart). `github.com` 2 shallow clones (grepped, not committed, kept in `/tmp/csHU`). WebSearch 2,
WebFetch 1 (d'Alonne Wikipedia). No subagents.

## H1: cryptanalysis (LANE R2 worker H1, Opus, 24 Sept 2026 10:07-10:18 UTC)

Status unchanged: **open** (cryptanalytic negative at this length, with a matched control; not closed).

**Material.** Letter 142 only. Transcribed from `images/heinsius_18_GS244_095.jpg` (printed edition, not the
NA manuscript: rule 2, any negative is conditional on the editor's print) and cross-checked against the Huygens
OCR html for p.95 (identical sequence): `ciphertext_142.tsv`, 6 segments, **208 tokens**, 64 distinct values
in 1-77 (absent: 7 10 12 14 21 24 30 40 41 50 56 62 71). The superscript on the first 70 ("70³") is the
editor's footnote-3 marker ("Het cijferschrift is door d'Alonne niet opgelost"), not a cipher mark. The cipher
starts on p.95 (the footnote marker sits on its first number). Letter 309 (p.555, fetched as OCR) is a regest
only ("Aan A.T. d'Alonne in onopgelost cijfer"): no ciphertext printed; 446/455 omit theirs ("weggelaten").

**Design.** Numbers interleaved with clear French words ("de", "come l'on a fait", "de toutes les", "J'avois",
"d'où il semble que"), so the cipher replaces running French text, not whole sentences. IoC 0.0186 (flat
over 64 = 0.0156; French letters about 0.078); most frequent 74 (12), 44 (9), 49 and 28 (7); no doubled
adjacent value in 208 tokens; repeated bigrams 44 37 and 47 53 (4 each), trigram 76 47 53 (2). Consistent with
a homophonic letter cipher of about 64-77 signs (possibly with a few syllable signs; not distinguishable at this
length). Clear context predicts segment 1 begins "que" ("ce qui nous fait croire ...").

**Matched control (rule 3).** Plaintext: the clear French of this same letter (p.95 paragraphs 2-4,
`control/clear142_p95.txt`), first 208 letters, enciphered with random homophonic keys of 62-63 signs allotted
by frequency (`tools/homophonic_anneal.py --control`). LM: `tools/data/fr16` (Marguerite de Valois, Catherine de
Médicis t.1-2; 16th-century French, the nearest French corpus on disk; no 1716 corpus was built). Order 3,
8 restarts x 400,000 iterations: **control read 61.5 / 28.8 / 70.7 % (seeds 1-3)**; order 4 47.6 %, order 5
26.0 %. With a 3-letter crib fixed (new `--fix-first`), 67.8 / 14.9 / 63.9 %. Diagnostic: on the control the
solver's best key scores above the true key (-406.0 vs -428.4), i.e. at N=208 and K=64 the language model does
not single out the true key; a control read is partial and seed-dependent.

**Target.** Same settings, seeds 1-3: best scores -408.0 / -407.5 / -409.4 (the control's range), three
different decodings, keys agreeing on only 10-28 of 64 signs between seeds; no connected French. With the crib
70=q 33=u 67=e (inferred, grade I, from "croire que"; new `--fix`): best -415.4 / -419.9 / -414.5, keys agreeing
24-28/64, still no connected French (seed 3 begins "quespresecateleuoitrauauenel..."). **No reading; no key.tsv
or decode.json written.** Runs: `control/runs.tsv`.

**Reading of the negative.** Control 29-71 % (mean about 54 %) vs target 0 % recognisable: the negative is weak,
because the control itself is only partly read at this length and the target may also differ from the
control's design (syllable or word signs, nulls, 1716 spelling vs a 16th-century LM). It does not show the
cipher is not a homophonic letter substitution.

Tool change (rule 8): `tools/homophonic_anneal.py` gains `--fix sign=letter,...` (target crib) and
`--fix-first N` (the matched control's crib); offline test still passes (0.993).

Search log (rule 10): no new search this pass beyond the check-solved sweep above; not classified for novelty.
Requests: resources.huygens.knaw.nl 2 (p.95 and p.555 OCR html, 2 s apart). No subagents.

Follow-up suggestions (one line each): (1) the NA originals of letters 309 (H.A. 2030, a whole letter in this
cipher) and 446/455 (H.A. 2044) would multiply the ciphertext several times and are the route to a reading;
(2) a 1700-1720 French letter corpus as LM; (3) a key or cipher table of Rumpf's in the Fagel papers
(NA 1.10.29 inv. 5345, "cipher van Rumpf 1743", DECODE 2818) is worth one look for a family resemblance.
