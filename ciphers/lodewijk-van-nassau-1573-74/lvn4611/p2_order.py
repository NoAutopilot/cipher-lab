"""LVN-P2B (15 Oct 2026): ordering repair of WVO 4611 p2_L13-L33 (PREREG-LVN-4611.md addendum LVN-P2B, step 2), applied by ../settle.py
as the last 4611 stage. The rows of p2_L13-L33 and the LVN-P2RETX inserts p2_R* are re-sequenced into the deskewed physical lines K13-K35
by the LVN-P2RETX map: a placed row (match/differs) or an insert takes (K, kpos); an unplaced row (no-ink, near-value 'duplicate') follows
the nearest preceding row of its own transcription line (else precedes the following one); a block duplicate (retx_p2.build.dup) is
retired to lvn4611/retired_p2.tsv unless graded H or C (kept, attached as unplaced). Rows become line p2_K<KK>, position 1..n; sign,
confidence and alt unchanged; why gains 'LVN-P2B order: was <line>/<position>'. No value changes.
usage: imported by ../settle.py (reorder(draft) -> (draft, retired, report))."""
import re
from pathlib import Path
import p2b_map, retx_p2
HERE = Path(__file__).resolve().parent
SEG = re.compile(r"^p2_(L(1[3-9]|2\d|3[0-3])|R\d\d[a-h])$")


def reorder(draft):
    mp = p2b_map.build_map(HERE / "ciphertext_4611_pre_retx.tsv")
    dup = retx_p2.build.dup
    at = {(r[0], r[1]): (r[4], int(r[5])) for r in mp if r[4]}
    idx = [i for i, r in enumerate(draft) if SEG.match(r["line"])]
    i0, i1 = idx[0], idx[-1] + 1
    assert idx == list(range(i0, i1)), "LVN-P2B: p2_L13-L33/R segment not contiguous"
    seg = draft[i0:i1]
    keys = [None] * len(seg); retired = []; kept_dup = []
    for j, r in enumerate(seg):
        if r["line"].startswith("p2_R"):
            m = re.search(r"\b(K\d\d)/(\d+);", r["why"]); keys[j] = (m.group(1), int(m.group(2)), 0, j)
        elif (r["line"], r["position"]) in at:
            K, kp = at[(r["line"], r["position"])]; keys[j] = (K, kp, 0, j)
    for j, r in enumerate(seg):
        if keys[j] is not None: continue
        if (r["line"], r["position"]) in dup:
            if r["confidence"] not in ("H", "C"):
                retired.append(dict(r)); keys[j] = "retired"; continue
            kept_dup.append(r)
        prev = [keys[q] for q in range(j - 1, -1, -1) if seg[q]["line"] == r["line"] and isinstance(keys[q], tuple)]
        if prev: keys[j] = (prev[0][0], prev[0][1], 1, j); continue
        nxt = [q for q in range(j + 1, len(seg)) if seg[q]["line"] == r["line"] and (seg[q]["line"], seg[q]["position"]) in at]
        assert nxt, ("LVN-P2B: unplaceable row", r["line"], r["position"])
        K, kp = at[(seg[nxt[0]]["line"], seg[nxt[0]]["position"])]; keys[j] = (K, kp, -1, j)
    order = sorted((j for j in range(len(seg)) if keys[j] != "retired"), key=lambda j: keys[j])
    out, n = [], {}
    for j in order:
        r = dict(seg[j]); K = keys[j][0]; n[K] = n.get(K, 0) + 1
        r["why"] = (r["why"] + "; " if r["why"] else "") + f"LVN-P2B order: was {r['line']}/{r['position']}"
        r["line"], r["position"] = f"p2_{K}", str(n[K])
        out.append(r)
    draft[i0:i1] = out
    rep = dict(rows_in=len(seg), rows_out=len(out), retired=len(retired), kept_dup=[(r["line"], r["position"], r["sign"], r["confidence"]) for r in kept_dup],
               lines=len(n))
    return draft, retired, rep
