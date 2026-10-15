"""ncbe_null.py -- MCC-JUDGE (LANE DEFAULT-A1-0740-15, 15 Oct 2026): NCBE-stem-keeping null for the MCC-SUFX candidate,
plus the renderings fed to tools/judge_plaintext.py. PREREG: ciphers/mccormick-1999/PREREG-MCC-JUDGE.md.

Null 'ncbe': as MCC-SUFX's type-mark null (token_anneal.shuffle_types keep_marks=True: letters of the distinct code types
permuted across types, each type keeps its length and its final mark SE/BE/E, repeated types stay repeated), except that
every occurrence of the letter string NCBE inside a type is also held in place (NCBE x11 and the 7 NCBE spans inside
run-on types are never shuffled); only the remaining letters are permuted. Null 'tm' re-runs MCC-SUFX's own type-mark null
at the same draw count on the same machine, for the share-of-margin figure. The class -> mark map is re-fitted on every
draw (token_anneal.fit_marks, MCC-SUFX's instrument unchanged).

Usage: python3 ncbe_null.py --draws 200 --procs 4 --out ncbe_null.json
       python3 ncbe_null.py --lexicon ../gregg/gregg1916_lexicon.txt --kinds ncbe --draws 200 --out ... (MCC-GREGG)
       python3 ncbe_null.py --selftest
"""
import argparse, json, random, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "specs/cheap-tests/mccormick-1999"))
sys.argv, _argv = sys.argv[:1], sys.argv
import token_anneal as T  # noqa: E402
sys.argv = _argv

FIX = "NCBE"
MARKS = ("SE", "BE", "E")


def fixed_mask(v):
    """per-letter True where the letter is held: inside an NCBE span, or in the type's final mark (if not already
    covered by an NCBE span ending the type)."""
    fx = [False] * len(v)
    i = v.find(FIX)
    while i >= 0:
        for j in range(i, i + len(FIX)):
            fx[j] = True
        i = v.find(FIX, i + len(FIX))
    m = next((m for m in MARKS if v.endswith(m) and len(v) > len(m)), "")
    for j in range(len(v) - len(m), len(v)):
        fx[j] = True
    return fx


def shuffle_ncbe(toks, rng):
    types = sorted(set(v for k, v in toks if k == "code"))
    masks = [fixed_mask(v) for v in types]
    free = [ch for v, fx in zip(types, masks) for ch, f in zip(v, fx) if not f]
    rng.shuffle(free)
    it = iter(free)
    new = {v: "".join(ch if f else next(it) for ch, f in zip(v, fx)) for v, fx in zip(types, masks)}
    return [(k, new[v]) if k == "code" else (k, v) for k, v in toks]


_S = {}


def _fit(job):
    toks, seed, kind = job
    rng = random.Random(seed)
    nt = shuffle_ncbe(toks, rng) if kind == "ncbe" else T.shuffle_types(toks, rng, keep_marks=True)
    fmap, row, _ = T.fit_marks(_S["wb"], nt, _S["alpha"], _S["beam"])
    return {"seed": seed, "coverage": row["coverage"], "spl": row["score_per_letter"], "fmap": fmap,
            "decode": row["decode"] if seed in _S["keep_decode"] else None}


def render(decode, read_only=False):
    """judge text from a skel decode string: read words as words; '?XYZ' unread segments as their code letters
    (render A) or dropped (render B, read_only); numbers dropped (the judge folds to letters anyway)."""
    out = []
    for tok in decode.split(" "):
        if not tok.startswith("["):
            continue
        for seg in tok.strip("[]").split("+"):
            if seg.startswith("?"):
                if not read_only:
                    out.append(seg[1:].lower())
            else:
                out.append(seg)
    return " ".join(out)


def selftest():
    toks = [("code", "NCBE"), ("code", "WLDNCBE"), ("code", "ABCSE"), ("number", "7"), ("code", "NCBE"), ("code", "XYZ")]
    for s in range(50):
        nt = shuffle_ncbe(toks, random.Random(s))
        assert nt[0] == ("code", "NCBE") and nt[4] == ("code", "NCBE") and nt[3] == ("number", "7")
        assert nt[1][1].endswith("NCBE") and nt[2][1].endswith("SE")
        assert sorted("".join(v for _, v in nt if v != "7")) == sorted("".join(v for _, v in toks if v != "7"))
        assert [len(v) for _, v in nt] == [len(v) for _, v in toks]
    assert fixed_mask("NCBRTSENCBE") == [False] * 7 + [True] * 4
    assert render("[nice+?XE] 71 [?AB]") == "nice xe ab" and render("[nice+?XE] [?AB]", True) == "nice"
    print("selftest OK"); return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=200)
    ap.add_argument("--procs", type=int, default=4)
    ap.add_argument("--pool", type=int, default=3000)
    ap.add_argument("--lexicon", help="MCC-GREGG: word-list file for the pool filter (token_anneal.lexicon_allows)")
    ap.add_argument("--kinds", default="ncbe,tm", help="MCC-GREGG: which nulls to draw (ncbe, tm)")
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    toks = T.tokenize(T.CIPHER_FILE.read_text())
    allowed = T.lexicon_allows(T.load_lexicon(a.lexicon)) if a.lexicon else None
    _S.update(wb=T.WordBigram(T.corpus_words_from(T.HELDOUT_EN), a.pool, allowed=allowed), alpha=3.0, beam=200,
              keep_decode={7000, 8000})
    t0 = time.time()
    fmap, tr, _ = T.fit_marks(_S["wb"], toks, 3.0, 200)
    out = {"target": {"coverage": tr["coverage"], "spl": tr["score_per_letter"], "fmap": fmap, "decode": tr["decode"]}}
    print(json.dumps({k: v for k, v in out["target"].items() if k != "decode"}), f"{time.time()-t0:.0f}s", file=sys.stderr)
    import multiprocessing as mp
    with mp.get_context("fork").Pool(a.procs) as pool:
        for kind, base in (("ncbe", 7000), ("tm", 8000)):
            if kind not in a.kinds.split(","):
                continue
            t0 = time.time()
            rows = pool.map(_fit, [(toks, base + i, kind) for i in range(a.draws)])
            out[kind] = rows
            print(kind, len(rows), f"{time.time()-t0:.0f}s", file=sys.stderr)
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
