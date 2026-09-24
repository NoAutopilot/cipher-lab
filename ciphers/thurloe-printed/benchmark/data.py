"""Real-data inputs for the Fauconberg benchmark (LANE T worker F, 24 Sept 2026).

groups(): the cipher group sequence of the nine Fauconberg-to-H.-Cromwell windows (P16-P24), from the
CLEANED lines of <Pn>/ciphertext.txt only. A token that is not a clean integer 1-60 after stripping
trailing punctuation (OCR merges such as 1141 or 54926, name capitals A. V. Z., stray words) ends the
fragment; fragments shorter than 2 are dropped. Nothing from the plain lines enters this sequence.

truth(): the scoring key, from Birch's printed decipherment. Cipher lines whose neighbouring [PLAIN]
line has exactly as many letters as the line has tokens (check_interlinear.py's exact matches) give
(group, letter) votes. Two passes: a provisional majority key, then only the pairs that agree with it on
at least half their positions (a pair of equal length but offset text is dropped), then the final vote.
A group enters the key with >= 2 votes and a top-letter share >= 0.5. Letters folded i=j, u=v.
"""
import collections, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROWS = ["P16", "P17", "P18", "P19", "P20", "P21", "P22", "P23", "P24"]
sys.path.insert(0, str(HERE.parent))
import check_interlinear as ci  # noqa: E402


def clean(t):
    t = t.rstrip(".,;:-")
    return int(t) if re.fullmatch(r"\d{1,2}", t) and 1 <= int(t) <= 60 else None


def groups():
    frags = []
    for r in ROWS:
        for k, v in ci.items(r):
            if k != "C":
                continue
            cur = []
            for t in v:
                g = clean(t)
                if g is None:
                    if len(cur) >= 2:
                        frags.append(cur)
                    cur = []
                else:
                    cur.append(g)
            if len(cur) >= 2:
                frags.append(cur)
    return frags


def fold(s):
    return s.lower().replace("j", "i").replace("v", "u")


def _pairs():
    out = []
    for r in ROWS:
        for v, b in ci.pairs(ci.items(r), 0):
            if b:
                out.append([(clean(t), fold(c)) for t, c in zip(v, b[1])])
    return out


def _vote(pairs):
    votes = collections.defaultdict(collections.Counter)
    for p in pairs:
        for g, c in p:
            if g is not None:
                votes[g][c] += 1
    key = {}
    for g, cnt in votes.items():
        c, n = cnt.most_common(1)[0]
        if n >= 2 and n / sum(cnt.values()) >= 0.5:
            key[g] = c
    return key, votes


def _shifted(k0):
    """Neighbour lines within +-3 letters (check_interlinear tolerance 3), each placed at the offset
    (-3..+3) that best agrees with the exact-match key k0; kept at >= 0.6 agreement over >= 5 known."""
    out = []
    for r in ROWS:
        for v, b in ci.pairs(ci.items(r), 3):
            if not b:
                continue
            gs, pl = [clean(t) for t in v], fold(b[1])
            best = None
            for off in range(-3, 4):
                p = [(g, pl[i + off]) for i, g in enumerate(gs) if 0 <= i + off < len(pl)]
                known = [(g, c) for g, c in p if g in k0]
                if len(known) >= 5:
                    a = sum(k0[g] == c for g, c in known) / len(known)
                    if best is None or a > best[0]:
                        best = (a, p)
            if best and best[0] >= 0.6:
                out.append(best[1])
    return out


def truth(extended=True):
    """extended=False: exact-length lines only. True: exact key, then +-3 lines aligned by best offset."""
    key, votes, a, b = _truth_exact()
    if not extended:
        return key, votes, a, b
    sh = _shifted(key)
    key2, votes2 = _vote(sh)
    return key2, votes2, len(sh), len(sh)


def _truth_exact():
    pairs = _pairs()
    k0, _ = _vote(pairs)
    kept = []
    for p in pairs:
        known = [(g, c) for g, c in p if g in k0]
        if known and sum(k0[g] == c for g, c in known) / len(known) >= 0.5:
            kept.append(p)
    key, votes = _vote(kept)
    return key, votes, len(pairs), len(kept)


if __name__ == "__main__":
    f = groups()
    n = sum(map(len, f))
    ke, _, np_, nk = truth(False)
    print(f"exact: pairs {np_}, kept {nk}, key groups {len(ke)}")
    key, votes, np_, nk = truth()
    print("disagreements exact vs extended:", {g: (ke[g], key.get(g)) for g in ke if key.get(g) != ke[g]})
    cov = sum(1 for x in f for g in x if g in key)
    print(f"fragments {len(f)} tokens {n} distinct {len({g for x in f for g in x})}")
    print(f"exact-length pairs {np_}, kept {nk}; key groups {len(key)}; token coverage {cov}/{n}")
    for g in sorted(votes):
        print(g, key.get(g, "-"), dict(votes[g].most_common()))
