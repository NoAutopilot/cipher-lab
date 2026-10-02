#!/usr/bin/env python3
"""Value-blind reconciliation of two blind sign passes (HARVEST-D2, 28 Sept 2026).

Aligns passA and passB per passage by sign id (Needleman-Wunsch: match +2, look-alike pair +1, mismatch -1, gap -1)
and writes:
  <out>_agreement.tsv     one row per aligned position: posA idA confA posB idB confB status merged merged_conf
  <out>_disagreements.tsv the positions a third blind eye must settle from the crop (status split/gapA/gapB)
  <out>.tsv               the merged sequence (passage pos sign_id conf note), '?' where the split is unsettled; a
                          position the adjudicator marks NONE is dropped here (positions renumber), while the
                          agreement file and the adjudication sheet keep the pre-adjudication numbering
Rules, applied without any sign value (no file but the two passes is read):
  agree               same id -> keep, conf = the lower of the two
  split, one side H   the H side, conf M (unless --adjudicated names the position: the third reader's verdict wins)
  split, otherwise    '?' pending adjudication (row listed in disagreements)
  gap (one pass only) kept as '?' with a note if the present side is H, else dropped -- listed either way
Agreement = agreed positions / aligned positions (gaps count as aligned).  --adjudicated FILE applies a third reader's
answers (columns passage pos sign_id conf) to the '?' rows and rewrites <out>.tsv.
"""
import argparse, csv, sys
from collections import OrderedDict

LOOKALIKE = {frozenset(p) for p in [("S30", "S49"), ("S30", "S73"), ("S49", "S73"), ("S24", "S88"), ("S37", "S74"),
                                    ("S55", "S94"), ("S13", "S69"), ("S13", "S95"), ("S69", "S95"), ("S65", "S80"),
                                    ("S53", "S54"), ("S37", "S54"), ("S26", "S66"), ("S16", "S42"), ("S74", "S77"),
                                    ("S47", "S91"), ("S91", "S93"), ("S58", "S76"), ("S59", "S50"),
                                    # NEVBIR-47 (2 Oct 2026): extra cells of the fr.3252 f.47r brief
                                    ("X_DSLASH", "S49"), ("X_DSLASH", "S73"), ("X_DSLASH", "S30"), ("X_DCARET", "S23"),
                                    ("X_DCARET", "S97"), ("S23", "S97"), ("X_TRI", "S16"), ("X_TRI", "S42")]}


def load(fn):
    P = OrderedDict()
    for r in csv.DictReader(open(fn), delimiter="\t"):
        P.setdefault(r["passage"].strip(), []).append((r["sign_id"].strip(), r.get("conf", "M").strip() or "M",
                                                        r.get("alt", "").strip(), r.get("note", "").strip()))
    return P


def sc(a, b):
    if a == b:
        return 2
    if frozenset((a, b)) in LOOKALIKE:
        return 1
    return -1


def align(A, B):
    n, m = len(A), len(B); G = -1
    S = [[0] * (m + 1) for _ in range(n + 1)]; T = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = i * G; T[i][0] = "u"
    for j in range(1, m + 1): S[0][j] = j * G; T[0][j] = "l"
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d = S[i - 1][j - 1] + sc(A[i - 1][0], B[j - 1][0]); u = S[i - 1][j] + G; l = S[i][j - 1] + G
            S[i][j], T[i][j] = max((d, "d"), (u, "u"), (l, "l"))
    i, j, out = n, m, []
    while i or j:
        t = T[i][j]
        if t == "d": out.append((i - 1, j - 1)); i -= 1; j -= 1
        elif t == "u": out.append((i - 1, None)); i -= 1
        else: out.append((None, j - 1)); j -= 1
    return out[::-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("passA"); ap.add_argument("passB"); ap.add_argument("--out", required=True)
    ap.add_argument("--adjudicated")
    a = ap.parse_args()
    A, B = load(a.passA), load(a.passB)
    adj = {}
    if a.adjudicated:
        for r in csv.DictReader(open(a.adjudicated), delimiter="\t"):
            adj[(r["passage"].strip(), int(r["pos"]))] = (r["sign_id"].strip(), r.get("conf", "M").strip() or "M")
    agree_f = open(a.out + "_agreement.tsv", "w"); dis_f = open(a.out + "_disagreements.tsv", "w")
    mer_f = open(a.out + ".tsv", "w")
    agree_f.write("passage\tposA\tidA\tconfA\tposB\tidB\tconfB\tstatus\tmerged\tmerged_conf\n")
    dis_f.write("passage\tmerged_pos\tposA\tidA\tconfA\tposB\tidB\tconfB\tstatus\tnoteA\tnoteB\n")
    mer_f.write("passage\tpos\tsign_id\tconf\tnote\n")
    tot = agreed = 0; splits = 0; merged_rows = []  # (passage, sign, conf, note); NONE rows dropped at write time
    for p in list(A) + [q for q in B if q not in A]:
        la, lb = A.get(p, []), B.get(p, [])
        pos = 0
        for ia, ib in align(la, lb):
            tot += 1
            ea = la[ia] if ia is not None else None; eb = lb[ib] if ib is not None else None
            if ea and eb:
                if ea[0] == eb[0]:
                    st, mid, mc = "agree", ea[0], min(ea[1], eb[1], key="HML".index) if ea[1] in "HML" and eb[1] in "HML" else "M"
                    if mc == "L": mc = "M"  # both readers named the same cell: at least M
                    agreed += 1
                elif ea[1] == "H" and eb[1] != "H": st, mid, mc = "split_H_A", ea[0], "M"
                elif eb[1] == "H" and ea[1] != "H": st, mid, mc = "split_H_B", eb[0], "M"
                else: st, mid, mc = "split", "?", "L"
            elif ea:
                st, mid, mc = "gapB", ("?" if ea[1] == "H" else None), "L"
            else:
                st, mid, mc = "gapA", ("?" if eb[1] == "H" else None), "L"
            if mid is not None:
                pos += 1
                key = (p, pos)
                if key in adj and st != "agree":  # a third reader's verdict overrides the confidence rule too
                    mid, mc = adj[key]; st += "+adj"
            agree_f.write(f"{p}\t{ia + 1 if ia is not None else ''}\t{ea[0] if ea else ''}\t{ea[1] if ea else ''}\t"
                          f"{ib + 1 if ib is not None else ''}\t{eb[0] if eb else ''}\t{eb[1] if eb else ''}\t{st}\t"
                          f"{mid or ''}\t{mc if mid else ''}\n")
            if st.startswith(("split", "gap")) and not st.endswith("+adj"):
                splits += 1
                dis_f.write(f"{p}\t{pos if mid is not None else ''}\t{ia + 1 if ia is not None else ''}\t{ea[0] if ea else ''}\t"
                            f"{ea[1] if ea else ''}\t{ib + 1 if ib is not None else ''}\t{eb[0] if eb else ''}\t"
                            f"{eb[1] if eb else ''}\t{st}\t{ea[3] if ea else ''}\t{eb[3] if eb else ''}\n")
            if mid is not None:
                merged_rows.append((p, mid, mc, "" if st == "agree" else st))
    npos = {}
    for p, mid, mc, note in merged_rows:
        if mid == "NONE":  # adjudicator: no sign at that position (one reader's phantom); dropped, later positions renumber
            continue
        npos[p] = npos.get(p, 0) + 1
        mer_f.write(f"{p}\t{npos[p]}\t{mid}\t{mc}\t{note}\n")
    print(f"aligned {tot}, agreed {agreed} ({agreed / tot:.2f}), unsettled {splits}")


if __name__ == "__main__":
    main()
