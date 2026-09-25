#!/usr/bin/env python3
"""Cheap test 2, step (d): bullet-tuscany-1944 -- crib drag for a periodic key.

Drags each of the 12 crib words over every offset in the 44-letter body under vig/beau/
varbeau, derives the key fragment that offset+tabula would imply, and checks whether that
fragment is consistent with SOME period P in 1..8 (i.e. positions i, i+P, i+2P... within the
fragment all derive the same key letter) at an offset where the check is non-trivial (some
residue class actually holds >=2 positions -- a fragment shorter than P+1 is periodic at P by
definition and proves nothing).

Matched control: the identical drag run on (a) a synthetic 44-letter English sentence built
around one crib word, enciphered under a real period-5 key, checking that the TRUE offset (where
the crib was actually placed) is found periodic and ranks among the periodic hits; and (b) 3
random 44-letter strings, reporting how many (crib, offset, tabula) triples come back
'periodic <= 8' purely by chance -- the false-positive rate this test's periodicity bar must beat.
"""
import json, os, random, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.insert(0, os.path.join(ROOT, "tools"))

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TABULAS = ["vig", "beau", "varbeau"]
CRIBS = ["GRENADE", "PIN", "PINS", "REINFORCEMENT", "REINFORCEMENTS", "PULL", "THROW", "ENEMY",
         "POSITION", "ATTACK", "TANK", "MG"]
BODY = "CBFUKYYEVOZILOOZVNCWJKQRSAWBYZUGYTZWYBATRSUA"
assert len(BODY) == 44, len(BODY)
PMAX = 8


def idx(c):
    return ord(c) - 65


def key_fragment(cipher_frag, plain_frag, tab):
    """key[i] such that decrypt(cipher_frag[i], key[i], tab) == plain_frag[i]."""
    out = []
    for c, p in zip(cipher_frag, plain_frag):
        cc, pp = idx(c), idx(p)
        if tab == "vig":       # c = p + k  =>  k = c - p
            k = (cc - pp) % 26
        elif tab == "beau":    # c = k - p  =>  k = c + p
            k = (cc + pp) % 26
        else:                  # varbeau: c = p - k  =>  k = p - c
            k = (pp - cc) % 26
        out.append(k)
    return out


def encrypt(plain, key, tab):
    out = []
    for i, c in enumerate(plain):
        k = idx(key[i % len(key)])
        pp = idx(c)
        if tab == "vig":
            cc = (pp + k) % 26
        elif tab == "beau":
            cc = (k - pp) % 26
        else:
            cc = (pp - k) % 26
        out.append(A[cc])
    return "".join(out)


def best_period(frag):
    """Smallest P in 1..PMAX at which frag is periodic AND the check is non-trivial (some
    residue class has >=2 samples). Returns (P, samples_checked) or (None, 0)."""
    n = len(frag)
    for P in range(1, PMAX + 1):
        if n <= P:
            continue  # trivial: no residue class repeats
        classes = defaultdict(list)
        for i, k in enumerate(frag):
            classes[i % P].append(k)
        nontrivial = any(len(v) >= 2 for v in classes.values())
        if not nontrivial:
            continue
        if all(len(set(v)) == 1 for v in classes.values()):
            return P, n
    return None, 0


def drag(body, cribs=CRIBS):
    """Every crib x every offset x every tabula. Returns list of hit dicts (periodic only)."""
    hits = []
    n = len(body)
    for crib in cribs:
        L = len(crib)
        if L > n:
            continue
        for off in range(0, n - L + 1):
            frag = body[off:off + L]
            for tab in TABULAS:
                key = key_fragment(frag, crib, tab)
                P, checked = best_period(key)
                if P is not None:
                    hits.append({"crib": crib, "offset": off, "tab": tab, "period": P,
                                 "key_fragment": "".join(A[k] for k in key), "checked_positions": checked})
    return hits


def build_sentence_with_crib(rng, crib, n=44):
    filler_words = ["THE", "AT", "OUR", "WILL", "NOW", "HOLD", "LINE", "DAWN", "WATCH", "FOR",
                     "SEND", "WITH", "IT", "AND", "NEST"]
    while True:
        words = [crib] + list(filler_words)
        rng.shuffle(words)
        s = ""
        pos_of_crib = None
        for w in words:
            if len(s) + len(w) > n:
                continue
            if w == crib:
                pos_of_crib = len(s)
            s += w
            if len(s) == n:
                return s, pos_of_crib
        if len(s) < n and pos_of_crib is not None:
            pad = "".join(rng.choice(A) for _ in range(n - len(s)))
            return s + pad, pos_of_crib


def main():
    out = {}

    # --- target ---
    hits = drag(BODY)
    out["target"] = {
        "n_hits": len(hits),
        "hits": hits,
        "min_period_found": min((h["period"] for h in hits), default=None),
    }

    # --- control A: true offset must be found periodic ---
    runs = []
    for i, crib in enumerate(["PULL", "ATTACK", "PIN"]):
        rng = random.Random(3000 + i)
        plain, true_off = build_sentence_with_crib(rng, crib)
        key = [rng.randrange(26) for _ in range(5)]  # real period-5 key
        keystr = "".join(A[k] for k in key)
        tab = TABULAS[i % 3]
        cipher = encrypt(plain, keystr, tab)
        chits = drag(cipher, cribs=[crib])
        true_hit = [h for h in chits if h["offset"] == true_off and h["tab"] == tab]
        runs.append({
            "seed": i, "crib": crib, "true_offset": true_off, "true_tab": tab, "true_period": 5,
            "plain": plain, "cipher": cipher, "n_hits_this_crib": len(chits),
            "true_offset_found_periodic": bool(true_hit),
            "true_offset_period_found": true_hit[0]["period"] if true_hit else None,
        })
    out["control_true_offset"] = {
        "runs": runs,
        "true_offset_found_count": sum(1 for r in runs if r["true_offset_found_periodic"]),
    }

    # --- control B: random text, false-positive rate ---
    fp_runs = []
    for i in range(3):
        rrng = random.Random(4000 + i)
        rand_body = "".join(rrng.choice(A) for _ in range(44))
        rhits = drag(rand_body)
        fp_runs.append({"seed": i, "random_body": rand_body, "n_hits": len(rhits)})
    out["control_random"] = {"runs": fp_runs, "total_hits": sum(r["n_hits"] for r in fp_runs)}

    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test2d_output.json")
    json.dump(out, open(outpath, "w", encoding="utf-8"), indent=1)
    print(f"target: {out['target']['n_hits']} periodic (<=8) hits across {len(CRIBS)} cribs x all offsets x 3 tabulas")
    print(f"control true-offset found periodic: {out['control_true_offset']['true_offset_found_count']}/3")
    print(f"control random false positives: {out['control_random']['total_hits']} hits across 3 seeds")
    print(f"written {outpath}")


if __name__ == "__main__":
    main()
