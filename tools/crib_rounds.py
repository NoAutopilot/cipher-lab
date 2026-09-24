#!/usr/bin/env python3
"""Model-in-the-loop crib rounds on a matched homophonic control (solvEX, 24 Sept 2026).

Wraps tools/homophonic_anneal.py. A reader (a person or a model session) sees only the decode and the
per-sign confidence, proposes sign=letter cribs from the language, and the control is re-annealed with those
signs held fixed. The control's plaintext and key sit in DIR/hidden.json, which the reader never opens;
only --score reads it, and it prints numbers only (accuracy, cribs right/wrong), never letters.

  make:   crib_rounds.py --control PLAIN --signs K --length N --corpus A.txt [--corpus B.txt ...] --dir DIR
                         [--seed 1] [--restarts 8] [--iters 40000] [--order 3]
          builds the control (homophonic_anneal.make_control), writes DIR/cipher.tsv, DIR/hidden.json,
          DIR/state.json, and runs round 0 (blind) -> DIR/round0.txt
  make from a prebuilt control (solvEX2, 24 Sept 2026; e.g. the code+mark design on a target's row pattern):
          crib_rounds.py --cipher-tsv C.tsv --plain H.json --corpus A.txt [...] --dir DIR [--seed --restarts --iters]
          C.tsv has a header and pos<TAB>sign rows (sign ids free of '=', ',', '#' and spaces); H.json holds
          {"plain": the letter per token, "truth": {sign: letter}}. Both are copied into DIR (cipher.tsv,
          hidden.json) and round 0 runs blind. The builder writes H.json without printing it.
  round:  crib_rounds.py --dir DIR --round R --cribs FILE
          FILE holds cumulative cribs, one sign=letter per line or comma-separated ('#' comments allowed);
          re-anneals with them fixed -> DIR/roundR.txt (decode + confidence) and DIR/roundR.json
  score:  crib_rounds.py --dir DIR --score [--round R]
          prints letter accuracy and sign-type accuracy of round R (default: all rounds) against the hidden
          plaintext, and for each round the cribs it added: proposed, right, wrong. Appends DIR/scores.tsv.
  view:   crib_rounds.py --dir DIR --view R [--width 20]
          prints round R's decode as a grid, position / letter row / sign-id row (what the reader works from
          when it names sign=letter cribs by position)

Confidence of a sign = share of the top restarts (all --restarts) whose key gives that sign the same letter
as the best restart; shown as a digit 0-9 under each symbol (9 = all agree), '*' for a crib-fixed sign.
For a homophonic control every token is one letter, so token accuracy equals letter accuracy.

Test: python3 tools/tests/test_crib_rounds.py
"""
import argparse, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import homophonic_anneal as ha  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rel = lambda f: os.path.relpath(os.path.abspath(f), ROOT)
at_root = lambda f: os.path.join(ROOT, f)


def load_state(d):
    return json.load(open(os.path.join(d, "state.json")))


def save_state(d, st):
    json.dump(st, open(os.path.join(d, "state.json"), "w"), indent=1)


def read_cribs(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        line = line.split("#", 1)[0]
        for kv in line.replace(",", " ").split():
            s, a = kv.split("=")
            a = ha.fold(a)
            if len(a) != 1:
                raise SystemExit(f"crib {kv}: letter must fold to one of {ha.ALPHA}")
            out[s] = a
    return out


def run_round(d, st, r, fixed):
    seq = [l.rstrip("\n").split("\t")[1] for l in open(os.path.join(d, "cipher.tsv"))][1:]
    model = ha.Model([open(at_root(f), encoding="utf-8").read() for f in st["corpus"]], st["order"])
    unknown = set(fixed) - set(seq)
    if unknown:
        raise SystemExit(f"cribs name signs not in the cipher: {sorted(unknown)}")
    res = ha.solve(seq, model, st["restarts"], st["iters"], st["seed"], st["uni_weight"], dict(fixed))
    best = res[0][1]
    conf = {}
    for s in set(seq):
        conf[s] = sum(1 for _, k in res if k[s] == best[s]) / len(res)
    dec = "".join(best[x] for x in seq)
    json.dump({"round": r, "cribs": fixed, "key": best, "decoded": dec, "conf": conf,
               "restart_scores": [round(x[0], 1) for x in res]},
              open(os.path.join(d, f"round{r}.json"), "w"), indent=1)
    # human/model-readable view: blocks of 40 symbols, sign ids / letters / confidence
    w = max(len(s) for s in seq)
    lines = [f"# round {r}: N={len(seq)} K={len(set(seq))} cribs={len(fixed)} best score {res[0][0]:.1f} "
             f"({res[0][0] / len(seq):.3f}/symbol); restarts {[round(x[0], 1) for x in res]}",
             "# stream (letters, confidence digit below, * = crib):"]
    cd = lambda s: "*" if s in fixed else str(min(9, int(conf[s] * 9 + 1e-9)))
    for i in range(0, len(seq), 80):
        lines.append(dec[i:i + 80])
        lines.append("".join(cd(s) for s in seq[i:i + 80]))
        lines.append("")
    lines.append("# signs by frequency: sign count letter conf  (positions of first 3 occurrences)")
    from collections import Counter
    for s, c in Counter(seq).most_common():
        ps = [i for i, x in enumerate(seq) if x == s][:3]
        lines.append(f"{s:>{w}} {c:4d} {best[s]} {cd(s)}   {ps}")
    open(os.path.join(d, f"round{r}.txt"), "w").write("\n".join(lines) + "\n")
    st.setdefault("rounds", {})[str(r)] = {"cribs": fixed}
    save_state(d, st)
    return dec


def score(d, st, rounds):
    hid = json.load(open(os.path.join(d, "hidden.json")))
    p, truth = hid["plain"], hid["truth"]
    rows, prev_acc, prev_cribs = [], None, {}
    for r in sorted(int(x) for x in st.get("rounds", {})):
        rj = json.load(open(os.path.join(d, f"round{r}.json")))
        dec, key, cribs = rj["decoded"], rj["key"], rj["cribs"]
        acc = sum(a == b for a, b in zip(dec, p)) / len(p)
        sig = sum(key[s] == truth[s] for s in truth if s in key) / len(key)
        new = {s: a for s, a in cribs.items() if prev_cribs.get(s) != a}
        right = sum(truth[s] == a for s, a in new.items())
        row = {"round": r, "letter_acc": round(100 * acc, 1), "sign_acc": round(100 * sig, 1),
               "before": prev_acc, "cribs_total": len(cribs), "cribs_new": len(new), "right": right,
               "wrong": len(new) - right}
        if rounds is None or r in rounds:
            rows.append(row)
        prev_acc, prev_cribs = row["letter_acc"], cribs
    f = os.path.join(d, "scores.tsv")
    hdr = "round\tbefore\tletter_acc\tsign_acc\tcribs_total\tcribs_new\tright\twrong\n"
    with open(f, "w") as fh:
        fh.write(hdr)
        for x in rows:
            fh.write("\t".join(str(x[k]) for k in hdr.strip().split("\t")) + "\n")
            print(f"round {x['round']}: letters {x['before']} -> {x['letter_acc']}% (signs {x['sign_acc']}%); "
                  f"cribs new {x['cribs_new']} right {x['right']} wrong {x['wrong']} (total {x['cribs_total']})")
    return rows


def view(d, r, width):
    seq = [l.rstrip("\n").split("\t")[1] for l in open(os.path.join(d, "cipher.tsv"))][1:]
    rj = json.load(open(os.path.join(d, f"round{r}.json")))
    dec, w = rj["decoded"], max(3, max(len(s) for s in seq))
    for i in range(0, len(seq), width):
        print(f"{i:4d} " + " ".join(f"{c:>{w}}" for c in dec[i:i + width]))
        print("     " + " ".join(f"{s:>{w}}" for s in seq[i:i + width]))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", required=True)
    ap.add_argument("--control")
    ap.add_argument("--cipher-tsv")
    ap.add_argument("--plain")
    ap.add_argument("--signs", type=int)
    ap.add_argument("--length", type=int)
    ap.add_argument("--corpus", action="append")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--restarts", type=int, default=8)
    ap.add_argument("--iters", type=int, default=40000)
    ap.add_argument("--order", type=int, default=3)
    ap.add_argument("--uni-weight", type=float, default=1.0)
    ap.add_argument("--round", type=int)
    ap.add_argument("--cribs")
    ap.add_argument("--score", action="store_true")
    ap.add_argument("--view", type=int)
    ap.add_argument("--width", type=int, default=20)
    a = ap.parse_args()
    if a.control:
        os.makedirs(a.dir, exist_ok=True)
        corpus = [rel(c) for c in a.corpus]
        model = ha.Model([open(at_root(f), encoding="utf-8").read() for f in corpus], a.order)
        seq, p, truth = ha.make_control(open(a.control, encoding="utf-8").read(), a.signs, a.length, model, a.seed)
        with open(os.path.join(a.dir, "cipher.tsv"), "w") as fh:
            fh.write("pos\tsign\n" + "".join(f"{i}\t{s}\n" for i, s in enumerate(seq)))
        json.dump({"plain": p, "truth": truth}, open(os.path.join(a.dir, "hidden.json"), "w"))
        st = {"control": rel(a.control), "corpus": corpus, "N": len(seq), "K": len(set(seq)),
              "seed": a.seed, "restarts": a.restarts, "iters": a.iters, "order": a.order,
              "uni_weight": a.uni_weight}
        save_state(a.dir, st)
        run_round(a.dir, st, 0, {})
        print(f"made control N={len(seq)} K={len(set(seq))}; round 0 -> {a.dir}/round0.txt")
    elif a.cipher_tsv:
        if not (a.plain and a.corpus):
            ap.error("--cipher-tsv needs --plain and --corpus")
        os.makedirs(a.dir, exist_ok=True)
        corpus = [rel(c) for c in a.corpus]
        seq = [l.rstrip("\n").split("\t")[1] for l in open(a.cipher_tsv)][1:]
        bad = [x for x in set(seq) if any(c in x for c in "=,# ")]
        if bad:
            raise SystemExit(f"sign ids must not contain '=', ',', '#' or spaces: {sorted(bad)[:5]}")
        hid = json.load(open(a.plain))
        if len(hid["plain"]) != len(seq) or set(seq) - set(hid["truth"]):
            raise SystemExit("--plain does not match --cipher-tsv (length or sign set)")
        with open(os.path.join(a.dir, "cipher.tsv"), "w") as fh:
            fh.write("pos\tsign\n" + "".join(f"{i}\t{s}\n" for i, s in enumerate(seq)))
        json.dump({"plain": hid["plain"], "truth": hid["truth"]}, open(os.path.join(a.dir, "hidden.json"), "w"))
        st = {"control": rel(a.cipher_tsv), "corpus": corpus, "N": len(seq), "K": len(set(seq)),
              "seed": a.seed, "restarts": a.restarts, "iters": a.iters, "order": a.order,
              "uni_weight": a.uni_weight}
        save_state(a.dir, st)
        run_round(a.dir, st, 0, {})
        print(f"loaded control N={len(seq)} K={len(set(seq))}; round 0 -> {a.dir}/round0.txt")
    elif a.view is not None:
        view(a.dir, a.view, a.width)
    elif a.score:
        score(a.dir, load_state(a.dir), None if a.round is None else {a.round})
    elif a.round is not None:
        st = load_state(a.dir)
        run_round(a.dir, st, a.round, read_cribs(a.cribs) if a.cribs else {})
        print(f"round {a.round} -> {a.dir}/round{a.round}.txt")
    else:
        ap.error("give --control or --cipher-tsv (make), --round (re-anneal) or --score")


if __name__ == "__main__":
    main()
