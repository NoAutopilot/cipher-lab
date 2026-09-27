// Exhaustive fixed-width decimal digit/position renumbering screen.
// No proposed plaintext is licensed by score alone. See REPORT.md.
#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
struct Hit {double score;int hits,oor;string key;bool operator<(const Hit&o)const{return score>o.score;}};
int main(int argc,char**argv){
 if(argc!=5){cerr<<"usage: renumber table-prefix sequence-file mode output-file\n";return 1;}
 string pref=argv[1],mode=argv[3];vector<float> lm(2001*2001);ifstream bin(pref+".bin",ios::binary);bin.read((char*)lm.data(),lm.size()*sizeof(float));if(!bin){cerr<<"bad model";return 2;}
 bool known[2001]={};ifstream kf(pref+".known");int v;while(kf>>v)known[v]=true;
 vector<int>seq;ifstream sf(argv[2]);while(sf>>v)seq.push_back(v);vector<int>uni=seq;sort(uni.begin(),uni.end());uni.erase(unique(uni.begin(),uni.end()),uni.end());uni.erase(remove(uni.begin(),uni.end(),-1),uni.end());
 int freq[10000]={};for(int c:seq)if(c>=0)freq[c]++;sort(uni.begin(),uni.end(),[&](int a,int b){return freq[a]>freq[b];});
 int dec[10000];fill(dec,dec+10000,-1);priority_queue<Hit> top;long long tested=0,scored=0;
 auto evaluate=[&](const string&key){tested++;int hits=0,oor=0;for(int c:uni){int d=dec[c];if(d<1||d>1600)oor+=freq[c];else if(known[d])hits+=freq[c];if(oor>20)return;}
 if(hits<120)return;scored++;double score=0;for(int i=1;i<(int)seq.size();i++){if(seq[i]<0||seq[i-1]<0)continue;int a=dec[seq[i-1]],b=dec[seq[i]];if(a>=1&&a<=2000&&b>=1&&b<=2000)score+=lm[a*2001+b];}
 if(top.size()<20||score>top.top().score){top.push({score,hits,oor,key});if(top.size()>20)top.pop();}};
 if(mode=="digits"){
 array<int,4>pos={0,1,2,3};do{
  vector<array<int,4>> ds;for(int c:uni){array<int,4>a={c/1000,c/100%10,c/10%10,c%10};ds.push_back({a[pos[0]],a[pos[1]],a[pos[2]],a[pos[3]]});}
  array<int,10>p={0,1,2,3,4,5,6,7,8,9};do{
   tested++;int hits=0,oor=0;bool skip=false;for(int j=0;j<(int)uni.size();j++){auto a=ds[j];int d=1000*p[a[0]]+100*p[a[1]]+10*p[a[2]]+p[a[3]];dec[uni[j]]=d;if(d<1||d>1600)oor+=freq[uni[j]];else if(known[d])hits+=freq[uni[j]];if(oor>20){skip=true;break;}}
   if(skip||hits<120)continue;scored++;double score=0;for(int i=1;i<(int)seq.size();i++){if(seq[i]<0||seq[i-1]<0)continue;int a=dec[seq[i-1]],b=dec[seq[i]];if(a>=1&&a<=2000&&b>=1&&b<=2000)score+=lm[a*2001+b];}
   if(top.size()<20||score>top.top().score){string key="positions=";for(int z:pos)key+=char('0'+z);key+=" digits=";for(int z:p)key+=char('0'+z);top.push({score,hits,oor,key});if(top.size()>20)top.pop();}
  }while(next_permutation(p.begin(),p.end()));
 }while(next_permutation(pos.begin(),pos.end()));
 }else if(mode=="affine"){
  for(int n:{1600,1700,1900,2000})for(int a=1;a<n;a++){if(n<*max_element(seq.begin(),seq.end())||__gcd(a,n)!=1)continue;for(int b=0;b<n;b++){
   for(int c:uni)dec[c]=(a*(c-1)+b)%n+1;evaluate("mod="+to_string(n)+" a="+to_string(a)+" b="+to_string(b));}}
 }else if(mode=="grid"){
  for(int n:{1600,1700,1900,2000})for(int cols=2;cols<=200;cols++)if(n>=*max_element(seq.begin(),seq.end())&&n%cols==0)for(int rev=0;rev<4;rev++)for(int off=0;off<n;off++){
   for(int c:uni){int x=(c-1+off)%n,rr=x/cols,cc=x%cols;if(rev&1)rr=n/cols-1-rr;if(rev&2)cc=cols-1-cc;dec[c]=cc*(n/cols)+rr+1;}
   evaluate("grid="+to_string(n)+" cols="+to_string(cols)+" rev="+to_string(rev)+" offset="+to_string(off));}
 }
 vector<Hit>hits;while(top.size()){hits.push_back(top.top());top.pop();}reverse(hits.begin(),hits.end());ofstream o(argv[4]);o<<"score\thits\tout_of_range\ttransform\n";for(auto h:hits)o<<h.score<<'\t'<<h.hits<<'\t'<<h.oor<<'\t'<<h.key<<'\n';cerr<<"tested "<<tested<<" scored "<<scored<<" best "<<(hits.empty()?0:hits[0].score)<<'\n';
}
