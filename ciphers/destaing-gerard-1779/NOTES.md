open
Doniol vol. IV (archive.org `histoiredelapart04doniuoft`) be-api full-text searched again by this worker (3 Oct 2026: "croisière de la Caroline" and "Estaing écrivait" hit the p.774 paraphrase; "30 avril 1779" 0 hits; "chiffré"/"pli chiffré" hit only a 6 Jan 1779 Martinique packet), and HMC *Report on American MSS in the Royal Institution* vols 1-2 (`reportonamerican12greauoft`) and HMC *Stopford-Sackville* vol. 2 (`reportonmanuscri02grea_0`) grepped whole-volume (djvu) -- none prints the 30 April 1779 letter or a British decipherment of it.
Doniol, *Histoire de la participation de la France...* vol. IV (archive.org `histoiredelapart04doniuoft`) and Meng, *Despatches and Instructions of C. A. Gérard* (archive.org `despatchesinstru00fran`) full-text searched by this worker (be-api fts, controls found: "Terre-Neuve"/"croisière de la Caroline" p.774 in Doniol iv, "Vergennes" in Meng) -- neither prints the 30 April 1779 letter's cipher passage deciphered.

## Check-solved (LANE CX2, 25 Sept 2026)

Re-check of an `open` target already carrying a solver-repository citation (Bourdeau, 15 Sept 2026, below), per the intake gate's requirement that this worker's own search be logged, not only quoted.

1. **Web search.** `WebSearch` "d'Estaing Gerard 1779 cipher letter solves Claude GPT deciphered" -- no hit for this specific item; general hits for other AI-cipher-solve stories (Cyphral Distich, a GPT-6 Nazi-radio solve) and dbourdeau's own site, not this target. No model-solve announcement found.
2. **Standard edition/calendar, this worker's own read.** Doniol vol. IV (`histoiredelapart04doniuoft`, archive.org) full-text searched (be-api `/fts/v1/search`, 1.6 s apart): control "Terre-Neuve" -> hit, page 774 (five snippets, footnote apparatus citing "États-Unis, suppléments, t. I, n° 156/158/1[5]7" and "Estaing écrivait alors de la Martinique à Gérard"); target phrase "croisière de la Caroline" (a crib phrase from our own NOTES.md's Ideas line) -> hit, same page 774, exact wording "être à la fin de may sur la croisière de la Caroline Méridionale". This confirms page 774 (this scan's pagination, not Bourdeau's "130-131", which may be a different scan/edition's numbering of the same passage) carries Doniol's own narrative/footnote treatment of the d'Estaing-Gérard correspondence context -- paraphrase and citation, not a verbatim decipherment of the 30 April letter. Meng 1939 (`despatchesinstru00fran`, archive.org) full-text searched: control "Vergennes" -> hit; "Estaing cipher" -> hit, page 988, in Meng's historical introduction discussing Gérard's use of cipher generally ("under the protection of a cipher... omitted from the office transcription of the cipher ordinarily employed by Gérard") and a footnote "explanation of the misfortune that followed d'Estaing's squadron in American waters. See Meng" -- again general/contextual, not the 30 April letter's plaintext. `"March 9" Estaing` -> no hit in Meng (the 9 March letter Bourdeau cited as summarised at Meng's n°80 was not found by this worker's phrase search; may use different date formatting in this scan's OCR). Clements Library's own finding-aid page (`clements.umich.edu`) and the CalmView-style exhibit page both returned HTTP 403 to curl -- not opened this sweep, consistent with the "found-solved"/pipeline note that this site blocks unauthenticated fetches; not chased further (out of scope, no browser-tool budget spent given the archive.org route already gave a controlled search).
3. **Community lists.** `sources/cryptiana/web/unsolved.htm` (on disk) greped for "destaing"/"d'estaing": one entry, lines 590-591, verbatim: "An encoded letter from Admiral D'Estaing to Gerard, French minister in Philadelphia, dated 30 April 1779 is preserved in William L. Clements Library, Clinton Papers, 'vol 64:14'. British Commander Sir Henry Clinton forwarded this intercepted letter home in July. (The next item 'vol 64:15' is a letter in clear from D'Estaing to Jean Holker from the same date in two copies, of which one is in André's hand.)" -- Tomokiyo lists it unsolved, confirming the NOTES.md line 6 "Background page" claim independently. `sources/cryptiana/web/marbois.htm` and the Luzerne blog post: no "destaing"/"d'estaing" hit by this worker's own grep (matches the existing note that neither decodes it).
4. **DECODE.** `sources/decode/*.tsv` (on disk catalogue snapshots, 24 Sept 2026) grepped for "estaing"/"gerard": no hit. Not on DECODE.
5. **Bourdeau.** Shallow-cloned `dbourdeau/cyphersolver` fresh this session (25 Sept 2026, superseding the 19 Sept clone this repo's LESSONS.md describes). `destaing/NOTES.md` verbatim: 217 numbers, 105 distinct, max 597; Doniol iv 130-131 "quotes/paraphrases the 9 March 1779 cipher letter... cribs only"; Meng's Gérard n°80 (6 May 1779) "summarises the 9 March letter (AAE-cp EU Supt 1:263) but the 30 April letter is not printed; its deciphered copy would be in AAE, Correspondance politique, États-Unis suppléments t.1 (not online), or a British decrypt in TNA if Willes read it"; the Luzerne 1781 code on cryptiana's blog runs to 1199, a different/larger code. Verdict: skipped.
6. **Aymeloglu.** Shallow-cloned `aaymeloglu/unsolved-ciphers` fresh this session: no file matches "destaing", "d'estaing" or "gérard"/"gerard" anywhere in the repository.

Requests: archive.org (advancedsearch + be-api fts) 8, 1.6 s apart; clements.umich.edu 2 (both 403); WebSearch 1.

Intake gate: `open` retained -- both editions named above were read by this worker (full-text search with control named and found), matching Bourdeau's independent finding that neither prints the 30 April letter's plaintext. No change to the target's status; the AAE Correspondance politique, États-Unis suppléments t.1 (not online) remains the only named route to a decipherment.

## ZX2-EST (25 Sept 2026, LANE ZX2)

Intake gate re-checked this session: `python3 tools/intake_gate_check.py destaing-gerard-1779` -> `destaing-gerard-1779: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Job: siblings, period codes with a matched control, cribs (`.claude/briefs/runs/2026-09-25-lane-zx2-est.md`).

**1. Tokenization and structure.** `tokenize_ciphertext.py` splits `ciphertext.txt` on its own document structure (dateline / salutation / cipher run A / embedded clear clause / cipher run B / clear closing paragraph + signature) rather than a naive digit regex, which over-counts by 2 (the dateline's "30" in "le 30 avril 1779", and the plain "9" inside "le 9 de mars dernier"). Result: **216 CODE tokens, 104 distinct, max 597** (vs Bourdeau/cyphersolver's cited "217 numbers, 105 distinct, max 597" -- one token off in both total and distinct count; not chased further, most likely a difference in whether the dateline/embedded-date digits are counted, see `ciphertext_note` in the spec). Output: `ciphertext.tsv` (pos, code_idx, kind CODE/CLEAR, token, before/after context, line_role).

Frequency: top codes 401 (13x), 382 (10x), 152 (8x), 109 (7x), 450 (6x), 235 (6x), 240 (5x), 410 (5x), 471 (4x), 402 (4x), 378 (4x), 346 (4x) -- matches the existing NOTES.md "Ideas" line's guess (401, 382, 152, 109, 450, 471) exactly. 56 of 104 distinct codes are hapax (54%), a Zipfian shape consistent with a nomenclator representing natural-language word/syllable frequency (function words repeat, content words don't). Value-range histogram is lopsided toward 400-499 (55 of 216 tokens), but that bin also holds most of the top-frequency codes, so the lopsidedness is a frequency artifact, not necessarily a structural one. Parity near-even (105 odd / 111 even); mod-5 residues uneven (0:56, 1:45, 2:58, 3:28, 4:29) but not a clean separator signal the way Soglia's "8 never in second place" was. No adjacent doubled codes (0 of 215 adjacent pairs).

**One-part vs two-part:** not directly testable from this letter. The only place CODE and CLEAR meet is at the boundaries of the two cipher runs (whole clauses of clear French bracket whole runs of code, not word-by-word alternation), so there is no clear-text-neighbour crib to check numeric order against for even one code. As a period prior only (grade M): `sources/cryptiana/web/marbois.htm` states its four reconstructed 1780-82 French codes (A/B/C/D, Vergennes/Luzerne/Montmorin/Castries correspondence) are explicitly **non-alphabetical (two-part)**. Suggestive of the design family, not evidence about this specific code.

**2. Siblings** (`siblings.tsv`). None found.
- Clements Library finding aid: `clements.umich.edu` and `findingaids.lib.umich.edu` both 403 to curl; headless browser (`tools/browser_fetch.js`) timed out behind a Cloudflare challenge (`brunhild.challenges.cloudflare.com` connect_rejected via the agent proxy); Wayback CDX fallback (`web.archive.org/cdx/search/cdx`) failed twice with "Recv failure: Connection reset by peer" (a transport-level failure, not a challenge page -- one retry used per the good-citizen rule, not chased further).
- Doniol vol.IV (`histoiredelapart04doniuoft`) numeral-run sweep: `tools/ia_numeral_runs.py` and two direct-node fetch attempts all got HTTP 500 from archive.org's download redirector, although `/metadata` confirms `histoiredelapart04doniuoft_djvu.txt` exists on `ia801602.us.archive.org`. One retry used; not chased further this session. **Doniol vol.IV was not swept for numeral runs.**
- Meng (`despatchesinstru00fran`) numeral-run sweep: succeeded, negative. 230 clusters found (`--min-tokens 6 --share 0.6`), all are book-index page-number lists (repeat_rate 0.00-0.17, prose context is index headwords like "New York, City of," or "Hudson River, military operations"), none has a cipher-shaped repeat profile. No sibling ciphertext in this volume.
- `sources/cryptiana/web/marbois.htm`: no "destaing"/"d'estaing" hit (already noted in the check-solved section above); describes a different code family for different, later correspondents.

**3. Period codes** (`period_code_test.py`, matched random-draw control, 1000 draws). Extracted the two genuine decoded-word specimens printed in `marbois.htm` (not its structural "indicator?"/"punctuation" annotations): the Marbois-to-Vergennes 13 March 1782 passage (Code A/B mixed, 160 distinct code keys) and the Marbois-to-Castries 17 March 1782 passage (Code C, 45 distinct code keys). Tested how many of d'Estaing's 104 distinct code VALUES also appear as KEYS in each dictionary, against a control of 1000 random 104-number draws from the same range (2-597):

| date (UTC) | family | parameters | seeds | CONTROL mean (5-95pct) | TARGET hits | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 | period_code_overlap (hand-run, not in tools/family_run.py) | marbois Code A/B specimen (160 keys, range 9-1195) vs N=104 draws range 2-597 | 1 (1000 MC draws) | 14.51 (10-20) | 17 | n/a (overlap count, not a plaintext candidate) | no -- inside control band | for LANE ZX2: destaing period code test |
| 25 Sept 2026 | period_code_overlap | marbois Code C specimen (45 keys, range 8-1154) vs N=104 draws range 2-597 | 1 (1000 MC draws) | 4.41 (2-8) | 6 | n/a | no -- inside control band | for LANE ZX2: destaing period code test |
| 25 Sept 2026 | period_code_overlap | marbois Code A/B+C combined (200 keys) vs N=104 draws range 2-597 | 1 (1000 MC draws) | 18.17 (13-24) | 22 | n/a | no -- inside control band | for LANE ZX2: destaing period code test |

All three real-overlap counts sit inside the control's 5th-95th percentile band (17 vs [10,20]; 6 vs [2,8]; 22 vs [13,24]) -- **a control-backed negative**: the numeric overlap between d'Estaing's code and marbois.htm's four 1780-82 codes is what bare chance predicts, consistent with these being different codebooks (different correspondents, three years later). Note also carries a caveat already true by construction: even a real hit would only mean the same integer appears in both books, not that it carries the same word (two-part codes assign numbers per book independently) -- see script docstring. Full output in `period_code_test.py`'s run (rerun with `python3 period_code_test.py`).

**4. Cribs** (`cribs.tsv`, no decode forced). Doniol vol.IV full-text search (`be-api.us.archive.org/fts/v1/search`, identifier `histoiredelapart04doniuoft`, phrases individually quoted) turned up more than the check-solved worker's earlier probe: page 774 carries the sentence **"...en précédaient d'autres. Estaing écrivait alors de la Martinique à Gérard qu'il espérait..."** -- Doniol's own narrative paraphrase of THIS 30 April letter (not only the 9 March one), on the same page the check-solved worker already found the phrase "être à la fin de may sur la croisière de la Caroline Méridionale" on. Candidate reading (grade M, inferred, not decoded): BODY_CODE_B (the 76-code run after "si ce la est") plausibly corresponds to that "fin de mai... croisière de la Caroline Méridionale" clause, since it is Doniol's paraphrase of content following the letter's own reference to "le plan"; BODY_CODE_A (the 140-code run before "Je me flatte...") is not directly paraphrased in any snippet found this session. Topical corroboration only (no new crib): the letter's own already-clear closing paragraph (Georgia, Americans, Spanish neighbours) matches Doniol p.774's "l'invasion des troupes anglaises en Géorgie et leur marche sur la Caroline méridionale" and "dangereuse pour les établissemens espagnols" almost word for word -- confirms Doniol p.774 is about this letter's news, supporting (not proving) that its other clauses paraphrase the ciphered parts too. Also confirmed: "Monsieur de le Marquis de Bretigni" (clear text, line 5) is a real correspondent -- Doniol prints "COPIE DE LA LETTRE DE M. LE MARQUIS DE BRÉTIGNY À M. D'ESTAING", 7 July 1779 (a later reply, not fetched/read this session).

**5. Spec.** `specs/destaing-gerard-1779.json` written: judge block uses `language: fr` (`tools/data/fr16`, 16th-c. Catherine de Medici letters) because `tools/data/fr18` did not exist yet when this was written (19:16 UTC; ZX2-FR18 claimed building it the same round) -- era mismatch (16th c. corpus vs an 18th c. letter) logged in the spec's own `note_corpus` field per the job brief's fallback instruction, not silently accepted. `min_word_cover: 0.6` included (RETRO-2026-09-25k flagged 7 of 10 bSPEC specs missing it); sanity-checked with a dummy 140-letter French sentence -- `tools/judge_plaintext.py` returns PASS with all three checks (length/language/words) firing, so the block is live, not silently skipped. No cribs wired into the hard gate (rule 10 / "without forcing a decode": every candidate this session is grade M, not confirmed) -- `crib_candidates_note` in the spec points to `cribs.tsv` instead.

**Grades:** all findings this session are S (structural/cryptanalytic, with controls) or M (inferred); no H or C tokens produced (no key applied, no reading claimed). Novelty not classified (rule 10, this worker's job).

Requests this session: archive.org (be-api fts + numeral-run sweep + metadata + direct-node fetches) 19, 1.5-1.6s apart; clements.umich.edu 1 (403); findingaids.lib.umich.edu 1 (403) + 1 browser-tool attempt (Cloudflare timeout); web.archive.org 2 (connection reset, 1 retry used). No subagents.

---

# Admiral d'Estaing to Gérard (Martinique, 30 April 1779)

- **Source:** William L. Clements Library, Clinton Papers, vol.64:14. Intercepted by the British and forwarded by Sir Henry Clinton in July 1779.
- **Status:** Open.
- **Transcription:** `ciphertext.txt`. French code, numbers up to 597, with a substantial cleartext passage in the middle and a cleartext closing.
- **Background page:** `sources/cryptiana/web/marbois.htm` (four French diplomatic codes of the period, none of which decodes this). Also `sources/cryptiana/blog/2021_09_decoded-but-not-identified-code-of.html` (a decoded but unidentified code of Luzerne).
- **Ideas:** Highest number 597 means a code of about 600 entries, smaller than the diplomatic codes. The cleartext middle passage names the subject (a plan sent in cipher on 9 March, Georgia, the Americans, the Spanish). Repeated groups such as 401, 382, 152, 109, 450, 471 are probably function words or the most common syllables. Look for a second letter in the same code in the Clinton Papers or in Gérard's papers.
- **Solver status (19 Sept 2026):** Skipped by Bourdeau (cyphersolver/destaing), 15 Sept 2026: 217 tokens of a 600-entry code, no key material. The deciphered copy would be in AAE Correspondance politique, Etats-Unis supplements t.1.

## Next step from the method registers (27 Sept 2026, parent 7k, from LESSONS-TOMOKIYO.md (d))

Named next step (not run): Tomokiyo's partial-encoding and dictionary-position steps (codebreaking.htm "Partial Encoding",
"Andre Langie's Example"). Guess the code groups at the two clear/code boundaries from the bracketing French clauses, then
test a one-part hypothesis by placing the frequent groups (de, la, le, que) at their dictionary-position bands in the 1-597
range; log support or no support against a shuffled-range control (rule 3). Cost band S (script pass; needs
`tools/freq.py --split-at` and `--onepart-dict`, SYSTEM.md "Tools wanted", added by the worker that runs it). Status stays open.

## DES-PART (27 Sept 2026, parent worker DES-PART)

Ran the named next step above. Intake gate re-checked: `python3 tools/intake_gate_check.py destaing-gerard-1779` ->
`open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Script-only, no subagents,
no network.

**U1: frequency and boundary groups.** `structure/codes_only.txt` (216 CODE tokens, the two runs concatenated in
document order, stripped of the CLEAR clause and header/closing text via `ciphertext.tsv`'s own `kind` column --
Note: concatenating the two runs creates one artificial adjacency at the seam, code_idx 139/140 (tokens 287|65),
that does not exist in the real letter; this affects only the single contact-table entry for the pair "287 65"/"65
367" and not the frequency counts, split-at counts, or the U3 test below, none of which depend on run-adjacency).
`tools/freq.py structure/codes_only.txt --contacts 12 --split-at 300` -> `structure/u1_contacts_split.tsv`:

| token | count | pct | self_succession | tag |
|---|---|---|---|---|
| 401 | 13 | 6.0% | 0 | neither |
| 382 | 10 | 4.6% | 0 | neither |
| 152 | 8 | 3.7% | 0 | neither |
| 109 | 7 | 3.2% | 0 | neither |
| 450 | 6 | 2.8% | 0 | neither |
| 235 | 6 | 2.8% | 0 | neither |
| 240 | 5 | 2.3% | 0 | neither |
| 410 | 5 | 2.3% | 0 | **prefix-like** |
| 471 | 4 | 1.9% | 0 | **suffix-like** |
| 402 | 4 | 1.9% | 0 | neither |
| 378 | 4 | 1.9% | 0 | neither |
| 346 | 4 | 1.9% | 0 | neither |

Matches ZX2-EST's earlier top-12 frequency list exactly (see check-solved/ZX2-EST section above); new this
session: 410 tags prefix-like (right context concentrated on 380/400, left context all-distinct) and 471 tags
suffix-like (left context concentrated on 109, right context all-distinct) under `--contacts`' Yardley-42635
rule -- both below `--tag-min`'s usual comfort zone (counts 5 and 4) so noted, not leaned on. `--split-at 300`:
low(<300) 108 tokens/58 distinct/IC 0.0190, high(>=300) 108 tokens/46 distinct/IC 0.0339 -- the high side is
somewhat less flat than the low side, but neither approaches a tight monoalphabetic block's IC (cf.
berthier-napoleon-1812's 0.0395-0.0742 low-block finding); not read as a structural signal on its own.

**Boundary groups** (verbatim, from `ciphertext.tsv`):

| run | position | codes | clear text on the other side |
|---|---|---|---|
| BODY_CODE_A start | code_idx 0-1 | 240, 318 | ...preceded by "Monsieur" (end of salutation) |
| BODY_CODE_A end | code_idx 138-139 | 14, 287 | ...followed by "Je me flatte que j'aurai l'ordre ou la permission de suivre..." |
| BODY_CODE_B start | code_idx 140-141 | 65, 367 | preceded by "...le 9 de mars dernier, si ce la est" |
| BODY_CODE_B end | code_idx 214-215 | 137, 401 | ...followed by "Monsieur de le Marquis de Bretigni que vous aviéz eu la bonté de m'annoncer n'est point arrivé..." |

**U2: boundary grammar (grade M, no candidate is a reading).** Two of the four boundaries are genuinely
grammar-forced (clause-initial, the code run opens a sentence whose syntax is fixed by what follows); the
other two are sentence-final (the code run ends before an unrelated new sentence/paragraph begins), which
18th-c. French syntax does not constrain beyond "ends with terminal punctuation" -- flagged as weak rather
than papered over with false confidence.

| boundary | constraint | forced word class | candidates (M, <=3, not a reading) |
|---|---|---|---|
| BODY_CODE_A start (after "Monsieur") | strong -- opens the letter's first independent clause; French finite clauses require an explicit subject | subject pronoun + finite verb (1st person report opening) | "J'ai" (report-opening formula, "j'ai l'honneur de..."); "Je" (bare subject before a verb); "Il" (impersonal, "il est de mon devoir...") |
| BODY_CODE_A end (before "Je me flatte...") | weak -- sentence-final; "Je me flatte que" opens an unconnected new sentence, no conjunction bridges the two | open class (any sentence-final content word) | "arriver" (verb, situation-report closing); "chiffres" (noun, echoing the immediately following clear "les chiffres de la lettre"); "Georgie" (place name, echoing the letter's later closing-paragraph topic) |
| BODY_CODE_B start (after "si ce la est") | strong -- "si cela est" is a conditional protasis; French syntax requires an apodosis clause to follow immediately | subject pronoun (or adverb) opening the apodosis | "Il" (impersonal apodosis, "il faudra/il sera..."); "Je" (first-person continuation, "je vous prie..."); "Vous" (addressing Gérard directly, "vous pourrez...") |
| BODY_CODE_B end (before "Monsieur de le Marquis de Bretigni...") | weak -- paragraph break; the closing paragraph opens an unconnected new topic (Bretigny's arrival) | open class (any sentence-final content word) | "Méridionale" (adjective, echoing cribs.tsv's candidate "...croisière de la Caroline Méridionale"); "secourir" (verb, echoing the letter's own later clear "de les y secourir"); "arriver" (verb, situation-report closing) |

No candidate above is wired into a decode or treated as a reading; all are grade M, offered as leads for a
future crib-anchored pass, per the brief.

**U3: one-part dictionary-position test.** Built `tools/freq.py --onepart-dict LANG` (Tomokiyo C2,
LESSONS-TOMOKIYO.md, SYSTEM.md "Tools wanted" row removed in this commit): given a language key from
`tools/judge_plaintext.py`'s `LANG_CORPORA`, it builds cumulative initial-letter (a-z) bands from the corpus's
DISTINCT folded word TYPES (not raw token counts, which BER-KWIC found dominated by function words like "je"
at 3.8% of tokens in one sample -- see berthier-napoleon-1812 NOTES.md), then maps a file's most frequent
numeric tokens to the band their relative position in a stated range lands in. Offline test:
`tools/tests/test_freq_onepart.py` (17/17 checks pass, entirely synthetic, no dependency on the real fr18
corpus), plus the existing `tools/tests/test_freq.py` (22/22, unaffected).

`ciphers/destaing-gerard-1779/onepart_test.py` runs the actual hypothesis test with the pre-registered gate
(built before this run, not adjusted after seeing the result): fr18 (era-matched, this letter's own spec
already names it -- see specs/destaing-gerard-1779.json's judge block) initial-letter bands from 66,291
distinct word types; the top 12 groups' relative position in range 2-597 (this letter's own min/max code
value) checked against the initials of {de, la, le, les, que, et, à, en, il, ne, pour, vous} -- 9 distinct
folded initials of 26 (a, d, e, i, l, n, p, q, v), covering about 47.6% of the band width by construction
(not 9/26 = 34.6%, since French function-word initials are themselves common letters in the fr18 vocabulary):

```
TARGET consistent-band count: 6 of 12
CONTROL (1000 draws of 12 distinct values, seed=1): mean 5.76 (sd 1.73), 5-95pct [3,9]
GATE (target > control p95): False -- no support for one-part at this N
```

6 of 12 sits inside the control's 5th-95th percentile band and close to the control mean (5.76) -- **no
support for one-part at this N** (rule 3: a target inside the control band is a non-test on the hypothesis,
not a negative on the code). The control itself is a real test, not a non-discriminating shape (CLAUDE.md
rule 3's bCAS/AX-5799 paragraph): band width is far from 0 or 1 (47.6%) and the control distribution has
real spread (sd 1.73, mean tracks the analytic expectation 12 x 0.476 = 5.71 closely), so the null this
control represents genuinely could have separated from the target and did not. The same control also stands
for the two-part null (position carries no information) per the script's own docstring -- one control run
answers both framings, since a two-part code's null model (position uninformative) IS the uniform-random
draw already used.

**U4: next step.** Both grammar-boundary candidates (U2) and the one-part test (U3) are now on file as leads,
neither a reading nor a further negative on the code as a whole (the code itself is not shown to be two-part
either -- only that this specific 12-group/9-initial test found no signal at N=12). The fr18 word-type bands
are coarse at 26 letters for a 600-entry code; a next worker with budget could try (a) a Weber/Meng-derived
period FRENCH DICTIONARY's actual headword list (not a running-text corpus's word types, which BER-KWIC
already flagged as a rougher proxy -- Tomokiyo's own C2 note wants "a period dictionary from tools/data",
which does not exist yet) for a sharper band test, or (b) extend U2's boundary-grammar candidates into a
targeted archive search for the AAE Corr. pol. Etats-Unis Supt.1 decipherment (REQUEST.md's named route,
unchanged) rather than a further structural pass -- nothing cheaper than those two is left untried on this
letter without a key or sibling. Status stays `open`. No "solved", "new", "first", "unpublished".

Requests this session: none (script-only, no network; fr18/ciphertext.tsv/judge_plaintext.py all read from
disk).

## While waiting (27 Sept 2026, WAIT-PASS-A)

Waits on a copy of Clements Library Clinton Papers vol. 64:14/64:15, "waiting on you" since 25 Sept 2026
(clements.umich.edu 403s to curl, Wayback CDX also failed once).

- Build the period French dictionary headword list (tools/data has none yet) that U4 names as sharpening the one-part band test already coded in tools/freq.py --onepart-dict. M.
- Extend U2's boundary-grammar candidates into a targeted search for the AAE Corr. pol. Etats-Unis Supt.1 decipherment, a different named archive route that needs no Clinton Papers image. M.
- Retry the Wayback Machine CDX for clements.umich.edu/findingaids.lib.umich.edu once more after a pause (one prior attempt failed with a connection reset; the good-citizen rule permits a single retry). S.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/destaing/NOTES.md
- Their extent, in their words: skipped: 217 tokens of a 600-code, no key material; needs the archive
- Their date: 15 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Check-solved re-run (GF4-BATCH13, account-4, 3 Oct 2026)

Gate fix (no logged web/blog pass, no Premise check). Per `.claude/briefs/check-solved.md`; earlier sweeps (LANE CX2 and ZX2-EST,
25 Sept; Bourdeau 15 Sept) are above and not repeated.

1. **Sender/recipient edition.** Doniol, *Histoire de la participation...* vol. IV, be-api fts (identifier
   `histoiredelapart04doniuoft`; its djvu download answered HTTP 500 again, as on 25 Sept): "croisière de la Caroline" 1 hit and
   "Estaing écrivait" 1 hit (the p.774 paraphrase of this letter, already logged); "30 avril 1779" 0; "chiffre" 1 hit, three
   snippets: "Un pli chiffré ... En rade de la Martinique, le 6 janvier 1779" (a different, earlier packet), "ma lettre en chiffre
   à M. de Sartine", and an unrelated "chiffré" (a sum). Doniol paraphrases; he does not print the 30 April cipher passage.
2. **The interceptor's side (British).** Clinton forwarded the letter home in July 1779 (Tomokiyo). HMC *Report on American
   Manuscripts in the Royal Institution* vols 1-2 (1904; `reportonamerican12greauoft`, whole-volume grep: Estaing 36, Gérard 2,
   intercept 15, cypher/cipher 47 hits, read): no entry for a d'Estaing-to-Gérard letter of 30 April 1779; its intercepted-letter
   entries for 1779 are Clinton's "conjectures gathered from intercepted dispatches" (20 Oct 1779) and the like. HMC
   *Stopford-Sackville* vol. 2 (1910, Germain's papers, `reportonmanuscri02grea_0`, whole-volume grep: Estaing 18, Gérard 3,
   intercept 11, cypher 3, read): the only intercepted French cipher printed is Luzerne to Vergennes "[1780, June ?]" (p.172,
   "Extracts of intercepted letters (in cypher) from M. De la Luzerne"), not this letter.
3. **Continental Congress / Founders.** Google Books API (key + country=US) `"d'Estaing" Gérard "30 April 1779"`: the *Index, Papers
   of the Continental Congress* (1978) volumes appear, snippets on other Gérard letters, none this one (an intercepted letter to
   Gérard would not reach Congress's files); `Papers of the Continental Congress Estaing Gerard April 1779 intercepted`: 0.
   founders.archives.gov search answered HTTP 202 (bot challenge), not retried; Founders pages surfaced by WebSearch (below) are
   other d'Estaing letters. *B. F. Stevens' Facsimiles* (index vol., 1898): Google Books lists a full-view copy for `"Estaing"
   "Gérard" Stevens facsimiles 1779 Martinique` with no snippet; no archive.org copy found by advancedsearch -- not reached this
   pass (the series centres on 1773-1778 European archives; logged, not a clearance).
4. **Web, blogs, DECODE, solver repositories:** web and blog log below; DECODE, Bourdeau (class b, 2 Oct 2026, above) and
   Aymeloglu as before.

**Verdict: open** (stays). No print of the 30 April 1779 cipher passage deciphered was found in the sender's editions (Doniol
iv, Meng), the interceptor's printed papers (HMC American MSS i-ii, Stopford-Sackville ii) or the Congress index. New lead for
the route list (from WebSearch, not checked): d'Estaing's campaign registers in Archives nationales, Marine B4 168 hold his
letters to Gérard (a letter of 26 Oct 1779 is cited at B4 168 p.59 in *Storm over Savannah*'s notes) -- the sender's own
register copy of 30 April 1779 may be there in clear.

Requests: archive.org 9 (advancedsearch 4, djvu 3 incl. the HTTP 500, be-api fts 6 -- 1.6 s apart); googleapis.com 2;
founders.archives.gov 1 (202, not retried); ugapress.manifoldapp.org 1 (WebFetch); WebSearch 4 + 3 blog-site searches.

## Web and blog check (GF4-BATCH13, account-4, 3 Oct 2026)

- Plain web: `d'Estaing to Gérard 30 April 1779 Martinique intercepted letter Clinton` (Storm over Savannah notes, Founders
  letters of 1779, Wikipedia -- none on this letter; the Savannah notes cite AN Marine B4 168 p.59 for a 26 Oct 1779 letter to
  Gérard, read by WebFetch: no April 1779 letter, no cipher, no intercept); `Clinton Papers "64:14" OR "volume 64" d'Estaing
  cipher Clements Library` (Clements exhibit pages, Arnold cipher -- no item-level hit); `"Je me flatte" d'Estaing Gérard 1779
  lettre chiffrée Géorgie` (Founders d'Estaing letters, Washington to Gérard 12 Sept 1779 -- not this letter); `Admiral
  d'Estaing coded letter to Gerard 1779 deciphered solved` (no solve announcement; a "Napoleon letter cracked by AI" news item is
  a different target).
- Cipherbrain (site:scienceblogs.de, `d'Estaing Gérard 1779 code letter`): Soglia, 1783 letter, Biermann posts -- none on this
  letter; no comment thread found naming it.
- Cryptiana (site:cryptiana.blogspot.com / cryptiana.web.fc2.com, `d'Estaing Gerard 1779 code`): no search results; the on-disk
  `sources/cryptiana/web/unsolved.htm` lines 590-591 list it unsolved (quoted in the CX2 section above).
- Cipher Mysteries (site:ciphermysteries.com, `d'Estaing Gerard 1779 cipher`): La Buse / Nageon de l'Estang posts only -- not
  this letter.
- Result: no blog post or comment thread reads it.

## Premise check (GF4-BATCH13, account-4, 3 Oct 2026)

- (a) Folder's own files: NOTES.md, REQUEST.md, cribs.tsv, siblings.tsv and the spec mention no decipherment or clear copy of
  this letter; the only "decipherment" mentions are the AAE Corr. pol. Etats-Unis Supt.1 copy Bourdeau names (not online) and
  Doniol's p.774 paraphrase (opened, a paraphrase only) -- not found.
- (b) Other solvers' working files: Bourdeau's `targets/destaing/NOTES.md` (skipped, no key run on this text); Aymeloglu has no
  file -- not found.
- (c) Physical neighbours: Clinton Papers 64:15 (same-date clear letter to Holker, two copies, one in André's hand) and whatever
  André or Clinton's office may have written on or beside 64:14 -- unreachable (no image; clements.umich.edu 403s, REQUEST.md
  and SEND-QUEUE S1 stand).
- (d) Recipient's side: Gérard's despatches (Meng 1939, searched 25 Sept) and the British recipients' printed papers (HMC American
  MSS i-ii, Stopford-Sackville ii, this pass) -- not found; AAE Supt.1 and AN Marine B4 168 -- unreachable from the cloud, named.

## FT4-destaing-gerard-1779 (3 Oct 2026, account-4) -- planned test, written before the run

Cheapest step named in the folder: the "While waiting" line (Archives nationales catalogue lookup for Marine B4 168);
the brief's fallback (design prior, period-key registers, Doniol p.774 as crib) is script-only and is run beside it.

- `tools/design_prior.py --no-write ciphertext.tsv` (216 tokens, 104 distinct, 127 references at this N): multi-sign
  (homophonic/nomenclator/syllabary) d=0.25 vs null_p05 0.23 -> "not above null"; letter-for-letter plausible; mixed
  plausible; **code excluded** (d=1.29 vs envelope 0.91). Shuffled-input false-positive rate 0.080. Advisory ranking:
  homophonic 0.29, nomenclator 0.38, syllabary 0.66. Reading: the sign statistics do not favour a large two-part code;
  a syllabary/nomenclator of about 600 entries stays the working family (grade S, advisory).
- KEY-OFFICES.tsv / KEY-DESIGN.tsv: the only French key of the 1770s-80s on file is La Luzerne-Destouches, 16 and 31 Jan
  1781 (`ciphers/huntington-luzerne-destouches-1781/key.tsv`, 281 valued codes in 1-1199, syllabary, French crown's
  American-theatre naval/diplomatic correspondence; Luzerne succeeded Gérard as minister in 1779). No French navy or
  Affaires étrangères key of 1778-1780 is on file. Candidate in hand: the Luzerne 1781 key (different correspondents,
  two years later -- a long shot, but the same office family and the same design family as the prior).
- **Planned known-key test (pre-registered).** Apply Luzerne `key.tsv` to the 216 CODE tokens. Statistics: (i) coverage
  (tokens with a keyed value) -- reported only, since a value-shuffled control cannot move it (rule 3, bCAS/AX-5799);
  (ii) primary: fr18 4-gram mean log10 score (tools/judge_plaintext.py NgramModel) of the decoded text over the
  maximal runs of consecutive keyed tokens (runs of >=2 tokens), and (iii) fr18 word cover of the same string.
  Control: 1000 value-shuffled keys (the key's values permuted among its codes; coverage fixed, reading varies, so the
  control can differ from the target on (ii) and (iii)). Gate: target (ii) above the control's p99. Positive control
  (matched N and coverage): the same key on its own ciphertext (Luzerne mssDE 108A/68, `ciphertext.tsv`), a 216-token
  window with tokens masked at random down to the target's own coverage, scored the same way against its own 1000
  value-shuffled keys; the test is a test only if the positive control clears its own p99 in at least 4 of 5 windows.
  Crib: Doniol p.774's paraphrase ("fin de mai ... croisière de la Caroline Méridionale") is checked only if the gate
  passes (a key that fails the gate gives no reading to compare).

**Result (run 3 Oct 2026 04:4x UTC, `known_key_test.py`, seed 1, no network).** Grade S throughout; no token read.

| statistic | TARGET | CONTROL | gate |
|---|---|---|---|
| coverage (reported only; value-shuffle cannot move it) | 44/216 tokens (0.204), 25/104 distinct | -- | -- |
| distinct-code overlap vs uniform draws from 2-597 (1000 draws; key has 130 codes in that range) | 25 | mean 22.7, 5-95pct [17,29] | inside band |
| fr18 4-gram score of runs >=2 keyed tokens (37 letters: "duans / avecdu / etatcen / ordrespasetatordres") | -0.842 (word cover 0.946) | value-shuffled mean -1.003, p95 -0.732, p99 -0.658 | **FAIL** (below p99 and p95) |
| positive control: same key on its own ciphertext, 5 windows of 216 tokens masked to 44 keyed | 1/5 windows clear their own p99 (scores -0.656 to -1.074) | -- | **NON-TEST at this coverage** (needs 4/5) |

Reading: the 4-gram statistic cannot recognise even the right key at 20% coverage, so the FAIL is a non-test (rule 3),
not a negative. The overlap and coverage numbers carry the weight instead. The Luzerne key covers 75-85% of its own
letters' tokens (163-184 of 216 per window, in-sample), but only 20% of d'Estaing's, and that is the share chance
predicts for an unrelated code with numbers in 2-597. d'Estaing's three most frequent groups (401 x13, 382 x10, 152 x8;
31 tokens) are all absent from the key. No out-of-sample positive control exists for the overlap test (the only second
key on file, Tomokiyo's from the 8 Jan 1781 Beinecke letter, shares 56 codes with key.tsv but agrees on none of them,
so it is not a clean same-code sibling). Conclusion, grade S: no support for d'Estaing writing in the Luzerne 1781 code.
Its overlap with that code is at chance level. Because the overlap test has no positive control, this is logged as "no
support", not as a design-family negative. The Doniol p.774 crib was not run because the gate failed and no reading
exists to compare.

**Archives nationales lookup (the While-waiting step).** francearchives.gouv.fr answered both curl requests with a
JS/cookie redirect page. The siv.archives-nationales host answered 302. The browser tool could not run because
installing libnss3-tools for the proxy-CA fix hung in this container and was killed. Per the CLAUDE.md host note
(archivesnationales/francearchives do not load from the cloud), this step is now LOCAL-QUEUE row **L42** (Marine B4 168
inventory record, availability flag, and whether the register holds the 30 April 1779 letter in clear).

Requests: francearchives.gouv.fr 2 (curl, JS redirect), siv.archives-nationales.culture.gouv.fr 1 (302); browser 0;
DECODE 0 (not needed: KEY-OFFICES/KEY-DESIGN gave the one period candidate). Vision calls 0.

## DEST-COLLATE, 5 Oct 2026 22:33-22:4x UTC (account-4 standing session, session_01PpZtGZsbseHrXViC8rzExA)

Brief .claude/briefs/runs/2026-10-05-acct3-dest-collate.md. Material: private repo destaing-gerard-1779/Clinton_vol_64_fols_14-15.pdf,
pages 2 (copy A), 5 (copy B) and 7 (copy C), extracted with `pdftoppm -r 200` (1654x2447, 1654x2562, 1654x2621) to the
scratchpad; nothing image-like committed here. Line centres from the ink profile of a central strip; crops by
`tools/iiif_lines.py --image <page> --out <scratch>/{A,B,C} --region ... --centres ...` (22 / 33 / 21 crops, every text line,
the readers marking clear-text lines CLEAR). Two blind Sonnet passes per copy (6 calls), numbers only.

**Result: `collation.tsv` (pos, ciphertext.txt, A, B, C, agreed, note), 216 code groups. 215 agree in all three copies and
ciphertext.txt; 1 is unsettled; 0 corrections to ciphertext.txt.**
- Copy C: both passes = ciphertext.txt on all 216 groups, no disagreement.
- Copy A: both passes = ciphertext.txt on 214. At pos 59 and 130 both read 370/407, and the image gives 378/487: this hand's
  8 is an open loop that looks like a 0 with a stroke (compare "380" in the same line).
- Copy B: the passes lost one whole line (pos 96-107). This copy's lines slope up to the right, and the crop centres
  849/939 straddled it; read from the image as 235 450 507 72 367 492 346 382 401 41 410 400, identical to ciphertext.txt. Nine
  more pass disagreements (pos 23, 57, 71, 85, 114, 130, 139, 158, 198) were settled from the image in favour of
  ciphertext.txt: the same open 8, a 2 and a 5 at the page edge, one pass slip.
- **Unsettled, pos 7 (copy B):** ciphertext.txt, A and C read 152. In B the middle digit is closer to a 3 than to this
  copyist's 5, and both B passes read 132. Possibly a copyist variant in B; recorded as "152|132" and not settled by
  majority. ciphertext.txt keeps 152, which is A = C.

Transcription status: the ciphertext as transcribed (Bourdeau, via ciphertext.txt) is confirmed against all three
British copies; the measured per-group disagreement among the copies is 1/216. Copyist slips found: none certain (pos 7 in
B possible). The image-check gap is closed. No decoding was done; no novelty words (rule 10). Requests: 0 network (disk only).
Cost: see the lane ledger (6 Sonnet calls + 1 reconciliation unit).

## Remaining gaps (FT4-destaing-gerard-1779, 3 Oct 2026)
Read so far: 0 of 216 code tokens (no key, no reading); transcription confirmed on three British copies (collation.tsv, 215/216, DEST-COLLATE 5 Oct 2026)
- whole code text (216 tokens) - blocker: no-key-material; no French navy/AE key of 1778-80 on file, and the Luzerne 1781 key has chance-level overlap (FT4 above); the decipherment copy (AAE Corr. pol. Etats-Unis Supt.1) and the sender's register (AN Marine B4 168) are offline
- sender's register copy in clear - blocker: waiting-on LOCAL-QUEUE L42 (AN Marine B4 168 catalogue record); francearchives JS-redirects the cloud, FT4 above

## Escalation (3 Oct 2026)
- [x] siblings: Meng and Clements finding aid swept (ZX2-EST, 25 Sept); none found; Doniol iv numeral sweep blocked by IA HTTP 500
- [ ] clear-pages: sender's register copy may be in clear; planned step LOCAL-QUEUE L42 then a page read
- [x] known-keys: Marbois codes A-D (ZX2-EST) and Luzerne 1781 key (FT4) both at chance overlap
- [x] print: Doniol iv, Meng, HMC American MSS i-ii, Stopford-Sackville ii, Continental Congress index (GF4-BATCH13)
- [n/a] key-rebuild: 216 tokens of a ~600-entry code with no crib that reaches any code
- [x] image-check: Clements scan of Clinton 64:14 (three British copies) collated against ciphertext.txt, 215/216 agree, 1 unsettled (pos 7 in copy B), 0 corrections (DEST-COLLATE, 5 Oct 2026)
- [n/a] retry: no earlier step failed on transport other than the Doniol djvu download
Verdict: keep going: 0 internal gaps; cheapest next: page read of AN Marine B4 168 once LOCAL-QUEUE L42 answers, ~$2

## While waiting (GF4-BATCH13, account-4, 3 Oct 2026)

Waits on: the Clements image (REQUEST.md / SEND-QUEUE S1). The one action that depends on nobody:

- S: query the Archives nationales
salle des inventaires virtuelle (FranceArchives / siv.archives-nationales.culture.gouv.fr) for Marine B4 168 and its neighbours
(d'Estaing's 1779 campaign registers) to see whether the register itself, with a clear copy of the 30 April 1779 letter, is
digitised -- a catalogue lookup, no person needed (S; FranceArchives may not load from the cloud, in which case it becomes a
LOCAL-QUEUE row, logged with the probe line).

## While waiting (FT4-destaing-gerard-1779, 3 Oct 2026)

Waits on: LOCAL-QUEUE L42 (AN Marine B4 168 record) and the Clements image (REQUEST.md / SEND-QUEUE S1). The one action
that depends on nobody:

- S: build a period French dictionary headword list in tools/data (named by DES-PART U4), so the one-part band test in
  `tools/freq.py --onepart-dict` can run at headword resolution rather than fr18 word types. Script work, no person needed.
- 5 Oct 2026 (PR-LAND-67): LOCAL-QUEUE L42 answer (PR 67) bounced by tools/lq_answer_check.py (missing holding-catalogue rung: catalogue_ladders.tsv has no Archives nationales/FranceArchives row); row back to queued, answer not landed.

## Clements Library reply, 5 Oct 2026 16:19 UTC (logged 5 Oct 2026 17:02 UTC)

Reference staff answered the 5 Oct enquiry (ticket in the project mailbox): images of Clinton Papers vol. 64:14 and 64:15 are
**free** (up to 100 images per patron per year); they will submit the duplication request themselves once the owner registers in
Aeon (aeon.clements.umich.edu). Next: owner registers, then sends the reply draft placed in Gmail ("registered"). Images expected
after that; the cipher letter (64:14) is the target, 64:15 the language control.

## Clements images received (5 Oct 2026, 19:40 UTC)
Clements Library sent "Clinton vol 64 fols. 14-15.pdf" (8.9 MB) by Hightail share link to the project mailbox, free,
after Aeon registration. The cloud browser could not complete the Hightail download (3 attempts: the download button
did not respond headless; stopped per the good-citizen rule). Owner downloads it once and puts it in the private repo
(destaing-gerard-1779/). Next: transcription + key test from the received scan.

## Clements scan on hand (5 Oct 2026, 22:1x UTC, account-3 orchestrator eye check)
Owner downloaded the Hightail file; it is in the private repo, destaing-gerard-1779/Clinton_vol_64_fols_14-15.pdf
(12 pages, phone-camera scans ~1700-2400 x 2100-3100 px, about 210-270 ppi; numbers clearly legible).
- 64:14 is THREE British copies of the intercepted letter ("Copy of a Letter from Monsieur D'Estaing to Monsieur
  Gerard in Cypher, dated on board the Languedoc, Martinique 30th April 1779. Intercepted"), each marked "2.da"
  (secunda): copy A (pp.2-3, clear passages written in, signed "Signed Estaing"), copy B (p.5, same layout), copy C
  (p.7, cipher only; the clear passage "Je me flatte ... si cela est" left as a gap; "(Signé) Estaing"). Docket p.8
  "Intercepted Letter of D'Estaing".
- 64:15 is two copies ("1.ma"/"3.tia"?) of a CLEAR covering letter, d'Estaing to "Monsieur Holker, Agent et Consul de
  France", same date: Gerard is said to be returning to Europe for his health; d'Estaing hopes Gerard left Holker
  "le Chiffre qui sert a sa Correspondance avec moi", so Holker can read "les Lettres que je mets a l'adresse de
  Monsieur Gerard". Confirms the cipher is the Gerard-d'Estaing correspondence cipher and that Holker may hold it.
- No decipherment, interlinear value or British working is written on any of the 12 pages (the planned "did
  Clinton's office write a decipherment on or beside 64:14" check: answered no, eye check of all pages).
- ciphertext.txt (from Bourdeau's transcription) matches copy A's opening run by a spot check of the first 3 lines;
  a full three-witness comparison (A/B/C number by number) is the next step and replaces the image-check gap.
Next: three-witness collation of the ~230 code numbers (one worker with the private repo in scope, ~$4); then the
Holker lead (Holker papers, LoC) for the Gerard cipher key.
