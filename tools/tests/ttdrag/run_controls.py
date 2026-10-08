#!/usr/bin/env python3
"""TT-DRAG known-answer controls for tools/running_key.py --drag (8 Oct 2026; pre-registered in tools/tests/PREREG-TT-DRAG.md).

  python3 tools/tests/ttdrag/run_controls.py A [--seeds 8]   synthetic hessen-1824-matched control (N=164, de19, vig) + random-key null
  python3 tools/tests/ttdrag/run_controls.py B [--seeds 5]   Brown's 2026 challenge (Tomokiyo, runningkey.htm) + shuffled-order null
  python3 tools/tests/ttdrag/run_controls.py B2              B with the dictionary widened by tools/data/en18 word types

Method credit: S. Tomokiyo, runningkey.htm ("Tips"; "Running Key Challenge"/"Solution", Matthew Brown's dictionary attack).
Writes TSV summaries beside this script (controlA.tsv, controlB.tsv).
"""
import argparse, io, os, random, re, sys, contextlib, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, TOOLS)
import running_key as rk  # noqa: E402

DE19 = os.path.join(TOOLS, "data", "de19")
WORK = os.environ.get("TTDRAG_WORK", os.path.join(tempfile.gettempdir(), "ttdrag_work"))


def tokens(path):
    return [w for w in (rk.fold(t) for t in re.findall(r"[^\W\d_]+", rk.read_text(path))) if w]


def window(toks, rng, n):
    lo = len(toks) // 20
    i = rng.randrange(lo, len(toks) * 19 // 20 - n)
    s = ""
    while len(s) < n:
        s += toks[i]
        i += 1
    return s[:n]


def drag(cipher, plain, key, corpus_words, lm_books, extra=()):
    os.makedirs(WORK, exist_ok=True)
    cf, pf, kf = (os.path.join(WORK, x) for x in ("c.txt", "p.txt", "k.txt"))
    for f, t in ((cf, cipher), (pf, plain), (kf, key)):
        open(f, "w").write(t + "\n")
    argv = [cf, "--drag", "10", "--corpus", corpus_words, "--pcorpus", *lm_books, "--all-tabulae", "--top", "20",
            "--truth", pf, kf, *extra]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        res = rk.main(argv)
    out = buf.getvalue()
    rows = res["rows"]
    h10 = sum(r["true"] == "yes" for r in rows[:10])
    h20 = sum(r["true"] == "yes" for r in rows[:20])
    first = next((i + 1 for i, r in enumerate(rows) if r["true"] == "yes"), None)
    return h10, h20, first, out


def control_a(seeds):
    books = rk.list_books([DE19])
    toks = {b: tokens(b) for b in books}
    words = os.path.join(WORK, "de19_words10.txt")
    os.makedirs(WORK, exist_ok=True)
    open(words, "w").write("\n".join(rk.drag_words([DE19], 10)) + "\n")
    lines = ["seed\tplain_book\tkey_book\tarm\thits@10\thits@20\tfirst_true_rank\ttop1"]
    for seed in range(1, seeds + 1):
        rng = random.Random(seed)
        pb, kb = rng.sample(books, 2)
        P, K = window(toks[pb], rng, 164), window(toks[kb], rng, 164)
        R = "".join(rng.choice(rk.A) for _ in range(164))
        lm = [b for b in books if b not in (pb, kb)]
        for arm, key in (("control", K), ("null_randomkey", R)):
            C = "".join(rk.A[rk.encipher("vig", rk.IDX[a], rk.IDX[b])] for a, b in zip(P, key))
            h10, h20, first, out = drag(C, P, key, words, lm)
            top1 = [l for l in out.splitlines() if l.startswith("1\t")][0].replace("\t", " ")
            lines.append(f"{seed}\t{os.path.basename(pb)}\t{os.path.basename(kb)}\t{arm}\t{h10}\t{h20}\t{first}\t{top1}")
            print(lines[-1], flush=True)
    return lines


def brown():
    """ciphertext and Brown's 207-letter partial plaintext/key from sources/cryptiana/web/runningkey.htm (read only)."""
    t = open(os.path.join(TOOLS, "..", "sources", "cryptiana", "web", "runningkey.htm"), encoding="utf-8", errors="replace").read()
    t = re.sub(r"<[^>]+>", " ", t)
    C = max(re.findall(r"[a-z]{900,}", t), key=len)
    P = re.search(r"ERRORCORRECTING[A-Z]+", t).group(0).lower()
    K = re.search(r"SINTHESPIRIT[A-Z]+", t).group(0).lower()
    for at in range(len(C) - len(P) + 1):
        if all(rk.encipher("vig", rk.IDX[p], rk.IDX[k]) == rk.IDX[c] for p, k, c in zip(P, K, C[at:])):
            return C, P, K, at
    sys.exit("Brown window not found in the ciphertext under vig")


def control_b(seeds, tag="B"):
    C, P, K, at = brown()
    en = [os.path.join(TOOLS, "data", "pg1661_holmes.txt"), os.path.join(TOOLS, "data", "pg2701_mobydick.txt"),
          os.path.join(TOOLS, "data", "en")]
    words = os.path.join(WORK, f"en_words10_{tag}.txt")
    os.makedirs(WORK, exist_ok=True)
    dsrc = en + ([os.path.join(TOOLS, "data", "en18")] if tag == "B2" else [])
    open(words, "w").write("\n".join(rk.drag_words(dsrc, 10)) + "\n")
    lines = [f"# {tag}: dictionary {sum(1 for _ in open(words))} types",
             f"# Brown challenge: N={len(C)}, truth window {len(P)} letters at offset {at} (vig)",
             "arm\tseed\thits@10\thits@20\tfirst_true_rank"]
    h10, h20, first, out = drag(C, P, K, words, en, ("--truth-at", str(at)))
    open(os.path.join(HERE, f"control{tag}_target_top20.tsv"), "w").write(out)
    lines.append(f"brown\t-\t{h10}\t{h20}\t{first}")
    print(lines[-1], flush=True)
    for seed in range(1, seeds + 1):
        s = list(C)
        random.Random(seed).shuffle(s)
        h10, h20, first, _ = drag("".join(s), P, K, words, en, ("--truth-at", str(at)))
        lines.append(f"null_shuffled\t{seed}\t{h10}\t{h20}\t{first}")
        print(lines[-1], flush=True)
    return lines


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("which", choices=["A", "B", "B2"])
    ap.add_argument("--seeds", type=int, default=None)
    a = ap.parse_args()
    lines = control_a(a.seeds or 8) if a.which == "A" else control_b(a.seeds or 5, a.which)
    open(os.path.join(HERE, f"control{a.which}.tsv"), "w").write("\n".join(lines) + "\n")
