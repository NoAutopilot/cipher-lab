"""Step d without a space class (spaces not assumed), for texts the screen says carry none: plain homophonic
solve under the no-space model of LANG; writes a score.py key. usage: nospace_solve.py TEXTID LANG RESTARTS ITERS SEED KEYOUT"""
import sys, os
sys.argv, args = sys.argv[:1], sys.argv[1:]
import pipeline as P
sys.path.insert(0, os.path.join(P.HERE, '..')); import score
tid, lang, R, I, seed, out = args[0], args[1], int(args[2]), int(args[3]), int(args[4]), args[5]
seq = score.flat(score.load_text(tid))
r = P.solve(seq, set(), lang, R, I, seed)
with open(out, 'w') as f:
    f.write('sign\tvalue\n')
    for s in sorted(set(seq)): f.write(f"{s}\t{r['key'][s]}\n")
print(tid, lang, 'gap', r['gap'], 'raw', r['rawgap'])
