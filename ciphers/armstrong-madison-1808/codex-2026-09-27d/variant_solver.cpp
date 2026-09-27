#include <bits/stdc++.h>
using namespace std;
// Jointly choose a homophonic alphabet and only the listed local glyph readings.
int main(int argc,char**argv){
 if(argc!=10&&argc!=11){cerr<<"model seq alt mode restarts iterations penalty seed output [prior]\n";return 1;}
 const int A=24;string alpha="abcdefghiklmnopqrstuwxyz";
 vector<float> lm(A+A*A+A*A*A+A*A*A*A);ifstream mf(argv[1],ios::binary);mf.read((char*)lm.data(),lm.size()*4);if(!mf)return 2;
 vector<int> orig;int t,K=0;ifstream sf(argv[2]);while(sf>>t){orig.push_back(t);K=max(K,t+1);}
 vector<int> pos;vector<vector<int>> options;ifstream af(argv[3]);string line;
 while(getline(af,line)){stringstream ss(line);int p;string vals;ss>>p>>vals;if(vals.empty())continue;pos.push_back(p);replace(vals.begin(),vals.end(),',',' ');stringstream vs(vals);vector<int> op;while(vs>>t){op.push_back(t);K=max(K,t+1);}if(op.empty()||op[0]!=orig.at(p))return 3;options.push_back(op);}
 bool soft=string(argv[4])=="soft";int R=stoi(argv[5]),I=stoi(argv[6]);double penalty=stod(argv[7]);mt19937 rng(stoul(argv[8]));uniform_real_distribution<double>U(0,1);
 vector<vector<int>> parents;
 if(argc==11){ifstream pf(argv[10]);while(getline(pf,line)){stringstream ss(line);string score,key;getline(ss,score,'\t');getline(ss,key,'\t');if((int)key.size()!=K)return 4;vector<int> k;for(char c:key){int x=alpha.find(c);if(x<0||x>=A)return 5;k.push_back(x);}parents.push_back(k);}}
 auto score=[&](const vector<int>&seq,const vector<int>&key,int changes){double s=-penalty*changes;int n=0,a=0,b=0,c=0;for(int x:seq){if(x<0){n=0;continue;}int d=key[x];int idx=n==0?d:n==1?A+a*A+d:n==2?A+A*A+(a*A+b)*A+d:A+A*A+A*A*A+((a*A+b)*A+c)*A+d;s+=lm[idx];if(n==0)a=d;else if(n==1)b=d;else if(n==2)c=d;else{a=b;b=c;c=d;}n++;}return s;};
 struct Candidate{double s;vector<int> key,seq;};vector<Candidate> all;
 for(int r=0;r<R;r++){
  vector<int> key(K),count(A),seq=orig;
  for(int&i:key){do{i=rng()%A;}while(count[i]>=2);count[i]++;}
  if(!parents.empty()&&r%2==0){key=parents[rng()%parents.size()];fill(count.begin(),count.end(),0);for(int i:key)count[i]++;for(int n=0;n<5;n++){int i=rng()%K,v=rng()%A;if(count[v]>=2)continue;count[key[i]]--;key[i]=v;count[v]++;}}
  int changes=0;double cur=score(seq,key,changes),best=cur;vector<int> bk=key,bs=seq;
  for(int it=0;it<I;it++){
   bool transcription=soft&&!pos.empty()&&U(rng)<.20;int i,j=-1,old,nv,oldchanges=changes;
   if(transcription){int a=rng()%pos.size();i=pos[a];old=seq[i];nv=options[a][rng()%options[a].size()];if(old==nv)continue;changes+=(nv!=orig[i])-(old!=orig[i]);seq[i]=nv;}
   else{i=rng()%K;old=key[i];if(U(rng)<.60){j=rng()%K;nv=key[j];if(nv==old)continue;swap(key[i],key[j]);}else{nv=rng()%A;if(nv==old||count[nv]>=2)continue;key[i]=nv;count[old]--;count[nv]++;}}
   double next=score(seq,key,changes),temp=2.5*pow(.02/2.5,double(it)/I);
   if(next>=cur||U(rng)<exp((next-cur)/temp)){cur=next;if(cur>best){best=cur;bk=key;bs=seq;}}
   else if(transcription){seq[i]=old;changes=oldchanges;}
   else if(j>=0)swap(key[i],key[j]);else{key[i]=old;count[old]++;count[nv]--;}
  }
  all.push_back({best,bk,bs});
 }
 sort(all.begin(),all.end(),[](const auto&a,const auto&b){return a.s>b.s;});ofstream out(argv[9]);
 for(int i=0;i<min(20,(int)all.size());i++){
  auto&c=all[i];out<<setprecision(12)<<c.s<<'\t';for(int v:c.key)out<<alpha[v];out<<'\t';
  for(int v:c.seq)out<<(v<0?'|':alpha[c.key[v]]);out<<'\t';bool first=true;
  for(int p:pos)if(c.seq[p]!=orig[p]){if(!first)out<<',';out<<p<<':'<<c.seq[p];first=false;}out<<'\n';
 }
 cerr<<argv[2]<<' '<<argv[4]<<" best="<<all[0].s<<'\n';
}
