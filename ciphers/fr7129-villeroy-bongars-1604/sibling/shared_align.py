#!/usr/bin/env python3
"""Shared-tool known-plaintext alignment of the f.260 / f.258 clerk pairs (D4-VILL, 7 Oct 2026; PREREG-D4-VILL.md).

  python3 shared_align.py run      pairs -> tools/interlinear_align.py -> key_shared.tsv, the two hold-outs, families
  python3 shared_align.py --check  exit 1 if shared_pairs_f260.tsv / key_shared_f260.tsv are stale

Same 28 observations as kp_key_v3.py holdout-em (VB-KEY): f.260 lines 1-12 per blind pass, f.258 lines 2-6. Only the
alignment instrument changes: each observation becomes one PAIRS.tsv row for the shared tool in --code-prefix mode
(2+-digit numerals '%', 0..12 letters; every other sign '@', 0..2 letters; --keep-fs; --prior = v2's single-letter
cells). The tool's per-token chunks are turned into (sign, chunk|'-', line) pairs and passed to kp_key_v3.build(), so
the key rule, the decode and the metric (compare_clerk.score) are VB-KEY's.
"""
import collections
import csv
import importlib.util
import random
import re
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOOL = ROOT / "tools" / "interlinear_align.py"
PAIRS_OUT, KEY_OUT = HERE / "shared_pairs_f260.tsv", HERE / "key_shared_f260.tsv"

spec = importlib.util.spec_from_file_location("kp", HERE / "kp_key_v3.py")
kp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kp)
cc, dec = kp.cc, kp.dec
WORD = re.compile(r"^\^?\d\d+$")
FAMILIES = ["g", "9", "y", "f", "u", "d", "do", "Zt", "ls", "ff", "xff", "1", "2", "4", "6", "7", "8", "^7", "99", "18"]


def enc(s):
    return ("%" if WORD.match(s) else "@") + s


def dec_tok(t):
    return t[1:]


def pairs_rows(obs):
    return [{"plain_line": f"{o[0][0]}:{o[0][1]}:{i}", "plain_raw": o[2],
             "cipher_line": f"{o[0][0]}:{o[0][1]}:{i}", "cipher_raw": " ".join(enc(s) for s in o[1])}
            for i, o in enumerate(obs)]


def write_pairs(rows, path):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["plain_line", "plain_raw", "cipher_line", "cipher_raw"], delimiter="\t",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def prior_file(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("code\tvalue\n")
        for s, r in kp.v2_rows().items():
            v = kp.norm(r[1]) if r[1] not in ("", "?") else ""
            if r[2] == "letter" and len(v) == 1:
                f.write(f"{enc(s)[1:]}\t{v}\n")


def align(rows, extra=()):
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        write_pairs(rows, td / "p.tsv")
        prior_file(td / "prior.tsv")
        cmd = [sys.executable, str(TOOL), "align", str(td / "p.tsv"), str(td / "a.tsv"), str(td / "k.tsv"),
               "--code-prefix", "@", "--word-code-prefix", "%", "--code-chunk", "2", "--max-chunk", "12",
               "--keep-fs", "--prior", str(td / "prior.tsv"), *extra]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stderr)
        out = []
        with open(td / "a.tsv", encoding="utf-8") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                out.append(row)
        return out, (td / "k.tsv").read_text(), r.stdout


def to_prs(arows):
    prs = []
    for r in arows:
        tok = r["raw"]
        if tok[:1] not in "@%":
            continue
        ch = kp.norm(r["plain_chunk"]) if r["plain_chunk"] else "-"
        prs.append((dec_tok(tok), ch or "-", int(r["cipher_line"].split(":")[1])))
    return prs


def holdout(obs, key_obs_filter, label):
    tm = tc = 0
    shuf = [0] * dec.N_SHUF
    for key_, sig, let in obs:
        train = [o for o in obs if key_obs_filter(o) and o[0] != key_]
        k = kp.as_key(kp.build(to_prs(align(pairs_rows(train))[0])))
        one, c = {0: sig}, {0: let}
        per = cc.score(one, c, k)[3]
        m, lc = per[0][1], per[0][2]
        rnd = random.Random(dec.SEED)
        for i in range(dec.N_SHUF):
            shuf[i] += cc.score(one, c, dec.shuffled(k, rnd))[3][0][1]
        tm, tc = tm + m, tc + lc
        print(f"  [{label}] {key_[0]} line {key_[1]}: {m}/{lc} = {m / max(lc, 1):.3f}", flush=True)
    sa = [x / tc for x in shuf]
    mu, sd = statistics.mean(sa), statistics.pstdev(sa)
    print(f"{label}: held-out letter agreement {tm}/{tc} = {tm / tc:.3f}; 20 class-shuffled keys mean {mu:.3f} sd "
          f"{sd:.3f} max {max(sa):.3f}; z {(tm / tc - mu) / sd:.2f}; gate 0.70 {'MET' if tm / tc >= 0.70 else 'NOT met'}")


def families(prs):
    by = collections.defaultdict(collections.Counter)
    for s, v, _ in prs:
        by[s][v] += 1
    v3 = {}
    for ln in open(kp.V3, encoding="utf-8"):
        if ln.startswith("#") or ln.startswith("sign\t"):
            continue
        f = ln.rstrip("\n").split("\t")
        v3.setdefault(f[0], f)
    print("family\tshared n\tshared top (share)\tv3 n\tv3 value (agree)")
    for s in FAMILIES:
        c = by.get(s, collections.Counter())
        n = sum(c.values())
        top = c.most_common(3)
        tops = ", ".join(f"{v}:{x}" for v, x in top)
        sh = f"{top[0][1] / n:.2f}" if n else "-"
        r = v3.get(s, [s, "", "", "", "", "", "", "", ""])
        print(f"{s}\t{n}\t{tops} ({sh})\t{r[7] if len(r) > 7 else ''}\t{r[1]} ({r[8] if len(r) > 8 else ''})")


def full_outputs():
    obs = kp.observations()
    f260 = [o for o in obs if o[0][0] == "260"]
    rows = pairs_rows(f260)
    arows, ktxt, _ = align(rows)
    import io
    s = io.StringIO()
    w = csv.DictWriter(s, fieldnames=["plain_line", "plain_raw", "cipher_line", "cipher_raw"], delimiter="\t",
                       lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    head = "# D4-VILL shared_align.py: f.260 pairs (VB-KEY blind passes) for tools/interlinear_align.py --code-prefix\n"
    khead = "# D4-VILL shared_align.py: tools/interlinear_align.py key on shared_pairs_f260.tsv (grade C, the clerk's)\n"
    return head + s.getvalue(), khead + ktxt, arows, f260


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "--help"
    if cmd == "run":
        ptxt, ktxt, arows, f260 = full_outputs()
        PAIRS_OUT.write_text(ptxt)
        KEY_OUT.write_text(ktxt)
        print(f"columns of the alignment TSV: {list(arows[0].keys())}")
        families(to_prs(arows))
        obs = kp.observations()
        holdout(obs, lambda o: o[0][0] == "260", "PRIMARY key from f.260 only")
        holdout(obs, lambda o: True, "SECONDARY VB-KEY scope")
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "p.tsv"
            write_pairs(pairs_rows(f260), p)
            prior_file(Path(td) / "prior.tsv")
            r = subprocess.run([sys.executable, str(TOOL), "align", str(p), str(Path(td) / "a.tsv"),
                                str(Path(td) / "k.tsv"), "--code-prefix", "@", "--word-code-prefix", "%",
                                "--code-chunk", "2", "--max-chunk", "12", "--keep-fs", "--prior",
                                str(Path(td) / "prior.tsv"), "--shuffle", "20"], capture_output=True, text=True)
            print("shared-tool --shuffle 20:", r.stdout.strip().splitlines()[-3:] if r.stdout else r.stderr[-400:])
    elif cmd == "--check":
        ptxt, ktxt, _, _ = full_outputs()
        stale = [f.name for f, t in ((PAIRS_OUT, ptxt), (KEY_OUT, ktxt)) if not f.exists() or f.read_text() != t]
        print("stale: " + ", ".join(stale) if stale else "ok")
        sys.exit(1 if stale else 0)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
