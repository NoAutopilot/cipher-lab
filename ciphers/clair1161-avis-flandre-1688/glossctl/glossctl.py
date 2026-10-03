#!/usr/bin/env python3
"""READ2-C1161B (3-4 Oct 2026): harder controls for the c186R gloss match (pre-registered in tx/PREREG_glossctl.md).

Statistic (same as READ2-C1161): decode the 220-sign c186R block (ciphertext.tsv, '/' dropped) with a key, take the
gloss letters a-z of align/pairs_c186R_v0.tsv row 'gloss' (170 letters, '?' dropped), and score
sum(difflib.SequenceMatcher(None, decode, gloss, autojunk=False).get_matching_blocks() sizes) / len(gloss).

  python3 glossctl.py target                 # real key.tsv -> statistic
  python3 glossctl.py windows [--n 200]      # control (b): real key's decode vs 200 fr16 corpus windows of len(gloss)
  python3 glossctl.py shuffled --seed S      # control (a): same anneal recipe as the real key (family_run homophonic,
                                             # anneal seed 1, restarts 32, noise 0.10, profile=target, fr16 judge corpora,
                                             # tokens space) on the token-ORDER-shuffled full ciphertext (family_run's own
                                             # --shuffle-target shuffle, seed S); key applied to the UNshuffled block.
Outputs append to glossctl/results.tsv; keys to glossctl/key_shuf<S>.tsv.
"""
import argparse, csv, difflib, json, os, random, re, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools"))

def block_tokens():
    return [r["sign"] for r in csv.DictReader(open(os.path.join(T, "ciphertext.tsv")), delimiter="\t")
            if r["line"].startswith("c186R") and r["sign"] != "/"]

def gloss_letters():
    for r in csv.DictReader(open(os.path.join(T, "align", "pairs_c186R_v0.tsv")), delimiter="\t"):
        if r["plain_line"] == "gloss":
            return re.sub("[^a-z]", "", r["plain_raw"].lower())

def stat(dec, ref):
    sm = difflib.SequenceMatcher(None, dec, ref, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks()) / len(ref)

def decode(key, toks):
    return "".join(key.get(t, "?") for t in toks)

def real_key():
    return {r["sign"]: r["value"] for r in csv.DictReader(open(os.path.join(T, "key.tsv")), delimiter="\t")}

def log(row):
    p = os.path.join(HERE, "results.tsv")
    new = not os.path.exists(p)
    with open(p, "a") as f:
        if new:
            f.write("utc\tcontrol\tseed\tvalue\tnote\n")
        f.write("\t".join(str(x) for x in row) + "\n")
    print("\t".join(str(x) for x in row))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["target", "windows", "shuffled"])
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--n", type=int, default=200)
    a = ap.parse_args()
    utc = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
    toks, g = block_tokens(), gloss_letters()
    if a.mode == "target":
        log([utc, "target", "-", f"{stat(decode(real_key(), toks), g):.4f}", f"block {len(toks)} signs, gloss {len(g)} letters"])
        return
    spec_path = os.path.join(ROOT, "specs", "clair1161-avis-flandre-1688.json")
    spec = json.load(open(spec_path))
    import judge_plaintext as jp, family_run as fr
    paths = fr.corpus_paths(spec, None)
    if a.mode == "windows":
        dec = decode(real_key(), toks)
        text = "".join(re.sub("[^a-z]", "", jp.read_corpus(p)) for p in paths)
        rng = random.Random(a.seed)
        vals = sorted(stat(dec, text[s:s + len(g)]) for s in (rng.randrange(len(text) - len(g)) for _ in range(a.n)))
        p95 = vals[int(0.95 * len(vals)) - 1 if len(vals) >= 20 else -1]
        log([utc, "b_windows", a.seed, f"p95={p95:.4f}", f"n={a.n} mean={sum(vals)/len(vals):.4f} max={vals[-1]:.4f} corpus letters {len(text)}"])
        return
    import families
    msgs, mode = fr.read_spec_cipher(spec, "space")
    rng = random.Random(a.seed)  # identical to family_run.py --shuffle-target
    flat = [t for m in msgs for t in m]; rng.shuffle(flat)
    shuf, pos = [], 0
    for m in msgs:
        shuf.append(flat[pos:pos + len(m)]); pos += len(m)
    allt = [t for m in shuf for t in m]
    params = {"noise": "0.10", "profile": "target", "N": len(allt), "K": len(set(allt)),
              "lengths": [len(m) for m in shuf], "target_msgs": shuf, "messages_independent": "separate" in mode}
    fam = families.load("homophonic")
    corpora = [jp.read_corpus(p) for p in paths]
    t0 = time.time()
    dec, sc, info = fam.solve(shuf, spec, 1, 32, corpora, dict(params))
    key = info["key"]
    with open(os.path.join(HERE, f"key_shuf{a.seed}.tsv"), "w") as f:
        f.write("sign\tvalue\n" + "".join(f"{k}\t{v}\n" for k, v in sorted(key.items())))
    log([utc, "a_shuffled_anneal", a.seed, f"{stat(decode(key, toks), g):.4f}",
         f"anneal score {sc:.1f}, {time.time()-t0:.0f}s"])

if __name__ == "__main__":
    main()
