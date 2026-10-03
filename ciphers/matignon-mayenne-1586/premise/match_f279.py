#!/usr/bin/env python3
"""Score the pre-registered crib-match rule (premise/prereg_f279.md) on a clear-text transcription of fr.15572
ff.279-280, with controls C1 (crib swap), C2 (text swap: f.282 margin, Tomokiyo) and C3 (positive control).

  python3 premise/match_f279.py premise/f279r_reconciled.tsv [more.tsv ...]   (TSV: line<TAB>text)
Exit 0 always; prints a table. Rule, normalisation and gate are fixed by the prereg; do not tune here.
"""
import re, sys, unicodedata, pathlib

HERE = pathlib.Path(__file__).resolve().parent
TARGET = ["doubte", "amis", "roussiere", "grand", "nombre"]
C1 = {"f143": ["laisse", "entendre", "voulloit", "partir", "malcontant"],
      "f111": ["villeroi", "verres", "lettre", "fais", "roi"],
      "f260": ["arriva", "hier", "olleron", "matin", "venu"]}
SECONDARY = ["guiolle", "aiguillon", "eguillon", "roussiere", "fontenai", "poudre"]
WINDOW, GATE = 60, 4


def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if not unicodedata.combining(c))
    w = w.replace("u", "v").replace("j", "i").replace("y", "i")
    w = re.sub(r"[^a-z]", "", w)
    return re.sub(r"(.)\1+", r"\1", w)


def tokens(text):
    text = re.sub(r"<del>.*?</del>", " ", text)
    text = text.replace("{", " ").replace("}", " ").replace("'", " ").replace("’", " ")
    out = []
    for raw in text.split():
        if "[?]" == raw.strip(".,;:/"):
            out.append("#")          # wildcard that matches nothing
            continue
        raw = re.sub(r"\[\?\]", "", raw).replace("[", "").replace("]", "")
        n = norm(raw)
        if n:
            out.append(n)
    return out


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def hit(cw, tok):
    if tok == "#":
        return False
    c = norm(cw)
    return lev(c, tok) <= (1 if len(c) <= 5 else 2)


def score(crib, toks):
    best, where = 0, None
    for s in range(max(1, len(toks) - WINDOW + 1)):
        win = toks[s:s + WINDOW]
        # longest in-order subsequence of crib words matched in window (exact DP)
        dp = [[0] * (len(win) + 1) for _ in range(len(crib) + 1)]
        for i in range(1, len(crib) + 1):
            for j in range(1, len(win) + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + hit(crib[i - 1], win[j - 1]))
        if dp[-1][-1] > best:
            best, where = dp[-1][-1], s
    return best, where


def f282():
    html = (HERE.parent.parent.parent / "sources/cryptiana/web/henryiii.htm").read_text(errors="replace")
    i = html.index("l'arme sera emploie")
    j = html.index("de deca", html.index("envo", i)) + len("de deca")
    return html[i:j]


def main():
    toks = []
    for p in sys.argv[1:]:
        for ln in pathlib.Path(p).read_text().splitlines()[1:]:
            if "\t" in ln:
                toks += tokens(ln.split("\t", 1)[1])
    print(f"text tokens: {len(toks)} (wildcards {toks.count('#')})")
    t, at = score(TARGET, toks)
    print(f"TARGET f276 crib: {t}/5 (window start {at}) -> {'MATCH' if t >= GATE else 'NO MATCH'} (gate {GATE})")
    c1max = 0
    for k, crib in C1.items():
        s, _ = score(crib, toks)
        c1max = max(c1max, s)
        print(f"C1 crib-swap {k}: {s}/5")
    ctl = tokens(f282())
    c2, _ = score(TARGET, ctl)
    print(f"C2 text-swap f282 margin ({len(ctl)} tok): {c2}/5")
    planted = ctl[:20] + tokens("la guiolle est en doute du pu pour les amys de la rousiere sont et grant nonbre") + ctl[20:]
    c3, _ = score(TARGET, planted)
    print(f"C3 positive control (planted respelled crib in f282): {c3}/5 (must be 5)")
    valid = c1max < GATE and c2 < GATE and c3 == 5
    print(f"controls valid: {valid}; verdict: {('MATCH' if t >= GATE else 'NO MATCH') if valid else 'NON-TEST'}")
    print("secondary (distance <= 2):")
    for w in SECONDARY:
        hits = [(i, x) for i, x in enumerate(toks) if x != '#' and lev(norm(w), x) <= 2]
        print(f"  {w}: {hits}")


if __name__ == "__main__":
    main()
