# Armstrong, 20 February 1808: space-aware glyph attack

27 September 2026. **Unsolved. No plaintext or historical key is established.**

This pass closes a specific gap in the earlier flat-alphabet experiment: its
model removed spaces and capped each plaintext letter at two graphic types.
Here, a cipher sign may represent an encoded space, and up to four types may
represent the same character. A five-character language model replaces the
earlier four-character model. This is an actual decoding experiment, not a
shorthand identification or an archival discovery.

## Result

The space-aware model recovered 257, 256 and 248 of 257 characters in three
synthetic known-answer controls (100%, 99.61%, 96.50%; mean 98.70%). The best
Armstrong candidate is incoherent. It beats all 20 fully optimized positional
shuffles, but **statistical structure is not readable plaintext**. There is no
independent key, coherent continuation, or manuscript-grounded decipherment.

| Space-aware experiment | Best log10 score | Correct known characters |
|---|---:|---:|
| control0 | -181.013503 | 257/257 |
| control1 | -171.043274 | 256/257 |
| control2 | -173.091888 | 248/257 |
| target | -342.574535 | unknown; incoherent |
| 20 shuffles, mean | -359.175970 | not applicable |
| 20 shuffles, range | -370.772283 to -346.439827 | not applicable |

Each run used 150 restarts × 50,000 proposals. Higher scores are better. These
are optimization scores, not probabilities of decipherment. Zero of 20 shuffled
maxima exceeded the target. A plus-one rank estimate is 1/21, but it is only a
descriptive comparison for this selected experiment, not a calibrated discovery
claim across all investigations. The modest separation does not validate any of
the candidate character assignments.

## Separate no-space control failure

I also removed spaces from both model training and the control plaintext, keeping
the four-homophone cap and all other machinery. This makes no-space spelling a
separate experiment. It did not reliably solve its known answers:

| Control | 150 × 50,000 correct | 600 × 100,000 correct | True-key score | Larger-run best score |
|---|---:|---:|---:|---:|
| control0 | 152/257 | 155/257 | -207.438556 | -280.590620 |
| control1 | 42/257 | 12/257 | -206.536339 | -285.395448 |
| control2 | 257/257 | 257/257 | -188.103456 | -188.103456 |

The true keys score substantially better than the failed searches for controls 0
and 1. This demonstrates an optimization failure on these examples, not an
information-theoretic impossibility. Increasing the search budget did not repair
it. **No Armstrong target or shuffled-target run was made for this variant.**
It provides no negative evidence against unspaced homophonic spelling. The good
space-aware controls must not be used to license that different model.

## Data, model and limits

The input is the unchanged provisional `codex-2026-09-27b/glyphs.txt`:
257 graphic tokens, 36 types, 28 fragments. Its type labels and punctuation
splits remain M-grade transcription assumptions. No numeral, manuscript reading,
or existing file was corrected in this pass. The original manuscript images were
consulted, including frame M34-014-0031, but no new glyph inventory was certified.

The model uses the five `tools/data/en18` volumes other than Jefferson volume IX.
Training normalizes j/i and v/u, converts nonletters into single spaces, and
retains a 25th character for space. Each volume is counted separately. Conditional
character n-grams of orders 1–5 use additive unigram smoothing of 0.5 and a
five-count backoff weight for each higher order. Fragment boundaries reset the
score. Numeric passages provide no plaintext anchors or bridges.

The held-out Jefferson volume supplies the three controls, starting at normalized
character offsets 40,000, 80,000 and 120,000. Each is 257 characters long and is
split into the target's exact fragment lengths. All use 36 observed cipher types,
a random label permutation, and a maximum of four homophones. Extra homophones
are concentrated on the most frequent plaintext characters and used cyclically.
Their keys start cold in the solver. This deliberately exercises three- and
four-type homophony that the old two-type model could not represent.

These are **size- and model-matched synthetic controls, not fully design-matched
historical controls**. They do not match the target's exact frequency spectrum,
possible selection for proper names, transcription error process, or unknown
rules. Their strong recovery establishes capability for clean English with
encoded spaces; it neither establishes that Armstrong used spaces nor excludes
abbreviations, syllables, word signs, nulls, another language, changing keys, or
compound glyphs. The no-space variant has its own normalized offsets and therefore
different source windows; its outcome must be assessed on its own controls.

Each shuffled sample preserves the entire target type-frequency spectrum and
fragment-length vector but randomizes token positions. All 20 receive the same
optimization budget as the space-aware target. Search uses a fixed random seed,
single-symbol reassignments and pair swaps, simulated annealing from 2.5 to 0.02,
and incremental affected-window scoring.

An independent full-score recomputation of all 24 space-aware winning keys and
the three larger-budget no-space control keys agreed with the incremental scores
within 5e-10. Every rendered candidate agreed with its stored key and sequence,
and every key satisfied the four-type cap. These checks verify the implementation
and recorded scores, not a target decipherment.

## Primary-source and external-claim checks

The [original target and editorial transcription](https://pjm.as.virginia.edu/john-armstrong-jr-james-madison-20-february-1808)
remain the historical source. The real
[15 February 1808 Armstrong–Jefferson letter](https://rotunda.upress.virginia.edu/founders/default.xqy?keys=FOEA-print-04-01-02-7420&mode=deref)
supports the provenance of the suggested bearer-description crib, not its
application to this ciphertext. The repeated `240` conflict and the manuscript's
opening `1843` reading remain as documented in the earlier report.

The later August 30–31 comments on
[Schmeh's article](https://klausschmeh.net/can-you-decipher-this-letter-sent-to-u-s-president-james-madison/)
were checked. Their author reports unsuccessful continuation searches and
withdraws two additional phrase proposals. The comments themselves caution that
the suggested opening assignments are not established as globally fixed entries.
They do not provide a verified complete reading or an independently usable key.
Their detailed numerical experiments were not reproduced here and are not
adopted as exclusions. The present solver uses none of their plaintext guesses.

The Livingston-key retrieval did not succeed. The official reel-3 manifest
request and a newly indexed
[reel-3 image-page reference](https://www.loc.gov/resource/mss33217.003/?sp=1111&st=image)
returned HTTP 403; the latter is a reel reference, **not an identified key frame**.
The [LOC finding aid](https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms009142/ms009142.pdf)
and existing index evidence locate the research lead, but no key image was
obtained or compared. Access failures do not establish absence of the item.
The possible relationship of the catalogued 1803 Livingston key to WE027 or to
this target remains unproved. No archival message was sent.

A brief Wouves 1797 syllabic-table search did not yield an inspected key plate;
no test or exclusion of that table is claimed. A numerical coordinate-code idea
was considered but not implemented as a controlled decoder. Neither conjecture
is promoted to a result.

## Reproduce without changing repository files

Save the Python block below to a new file **outside** the repository. It requires
Python 3, NumPy and g++. Pass the repository root and a separate scratch output
directory. The script rejects output directories inside the repository.

```sh
python attack.py /path/to/cipher-lab /path/to/scratch/space --run control
python attack.py /path/to/cipher-lab /path/to/scratch/space --run target
python attack.py /path/to/cipher-lab /path/to/scratch/space --run shuffle
```

For the no-space experiment, make a separate script copy in scratch and append
`.replace(' ','')` to the return expression of `norm`. Use a separate output
directory so the language models cannot be mixed. Run its controls with defaults,
retain those results, then run controls with `--restarts 600 --steps 100000`.
Do not interpret a target failure from this variant until its control problem is
resolved. The exact script and both model hashes are recorded below.

The script emits inputs, model, compiled solver, manifest, top candidates and
results into scratch. Candidate outputs are optimization artifacts, **not
plaintext**. This single report embeds the executable source so this submission
adds exactly one repository file.

### Reproducibility record

```json
{
  "space_manifest": {
    "N": 257,
    "K": 36,
    "lengths": [
      1,
      5,
      8,
      1,
      5,
      17,
      10,
      8,
      31,
      10,
      3,
      25,
      8,
      5,
      1,
      14,
      8,
      6,
      1,
      6,
      5,
      4,
      8,
      20,
      2,
      9,
      9,
      27
    ],
    "symbols": [
      "10",
      "12",
      "14",
      "16",
      "18",
      "20",
      "22",
      "23",
      "24",
      "26",
      "28",
      "29",
      "32",
      "33",
      "34",
      "35",
      "36",
      "38",
      "40",
      "42",
      "44",
      "46",
      "47",
      "48",
      "60",
      "62",
      "64",
      "65",
      "66",
      "68",
      "70",
      "72",
      "73",
      "74",
      "76",
      "78"
    ],
    "seed": 731,
    "restarts": 150,
    "steps": 50000,
    "cap": 4,
    "sha256": {
      "ciphers/armstrong-madison-1808/codex-2026-09-27b/glyphs.txt": "f21eed0b9bd3e8825bd84cfb0401a76245c58d246e4920df581de59ce0f75fa0",
      "tools/data/en18/writingsalbertg01gallgoog.txt.gz": "3a0c22fa11df82ca897e308370ba4fbd4f9108324351ff0b9b13da3c1c25fafa",
      "tools/data/en18/writingsjamesmo02unkngoog.txt.gz": "767e25f617efe7f18abced8006ec311455514fa13e00d3a7383cd32f7bb128a3",
      "tools/data/en18/writingsjamesmo11monrgoog.txt.gz": "959c7731a6271e51a17ff6e55c15c67e4be909667bf51ec4e916c35147aedb19",
      "tools/data/en18/writingsofjamesm0007unse_s2a1.txt.gz": "52fc552738110e6179e29e195738d21b48aca64ee867c3b5ff8a3d585cfa5a66",
      "tools/data/en18/writingsofjamesm0008unse.txt.gz": "a453af6233fda25c9915ea120e5bd4e9d441628678b18d220ff5d68307830b50",
      "tools/data/en18/writingsofthomas09jeffiala.txt.gz": "6c055ee098042a15656bb52bfaa3da2a9e61e0f8b7961f180b29993557a5bb4e"
    }
  },
  "script_sha256": {
    "attack.py": "a80975895c6b32b05af4666e88093c51b2e094bf198117ca06e6c1c7ddb20c25",
    "attack_unspaced.py": "593e8f1a96f453ecf7894bac6256b67e027354614c416803b786a479e2b79ef0"
  },
  "model_sha256": {
    "output": "92068a8a9b4fffd80752d2c15f9ccec3dd569d8c29f59e885fa3345c5476f35c",
    "unspaced": "9ec204bc4ee1024bb20dd8b5dd72c46955f5d4c6d08be6923a70a9462b376fec"
  },
  "space_scores": {
    "control0": -181.013502953,
    "control1": -171.043274489,
    "control2": -173.091887552,
    "target": -342.574534913,
    "shuffle0": -356.234944916,
    "shuffle1": -358.32710353,
    "shuffle2": -363.255754057,
    "shuffle3": -353.912448647,
    "shuffle4": -361.347477593,
    "shuffle5": -370.772283492,
    "shuffle6": -365.284059098,
    "shuffle7": -354.744868076,
    "shuffle8": -346.4398272,
    "shuffle9": -348.48258202,
    "shuffle10": -355.054631744,
    "shuffle11": -358.62304908,
    "shuffle12": -365.340090906,
    "shuffle13": -358.251205005,
    "shuffle14": -355.089574336,
    "shuffle15": -357.671061433,
    "shuffle16": -364.045982893,
    "shuffle17": -365.05645142,
    "shuffle18": -362.090562796,
    "shuffle19": -363.495435907
  },
  "no_space_initial": {
    "control0": {
      "score": -292.109389604,
      "correct": 152,
      "restarts": 150,
      "steps": 50000
    },
    "control1": {
      "score": -297.815080296,
      "correct": 42,
      "restarts": 150,
      "steps": 50000
    },
    "control2": {
      "score": -188.103456272,
      "correct": 257,
      "restarts": 150,
      "steps": 50000
    }
  },
  "no_space_larger": {
    "control0": {
      "score": -280.590619602,
      "correct": 155,
      "restarts": 600,
      "steps": 100000
    },
    "control1": {
      "score": -285.395447777,
      "correct": 12,
      "restarts": 600,
      "steps": 100000
    },
    "control2": {
      "score": -188.103456272,
      "correct": 257,
      "restarts": 600,
      "steps": 100000
    }
  }
}
```

### Executable source

```python
"""Space-aware homophonic screen. Writes only into the supplied output directory."""
import argparse, collections, gzip, hashlib, json, random, re, subprocess
from pathlib import Path
import numpy as np

ALPHA = 'abcdefghiklmnopqrstuwxyz '
CPP = r'''
#include <bits/stdc++.h>
using namespace std;
int main(int ac,char**av){
 if(ac!=8)return 1; const int A=25;
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
 ofstream out(av[7]);string alpha="abcdefghiklmnopqrstuwxyz_";
 for(int r=0;r<min(20,R);r++){
  out<<setprecision(12)<<results[r].first<<'\t';for(int c:results[r].second)out<<alpha[c];out<<'\t';
  for(int c:seq)out<<(c<0?'|':alpha[results[r].second[c]]);out<<'\n';
 }
}
'''

def norm(s):
    return re.sub('[^a-z]+', ' ', s.lower().replace('j','i').replace('v','u')).strip()

def model(paths, dest):
    counts = [np.zeros(25**n, dtype=np.float64) for n in range(1,6)]
    for p in paths:
        text = norm(gzip.open(p,'rt').read())
        a = np.array([ALPHA.index(c) for c in text], dtype=np.int64)
        for n in range(1,6):
            codes = a[:len(a)-n+1].copy()
            for j in range(1,n): codes = codes*25+a[j:len(a)-n+j+1]
            counts[n-1] += np.bincount(codes,minlength=25**n)
    lower = (counts[0]+.5)/(counts[0].sum()+12.5)
    with dest.open('wb') as f:
        np.log10(lower).astype('float32').tofile(f)
        for n in range(2,6):
            c=counts[n-1].reshape((-1,25)); total=c.sum(axis=1,keepdims=True)
            prior=np.tile(lower.reshape((-1,25)),(25,1))
            lower=((c+5*prior)/(total+5)).ravel()
            np.log10(lower).astype('float32').tofile(f)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('repo',type=Path);ap.add_argument('out',type=Path)
    ap.add_argument('--restarts',type=int,default=150);ap.add_argument('--steps',type=int,default=50000)
    ap.add_argument('--shuffles',type=int,default=20);ap.add_argument('--run',default='all')
    a=ap.parse_args();r=a.repo.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
    if out==r or r in out.parents:raise ValueError('Output must be outside repository')
    source=r/'ciphers/armstrong-madison-1808/codex-2026-09-27b/glyphs.txt'
    raw=[s.split(';') for s in source.read_text().splitlines() if s]
    symbols=sorted(set(sum(raw,[])),key=int);frags=[[symbols.index(c) for c in f] for f in raw]
    lengths=list(map(len,frags));N=sum(lengths);K=len(symbols)
    paths=sorted((r/'tools/data/en18').glob('*.gz'));held=next(p for p in paths if 'thomas' in p.name)
    train=[p for p in paths if p!=held]
    if not (out/'lm.bin').exists():model(train,out/'lm.bin')
    if not (out/'solve').exists():
        (out/'solve.cpp').write_text(CPP);subprocess.run(['g++','-O3','-std=c++17',str(out/'solve.cpp'),'-o',str(out/'solve')],check=True)
    text=norm(gzip.open(held,'rt').read());cases={'target':{'frags':frags}}
    for seed,start in enumerate([40000,80000,120000]):
        rng=random.Random(260927+seed);plain=text[start:start+N];freq=collections.Counter(plain)
        key={c:[i] for i,c in enumerate(sorted(freq))};nextid=len(key)
        # Concentrate some homophones on frequent characters; max 4 per character.
        for c,_ in freq.most_common():
            while len(key[c])<min(4,freq[c]) and nextid<K:key[c].append(nextid);nextid+=1
        assert nextid==K
        perm=list(range(K));rng.shuffle(perm);seen=collections.Counter();cipher=[]
        for c in plain:
            cipher.append(perm[key[c][seen[c]%len(key[c])]]);seen[c]+=1
        assert len(set(cipher))==K
        fs=[];at=0
        for n in lengths:fs.append(cipher[at:at+n]);at+=n
        cases[f'control{seed}']={'frags':fs,'plain':plain,'start':start,'max_homophones':max(map(len,key.values()))}
    flat=sum(frags,[])
    for seed in range(a.shuffles):
        s=flat.copy();random.Random(270927+seed).shuffle(s);fs=[];at=0
        for n in lengths:fs.append(s[at:at+n]);at+=n
        cases[f'shuffle{seed}']={'frags':fs}
    manifest={'N':N,'K':K,'lengths':lengths,'symbols':symbols,'seed':731,'restarts':a.restarts,'steps':a.steps,'cap':4,
              'sha256':{str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [source]+paths}}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    results={}
    if (out/'results.json').exists():results=json.loads((out/'results.json').read_text())
    for name,case in cases.items():
        if a.run!='all' and not name.startswith(a.run):continue
        (out/(name+'.seq')).write_text('\n'.join(' '.join(map(str,f))+' -1' for f in case['frags'])+'\n')
        subprocess.run([str(out/'solve'),str(out/'lm.bin'),str(out/(name+'.seq')),str(a.restarts),str(a.steps),'4','731',str(out/(name+'.tsv'))],check=True)
        lines=(out/(name+'.tsv')).read_text().splitlines();score,key,reading=lines[0].split('\t')
        result={'score':float(score),'key':key,'reading':reading,'restarts':a.restarts,'steps':a.steps}
        if 'plain' in case:
            decoded=reading.replace('|','').replace('_',' ')
            result.update(plain=case['plain'],correct=sum(x==y for x,y in zip(decoded,case['plain'])),N=N,start=case['start'],max_homophones=case['max_homophones'])
        results[name]=result;(out/'results.json').write_text(json.dumps(results,indent=2)+'\n')
        print(name,score,result.get('correct',''),flush=True)

if __name__=='__main__':main()
```
