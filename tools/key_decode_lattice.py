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
               --confusion-matrix M.tsv [--spread S] [--matrix-only] (TXE-E, 9 Oct 2026; TX-IDEAS M5): M.tsv (columns true, read,
               p, optional pass = A/B) is P(read | true) learnt by `learn-confusion`; each read sign r adds, for every true
               sign t with p(r|t) > 0, candidate t with weight S x weight(reader) x p(r|t) / sum_t p(r|t) (a Bayes flip
               with a flat prior over the signs that could have produced r), on top of the fixed rule; S default 0.3.
               --matrix-only drops the confusion_1572 spread (a disagreement count, not an error rate) and keeps the flip.
               Lesson it answers: half of pass A's errors on Birago no.87 are the same wrong sign in both readers, and only
               27 of 97 errors had the truth anywhere in the two-pass lattice (TX-DECODE).
               --stability STAB.tsv [--box-pos BOX_POS.tsv] [--stab-floor 0.6] [--stab-gain 0.9] [--stab-shuffle SEED]
               (TXE-J, 9 Oct 2026; TX-IDEAS M11): a per-position prior from the IMAGE. STAB.tsv is `glyph_atlas.py classify
               --jitter` output (box, stab) mapped to positions by --box-pos (`tools/tx_compare.py map`, label-blind; a
               position under several boxes takes their minimum stab), or a TSV line, pos, stab. At a position with
               stab < floor the readers' candidates stay as they are (the doubtful tile); at stab >= floor the top-1
               candidate's weight p becomes p + (1 - p) x gain and the others are scaled by (1 - gain) (the image is sure;
               the lattice must not override the readers there). Unmapped positions are unchanged. --stab-shuffle SEED
               permutes the stab values over the mapped positions: the rule-3 control. Lesson it answers: the lattice
               had only the readers' stated confidence, and a blanket lattice override raises error (TX-DECODE).
  learn-confusion PASS.tsv [PASS2.tsv ...] --truth TRUTH.tsv --lines L... --out M.tsv [--key KEY.tsv] [--line-prefix P]
               [--per-pass] [--shuffle-offdiag SEED]
               estimates P(read | true) over the named lines only, from tools/tx_bench.py's per-position alignment of each
               pass line to the truth's reference skeleton (scored positions; a truth `|`-set splits a miss's count
               equally over its members; deletions are not counted), add-0.5 smoothing over the sheet's cells (the key's
               signs, --key; else every sign seen). It reads truth, so it is run ONLY on tune lines; the lines it learnt
               from are written in M.tsv's '#' header. --shuffle-offdiag SEED permutes each true row's off-diagonal cells
               (same row mass): the rule-3 control matrix. Prints the top off-diagonal mass.
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


def read_matrix(p):
    """{pass or '': {read: {true: p}}} from a learn-confusion M.tsv ('#' lines are header comments)."""
    M = defaultdict(lambda: defaultdict(dict))
    if not p:
        return M
    rows = csv.DictReader((l for l in open(p, encoding="utf-8") if not l.startswith("#")), delimiter="\t")
    for r in rows:
        v = float(r["p"])
        if v > 0:
            M[(r.get("pass") or "").strip()][r["read"]][r["true"]] = v
    return M


def flip_mass(s, w, flip, spread):
    """Bayes flip of read sign s: {true t: spread x w x p(s|t) / sum_t p(s|t)} (flat prior over t)."""
    col = (flip or {}).get(s)
    if not col:
        return {}
    tot = sum(col.values())
    return {t: spread * w * v / tot for t, v in col.items()}


def reader_mass(row, nb, alts_out=None, flip=None, spread=0.3):
    out = defaultdict(float)
    s, alts, conf = split_cands(row)
    w = CONF_W.get(conf, 0.6)
    out[s] += w
    for t, v in flip_mass(s, w, flip, spread).items():
        out[t] += v
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


def from_passes(pa, pb, ref, nb, keep_alts=False, matrix=None, spread=0.3):
    A, B = read_pass(pa), read_pass(pb)
    matrix = matrix or {}
    flips = [matrix.get("A") or matrix.get(""), matrix.get("B") or matrix.get("")]
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
        for P, flip in zip((A, B), flips):
            prow = P.get(key_of[ln], [])
            m = align(skel, [split_cands(r)[0] for r in prow])
            for j, r in enumerate(prow):
                if j in m:
                    for k, v in reader_mass(r, nb, keep[m[j]] if keep_alts else None, flip, spread).items():
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


def read_stability(path, box_pos=None):
    """{(line, pos): stab}. With box_pos (sid, line, pos, op), STAB rows are keyed by box; several boxes on one
    position -> the minimum; one box over two positions -> both."""
    rows = read_tsv(path)
    st = {}
    if box_pos:
        by_box = {r["box"]: float(r["stab"]) for r in rows if r.get("stab", "") != ""}
        for r in read_tsv(box_pos):
            if r["sid"] in by_box:
                k = (r["line"], int(r["pos"]))
                st[k] = min(st.get(k, 1.0), by_box[r["sid"]])
    else:
        for r in rows:
            st[(r["line"], int(r["pos"]))] = float(r["stab"])
    return st


def shuffle_stability(st, seed):
    keys = sorted(st); vals = [st[k] for k in keys]
    random.Random(seed).shuffle(vals)
    return dict(zip(keys, vals))


def apply_stability(rows, st, floor=0.6, gain=0.9):
    """rows (line, pos, cand, p) -> rows with the top-1 sharpened where stab >= floor (see --stability)."""
    by = defaultdict(list)
    order = []
    for ln, pos, c, p in rows:
        if (ln, pos) not in by:
            order.append((ln, pos))
        by[(ln, pos)].append((c, p))
    out, n = [], 0
    for k in order:
        cs = by[k]
        if k in st and st[k] >= floor and len(cs) > 1:
            top = max(cs, key=lambda cp: cp[1])[0]
            cs = [(c, p + (1 - p) * gain if c == top else p * (1 - gain)) for c, p in cs]
            n += 1
        out += [(k[0], k[1], c, p) for c, p in cs]
    return out, n


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


def learn_confusion(passes, truth_rows, lines, prefix=None, signs=None, per_pass=False, smooth=0.5):
    """counts[(pass, true, read)] over the scored positions of `lines`, aligned with tx_bench.align; returns
    (rows [(pass, true, read, p)], stats). P(read | true) = (n + smooth) / (N_true + smooth x |signs|)."""
    import tx_bench
    lines = set(lines)
    by = defaultdict(list)
    for r in truth_rows:
        if r["line"] in lines:
            by[r["line"]].append(r)
    cnt = defaultdict(float); seen = set(signs or [])
    stats = {"lines": len(by), "positions": 0, "misses": 0, "deleted": 0}
    for i, pp in enumerate(passes):
        tag = "AB"[i] if per_pass and i < 2 else (str(i + 1) if per_pass else "")
        P = read_pass(pp)
        for ln, rows in by.items():
            rows.sort(key=lambda r: float(r["pos"]))
            pk = ln if ln in P else (ln[len(prefix) + 1:] if prefix and ln.startswith(prefix + "_") else short(ln))
            out = [split_cands(r)[0] for r in P.get(pk, [])]
            if not out:
                continue
            ref = [r["ref_sign"] for r in rows]
            ts = [set(filter(None, r["truth"].split("|"))) for r in rows]
            for ri, osg in tx_bench.align(ref, ts, out):
                if ri is None or rows[ri]["status"] != "scored":
                    continue
                if osg is None:
                    stats["deleted"] += 1
                    continue
                stats["positions"] += 1
                seen.add(osg); seen.update(ts[ri])
                if osg in ts[ri]:
                    cnt[(tag, osg, osg)] += 1
                else:
                    stats["misses"] += 1
                    for t in ts[ri]:
                        cnt[(tag, t, osg)] += 1 / len(ts[ri])
    signs = sorted(signs or seen)
    tags = sorted({k[0] for k in cnt}) or [""]
    out = []
    for tag in tags:
        for t in signs:
            N = sum(cnt.get((tag, t, r), 0) for r in signs)
            for r in signs:
                out.append((tag, t, r, (cnt.get((tag, t, r), 0) + smooth) / (N + smooth * len(signs))))
    stats["signs"] = len(signs)
    return out, stats


def shuffle_offdiag(rows, seed):
    """permute each (pass, true) row's off-diagonal p values among its own off-diagonal cells (row mass kept)."""
    rnd = random.Random(seed)
    grp = defaultdict(list)
    for i, (tag, t, r, p) in enumerate(rows):
        if t != r:
            grp[(tag, t)].append(i)
    rows = list(rows)
    for idx in grp.values():
        vals = [rows[i][3] for i in idx]; rnd.shuffle(vals)
        for i, v in zip(idx, vals):
            rows[i] = rows[i][:3] + (v,)
    return rows


def write_matrix(rows, out, header):
    per = any(tag for tag, *_ in rows)
    with open(out, "w", encoding="utf-8") as f:
        for h in header:
            f.write("# " + h + "\n")
        f.write(("pass\t" if per else "") + "true\tread\tp\n")
        for tag, t, r, p in rows:
            f.write((tag + "\t" if per else "") + f"{t}\t{r}\t{p:.6f}\n")


def top_offdiag(rows, n=12):
    """off-diagonal cells ranked by p(read | true) minus the row's smoothing floor."""
    floor = defaultdict(lambda: 1.0)
    for tag, t, r, p in rows:
        floor[(tag, t)] = min(floor[(tag, t)], p)
    ex = [(p - floor[(tag, t)], tag, t, r, p) for tag, t, r, p in rows if t != r and p > floor[(tag, t)] + 1e-12]
    return sorted(ex, reverse=True)[:n]


def cmd_learn_confusion(args):
    import tx_bench
    truth = tx_bench.read_tsv(args.truth)
    signs = sorted(read_key(args.key)) if args.key else None
    rows, stats = learn_confusion(args.passes, truth, args.lines, args.line_prefix, signs, args.per_pass, args.smooth)
    hdr = ["learn-confusion (tools/key_decode_lattice.py, TXE-E): P(read | true), add-%g smoothing over %d signs"
           % (args.smooth, stats["signs"]),
           "learnt from lines: " + " ".join(args.lines),
           "passes: " + " ".join(args.passes) + "; truth: " + args.truth]
    if args.shuffle_offdiag is not None:
        rows = shuffle_offdiag(rows, args.shuffle_offdiag)
        hdr.append("CONTROL: off-diagonal cells permuted within each true row, seed %d" % args.shuffle_offdiag)
    write_matrix(rows, args.out, hdr)
    stats["top_offdiag"] = ["%s%s<-%s p %.3f (excess %.3f)" % (tag + ":" if tag else "", t, r, p, e)
                            for e, tag, t, r, p in top_offdiag(rows)]
    print(json.dumps(stats, indent=1))


def cmd_from_passes(args):
    if args.matrix_only and not args.confusion_matrix:
        sys.exit("--matrix-only needs --confusion-matrix")
    nb = {} if args.matrix_only else read_confusion(args.confusion)
    rows, stats = from_passes(args.passA, args.passB, args.ref, nb, args.keep_alts,
                              read_matrix(args.confusion_matrix), args.spread)
    if args.stability:
        st = read_stability(args.stability, args.box_pos)
        if args.stab_shuffle is not None:
            st = shuffle_stability(st, args.stab_shuffle)
        rows, n = apply_stability(rows, st, args.stab_floor, args.stab_gain)
        stats.update(stab_mapped=len(st), stab_sharpened=n, stab_doubtful=sum(v < args.stab_floor for v in st.values()))
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
    f.add_argument("--confusion-matrix", help="learn-confusion M.tsv: add the Bayes-flip candidates (TXE-E)")
    f.add_argument("--spread", type=float, default=0.3, help="flip weight S (default 0.3)")
    f.add_argument("--matrix-only", action="store_true", help="replace the confusion_1572 spread with the flip")
    f.add_argument("--stability", help="TXE-J: glyph_atlas classify --jitter TSV (with --box-pos) or line,pos,stab TSV")
    f.add_argument("--box-pos", help="tx_compare.py map box_pos.tsv (sid, line, pos, op): maps --stability boxes to positions")
    f.add_argument("--stab-floor", type=float, default=0.6, help="stab below this: readers' candidates kept as they are (0.6)")
    f.add_argument("--stab-gain", type=float, default=0.9, help="stab >= floor: top-1 p -> p + (1-p) x gain (0.9)")
    f.add_argument("--stab-shuffle", type=int, default=None, help="control: permute stab over mapped positions (seed)")
    lc = sub.add_parser("learn-confusion", help="P(read | true) from passes + truth on named (tune) lines")
    lc.add_argument("passes", nargs="+"); lc.add_argument("--truth", required=True)
    lc.add_argument("--lines", nargs="+", required=True); lc.add_argument("--out", required=True)
    lc.add_argument("--key", help="key TSV: its signs are the sheet's cells for smoothing")
    lc.add_argument("--line-prefix", help="page prefix of the truth lines (f178v) when pass lines are bare L01")
    lc.add_argument("--per-pass", action="store_true", help="one matrix per pass (column pass = A, B)")
    lc.add_argument("--smooth", type=float, default=0.5)
    lc.add_argument("--shuffle-offdiag", type=int, default=None, help="control: permute off-diagonal cells (seed)")
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
    {"decode": cmd_decode, "from-passes": cmd_from_passes, "learn-confusion": cmd_learn_confusion}[a.cmd](a)


if __name__ == "__main__":
    main()
