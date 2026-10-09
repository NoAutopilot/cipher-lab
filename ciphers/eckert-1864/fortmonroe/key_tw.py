#!/usr/bin/env python3
"""KEY-TW (9 Oct 2026): test two candidate Cipher No. 1 key rows at every filed occurrence in ciphertext.txt.

Candidates (not in key.md): Tulip = stop (key.md has Tulip = Open; CONF-FM) and whiskey = Troops (key.md has
Whisky = Troops; the spelling "whiskey" is carried by per-entry `variant:` notes at grade M; FV-FM8a).

For every occurrence the entry is decoded by decode.py as filed (notes applied) and a window of the reading is
printed with the candidate token rendered both ways: with the candidate value and with the key.md value (or as
written). Two controls:
  1. Boundary statistic (Tulip = stop only, mechanical): the share of occurrences followed by a clause start
     (a capitalised word, a word in STARTERS fixed before the run, or the end of the message text). Positive
     control: the same share for every occurrence of the No. 1 period words (Unity, Zebra, Zodiac). Null: the
     same share over N random occurrences of non-punctuation key words, 2000 draws.
  2. Blind context read (both candidates): the candidate's windows are mixed with an equal number of windows in
     which a randomly drawn key-word occurrence is given the same value, shuffled under a fixed seed and printed
     with ids hidden (--blind). The reader marks each R (reads) or N; --unmask prints which id was which.
     Judgements are stored in key_tw_judgements.tsv; the summary counts reads for candidate vs control.

Usage: python3 key_tw.py            # occurrences, boundary statistic
       python3 key_tw.py --blind    # the mixed shuffled windows, ids hidden
       python3 key_tw.py --unmask   # score key_tw_judgements.tsv against the hidden ids
"""
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import decode  # noqa: E402

STARTERS = {"i", "we", "you", "he", "they", "it", "there", "the", "shall", "will", "your", "my", "our", "have",
            "please", "send", "if", "all", "no", "is", "has", "can", "do", "a", "this", "that", "unless", "when"}
CANDIDATES = {"tulip": "stop", "whiskey": "Troops"}
PERIOD_WORDS = {"unity", "zebra", "zodiac"}
SEED = 20261009


def occurrences(key, blocks):
    """Yield (entry header, index, word list, readings list) for every token in No. 1 entries."""
    for header, lines in blocks:
        text = decode.entry_text(lines)
        words = text.split(" ")
        yield header, words


def bare(w):
    """The token as written, without decode.py's note marks (trailing backslash, ~=~ / ~ suffixes)."""
    return w.split("~")[0].rstrip("\\")


def core(w):
    return re.sub(r"[^a-z]", "", bare(w).lower())


def strip_end(c):
    for e in ("ing", "ed", "s"):
        if c.endswith(e) and len(c) > len(e) + 2:
            return c[: -len(e)]
    return c


def window(words, i, value, k=6):
    lo, hi = max(0, i - k), min(len(words), i + k + 1)
    left = " ".join(bare(w) for w in words[lo:i] if w != "|")
    right = " ".join(bare(w) for w in words[i + 1:hi] if w != "|")
    return f"... {left} [{value}] {right} ..."


def body_end(words, key):
    """Index of the signature marker (end of message text) or len(words)."""
    for j, w in enumerate(words):
        c = core(w)
        if c in key and key[c][2] == "sig":
            return j
    return len(words)


def clause_start(words, i, key):
    if i + 1 >= len(words):
        return True
    nxt = bare(words[i + 1])
    c = core(nxt)
    if c in key and key[c][2] in ("punct", "sig"):
        return True
    return nxt[:1].isupper() or c in STARTERS


def main(argv):
    key = decode.load_key()
    blocks = decode.load_ciphertext()
    rng = random.Random(SEED)
    cand = {c: [] for c in CANDIDATES}
    period, pool = [], []
    for header, words in occurrences(key, blocks):
        for i, w in enumerate(words):  # whole entry: several entries hold two or three telegrams
            c = core(w)
            if not c:
                continue
            if c in CANDIDATES:
                cand[c].append((header, words, i))
            elif w.endswith("\\") or "~" in w:
                continue
            elif c in PERIOD_WORDS:
                period.append((header, words, i))
            else:
                s = c if c in key else strip_end(c)
                if s in key and key[s][2] == "word":
                    pool.append((header, words, i))
    if "--blind" in argv or "--unmask" in argv:
        items = []
        for c, val in CANDIDATES.items():
            ctl = rng.sample(pool, len(cand[c]))
            items += [(c, "cand", h, ws, i, val) for h, ws, i in cand[c]]
            items += [(c, "ctl", h, ws, i, val) for h, ws, i in ctl]
        rng.shuffle(items)
        if "--blind" in argv:
            for n, (c, kind, h, ws, i, val) in enumerate(items):
                print(f"{n:02d}\t{val}\t{window(ws, i, val)}")
            return 0
        judg = {}
        for line in (HERE / "key_tw_judgements.tsv").read_text().splitlines():
            if line and not line.startswith("#"):
                n, mark = line.split("\t")[:2]
                judg[int(n)] = mark.strip()
        for c in CANDIDATES:
            for kind in ("cand", "ctl"):
                rows = [(n, it) for n, it in enumerate(items) if it[0] == c and it[1] == kind]
                r = sum(judg.get(n) == "R" for n, _ in rows)
                print(f"{c}={CANDIDATES[c]}\t{kind}\treads {r} of {len(rows)}\tids " +
                      ",".join(f"{n}{judg.get(n, '?')}" for n, _ in rows))
        return 0
    for c, val in CANDIDATES.items():
        kv = key.get(c, key.get("whisky") if c == "whiskey" else None)
        print(f"## {c} = {val} (key.md: {kv[0] if kv else 'none'}); {len(cand[c])} occurrences")
        for h, ws, i in cand[c]:
            print(f"{h[:60]}\t{window(ws, i, val)}\tkey: [{kv[0] if kv else ws[i]}]")
    def share(occ):
        return sum(clause_start(ws, i, key) for _, ws, i in occ) / len(occ)
    n = len(cand["tulip"])
    t = share(cand["tulip"])
    p = share(period)
    null = sorted(share(rng.sample(pool, n)) for _ in range(2000))
    p95 = null[int(0.95 * len(null))]
    mean = sum(null) / len(null)
    ge = sum(x >= t for x in null) / len(null)
    print(f"\nboundary share: tulip {t:.3f} (n={n}); period words {p:.3f} (n={len(period)}); "
          f"null mean {mean:.3f}, p95 {p95:.3f} (n={n}, 2000 draws, pool {len(pool)}); P(null >= tulip) {ge:.3f}")
    print(f"whiskey boundary share (for comparison): {share(cand['whiskey']):.3f} (n={len(cand['whiskey'])})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
