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
