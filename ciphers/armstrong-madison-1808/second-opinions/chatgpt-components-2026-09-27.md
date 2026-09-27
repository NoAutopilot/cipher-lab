# Armstrong–Madison, 20 February 1808: component and fixed-null tests

Recorded 2026-09-27T19:21:36+00:00. **Not deciphered. No new target plaintext or key is established.**

This is a single-file continuation of the Chat GPT Push work and PRs #40–41. It contains three additional, narrowly defined tests, their positive controls, shuffled-input baselines, primary-source observations, and a self-contained reproducer. It changes no existing repository file. The public-source work below did not obtain the missing Livingston/Brant key or a second letter in the target system.

## Results

All searches used 150 independent starts × 50,000 proposals, seed 731. Higher scores are better; scores are sums and **must not be compared across different text lengths**.

| Hypothesis | Held-out positive controls: correct characters | Target score | Scrambled targets at or above target |
|---|---:|---:|---:|
| Three decimal fields, each encodes one letter; zero omitted | 729/729; 731/731; 769/769 | -1379.939337240 | 1/20 |
| Glyph 20 always null; remaining shapes ≤2 homophones per letter | 220/220; 218/220; 220/220 | -274.415061677 | 0/20 |
| Glyphs 20 and 22 always null; remaining shapes ≤2 homophones per letter | 207/207; 205/207; 207/207 | -263.987430959 | 6/20 |

None of the three target outputs is sustained readable English. Short accidental words are not a decipherment. The glyph-20 result outranks its 20 shuffles, but this is a small, exploratory comparison among multiple tried models, **not** proof that glyph 20 is null or that the winning letters are right. Existing symbol order may carry structure under a wrong model.

The independent scorer checked **72 winning outputs**: nine positive controls, three targets, and 60 shuffled inputs. It recomputed scores directly from the saved keys and model, checked rendered output against the input sequence, and checked key constraints. Maximum absolute score discrepancies: 4.89e-09 (decimal model), 4.98e-10 (glyph models).

## Exact scope of the decimal test

For a number `n`, the fields are `n//100`, `(n//10)%10`, and `n%10`, in that order. Nonzero values select letters from independent registers of sizes 19, 9, and 9. Zero emits nothing. A register is injective; letters can recur in different registers. Thus this is an unknown three-component spelling table, **not** a free number-to-word substitution and not a recovered historical system. It was motivated by the maximum 1900 and frequent final zeroes.

The 366 numeric groups expand to 846 characters using all 37 field values. Graphic passages and the existing nonnumeric markers are opaque breaks, giving 28 numeric fragments. The source retains its uncertain readings (including first `1841` versus manuscript `1843`, and `203` versus `200`); it is not a certified manuscript transcription.

Controls use held-out Jefferson text at normalized offsets 40000, 80000, and 120000. The other five en18 volumes train the model. Each control is genuinely enciphered through the three-register mechanism with the same 366 group slots and numeric-fragment group counts. The first register contains the 19 most frequent training letters; the middle contains the remaining five plus the four most frequent; the final contains the nine most frequent. Each register is independently shuffled. Encoding greedily consumes the next matching letter at each register, emitting zero otherwise. This guarantees encodability without consulting target plaintext.

The resulting controls have 729, 731, and 769 letters and 34, 35, and 34 observed field values; **they do not exactly match the target's 846 letters, 37 observed values, or component frequencies**. Their exact recovery demonstrates capability on these examples, not a universal exclusion of all compositional numeric systems. Other field orders, nonempty zeroes, digraphs, phonetic spelling, polyalphabetic rules, and codebook entries are outside this test.

The numeric nulls shuffle entire numeric groups, then restore the same fragment group counts before expansion. This preserves each number and its internal fields; it does not shuffle component letters independently. Twenty null scores range from -1409.264801650 to -1364.251557950, mean -1398.767973873.

## Exact scope of the glyph tests

These tests use the existing 257-token, 36-shape transcription; its shape labels remain provisional. Shape 20 occurs 37 times; shape 22 occurs 13 times. The tests **fix** the null sets in advance of each search; the solver does not infer which signs are null. Their purpose is to test whether deleting these common curved shapes makes an ordinary alphabetic reading recoverable, including the otherwise awkward repetitions near the end of the long final glyph passage.

After deletion, the targets contain 220 characters/35 types and 207 characters/34 types. Empty fragments are dropped; other boundaries remain. The controls have exactly these post-deletion lengths, observed-type counts, and fragment lengths. They are English prose enciphered with at most two homophones per letter; frequent letters receive the extra homophones and those homophones alternate. They do not reproduce the target's exact symbol frequencies or its possibly deliberate selection of names/foreign words for graphic writing. They do not validate the glyph transcription. Whole-word signs, syllables, contextual nulls, wider homophony, and historical shorthand rules remain untested.

Each null baseline shuffles the surviving symbol tokens and restores the surviving fragment lengths. All search budgets and scoring rules match the target. No inferred null or winning substitution is promoted into the cipher inventory.

## Primary-source work

### Annet manuals

Read the actual 1752 and 1770 manuals, including their alphabet plates. They are materially different editions: for example, the 1752 plate gives `h` a short horizontal stroke and the word value “have”; the 1770 plate gives a horizontal `e` the word value “the”. Mixing sign values across these editions would be unsafe.

The 1770 manual allows alphabetic signs, word values, word-part signs, omitted silent/doubled letters, and phonetic/abbreviated spelling. PDF page 16 supplies the plaintext for the twenty engraved examples on PDF page 17. Those paired examples provide an actual shorthand control source for a future literal implementation. **The present solver does not implement those rules or decode that plate.** The earlier letter/digraph experiments must continue to be described as surrogates. No identification of Armstrong's symbols as Annet follows from the visual resemblance of a few curves.

Sources (public-domain manuals; page numbering here is PDF page numbering):

- [Annet 1752 PDF](https://www.dropbox.com/scl/fi/i0dqytfc2xt35hft2ppvr/Annets-Shorthand-1752.pdf?dl=1&rlkey=1k8jfq01kzsfqj03cirrdsjp2), alphabet page 3, SHA-256 `4aa2d9c1d3e1cf4ba316eec1c8304a35fc67c8ac7b1bd56abf3de8afde4f47ee`.
- [Annet 1770 PDF](https://www.dropbox.com/scl/fi/e0nih2zcsrhl5tfq2d8wy/Annets-Shorthand-1770.pdf?dl=1&rlkey=rn4g1tw3iwvnkv0wasqory24m), alphabet page 3, examples pages 16–17, SHA-256 `243dfc316e7b7d2fb7cd282dcb503ce50aac3d44334bf93fa03e419bb017df3c`.
- Download links were published by [Stenophile's historical collection](https://www.stenophile.com/historical). The scans were inspected, not just their catalogue descriptions.

### Wouves table: actual mechanism reached, complete table not obtained

[Roberto R. Narváez's article](https://www.scielo.org.mx/pdf/hm/v71n3/2448-6531-hm-71-03-1361.pdf) reproduces instructions and photographs from AGN, IV, c.2610, exp.026, f.19. Its figures 3–4 are details, not a complete transcribed key. The scheme has 62 alphabetic columns with rows 1–99; each column receives an arbitrary hundred base. An entry is the base plus its row. Example: base 5800 plus row 7 gives 5807 for “hoy”. The instructions also allow adding/subtracting a shared constant. Therefore final zeroes or values below 100 cannot by themselves exclude an offset variant. The target occupies 77 of the 100 suffix residues; 23 offsets avoid a forbidden zero row. This is only a necessary arithmetic condition, not a match. No connection to Armstrong is established.

The [Wellcome catalogue](https://wellcomecollection.org/works/jegb9q9f) points to ECCO item `CB0131087164`; its full table was not retrieved. Article PDF SHA-256: `43ea6b201bc779774c5795b4dcc0d4bde5529fa56ee40ba13e7fd6f8663c8510`.

### Livingston image annotations: extraction lead, not a target key

Re-examined the existing native-resolution images in `pool/liv/img/`. The frame `mjm014253_0303.jpg` has a short, readily located cipher passage on the **right-hand page near the top**, contrary to the earlier manifest's “not located” outcome. It contains these interlinear word/phrase associations (one-reader observations, grade **M**, not an independently certified key):

| Numeric group/run | Interlinear reading | Evidence location |
|---|---|---|
| `324` | my | `mjm014253_0303.jpg`, right page, short upper passage |
| `731` | friend | same |
| `1523 518 1126 1467` | Marbois | same, crosses the manuscript line break |
| `1295 934 1667` | Talleyrand | same; retain as a run, do not force its internal split |
| `1467` | is | same, following the Talleyrand run |
| `1[0/6]75` | all | same; middle digit retained as uncertain |
| `648 1583` | powerfull / powerful | same; compound boundary is provisional |
| `715 1583 648 967 913` | his full power(s) that he | `mjm014123_1076.jpg`, right page, first coded passage |
| `968` | the | `mjm014123_1076.jpg`, left page, first coded line |

The repeated `1583`/`648` in “powerfull” versus “full powers” makes these two images useful for checking component boundaries and word/inflection conventions. It does not establish every individual value from a multi-number name. Preserve the original punctuation/diacritics before a full reconstruction. The repo manifest labels the May frame Madison→Livingston, while its running text appears to be the Paris correspondent's account; direction was not independently resolved here, so the image identifier/frame is the provenance anchor.

These are observations about another cipher witness. Literal overlap of a few values with Armstrong is insufficient to transfer the readings. No such transfer is claimed. Full modern-edition text alignment was not obtained: publisher links failed to resolve in the available retrieval tool, and direct retrieval returned 403. The Brant Box 37 key and Monroe 1803 key remain unacquired; this pass sent no archival requests.

## Raw target outputs (audit only, not proposed plaintext)

### decimal

Key: `tbiuonldfyseahpcrmgstuenioapstoacnier`

```text
unobeliha|ucnasrntmesasamebe|iaasenasaecteeiisaonaepe|iaeatenaiaraieshonnneennboue|sesmeepescueaeaetittsinnunasiceeonsarieiiisec|eeaisesesteouunuarsifenupnseungsistesa|eatonoiaiaidenosesuussenerarissoiciasbeniaasasuestansanoseeio|lnssepeatstssomet|esensi|esnacusstoeinholiasems|oeaiarnstsuts|sianisnoatysise|eeehusonsiamsreinotoiauaseiises|ecteisne|eeeeoeidiaritsseiapiiecueserestatnsiseehuronmuohnstepepuisimpa|sobuuas|sseiiaasresiiasi|haritstshoshattoissiressiauisi|sicesreionbupe|sissaoahismostnimproeirantuostripsiaaioontonsehali|eioobuenas|nentaiunsoonsinaueuncneuiiic|sioisuoaitoaooooaacsale|iilaaia|somesssisnoalsoispasetoriimoc|tibedonanssiria|hottsonsstauecesscanasitonneerfiimissnoonpiastashislesstainestonuuiaohnssomitsusnuesneetes|sutiatariitituetisscoarsnstinsanestsaectonaidiisgorsasiaonreseueliaiiaeesihstonnosnaaoiueeitiiaailiesadouiteineeteeifasclieiueoato|
```

### delete-20

Key: `apcrooiiudearmsttmhfbflsunelpbcngdh`

```text
r|emcm|toftest|f|pstos|etomsisrisethrr|amintoitse|ntoredt|prereiecedaiortsorriceboare|etreactatr|it|iessuranceeuerturnsuldb|nnnre|bill|c|sotiuemddt|dtesing|ptito|ntiluo|onsm|icnt|delamo|otetocessinesneut|du|otouiruu|omrrsoth|osotomrisncedsotomitt|
```

### delete-20-and-22

Key: `wgrnsdtacituaseipkfzhoruoenhldmmgl`

```text
n|epra|esfeesi|h|gsess|eesastsutseekuu|tatoestere|oesnece|gneuidedicttuessnudrezstue|ienewritiu|de|dersunwodieuiueauorangl|omone|ldno|d|ssidueacce|cierdom|hedis|oidous|msa|ddmi|ginwas|iiidisstoermiae|ga|eaduau|aunsel|seandsoregreatie|
```

## Recorded metrics

```json
{
  "positive_controls": {
    "control0": {
      "score": -535.848420518,
      "N": 729,
      "K": 34,
      "restarts": 150,
      "steps": 50000,
      "correct": 729
    },
    "control1": {
      "score": -539.805129984,
      "N": 731,
      "K": 35,
      "restarts": 150,
      "steps": 50000,
      "correct": 731
    },
    "control2": {
      "score": -490.189750694,
      "N": 769,
      "K": 34,
      "restarts": 150,
      "steps": 50000,
      "correct": 769
    },
    "null20_control0": {
      "score": -183.784253198,
      "correct": 220,
      "N": 220,
      "K": 35
    },
    "null20_control1": {
      "score": -164.270870794,
      "correct": 218,
      "N": 220,
      "K": 35
    },
    "null20_control2": {
      "score": -166.176790072,
      "correct": 220,
      "N": 220,
      "K": 35
    },
    "null20_22_control0": {
      "score": -169.035578985,
      "correct": 207,
      "N": 207,
      "K": 34
    },
    "null20_22_control1": {
      "score": -165.442419225,
      "correct": 205,
      "N": 207,
      "K": 34
    },
    "null20_22_control2": {
      "score": -156.633760088,
      "correct": 207,
      "N": 207,
      "K": 34
    }
  },
  "numeric_nulls": {
    "scores": [
      -1397.4319962,
      -1394.91550387,
      -1394.3650129,
      -1399.62921537,
      -1392.21100965,
      -1404.06915105,
      -1364.25155795,
      -1394.27489173,
      -1405.88761955,
      -1405.59934638,
      -1391.12979913,
      -1409.26480165,
      -1385.58029803,
      -1399.21815019,
      -1408.21134203,
      -1403.97461443,
      -1408.89993943,
      -1405.34470951,
      -1405.24835663,
      -1405.85216178
    ],
    "n": 20,
    "mean": -1398.767973873,
    "min": -1409.26480165,
    "max": -1364.25155795,
    "ge_target": 1,
    "target": -1379.93933724
  },
  "glyph_nulls": {
    "null20_shuffle00": -289.999879148,
    "null20_shuffle01": -289.470783908,
    "null20_shuffle02": -282.039885758,
    "null20_shuffle03": -285.868059648,
    "null20_shuffle04": -289.745350914,
    "null20_shuffle05": -290.938363466,
    "null20_shuffle06": -292.526366256,
    "null20_shuffle07": -295.94873823,
    "null20_shuffle08": -282.556346937,
    "null20_shuffle09": -285.963763047,
    "null20_shuffle10": -284.857144572,
    "null20_shuffle11": -275.804233704,
    "null20_shuffle12": -286.116789257,
    "null20_shuffle13": -284.360671099,
    "null20_shuffle14": -284.755241349,
    "null20_shuffle15": -287.111145567,
    "null20_shuffle16": -289.06516926,
    "null20_shuffle17": -292.779431233,
    "null20_shuffle18": -292.937242629,
    "null20_shuffle19": -285.769528209,
    "null20_22_shuffle00": -264.687762718,
    "null20_22_shuffle01": -261.825390016,
    "null20_22_shuffle02": -265.021700003,
    "null20_22_shuffle03": -266.028056833,
    "null20_22_shuffle04": -269.746437599,
    "null20_22_shuffle05": -264.153393688,
    "null20_22_shuffle06": -269.645271126,
    "null20_22_shuffle07": -270.272633523,
    "null20_22_shuffle08": -264.42965097,
    "null20_22_shuffle09": -262.451692379,
    "null20_22_shuffle10": -258.857171632,
    "null20_22_shuffle11": -264.913315269,
    "null20_22_shuffle12": -261.121434534,
    "null20_22_shuffle13": -264.421865452,
    "null20_22_shuffle14": -268.392706348,
    "null20_22_shuffle15": -264.066234115,
    "null20_22_shuffle16": -265.807690757,
    "null20_22_shuffle17": -264.298152623,
    "null20_22_shuffle18": -263.821781574,
    "null20_22_shuffle19": -259.196865689
  },
  "truth_scores": {
    "coordinate": {
      "control0": -535.8484205179811,
      "control1": -539.8051299843637,
      "control2": -490.18975069376756
    },
    "glyph_null": {
      "null20_control0": -183.78425319799499,
      "null20_control1": -167.21033717948012,
      "null20_control2": -166.17679007232073,
      "null20_22_control0": -169.0355789848836,
      "null20_22_control1": -168.38188560982235,
      "null20_22_control2": -156.63376008809428
    }
  }
}
```

## Input hashes

```json
{
  "ciphers/armstrong-madison-1808/codex-2026-09-27/ciphertext_editorial_clean.txt": "bc25f718fa59dda0ccd6e9ddad5049d370c47343550031fb3f3c7e8239db5f30",
  "ciphers/armstrong-madison-1808/codex-2026-09-27b/glyphs.txt": "f21eed0b9bd3e8825bd84cfb0401a76245c58d246e4920df581de59ce0f75fa0",
  "tools/data/en18/writingsalbertg01gallgoog.txt.gz": "3a0c22fa11df82ca897e308370ba4fbd4f9108324351ff0b9b13da3c1c25fafa",
  "tools/data/en18/writingsjamesmo02unkngoog.txt.gz": "767e25f617efe7f18abced8006ec311455514fa13e00d3a7383cd32f7bb128a3",
  "tools/data/en18/writingsjamesmo11monrgoog.txt.gz": "959c7731a6271e51a17ff6e55c15c67e4be909667bf51ec4e916c35147aedb19",
  "tools/data/en18/writingsofjamesm0007unse_s2a1.txt.gz": "52fc552738110e6179e29e195738d21b48aca64ee867c3b5ff8a3d585cfa5a66",
  "tools/data/en18/writingsofjamesm0008unse.txt.gz": "a453af6233fda25c9915ea120e5bd4e9d441628678b18d220ff5d68307830b50",
  "tools/data/en18/writingsofthomas09jeffiala.txt.gz": "6c055ee098042a15656bb52bfaa3da2a9e61e0f8b7961f180b29993557a5bb4e"
}
```

## Self-contained reproducer

Requires Python 3, NumPy and a C++17 compiler. Save the block as `reproduce.py` **outside the repository**, then run:

```bash
python reproduce.py /absolute/path/to/cipher-lab /absolute/path/to/scratch-output
```

It reads the existing input files and writes all outputs outside the repository. It does not call Git or GitHub. It reconstructs both solvers, controls and shuffles, and verifies the 72 winning outputs. Its control thresholds gate the target runs. Corpus tokenization folds J→I and V→U, strips nonletters, and fits a character 5-gram model with recursive backoff weight 5. The original run used g++ (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0. Search implementations and training/control generation are included below.

```python
"""Three-field decimal spelling hypothesis; scratch-only experiment."""
from pathlib import Path
import collections,gzip,hashlib,json,random,re,subprocess,sys
import numpy as np

ROOT=Path(sys.argv[1]).resolve()
OUT=Path(sys.argv[2]).resolve()
if OUT==ROOT or ROOT in OUT.parents: raise ValueError('Output must be outside repository')
OUT.mkdir(parents=True,exist_ok=True)
D=OUT/'coordinate'
D.mkdir(exist_ok=True)
ALPHA='abcdefghiklmnopqrstuwxyz'

CPP=r'''
#include <bits/stdc++.h>
using namespace std;
int main(int ac,char**av){
 if(ac!=7)return 1;const int A=24,K=37;int off[6]={0},sz=0;
 for(int n=1,p=A;n<=5;n++,p*=A){off[n]=sz;sz+=p;}
 vector<float>lm(sz);ifstream mf(av[1],ios::binary);mf.read((char*)lm.data(),sz*4);if(!mf)return 2;
 vector<int>seq;ifstream sf(av[2]);int x;while(sf>>x)seq.push_back(x);
 int R=stoi(av[3]),T=stoi(av[4]);mt19937 rng(stoul(av[5]));uniform_real_distribution<double>U(0,1);
 vector<vector<int>>ctx,affected(K);for(int i=0;i<(int)seq.size();i++)if(seq[i]>=0){
  vector<int>c;for(int j=i;j>=0&&j>i-5&&seq[j]>=0;j--)c.push_back(seq[j]);reverse(c.begin(),c.end());
  int q=ctx.size();ctx.push_back(c);sort(c.begin(),c.end());c.erase(unique(c.begin(),c.end()),c.end());for(int t:c)affected[t].push_back(q);
 }
 vector<vector<vector<int>>>pairs(K,vector<vector<int>>(K));
 for(int a=0;a<K;a++)for(int b=0;b<K;b++)set_union(affected[a].begin(),affected[a].end(),affected[b].begin(),affected[b].end(),back_inserter(pairs[a][b]));
 vector<int>key(K),domain(K),starts={0,19,28},lens={19,9,9};int inverse[3][24];
 for(int i=0;i<K;i++)domain[i]=(i<19?0:i<28?1:2);
 auto term=[&](int q){int z=0;for(int t:ctx[q])z=z*A+key[t];return lm[off[ctx[q].size()]+z];};
 vector<double>temps(T);for(int i=0;i<T;i++)temps[i]=2.0*pow(.02/2.0,double(i)/T);
 vector<pair<double,vector<int>>>results;
 for(int r=0;r<R;r++){
  for(int d=0;d<3;d++){
   fill(inverse[d],inverse[d]+A,-1);vector<int>a(A);iota(a.begin(),a.end(),0);shuffle(a.begin(),a.end(),rng);
   for(int j=0;j<lens[d];j++){int i=starts[d]+j;key[i]=a[j];inverse[d][a[j]]=i;}
  }
  double cur=0;for(int q=0;q<(int)ctx.size();q++)cur+=term(q);double best=cur;vector<int>bk=key;
  for(int it=0;it<T;it++){
   int i=rng()%K,d=domain[i],old=key[i],nv=rng()%A;if(old==nv)continue;int j=inverse[d][nv];
   auto&qs=j<0?affected[i]:pairs[i][j];double bef=0;for(int q:qs)bef+=term(q);
   key[i]=nv;if(j>=0)key[j]=old;
   double aft=0;for(int q:qs)aft+=term(q);double delta=aft-bef;
   if(delta>=0||U(rng)<exp(delta/temps[it])){
    inverse[d][nv]=i;inverse[d][old]=j;cur+=delta;if(cur>best){best=cur;bk=key;}
   }else{key[i]=old;if(j>=0)key[j]=nv;}
  }
  results.push_back({best,bk});
 }
 sort(results.begin(),results.end(),[](auto&a,auto&b){return a.first>b.first;});ofstream out(av[6]);string alpha="abcdefghiklmnopqrstuwxyz";
 for(int r=0;r<min(20,R);r++){out<<setprecision(12)<<results[r].first<<'\t';for(int c:results[r].second)out<<alpha[c];out<<'\t';for(int c:seq)out<<(c<0?'|':alpha[results[r].second[c]]);out<<'\n';}
}
'''

def norm(s):return re.sub('[^a-z]','',s.lower().replace('j','i').replace('v','u'))
def fields(n):return [v for v in [n//100-1 if n//100 else -1,19+n//10%10-1 if n//10%10 else -1,28+n%10-1 if n%10 else -1] if v>=0]
def model():
    counts=[np.zeros(24**n,dtype=np.float64) for n in range(1,6)]
    for p in sorted((ROOT/'tools/data/en18').glob('*.gz')):
        if 'thomas' in p.name:continue
        a=np.array([ALPHA.index(c) for c in norm(gzip.open(p,'rt').read())],dtype=np.int64)
        for n in range(1,6):
            codes=a[:len(a)-n+1].copy()
            for j in range(1,n):codes=codes*24+a[j:len(a)-n+j+1]
            counts[n-1]+=np.bincount(codes,minlength=24**n)
    lower=(counts[0]+.5)/(counts[0].sum()+12)
    with (D/'lm.bin').open('wb') as f:
        np.log10(lower).astype('float32').tofile(f)
        for n in range(2,6):
            c=counts[n-1].reshape(-1,24);tot=c.sum(axis=1,keepdims=True)
            lower=((c+5*np.tile(lower.reshape(-1,24),(24,1)))/(tot+5)).ravel()
            np.log10(lower).astype('float32').tofile(f)

def prepare():
    source=ROOT/'ciphers/armstrong-madison-1808/codex-2026-09-27/ciphertext_editorial_clean.txt'
    nums=[];fr=[]
    for t in '\n'.join(s for s in source.read_text().splitlines() if not s.startswith('#')).split():
        if t.isdecimal():fr.append(int(t))
        elif fr:nums.append(fr);fr=[]
    if fr:nums.append(fr)
    cases={'target':{'numbers':nums}}
    text=norm(gzip.open(next((ROOT/'tools/data/en18').glob('*thomas*')),'rt').read())
    # Registers fixed from training frequencies; rare letters in middle field guarantee coverage.
    training=''.join(norm(gzip.open(p,'rt').read()) for p in sorted((ROOT/'tools/data/en18').glob('*.gz')) if 'thomas' not in p.name)
    order=[c for c,_ in collections.Counter(training).most_common()]
    alphabets=[order[:19],order[19:]+order[:4],order[:9]]
    assert all(len(set(a))==len(a) for a in alphabets) and set().union(*map(set,alphabets))==set(ALPHA)
    for seed,start in enumerate([40000,80000,120000]):
        rng=random.Random(270928+seed);keys=[a.copy() for a in alphabets]
        for a in keys:rng.shuffle(a)
        inv=[{c:i+1 for i,c in enumerate(a)} for a in keys];at=start;enc=[]
        for fs in nums:
            new=[]
            for _ in fs:
                n=0
                for pos,base in enumerate([100,10,1]):
                    if text[at] in inv[pos]:n+=base*inv[pos][text[at]];at+=1
                assert n>0;new.append(n)
            enc.append(new)
        cases[f'control{seed}']={'numbers':enc,'plain':text[start:at],'key':''.join(''.join(a) for a in keys),'start':start}
    for name,obj in cases.items():
        fs=[[v for n in f for v in fields(n)] for f in obj['numbers']]
        obj.update(N=sum(map(len,fs)),K=len(set(sum(fs,[]))),lengths=list(map(len,fs)))
        (D/(name+'.seq')).write_text('\n'.join(' '.join(map(str,f))+' -1' for f in fs)+'\n')
    (D/'cases.json').write_text(json.dumps(cases,indent=2)+'\n')
    (D/'solve.cpp').write_text(CPP);subprocess.run(['g++','-O3','-std=c++17',str(D/'solve.cpp'),'-o',str(D/'solve')],check=True)
    if not (D/'lm.bin').exists():model()

def run(prefix,R,T):
    cases=json.loads((D/'cases.json').read_text());results={}
    if (D/'results.json').exists():results=json.loads((D/'results.json').read_text())
    for name,c in cases.items():
        if not name.startswith(prefix):continue
        subprocess.run([str(D/'solve'),str(D/'lm.bin'),str(D/(name+'.seq')),str(R),str(T),'731',str(D/(name+'.tsv'))],check=True)
        score,key,reading=(D/(name+'.tsv')).read_text().splitlines()[0].split('\t')
        v={'score':float(score),'key':key,'reading':reading,'N':c['N'],'K':c['K'],'restarts':R,'steps':T}
        if 'plain' in c:v['correct']=sum(x==y for x,y in zip(reading.replace('|',''),c['plain']))
        results[name]=v;(D/'results.json').write_text(json.dumps(results,indent=2)+'\n');print(name,v['score'],v.get('correct'),v['N'],v['K'],flush=True)


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


def shuffle_run(directory, jobs, flat=False):
    import concurrent.futures
    def one(name):
        args=[str(directory/'solve'),str(D/'lm.bin'),str(directory/(name+'.seq')),'150','50000']
        if flat:args+=['2']
        args+=['731',str(directory/(name+'.tsv'))]
        subprocess.run(args,check=True)
        return name,float((directory/(name+'.tsv')).read_text().split('\t')[0])
    results={}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for name,s in pool.map(one,jobs):
            results[name]=s
            print(name,s,flush=True)
    (directory/'nulls.json').write_text(json.dumps(results,indent=2)+'\n')

def coordinate_nulls():
    nums=json.loads((D/'cases.json').read_text())['target']['numbers'];flat=sum(nums,[]);jobs=[]
    for s in range(20):
        a=flat.copy();random.Random(270930+s).shuffle(a);at=0;seq=[]
        for fr in nums:
            seq += [v for n in a[at:at+len(fr)] for v in fields(n)]+[-1];at+=len(fr)
        name=f'null{s:02d}';(D/(name+'.seq')).write_text(' '.join(map(str,seq))+'\n');jobs.append(name)
    shuffle_run(D,jobs)

def glyph_run():
    G=OUT/'glyph_null';G.mkdir(exist_ok=True)
    (G/'solve.cpp').write_text(FLAT_CPP)
    subprocess.run(['g++','-O3','-std=c++17',str(G/'solve.cpp'),'-o',str(G/'solve')],check=True)
    src=ROOT/'ciphers/armstrong-madison-1808/codex-2026-09-27b/glyphs.txt'
    raw=[[int(t) for t in line.split(';')] for line in src.read_text().splitlines() if line]
    held=norm(gzip.open(next((ROOT/'tools/data/en18').glob('*thomas*')),'rt').read());cases={}
    for tag,nulls in [('null20',[20]),('null20_22',[20,22])]:
        fs=[[n for n in f if n not in nulls] for f in raw];fs=[f for f in fs if f]
        symbols=sorted(set(sum(fs,[])));fs=[[symbols.index(n) for n in f] for f in fs]
        K=len(symbols);N=sum(map(len,fs))
        cases[tag+'_target']={'frags':fs,'K':K,'N':N,'nulls':nulls,'symbols':symbols}
        for k,start in enumerate([40000,80000,120000]):
            plain=held[start:start+N];freq=collections.Counter(plain)
            keys={c:[i] for i,c in enumerate(sorted(freq))};i=len(keys)
            for c,_ in freq.most_common():
                if i==K:break
                if freq[c]>=2:keys[c].append(i);i+=1
            assert i==K
            rng=random.Random(270927+k);perm=list(range(K));rng.shuffle(perm)
            used=collections.Counter();cipher=[]
            for c in plain:cipher.append(perm[keys[c][used[c]%len(keys[c])]]);used[c]+=1
            assert len(set(cipher))==K
            at=0;new=[]
            for f in fs:new.append(cipher[at:at+len(f)]);at+=len(f)
            cases[tag+f'_control{k}']={'frags':new,'plain':plain,'N':N,'K':K}
    (G/'cases.json').write_text(json.dumps(cases,indent=2)+'\n');results={}
    # Controls precede target. Do not interpret a failed target if controls fail.
    for name in sorted(cases,key=lambda x: ('target' in x,x)):
        c=cases[name]
        if name.endswith('target'):
            tag=name[:-7]
            assert all(results[tag+f'_control{i}']['correct']/results[tag+f'_control{i}']['N']>=.98 for i in range(3))
        (G/(name+'.seq')).write_text('\n'.join(' '.join(map(str,f))+' -1' for f in c['frags'])+'\n')
        subprocess.run([str(G/'solve'),str(D/'lm.bin'),str(G/(name+'.seq')),'150','50000','2','731',str(G/(name+'.tsv'))],check=True)
        sc,key,read=(G/(name+'.tsv')).read_text().splitlines()[0].split('\t')
        v={'score':float(sc),'key':key,'reading':read,'N':c['N'],'K':c['K']}
        if 'plain' in c:v['correct']=sum(x==y for x,y in zip(read.replace('|',''),c['plain']))
        results[name]=v;print(name,sc,v.get('correct'),flush=True)
    (G/'results.json').write_text(json.dumps(results,indent=2)+'\n');jobs=[]
    for tag in ['null20','null20_22']:
        fs=cases[tag+'_target']['frags'];flat=sum(fs,[])
        for s in range(20):
            a=flat.copy();random.Random(270932+s).shuffle(a);at=0;seq=[]
            for f in fs:seq+=a[at:at+len(f)]+[-1];at+=len(f)
            name=f'{tag}_shuffle{s:02d}';(G/(name+'.seq')).write_text(' '.join(map(str,seq))+'\n');jobs.append(name)
    shuffle_run(G,jobs,True)

def verify_all():
    lm=np.fromfile(D/'lm.bin',dtype=np.float32);offset=[0];at=0;out={}
    for n in range(1,6):offset.append(at);at+=24**n
    for directory in [D,OUT/'glyph_null']:
        checks=[]
        for path in sorted(directory.glob('*.tsv')):
            seq=list(map(int,path.with_suffix('.seq').read_text().split()))
            sc,key,read=path.read_text().splitlines()[0].split('\t');ctx=[];s=0
            for v in seq:
                if v<0:ctx=[];continue
                ctx=(ctx+[ALPHA.index(key[v])])[-5:];z=0
                for a in ctx:z=z*24+a
                s+=float(lm[offset[len(ctx)]+z])
            assert abs(s-float(sc))<1e-7
            assert read==''.join('|' if x<0 else key[x] for x in seq)
            if directory==D:
                for x,y in [(0,19),(19,28),(28,37)]:assert len(set(key[x:y]))==y-x
            else:assert max(collections.Counter(key).values())<=2
            checks.append({'name':path.stem,'score':s,'delta':s-float(sc)})
        out[directory.name]=checks
    (OUT/'verification.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    prepare();run('control',150,50000)
    controls=json.loads((D/'results.json').read_text())
    assert all(controls[f'control{i}']['correct']==controls[f'control{i}']['N'] for i in range(3))
    run('target',150,50000);coordinate_nulls();glyph_run();verify_all()

```
