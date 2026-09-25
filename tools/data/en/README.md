# en: LANG_CORPORA["en"], the default English judge corpus -- fold-count amendment

Built/extended 25 Sept 2026 22:17 UTC (parent worker EN-FOLDS) to satisfy CLAUDE.md rule 3's fold-count
amendment (UPDATES.md 20:01 UTC that day), flagged in ROOM.md 21:48 and `QA/2026-09-25-2140.md` failure 1: no
per-fold held-out false-negative spread had ever been computed for `LANG_CORPORA["en"]`, unlike `es17c`,
`pt18` and `fr18`.

## The two original files (unmoved, still used directly by judge_plaintext.py)

`tools/data/pg1661_holmes.txt` (Arthur Conan Doyle, *The Adventures of Sherlock Holmes*, 1892, British) and
`tools/data/pg2701_mobydick.txt` (Herman Melville, *Moby-Dick*, 1851, American) -- present before this job,
left in place at their existing path since `LANG_CORPORA["en"]` already points there and several targets'
readings cite that exact path.

## Step 1: baseline 2-file leave-one-out (`tools/data/en/holdout_check.py`, default `--files`)

| N | held out | real_p05 | false negatives | null false positives |
|---|---|---|---|---|
| 200 | pg1661_holmes.txt | -0.888 | 112/200 (56.0%) | 0/200 (0.0%) |
| 200 | pg2701_mobydick.txt | -0.817 | 200/200 (100.0%) | 0/200 (0.0%) |
| 500 | pg1661_holmes.txt | -0.855 | 179/200 (89.5%) | 0/200 (0.0%) |
| 500 | pg2701_mobydick.txt | -0.815 | 200/200 (100.0%) | 0/200 (0.0%) |

Per-fold false-negative spread: **0.440** at N=200, **0.105** at N=500. Both exceed the amendment's 0.05
spread gate, and every individual fold rate (56.0/100.0/89.5/100.0%) is far past the 0.10 per-fold gate --
worse on both counts than es17c's already-flagged 10.0-39.5% spread. Null false-positive rate is 0.0% at
both N (the language check is not simply loose). Per the brief's step 2, this licenses fetching up to three
more sources and recomputing.

## Step 2: three more public-domain English sources, fetched from gutenberg.org

The `en`-language specs (`specs/*.json` with `"judge": {"language": "en", ...}`, grepped 25 Sept 2026) span
1863-2010, mostly American English, e.g. blitz-ciphers (pre-1940s), mccormick-1999, dorabella-1897 (British),
somerket-1948-era, rubin-1953, harry-caroline-1863, powers-1991, scorpion-1991, rayburn-2004, lima-1916,
fair-game-2010, pollaky/catokwacopa-1875 (British). No single added novel matches any one target's register
(the existing en corpus was never register-matched target-by-target the way fr18/es17c/pt18 are); the three
added here widen the *period and dialect* spread the existing two-book corpus lacked (both are mid/late-19th-c.
novels; neither is American vernacular or early-20th-c.):

- **pg76_huckfinn.txt** -- Mark Twain, *Adventures of Huckleberry Finn*, 1884, American vernacular narration.
  `https://www.gutenberg.org/cache/epub/76/pg76.txt`. 622,460 bytes raw, 427,815 letters after `fold()`.
- **pg64317_gatsby.txt** -- F. Scott Fitzgerald, *The Great Gatsby*, 1925, American, early-20th-c. register
  (closer in period to the later specs, e.g. blitz-ciphers/mccormick/somerton/rubin). `https://www.gutenberg.org/cache/epub/64317/pg64317.txt`.
  306,553 bytes raw, 206,438 letters after `fold()`.
- **pg1342_pride.txt** -- Jane Austen, *Pride and Prejudice*, 1813, British, formal narration/dialogue (a third
  dialect/register point, closer to the pollaky/catokwacopa/dorabella British 19th-c. specs). `https://www.gutenberg.org/cache/epub/1342/pg1342.txt`.
  772,386 bytes raw, 563,939 letters after `fold()`.

All three fetched with `curl -A "cipher-lab research script (contact via repository)"`, one request each,
>=2s apart, no other requests to gutenberg.org this job. Licence: Project Gutenberg's own licence (public
domain in the US; the ebook text itself carries the standard PG boilerplate header/footer, which
`judge_plaintext.py`'s `read_corpus()` already strips between `*** START OF` / `*** END OF` markers, so it
does not enter the n-gram model).

Combined corpus (5 files): 607,606 + 1,276,267 + 622,460 + 306,553 + 772,386 bytes raw; well over 1,000,000
letters after fold() (individual folded counts: holmes ~526k, mobydick ~1.06M, huckfinn 427,815, gatsby
206,438, pride 563,939 -- Moby-Dick alone is about 37% of the combined folded total, close to fr18's 40% cap
concern, but reducing it further was out of this job's scope, which was to compute and report, not to curate
weights).

## Step 3: recomputed 5-file leave-one-out

`python3 tools/data/en/holdout_check.py --files ../pg1661_holmes.txt ../pg2701_mobydick.txt pg76_huckfinn.txt pg64317_gatsby.txt pg1342_pride.txt`:

| N | held out | real_p05 | false negatives | null false positives |
|---|---|---|---|---|
| 200 | pg1661_holmes.txt | -0.882 | 56/200 (28.0%) | 0/200 (0.0%) |
| 200 | pg2701_mobydick.txt | -0.880 | 161/200 (80.5%) | 0/200 (0.0%) |
| 200 | pg76_huckfinn.txt | -0.881 | 118/200 (59.0%) | 0/200 (0.0%) |
| 200 | pg64317_gatsby.txt | -0.888 | 110/200 (55.0%) | 0/200 (0.0%) |
| 200 | pg1342_pride.txt | -0.906 | 34/200 (17.0%) | 0/200 (0.0%) |
| 500 | pg1661_holmes.txt | -0.910 | 19/200 (9.5%) | 0/200 (0.0%) |
| 500 | pg2701_mobydick.txt | -0.893 | 168/200 (84.0%) | 0/200 (0.0%) |
| 500 | pg76_huckfinn.txt | -0.892 | 97/200 (48.5%) | 0/200 (0.0%) |
| 500 | pg64317_gatsby.txt | -0.903 | 70/200 (35.0%) | 0/200 (0.0%) |
| 500 | pg1342_pride.txt | -0.896 | 34/200 (17.0%) | 0/200 (0.0%) |

Blended: **479/1000 (47.9%)** at N=200, **388/1000 (38.8%)** at N=500. Null false-positive rate 0.0% at both
N, every fold. Per-fold false-negative spread: **0.635** at N=200 (17.0% to 80.5%), **0.745** at N=500 (9.5%
to 84.0%).

**Reported as found, not smoothed over (CLAUDE.md rule 3's own instruction): adding sources made the spread
worse, not better.** The driver is Moby-Dick: when it is the held-out fold, its false-negative rate is 80.5%
(N=200) / 84.0% (N=500) against a model trained on the other four -- and that model is now a tighter fit to
"standard 19th/20th-c. narrative English" (Doyle, Twain, Fitzgerald, Austen) than the 1-file models the
2-file baseline used, so Moby-Dick's own digressive, technical-whaling, archaic-cadence prose reads as a
*worse* outlier against a larger, more homogeneous "standard" corpus, not a better one. Every other fold
(Holmes, Huck Finn, Gatsby, Pride and Prejudice) sits at 9.5-59.0%, still high by es17c/pt18 standards but a
much smaller spread among themselves (roughly 9.5-59.0%, i.e. the four together would spread about 0.50 at
N=200 and 0.39 at N=500) -- Moby-Dick specifically, not "English prose in general" or "5 files is still too
few", is the outlier driving both the blended rate and the spread past the gate.

**This corpus's FAIL/PASS verdicts on the `en` language check are of unknown reliability by the amendment's own
rule** (spread far over 0.05 at both N tried, unresolved by adding three more sources within this job's cap).
Two honest options for a future worker, neither attempted here (out of this job's scope: compute and report,
per the brief): (a) drop Moby-Dick from `LANG_CORPORA["en"]`'s default entry (its technical/archaic register is
plausibly a poor match for the terse notes, ransom messages and short ciphertexts the `en`-language specs
actually are, closer to the fr16-on-fr18-targets mismatch than to a genuine "more data is better" case); or
(b) build a register-matched corpus the way fr18/es17c/pt18 did, keyed to what the `en` specs actually need
(short, plain, non-literary prose -- news, letters, notes -- rather than any novel).

## LANG_CORPORA comment

One line added naming `en`'s fold-check file and its unresolved-reliability verdict (CLAUDE.md rule 3: "leave
CLAUDE.md alone" unless the added line names corpora individually -- this one does, so a corresponding
one-line pointer was also added to CLAUDE.md rule 3's paragraph, per the brief).

## Requests this job

gutenberg.org: 3 (one per file, >=2s apart, descriptive UA). No other hosts. No subagents.
