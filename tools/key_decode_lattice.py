#!/usr/bin/env python3
"""Key-constrained decoding over a per-sign candidate lattice (TRANSCRIPTION.md pipeline step 6, TX-DECODE, 3 Oct 2026).

Given, for every sign position, top-k reader candidates with scores, a key (tools/decode_key.py key.tsv format: columns
sign, value; value NULL = null) and a letter n-gram language model (tools/judge_plaintext.py corpora), choose the most
probable sign sequence by beam Viterbi over the lattice:

    objective = sum over letters of (log10 P_lm(letter | 3 previous) + bonus)  +  lam * sum over signs of log10 prior(sign)

`bonus` is minus the corpus's own mean per-letter log10 probability (so a typical letter of real prose costs ~0 and a
value of several letters is not penalised for its length); a candidate whose sign is not in the key (X_*, '?') costs
`unk_cost` and leaves the n-gram state unchanged. Every position where the chosen sign differs from the top-1 reader
candidate is listed: such a choice rests on the key and the language model, so it is graded S at best, never H.

Built-in controls (CLAUDE.md rule 3):
  * shuffled keys: the same lattice decode under N value-shuffled keys (the value column permuted over the key's signs);
    the real key must beat them by rank/z on the decoded text's mean 4-gram score, else the gain is the language model
    inventing text. The top-1 (no-lattice) decode's rank/z is reported beside it.
  * known answer (--truth): err before (top-1 decode) and after (lattice decode) against a per-position true value.
  * power (--power-err E): synthetic windows of corpus prose of the target's length, enciphered with the real key
    (homophones drawn at random), read by two simulated readers each wrong with probability E (substitutes drawn from the
    confusion table, else any key sign), turned into a lattice by the same `from-passes` rule; power = share of windows
    where the real key ranks 1 among the shuffles.

Subcommands
  from-passes  passA.tsv passB.tsv [--ref ciphertext.tsv] [--confusion confusion.tsv] --out topk.tsv
               Synthesizes a top-k TSV (line, pos, cand, score) from two blind line passes (columns passage, pos, sign_id,
               alt, conf). Pre-registered rule (fixed before any known-answer run): reader weight H 1.0 / M 0.6 / L 0.3
               (blank 0.6); a reader's alt gets 0.3 x weight; each read sign spreads 0.15 x weight over its top-3 confusion
               neighbours in proportion to their pair counts; normalise; drop < 0.02; keep top 4. With --ref (a committed
               ciphertext TSV: line, pos, sign), each pass line is aligned to the ref line by difflib and the ref's
               positions are the lattice skeleton (the ref's own signs are NOT used as candidates); without it, pass A is
               the skeleton and B is aligned onto it.
               --keep-alts (TX-ALTS, 4 Oct 2026): a sign_id written `a/b?` (DECRYPT convention) is first choice a with
               alternative b at the alt weight, and every reader-written alternative stays in the lattice (exempt from
               the 0.02 floor and the top-4 cut). Without it, a/b? is still parsed but alternatives may be cut.
  decode       topk.tsv --key key.tsv (--lang L | --corpus F...) [--truth truth.tsv] [--shuffles N] [--power-err E]
               [--out-prefix P] writes P.decode.tsv (line pos top1 chosen value prior changed), P.plain.txt, P.json.

Usage (Birago no.87 known-answer, from ciphers/nevers-birago-fr3251-1572/harvest):
  python3 tools/key_decode_lattice.py from-passes f178v/passA.tsv f178v/passB.tsv --ref ciphertext_f178v.tsv \\
      --confusion confusion_1572.tsv --out /tmp/f178v_topk.tsv
  python3 tools/key_decode_lattice.py decode /tmp/f178v_topk.tsv --key key_1572_sheet.tsv --lang it16dip --shuffles 200
Offline test: tools/tests/test_key_decode_lattice.py. No network.
"""
import argparse, csv, difflib, json, math, random, statistics, sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus, fold  # noqa: E402

CONF_W = {"H": 1.0, "M": 0.6, "L": 0.3, "": 0.6}
ALT_F, CONF_F, MIN_P, TOPK = 0.3, 0.15, 0.02, 4
UNK = {"", "?"}


# ---------------------------------------------------------------- inputs
def read_tsv(p):
    return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))


def read_key(p):
    key = {}
    for r in read_tsv(p):
        s, v = (r.get("sign") or "").strip(), (r.get("value") or "").strip()
        if not s:
            continue
        key[s] = "" if v.upper() == "NULL" else fold(v)
    return key


def read_confusion(p):
    nb = defaultdict(dict)
    if not p:
        return nb
    for r in read_tsv(p):
        a, b, n = r["label_a"], r["label_b"], float(r.get("n") or 1)
        nb[a][b] = nb[a].get(b, 0) + n
        nb[b][a] = nb[b].get(a, 0) + n
    return nb


def read_pass(p):
    by = defaultdict(list)
    for r in read_tsv(p):
        by[r["passage"]].append(r)
    for k in by:
        by[k].sort(key=lambda r: int(r["pos"]))
    return by


def read_topk(p):
    lat = defaultdict(dict); order = []
    for r in read_tsv(p):
        k = (r["line"], int(r["pos"]))
        if k not in lat:
            order.append(k)
        lat[k][r["cand"]] = float(r["score"])
    return [(k, lat[k]) for k in order]


# ---------------------------------------------------------------- lattice synthesis
def split_cands(row):
    """(first sign, [alternatives], conf) from one pass row. TX-ALTS (4 Oct 2026): a sign_id written in the DECRYPT
    convention (Megyesi 2020) `a/b?` or `a/b/c?` is read as first choice `a` with alternatives `b`, `c`; the `alt`
    column may also hold several cells separated by '/'. A trailing '?' caps conf H at M (as reconcile_passes REC-CONF).
    A plain sign_id with no '/' parses exactly as before."""
    raw = (row.get("sign_id") or "").strip()
    conf = (row.get("conf") or "").strip()
    if raw.endswith("?") and len(raw) > 1:
        raw = raw[:-1]
        if conf == "H":
            conf = "M"
    parts = [x.strip() for x in raw.split("/")] if "/" in raw else [raw]
    first = parts[0] or "?"
    alts = [x for x in parts[1:] if x]
    alts += [x.strip() for x in (row.get("alt") or "").split("/") if x.strip()]
    alts = [x for x in dict.fromkeys(alts) if x != first]
    return first, alts, conf


def reader_mass(row, nb, alts_out=None):
    out = defaultdict(float)
    s, alts, conf = split_cands(row)
    w = CONF_W.get(conf, 0.6)
    out[s] += w
    for alt in alts:
        out[alt] += ALT_F * w
        if alts_out is not None:
            alts_out.add(alt)
    near = sorted(nb.get(s, {}).items(), key=lambda kv: -kv[1])[:3]
    tot = sum(n for _, n in near)
    for b, n in near:
        out[b] += CONF_F * w * n / tot
    return out


def finish(mass, keep=()):
    """normalise; drop < MIN_P; keep top TOPK. Candidates in `keep` (reader-written alternatives under --keep-alts)
    are exempt from the floor and the cut."""
    t = sum(mass.values())
    if t <= 0:
        return {"?": 1.0}
    c = {k: v / t for k, v in mass.items() if v / t >= MIN_P}
    c = dict(sorted(c.items(), key=lambda kv: -kv[1])[:TOPK])
    for k in keep:
        if k in mass and mass[k] > 0:
            c[k] = mass[k] / t
    t = sum(c.values())
    return {k: v / t for k, v in sorted(c.items(), key=lambda kv: -kv[1])}


def align(skel, other):
    """map index in `other` -> index in `skel` via difflib (equal blocks 1:1, replace blocks positional)."""
    m = {}
    sm = difflib.SequenceMatcher(a=skel, b=other, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("equal", "replace"):
            for d in range(min(i2 - i1, j2 - j1)):
                m[j1 + d] = i1 + d
    return m


def ref_lines(p):
    by = defaultdict(list); order = []
    for r in read_tsv(p):
        ln = r["line"]
        if ln not in by:
            order.append(ln)
        by[ln].append(r["sign"])
    return order, by


def short(line):
    return line.split("_")[-1]


def from_passes(pa, pb, ref, nb, keep_alts=False):
    A, B = read_pass(pa), read_pass(pb)
    rows = []
    if ref:
        order, R = ref_lines(ref)
        skel_of = {ln: R[ln] for ln in order}
        key_of = {ln: short(ln) for ln in order}
    else:
        order = list(A)  # pass A file order
        skel_of = {ln: [split_cands(r)[0] for r in A[ln]] for ln in order}
        key_of = {ln: ln for ln in order}
    stats = {"positions": 0, "no_reader": 0, "one_reader": 0}
    for ln in order:
        skel = skel_of[ln]; mass = [defaultdict(float) for _ in skel]; seen = [0] * len(skel)
        keep = [set() for _ in skel]
        for P in (A, B):
            prow = P.get(key_of[ln], [])
            m = align(skel, [split_cands(r)[0] for r in prow])
            for j, r in enumerate(prow):
                if j in m:
                    for k, v in reader_mass(r, nb, keep[m[j]] if keep_alts else None).items():
                        mass[m[j]][k] += v
                    seen[m[j]] += 1
        for i, ms in enumerate(mass):
            stats["positions"] += 1
            if seen[i] == 0:
                stats["no_reader"] += 1
            elif seen[i] == 1:
                stats["one_reader"] += 1
            if keep[i]:
                stats["alt_positions"] = stats.get("alt_positions", 0) + 1
            for c, p in finish(ms, keep[i]).items():
                rows.append((ln, i + 1, c, p))
    return rows, stats


def write_topk(rows, out):
    with open(out, "w", encoding="utf-8") as f:
        f.write("line\tpos\tcand\tscore\n")
        for ln, pos, c, p in rows:
            f.write(f"{ln}\t{pos}\t{c}\t{p:.4f}\n")


# ---------------------------------------------------------------- language model + decoding
class LM:
    def __init__(self, model, unk_cost=None):
        self.m = model; self.n = model.n
        self.k = model.k
        self.lp_cache = {}
        real, _, _ = model.controls(400, samples=60, seed=7)
        self.mean = statistics.mean(real)
        self.bonus = -self.mean
        self.unk_cost = unk_cost if unk_cost is not None else -0.5

    def lp(self, ctx, ch):
        g = ctx + ch
        v = self.lp_cache.get(g)
        if v is None:
            if len(ctx) < self.n - 1:
                v = self.mean
            else:
                v = math.log10((self.m.c.get(g, 0) + self.k) / (self.m.ctx.get(ctx, 0) + 26 * self.k))
            self.lp_cache[g] = v
        return v

    def extend(self, state, val):
        s = 0.0
        for ch in val:
            s += self.lp(state, ch) + self.bonus
            state = (state + ch)[-(self.n - 1):]
        return state, s


def viterbi(lat, key, lm, lam=1.0, beam=64):
    """lat: list of (pos_key, {cand: prior}). Returns list of chosen cands."""
    beams = {"": (0.0, None)}  # state -> (score, backpointer node)
    for _, cands in lat:
        nxt = {}
        for st, (sc, bp) in beams.items():
            for c, p in cands.items():
                pr = lam * math.log10(max(p, 1e-6))
                if c in key:
                    st2, s = lm.extend(st, key[c])
                else:
                    st2, s = st, lm.unk_cost
                tot = sc + pr + s
                o = nxt.get(st2)
                if o is None or tot > o[0]:
                    nxt[st2] = (tot, (c, bp))
        if len(nxt) > beam:
            nxt = dict(sorted(nxt.items(), key=lambda kv: -kv[1][0])[:beam])
        beams = nxt
    best = max(beams.values(), key=lambda v: v[0])
    out = []; node = best[1]
    while node is not None:
        out.append(node[0]); node = node[1]
    return out[::-1], best[0]


def top1(lat):
    return [max(c.items(), key=lambda kv: kv[1])[0] for _, c in lat]


def text_of(seq, key):
    return "".join(key.get(c, "") for c in seq)


def shuffled(key, rnd):
    signs = sorted(key); vals = [key[s] for s in signs]; rnd.shuffle(vals)
    return dict(zip(signs, vals))


def rank_z(real, others):
    r = 1 + sum(1 for o in others if o >= real)
    mu = statistics.mean(others); sd = statistics.pstdev(others) or 1e-9
    return r, (real - mu) / sd, mu, max(others)


def control(lat, key, lm, model, n, seed, lam, beam):
    rnd = random.Random(seed)
    real_l = model.score(text_of(viterbi(lat, key, lm, lam, beam)[0], key))
    real_t = model.score(text_of(top1(lat), key))
    sh_l, sh_t = [], []
    for _ in range(n):
        k2 = shuffled(key, rnd)
        sh_l.append(model.score(text_of(viterbi(lat, k2, lm, lam, beam)[0], k2)))
        sh_t.append(model.score(text_of(top1(lat), k2)))
    rl = rank_z(real_l, sh_l); rt = rank_z(real_t, sh_t)
    return {"lattice": {"real": real_l, "rank": rl[0], "z": rl[1], "shuf_mean": rl[2], "shuf_max": rl[3]},
            "top1": {"real": real_t, "rank": rt[0], "z": rt[1], "shuf_mean": rt[2], "shuf_max": rt[3]},
            "n_shuffles": n}


def power(lat_len, key, lm, model, nb, err, windows, n_shuf, seed, lam, beam):
    """synthetic windows of corpus prose enciphered with the real key, two readers wrong with prob err each."""
    rnd = random.Random(seed)
    inv = defaultdict(list)
    for s, v in key.items():
        if len(v) == 1:
            inv[v].append(s)
    signs = sorted(key)
    res = []
    for w in range(windows):
        seq = []
        while len(seq) < lat_len:
            j = rnd.randrange(0, len(model.raw) - 4 * lat_len)
            for ch in model.raw[j:j + 4 * lat_len]:
                ch = {"v": "u", "j": "i", "k": "c", "w": "u", "y": "i"}.get(ch, ch) if ch not in inv else ch
                if ch in inv:
                    seq.append(rnd.choice(inv[ch]))
                if len(seq) >= lat_len:
                    break
        lat = []
        for i, s in enumerate(seq):
            mass = defaultdict(float)
            for _r in range(2):
                read = s
                if rnd.random() < err:
                    near = list(nb.get(s, {}).items())
                    if near and rnd.random() < 0.8:
                        tot = sum(n for _, n in near); x = rnd.random() * tot
                        for b, n in near:
                            x -= n
                            if x <= 0:
                                read = b; break
                    else:
                        read = rnd.choice(signs)
                for k, v in reader_mass({"sign_id": read, "conf": "M"}, nb).items():
                    mass[k] += v
            lat.append((("syn", i), finish(mass)))
        c = control(lat, key, lm, model, n_shuf, seed + 1000 + w, lam, beam)
        res.append(c)
    return {"err": err, "windows": windows, "n_shuffles": n_shuf,
            "lattice_rank1": sum(1 for c in res if c["lattice"]["rank"] == 1),
            "top1_rank1": sum(1 for c in res if c["top1"]["rank"] == 1),
            "lattice_z_median": statistics.median(c["lattice"]["z"] for c in res),
            "top1_z_median": statistics.median(c["top1"]["z"] for c in res)}


def load_model(args):
    paths = args.corpus or LANG_CORPORA.get(args.lang)
    if not paths:
        sys.exit(f"no corpus for --lang {args.lang!r}")
    return NgramModel([read_corpus(p) for p in paths])


def truth_err(lat, seq, key, truth):
    tot = wrong = unk = 0
    for (k, _), c in zip(lat, seq):
        t = truth.get(k)
        if t is None:
            continue
        tot += 1
        if c not in key:
            unk += 1
        elif key[c] != t:
            wrong += 1
    return {"aligned": tot, "wrong": wrong, "unvalued": unk,
            "err": wrong / tot if tot else None, "err_with_U": (wrong + unk) / tot if tot else None}


def cmd_decode(args):
    lat = read_topk(args.topk)
    key = read_key(args.key)
    model = load_model(args)
    lm = LM(model, args.unk_cost)
    seq, obj = viterbi(lat, key, lm, args.lam, args.beam)
    t1 = top1(lat)
    out = {"positions": len(lat), "lam": args.lam, "beam": args.beam, "bonus": lm.bonus, "unk_cost": lm.unk_cost,
           "changed": sum(1 for a, b in zip(t1, seq) if a != b),
           "score_top1": model.score(text_of(t1, key)), "score_lattice": model.score(text_of(seq, key))}
    if args.truth:
        truth = {}
        for r in read_tsv(args.truth):
            truth[(r["line"], int(r["pos"]))] = fold(r["value"]) if r["value"].upper() != "NULL" else ""
        out["truth_top1"] = truth_err(lat, t1, key, truth)
        out["truth_lattice"] = truth_err(lat, seq, key, truth)
    if args.shuffles:
        out["control"] = control(lat, key, lm, model, args.shuffles, args.seed, args.lam, args.beam)
    if args.power_err is not None:
        out["power"] = power(args.power_len or len(lat), key, lm, model, read_confusion(args.confusion), args.power_err,
                             args.power_windows, args.power_shuffles, args.seed, args.lam, args.beam)
    if args.out_prefix:
        with open(args.out_prefix + ".decode.tsv", "w", encoding="utf-8") as f:
            f.write("line\tpos\ttop1\tchosen\tvalue\tprior\tchanged\tgrade_cap\n")
            for (k, c), a, b in zip(lat, t1, seq):
                ch = a != b
                f.write(f"{k[0]}\t{k[1]}\t{a}\t{b}\t{key.get(b, '?')}\t{c.get(b, 0):.3f}\t{int(ch)}\t{'S' if ch else ''}\n")
        Path(args.out_prefix + ".plain.txt").write_text(text_of(seq, key) + "\n", encoding="utf-8")
        Path(args.out_prefix + ".json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


def cmd_from_passes(args):
    rows, stats = from_passes(args.passA, args.passB, args.ref, read_confusion(args.confusion), args.keep_alts)
    write_topk(rows, args.out)
    print(json.dumps(stats))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("from-passes", help="synthesize a top-k TSV from two blind passes")
    f.add_argument("passA"); f.add_argument("passB")
    f.add_argument("--ref"); f.add_argument("--confusion"); f.add_argument("--out", required=True)
    f.add_argument("--keep-alts", action="store_true",
                   help="keep every reader-written alternative (a/b? or the alt column) in the lattice, exempt from "
                        "the 0.02 floor and the top-4 cut (TX-ALTS)")
    d = sub.add_parser("decode", help="lattice decode + controls")
    d.add_argument("topk"); d.add_argument("--key", required=True)
    d.add_argument("--lang", default="it"); d.add_argument("--corpus", nargs="*")
    d.add_argument("--truth", help="TSV line, pos, value (known answer)")
    d.add_argument("--lam", type=float, default=1.0); d.add_argument("--beam", type=int, default=64)
    d.add_argument("--unk-cost", type=float, default=None)
    d.add_argument("--shuffles", type=int, default=0); d.add_argument("--seed", type=int, default=1)
    d.add_argument("--power-err", type=float, default=None); d.add_argument("--confusion")
    d.add_argument("--power-windows", type=int, default=20); d.add_argument("--power-shuffles", type=int, default=50)
    d.add_argument("--power-len", type=int, default=0, help="synthetic window length in signs (default: the lattice's)")
    d.add_argument("--out-prefix")
    a = ap.parse_args(argv)
    (cmd_decode if a.cmd == "decode" else cmd_from_passes)(a)


if __name__ == "__main__":
    main()
