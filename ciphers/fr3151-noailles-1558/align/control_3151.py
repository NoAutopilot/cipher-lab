#!/usr/bin/env python3
"""Leave-one-out control for the fr3151-noailles-1558 marginal-gloss alignment (NX-3151G, rule 3).

Unlike fr3625-lauriere-1593 (control_lau.py), there is no independently published ground-truth key to
check against here -- nobody has read this gloss before (rule 10; guiche1551/NOTES.md only quotes two
short phrases of gloss1 without proposing a cipher-value key). So this is a self-consistency check of our
own DP alignment (tools/interlinear_align.py), not a known-answer check.

Data reality (see NOTES.md): only gloss1 (beside block 1, f60r L01-L03) is legible enough to extract word
fragments at all -- 3 lines, one short fragment per line, most of each line cut off by the binding. Gloss2
(beside block 2) is illegible past isolated, unconfident fragments; gloss3 (beside block 3) has a few
legible words but the mapping of which gloss line pairs with which of the 7 cipher lines is itself an
unconfirmed visual inference, not a secure pairing (see NOTES.md). Per this job's own brief ("leave-one-
BLOCK-out"), only a block whose gloss is both legible AND confidently line-paired can serve as training or
held-out data; on that standard, only block 1 qualifies at all -- there is no second or third block to
leave out. This script still runs the closest defensible analogue (leave-one-LINE-out within block 1's own
3 lines) so the numbers are on record, but flags plainly that this is not the brief's block-level design.
"""
import random, sys
sys.path.insert(0, '/home/user/cipher-lab/tools')
import interlinear_align as ia

# (line id, gloss fragment as read -- most of each line lost to the binding, this is what survives,
#  reconciled-draft cipher sign sequence for that line, majority/A-preferred pick, mostly M-grade)
RUNS = [
    ("f60r_L01", "en mauvaise",
     "hookC 20 unk1 9 hash tbar dash arrowL tbar hookC tbar hash 9 slash 10 9 loop6 unk2 pipe 70 loop6 4 tbar dash 20 9"),
    ("f60r_L02", "gouvernement",
     "Hmark circleO slash 70 loop6 Ymark 2 tbar Ymark slash 9 slash 10 tri 6 hash hash plus plus loop6 9 arrowL 2 tbar 9 13 tri tri 2 slash arrowL circleO hookC"),
    ("f60r_L03", "de que iustice",
     "5 6 hash tbar plus plus unk3 2 2 slash hookC tbar 9 13 tri tri 2 slash dash arrowL hookC loop6 hash tbar"),
]


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


def leave_one_out(runs, tm, label):
    """For each held-out line, train the DP on the other two, then check: of the held-out line's own
    sign values, how many were seen (>=2 times, i.e. 'attested twice elsewhere') in the training pair, and
    for those, does the training-derived top meaning appear anywhere in the held-out line's own gloss
    fragment (the closest self-consistency check available without an external ground truth)."""
    per_line = []
    total_c = total_q = 0
    for i in range(len(runs)):
        train = runs[:i] + runs[i + 1:]
        held_id, held_plain, held_cipher = runs[i]
        train_pairs = pairs_from(train, tm)
        _, _, counts, shown = ia.run_align(train_pairs, floor=0)
        held_words = set(fold(w) for w in held_plain.split())
        held_toks = held_cipher.split()
        qualifying = 0
        correct = 0
        for t in held_toks:
            val = tm[t]
            cnt = counts.get(val)
            if not cnt or sum(cnt.values()) < 2:
                continue  # not attested >=2 times in the training pair
            qualifying += 1
            top, _ = ia.top_of(cnt)
            if fold(top) in held_words:
                correct += 1
        acc = correct / qualifying if qualifying else None
        per_line.append((held_id, qualifying, correct, acc))
        total_q += qualifying
        total_c += correct
    mean_acc = total_c / total_q if total_q else None
    print(f"-- {label} --")
    for held_id, q, c, acc in per_line:
        print(f"  {held_id}: qualifying={q} correct={c} acc={'%.3f' % acc if acc is not None else 'n/a (0 qualifying)'}")
    print(f"  TOTAL qualifying={total_q} correct={total_c} mean_acc={'%.3f' % mean_acc if mean_acc is not None else 'n/a (0 qualifying)'}")
    return total_q, total_c, mean_acc


if __name__ == '__main__':
    tm = build_surrogate_map(RUNS)
    print(f"NOTE: only {len(RUNS)} lines have any usable gloss fragment (all from block 1). This is a")
    print("leave-one-LINE-out check, not the brief's leave-one-BLOCK-out (blocks 2 and 3 contributed no")
    print("usable gloss -- see NOTES.md). Reported for the record; treat as informative, not the brief's design.")
    print()
    print("(a) true pairing, leave-one-line-out")
    leave_one_out(RUNS, tm, "true pairing")
    print()
    print("(b) shuffled-pairing control: gloss fragments permuted across the 3 lines, 10 permutations (seed 20260926)")
    plains = [p for _, p, _ in RUNS]
    ciphers = [c for _, _, c in RUNS]
    ids = [i for i, _, _ in RUNS]
    rng = random.Random(20260926)
    accs = []
    for k in range(10):
        perm = plains[:]
        tries = 0
        while True:
            rng.shuffle(perm)
            tries += 1
            if all(perm[j] != plains[j] for j in range(len(plains))) or tries > 50:
                break
        shuffled_runs = [(ids[j], perm[j], ciphers[j]) for j in range(len(ids))]
        tq, tc, macc = leave_one_out(shuffled_runs, tm, f"shuffle {k + 1}")
        if macc is not None:
            accs.append(macc)
    if accs:
        print(f"\nshuffle mean over {len(accs)} permutations with >=1 qualifying token: {sum(accs) / len(accs):.3f} (range {min(accs):.3f}-{max(accs):.3f})")
    else:
        print("\nno shuffle permutation produced any qualifying token")
