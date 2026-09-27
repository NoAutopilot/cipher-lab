#!/usr/bin/env python3
"""Known-plaintext key re-derivation from the clerk's interlinear decipherment of f.260r (VB-KEY, 27 Sept 2026).

  python3 kp_key_v3.py merge      passes/f260_S*[AB].tsv -> ciphertext_f260.txt, plaintext_f260.txt, aligned_f260.tsv
  python3 kp_key_v3.py key        aligned_f260.tsv + ../keys/key_f275_v2.tsv -> ../keys/key_f275_v3.tsv
  python3 kp_key_v3.py holdout    leave-one-line-out on f.260, and f.260-derived key on f.258 (VB-KP files)
  python3 kp_key_v3.py --check    exit 1 if any of the four written files is stale

Instead of aligning a clerk letter stream to a cipher stream after the fact (interlinear_align.py's DP), each blind
pass reads, per cipher sign, the gloss letters the clerk wrote directly above it: the pairing is read off the page.
Two passes (A, B) per line; sign sequences are aligned with difflib. A (sign, clerk) pair is used for the key only
where both passes gave the same sign id AND the same clerk letters (normalized: lower case, j->i, v->u, letters
only; '-' = nothing written above). Stretches where the passes differ keep pass A's tokens in the merged ciphertext
(ties to A, the VB-KP rule without confidences) but give no key evidence.
Key rule: per sign, value = the clerk reading attested most often; count and agreement (share of the majority) kept,
with the f.260 line numbers. A sign never attested keeps its v2 row (count 0). A sign whose majority is '-' in 2 or
more occurrences becomes a null. Grade: C (every value is the clerk's).
Hold-out (rule 3): a line's letter agreement with the clerk is measured with a key built without that line, and set
against the same measure under 20 class-shuffled copies of that key (decode_f275.shuffled, same seed) -- a control
that can differ from the target, since the shuffle moves values between signs of one kind.
"""
import collections
import difflib
import importlib.util
import random
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PASSES = sorted((HERE / "passes").glob("f260_S*[AB].tsv"))
CIPH, PLAIN, ALIGN = HERE / "ciphertext_f260.txt", HERE / "plaintext_f260.txt", HERE / "aligned_f260.tsv"
V2, V3 = HERE.parent / "keys" / "key_f275_v2.tsv", HERE.parent / "keys" / "key_f275_v3.tsv"
NUM = re.compile(r"^\^?\d+$")

spec = importlib.util.spec_from_file_location("cc", HERE / "compare_clerk.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)
dec = cc.dec


def norm(s):
    s = s.strip()
    return "-" if s in ("-", "") else cc.norm(s)


def read_pass(p):
    lines = collections.defaultdict(list)
    for ln in open(p, encoding="utf-8"):
        f = ln.rstrip("\n").split("\t")
        if len(f) < 3 or not f[0].strip().isdigit():
            continue
        lines[int(f[0])].append((f[2].strip(), f[3] if len(f) > 3 else "?"))
    return lines


def merge_rows():
    A, B = collections.defaultdict(list), collections.defaultdict(list)
    for p in PASSES:
        (A if p.stem.endswith("A") else B).update(read_pass(p))
    rows = []
    for n in sorted(set(A) | set(B)):
        a, b = A.get(n, []), B.get(n, [])
        sm = difflib.SequenceMatcher(a=[s for s, _ in a], b=[s for s, _ in b], autojunk=False)
        pos = 0
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                for (s, ca), (_, cb) in zip(a[i1:i2], b[j1:j2]):
                    pos += 1
                    rows.append((n, pos, s, ca, cb, "AB"))
            elif op in ("replace", "delete") or (op == "insert" and not a):
                src = a[i1:i2] if a else b[j1:j2]
                for s, c in src:
                    pos += 1
                    rows.append((n, pos, s, c, "", "A" if a else "B"))
    return rows


def load_align():
    rows = []
    for ln in open(ALIGN, encoding="utf-8"):
        if ln.startswith("#") or ln.startswith("line\t"):
            continue
        n, pos, s, ca, cb, g = ln.rstrip("\n").split("\t")
        rows.append((int(n), int(pos), s, ca, cb, g))
    return rows


def merge_texts(rows):
    head = ("# Known-plaintext sibling, BnF fr.7129 f.260r (Gallica btv1b8555834s canvas f525), lower cipher block, 12\n"
            "# lines (native y 2381-4355) under the clerk's interlinear gloss. VB-KEY, 27 Sept 2026. Two blind Sonnet\n"
            "# passes (sibling/passes/f260_S<set><A|B>.tsv), each reading per cipher sign the sign id (inventory.txt) and\n"
            "# the gloss letters directly above it; merged by kp_key_v3.py (A=B kept, else pass A). Line numbers count\n"
            "# the block's lines from its first (the line under 'aitreueillez & peutestre'). Scratch crops only.\n")
    ciph = [head + "side\tline\tpos\ttoken\tagree"] + [f"r\t{n}\t{p}\t{s}\t{g}" for n, p, s, ca, cb, g in rows]
    per = collections.OrderedDict()
    for n, p, s, ca, cb, g in rows:
        per.setdefault(n, []).append(ca if ca.strip() not in ("-", "?") else "")
    plain = [head.replace("Two blind", "Clerk text = pass A's gloss letters per sign, joined; two blind") +
             "# Literal gloss letters, not our reading; a period decipherment.\nline\tclerk"]
    plain += [f"{n}\t{' '.join(x for x in v if x)}" for n, v in per.items()]
    al = [head + "line\tpos\tsign\tclerkA\tclerkB\tagree"] + ["\t".join(map(str, r)) for r in rows]
    return "\n".join(ciph) + "\n", "\n".join(plain) + "\n", "\n".join(al) + "\n"


def pairs(rows, skip=None):
    out = []
    for n, p, s, ca, cb, g in rows:
        if g != "AB" or n == skip:
            continue
        va, vb = norm(ca), norm(cb)
        if va == vb and va != "" and "?" not in ca + cb:
            out.append((s, va, n))
    return out


def v2_rows():
    rows = collections.OrderedDict()
    for ln in open(V2, encoding="utf-8"):
        if ln.startswith("#") or ln.startswith("sign\t"):
            continue
        f = ln.rstrip("\n").split("\t")
        f += [""] * (7 - len(f))
        rows.setdefault(f[0], f[:7])  # first row wins (v2 has 6 and 8 twice; letter rows come first)
    return rows


def build(prs):
    by = collections.defaultdict(collections.Counter)
    src = collections.defaultdict(set)
    for s, v, n in prs:
        by[s][v] += 1
        src[s].add(n)
    v2 = v2_rows()
    out = collections.OrderedDict()
    for s in list(v2) + sorted(set(by) - set(v2)):
        old = v2.get(s)
        if s in by:
            val, c = by[s].most_common(1)[0]
            tot = sum(by[s].values())
            if val == "-":
                kind, val = ("null", "") if c >= 2 else ("letter", "?")
            else:
                kind = "word" if (NUM.match(s) and len(val) > 1) else "letter"
            oldv = norm(old[1]) if old and old[1] not in ("", "?") else ""
            if not old:
                flag = "new"
            elif old[1] in ("", "?") or old[5] == "1":
                flag = "v2-unclear" if oldv != (val if kind != "null" else "") else "confirmed-unclear"
            else:
                flag = "confirmed" if oldv == (val if kind != "null" else "") and old[2] == kind else "changed"
            alts = ",".join(f"{k}:{n}" for k, n in by[s].most_common())
            note = f"clerk f.260 {alts}; v2 {old[1] + '/' + old[2] if old else 'absent'}"
            out[s] = [s, val, kind, "260r", "clerk", "0" if c >= 2 and c / tot >= 0.6 else "1", note, str(tot),
                      f"{c / tot:.2f}", ",".join(map(str, sorted(src[s]))), flag]
        else:
            out[s] = old + ["0", "", "", "v2-kept"]
    return out


def key_text(k):
    head = ("# Bongars cipher no.3 (fr.7129 f.275) key re-derived from the clerk's interlinear decipherment of the sibling\n"
            "# f.260r (VB-KEY, 27 Sept 2026; sibling/kp_key_v3.py key). Grade C: every attested value is the clerk's. Columns\n"
            "# 1-7 as key_f275_v2.tsv (decode_f275.py reads them); count = pairs where both passes agree on sign and gloss;\n"
            "# agree = share of the majority value; lines = f.260 lines attesting it; flag: confirmed / changed (clerk\n"
            "# contradicts v2) / v2-unclear (v2 had it unclear or blank, clerk gives another value) / confirmed-unclear /\n"
            "# new (sign absent from v2) / v2-kept (never attested by the clerk: v2's value kept). unclear=1 when count 1 or\n"
            "# agreement under 0.6.\n")
    cols = "sign\tvalue\tkind\tfolio\tcolumn\tunclear\tnote\tcount\tagree\tlines\tflag"
    return head + cols + "\n" + "\n".join("\t".join(r) for r in k.values()) + "\n"


def as_key(k):
    return {s: {"value": r[1], "kind": r[2], "unclear": r[5]} for s, r in k.items()}


def holdout():
    rows = load_align()
    lines = collections.OrderedDict()
    for n, p, s, ca, cb, g in rows:
        lines.setdefault(n, []).append(s)
    clerk = {n: t for n, t in (l.split("\t", 1) for l in PLAIN.read_text().splitlines()
                               if l and not l.startswith("#") and not l.startswith("line\t"))}
    tm = tc = 0
    shuf_m = [0] * dec.N_SHUF
    print("leave-one-line-out on f.260 (key from the other 11 lines + v2 fallback):")
    for n, toks in lines.items():
        key = as_key(build(pairs(rows, skip=n)))
        one = {n: toks}
        c = {n: clerk[str(n)]}
        r, *_ , per, _ = cc.score(one, c, key)
        m, lc = per[0][1], per[0][2]
        rnd = random.Random(dec.SEED)
        sl = []
        for i in range(dec.N_SHUF):
            sk = dec.shuffled(key, rnd)
            per_s = cc.score(one, c, sk)[3]
            shuf_m[i] += per_s[0][1]
            sl.append(per_s[0][1] / max(lc, 1))
        tm, tc = tm + m, tc + lc
        mu, sd = statistics.mean(sl), statistics.pstdev(sl) or 1e-9
        print(f"  line {n}: {m}/{lc} = {m / max(lc, 1):.3f}; shuffled {mu:.3f}+-{sd:.3f}; z {(m / lc - mu) / sd:.2f}")
    sa = [x / tc for x in shuf_m]
    mu, sd = statistics.mean(sa), statistics.pstdev(sa)
    print(f"f.260 held-out letter agreement {tm}/{tc} = {tm / tc:.3f}; 20 class-shuffled keys mean {mu:.3f} sd {sd:.3f}"
          f" max {max(sa):.3f}; z {(tm / tc - mu) / sd:.2f}")
    # f.260 -> f.258 (VB-KP's transcription of f.258r block 1, lines 2-6): no f.258 data went into this key
    key = as_key(build(pairs(rows)))
    l258, c258 = cc.load(HERE / "ciphertext_f258.txt", HERE / "plaintext_f258.txt")
    real, conf, valued, per, _ = cc.score(l258, c258, key)
    rnd = random.Random(dec.SEED)
    sh = [cc.score(l258, c258, dec.shuffled(key, rnd))[0] for _ in range(dec.N_SHUF)]
    mu, sd = statistics.mean(sh), statistics.pstdev(sh)
    print(f"f.258 (held out entirely) letter agreement {real:.3f}; shuffled mean {mu:.3f} sd {sd:.3f} max {max(sh):.3f};"
          f" z {(real - mu) / sd:.2f}  [VB-KP with key v2: 0.467]")
    for n, m, lc, d, c in per:
        print(f"  f258 line {n}: {m}/{lc} ({100 * m / max(lc, 1):.0f}%)")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "--help"
    if cmd == "merge":
        c, p, a = merge_texts(merge_rows())
        CIPH.write_text(c), PLAIN.write_text(p), ALIGN.write_text(a)
        rows = load_align()
        for n in sorted({r[0] for r in rows}):
            lr = [r for r in rows if r[0] == n]
            ab = sum(r[5] == "AB" for r in lr)
            cl = sum(1 for r in lr if r[5] == "AB" and norm(r[3]) == norm(r[4]))
            print(f"line {n}: merged {len(lr)}, signs A=B {ab} ({100 * ab / len(lr):.0f}%), sign+gloss A=B {cl}")
        print(f"all: merged {len(rows)}, sign A=B {sum(r[5] == 'AB' for r in rows)}, usable pairs {len(pairs(rows))}")
    elif cmd == "key":
        k = build(pairs(load_align()))
        V3.write_text(key_text(k))
        fl = collections.Counter(r[10] for r in k.values())
        print(dict(fl), "attested>=2:", sum(1 for r in k.values() if r[7] not in ("", "0", "1")))
    elif cmd == "holdout":
        holdout()
    elif cmd == "--check":
        c, p, a = merge_texts(merge_rows())
        stale = [f.name for f, t in ((CIPH, c), (PLAIN, p), (ALIGN, a)) if f.read_text() != t]
        if V3.read_text() != key_text(build(pairs(load_align()))):
            stale.append(V3.name)
        print("stale: " + ", ".join(stale) if stale else "ok")
        sys.exit(1 if stale else 0)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
