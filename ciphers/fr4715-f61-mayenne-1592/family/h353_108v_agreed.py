#!/usr/bin/env python3
"""H353 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: f.108v (f.61's own hand) is fragile because its
two sign drafts (passes/rec108v, passes/recf108vg; the same seven lines L01-L07) behave differently under H344. The two ciphertext_draft.tsv files are
turned into pass-format TSVs (pos = position), aligned by tools/reconcile_passes.py (nw) into passes/rec108v_x/, and only the columns both drafts read
alike (why 'agree' or 'agree-flagged') are kept, in order, as passes/recf108vagree/ciphertext_draft.tsv. Then H342's leaf() on it, and H344's control
(3 whole-leaf shuffles, seeds 3440-3442) on it, both unchanged. Pre-stated: 'f.108v's order signal is carried by the signs both drafts read' iff H342
reads 'order signal' AND 0/3 shuffled targets do; else 'fragile' stands.   python3 h353_108v_agreed.py [--check]"""
import csv, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); P = f"{HERE}/passes"; ARGS = sys.argv[1:]; out = []
rd = lambda f: list(csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t"))
os.makedirs(f"{P}/rec108v_x", exist_ok=True)
for tag, src in (("a", "rec108v"), ("b", "recf108vg")):
    rows = rd(f"{P}/{src}/ciphertext_draft.tsv")
    open(f"{P}/rec108v_x/draft_{tag}.tsv", "w").write("line\tpos\tsign\tconf\tsegment\tx_px\tnote\n" + "".join(f"{r['line']}\t{r['position']}\t{r['sign']}\tm\ts1\t0\t\n" for r in rows))
subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{P}/rec108v_x/draft_a.tsv", f"{P}/rec108v_x/draft_b.tsv", "--out-dir", f"{P}/rec108v_x", "--method", "nw"], capture_output=True, text=True, check=True)
x = rd(f"{P}/rec108v_x/ciphertext_draft.tsv"); keep = [r for r in x if r["why"].startswith("agree")]
os.makedirs(f"{P}/recf108vagree", exist_ok=True)
open(f"{P}/recf108vagree/ciphertext_draft.tsv", "w").write("line\tposition\tsign\tconfidence\talt\twhy\n" + "".join(f"{r['line']}\t{i}\t{r['sign']}\t{r['confidence']}\t{r['alt']}\t{r['why']}\n" for i, r in enumerate(keep, 1)))
out.append(f"f.108v drafts aligned: {len(x)} columns, {len(keep)} read alike by both drafts ({len(keep) / len(x):.3f})")
h342 = open(f"{HERE}/h342_beam_seqgain.py").read(); h342 = h342[:h342.index("res = {}")]
g = {"__file__": f"{HERE}/h342_beam_seqgain.py", "__name__": "h353"}; sys.argv = [sys.argv[0]]; exec(compile(h342, "h342_prefix", "exec"), g)
gv, p95, null, nr, ns = g["leaf"]("recf108vagree"); sig = gv > p95
out.append(f"H342 on agreed signs: runs {nr}, signs {ns}; gain(v7) {gv:.4f} vs binned p95 {p95:.4f} ({sum(x >= gv for x in null)}/100) -> {'order signal' if sig else 'no order signal'}")
h344 = open(f"{HERE}/h344_seqgain_shuftarget.py").read()
h344 = h344.replace('("recf101r", "recf188r", "recf124r", "recf97r", "rec108v", "recf108vg")', '("recf108vagree",)')
h344 = h344[:h344.index('txt = "\\n".join(out)')]
g2 = {"__file__": f"{HERE}/h344_seqgain_shuftarget.py", "__name__": "h353b"}; sys.argv = [sys.argv[0]]; exec(compile(h344, "h344_on_agreed", "exec"), g2)
out.append("H344 on agreed signs: " + g2["out"][0].split(": ", 1)[1]); shuf_clean = not g2["void"]
out.append("read-out: " + ("f.108v's order signal is carried by the signs both drafts read" if sig and shuf_clean else "fragile stands"))
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h353_108v_agreed_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
