#!/usr/bin/env python3
"""Held-out test of both letter alphabets on R9502 f.40 vs its period decipherment f.42 (R12-RJM42, 6 Oct 2026).

Pre-registration: witness/PREREG_f42.md (committed and pushed before this script was first run on the passes).

Inputs (this folder): passes/f40_A.tsv, passes/f40_B.tsv (two blind Sonnet passes of R9502 f.40 on tools/iiif_lines.py
crops, shared inventory passes/inventory.md, B read in reverse order), passes/gloss_f42.tsv (one Sonnet read of the clerk's
decipherment f.42), keys alphabet.tsv (this folder's f.194/f.197 alphabet, test 1) and key_tomokiyo_alpha.tsv (published,
Tomokiyo), nomenclator sources/cryptiana/keys/AlonsoSanchez_2.tsv. Reuses scripts/test1.py's reconcile/to_pair and
tools/interlinear_align.py's run_align with test 1's settings unchanged.

Steps (as pre-registered)
  1. reconcile A/B (test1.reconcile); err_2reader reported. Cipher lines written wholly in clear in pass A (every token
     bracketed) are dropped: the clerk writes "Claro" for them and gloss_text drops "claro". Gloss rows with confidence
     'heading' are dropped.
  2. one prior-free alignment of f.40 against f.42 (test1 settings: --code-chunk 2, word codes %, null cost -1.0,
     max chunk 10, clear-consumes). Nothing from any key enters it.
  3. calibration gate, before any key is scored: share of nomenclator code tokens whose aligned chunk equals their own
     table word >= 0.50. Below it: "non-test at this alignment", no S is computed for either key.
  4. per key: S = share of scored symbol tokens whose chunk equals the key's value (null = empty chunk); control = 200
     keys with the same values permuted among the same labels (seeds 1..200). Gate: S > control max AND S >= 0.24.
     Scored set = symbol tokens NOT on cipher line 1 and whose chunk does not start inside the first len(INCIPIT)
     gloss letters (Tomokiyo prints this letter's first line); the excluded set is scored separately, reported only.

  python3 scripts/test42.py [--check] [--shuffles 200]      writes results_test42.json; --check exits 1 if stale
"""
import argparse, csv, importlib.util, json, random, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("t1", HERE / "scripts/test1.py")
t1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t1)
ia = t1.ia

# Tomokiyo, Cryptiana AlonsoSanchez.htm, "Juan Manuel to Charles V, 8 March 1522, R9502": first line of the decipherment
INCIPIT = "Esta otra letra se cerro anoche y no pudo"
# pass-local ?n -> shared label, per pass; filled before scoring from each pass's own notes only (PREREG_f42.md addendum)
NORM42 = {"A": {"?1": "7"}, "B": {"?3": "R", "?4": "T"}}
CAL_GATE = 0.50


def load(p):
    t1.NORM[("f40", p)] = NORM42[p]
    rows = {}
    with open(HERE / "passes" / f"f40_{p}.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            n = int(r["line"])
            rows[n] = t1.tokens(r.get("tokens", ""), "f40", p)
    return rows


def keys():
    alpha = {}
    with open(HERE / "alphabet.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            alpha[r["sign"]] = r["letter"]
    tom = {}
    for r in csv.DictReader((l for l in open(HERE / "key_tomokiyo_alpha.tsv", encoding="utf-8") if not l.startswith("#")),
                            delimiter="\t"):
        if r["firm"] == "1" and r["our_label"]:
            for lab in r["our_label"].split(","):
                tom[lab] = "" if r["letter"] == "null" else r["letter"]
    return {"alphabet.tsv": alpha, "key_tomokiyo_alpha.tsv": tom}


def score(idx, raw, chunks, values, shuffles):
    idx = [i for i in idx if raw[i][1:] in values]

    def stat(vals):
        return sum(ia.fold(chunks[i]) == vals[raw[i][1:]] for i in idx) / len(idx) if idx else 0.0
    real = stat(values)
    labs = sorted(values)
    null = []
    for s in range(1, shuffles + 1):
        perm = [values[l] for l in labs]
        random.Random(s).shuffle(perm)
        null.append(stat(dict(zip(labs, perm))))
    null.sort()
    per = {}
    for i in idx:
        l = raw[i][1:]
        h, n = per.get(l, (0, 0))
        per[l] = (h + (ia.fold(chunks[i]) == values[l]), n + 1)
    return {"N": len(idx), "S_real": round(real, 4), "null_mean": round(sum(null) / len(null), 4),
            "null_p95": round(null[int(0.95 * len(null)) - 1], 4), "null_max": round(null[-1], 4),
            "rank": 1 + sum(x >= real for x in null), "of": len(null) + 1,
            "gate": "PASS" if real > null[-1] and real >= 0.24 else "FAIL",
            "per_label": {l: "%d/%d" % per[l] for l in sorted(per)}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--shuffles", type=int, default=200)
    a = ap.parse_args()
    key = t1.load_key()
    A, B = load("A"), load("B")
    clear = {n for n, toks in A.items() if toks and all(t.startswith("[") for t in toks)}
    A = {n: v for n, v in A.items() if n not in clear}
    B = {n: v for n, v in B.items() if n not in clear}
    rec, err, agree, tot = t1.reconcile(A, B, key)
    res = {"err_2reader": round(err, 4), "agree_tokens": agree, "max_tokens": tot, "lines": len(rec),
           "clear_lines_dropped": sorted(clear),
           "symbols_agreed": sum(1 for l in rec.values() for t, s in l if s == "agree" and t1.SYMBOL.match(t)),
           "symbols_split": sum(1 for l in rec.values() for t, s in l if s == "split")}
    gl = []
    with open(HERE / "passes/gloss_f42.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r.get("confidence", "").strip().lower() == "heading":
                continue
            txt = re.sub(r"^\s*claro\b[.:]?", "", r["text"].strip(), flags=re.I)  # the clerk's "Claro" marker, own row or not
            if txt.strip():
                gl.append(txt)
    gloss = " ".join(gl)
    raw, kinds, lines = [], [], []
    for n in sorted(rec):
        r, k = t1.to_pair(rec[n], key)
        raw += r; kinds += k; lines += [n] * len(r)
    c = 0
    for i, t in enumerate(raw):
        if t == "@~":
            c += 1
            raw[i] = "@~%d" % c
    ia.WORD_PFX = "%"
    ia.CODE_CHUNK = 2
    pair = {"plain_line": "1", "plain_raw": gloss, "cipher_line": "1", "cipher_raw": " ".join(raw)}
    prepared, results, counts, shown = ia.run_align([pair], floor=0, clear_consumes=True, code_prefix="@",
                                                    null_cost=-1.0, max_chunk=10)
    letters = prepared[0][3]
    offs = [cc for cc in results[0]]
    chunks = [letters[x[0]:x[1]] if x else "" for x in offs]
    code_n = sum(1 for k in kinds if k == "code")
    code_hit = sum(1 for t, k, ch in zip(raw, kinds, chunks) if k == "code" and ia.fold(ch) == ia.fold(t))
    inc_len = len(ia.plain_letters(INCIPIT)[0])
    gl_head = letters[:inc_len]
    res["gloss_letters"] = len(letters)
    res["incipit_letters"] = inc_len
    res["gloss_starts_with_incipit"] = ia.fold(gl_head) == ia.fold(ia.plain_letters(INCIPIT)[0])
    res["calibration"] = {"code_words": code_n, "code_words_matched": code_hit,
                          "share": round(code_hit / code_n, 4) if code_n else None, "gate": CAL_GATE,
                          "verdict": "PASS" if code_n and code_hit / code_n >= CAL_GATE else "FAIL"}
    sym = [i for i, k in enumerate(kinds) if k == "sym"]
    excl = [i for i in sym if lines[i] == 1 or (offs[i] and offs[i][0] < inc_len)]
    scored = [i for i in sym if i not in excl]
    res["symbol_tokens"] = {"all": len(sym), "scored": len(scored), "excluded_line1_incipit": len(excl),
                            "labels": dict(Counter(raw[i][1:] for i in sym))}
    if res["calibration"]["verdict"] == "PASS":
        res["keys"] = {}
        for name, vals in keys().items():
            res["keys"][name] = {"values": vals, "heldout": score(scored, raw, chunks, vals, a.shuffles),
                                 "line1_incipit_separate": score(excl, raw, chunks, vals, a.shuffles)}
    else:
        res["keys"] = "not scored: calibration gate FAIL (non-test at this alignment)"
    out_json = json.dumps(res, indent=1, sort_keys=True) + "\n"
    rc = "line\ttokens\n" + "".join("%d\t%s\n" % (n, " ".join(t for t, _ in rec[n])) for n in sorted(rec))
    al = "i\tline\tkind\ttoken\tchunk\n" + "".join("%d\t%d\t%s\t%s\t%s\n" % (i, lines[i], kinds[i], raw[i], chunks[i])
                                                    for i in range(len(raw)))
    outs = {"results_test42.json": out_json, "ciphertext_f40_reconciled.tsv": rc, "passes/align_f40_f42.tsv": al}
    if a.check:
        ok = all((HERE / p).exists() and (HERE / p).read_text() == s for p, s in outs.items())
        print("up to date" if ok else "STALE")
        sys.exit(0 if ok else 1)
    for p, s in outs.items():
        (HERE / p).write_text(s)
    print(out_json)


if __name__ == "__main__":
    main()
