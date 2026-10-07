#!/usr/bin/env python3
"""Gloss-in-view f.260r transcription -> shared-tool key -> M9 hold-out (D4-VILL2, 7 Oct 2026; PREREG-D4-VILL2.md).

  python3 vill2_align.py run      reconcile passes_r2/C_L*.tsv -> pairs_r2_f260.tsv; key_r2_f260.tsv; P1, P2, families
  python3 vill2_align.py --check  exit 1 if pairs_r2_f260.tsv / key_r2_f260.tsv are stale

Reader (R_L<NN>.tsv) and checker (C_L<NN>.tsv) passes over sibling/f260r_crops/p260_L<NN>_s1|s2.jpg; the checker file
carries every reader row with the checked values and a verdict (ok/fix/del/ins/unsure). Reconciled line = checker rows
minus 'del', in pos order ('unsure' rows keep the reader's values, which the checker leaves in place). The key comes from
tools/interlinear_align.py exactly as shared_align.py (D4-VILL) runs it, then kp_key_v3.build(); the metric and control
are compare_clerk.score and decode_f275.shuffled, as VB-KEY and D4-VILL.
"""
import collections
import csv
import importlib.util
import io
import random
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
P2DIR = HERE / "passes_r2"
PAIRS_OUT, KEY_OUT = HERE / "pairs_r2_f260.tsv", HERE / "key_r2_f260.tsv"

spec = importlib.util.spec_from_file_location("sa", HERE / "shared_align.py")
sa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sa)
kp, cc, dec = sa.kp, sa.cc, sa.dec


def read_tsv(p):
    with open(p, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f, delimiter="\t")]
    return [{k.strip().lower(): (v or "").strip() for k, v in r.items() if k} for r in rows]


def lines():
    """{n: [(sign, gloss, verdict)]} from the checker files; reader-only when a checker file is missing."""
    out, stats = {}, collections.Counter()
    for n in range(1, 14):
        c, r = P2DIR / f"C_L{n:02d}.tsv", P2DIR / f"R_L{n:02d}.tsv"
        src = c if c.exists() else r
        if not src.exists():
            continue
        rows = read_tsv(src)
        rows.sort(key=lambda x: float(x.get("pos") or 0))
        keep = []
        for x in rows:
            v = (x.get("chk") or "reader").lower()
            stats[v] += 1
            if v == "del" or not x.get("sign"):
                continue
            keep.append((x["sign"].replace(" ", ""), x.get("gloss", "") or "-", v))
        out[n] = keep
    return out, stats


def obs_new(L):
    """One observation per new line: (('260n', n), signs, clerk letters normalized)."""
    obs = []
    for n, rows in L.items():
        sig = [s for s, _, _ in rows if s != "?"]
        let = "".join(kp.norm(g) for _, g, _ in rows if kp.norm(g) != "-" and "?" not in g)
        obs.append((("260n", n), sig, let))
    return obs


def pairs_rows(obs):
    return [{"plain_line": f"260:{o[0][1]}:{i}", "plain_raw": o[2], "cipher_line": f"260:{o[0][1]}:{i}",
             "cipher_raw": " ".join(sa.enc(s) for s in o[1])} for i, o in enumerate(obs)]


def key_from(obs):
    return kp.as_key(kp.build(sa.to_prs(sa.align(pairs_rows(obs))[0])))


def score(tests, label):
    """tests: [(name, signs, clerk, key)]; prints per-test, total, 20 class-shuffled control."""
    tm = tc = 0
    shuf = [0] * dec.N_SHUF
    for name, sig, let, k in tests:
        one, c = {0: sig}, {0: let}
        per = cc.score(one, c, k)[3]
        m, lc = per[0][1], per[0][2]
        rnd = random.Random(dec.SEED)
        for i in range(dec.N_SHUF):
            shuf[i] += cc.score(one, c, dec.shuffled(k, rnd))[3][0][1]
        tm, tc = tm + m, tc + lc
        print(f"  [{label}] {name}: {m}/{lc} = {m / max(lc, 1):.3f}", flush=True)
    sa_ = [x / tc for x in shuf]
    mu, sd = statistics.mean(sa_), statistics.pstdev(sa_)
    print(f"{label}: held-out letter agreement {tm}/{tc} = {tm / tc:.3f}; 20 class-shuffled keys mean {mu:.3f} sd "
          f"{sd:.3f} max {max(sa_):.3f}; z {(tm / tc - mu) / sd:.2f}; gate 0.70 {'MET' if tm / tc >= 0.70 else 'NOT met'}")
    return tm / tc


def outputs(L):
    obs = obs_new(L)
    rows = pairs_rows(obs)
    arows, ktxt, _ = sa.align(rows)
    s = io.StringIO()
    s.write("# D4-VILL2 vill2_align.py: f.260r lower block L01-L13, gloss-in-view reader + checker, reconciled; sign-aligned\n"
            "# pairs as read off the page (gloss = clerk letters directly above the sign; grade C, the clerk's values)\n")
    w = csv.writer(s, delimiter="\t", lineterminator="\n")
    w.writerow(["line", "pos", "sign", "gloss", "verdict"])
    for n, rr in L.items():
        for i, (sg, g, v) in enumerate(rr, 1):
            w.writerow([n, i, sg, g, v])
    khead = "# D4-VILL2 vill2_align.py: tools/interlinear_align.py key on the gloss-in-view f.260r pairs (grade C, the clerk's)\n"
    return s.getvalue(), khead + ktxt, arows, obs


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "--help"
    L, stats = lines()
    if cmd == "run":
        ptxt, ktxt, arows, newobs = outputs(L)
        PAIRS_OUT.write_text(ptxt)
        KEY_OUT.write_text(ktxt)
        print("verdicts:", dict(stats), "| lines:", {n: len(r) for n, r in L.items()})
        print("families (shared tool on the new pairs):")
        sa.families(sa.to_prs(arows))
        # direct read-off pairing (descriptive): majority of the gloss chunk read above each sign
        by = collections.defaultdict(collections.Counter)
        for rr in L.values():
            for sg, g, _ in rr:
                by[sg][kp.norm(g)] += 1
        print("direct read-off pairing, families:")
        for f in sa.FAMILIES:
            c = by.get(f)
            if c:
                n = sum(c.values())
                print(f"  {f}\t{n}\t{', '.join(f'{v}:{x}' for v, x in c.most_common(4))}\t({c.most_common(1)[0][1] / n:.2f})")
        # P1: M9 hold-out of record
        tests = []
        for key_, sig, let in kp.observations():
            if key_[0] == "260":
                n = key_[1]
                train = [o for o in newobs if o[0][1] not in (n - 1, n, n + 1)]
            else:
                train = newobs
            tests.append((f"{key_[0]} line {key_[1]}", sig, let, key_from(train)))
        p1 = score(tests, "P1 M9 hold-out (VB-KEY 28 obs)")
        # P2: leave-one-line-out inside the new transcription
        tests = [(f"new L{o[0][1]:02d}", o[1], o[2], key_from([x for x in newobs if x[0] != o[0]])) for o in newobs]
        p2 = score(tests, "P2 new-transcription leave-one-line-out")
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "p.tsv"
            sa.write_pairs(pairs_rows(newobs), p)
            sa.prior_file(Path(td) / "prior.tsv")
            r = subprocess.run([sys.executable, str(sa.TOOL), "align", str(p), str(Path(td) / "a.tsv"),
                                str(Path(td) / "k.tsv"), "--code-prefix", "@", "--word-code-prefix", "%",
                                "--code-chunk", "2", "--max-chunk", "12", "--keep-fs", "--prior",
                                str(Path(td) / "prior.tsv"), "--shuffle", "20"], capture_output=True, text=True)
            print("shared-tool --shuffle 20:", r.stdout.strip().splitlines()[-3:] if r.stdout else r.stderr[-400:])
        print(f"SUMMARY P1 {p1:.3f} P2 {p2:.3f} (gate 0.70)")
    elif cmd == "--check":
        ptxt, ktxt, _, _ = outputs(L)
        stale = [f.name for f, t in ((PAIRS_OUT, ptxt), (KEY_OUT, ktxt)) if not f.exists() or f.read_text() != t]
        print("stale: " + ", ".join(stale) if stale else "ok")
        sys.exit(1 if stale else 0)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
