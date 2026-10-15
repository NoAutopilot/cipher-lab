"""LVN-P2RETX (15 Oct 2026): re-transcription of the mixed WVO 4611 p2 lines K13-K35 (PREREG-LVN-4611.md addendum LVN-P2RETX).
Lines come from tools/iiif_lines.py --image <p2 300-dpi png> --region 250,140,2200,3000 --prefix p2 --deskew --centres $(cat p2_centres.txt).
usage:
  python3 retx_p2.py crops LINES_DIR OUTDIR      half-line crops per batch call, opaque ids, shuffled per call seed; writes retx_p2_key.tsv
                                                (images to OUTDIR in scratch, never into git)
  python3 retx_p2.py gate READS.tsv             control gate per call (reads: call, img, tokens comma-separated)"""
import sys, os, csv, random, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parent
BATCH = {1: ([f"K{k:02d}" for k in range(13, 25)], "K04"), 2: ([f"K{k:02d}" for k in range(25, 36)], "K12")}
CALLS = {"A1": (1, 20261015), "B1": (1, 20261016), "A2": (2, 20261017), "B2": (2, 20261018)}
CONTROL_ROWS = {"K04": "p2_L04", "K12": "p2_L12"}


def split_x(im):
    import numpy as np
    a = np.array(im.convert("L")); h = a.shape[0]
    col = (a[int(h * .2):int(h * .85)] < 150).sum(0)
    mid = a.shape[1] // 2; best = None
    for x in range(mid - 300, mid + 300):
        if col[max(0, x - 6):x + 7].sum() == 0:
            if best is None or abs(x - mid) < abs(best - mid): best = x
    return best if best is not None else mid


def crops(lines, out):
    from PIL import Image
    rows = []
    for call, (b, seed) in CALLS.items():
        tg, ctl = BATCH[b]; items = []
        for K in tg + [ctl]:
            im = Image.open(os.path.join(lines, f"p2_L{K[1:]}.jpg")); x = split_x(im)
            items += [(K, "a", im.crop((0, 0, x, im.height))), (K, "b", im.crop((x, 0, im.width, im.height)))]
        random.Random(seed).shuffle(items)
        os.makedirs(os.path.join(out, call), exist_ok=True)
        for i, (K, half, c) in enumerate(items, 1):
            img = f"{call}-{i:02d}"
            c.save(os.path.join(out, call, img + ".png")); rows.append((call, img, K, half))
    with open(HERE / "retx_p2_key.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["call", "img", "K", "half"]); w.writerows(rows)
    print(len(rows), "images")


def nums(toks):
    return [t for t in toks if t.replace("?", "").isdigit() or "?" in t and any(c.isdigit() for c in t)]


def line_reads(reads_path):
    key = {(r["call"], r["img"]): (r["K"], r["half"]) for r in csv.DictReader(open(HERE / "retx_p2_key.tsv"), delimiter="\t")}
    got = {}
    for r in csv.DictReader(open(reads_path), delimiter="\t"):
        K, half = key[(r["call"], r["img"])]
        got.setdefault(r["call"], {}).setdefault(K, {})[half] = [t.strip() for t in r["tokens"].split(",") if t.strip()]
    return {c: {K: d.get("a", []) + d.get("b", []) for K, d in v.items()} for c, v in got.items()}


def gate(reads_path):
    rd = line_reads(reads_path)
    ct = list(csv.DictReader(open(HERE.parent / "ciphertext_4611.tsv"), delimiter="\t"))
    res = {}
    for call, (b, _) in CALLS.items():
        if call not in rd: continue
        ctl = BATCH[b][1]; L = CONTROL_ROWS[ctl]
        ref = [(r["sign"], r["confidence"]) for r in ct if r["line"] == L and r["sign"].isdigit()]
        got = nums(rd[call].get(ctl, []))
        sm = difflib.SequenceMatcher(a=[s for s, _ in ref], b=got, autojunk=False)
        ok = set()
        for blk in sm.get_matching_blocks():
            ok.update(range(blk.a, blk.a + blk.size))
        hn = [i for i, (_, g) in enumerate(ref) if g == "H"]; hit = sum(1 for i in hn if i in ok)
        need = -(-len(hn) * 8 // 10)
        res[call] = (hit, len(hn), hit >= need)
        print(f"{call} control {ctl}: {hit}/{len(hn)} H numerals exact (gate >= {need}) {'PASS' if hit >= need else 'FAIL'}")
    return res


if __name__ == "__main__":
    if sys.argv[1] == "crops": crops(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "gate": gate(sys.argv[2])


# ---- stage 2: reconcile, map, insert (run after the reads; see the addendum) ----
def norm(t):
    t = t.strip().replace("|cut", "")
    return t.lower() if t.startswith("=") else t


def recon_lines(reads_path, recon_path):
    """A/B per K line aligned; A == B stands; the rest from recon_p2.tsv (K, a_idx, token) or left '?'."""
    rd = line_reads(reads_path); g = gate(reads_path)
    rec = {}
    if Path(recon_path).exists():
        for r in csv.DictReader(open(recon_path), delimiter="\t"):
            rec[(r["K"], int(r["n"]))] = r["token"]
    out = []
    for b, (tg, _) in BATCH.items():
        ca, cb = f"A{b}", f"B{b}"
        okA = g.get(ca, (0, 0, False))[2]; okB = g.get(cb, (0, 0, False))[2]
        for K in tg:
            A = [norm(t) for t in rd.get(ca, {}).get(K, [])] if okA else []
            B = [norm(t) for t in rd.get(cb, {}).get(K, [])] if okB else []
            if okA and okB:
                sm = difflib.SequenceMatcher(a=A, b=B, autojunk=False); seq = []
                for op, i1, i2, j1, j2 in sm.get_opcodes():
                    if op == "equal":
                        seq += [(A[i], A[i], B[j - i1 + j1] if False else A[i], "A=B") for i in range(i1, i2)]
                    else:
                        aa, bb = A[i1:i2], B[j1:j2]
                        for k in range(max(len(aa), len(bb))):
                            x = aa[k] if k < len(aa) else "-"; y = bb[k] if k < len(bb) else "-"
                            seq.append((None, x, y, "recon"))
                n = 0; rows = []
                for tok, x, y, how in seq:
                    n += 1
                    if tok is None:
                        # numerals: the reconcile's value (recon_p2.tsv); words: A's spelling unless A has none (graded M either way)
                        tok = rec.get((K, n)) or ((x if x != "-" else y) if (x + y).startswith("=") or x.startswith("=") or y.startswith("=") else "?")
                    rows.append((K, n, tok, x, y, how))
                out += rows
            elif okA or okB:
                S = A if okA else B
                out += [(K, i + 1, t, t if okA else "-", t if okB else "-", "single-pass") for i, t in enumerate(S)]
    return out


def wkey(t):
    t = norm(t)
    return ("W" + t[1:2]) if t.startswith("=") else t


def alike(xs, ys):
    """positional pairing is allowed only when every pair agrees in kind (word/numeral) and at least half look alike
    (numerals: same length and one digit equal in place; words: same first letter)."""
    n = 0
    for x, y in zip(xs, ys):
        x, y = norm(x), norm(y)
        if x.startswith("=") != y.startswith("="): return False
        if x.startswith("="): n += x[1:2] == y[1:2]
        else: n += len(x) == len(y) and any(a == b for a, b in zip(x, y))
    return 2 * n >= len(xs)


def build(reads_path, recon_path, ct_path):
    """Map every existing p2_L13-L33 row to the reconciled physical lines; list the ink tokens no row carries."""
    lines = recon_lines(reads_path, recon_path)
    K = {}
    for k, n, tok, x, y, how in lines:
        K.setdefault(k, []).append((n, tok, x, y, how))
    ct = list(csv.DictReader(open(ct_path), delimiter="\t"))
    old = [(i, r) for i, r in enumerate(ct) if "p2_L13" <= r["line"] <= "p2_L33" and not r["sign"].startswith("[")]
    byline = {}
    for i, r in old:
        byline.setdefault(r["line"], []).append(i)
    taken = {}; got = {}; dup = set()
    blocks = []
    for L, idx in byline.items():
        ln = int(L[4:]); seqo = [wkey(ct[i]["sign"]) for i in idx]
        for kk in range(ln - 1, ln + 4):
            kn = f"K{kk:02d}"
            if kn not in K: continue
            seqk = [wkey(t[1]) for t in K[kn]]
            for b in difflib.SequenceMatcher(a=seqo, b=seqk, autojunk=False).get_matching_blocks():
                if b.size >= 2: blocks.append((b.size, L, kn, b.a, b.b))
    blocks.sort(key=lambda b: (-b[0], b[1], b[2]))
    # pass 1: blocks onto free ink tokens only; pass 2 (after the gaps): blocks wholly on taken ink = pass duplicates
    for size, L, kn, a, bb in blocks:
        idx = byline[L]
        rows = [idx[a + j] for j in range(size)]
        ks = [(kn, bb + j) for j in range(size)]
        if any(r in got for r in rows) or any(k in taken for k in ks): continue
        for r, k in zip(rows, ks): got[r] = k; taken[k] = r
    # gaps between two mapped rows of one old line on one physical line, equal length: positional
    for L, idx in byline.items():
        pos = [j for j, i in enumerate(idx) if i in got]
        for p, q in zip(pos, pos[1:]):
            (k1, a1), (k2, a2) = got[idx[p]], got[idx[q]]
            if k1 != k2 or q - p < 2 or a2 - a1 < 2: continue
            gr = [idx[j] for j in range(p + 1, q)]; gk = [(k1, a) for a in range(a1 + 1, a2)]
            if q - p == a2 - a1:      # equal-length gap: positional
                pairs = list(zip(gr, gk))
            else:                     # unequal: single-token value matches inside the gap
                sm = difflib.SequenceMatcher(a=[wkey(ct[i]["sign"]) for i in gr], b=[wkey(K[k1][a][1]) for _, a in gk], autojunk=False)
                pairs = [(gr[b.a + j], gk[b.b + j]) for b in sm.get_matching_blocks() for j in range(b.size)]
            for r, k in pairs:
                if r not in got and k not in taken: got[r] = k; taken[k] = r
    # heads and tails: a run of unmapped rows next to one mapped row, against the free ink run on the same side of that row's token;
    # positional when the two runs have equal length, else single-token value matches only
    def free_run(kn, a, step):
        out = []; a += step
        while 0 <= a < len(K[kn]) and (kn, a) not in taken: out.append((kn, a)); a += step
        return out if step > 0 else out[::-1]
    for L, idx in byline.items():
        j = 0
        while j < len(idx):
            if idx[j] in got: j += 1; continue
            e = j
            while e < len(idx) and idx[e] not in got: e += 1
            gr = idx[j:e]; opts = []          # (free ink run, side the pairing starts from)
            if j > 0: opts.append((free_run(*got[idx[j - 1]], 1), "start"))
            if e < len(idx): opts.append((free_run(*got[idx[e]], -1), "end"))
            ln = int(L[4:])
            for kk in range(ln - 1, ln + 4):      # a run at the head/tail of its old line may sit at the head/tail of a neighbouring line
                kn = f"K{kk:02d}"
                if kn not in K: continue
                if j == 0: opts.append((free_run(kn, -1, 1), "start"))
                if e == len(idx): opts.append((free_run(kn, len(K[kn]), -1), "end"))
            done = False
            for gk, side in opts:                 # positional, the run's own side first; whole run, or >= 2 tokens, all alike-checked
                m = min(len(gk), len(gr))
                if m == 0 or (m < 2 and m < len(gr)): continue
                rr, kk_ = (gr[:m], gk[:m]) if side == "start" else (gr[-m:], gk[-m:])
                if alike([ct[i]["sign"] for i in rr], [K[k][a_][1] for k, a_ in kk_]):
                    for r, k in zip(rr, kk_):
                        if r not in got and k not in taken: got[r] = k; taken[k] = r
                    done = True; break
            if not done:
                for gk, side in opts:             # else single-token value matches
                    if not gk: continue
                    sm = difflib.SequenceMatcher(a=[wkey(ct[i]["sign"]) for i in gr], b=[wkey(K[k][a_][1]) for k, a_ in gk], autojunk=False)
                    for bl in sm.get_matching_blocks():
                        for t in range(bl.size):
                            r, k = gr[bl.a + t], gk[bl.b + t]
                            if r not in got and k not in taken: got[r] = k; taken[k] = r
            j = e
    for size, L, kn, a, bb in blocks:
        rows = [byline[L][a + j] for j in range(size)]
        if all((kn, bb + j) in taken for j in range(size)):
            dup.update(r for r in rows if r not in got)
    mp = []
    for i, r in old:
        if i in got:
            kn, a = got[i]; tok = K[kn][a][1]
            st = "match" if wkey(tok) == wkey(r["sign"]) and (tok.startswith("=") or tok == r["sign"]) else "differs"
            mp.append((r["line"], r["position"], r["sign"], r["confidence"], kn, K[kn][a][0], tok, st))
        else:
            ln = int(r["line"][4:])
            near = any(wkey(t[1]) == wkey(r["sign"]) for kk in range(ln - 1, ln + 4) for t in K.get(f"K{kk:02d}", []))
            mp.append((r["line"], r["position"], r["sign"], r["confidence"], "", "", "", "duplicate" if (i in dup or near) else "no-ink"))
    # ink tokens in no row -> inserts, anchored on the row of the preceding (else following) ink token
    ins = []
    for kn in sorted(K):
        toks = K[kn]; run = []; runs = []
        for a, t in enumerate(toks):
            if (kn, a) in taken:
                if run: runs.append(run); run = []
            else: run.append(a)
        if run: runs.append(run)
        for ri, rr in enumerate(runs):
            prev = [taken[(kn, a)] for a in range(rr[0] - 1, -1, -1) if (kn, a) in taken]
            nxt = [taken[(kn, a)] for a in range(rr[-1] + 1, len(toks)) if (kn, a) in taken]
            if prev: anc = ("after", ct[prev[0]]["line"], ct[prev[0]]["position"])
            elif nxt: anc = ("before", ct[nxt[0]]["line"], ct[nxt[0]]["position"])
            else: anc = ("after", "", "")
            lid = f"p2_R{kn[1:]}{'abcdefgh'[ri]}"
            for j, a in enumerate(rr, 1):
                n, tok, x, y, how = toks[a]
                why = {"A=B": "LVN-P2RETX free read A = B", "recon": "LVN-P2RETX reconcile (A/B differ)", "single-pass": "LVN-P2RETX single pass"}[how]
                ins.append((lid, j, tok, "M", f"A:{x} B:{y}", f"{why}; {kn}/{n}; ink in no 150-dpi row", anc[0], anc[1], anc[2]))
    return lines, mp, ins


def write(reads_path, recon_path, check=False):
    pre = HERE / "ciphertext_4611_pre_retx.tsv"
    lines, mp, ins = build(reads_path, recon_path, pre)
    outs = {"retx_p2_lines.tsv": (["K", "pos", "token", "A", "B", "how"], lines),
            "retx_p2_map.tsv": (["line", "position", "sign", "confidence", "K", "kpos", "ink", "status"], mp),
            "insert_p2retx.tsv": (["line", "position", "sign", "confidence", "alt", "why", "anchor", "anchor_line", "anchor_position"], ins)}
    stale = False
    import io
    for name, (hdr, rows) in outs.items():
        b = io.StringIO(); w = csv.writer(b, delimiter="\t", lineterminator="\n"); w.writerow(hdr); w.writerows(rows)
        p = HERE / name
        if check:
            if not p.exists() or p.read_text() != b.getvalue(): print("STALE", p); stale = True
        else: p.write_text(b.getvalue())
    from collections import Counter
    print("map:", dict(Counter(r[7] for r in mp)), "inserts:", len(ins))
    if stale: sys.exit(1)


if __name__ == "__main__" and sys.argv[1] in ("write", "check"):
    write(HERE / "reads_p2retx.tsv", HERE / "recon_p2.tsv", check=sys.argv[1] == "check")
