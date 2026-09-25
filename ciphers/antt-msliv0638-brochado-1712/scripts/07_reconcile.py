#!/usr/bin/env python3
"""Reconcile pass A (ciphertext_appendix.tsv/plaintext_appendix.tsv) against pass B
(passB_cipher.tsv/passB_plain.tsv, PX-BROPASSB's blind second pass) for the Deciffrada
appendix of antt-msliv0638-brochado-1712.

tools/reconcile_passes.py does not fit this layout (it expects a per-line-of-image 'wide'
or 'long' pass keyed by a crop id, not a per-entry token table with an entry_label key and
no crop directory), so this is the short script named as the fallback in
.claude/briefs/runs/2026-09-25-lane-px-bropassb.md step 2.

Method: entries are matched by the (leaf, entry_label) key (identical set in both passes,
checked before this script is run). Within each entry, pass A's and pass B's ordered coded
-token lists are aligned with difflib.SequenceMatcher (trailing '?' uncertainty markers
stripped for comparison only). 'equal' opcodes are grade H; 'replace'/'delete'/'insert'
opcodes are logged to disagreements.tsv and graded M. The overall agreement rate is
(aligned positions in 'equal' blocks) / (aligned positions total, i.e. every opcode block
contributes max(len_a, len_b) to the denominator -- an insertion or deletion counts against
agreement the same way reconcile_passes.py's own doc string defines it).

Writes (in the target folder):
  disagreements.tsv   leaf, entry_label, a_position, a_token, b_token, kind
  agreement.tsv        leaf, entry_label, a_tokens, b_tokens, agree, aligned, share
  ciphertext_appendix.tsv   rewritten in place with a new trailing 'grade' column (H/M)
  plaintext_appendix.tsv    rewritten in place with a new trailing 'grade' column (H/M),
                            graded by exact string equality of deciffrada_line (period
                            spelling kept, so a real orthographic variant reads as M, not
                            silently normalised)

Exits 0. Prints the overall token agreement rate and the deciffrada_line agreement rate.
"""
import csv
import difflib
import sys
from pathlib import Path

REPORT_ONLY = "--report-only" in sys.argv
# --report-only (added PX-BROGLYPH, 25 Sept 2026): print the agreement numbers against passB without
# touching disagreements.tsv/agreement.tsv/ciphertext_appendix.tsv/plaintext_appendix.tsv or the 90% gate --
# for checking a post-settlement agreement rate against pass B after a hand-settlement pass (e.g.
# scripts/08_settle_glyphs.py) that deliberately keeps some of pass A's tokens over pass B's on crop
# evidence, so "matches passB" is a report figure here, not the grading rule (grades come from the
# settlement script itself, which knows which side it sided with and why).

D = Path(__file__).resolve().parent.parent


def load_tsv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_tsv(path, rows, fields):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def norm_tok(t):
    return t.rstrip("?").strip()


def group_by_entry(rows):
    g = {}
    for r in rows:
        g.setdefault((r["leaf"], r["entry_label"]), []).append(r)
    for k in g:
        g[k].sort(key=lambda r: int(r["position"]))
    return g


def main():
    a_tok = load_tsv(D / "ciphertext_appendix.tsv")
    b_tok = load_tsv(D / "passB_cipher.tsv")
    a_line = load_tsv(D / "plaintext_appendix.tsv")
    b_line = load_tsv(D / "passB_plain.tsv")

    ga, gb = group_by_entry(a_tok), group_by_entry(b_tok)
    keys = sorted(set(ga) | set(gb))
    missing_a = [k for k in keys if k not in ga]
    missing_b = [k for k in keys if k not in gb]
    if missing_a or missing_b:
        print("WARNING entry-key mismatch, A missing:", missing_a, "B missing:", missing_b, file=sys.stderr)

    disagreements = []
    agreement_rows = []
    out_tok_rows = []
    total_aligned = total_agree = 0

    for k in keys:
        la, lb = ga.get(k, []), gb.get(k, [])
        aseq = [norm_tok(r["token"]) for r in la]
        bseq = [norm_tok(r["token"]) for r in lb]
        sm = difflib.SequenceMatcher(None, aseq, bseq, autojunk=False)
        e_aligned = e_agree = 0
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                n = i2 - i1
                total_aligned += n
                total_agree += n
                e_aligned += n
                e_agree += n
                for off in range(n):
                    out_tok_rows.append({**la[i1 + off], "grade": "H"})
            elif tag == "replace":
                n = max(i2 - i1, j2 - j1)
                total_aligned += n
                e_aligned += n
                for off in range(i2 - i1):
                    ra = la[i1 + off]
                    bval = bseq[j1 + off] if off < (j2 - j1) else "(missing in B)"
                    disagreements.append((k[0], k[1], ra["position"], ra["token"], bval, "replace"))
                    out_tok_rows.append({**ra, "grade": "M"})
                for off in range(i2 - i1, j2 - j1):
                    disagreements.append((k[0], k[1], "(extra in B)", "", bseq[j1 + off], "extra-b"))
            elif tag == "delete":
                n = i2 - i1
                total_aligned += n
                e_aligned += n
                for off in range(n):
                    ra = la[i1 + off]
                    disagreements.append((k[0], k[1], ra["position"], ra["token"], "(missing in B)", "delete"))
                    out_tok_rows.append({**ra, "grade": "M"})
            elif tag == "insert":
                n = j2 - j1
                total_aligned += n
                e_aligned += n
                for off in range(n):
                    disagreements.append((k[0], k[1], "(extra in B)", "", bseq[j1 + off], "insert"))
        agreement_rows.append({
            "leaf": k[0], "entry_label": k[1],
            "a_tokens": str(len(la)), "b_tokens": str(len(lb)),
            "agree": str(e_agree), "aligned": str(e_aligned),
            "share": f"{(e_agree / e_aligned):.3f}" if e_aligned else "n/a",
        })

    disagreements_rows = [
        {"leaf": l, "entry_label": e, "a_position": p, "a_token": at, "b_token": bt, "kind": kind}
        for (l, e, p, at, bt, kind) in disagreements
    ]
    if not REPORT_ONLY:
        write_tsv(D / "disagreements.tsv", disagreements_rows,
                  ["leaf", "entry_label", "a_position", "a_token", "b_token", "kind"])
        write_tsv(D / "agreement.tsv", agreement_rows,
                  ["leaf", "entry_label", "a_tokens", "b_tokens", "agree", "aligned", "share"])

    # deciffrada_line word-level agreement (exact full-line string match is too strict a
    # metric for a >=1000-char line -- one accent or spacing slip fails the whole line even
    # when every word agrees -- so this reports both, and the gate below uses the token rate)
    def group_line(rows):
        g = {}
        for r in rows:
            g[(r["leaf"], r["entry_label"])] = r
        return g

    gal, gbl = group_line(a_line), group_line(b_line)
    line_exact_agree = line_total = 0
    word_agree = word_total = 0
    for k in keys:
        ra, rb = gal.get(k, {}), gbl.get(k, {})
        a_dec = (ra.get("deciffrada_line") or "").strip()
        b_dec = (rb.get("deciffrada_line") or "").strip()
        line_total += 1
        if a_dec and a_dec == b_dec:
            line_exact_agree += 1
        aw, bw = a_dec.split(), b_dec.split()
        wsm = difflib.SequenceMatcher(None, aw, bw, autojunk=False)
        for tag, i1, i2, j1, j2 in wsm.get_opcodes():
            n = max(i2 - i1, j2 - j1)
            word_total += n
            if tag == "equal":
                word_agree += i2 - i1

    tok_rate = total_agree / total_aligned if total_aligned else 0.0
    line_rate = line_exact_agree / line_total if line_total else 0.0
    word_rate = word_agree / word_total if word_total else 0.0
    print(f"token agreement (gate metric): {total_agree}/{total_aligned} = {tok_rate:.4f}")
    print(f"deciffrada_line exact full-string match: {line_exact_agree}/{line_total} = {line_rate:.4f}")
    print(f"deciffrada_line word-level agreement: {word_agree}/{word_total} = {word_rate:.4f}")
    print(f"disagreements: {len(disagreements_rows)} rows" + ("" if REPORT_ONLY else " -> disagreements.tsv"))

    if REPORT_ONLY:
        return 0

    if tok_rate < 0.90:
        print("GATE: token agreement under 90% -- stopping after writing the numbers "
              "(disagreements.tsv, agreement.tsv); ciphertext_appendix.tsv and "
              "plaintext_appendix.tsv left unchanged, per job brief step 2", file=sys.stderr)
        return 1

    out_tok_rows.sort(key=lambda r: (r["leaf"], r["entry_label"], int(r["position"])))
    write_tsv(D / "ciphertext_appendix.tsv", out_tok_rows,
              ["leaf", "entry_label", "position", "token", "token_type", "grade"])
    line_out_rows = []
    for k in keys:
        ra, rb = gal.get(k, {}), gbl.get(k, {})
        a_dec = (ra.get("deciffrada_line") or "").strip()
        b_dec = (rb.get("deciffrada_line") or "").strip()
        row = dict(ra) if ra else {"leaf": k[0], "entry_label": k[1]}
        row["grade"] = "H" if a_dec and a_dec == b_dec else "M"
        line_out_rows.append(row)
    line_out_rows.sort(key=lambda r: (r["leaf"], r["entry_label"]))
    write_tsv(D / "plaintext_appendix.tsv", line_out_rows,
              ["leaf", "entry_label", "cipher_line", "deciffrada_line", "grade"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
