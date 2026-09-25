"""syllabary: partial syllabary -- base code = letter, a superscript mark on a consonant base = the FOLLOWING vowel.

Design (LANE R8 DSN, 25 Sept 2026, for fr2933-salviati-1525; the period pattern is the Venetian letter-plus-superscript
family, sources/cryptiana/web/venetian.htm: "syllables ... represented by a letter followed by one or two digits",
with -a -e -i -o -u given a consistent figure). A token is code^marks. A bare token stands for one letter (the base
codes are homophones of the alphabet); a marked token stands for a consonant plus the vowel the mark names, so the
same mark means the same vowel on every base (regular assignment) and the marks are homophones of a e i o u. Unlike
LANE R4 P's `vi` control (every consonant+vowel merged, 51% of tokens marked against the target's 32%), the scribe
uses a syllable sign only a share `use` of the time, chosen so the control's marked share matches the target's own.

Control: a plaintext window from the judge corpus (held out of the solver's model), laid out on the target's own
sign/plain-box row pattern (spec["row_pattern"], S = sign box, _ = plain box, tiled; each plain box withholds
`gap` letters, default 2 as in the Salviati cm controls), the target's own base codes allotted to letters and its
own mark strings to vowels by frequency deficit (each letter picks a homophone with the target type's frequency as
weight), then the MEASURED transcription-error mix of NOTES 'CM3' sec.1 applied at the token level (`err`, default
0.05, split del:ins:code 0.465:0.331:0.204 -- a deleted token loses its 1-2 letters, an inserted token is a spurious
type at the target's frequencies, a code confusion swaps the base for a listed partner #/+ g/y bh/g #/Z f/y bh/phi).
Solver: every token is written as a code symbol then a mark symbol (P's expansion), mark symbols restricted to
a e i o u (`allowed`), and tools/homophonic_anneal.py anneals over the ~76 symbols with the corpus trigram model.
Recovery on a control is TOKEN accuracy (every letter the token stands for right; a deleted token counts wrong, an
inserted one in neither numerator nor denominator), the CM3 convention, so the numbers sit beside CM3's rows.

params: err (0.05), gap (2), use (auto = matched to the target's marked share, or a number 0..1), iters (120000),
order (3), uni_weight (1.0). The control's truth alignment and the last solve's per-token decode are kept in the
module (_STASH) between family_run.py's make_control / solve / score_recovery calls, as codemark_curve.py's
TRUTH_INDEX does. Test: python3 tools/tests/test_syllabary.py"""
import random
from collections import Counter
import homophonic_anneal as ha
from families import draw_window

DESCRIPTION = ("partial syllabary: base code = letter, mark on a consonant = following vowel (--param use=auto err=0.05 "
               "gap=2); control on the spec's row_pattern with the CM3 measured error mix; token accuracy")
VOW = "aeiou"
CONFUSE = [("#", "+"), ("g", "y"), ("bh", "g"), ("#", "Z"), ("f", "y"), ("bh", "phi")]
MIX = (0.465, 0.331, 0.204)
_STASH = {}


def _p(params, k, d):
    return type(d)(params.get(k, d))


def split_tok(t):
    code, _, mark = t.partition("^")
    return code, mark


def alloc(units, freqs):
    """Greedy homophone allotment (LANE R4 P's rule): highest-frequency unit to the letter with the largest remaining
    deficit, every letter getting one unit before any gets two. units: [(name, weight)] most frequent first."""
    if len(units) < sum(1 for f in freqs.values() if f > 0):
        raise SystemExit(f"syllabary: {len(units)} units for {sum(1 for f in freqs.values() if f > 0)} letters; the target's "
                         "base codes (or marks) are fewer than the letters they must cover")
    tot_u, tot_f = sum(w for _, w in units), sum(freqs.values()) or 1
    deficit = {a: f / tot_f for a, f in freqs.items()}
    homs = {a: [] for a in freqs}
    for name, w in units:
        empty = [a for a in homs if not homs[a]]
        a = max(empty, key=lambda a: freqs[a]) if empty else max(deficit, key=deficit.get)
        homs[a].append((name, w))
        deficit[a] -= w / tot_u
    return homs


def _pattern(spec, params):
    pat = spec.get("row_pattern")
    if pat:
        return [c == "S" for c in pat]
    out = []  # no pattern on file: one run per message, one plain box between runs
    for L in params.get("lengths") or [params["N"]]:
        out += [True] * L + [False]
    return out


def _layout(p, pattern, N, gap, use, rng):
    """Walk the tiled row pattern over plaintext p; returns the list of token letter strings (1 or 2 letters)."""
    toks, i, k = [], 0, 0
    while len(toks) < N:
        is_sign = pattern[k % len(pattern)]
        k += 1
        if i + 2 >= len(p):
            raise SystemExit("syllabary: plaintext window too short for the layout")
        if not is_sign:
            i += gap
            continue
        if p[i] not in VOW and p[i + 1] in VOW and rng.random() < use:
            toks.append(p[i:i + 2]); i += 2
        else:
            toks.append(p[i]); i += 1
    return toks


def measured_error(seq, types, code_freq, err, rng, mix=MIX, confuse=CONFUSE):
    """The CM3 measured error mix on a token list. Returns (noisy_seq, truth_index, counts); truth_index[i] is the
    clean position a surviving token came from, None for an inserted one."""
    pdel, pins, pcode = [err * m / sum(mix) for m in mix]
    partners = {}
    for a, b in confuse:
        partners.setdefault(a, []).append(b); partners.setdefault(b, []).append(a)
    tn, tw = zip(*types) if types else ((), ())
    cn, cw = zip(*code_freq) if code_freq else ((), ())
    out, tix, ndel, nins, ncode = [], [], 0, 0, 0
    for i, s in enumerate(seq):
        r = rng.random()
        if r < pdel:
            ndel += 1; continue
        if r < pdel + pcode:
            code, mark = split_tok(s)
            p = partners.get(code)
            newcode = rng.choice(p) if p else rng.choices(cn, cw)[0]
            if newcode != code:
                ncode += 1
            s = f"{newcode}^{mark}"
        out.append(s); tix.append(i)
        if tn and rng.random() < pins:
            out.append(rng.choices(tn, tw)[0]); tix.append(None); nins += 1
    return out, tix, {"del": ndel, "ins": nins, "code": ncode}


def make_control(spec, seed, corpora, params):
    N = params["N"]
    gap, err = _p(params, "gap", 2), _p(params, "err", 0.05)
    rng = random.Random(seed + 7000)
    ttoks = [t for m in params.get("target_msgs") or [] for t in m]
    tparts = [split_tok(t) for t in ttoks]
    codes = Counter(c for c, _ in tparts).most_common()
    marks = Counter(m for _, m in tparts if m).most_common()
    types = Counter(ttoks).most_common()
    marked_share = sum(1 for _, m in tparts if m) / max(1, len(ttoks))
    pattern = _pattern(spec, params)
    n_plain = sum(1 for x in pattern if not x)
    text = ha.fold("\n".join(corpora))
    n_letters = int(N * 1.6 + gap * n_plain * (N / max(1, sum(pattern))) * 1.2) + 200
    plain, rest = draw_window(text, n_letters, seed)
    use = params.get("use", "auto")
    if use == "auto":  # bisection on the use rate (dry walks, seed-fixed) until the marked share matches the target's
        lo, hi, use = 0.0, 1.0, 1.0
        for _ in range(14):
            use = (lo + hi) / 2
            got = sum(1 for t in _layout(plain, pattern, N, gap, use, random.Random(seed + 7000)) if len(t) == 2) / N
            if abs(got - marked_share) < 0.004:
                break
            lo, hi = (use, hi) if got < marked_share else (lo, use)
    else:
        use = float(use)
    toks = _layout(plain, pattern, N, gap, use, random.Random(seed + 7000))
    chom = alloc(codes, Counter(t[0] for t in toks))
    mhom = alloc(marks, Counter(t[1] for t in toks if len(t) == 2))
    seq = []
    for t in toks:
        c, w = zip(*chom[t[0]]); code = rng.choices(c, w)[0]
        if len(t) == 2:
            m, w = zip(*mhom[t[1]]); seq.append(f"{code}^{rng.choices(m, w)[0]}")
        else:
            seq.append(f"{code}^")
    counts = {}
    tix = list(range(len(seq)))
    if err:
        seq, tix, counts = measured_error(seq, types, codes, err, random.Random(seed + 9500))
    _STASH.clear()
    _STASH.update({"truth_tokens": toks, "truth_index": tix, "use": round(use, 3), "err": err, "gap": gap,
                   "marked_share": round(sum(1 for t in toks if len(t) == 2) / N, 3), **counts})
    return [seq], "".join(toks), [rest]


def expand(seq):
    """Tokens -> symbol stream: C<code>, then M<marks> when marked."""
    out, spans = [], []
    for t in seq:
        code, mark = split_tok(t)
        a = len(out); out.append("C" + code)
        if mark:
            out.append("M" + mark)
        spans.append((a, len(out)))
    return out, spans


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    model = ha.Model(corpora, _p(params, "order", 3))
    seq = [s for m in cipher_msgs for s in m]
    stream, spans = expand(seq)
    allowed = {s: VOW for s in stream if s.startswith("M")}
    res = ha.solve(stream, model, restarts, _p(params, "iters", 120000), seed, _p(params, "uni_weight", 1.0), allowed=allowed)
    sc, key = res[0][:2]
    dec_tokens = ["".join(key[x] for x in stream[a:b]) for a, b in spans]
    dec = "".join(dec_tokens)
    _STASH["dec_tokens"] = dec_tokens
    info = {"restart_scores": [round(r[0], 1) for r in res], "symbols": len(set(stream)), "letters": len(dec),
            "score_per_symbol": round(sc / max(1, len(stream)), 4), "score_per_letter": round(sc / max(1, len(dec)), 4),
            **{k: v for k, v in _STASH.items() if k not in ("truth_tokens", "truth_index", "dec_tokens")}, "key": key}
    return dec, sc, info


def score_recovery(plain, truth):
    """Token accuracy against the control stash when it matches the last solve; else letter-wise."""
    tt, tix, dt = _STASH.get("truth_tokens"), _STASH.get("truth_index"), _STASH.get("dec_tokens")
    if tt and tix and dt and len(dt) == len(tix):
        ok = sum(dt[i] == tt[j] for i, j in enumerate(tix) if j is not None)
        return ok / max(1, len(tt))
    n = max(1, len(truth))
    return sum(1 for a, b in zip(plain, truth) if a == b) / n


def split_decode(dec, msgs):
    """family_run.py hook: the decode file's lines follow the messages' TOKEN counts (a marked token is 2 letters)."""
    dt = _STASH.get("dec_tokens")
    if not dt or len(dt) != sum(len(m) for m in msgs):
        return None
    lines, pos = [], 0
    for m in msgs:
        lines.append("".join(dt[pos:pos + len(m)])); pos += len(m)
    return lines
