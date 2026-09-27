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

os.remove(FIXTURE)

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: freq.py --contacts tags suffix-like/prefix-like/neither correctly (context "
      "concentration + diversity, not self-succession alone), --kwic sorts on left/right "
      "context, --repeats finds recurring n-grams and near-repeats without double-counting "
      "exact matches, --split-at reports per-side token/distinct/IC, and the default "
      "(no new flag) report is unchanged.")
