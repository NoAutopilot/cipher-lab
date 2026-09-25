# LANE YX triage: every open/partial target the lane could still finish, 25 September 2026

Disk-only pass (no network fetching). Candidates: `ciphers/*/NOTES.md` whose first-lines status word is `open`
or `partial` (rule 5; a few older folders write "Status: Open." instead of the bare word — scored, matched
case-insensitively, not read by hand). 213 folders scanned, 128 open/partial. Dropped 17 never-touch
(fr2933/3151/3985-3990/5761, roell-vandedem-1809, the rest of the firm N4 nominations — fr3993-villeroy-1595,
fr3625-lauriere-1593, fr3621-dinteville-1592, hellen-frederick-1752, vanspaen-vandergoes-1808 — colbert26,
every na-*, roell/schonenberg/suriname/janssens, and the lane's own three); confirmed against ROOM.md's last
6h that none of the 17 has a stray live claim beyond the ones already on the never-touch list. Dropped 12 with
an AUDIT.md (already past a verifier). **99 candidates remain.**

Rule 10: report only what was found and where it was not found; no novelty wording, no "first"/"unpublished".
Everything below quotes or paraphrases what the target's own NOTES.md already says; this pass ran no new
searches and touched no files but this one and ROOM.md.

Intake gate (per `.claude/briefs/check-solved.md`): PASS needs a sentence naming the standard edition and the
pages, or a full-text search that names a control phrase found. Of the 99, only a handful carry that exact
shape (flagged PASS below); most are pre-25-Sept folders whose "Status: Open" line has no formal six-source
check-solved verdict attached at all — those are FAIL (missing verdict), not because anything is wrong with
them, but because no worker has run the intake gate on them yet.

## Top five

| target | route | next test | gate |
|---|---|---|---|
| clair349-este-guise-1556 | recovery (key public, leaf identified) | fetch Tomokiyo's fr.20974 key images (f.57, f.69) + full-res Clair 349 f.3 (canvas f9), transcribe key.tsv, apply | FAIL (no formal check-solved; edition check partial, see below) |
| wellington-maitland-1812 | recovery (dictionary-code book test) | test London Entick 1801-1811 editions + Scott's (Edinburgh) abridgement against the known word→page/position constraints in `codebook.tsv`, via IA/Google Books/HathiTrust | PASS ("Fetched and grepped the full OCR text of both dispatchesoffie09welluoft... and vol9dispatchesof00well... pp. 388-389 and pp. 392-393 respectively") |
| willem-van-hessen-1567 | recovery/cryptanalysis (crib, same-office key) | fetch WVO briefnr 174 and 1069 detail pages, check PDF availability (OX triage 25 Sept, score 8/10, unchanged) | FAIL (no formal check-solved on this exact letter logged) |
| decode-2754-bnf-baluze156-1636 | recovery (untried sibling key) | fetch Lasry's second Sabran-circle key (Baluze 156 f.40, "?Odoardo Farnese", GL.htm) and test it on f.157r's tokens — the first Sabran key (fr.4134/Baluze155 f.79) already tried, negative with a control | PASS (six-source sweep logged, quoted below) |
| courten-diary | recovery, blocked only on a copy order (key already on the leaf, f.66) | none free — BL Add MS 4956 has no IIIF (BL viewer dead since 2023); REQUEST.md already drafted for BL Imaging Services | PASS (searcharchives.bl.uk catalogue read verbatim, web/Cipherbrain/solver-repos/DECODE all checked negative) |

All five share the OX triage's winning shape: a key or decipherment already identified in the source material
itself, with either a genuinely cheap copy-free test left (clair349, wellington-maitland, willem-van-hessen,
decode-2754) or a clean stop at a copy order already logged (courten-diary).

---

## A. Recovery: key, decipherment or dictionary edition already named in the sources

**clair349-este-guise-1556** (partial). Tomokiyo has already published the key (fr.20974 no.15, 2020/2022)
*and* identified and photographed the exact matching ciphertext letter down to the folio. Nothing published
plaintext/decipherment of this specific letter, but per rule 10/M9 this is not "open": a solver only needs to
fetch the key images (`guise/BnFfr20974f57.png`, `f69.png`) and Clair 349 f.3 (canvas f9), transcribe key.tsv,
and apply it — no fresh cryptanalysis. Edition check (Ribier 1666, one hit p.667, generic, not confirmed to
date) not fully closed. On disk: 1 image. **Score 9/10** — cheapest, highest-confidence item in the whole
pool; cap $3-4, no login, no copy order.

**wellington-maitland-1812** (partial). Dictionary code + strip cipher; Hayes/Lasry published the strip key,
Tomokiyo added two more and resolved one run ("Vila Castin"). What's outstanding: the *dictionary edition*
itself (57+ IA candidates already ruled out) and the strip null/permutation rule. Formal check-solved sweep on
file, quoting Gurwood vol.9 pp.388-389/392-393 read on two independent IA copies. Next test named directly in
NOTES.md ("Next step" section): test the London Entick 1801-1811 editions and Scott's Edinburgh abridgement,
copy-free (IA/Google Books/HathiTrust). **Score 8/10.**

**decode-2754-bnf-baluze156-1636** (open). Two Sabran-circle nomenclator/letter-alphabet trials already run
with matched controls, both negative (numeral trial: 0/31 real hits vs. control mean 19.1%; letter trial:
5.649 bits/char vs. a positive control at 3.066, inside the shuffle range). What's still untried: Lasry's
*second* Sabran-circle key (Baluze 156 f.40 itself, the Farnese-to-Sabran break, same volume) — never fetched.
A named crib also survives: the repeat `7 4 t o` sits where plaintext elsewhere names "Levanto"/"ledit",
suggesting a -ANTO name ending. Six-source sweep logged and quoted in file. On disk: 3 images, 2 key files
(for the *wrong* sibling), 87.6% two-pass transcription agreement. **Score 6/10.**

**courten-diary** (open). BL Add MS 4956, key appended by Sir Frederic Madden on the diary's own last leaf
(f.66) — a same-manuscript key, the cheapest recovery shape there is, if it can be seen. BL's viewer has been
dead since 2023 (per CLAUDE.md's host table) and no alternate image route was found (Discovery API gives
metadata only). REQUEST.md already drafted (BL Imaging Services quote). Six sources checked, no hit; a
tangential finding (Courten also used a short cipher on Sloane Herbarium specimen labels, already decoded by
outside scholarship — a different corpus, flagged only for caution). **Score 5/10** (recovery-shaped, but the
one remaining step is a paid copy order, not a worker task).

**bl-charles-digby, bl-james-1669, bl-sacchetti-nunzio-1623, bl-gualterio-1700** (all open; on disk: 0 images
each). A cluster of BL-only items, each with one or two concrete, copy-free next steps named in its own
NOTES.md and none yet a REQUEST.md:
- *bl-charles-digby*: IF the shelfmark resolves to Add MS 6912, this reclassifies found-solved (Wheatstone's
  1862 key, already in print); if not, Wheatstone's key is still the first thing to try, since both are the
  same king's cipher hand. Next test: confirm the shelfmark via the BL catalogue API. **Score 5/10.**
- *bl-james-1669*: full-text search Clarke's *Life of James the Second* (IA `lifeofjamessecon01inne`) for
  "cipher"/"cypher" and 1669, check CSP Domestic 1669 for a matching calendar entry. If both negative, ff.1-8
  (the letters plus their own partial name-key) is "the cheapest solve in the volume" per the QUEUE row's own
  note — a narrow reading-room ask, not the whole volume. **Score 5/10.**
- *bl-sacchetti-nunzio-1623*: Google Books search-within for "Sacchetti"+"nunziatura"+"Spagna", and Pastor's
  *History of the Popes* vol.13 (English ed.) around p.273 for a quoted cipher passage; then ISIME's own
  published-volumes list. **Score 4/10** (six registers is a large ask if this fails; not yet drafted).
- *bl-gualterio-1700*: 14 volumes, no image sampled yet; next step is checking whether any volume shares a
  correspondent (Torcy, Acquaviva, Ottoboni, Medinaceli/D'Estrées network) with an already-published Tomokiyo
  key, and whether the same acquisition's known interlinear-decipherment habit (Add MS 20244) extends to the
  volume that would be requested. **Score 3/10** (large, unfocused; a copy order either way).

**mornington-1798** (partial). D623/23 found-solved elsewhere; D623/10, /11 already known to the cataloguer;
nine more items now stage-2 verified-unsolved after a six-edition print check. REQUEST.md already drafted for
D623/41 (the key) plus the shortest unprinted despatch as a size/legibility test. **One real risk flagged**:
Edward Ingram's 1970 *Two Views of British India* prints exactly this private correspondence and is not on IA
— check it (IA loan / HathiTrust search-only / library copy) before paying for imaging. **Score 5/10**
(genuine cheap test — the Ingram check — still open ahead of the copy order).

**pro3055-clinton-1779** (partial). PRO 30/55/24/76 matches a known British Museum copy (needs locating, not
cryptanalysis). Seven more items have HMC calendar paraphrases in print since 1904-09 but nobody has opened
the actual HMC Report volume pages (vol.3 entries 3689-3868, vol.4 entries 6004-6048) to check whether a
decipherment, not just a paraphrase, sits beside the summary. Both steps are archive.org reads, copy-free.
**Score 6/10.**

**decode-9970-simancas-1527** (open). Narrowed a 1214-page catalogue volume to two candidate pages (the 26 Oct
1527 del Burgo-to-Gattinara letter) via HTRC Extracted Features word-count matching — genuine progress, not a
block, and reachable copy-free (`tools/htrc_ef_headwords.py`, no HathiTrust login needed for the EF API).
**Score 5/10.**

**clairambault296-paget-1713** (open; see also the never-touch clairambault1225-paget-1714, a different
folio/year of the same correspondent). No image of either Paget letter is on disk yet; 36 Gallica canvas
probes this pass, all either negative or transient connection resets, none pinned. **Score 3/10** (cheap,
copy-free, but unlocated after real effort already spent).

**fr16092-maisse-1582** (open, no formal six-source check-solved run — **gate FAIL**). The key itself is
already imaged (canvas 12, "La Clef du chiffre de Mr. de Maisse", a numeral nomenclator 12-65 + letter figures
40-61): a genuine recovery shape. But no actual ciphertext passage has been located yet in this 932-canvas,
all-`NP`-labelled volume — a 4-leaf sample (canvases 12/20/30/70) found only clear French. The neighbouring
volume (fr.16093) uses an offset of ≈+48/+49 between canvas and folio; the same offset here would put the key's
own stated f.5-f.9 near canvas 12-17. One real risk flagged and unresolved: whether Boucher's *Lettres de
Henri III* tome V/VI (2000/2006) already prints any of these letters in clear from a lost decipherment.
**Score 5/10** — send a check-solved worker first (formal sweep + the Boucher check), then a canvas sweep at
the estimated offset for the key's numeral range.

**espagnol142-mercy-1648** (open, no formal check-solved — **gate FAIL**). A "chiffre" item (6 June 1648,
abbé de Mercy to Barneton per the finding aid) not yet pinned to a canvas in a run of 1640s French diplomatic
instructions (canvases 20-30 confirmed same genre, still clear French). Next test: ~15-20 more canvas probes
in the 30-70 range for the date "1648" or the names "Mercy"/"Barneton". **Score 4/10.**

## B. Cryptanalysis: design known or partly known, control status varies

**fr4687-paleologue-nevers** (open, no formal check-solved — **gate FAIL**). Three Italian letters (1562-64,
Marguerite Paléologue to her son, later Duke of Nevers) confirmed to carry real ciphertext (canvas 8/f.6, dense
two-digit numeral groups, 15-25 per line across 6+ lines) but not yet transcribed. No key candidate found after
checking Tomokiyo's fr.3995 catalogue by three independent structural reasons (wrong decade, wrong "Duchesse").
Class-gate search (Ferrari 1999 paywalled/unread, Boltanski 2006 negative by phrase search, BnF's own fuller
catalogue notice unreachable) found no prior print. **Score 5/10** — transcribe f.6, then a design-matched
Italian-nomenclator control before any solve attempt; a formal check-solved sweep is still owed first.

**harley-287-1587** (partial). Not an unattempted target: Bourdeau's project already has near-complete public
readings for most of this DECODE range (needham1587 ~98%, harley287/R8477+R8482-87 read in sense throughout,
cobham1588 about a third). Any further work here is finishing/verifying Bourdeau's existing key (MIT/CC BY
4.0 — cite, don't duplicate), not fresh cryptanalysis. **Score 3/10.**

**clair1161-avis-flandre-1688, clair571-estrades-1645, decode-1411-hhsta-vienna-1600** (all open). Each has a
named, specific next step (respectively: a successful native-res image already fetched, awaiting a
transcription pass; pin the exact volume among Clair 571-582, then read Clair 574's existing Brasset key
against it before fresh solving — flagged low-priority, duplicate-risk by its own nominator; transcribe, since
inline cleartext already confirms the passages are genuine diplomatic cipher not a partial break). **Score
4/10 each** — real but modest, none copy-free-blocked.

**Already negative or substantially resolved elsewhere — low priority, listed for completeness:**

| target | status | what's on file |
|---|---|---|
| la-garde-1577 | open | control-backed negative x2 (homophonic + periodic Vigenère/Beaufort, both clean on controls); GSME/LMSAC print check negative. Score 3/10 (OX triage, unchanged). |
| birago-nevers-1571 | open | closed-negative by Bourdeau after glyph-level re-transcription; variable-length designs excluded against controls. Needs a sibling or crib. Score 2/10. |
| moray-wood-1568 | open | **substantially read by Aymeloglu already** (119/134 glyphs, key-shuffle z=17) — this repo's own transcription conflates two glyphs; flag for the orchestrator that the status word may deserve `found-solved`/`partial` from Aymeloglu's key, not `open`. Score n/a, not a fresh target. |
| ormond-arran-1678 | open | ~20 code groups, below unicity distance; needs another letter in the same cipher. Score 2/10. |
| sp53-16-78, sp53-16-79, sp53-22-f52 | open (x3) | all three closed-negative by both Bourdeau and Aymeloglu (no language basin in 5 languages at matched control lengths; SP53/22's own 61 key images tried). Needs page images, not another cryptanalysis pass. Score 1/10 each. |
| fr3022-garbino-1528, fr2988-ranzo-1520s | open (x2) | LANE R4 (18:22 24 Sept): "no design with a working control at their lengths" (Garbino, 1,315 groups); fr2988 folded into the same corpus, not independent. One untried lead: Tomokiyo's partial Ranzo key against fr2988's own ciphertext. Score 2/10. |
| decode-4450-bnf-fr20506-1525 | open | a partial second-witness copy of the same Ranzo/Garbino corpus (fr.20506 f.136, ends mid-letter); attribution rests entirely on Bourdeau's unpublished-license repo. Score 2/10. |
| thurloe-barriere-1654 | open | LANE TX: negative with matched control (gloss-key coverage 29.3% vs. control 33.4%, 10 seeds); spec on file; next named test is a permutation z-test on gloss positions. Score 3/10. |
| catokwacopa-1875 | partial | mechanism agreed by every source, several partial readings proposed since 2018, but the omission rule may structurally prevent a unique solve (Bourdeau's own audit); no matched-control test has actually been run. Score 2/10 (the control test itself would be the one open move). |

## C. Heinsius circle (NA 3.01.19) — reused from `.claude/briefs/runs/2026-09-25-lane-ox-triage.md`, unchanged

All five sit on one undigitised key subsection (invnrs 2315-2317); none has a cheap web test left.

| target | route | score | next |
|---|---|---|---|
| heinsius-hermitage-1704 | recovery, candidate key 2317, archive-only | 5 | consolidate REQUEST.md: H.A. 946+1034+2317 |
| borssele-heinsius-1714 | recovery, decipherment reported on the same leaf, archive-only | 5 | photograph H.A. 1836 |
| heinsius-dopff-1702 | cryptanalysis, below unicity, no key fit | 3 | none cheap |
| rumpf-vandebie-heinsius-1716-19 | cryptanalysis, one instance already negative | 3 | archive copies of 309/446/455 |
| heinsius-vanhaersolte-1703 | cryptanalysis, 2 tokens, no key fit | 2 | none cheap |

## D. Blocked: already logged, waiting on a person or a gated account

**Copy-order/archive-only, offline since BL's 2023 outage or never digitised** (no REQUEST.md yet but the
target's own NOTES.md names the block and the person-facing next step): hamilton-1650 (offline-only, first
target of the archive-request lane, REQUEST.md-equivalent already in file), monck-1660 (BL, no digital image
anywhere), whitworth-1707 (four of five gap items resolved, one copy order left), stair-townshend-1710 (Univ.
of Kansas, physical), destaing-gerard-1779 (Bourdeau: no key material, decipherment would be in AAE archives),
maurice-rupert-1645 (BL Add MS 18980-82/72438, offline since 2023), berthier-napoleon-1812 (Vilcoq 1969 not
digitised; Chuquet 1912 crib exists but not yet fetched), rah-xiquena-1868 (six sources checked, RAH's own
site Anubis-blocked per the Access playbook table).

**DECODE account-gated** (login works, but this account's role cannot see full images/documents — ASKS row
42): decode-1162-modena-ambung-1492, decode-1168-modena-costabili-1492 (DECODE's own "Partially decrypted"
field, not independently confirmed), decode-2678-bnf-colbert127-gravel-1665 (flagged in its own file as
already someone else's WIP, not attacked here), intercepted-royalist-1646 (RecordsView metadata only, image
and document both return the same "Insufficient permissions" placeholder as 24 Sept).

**Large, multi-session, print-check-before-copy-order campaigns** (each has a named cheapest-first step, none
copy-free-cleared yet): sp35-townshend-key-1719 (locate the 1723/1803 Commons-committee appendix by topic
section before any copy order), sp54-maclean-1745 (*Lyon in Mourning* + HMC *Stuart Papers* full-text search
first), sp87-brunswick-1759 (818 items, 98 cipher-flagged — "a multi-session campaign, not a single check-
solved sweep"), sp87-chesterfield-1747 (check Dobrée's *Diplomatic Correspondence* at the Waldeck/Cronstrom
passage first), sp87-further-1712 (QUEUE's own note: fold into sp87's campaign, don't open separately),
sp87-newcastle-1743 (check Williams's *Carteret and Newcastle* first), sp90-raby-1704 and sp90-raby-
whitworth-1705 (check Wentworth Papers page-by-page, then BL Add MS 37373-89 for a contemporary decipher,
before any TNA copy order).

**41 targets with REQUEST.md already on file**, every one status `open`, every one's REQUEST.md opening line
"waiting on you" or a named archive/reproduction order (Riksarkivet, Archivio Segreto Estense, Archivio di
Stato di Torino/Genova, and others): belmesseri-napoli-1627, bl-farnese-cipher, bl-portugal-bombay-1661,
clerville-francia-1648, della-torre-olanda-1690, gla-claudiamedici-1633, hstas-osiander-1627, hza-hohenlohe-
1679, konstanz-talleyrand-sieyes-1798, lambeth-bacon-649, lambeth-casenowe-1586, newcastle-stone-1728, nla-
heinrich-braunschweig-1519, pro30-shaftesbury-1682, pro3053-horesse-1717, ra-celsing-dohsson-1779, ra-celsing-
sillen-1755, ra-crusenstolpe-1809, ra-karlxi-fullmakt-1677, ra-morner-welin, ra-vellingk-1713, salvago-caraffa-
1691, sp105-paget-1693, sp36-ball-1745, sp36-stquentin-pretender-1743, sp77-nicholas-1659, sp78-cesy-1628,
sp78-doncaster-1621, sp78-france-1583, sp78-waldegrave-delafaye-1734, sp78-yorke-1749, sp8-ehrenstein-1689,
sp81-roe-1638, sp81-stanning-1631, sp81-wroth-1596, sp99-wotton-1622, stas-waldburg-1653, taurello-roma-1527,
ula-degeer-1644, viganego-torino-1717, zbz-busbecq-1587.

One of these, **ra-karlxi-fullmakt-1677, is marked "Gated — do not send"** in its own REQUEST.md: the edition
search (*Sverges traktater med främmande magter*, vol. covering 1672-1697) is inconclusive, not negative, and
a copy order would be wasted if the cipher passage turns out to be already in print (deciphered or noted
illegible). **Score 4/10** — the one item in this bucket with a real cheap test still open ahead of the
archive ask; the rest score 1/10 (nothing left for a worker, correctly parked on the person).

## Count

Candidates scanned: 213 folders, 128 open/partial. Dropped by never-touch list: 17. Dropped for having an
AUDIT.md: 12. **99 triaged here.** Intake gate: PASS 2 (wellington-maitland-1812, decode-2754-bnf-
baluze156-1636), FAIL/missing verdict the remaining 97 (most because no formal six-source check-solved sweep
has ever been run on them, not because anything found is wrong). Route split of the 99: recovery-shaped 15,
cryptanalysis 16 (12 of them already negative or substantially resolved elsewhere), Heinsius circle 5,
blocked (archive/copy-order/DECODE-gated/person) 63.
