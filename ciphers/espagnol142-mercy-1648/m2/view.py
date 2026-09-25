#!/usr/bin/env python3
"""LANE R6 M2 helper (25 Sept 2026): show every code run of ciphertext.tsv decoded under a key, with its plain
neighbours, and score the whole code stream on the es17 trigram model used by tools/homophonic_anneal.py.

  python3 ciphers/espagnol142-mercy-1648/m2/view.py --key KEY.json|key.tsv [--corpus-dir DIR] [--runs] [--codes 12,15]
  --runs   print each code run: codes on one line, letters aligned below, plain context in brackets
  --codes  print every occurrence of the named codes with 6 letters of decoded context either side
  --score  print the anneal-style score (trigram + unigram term) of the decode
"""
import argparse, csv, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
from homophonic_anneal import Model, score  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)


def load_key(path):
    if path.endswith(".json"):
        d = json.load(open(path))
        return d["key"] if "key" in d else d
    key = {}
    for r in csv.DictReader(open(path), delimiter="\t"):
        if r.get("code", "").startswith("#"):
            continue
        key[r["code"]] = r["letter"]
    return key


def load_ct():
    rows = list(csv.DictReader(open(os.path.join(TARGET, "ciphertext.tsv")), delimiter="\t"))
    return rows


def runs(rows):
    """Yield (plain_before, [code rows], plain_after)."""
    out, cur, plain = [], [], []
    for r in rows:
        s = r["sign"]
        if s.startswith("[PLAIN:"):
            if cur:
                out.append([plain, cur, []])
                plain = []
                cur = []
            plain.append(s[7:-1])
        else:
            cur.append(r)
    if cur:
        out.append([plain, cur, []])
    for i in range(len(out) - 1):
        out[i][2] = out[i + 1][0]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", required=True)
    ap.add_argument("--corpus-dir", default=os.environ.get("ES17_DIR", "/tmp/claude-0/-home-user-cipher-lab/46717fb3-ed69-5f35-84c3-095a99ef1f15/scratchpad"))
    ap.add_argument("--runs", action="store_true")
    ap.add_argument("--codes")
    ap.add_argument("--score", action="store_true")
    ap.add_argument("--width", type=int, default=30)
    a = ap.parse_args()
    key = load_key(a.key)
    rows = load_ct()
    codes = [r for r in rows if not r["sign"].startswith("[PLAIN:")]
    dec = "".join(key.get(r["sign"], "?") for r in codes)
    if a.runs:
        for i, (pb, cur, pa) in enumerate(runs(rows)):
            print(f"--- run {i+1}: lines {cur[0]['line']}-{cur[-1]['line']}, {len(cur)} codes")
            print("  [" + " ".join(pb[-8:]) + "]")
            for j in range(0, len(cur), a.width):
                chunk = cur[j:j + a.width]
                print("  " + " ".join(f"{r['sign'].replace('[MARK:','').rstrip(']'):>3}" for r in chunk))
                print("  " + " ".join(f"{key.get(r['sign'],'?'):>3}" for r in chunk))
            print("  [" + " ".join(pa[:8]) + "]")
    if a.codes:
        want = set(a.codes.split(","))
        for i, r in enumerate(codes):
            if r["sign"] in want:
                l = dec[max(0, i - 8):i]
                rr = dec[i + 1:i + 9]
                print(f"{r['sign']:>11} {r['line']}:{r['position']:>2}  {l:>8} [{dec[i]}] {rr:<8}  conf={r['confidence']}")
    if a.score:
        model = Model([open(os.path.join(a.corpus_dir, f)).read() for f in ("donquijote.txt", "buscon.txt")], 3)
        print(f"score {score(model, dec, 1.0):.1f}  N={len(dec)}")
    if not (a.runs or a.codes or a.score):
        print(dec)


if __name__ == "__main__":
    main()
