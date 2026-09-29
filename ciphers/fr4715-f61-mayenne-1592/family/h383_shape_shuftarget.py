#!/usr/bin/env python3
"""H383 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), script-only, written before running: the ARM-C1 arm H379/H380 lacked (H360 carried
it): H344's shuffled-target control, code unchanged, on the two shape-relabelled drafts, now written to disk for the verifier:
  passes/rec108v_shape/ciphertext_draft.tsv -- H59's f.108v draft with H199's answers applied (bowl -> 4TRI, no -> C43), as H379 built it;
  passes/recf106r_shape/ciphertext_draft.tsv -- recf106rall18 with the H231/H368 answers applied where the draft matches pass A, as H380 built it.
Pre-stated: a leaf's H379/H380 read-out stands iff v7 shows 'order signal' on 0/3 of its shuffled targets (seeds 3440-3442); >= 1 voids it.
python3 h383_shape_shuftarget.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; ARGS = sys.argv[1:]; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def write_drafts():
    H = rd(f"{HERE}/h199_bowl_positions.tsv"); lab = {(h["line"], h["column"]): h["bowl"] for h in H}
    rows = rd(f"{P}/f108v3z_draft_reconciled.tsv"); cols = list(rows[0]); os.makedirs(f"{P}/rec108v_shape", exist_ok=True)
    with open(f"{P}/rec108v_shape/ciphertext_draft.tsv", "w") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            a = lab.get((r["line"], r["position"])); r["sign"] = "4TRI" if a == "yes" else "C43" if a == "no" else r["sign"]
            f.write("\t".join(r[c] for c in cols) + "\n")
    sys.argv = [sys.argv[0], "f97r"]
    import h380_106r_shape_relabel as h380
    lab = h380.answers(); raw = list(open(f"{P}/recf106rall18/ciphertext_draft.tsv")); D = {tuple(l.split("\t")[:2]): l.split("\t")[2] for l in raw[1:]}
    use = {k: a for k, (c, a) in lab.items() if a in ("yes", "no") and D.get(k) == c}; new = [raw[0]]
    for l in raw[1:]:
        c = l.rstrip("\n").split("\t"); a = use.get((c[0], c[1]))
        if a: c[2] = "4TRI" if a == "yes" else "C43"
        new.append("\t".join(c) + "\n")
    os.makedirs(f"{P}/recf106r_shape", exist_ok=True); open(f"{P}/recf106r_shape/ciphertext_draft.tsv", "w").write("".join(new))
    return len(use)
n106 = write_drafts()
src = open(f"{HERE}/h344_seqgain_shuftarget.py").read()
old = '("recf101r", "recf188r", "recf124r", "recf97r", "rec108v", "recf108vg")'; assert old in src
src = src.replace(old, '("rec108v_shape", "recf106r_shape")')
src = src.replace('rs = f"{HERE}/h344_seqgain_shuftarget_result.txt"', 'rs = f"{HERE}/h383_shape_shuftarget_result.txt"')
src = src.replace('out = []', f'out = ["shape drafts written: rec108v_shape (H199 answers), recf106r_shape ({n106} tokens)"]', 1)
g = {"__file__": f"{HERE}/h344_seqgain_shuftarget.py", "__name__": "__main__"}; sys.argv = [sys.argv[0]] + ARGS
exec(compile(src, "h344_on_shape_drafts", "exec"), g)
