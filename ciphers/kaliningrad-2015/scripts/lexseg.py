#!/usr/bin/env python3
"""lexseg.py (R10-KAL7, 6 Oct 2026): lexicon word-segmentation coverage of two-stage homophonic decodes, kaliningrad-2015.

The second instrument on the S3' (ru-s3p-soft) design after R9-KAL6's ru19_soft n-gram judge could not separate the
target decode from its shuffle. Pre-registration: ciphers/kaliningrad-2015/HYPOTHESES.md "R10-KAL7".

  decode  KIND SEED OUT   KIND = target | shuf (target shuffled with family_run.py's own shuffle, RNG seed SEED)
                          | synth (family homophonic make_control window, seed SEED) | synthshuf (synth seed 1, shuffled SEED)
  score   LEXICON FILE... coverage per decode file

Decoder: tools/families/homophonic.solve, params profile=target alphabet=ru-s3p-soft soft=two-stage, restarts 20, solve
seed 1 -- R9-KAL6's unit -- but trained on the S3'-soft Synodal Bible with the New Testament (books 40-66) removed,
so the lexicon (NT word types) is held out from every corpus the decoder used. Train corpus, offline, a few seconds:
  mkdir tr; ln -s tools/data/ru19/{0[1-9],[1-3]?,6[7-9],[7-8]?}_*.txt.gz tr/  (every book number outside 40-66)
  python3 tools/translit_ru.py --scheme s3p --soft-letters tr TRAIN.txt.gz      (env LEXSEG_TRAIN=TRAIN.txt.gz)
R12-KAL8 (6 Oct 2026): the same driver for the remaining schemes -- env LEXSEG_CIPHER (a ciphertext TSV, default the
convention-A file) and LEXSEG_PARAMS (JSON replacing PARAMS, e.g. {"profile": "target"}); unset, behaviour is R10-KAL7's.
Train corpora and lexicons for those units: scripts/lexseg_build.py.
Coverage: the largest number of decode letters covered by non-overlapping lexicon words (dynamic programming, each
message line separately, case-sensitive), divided by all decode letters.
"""
import gzip, json, os, random, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import family_run as fr  # noqa: E402
from families import homophonic as H  # noqa: E402

CIPHER = os.environ.get("LEXSEG_CIPHER") or os.path.join(ROOT, "ciphers/kaliningrad-2015/ciphertext_signs.tsv")
PARAMS = json.loads(os.environ["LEXSEG_PARAMS"]) if os.environ.get("LEXSEG_PARAMS") else \
    {"profile": "target", "alphabet": "ru-s3p-soft", "soft": "two-stage"}
RESTARTS, SOLVE_SEED = 20, 1


def target_msgs(shuffle=None):
    msgs, _ = fr.read_cipher_file(CIPHER, "auto")
    if shuffle is not None:  # identical to family_run.py --shuffle-target
        rng = random.Random(shuffle)
        t = [x for m in msgs for x in m]
        rng.shuffle(t)
        out, pos = [], 0
        for m in msgs:
            out.append(t[pos:pos + len(m)])
            pos += len(m)
        msgs = out
    return msgs


def params_for(msgs):
    toks = [t for m in msgs for t in m]
    p = dict(PARAMS)
    p.update({"N": len(toks), "K": len(set(toks)), "lengths": [len(m) for m in msgs], "target_msgs": msgs,
              "messages_independent": False})
    return p


def decode(kind, seed, out):
    corpus = [gzip.open(os.environ["LEXSEG_TRAIN"], "rt", encoding="utf-8").read()]
    tm = target_msgs()
    info = {"kind": kind, "seed": seed}
    if kind in ("target", "shuf"):
        msgs = target_msgs(seed if kind == "shuf" else None)
        corp = corpus
    else:
        p = params_for(tm)
        cs, plain, rest = H.make_control({}, 1 if kind == "synthshuf" else seed, corpus, p)
        seq = [x for m in cs for x in m]
        if kind == "synthshuf":
            random.Random(seed).shuffle(seq)
        msgs, corp = [seq], rest
        info["truth"] = plain
    p = params_for(tm)  # profile from the real target, as family_run.py sets it
    dec, sc, extra = H.solve(msgs, {}, SOLVE_SEED, RESTARTS, corp, p)
    if "truth" in info:
        info["recovery"] = round(H.score_recovery(dec, info["truth"]), 3)
    lines, pos = [], 0
    for m in msgs:
        lines.append(dec[pos:pos + len(m)])
        pos += len(m)
    info["score"] = round(sc, 1)
    with open(out, "w", encoding="utf-8") as f:
        f.write("# " + json.dumps(info) + "\n" + "\n".join(lines) + "\n")


def coverage(text, lex, maxlen, minlen=4):
    n = len(text)
    best = [0] * (n + 1)
    for i in range(1, n + 1):
        b = best[i - 1]
        for L in range(minlen, min(maxlen, i) + 1):
            if text[i - L:i] in lex and best[i - L] + L > b:
                b = best[i - L] + L
        best[i] = b
    return best[n], n


def score(lexfile, files):
    minlen = int(os.environ.get("LEXSEG_MINLEN", "4"))  # 5 = the registered secondary figure
    lex = set(w for w in open(lexfile, encoding="utf-8").read().split() if len(w) >= minlen)
    ml = max(map(len, lex))
    for fn in files:
        cov = tot = 0
        hdr = ""
        for line in open(fn, encoding="utf-8"):
            if line.startswith("#"):
                hdr = json.loads(line[2:])
                hdr.pop("truth", None)
                continue
            c, n = coverage(line.strip(), lex, ml, minlen)
            cov, tot = cov + c, tot + n
        print(f"{os.path.basename(fn)}\t{cov}\t{tot}\t{cov / tot:.4f}\t{json.dumps(hdr)}")


if __name__ == "__main__":
    if sys.argv[1] == "decode":
        decode(sys.argv[2], int(sys.argv[3]), sys.argv[4])
    else:
        score(sys.argv[2], sys.argv[3:])
