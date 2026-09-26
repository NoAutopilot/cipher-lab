#!/usr/bin/env python3
"""MAL-MONO (26 Sept 2026): grep everything already transcribed for malsburg-hessen-1636 for the
G.G./A.A./K.K. monogram labels bMALS found on f.32/f.33, and for any sign glyph_map.tsv or
equivalences.tsv maps to a diamond/lozenge/sigil, per NOTES.md's "One-line follow-up suggestion"
(line ~1419) and NEXT-STEPS.tsv's top runnable row for this account. Disk-only, no judgement of
what a hit means (CLAUDE.md rule 10: search result, not a crib call). Scans:
  - pool/pooled.tsv and every recon_*/ciphertext_draft*.tsv (per-line sign streams)
  - every recon_*/disagreements.tsv (per-token A/B alternate readings)
  - manual_witness_settled*.tsv, dup_align.tsv (settled/aligned values)
  - cribs.tsv (code column + left/right_context + word columns)
  - clear_00*.txt (prose transcriptions)
  - glyph_map.tsv, equivalences.tsv (checked for a diamond/lozenge/sigil label only)
Writes mono_hits.tsv: file, line, leaf, position, token, label, context_before, context_after, note.
"""
import csv
import glob
import os
import re

TARGETS = {
    "G.G.": re.compile(r"^G\.?G\.?$", re.IGNORECASE),
    "A.A.": re.compile(r"^A\.?A\.?$", re.IGNORECASE),
    "K.K.": re.compile(r"^K\.?K\.?$", re.IGNORECASE),
}
SIGIL_WORDS = re.compile(r"diamond|lozenge|sigil", re.IGNORECASE)

ROOT = os.path.dirname(os.path.abspath(__file__))
hits = []


def leaf_from_line_id(line_id):
    """Leaf id is the 3-4 digit group immediately before the trailing _L<n> line marker
    (hstam_4_h_1411_0023_L46 -> 0023), not the shelfmark's own 1411 folder number earlier
    in the same string."""
    m = re.search(r"_(\d{3,4})_L\d+$", line_id or "")
    if m:
        return m.group(1)
    m = re.search(r"_(\d{4})_", line_id or "")
    return m.group(1) if m else ""


def label_for(token):
    t = (token or "").strip()
    if not t:
        return None
    for label, pat in TARGETS.items():
        if pat.match(t):
            return label
    return None


def add_hit(path, line_id, leaf, position, token, label, before, after, note=""):
    hits.append({
        "file": os.path.relpath(path, ROOT),
        "line": line_id, "leaf": leaf or leaf_from_line_id(line_id), "position": position,
        "token": token, "label": label,
        "context_before": " ".join(str(x) for x in before[-5:]),
        "context_after": " ".join(str(x) for x in after[:5]),
        "note": note,
    })


def scan_sign_stream_tsv(path):
    """pooled.tsv / ciphertext_draft*.tsv shape: line, position, sign, ..."""
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if not rows or "sign" not in rows[0]:
        return
    by_line = {}
    for row in rows:
        by_line.setdefault(row.get("line", ""), []).append(row)
    for lid, rws in by_line.items():
        def poskey(rw):
            try:
                return int(rw.get("position", rw.get("col", "0")) or 0)
            except ValueError:
                return 0
        rws.sort(key=poskey)
        toks = [rw.get("sign", "") for rw in rws]
        for i, rw in enumerate(rws):
            tok = rw.get("sign", "")
            label = label_for(tok)
            pos = rw.get("position", rw.get("col", ""))
            if label:
                add_hit(path, lid, "", pos, tok, label, toks[max(0, i - 5):i], toks[i + 1:i + 6],
                        note=f"grade={rw.get('confidence', '')}")
            if SIGIL_WORDS.search(tok):
                add_hit(path, lid, "", pos, tok, "SIGIL-WORD", toks[max(0, i - 5):i], toks[i + 1:i + 6])


def scan_disagreements_tsv(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for row in rows:
        for col in ("A", "B"):
            tok = row.get(col, "")
            label = label_for(tok)
            if label:
                add_hit(path, row.get("line", ""), "", row.get("col", ""), tok, label, [], [],
                        note=f"disagreement col {col}, flagged={row.get('flagged', '')}")
            if SIGIL_WORDS.search(tok or ""):
                add_hit(path, row.get("line", ""), "", row.get("col", ""), tok, "SIGIL-WORD", [], [], note=col)


def scan_manual_witness(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if not rows or "value" not in rows[0]:
        return
    for row in rows:
        tok = row.get("value", "")
        label = label_for(tok)
        if label:
            add_hit(path, row.get("line", ""), "", row.get("col", ""), tok, label, [], [],
                    note=f"source={row.get('source', '')}")


def scan_dup_align(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for row in rows:
        for col in ("f28_group", "f30_group"):
            tok = row.get(col, "")
            label = label_for(tok)
            if label:
                add_hit(path, row.get("idx", ""), "", "", tok, label, [], [], note=col)


def scan_cribs(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for row in rows:
        leaf = row.get("leaf", "")
        lid = row.get("line", "")
        pos = row.get("position", "")
        code = row.get("code", "")
        lbl = label_for(code)
        if lbl:
            add_hit(path, lid, leaf, pos, code, lbl, [], [], note="code column")
        for ctxcol in ("left_context", "right_context", "word"):
            text = row.get(ctxcol, "") or ""
            toks = text.split()
            for i, t in enumerate(toks):
                tclean = t.strip(",.;:")
                label = label_for(tclean) or label_for(t)
                if label:
                    add_hit(path, lid, leaf, pos, t, label, toks[max(0, i - 5):i], toks[i + 1:i + 6],
                            note=f"{ctxcol} column")
            if SIGIL_WORDS.search(text):
                add_hit(path, lid, leaf, pos, text, "SIGIL-WORD", [], [], note=ctxcol)


def scan_text(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    for ln, line in enumerate(lines, start=1):
        toks = line.split()
        for i, t in enumerate(toks):
            tclean = t.strip(",.;:()[]")
            label = label_for(tclean)
            if label:
                add_hit(path, f"L{ln}", "", i + 1, t, label, toks[max(0, i - 5):i], toks[i + 1:i + 6],
                        note="prose")
        if SIGIL_WORDS.search(line):
            add_hit(path, f"L{ln}", "", "", line.strip()[:80], "SIGIL-WORD", [], [], note="prose")


def main():
    sign_stream_files = [os.path.join(ROOT, "pool", "pooled.tsv")]
    for d in sorted(glob.glob(os.path.join(ROOT, "recon_*"))):
        for fn in ("ciphertext_draft.tsv", "ciphertext_draft_ciphonly.tsv"):
            p = os.path.join(d, fn)
            if os.path.exists(p):
                sign_stream_files.append(p)
    for p in sign_stream_files:
        scan_sign_stream_tsv(p)

    for d in sorted(glob.glob(os.path.join(ROOT, "recon_*"))):
        p = os.path.join(d, "disagreements.tsv")
        if os.path.exists(p):
            scan_disagreements_tsv(p)

    for p in sorted(glob.glob(os.path.join(ROOT, "manual_witness_settled*.tsv"))):
        scan_manual_witness(p)

    dup_align = os.path.join(ROOT, "dup_align.tsv")
    if os.path.exists(dup_align):
        scan_dup_align(dup_align)

    cribs = os.path.join(ROOT, "cribs.tsv")
    if os.path.exists(cribs):
        scan_cribs(cribs)

    for p in sorted(glob.glob(os.path.join(ROOT, "clear_00*.txt"))):
        scan_text(p)

    for p in (os.path.join(ROOT, "glyph_map.tsv"), os.path.join(ROOT, "equivalences.tsv")):
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                text = f.read()
            if SIGIL_WORDS.search(text):
                add_hit(p, "", "", "", "", "SIGIL-WORD", [], [], note="found in file")

    out_path = os.path.join(ROOT, "mono_hits.tsv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["file", "line", "leaf", "position", "token", "label", "context_before",
                    "context_after", "note"])
        for h in hits:
            w.writerow([h["file"], h["line"], h["leaf"], h["position"], h["token"], h["label"],
                        h["context_before"], h["context_after"], h["note"]])

    print(f"{len(hits)} hits written to mono_hits.tsv")
    for h in hits:
        print(h)


if __name__ == "__main__":
    main()
