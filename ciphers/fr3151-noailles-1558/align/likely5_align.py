#!/usr/bin/env python3
"""LIKELY-5 (2 Oct 2026, account-4): marginal-gloss -> cipher alignment for fr3151-noailles-1558, with its controls.

Design (pre-registered before the first run; see NOTES.md "## LIKELY-5"):
  * one (gloss, cipher) pair per BLOCK, not per line: the two gloss crops viewed this session show the margin
    gloss wrapping on its own line widths (gloss3 is running French prose, 7 margin lines beside 6 cipher lines),
    so a line-to-line pairing (the NX-3151G design, 26 Sept) has no physical basis.  The cipher lines of a block
    are concatenated in order; the surviving gloss words are concatenated in order.
  * tools/interlinear_align.py DP/hard-EM, symbol signs as surrogate codes 1..99 (below --floor 100: one letter
    or null), numerals as 100+n (word/syllable codes, one or more letters).  No prior, no cryptanalysis.
  * statistic per run: consistency = (sum over codes with >=2 aligned occurrences of the top chunk's count) /
    (their total aligned occurrences); and n_cons = codes with >=3 occurrences agreeing on >=2/3 of them.
    Both CAN differ between the true gloss and a shuffled one (rule 3: the control can fail differently).
  * controls, each with the same statistic: (a) shuffled-gloss: the gloss WORDS permuted, 200 permutations;
    (b) shuffled cipher-line order within the block, 100 permutations.  Gate (pre-registered): target
    consistency > control (a) p95 AND n_cons >= 5.  Only then key.tsv -> decode_key -> judge fr16.
  * matched positive control (rule 3): synthetic French (fr16 corpus) blocks of the SAME sign counts (83/65/158),
    homophonic symbol cipher (25 symbols over the 20 commonest letters, 8% nulls) with the gloss cut the way the
    real one is: block-1 shape = the last 41% of each line's plaintext survives the gutter; block-3 shape = 55% of
    the words legible, order kept.  5 seeds each, each vs 100 word-shuffles.  If the positive control does not
    beat its own shuffle p95, a miss on the target is a non-test at this N and gloss coverage, not a negative.
"""
import csv, gzip, random, re, sys
from collections import Counter, defaultdict
sys.path.insert(0, '/home/user/cipher-lab/tools')
import interlinear_align as ia

HERE = '/home/user/cipher-lab/ciphers/fr3151-noailles-1558/align/'
BLOCKS = {1: 'ciphertext_draft_block1.tsv', 2: 'ciphertext_draft_block2.tsv', 3: 'ciphertext_draft_block3.tsv'}

# Gloss witnesses (grade M throughout; [..] = lost to the binding, [?] = unsure; only words read are used).
GLOSS = {
    # gloss1: this worker's own read of margin_gloss1_zoom.jpg (2 Oct) agrees with NX-3151G's subagent on lines 1-2;
    # line 3's last word is unresolved (iustice / duction / affaires): 'iustice' used, as the on-disk witness has it.
    (1, 'subagent+worker'): "en mauluaise gouuernement de que iustice",
    # gloss2: NX-3151G subagent fragments only, each low confidence (the crop is the worst of the three).
    (2, 'subagent'): "Loysanne fue liege gaur moy de la pallis",
    # gloss3, witness A: NX-3151G subagent read (align/gloss_read_subagent.md), [?]/[..] stripped.
    (3, 'subagent'): "a mre a chiffre auec le Sr Chef a prou prest a me chascune chose stoffee de mo p a Hyai baucy a",
    # gloss3, witness B: this worker's own read of margin_gloss3_zoom.jpg, 2 Oct 2026 (vision call 2 of 2).
    (3, 'worker'): "Mais ie me doubte que le Sr Che a sur a prou fait ch oue une allee ssee le me nuieuure pour et",
}


def load_block(n):
    lines = defaultdict(list)
    with open(HERE + BLOCKS[n]) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            lines[r['line']].append(r['sign'])
    return [lines[k] for k in sorted(lines)]


def surrogates(all_lines):
    sym = {}
    for ln in all_lines:
        for t in ln:
            if t.isdigit():
                continue
            if t not in sym:
                sym[t] = len(sym) + 1
    assert len(sym) < 99
    return sym


def encode(lines, sym):
    return [' '.join(str(100 + int(t)) if t.isdigit() else str(sym[t]) for t in ln) for ln in lines]


def stat(counts):
    tot = top = 0
    ncons = 0
    for val, cnt in counts.items():
        n = sum(cnt.values())
        if n < 2:
            continue
        t = ia.top_of(cnt)[1]
        tot += n
        top += t
        if n >= 3 and t * 3 >= 2 * n:
            ncons += 1
    return (top / tot if tot else 0.0), ncons


def run(plain, cipher_lines):
    pairs = [{'plain_line': 'g', 'plain_raw': plain, 'cipher_line': 'c', 'cipher_raw': ' '.join(cipher_lines)}]
    _, _, counts, _ = ia.run_align(pairs, floor=100)
    return stat(counts), counts


def controls(plain, cipher_lines, rng, n_word=200, n_line=100):
    words = plain.split()
    a = []
    for _ in range(n_word):
        w = words[:]
        rng.shuffle(w)
        a.append(run(' '.join(w), cipher_lines)[0])
    b = []
    for _ in range(n_line):
        c = cipher_lines[:]
        rng.shuffle(c)
        b.append(run(plain, c)[0])
    return a, b


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def report(label, real, a, b=None):
    ca = [x[0] for x in a]
    na = [x[1] for x in a]
    line = (f"{label}: consistency {real[0]:.3f} (n_cons {real[1]}) | shuffled-gloss n={len(a)} mean {sum(ca)/len(ca):.3f} "
            f"p95 {pct(ca, 0.95):.3f} max {max(ca):.3f}, n_cons mean {sum(na)/len(na):.2f} max {max(na)}")
    if b:
        cb = [x[0] for x in b]
        line += f" | shuffled-lines n={len(b)} mean {sum(cb)/len(cb):.3f} p95 {pct(cb, 0.95):.3f}"
    gate = real[0] > pct(ca, 0.95) and real[1] >= 5
    print(line + f" -> {'CLEARS' if gate else 'does not clear'} gate")
    return gate


# ---------- synthetic positive control ----------
def french_text(nletters, rng):
    with gzip.open('/home/user/cipher-lab/tools/data/fr16/lettresdecatheri01cathuoft_djvu.txt.gz', 'rt', errors='ignore') as f:
        txt = f.read()
    words = re.findall(r"[a-zàâäéèêëîïôöùûüç]+", txt.lower())
    words = [re.sub(r'[^a-z]', lambda m: {'à':'a','â':'a','ä':'a','é':'e','è':'e','ê':'e','ë':'e','î':'i','ï':'i','ô':'o','ö':'o','ù':'u','û':'u','ü':'u','ç':'c'}.get(m.group(0), ''), w) for w in words[20000:]]
    words = [w for w in words if w]
    start = rng.randrange(0, len(words) - 2000)
    out, n = [], 0
    while n < nletters:
        out.append(words[start]); n += len(words[start]); start += 1
    return out


def synth_block(line_counts, shape, rng):
    """Returns (gloss_text, cipher_lines) for a block of the given per-line sign counts."""
    nsigns = sum(line_counts)
    words = french_text(int(nsigns * 0.92) + 5, rng)
    letters = ''.join(words)
    freq = Counter(letters)
    top20 = [l for l, _ in freq.most_common(20)]
    key = defaultdict(list)
    syms = list(range(1, 26))
    rng.shuffle(syms)
    for i, l in enumerate(top20):
        key[l].append(syms[i])
    for s in syms[20:]:  # 5 extra homophones for the 5 commonest letters
        key[top20[syms.index(s) % 5]].append(s)
    null = 99
    # encipher letter stream, drop letters without a key (rare), insert 8% nulls, then cut into the real line counts
    stream = []
    for l in letters:
        if l in key:
            stream.append(key[l][rng.randrange(len(key[l]))])
            if rng.random() < 0.08:
                stream.append(null)
    stream = stream[:nsigns]
    lines, pos = [], 0
    for c in line_counts:
        lines.append(' '.join(str(x) for x in stream[pos:pos + c])); pos += c
    # the plaintext actually enciphered (letters with a key, up to what fitted)
    plain_used = ''.join(l for l in letters if l in key)
    # approximate letters per line proportional to signs
    wl = []
    if shape == 'tail41':
        # per line, keep the last 41% of that line's share of the plaintext, as whole words where possible
        total = len(plain_used)
        cuts, acc = [], 0
        for c in line_counts:
            acc += c
            cuts.append(int(total * acc / nsigns))
        prev = 0
        for cut in cuts:
            seg = plain_used[prev:cut]; prev = cut
            keep = seg[int(len(seg) * 0.59):]
            wl.append(keep)
        gloss = ' '.join(wl)
    else:  # words55: 55% of the words legible, order kept
        used, n = [], 0
        for w in words:
            if n >= len(plain_used):
                break
            used.append(w); n += len(w)
        gloss = ' '.join(w for w in used if rng.random() < 0.55)
    return gloss, lines


def positive_controls(rng):
    print("\n== matched positive control (synthetic French, homophonic symbols, same sign counts) ==")
    for shape, counts in (('tail41', [26, 33, 24]), ('words55', [8, 27, 33, 24, 24, 25, 17])):
        wins = 0
        for seed in range(5):
            r = random.Random(1000 + seed)
            gloss, lines = synth_block(counts, shape, r)
            real, _ = run(gloss, lines)
            a, _ = controls(gloss, lines, r, n_word=100, n_line=0)
            if report(f"  synth {shape} seed {seed} (gloss {len(gloss.replace(' ', ''))} letters / {sum(counts)} signs)", real, a):
                wins += 1
        print(f"  => {shape}: {wins}/5 seeds clear their own shuffled-gloss gate")


if __name__ == '__main__':
    rng = random.Random(20261002)
    blocks = {n: load_block(n) for n in BLOCKS}
    sym = surrogates([ln for n in blocks for ln in blocks[n]])
    print(f"sign inventory: {len(sym)} symbol codes + numerals; blocks: " +
          ', '.join(f"b{n} {len(blocks[n])} lines/{sum(len(l) for l in blocks[n])} signs" for n in blocks))
    print("\n== target: one gloss->block pair per block ==")
    any_gate = False
    for (n, wit), gloss in GLOSS.items():
        enc = encode(blocks[n], sym)
        real, counts = run(gloss, enc)
        a, b = controls(gloss, enc, rng)
        g = report(f"block {n} gloss[{wit}] ({len(gloss.replace(' ', ''))} letters / {sum(len(l) for l in blocks[n])} signs)", real, a, b)
        any_gate = any_gate or g
    print("\n== comparison: NX-3151G's line-to-line pairing on block 1 (same statistic) ==")
    g1 = GLOSS[(1, 'subagent+worker')].split()
    pairs = [{'plain_line': f'L{i}', 'plain_raw': p, 'cipher_line': f'L{i}', 'cipher_raw': c}
             for i, (p, c) in enumerate(zip(["en mauluaise", "gouuernement", "de que iustice"], encode(blocks[1], sym)))]
    _, _, counts, _ = ia.run_align(pairs, floor=100)
    real = stat(counts)
    a = []
    for _ in range(200):
        pl = ["en mauluaise", "gouuernement", "de que iustice"]; rng.shuffle(pl)
        pp = [dict(p, plain_raw=q) for p, q in zip(pairs, pl)]
        a.append(stat(ia.run_align(pp, floor=100)[2]))
    report("block 1 line-pairs", real, a)
    positive_controls(rng)
    print("\nTARGET GATE:", "cleared on at least one block" if any_gate else "not cleared on any block -- no key.tsv, no decode, no judge run")
