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
order (3), uni_weight (1.0), assign (regular: one vowel per mark string on every base; irregular: one vowel per marked
code+mark type, the base still the consonant -- the control is the same regular-assignment cipher read through the
looser key, so the irregular solver's control number says how much the extra freedom costs). The control's truth alignment and the last solve's per-token decode are kept in the
module (_STASH) between family_run.py's make_control / solve / score_recovery calls, as codemark_curve.py's
TRUTH_INDEX does. Test: python3 tools/tests/test_syllabary.py

DSN2 extension (LANE R8 DSN2, 25 Sept 2026; defaults unchanged, DSN's runs regenerate byte-identically):
  marks=SPEC   per-mark allowed-letter class. SPEC is `mixed` (a mark string whose first element is a numeral, or `?`,
               names a following VOWEL; one containing `~` names a following n or m, the period suspension stroke;
               every other mark -- # + dot o ot and their compounds -- DOUBLES the base letter) or an explicit
               `mark:class,mark:class,*:class` list where class is a letter set (aeiou, nm, ...) or `dbl`. The
               control merges the matching plaintext pairs (consonant+vowel, letter+n/m, a double letter) with a
               use rate bisected PER CLASS so each class's share of N matches the target's; the solver gives a
               letter-set mark a symbol restricted to the set and a doubling mark no symbol (the base code is
               emitted twice).
  boundary=1   a word-edge symbol at every sign/plain run edge, control and target alike: the corpus is folded with
               word spaces kept as the letter `w` (unused in Italian; j->i, v->u already), the stream carries a
               fixed symbol B->w at the start and end of every run (each spec ciphertext line is a run), and the
               control's plain boxes withhold whole words (a run starts and ends at a word boundary) instead of
               `gap` letters. Word boundaries inside a run stay invisible, as on the leaf.
  bases=N      the control's marked tokens use only the N bases that carry the most marks in the target (N=8 for
               Salviati: g e ] eps S7 a m lam), allotted first to the N letters that most need a marked base, so
               the control's code+mark TYPE count sits near the target's (DSN: 278-316 vs 223 without this).
  Decode files: family_run.py now suffixes the file with the --param set (syllabary-1-err=0.05,marks=mixed.txt)."""
import random, re
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


def alloc(units, freqs, pre=None):
    """Greedy homophone allotment (LANE R4 P's rule): highest-frequency unit to the letter with the largest remaining
    deficit, every letter getting one unit before any gets two. units: [(name, weight)] most frequent first.
    pre: {letter: [(name, weight)]} units already allotted (bases=N), counted against the deficit."""
    if pre is None and len(units) < sum(1 for f in freqs.values() if f > 0):
        raise SystemExit(f"syllabary: {len(units)} units for {sum(1 for f in freqs.values() if f > 0)} letters; the target's "
                         "base codes (or marks) are fewer than the letters they must cover")
    tot_u, tot_f = sum(w for _, w in units), sum(freqs.values()) or 1
    homs = {a: list((pre or {}).get(a, [])) for a in freqs}
    tot_u += sum(w for h in homs.values() for _, w in h)
    deficit = {a: f / tot_f - sum(w for _, w in homs[a]) / tot_u for a, f in freqs.items()}
    for name, w in units:
        empty = [a for a in homs if not homs[a]]
        a = max(empty, key=lambda a: freqs[a]) if empty else max(deficit, key=deficit.get)
        homs[a].append((name, w))
        deficit[a] -= w / tot_u
    return homs


def mark_classes(marks, spec_str):
    """{mark string: class} from --param marks=...; class is a letter set (e.g. 'aeiou', 'nm') or 'dbl'."""
    if spec_str in (None, "", "vowel"):
        return {m: VOW for m in marks}
    if spec_str == "mixed":
        out = {}
        for m in marks:
            el = m.split("|")
            if "~" in el:
                out[m] = "nm"
            elif el[0].isdigit() or el[0] == "?":
                out[m] = VOW
            else:
                out[m] = "dbl"
        return out
    table, default = {}, VOW
    for item in spec_str.split(","):
        k, _, v = item.partition(":")
        if k == "*":
            default = v
        else:
            table[k] = v
    return {m: table.get(m, default) for m in marks}


def fold_b(text):
    """ha.fold with word spaces kept as the letter w (boundary=1)."""
    return ha.fold(re.sub(r"\s+", "w", text.strip()))


def _pattern(spec, params):
    pat = spec.get("row_pattern")
    if pat:
        return [c == "S" for c in pat]
    out = []  # no pattern on file: one run per message, one plain box between runs
    for L in params.get("lengths") or [params["N"]]:
        out += [True] * L + [False]
    return out


def _layout(p, pattern, N, gap, use, rng, classes=None, markable=None, boundary=False, runs=None):
    """Walk the tiled row pattern over plaintext p; returns the list of token letter strings (1 or 2 letters).
    use: a rate, or {class: rate} when classes (the set of mark classes) is given; a pair merges only when its
    first letter is in markable (None = any consonant for the vowel class, any letter otherwise). boundary: p
    carries w for word spaces; a plain box withholds the rest of the current word, sign tokens skip w. runs, if
    a list, receives the run lengths in tokens."""
    toks, i, k, cur = [], 0, 0, 0
    rates = use if isinstance(use, dict) else {VOW: use}
    classes = classes or {VOW}
    while len(toks) < N:
        is_sign = pattern[k % len(pattern)]
        k += 1
        if i + 3 >= len(p):
            raise SystemExit("syllabary: plaintext window too short for the layout")
        if not is_sign:
            if runs is not None and cur:
                runs.append(cur); cur = 0
            if boundary:
                j = p.find("w", i)
                i = len(p) if j < 0 else j + 1
            else:
                i += gap
            continue
        if boundary:
            while i < len(p) and p[i] == "w":
                i += 1
            if i + 3 >= len(p):
                raise SystemExit("syllabary: plaintext window too short for the layout")
        a, b = p[i], p[i + 1]
        cls = None
        if b != "w" and (markable is None or a in markable):
            if "dbl" in classes and a == b:
                cls = "dbl"
            else:
                for c in classes:
                    if c != "dbl" and c != VOW and b in c:
                        cls = c; break
                if cls is None and VOW in classes and a not in VOW and b in VOW:
                    cls = VOW
        if cls and rng.random() < rates.get(cls, 0):
            toks.append(p[i:i + 2]); i += 2
        else:
            toks.append(p[i]); i += 1
        cur += 1
    if runs is not None and cur:
        runs.append(cur)
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


def _class_of(tok, classes):
    """The class a 2-letter control token belongs to (dbl, a letter set, or VOW)."""
    if "dbl" in classes and tok[0] == tok[1]:
        return "dbl"
    for c in classes:
        if c not in ("dbl", VOW) and tok[1] in c:
            return c
    return VOW


def make_control(spec, seed, corpora, params):
    N = params["N"]
    gap, err = _p(params, "gap", 2), _p(params, "err", 0.05)
    boundary = str(params.get("boundary", "0")) not in ("0", "", "no", "false")
    nbases = int(params.get("bases", 0) or 0)
    rng = random.Random(seed + 7000)
    ttoks = [t for m in params.get("target_msgs") or [] for t in m]
    tparts = [split_tok(t) for t in ttoks]
    codes = Counter(c for c, _ in tparts).most_common()
    marks = Counter(m for _, m in tparts if m).most_common()
    types = Counter(ttoks).most_common()
    mclass = mark_classes([m for m, _ in marks], params.get("marks"))
    classes = set(mclass.values())
    tshare = {c: sum(n for m, n in marks if mclass[m] == c) / max(1, len(ttoks)) for c in classes}
    marked_share = sum(1 for _, m in tparts if m) / max(1, len(ttoks))
    pattern = _pattern(spec, params)
    n_plain = sum(1 for x in pattern if not x)
    text = fold_b("\n".join(corpora)) if boundary else ha.fold("\n".join(corpora))
    g = 6 if boundary else gap
    n_letters = int(N * 1.6 + g * n_plain * (N / max(1, sum(pattern))) * 1.2) + 200
    plain, rest = draw_window(text, n_letters, seed)
    markable = None
    pre = {}
    dry = _layout(plain, pattern, N, gap, {c: 1.0 for c in classes}, random.Random(seed + 7000), classes, None, boundary)
    # a letter-set class with fewer mark strings than letters keeps only its most-needed letters (a class of one
    # mark for n and m becomes a class for whichever the text needs more), so every merged pair has a mark
    for c in sorted(classes):
        nmarks = sum(1 for m in mclass if mclass[m] == c)
        if c != "dbl" and nmarks < len(c):
            need2 = Counter(t[1] for t in dry if len(t) == 2 and _class_of(t, classes) == c)
            eff = "".join(sorted(need2, key=lambda a: -need2[a])[:nmarks])
            mclass = {m: (eff if k == c else k) for m, k in mclass.items()}
            tshare[eff] = tshare.pop(c)
    classes = set(mclass.values())
    if nbases:  # the N most-marked target bases carry every control mark, allotted first to the neediest letters
        bcount = Counter(c for c, m in tparts if m)
        B = [c for c, _ in bcount.most_common(nbases)]
        need = Counter(t[0] for t in dry if len(t) == 2)
        top = [a for a, _ in need.most_common(nbases)]
        pre = alloc([(b, dict(codes)[b]) for b in B], {a: need[a] for a in top})
        markable = set(top)
        codes_rest = [(c, n) for c, n in codes if c not in B]
    use = params.get("use", "auto")
    lay = lambda rates: _layout(plain, pattern, N, gap, rates, random.Random(seed + 7000), classes, markable, boundary)
    if use == "auto":  # per-class bisection on the use rate (dry walks, seed-fixed) until each class share matches
        rates = {c: 1.0 for c in classes}
        for _ in range(3 if len(classes) > 1 else 1):
            for c in classes:
                lo, hi = 0.0, 1.0
                for _ in range(14):
                    rates[c] = (lo + hi) / 2
                    got = sum(1 for t in lay(rates) if len(t) == 2 and _class_of(t, classes) == c) / N
                    if abs(got - tshare[c]) < 0.004:
                        break
                    lo, hi = (rates[c], hi) if got < tshare[c] else (lo, rates[c])
        use = rates
    else:
        use = {c: float(use) for c in classes}
    runs = []
    toks = _layout(plain, pattern, N, gap, use, random.Random(seed + 7000), classes, markable, boundary, runs)
    if nbases:
        chom = alloc(codes_rest, Counter(t[0] for t in toks), pre=pre)
    else:
        chom = alloc(codes, Counter(t[0] for t in toks))
    mhom = {}
    for c in classes:
        cm = [(m, n) for m, n in marks if mclass[m] == c]
        if c == "dbl":
            mhom[c] = {"2": alloc(cm, {"2": 1})["2"]}
        else:
            need = Counter(t[1] for t in toks if len(t) == 2 and _class_of(t, classes) == c)
            mhom[c] = alloc(cm, {a: need[a] for a in c} if c != VOW else {a: need[a] for a in VOW})
    seq = []
    for t in toks:
        if len(t) == 2:
            c = _class_of(t, classes)
            bset = {x for x, _ in pre.get(t[0], [])}
            hb = [(n, w) for n, w in chom[t[0]] if n in bset] if nbases else chom[t[0]]
            n_, w = zip(*(hb or chom[t[0]])); code = rng.choices(n_, w)[0]
            key = "2" if c == "dbl" else t[1]
            m, w = zip(*mhom[c][key]); seq.append(f"{code}^{rng.choices(m, w)[0]}")
        else:
            n_, w = zip(*chom[t[0]]); seq.append(f"{n_[rng.choices(range(len(n_)), w)[0]]}^")
    counts = {}
    tix = list(range(len(seq)))
    if err:
        seq, tix, counts = measured_error(seq, types, codes, err, random.Random(seed + 9500))
    _STASH.clear()
    _STASH.update({"truth_tokens": toks, "truth_index": tix, "use": use if isinstance(use, float) else
                   {k: round(v, 3) for k, v in use.items()}, "err": err, "gap": gap,
                   "marked_share": round(sum(1 for t in toks if len(t) == 2) / N, 3),
                   "class_share": {c: round(sum(1 for t in toks if len(t) == 2 and _class_of(t, classes) == c) / N, 3) for c in classes},
                   "control_types": len(set(seq)), "bases": nbases, "boundary": boundary, **counts})
    if boundary:  # the noisy sequence split back into runs by the clean run lengths, shifted by the error's index map
        msgs, pos = [], 0
        starts = set()
        acc = 0
        for L in runs:
            starts.add(acc); acc += L
        cur = []
        for s_, j in zip(seq, tix):
            if j is not None and j in starts and cur:
                msgs.append(cur); cur = []
            cur.append(s_)
        if cur:
            msgs.append(cur)
        return msgs, "".join(toks), [rest]
    return [seq], "".join(toks), [rest]


def expand(seq, assign="regular", mclass=None, boundary=False, msgs=None):
    """Tokens -> symbol stream: C<code>, then a vowel symbol when marked: M<marks> under the regular assignment (the
    same mark names the same vowel on every base), M<code^marks> under assign=irregular (each marked TYPE names its own
    vowel, as in the Venetian keys with irregular arrangement; the base still gives the consonant)."""
    out, spans = [], []
    groups = msgs if (boundary and msgs) else [seq]
    for g in groups:
        if boundary:
            out.append("B")
        for t in g:
            code, mark = split_tok(t)
            a = len(out); out.append("C" + code)
            if mark:
                cls = (mclass or {}).get(mark, VOW)
                if cls == "dbl":
                    out.append("C" + code)
                else:
                    out.append("M" + (t if assign == "irregular" else mark))
            spans.append((a, len(out)))
        if boundary:
            out.append("B")
    return out, spans


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    boundary = str(params.get("boundary", "0")) not in ("0", "", "no", "false")
    model = ha.Model([fold_b(t) for t in corpora] if boundary else corpora, _p(params, "order", 3))
    seq = [s for m in cipher_msgs for s in m]
    ttoks = [t for m in params.get("target_msgs") or [] for t in m]
    mclass = mark_classes(sorted({split_tok(t)[1] for t in ttoks + seq if split_tok(t)[1]}), params.get("marks"))
    stream, spans = expand(seq, params.get("assign", "regular"), mclass, boundary, cipher_msgs)
    allowed = {}
    if boundary:  # the boundary letter is reserved: no free symbol may decode to it
        allowed = {s: ha.ALPHA.replace("w", "") for s in stream if s.startswith("C")}
    for s in stream:
        if s.startswith("M"):
            mk = s[1:] if params.get("assign", "regular") != "irregular" else split_tok(s[1:])[1]
            allowed[s] = mclass.get(mk, VOW)
    res = ha.solve(stream, model, restarts, _p(params, "iters", 120000), seed, _p(params, "uni_weight", 1.0), allowed=allowed,
                   fixed={"B": "w"} if boundary else None)
    sc, key = res[0][:2]
    dec_tokens = ["".join(key[x] for x in stream[a:b]) for a, b in spans]
    dec = "".join(dec_tokens)  # decode carries no boundary letters: token spans exclude B
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
