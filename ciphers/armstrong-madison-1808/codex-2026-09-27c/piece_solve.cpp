#include <bits/stdc++.h>
using namespace std;
// Fixed code value -> one letter or one digraph. At most two homophones per piece.
int main(int argc,char**argv){
 if(argc!=9&&argc!=10){cerr<<"usage: model pieces sequence restarts iterations bonus output seed [prior-output]\n";return 1;}
 const int A=24;string alpha="abcdefghiklmnopqrstuwxyz";
 vector<float> lm(A+A*A+A*A*A+A*A*A*A);ifstream in(argv[1],ios::binary);in.read((char*)lm.data(),lm.size()*4);if(!in)return 2;
 ifstream pf(argv[2]);vector<string> names;vector<vector<int>> pieces;string x;
 while(pf>>x){vector<int> p;for(char c:x){auto at=alpha.find(c);if(at==string::npos)return 3;p.push_back(at);}pieces.push_back(p);names.push_back(x);}
 ifstream sf(argv[3]);vector<int> seq;int t,K=0;while(sf>>t){seq.push_back(t);K=max(K,t+1);}
 int M=pieces.size(),restarts=stoi(argv[4]),iterations=stoi(argv[5]);double bonus=stod(argv[6]);if(K==0||K>2*M)return 4;
 mt19937 rng(stoul(argv[8]));uniform_real_distribution<double>U(0,1);
 vector<vector<int>> prior;
 if(argc==10){ifstream old(argv[9]);string line;while(getline(old,line)){
  auto begin=line.find('\t'),end=line.find('\t',begin+1);if(begin==string::npos||end==string::npos)return 5;
  stringstream ss(line.substr(begin+1,end-begin-1));vector<int> k;string p;
  while(getline(ss,p,',')){auto at=find(names.begin(),names.end(),p);if(at==names.end())return 6;k.push_back(at-names.begin());}
  if((int)k.size()!=K)return 7;prior.push_back(k);
 }}
 auto score=[&](const vector<int>&key){double score=0;int n=0,a=0,b=0,c=0;for(int t:seq){if(t<0){n=0;continue;}for(int d:pieces[key[t]]){
   int idx=n==0?d:n==1?A+a*A+d:n==2?A+A*A+(a*A+b)*A+d:A+A*A+A*A*A+((a*A+b)*A+c)*A+d;
   score+=lm[idx]+bonus;if(n==0)a=d;else if(n==1)b=d;else if(n==2)c=d;else{a=b;b=c;c=d;}n++;
 }}return score;};
 vector<pair<double,vector<int>>> bests;
 for(int r=0;r<restarts;r++){
  vector<int> key(K),counts(M);for(int&i:key){do{i=rng()%M;}while(counts[i]>=2);counts[i]++;}
  if(!prior.empty()&&r%2==0){key=prior[rng()%prior.size()];fill(counts.begin(),counts.end(),0);for(int i:key)counts[i]++;
   for(int j=0;j<5;j++){int i=rng()%K,v=rng()%M;if(counts[v]>=2)continue;counts[key[i]]--;key[i]=v;counts[v]++;}
  }
  double cur=score(key),best=cur;vector<int> saved=key;
  for(int it=0;it<iterations;it++){
   int i=rng()%K,j=-1,old=key[i],next;
   if(U(rng)<.60){j=rng()%K;next=key[j];if(next==old)continue;swap(key[i],key[j]);}
   else{next=rng()%M;if(next==old||counts[next]>=2)continue;key[i]=next;counts[old]--;counts[next]++;}
   double val=score(key),temp=3*pow(.015/3,double(it)/iterations);
   if(val>=cur||U(rng)<exp((val-cur)/temp)){cur=val;if(cur>best){best=cur;saved=key;}}
   else if(j>=0)swap(key[i],key[j]);else{key[i]=old;counts[old]++;counts[next]--;}
  }
  bests.push_back({best,saved});
 }
 sort(bests.begin(),bests.end(),[](auto&a,auto&b){return a.first>b.first;});ofstream out(argv[7]);
 for(int i=0;i<min(20,(int)bests.size());i++){
  auto &b=bests[i];out<<setprecision(10)<<b.first<<'\t';for(int j=0;j<K;j++)out<<(j?",":"")<<names[b.second[j]];out<<'\t';
  for(int t:seq)out<<(t<0?"|":names[b.second[t]]);out<<'\n';
 }
 cerr<<"K="<<K<<" best="<<bests[0].first<<'\n';
}
