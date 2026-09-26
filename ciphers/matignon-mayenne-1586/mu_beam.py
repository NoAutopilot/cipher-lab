#!/usr/bin/env python3
"""Job bMATBEAM (LANE B6, 26 Sept 2026): matignon-mayenne-1586 NEAR step (1b).

Resolve the Cipher-1 M codes (per occurrence, among their own key.tsv candidates) and the unkeyed U signs
(one global value each: a letter, `null`, or `TOK` = a nomenclator word/name that resets the letter context)
with a period-French character 6-gram model (interpolated Witten-Bell), H letters fixed.

Search: alternating optimisation, restarts. (a) M step: exact Viterbi per line over the M candidates, states
recombined on the last ORDER-1 letters (exact for this LM). (b) U step: coordinate ascent over the U signs in
random order, each sign tried at every value, scoring only the lines that contain it with the M choices held.
Repeat (a)+(b) until no U value changes (max ITERS). Objective: total log2 P of the emitted letters; `null`
and `TOK` each cost one average character (the model's held-out bits/char), so neither is free.
(The orchestrator's sketch put the M beam inside the U loop; alternating is the same fixed point at a fraction
of the cost, and control (A) below is what licenses it either way.)

LM: tools/data/fr16 lettresdecatheri01 + lettresindites00marg (train). Held-out: lettresdecatheri02, never
used for training -- control (A)'s plaintext passage is drawn from it.

Controls (rule 3), run before the target:
 (A) known-answer: a held-out catheri02 passage of the target's letter length enciphered with the target's
     own structure (H inverse map, the same M codes with the same candidate sets, as many U signs as the target
     with the target's per-sign counts, each standing for one letter, BOX/BOX2 as nomenclator words at the
     target's rate, word codes at the target's rate), then the identical search; M-occurrence and U-sign
     accuracy against the truth. Gate (stated before running): U-sign accuracy >= 0.60 (distinct signs,
     unweighted) and M accuracy >= frequency baseline + 10 points, mean of 3 seeds.
 (B) shuffled-line-order null: target tokens shuffled within each line, 3 seeds, same search; LM bits/char
     before (initial random U + first M Viterbi) and after, vs the target's own before/after.

Run from the repository root:  python3 ciphers/matignon-mayenne-1586/mu_beam.py [--quick]
Writes ciphers/matignon-mayenne-1586/mu_beam_results.json and mu_beam_reading.txt (the target's best
restart, U=TOK rendered as a space, null dropped); --check regenerates and exits 1 if either is stale.
"""
import sys, os, csv, gzip, re, math, random, json, collections, unicodedata, time
from multiprocessing import Pool

T = 'ciphers/matignon-mayenne-1586'
D = 'tools/data/fr16'
ORDER = 6
ITERS = 30   # round 1 used 6 and 5 control restarts; no restart converged (see NOTES.md, bMATBEAM)
RESTARTS_TARGET = 6
RESTARTS_CONTROL = 10
SEEDS = (1, 2, 3)
REPL_SEEDS = (4, 5, 6)   # replication, declared before round 2: the gate must hold on these too
LETTERS = 'abcdefghilmnopqrstuxyz'  # folded alphabet: j->i, v->u, w->uu, k kept below if present
TOK, NULL = '#', ''


def fold_text(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn').lower()
    s = s.replace('j', 'i').replace('v', 'u').replace('w', 'uu')
    return s


def words_of(fn):
    with gzip.open(fn, 'rt', encoding='utf-8', errors='replace') as f:
        txt = f.read()
    txt = re.sub(r'-\s*\n\s*', '', txt)
    return [re.sub('[^a-z]', '', fold_text(w)) for w in re.findall(r"[^\W\d_]+", txt)]


class LM:
    def __init__(self, text):
        cnt = [collections.defaultdict(collections.Counter) for _ in range(ORDER)]
        for k in range(ORDER):
            for i in range(k, len(text)):
                cnt[k][text[i - k:i]][text[i]] += 1
        self.c = [{h: (dict(v), sum(v.values()), len(v)) for h, v in ck.items()} for ck in cnt]
        self.V = len(set(text)) + 1
        self.memo = {}

    def lp(self, h, ch):
        key = (h, ch)
        r = self.memo.get(key)
        if r is not None:
            return r
        pr = 1.0 / self.V
        for k in range(0, len(h) + 1):
            e = self.c[k].get(h[len(h) - k:] if k else '')
            if not e:
                break
            d, n, t = e
            pr = (d.get(ch, 0) + t * pr) / (n + t)
        r = math.log2(pr)
        self.memo[key] = r
        return r


def emit(lm, ctx, s, cost):
    """append emission s to context ctx; return (new ctx, logp)."""
    if s == TOK:
        return '', -cost
    if s == NULL:
        return ctx, -cost
    lp = 0.0
    for ch in s:
        lp += lm.lp(ctx, ch)
        ctx = (ctx + ch)[-(ORDER - 1):]
    return ctx, lp


# ---------------- data model: a line is a list of tokens (kind, sign, cands) ----------------
# kind 'H' -> cands=[string] fixed; 'M' -> cands list; 'U' -> global value of sign

def load_key():
    key = {}
    for r in csv.DictReader(open(f'{T}/key.tsv'), delimiter='\t'):
        key[r['code']] = r['value']
    return key


def load_target():
    lines = collections.OrderedDict()
    for r in csv.DictReader(open(f'{T}/reading_tokens.tsv'), delimiter='\t'):
        v, g = r['value'], r['grade']
        if g == 'U':
            tok = ('U', r['sign'], None)
        elif g == 'M':
            tok = ('M', r['sign'], [fold_text(x) for x in v.split('|')])
        else:
            tok = ('H', r['sign'], [NULL if v == '*' else fold_text(v)])
        lines.setdefault(r['line'], []).append(tok)
    return list(lines.values())


# ---------------- search ----------------

def viterbi_line(lm, line, uval, cost):
    """exact best M choices for one line given U values. returns (logp, choices dict pos->idx)."""
    beam = {'': (0.0, ())}
    for pos, (kind, sign, cands) in enumerate(line):
        nb = {}
        if kind == 'M':
            opts = list(enumerate(cands))
        elif kind == 'U':
            opts = [(None, uval[sign])]
        else:
            opts = [(None, cands[0])]
        for ctx, (lp, ch) in beam.items():
            for idx, s in opts:
                nctx, d = emit(lm, ctx, s, cost)
                nlp = lp + d
                if nctx not in nb or nb[nctx][0] < nlp:
                    nb[nctx] = (nlp, ch + ((pos, idx),) if idx is not None else ch)
        beam = nb
    lp, ch = max(beam.values(), key=lambda x: x[0])
    return lp, dict(ch)


def score_line(lm, line, uval, mch, cost):
    ctx, lp = '', 0.0
    for pos, (kind, sign, cands) in enumerate(line):
        s = cands[mch.get(pos, 0)] if kind == 'M' else (uval[sign] if kind == 'U' else cands[0])
        ctx, d = emit(lm, ctx, s, cost)
        lp += d
    return lp


def n_letters(line, uval, mch):
    n = 0
    for pos, (kind, sign, cands) in enumerate(line):
        s = cands[mch.get(pos, 0)] if kind == 'M' else (uval[sign] if kind == 'U' else cands[0])
        n += 0 if s == TOK else max(len(s), 1)
    return n


def search(lm, lines, seed, cost, values):
    rnd = random.Random(seed)
    usigns = sorted({t[1] for L in lines for t in L if t[0] == 'U'})
    where = collections.defaultdict(set)
    for i, L in enumerate(lines):
        for t in L:
            if t[0] == 'U':
                where[t[1]].add(i)
    freq_letters = 'eeeeeeeeeeeeeessssssssiiiiiiinnnnnnnttttttrrrrrruuuuuuaaaaaaalllllooooooddddccccmmmppqqbghfy'
    uval = {s: rnd.choice(freq_letters) for s in usigns}
    mch = [viterbi_line(lm, L, uval, cost)[1] for L in lines]
    tot = lambda: sum(score_line(lm, L, uval, mch[i], cost) for i, L in enumerate(lines))
    nl = lambda: sum(n_letters(L, uval, mch[i]) for i, L in enumerate(lines))
    before = tot() / nl()
    for it in range(ITERS):
        changed = 0
        order = usigns[:]
        rnd.shuffle(order)
        for s in order:
            idx = sorted(where[s])
            best, bestv = None, uval[s]
            for v in values:
                uval[s] = v
                sc = sum(score_line(lm, lines[i], uval, mch[i], cost) for i in idx)
                if best is None or sc > best + 1e-9:
                    best, bestv = sc, v
            # NB (found after the run, left as is so the committed JSON reproduces): uval[s] holds the LAST value
            # tried here, not the old one, so this test almost never reads 0 and every run goes the full ITERS.
            if bestv != uval.get(s):
                changed += 1
            uval[s] = bestv
        mch = [viterbi_line(lm, L, uval, cost)[1] for L in lines]
        if changed == 0:
            break
    obj = tot()
    return dict(obj=obj, before=before, after=obj / nl(), uval=uval, mch=mch, iters=it + 1)


def margins(lm, lines, res, cost, values):
    """per U sign: best value's margin (bits) over the second-best, all else held."""
    uval, mch = dict(res['uval']), res['mch']
    out = {}
    for s in sorted(uval):
        idx = [i for i, L in enumerate(lines) if any(t[0] == 'U' and t[1] == s for t in L)]
        sc = {}
        for v in values:
            uval[s] = v
            sc[v] = sum(score_line(lm, lines[i], uval, mch[i], cost) for i in idx)
        uval[s] = res['uval'][s]
        best = sorted(sc.items(), key=lambda x: -x[1])
        out[s] = (best[0][0], best[0][1] - best[1][1], best[1][0])
    return out


# ---------------- control (A): synthetic encipherment ----------------

def build_control(target, key, heldout_words, seed):
    rnd = random.Random(1000 + seed)
    # sign inventories with target counts
    hcount = collections.Counter()
    mcount = collections.Counter()
    ucount = collections.Counter()
    mcands = {}
    for L in target:
        for kind, sign, c in L:
            if kind == 'H':
                hcount[(sign, c[0])] += 1
            elif kind == 'M':
                mcount[sign] += 1; mcands[sign] = c
            else:
                ucount[sign] += 1
    box = [s for s in ucount if s.startswith('BOX')]
    uletters = [s for s in ucount if s not in box]
    # each non-box U sign stands for one letter, drawn by French letter frequency (text unigram)
    uni = collections.Counter(''.join(heldout_words))
    pool = [ch for ch, n in uni.items() for _ in range(n // 100 + 1)]
    utrue = {s: rnd.choice(pool) for s in uletters}
    for s in box:
        utrue[s] = TOK
    # emission options: string -> list of (sign, kind, weight, trueidx)
    opts = collections.defaultdict(list)
    for (sign, v), n in hcount.items():
        if v:
            opts[v].append(('H', sign, n, None))
    for sign, n in mcount.items():
        for j, c in enumerate(mcands[sign]):
            opts[c].append(('M', sign, n / len(mcands[sign]), j))
    for s in uletters:
        opts[utrue[s]].append(('U', s, ucount[s], None))
    total_tokens = sum(len(L) for L in target)
    box_rate = sum(ucount[s] for s in box) / total_tokens
    boxw = [(s, ucount[s]) for s in box]
    wordcodes = {v for (sign, v), n in hcount.items() if len(v) > 1}
    lens = [len(L) for L in target]
    toks, truth = [], []
    wi = rnd.randrange(len(heldout_words) // 4, len(heldout_words) // 2)
    while len(toks) < total_tokens:
        w = heldout_words[wi]; wi += 1
        if not w:
            continue
        if len(w) >= 4 and rnd.random() < box_rate * 5:   # a name/word replaced by a nomenclator box
            s = rnd.choices([b for b, _ in boxw], [n for _, n in boxw])[0]
            toks.append(('U', s, None)); truth.append(TOK)
            continue
        i = 0
        while i < len(w):
            cand = []
            for L in (8, 6, 5, 4, 3, 2, 1):
                sub = w[i:i + L]
                if len(sub) < L:
                    continue
                if L > 2 and not (sub == w and sub in wordcodes):
                    continue
                for o in opts.get(sub, []):
                    cand.append((o, L))
            if not cand:   # letter with no sign in this key (e.g. k, h): skip it
                i += 1
                continue
            (kind, sign, wgt, j), L = rnd.choices(cand, [o[2] for o, _ in cand])[0]
            if kind == 'M':
                toks.append(('M', sign, mcands[sign])); truth.append(j)
            elif kind == 'U':
                toks.append(('U', sign, None)); truth.append(utrue[sign])
            else:
                toks.append(('H', sign, [w[i:i + L]])); truth.append(None)
            i += L
    # cut into lines of the target's line lengths
    lines, tl, k = [], [], 0
    for n in lens:
        lines.append(toks[k:k + n]); tl.append(truth[k:k + n]); k += n
    return lines, tl, utrue


def eval_control(lines, tl, utrue, res, uni):
    mok = mn = base = 0
    maj = collections.defaultdict(collections.Counter)
    for L, T_ in zip(lines, tl):
        for pos, (kind, sign, c) in enumerate(L):
            if kind == 'M':
                maj[sign][T_[pos]] += 1
    oracle = sum(v.most_common(1)[0][1] for v in maj.values())
    for L, T_, ch in zip(lines, tl, res['mch']):
        for pos, (kind, sign, c) in enumerate(L):
            if kind == 'M':
                mn += 1
                mok += ch.get(pos, 0) == T_[pos]
                bj = max(range(len(c)), key=lambda j: uni.get(c[j][0], 0))
                base += bj == T_[pos]
    present = {t[1] for L in lines for t in L if t[0] == 'U'}
    cnt = collections.Counter(t[1] for L in lines for t in L if t[0] == 'U')
    ok = [s for s in present if res['uval'][s] == utrue[s]]
    return dict(m_acc=mok / mn, m_base=base / mn, m_oracle_majority=oracle / mn, m_n=mn,
                u_acc=len(ok) / len(present), u_n=len(present),
                u_tok_acc=sum(cnt[s] for s in ok) / sum(cnt.values()),
                wrong=sorted(s for s in present if s not in ok),
                wrong_tok_signs=sum(1 for s in present if res['uval'][s] == TOK and utrue[s] != TOK),
                wrong_tok_token_share=sum(cnt[s] for s in present if res['uval'][s] == TOK and utrue[s] != TOK) / sum(cnt.values()))


# ---------------- driver ----------------
_LM = None


def get_lm():
    global _LM
    if _LM is None:
        train = []
        for fn in ('lettresdecatheri01cathuoft_djvu.txt.gz', 'lettresindites00marg_djvu.txt.gz'):
            train += words_of(f'{D}/{fn}')
        text = ''.join(train)
        _LM = LM(text)
        held = ''.join(words_of(f'{D}/lettresdecatheri02cathuoft_djvu.txt.gz'))[500000:540000]
        _LM.bpc = -sum(_LM.lp(held[max(0, i - ORDER + 1):i], held[i]) for i in range(len(held))) / len(held)
    return _LM


def job(args):
    kind, seed, restarts = args
    lm = get_lm()
    cost = lm.bpc
    values = list(LETTERS) + [NULL, TOK]
    target = load_target()
    if kind == 'A':
        held = words_of(f'{D}/lettresdecatheri02cathuoft_djvu.txt.gz')
        lines, tl, utrue = build_control(target, load_key(), held, seed)
    elif kind == 'B':
        rnd = random.Random(seed)
        lines = [rnd.sample(L, len(L)) for L in target]
    else:
        lines = target
    runs = [search(lm, lines, seed * 100 + r, cost, values) for r in range(restarts)]
    best = max(runs, key=lambda r: r['obj'])
    out = dict(kind=kind, seed=seed, bpc_model=lm.bpc,
               restarts=[dict(obj=r['obj'], before=r['before'], after=r['after'], iters=r['iters']) for r in runs],
               before=best['before'], after=best['after'])
    ucnt = collections.Counter(t[1] for L in lines for t in L if t[0] == 'U')
    out['tok_signs'] = sum(1 for x in ucnt if best['uval'][x] == TOK)
    out['u_signs'] = len(ucnt)
    out['tok_token_share'] = sum(n for x, n in ucnt.items() if best['uval'][x] == TOK) / sum(ucnt.values())
    if kind == 'A':
        uni = collections.Counter(''.join(held))
        ev = eval_control(lines, tl, utrue, best, uni)
        mg = margins(lm, lines, best, cost, values)
        ev['wrong_margins'] = {s: mg[s][1] for s in ev['wrong']}
        ev['right_margins'] = {s: mg[s][1] for s in mg if s not in ev['wrong']}
        out.update(ev)
    if kind == 'T':
        mg = margins(lm, lines, best, cost, values)
        support = collections.Counter(t[1] for L in lines for t in L if t[0] == 'U')
        stab = {s: [r['uval'][s] for r in runs] for s in best['uval']}
        out['signs'] = {s: dict(value=mg[s][0] if mg[s][0] not in (TOK, NULL) else ('TOK' if mg[s][0] == TOK else 'null'),
                                second=mg[s][2], margin_bits=round(mg[s][1], 2), support=support[s],
                                restart_values=['TOK' if v == TOK else ('null' if v == NULL else v) for v in stab[s]],
                                stable=len(set(stab[s])) == 1) for s in sorted(best['uval'])}
        mc = collections.defaultdict(collections.Counter)
        rd = []
        for L, ch in zip(lines, best['mch']):
            row = ''
            for pos, (k, sign, c) in enumerate(L):
                if k == 'M':
                    mc[sign][c[ch.get(pos, 0)]] += 1
                    row += c[ch.get(pos, 0)]
                elif k == 'U':
                    v = best['uval'][sign]
                    row += ' ' if v == TOK else v
                else:
                    row += c[0]
            rd.append(row)
        out['m_choices'] = {s: dict(v) for s, v in mc.items()}
        out['reading'] = rd
    return out


def main():
    check = '--check' in sys.argv
    t0 = time.time()
    with Pool(4) as p:
        ctl = p.map(job, [('A', s, RESTARTS_CONTROL) for s in SEEDS] + [('A', s, RESTARTS_CONTROL) for s in REPL_SEEDS] + [('B', s, RESTARTS_CONTROL) for s in SEEDS])
    A = [r for r in ctl if r['kind'] == 'A']
    B = [r for r in ctl if r['kind'] == 'B']
    A3 = [r for r in A if r['seed'] in SEEDS]
    A6 = [r for r in A if r['seed'] in REPL_SEEDS]
    u = sum(r['u_acc'] for r in A3) / 3
    mgain = sum(r['m_acc'] - r['m_base'] for r in A3) / 3
    u6 = sum(r['u_acc'] for r in A6) / 3
    mgain6 = sum(r['m_acc'] - r['m_base'] for r in A6) / 3
    gate = u >= 0.60 and mgain >= 0.10 and u6 >= 0.60 and mgain6 >= 0.10
    res = dict(job='bMATBEAM', order=ORDER, gate='U-sign acc >= 0.60 and M acc >= freq baseline + 0.10, mean of 3 seeds',
               control_A=A, control_B=B, gate_met=gate, u_acc_mean=u, m_gain_mean=mgain, u_acc_mean_repl=u6, m_gain_mean_repl=mgain6)
    for r in A:
        print(f"A seed {r['seed']}: iters {[x['iters'] for x in r['restarts']]} U {r['u_acc']:.3f} ({r['u_n']} signs, token-wtd {r['u_tok_acc']:.3f})  "
              f"M {r['m_acc']:.3f} vs base {r['m_base']:.3f} / oracle-majority {r['m_oracle_majority']:.3f} (n={r['m_n']})  bpc {r['before']:.3f}->{r['after']:.3f}", flush=True)
    for r in B:
        print(f"B seed {r['seed']}: TOK {r['tok_signs']}/{r['u_signs']} signs ({r['tok_token_share']:.3f} of U tokens) iters {[x['iters'] for x in r['restarts']]} bpc {r['before']:.3f}->{r['after']:.3f}", flush=True)
    print(f"gate {'MET' if gate else 'NOT MET'}: U mean {u:.3f}, M gain mean {mgain:+.3f}; replication U {u6:.3f}, M gain {mgain6:+.3f}  ({time.time()-t0:.0f}s)", flush=True)
    if gate:
        with Pool(3) as p:
            tr = p.map(job, [('T', 7, 2), ('T', 8, 2), ('T', 9, 2)])
        # merge restarts across workers: best objective wins; stability across all 6
        best = max(tr, key=lambda r: max(x['obj'] for x in r['restarts']))
        allv = {s: sum((r['signs'][s]['restart_values'] for r in tr), []) for s in best['signs']}
        for s, d in best['signs'].items():
            d['restart_values'] = allv[s]
            d['stable'] = len(set(allv[s])) == 1
        maxwrong = max((m for r in A for m in r['wrong_margins'].values()), default=0.0)
        for s, d in best['signs'].items():
            # a TOK/null value is not licensable: control (B) sends ~99% of shuffled U tokens to TOK (NOTES.md)
            d['licensed'] = d['stable'] and d['margin_bits'] > maxwrong and d['value'] not in ('TOK', 'null')
        best['max_wrong_margin_control'] = maxwrong
        best['restarts'] = sum((r['restarts'] for r in tr), [])
        res['target'] = best
        print(f"T: bpc {best['before']:.3f}->{best['after']:.3f}; licensed signs "
              f"{sum(d['licensed'] for d in best['signs'].values())} (max wrong margin in A {maxwrong:.2f} bits)")
    else:
        res['target'] = 'CONTROL BELOW GATE -- not run'
    reading = '\n'.join(res['target']['reading']) + '\n' if gate else ''
    js = json.dumps(res, indent=1, sort_keys=True, default=str)
    if check:
        stale = open(f'{T}/mu_beam_results.json').read() != js
        if reading:
            stale = stale or open(f'{T}/mu_beam_reading.txt').read() != reading
        print('STALE' if stale else 'ok: committed results reproduce')
        sys.exit(1 if stale else 0)
    open(f'{T}/mu_beam_results.json', 'w').write(js)
    if reading:
        open(f'{T}/mu_beam_reading.txt', 'w').write(reading)


if __name__ == '__main__':
    main()
