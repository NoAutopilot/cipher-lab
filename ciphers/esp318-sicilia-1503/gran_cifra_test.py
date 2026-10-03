#!/usr/bin/env python3
"""Gran-cifra key test on no. 94 (f.120r) against a shuffled-key control (rule 3).

  python3 ciphers/esp318-sicilia-1503/gran_cifra_test.py [--controls 200] [--corpus es17] [--check]

Reads ciphertext.tsv (line, pos, sign, conf; w:word clear, g:abc code group, sheet labels such as e2, ?desc unmatched)
and key/key_gran_cifra.tsv. Writes gran_cifra_result.json. The cipher-only stream (sheet signs -> their row letter,
code groups -> the key's word, unmatched/unknown -> dropped) is scored by tools/judge_plaintext.py's 4-gram model; the
control re-scores the same token stream under 200 keys whose row->letter and code->word assignments are permuted
(same transcription, same token positions, same number of distinct values; only the key changes).
--check exits 1 if the committed gran_cifra_result.json differs from a regeneration (rule 7).
"""
import argparse, csv, json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
import judge_plaintext as jp

def load_key(p):
    sign, code = {}, {}
    for ln in open(p, encoding="utf-8"):
        if ln.startswith("#") or ln.startswith("code\t"):
            continue
        c, v, *_ = ln.rstrip("\n").split("\t")
        (code if c.startswith("g:") else sign)[c] = v
    return sign, code

def load_ct(p):
    return [r for r in csv.DictReader(open(p, encoding="utf-8"), delimiter="\t")]

def stream(rows, sign, code):
    out, hit, n = [], 0, 0
    for r in rows:
        t = r["sign"]
        if t.startswith("w:"):
            out.append(" "); continue
        n += 1
        if t in sign:
            hit += 1; out.append(sign[t].split("|")[0])
        elif t in code:
            hit += 1; out.append(" " + code[t].split("|")[0] + " ")
        else:
            out.append("")
    return "".join(out), hit, n

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--controls", type=int, default=200)
    ap.add_argument("--corpus", default="es"); ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    sign, code = load_key(HERE / "key" / "key_gran_cifra.tsv")
    rows = load_ct(HERE / "ciphertext.tsv")
    text, hit, n = stream(rows, sign, code)
    model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA[a.corpus]])
    L = len(jp.fold(text)); sc = model.score(text)
    real, null, _ = model.controls(max(L, 20), samples=200)
    rnd = random.Random(94); rowvals = sorted(set(sign.values())); ctl = []
    for _ in range(a.controls):
        perm = rowvals[:]; rnd.shuffle(perm); m = dict(zip(rowvals, perm))
        s2 = {k: m[v] for k, v in sign.items()}
        cv = list(code.values()); rnd.shuffle(cv); c2 = dict(zip(code.keys(), cv))
        ctl.append(round(model.score(stream(rows, s2, c2)[0]), 4))
    ctl.sort(); rank = sum(c >= sc for c in ctl)
    res = {"cipher_tokens": n, "tokens_with_key_value": hit, "overlap": round(hit / n, 3) if n else 0,
           "letters_scored": L, "corpus": a.corpus, "score": round(sc, 4),
           "control_shuffled_key": {"n": len(ctl), "p50": jp.pct(ctl, .5), "p95": jp.pct(ctl, .95), "p99": jp.pct(ctl, .99),
                                    "controls_at_or_above_target": rank},
           "judge_real_p05": round(jp.pct(real, .05), 4), "judge_null_p99": round(jp.pct(null, .99), 4),
           "reading_cipher_only": " ".join(text.split())}
    out = HERE / "gran_cifra_result.json"
    new = json.dumps(res, indent=1, ensure_ascii=False) + "\n"
    if a.check:
        ok = out.exists() and out.read_text(encoding="utf-8") == new
        print("check:", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    out.write_text(new, encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if k != "reading_cipher_only"}, indent=1))
    print(res["reading_cipher_only"][:600])

if __name__ == "__main__":
    main()
