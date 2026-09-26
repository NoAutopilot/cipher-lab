#!/usr/bin/env python3
"""design_prior.py: predict the design family of an unread ciphertext from its sign statistics, before an attack
is chosen, by comparing it with every key on file (KEY-DESIGN.tsv, tools/key_design.py).

OPTIMIZATION-2026-09-26.md section (d), KEY-DESIGN (26 Sept 2026): "a's structure narrows b's hypothesis", made
mechanical. No learned model: a distance on five token statistics, a shuffled control, stated thresholds.

  python3 tools/design_prior.py CIPHERTEXT [CIPHERTEXT ...]   print a verdict per ciphertext
  python3 tools/design_prior.py --calibrate                   rank the true family of every verified pair
                                                              (key_crossmatch.VERIFIED_PAIRS), write
                                                              KEY-DESIGN-CAL.tsv
  python3 tools/design_prior.py --unkeyed                     every ciphertext in an open/partial folder that no
                                                              usable key claims as its own text; write
                                                              KEY-DESIGN-PRIORS.tsv
  options: --draws 200 (shuffled-control draws), --seed 0, --no-write

Method.
 1. Statistics of a token stream at length N (the target's own length): type-token ratio K/N, singleton share
    (types seen once / K), top-10 share (tokens in the 10 commonest types / N), top-1 share, log index of
    coincidence. All five are label-free: they depend on the frequency profile, not on what the signs are.
 2. References, one per distinct key (duplicates in KEY-DESIGN.tsv's duplicate_of dropped): the key's own
    ciphertext when it has at least N tokens (mean over up to 5 evenly spaced windows of N); otherwise a
    synthetic text of the same N enciphered with that key from its language's corpus in tools/data
    (whole-word codes first, then the longest syllable value, then a letter; homophones uniform; nulls at 5%
    when the table declares any). A table that cannot spell at least half the corpus letters gets no
    synthetic reference (too partial). The `source` field says which (real/synthetic).
 3. Two tiers. The operative tier scores DESIGN CLASSES: letter-for-letter (alphabet substitution), multi-sign
    (homophonic, nomenclator and syllabary tables together), code, mixed (a partial table). The fine tier ranks
    KEY-DESIGN.tsv's six families and is printed as advisory only: calibration shows these statistics do not
    separate homophonic from nomenclator from syllabary (KEY-DESIGN-CAL.tsv).
    Distance: RMS of the per-statistic differences, each scaled by that statistic's spread (standard
    deviation) over all references at this N. Family distance = the nearest reference of that family.
 4. Envelope of a family at this N: for each member, its distance to the nearest member of the same family in
    another folder; the envelope is the 90th percentile of those (the largest when fewer than 10 members). A
    family needs members in at least two folders to have an envelope.
 5. Shuffled control, 200 draws: every token relabelled independently at random from the target's own sign
    inventory (uniform, with replacement). A bijective relabelling (a one-to-one renaming of the signs) is NOT
    used as the control: every statistic here is label-free, so it would return the target's own distances
    exactly and could never fail differently from the target (CLAUDE.md rule 3, the bCAS/AX-5799 non-test);
    the tool checks that invariance once per target instead and prints it.
 6. Verdict per family: `plausible` when the family distance is inside the family's envelope AND below the
    5th percentile of the same distance over the shuffled draws; `excluded` when it is outside the envelope;
    `not above null` when inside the envelope but not below the null's 5th percentile; `no reference` when the
    family has no envelope at this N. The false-positive rate is the share of shuffled draws that would
    themselves be called plausible for any family.
 A well-flattened homophonic text is itself close to the uniform null (that is what homophones are for), so
 the multi-sign class often reads `not above null` rather than `plausible` on such a text; it is not excluded,
 and the ranking, not the null test, carries the information there.
 This licenses a design hypothesis to test first, never a reading and never a key.
"""
import argparse
import hashlib
import math
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
import key_crossmatch as kx  # noqa: E402
import key_design as kd  # noqa: E402

ROOT = TOOLS.parent
PRIORS = ROOT / 'KEY-DESIGN-PRIORS.tsv'
CAL = ROOT / 'KEY-DESIGN-CAL.tsv'
FAMILIES = ['alphabet substitution', 'homophonic', 'nomenclator', 'syllabary', 'code numbers', 'mixed',
            'letter-for-letter', 'multi-sign (homophonic/nomenclator/syllabary)', 'code', 'mixed (partial table)']
SYN_LEN = 6200          # synthetic stream length (longest ciphertext on disk is dupuy452-carpi's 6132)
MIN_TOKENS = 30         # below this the statistics are not computed
OFFICE_STOP = {'secretaire', 'etat', 'affaires', 'etrangeres', 'office', 'chancery', 'correspondence', 'court',
               'crown', 'french', 'english', 'dutch', 'spanish', 'diplomatic', 'embassy', 'network', 'with',
               'from', 'same', 'folder', 'household', 'secretariat', 'letters', 'letter', 'cipher', 'king',
               'mission', 'resident', 'ambassador', 'agent', 'principal', 'secretary', 'state', 'orange'}
LANG_FALLBACK = {'sv': 'de', 'en16': 'en', '?': 'fr', '': 'fr'}


# ------------------------------------------------------------------ statistics

def features(signs):
    s = kd.ct_stats(signs)
    return [s['ttr'], s['singleton'], s['top10'], s['top'], math.log(max(s['ioc'], 1e-5))]


def window_features(signs, n):
    L = len(signs)
    if L < n:
        return None
    if L == n:
        return features(signs)
    k = min(5, 1 + (L - n) // max(1, n // 2))
    starts = [round(i * (L - n) / max(1, k - 1)) for i in range(k)] if k > 1 else [0]
    fs = [features(signs[s:s + n]) for s in starts]
    return [sum(col) / len(col) for col in zip(*fs)]


# ------------------------------------------------------------------ synthetic references

_CORPUS = {}


def corpus_words(lang):
    lang = LANG_FALLBACK.get(lang, lang)
    if lang not in _CORPUS:
        files = kx.BUILTIN_LANG_CORPORA.get(lang) or sorted((kx.DATA / f'{lang}_repo').glob('*.txt')) \
            or sorted((kx.DATA / f'{lang}20').glob('*.txt')) or kx.BUILTIN_LANG_CORPORA['fr']
        text = ''
        for f in files:
            text += Path(f).read_text(encoding='utf-8', errors='replace')[:120000] + '\n'
        _CORPUS[lang] = re.findall(r'[a-z]+', kd.fold(text).lower())
    return _CORPUS[lang]


SUBST = {'j': 'i', 'v': 'u', 'u': 'v', 'w': 'u', 'k': 'c', 'y': 'i', 'z': 's', 'q': 'c', 'i': 'j'}


def synthesize(key, lang, seed, n=SYN_LEN):
    """(signs, dropped_letter_share) -- corpus text enciphered with this key table, or (None, share)."""
    all_caps = False
    letter, piece, word, nulls = defaultdict(list), defaultdict(list), defaultdict(list), []
    for code, v in key.items():
        c, norm = kd.classify_value(v, all_caps)
        if c == 'letter':
            letter[norm].append(code)
        elif c == 'short':
            piece[norm].append(code); word[norm].append(code)
        elif c in ('word', 'name'):
            word[norm].append(code)
        elif c == 'null':
            nulls.append(code)
    if not letter and not piece:
        return None, 1.0
    rnd = random.Random(seed)
    words = corpus_words(lang)
    start = rnd.randrange(max(1, len(words) - 40000))
    out, seen, dropped = [], 0, 0
    i = start
    while len(out) < n and i < len(words) + start + 200000:
        w = words[i % len(words)]
        i += 1
        if nulls and rnd.random() < 0.05:
            out.append(rnd.choice(nulls))
        if w in word and (len(w) > 3 or rnd.random() < 0.5):
            out.append(rnd.choice(word[w]))
            seen += len(w)
            continue
        j = 0
        while j < len(w):
            for L in (3, 2):
                if j + L <= len(w) and w[j:j + L] in piece:
                    out.append(rnd.choice(piece[w[j:j + L]])); seen += L; j += L
                    break
            else:
                ch = w[j]
                codes = letter.get(ch) or letter.get(SUBST.get(ch, ''))
                seen += 1
                if codes:
                    out.append(rnd.choice(codes))
                else:
                    dropped += 1
                j += 1
    share = dropped / max(1, seen)
    if share > 0.5 or len(out) < n:
        return None, share
    return out[:n], share


# ------------------------------------------------------------------ references

class Refs:
    def __init__(self):
        rows = kd.build(with_signs=True)
        self.rows = [r for r in rows if r.get('usable') == 'yes']
        self.by_path = {r['key_path']: r for r in self.rows}
        self.canon = {r['key_path']: (r.get('duplicate_of') or r['key_path']) for r in self.rows}
        self.refs = [r for r in self.rows if not r.get('duplicate_of')]
        self._syn = {}

    def synthetic(self, r, n=SYN_LEN):
        want = max(SYN_LEN, n)
        cur = self._syn.get(r['key_path'])
        if cur is None or (cur[0] is not None and len(cur[0]) < want) or (cur[0] is None and cur[2] < want):
            seed = int(hashlib.sha1(r['key_path'].encode()).hexdigest()[:8], 16)
            syn, share = synthesize(r['_key'], r.get('language', 'fr'), seed, want)
            self._syn[r['key_path']] = (syn, share, want)
        return self._syn[r['key_path']][:2]

    def at(self, n, leave_folder=None, leave_canon=None):
        """[(row, source, feature_vector)] for every reference usable at length n."""
        out = []
        for r in self.refs:
            if leave_folder and r['_folder'] == leave_folder:
                continue
            if leave_canon and self.canon[r['key_path']] == leave_canon:
                continue
            f = window_features(r['_signs'], n) if r['_signs'] else None
            src = 'real'
            if f is None:
                syn, _ = self.synthetic(r, n)
                if syn is None or len(syn) < n:
                    continue
                f, src = window_features(syn, n), 'synthetic'
            out.append((r, src, f))
        return out


def scales(vecs):
    sc = []
    for col in zip(*vecs):
        m = sum(col) / len(col)
        sd = math.sqrt(sum((x - m) ** 2 for x in col) / max(1, len(col) - 1))
        sc.append(sd if sd > 1e-9 else 1.0)
    return sc


def dist(a, b, sc):
    return math.sqrt(sum(((x - y) / s) ** 2 for x, y, s in zip(a, b, sc)) / len(sc))


def envelopes(refs, sc):
    env = {}
    for fam in {fam_of(r) for r, _, _ in refs}:
        mem = [(r, f) for r, _, f in refs if fam_of(r) == fam]
        if len({r['_folder'] for r, _ in mem}) < 2:
            continue
        dmins = []
        for r, f in mem:
            ds = sorted(dist(f, g, sc) for s, g in mem if s['_folder'] != r['_folder'])[:AGG_K]
            dmins.append(sum(ds) / len(ds))
        dmins.sort()
        env[fam] = dmins[-1] if len(dmins) < 10 else dmins[math.ceil(0.9 * len(dmins)) - 1]
    return env


AGG_K = 3   # family distance = mean of the K nearest members (min would favour the families with most members)
EXCLUDE_RATIO = 2.0   # excluded = outside the envelope AND > 2x the best class's distance (fitted on
                      # KEY-DESIGN-CAL: the envelope alone excluded the true class in 8 of 29 verified pairs)
SKIP = '_skip'
MULTI = 'multi-sign (homophonic/nomenclator/syllabary)'
COARSE = {'alphabet substitution': 'letter-for-letter', 'homophonic': MULTI, 'nomenclator': MULTI,
          'syllabary': MULTI, 'code numbers': 'code', 'mixed': 'mixed (partial table)'}
MERGE = dict(COARSE)  # family relabelling applied to references, e.g. {'nomenclator': 'homophonic'}; set by --coarse


def fam_of(r):
    return MERGE.get(r['design_family'], r['design_family'])


def family_distances(f, refs, sc):
    per = defaultdict(list)
    for r, _, g in refs:
        per[fam_of(r)].append(dist(f, g, sc))
    return {fam: sum(sorted(v)[:AGG_K]) / len(sorted(v)[:AGG_K]) for fam, v in per.items()}


def inventory(signs):
    st = kx.sign_type(signs)
    if st == 'symbols' or (st == 'mixed' and sum(bool(re.search(r'[^\x00-\x7f]|[a-z]-[a-z]', s)) for s in signs) > len(signs) / 3):
        st = 'glyphs'
    return st


def numeral_overlap(signs, row):
    nums = [int(s) for s in signs if re.fullmatch(r'\d+', s)]
    if not nums or row.get('numeral_min', '') == '':
        return ''
    lo, hi = min(nums), max(nums)
    klo, khi = int(row['numeral_min']), int(row['numeral_max'])
    inside = sum(1 for x in nums if klo <= x <= khi) / len(nums)
    return f'{inside:.2f}'


def name_tokens(text):
    return {w for w in re.findall(r'[a-z]{4,}', kd.fold(text or '').lower()) if w not in OFFICE_STOP}


# ------------------------------------------------------------------ the verdict

def prior(signs, R, draws=200, seed=0, leave_folder=None, leave_canon=None):
    n = len(signs)
    res = dict(n=n, k=len(set(signs)), inventory=inventory(signs))
    if n < MIN_TOKENS:
        res['note'] = f'short: {n} tokens < {MIN_TOKENS}, no statistics'
        return res
    refs = [t for t in R.at(n, leave_folder, leave_canon) if fam_of(t[0]) != SKIP]
    fams = [f for f in FAMILIES + sorted({fam_of(t[0]) for t in refs}) if f in {fam_of(t[0]) for t in refs}]
    fams = list(dict.fromkeys(fams))
    sc = scales([f for _, _, f in refs])
    env = envelopes(refs, sc)
    ft = features(signs)
    dfam = family_distances(ft, refs, sc)
    # invariance check: a bijective relabelling gives identical statistics (why it is not the control)
    rnd = random.Random(seed)
    types = sorted(set(signs))
    perm = dict(zip(types, rnd.sample(types, len(types))))
    res['relabel_invariant'] = features([perm[s] for s in signs]) == ft
    null = defaultdict(list)
    null_feats = []
    for _ in range(draws):
        g = features([rnd.choice(types) for _ in range(n)])
        null_feats.append(g)
        for fam, x in family_distances(g, refs, sc).items():
            null[fam].append(x)
    p05 = {fam: sorted(v)[max(0, int(0.05 * len(v)) - 1)] for fam, v in null.items()}

    def verdict(dd):
        out = {}
        best = min(dd.values()) if dd else 0.0
        for fam in fams:
            if fam not in env or fam not in dd:
                out[fam] = 'no reference'
            elif dd[fam] > env[fam] and dd[fam] > EXCLUDE_RATIO * best:
                out[fam] = 'excluded'
            elif dd[fam] < p05[fam]:
                out[fam] = 'plausible'
            else:
                out[fam] = 'not above null'
        return out
    v = verdict(dfam)
    fp = sum(1 for g in null_feats if 'plausible' in verdict(family_distances(g, refs, sc)).values())
    ranked = sorted(dfam.items(), key=lambda kv: kv[1])
    near = sorted(((dist(ft, f, sc), r, src) for r, src, f in refs), key=lambda t: t[0])[:3]
    clusters = defaultdict(lambda: 1e9)
    for r, src, f in refs:
        key = (r.get('office', '?')[:70], r.get('decade', '?'))
        clusters[key] = min(clusters[key], dist(ft, f, sc))
    res.update(families=fams, ranking=ranked, verdict=v, envelope=env, null_p05=p05, fp=fp / draws, n_refs=len(refs),
               nearest=[(d, r, src) for d, r, src in near],
               clusters=sorted(clusters.items(), key=lambda kv: kv[1])[:3])
    return res


def fmt_ranking(res):
    return '; '.join(f'{fam}={d:.2f}' for fam, d in res.get('ranking', []))


def fmt_near(res, signs):
    out = []
    for d, r, src in res.get('nearest', []):
        form = r.get('sign_inventory', '')
        ov = numeral_overlap(signs, r)
        out.append(f"{r['key_path']} [{r['design_family']}; {r.get('office', '?')[:60]}; {r.get('years', '?')[:20]}; "
                   f"d={d:.2f}; {src}; inv={form}{'; num_in_range=' + ov if ov else ''}]")
    return ' || '.join(out)


# ------------------------------------------------------------------ calibration

def set_mode(mode):
    """'class' (the calibrated, operative tier) or 'family' (the fine tier, advisory)."""
    MERGE.clear()
    if mode == 'class':
        MERGE.update(COARSE)


def calibrate(R, draws, seed, write=True):
    """Both tiers for every verified/print pair; returns {mode: (ok, tot, chance, fp_mean)} and the TSV text."""
    per = {}
    summary = {}
    for mode in ('class', 'family'):
        set_mode(mode)
        ok = tot = false_excl = 0
        chance, fps = [], []
        for kp, cp, tier, why in kx.VERIFIED_PAIRS:
            row = R.by_path.get(kp)
            ctp = ROOT / cp
            base = per.setdefault((kp, cp), dict(tier=tier, key_path=kp, ciphertext_path=cp))
            if row is None or not ctp.exists():
                base['note'] = 'key not usable in KEY-DESIGN.tsv' if row is None else 'no ciphertext'
                continue
            signs = kx.tokenize_ciphertext(ctp)[0]
            base['n_tokens'] = len(signs)
            true = fam_of(row)
            base[f'true_{mode}'] = true
            res = prior(signs, R, draws, seed, leave_folder=kx.folder_of(ctp), leave_canon=R.canon[kp])
            if 'ranking' not in res:
                base['note'] = res.get('note', '')
                continue
            fams = [f for f, _ in res['ranking']]
            rank = fams.index(true) + 1 if true in fams else ''
            base[f'{mode}_rank'] = rank
            base[f'{mode}_ranking'] = fmt_ranking(res)
            if rank:
                tot += 1
                ok += rank <= 2
                chance.append(min(1.0, 2 / len(fams)))
                fps.append(res['fp'])
                base[f'{mode}_verdict'] = res['verdict'][true]
                false_excl += res['verdict'][true] == 'excluded'
            else:
                base[f'{mode}_verdict'] = f'no out-of-folder reference of {true}'
        summary[mode] = (ok, tot, sum(chance), sum(fps) / len(fps) if fps else 0.0, false_excl)
    set_mode('class')
    oc, tc, cc, fc, xc = summary['class']
    of, tf, cf, ff, xf = summary['family']
    head = (f'# KEY-DESIGN-CAL.tsv -- tools/design_prior.py --calibrate, leave-folder-out, duplicates of the true key '
            f'dropped, {draws} shuffled draws per pair. DESIGN CLASS (operative): true class in the top two for {oc} of '
            f'{tc} rankable pairs (chance {cc:.1f} of {tc}); shuffled-input false-positive rate {fc:.3f} (mean share of '
            f'draws called plausible for any class); true class wrongly excluded in {xc} of {tc}. FINE FAMILY (advisory, '
            f'fails the top-two bar): {of} of {tf} (chance {cf:.1f}); fp {ff:.3f}; wrongly excluded {xf}. Frequency statistics do not separate homophonic, nomenclator and '
            f'syllabary tables from each other.\n')
    cols = ['tier', 'key_path', 'ciphertext_path', 'n_tokens', 'true_class', 'class_rank', 'class_verdict',
            'class_ranking', 'true_family', 'family_rank', 'family_ranking', 'note']
    text = head + '\t'.join(cols) + '\n' + ''.join('\t'.join(str(r.get(c, '')) for c in cols) + '\n'
                                                   for r in per.values())
    if write:
        CAL.write_text(text, encoding='utf-8')
    return summary, text


# ------------------------------------------------------------------ unkeyed sweep

def unkeyed_targets(R):
    claimed = set()
    for r in R.rows:
        claimed.update(p for p in (r.get('own_ciphertexts') or '').split(';') if p)
    cts, _ = kx.find_ciphertext_files()
    out = []
    for p in cts:
        rel = str(p.relative_to(ROOT))
        folder = kx.folder_of(p)
        status, office, years, _ = kx.notes_meta(folder)
        if status in ('open', 'partial') and rel not in claimed:
            out.append((p, rel, folder, status, office, years))
    return out


def sweep(R, draws, seed, write=True):
    cols = ['ciphertext_path', 'folder', 'status', 'decade', 'n_tokens', 'distinct', 'inventory', 'plausible',
            'excluded', 'not_above_null', 'class_ranking', 'family_ranking_advisory', 'fp_rate', 'nearest_keys', 'nearest_office_decade',
            'same_office_decade_lead', 'note']
    lines, leads = [], []
    for p, rel, folder, status, office, years in unkeyed_targets(R):
        signs = kx.tokenize_ciphertext(p)[0]
        set_mode('family')
        fine = prior(signs, R, 20, seed)
        set_mode('class')
        res = prior(signs, R, draws, seed)
        decade = kd.decade_of(years, folder)
        row = dict(ciphertext_path=rel, folder=folder, status=status, decade=decade, n_tokens=len(signs),
                   distinct=len(set(signs)), inventory=res['inventory'], note=res.get('note', ''))
        if 'ranking' in res:
            v = res['verdict']
            F = res['families']
            row.update(plausible=','.join(f for f in F if v[f] == 'plausible'),
                       excluded=','.join(f for f in F if v[f] == 'excluded'),
                       not_above_null=','.join(f for f in F if v[f] == 'not above null'),
                       class_ranking=fmt_ranking(res), family_ranking_advisory=fmt_ranking(fine), fp_rate=f"{res['fp']:.3f}", nearest_keys=fmt_near(res, signs),
                       nearest_office_decade=' || '.join(f'{o} ({dec}) d={d:.2f}' for (o, dec), d in res['clusters']))
            tgt_names = name_tokens(office + ' ' + folder.replace('-', ' '))
            lead = []
            for d, r, src in res['nearest']:
                same_office = r['_folder'] == folder or bool(
                    tgt_names & name_tokens(r.get('office', '') + ' ' + r.get('correspondents', '') + ' ' + r['_folder'].replace('-', ' ')))
                if same_office and r.get('decade') == decade and decade != '?' and r.get('sign_inventory') == res['inventory']:
                    where = 'same folder' if r['_folder'] == folder else 'cross-folder'
                    lead.append(f"{where}: {r['key_path']} (d={d:.2f}, {r['design_family']})")
            if lead:
                row['same_office_decade_lead'] = lead[0]
                leads.append((rel, lead[0], row['plausible']))
        lines.append(row)
    head = ('# KEY-DESIGN-PRIORS.tsv -- tools/design_prior.py --unkeyed: every ciphertext in an open/partial folder that '
            'no usable key claims as its own text. A design prior to choose the first attack family, never a reading. '
            'Lead = nearest key in the same office (shared name or folder), same decade, same sign inventory.\n')
    text = head + '\t'.join(cols) + '\n' + ''.join('\t'.join(str(r.get(c, '')) for c in cols) + '\n' for r in lines)
    if write:
        PRIORS.write_text(text, encoding='utf-8')
    return lines, leads


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('ciphertexts', nargs='*')
    ap.add_argument('--calibrate', action='store_true')
    ap.add_argument('--unkeyed', action='store_true')
    ap.add_argument('--draws', type=int, default=200)
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--no-write', action='store_true')
    a = ap.parse_args(argv)
    R = Refs()
    if a.calibrate:
        summary, text = calibrate(R, a.draws, a.seed, not a.no_write)
        print(text)
    if a.unkeyed:
        lines, leads = sweep(R, a.draws, a.seed, not a.no_write)
        print(f'{len(lines)} unkeyed ciphertexts scored; {len(leads)} same-office-decade leads')
        for rel, lead, pl in leads:
            print(f'  lead: {rel} -> {lead}; plausible: {pl or "-"}')
    for c in a.ciphertexts:
        p = Path(c) if Path(c).is_absolute() else ROOT / c
        signs = kx.tokenize_ciphertext(p)[0]
        res = prior(signs, R, a.draws, a.seed)
        print(f'{c}: {res["n"]} tokens, {res["k"]} distinct, inventory {res["inventory"]}')
        if 'ranking' not in res:
            print('  ' + res.get('note', ''))
            continue
        print(f'  relabel-invariant statistics: {res["relabel_invariant"]}; references at this N: {res["n_refs"]}')
        for fam, d in res['ranking']:
            env = res['envelope'].get(fam)
            print(f'  {fam:22s} d={d:.2f} envelope={env if env is None else round(env, 2)} '
                  f'null_p05={res["null_p05"].get(fam, 0):.2f} -> {res["verdict"][fam]}')
        print(f'  shuffled-input false-positive rate: {res["fp"]:.3f}')
        set_mode('family')
        print('  fine family ranking (advisory, not calibrated): ' + fmt_ranking(prior(signs, R, 20, a.seed)))
        set_mode('class')
        print('  nearest keys: ' + fmt_near(res, signs))
    return 0


if __name__ == '__main__':
    sys.exit(main())
