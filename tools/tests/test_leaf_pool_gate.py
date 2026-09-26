#!/usr/bin/env python3
"""Offline test for tools/leaf_pool_gate.py (LANE B9, 26 Sept 2026). No network. Synthetic K=90 two-digit
nomenclator with a Zipf profile: (1) a second leaf drawn from the same key is ADMITTED; (2) a leaf drawn from the
same profile under a different key (values permuted) is HELD on the system gate although its vocabulary overlap
is near 1 (why overlap does not gate), and pooled_h_only is False since it fails system, not just quality;
(3) a same-key leaf with 30% M rows clears form + system but fails quality, so it is POOLED (H-only, M held
per-token), not HELD outright (RETRO-2026-09-26g item 2: a leaf that is decisively the same system should not be
discarded wholesale for an M-share it can fix per-token); (4) a leaf with 10% off-form signs ('3z', '5i') is HELD
on form. Run: python3 tools/tests/test_leaf_pool_gate.py"""
import json, os, random, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, "tools", "leaf_pool_gate.py")


def write(path, signs, grades=None):
    with open(path, "w") as f:
        f.write("line\tposition\tsign\tconfidence\n")
        for i, s in enumerate(signs):
            f.write(f"1\t{i+1}\t{s}\t{(grades or ['H'] * len(signs))[i]}\n")


def draw(rng, vals, weights, n):
    return rng.choices(vals, weights=weights, k=n)


def run(leaf, pool, json_out=None):
    args = [sys.executable, TOOL, "--leaf", leaf, "--pool", pool]
    if json_out:
        args += ["--json", json_out]
    r = subprocess.run(args, capture_output=True, text=True)
    return r.returncode, r.stdout


def main():
    rng = random.Random(7)
    vals = [f"{i:02d}" for i in range(10, 100)]
    weights = [1 / (r + 1) for r in range(len(vals))]
    other = vals[:]
    rng.shuffle(other)
    with tempfile.TemporaryDirectory() as d:
        pool, same, diff, noisy, off = (os.path.join(d, x) for x in ("pool", "same", "diff", "noisy", "off"))
        write(pool, draw(rng, vals, weights, 1000))
        write(same, draw(rng, vals, weights, 500))
        write(diff, draw(rng, other, weights, 500))
        s = draw(rng, vals, weights, 500)
        write(noisy, s, ["M" if rng.random() < 0.3 else "H" for _ in s])
        s = draw(rng, vals, weights, 500)
        write(off, [x if rng.random() > 0.1 else x[0] + rng.choice("zi") for x in s])
        code, out = run(same, pool); assert code == 0 and "ADMITTED" in out, out
        diff_json = os.path.join(d, "diff.json")
        code, out = run(diff, pool, diff_json); assert code == 1 and "HELD" in out, out
        assert float(out.split("vocab overlap ")[1].split(";")[0]) > 0.95, out
        with open(diff_json) as f:
            r = json.load(f)
        assert r["pooled_h_only"] is False and r["admitted"] is False, r
        noisy_json = os.path.join(d, "noisy.json")
        code, out = run(noisy, pool, noisy_json)
        assert code == 1 and "POOLED (H-only, M held per-token)" in out, out
        with open(noisy_json) as f:
            r = json.load(f)
        assert r["pooled_h_only"] is True and r["admitted"] is False, r
        code, out = run(off, pool); assert code == 1 and "offform examples" in out, out
    print("ok: leaf_pool_gate admits same-key, holds different-key/off-form leaves, pools H-only on quality-only fail")


if __name__ == "__main__":
    main()
