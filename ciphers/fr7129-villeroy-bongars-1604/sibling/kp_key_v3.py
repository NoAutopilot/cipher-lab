#!/usr/bin/env python3
"""Known-plaintext key re-derivation from the clerk's interlinear decipherment of f.260r (VB-KEY, 27 Sept 2026).

  python3 kp_key_v3.py merge      passes/f260_S*[AB].tsv -> ciphertext_f260.txt, plaintext_f260.txt, aligned_f260.tsv
  python3 kp_key_v3.py key        hard-EM pairs (f.258 + f.260, v2 seed) -> ../keys/key_f275_v3.tsv
  python3 kp_key_v3.py holdout    per-pass pairing: leave-one-line-out on f.260, and the f.260 key on f.258
  python3 kp_key_v3.py holdout-em hard-EM line alignment: leave-one-line-out over f.258 + f.260 (the test of record)
  python3 kp_key_v3.py --check    exit 1 if any of the four written files is stale

Instead of aligning a clerk letter stream to a cipher stream after the fact (interlinear_align.py's DP), each blind
pass reads, per cipher sign, the gloss letters the clerk wrote directly above it: the pairing is read off the page.
Two passes (A, B) per line; sign sequences are aligned with difflib. The two passes pair gloss and signs at different offsets (VB-KEY: only
9 of 328 merged positions agree on both sign and gloss), so the key uses every pass row as one observation (normalized:
lower case, j->i, v->u, letters only; '-' = nothing written above) and takes the majority per sign; the hold-out
below, not the pairing, is the test. Stretches where the passes differ keep pass A's tokens in the merged ciphertext
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


def gloss_copy(line):
    """A pass line whose sign column mostly repeats its own gloss column read the gloss row as cipher (seen on f.260
    line 5, pass A: 'p=p r=r e=e t=t ...'). Such a pass line is dropped; the other pass stands alone."""
    same = sum(1 for s, c in line if s.isalpha() and norm(s) == norm(c))
    return bool(line) and same / len(line) > 0.25


def merge_rows():
    A, B = collections.defaultdict(list), collections.defaultdict(list)
    for p in PASSES:
        (A if p.stem.endswith("A") else B).update(read_pass(p))
    rows = []
    for n in sorted(set(A) | set(B)):
        a, b = A.get(n, []), B.get(n, [])
        a, b = (x if not gloss_copy(x) else [] for x in (a, b))
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


def pairs(rows=None, skip=None):
    """(sign, clerk value, line) observations: every row of every pass (each pass's own reading of which gloss letters
    stand above which sign), gloss-copy pass lines dropped, '?' signs or glosses dropped. The line `skip` is left out
    (both passes) for the hold-out. `rows` is unused (kept for the call sites)."""
    out = []
    for p in PASSES:
        for n, line in read_pass(p).items():
            if n == skip or gloss_copy(line):
                continue
            for s, c in line:
                v = norm(c)
                if s != "?" and "?" not in c and v != "":
                    out.append((s, v, n))
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
            note = f"clerk {alts}; v2 {old[1] + '/' + old[2] if old else 'absent'}"
            out[s] = [s, val, kind, "260r", "clerk", "0" if c >= 2 and c / tot >= 0.6 else "1", note, str(tot),
                      f"{c / tot:.2f}", ",".join(map(str, sorted(src[s]))), flag]
        else:
            out[s] = old + ["0", "", "", "v2-kept"]
    return out


def key_text(k):
    head = ("# Bongars cipher no.3 (fr.7129 f.275) key re-derived from the clerk's interlinear decipherment of the sibling\n"
            "# f.260r and f.258r (VB-KEY, 27 Sept 2026; sibling/kp_key_v3.py key, hard-EM alignment of each line's signs to\n# the clerk's letters, v2 seeding round 1). Grade C: every attested value is the clerk's. Columns\n"
            "# 1-7 as key_f275_v2.tsv (decode_f275.py reads them); count = aligned occurrences (f.260 counts each pass's line; f.258 the merged line);\n"
            "# agree = share of the majority value; lines = line numbers attesting it (f.258 2-6 and f.260 1-12 share numbers); flag: confirmed / changed (clerk\n"
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


# ---- hard-EM alignment (VB-KEY, second instrument) ------------------------------------------------------------------
# Each observation is one line: a sign sequence and the clerk's letter stream for that line (f.260: each pass line,
# its own gloss column joined; f.258: VB-KP's merged ciphertext and merged clerk text). A DP gives each sign a chunk
# of the letters -- 0 or 1 letter for a letter-shaped sign (2 for the syllable signs), 0-12 for a number -- scored by
# how often that sign read that chunk elsewhere (v2's value seeds the first round with weight 1). Six rounds. The
# held-out line never enters the counts that decode it.
import math

def observations():
    obs = []
    for p in PASSES:
        for n, line in read_pass(p).items():
            if gloss_copy(line):
                continue
            s = [x for x, _ in line if x != "?"]
            c = "".join(norm(g) for _, g in line if norm(g) not in ("-",) and "?" not in g)
            obs.append((("260", n), s, c))
    l258, c258 = cc.load(HERE / "ciphertext_f258.txt", HERE / "plaintext_f258.txt")
    for n, toks in l258.items():
        obs.append((("258", n), [t for t in toks if t != "?"], cc.norm(c258.get(n, ""))))
    return obs


def maxlen(s):
    return 12 if NUM.match(s) and len(s.lstrip("^")) > 1 else (2 if len(s) > 1 and s.isalpha() else 1)


def align(sig, let, cnt, tot):
    n, m = len(sig), len(let)
    NEG = -1e18
    best = [[NEG] * (m + 1) for _ in range(n + 1)]
    back = [[0] * (m + 1) for _ in range(n + 1)]
    best[0][0] = 0.0
    for i in range(n):
        s = sig[i]
        ml = maxlen(s)
        for j in range(m + 1):
            b = best[i][j]
            if b <= NEG:
                continue
            for k in range(0, ml + 1):
                if j + k > m:
                    break
                ch = let[j:j + k]
                c = cnt.get(s, {}).get(ch, 0)
                sc = math.log((c + 0.1) / (tot.get(s, 0) + 3.0)) + (math.log(0.15) if k == 0 else 0)
                if b + sc > best[i + 1][j + k]:
                    best[i + 1][j + k], back[i + 1][j + k] = b + sc, k
    # letters left over at the end are allowed (clerk may run past the last sign read): take the best end column
    j = max(range(m + 1), key=lambda jj: best[n][jj] - 2.0 * (m - jj))
    out = []
    for i in range(n, 0, -1):
        k = back[i][j]
        out.append((sig[i - 1], let[j - k:j] if k else "-"))
        j -= k
    return out[::-1]


def em_pairs(skip=None, rounds=6):
    obs = [o for o in observations() if o[0] != skip]
    cnt, tot = collections.defaultdict(collections.Counter), collections.Counter()
    for s, r in v2_rows().items():
        if r[1] not in ("", "?"):
            cnt[s][norm(r[1])] += 1
            tot[s] += 1
    for _ in range(rounds):
        prs = [(s, v, key[1]) for key, sig, let in obs for s, v in align(sig, let, cnt, tot)]
        cnt, tot = collections.defaultdict(collections.Counter), collections.Counter()
        for s, v, _ in prs:
            cnt[s][v] += 1
            tot[s] += 1
    return prs


def holdout_em():
    obs = observations()
    tm = tc = 0
    shuf = [0] * dec.N_SHUF
    for key_, sig, let in obs:
        if key_[0] == "258":
            k = as_key(build(em_pairs(skip=key_)))
        else:  # leave the line out of both passes
            k = as_key(build([p for p in em_pairs(skip=key_) if True]))
        one, c = {0: sig}, {0: let}
        per = cc.score(one, c, k)[3]
        m, lc = per[0][1], per[0][2]
        rnd = random.Random(dec.SEED)
        sl = []
        for i in range(dec.N_SHUF):
            x = cc.score(one, c, dec.shuffled(k, rnd))[3][0][1]
            shuf[i] += x
            sl.append(x / max(lc, 1))
        tm, tc = tm + m, tc + lc
        mu, sd = statistics.mean(sl), statistics.pstdev(sl) or 1e-9
        print(f"  {key_[0]} line {key_[1]}: {m}/{lc} = {m / max(lc, 1):.3f}; shuffled {mu:.3f}+-{sd:.3f}; z {(m / max(lc,1) - mu) / sd:.2f}")
    sa = [x / tc for x in shuf]
    mu, sd = statistics.mean(sa), statistics.pstdev(sa)
    print(f"EM held-out letter agreement {tm}/{tc} = {tm / tc:.3f}; 20 class-shuffled keys mean {mu:.3f} sd {sd:.3f} "
          f"max {max(sa):.3f}; z {(tm / tc - mu) / sd:.2f}")


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
        k = build(em_pairs())
        V3.write_text(key_text(k))
        fl = collections.Counter(r[10] for r in k.values())
        print(dict(fl), "attested>=2:", sum(1 for r in k.values() if r[7] not in ("", "0", "1")))
    elif cmd == "holdout":
        holdout()
    elif cmd == "holdout-em":
        holdout_em()
    elif cmd == "--check":
        c, p, a = merge_texts(merge_rows())
        stale = [f.name for f, t in ((CIPH, c), (PLAIN, p), (ALIGN, a)) if f.read_text() != t]
        if V3.read_text() != key_text(build(em_pairs())):
            stale.append(V3.name)
        print("stale: " + ", ".join(stale) if stale else "ok")
        sys.exit(1 if stale else 0)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
