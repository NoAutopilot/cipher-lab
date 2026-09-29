/* climb_fast.c -- HARNESS-2 (29 Sept 2026): the harness reference climber, selftest_climb.py's algorithm in C with
   an incremental score (same moves, pool, temperature schedule and acceptance rule; its own RNG, so keys differ from
   the Python version seed for seed). Input on stdin: K N, N sign ids, 26^4 log10 quadgram table, pool string,
   restarts iters seed. Output: K letters. Used only as the refit-null fitter in the harness self-test. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
static unsigned long long rs;
static inline unsigned long long rnd(void){ rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void){ return (rnd() >> 11) * (1.0 / 9007199254740992.0); }
int main(void){
  int K, N; if(scanf("%d %d",&K,&N)!=2) return 1;
  int *seq=malloc(sizeof(int)*N); for(int i=0;i<N;i++) if(scanf("%d",&seq[i])!=1) return 2;
  float *Q=malloc(sizeof(float)*456976); for(long i=0;i<456976;i++) if(scanf("%f",&Q[i])!=1) return 3;
  char pool[512]; if(scanf("%511s",pool)!=1) return 4; int np=strlen(pool);
  int R; long IT; unsigned long long seed; if(scanf("%d %ld %llu",&R,&IT,&seed)!=3) return 5;
  rs = 0x9E3779B97F4A7C15ULL ^ (seed*2654435761ULL); if(!rs) rs=1;
  const char *alt="abcdefghijlmnopqrstuvxyz"; int na=strlen(alt);
  /* per sign: list of unique window starts touching it */
  int *cnt=calloc(K,sizeof(int)); int nw = N>=4 ? N-3 : 0;
  int **w=malloc(sizeof(int*)*K); int *nwk=calloc(K,sizeof(int));
  for(int s=0;s<K;s++) w[s]=malloc(sizeof(int)*(4*N+1));
  for(int i=0;i<nw;i++){ int seen[4]={-1,-1,-1,-1}; for(int j=0;j<4;j++){ int s=seq[i+j]; int dup=0; for(int t=0;t<j;t++) if(seen[t]==s) dup=1; seen[j]=s; if(!dup) w[s][nwk[s]++]=i; } }
  int *k=malloc(sizeof(int)*K), *best=malloc(sizeof(int)*K); double ball=-1e300;
  #define WS(i) Q[((k[seq[i]]*26+k[seq[i+1]])*26+k[seq[i+2]])*26+k[seq[i+3]]]
  for(int r=0;r<R;r++){
    for(int s=0;s<K;s++) k[s]=pool[rnd()%np]-'a';
    double cur=0; for(int i=0;i<nw;i++) cur+=WS(i);
    double T=2.0;
    for(long it=0;it<IT;it++){
      int j=rnd()%K; int old=k[j]; double before=0; for(int t=0;t<nwk[j];t++) before+=WS(w[j][t]);
      k[j] = (urand()<0.3) ? alt[rnd()%na]-'a' : pool[rnd()%np]-'a';
      double after=0; for(int t=0;t<nwk[j];t++) after+=WS(w[j][t]);
      double nw_=cur-before+after;
      if(nw_>=cur || urand()<exp((nw_-cur)/T)) cur=nw_; else k[j]=old;
      T = 2.0*(1.0-(double)it/IT); if(T<0.05) T=0.05;
    }
    if(cur>ball){ ball=cur; memcpy(best,k,sizeof(int)*K); }
  }
  for(int s=0;s<K;s++) putchar('a'+best[s]); putchar('\n'); printf("%f\n", ball/(nw>0?nw:1));
  return 0;
}
