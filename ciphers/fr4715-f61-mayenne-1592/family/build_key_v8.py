#!/usr/bin/env python3
"""F61-FAMILY-13 (29 Sept 2026): key v8 = key v7 plus exactly what VERIFY-F61-V11 endorsed (AUDIT.md section "VERIFY-F61-V11 (29 Sept 2026)",
its "Exact cell change for a key v8" and the L05 14 note; verify_v11/).

1. A split class 4TRI_NB = CELL a/n (C43's period cell), applied only to 4TRI tokens answered no-bowl in a gated blind read. Grade C where
   f.101r's period letter (passes/f101r_align.tsv through verify_v11/v11_crosstab.letter_map) is a or n; grade M where the call is shape-only
   (f.124r, and f.101r tokens with no period letter or another letter). Per token, which reader and which call made each answer:
   family/key_v8_4tri_nb_tokens.tsv. Gated reads used (the ones V11 audited): runner 13 H362 + H365 (f.101r) and H359 + H360 (f.124r),
   each call's gate >= 17/20 on H193's f.176v anchors; VERIFY-F61-V11's own calls c1-c5 (anchors >= 8/10 and repeats >= 5/6); runner 14
   H367 on f.61 (gate 19/20) with H194 as the earlier f.61 read.
   A token answered no-bowl by one gated read and bowl by another is a CONFLICT (rule 4, the same shape as f.61 L05 14 in V11): it stays
   4TRI, its a/n alternative recorded in the token table, not settled by majority.
2. 4TRI (the bowl class, or not bowl-read) unchanged from v7: pooled c/p/t, f.61 reading cell c/p.
3. f.61 L05 14 stays 4TRI c/p at grade M (H194 bowl vs H367 no-bowl, rule 4), an F61TOK note row; no f.61 token is 4TRI_NB.
Not merged: V10's audit (session_01BBihDVXNJZJwuUvhLshzw4) names nothing for the key; runner 14's f.97r reads (H368, recf97r_split*) were not
audited by V11 and are not used. Nothing else changes.

Output family/key_period_v8.tsv (key_period_v7.tsv is never edited): every v7 line verbatim, then the 4TRI_NB rows and the L05 14 F61TOK row;
family/key_v8_4tri_nb_tokens.tsv; family/key_v8_cells.tsv (key_v7_cells_h354.tsv + 4TRI_NB a/n, for tools/partial_key_test.py --cells);
v8 drafts passes/recf101r_split_nb/, recf124r_split_nb/ (runner 13's split drafts with the relabelled tokens labelled 4TRI_NB, not C43) and
passes/recf101r_v8/, recf124r_v8/ (the v8 token assignment of this script, conflicts left 4TRI).

Reproduction (from key_period_v8.tsv through load_key_v8): every class load_key_v7 gives is unchanged in v8 (pooled, form A, f.61 reading key);
f.61 five known spans 53/55 and f.108r overlay 74/84 (2000 permuted keys, seed 20260929, as build_key_v7); V11's meter (verify_v8/meter_v8.py bands):
key v8 as merged (all six f.61 4TRI c/p, L05 14 at grade M) 12 / 59 / 2 / 26, V11's H367 variant (L05 14 a/n) 12 / 59 / 2 / 26, f.61 left unread
(each f.61 4TRI a/c/n/p) 12 / 53 / 8 / 26. The order gain on f.101r / f.124r (tools/partial_key_test.py --cells --shuffle-target 3) is run by
run_pkt_v8.sh, whose outputs pkt_v8_*.txt are compared here with V11's verify_v11/pkt_f101r_split.txt / pkt_f124r_split.txt.
Writes the files above and build_key_v8_result.txt; exits non-zero on any mismatch.
  python3 build_key_v8.py [--check]   (--check: regenerate everything in memory, fail if any committed file is stale)"""
import csv, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); V11D = os.path.abspath(f"{HERE}/../verify_v11")
P = f"{HERE}/passes"
sys.path.insert(0, HERE); sys.path.insert(0, S); sys.path.insert(0, V11D)
CHECK = "--check" in sys.argv
V7, V8 = f"{HERE}/key_period_v7.tsv", f"{HERE}/key_period_v8.tsv"
TOK, CELLS7, CELLS8 = f"{HERE}/key_v8_4tri_nb_tokens.tsv", f"{HERE}/key_v7_cells_h354.tsv", f"{HERE}/key_v8_cells.tsv"
RES = f"{HERE}/build_key_v8_result.txt"
LEAF = {"f101r": "fr.3982 f.101r", "f124r": "fr.3982 f.124r", "f61": "fr.4715 f.61r"}
V11 = "VERIFY-F61-V11"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def h193_gate(ans):
    ctl = rd(f"{HERE}/h193_items.tsv")
    return sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in ctl if r["group"] in ("CP", "AN"))
def reads():
    """(leaf, line, pos) -> list of (call, answer) from gated calls only; also returns the per-call gate log."""
    R = defaultdict(list); log = []
    def runner(tag, leaf, items_f, reply_f, chunk=None):
        ans = {r["id"]: r["answer"].strip().lower() for r in rd(reply_f)}; g = h193_gate(ans); ok = g >= 17
        log.append(f"{tag}: gate {g}/20 {'PASS' if ok else 'FAIL (not used)'}")
        if not ok: return
        for r in rd(items_f):
            if r["code"] == "4TRI" and (chunk is None or r["chunk"] == chunk):
                R[(leaf, r["line"], r["pos"])].append((tag, ans.get(r["item"], "missing")))
    runner("runner13 H362", "f101r", f"{HERE}/h362_items.tsv", f"{P}/h362_reply.tsv")
    for c in sorted({r["chunk"] for r in rd(f"{HERE}/h365_items.tsv")}):
        runner(f"runner13 H365 {c}", "f101r", f"{HERE}/h365_items.tsv", f"{P}/h365_reply_{c}.tsv", c)
    runner("runner13 H359", "f124r", f"{HERE}/h359_items.tsv", f"{P}/h359_reply.tsv")
    for c in sorted({r["chunk"] for r in rd(f"{HERE}/h360_items.tsv")}):
        runner(f"runner13 H360 {c}", "f124r", f"{HERE}/h360_items.tsv", f"{P}/h360_reply_{c}.tsv", c)
    runner("runner14 H367", "f61", f"{HERE}/h367_items.tsv", f"{P}/h367_reply.tsv")
    import h367_bowl_f61 as h367
    for (line, pos), a in sorted(h367.h194().items()):     # H194: the earlier f.61 bowl read (gate passed, NOTES H194)
        if (line, pos) in {(r["line"], r["pos"]) for r in rd(f"{HERE}/h367_items.tsv") if r["code"] == "4TRI"}:
            R[("f61", line, pos)].append(("runner H194", a))
    for items_f, calls in ((f"{V11D}/v11_items.tsv", ("c1", "c2", "c3")), (f"{V11D}/v11e_items.tsv", ("c4", "c5"))):
        items = rd(items_f)
        for c in calls:
            ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{V11D}/v11_reply_{c}.tsv")}; its = [r for r in items if r["call"] == c]
            anc = [r for r in its if r["role"] == "anchor"]; reps = [r for r in its if r["repeat_of"]]
            ah = sum((ans.get(r["id"]) == "yes") == (r["group"] == "CP") and ans.get(r["id"]) in ("yes", "no") for r in anc)
            rh = sum(ans.get(r["id"]) == ans.get(r["repeat_of"]) for r in reps); ok = ah >= 8 and rh >= 5
            log.append(f"{V11} {c}: anchors {ah}/{len(anc)}, repeats {rh}/{len(reps)} {'PASS' if ok else 'FAIL (not used)'}")
            if ok:
                for r in its:
                    if r["role"] == "target" and not r["repeat_of"]:
                        R[(r["leaf"], r["line"], r["pos_or_seg"])].append((f"{V11} {c}", ans.get(r["id"], "missing")))
    return R, log
def assign():
    """Per token: NB (>= 1 gated 'no', no gated 'yes'), CONFLICT (both), BOWL (only 'yes'), else UNREAD. f.61 L05 14 is CONFLICT here."""
    import v11_crosstab as X
    R, log = reads(); lm = X.letter_map("f101r"); rows = []
    for (leaf, line, pos), rs in sorted(R.items(), key=lambda kv: (kv[0][0], int(kv[0][1][1:]), int(kv[0][2]))):
        a = {x for _, x in rs}
        st = "CONFLICT" if {"yes", "no"} <= a else "NB" if "no" in a else "BOWL" if "yes" in a else "UNREAD"
        L = lm.get((line, pos), ("", False, False))[0] if leaf == "f101r" else ""
        if st == "NB": grade = "C" if L in ("a", "n") else "M"
        elif st == "CONFLICT": grade = "M"
        else: grade = "-"
        val = {"NB": "a/n", "CONFLICT": "c/p (a/n alternative)" if leaf == "f61" else "c/p/t (a/n alternative)", "BOWL": "c/p" if leaf == "f61" else "c/p/t", "UNREAD": "c/p/t"}[st]
        rows.append(dict(leaf=leaf, line=line, pos=pos, v8_class="4TRI_NB" if st == "NB" else "4TRI", status=st, value=val, grade=grade,
                         period_letter=L or "-", no_by=";".join(c for c, x in rs if x == "no") or "-",
                         bowl_by=";".join(c for c, x in rs if x == "yes") or "-", other=";".join(f"{c}={x}" for c, x in rs if x not in ("yes", "no")) or "-"))
    return rows, log
def tok_tsv(rows):
    hdr = ["leaf", "line", "pos", "v8_class", "status", "value", "grade", "period_letter", "no_by", "bowl_by", "other"]
    head = ["# key_v8_4tri_nb_tokens.tsv -- F61-FAMILY-13 (key v8), 29 Sept 2026: every 4TRI token with a gated blind bowl read, per token which "
            "reader and call answered no-bowl (no_by) and bowl (bowl_by). Built by build_key_v8.py; do not hand-edit.",
            "# status NB = no-bowl only -> 4TRI_NB a/n (grade C if f.101r's period letter is a/n, else M); CONFLICT = both answers -> stays 4TRI, "
            "a/n alternative (rule 4, not settled by majority); BOWL = bowl only -> 4TRI. period_letter: passes/f101r_align.tsv (grade C per pair)."]
    return "\n".join(head + ["\t".join(hdr)] + ["\t".join(r[h] for h in hdr) for r in rows]) + "\n"
def build(rows):
    v7 = open(V7).read().rstrip("\n").split("\n")
    nb = [r for r in rows if r["status"] == "NB"]; cf = [r for r in rows if r["status"] == "CONFLICT"]
    c101 = Counter(r["period_letter"] for r in nb if r["leaf"] == "f101r")
    n124 = sum(r["leaf"] == "f124r" for r in nb)
    head = ["# key_period_v8.tsv -- F61-FAMILY-13 (key v8), 29 Sept 2026: key_period_v7.tsv verbatim plus what VERIFY-F61-V11 endorsed (AUDIT.md, "
            "'Exact cell change for a key v8'). Built by build_key_v8.py; do not hand-edit.",
            "# Added: split class 4TRI_NB = CELL a/n (C43's period cell) for 4TRI tokens answered no-bowl in a gated blind read, per token in "
            "key_v8_4tri_nb_tokens.tsv; 4TRI (bowl, or not bowl-read) unchanged from v7; f.61 L05 14 stays 4TRI c/p at grade M (F61TOK note).",
            "# Not merged: anything from VERIFY-F61-V10 (its lists name no key change); f.97r bowl reads (H368, not audited by V11).",
            "# Key source: period (fr.3982 f.101r decipherment, C43's cell) for 4TRI_NB; token assignment by blind shape reads (runner 13, V11). "
            "v7 file follows verbatim:"]
    add = [f"4TRI_NB\ta\t{c101['a']}\t{LEAF['f101r']}\tCELL a/n {V11} (4TRI answered no-bowl in a gated blind read = C43's cell); grade C on "
           f"this leaf where the period letter is a or n; f.101r NB tokens {sum(c101.values())}: period a {c101['a']}, n {c101['n']}, "
           f"other/none {sum(v for k, v in c101.items() if k not in ('a', 'n'))} (grade M)",
           f"4TRI_NB\tn\t{c101['n']}\t{LEAF['f101r']}\tCELL a/n (cell partner; the count is f.101r NB tokens whose period letter is n)",
           f"4TRI_NB\ta\t0\t{LEAF['f124r']}\tCELL a/n {V11}; f.124r NB tokens {n124}, grade M (shape-only; no usable period-letter join on f.124r)",
           f"4TRI\t-\t0\t{LEAF['f61']}\tF61TOK L05 14 stays c/p grade M: H194 bowl vs H367 no-bowl ({V11}, rule 4, not settled by the later read); "
           f"a/n noted as the alternative; the other five f.61 4TRI read bowl (H367, H194) and keep F61READ c/p",
           f"# conflicts left 4TRI (grade M, a/n alternative): {len(cf)} tokens -- " + " ".join(f"{r['leaf']}:{r['line']}:{r['pos']}" for r in cf)]
    return "\n".join(head + v7 + add) + "\n"
def load_key_v8(path=V8, **kw):
    """As build_key_v7.load_key_v7 on the v8 file: 4TRI_NB's CELL rows give a/n; the F61TOK L05 14 row carries no letter and loads nothing."""
    from build_key_v7 import load_key_v7
    return load_key_v7(path, **kw)
def cells8():
    lines = open(CELLS7).read().rstrip("\n").split("\n")
    return "\n".join(["# key_v8_cells.tsv -- F61-FAMILY-13: key_v7_cells_h354.tsv verbatim plus 4TRI_NB a/n (key v8); for tools/partial_key_test.py --cells"]
                     + lines + ["4TRI_NB\ta/n"]) + "\n"
def drafts(rows):
    out = {}
    nbset = {(r["leaf"], r["line"], r["pos"]) for r in rows if r["status"] == "NB"}
    for leaf in ("f101r", "f124r"):
        d0 = open(f"{P}/rec{leaf}/ciphertext_draft.tsv").read().rstrip("\n").split("\n"); d1 = open(f"{P}/rec{leaf}_split/ciphertext_draft.tsv").read().rstrip("\n").split("\n")
        a, b = [d0[0]], [d0[0]]
        for l0, l1 in zip(d0[1:], d1[1:]):
            c0, c1 = l0.split("\t"), l1.split("\t")
            x = list(c0)
            if c0[2] != c1[2]:
                assert c0[2] == "4TRI" and c1[2] == "C43", (l0, l1); x[2] = "4TRI_NB"
            a.append("\t".join(x))
            y = list(c0)
            if c0[2] == "4TRI" and (leaf, c0[0], c0[1]) in nbset: y[2] = "4TRI_NB"
            b.append("\t".join(y))
        out[f"{P}/rec{leaf}_split_nb/ciphertext_draft.tsv"] = "\n".join(a) + "\n"
        out[f"{P}/rec{leaf}_v8/ciphertext_draft.tsv"] = "\n".join(b) + "\n"
    return out
def repro(tsv, rows, log):
    import tempfile
    from build_key_v7 import load_key_v7, f61_relabel
    tmp = tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False); tmp.write(tsv); tmp.close()
    out, bad = ["gated calls: " + "; ".join(log)], []
    k7 = {m: load_key_v7(**kw) for m, kw in (("B", {}), ("A", {"ebr": "A"}), ("raw", {"fold": False}), ("f61", {"f61": True}), ("f61raw", {"f61": True, "fold": False}))}
    k8 = {m: load_key_v8(tmp.name, **kw) for m, kw in (("B", {}), ("A", {"ebr": "A"}), ("raw", {"fold": False}), ("f61", {"f61": True}), ("f61raw", {"f61": True, "fold": False}))}
    os.unlink(tmp.name)
    for m in k7:
        extra = sorted(set(k8[m]) - set(k7[m])); moved = sorted(c for c in k7[m] if k7[m][c] != k8[m].get(c))
        if extra != ["4TRI_NB"] or moved or k8[m]["4TRI_NB"] != ("a", "n"): bad.append(f"load {m}: extra {extra}, moved {moved}")
    out.append(f"v7 -> v8 loaded key (pooled B, form A, unfolded, f.61 reading, f.61 unfolded): only change 4TRI_NB added = "
               f"{'/'.join(k8['B']['4TRI_NB'])}; every v7 class unchanged ({len(k7['B'])} pooled classes); 4TRI = {'/'.join(k8['B']['4TRI'])}, "
               f"f.61 reading 4TRI = {'/'.join(k8['f61']['4TRI'])}, C43 = {'/'.join(k8['B']['C43'])}")
    st = Counter((r["leaf"], r["status"]) for r in rows); gr = Counter((r["leaf"], r["grade"]) for r in rows if r["status"] == "NB")
    out.append("token assignment (gated reads): " + "; ".join(f"{lf} " + " ".join(f"{s} {st[(lf, s)]}" for s in ("NB", "BOWL", "CONFLICT", "UNREAD") if st[(lf, s)])
                                                             + f" [NB grade C {gr[(lf, 'C')]}, M {gr[(lf, 'M')]}]" for lf in ("f101r", "f124r", "f61")))
    f61 = {(r["line"], r["pos"]): r for r in rows if r["leaf"] == "f61"}
    if f61.get(("L05", "14"), {}).get("status") != "CONFLICT" or any(r["status"] == "NB" for r in f61.values()) or len(f61) != 6:
        bad.append("f.61 4TRI assignment (want 6 tokens, L05 14 CONFLICT, none NB)")
    out.append("f.61 4TRI: " + " ".join(f"{l}:{p} {r['status']} ({r['bowl_by']} bowl / {r['no_by']} no)" for (l, p), r in sorted(f61.items(), key=lambda kv: (int(kv[0][0][1:]), int(kv[0][1])))))
    # meter (bands as verify_v8/meter_v8.py, baseline as verify_v11/meter_v11.py)
    def band(letters, cls):
        if cls == "C6" or letters in ("-", ""): return "unread/null"
        n = len(letters.split("/")); return "firm" if n == 1 else ("two-way" if n == 2 else "wider")
    NEW = {c: "/".join(k8["f61raw"][c]) for c in {"4STEM", "4TRI", "HASH4", "ZHOOK", "VBAR_A", "EBR", "SBS"}}
    d = list(csv.DictReader(open(f"{HERE}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t"))
    def v8(r, tri):
        if r["class"] == "4PI": return "a/n" if (r["line"], int(r["pos"])) == ("L11", 9) else "-"
        if r["class"] == "4TRI": return tri(r)
        return NEW.get(r["class"], r["period_letters"])
    for tag, tri, want in (("key v8 as merged (six f.61 4TRI c/p, L05 14 grade M)", lambda r: NEW["4TRI"], (12, 59, 2, 26, 99)),
                           ("V11 variant, H367 reads (L05 14 a/n, five c/p)", lambda r: "a/n" if (r["line"], r["pos"]) == ("L05", "14") else NEW["4TRI"], (12, 59, 2, 26, 99)),
                           ("f.61 4TRI left unread (each a/c/n/p)", lambda r: "a/c/n/p", (12, 53, 8, 26, 99))):
        c = Counter(band(v8(r, tri), r["class"]) for r in d); meter = (c["firm"], c["two-way"], c["wider"], c["unread/null"], len(d))
        out.append(f"f.61 meter, {tag}: {len(d)} signs: firm {meter[0]} / two-way {meter[1]} / wider {meter[2]} / unread-or-null {meter[3]}")
        if meter != want: bad.append(f"meter {tag} {meter} != {want}")
    # known spans (as build_key_v7)
    from f61crib import align, load_read, load_spans
    from f61crib4 import split_lines
    from f61joint import f108_lines
    from sbs_relabel import relabel
    FOLD = str.maketrans("jvy", "iui")
    lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    lines61 = f61_relabel({k: list(v) for k, v in lines.items()})
    s61 = load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    def sc(key, spans, ll):
        mt = tot = 0
        for s, l, m in spans:
            mm = m.translate(FOLD); mt += align(mm, ll[l], key)[0]; tot += sum(1 for ch_ in mm if ch_ != "-")
        return mt, tot
    for tag, spans, k, ll, want in (("f.61 five spans, f.61 reading key", s61, k8["f61"], lines61, (53, 55)),
                                    ("f.108r overlay, pooled key (EBR form A)", s108, k8["A"], lines, (74, 84))):
        mt, tot = sc(k, spans, ll); labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
        for _ in range(2000):
            v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v)), spans, ll)[0])
        cs.sort(); ge = sum(x >= mt for x in cs)
        out.append(f"{tag} (j=i, v=u, y=i folded): v8 {mt}/{tot} = {mt/tot:.3f}; 2000 permuted mean {sum(cs)/2000/tot:.3f} p95 {cs[1899]/tot:.3f} max {cs[-1]/tot:.3f}; >= key {ge}/2000")
        if (mt, tot) != want: bad.append(f"{tag} {mt}/{tot} != {want[0]}/{want[1]}")
    # order gain: pkt_v8_*.txt from run_pkt_v8.sh vs V11's tool runs
    for leaf in ("f101r", "f124r"):
        ref = open(f"{V11D}/pkt_{leaf}_split.txt").read(); f = f"{HERE}/pkt_v8_{leaf}_split.txt"
        got = open(f).read() if os.path.exists(f) else ""
        ok = got == ref; out.append(f"order gain {leaf}, runner 13's split draft, key_v8_cells.tsv: {'identical to' if ok else 'DIFFERS from'} {V11}'s "
                                    f"pkt_{leaf}_split.txt ({ref.split(chr(10))[0]}; {ref.rstrip().split(chr(10))[-1]})")
        if not ok: bad.append(f"order gain {leaf} not reproduced")
        for suf, what in (("split_nb", "same tokens labelled 4TRI_NB (info)"), ("v8", "v8 token assignment, conflicts left 4TRI (info)")):
            g = f"{HERE}/pkt_v8_{leaf}_{suf}.txt"
            if os.path.exists(g):
                t = open(g).read().rstrip().split("\n"); out.append(f"order gain {leaf}, {what}: {t[0]}; {t[-1]}")
            else: bad.append(f"missing {g}")
    out.append("REPRODUCED: " + ("yes" if not bad else "NO -- " + "; ".join(bad)))
    return "\n".join(out) + "\n", bad
def main():
    rows, log = assign(); files = {TOK: tok_tsv(rows), V8: build(rows), CELLS8: cells8()}; files.update(drafts(rows))
    if CHECK:
        stale = [os.path.relpath(f, HERE) for f, t in files.items() if not os.path.exists(f) or open(f).read() != t]
        if stale: sys.exit("STALE " + " ".join(stale))
    else:
        for f, t in files.items():
            os.makedirs(os.path.dirname(f), exist_ok=True); open(f, "w").write(t)
    txt, bad = repro(files[V8], rows, log)
    if CHECK:
        if open(RES).read() != txt: sys.exit("STALE build_key_v8_result.txt")
        print("check OK")
    else:
        open(RES, "w").write(txt); print(txt, end="")
    if bad: sys.exit(1)
if __name__ == "__main__": main()
