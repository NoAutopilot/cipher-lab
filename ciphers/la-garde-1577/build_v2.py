#!/usr/bin/env python3
"""L4 (24 Sept 2026): reconcile the three witnesses for 6179 (ciphertext_6179_passA.tsv,
ciphertext_6179_passB.tsv, ciphertext_6179_L1.tsv) and the two for 6467 (ciphertext_6467_passA.tsv,
ciphertext_6467_L1.tsv) into ciphertext_6179_v2.tsv / ciphertext_6467_v2.tsv.

  python3 ciphers/la-garde-1577/build_v2.py [--check]

Pass A (the L3 crop-based Sonnet pass) is the reference for line/position numbering and for page/run
segmentation, since it used the manuscript's own line numbers throughout, unlike L1 (its own running
sub-index for 6467, and an off-by-one line-label shift on 6179 p3 -- both cosmetic, not content, since the
token *sequence* and per-page totals match A's; see NOTES 'L4'). 6179 pass B never reached 6467 or 6179 p3
(stopped over cap, NOTES 'L3'), so 6179 p2 reconciles 3-way (A, B, L1) and 6179 p3 reconciles 2-way (A, L1);
6467's two cipher runs (p2 lines 6-8 and 10-11) both reconcile 2-way (A, L1) throughout, there being no pass B.

Reuses tools/reconcile_passes.py's own norm_sign/nw alignment (imported, not re-implemented) so a page's
signs align the same way this repo's other reconciliations do. Adds one refinement reconcile_passes.py does
not have: a *base-digit* majority pass for cells where the literal strings (which include the '^'/'~' marks)
have no majority but the underlying numeral does -- e.g. A=24^, B=29^, C=24 has no 2-of-3 literal match, but
A and C agree the numeral is 24, so this writes 24 at conf M with a note, rather than leaving it an
unresolved 3-way split. A true split (no two witnesses agreeing on the numeral itself) is written as A's own
reading at conf M with the other reading(s) in `alt`, marked `unresolved` -- this pass could not adjudicate
these further: no PIL/ImageMagick and no network are available to this brief (crop tooling needs one or the
other), so the only recourse was a direct read of the full-page PNG already on disk, which was legible enough
to confirm 6467 run 2's position 13/14 split (A's 07 + a following free-standing mark, matched against L1's
merged "07~~" -- the image shows a small mark after the second "07" on that line, confirming A's segmentation,
not L1's) but not fine enough, at this resolution and without a crop tool, to safely call the small number of
remaining true numeral-level disagreements (listed below) rather than guess.

Exits 0 always (a reconciliation, not a check); prints the count of H/M rows and the unresolved list.
"""
import csv, os, sys, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import reconcile_passes as rp  # noqa: E402


class NS:
    pass


def default_args():
    a = NS()
    a.split_chars = False
    a.keep_dots = False
    a.keep_plain = False
    a.halves = False
    a.line_sub = []
    a.flag_conf = ",".join(sorted(rp.FLAG_CONF))
    a.flag = set(a.flag_conf.split(","))
    return a


def load_rows(path):
    """[(line, pos, group, conf, left, right, margin_or_None)], original file order, header-driven."""
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8") if l.strip()]
    head, body = rows[0], rows[1:]
    hi = {h: i for i, h in enumerate(head)}
    out = []
    for r in body:
        if len(r) <= hi["sign"] if "sign" in hi else len(r) <= hi.get("group", 2):
            continue
        gi = hi.get("sign", hi.get("group"))
        ci = hi.get("conf", hi.get("confidence"))
        li = hi.get("left")
        ri = hi.get("right")
        mi = hi.get("margin_note")

        def g(i):
            return r[i] if i is not None and i < len(r) else ""

        out.append((r[hi["line"]], r[hi["pos"]], g(gi), g(ci), g(li), g(ri), g(mi) if mi is not None else None))
    return out


def sign_seq(rows, a):
    """[(sign, flagged), ...] normalised the way reconcile_passes.py would for these rows."""
    out = []
    for _, _, grp, conf, *_ in rows:
        s = rp.norm_sign(grp, a)
        if s:
            sign, fl = s
            out.append((sign, fl or conf in a.flag))
    return out


def base_digit(sign):
    """numeral part of a sign, or None for a pure mark ('[mark]', '[mark]15' -> '15')."""
    s = sign
    if s.startswith("[mark]"):
        s = s[len("[mark]"):]
    s = s.rstrip("^~")
    return s if s and s[0].isdigit() else None


def reconcile_page(a_rows, other_rows_list, a):
    """a_rows: A's rows with metadata (may include dropped tokens, so filter through norm_sign first).
    other_rows_list: list of witness rows (each like a_rows) to align against A.
    Returns list of dict per A position, plus a list of unattached insertions from other witnesses."""
    a_filtered = [(ln, pos, s[0], s[1]) for (ln, pos, grp, conf, *_ ) in a_rows
                  for s in [rp.norm_sign(grp, a)] if s]
    a_signs = [(s, fl) for _, _, s, fl in a_filtered]
    other_seqs = [sign_seq(rows, a) for rows in other_rows_list]
    aligned = [[] for _ in a_filtered]  # aligned[i] = list of (witness_index, sign, flagged) landing on A position i
    insertions = []  # (witness_index, sign, flagged, after_a_index)
    for wi, seq in enumerate(other_seqs):
        pairs = rp.nw([c[0] for c in a_signs], [c[0] for c in seq])
        last = -1
        for i, j in pairs:
            if i is not None:
                if j is not None:
                    aligned[i].append((wi, seq[j][0], seq[j][1]))
                last = i
            else:
                insertions.append((wi, seq[j][0], seq[j][1], last))
    out = []
    for i, (ln, pos, sign, flagged) in enumerate(a_filtered):
        others = aligned[i]  # [(witness_index, sign, flagged)]
        all_signs = [sign] + [s for _, s, _ in others]
        n_witness = 1 + len(others)
        literal_majority = None
        if n_witness >= 2:
            from collections import Counter
            cnt = Counter(all_signs)
            best, best_n = cnt.most_common(1)[0]
            if best_n > 1 and (len(cnt) == 1 or best_n > sorted(cnt.values())[-2]):
                literal_majority = best
        note = ""
        conf = "H"
        final = sign
        if n_witness == 1:
            conf, note = "M", "only A read this line"
        elif literal_majority is not None:
            if literal_majority == sign and all(s == sign for s in all_signs):
                conf = "H"
            else:
                final = literal_majority
                conf, note = "M", "literal majority"
        else:
            digits = [base_digit(s) for s in all_signs]
            present = [d for d in digits if d is not None]
            from collections import Counter
            dc = Counter(present)
            if present and dc.most_common(1)[0][1] > 1 and (len(dc) == 1 or dc.most_common(1)[0][1] > dc.most_common(2)[1][1]):
                dmaj = dc.most_common(1)[0][0]
                if base_digit(sign) == dmaj:
                    final = sign
                else:
                    for s in all_signs:
                        if base_digit(s) == dmaj:
                            final = s
                            break
                conf, note = "M", f"digit majority {dmaj}, mark disputed"
            else:
                conf, note = "M", "unresolved: " + "/".join(f"w{wi}:{s}" for wi, s in enumerate([sign] + [s for _, s, _ in others]))
        alt = "/".join(f"{'A' if k == -1 else 'BC'[k]}:{s}" for k, s in ([(-1, sign)] + [(wi, s) for wi, s, _ in others]) if s != final)
        out.append(dict(line=ln, pos=pos, group=final, conf=conf, alt=alt, note=note))
    return out, insertions


def write_v2(rows, insertions, path, witness_names):
    with open(path, "w", encoding="utf-8") as f:
        f.write("line\tpos\tgroup\tconf\talt\tnote\n")
        for r in rows:
            f.write("\t".join([r["line"], r["pos"], r["group"], r["conf"], r["alt"], r["note"]]) + "\n")
        for wi, s, fl, after in insertions:
            f.write("\t".join(["", "", s, "M", "", f"insertion by {witness_names[wi]} after A idx {after}, not in A"]) + "\n")


# Manually confirmed against images/06467_p2.png this pass (L4): the mark after the second "07" on the
# third cipher line (run 2) is legible as a small free-standing stroke distinct from the digit, matching A's
# split ("07" then "[mark]") rather than L1's merged "07~~". No other unresolved cell was legible enough at
# this image's resolution (no crop tool, no PIL, no network available to this brief) to call safely.
CONFIRMED = {("p2L11", "8"): "confirmed on images/06467_p2.png (L4): a separate mark follows the second 07, matching A's split over L1's merged 07~~"}


def apply_confirmed_pair(rows_ins):
    rows, ins = rows_ins
    for r in rows:
        key = (r["line"], r["pos"])
        if key in CONFIRMED and "unresolved" in r["note"]:
            r["note"] = CONFIRMED[key]
    return rows, ins


def summarise(rows, insertions, label):
    h = sum(1 for r in rows if r["conf"] == "H")
    m = sum(1 for r in rows if r["conf"] == "M")
    unresolved = [r for r in rows if "unresolved" in r["note"]]
    print(f"{label}: {len(rows)} rows, H {h}, M {m} (of which unresolved {len(unresolved)}), "
          f"{len(insertions)} witness insertion(s) not in A")
    for r in unresolved:
        print(f"    {r['line']} pos {r['pos']}: A={r['group']} alt={r['alt']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if a v2 file on disk is stale")
    args = ap.parse_args()
    a = default_args()

    # 6179: p2 three-way (A, B, L1), p3 two-way (A, L1; pass B never reached p3)
    a_p2 = [r for r in load_rows(os.path.join(HERE, "ciphertext_6179_passA.tsv")) if r[0].startswith("p2")]
    b_p2 = [r for r in load_rows(os.path.join(HERE, "ciphertext_6179_passB.tsv")) if r[0].startswith("p2")]
    l1_p2 = [r for r in load_rows(os.path.join(HERE, "ciphertext_6179_L1.tsv")) if r[0].startswith("p2")]
    a_p3 = [r for r in load_rows(os.path.join(HERE, "ciphertext_6179_passA.tsv")) if r[0].startswith("p3")]
    l1_p3 = [r for r in load_rows(os.path.join(HERE, "ciphertext_6179_L1.tsv")) if r[0].startswith("p3")]

    rows_p2, ins_p2 = reconcile_page(a_p2, [b_p2, l1_p2], a)
    rows_p3, ins_p3 = reconcile_page(a_p3, [l1_p3], a)
    summarise(rows_p2, ins_p2, "6179 p2 (A,B,L1)")
    summarise(rows_p3, ins_p3, "6179 p3 (A,L1)")
    write_v2(rows_p2 + rows_p3, [(0 if wi == 0 else 1, s, fl, after) for wi, s, fl, after in ins_p2] +
             [(1, s, fl, after) for wi, s, fl, after in ins_p3],
             os.path.join(HERE, "ciphertext_6179_v2.tsv"), {0: "passB", 1: "L1"})

    # 6467: two cipher runs on p2 (lines 6-8 and 10-11 in A's numbering), each two-way (A, L1)
    a_all = load_rows(os.path.join(HERE, "ciphertext_6467_passA.tsv"))
    l1_all = load_rows(os.path.join(HERE, "ciphertext_6467_L1.tsv"))
    a_run1 = [r for r in a_all if r[0] in ("p2L6", "p2L7", "p2L8")]
    a_run2 = [r for r in a_all if r[0] in ("p2L10", "p2L11")]
    l1_run1 = [r for r in l1_all if r[0] in ("p2L1", "p2L2", "p2L3")]
    l1_run2 = [r for r in l1_all if r[0] in ("p2L4", "p2L5")]
    rows_r1, ins_r1 = reconcile_page(a_run1, [l1_run1], a)
    rows_r2, ins_r2 = apply_confirmed_pair(reconcile_page(a_run2, [l1_run2], a))
    summarise(rows_r1, ins_r1, "6467 run1 (A,L1)")
    summarise(rows_r2, ins_r2, "6467 run2 (A,L1)")
    write_v2(rows_r1 + rows_r2, [(1, s, fl, after) for _, s, fl, after in ins_r1] +
             [(1, s, fl, after) for _, s, fl, after in ins_r2],
             os.path.join(HERE, "ciphertext_6467_v2.tsv"), {1: "L1"})

    print("wrote ciphertext_6179_v2.tsv, ciphertext_6467_v2.tsv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
