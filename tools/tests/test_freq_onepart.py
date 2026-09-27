#!/usr/bin/env python3
"""Offline test for tools/freq.py's --onepart-dict option (DES-PART, 27 Sept 2026,
LESSONS-TOMOKIYO.md C2). Built entirely against synthetic word lists passed straight
to word_type_bands()/band_for_frac() -- no real tools/data corpus is read, so this
test has no dependency on tools/data/fr18 or judge_plaintext.py's LANG_CORPORA.

Cases covered:
- word_type_bands() counts DISTINCT folded word TYPES, not raw token occurrences (a
  word repeated many times in the text counts once toward its letter's band, per the
  berthier-napoleon-1812 NOTES.md caveat that a token-frequency count is dominated by
  function words like "je").
- accented/uppercase input folds the same way tools/judge_plaintext.py's fold() does
  (translate accents, drop everything outside a-z) before the initial letter is taken.
- bands are cumulative and cover [0,1) with no gaps, in alphabetical order.
- band_for_frac() returns the letter whose band contains a given fraction, including
  the two edges (frac=0.0 and frac just under 1.0).
- print_onepart()'s per-token mapping, exercised through freq.py's CLI on a tiny fixture
  file, reports each top token's correct frac and band for a stated range, and the
  default (no new flag) report is unaffected by this option's presence.

Run: python3 tools/tests/test_freq_onepart.py"""
import io
import contextlib
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


# a: 3 distinct types (ami, avant, autre); b: 1 (bon); d: 2 (de, dans)
# "de" repeated 5 times as a raw token in text 1, "ami" 3 times -- neither must inflate its band
TEXTS = [
    "Ami ami ami de de de de de bon avant autre",
    "Dans dans DE Ami Bon",  # repeats + uppercase forms of already-seen types, one new type (dans)
]
bands, total = freq.word_type_bands(TEXTS)
check("distinct type count is 6 (ami, de, bon, avant, autre, dans), not the raw token count",
      total == 6)

by_letter = {letter: (s, e) for letter, s, e in bands}
check("bands cover 26 letters", len(by_letter) == 26)
check("bands are contiguous and start at 0 / end at 1",
      bands[0][1] == 0.0 and bands[-1][2] == 1.0 and
      all(abs(bands[i][2] - bands[i + 1][1]) < 1e-9 for i in range(25)))
# a: ami, avant, autre = 3/6 = 0.5 -> [0, 0.5); b: bon = 1/6 -> [0.5, 0.6667);
# d: de, dans = 2/6 -> [0.6667, 1.0)
check("'a' band is [0, 0.5) (3 of 6 types, not inflated by 'de' or 'ami' token repeats)",
      abs(by_letter["a"][0] - 0.0) < 1e-6 and abs(by_letter["a"][1] - 0.5) < 1e-6)
check("'b' band is [0.5, 0.6667)", abs(by_letter["b"][0] - 0.5) < 1e-6 and abs(by_letter["b"][1] - 2 / 3) < 1e-6)
check("'d' band is [0.6667, 1.0) and case-folded 'DE' merges with lowercase 'de', not double-counted",
      abs(by_letter["d"][0] - 2 / 3) < 1e-6 and abs(by_letter["d"][1] - 1.0) < 1e-6)
check("a letter with no type in this corpus has a zero-width band",
      by_letter["z"][0] == by_letter["z"][1])

check("band_for_frac(0.0) lands in the first non-empty band ('a')", freq.band_for_frac(bands, 0.0) == "a")
check("band_for_frac just under 1.0 lands in the last non-empty band ('d')",
      freq.band_for_frac(bands, 0.999999) == "d")
check("band_for_frac(0.5) lands exactly on the a/b boundary, in 'b' (half-open [start,end))",
      freq.band_for_frac(bands, 0.5) == "b")
check("fold_word strips accents and case the same way for repeated lookups",
      freq.fold_word("À") == freq.fold_word("a") == "a")

# --- CLI: --onepart-dict wired through freq.py, bypassing corpus loading by
# monkeypatching onepart_dict_bands (the file-loading half is exercised for real by
# ciphers/destaing-gerard-1779/onepart_test.py against the actual fr18 corpus) ---
freq.onepart_dict_bands = lambda lang: (bands, total)

FIXTURE = os.path.join(ROOT, "tools", "tests", "fixtures", "freq_onepart_synth.txt")
os.makedirs(os.path.dirname(FIXTURE), exist_ok=True)
with open(FIXTURE, "w", encoding="utf-8") as f:
    f.write("10 20 10 90 10 20\n")  # 10 x3, 20 x2, 90 x1; range 10-90

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    sys.argv = ["freq.py", FIXTURE, "--onepart-dict", "fake", "--top", "3", "--onepart-range", "10,90"]
    freq.main()
out = buf.getvalue()
check("CLI prints the requested language's band table header", "onepart-dict fake: 6 distinct word types" in out)
check("CLI prints the stated range", "# range 10-90" in out)
# token 10: frac (10-10)/(90-10)=0.0 -> band a; token 20: frac (20-10)/80=0.125 -> band a;
# token 90: frac (90-10)/80=1.0 -> clamped to 0.999999 -> band d (last band)
check("token 10 (frac 0.0) mapped to band 'a'", "10\t3\t0.0000\ta" in out)
check("token 20 (frac 0.125) mapped to band 'a'", "20\t2\t0.1250\ta" in out)
check("token 90 (frac 1.0, clamped) mapped to the last band 'd'", "90\t1\t1.0000\td" in out)

buf2 = io.StringIO()
with contextlib.redirect_stdout(buf2):
    sys.argv = ["freq.py", FIXTURE]
    freq.main()
out2 = buf2.getvalue()
check("default output (no --onepart-dict) is unaffected by this option's presence",
      out2.startswith("tokens:") and "onepart-dict" not in out2)

os.remove(FIXTURE)

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: freq.py --onepart-dict counts distinct folded word TYPES (not raw token "
      "occurrences) for its initial-letter bands, bands are contiguous and cover [0,1), "
      "band_for_frac() resolves both edges correctly, and the CLI maps top tokens to the "
      "right band at a stated range without disturbing the default report.")
