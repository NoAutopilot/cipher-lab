#!/usr/bin/env python3
"""LIKELY-1 (2 Oct 2026): apply keys/key_vieuville_nevers.tsv to a reconciled transcription of a leaf and score the
decoded cipher runs by French word-cover against N letter-shuffled keys (CLAUDE.md rule 3: control first).

    python3 scripts/keytest.py known-answer            # the scorer on no.58's Tomokiyo dump stream (a leaf the key is
                                                       # known to read): must separate the real key from shuffles
    python3 scripts/keytest.py target ciphertext.tsv   # the same scorer on this leaf's reconciled transcription
    python3 scripts/keytest.py target ciphertext.tsv --shuffles 200 --dump-decode out.txt

Scorer (same statistic as fr4715-montholon-1589/scripts/mont4715c.py u3cover, re-implemented here so this folder
needs no sibling import): every maximal run of consecutive cipher tokens that decode under the key is one segment;
a dotted word-code (leading apostrophe), a clear word (w:word), an out-of-key token or an illegible token breaks the
run. Word-cover = letters of the decoded segments covered by a greedy longest-word segmentation into tools/data/fr16
words (3-14 letters, corpus frequency >= 3). Control: the key's letter values permuted among its letter rows (same
homophone structure, same code inventory), N seeds, mean/sd/max; z = (real - mean)/sd and rank among N+1.
Disk only; no network.
"""
import argparse
import csv
import glob
import gzip
import os
import random
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("CIPHERLAB_ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
KEY = os.path.join(ROOT, "ciphers", "fr4715-montholon-1589", "keys", "key_vieuville_nevers.tsv")
DUMP = os.path.join(ROOT, "ciphers", "fr4715-montholon-1589", "witness", "aligned_dump_codes.txt")
FR16 = os.path.join(ROOT, "tools", "data", "fr16", "*.txt.gz")


def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn")
    return w.replace("j", "i").replace("v", "u")


def load_key(path=KEY):
    rows = []
    for ln in open(path, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln.strip() or ln.startswith("#"):
            continue
        c = ln.split("\t")
        if c[0] == "sign":
            continue
        rows.append({"sign": c[0], "value": c[1], "kind": c[2], "grade": c[3] if len(c) > 3 else "H"})
    return rows


def wordlist(minfreq=3, minlen=3, maxlen=14):
    cnt = {}
    for p in sorted(glob.glob(FR16)):
        txt = gzip.open(p, "rt", encoding="utf-8", errors="ignore").read().lower()
        for w in re.findall(r"[a-zà-ÿ]+", txt):
            w = norm(w)
            if minlen <= len(w) <= maxlen:
                cnt[w] = cnt.get(w, 0) + 1
    return {w for w, n in cnt.items() if n >= minfreq}


def cover(segments, words, maxlen=14):
    covered = total = 0
    for seg in segments:
        n = len(seg)
        total += n
        best = [0] * (n + 1)
        for i in range(1, n + 1):
            best[i] = best[i - 1]
            for L in range(3, min(maxlen, i) + 1):
                if seg[i - L:i] in words:
                    best[i] = max(best[i], best[i - L] + L)
        covered += best[n]
    return covered, total


def segments(tokens, valmap):
    """tokens: list of cipher tokens in reading order; None breaks a run (clear word, illegible, dotted code)."""
    segs, cur = [], ""
    for t in tokens:
        v = valmap.get(t) if t is not None else None
        if v is None:
            if cur:
                segs.append(cur)
            cur = ""
        else:
            cur += norm(v)
    if cur:
        segs.append(cur)
    return segs


def tokens_from_dump(path=DUMP):
    toks = []
    for raw in open(path, encoding="utf-8").read().split():
        toks.append(None if raw.startswith("'") else raw)
    return toks


def tokens_from_tsv(path):
    """ciphertext.tsv: line, pos, token, conf[, note]. 'w:word' clear words, '?' or '[illegible]' break runs; a
    trailing '?' on a token is stripped (M-graded by decode_key.py, still decoded here); a leading '.' or "'" marks a
    dotted word-code (breaks the run, not decoded)."""
    toks, n_cipher, n_plain, n_dotted, n_illeg = [], 0, 0, 0, 0
    lines = [ln for ln in open(path, encoding="utf-8") if not ln.startswith("#")]
    for r in csv.DictReader(lines, delimiter="\t"):
        t = (r.get("token") or r.get("sign") or "").strip()
        if not t:
            continue
        if t.startswith("w:") or t.startswith("[PLAIN"):
            toks.append(None); n_plain += 1
        elif t in ("?", "[illegible]", "[?]"):
            toks.append(None); n_illeg += 1
        elif t[0] in ".'" or t.startswith("°"):
            toks.append(None); n_dotted += 1
        else:
            toks.append(t.rstrip("?")); n_cipher += 1
    return toks, dict(cipher=n_cipher, plain=n_plain, dotted=n_dotted, illegible=n_illeg)


def run(toks, key, words, n_shuffles, seed=1, label=""):
    real = {r["sign"]: r["value"] for r in key}
    letter_signs = [r["sign"] for r in key if r["kind"] == "letter"]
    c, t = cover(segments(toks, real), words)
    in_key = sum(1 for x in toks if x is not None and x in real)
    out_key = sorted({x for x in toks if x is not None and x not in real})
    rng = random.Random(seed)
    sh = []
    for _ in range(n_shuffles):
        vals = [real[s] for s in letter_signs]
        rng.shuffle(vals)
        vm = dict(real); vm.update(zip(letter_signs, vals))
        c2, t2 = cover(segments(toks, vm), words)
        sh.append(c2 / t2 if t2 else 0.0)
    score = c / t if t else 0.0
    m = statistics.mean(sh) if sh else float("nan")
    s = statistics.stdev(sh) if len(sh) > 1 else float("nan")
    rank = 1 + sum(1 for x in sh if x >= score)
    z = (score - m) / s if s and s == s and s > 0 else float("nan")
    print(f"[{label}] cipher tokens {sum(1 for x in toks if x is not None)}, in key {in_key}, "
          f"out of key {len(out_key)} distinct {out_key[:30]}")
    print(f"[{label}] decoded letters {t}; word-cover REAL {c}/{t} = {score:.4f}; "
          f"{n_shuffles} letter-shuffled keys: mean {m:.4f} sd {s:.4f} max {max(sh) if sh else float('nan'):.4f}; "
          f"z {z:.2f}; rank {rank} of {n_shuffles + 1}")
    if n_shuffles >= 20:
        s20 = sh[:20]
        print(f"[{label}] first 20 shuffles: mean {statistics.mean(s20):.4f} max {max(s20):.4f}; "
              f"real beats all 20: {score > max(s20)}")
    return dict(score=score, mean=m, sd=s, z=z, rank=rank, n=n_shuffles, letters=t, max=max(sh) if sh else None)


def subsampled_control(toks, key, words, k, n_windows, n_shuffles, seed):
    """Windows of k consecutive in-key groups from the dump (no dotted code inside): real-key cover vs the same
    window under n_shuffles letter-shuffled keys. Reports how often the real key wins at this N."""
    real = {r["sign"]: r["value"] for r in key}
    letter_signs = [r["sign"] for r in key if r["kind"] == "letter"]
    starts = [i for i in range(len(toks) - k + 1) if all(t is not None and t in real for t in toks[i:i + k])]
    rng = random.Random(seed)
    picks = [starts[rng.randrange(len(starts))] for _ in range(n_windows)]
    wins_all = wins_mean = 0
    reals, shm, shmax = [], [], []
    for st in picks:
        w = toks[st:st + k]
        c, t = cover(segments(w, real), words)
        r = c / t
        sh = []
        for _ in range(n_shuffles):
            vals = [real[s] for s in letter_signs]
            rng.shuffle(vals)
            vm = dict(real); vm.update(zip(letter_signs, vals))
            c2, t2 = cover(segments(w, vm), words)
            sh.append(c2 / t2)
        reals.append(r); shm.append(statistics.mean(sh)); shmax.append(max(sh))
        wins_all += r > max(sh)
        wins_mean += r > statistics.mean(sh)
    print(f"[no.58 dump, {n_windows} windows of {k} in-key groups, {n_shuffles} shuffles each] real cover mean "
          f"{statistics.mean(reals):.3f}; shuffle mean of means {statistics.mean(shm):.3f}; shuffle max mean "
          f"{statistics.mean(shmax):.3f}; real beats the shuffle mean in {wins_mean}/{n_windows} windows, beats every "
          f"shuffle (rank 1) in {wins_all}/{n_windows}; real cover == 1.0 in {sum(1 for r in reals if r >= 0.999)}/{n_windows}, "
          f"shuffle max == 1.0 in {sum(1 for m in shmax if m >= 0.999)}/{n_windows}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["known-answer", "target"])
    ap.add_argument("ciphertext", nargs="?")
    ap.add_argument("--shuffles", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--key", default=KEY)
    ap.add_argument("--dump-decode", help="write the decoded letter runs (target mode)")
    ap.add_argument("--window", type=int, help="known-answer only: subsample the control to windows of this many "
                    "consecutive in-key groups (CLAUDE.md rule 3, ARM3-ADJ: a control's power is shown at the target's own N)")
    ap.add_argument("--windows", type=int, default=200)
    a = ap.parse_args()
    key = load_key(a.key)
    words = wordlist()
    print(f"wordlist: tools/data/fr16 ({len(glob.glob(FR16))} files), words len 3-14 freq>=3: {len(words)}; "
          f"key rows {len(key)}")
    if a.mode == "known-answer":
        toks = tokens_from_dump()
        if a.window:
            subsampled_control(toks, key, words, a.window, a.windows, a.shuffles, a.seed)
            return
        run(toks, key, words, a.shuffles, a.seed, "no.58 dump, Tomokiyo's own groups, dotted word-codes break runs")
    else:
        toks, counts = tokens_from_tsv(a.ciphertext)
        print(f"tokens: {counts}")
        res = run(toks, key, words, a.shuffles, a.seed, os.path.basename(a.ciphertext))
        if a.dump_decode:
            real = {r["sign"]: r["value"] for r in key}
            with open(a.dump_decode, "w", encoding="utf-8") as f:
                f.write("\n".join(segments(toks, real)) + "\n")
        sys.exit(0 if res["rank"] == 1 else 2)


if __name__ == "__main__":
    main()
