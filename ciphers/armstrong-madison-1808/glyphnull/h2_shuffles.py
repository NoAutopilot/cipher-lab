#!/usr/bin/env python3
"""Campaign step H2 (27 Sept 2026): rule-3-sized control for the SO-ARMSTRONG-COMPONENTS glyph-null finding.

The second opinion (second-opinions/chatgpt-components-2026-09-27.md, its "Self-contained reproducer") deleted glyph 20
(and, in a second model, glyphs 20 and 22) from the codex-2026-09-27b 257-token / 36-shape provisional glyph
transcription, searched a <=2-homophone letter substitution with a character 5-gram model (en18 minus the Jefferson
volume, backoff weight 5, J->I, V->U) at 150 restarts x 50,000 proposals, seed 731, and found the glyph-20 target
outranking all 20 of its own token shuffles (0/20), the glyph-20+22 target 6/20. Twenty shuffles is below this
repository's own convention (ARM-A2, ARM3-DICT: 200). This script rebuilds that exact model and solver, reproduces the
recorded 20 shuffles (same seeds 270932+s), extends to 200 shuffles per model, runs the three matched positive controls
first (gate: >=98% characters recovered, as the reproducer itself required), and reports the target's real percentile.

Pre-registered reading: PASS = target score above the 200-shuffle 95th percentile (fewer than 10 of 200 at or above it);
FAIL otherwise. A PASS says only that the token ORDER carries structure a shuffle destroys under this model; it is not
a reading, and the reproducer's own raw outputs are not readable English.

Usage (repository root): python3 ciphers/armstrong-madison-1808/glyphnull/h2_shuffles.py SCRATCH_DIR [--nshuf 200]
Writes glyphnull/h2_results.tsv and h2_shuffle_scores.tsv in the repository; sequences, model and binaries in SCRATCH_DIR.
"""
import collections, concurrent.futures, gzip, json, random, re, statistics, subprocess, sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = Path(sys.argv[1]).resolve()
NSHUF = int(sys.argv[sys.argv.index('--nshuf')+1]) if '--nshuf' in sys.argv else 200
OUT.mkdir(parents=True, exist_ok=True)
ALPHA = 'abcdefghiklmnopqrstuwxyz'
R, T, CAP, SEED = 150, 50000, 2, 731

FLAT_CPP = r'''
#include <bits/stdc++.h>
using namespace std;
int main(int ac,char**av){
 if(ac!=8)return 1; const int A=24;
 int off[6]={0},sz=0;for(int n=1,p=A;n<=5;n++,p*=A){off[n]=sz;sz+=p;}
 vector<float> lm(sz);ifstream mf(av[1],ios::binary);mf.read((char*)lm.data(),sz*4);if(!mf)return 2;
 vector<int> seq;ifstream sf(av[2]);int x,K=0;while(sf>>x){seq.push_back(x);K=max(K,x+1);}
 int R=stoi(av[3]),T=stoi(av[4]),cap=stoi(av[5]);mt19937 rng(stoul(av[6]));
 vector<vector<int>> ctx,affected(K);vector<int> plainseq;
 for(int i=0;i<(int)seq.size();i++)if(seq[i]>=0){
  vector<int> c;for(int j=i;j>=0&&j>i-5&&seq[j]>=0;j--)c.push_back(seq[j]);reverse(c.begin(),c.end());
  int q=ctx.size();ctx.push_back(c);sort(c.begin(),c.end());c.erase(unique(c.begin(),c.end()),c.end());
  for(int y:c)affected[y].push_back(q);
 }
 vector<vector<vector<int>>> pairs(K,vector<vector<int>>(K));
 for(int a=0;a<K;a++)for(int b=0;b<K;b++)set_union(affected[a].begin(),affected[a].end(),affected[b].begin(),affected[b].end(),back_inserter(pairs[a][b]));
 vector<int> key(K),counts(A);uniform_real_distribution<double> U(0,1);
 auto term=[&](int q){int z=0;for(int c:ctx[q])z=z*A+key[c];return lm[off[ctx[q].size()]+z];};
 vector<double> temp(T);for(int i=0;i<T;i++)temp[i]=2.5*pow(.02/2.5,double(i)/T);
 vector<pair<double,vector<int>>> results;
 for(int r=0;r<R;r++){
  fill(counts.begin(),counts.end(),0);for(int&i:key){do{i=rng()%A;}while(counts[i]>=cap);counts[i]++;}
  double cur=0;for(int q=0;q<(int)ctx.size();q++)cur+=term(q);double best=cur;vector<int> bk=key;
  for(int it=0;it<T;it++){
   int i=rng()%K,j=-1,old=key[i],nv;bool sw=U(rng)<.6;
   if(sw){j=rng()%K;nv=key[j];if(nv==old)continue;}else{nv=rng()%A;if(nv==old||counts[nv]>=cap)continue;}
   auto& qs=sw?pairs[i][j]:affected[i];double before=0;for(int q:qs)before+=term(q);
   if(sw)swap(key[i],key[j]);else{key[i]=nv;counts[old]--;counts[nv]++;}
   double after=0;for(int q:qs)after+=term(q);double delta=after-before;
   if(delta>=0||U(rng)<exp(delta/temp[it])){cur+=delta;if(cur>best){best=cur;bk=key;}}
   else if(sw)swap(key[i],key[j]);else{key[i]=old;counts[old]++;counts[nv]--;}
  }
  results.push_back({best,bk});
 }
 sort(results.begin(),results.end(),[](auto&a,auto&b){return a.first>b.first;});
 ofstream out(av[7]);string alpha="abcdefghiklmnopqrstuwxyz";
 for(int r=0;r<min(20,R);r++){
  out<<setprecision(12)<<results[r].first<<'\t';for(int c:results[r].second)out<<alpha[c];out<<'\t';
  for(int c:seq)out<<(c<0?'|':alpha[results[r].second[c]]);out<<'\n';
 }
}
'''

def norm(s): return re.sub('[^a-z]', '', s.lower().replace('j', 'i').replace('v', 'u'))

def model(path):
    counts = [np.zeros(24**n, dtype=np.float64) for n in range(1, 6)]
    for p in sorted((ROOT/'tools/data/en18').glob('*.gz')):
        if 'thomas' in p.name: continue
        a = np.array([ALPHA.index(c) for c in norm(gzip.open(p, 'rt').read())], dtype=np.int64)
        for n in range(1, 6):
            codes = a[:len(a)-n+1].copy()
            for j in range(1, n): codes = codes*24 + a[j:len(a)-n+j+1]
            counts[n-1] += np.bincount(codes, minlength=24**n)
    lower = (counts[0]+.5)/(counts[0].sum()+12)
    with path.open('wb') as f:
        np.log10(lower).astype('float32').tofile(f)
        for n in range(2, 6):
            c = counts[n-1].reshape(-1, 24); tot = c.sum(axis=1, keepdims=True)
            lower = ((c + 5*np.tile(lower.reshape(-1, 24), (24, 1)))/(tot+5)).ravel()
            np.log10(lower).astype('float32').tofile(f)

def seqfile(name, frags):
    p = OUT/(name+'.seq'); p.write_text('\n'.join(' '.join(map(str, f))+' -1' for f in frags)+'\n'); return p

def solve(name):
    out = OUT/(name+'.tsv')
    subprocess.run([str(OUT/'solve'), str(OUT/'lm.bin'), str(OUT/(name+'.seq')), str(R), str(T), str(CAP), str(SEED), str(out)], check=True)
    sc, key, read = out.read_text().splitlines()[0].split('\t')
    return float(sc), key, read

def main():
    lm = OUT/'lm.bin'
    if not lm.exists(): model(lm)
    (OUT/'solve.cpp').write_text(FLAT_CPP)
    subprocess.run(['g++', '-O3', '-std=c++17', str(OUT/'solve.cpp'), '-o', str(OUT/'solve')], check=True)
    raw = [[int(t) for t in line.split(';')] for line in (ROOT/'ciphers/armstrong-madison-1808/codex-2026-09-27b/glyphs.txt').read_text().splitlines() if line]
    held = norm(gzip.open(next((ROOT/'tools/data/en18').glob('*thomas*')), 'rt').read())
    rows, shuf_rows = [], []
    for tag, nulls in [('null20', [20]), ('null20_22', [20, 22])]:
        fs = [[n for n in f if n not in nulls] for f in raw]; fs = [f for f in fs if f]
        symbols = sorted(set(sum(fs, []))); fs = [[symbols.index(n) for n in f] for f in fs]
        K = len(symbols); N = sum(map(len, fs))
        # matched positive controls first (the reproducer's own construction and seeds)
        ctrl = []
        for k, start in enumerate([40000, 80000, 120000]):
            plain = held[start:start+N]; freq = collections.Counter(plain)
            keys = {c: [i] for i, c in enumerate(sorted(freq))}; i = len(keys)
            for c, _ in freq.most_common():
                if i == K: break
                if freq[c] >= 2: keys[c].append(i); i += 1
            assert i == K
            rng = random.Random(270927+k); perm = list(range(K)); rng.shuffle(perm)
            used = collections.Counter(); cipher = []
            for c in plain: cipher.append(perm[keys[c][used[c] % len(keys[c])]]); used[c] += 1
            at = 0; new = []
            for f in fs: new.append(cipher[at:at+len(f)]); at += len(f)
            seqfile(f'{tag}_control{k}', new)
            sc, key, read = solve(f'{tag}_control{k}')
            correct = sum(x == y for x, y in zip(read.replace('|', ''), plain))
            ctrl.append((sc, correct, N)); print(tag, 'control', k, sc, f'{correct}/{N}', flush=True)
        gate_ok = all(c[1]/c[2] >= .98 for c in ctrl)
        if not gate_ok:
            rows.append((tag, N, K, 'CONTROL BELOW GATE', ';'.join(f'{c[1]}/{c[2]}' for c in ctrl), '', '', '', '', '', '', 'target not run (rule 3)'))
            continue
        seqfile(f'{tag}_target', fs)
        tsc, tkey, tread = solve(f'{tag}_target'); print(tag, 'target', tsc, flush=True)
        flat = sum(fs, []); jobs = []
        for s in range(NSHUF):
            a = flat.copy(); random.Random(270932+s).shuffle(a); at = 0; new = []
            for f in fs: new.append(a[at:at+len(f)]); at += len(f)
            seqfile(f'{tag}_shuffle{s:03d}', new); jobs.append(f'{tag}_shuffle{s:03d}')
        scores = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            for name, (sc, _, _) in zip(jobs, pool.map(solve, jobs)):
                scores[name] = sc; shuf_rows.append((tag, name, sc))
        v = sorted(scores.values()); n = len(v)
        ge = sum(x >= tsc for x in v); p95 = v[int(.95*n)-1] if n >= 20 else v[-1]
        verdict = 'PASS' if ge < max(1, round(.05*n)) else 'FAIL'
        rows.append((tag, N, K, f'{tsc:.6f}', ';'.join(f'{c[1]}/{c[2]}' for c in ctrl), n, f'{statistics.mean(v):.3f}', f'{statistics.pstdev(v):.3f}', f'{p95:.3f}', f'{v[-1]:.3f}', f'{ge}/{n}', verdict + (f' (target percentile {100*(n-ge)/n:.1f})')))
        print(tag, 'shuffles', n, 'mean', statistics.mean(v), 'p95', p95, 'max', v[-1], 'at/above target', ge, verdict, flush=True)
    with (HERE/'h2_results.tsv').open('w') as f:
        f.write('model\tN\tK\ttarget_score\tcontrols_correct\tn_shuffles\tshuffle_mean\tshuffle_sd\tshuffle_p95\tshuffle_max\tshuffles_at_or_above_target\tverdict\n')
        for r in rows: f.write('\t'.join(map(str, r))+'\n')
    with (HERE/'h2_shuffle_scores.tsv').open('w') as f:
        f.write('model\tshuffle\tscore\n')
        for r in shuf_rows: f.write('\t'.join(map(str, r))+'\n')

if __name__ == '__main__':
    main()
