/* hsolve.c -- DEB-SWARM-B homophonic letter-substitution annealer (English quadgrams + unigram KL term).
 *
 * Usage: hsolve MODEL.bin CIPHER.txt RESTARTS ITERS SEED BETA [T0] [FIXFILE]
 *   MODEL.bin : 26^4 floats (log10 P(quadgram)), then 26 floats (unigram P), written by build_model.py
 *   CIPHER.txt: first line "K N", then N ints (sign ids 0..K-1, or -1 for an unread box / text break)
 *   BETA      : weight of the N*KL(plain unigram || English unigram) penalty (natural-log units, scaled to log10)
 *   FIXFILE   : optional lines "sign letter" (0-25) held fixed (letter -1 = null: the sign is dropped as a gap)
 * Output (stdout): per restart one line "R score"; at the end "BEST score" and "KEY k0 k1 ... kK-1" (letters 0-25).
 * Score = sum over every window of 4 consecutive non-gap positions of log10 P(quadgram) - BETA*N*KL.
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#ifndef A
#define A 26
#endif
#ifndef ORD
#define ORD 4
#endif
#define TSZ ((long)A*A*A*A*(ORD==5?A:1))

static float *Q; static double U[A];
static int K, N, *C, *key, *bestkey, *fixed;
static int **wins, *nwins; /* per sign: unique window starts touching it */
static int nvalid; static int *valid; /* window start valid? */
static unsigned long long rs;
static inline unsigned rnd(void){ rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return (unsigned)(rs >> 11); }
static inline double urand(void){ return (rnd() & 0xFFFFFF) / (double)0x1000000; }
static int cnt[A]; static int mult[4096];

static inline double wscore(int s){ long id=0; for(int j=0;j<ORD;j++) id=id*A+key[C[s+j]]; return Q[id]; }
static double klpen(void){ int tot=0; for(int i=0;i<A;i++) tot+=cnt[i]; double kl=0; for(int i=0;i<A;i++) if(cnt[i]){ double p=(double)cnt[i]/tot; kl+=p*log(p/U[i]); } return kl*tot/log(10.0); }
static double full(void){ double s=0; for(int i=0;i+ORD-1<N;i++) if(valid[i]) s+=wscore(i); return s; }

int main(int argc, char **argv){
  if(argc<7){ fprintf(stderr,"usage\n"); return 2; }
  FILE *f=fopen(argv[1],"rb"); Q=malloc(sizeof(float)*TSZ); if(fread(Q,sizeof(float),TSZ,f)!=TSZ) return 3;
  float u[A]; if(fread(u,sizeof(float),A,f)!=A) return 3; for(int i=0;i<A;i++) U[i]=u[i]; fclose(f);
  { char*e=getenv("HS_ROBUST"); double q= e? atof(e):0; if(q>0) for(long i=0;i<TSZ;i++) Q[i]=(float)log10((1-q)*pow(10,Q[i])+q/(double)A); }
  f=fopen(argv[2],"r"); if(fscanf(f,"%d %d",&K,&N)!=2) return 4; C=malloc(sizeof(int)*N);
  for(int i=0;i<N;i++) if(fscanf(f,"%d",&C[i])!=1) return 4; fclose(f);
  int R=atoi(argv[3]); long IT=atol(argv[4]); rs=0x9E3779B97F4A7C15ULL ^ (unsigned long long)atoll(argv[5])*2654435761ULL; if(!rs) rs=1;
  double BETA=atof(argv[6]); double T0 = argc>7 ? atof(argv[7]) : 1.5;
  fixed=malloc(sizeof(int)*K); for(int i=0;i<K;i++) fixed[i]=-2;
  if(argc>8){ f=fopen(argv[8],"r"); int s,l; while(fscanf(f,"%d %d",&s,&l)==2) if(s>=0&&s<K) fixed[s]=l; fclose(f); }
  /* nulls: fixed -1 -> turn into gaps */
  for(int i=0;i<N;i++) if(C[i]>=0 && fixed[C[i]]==-1) C[i]=-1;
  valid=calloc(N,sizeof(int)); for(int i=0;i+ORD-1<N;i++){ valid[i]=1; for(int j=0;j<ORD;j++) if(C[i+j]<0) valid[i]=0; }
  memset(mult,0,sizeof(mult)); for(int i=0;i<N;i++) if(C[i]>=0) mult[C[i]]++;
  wins=malloc(sizeof(int*)*K); nwins=calloc(K,sizeof(int)); int *mark=calloc(N,sizeof(int)); int stamp=0;
  for(int s=0;s<K;s++){ stamp++; wins[s]=malloc(sizeof(int)*(ORD*mult[s]+1)); for(int i=0;i<N;i++) if(C[i]==s) for(int j=i-ORD+1;j<=i;j++) if(j>=0&&j+ORD-1<N&&valid[j]&&mark[j]!=stamp){ mark[j]=stamp; wins[s][nwins[s]++]=j; } }
  int *free_s=malloc(sizeof(int)*K), nf=0; for(int s=0;s<K;s++) if(mult[s]>0 && fixed[s]<0 && fixed[s]!=-1) free_s[nf++]=s;
  key=malloc(sizeof(int)*K); bestkey=malloc(sizeof(int)*K); double best=-1e300;
  /* cumulative English unigram for random letter draws */
  double cu[A]; double acc=0; for(int i=0;i<A;i++){ acc+=U[i]; cu[i]=acc; }
  for(int r=0;r<R;r++){
    for(int s=0;s<K;s++){ if(fixed[s]>=0) key[s]=fixed[s]; else { double x=urand()*acc; int l=0; while(l<A-1&&cu[l]<x) l++; key[s]=l; } }
    memset(cnt,0,sizeof(cnt)); for(int s=0;s<K;s++) cnt[key[s]]+=mult[s];
    double ng=full(), kp=klpen(), cur=ng-BETA*kp, rbest=cur;
    for(long it=0; it<IT; it++){
      double T=T0*(1.0-(double)it/IT); if(T<1e-4) T=1e-4;
      int s=free_s[rnd()%nf]; int old=key[s]; int nl;
      if(rnd()&1){ double x=urand()*acc; nl=0; while(nl<A-1&&cu[nl]<x) nl++; } else nl=rnd()%A;
      if(nl==old) continue;
      double d=0; for(int w=0;w<nwins[s];w++) d-=wscore(wins[s][w]);
      key[s]=nl; for(int w=0;w<nwins[s];w++) d+=wscore(wins[s][w]);
      cnt[old]-=mult[s]; cnt[nl]+=mult[s]; double nkp=klpen();
      double nd = d - BETA*(nkp-kp);
      if(nd>=0 || urand()<exp(nd/T)){ ng+=d; kp=nkp; cur=ng-BETA*kp; if(cur>rbest) rbest=cur; }
      else { key[s]=old; cnt[old]+=mult[s]; cnt[nl]-=mult[s]; }
    }
    /* final greedy polish */
    int improved=1; while(improved){ improved=0; for(int q=0;q<nf;q++){ int s=free_s[q]; int old=key[s]; int bl=old; double bd=0;
      for(int nl=0;nl<A;nl++){ if(nl==old) continue; double d=0; for(int w=0;w<nwins[s];w++) d-=wscore(wins[s][w]); key[s]=nl; for(int w=0;w<nwins[s];w++) d+=wscore(wins[s][w]); key[s]=old;
        cnt[old]-=mult[s]; cnt[nl]+=mult[s]; double nkp=klpen(); cnt[old]+=mult[s]; cnt[nl]-=mult[s]; double nd=d-BETA*(nkp-kp); if(nd>bd+1e-9){ bd=nd; bl=nl; } }
      if(bl!=old){ double d=0; for(int w=0;w<nwins[s];w++) d-=wscore(wins[s][w]); key[s]=bl; for(int w=0;w<nwins[s];w++) d+=wscore(wins[s][w]); cnt[old]-=mult[s]; cnt[bl]+=mult[s]; ng+=d; kp=klpen(); improved=1; } } }
    cur=ng-BETA*kp;
    printf("R %d %.3f\n", r, cur);
    if(cur>best){ best=cur; memcpy(bestkey,key,sizeof(int)*K); }
  }
  printf("BEST %.3f\nKEY", best); for(int s=0;s<K;s++) printf(" %d", bestkey[s]); printf("\n");
  return 0;
}
