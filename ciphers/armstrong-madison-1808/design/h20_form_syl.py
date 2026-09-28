#!/usr/bin/env python3
"""H20 (28 Sept 2026, campaign runner, owner account): syllabic PRINTED-FORM designs as positive controls.

Question (H14/H18/H19 pointed here): are the target's two design anomalies -- the 901-1099 trough and the 0/1
units-digit skew among values >= 100 -- what a syllable-spelling nomenclator on a 17x100 printed form with
modifier marks produces?  ARM-DESIGN's contiguous controls were WORD tables (WE028 vocabulary) without a
syllable inventory, without a category block, and without the marks.

Designs (1,700 cells = 17 columns x 100, values 1..1700; en18 text encoded, 60 letters of 369 groups each):
  form_alpha_cat   entries in one alphabetical run over the 1,500 ordinary cells; cells 901-1100 hold a CATEGORY
                   block (number words, ordinals, months, days, places, personal names, titles) as the reel-9
                   table shows in that region (H12: twelve 907, june 1007, friday 1016, virginia 1026, europe 917)
  form_rand_cat    same entries, random order over the ordinary cells, same category block
  form_alpha_nocat 1,700 ordinary entries alphabetical, no category block (control for the trough)
  form_rand_nocat  1,700 ordinary entries random, no category block
  form_alpha_cat_F300 / form_rand_cat_F300  as *_cat with a 300-fragment inventory instead of 600 (sensitivity)
Vocabulary: fragments = the syllable/letter entries of the two sibling tables (WE028 532 + THE972 116, deduped,
plus the 26 letters); words = the commonest en18 forms not already fragments.  Encoding per word: whole entry if
present; else the entry for the word with its grammatical suffix removed (-s/-es/-ed/-d: the printed form's rules
1-2 make plural/genitive/person/tense a MARK, not a group), with doubled letters collapsed (rule 3 makes a
doubled letter a mark under a digit); else greedy longest-prefix spelling with fragments and letters.
Statistics: design_stats.stats (the ARM-DESIGN set), target vmax 1900, forms vmax 1700.  Offline, stdlib.
  python3 h20_form_syl.py [--sims 60] [--seed 1]
"""
import argparse, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import design_stats as ds

CAT_WORDS = ("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
 "seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million "
 "first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth twentieth "
 "january february march april may june july august september october november december "
 "monday tuesday wednesday thursday friday saturday sunday "
 "london paris madrid lisbon vienna berlin petersburg amsterdam hague copenhagen stockholm naples rome milan "
 "genoa leghorn venice trieste hamburg bremen antwerp brussels bordeaux havre nantes marseilles toulon brest "
 "cadiz gibraltar malta constantinople smyrna algiers tunis tripoli tangier morocco "
 "washington philadelphia newyork boston baltimore charleston norfolk richmond virginia maryland pennsylvania "
 "massachusetts carolina georgia kentucky tennessee ohio louisiana orleans mississippi florida canada quebec "
 "halifax bermuda jamaica havanna martinique guadaloupe domingo cuba mexico vera cruz buenos ayres "
 "england britain scotland ireland france spain portugal holland germany prussia austria russia sweden denmark "
 "italy sicily sardinia switzerland turkey egypt "
 "bonaparte napoleon talleyrand champagny decres cambaceres marbois berthier murat junot fouche "
 "jefferson madison monroe pinkney erving bowdoin armstrong livingston skipwith warden barlow gallatin "
 "canning grenville fox howick percival castlereagh wellesley godoy cevallos yrujo "
 "emperor king queen prince duke marquis count baron minister ambassador consul admiral general colonel "
 "captain lieutenant bishop cardinal pope sultan dey bey pacha").split()

def build_vocab():
    we = ds.load_table(ds.US / "WE028.tsv"); the = ds.load_table(ds.US / "THE972_bourdeau.tsv")
    corp = ds.en18_words(); allw = Counter(w for f in corp for w in f)
    ents = [re.sub(r"[^a-z]", "", w) for t in (we, the) for w in t.values()]
    frags = []
    for e in ents:
        if e and (allw[e] < 3 or len(e) == 1) and e not in frags:
            frags.append(e)
    letters = [c for c in "abcdefghijklmnopqrstuvwxyz"]
    fragset = set(frags) | set(letters)
    cat = []
    for w in CAT_WORDS:
        if w not in cat: cat.append(w)
    words = [w for w, _ in allw.most_common(6000) if w not in fragset and w not in cat and len(w) > 1]
    return corp, allw, frags, letters, cat, words

class FormCode(ds.TableCode):
    SUF = ("s", "es", "ed", "d")
    def encode(self, words, rng, **kw):
        out = []
        for w in words:
            if w in self.enc:
                out.append(self.pick(self.enc[w], rng)); continue
            hit = None
            for suf in self.SUF:
                if w.endswith(suf) and len(w) > len(suf) + 2 and w[:-len(suf)] in self.enc:
                    hit = self.enc[w[:-len(suf)]]; break
                if w.endswith(suf) and len(w) > len(suf) + 2 and w[:-len(suf)] + "e" in self.enc:
                    hit = self.enc[w[:-len(suf)] + "e"]; break
            if hit is not None:
                out.append(self.pick(hit, rng)); continue
            w2 = re.sub(r"(.)\1", r"\1", w)  # doubled letters carried by the under-digit mark
            if w2 in self.enc:
                out.append(self.pick(self.enc[w2], rng)); continue
            i, seq, ok = 0, [], True
            while i < len(w2):
                for L in range(min(self.maxlen, len(w2) - i), 0, -1):
                    if w2[i:i + L] in self.enc:
                        seq.append(self.pick(self.enc[w2[i:i + L]], rng)); i += L; break
                else:
                    ok = False; break
            if ok: out.extend(seq)
            else: self.drops += 1
        return out

def make_form(rng, frags, letters, cat, words, nfrag, alpha, catblock):
    ncell = 1700
    catcells = list(range(901, 1101)) if catblock else []
    ordinary = [v for v in range(1, ncell + 1) if v not in set(catcells)]
    fr = frags[:nfrag - len(letters)] + letters
    nwords = len(ordinary) - len(fr)
    entries = fr + words[:nwords]
    if alpha: entries = sorted(entries)
    else: rng.shuffle(entries)
    table = dict(zip(ordinary, entries))
    if catblock:
        cw = cat[:len(catcells)]
        if len(cw) < len(catcells):  # pad with rare en18 forms
            cw = cw + words[nwords:nwords + len(catcells) - len(cw)]
        if alpha: cw = sorted(cw)
        else: rng.shuffle(cw)
        table.update(dict(zip(catcells, cw)))
    c = FormCode(table); c.drops = 0
    return c

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sims", type=int, default=60); ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--n", type=int, default=369)
    a = ap.parse_args()
    corp, allw, frags, letters, cat, words = build_vocab()
    print(f"vocab: fragments {len(frags)} (+26 letters), category words {len(cat)}, word pool {len(words)}")
    designs = {
        "form_alpha_cat": (600, True, True), "form_rand_cat": (600, False, True),
        "form_alpha_nocat": (600, True, False), "form_rand_nocat": (600, False, False),
        "form_alpha_cat_F300": (300, True, True), "form_rand_cat_F300": (300, False, True),
    }
    def sample_words(r, n):
        f = r.choice(corp); i = r.randrange(0, len(f) - n); return f[i:i + n]
    tgt = ds.target_tokens(); T = ds.stats(tgt, random.Random(7), 1900)
    sims = defaultdict(list); drops = defaultdict(list); spell = defaultdict(list); catuse = defaultdict(list)
    for name, (nfrag, alpha, catb) in designs.items():
        for i in range(a.sims):
            r = random.Random(a.seed * 1000 + i)
            code = make_form(r, frags, letters, cat, words, nfrag, alpha, catb)
            ws = sample_words(r, a.n * 2)
            toks = code.encode(ws, r)[:a.n]
            drops[name].append(code.drops)
            # share of groups that are fragments (spelling) and that land in the category block
            fragvals = {v for v, w in code.enc.items() for v in w} if False else None
            inv = {v: w for w, vs in code.enc.items() for v in vs}
            fs = set(frags[:nfrag - 26] + letters)
            spell[name].append(sum(1 for t in toks if inv.get(t) in fs) / len(toks))
            catuse[name].append(sum(1 for t in toks if 901 <= t <= 1100) / len(toks))
            sims[name].append(ds.stats(toks, random.Random(i), 1700))
    KEYS = ["D/N", "low_share", "low_distinct", "hi_distinct", "units_top1", "units_top2", "units_H",
            "units_digit0_share", "decade_units_z", "block_trough", "block_pair_min", "digit_order_rho",
            "digits23_share", "top10_share", "onepart_dist"]
    with open(HERE / "h20_stats_sim.tsv", "w") as f:
        f.write("design\tstat\tmean\tsd\tp05\tp50\tp95\ttarget\ttarget_percentile\n")
        for name, lst in sims.items():
            for k in KEYS:
                xs = sorted(s[k] for s in lst if s[k] == s[k])
                mu = sum(xs) / len(xs); sd = (sum((x - mu) ** 2 for x in xs) / len(xs)) ** 0.5
                q = lambda p: xs[min(len(xs) - 1, int(p * len(xs)))]
                tv = T[k]; pct = 100 * sum(1 for x in xs if x < tv) / len(xs) + 50 * sum(1 for x in xs if x == tv) / len(xs)
                f.write(f"{name}\t{k}\t{mu:.3f}\t{sd:.3f}\t{ds.fmt(q(.05))}\t{ds.fmt(q(.5))}\t{ds.fmt(q(.95))}\t{ds.fmt(tv)}\t{pct:.0f}\n")
    print("stat".ljust(20) + "target".rjust(9) + "".join(n[:17].rjust(18) for n in designs))
    for k in KEYS:
        row = k.ljust(20) + ds.fmt(T[k]).rjust(9)
        for name in designs:
            xs = [s[k] for s in sims[name] if s[k] == s[k]]; mu = sum(xs) / len(xs)
            pct = 100 * sum(1 for x in xs if x < T[k]) / len(xs)
            row += f"{mu:8.3f} (p{pct:3.0f})".rjust(18)
        print(row)
    for name in designs:
        print(f"{name}: OOV drops/letter {sum(drops[name])/len(drops[name]):.1f}; spelled-fragment share {sum(spell[name])/len(spell[name]):.3f}; "
              f"share of groups in 901-1100 {sum(catuse[name])/len(catuse[name]):.3f} (target {sum(1 for t in tgt if 901<=t<=1100)/len(tgt):.3f})")

if __name__ == "__main__":
    main()
