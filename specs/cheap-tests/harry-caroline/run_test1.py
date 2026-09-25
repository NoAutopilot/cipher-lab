#!/usr/bin/env python3
"""Cheap test 1 for specs/harry-caroline-1863.json: MASC with word boundaries, jointly on the
Harry and Caroline ads (Evening Standard 1863), single-letter words fixed to a/I, plus a matched
control (real English text cut to the same word-length pattern, random MASC, same solver, 3 seeds).
Written 25 Sept 2026, LANE B2 worker bHAR2. Uses tools/subst_hillclimb.py as a library (CLAUDE.md
Usage 8: shared script, not a private copy) with numpy (installed this session, not in repo reqs).
"""
import itertools, json, random, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from subst_hillclimb import ALPHA, IDX, A, Model, anneal, load_cipher  # noqa: E402

OUT = Path(__file__).resolve().parent

# --- 1. The joint ciphertext, message bodies only (address label / signature stripped) ---
HARRY_WORDS = ["gd", "kzd", "lgsuoabzbt", "hjf", "pw", "ebcvgfm", "klv", "slxdzp", "t", "ugwxbz"]
CAROLINE_WORDS = ["u", "ponngf", "qw", "g", "xtab", "io", "cwldf", "zhnc", "vh", "xwcd"]
JOINT_WORDS = HARRY_WORDS + CAROLINE_WORDS
LENS = [len(w) for w in JOINT_WORDS]
NLETTERS = sum(LENS)


def words_to_frags(words):
    return [list(w) for w in words]


def apply_key(words, keymap):
    return [ "".join(keymap.get(c, "?") for c in w) for w in words ]


def run_main_test():
    model = Model([open(ROOT / "tools/data/pg2701_mobydick.txt", encoding="utf-8", errors="replace").read()])
    frags_all = words_to_frags(JOINT_WORDS)
    # symbol positions: harry_words[8]=='t' single-letter word; caroline_words[0]=='u'; caroline_words[3]=='g'
    combos = list(itertools.product("ai", repeat=3))  # (t, u, g)
    results = []
    for (ft, fu, fg) in combos:
        fixed = {"t": ft, "u": fu, "g": fg}
        res = anneal(frags_all, model, restarts=15, iters=1500, seed=1, fixed=fixed, max_homo=2)
        results.append({"fixed": fixed, "score_per_token": res["score_per_token"],
                         "reading": res["reading"], "key": res["key"]})
    results.sort(key=lambda r: -r["score_per_token"])
    best = results[0]

    # variant: exclude 'ebcvgfm' (tried as a name) from the scored fragments, same fixed combo as best
    frags_excl = [w for w in JOINT_WORDS if w != "ebcvgfm"]
    res_excl = anneal(words_to_frags(frags_excl), model, restarts=15, iters=1500, seed=1,
                       fixed=best["fixed"], max_homo=2)

    out = {
        "n_letters_joint": NLETTERS,
        "word_lengths": LENS,
        "note_spec_letter_counts": "spec's harry_letters=44/caroline_letters=27 (71 total) do not match a"
                                    " direct extraction of the message bodies (harry 43, caroline 31, 74"
                                    " total); recorded here, not corrected in the spec by this worker.",
        "all_combos_sorted_by_score": [
            {"fixed": r["fixed"], "score_per_token": r["score_per_token"]} for r in results
        ],
        "best_combo": {"fixed": best["fixed"], "score_per_token": best["score_per_token"],
                        "reading_words": best["reading"], "key": best["key"]},
        "best_combo_excluding_ebcvgfm": {
            "score_per_token": res_excl["score_per_token"], "reading_words": res_excl["reading"],
            "key": res_excl["key"],
        },
        "homophone_note": "t, u, g are three distinct cipher symbols each standing alone as a single-letter"
                           " word at least once; English single-letter words are only 'a'/'I', so a strict"
                           " one-to-one MASC cannot map all three into {a,i} without a collision -- ran with"
                           " max_homo=2 (homophones allowed) to make the fix satisfiable at all; this alone is"
                           " a negative sign for a plain one-to-one MASC reading of the single-letter words.",
    }
    (OUT / "test1_main.json").write_text(json.dumps(out, indent=1))
    return out


def pick_control_words(source_words_by_len, lens, seed):
    rng = random.Random(seed)
    out = []
    for L in lens:
        choices = source_words_by_len.get(L)
        if not choices:
            raise SystemExit(f"no source word of length {L} found")
        out.append(rng.choice(choices))
    return out


def run_control():
    import re
    text = (ROOT / "tools/data/pg1661_holmes.txt").read_text(encoding="utf-8", errors="replace")
    a = text.find("*** START OF")
    b = text.find("*** END OF")
    if a >= 0 and b > a:
        text = text[text.find("\n", a) + 1:b]
    words = re.findall(r"[A-Za-z]+", text)
    by_len = {}
    for w in words:
        wl = w.lower()
        if all(c in IDX for c in wl):
            by_len.setdefault(len(wl), []).append(wl)

    model = Model([open(ROOT / "tools/data/pg2701_mobydick.txt", encoding="utf-8", errors="replace").read()])
    seed_results = []
    for seed in (1, 2, 3):
        plain_words = pick_control_words(by_len, LENS, seed)
        plain_letters = list("".join(plain_words))
        rng = random.Random(1000 + seed)
        perm = ALPHA_LIST = list(ALPHA)
        shuffled = perm[:]
        rng.shuffle(shuffled)
        enc_map = {ALPHA[i]: shuffled[i] for i in range(A)}  # plaintext letter -> cipher symbol
        cipher_words = ["".join(enc_map[c] for c in w) for w in plain_words]
        frags = words_to_frags(cipher_words)
        res = anneal(frags, model, restarts=15, iters=1500, seed=seed, fixed=None, max_homo=1)
        dec_words = res["reading"]
        dec_letters = list("".join(dec_words))
        correct = sum(1 for x, y in zip(dec_letters, plain_letters) if x == y)
        pct = 100.0 * correct / len(plain_letters)
        seed_results.append({
            "seed": seed, "plain_words": plain_words, "cipher_words": cipher_words,
            "decoded_words": dec_words, "score_per_token": res["score_per_token"],
            "letters_correct": correct, "letters_total": len(plain_letters), "pct_correct": round(pct, 1),
        })
    out = {"n_letters": NLETTERS, "word_lengths": LENS, "seeds": seed_results,
           "pct_correct_by_seed": [r["pct_correct"] for r in seed_results]}
    (OUT / "test1_control.json").write_text(json.dumps(out, indent=1))
    return out


if __name__ == "__main__":
    main_out = run_main_test()
    print("MAIN best combo:", main_out["best_combo"]["fixed"],
          "score_per_token=", main_out["best_combo"]["score_per_token"])
    print("MAIN reading:", " ".join(main_out["best_combo"]["reading_words"]))
    ctrl_out = run_control()
    print("CONTROL pct_correct by seed:", ctrl_out["pct_correct_by_seed"])
