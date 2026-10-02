#!/usr/bin/env python3
"""RIK-CRIBS (2 Oct 2026, account-4): R4282's own four clear-Latin phrases dragged along R4282's cipher stream
as cribs with tools/crib_pattern.py (H28), under same-sign-same-letter constraints (homophones allowed: R4284's
key-test leaf shows one letter has several signs), scored by the implied partial key's whole-text la18 unigram
statistic, against (a) the tool's shuffled-order control and (b) a negative crib of the same folded length drawn
from the la18 corpus (Zaluski, tools/data/la18, not on the leaf), run under identical settings.

Reproducible per CLAUDE.md rule 7: regenerates everything from r4282_transcription_bourdeau.txt (Bourdeau,
dbourdeau/cyphersolver, riksarkivet1628/, commit fc0c9e8, CC BY 4.0) and report.json (bRIK's R4284 crib key).
Writes cribs/r4282_codes.tsv, cribs/brik_crib_key_compare.tsv, cribs/clear_cribs_report.json. `--check`
re-derives and diffs against the committed report; exits 1 if stale.

No reading is claimed; letter values from a placement are grade M at most (rule 4). The tool never writes
solved, new or first and neither does this script.
"""
import argparse, collections, csv, json, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE.parent
ROOT = TARGET.parent.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(HERE))
import crib_pattern as cp  # noqa: E402
import homophonic_anneal as ha  # noqa: E402
import judge_plaintext as jp  # noqa: E402
import crib_test  # noqa: E402  (bRIK's parser, for the flat-stream identity check)

OUT = TARGET / "cribs"
CODES = OUT / "r4282_codes.tsv"
COMPARE = OUT / "brik_crib_key_compare.tsv"
REPORT = OUT / "clear_cribs_report.json"

# The four clear-Latin phrases as transcribed on the R4282 leaf (brackets in r4282_transcription_bourdeau.txt);
# "eius?" is Bourdeau's own uncertain reading and is kept (the fold drops the '?').
PHRASES = [
    ("P1", "et qualis sit eius futurus status dubitatur", "p1, line 10, inside the sentence: 'xpEr4m [..] Spr MrAq5bD'"),
    ("P2", "sed tamen ut res", "p1, line 21, inside the sentence: 'rbbl5p8MmLu [..] LkMnl7oa'"),
    ("P3", "tractatus magnas admodum", "p1, line 25, after a stop: 'fDeMrbm4nLx5 . [..] EptMSab?'"),
    ("P4", "Mittatur nobis responsum", "p2, line 1, opens the page: '[..] S? fbm7o E4lMrq5'"),
    # Bourdeau brackets P1 as three pieces, '[et qualis sit] [eius?] [futurus status dubitatur]'; the two
    # unambiguous pieces are run on their own as well, since the 37-letter whole places nowhere at err 0-1.
    ("P1a", "et qualis sit", "p1, line 10, first bracket of P1"),
    ("P1b", "futurus status dubitatur", "p1, line 10, third bracket of P1"),
]
SETTINGS = [("err0", 0), ("err1", 1), ("err2", 2)]
SHUFFLES = 200
SEED = 1


def read_r4282_by_page():
    """Same cleaning as crib_test.read_r4282_signs, but keeps the page each sign sits on."""
    text = (TARGET / "r4282_transcription_bourdeau.txt").read_text(encoding="utf-8")
    rows, page = [], None
    for line in text.splitlines():
        if line.startswith("## "):
            page = line[3:].split()[0]
            continue
        if not line.strip() or line.startswith("#"):
            continue
        line = re.sub(r"\[[^\]]*\]", " ", line)
        for raw in line.split():
            tok = raw.strip("?^")
            if not tok or tok in (":", ".", "-"):
                continue
            tok = tok.rstrip(".").rstrip(":")
            for ch in tok:
                rows.append((page, tok, ch))
    return rows


def write_codes(rows):
    OUT.mkdir(exist_ok=True)
    with open(CODES, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["pos", "page", "token", "code"])
        for i, (page, tok, ch) in enumerate(rows):
            w.writerow([i, page, tok, ch])


def brik_compare():
    """bRIK's R4284 key-test crib key, reversed sign -> majority letter (ties listed, value left '?')."""
    rep = json.loads((TARGET / "report.json").read_text(encoding="utf-8"))
    sym = collections.defaultdict(collections.Counter)
    for letter, signs in rep["crib_letter_to_symbols"].items():
        for s, n in signs.items():
            sym[s][letter] += n
    out, ties = {}, {}
    with open(COMPARE, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["code", "value", "support", "note"])
        for s in sorted(sym):
            mc = sym[s].most_common()
            top = [l for l, n in mc if n == mc[0][1]]
            if len(top) > 1:
                ties[s] = dict(mc)
                w.writerow([s, "?", json.dumps(dict(mc)), "tie: not compared"])
            else:
                out[s] = ha.fold(top[0])
                w.writerow([s, top[0], json.dumps(dict(mc)), ""])
    return out, ties


def corpus_words(path, min_count=20):
    """Corpus words in order, with any word seen fewer than min_count times in the volume dropped (OCR junk such
    as 'refclialcus' or 'inlerere' otherwise lands in a negative crib)."""
    t = jp.read_corpus(str(path)).lower()
    words = re.findall(r"[a-z]{2,}", t)
    cnt = collections.Counter(words)
    return [w for w in words if cnt[w] >= min_count]


def negative_crib(words, length, rng, avoid):
    """A word-boundary-aligned phrase from the corpus whose folded length equals `length`; never a phrase
    sharing a word with the leaf's own clear phrases."""
    cands = []
    for i in range(0, len(words) - 12, 7):
        acc, j = "", i
        while j < len(words) and len(acc) < length:
            acc += ha.fold(words[j]); j += 1
        if len(acc) == length and not (set(words[i:j]) & avoid):
            cands.append(" ".join(words[i:j]))
        if len(cands) >= 400:
            break
    return rng.choice(cands)


def synthetic(words, phrase, N, K, rng):
    """A design-matched positive control (rule 3): la18 prose of N signs with the folded phrase embedded once,
    enciphered by a homophonic letter -> sign key of K signs (every letter one sign, the K-24 extra signs given to
    the most frequent letters as second/third homophones, chosen uniformly per occurrence -- the shape R4284's
    key-test leaf shows: e has three signs, s four, t one). Returns (groups, true_start, true_key sign->letter)."""
    crib = ha.fold(phrase)
    text = ha.fold(" ".join(words))
    s0 = rng.randrange(1000, len(text) - N)
    body = text[s0:s0 + N - len(crib)]
    pos = rng.randrange(0, len(body))
    plain = body[:pos] + crib + body[pos:]
    freq = [a for a, _ in collections.Counter(text[:200000]).most_common()]
    letters = list(ha.ALPHA)
    signs = [f"s{i}" for i in range(K)]
    rng.shuffle(signs)
    key = {a: [signs[i]] for i, a in enumerate(letters)}
    for j, sgn in enumerate(signs[len(letters):]):
        key[freq[j % len(freq)]].append(sgn)
    seq = [rng.choice(key[a]) for a in plain]
    true_key = {sg: a for a, sgs in key.items() for sg in sgs}
    return [seq], pos, true_key


def positive_control(words, phrase, N, K, uni, max_err, seed):
    rng = random.Random(seed)
    groups, pos, true_key = synthetic(words, phrase, N, K, rng)
    crib = ha.fold(phrase)
    real, starts = cp.run(groups, crib, set(), set(), 0, True, uni, max_err)
    rank = next((i + 1 for i, r in enumerate(real) if r[1] == pos), None)
    top_right = (sum(1 for c, l in real[0][3].items() if true_key.get(c) == l), len(real[0][3])) if real else None
    rng2 = random.Random(seed)
    counts, bests = [], []
    for _ in range(100):
        sh, _ = cp.run(cp.shuffle_groups(groups, rng2), crib, set(), set(), 0, True, uni, max_err)
        counts.append(len(sh)); bests.append(sh[0][0] if sh else None)
    fb = [b for b in bests if b is not None]
    rb = real[0][0] if real else None
    return {"kind": "positive-control", "crib": phrase, "max_err": max_err, "N": N, "K": K, "true_start": pos,
            "real_placements": len(real), "true_placement_found": rank is not None, "true_placement_rank": rank,
            "top_key_right": top_right, "real_best_score": round(rb, 4) if rb is not None else None,
            "control_placements": {"mean": round(sum(counts) / len(counts), 2), "p95": cp.pct(counts, .95), "max": max(counts)},
            "control_best_score": {"mean": round(sum(fb) / len(fb), 4) if fb else None, "p95": round(cp.pct(fb, .95), 4) if fb else None,
                                   "n_with_placement": len(fb)},
            "rank_placements_at_or_above": sum(1 for c in counts if c >= len(real)),
            "rank_best_at_or_above": (sum(1 for b in fb if b >= rb) if rb is not None else None), "shuffles": 100}


def one_run(groups, crib_text, uni, max_err, cmp, rng_seed):
    crib = ha.fold(crib_text)
    N = sum(len(g) for g in groups)
    real, real_starts = cp.run(groups, crib, set(), set(), 0, True, uni, max_err)
    rng = random.Random(rng_seed)
    counts, starts, bests = [], [], []
    for _ in range(SHUFFLES):
        sh, st = cp.run(cp.shuffle_groups(groups, rng), crib, set(), set(), 0, True, uni, max_err)
        counts.append(len(sh)); starts.append(st); bests.append(sh[0][0] if sh else None)
    fb = [b for b in bests if b is not None]
    top = []
    for sc, s, sk, m, cov, e in real[:5]:
        agree = {c: l for c, l in m.items() if cmp.get(c) == l}
        conflict = {c: f"{l}!={cmp[c]}" for c, l in m.items() if c in cmp and cmp[c] != l}
        top.append({"start": s, "errs": e, "score": round(sc, 4), "coverage": cov, "key": dict(sorted(m.items())),
                    "agree_with_brik": agree, "conflict_with_brik": conflict, "compared": sum(1 for c in m if c in cmp)})
    rb = real[0][0] if real else None
    # agreement with bRIK's key over EVERY real placement (not only the top): the brief's signal is 3-4 letters
    # agreeing across two independent cribs, wherever that placement ranks
    agree_all = [sum(1 for c, l in m.items() if cmp.get(c) == l) for _, _, _, m, _, _ in real]
    agree_hist = dict(sorted(collections.Counter(agree_all).items()))
    return {
        "agree_with_brik_max_any_placement": max(agree_all) if agree_all else None,
        "agree_with_brik_histogram": agree_hist,
        "crib": crib_text, "folded": crib, "length": len(crib), "max_err": max_err, "N": N,
        "real_placements": len(real), "real_distinct_starts": real_starts,
        "real_best_score": round(rb, 4) if rb is not None else None,
        "control_placements": {"mean": round(sum(counts) / len(counts), 2), "p95": cp.pct(counts, .95), "max": max(counts)},
        "control_starts": {"mean": round(sum(starts) / len(starts), 2), "p95": cp.pct(starts, .95), "max": max(starts)},
        "control_best_score": {"mean": round(sum(fb) / len(fb), 4) if fb else None, "p95": round(cp.pct(fb, .95), 4) if fb else None,
                               "max": round(max(fb), 4) if fb else None, "n_with_placement": len(fb)},
        "rank_placements_at_or_above": sum(1 for c in counts if c >= len(real)),
        "rank_best_at_or_above": (sum(1 for b in fb if b >= rb) if rb is not None else None),
        "shuffles": SHUFFLES, "top": top,
    }


def derive():
    rows = read_r4282_by_page()
    flat = "".join(ch for _, _, ch in rows)
    _, flat_brik = crib_test.read_r4282_signs()
    assert flat == flat_brik, "page-aware parse differs from crib_test.read_r4282_signs"
    write_codes(rows)
    cmp, ties = brik_compare()
    groups = cp.read_codes(str(CODES), "page")
    paths = [str(p) for p in jp.LANG_CORPORA["la18"]]
    uni = cp.unigram([jp.read_corpus(p) for p in paths])
    words = corpus_words(paths[0])
    avoid = set(w for _, ph, _ in PHRASES for w in re.findall(r"[a-z]+", ph.lower()))
    rng = random.Random(SEED)
    results = []
    for pid, phrase, where in PHRASES:
        neg = negative_crib(words, len(ha.fold(phrase)), rng, avoid)
        for sname, me in SETTINGS:
            results.append({"id": f"{pid}-{sname}", "kind": "target", "where": where,
                            **one_run(groups, phrase, uni, me, cmp, SEED)})
            results.append({"id": f"{pid}-{sname}-neg", "kind": "negative-crib", "where": "la18 tomus I, not on the leaf",
                            **one_run(groups, neg, uni, me, cmp, SEED)})
            if me <= 1:
                results.append({"id": f"{pid}-{sname}-pos", "where": "synthetic la18 letter, N=1094 K=34, phrase embedded",
                                **positive_control(words, phrase, len(rows), len(set(flat)), uni, me, SEED)})
    return {"transcription": "r4282_transcription_bourdeau.txt (Bourdeau, dbourdeau/cyphersolver fc0c9e8, CC BY 4.0)",
            "N": len(rows), "K": len(set(flat)), "groups": [len(g) for g in groups], "corpus": paths,
            "brik_compare_ties": ties, "settings": {"homophones": True, "wild": [], "skip": [], "shuffles": SHUFFLES, "seed": SEED},
            "runs": results}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    rep = derive()
    if a.check:
        old = json.loads(REPORT.read_text(encoding="utf-8"))
        if old != json.loads(json.dumps(rep)):  # round-trip: JSON turns int dict keys into strings
            print("STALE: cribs/clear_cribs_report.json differs from a fresh re-derivation"); sys.exit(1)
        print("OK: cribs/clear_cribs_report.json matches a fresh re-derivation"); return
    REPORT.write_text(json.dumps(rep, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for r in rep["runs"]:
        if r["kind"] == "positive-control":
            print(f"{r['id']:<12} L={len(ha.fold(r['crib'])):2d} err={r['max_err']} POS: {r['real_placements']} pl, true start {r['true_start']} found {r['true_placement_found']} rank {r['true_placement_rank']}, "
                  f"top key right {r['top_key_right']}, best {r['real_best_score']} | ctrl pl mean {r['control_placements']['mean']} p95 {r['control_placements']['p95']}; "
                  f"best mean {r['control_best_score']['mean']} p95 {r['control_best_score']['p95']} ({r['control_best_score']['n_with_placement']}/100 place) | rank pl {r['rank_placements_at_or_above']}/100 best {r['rank_best_at_or_above']}")
            continue
        print(f"{r['id']:<12} L={r['length']:2d} err={r['max_err']} real: {r['real_placements']:5d} pl / {r['real_distinct_starts']:4d} starts, best {r['real_best_score']} | "
              f"ctrl pl mean {r['control_placements']['mean']} p95 {r['control_placements']['p95']} max {r['control_placements']['max']}; "
              f"best mean {r['control_best_score']['mean']} p95 {r['control_best_score']['p95']} max {r['control_best_score']['max']} "
              f"({r['control_best_score']['n_with_placement']}/{SHUFFLES} place) | rank pl {r['rank_placements_at_or_above']}/{SHUFFLES} best {r['rank_best_at_or_above']}")
        if r["top"]:
            t = r["top"][0]
            print(f"             top: start {t['start']} errs {t['errs']} agree {len(t['agree_with_brik'])}/{t['compared']} conflict {t['conflict_with_brik']} key {t['key']}")


if __name__ == "__main__":
    main()
