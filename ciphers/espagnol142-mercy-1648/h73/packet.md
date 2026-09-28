You are an adversarial reviewer. Below is the evidence a cryptanalysis campaign gathered for a CRIB CANDIDATE: that an unread stretch of a 1648 Spanish cipher letter (a homophonic numeric cipher, letters 2-34, a small nomenclature of codes 48/52/65/72 above the alphabet) names 'Burgsdorf' (Konrad von Burgsdorff, the Elector of Brandenburg's Oberkammerherr) and calls him 'su camarero mayor'. Your job is to find the strongest reasons the crib is WRONG or over-stated: statistical flaws, selection effects (the name was chosen by eye before the tests), multiple-comparison problems, circularity, historical implausibility, alternative readings. Be specific and concrete; rank your objections by severity (fatal / serious / minor); for each say what test or source would settle it. Do not propose that it is right; argue against it. Output a numbered list, then one line 'OVERALL:' with your verdict on how much weight the crib can bear. Read only this file.

## Campaign step H41 (2026-09-28 15:24-15:06 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. A crib candidate, not a reading.** The unread stretch after "el Elector de Brandenburg"
(r16-r17) carries the letters "... d l o n b u r g s [72] r f s [25] c m a r e [52] m a y o r ...". Hypothesis (formed by
eye from the context "pasareis a Cleues a ueros con el Elector de Brandenburg y con ..."): **BURGS[72]RF = Burgsdorf**,
with the nomenclature code 72 standing for a syllable (do) -- Konrad von Burgsdorff, the Elector's Oberkämmerer in the
1640s. Because the name was chosen after seeing the text, it is tested against every name a reader in that context
could have chosen instead:

- **Name list, built before scoring** (`h41/names.py` -> `h41/namelist.tsv`): 402 names -- every surname or place after
  von / v. / Graf / Freiherr / Herr / Oberst / Kanzler or with a possessive 's, 6-12 letters, seen twice or more, in
  *Urkunden und Actenstücke zur Geschichte des Kurfürsten Friedrich Wilhelm von Brandenburg* Bd. 4 (1867) and Bd. 5
  (1869), Internet Archive `urkundenundacten04berluoft`, `urkundenundacten05berluoft` (_djvu.txt; archive.org 3
  requests). Burgsdorf is 5th by frequency (95); the list keeps OCR variants (hurgsdorf, bnrgsdorf) and places.
- **Fit** (`h41/fit.py`, `h41/result.log`): each name aligned whole to the token stream, S-graded tokens +1 equal / -1
  unequal, M-graded and nomenclature tokens (48/52/65/72, 9, 15, 25) as wildcards for one or two letters, best start.

| window | Burgsdorf fit | rank | next real name | P (list fits >= Burgsdorf) |
|---|---|---|---|---|
| r15-r18, as pre-registered | 7 at r16:16 | 2 | brandenburg 11 at r15:11 (the already-read word) | 0.005 |
| r16:2-r18 (after the read "Brandenburg") | **7 at r16:16** | **1** (unique) | oranien / garantie / brandenburg 4 | **0.002** |

The pre-registered window ranked Burgsdorf second only behind the word the reading already holds at r15 ("Brandenburg"
itself); on the unread part it is the list's unique best fit, three points clear of any other name (its two OCR
variants aside), 7 of 9 letters matching at S-graded tokens with no mismatch. **By the row's rule it is a crib
candidate**, with the window caveat stated. What it implies, untested here: 72 is a syllable code (do), which fits H2's
nomenclature class; the next row (H42) tests the independent half of the same hypothesis ("su camarero mayor" after
the name). No key.tsv, token, grade or class change; nothing here is a reading.


## Campaign step H42 (2026-09-28 15:28-15:08 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Borderline; not a reading.** The independent half of H41's hypothesis: after the
Burgsdorf candidate, r17 reads "s [25] c m a r e [52] m a y o r" -- "su camarero mayor" (Oberkämmerer) if 25 = u,
one a is unwritten and 52 is a syllable (ro). Title list built before scoring (`h42/titles.py` -> `titlelist.tsv`): every
word X in "X mayor" in the es17c7 Cartas corpus, 4-12 letters, 3+ occurrences (37 titles; camarero itself is not among
them at that threshold -- camarera is -- so camarero was added as the tested item). Each phrase "su X mayor" aligned to
r17-r18 with H41's scorer (S tokens +1/-1, M and nomenclature tokens one-or-two-letter wildcards, no deletions for any
candidate); `h42/result.log`.

**camarero: fit 9 at r17:3, rank 1, tied with camarera** (the same title, differing only in the letter that falls on
the 52 wildcard); next correo 7 (correo mayor, also a real office), then guarda / alferez 5. P (list phrases fitting at
least as well) = 2/38 = **0.053 -- the pre-registered P < 0.05 is not met by the strict count**; with camarera merged as
a gendered variant of the same title (as H41 kept OCR variants apart but they are one name) it is 1/37 = 0.027. The list
is small, so P cannot resolve finer than about 0.03. Read with H41: the name that best fits the stretch is the Elector's
chief chamberlain, and the title that best fits the next words is chief chamberlain -- two fits that agree, one clearing
its gate and one on the line. Both assume nomenclature codes stand for syllables (72 = do, 52 = ro), which no period key
has confirmed. **Crib candidates for the orchestrator and the Brussels register comparison, not a reading**; no key.tsv,
token, grade or class change. REGISTER-CHECKLIST.md gains the two syllable values to check.


## Campaign step H43 (2026-09-28 15:31-15:10 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Context corroboration for the H41-H42 crib candidates; not a reading, no print of this
letter.** Full text of *Urkunden und Actenstücke ... Friedrich Wilhelm* Bd. 4 and 5 (the H41 downloads, grepped on
disk) and IA be-api full-text search of Cuvelier-Lefèvre VI (`correspondancede0006jose`; positive control "Brandebourg"
and "Clèves" both hit; `h43/fts_cuvelier6_*.json`; be-api 4 requests):

- **Title and place match the crib.** Urkunden Bd. 4 prints an "Instruction für den **Oberkammerherrn Conrad von
  Burgsdorf** zur Verhandlung mit dem Pfalzgrafen, Dat. **Cleve** 9. Febr. 1647" and a "Kurfürstliche Attestation für
  Burgsdorf dat. Cleve 10. Sept. 1647 -- Der Oberkammerherr etc. Conrad von Burgsdorf"; Bd. 5 calls him "den
  einflussreichen Oberkammerherrn Konrad v. Burgsdorf". Oberkammerherr is literally camarero mayor, and in 1647 he was at
  Cleves, the town the letter sends Mercy to ("pasareis a Cleues a ueros con el Elector de Brandenburg").
- **Spanish contact in the same business:** Bd. 4 records the Spanish governor of Guelders (Baron de Ribeaucourt,
  Roermond, 13 Feb 1647) sending a letter that the Elector forwarded to Burgsdorf at Düsseldorf, and Burgsdorf reporting
  "die spanische Mahnung zum Frieden an den Pfalzgrafen" (18 Feb 1647); and a 1647-48 section "Burgsdorfs an Kursachsen
  und Braunschweig". Spanish Netherlands officials dealt with him directly the year before.
- **Not found:** no 1648 passage naming Mercy, a Spanish envoy's approach to Burgsdorf, or a levy of 3,000 infantry in
  Bd. 4-5 (grep of Burgsdorf within three lines of spani-/Leopold/Erzherzog/Brüssel/Mercy/Niederland: five hits, all
  1647 or general); Cuvelier-Lefèvre VI has no Burgsdorf at all (0 hits, both spellings).

Corroboration of plausibility only: the man the name crib picks was the Elector's chief chamberlain, at Cleves, dealing
with Spanish officials, in the months before the letter. The crib stays a candidate until the Brussels register gives 72
and 52 (REGISTER-CHECKLIST.md). No key.tsv, token, grade or class change.


## Campaign step H44 (2026-09-28 15:38-15:40 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Control failed on the name; the target reader was not run.** Blind replication of the
H41-H42 crib, control first (`h44/build.py`, `packet_control.txt`, `packet_target.txt`, `reply_control.txt`). Control: a
Cartas sentence with a known person and title ("y al conde de Baynete, su caballerizo mayor"), encoded as the target
stretch is shown (letters run together, 4 of 35 as "?", 2 wrong letters), with its clear context. The blind Sonnet
reader returned **"y al conde de Basto es su caballerizo mayor" -- office right, name wrong**: it read the damaged
"baysete" as a better-known title ("Basto") and explained the mismatching letters away as damage. By the row's rule the
control must recover its known name before the target counts, so the target packet was not read.

What this shows about the instrument: a reader recovers a common office from damaged letters but fills a proper name
from world knowledge where the letters are few and uncertain. A target reader naming Burgsdorf would therefore not
have been independent evidence either -- Burgsdorff is the best-known courtier of that Elector. The letter-fit test
against a list built before scoring (H41) is the right instrument for the name, and it stands as it was. One text
call. No token, grade or class change.


## Campaign step H45 (2026-09-28 15:45-15:56 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** If the nomenclature codes stand for syllables (H41-H42's reading of 72 and 52), which one-
or two-letter value reads best for 48 and 65? Every value of 1-2 letters (506) substituted at all of a code's
occurrences in the key.tsv decode, scored by H35's word segmentation (es17c7 word unigram); control: 200 draws of the
same number of random S-graded positions searched the same way (`h45/syll.py`, `h45/result.log`, 16 min CPU).
Pre-registered: a candidate must improve every occurrence and beat the control's 95th percentile.

| code | occurrences | key.tsv | best value | gain | per occurrence | control median / p95 | candidate |
|---|---|---|---|---|---|---|---|
| 48 | r17:20, r20:15 | d | "qu" | +4.42 | +4.97, -0.55 | -1.47 / +6.54 | no |
| 65 | r24:4 | s | **"sr"** | **+15.16** | +15.16 | 0.00 / +7.08 | **yes** |

65 = "sr" gives "tres regimient-" at r24 ("en dos o tres regimientos"); key.tsv's s leaves "tres egimient-". The test
cannot separate two readings of that gain: 65 as a two-letter unit (s + r, across a word boundary -- unusual for a
syllable code) or 65 = s with the scribe leaving out the r. Either way the word is "regimientos" and the passage reads
"en dos o tres regimientos". 48 has no value that helps both occurrences; it stays d (M). No key.tsv, token, grade or
class change: 65 stays M, with "sr" logged as the candidate value in REGISTER-CHECKLIST.md.

Note from DECODE-OPEN's H17 (merged this hour): the Brussels register 958-965, read at full size, holds no candidate
period key for this letter and no values for the M codes or the boxed 101, so the register checklist's syllable
questions (72, 52, 65, 48) have no period source on file; they stay cryptanalytic.


## Campaign step H46 (2026-09-28 16:07-15:57 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** The other unread stretch, v04 after "y que corra por su": its letters with M
and nomenclature tokens as "?" read "noladire?tnonysiiu?a". List built before scoring: every word after "por su" in the
es17c7 Cartas corpus, 4-12 letters, 3+ occurrences (30 words, `h46/wordlist.tsv`); each aligned to v04:1 with H41's
scorer (`h46/crib.py`, `h46/result.log`). Best: **"poca", fit 0** (two letters agree, two disagree), then vida / casa /
alma -2. The pre-registered rule (unique best, P < 0.05) is met only formally (P 1/30 = 0.033): a fit of 0 means nothing
aligns, so this is logged as no candidate, and the rule's gap is noted -- a list test also needs a minimum fit (for
example most letters of the word agreeing), which H41's Burgsdorf (7 of 9 letters, no mismatch) met and this does not.
v04 may not begin a word, or "por su" may not be the phrase boundary; the stretch stays unread. No token, grade or
class change.


## Campaign step H47 (2026-09-28 15:59-15:59 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** A given name before the Burgsdorf candidate? The tokens ending at r16:15 read
"...y e o n e o p ? r a d l o n". List built before scoring (`h47/given.py` -> `h47/namelist.tsv`): 217 words standing
before "von <Name>" in Urkunden Bd. 4-5 (mostly given names -- Iohann, Conrad, Friedrich, Moritz, Wilhelm -- with some
nouns), each fitted as "X" and "X de" ending at r16:15, H41's scorer. Best: **"anton", 3 letters agree and 2 disagree
(fit +1)**; then garnison 0, the rest below. The pre-registered rule (unique best, P < 0.05, >= 60% of letters
agreeing, at most one mismatch) is **not met**. Conrad fits badly in every form (conrad / conrad de / conrado: 0 letters
agreeing; conrado de: 3 agree, 4 disagree). So the words before the name are not his given name in any form the list
holds; the stretch before "burgs" stays unread, and the H41 name candidate neither gains nor loses. `h47/result.log`.
No token, grade or class change.


## Campaign step H48 (2026-09-28 16:00 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** The list-crib instrument of H41/H42/H46/H47 is now a shared tool,
`tools/crib_list_fit.py` (a keyed code stream, a window, a word list built before scoring; S tokens +1/-1, other
grades 1-2-letter wildcards; the list as the null; anchors start/end/free; forms such as '{w}de' or 'su{w}mayor'), with
the minimum-fit rule H46 showed was missing (candidate only as unique best, P < 0.05, >= 60% of letters agreeing, at
most one mismatch). Offline test `tools/tests/test_crib_list_fit.py`: catches H41 (burgsdorf unique best, 7 agree / 0
disagree at r16:16, candidate) and refuses H46 (poca unique best at P < 0.05 but 2 agree / 2 disagree). Re-run on H41's
402-name list it reproduces H41 exactly (burgsdorf 7, P 0.002, candidate True). SYSTEM.md names it (system_map_check
ok); h41/fit.py and h46/crib.py carry a pointer to it. Under the new rule H42's "su camarero mayor" would also need
checking against its minimum fit (it agrees on its S letters; its borderline was P, not fit). No token change.


## Campaign step H49 (2026-09-28 16:01 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. No candidate by the rule (tie).** The word after "para" at r17:20, window "?iense i embian
cartas de cr..." (48 as wildcard): list built before scoring = every word after "para" in the es17c7 corpus, 4-12
letters, 3+ occurrences (299 words, `h49/wordlist.tsv`); `tools/crib_list_fit.py --anchor start --start r17:20`
(`h49/result.log`). Best: **"bien" and "quien" tied, 3 letters agreeing and 0 disagreeing** (P 0.007); next defensa /
hacerse / poderse at 3/2. Not unique, so not a candidate. Observation only, for the record: with 48 = "qu" the passage
reads "... mayor, para quien se embian cartas de creencia que uan con esta" (to whom letters of credence are sent,
which go with this), which is also the value H45 found best for 48 at this occurrence (+4.97) -- but H45 found the same
value slightly worse at 48's other occurrence (r20:15, -0.55), so 48 stays d (M) and "qu" stays an observation. No
token, grade or class change.


## Campaign step H51 (2026-09-28 16:08 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Context corroboration only.** The remaining *Urkunden und Actenstücke* volumes, Bd. 1
(1864), 2 (1865), 3 (1866) and 6 (1872) (IA `urkundenundacten0{1,2,3,6}berluoft` _djvu.txt; archive.org 4 requests),
grepped for Burgsdorf within three lines of spani-/Leopold/Erzherzog/Brüssel/Mercy/Werbung/Infanterie/1648
(`h43/h51_hits.txt`; Burgsdorf occurs 57 / 20 / 1 / 18 times). Eight hits; the relevant ones:

- **Bd. 2 (French side), Cleve, January-February 1648:** Wicquefort to Lionne, "Dat. Cleve 14. Jan. 1648 -- Burgsdorf
  und ein anderer Vertreter der 'guten Partei' an diesem Hofe zu Gratificationen vorgeschlagen"; Schwerin to Wicquefort,
  Cleve 20 Feb 1648, calling him "M. le grand-chambellan" (the French for Oberkammerherr, i.e. camarero mayor), and the
  editors' note that the Elector's Oberkammerherr Conrad von Burgsdorf was then working on a "third" armed party in the
  Empire with the Brunswick courts and Saxony.
- **Bd. 1:** a copy sent to Conrad v. Burgsdorf "nach Cleve" (Königsberg, 7 Oct 1648): he was at Cleves in 1648.
- No passage names Mercy, a Spanish envoy, or a Spanish request for troops through Burgsdorf; Bd. 3 has nothing; Bd. 6
  only a 1651 mission.

So in the months around 6 June 1648 the Elector's court sat at Cleves, Burgsdorf was its chief chamberlain and the
man foreign courts approached (the French proposing to pay him), which is what the H41-H42 crib has the Brussels court
telling Mercy to do. Corroboration of plausibility, not of the reading; absence of a Spanish passage refutes nothing.
No token, grade or class change.


## Campaign step H52 (2026-09-28 16:09 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** For the orchestrator's decision whether to send the r16-r17 crib to a separate verifier
session: `candidates/candidates.tsv` lists each candidate value with its step, test and result (72 = do, H41 met; 52 =
ro, H42 not met strictly; 65 = sr, H45 met but indistinguishable from an omitted r; 48 = qu at r17:20 only, not met,
observation), and `candidates/make_candidates.py [--check]` writes `candidates/reading_candidates.txt`: every cipher
line under key.tsv (K) and, where a candidate applies, the same line with it in braces (C):
r16 "GYEONEOPURADLONBURGS{do}", r17 "RFSUCMARE{ro}MAYORPARA{qu}I", r24 "TRE{sr}EGIMIENTIYCONQUE". --check passes.
reading.txt, key.tsv and every grade are unchanged; the file's header says these are candidates, not a reading.


## Campaign step H53 (2026-09-28 16:11 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Robustness of H41 to its wildcard set: the same 402-name list and window (r16:2-r18:21)
through `tools/crib_list_fit.py` with fewer wildcards (`h53/result.log`):

| wildcards | Burgsdorf | next real name | P | candidate |
|---|---|---|---|---|
| (0) every non-S token (H41 as run) | 7 agree / 0 disagree, unique best | brandenburg / garantie 4 | 0.002 | yes |
| (a) only nomenclature 48/52/65/72 (9, 15, 25 at key.tsv letters) | 7 / 0, unique best | garantie / oranien 4 | 0.002 | yes |
| (b) only 72 | 7 / 0, unique best | altenburg / brandenburg 3 | 0.002 | yes |
| (c) none (72 = z) | not in the top 5 | altenburg 3 (6/3), 7-way tie | 0.017 | no |

The crib does not lean on the uncertain letter codes (9, 15, 25) at all: it stands on **one assumption, that the
nomenclature code 72 is a two-letter unit** (do); with 72 as the single letter z nothing on the list fits the stretch.
That is the one question a period key of this office, or another letter using 72, would settle. No token, grade or
class change.


## Campaign step H54 (2026-09-28 16:12 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** The words between "el Elector de Brandenburg" and the Burgsdorf candidate,
r16:2-15 "y e o n e o p ? r a d l o n": list built before scoring = every 2-5-word sequence in es17c7 beginning "y con",
8-16 letters, 3+ occurrences (79, `h54/phrases.tsv`), fitted with `tools/crib_list_fit.py --anchor end --end r16:15`
(`h54/result.log`). Best "y con esta ocasion", 7 agree / 6 disagree (fit +1); everything else below 0. No phrase meets
the rule. The span may hold a title or particle the newsletters do not use ("y con el Oberkammerherr" has no Spanish
form in the corpus), or carry misread tokens; it stays unread and the H41 name candidate is unaffected. No token,
grade or class change.


## Campaign step H55 (2026-09-28 16:13 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** v04 anchored at its end (the clear "sera mas conuenient" follows): list =
every word before "sera" in es17c7, 4-12 letters, 3+ occurrences (17, `h55/wordlist.tsv`), `tools/crib_list_fit.py
--anchor end` at v04:19 (the gutter token, 15, M, wild) and at v04:18 (`h55/result.log`). Best "cual" fit 0 (1/1) at
v04:19, "bien" -2 at v04:18; no word meets the rule. With H46 (start-anchored) both ends of v04 are tested by list and
neither fits; the stretch stays unread. No token, grade or class change.


## Campaign step H56 (2026-09-28 16:14 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Is H53's one assumption (72 is a multi-letter unit) this office's habit? Answered from
DECODE-OPEN's transcriptions already on disk (`period_keys/README.md`, section "The M codes and the H41/H42 syllable
reading"; no new fetch): in the Brussels register's own keys, codes just above the letter alphabet are syllables where
they occur -- R960 48 = no, 65 = ba; R962 (Latin) 52 = re, 65 = s, 72 = san, 101 = vu; R963 101 = ay; R959's two-letter
word codes (au, de, du ...) run 12-89 and R961's syllabary starts at 35. So a syllable at 72 in a key of this office
is the office's practice, not an exception; **the assumption the Burgsdorf crib rests on is consistent with the
register's design, but no table gives 72 = do or 52 = ro** (these are other keys). No token, grade or class change.


## Campaign step H57 (2026-09-28 16:15 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Usage attested both ways -- a caution for H42.** Google Books API (key present, country=US;
7 queries, 1.6 s apart; `h57/gbooks.tsv`):

- **"camarero mayor del Elector" for an elector's courtier is period usage**: *Mercurio histórico y político* (1739),
  "el Conde de Preysing, Camarero Mayor del Elector" (Bavaria); *El gran diccionario histórico* (1753), "camarero mayor
  del elector de Baviera". So a Spanish writer could call an electoral Oberkammerherr "su camarero mayor".
- **But "camarero mayor" is also the Spanish title of the Elector of Brandenburg himself**, as Arch-Chamberlain of the
  Empire (Erzkämmerer): *Crónica del emperador Carlos V* ("el Marqués de Brandemburgo, su Camarero mayor"), *Estado
  político de la Europa* (1740), *El gran diccionario histórico* (1753, "Brandeburgo, Camarero Mayor"). Near "el Elector
  de Brandenburg" the phrase could therefore name the Elector's own imperial office rather than a courtier.
- Spanish print knows the man as "Conrado de Burgsdorf" only in modern works (1919, 2006); no 17th-century Spanish hit
  for Burgsdorf; "Burgsdorf" with "camarero mayor" 0.

Effect on the crib: the name fit (H41, H53) does not depend on the title; the title fit (H42, borderline) now has a
second reading that does not need Burgsdorf at all ("... [Burgsdorf], su camarero mayor" vs a phrase about the Elector
as camarero mayor del Imperio). H42 stays borderline, and the pair of fits is weaker evidence of one person than H42's
note put it. No token, grade or class change.


## Campaign step H58 (2026-09-28 16:18 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** The Brussels side in calendar form, for 1648 entries on Brandenburg / Cleves /
a levy / Mercy that might name the persons Mercy was to see. (1) Cuvelier-Lefèvre VI, IA be-api full-text search
(`correspondancede0006jose`; 8 queries, `h58/fts_*.json`): Brandebourg, Clèves, levée, "trois mille", Neubourg hit
only early-century entries (Archduke Albert, the Jülich-Cleves question); Mercy hits only the known p.647 (no. 1499) and
index lines; Burgsdorf 0. The API returns at most five snippets per query, so this is a sample, not a full read. (2)
Lonchay 1896, *La rivalité de la France et de l'Espagne aux Pays-Bas*, full _djvu.txt (IA
`la-rivalite-de-la-france-et-d-espagne-aux-pays-bas-1635-1700`, grep; `h58/lonchay_hits.txt`): one Brandenburg passage
near 1647-49 dates (the 1658 imperial election), nothing on Mercy's Cleves mission beyond p.445 (already in
siblings_brussels.md). archive.org 3 requests, be-api 8. No token, grade or class change.


## Campaign step H59 (2026-09-28 16:32 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Non-test by construction, not a negative.** A list-free check of the crib: H45's value
search (506 one- and two-letter values, word-segmentation gain, 200 random-S-token draws) run for 72 and 52
(`h59/syll_72_52.py`, `h59/result.log`).

| code | best value (gain) | crib value: rank of 506, gain | control p95 | candidate |
|---|---|---|---|---|
| 72 (r16:21) | "e" (+3.07) | **do: 134th, -3.00** | +7.08 | no |
| 52 (r17:10) | "s" (+2.43) | **ro: 390th, -5.69** | +7.01 | no |

Neither crib value is favoured, but neither could have been by this instrument, and the control could not show it
(CLAUDE.md rule 3, "a control that cannot vary on the same axis"): the word model is es17c7's Spanish vocabulary, in
which "burgsdorf" occurs 0 times, so "burgs-do-rf" makes no known word and earns nothing; and "camarero" (17
occurrences) cannot be formed at 52 by any value, because the stretch reads "s u c m a r e [52]" -- the a after c is
missing, which a value at 52 cannot supply. A list-free value search can only confirm a value that completes a word
the corpus knows with no other letter missing. The crib's evidence stays H41/H53 (name fit, list null) with H43/H51/H56
as context. No token, grade or class change.


## Campaign step H60 (2026-09-28 16:33 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** The crib's own tokens (r16:14-21, r17:1-12) in every pass on disk: pass A and pass B
(Y6) agree on every token (A grades 72 and 52 m, B h); `disagreements.tsv` has no r16/r17 row; MEYE's blind pass
(`meye/blind_pass.tsv`) reads the same codes, with 72 at r16:21 graded M: **"written as one run-together stroke pair
with no visible gap; could be a single two-digit code 72 or two adjacent single tokens 7, 2"**; H2's three reads
(`h2crops/reconcile.tsv`) settle 72 as one group, 3 of 3 ("7 has the hand's leading top bar; gap 7-2 matches
intra-group gaps"); 52 is one group 3 of 3. So the transcription of the crib's letters is solid, and the one
alternative any pass raised is at 72 itself: **if r16:21 were the two tokens 7 (t) and 2 (o), both S-graded letters,
the stretch would read BURGS-T-O-RF, "Burgstorf", with no syllable assumption at all.** H2's gap measurement favours one
group; the question is filed as H62 (score the split reading with the same list and rule). No token, grade or class
change.


## Campaign step H62 (2026-09-28 16:34 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. The name fit no longer needs the syllable assumption, if r16:21 is two signs.** MEYE's
alternative (H60): r16:21 read as the two tokens 7 (t, S) and 2 (o, S) instead of the one code 72. A copy of the stream
with that split (`h62/cipher_codes_split72.tsv`; cipher_codes.tsv untouched) through `tools/crib_list_fit.py` on H41's
402-name list, window r16:2-r18:21 (`h62/result.log`):

| wildcards | Burgsdorf | P | candidate |
|---|---|---|---|
| default (M-graded tokens wild) | unique best, 8 of 9 letters agree, 1 disagrees (t for d) | 0.002 | yes |
| only 48/52/65 wild (9, 15, 25 at key.tsv letters) | same, 8 / 1 | 0.002 | yes |
| **none at all** (every token at its key.tsv letter) | **same, 8 / 1** -- next altenburg / brandenburg 3 | **0.002** | **yes** |

Read with 7 2, the stretch gives **B-U-R-G-S-T-O-R-F** letter for letter from codes graded S (12 b, 8 u, 5 r, 22 g,
6 s, 7 t, 2 o, 5 r, 20 f), and **"Burgstorf" is a period spelling of the name**: Urkunden Bd. 1 prints "Burgstorf" 7
times and "Burgstorff" 15 times beside 57 "Burgsdorf" (grep of the H51 download). The one disagreement with the list's
"burgsdorf" is exactly that spelling difference. Against it: H2's three reads call 72 one group ("gap 7-2 matches
intra-group gaps"), the code 72 occurs only here, and a separate 7 followed by a separate 2 occurs nowhere else in the
letter (0 pairs). So the crib now rests on a single transcription question -- one sign or two at r16:21 -- which an
objective gap measurement on the image can settle (H63). No token, grade or class change; cipher_codes.tsv unchanged.


## Campaign step H63 (2026-09-28 16:36 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. One sign: 72.** Objective gap measurement on line r16 of the native image
(`images/f22r_canvas58.jpg`, band y 3019-3244, H15's settings: threshold < 100, components of area >= 40 px and height
>= 12 px; `h63/gaps.py`, `h63/gaps.log`). The line's 34 ink spans map onto its 21 tokens from the end (72 = spans 32-33,
6 = 31, 22 = 29-30, 5 = 28, ...). Gaps split cleanly at about 25 px: **inside a group 5-14 px** (n = 14, the 13 px gap itself included), **between groups
33-74 px** (n = 19). **The 7-2 gap at r16:21 is 13 px**, inside the intra-group range and 20 px below the smallest
between-group gap on the line. So r16:21 is one code, 72, as H2's three reads had it; MEYE's "7, 2" alternative and
H62's letter-for-letter "BURGSTORF" are disfavoured by the leaf's own spacing. The Burgsdorf crib therefore rests again
on H53's one assumption, that the nomenclature code 72 stands for two letters (do) -- consistent with the office's
habit (H56) but unattested for this key. H62's result stands as recorded (the fit if the split were real), with this
measurement against the split. No token, grade or class change.


## Campaign step H61 (2026-09-28 16:37 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** H41 against larger lists built the same way (`h41/names.py`) from the Urkunden volumes
H41 did not use -- Bd. 1, 2, 3, 6 alone (599 names, `h61/names_bd1236.tsv`) and all six volumes (883,
`h61/names_bd1to6.tsv`) -- through `tools/crib_list_fit.py` on r16:2-r18:21, with only 72 wild (every other token at its
key.tsv letter) and with the default wildcards (`h61/result.log`). In all four runs **every fit of 5 or more is a
spelling of the one name** -- burgsdorfs 8/0 (the genitive, its s landing on the s of "su"), burgsdorf 7/0,
burgstorff 7/1, buigsdorf / bnrgsdorf / hurgsdorf (OCR variants) 6/1 -- and the best other name is "brandenburg" at 3-4,
the word already read at r16:9. P (list fits >= best) 0.002 (599) and 0.001 (883). The name fit is stable to the list:
a list three times larger from independent volumes turns up no rival. It still rests on 72 standing for two letters
(H53, H63). No token, grade or class change.


## Campaign step H64 (2026-09-28 16:38 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** The crib record is consolidated for the orchestrator: `candidates/candidates.tsv` (72's
row now carries H53, H61, H62/H63; 52's carries H57) and REGISTER-CHECKLIST.md ("Update, 28 Sept 2026 evening").
`candidates/make_candidates.py --check` passes (the reading_candidates.txt lines are unchanged: the candidate values did
not change, only their evidence). In one sentence: the unread r16-r17 stretch fits the name Burgsdorf (the Elector's
Oberkammerherr, at Cleves in 1647-48) better than any of 883 period names if, and only if, the nomenclature code 72 stands
for the two letters "do" -- the office's habit, unattested for this key. Disk only; no token, grade or class change.


## Campaign step H65 (2026-09-28 16:39 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative, with a precedent.** Meinardus, *Protokolle und Relationen des Brandenburgischen
Geheimen Rates* (1889-1907), six IA copies (`bub_gb_EeYXAAAAYAAJ` = Bd. 3, `protokolleundre01meingoog`,
`protokolleundre03meingoog`, `bub_gb_x-4XAAAAYAAJ`, `bub_gb_zuQXAAAAYAAJ`, `protokolleundre02meingoog`), _djvu.txt grepped on
disk (archive.org 7 requests). "Mercy" occurs once in all six (a "Kapitän Mercy" in a muster list, Bd. 3); no Spanish
envoy, Abt or Erzherzog passage is dated 1648 or tied to Mercy. The one Leopold Wilhelm mission found is Bd. 3 no. 501:
**"Sendung des Freiherrn von Ribaucourt seitens des Erzherzogs Leopold Wilhelm an den Kurfürsten. Cleve. [15 August]
1647"**, about restoring Count Schwarzenberg -- not Mercy's business, but a precedent a year earlier for the archduke
sending an envoy to the Elector at Cleves (Ribaucourt, governor of Spanish Guelders, is the same man who wrote to
Burgsdorf in Feb 1647, H43). Corroboration of the channel only. No token, grade or class change.


## Campaign step H67 (2026-09-28 16:42 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative: no alternates to try.** v03-v05 in every pass on disk: pass A and pass B agree
on all 18 readable tokens of v04 (A grades 15 at v04:9, 7 at v04:10, 21 at v04:16 and 15 at v04:19 m); disagreements.tsv
has only v04:19 (B has no token there); MEYE marks v04:16 "21" followed by a colon-like mark (punctuation, as H13
inventoried) and v04:19 "1?" unreadable at the gutter; H2's three reads agree: 15 one group at v04:9, 21 + colon at
v04:16, v04:19 cut by the photograph's edge (partial, 15/16/19). So the unread v04 stretch is not a transcription
tangle: every token but the gutter one is read the same by every pass, and the gutter token was already a wildcard in
H46 and H55. No list crib gets a new substitution to test; the stretch waits for a period key or the gutter capture
(H12, ASKS 81). No token, grade or class change.


## Campaign step H68 (2026-09-28 16:44 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** BSB/MDZ (www.digitale-sammlungen.de): the search page is rendered client-side
(plain curl returns the shell only), so `tools/browser_fetch.js` was used, one request at a time, 3-4 s apart (6
requests; saved pages in `h68/`). MDZ's search covers metadata and full texts of the Theatrum Europaeum continuations
(e.g. bsb10807452, vol. 14). Exact-phrase queries: **"Abt von Mercy" 0 matches, "Abbt von Mercy" 0**. Unquoted queries
(Mercy Cleve Churfürst 1648; Mercy Burgsdorff) are OR-matched across the library (406,192 and 103,584 hits, topped by an
English novel), so they are noise, not a test. Vol. 6 itself (1647-1651) was not opened page by page. No
contemporary German print of the abbé's 1648 mission found by this route. No token, grade or class change.


## Campaign step H70 (2026-09-28 16:47 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. Negative.** The *Gazette* (Renaudot) for 1648 is one annual volume on Gallica
(`ark:/12148/bpt6k6391523f`, the collection's only 1648 date, 16480101). Gallica ContentSearch inside it (5 requests
including the date listing, 2 s apart; `h69/cs_*.xml`): "Mercy" / "Merci" 6 hits, all the word *merci* ("à la merci
des Confédérez", "se rendre à la merci du Parlement"), never the abbé; "Brandebourg" 14 hits, all the peace treaty,
Pomerania, the Elector's levy in Prussia (PAG_572) and the Polish succession -- none on a Spanish envoy at Cleves. The
Paris Gazette did not report Mercy's mission. No token, grade or class change.


## Campaign step H71 (2026-09-28 16:49 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial. The Burgsdorf fit does not occur by chance in this letter's read text; the tool's rule
needed a floor, now added.** False-positive control for H41's method (`h71/fp.py`, `h71/windows.tsv`,
`h71/result.log`): every 62-token window (the unread stretch's length), step 8, over the letter's cipher stream,
excluding the unread stretch, v04, and the cipher spellings of Brandenburg, Cleues and Cheureuse -- 24 read, name-free
windows -- scored against the 883-name list (Urkunden Bd. 1-6) with the same wildcard rule.

- **No window reaches Burgsdorf's fit**: the best fit in any read window is **4** (24 of 24 at most 4), against **7 with
  no mismatch** for Burgsdorf on r16:16 (8 for the genitive burgsdorfs). Read Spanish text of this letter does not throw
  up a name-fit anywhere near the one on the unread stretch.
- **But the tool's candidate rule (H48) passed short names at fit 4** in 10 of the 24 windows -- two distinct spots,
  "xanten" (5 agree / 1 disagree) around r19-r21 and "tarent" in v05-v06 -- because uniqueness, P and "60% of letters,
  at most one mismatch" are all easy for a six-letter name. Fixed in `tools/crib_list_fit.py`: `--min-score` (default
  6) requires an absolute fit above what the target's read text produces; `tools/tests/test_crib_list_fit.py` gains the
  H71 must-not case (xanten at r19:6 refused, and passing without the floor); SYSTEM.md's entry updated. Re-run with the
  floor: 0 of 24 read windows pass, and H41's Burgsdorf (7) still passes. H46, H47, H49, H54, H55 were all negatives
  under the old rule, so the floor changes none of them.

No token, grade or class change.


## Campaign step H72 (2026-09-28 16:50 UTC, campaign runner owner account, session_01K2B2cTCwujqmMqmGYyE6BY)

**Status unchanged: partial.** Synthetic-name null for H41, finer than the list's 1/883 (`h72/synth.py`,
`h72/result.log`): a character trigram model trained on the 883 Urkunden names sampled 10,000 name-shaped strings of
6-12 letters (seed 72, list names excluded), each fitted to r16:2-r18:21 with `tools/crib_list_fit.py`'s default
wildcards. **0 of 10,000 reach Burgsdorf's fit (7 agree, 0 disagree): P < 0.0001 (95% upper bound about 0.0003).** Three
reach 6, and they are the model rebuilding the Burgsdorf pattern itself from its training names ("burgsdorfdrg",
"urgsburf", "lenburgse"). With H71 (read text of the letter never above 4), H61 (no rival among 883 real names) and
H53/H63 (the fit needs only 72 to stand for two letters, and 72 is one sign), the name fit is as strong as a
cryptanalytic crib gets here without a key; it is still a candidate, not a reading, because the one assumption is
unattested for this key. No token, grade or class change.


## candidates/candidates.tsv

code	where	candidate	key_tsv	step	test	result
72	all (r16:21)	do	z (M)	H41	name list fit, 402 Urkunden Bd. 4-5 names, tools/crib_list_fit.py	Burgsdorf unique best on r16:2-r18, 7 agree / 0 disagree, P 0.002; rank 2 on the pre-registered r15-r18 window behind the already-read Brandenburg (P 0.005); H53: holds with only 72 wild (every other token at its key.tsv letter), gone if 72 is one letter; H61: on 599/883 independent names every fit >= 5 is a spelling of Burgsdorf, P 0.002/0.001; H62/H63: if r16:21 were two signs 7 2 it would spell BURGSTORF (a period spelling) from S codes, but the 7-2 gap is 13 px, inside the line's intra-group range (5-14) and below every between-group gap (33-74), so it is one sign and the fit rests on 72 as a two-letter unit (the office's habit, H56; unattested for this key)
52	all (r17:10)	ro	y (M)	H42	title list fit, 38 Cartas "X mayor" titles	camarero ties camarera, fit 9; P 0.053 strict (not met), 0.027 with camarera merged; H57: "camarero mayor" is also the Spanish title of the Elector of Brandenburg himself (Arch-Chamberlain of the Empire), so this fit does not point to Burgsdorf on its own
65	all (r24:4)	sr	s (M)	H45	1-2-letter value search, word-segmentation gain vs 200 random-S-token draws	+15.16 vs control p95 +7.08, met; the same gain would come from s with the r left out by the scribe
48	r17:20 only	qu	d (M)	H45, H49, H50	value search (1-3 letters) at both occurrences; word list after "para"	not met: qu +4.97 at r17:20 but -0.55 at r20:15; "bien"/"quien" tie in H49; observation only
