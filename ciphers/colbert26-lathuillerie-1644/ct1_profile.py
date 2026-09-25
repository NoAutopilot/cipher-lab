#!/usr/bin/env python3
"""KX-LATHCT1, 25 Sept 2026 -- breadth-lane cheap test 1 for specs/colbert26-lathuillerie-1644.json.

Question: is the La Thuillerie cipher (canvases 20+21+27, and separately canvas 30) the same key
family as a key we already hold (clair1067 key_1646.tsv, key_brienne_1647.tsv; fr5160 key_1659.tsv),
and are canvas 20+21+27 and canvas 30 one alphabet or two?

Method: sign-class profile (digit-width / letter / marked / mixed / symbol), distinct-signs-per-100,
repeat rate, index of coincidence on the sign stream, and Jaccard overlap of code inventories --
each judged against a matched synthetic control (rule 3): a mixed nomenclator of the SAME K and
class shares, code->French-letter assignment randomised, French plaintext from tools/data/fr16
run through it. No network. Deterministic (SEED fixed). Re-run: python3 ct1_profile.py

Data sources for the four corpora compared:
  A  = ciphers/colbert26-lathuillerie-1644/ciphertext.tsv canvases 20+21+27, tokens agreed by both
       passes (ciphertext.tsv vs passB.tsv, via disagreements.tsv)
  B  = same file, canvas 30, agreed tokens
  K1646 = ciphers/clair1067-brienne-poland-1646/ciphertext.txt (key_1646.tsv's own attested letter,
          19 May 1646, our own transcription -- a real running ciphertext)
  K1647 = ciphers/clair1067-brienne-poland-1646/key_brienne_1647.tsv -- Tomokiyo's PUBLISHED table
          for a different correspondent (D'Estrades, 1647); we hold no ciphertext of our own actually
          enciphered under it, only the code inventory, so N/IC/repeat-rate do not apply to it (noted,
          not silently skipped -- rule 8).
  K1659 = ciphers/fr5160-letellier-1653/ciphertext_f67.tsv, cipher-only tokens (10 Oct 1659 letter,
          key_1659.tsv reads it at 92.3% coverage per that folder's NOTES.md -- a real running
          ciphertext under that key), punctuation tokens (",", ";", ".", ":", "—", "X") excluded
          per that folder's decode_f67.json "nonsign" list.
"""
import json
import random
import string
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

SEED = 20260925
N_CONTROL = 200
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

MARKS = "'+°\"_"


def classify(tok):
    if tok.isdigit():
        return "d1" if len(tok) == 1 else ("d2" if len(tok) == 2 else "d3p")
    if any(ch in MARKS for ch in tok):
        return "mark"
    if tok.isalpha():
        return "l1" if len(tok) == 1 else "l2p"
    if any(ch.isdigit() for ch in tok) and any(ch.isalpha() for ch in tok):
        return "mixed"
    return "sym"


def profile(tokens):
    n = len(tokens)
    token_classes = Counter(classify(t) for t in tokens)  # occurrence shares, for the text profile
    shares = {c: token_classes.get(c, 0) / n for c in ["d1", "d2", "d3p", "l1", "l2p", "mark", "mixed", "sym"]}
    distinct_codes = set(tokens)
    distinct = len(distinct_codes)
    # code_class_counts: DISTINCT codes per class (the nomenclator table size K per class) -- this,
    # not token-occurrence counts, is what a matched-K synthetic control must reproduce.
    code_class_counts = Counter(classify(c) for c in distinct_codes)
    counts = Counter(tokens)
    ic = sum(c * (c - 1) for c in counts.values()) / (n * (n - 1)) if n > 1 else float("nan")
    return {
        "n": n,
        "distinct": distinct,
        "distinct_per_100": 100.0 * distinct / n,
        "repeat_rate": 1.0 - distinct / n,
        "ic": ic,
        "class_shares": shares,
        "class_counts": dict(code_class_counts),
        "codes": distinct_codes,
    }


def jaccard(a, b):
    a, b = set(a), set(b)
    u = a | b
    return len(a & b) / len(u) if u else float("nan")


# ---------------------------------------------------------------------------
# Loading the two real corpora under test (colbert26 canvases, agreed tokens)
# ---------------------------------------------------------------------------

def load_ciphertext_tsv(path):
    rows = defaultdict(list)  # canvas -> [token,...] in file order
    with open(path, encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        ci, ti = header.index("canvas"), header.index("token")
        for line in f:
            if not line.strip():
                continue
            cols = line.rstrip("\n").split("\t")
            rows[cols[ci]].append(cols[ti])
    return rows


def load_drop_positions(path):
    """canvas -> set of a_pos (1-based) that are NOT agreed (excludes 'settled from crop' rows,
    whose current ciphertext.tsv value already reflects the corrected, agreeing reading)."""
    drop = defaultdict(set)
    with open(path, encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        ci, api, ki, ni = (header.index(x) for x in ["canvas", "a_pos", "kind", "note"])
        for line in f:
            if not line.strip():
                continue
            cols = line.rstrip("\n").split("\t")
            canvas, a_pos, kind, note = cols[ci], cols[api], cols[ki], cols[ni]
            if kind.startswith("B-only"):
                continue  # not an A position at all
            if a_pos == "":
                continue
            if note.startswith("settled from crop"):
                continue  # ciphertext.tsv already corrected to the agreeing value
            drop[canvas].add(int(a_pos))
    return drop


def agreed_tokens(all_tokens, drop_positions, canvases):
    used, dropped = [], 0
    for canvas in canvases:
        toks = all_tokens[canvas]
        drops = drop_positions.get(canvas, set())
        for pos, tok in enumerate(toks, start=1):
            if pos in drops:
                dropped += 1
            else:
                used.append(tok)
    return used, dropped


# ---------------------------------------------------------------------------
# Held-key corpora
# ---------------------------------------------------------------------------

def load_k1646():
    toks = []
    with open(REPO / "ciphers/clair1067-brienne-poland-1646/ciphertext.txt", encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        ti = header.index("token")
        for line in f:
            if not line.strip():
                continue
            toks.append(line.rstrip("\n").split("\t")[ti])
    return toks


def load_k1659():
    nonsign = {",", ";", ".", ":", "—", "X"}
    toks = []
    with open(REPO / "ciphers/fr5160-letellier-1653/ciphertext_f67.tsv", encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        gi = header.index("group")
        for line in f:
            if not line.strip():
                continue
            g = line.rstrip("\n").split("\t")[gi]
            if g.startswith("[") or g in nonsign or g == "":
                continue
            toks.append(g)
    return toks


def load_k1647_codes():
    codes = []
    with open(REPO / "ciphers/clair1067-brienne-poland-1646/key_brienne_1647.tsv", encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        ci = header.index("code")
        for line in f:
            if not line.strip():
                continue
            codes.append(line.rstrip("\n").split("\t")[ci])
    return codes


# ---------------------------------------------------------------------------
# French plaintext letter stream (for the matched control)
# ---------------------------------------------------------------------------

def load_french_letters():
    import gzip
    p = REPO / "tools/data/fr16/lettresindites00marg_djvu.txt.gz"
    text = gzip.open(p, "rt", encoding="utf-8", errors="ignore").read()
    letters = []
    for ch in text:
        ch2 = unicodedata.normalize("NFKD", ch)
        base = "".join(c for c in ch2 if not unicodedata.combining(c))
        if base.isalpha() and base.isascii():
            letters.append(base.upper())
    return letters


LETTERS26 = list(string.ascii_uppercase)


def french_letter_freq(stream):
    c = Counter(stream)
    total = sum(c.values())
    return {L: c.get(L, 0) / total for L in LETTERS26}


# ---------------------------------------------------------------------------
# Matched synthetic nomenclator: same class shares (K per class), French plaintext through it
# ---------------------------------------------------------------------------

POOLS = {
    "d1": [str(i) for i in range(10)],
    "d2": [str(i) for i in range(10, 100)],
    "d3p": [str(i) for i in range(100, 400)],
    "l1": list(string.ascii_lowercase) + list(string.ascii_uppercase),
    "l2p": [a + b for a in string.ascii_lowercase for b in string.ascii_lowercase],
    "mark": [c + m for c in (string.ascii_lowercase + string.ascii_uppercase + "".join(str(i) for i in range(10)))
             for m in MARKS],
    "mixed": [a + d for a in string.ascii_lowercase for d in "0123456789"] +
             [d + a for a in string.ascii_lowercase for d in "0123456789"],
    "sym": list("&%§#@~^†‡"),
}


def sample_codes(class_counts, rng):
    codes = []
    for cls, k in class_counts.items():
        if k <= 0:
            continue
        pool = POOLS[cls]
        codes += rng.sample(pool, min(k, len(pool)))
    return codes


def build_key(codes, letter_freq, rng):
    letters = LETTERS26
    weights = [letter_freq.get(L, 0.0001) for L in letters]
    code_to_letter = {}
    letter_to_codes = defaultdict(list)
    shuffled = codes[:]
    rng.shuffle(shuffled)
    idx = 0
    for L in letters:
        if idx >= len(shuffled):
            break
        code_to_letter[shuffled[idx]] = L
        letter_to_codes[L].append(shuffled[idx])
        idx += 1
    for c in shuffled[idx:]:
        L = rng.choices(letters, weights=weights, k=1)[0]
        code_to_letter[c] = L
        letter_to_codes[L].append(c)
    return letter_to_codes


def encipher(letter_stream, offset, n, letter_to_codes, rng):
    out = []
    i = offset
    L = len(letter_stream)
    tries = 0
    while len(out) < n and tries < n * 50:
        ch = letter_stream[i % L]
        i += 1
        tries += 1
        opts = letter_to_codes.get(ch)
        if opts:
            out.append(rng.choice(opts))
    return out


def synth_profile_control(class_counts, n, letter_stream, letter_freq, rng, reps=N_CONTROL):
    ics, distincts, repeats = [], [], []
    for r in range(reps):
        codes = sample_codes(class_counts, rng)
        key = build_key(codes, letter_freq, rng)
        offset = rng.randrange(len(letter_stream))
        text = encipher(letter_stream, offset, n, key, rng)
        p = profile(text)
        ics.append(p["ic"])
        distincts.append(p["distinct_per_100"])
        repeats.append(p["repeat_rate"])
    return {"ic": ics, "distinct_per_100": distincts, "repeat_rate": repeats}


def percentile_of(value, sample):
    sample = sorted(sample)
    if not sample:
        return float("nan")
    below = sum(1 for x in sample if x <= value)
    return 100.0 * below / len(sample)


def pair_jaccard_controls(class_counts_x, class_counts_y, n_x, n_y, letter_stream, letter_freq, rng,
                           reps=N_CONTROL):
    diff_key = []
    for r in range(reps):
        cx = sample_codes(class_counts_x, rng)
        cy = sample_codes(class_counts_y, rng)
        diff_key.append(jaccard(cx, cy))
    same_key = []
    merged = {c: max(class_counts_x.get(c, 0), class_counts_y.get(c, 0)) for c in POOLS}
    for r in range(reps):
        codes = sample_codes(merged, rng)
        key = build_key(codes, letter_freq, rng)
        off1 = rng.randrange(len(letter_stream))
        off2 = rng.randrange(len(letter_stream))
        t1 = encipher(letter_stream, off1, n_x, key, rng)
        t2 = encipher(letter_stream, off2, n_y, key, rng)
        same_key.append(jaccard(t1, t2))
    return diff_key, same_key


def summarize(vals):
    vals = sorted(v for v in vals if v == v)  # drop nan
    if not vals:
        return "n/a"
    mean = sum(vals) / len(vals)
    return f"mean {mean:.3f} range[{vals[0]:.3f},{vals[-1]:.3f}]"


def main():
    rng = random.Random(SEED)

    all_tokens = load_ciphertext_tsv(HERE / "ciphertext.tsv")
    drops = load_drop_positions(HERE / "disagreements.tsv")

    a_tok, a_dropped = agreed_tokens(all_tokens, drops, ["20", "21", "27"])
    b_tok, b_dropped = agreed_tokens(all_tokens, drops, ["30"])
    a_total = sum(len(all_tokens[c]) for c in ["20", "21", "27"])
    b_total = len(all_tokens["30"])

    k1646_tok = load_k1646()
    k1659_tok = load_k1659()
    k1647_codes = load_k1647_codes()

    letter_stream = load_french_letters()
    letter_freq = french_letter_freq(letter_stream)

    corpora = {
        "A_canvas20+21+27": profile(a_tok),
        "B_canvas30": profile(b_tok),
        "K1646_ciphertext.txt": profile(k1646_tok),
        "K1659_ciphertext_f67": profile(k1659_tok),
    }
    # K1647 has no attested running text -- inventory only, IC/repeat/N n/a
    k1647_profile = {
        "n": None, "distinct": len(set(k1647_codes)), "distinct_per_100": None,
        "repeat_rate": None, "ic": None,
        "class_shares": None, "class_counts": Counter(classify(c) for c in k1647_codes),
        "codes": set(k1647_codes),
    }

    results = []
    results.append(f"# ct1_profile.py -- SEED={SEED}, N_CONTROL={N_CONTROL}")
    results.append(f"tokens_used\tA(20+21+27)\t{len(a_tok)}\tdropped\t{a_dropped}\tof\t{a_total}")
    results.append(f"tokens_used\tB(30)\t{len(b_tok)}\tdropped\t{b_dropped}\tof\t{b_total}")
    results.append("")
    results.append("## Per-corpus profile (real) + matched-control percentile (200 synthetic mixed-nomenclator texts, same N/class-shares, French plaintext from tools/data/fr16)")
    results.append("corpus\tN\tdistinct\tdistinct_per_100\trepeat_rate\tic\tclass_shares")

    ctrl_lines = []
    for name, p in corpora.items():
        shares_str = ",".join(f"{k}={v:.3f}" for k, v in p["class_shares"].items() if v > 0)
        results.append(f"{name}\t{p['n']}\t{p['distinct']}\t{p['distinct_per_100']:.2f}\t{p['repeat_rate']:.3f}\t{p['ic']:.4f}\t{shares_str}")
        ctrl = synth_profile_control(p["class_counts"], p["n"], letter_stream, letter_freq, rng)
        pct_ic = percentile_of(p["ic"], ctrl["ic"])
        pct_dp = percentile_of(p["distinct_per_100"], ctrl["distinct_per_100"])
        pct_rr = percentile_of(p["repeat_rate"], ctrl["repeat_rate"])
        ctrl_lines.append(
            f"{name}\tcontrol_ic\t{summarize(ctrl['ic'])}\tobserved_pctile\t{pct_ic:.1f}\t"
            f"control_distinct_per_100\t{summarize(ctrl['distinct_per_100'])}\tobserved_pctile\t{pct_dp:.1f}\t"
            f"control_repeat_rate\t{summarize(ctrl['repeat_rate'])}\tobserved_pctile\t{pct_rr:.1f}"
        )
    results.append("")
    results.append("K1647_key_brienne_1647.tsv\tn/a (key TABLE only, no attested running text of ours under it)\t"
                    f"distinct={k1647_profile['distinct']}\tclass_counts={dict(k1647_profile['class_counts'])}")
    results.append("")
    results.append("## Per-corpus control lines")
    results.extend(ctrl_lines)

    # Pairwise Jaccard + same-key/different-key calibration
    results.append("")
    results.append("## Pairwise code-inventory Jaccard (observed) + calibration (200 reps each)")
    pairs = [
        ("A_canvas20+21+27", corpora["A_canvas20+21+27"], "B_canvas30", corpora["B_canvas30"]),
        ("A_canvas20+21+27", corpora["A_canvas20+21+27"], "K1646", corpora["K1646_ciphertext.txt"]),
        ("A_canvas20+21+27", corpora["A_canvas20+21+27"], "K1647", k1647_profile),
        ("A_canvas20+21+27", corpora["A_canvas20+21+27"], "K1659", corpora["K1659_ciphertext_f67"]),
        ("B_canvas30", corpora["B_canvas30"], "K1646", corpora["K1646_ciphertext.txt"]),
        ("B_canvas30", corpora["B_canvas30"], "K1647", k1647_profile),
        ("B_canvas30", corpora["B_canvas30"], "K1659", corpora["K1659_ciphertext_f67"]),
    ]
    for xname, xp, yname, yp in pairs:
        obs = jaccard(xp["codes"], yp["codes"])
        n_x = xp["n"]
        n_y = yp["n"] if yp["n"] is not None else n_x  # K1647 has no N; use x's N for the "same key" text-length sim
        diff_key, same_key = pair_jaccard_controls(xp["class_counts"], yp["class_counts"], n_x, n_y,
                                                     letter_stream, letter_freq, rng)
        pct = percentile_of(obs, diff_key)
        results.append(
            f"{xname}\tvs\t{yname}\tobserved_jaccard\t{obs:.3f}\t"
            f"diff_key_control\t{summarize(diff_key)}\tobserved_pctile_in_diff_key\t{pct:.1f}\t"
            f"same_key_control\t{summarize(same_key)}"
        )

    out = HERE / "ct1_results.tsv"
    out.write_text("\n".join(results) + "\n", encoding="utf-8")
    print("\n".join(results))


if __name__ == "__main__":
    main()
