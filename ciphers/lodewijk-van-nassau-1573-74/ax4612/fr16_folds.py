"""AX-4612: leave-one-file-out false-negative rate of the fr16 judge corpus (rule 3 fold-count amendment) at the
target's N=775 letters. For each held-out file: NgramModel on the other two, real_p05 from that model's own
controls (as judge_plaintext.py computes it), FN = share of 200 held-out windows scoring below real_p05."""
import sys, random, os
sys.path.insert(0, 'tools')
import judge_plaintext as jp
F = ['tools/data/fr16/lettresdecatheri01cathuoft_djvu.txt.gz', 'tools/data/fr16/lettresdecatheri02cathuoft_djvu.txt.gz',
     'tools/data/fr16/lettresindites00marg_djvu.txt.gz']
N = int(sys.argv[1]) if len(sys.argv) > 1 else 775
texts = [jp.read_corpus(f) for f in F]
tot_fn = tot = 0
for i, f in enumerate(F):
    m = jp.NgramModel([t for j, t in enumerate(texts) if j != i])
    real, null, cov = m.controls(N, samples=200)
    r05 = jp.pct(real, 0.05)
    held = jp.fold(texts[i]); rnd = random.Random(5); fn = 0
    for _ in range(200):
        j = rnd.randrange(0, max(1, len(held) - N)); fn += m.score(held[j:j + N]) < r05
    tot_fn += fn; tot += 200
    print(f'held out {os.path.basename(f)}: real_p05 {r05:.3f}, FN {fn}/200 = {fn/2:.1f}%')
print(f'blended FN {tot_fn}/{tot} = {100*tot_fn/tot:.1f}% (N={N}, 3 folds)')
