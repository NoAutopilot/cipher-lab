#!/usr/bin/env python3
"""Agreement-only reconciliation of two blind passes per Fagel 5177 page (PREREG-HELFAGEL section 1, the reconciliation unit).

  python3 key_rebuild/reconcile_fagel.py TXDIR [--out key_rebuild/fagel_corpus_H.txt] [--stats key_rebuild/fagel_agreement.tsv]

TXDIR holds <page>_A.txt and <page>_B.txt ("crop<TAB>text" per manuscript line). Line-end hyphens ("=", "-") are joined to
the next line in both passes alike. Words are compared after phrase_crib.norm(); a word enters the corpus only where both
passes agree (difflib equal blocks); every disagreement, uncertain word ("[?]", "word[?]") and page boundary becomes "|".
No vision call; the corpus keeps pass A's spelling of agreed words.
"""
import argparse, difflib, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from phrase_crib import norm  # noqa: E402

PAGES = ["s93R", "s94L", "s94R", "s89R", "s90L", "s85L", "s85R", "s87L"]


def words(path):
    txt = ""
    for ln in Path(path).read_text().splitlines():
        t = ln.split("\t", 1)[-1].strip()
        if txt.endswith(("=", "-")):
            txt = txt[:-1] + t
        else:
            txt += " " + t
    out = []
    for w in txt.split():
        out.append("|" if "[?]" in w else w)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("txdir")
    here = Path(__file__).resolve().parent
    ap.add_argument("--out", default=str(here / "fagel_corpus_H.txt"))
    ap.add_argument("--stats", default=str(here / "fagel_agreement.tsv"))
    a = ap.parse_args()
    corpus, stats = [], ["page\twords_A\twords_B\tagreed\tagree_share_of_A"]
    for p in PAGES:
        A, B = words(Path(a.txdir) / f"{p}_A.txt"), words(Path(a.txdir) / f"{p}_B.txt")
        na, nb = [norm(w) if w != "|" else "|" for w in A], [norm(w) if w != "|" else "|" for w in B]
        sm = difflib.SequenceMatcher(None, na, nb, autojunk=False)
        out, agreed = [], 0
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                for k in range(i1, i2):
                    if na[k] == "|" or not na[k]:
                        out.append("|")
                    else:
                        out.append(A[k])
                        agreed += 1
            else:
                out.append("|")
        line = re.sub(r"(\|\s*)+", "| ", " ".join(out)).strip()
        corpus.append(f"# {p}\n{line} |")
        stats.append(f"{p}\t{len(A)}\t{len(B)}\t{agreed}\t{agreed / max(1, len(A)):.3f}")
    Path(a.out).write_text("# Fagel 5177 corpus H (D2-HELFAGEL, 5 Oct 2026): words both blind passes agree on; '|' = break.\n"
                           + "\n".join(corpus) + "\n")
    Path(a.stats).write_text("\n".join(stats) + "\n")
    print("\n".join(stats))


if __name__ == "__main__":
    main()
