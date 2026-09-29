/* hsa.c -- homophonic substitution annealer for DEB-SWARM-G (29 Sept 2026).
   usage: hsa MODEL.bin CIPHER.txt RESTARTS ITERS SEED KLW [FIXED.txt]
   MODEL.bin: 26 float unigram logp, then 26^4 float log P(d|abc) (conditional quadgram, interpolated).
   CIPHER.txt: first line "N K", then N ints (sign ids 0..K-1).
   Score = sum_i log P(x_i | x_{i-3..i-1}) (i>=3) - KLW * N * KL(obs letter dist || corpus unigram).
   Env HSA_PERTURB=p: restarts after the first start from the best key so far with a share p of signs re-drawn
   (iterated local search); HSA_T0=f scales their start temperature.
   Prints per restart: "R score" and finally "BEST score" then K letters (a-z) one line. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
static float uni[26]; static float *q;
static int N,K,*c,*key,*best,*cnt,**occ,*nocc;
static int *touch; static int *mark;
static double klw;
static unsigned long long rs;
static inline unsigned long long rnd(void){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
static inline double urand(void){return (rnd()>>11)*(1.0/9007199254740992.0);}
static inline float w4(int i){ /* quadgram term ending at i */
  return q[((key[c[i-3]]*26+key[c[i-2]])*26+key[c[i-1]])*26+key[c[i]]]; }
static double klterm(void){ double s=0; for(int a=0;a<26;a++) if(cnt[a]){double p=(double)cnt[a]/N; s+=cnt[a]*(log(p)-uni[a]);} return s; }
static double full(void){ double s=0; for(int i=3;i<N;i++) s+=w4(i); return s - klw*klterm(); }
int main(int argc,char**argv){
  if(argc<7){fprintf(stderr,"usage\n");return 1;}
  FILE*f=fopen(argv[1],"rb"); fread(uni,4,26,f); q=malloc(4*456976); fread(q,4,456976,f); fclose(f);
  f=fopen(argv[2],"r"); fscanf(f,"%d %d",&N,&K); c=malloc(4*N); for(int i=0;i<N;i++) fscanf(f,"%d",&c[i]); fclose(f);
  int R=atoi(argv[3]); long IT=atol(argv[4]); rs=strtoull(argv[5],0,10)*2654435761ULL+88172645463325252ULL; klw=atof(argv[6]);
  int *fixed=calloc(K,4); for(int s=0;s<K;s++) fixed[s]=-1;
  if(argc>7){ f=fopen(argv[7],"r"); int s; char l; while(fscanf(f,"%d %c",&s,&l)==2) fixed[s]=l-'a'; fclose(f);}
  key=malloc(4*K); best=malloc(4*K); cnt=calloc(26,4);
  nocc=calloc(K,4); occ=malloc(sizeof(int*)*K); mark=calloc(N,4); touch=malloc(4*N*4+16);
  /* per sign, list of quadgram end positions affected */
  for(int s=0;s<K;s++) occ[s]=malloc(4*(4*N+4));
  for(int s=0;s<K;s++){ int n=0; for(int i=0;i<N;i++) if(c[i]==s) for(int j=i;j<i+4&&j<N;j++) if(j>=3){ int dup=0; for(int t=0;t<n;t++) if(occ[s][t]==j){dup=1;break;} if(!dup) occ[s][n++]=j; } nocc[s]=n; }
  int *signcount=calloc(K,4); for(int i=0;i<N;i++) signcount[c[i]]++;
  double gbest=-1e300; double perturb = getenv("HSA_PERTURB") ? atof(getenv("HSA_PERTURB")) : 0; /* iterated restarts: keep best key, re-draw this share */
  double t0f = getenv("HSA_T0") ? atof(getenv("HSA_T0")) : 1.0;
  /* letter sampling from unigram */
  double cum[26]; double tot=0; for(int a=0;a<26;a++){tot+=exp(uni[a]); cum[a]=tot;}
  for(int r=0;r<R;r++){
    memset(cnt,0,4*26);
    for(int s=0;s<K;s++){ if(fixed[s]>=0) key[s]=fixed[s]; else if(perturb>0 && r>0 && urand()>perturb) key[s]=best[s]; else { double u=urand()*tot; int a=0; while(a<25&&cum[a]<u) a++; key[s]=a; } }
    for(int i=0;i<N;i++) cnt[key[c[i]]]++;
    double sc=full(), rb=sc; int *rbest=malloc(4*K); memcpy(rbest,key,4*K);
    double T0=(N*0.02+1.0)*((perturb>0&&r>0)?t0f:1.0), T1=0.02;
    for(long it=0;it<IT;it++){
      double T=T0*pow(T1/T0,(double)it/IT);
      int s=rnd()%K; if(fixed[s]>=0) continue;
      int old=key[s], nw;
      int swap = (rnd()%5==0); int s2=-1;
      if(swap){ s2=rnd()%K; if(s2==s||fixed[s2]>=0||key[s2]==old) continue; nw=key[s2]; }
      else { nw=rnd()%26; if(nw==old) continue; }
      /* delta */
      double d=0; int nt=0;
      if(!swap){ for(int t=0;t<nocc[s];t++) d-=w4(occ[s][t]); }
      else { for(int t=0;t<nocc[s];t++){int j=occ[s][t]; if(!mark[j]){mark[j]=1;touch[nt++]=j;}} for(int t=0;t<nocc[s2];t++){int j=occ[s2][t]; if(!mark[j]){mark[j]=1;touch[nt++]=j;}} for(int t=0;t<nt;t++) d-=w4(touch[t]); }
      double klold=klterm();
      key[s]=nw; cnt[old]-=signcount[s]; cnt[nw]+=signcount[s];
      if(swap){ key[s2]=old; cnt[nw]-=signcount[s2]; cnt[old]+=signcount[s2]; }
      if(!swap){ for(int t=0;t<nocc[s];t++) d+=w4(occ[s][t]); }
      else { for(int t=0;t<nt;t++){ d+=w4(touch[t]); mark[touch[t]]=0; } }
      d -= klw*(klterm()-klold);
      if(d>=0 || urand()<exp(d/T)){ sc+=d; if(sc>rb){rb=sc; memcpy(rbest,key,4*K);} }
      else { key[s]=old; cnt[nw]-=signcount[s]; cnt[old]+=signcount[s]; if(swap){ key[s2]=nw; cnt[old]-=signcount[s2]; cnt[nw]+=signcount[s2]; } }
    }
    memcpy(key,rbest,4*K); memset(cnt,0,4*26); for(int i=0;i<N;i++) cnt[key[c[i]]]++;
    double chk=full();
    printf("R %d %.4f\n",r,chk); fflush(stdout);
    if(chk>gbest){gbest=chk; memcpy(best,rbest,4*K);}
    free(rbest);
  }
  printf("BEST %.4f\n",gbest); for(int s=0;s<K;s++) putchar('a'+best[s]); putchar('\n');
  return 0;
}
