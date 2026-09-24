#!/usr/bin/env python3
"""16th-c. Italian letter corpus filter, feeding tools/italian_ngram.py (same normalisation and model format).

Written 24 Sept 2026 for ciphers/fr4687-paleologue-nevers (Mantua, 1562-1564). Own code.

italian_ngram.py's own filter keeps 15th-c. Lombard chancery paragraphs (nuy, havemo, epso). Letters of the
1550s-1570s printed in 19th-c. editions are mixed with the editor's modern prose, so this filter keeps a
paragraph when period letter markers (et, V.S., Signoria, havere/haver, fusse, anchora, perho, ...) outnumber
19th-c. editorial markers (ed, degli, dell', accented è used as verb, footnote apparatus), and Latin/French is
rare. Everything else (normalisation, '#' word boundaries, the model) is italian_ngram.py's.

  python3 tools/italian16_corpus.py SRC.txt... --out corpus.txt [--exclude FILE]
  python3 tools/italian_ngram.py build corpus.txt --out model.npz
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from italian_ngram import fold, norm, paragraphs  # noqa: E402

PERIOD = set("et v s vs sig signor signoria ill illmo illma ecc eccellenza excellentia havere haver havuto "
             "havendo ho hauere hauer hauuto fusse fussi fosse anchora ancho perho pero cosi hoggi hora "
             "mi vi ci ne gli lo la le quale qual quanto piu cardinale duca duchessa madama mantova mantoa "
             "baso bascio mano mani affettionato affettionatissimo servitore figliuolo figlio madre "
             "nostro vostro vostra nostra alla alle al del delle dal con che non per".split())
MODERN = set("ed degli dell nell dall sull furono veniva pubblicato pubblicata archivio documento documenti "
             "codice vedi pag cit ibid op nota lettera lettere secolo storia storico autografo autografa "
             "originale edizione stampa stampato biblioteca".split())
FOREIGN = set("est une qui dans pour sont avec nous vous quod sunt eius atque enim nobis quae autem ipse "
              "ipsum illius dominus domini nostri sancti eiusdem item ipsius quam hoc esse erat fuit los las "
              "muy senor the and of".split())


def keep(par):
    w = re.findall(r"[a-z]+", fold(par))
    n = len(w)
    if n < 15:
        return False
    p = sum(1 for x in w if x in PERIOD)
    m = sum(1 for x in w if x in MODERN)
    f = sum(1 for x in w if x in FOREIGN)
    f += sum(1 for x in w if len(x) > 3 and re.search(r"(orum|arum|ibus|unt)$", x))
    et = w.count("et")
    junk = sum(1 for x in re.findall(r"\S+", par) if not re.search(r"[A-Za-zÀ-ÿ]{2}", x))
    return (et >= 1 and p >= 0.25 * n and m <= max(1, 0.03 * n) and f <= 0.03 * n and junk <= 0.2 * n
            and par.count("]") < 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--exclude")
    a = ap.parse_args()
    excl = []
    if a.exclude:
        excl = [norm(l).strip("#") for l in open(a.exclude, encoding="utf-8") if len(l.strip()) > 20]
    out, per = [], {}
    for src in a.src:
        text = open(src, encoding="utf-8", errors="replace").read()
        text = re.sub(r"-\s*\n\s*", "", text)  # rejoin words hyphenated across OCR lines
        k = t = 0
        for par in paragraphs(text):
            t += 1
            if not keep(par):
                continue
            z = norm(par).strip("#")
            if any(e and e[:40] in z for e in excl):
                continue
            out.append(z)
            k += 1
        per[os.path.basename(src)] = (k, t)
    with open(a.out, "w") as f:
        f.write("\n".join(out) + "\n")
    for s, (k, t) in per.items():
        print(f"{s}: kept {k}/{t}", file=sys.stderr)
    print(f"{len(out)} paragraphs, {sum(len(z) for z in out)} symbols -> {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
