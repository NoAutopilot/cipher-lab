#!/usr/bin/env python3
"""HEID-1621G: build unit tables from the reconciled token lines, the 375-vs-379 control and the pooled unit inventory.

usage: python3 units.py [--check]
Inputs (this folder): recon_375.txt, recon_423.txt -- one line per crop line: "Lnn<TAB>tok tok ...", where a token is a number, a
letter, [clear...] or [sym...]; a reader split is written "A|B" (A = reconciled reading, B = the other reader's), which makes the
unit M. ../ciphertext.tsv (scan 379, HEID-1621) is the control reference.
Unit grammar (PREREG-HEID1621G.md): a maximal run of numerals closed by one letter; a run closed by [clear]/[sym]/block end is N; a
letter with no numeral before it is L. Unit id = numbers joined by '.' + '.' + lower-cased letter (N: numbers + '.-'; L: '-.' + letter).
Outputs: ciphertext_6021_375.tsv, ciphertext_6021_423.tsv, agree_375_379.tsv, units.tsv. --check rebuilds in memory and exits 1 if
any committed output differs. No values are read; nothing here decodes.
"""
import sys, os, difflib, csv, io
H = os.path.dirname(os.path.abspath(__file__))

def is_num(t): return t.isdigit()
def is_let(t): return len(t) == 1 and t.isalpha()

def units_from_tokens(seq):
    """seq: list of (line, pos, tok, alt). Returns unit dicts."""
    out, run = [], []
    def flush(letter=None, why_close=""):
        nonlocal run
        if not run and letter is None: return
        toks = run + ([letter] if letter else [])
        nums = [t[2] for t in run]
        let = letter[2].lower() if letter else ""
        form = ("P" if len(nums) == 2 else "S1" if len(nums) == 1 else "L" if not nums else "R%d" % len(nums)) if letter else "N"
        uid = (".".join(nums) if nums else "-") + "." + (let if let else "-")
        splits = [f"{t[2]}|{t[3]}" for t in toks if t[3]]
        out.append(dict(line=toks[0][0], pos=toks[0][1], unit=uid, form=form, numbers=".".join(nums), letter=let,
                        confidence="M" if splits else "S", why=("readers split " + ",".join(splits)) if splits else "two readers agree"))
        run = []
    for t in seq:
        if is_num(t[2]): run.append(t)
        elif is_let(t[2]): flush(t)
        else: flush()
    flush()
    return out

def read_recon(name):
    seq = []
    for ln in open(os.path.join(H, name), encoding="utf-8"):
        if not ln.strip() or ln.startswith("#"): continue
        line, rest = ln.rstrip("\n").split("\t", 1)
        pos = 0; buf = []
        for tok in rest.replace("] ", "]\x00").replace(" [", "\x00[").split("\x00"):
            buf += [tok] if tok.startswith("[") else tok.split()
        for tok in buf:
            pos += 1
            a, b = (tok.split("|", 1) + [""])[:2] if not tok.startswith("[") else (tok, "")
            seq.append((line, pos, a, b))
    return seq

def read_379():
    seq = []
    for r in csv.reader((l for l in open(os.path.join(H, "..", "ciphertext.tsv"), encoding="utf-8") if not l.startswith("#")), delimiter="\t"):
        if r[0] == "line": continue
        tok = "[clear]" if r[2] == "word" else ("[sym]" if r[2] == "sym" else r[3])
        seq.append((r[0], int(r[1]), tok, r[4] if len(r) > 4 else ""))
    return seq

def tsv(rows, cols):
    s = io.StringIO(); s.write("\t".join(cols) + "\n")
    for r in rows: s.write("\t".join(str(r[c]) for c in cols) + "\n")
    return s.getvalue()

def build():
    files = {}
    u375, u423, u379 = units_from_tokens(read_recon("recon_375.txt")), units_from_tokens(read_recon("recon_423.txt")), units_from_tokens(read_379())
    cols = ["line", "pos", "unit", "form", "numbers", "letter", "confidence", "why"]
    hdr = "# NL-HaNA 1.01.02 inv. 6021 scan %s, HEID-1621G (15 Oct 2026): two blind Sonnet readers + reconciliation on line crops; S = both readers agree on the signs as transcribed (no value read), M = split.\n"
    a, b = [u["unit"] for u in u375], [u["unit"] for u in u379]
    gate = difflib.SequenceMatcher(None, a, b, autojunk=False)
    gate_ok = sum(bl.size for bl in gate.get_matching_blocks()) / max(len(a), len(b)) >= 0.90
    if not gate_ok:  # PREREG: below the gate the pass is a non-test; grade both blocks M throughout
        for u in u375 + u423:
            if u["confidence"] == "S": u["confidence"], u["why"] = "M", "two readers agree; control below gate (PREREG), M"
            else: u["why"] += "; control below gate, M"
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    rows = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        for k in range(max(i2 - i1, j2 - j1)):
            x = u375[i1 + k] if i1 + k < i2 else None; y = u379[j1 + k] if j1 + k < j2 else None
            rows.append(dict(op=op, u375=x["unit"] if x else "", line375=x["line"] if x else "", conf375=x["confidence"] if x else "",
                             u379=y["unit"] if y else "", line379=y["line"] if y else "", conf379=y["confidence"] if y else ""))
    files["ciphertext_6021_375.tsv"] = hdr % "375 (13 Aug 1621, signed letter)" + tsv(u375, cols)
    files["ciphertext_6021_423.tsv"] = hdr % "423 (17 Sept 1621)" + tsv(u423, cols)
    match = sum(1 for r in rows if r["op"] == "equal")
    agree = match / max(len(a), len(b))
    # per-token: numbers and letters separately, over aligned replace pairs and equal units
    nt = nm = lt = lm = 0
    for r in rows:
        if r["u375"] and r["u379"]:
            p, q = r["u375"].split("."), r["u379"].split(".")
            pn, qn = p[:-1], q[:-1]
            if len(pn) == len(qn):
                nt += len(pn); nm += sum(x == y for x, y in zip(pn, qn))
            lt += 1; lm += p[-1] == q[-1]
    summ = f"# per-unit agreement 375 vs 379: {match}/{max(len(a), len(b))} = {agree:.3f} (gate 0.90); units 375={len(a)} 379={len(b)}; " \
           f"numbers in aligned same-length units {nm}/{nt}; letters in aligned units {lm}/{lt}\n"
    NORM = {"r": "x", "c": "x", "w": "e", "j": "s", "f": "s", "b": "s"}  # POST-HOC glyph-convention classes seen in the diffs; not the gate
    na = [u[:-1] + NORM.get(u[-1], u[-1]) for u in a]; nb = [u[:-1] + NORM.get(u[-1], u[-1]) for u in b]
    nmatch = sum(bl.size for bl in difflib.SequenceMatcher(None, na, nb, autojunk=False).get_matching_blocks())
    summ += f"# PREREG gate {'PASS' if gate_ok else 'FAIL: the pass is a non-test for letter identity; every unit graded M'}. " \
            f"Post-hoc only (not the gate): numbers alone agree as above; letters merged by glyph-convention class {NORM} -> {nmatch}/{max(len(a), len(b))} = {nmatch / max(len(a), len(b)):.3f}\n"
    files["agree_375_379.tsv"] = summ + tsv(rows, ["op", "u375", "line375", "conf375", "u379", "line379", "conf379"])
    inv = {}
    for name, us in (("n_13aug", u375), ("n_17sept", u423)):
        for u in us:
            d = inv.setdefault(u["unit"], dict(unit=u["unit"], form=u["form"], numbers=u["numbers"], letter=u["letter"], n_13aug=0, n_17sept=0))
            d[name] += 1
    rows = sorted(inv.values(), key=lambda d: (d["letter"], [int(x) for x in d["numbers"].split(".") if x] or [0]))
    shared = sum(1 for d in rows if d["n_13aug"] and d["n_17sept"])
    # fixed question: S1 units of 423 whose number is the first number of a P unit of 375/379 with the same letter
    pfirst = {(u["numbers"].split(".")[0], u["letter"]) for u in u375 + u379 if u["form"] == "P"}
    s1 = [u for u in u423 if u["form"] == "S1"]
    hit = [u for u in s1 if (u["numbers"], u["letter"]) in pfirst]
    pany = {(n, u["letter"]) for u in u375 + u379 if u["form"] == "P" for n in u["numbers"].split(".")}
    hit2 = [u for u in s1 if (u["numbers"], u["letter"]) in pany]
    s = ("" if gate_ok else "# NO INVENTORY CLAIM (PREREG): the 375-vs-379 control is below its 0.90 gate; counts below are M, for planning only.\n") + f"# 13 Aug = scan 375 reconciled; 17 Sept = scan 423 reconciled. distinct units {len(rows)}; shared by both letters {shared}; " \
        f"423 S1 units whose number is the FIRST number of a 13 Aug P unit with the same letter: {len(hit)}/{len(s1)} " \
        f"({','.join(u['unit'] for u in s1 if u not in hit)} not); either number: {len(hit2)}/{len(s1)}\n"
    files["units.tsv"] = s + tsv(rows, ["unit", "form", "numbers", "letter", "n_13aug", "n_17sept"])
    return files

if __name__ == "__main__":
    files = build()
    if "--check" in sys.argv:
        bad = [f for f, c in files.items() if not os.path.exists(os.path.join(H, f)) or open(os.path.join(H, f), encoding="utf-8").read() != c]
        print("stale:" if bad else "ok: outputs reproduce", *bad); sys.exit(1 if bad else 0)
    for f, c in files.items(): open(os.path.join(H, f), "w", encoding="utf-8").write(c)
    for f in files: print(f, open(os.path.join(H, f)).readline().rstrip())
