# PREREG MQS-PILE-REGISTER (LANE MQS-3, account 4), written 9 Oct 2026 10:15 UTC by date -u (first draft of this line said 10:3x, wrong), before any control run

Tool: `tools/pile_register.py` (register of held + referenced letters per pool, built on `tools/holder_export.py`'s
`read_list`/`build_rows`; text timeline; `--refs-scan EDITION.txt --dates DATES.tsv` greps an edition's letters at the
given dates for back-references -- 'your letter of', 'your favour of', 'my letter of', 'votre lettre du', 'ma lettre
du', 'vuestra carta de' and kin -- and resolves the date each one names, as leads). Paper row M05 + M32 (Lasry,
Biermann and Tomokiyo 2023, App. C pp.200-202, Figs 17, C25-C26; Bossy 2001).

## Known answer

Edition on disk: Massachusetts Historical Society, *Collections* 7th ser. vol. VI (Bowdoin and Temple Papers, part
II, 1907), IA OCR at `ciphers/armstrong-madison-1808/sources/h75/bt2_djvu.txt` (already in the repository; no host).
Every printed letter carries a header 'A TO B.' and a place-and-date line; the edition therefore lists its letters by
date. prior_work.py step (`armstrong-madison-1808 --item-spec 'shelfmark=MHS Collections 7th ser. vol. 6 ...;
sender=Bowdoin;recipient=Temple;kind=edition' --step-type decode --known-answer gate:MQS-PILE-REGISTER --fetch`):
`exit 4: owed before this step: LOOK adhoc-f3c937:2-leaf:3ca102, UNCHECKED adhoc-f3c937:3-solver:a7793a, UNCHECKED
adhoc-f3c937:3-tomokiyo:80d907` (warn-first; the material is printed clear text, which is the point of a known answer;
nothing is read, keyed or decoded on any target).

Ground truth G: every (from, to, date) parsed from a header + date line (4-digit year, 1700-1830), parsed by the
harness `tools/tests/mqs_pile_register_control.py` with the tool's own date-line parser.

Held-out set K (fixed from headers alone, before any scan): every letter X = (A -> B, D) in G for which G also holds
a letter B -> A dated D < D2 <= D + 60 days (a reply exists in the edition). All such X are held out together.
Held = G minus K. The scan is run with `--dates` = the held letters' dates, window 0 (only the held letters'
own text is scanned).

Statistic: recall = share of K whose date D is within +-1 day of at least one date the scan resolves.

Null (date-shuffled): each held-out D replaced by D + o, o uniform integer in [-90, -7] u [7, 90] days, seed 0, 1000
draws; recall computed against the SAME resolved reference dates. Why the null can fail differently: the statistic is
a date coincidence between the scan's resolved dates and K's dates; the null moves K's dates and leaves the scan output
unchanged, so it can only score by chance density of resolved dates, while the known answer scores when the scan
actually reads the reply's back-reference -- order, coverage or key are not involved.

Ceiling check: if the null mean is >= 0.95 or the real recall is reached by the null p95, the gate fails as no headroom.

## Expected and gate

Expected (guess, OCR of 1907 print, many references without a resolvable date): recall 0.30-0.50, null mean <= 0.10.

Gate (all three): recall >= 0.25; recall > null p95; recall - null mean >= 0.15.
PASS -> shelf grade `controlled-only` (leads only, never a held/referenced decision without a person or verifier
reading the edition). Miss -> shipped `weak` with both numbers; nothing run on a target from it; not re-briefed.

The register itself (held/referenced classes, timeline, duplicate check) has offline tests only: plumbing.

## Result (9 Oct 2026, 10:17 and 10:18 UTC by date -u)

`python3 tools/tests/mqs_pile_register_control.py` (header parser fixed for OCR month tails and blank lines BEFORE
the first scan: 62 -> 87 dated letters; no recall had been computed at that point).

| run | G | K | references resolved | recall | null mean | null p95 | gate |
|---|---|---|---|---|---|---|---|
| 1 (10:17) | 87 | 9 | 32 | 0.111 (1/9) | 0.060 | 0.222 | FAIL |
| 2 (10:18, after a bug fix) | 87 | 9 | 33 | 0.111 (1/9) | 0.064 | 0.222 | FAIL |

Run 2 follows a code defect found by the offline tests, not a tuning: the reference regex's trailing context was a
consuming group, so a second reference inside the first one's 48-character context ('your letter of Oct. 20 and my
letter of Dec 31') was skipped; it is now a lookahead. Same gate, same seed; the number did not move.

Why it misses (diagnostic, read after the gate): the one hit is Armstrong 25 Oct 1806, named in Bowdoin's 29 Oct reply
('your letters of the 25th instant'). Of the other eight, the reply names a different letter (Shepard's 19 Jan, not
printed: a true referenced-but-missing letter the ground truth cannot score), names a range ('from the 18 of June to the
31 of ...'), or opens with no back-reference. K defined by 'a reply exists' over-counts the letters a reply actually
names, and K = 9 is too small for the gate to separate from the null at p95 (one hit = 0.111).

Verdict: `--refs-scan` ships shelf grade `weak` with both numbers; it yields leads only; nothing is run on a target
from it; not re-briefed. The register (held / referenced / held? / timeline / --check) is plumbing, grade n/a, offline
tests only. A better known answer would be an edition whose editor lists the letters each letter acknowledges (a
calendar with 'answers X of D' notes), scored per acknowledged letter -- a one-line suggestion, not this job.
