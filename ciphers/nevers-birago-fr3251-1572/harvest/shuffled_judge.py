#!/usr/bin/env python3
"""Judge control for a keyed decode (CLAUDE.md rule 3, ARM-C1 shape; GAPS-nevers-birago, 2 Oct 2026): the same key
applied to the same signs in shuffled order, N seeds, each decode scored by tools/judge_plaintext.py's judge() against
the target's spec. A PASS on any shuffled decode voids the judge as a gate for this family at this N.
  python3 shuffled_judge.py SPEC MAP.json SEQ.tsv [SEQ2.tsv ...] [--seeds 20] [--real]
SEQ.tsv: passage pos sign_id ... (a reconciled pass file). Signs are shuffled across the whole joined sequence and
re-cut to the original passage lengths; unkeyed signs (X_*, ?) are dropped from the letters, as decode_key.py's U
tokens are dropped by letters_from_reading.py.
"""
import argparse, csv, json, random, statistics, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import judge_plaintext as jp  # noqa: E402

ap = argparse.ArgumentParser(); ap.add_argument("spec"); ap.add_argument("map"); ap.add_argument("seq", nargs="+")
ap.add_argument("--seeds", type=int, default=20); ap.add_argument("--real", action="store_true")
a = ap.parse_args()
spec = json.load(open(a.spec)); m = {e["id"]: e["value"] for e in json.load(open(a.map))}
lens, signs = [], []
for fn in a.seq:
    cur = None; n = 0
    for r in csv.DictReader(open(fn), delimiter="\t"):
        if r["passage"] != cur:
            if cur is not None: lens.append(n)
            cur, n = r["passage"], 0
        signs.append(r["sign_id"].strip()); n += 1
    lens.append(n)

def letters(seq):
    out, i = [], 0
    for L in lens:
        out.append("".join(m[s] for s in seq[i:i + L] if s in m and m[s] != "null")); i += L
    return "\n".join(out)

corpora = spec["judge"].get("corpora") or jp.LANG_CORPORA[spec["judge"]["language"]]
model = jp.NgramModel([jp.read_corpus(p) for p in corpora])  # built once; judge() would rebuild it per call
N = max(len(jp.fold(letters(signs))), 20)
real_c, null_c, _ = model.controls(N, samples=int(spec["judge"].get("control_samples", 200)))
null99, real05 = round(jp.pct(null_c, 0.99), 3), round(jp.pct(real_c, 0.05), 3)

def score(text):  # the same test judge() applies (mode 'both'), with the model and controls built once
    sc = model.score(jp.fold(text))
    return sc, (sc > null99 and sc > real05), real05, null99

if a.real:
    s, p, r05, n99 = score(letters(signs))
    print(f"real order: score {s:.3f} {'PASS' if p else 'FAIL'} (real_p05 {r05}, null_p99 {n99})")
rows = []
for seed in range(1, a.seeds + 1):
    seq = list(signs); random.Random(seed).shuffle(seq)
    s, p, r05, n99 = score(letters(seq)); rows.append((seed, s, p))
    print(f"seed {seed:2d}: score {s:.3f} {'PASS' if p else 'FAIL'}")
ss = [s for _, s, _ in rows]
print(f"SHUFFLED-TARGET: {len(rows)} decodes of {len(signs)} signs; score mean {statistics.mean(ss):.3f} min {min(ss):.3f} "
      f"max {max(ss):.3f}; PASS {sum(p for _, _, p in rows)} of {len(rows)}; real_p05 {r05}, null_p99 {n99}")
