# Blathwayt Papers Addenda — Madrid/Port Ste Marie diplomatic-intelligence run, 1725-1729 — Huntington mssBLA 176-195

Status: open

## Description

Huntington Library, William Blathwayt papers addenda (mssBLA 1-195; OAC finding aid
`oac.cdlib.org/findaid/ark:/13030/kt1199n4mx`), item-level entries BLA 176-195: secret diplomatic
correspondence and intelligence reports, 1720-1734 (after Blathwayt's own death in 1717 — these items ended up
in his family's papers, not his own correspondence), addressed to Alexander Hume-Campbell (2nd Earl of
Marchmont), Charles Whitworth, Charles Townshend and Thomas Pelham-Holles (Duke of Newcastle), from agents in
Berlin, Hamburg, Cambrai, Paris, Port Sainte Marie (Spain) and Madrid.

## Check-solved sweep, 24 September 2026

**Editions first.** No Calendar of State Papers series covers this material directly (CSP Domestic effectively
ends 1704; this is 1720s British diplomatic/intelligence correspondence, closer to State Papers Foreign Spain,
SP 94, which TNA Discovery would catalogue but this brief holds no TNA Discovery slot, so not queried). No
printed edition of this specific Blathwayt-addenda intelligence run was located by web search (queries:
`"Port Ste Marie" OR "Port Sainte Marie" 1729 spy intelligence Spain Newcastle Townshend cipher published` —
no relevant hit; general espionage-history results only). Not exhaustive — Coxe's *Memoirs of Sir Robert
Walpole* and the published Townshend/Newcastle diplomatic papers were not checked this pass, logged as
unchecked, not negative.

**The full item-level run, read from the OAC finding aid (`entire_text`, fetched via `tools/browser_fetch.js`
after a bare curl returned an empty 202/302 — Cloudflare-style gate), corrects and substantially extends the
scout's row.** The scout's row (QUEUE.md, 24 Sept 2026) named only BLA 186 (Madrid, 13 Sept 1728, "two lines in
cipher") and BLA 188 (a July 1729 enclosure "deciphered in French") among "8 further unopened items." Opening
all 20 items BLA 176-195 gives, verbatim from the finding aid's Scope and content field, every cipher-bearing
item in the run:

| Item | Date | Correspondence | Cipher note (verbatim) |
|---|---|---|---|
| BLA 179 | 1725 June 7 | Pareti to [-----], Paris | "In French with 3 lines in cipher, deciphered." |
| BLA 184 | [1727-1728] | Statement re M. Rottembourg | "In French, partly in cipher." (no "deciphered" noted) |
| BLA 185 | 1728 Jan. | To [-----] | "With separate sheet in cipher, deciphered in French." |
| **BLA 186** | **1728 Sep. 13** | **Letter of intelligence, Madrid** | **"In French, with two lines in cipher."** (no "deciphered" noted — this is the row's headline item) |
| BLA 187 | 1729 June 23 | To [-----], Port Ste Marie | "Enclosing a cipher, in French, endorsed..." (wording distinct from "deciphered in French" elsewhere in this finding aid — ambiguous, not scored either way) |
| BLA 188 | 1729 June 29-July 19 | Copies of 3 letters to Newcastle/Townshend | "...an unsigned, undated intelligence report in cipher [from Port Ste. Marie], deciphered in French." |
| BLA 189 | 1729 July 14 | To [-----], Port de Sainte Marie | "Enclosing: passage in cipher, deciphered in French." |
| BLA 190 | 1729 Aug. 4 | To [-----], Port Ste. Marie | "Enclosure: 2 pages in cipher, deciphered in French." |
| BLA 191 | 1729 Aug. 8 | To Newcastle, Cesnok | Enclosure (a) "undated, in cipher" (no "deciphered" noted); (b) "July 21, 1729, in French" |
| BLA 194 | [c. 1729] | To [-----] | "In cipher, deciphered in French." |

Six of the ten cipher-bearing items in this one run (BLA 179, 185, 188, 189, 190, 194) are explicitly noted by
the Huntington's own cataloguer as **already deciphered in French**, i.e. a contemporary clerk's decipherment
sits beside the ciphertext in the archive for most of this network's traffic — a stronger instance of
LESSONS.md's "the key was in the archive beside the letter" pattern than the scout's row recorded (which knew
of only one deciphered sibling, BLA 188). Only BLA 186 (two lines, Madrid, the row's own headline item), BLA
191(a) (an undated enclosure), and the ambiguous BLA 187 and partly-ciphered BLA 184 lack an explicit
"deciphered" note. This makes the "recovery" classification considerably less tentative than QUEUE.md's
caveat #3 states: the same small collection carries several 1725-1729 contemporary decipherments in the same
correspondence network (Port Ste Marie agent to Newcastle/Townshend, and separately Pareti to the Cambrai
ambassadors), from which a key or keys could plausibly be reconstructed and applied to BLA 186/187/191(a)/184.
This has not been attempted by anyone found in this sweep.

**Community lists.** Cryptiana's local snapshot and live web search for "Blathwayt" cipher return nothing;
Blathwayt does not appear anywhere in `sources/cryptiana/`.

**DECODE.** Login broken (ASKS.md row 1), not attempted. The cached DECODE catalogue in Aymeloglu's repo
(`unsolved-ciphers/catalogue/decode-catalog.csv`) has no "Blathwayt" row.

**Bourdeau (dbourdeau/cyphersolver).** Shallow clone. `grep -rliE "blathwayt"` — zero hits anywhere in the
repository (README, TARGETS.md, SOLVED_CATALOGUE.md, all target folders). Also checked the specific names from
the finding aid above (Dubourgay, Pareti, Rottembourg, "Port Ste") — the only "Rottembourg" hits are a
Napoleonic-era general in the unrelated `napoleon/` target's source texts (false positive, different person and
century).

**Aymeloglu (aaymeloglu/unsolved-ciphers).** Shallow clone. `grep -rliE "blathwayt"` — zero hits (README,
TARGETS.md, SHORTLIST.md, CATALOGUE.md, decode-catalog.csv).

## Verdict

**open.** No solution, key or documented cryptanalytic attempt on any BLA 176-195 item was found in the six
sources swept. The item-level finding aid (not previously read at this level of detail) shows most of the
cipher traffic in this small run already carries a contemporary French decipherment in the archive itself,
which strengthens the "recovery" framing for the handful of items that do not (principally BLA 186, the row's
headline "two lines in cipher" fragment, plus BLA 184/187/191(a)) — but nobody has yet fetched the deciphered
siblings' images and aligned them into a key. Report only: found in editions/community lists/DECODE/Bourdeau/
Aymeloglu — nothing; found in the archive's own finding aid — six contemporary decipherments in the same
collection. No novelty classification made here.

**Copy status.** Copy-free: "digitized in its entirety," Huntington Digital Library viewer pages load without a
login wall (confirmed by the scout for BLA 186/188; not individually re-confirmed for every item BLA 176-195
this pass — flagged for the next worker). No REQUEST.md needed for U2.

## Access notes

OAC finding aid needed `tools/browser_fetch.js` (bare curl returned empty 202 then 302 with 0 bytes — a
Cloudflare-style or JS-rendering gate on oac.cdlib.org, not documented in CLAUDE.md before now; worth adding if
another worker hits the same host). No additional Huntington CONTENTdm calls made this pass beyond what the
scout already logged (item-info calls, not the search endpoint); request count below.

## Searched, 24 September 2026 (for CLAUDE.md rule 1)

Cipher's name/shelfmark in a search engine (web); sender's/correspondent's printed diplomatic papers (not
located — no CSP series covers 1720s Anglo-Spanish intelligence traffic at this level, and no dedicated edition
of this Blathwayt-addenda run was found); community list comment threads (Cryptiana local + live search);
DECODE (cache only, login broken); both solver repositories (shallow clone, grep, both by collection name and
by the correspondent names read from the finding aid).

## Image capture and inventory, 24 September 2026 (LANE R worker R1)

**Access route.** Huntington CONTENTdm dmwebservices API, confirmed working parameter order (the earlier
"CISOSEARCHALL^TERM^all^and, suppressfulltextsearch=1" note in CLAUDE.md's Access playbook undercounts the path
segments): `dmQuery/ALIAS/SEARCHSTRING/FIELDS/SORT/MAXRECS/START/0/0/0/json` — i.e. the three positions before
`json` are `0/0/0` (suppress/docptr/suppressfields), not `.../1/0/json`. With that, `CISOSEARCHALL^cipher^all^and`
on `p15150coll7` reproduces the scout's 31 hits exactly. Exact item lookup: field `callid` (Call Number, dc
`identi`) holds the shelfmark verbatim as catalogued, e.g. `callid^mssBLA 186^all^and` — the `mss` prefix and the
exact spacing/parenthesis matter (`callid^BLA 186^all^and` with no prefix returns 0; `callid^BLA^begins^and`
silently reproduces the "naive form" bug, a fixed alphabetical listing regardless of term — confirms that
diagnosed bug is in the search *type* "begins", not fixed by the `0/0/0` correction). `dmGetItemInfo/ALIAS/POINTER/json`
on each item's own compound-object (`cpd`) pointer gives the full catalogue `notes` field verbatim, richer than
the OAC finding aid snippet already in this file (box numbers, `placre`, full endorsement text) — all ten BLA
records confirm the finding aid table above verbatim, no discrepancies. Page images: IIIF
`https://hdl.huntington.org/iiif/2/p15150coll7:POINTER/full/1200,/0/default.jpg` (native res up to 8708x11608
available at `full/max/...`; 1200px width used to stay under the 30 MB folder cap — ~200 KB/page, 74 pages,
~15 MB total). No login wall, confirmed on every page fetched.

**Fetched:** all pages of BLA 179, 184, 185, 186, 187, 188, 189, 190, 191, 194 (74 images total, including
cover/note/blank pages) to `images/`, with `images/manifest.json` (item, page, pointer, url, file, bytes, sha1,
date, catalogue_note verbatim) and `images/inventory.tsv` (item, page, content description, cipher type, approx
token count, notes) built from direct examination of every page.

**Major finding: this run is far more "recovery" than the scout's or the check-solved sweep's rows say, and the
key is not merely "somewhere in the collection" — it is written on the same page as most of the cipher, or on
a directly adjoining enclosure sheet, in most of these ten items.** Per-item, from direct examination (full
detail in `images/inventory.tsv`):

| Item | Cipher location | Decipherment on the page? | Approx. tokens |
|---|---|---|---|
| BLA 179 | p6, 4 lines inline in an otherwise clear letter | **Yes**, interlinear, same page | ~32 |
| BLA 184 | p1, 7 numeric code-words embedded in clear prose (a small nomenclator, not a running cipher) | No | 7 |
| BLA 185 | p5, a separate cipher sheet, ~11 lines | **Yes**, interlinear, same sheet | ~90 |
| BLA 186 | p1 (1 line) + p3 (1 line), inline in an otherwise clear letter | No | 24 |
| BLA 187 | p3, the enclosed cipher sheet | **Yes, but with visible gaps** (a genuine partial contemporary decipherment, some letters left as dashes) | ~85 |
| BLA 188 | p2(partial)-p5(top), the largest cipher table in the run | **Yes, partial** (same dash-gap style as 187) | ~400 |
| BLA 189 | p3, the enclosed cipher sheet | **Yes — and it is the letter's OWN plaintext**: p1-p2's clear French marks the same passages off in [square brackets], and p3 gives each bracketed cipher group followed by that exact bracketed clear phrase. This is a genuine known-plaintext/ciphertext pair, not merely a decipherer's rendering. | ~85 |
| BLA 190 | p5-p6 (2 pages), same bracket/known-plaintext pattern as 189; PLUS a third, separate cipher+decipherment passage on p7 (see anomaly below) | **Yes** (p5-p6, known-plaintext); p7 also carries its own interlinear decipherment | ~180 (p5-p6) + ~110 (p7) |
| BLA 191 | p5, enclosure (a), 12 lines | **No** — pure numeric cipher, no decipherment anywhere on the leaf. This is the one item in the run confirmed genuinely undeciphered in the archive. | ~130 |
| BLA 194 | p1-p2, the whole item | **Yes**, interlinear, same pages | ~93 |

Total: ~1046 cipher tokens across the run, of which only BLA 184 (7 tokens, a handful of code-words) and BLA 191
(~130 tokens) lack any decipherment on the page. Six of the ten items carry not just "a key exists in this
collection" (the finding-aid-level claim already in this file) but the actual reading, in the same hand, on the
same leaf or its immediate enclosure. BLA 189 and BLA 190 (p5-p6) go a step further: the "decipherment" is
demonstrably the letter's own drafted plaintext (bracketed in the clear copy), not a third party's rendering —
about as close to grade C (known plaintext) as this kind of material gets without an independent source.

**Anomaly, not yet resolved:** BLA 190 p7 is a fourth cipher+decipherment page in that item's image set, textually
self-contained (its own opening and a closing "Fait ... Mille sept cent vingt neuf" reading as "3 November 1729"),
which is *later* than the item's own catalogued date (4 Aug 1729) and not part of the catalogue's stated "2 pages
in cipher" (that is p5-p6). It may be a misfiled leaf from a different, later letter in the same mssBLA run bound
into this compound object by the library, or a draft/copy kept with this letter. Flagged for the next worker
before treating its decipherment as this item's own.

**Passes.** Per brief, two blind Sonnet subagents were set to transcribe every cipher passage in U2 (numeric
tokens only, from the 17 cipher-bearing page images, ignoring any interlinear French) to `passA.tsv`/`passB.tsv`,
plus a third single (non-blind) pass to transcribe the contemporary French decipherment itself into
`decipherment_<item>.txt` files, one line per cipher line, as written (gaps kept as the clerk left them). Run
`tools/reconcile_passes.py passA.tsv passB.tsv` (wide format) to get `disagreements.tsv` before any reading is
attempted — disagreements are for a reconciler to settle from the image, not settled here. No decoding, no key,
no novelty wording in this pass.

**Not done this pass:** mssBLA 184's 7 code-numbers and 186's 2 inline lines were not attacked (no decipherment
sibling on the page for either); BLA 191's ~130-token undeciphered enclosure likewise untouched cryptanalytically
— all left for a solver session with a matched control (rule 3), after the passes above land.

## R7 progress, 24 Sep 2026 07:11 UTC (LANE R worker R7, stopped over cap by the orchestrator)

**Done.**
- Step 1, provisional: one code across the run. The same groups have the same values in BLA 179 (Paris 1725), 185, 186 (Madrid 1728), 189 and 191 (Port Ste Marie 1729): 659 = l', 78 = ambassadeur, 737 = Monsieur, 278 = de, 926 = que, 661 = le, 580 = je, 1154 = vous, 18 = a, 756 = ne. Groups 1240/1243/1250/1324 act as nulls or dashes (189 p3; used inline in 184 p1). This is by eye from the images; it is not yet backed by a count of conflicting pairs.
- BLA 186 p1 cipher line begins 659.78 (l'ambassadeur...) under that code. This is an image-only observation, not graded.
- **BLA 188 p2 has no cipher of its own.** Its right-hand "column" is the edge of p3 caught in the gutter of the photograph: 18 rows of two groups that repeat the start of p3 L01-L08 (pass A confirms, e.g. 1212 298 / 591 1102 / 941 250 ...). Drop BLA188_p2 lines from any ciphertext. The inventory's ~60 tokens on p2 are double-counted.
- `passA.tsv`: blind Sonnet pass A over all 18 cipher pages (1565 groups, with the interlinear gloss per group). Brief: `pass_brief.md`. Pass A reports BLA191_p5 L05 pos 10 as "1899", out of range, to check on the image.
- `passB_partial.tsv`: blind pass B, **stopped part-way** (793 groups). It covers 186 p1/p3, 187 p3, 188 p2-p3, 190 p6-p7, 191 p5 and 194 p1-p2. It does **not** cover 179 p6, 184 p1, 185 p5, 188 p4-p6, 189 p3 or 190 p5.
- `recon_partial/`: `tools/reconcile_passes.py passA.tsv passB_partial.tsv` output. On the lines both passes cover, 645 of 795 aligned columns agree (81%). Partial and not settled on the image.
- `sources.tsv`: print-check sources (Coxe Walpole 1798 vols 1-3, Coxe Horatio Walpole 1802, Coxe Kings of Spain vols 2-3, HMC Townshend 1887, Armstrong 1892, OpenAlex, CrossRef). Not yet run: no phrases yet.

**Left.** Finish pass B for the six missing pages. Settle recon disagreements on the image, excluding BLA188_p2. Write ciphertext.tsv. Build key.tsv from the glosses (H) and the 189/190 bracket pairs (C), with a conflict count per item to confirm or refute one system. Read 186, 184 and 191 p5 through decode.json + tools/decode_key.py with a matched synthetic control. Write phrases.txt and run `tools/print_check.py --only ia,ia-global,htrc,openalex,crossref` (not gbooks). Suggestion: a fresh worker can start from passA.tsv and must not repeat pass A.

## R11: pass B finished, 24 Sept 2026 07:46 UTC (LANE R worker R11, session_01HQ6j9nsqSZ7JCHyNaSebLu)

**Done.**
- One blind Sonnet subagent (not shown pass A) finished the six pages R7 left uncovered: 179 p6, 184 p1, 185
  p5, 188 p4-p6, 189 p3, 190 p5 (774 groups, 752 H / 22 M-L). Output `passB_missing.tsv`.
- Band crops for these 8 page images were regenerated in this session's scratchpad (R7's own scratchpad no
  longer exists); same convention as `pass_brief.md` (3 overlapping 2x horizontal bands per page).
- `BLA190_p5`: the subagent split the page's one long paragraph block into `L14a`-`L14e` rather than forcing
  `L14`-`L18`, since it wasn't shown pass A's line numbering. Per-line group counts matched pass A's `L14`-`L20`
  exactly (13/12/12/14/1/5/4 both ways), so relabelled `L14a→L14, L14b→L15, L14c→L16, L14d→L17, L14e→L18`, old
  `L15→L19`, old `L16→L20` before merging — a naming fix, not a content change; every group's number/conf/gloss
  is untouched.
- `BLA188_p4`/`p5`: the subagent independently flagged that p4's right-hand narrow column duplicates p5's
  opening lines (bleed-through near the gutter) and transcribed that content only under p5. This was not asked
  for and not cross-checked against pass A's judgement call on the same split — but the resulting per-line
  group counts for both p4 (18 lines) and p5 (18 lines) match pass A's counts for those pages exactly, which is
  reassuring (both blind passes independently drew the p4/p5 boundary in the same place) but not a substitute
  for eye-checking the boundary on the image, which nobody has done. Flagged for the reconciler, distinct from
  the confirmed BLA188_p2/p3 gutter duplicate below.
- Dropped `BLA188_p2` (36 rows) from `passA.tsv` in place (R7's finding: p2's "column" is the edge of p3
  caught in the gutter of the photograph, not its own cipher — see "Major finding" above). `passB_missing.tsv`
  was never asked to cover p2, so `passB.tsv` (below) needed no p2 rows dropped from the new material, only
  from the carried-over `passB_partial.tsv` rows.
- `passB.tsv` = `passB_partial.tsv` (minus its 36 `BLA188_p2` rows) + `passB_missing.tsv` (renamed), 1531
  groups across all 17 cipher-bearing pages (`passB_partial.tsv` kept as-is, unmodified, per brief).
- `tools/reconcile_passes.py passA.tsv passB.tsv --out-dir recon`: **1344/1543 aligned columns agree, 87.1%**
  (vs the partial-pass figure of 81% in `recon_partial/`, now superseded). 200 disagreement rows in
  `recon/disagreements.tsv`, `recon/ciphertext_draft.tsv` (332 of 1543 signs M), `recon/agreement.tsv`. Not
  settled — that is the next worker's job, from the image, excluding anything already resolved as the
  BLA188_p2/p3 gutter duplicate.

**Left.** Settle `recon/disagreements.tsv` on the image (200 rows), including eye-checking the BLA188_p4/p5
boundary noted above before trusting it. Write `ciphertext.tsv`. Everything else in R7's "Left" section
(key.tsv, decode.json + decode_key.py reading, matched control, phrases.txt + print_check.py) is still open.

Requests: 0 network (images already on disk; band crops regenerated locally, no fetch).

## R17: key and reading, 24 Sept 2026 08:30 UTC (LANE R worker R17, Opus, session_011yvU8fdYtfhhpuMK1C9nvJ)

**Settling (`settle.py`, `--check` 0).** Pass A split BLA188 p3 line 9 in two, so its L10-L19 sat one line ahead of
pass B; `settle.py` joins A L09+L10 and renumbers before aligning (this accounted for most of the 109 BLA188 p3 rows in
`recon/disagreements.tsv`). Then rule 'key-consistent' (the gloss over the disputed column is attested for one group
elsewhere in the run and not for the other): 33 disagreements and 32 agree-flagged columns settled to H without an
image. Image, 10 crops from the 1200 px disk copies (no fetch): every M column in BLA186 p1/p3 and BLA191 p5, 57 columns
(`settle_image.tsv`, by eye). Result `ciphertext.tsv`: 1532 columns, H 1393, M 139 (68 disagreements left undecided
with the alternative kept, 57 agree-flagged, 3 gaps, 5 null-like groups without gloss). `settle_log.tsv` shows each
decision with the gloss evidence.

**Finding for anyone re-reading these pages: the hand of BLA186 and BLA191 writes 7 as '>' or ')'.** Both blind passes
agreed on a wrong reading at five places the image settles: 186 p3 pos 1 is 737 (monsieur), not 733; 191 p5 L02 pos 1
137 not 135; L05 pos 8 278 (de) not 258; L07 pos 9 probably 937 not 933 (M); L01 pos 9 probably 941 not 947 (M). The
glossed pages (other hands) were not re-checked for this; 'agree' there means two passes agreed, nothing more.

**Key (`build_key.py`, `--check` 0).** `key.tsv`: 395 groups, all grade C (contemporary gloss on the leaf, or on BLA189
p3 / BLA190 p5-p6 the letter's own bracketed clear phrase), value = majority gloss over H columns; 90 groups carry a
second gloss (mostly syllable fragments of the same word, e.g. 385 et/es), 29 are ties 'a|b' and decode as M.
`key_conflicts.tsv`, glossed columns that differ from the key value, per item: BLA179 2/24, 185 2/103, 187 11/72,
188 57/405, 189 7/151, 190 34/347, 194 22/103.

**One system for 1725-29: yes, on this evidence.** Leave-one-item-out (`key_items.tsv`): the share of an item's
glossed columns whose gloss equals the value the other items give the same group is BLA179 (Paris, 1725) 16/18 =
0.89, 185 0.91, 187 0.70, 188 0.73, 189 0.86, 190 0.77, 194 0.68. Under two unrelated systems the expected share
would be near zero; the shortfall from 1.0 is gloss fragments and pass noise, not a second table. BLA186 (Madrid 1728)
and BLA191 (1729) carry no gloss and are tested only by whether the key reads them as French, which it does.

**Reading (`decode.json`, `tools/decode_key.py . --check` 0), `reading.txt` / `reading_tokens.tsv`.** 172 tokens: C 129,
S 0, M 22, U 21, H 0.

| Item | tokens | C | M | U |
|---|---|---|---|---|
| BLA184 p1 | 7 | 3 | 3 | 1 |
| BLA186 p1+p3 | 24 | 20 | 0 | 4 |
| BLA191 p5 | 141 | 106 | 19 | 16 |

French rendering (key values joined into words; [..] = unkeyed group; nothing filled from context; no S, since no
context fill was attempted and so no control was needed):

- **BLA186 p1** (after "...s'il se trouve sur leurs estats.", Ripperda's escape): *l'ambassadeur [73] a été fort [470]
  [778] [190]te affaire.* ("[190]te affaire" is likely "cette affaire", an inference, not graded.)
- **BLA186 p3** (after "...pour empescher les gallions de passer en Europe."): *Monsieur de Patigno m'en a [849 =
  'monsieur', one gloss in BLA188, doubtful] ce soir.* Patiño, by the key's syllables pa-ti-g-no.
- **BLA191 p5** (enclosure (a), 1729): *L'[805] que je vous ai, milord, est bien grande pour votre lettre du [6] [j'y|
  parle] ai ... quand ce [1210] de [689]ars à la première ad[..]ri... hier quand vous me [460]ri(?) sçavoi[r], comme je
  [285]is agit après le départ du [214], car Monsieur Keene m'a[i]me, mais il n'a aucun ordre des [1019][711]s pour
  moi, quoyque dans l'affaire passée je lui ai fait [1118] bon [1052]ce, sans qu'il m'ait jamais dit ce que je pouvois
  fournir pour le mieux à l'accommodement, et par [585=ig]norance [1152] intentions, et je serai inutile dans
  l'ignorance. Mandez-moi donc quelque ordre pour ma [222].* The writer asks his correspondent ("milord") for
  instructions, complaining that Keene (the British minister at Madrid) gives him no orders. 585 = "ig" is inferred
  from "[585]no ra n ce" twice (I, not in the key).
- **BLA184 p1**: 1150 1259 / 1240 1243 / 1243 1240 / 1250 sit in clear prose as names or place-holders ("et Monsieur
  1240 de 1243 la Paz", "1243.1240. Si Monsieur Rotembourg..."); the glosses of this range elsewhere (1250 hier|c'est,
  1150 vo) do not fit, and R7 saw 1240/1243/1250 used as nulls in 189. Not read: this range is probably a names section
  the glossed items never use.

**What is left.** 21 unkeyed groups (805, 6, 1210, 689, 460, 285, 214, 1019, 711, 1118, 1052, 836, 1152, 222, 73, 470,
778, 190, 1259, 1240, 1243); a context-fill pass with a matched control (blank the same share of a glossed item, e.g.
BLA185, and score) could move some to S; 849 needs its BLA188 gloss re-checked on the image. BLA190 p7 date anomaly
(R1) untouched. The 68 undecided columns are all in glossed items, not in the targets.

**Search log (prior print of these letters), 24 Sept 2026.** `tools/print_check.py . --only ia,ia-global,openalex,crossref`
with `phrases.txt` (5 decoded joins, 2 clear-text phrases from BLA186) against `sources.tsv` (Coxe, Walpole 1798
vols 1-3; Coxe, Horatio Walpole 1802; Coxe, Kings of Spain vols 2-3; HMC Townshend 1887; Armstrong, Elisabeth Farnese
1892): 63 phrase x source searches, no hits, including IA full text across all items (ia-global). OpenAlex answered
HTTP 429 on the first call and was not retried (8 rows 'not searched'). CrossRef keyword searches returned only
unrelated records. Not searched: Google Books (LANE V's host), HathiTrust, TNA SP 94 calendars, the BL Newcastle papers.
Requests: archive.org 8, be-api.us.archive.org 7, api.openalex.org 1 (429), api.crossref.org 2. No novelty classified.
