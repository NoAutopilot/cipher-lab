#!/usr/bin/env python3
"""DEC1162-RK (15 Oct 2026): apply the owner's g/q piles (settled_labels.tsv) to decode-1162 and decode-1168, re-key 1168.

  python3 ciphers/decode-1162-modena-ambung-1492/sorter/apply_split.py          write the *_split.* files, print the report
  python3 ciphers/decode-1162-modena-ambung-1492/sorter/apply_split.py --check  exit 1 if any *_split.* file is stale

Pre-registered in ../PREREG-DEC1162RK.md. Steps: (0) the A2-COS2 combination rule must rebuild the committed merged key.tsv from
align/f12r_key_A.tsv + f12r_key_B.tsv exactly; (1) relabel both ciphertext.tsv files by pile; (2) relabel the 1168 alignment pairs
(pass A = the 14 groups; pass B aligned to the group of the same gloss, unsorted g/q -> g.u/q.u); (3) tools/interlinear_align.py on
each pass + the run_align 20-seed gloss-shuffle control; (4) combine -> 1168 key_split.tsv. score_g.py --split scores it.
"""
import csv, collections, difflib, random, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
T62 = HERE.parent
T68 = T62.parent / "decode-1168-modena-costabili-1492"
ROOT = T62.parents[1]
AL = T68 / "align"
OUT = AL / "split"
GQ = {"g", "q"}
ALIAS = {"diliarte": "delaarte", "tale": "talur"}  # pass B's gloss spelling -> the 1168 group name


def tsv(p):
    return list(csv.DictReader(open(p), delimiter="\t"))


def combine(ka, kb):
    """A2-COS2 rule: C if both passes' top value agree with >= 2 agreeing occurrences each; value from A, else B."""
    A = {r["value"]: r for r in tsv(ka)}; B = {r["value"]: r for r in tsv(kb)}
    out = []
    for s in sorted(set(A) | set(B)):
        a, b = A.get(s), B.get(s)
        c = bool(a and b and a["meaning"] == b["meaning"] and int(a["agree"]) >= 2 and int(b["agree"]) >= 2)
        v = (a or b)["meaning"]
        fa = f"passA {a['agree']}/{a['n']}" if c and a else (f"passA {a['meaning']} {a['agree']}/{a['n']}" if a else "passA None")
        fb = f"passB {b['agree']}/{b['n']}" if c and b else (f"passB {b['meaning']} {b['agree']}/{b['n']}" if b else "passB None")
        out.append((s, v, "C" if c else "M", "period gloss f.12r", f"{fa}, {fb}"))
    return out


def piles():
    return {r["sid"]: r["new_sign"] for r in tsv(HERE / "settled_labels.tsv")}


def relabel_ct(path, prefix, pl):
    rows = tsv(path); n = 0
    for r in rows:
        sid = f"{prefix}_{r['line']}_{int(r['pos']):02d}"
        if sid in pl:
            assert r["sign"] in GQ, sid
            r["sign"] = pl[sid]; n += 1
        else:
            assert r["sign"] not in GQ, ("unsorted g/q in ciphertext", path, sid)
    return rows, n


def write_ct(rows, path):
    with open(path, "w") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["line", "pos", "sign", "conf"])
        for r in rows: w.writerow([r["line"], r["pos"], r["sign"], r["conf"]])


def relabel_pairs(ct68):
    """ct68: group -> list of split signs (1168 ciphertext order). Returns {A: rows, B: rows}, log lines."""
    merged = {}
    for r in tsv(T68 / "ciphertext.tsv"): merged.setdefault(r["line"], []).append(r["sign"])
    byname = {ln.split("_", 2)[2]: ln for ln in merged}
    res, log = {}, []
    for p in "AB":
        rows = []
        for r in tsv(AL / f"f12r_pairs_{p}.tsv"):
            sg = [t[1:] for t in r["cipher_raw"].split()]
            name = ALIAS.get(r["plain_raw"], r["plain_raw"])
            new = list(sg)
            if name in byname:
                ln = byname[name]; m = merged[ln]; sp = ct68[ln]
                if p == "A": assert sg == m, (p, name)
                sm = difflib.SequenceMatcher(a=sg, b=m, autojunk=False)
                amap = {}
                for blk in sm.get_matching_blocks():
                    for k in range(blk.size): amap[blk.a + k] = blk.b + k
                # equal-length replace blocks are position-aligned (a different label on the same physical sign)
                for op, a0, a1, b0, b1 in sm.get_opcodes():
                    if op == "replace" and a1 - a0 == b1 - b0:
                        for k in range(a1 - a0): amap[a0 + k] = b0 + k
                for i, t in enumerate(sg):
                    if t not in GQ: continue
                    j = amap.get(i)
                    if j is not None and m[j] in GQ:
                        new[i] = sp[j]
                        if m[j] != t: log.append(f"pass {p} {name} pos {i+1}: B label {t} on tile labelled {m[j]} -> {sp[j]}")
                    else:
                        new[i] = t + ".u"; log.append(f"pass {p} {name} pos {i+1}: {t} not on a sorted tile -> {t}.u")
            else:
                for i, t in enumerate(sg):
                    if t in GQ: new[i] = t + ".u"
                if any(t in GQ for t in sg): log.append(f"pass {p} {name}: B-only pair, g/q -> .u")
            rows.append((r["plain_line"], r["plain_raw"], r["cipher_line"], " ".join("@" + t for t in new)))
        res[p] = rows
    return res, log


def run_align(rows, tag):
    pp = OUT / f"{tag}_pairs.tsv"
    with open(pp, "w") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["plain_line", "plain_raw", "cipher_line", "cipher_raw"])
        for r in rows: w.writerow(r)
    subprocess.run(["python3", "tools/interlinear_align.py", "align", str(pp), str(OUT / f"{tag}_align.tsv"), str(OUT / f"{tag}_key.tsv"),
                    "--code-prefix", "@", "--keep-fs"], cwd=ROOT, capture_output=True, text=True, check=True)
    st = collections.Counter(r["status"].split(":")[0] for r in tsv(OUT / f"{tag}_align.tsv"))
    tot = sum(st.values()); return st.get("agrees", 0) / tot if tot else 0.0


def main():
    rep = []
    # (0) reproducibility of the combination rule on the committed merged key
    rebuilt = combine(AL / "f12r_key_A.tsv", AL / "f12r_key_B.tsv")
    have = [(r["sign"], r["value"], r["grade"]) for r in tsv(T68 / "key.tsv")]
    same = sorted(have) == sorted((s, v, g) for s, v, g, *_ in rebuilt)
    rep.append(f"step0 merged-key rebuild by the A2-COS2 rule: {'EXACT' if same else 'DIFFERS'} ({len(have)} signs)")
    if not same:
        print("\n".join(rep)); print(set(have) ^ set((s, v, g) for s, v, g, *_ in rebuilt)); sys.exit(2)
    # (0b) the committed merged pairs re-aligned now must give the committed per-pass keys
    for p in "AB":
        rows = [(r["plain_line"], r["plain_raw"], r["cipher_line"], r["cipher_raw"]) for r in tsv(AL / f"f12r_pairs_{p}.tsv")]
        run_align(rows, f"merged{p}")
        ok = tsv(OUT / f"merged{p}_key.tsv") == tsv(AL / f"f12r_key_{p}.tsv")
        rep.append(f"step0b pass {p} merged pairs re-aligned -> committed f12r_key_{p}.tsv: {'EXACT' if ok else 'DIFFERS'}")
    pl = piles()
    r62, n62 = relabel_ct(T62 / "ciphertext.tsv", "R1162", pl); write_ct(r62, T62 / "ciphertext_split.tsv")
    r68, n68 = relabel_ct(T68 / "ciphertext.tsv", "R1168", pl); write_ct(r68, T68 / "ciphertext_split.tsv")
    rep.append(f"step1 relabelled tiles: 1162 {n62}, 1168 {n68} (of {len(pl)})")
    ct68 = {}
    for r in r68: ct68.setdefault(r["line"], []).append(r["sign"])
    pairs, log = relabel_pairs(ct68)
    rep += ["step2 " + l for l in log]
    for p in "AB":
        real = run_align(pairs[p], f"split{p}")
        sh = []
        for seed in range(20):
            random.seed(seed); gl = [r[1] for r in pairs[p]]; random.shuffle(gl)
            sh.append(run_align([(a, g2, c, d) for (a, _, c, d), g2 in zip(pairs[p], gl)], f"sh{p}"))
        sh.sort()
        rep.append(f"step3 pass {p}: pairs {len(pairs[p])} real agree {real:.3f} shuffle mean {sum(sh)/len(sh):.3f} p95 {sh[18]:.3f} "
                   f"-> {'beats' if real > sh[18] else 'DOES NOT beat'} p95")
    for f in OUT.glob("sh?_*"): f.unlink()
    key = combine(OUT / "splitA_key.tsv", OUT / "splitB_key.tsv")
    with open(T68 / "key_split.tsv", "w") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["sign", "value", "grade", "source", "note"])
        for row in key: w.writerow(row)
    for s, v, g, _, n in key:
        if s.split(".")[0].split("-")[0] in GQ: rep.append(f"step4 key_split {s} = {v} {g} ({n})")
    (OUT / "report.txt").write_text("\n".join(rep) + "\n")
    print("\n".join(rep))


if __name__ == "__main__":
    if "--check" in sys.argv:
        old = {p: p.read_bytes() for p in [T62 / "ciphertext_split.tsv", T68 / "ciphertext_split.tsv", T68 / "key_split.tsv", OUT / "report.txt"]}
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()): main()
        bad = [str(p) for p, b in old.items() if p.read_bytes() != b]
        print("split files up to date" if not bad else "STALE: " + ", ".join(bad)); sys.exit(1 if bad else 0)
    main()
