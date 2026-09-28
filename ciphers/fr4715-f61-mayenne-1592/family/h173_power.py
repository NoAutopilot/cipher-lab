#!/usr/bin/env python3
"""H173 (runner 6, 28 Sept 2026): positive control for h170_gate.py's statistic, PRE-REGISTERED here before the run.
Known pair: fr.3984 f.188r (cipher, blind passes A/B on disk, F61-FAMILY-3) and its separate-sheet clear f.184r. Two all-cipher
windows of four rows each, the same size as H170's (about 250 signs): W1 = L19-L22, W2 = L08-L11 (PLAIN tokens dropped). The true
clear of a window = the concatenated plain_chunk of passes/f188r_align.tsv's rows on those lines (f.184r's words as
align_separate.py split them over the bands). Key: key_period_v4.tsv WITHOUT the rows of leaf 'fr.3984 f.188r/f.184r'
(f.101r + f.274r only, so the leaf never scores itself), same --min 2 / --frac 0.1 / EBR collapse / 4TRI+4HOOK union as H170.
Statistic, N (min(letters, floor(0.8 x signs))), 200 permuted keys (seed 1) and the gate are H170's, applied per pass (A, B):
true clear > permuted max AND true - max(wrong) >= 0.10. Wrong texts: fol. 175r's blind read (passes/f175r_clearA_h170.tsv) and
the other window's true clear. Reading: if the true pair clears the gate on both passes of at least one window, H170's
statistic has power at this N and H170's FAIL stands as 'not rendered by fol. 175r at f.176r's head'; if it clears on none,
H170's FAIL is a non-test (instrument without power at this N and pass quality).
  python3 h173_power.py [--check]"""
import csv, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import h170_gate as g
P = f"{HERE}/passes"
def key_wo_188():
    rows = g.rd(f"{HERE}/key_period_v4.tsv"); rows = [r for r in rows if not r["leaf"].startswith("fr.3984 f.188r")]
    tot = Counter(); key = {}
    for r in rows:
        if r["letter"] not in ("-", ""): tot[(r["class"], r["leaf"])] += int(r["n"])
    for r in rows:
        if r["letter"] in ("-", "") or r["class"] in ("PLAIN", "OTHER", "DASH") or int(r["n"]) < 2: continue
        if int(r["n"]) < 0.1 * tot[(r["class"], r["leaf"])]: continue
        key.setdefault({"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["class"], r["class"]), set()).add(r["letter"])
    key["4TRI"] = key.get("4TRI", set()) | key.get("4HOOK", set())
    return {c: tuple(sorted(v)) for c, v in key.items()}
W = {"W1": ["L19", "L20", "L21", "L22"], "W2": ["L08", "L09", "L10", "L11"]}
def main():
    key = key_wo_188(); al = g.rd(f"{P}/f188r_align.tsv"); out = [f"key v4 without f.188r rows: {len(key)} classes"]
    true = {w: g.fold("".join(r["plain_chunk"] for r in al if r["cipher_line"] in ls and r["kind"] == "code")) for w, ls in W.items()}
    f175 = "".join(g.fold(r["text"]) for r in g.rd(f"{P}/f175r_clearA_h170.tsv"))
    anyw = False
    for w, ls in W.items():
        other = true["W2" if w == "W1" else "W1"]; both = True
        for tag in "AB":
            seq = [ {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["sign"], r["sign"]) for r in g.rd(f"{P}/f188r_signs{tag}.tsv")
                    if r["line"] in ls and r["sign"] != "PLAIN"]
            N = min(len(true[w]), len(other), len(f175), int(0.8 * len(seq)))
            t = true[w][:N]; ft = g.frac(t, seq, key); fw = [g.frac(f175[:N], seq, key), g.frac(other[:N], seq, key)]
            rng = random.Random(1); cls = list(key); sets = [key[c] for c in cls]; perm = []
            for _ in range(200):
                rng.shuffle(sets); perm.append(g.frac(t, seq, dict(zip(cls, sets))))
            pmax = max(perm); ok = ft > pmax and ft - max(fw) >= 0.10; both &= ok
            out.append(f"{w} pass {tag}: signs {len(seq)}, true letters {len(true[w])}, N {N}; true {ft:.3f}; wrong f175 {fw[0]:.3f}, "
                       f"other window {fw[1]:.3f}; permuted mean {sum(perm)/200:.3f} p95 {sorted(perm)[189]:.3f} max {pmax:.3f}; {'PASS' if ok else 'FAIL'}")
        out.append(f"{w}: {'PASS both passes' if both else 'FAIL'}"); anyw |= both
    out.append(f"POWER at H170's N and design: {'YES (H170 FAIL stands)' if anyw else 'NO (H170 FAIL is a non-test)'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h173_power_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
