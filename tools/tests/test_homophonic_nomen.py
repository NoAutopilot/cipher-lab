"""Offline test for homophonic_anneal.anneal_nomen/solve_nomen (R10-SIENA7N, 6 Oct 2026): (1) the incremental score
equals a full re-score of the returned key; (2) on a clean synthetic text with two word-signs the solver recovers the
words and most letters; (3) with an empty vocab no sign ever decodes to more than one letter."""
import random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import homophonic_anneal as H

TXT = ("la signoria vostra sapra che el duca et il signore sono qui per la pace et che non se fa altro che parlare "
       "della guerra et della pace con li ambasciatori del re et del papa per che la cosa e grande ") * 40


def main():
    m = H.Model([TXT], 3)
    rng = random.Random(4)
    words = TXT.split()[:300]
    seq, truth = [], {}
    homs = {}
    for w in words:
        if w in ("che", "et"):
            seq.append("W" + w); truth["W" + w] = w
        else:
            for ch in H.fold(w):
                k = homs.setdefault(ch, [f"{ch}{i}" for i in range(2)])
                s = rng.choice(k); seq.append(s); truth[s] = ch
    sc, key = H.solve_nomen(seq, m, 4, 20000, 1, 1.0, ["che", "et", "per", "non"], 0.15)[0]
    full = H.score(m, "".join(key[x] for x in seq), 1.0)  # word_bonus 0
    assert abs(sc - full) < 1e-6, (sc, full)
    acc = sum(key[x] == truth[x] for x in seq) / len(seq)
    assert key["Wche"] == "che" and key["Wet"] == "et", (key["Wche"], key["Wet"])
    assert acc > 0.8, acc
    sc2, key2 = H.solve_nomen(seq, m, 1, 3000, 2, 1.0, [], 0.15)[0]
    assert all(len(v) == 1 for v in key2.values())
    print(f"ok: token accuracy {acc:.3f}")


if __name__ == "__main__":
    main()
