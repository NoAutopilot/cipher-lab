#!/usr/bin/env python3
"""Known-answer leave-one-run-out control + shuffled-pairing control for the fr3625-lauriere-1593
no.10 alignment (NX-LAU, rule 3). Ground truth = D. Bourdeau's key_lauriere.txt 12-entry table
(the office's own interlinear decipherment read against no.10's seven glossed runs, R1-R7), used
here only as an independent known-answer check on our own DP alignment, not copied as the result.
"""
import csv, random, sys, itertools
sys.path.insert(0, '/home/user/cipher-lab/tools')
import interlinear_align as ia

RUNS = [
    ("R1", "le Pape ... traitera avant que le Roy soit Catholique",
     "10 197 Δ124 28# 99 159+ 25 ✗ 335 141 288"),
    ("R2", "nous avions pris parole de luy qu'aussitost que Sa Majesté auroit esté a la messe qu'il traicteroit sans",
     "Δ57 9n 92# 10 54 20 17 262 25 103 56nΔ 25 13 ✗ 101 54y+ 184y ω.6. 22n27 39E Δ‡ω 28 ⱨ 54y+ 3? λ14q"),
    ("R3", "attendre la volonté du pape", "26 βω 346 59 XX"),
    ("R4", "sur la response qu'a eue de la ligue a", "69.6.26n52 ‡16 25 16⊥y 17.6.34 61y ω57hy"),
    ("R5", "aucun faut avec nostre confiance de ne pouvoir recognoistre le Roy Catholique qui ne viendroient jamais a cest terme que n'eussions la volonté du pape",
     "9Δ 203 100 51#Δ26n Δ Eω 44q 8 120‡16 17 23.303 26 150 ✗ 25 92y 36P26. 8q 248 23⊥n 27 187.6 346 59 XX"),
    ("R6", "le pape ne", "185 25 29 18 12 344 234 P2n 8hq 28.9 97+ 304 ωq24nμ y‡ 25 XX qy EP 26 55h 29 39 27 54hΔ 56‡n"),
    ("R7", "catholique sans attendre autre chose de", "141 320 ω+λqn‡y 101Δ26 154 Ey 26 44q ωqh Δ54q+"),
]

# ground truth: raw cipher token -> acceptable folded meaning(s), from key_lauriere.txt
GT = {
    "✗": {"que"},
    "335": {"leroy", "roy"},
    "346": {"volont", "volonte", "volonté".replace("é","e")},
    "59": {"du"},
    "XX": {"pape"},
    "141": {"soit"},
    "288": {"catholique"},
    "103": {"aussitost"}, "56nΔ": {"aussitost"},
    "101": {"samajeste", "majeste"}, "54y+": {"samajeste", "majeste"},
    "184y": {"auroit"},
    "25": {"le", "la", "que"},
    "26": {"a", "de"},
}

def fold(s):
    return ia.fold(s.lower())

def build_surrogate_map(runs):
    tm = {}
    nxt = 100
    for _, _, cipher in runs:
        for t in cipher.split():
            if t not in tm:
                tm[t] = nxt
                nxt += 1
    return tm

def pairs_from(runs, tm):
    out = []
    for run_id, plain, cipher in runs:
        toks = cipher.split()
        surrogate = ' '.join(str(tm[t]) for t in toks)
        out.append({'plain_line': run_id, 'plain_raw': plain, 'cipher_line': run_id, 'cipher_raw': surrogate})
    return out

def known_answer_loo(runs, tm, label):
    per_run = []
    total_c = total_q = 0
    for i in range(len(runs)):
        train = runs[:i] + runs[i+1:]
        held_id, held_plain, held_cipher = runs[i]
        train_pairs = pairs_from(train, tm)
        _, _, counts, shown = ia.run_align(train_pairs, floor=0)
        held_toks = held_cipher.split()
        qualifying = 0
        correct = 0
        for t in held_toks:
            if t not in GT:
                continue
            val = tm[t]
            cnt = counts.get(val)
            if not cnt or sum(cnt.values()) < 2:
                continue  # value not attested >=2 times in the other six
            qualifying += 1
            top, _ = ia.top_of(cnt)
            if fold(top) in {fold(m) for m in GT[t]}:
                correct += 1
        acc = correct / qualifying if qualifying else None
        per_run.append((held_id, qualifying, correct, acc))
        total_q += qualifying
        total_c += correct
    mean_acc = total_c / total_q if total_q else None
    print(f"-- {label} --")
    for held_id, q, c, acc in per_run:
        print(f"  {held_id}: qualifying={q} correct={c} acc={'%.3f' % acc if acc is not None else 'n/a (0 qualifying)'}")
    print(f"  TOTAL qualifying tokens={total_q} correct={total_c} mean_acc={'%.3f' % mean_acc if mean_acc is not None else 'n/a'}")
    return total_q, total_c, mean_acc

if __name__ == '__main__':
    tm = build_surrogate_map(RUNS)
    print("(a) known-answer leave-one-run-out, true pairing")
    known_answer_loo(RUNS, tm, "true pairing")
    print()
    print("(b) shuffled-pairing control: gloss texts permuted across cipher lines, 10 permutations")
    plains = [p for _, p, _ in RUNS]
    ciphers = [c for _, _, c in RUNS]
    ids = [i for i, _, _ in RUNS]
    rng = random.Random(20260926)
    accs = []
    for k in range(10):
        perm = plains[:]
        while True:
            rng.shuffle(perm)
            if all(perm[j] != plains[j] for j in range(len(plains))):
                break
        shuffled_runs = [(ids[j], perm[j], ciphers[j]) for j in range(len(ids))]
        tq, tc, macc = known_answer_loo(shuffled_runs, tm, f"shuffle {k+1}")
        if macc is not None:
            accs.append(macc)
    if accs:
        print(f"\nshuffle mean over {len(accs)} permutations with >=1 qualifying token: {sum(accs)/len(accs):.3f} (range {min(accs):.3f}-{max(accs):.3f})")
    else:
        print("\nno shuffle permutation produced any qualifying token")
