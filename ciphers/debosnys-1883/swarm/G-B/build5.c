/* build5.c -- Witten-Bell interpolated 5-gram conditional model, log10 P(e|abcd), 26^5 floats + 26 unigram floats.
   usage: build5 LETTERS.txt OUT.bin   (LETTERS.txt: a-z only) */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){
  FILE*f=fopen(argv[1],"rb"); fseek(f,0,SEEK_END); long n=ftell(f); fseek(f,0,SEEK_SET);
  unsigned char*s=malloc(n); if(fread(s,1,n,f)!=(size_t)n) return 1; fclose(f);
  long sz[6]={1,26,676,17576,456976,11881376};
  double *c[6]; for(int k=1;k<=5;k++) c[k]=calloc(sz[k],sizeof(double));
  for(long i=0;i<n;i++){ long id=0; for(int k=1;k<=5 && i-k+1>=0;k++){ /* ngram ending at i of length k */
      id=0; for(long j=i-k+1;j<=i;j++) id=id*26+(s[j]-'a'); c[k][id]+=1; } }
  /* context totals and type counts: for order k (k>=2), context = first k-1 letters */
  double *P[6]; P[1]=malloc(sizeof(double)*26); double tot=0; for(int a=0;a<26;a++) tot+=c[1][a];
  for(int a=0;a<26;a++) P[1][a]=(c[1][a]+0.5)/(tot+13);
  for(int k=2;k<=5;k++){ P[k]=malloc(sizeof(double)*sz[k]);
    for(long h=0;h<sz[k-1];h++){ double ch=0,T=0; for(int w=0;w<26;w++){ double x=c[k][h*26+w]; ch+=x; if(x>0) T++; }
      long hs = h % sz[k-2]; /* drop first letter of context */
      for(int w=0;w<26;w++){ double low=P[k-1][hs*26+w]; P[k][h*26+w]= (ch+T>0)? (c[k][h*26+w]+T*low)/(ch+T) : low; } } }
  FILE*o=fopen(argv[2],"wb"); float *out=malloc(sizeof(float)*sz[5]); for(long i=0;i<sz[5];i++) out[i]=(float)log10(P[5][i]);
  fwrite(out,sizeof(float),sz[5],o); float u[26]; for(int a=0;a<26;a++) u[a]=P[1][a]; fwrite(u,sizeof(float),26,o); fclose(o);
  fprintf(stderr,"built from %ld letters\n",n); return 0; }
