#!/usr/bin/env python3
"""Trial decode of R9501 f.34 with Tomokiyo's published key (R12-RJM9501, 6 Oct 2026).

Licensed by R12-RJMV (AUDIT.md): a trial decode of R9501 with key_tomokiyo_alpha.tsv (letter alphabet, published, Satoshi
Tomokiyo, Cryptiana) and the nomenclator sources/cryptiana/keys/AlonsoSanchez_2.tsv (Tomokiyo, published). R9501 has no
period decipherment in DECODE, so nothing here is H or C.

Inputs: passes/f34_A.tsv (forward), passes/f34_B.tsv (reverse order), two blind Sonnet passes on tools/iiif_lines.py crops of
R9501 f.34 (30 lines), shared inventory passes/inventory.md. Reconciled with scripts/test1.py's reconcile (unchanged).

Per-token grades (R12-RJMV's rule; rule 4):
  S  an agreed nomenclator code (Tomokiyo's table, control-backed in test 0) or an agreed symbol of A, Z, R, 4, F
     (the five labels that cleared the held-out test on R9502 f.40)
  M  a code that only one pass read (split-code); an agreed symbol of the other valued labels (T, 9, X, 3, E, V, K)
  U  unread: a split symbol (~), a symbol with no firm value (Q, D, W, B, 7, ?n), a Latin group not in the table
Outputs: ciphertext_f34_reconciled.tsv, reading_f34_tomokiyo.txt (per line, code words and letter runs, '_' = unread),
grades_f34_tomokiyo.tsv, reading_f34_shuffled.txt (the same key on the reconciled tokens in a seeded random order: the
judge's ARM-C1 control, rule 3), results_decode9501.json.

  python3 scripts/decode9501.py [--check]      --check exits 1 if any committed output differs from a rerun
"""
import argparse, csv, importlib.util, json, random, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("t1", HERE / "scripts/test1.py")
t1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t1)

# pass-local ?n -> shared label, from each pass's own notes only (filled before the decode was first run)
NORM34 = {"A": {"?1": "K"}, "B": {}}   # A ?1 "ankh-like, small cross with a loop above" = K (as f194 A ?2 / B ?1); B ?1 "triangle-like with a bar": no label, unvalued
# pass B numbered its rows in its own (reverse) reading order, not by crop: row k = crop L(31-k) (row 30 = L01 "F V A P T ...",
# row 2 = L29 "kiz ..."; row 1 is a faint partial read of L30). Checked by eye on rows 1-3 and 29-30 against pass A and the
# crops; the pass file is kept as written and the remap is applied here.
LINE_MAP = {"A": lambda n: n, "B": lambda n: 31 - n}
S_LABELS = {"A", "Z", "R", "4", "F"}
SHUFFLE_SEED = 1


def load(p):
    t1.NORM[("f34", p)] = NORM34[p]
    rows = {}
    with open(HERE / "passes" / f"f34_{p}.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            rows[LINE_MAP[p](int(r["line"]))] = t1.tokens(r.get("tokens", ""), "f34", p)
    return rows


def alpha():
    tom = {}
    for r in csv.DictReader((l for l in open(HERE / "key_tomokiyo_alpha.tsv", encoding="utf-8") if not l.startswith("#")),
                            delimiter="\t"):
        if r["firm"] == "1" and r["our_label"]:
            for lab in r["our_label"].split(","):
                tom[lab] = "" if r["letter"] == "null" else r["letter"]
    return tom


def decode_tok(t, st, key, alp):
    """-> (value, grade, kind); value '' for a null, '_' for unread."""
    if t.startswith("["):
        return t[1:-1], "clear", "clear"
    if t == "~":
        return "_", "U", "split"
    if t1.SYMBOL.match(t):
        if t in alp:
            g = "S" if (t in S_LABELS and st == "agree") else "M"
            return alp[t], g, "sym"
        return "_", "U", "sym-novalue"
    if t in key:
        return key[t], ("S" if st == "agree" else "M"), "code"
    return "_", "U", "miss"


def render(toks):
    """code words as words, consecutive letter values joined into one run, '_' for unread."""
    out, run = [], ""
    for v, kind in toks:
        if kind == "sym":
            run += v
            continue
        if run:
            out.append(run); run = ""
        if v:
            out.append(v)
    if run:
        out.append(run)
    return " ".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    key = t1.load_key()
    alp = alpha()
    A, B = load("A"), load("B")
    rec, err, agree, tot = t1.reconcile(A, B, key)
    grades, read_lines, flat = [], [], []
    for n in sorted(rec):
        toks = []
        for j, (t, st) in enumerate(rec[n]):
            v, g, kind = decode_tok(t, st, key, alp)
            grades.append((n, j + 1, t, st, kind, v, g))
            toks.append((v, kind))
            flat.append((t, st))
        read_lines.append("%d\t%s" % (n, render(toks)))
    sh = flat[:]
    random.Random(SHUFFLE_SEED).shuffle(sh)
    sh_toks = [(decode_tok(t, st, key, alp)[0], decode_tok(t, st, key, alp)[2]) for t, st in sh]
    gc = Counter(g for *_, g in grades)
    kc = Counter((kind, g) for *_, kind, v, g in grades)
    labs = Counter(t for _, _, t, st, kind, _, _ in grades if kind in ("sym", "sym-novalue"))
    res = {"err_2reader": round(err, 4), "agree_tokens": agree, "max_tokens": tot, "lines": len(rec),
           "tokens": len(grades), "grades": dict(sorted(gc.items())),
           "by_kind_grade": {"%s/%s" % k: c for k, c in sorted(kc.items())},
           "symbol_labels": dict(sorted(labs.items())),
           "letter_key": alp, "s_labels": sorted(S_LABELS), "shuffle_seed": SHUFFLE_SEED,
           "key_source": "published (Tomokiyo, Cryptiana: JuanManuel.png alphabet; AlonsoSanchez.htm nomenclator)"}
    out_json = json.dumps(res, indent=1, sort_keys=True) + "\n"
    rc = "line\ttokens\n" + "".join("%d\t%s\n" % (n, " ".join(t for t, _ in rec[n])) for n in sorted(rec))
    gr = "line\tpos\ttoken\treaders\tkind\tvalue\tgrade\n" + "".join("%d\t%d\t%s\t%s\t%s\t%s\t%s\n" % r for r in grades)
    rd = ("# R9501 f.34 trial decode, key published (Tomokiyo), grades in grades_f34_tomokiyo.tsv; '_' = unread; "
          "letter runs joined, word breaks not marked\n" + "\n".join(read_lines) + "\n")
    shuf = "# control: reconciled f.34 tokens in random order (seed %d), same key\n%s\n" % (SHUFFLE_SEED, render(sh_toks))
    outs = {"results_decode9501.json": out_json, "ciphertext_f34_reconciled.tsv": rc,
            "grades_f34_tomokiyo.tsv": gr, "reading_f34_tomokiyo.txt": rd, "reading_f34_shuffled.txt": shuf}
    if a.check:
        ok = all((HERE / p).exists() and (HERE / p).read_text() == s for p, s in outs.items())
        print("up to date" if ok else "STALE")
        sys.exit(0 if ok else 1)
    for p, s in outs.items():
        (HERE / p).write_text(s)
    print(out_json)


if __name__ == "__main__":
    main()
