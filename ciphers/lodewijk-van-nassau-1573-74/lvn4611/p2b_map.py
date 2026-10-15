"""LVN-P2B (15 Oct 2026): p2b settle on the LVN-P2RETX map (PREREG-LVN-4611.md addendum LVN-P2B, step 1, unit p2bm).
'Read' for a key_p2b.tsv target = the ink token its row maps to in retx_p2_map.tsv. Eligible: map status match, the ink token A=B in
retx_p2_lines.tsv, anchored (row at position +/-1 of the same line maps to the same K at kpos +/-1), ink equals A150 or B150.
Controls: the 10 key_p2b.tsv control rows (H): positive gate >= 8/10 eligible by (i)-(iii) with ink == sign; power gate: each control's
sign swapped for its seeded look-alike in a scratch copy of ciphertext_4611_pre_retx.tsv, map rebuilt, >= 9/10 not eligible by (i)-(iii).
usage: imported by settle.py (rows()); python3 p2b_map.py  prints the gates and counts."""
import csv, os, tempfile
from pathlib import Path
import retx_p2
HERE = Path(__file__).resolve().parent
rd = lambda p: list(csv.DictReader(open(p), delimiter="\t"))


def index(mp):
    return {(r[0], r[1]): r for r in mp}


def how_of():
    return {(r["K"], r["pos"]): r["how"] for r in rd(HERE / "retx_p2_lines.tsv")}


def elig(at, how, line, pos):
    """(i)-(iii): returns (ok, reason, ink)."""
    m = at.get((line, pos))
    if m is None: return False, "not in map", ""
    st, K, kp, ink = m[7], m[4], m[5], m[6]
    if st != "match": return False, "map " + st, ink
    if how.get((K, str(kp))) != "A=B": return False, "ink not A=B (" + str(how.get((K, str(kp)))) + ")", ink
    for d in (1, -1):
        n = at.get((line, str(int(pos) + d)))
        if n and n[4] == K and n[5] != "" and int(n[5]) == int(kp) + d: return True, "anchored", ink
    return False, "not anchored", ink


def build_map(ct_path):
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):
        _, mp, _ = retx_p2.build(HERE / "reads_p2retx.tsv", HERE / "recon_p2.tsv", ct_path)
    return mp


def gates():
    key = rd(HERE / "key_p2b.tsv"); how = how_of()
    at = index(build_map(HERE / "ciphertext_4611_pre_retx.tsv"))
    ctl = [k for k in key if k["role"] == "control"]
    pos = [(k["tid"], *elig(at, how, k["line"], k["position"])) for k in ctl]
    pos_ok = [p for p, k in zip(pos, ctl) if p[1] and p[3] == k["sign"]]
    pre = rd(HERE / "ciphertext_4611_pre_retx.tsv"); hdr = list(pre[0].keys())
    power = []
    for k in ctl:
        alt = [c.strip() for c in k["candidates"].split("|") if c.strip() != k["sign"]][0]
        with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False) as fh:
            w = csv.DictWriter(fh, hdr, delimiter="\t", lineterminator="\n"); w.writeheader()
            for r in pre:
                r2 = dict(r)
                if (r["line"], r["position"]) == (k["line"], k["position"]): assert r["sign"] == k["sign"]; r2["sign"] = alt
                w.writerow(r2)
        a2 = index(build_map(fh.name)); os.unlink(fh.name)
        ok, why, ink = elig(a2, how, k["line"], k["position"])
        power.append((k["tid"], alt, ok, why, ink))
    rej = sum(not p[2] for p in power)
    return at, how, pos, len(pos_ok), power, rej


def rows():
    """settle_p2bm rows in lvn4611/settle.py's format, and a gate line."""
    at, how, pos, npos, power, rej = gates()
    codes = {r["code"] for r in rd(HERE.parent / "key_full.tsv")}
    gate = npos >= 8 and rej >= 9
    out = []
    for k in sorted((k for k in rd(HERE / "key_p2b.tsv") if k["role"] == "target"), key=lambda k: (k["line"], int(k["position"]))):
        m = at.get((k["line"], k["position"])); assert m is None or m[2] == k["sign"], (k, m)
        ok, why, ink = elig(at, how, k["line"], k["position"])
        ab = ink in (k["A150"], k["B150"])
        if ok and not ab: why = "ink %s not A150/B150" % ink
        ok = gate and ok and ab
        conf = ("H" if ink in codes else "M") if ok else "M"
        act = (("settled" if ink != k["sign"] else "confirmed") if conf == "H" else "read-confirmed-not-key-code") if ok else "stays"
        out.append([k["line"], k["position"], k["sign"], ink if ok else k["sign"], conf, act,
                    f"LVN-P2B map settle: ink {ink or '-'} ({why}; A150 {k['A150']}, B150 {k['B150']}; {k['tid']}; p2bm controls {npos}/10 pos, {rej}/10 power)"])
    line = "p2bm positive control %d/10 (gate >= 8), power control %d/10 rejected (gate >= 9): %s" % (npos, rej, "PASS" if gate else "FAIL")
    return out, line, pos, power


if __name__ == "__main__":
    from collections import Counter
    out, line, pos, power = rows()
    print(line)
    for p in pos: print("  pos", p)
    for p in power: print("  power", p)
    print(Counter(r[5] for r in out))
    print(Counter(r[6].split("(")[1].split(";")[0] for r in out if r[5] == "stays"))
