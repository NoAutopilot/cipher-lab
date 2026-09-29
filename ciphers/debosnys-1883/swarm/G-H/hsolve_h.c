/* Homophonic annealer with optional known word spaces (group H, Copiale-method replication).
   usage: hsolve_h LM.bin CIPHER.txt RESTARTS ITERS SEED [FIXED.txt]
   CIPHER.txt: one integer per token: -1 = word space (fixed), 0..K-1 = sign id.
   LM.bin: float32 log P(d|abc), 27^4, symbols a-z=0..25, space=26.
   Each sign maps to one letter 0..25. Score = sum over positions of log P(x_i | x_{i-3..i-1}), with space tokens
   as symbol 26 (contexts padded with space). Prints: best score per char, then K letters (a-z) for the best key.
   FIXED.txt (optional): lines "sign letter" pinning a sign ('-' for none).
   INIT.txt (optional 7th arg): sign ids that start as word space; with env HS_SPACE=1 any sign may take the
   value space (27 values), so the space class is found by the solve itself. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define A 27
static float *lm; static int n, K; static int *tok; static int *pos_start, *pos_list;
static unsigned long long rs;
static inline unsigned long long rnd(void){ rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void){ return (rnd() >> 11) * (1.0/9007199254740992.0); }
static int key[4096], best[4096], fixed[4096];
static int NV=26; static int initsp[4096];
static inline int sym(int i){ if(i<0) return 26; int t=tok[i]; return t<0?26:key[t]; }
static inline double term(int i){ int a=sym(i-3),b=sym(i-2),c=sym(i-1),d=sym(i); return lm[((a*A+b)*A+c)*A+d]; }
double total(void){ double s=0; for(int i=0;i<n;i++) s+=term(i); return s; }
static int *mark; static int stamp=1;
double local(int s){ /* sum of terms touched by sign s */
  double v=0; stamp++;
  for(int j=pos_start[s];j<pos_start[s+1];j++){ int p=pos_list[j];
    for(int i=p;i<p+4 && i<n;i++){ if(mark[i]!=stamp){ mark[i]=stamp; v+=term(i);} } }
  return v; }
int main(int argc,char**argv){
  if(argc<6){fprintf(stderr,"usage\n");return 1;}
  lm=malloc(sizeof(float)*A*A*A*A); FILE*f=fopen(argv[1],"rb"); if(fread(lm,sizeof(float),A*A*A*A,f)!=A*A*A*A){fprintf(stderr,"lm\n");return 1;} fclose(f);
  f=fopen(argv[2],"r"); int cap=1<<20; tok=malloc(sizeof(int)*cap); n=0; K=0; int x;
  while(fscanf(f,"%d",&x)==1){ tok[n++]=x; if(x+1>K) K=x+1; } fclose(f);
  int R=atoi(argv[3]); long I=atol(argv[4]); rs=0x9E3779B97F4A7C15ULL^(unsigned long long)atol(argv[5])*2654435761ULL; if(!rs) rs=1;
  for(int s=0;s<K;s++) fixed[s]=-1;
  if(getenv("HS_SPACE")) NV=27;
  if(argc>7){ f=fopen(argv[7],"r"); int s; while(fscanf(f,"%d",&s)==1) if(s<4096) initsp[s]=1; fclose(f);}
  if(argc>6 && strcmp(argv[6],"-")){ f=fopen(argv[6],"r"); int s; char c; while(fscanf(f,"%d %c",&s,&c)==2) if(s<K) fixed[s]=c-'a'; fclose(f);}
  pos_start=calloc(K+2,sizeof(int)); pos_list=malloc(sizeof(int)*n); mark=calloc(n+8,sizeof(int));
  for(int i=0;i<n;i++) if(tok[i]>=0) pos_start[tok[i]+1]++;
  for(int s=0;s<K;s++) pos_start[s+1]+=pos_start[s];
  int *fill=calloc(K+1,sizeof(int));
  for(int i=0;i<n;i++) if(tok[i]>=0){ int s=tok[i]; pos_list[pos_start[s]+fill[s]++]=i; }
  int *active=malloc(sizeof(int)*K), na=0; for(int s=0;s<K;s++) if(pos_start[s+1]>pos_start[s] && fixed[s]<0) active[na++]=s;
  static const double fr[26]={8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,.15,.77,4.0,2.4,6.7,7.5,1.9,.1,6.0,6.3,9.1,2.8,1.0,2.4,.15,2.0,.07};
  double bestall=-1e300;
  for(int r=0;r<R;r++){
    for(int s=0;s<K;s++){ if(fixed[s]>=0){key[s]=fixed[s];continue;} double u=urand()*100,c=0; int L=0; for(;L<25;L++){c+=fr[L]; if(u<c)break;} key[s]=L; if(initsp[s]) key[s]=26; }
    double cur=total(), rb=cur; int rkey[4096]; memcpy(rkey,key,sizeof(int)*K);
    double T0=2.0*(n/1000.0+0.5), T;
    for(long it=0; it<I && na>0; it++){
      T=T0*(1.0-(double)it/I)+1e-3;
      int s=active[rnd()%na]; int old=key[s]; int nw=rnd()%NV; if(nw==old) continue;
      double before=local(s); key[s]=nw; double after=local(s); double d=after-before;
      if(d>=0 || urand()<exp(d/T)){ cur+=d; if(cur>rb){rb=cur; memcpy(rkey,key,sizeof(int)*K);} }
      else key[s]=old;
    }
    if(rb>bestall){ bestall=rb; memcpy(best,rkey,sizeof(int)*K); }
  }
  memcpy(key,best,sizeof(int)*K);
  printf("%.6f\n", total()/n);
  for(int s=0;s<K;s++) putchar(best[s]==26?'_':'a'+best[s]); putchar('\n');
  return 0; }
