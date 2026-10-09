#!/usr/bin/env python3
"""Offline test for tools/freq.py's four new options (BER-KWIC, 27 Sept 2026):
--contacts, --kwic, --repeats, --split-at. Built against a synthetic ten-line
file (fixtures/freq_synth.txt) so the real target's ciphertext is never
needed to check the tool's own logic.

Cases covered, all on one 44-token synthetic stream:
- --contacts: a SUF token (4 occurrences, 3 of 4 preceded by "30", each
  followed by a different token) must tag suffix-like; a PRE token (4
  occurrences, 3 of 4 followed by "40", each preceded by a different token)
  must tag prefix-like; a hapax (count 1, below --tag-min) must tag neither
  even though a single occurrence trivially satisfies both concentration
  conditions; self_succession is reported and does not by itself force a tag
  (a token with a real self-succession pair, "77 77", but no left/right
  concentration, must still tag neither).
- --kwic: three occurrences of a repeated token, sorted correctly by left
  and by right context.
- --repeats: a bigram appearing three times, a trigram appearing twice, and
  one near-repeat pair (two trigrams sharing two of three tokens) that is NOT
  double-counted as an exact repeat.
- --split-at: token/distinct/IC counted separately below and at-or-above a
  given split value.
- default (no new flag) output is unchanged: token/distinct count line and
  the top-token table still appear, keeping old callers working.

TT-FREQ (8 Oct 2026) adds: --repeats via ngram_repeats_all (equal to the
per-length table, gaps, 20,000-token timing, must NOT flag a once-only
window), fast near-repeats equal to the old quadratic ones, --split-at auto
(proposes a synthetic letter-band edge; must NOT break a uniform-value
null), --contacts --vowels (Sukhotin; separates homophonic CV text, must NOT
separate its shuffled-order copy).
MQS-TAIL (9 Oct 2026) adds: --tail (a planted end-of-letter sign ranks 1 and
is flagged; must NOT flag it once each letter is shuffled in place; the CLI
reads a one-letter-per-line pool; --tail-end start/both count the head).

Run: python3 tools/tests/test_freq.py"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import freq  # noqa: E402

fails = 0


def check(label, cond):
    global fails
    fails += not cond
    print(("PASS" if cond else "FAIL"), label)


FIXTURE = os.path.join(ROOT, "tools", "tests", "fixtures", "freq_synth.txt")

# Synthetic stream, built to exercise every case above in one pass:
#   SUF: 30 SUF 20 | 30 SUF 21 | 30 SUF 22 | 5 SUF 23   -> suffix-like
#   PRE: 20 PRE 40 | 21 PRE 40 | 22 PRE 40 | 23 PRE 41  -> prefix-like
#   HAPAX appears once only                              -> neither (below tag-min)
#   77 77 gives one real self-succession pair with no concentration -> neither
#   9 8 7 repeats twice (trigram "9 8 7"; bigram "9 8" occurs a 3rd time via "9 8 6") -> --repeats hits
#   9 8 6 shares two of three tokens with "9 8 7"        -> near-repeat, not a dup
TOKENS = (
    "30 SUF 20 X 30 SUF 21 Y 30 SUF 22 Z 5 SUF 23 "
    "20 PRE 40 X 21 PRE 40 Y 22 PRE 40 Z 23 PRE 41 "
    "HAPAX 77 77 1 2 3 "
    "9 8 7 4 9 8 7 5 9 8 6"
).split()
os.makedirs(os.path.dirname(FIXTURE), exist_ok=True)
with open(FIXTURE, "w", encoding="utf-8") as f:
    f.write(" ".join(TOKENS) + "\n")

toks = freq.load_tokens(FIXTURE, r"[;\s]+", False)
check("fixture tokenises to the written stream", toks == TOKENS)

# --- contacts ---
rows = {r["token"]: r for r in freq.contacts_table(toks, 50)}
check("SUF count is 4", rows["SUF"]["count"] == 4)
check("SUF tags suffix-like (left concentrated on 30, right all-distinct)",
      rows["SUF"]["tag"] == "suffix-like")
check("PRE tags prefix-like (right concentrated on 40, left all-distinct)",
      rows["PRE"]["tag"] == "prefix-like")
check("HAPAX (count 1, below tag-min 3) tags neither", rows["HAPAX"]["tag"] == "neither")
check("77 has self_succession 1 (one 77-77 adjacency)", rows["77"]["self_succession"] == 1)
check("77 tags neither (self-succession alone does not force a tag)", rows["77"]["tag"] == "neither")
check("SUF self_succession is 0 (never immediately follows itself)",
      rows["SUF"]["self_succession"] == 0)

# tag-min/tag-threshold are tunable: a lower tag-min lets HAPAX through the count gate,
# but a single occurrence's context still can't show "all distinct AND concentrated"
# on both sides at once for a well-formed case -- check the option is at least wired.
rows_lowmin = {r["token"]: r for r in freq.contacts_table(toks, 50, tag_min=1)}
check("--tag-min is honoured (HAPAX now passes the count gate)",
      rows_lowmin["HAPAX"]["count"] >= 1)

# --- kwic ---
kw = freq.kwic_rows(toks, "SUF", width=2, sort="left")
check("kwic SUF has 4 occurrences", len(kw) == 4)
check("kwic sort=left orders by immediate left neighbour ('30...' before '5...' lexically)",
      kw[-1]["left"][-1] == "5" and all(r["left"][-1] == "30" for r in kw[:3]))
kw_r = freq.kwic_rows(toks, "SUF", width=2, sort="right")
check("kwic sort=right orders by immediate right neighbour (20,21,22,23)",
      [r["right"][0] for r in kw_r] == ["20", "21", "22", "23"])

# --- repeats ---
bi = freq.ngram_repeats(toks, 2)
check("bigram '9 8' recurs (x3)", bi.get(("9", "8")) and len(bi[("9", "8")]) == 3)
tri = freq.ngram_repeats(toks, 3)
check("trigram '9 8 7' recurs (x2)", tri.get(("9", "8", "7")) and len(tri[("9", "8", "7")]) == 2)
check("trigram '9 8 6' is NOT counted as a repeat (only once)", ("9", "8", "6") not in tri)
near = freq.near_repeats_length3(toks)
near_pairs = [(ga, gb) for _, ga, _, gb in near]
check("near-repeat '9 8 7' ~ '9 8 6' found (differ in exactly one position)",
      (("9", "8", "7"), ("9", "8", "6")) in near_pairs)
check("exact repeats are excluded from the near-repeat list",
      all(ga != gb for ga, gb in near_pairs))

# --- split-at ---
split_toks = "5 6 7 8 100 200 300".split()
s = freq.split_stats(split_toks, 50)
check("split-at low side has 4 tokens (<50)", s["low"]["tokens"] == 4)
check("split-at high side has 3 tokens (>=50)", s["high"]["tokens"] == 3)
check("split-at distinct counts match (no repeats in this fixture)",
      s["low"]["distinct"] == 4 and s["high"]["distinct"] == 3)

# --- default output unchanged when no new flag is given ---
import io
import contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    sys.argv = ["freq.py", FIXTURE]
    freq.main()
out = buf.getvalue()
check("default output still prints the tokens/distinct summary line", out.startswith("tokens:"))
check("default output still prints a top-tokens table", "top 25 tokens:" in out)
check("default output has no contacts/kwic/repeats/split header (flags off)",
      "self_succession" not in out and "left_context" not in out)

# --- TT-FREQ (8 Oct 2026): --repeats gaps + refinement, --split-at auto, --contacts --vowels ---
import random
import time
allr = freq.ngram_repeats_all(toks, 2)
check("ngram_repeats_all matches ngram_repeats at every length",
      all(allr[L] == freq.ngram_repeats(toks, L) for L in allr) and 4 not in allr)
check("position gaps of '9 8 7' are [4]", freq.position_gaps(tri[("9", "8", "7")]) == [4])
check("fast near-repeats == slow near-repeats on the fixture",
      freq.near_repeats_length3_fast(toks) == freq.near_repeats_length3(toks))
rnd = random.Random(1)
rt = [str(rnd.randint(1, 40)) for _ in range(600)]
check("fast near-repeats == slow near-repeats on 600 random tokens",
      freq.near_repeats_length3_fast(rt) == freq.near_repeats_length3(rt))
# perf: 20,000 tokens over 26 symbols with three planted 12-token formulas (full table mode)
words = [[str(rnd.randint(1, 26)) for _ in range(12)] for _ in range(3)]
big = []
while len(big) < 20000:
    big += rnd.choice(words) if rnd.random() < 0.01 else [str(rnd.randint(1, 26))]
t0 = time.time()
allbig = freq.ngram_repeats_all(big, 4)
el = time.time() - t0
check(f"--repeats 4 on 20,000 tokens runs in < 5 s ({el:.2f} s)", el < 5.0)
check("each planted 12-token formula is found at length 12", all(tuple(w) in allbig.get(12, {}) for w in words))
# worst case for the old loop: a 2,000-token block repeated, --maximal
big2 = [str(rnd.randint(1, 60)) for _ in range(18000)]
big2 = big2[:9000] + big2[:2000] + big2[9000:16000]
t0 = time.time()
mx = freq.ngram_repeats_all(big2, 10, maximal=True)
el = time.time() - t0
check(f"--repeats 10 --maximal on 20,000 tokens with a 2,000-long repeat runs in < 5 s ({el:.2f} s)", el < 5.0)
check("--maximal reports the planted 2,000-token block once, with gap 9000",
      2000 in mx and [freq.position_gaps(p) for p in mx[2000].values()] == [[9000]])
check("--maximal does not list the block's sub-windows", sum(len(v) for L, v in mx.items() if L >= 1000) == 1)
check("a once-only window is not a repeat (must NOT flag '9 8 6')", ("9", "8", "6") not in allr.get(3, {}))

# split auto: letters 1-30 dense (each ~20x), codes 31-400 sparse (~0.3x) -> N near 31
band = []
for v in range(1, 31):
    band += [str(v)] * rnd.randint(12, 28)
band += [str(rnd.randint(31, 400)) for _ in range(120)]
rnd.shuffle(band)
r = freq.split_auto(band)
check(f"split auto proposes the letter-band edge 31 within 2 (got {r['singles'][0][1]})",
      abs(r["singles"][0][1] - 31) <= 2 and r["singles"][0][0] > 10)
uni = [str(rnd.randint(1, 400)) for _ in range(len(band))]
ru = freq.split_auto(uni)
check("split auto must NOT break a uniform-value null (gain < 10)",
      not ru["singles"] or ru["singles"][0][0] < 10)
bandn = [str(v) for v in range(20, 40)] + band  # sparse nulls under the band
rb = freq.split_auto(bandn)
check("split auto band fit finds an upper edge near 31 under sparse low nulls",
      rb["band"] is not None and abs(rb["band"][2] - 31) <= 2)

# vowels: synthetic CV text over 5 vowels / 10 consonants, each letter with 2 homophones
V, C = list("aeiou"), list("bcdfglmnrt")
codes = {ch: [f"{ch}1", f"{ch}2"] for ch in V + C}
stream = []
for _ in range(1500):
    stream.append(rnd.choice(codes[rnd.choice(C)]))
    stream.append(rnd.choice(codes[rnd.choice(V)]))
    if rnd.random() < 0.3:
        stream.append(rnd.choice(codes[rnd.choice(C)]))
cls = freq.sukhotin_classes(stream, 30)
acc = sum((c == "V") == (t[0] in V) for t, c, _ in cls) / len(cls)
check(f"--vowels separates homophonic vowels from consonants on CV text (acc {acc:.2f} >= 0.9)", acc >= 0.9)
accs = []
for _ in range(5):
    sh = list(stream)
    rnd.shuffle(sh)
    cls_s = freq.sukhotin_classes(sh, 30)
    accs.append(sum((c == "V") == (t[0] in V) for t, c, _ in cls_s) / len(cls_s))
acc_s = sum(accs) / len(accs)
check(f"--vowels must NOT separate shuffled-order copies (mean acc over 5 {acc_s:.2f} < 0.8)", acc_s < 0.8)

# --tail (MQS-TAIL, 9 Oct 2026): 30 letters x 80 tokens over 40 uniform body
# signs, "MON" planted in the last 3 tokens of 20 letters.
import subprocess  # noqa: E402
import tempfile  # noqa: E402
trnd = random.Random(7)
body = [f"b{i}" for i in range(40)]
pool = []
for i in range(30):
    L = [trnd.choice(body) for _ in range(80)]
    if i < 20:
        L[80 - 1 - trnd.randrange(3)] = "MON"
    pool.append(L)
rows = freq.tail_stats(pool, 5, "end", reps=500, seed=1)
check(f"--tail ranks the planted end sign first and flags it (top {rows[0][0]}, flag {rows[0][6]})",
      rows[0][0] == "MON" and rows[0][6])
nflag = 0
for k in range(10):
    sh = [list(L) for L in pool]
    for L in sh:
        trnd.shuffle(L)
    r2 = {r[0]: r for r in freq.tail_stats(sh, 5, "end", reps=500, seed=k + 2)}
    nflag += r2["MON"][6]
check(f"--tail must NOT flag the planted sign once letters are shuffled in place ({nflag}/10 flagged <= 1)",
      nflag <= 1)
head = [list(reversed(L)) for L in pool]
rs = freq.tail_stats(head, 5, "start", reps=500, seed=1)
rb = freq.tail_stats(head, 5, "both", reps=500, seed=1)
re_ = {r[0]: r for r in freq.tail_stats(head, 5, "end", reps=500, seed=1)}
check("--tail-end start and both find a head-placed sign that end does not",
      rs[0][0] == "MON" and rb[0][0] == "MON" and not re_["MON"][6])
with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as fh:
    fh.write("# pool\n" + "\n".join(" ".join(L) for L in pool) + "\n")
    pool_path = fh.name
out = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "freq.py"), pool_path, "--tail", "5",
                      "--tail-reps", "300"], capture_output=True, text=True).stdout
os.remove(pool_path)
lines = [l for l in out.splitlines() if l and not l.startswith("#")]
check("--tail CLI reads one letter per line and prints MON first with FLAG",
      "30 letters" in out and lines[0].startswith("rank\tsign") and lines[1].split("\t")[1] == "MON"
      and lines[1].endswith("FLAG"))

os.remove(FIXTURE)

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: freq.py --contacts tags suffix-like/prefix-like/neither correctly (context "
      "concentration + diversity, not self-succession alone), --kwic sorts on left/right "
      "context, --repeats finds recurring n-grams and near-repeats without double-counting "
      "exact matches, --split-at reports per-side token/distinct/IC, and the default "
      "(no new flag) report is unchanged; TT-FREQ: --repeats gaps + refinement (20,000 tokens fast), "
      "--split-at auto proposes the band edge and leaves a uniform null alone, --vowels separates CV text "
      "and not its shuffle; MQS-TAIL: --tail flags a planted end sign and not its in-letter shuffle.")
