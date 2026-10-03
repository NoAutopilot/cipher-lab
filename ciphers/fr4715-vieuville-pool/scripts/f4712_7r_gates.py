#!/usr/bin/env python3
"""Gates G1 and G2 on the BnF fr.4712 f.7r period interlinear pair, as pre-registered in witness/key71/PREREG3.md
(GAPS-fr4715-vieuville-pool-16, 3 Oct 2026).

  python3 scripts/f4712_7r_gates.py [--pairs witness/f4712_7r_pairs.tsv]

The pairs file's cipher_raw carries one token per group: N unmarked, dN one dot, tN two dots, bN bar. They are mapped to
numerals for tools/interlinear_align.py (unmarked N; dot 100+N; two dots 200+N; bar 300+N) and aligned from a flat
start (--floor 100 --keep-fs, no --prior).

G1 (the leaf's own control): A = distinct unmarked codes whose single-letter modal chunk equals a value Tomokiyo's table
gives that code; S = unmarked codes with a single-letter chunk that the table lists. Control: the table's values
permuted over its codes, 10,000 draws, seed 4712. PASS: S >= 12, A/S >= 0.70, A > p99.
G2 (only if G1 passes): each marked code's aligned meaning against key no.71's cell in the mark's layer, with the
notation-normalized match of PREREG3. Controls: label permutation (exact if <= 8 items, else 10,000, seed 4712) and
random code (10,000, seed 71). PASS: scorable >= 8, SHARE >= 0.80, REAL > p95 of both.
Exit 0 = G1 and G2 PASS, 2 = G1 FAIL (leaf held), 3 = G2 FAIL, 4 = G2 NON-TEST.
"""
import argparse, csv, itertools, random, re, subprocess, sys, unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from key71_control import load_key, norm_tokens, p95  # noqa: E402

HERE = Path(__file__).resolve().parent.parent
REPO = HERE.parent.parent
TOMO = HERE.parent / "fr4715-montholon-1589/keys/key_vieuville_nevers.tsv"
KEY71 = HERE / "witness/key71/key71_reconciled.tsv"
OFFSET = {"": 0, "d": 100, "t": 200, "b": 300}
LAYER = {100: "mots", 200: "places", 300: "persons"}
RANGE = {"mots": (11, 99), "places": (1, 99), "persons": (1, 89)}
ELIDE = ("qu", "l", "d", "j", "n", "s", "m", "t", "c")


def p99(xs):
    xs = sorted(xs)
    return xs[int(0.99 * (len(xs) - 1))]


def to_numeral(tok):
    m = re.fullmatch(r"([dtb]?)(\d{1,2})", tok)
    if not m:
        return None
    return str(OFFSET[m.group(1)] + int(m.group(2)))


def flat(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = s.replace("v", "u").replace("y", "i").replace("j", "i").replace("h", "")
    return re.sub(r"[^a-z]", "", s)


def squash(s):
    s = re.sub(r"s(?=[^aeiou])", "", s)
    return re.sub(r"(.)\1+", r"\1", s)


def nmatch(gloss, entry):
    g, e = norm_tokens(gloss), norm_tokens(entry)
    if g and e and (g <= e or e <= g):
        return True
    fg, fe = flat(gloss), flat(entry)
    if not fg or not fe:
        return False
    cands_g = {fg} | {fg[len(p):] for p in ELIDE if fg.startswith(p) and len(fg) > len(p)}
    cands_e = {fe} | {fe[len(p):] for p in ELIDE if fe.startswith(p) and len(fe) > len(p)}
    if cands_g & cands_e:
        return True
    if {squash(x) for x in cands_g} & {squash(x) for x in cands_e}:
        return True
    sg, se = {squash(t) for t in g}, {squash(t) for t in e}  # rule (iii) on the tokens of rule (i) as well
    return bool(sg and se and (sg <= se or se <= sg))


def judge(word, layer, num, val):
    cells = word.get((layer, str(num)), [])
    if not cells:
        return "absent", cells
    return ("match" if any(nmatch(val, e) for e in cells) else "conflict"), cells


def score(word, items):
    res = [judge(word, l, n, v)[0] for l, n, v in items]
    return res.count("match"), res.count("conflict")


def tomokiyo():
    t = {}
    for r in csv.DictReader((l for l in open(TOMO, encoding="utf-8") if not l.startswith("#")), delimiter="\t"):
        if r["kind"] == "letter" and r["sign"].isdigit():
            t[str(int(r["sign"]))] = r["value"].strip().lower()
    return t


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pairs", default=str(HERE / "witness/f4712_7r_pairs.tsv"))
    ap.add_argument("--out", default=str(HERE / "witness/f4712_7r"))
    a = ap.parse_args()
    num_pairs = a.out + "_pairs_numeral.tsv"
    with open(a.pairs, encoding="utf-8") as f, open(num_pairs, "w", encoding="utf-8") as g:
        rows = list(csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t"))
        g.write("plain_line\tplain_raw\tcipher_line\tcipher_raw\n")
        for r in rows:
            toks = [to_numeral(t) for t in r["cipher_raw"].split()]
            toks = [t for t in toks if t]
            g.write(f"{r['plain_line']}\t{r['plain_raw']}\t{r['cipher_line']}\t{' '.join(toks)}\n")
    akey = a.out + "_align_key.tsv"
    subprocess.run([sys.executable, str(REPO / "tools/interlinear_align.py"), "align", num_pairs, a.out + "_align.tsv",
                    akey, "--floor", "100", "--keep-fs"], check=True, stdout=subprocess.DEVNULL)
    learned = {}
    for r in csv.DictReader(open(akey, encoding="utf-8"), delimiter="\t"):
        learned[r["value"]] = (r["meaning"], r["n"])
    tomo = tomokiyo()
    letters = {v: m for v, (m, _) in learned.items() if int(v) < 100 and len(m) == 1 and v in tomo}
    A = sum(1 for v, m in letters.items() if tomo[v] == m)
    S = len(letters)
    codes, vals = list(tomo), list(tomo.values())
    rng = random.Random(4712)
    ctl = []
    for _ in range(10000):
        rng.shuffle(vals)
        perm = dict(zip(codes, vals))
        ctl.append(sum(1 for v, m in letters.items() if perm[v] == m))
    q = p99(ctl)
    for v in sorted(letters, key=int):
        print(f"G1\t{v}\taligned={letters[v]}\ttomokiyo={tomo[v]}\t{'agree' if tomo[v] == letters[v] else 'DIFFER'}")
    g1 = S >= 12 and S and A / S >= 0.70 and A > q
    print(f"G1 A {A}/{S} = {A / S if S else 0:.3f} | control (10000 value permutations) mean {sum(ctl)/len(ctl):.2f}"
          f" p99 {q} max {max(ctl)} | {'PASS' if g1 else 'FAIL'}")
    if not g1:
        sys.exit(2)
    word, _ = load_key(KEY71)
    items = []
    for v, (m, n) in learned.items():
        iv = int(v)
        if iv >= 100 and m:
            items.append((LAYER[iv // 100 * 100], iv % 100, m))
    for l, n, m in sorted(items):
        verdict, cells = judge(word, l, n, m)
        print(f"G2\t{l} {n}\tgloss={m}\tkey71={' | '.join(cells) or '-'}\t{verdict}")
    mt, k = score(word, items)
    sc = mt + k
    share = mt / sc if sc else 0.0
    vals = [v for _, _, v in items]
    if len(items) <= 8:
        perm = [score(word, [(l, n, vals[p[i]]) for i, (l, n, _) in enumerate(items)])[0]
                for p in itertools.permutations(range(len(items)))]
    else:
        rng = random.Random(4712)
        perm = []
        for _ in range(10000):
            rng.shuffle(vals)
            perm.append(score(word, [(l, n, vals[i]) for i, (l, n, _) in enumerate(items)])[0])
    rng = random.Random(71)
    rnd = [score(word, [(l, rng.randint(*RANGE[l]), v) for l, _, v in items])[0] for _ in range(10000)]
    pp, pr = p95(perm), p95(rnd)
    print(f"G2 REAL {mt} match, {k} conflict, {len(items) - sc} absent | SHARE {mt}/{sc} = {share:.3f} | permutation"
          f" ({len(perm)}) p95 {pp} max {max(perm)} | random-code (10000) p95 {pr} max {max(rnd)}")
    if sc < 8:
        print("G2 NON-TEST")
        sys.exit(4)
    ok = share >= 0.80 and mt > pp and mt > pr
    print("G2", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 3)


if __name__ == "__main__":
    main()
