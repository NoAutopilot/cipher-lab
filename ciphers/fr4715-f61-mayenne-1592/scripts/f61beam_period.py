#!/usr/bin/env python3
"""F61-BEAM-PERIOD (campaign step H130, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. On the two
long period-glossed family leaves H129 ranks first in f.61's cells (f.101r, f.188r), the 4-gram beam's within-pair choice
(14-cell map; scripts/f61hash4_108r.resolve) is scored against the period decipherer's letter aligned under each sign
(family/passes/<leaf>_align.tsv, plain_chunk, a single letter). Lines = the align file's code rows in order (clear rows
dropped). Scored only where the period letter lies in the sign's pair; baseline always-first-letter. Pre-registered gate
(CAMPAIGN.md H130): accuracy >= 0.80 on >= 100 positions, pooled over the two leaves. The alignment itself is imperfect
(the align files' own status column) -- misaligned letters fall mostly outside the pair and are not scored.
  -> scripts/f61beam_period_result.txt [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = os.path.abspath(f"{HERE}/../family/passes"); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61hash4_108r as H
jp = H.jp
EXT = "--ext" in ARGS   # H133 (28 Sept 2026): KEY.md period equivalences added (LOOPS = h/u, H24 = i/x, ZBAR = f/s); gate unchanged
def main():
    C = H.J.cells(); out = []; R = N = F = 0
    if EXT: C = dict(C, LOOPS="h/u", H24="i/x", ZBAR="f/s")
    for leaf in ("f101r", "f188r"):
        lines = {}
        for r in csv.DictReader(open(f"{FAM}/{leaf}_align.tsv"), delimiter="\t"):
            if r["kind"] == "code": lines.setdefault(r["cipher_line"], []).append((r["raw"].lstrip("@"), r["plain_chunk"].strip()))
        right = n = first = 0
        for seq in lines.values():
            idx = [k for k, (c, _) in enumerate(seq) if c in C]
            pairs = [tuple(jp.fold(x) for x in C[seq[k][0]].split("/")) for k in idx]
            s, _, _ = H.resolve(pairs)
            for i, k in enumerate(idx):
                t = jp.fold(seq[k][1]) if len(seq[k][1]) == 1 else ""
                if t and t in pairs[i]: n += 1; right += s[i] == t; first += pairs[i][0] == t
        out.append(f"{leaf}: {sum(len(v) for v in lines.values())} code signs; scored {n}; beam right {right}/{n} = {right / n:.3f}; always-first-letter {first / n:.3f}")
        R += right; N += n; F += first
    ok = N >= 100 and R / N >= 0.80
    out.append(f"pooled: beam {R}/{N} = {R / N:.3f}; always-first-letter {F / N:.3f}; GATE H130 (>= 0.80 on >= 100): {'PASS' if ok else 'FAIL'}")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61beam_period{'_ext' if EXT else ''}_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
