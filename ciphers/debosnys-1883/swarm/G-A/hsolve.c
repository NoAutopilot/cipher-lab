/* DEB-SWARM-A homophonic letter-substitution solver (simulated annealing, 5-gram log counts + letter-frequency term).
 * Usage: hsolve TRAIN.txt CIPHER.txt RESTARTS ITERS SEED [W_FREQ] [T0] > out
 * CIPHER.txt: whitespace-separated integer symbol ids (0..K-1). Output: best score line, then "sym letter" per symbol,
 * then the plaintext. Symbols listed in the optional env FIXED ("id:letter,id:letter") are pinned (crib mode). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define NG 5
static long TSZ; static int AL = 26;
static float *lp;
static int n, K, *c, *p, *key, **pos, *npos, *mark;
static double efreq[32];
static unsigned long long rs;
static inline unsigned long long rnd(void){ rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void){ return (rnd() >> 11) * (1.0/9007199254740992.0); }
static inline float win(int i){ int x = 0; for (int k = 0; k < NG; k++) x = x*AL + p[i+k]; return lp[x]; }
static double full(void){ double s = 0; for (int i = 0; i + NG <= n; i++) s += win(i); return s; }
static int cnt[32];
static double freqterm(void){ double s = 0; for (int l = 0; l < AL; l++){ double e = efreq[l]*n + 0.5; double d = cnt[l]-e; s += d*d/e; } return -s; }
int main(int argc, char **argv){
  if (argc < 6){ fprintf(stderr, "usage\n"); return 1; }
  int R = atoi(argv[3]); long IT = atol(argv[4]); rs = 88172645463325252ULL ^ (unsigned long long)atoll(argv[5])*2654435761ULL;
  double WF = argc > 6 ? atof(argv[6]) : 1.0, T0 = argc > 7 ? atof(argv[7]) : 0.6;
  /* model */
  if (getenv("ALPHA")) AL = atoi(getenv("ALPHA")); TSZ = (long)AL*AL*AL*AL*AL;
  FILE *f = fopen(argv[1], "r"); fseek(f, 0, SEEK_END); long L = ftell(f); rewind(f);
  char *t = malloc(L+1); fread(t, 1, L, f); fclose(f);
  /* interpolated conditional 5-gram: lp[x1..x5] = log P(x5 | x1..x4), Witten-Bell style fixed lambdas */
  double uc[32] = {0}; long tot = 0;
  for (long i = 0; i < L; i++) if (t[i] >= 'a' && t[i] <= 'a'+AL-1) { uc[t[i]-'a']++; tot++; }
  unsigned *c5 = calloc(TSZ, sizeof(unsigned)), *c4 = calloc(TSZ/AL, sizeof(unsigned)), *c3 = calloc(TSZ/(AL*AL), sizeof(unsigned)), *c2 = calloc(AL*AL, sizeof(unsigned));
  for (long i = 0; i + NG <= L; i++){ int x = 0; for (int k = 0; k < NG; k++) x = x*AL + (t[i+k]-'a'); c5[x]++; }
  for (long x = 0; x < TSZ; x++) c4[x/AL] += c5[x];   /* 4-gram prefix counts = counts of x1..x4 */
  for (long x = 0; x < TSZ/AL; x++) c3[x/AL] += c4[x];
  for (long x = 0; x < TSZ/(AL*AL); x++) c2[x/AL] += c3[x];
  double LAM = getenv("LAM") ? atof(getenv("LAM")) : 2.0;  /* WB-like: lambda = n/(n+LAM*types) approx via n/(n+LAM*AL^0.5) */
  double FLOOR = getenv("FLOOR") ? atof(getenv("FLOOR")) : -99;
  lp = malloc(sizeof(float)*TSZ);
  static double p1[32]; for (int l = 0; l < AL; l++) p1[l] = (uc[l]+1)/(tot+AL);
  /* conditional tables built on the fly: P2(b|a), P3(c|ab), P4(d|abc), P5(e|abcd) */
  for (long x = 0; x < TSZ; x++){
    int e = x % AL; long h4 = x / AL;          /* abcd */
    long h3 = h4 % (AL*AL*AL);                  /* bcd  */
    long h2 = h4 % (AL*AL); long h1 = h4 % AL;  /* cd, d */
    /* counts of (d,e), (c,d,e), (b,c,d,e), (a,b,c,d,e) and of their histories */
    double n2 = c2[h1*AL+e], d2 = 0; for (int q = 0; q < AL; q++) d2 += c2[h1*AL+q];
    double n3 = c3[h2*AL+e], d3 = c2[h2];
    double n4 = c4[h3*AL+e], d4 = c3[h3];
    double n5 = c5[x], d5 = c4[h4];
    double P = p1[e];
    P = (n2 + LAM*AL*P)/(d2 + LAM*AL);
    P = (n3 + LAM*10*P)/(d3 + LAM*10);
    P = (n4 + LAM*5*P)/(d4 + LAM*5);
    P = (n5 + LAM*3*P)/(d5 + LAM*3);
    lp[x] = (float)log(P); if (lp[x] < FLOOR) lp[x] = FLOOR;
  }
  double us = 0; for (int l = 0; l < AL; l++) us += uc[l]; for (int l = 0; l < AL; l++) efreq[l] = uc[l]/us;
  free(c5); free(c4); free(c3); free(c2); free(t);
  /* cipher */
  f = fopen(argv[2], "r"); int cap = 1<<16; c = malloc(sizeof(int)*cap); n = 0; K = 0;
  while (fscanf(f, "%d", &c[n]) == 1){ if (c[n]+1 > K) K = c[n]+1; n++; } fclose(f);
  p = malloc(sizeof(int)*n); key = malloc(sizeof(int)*K); mark = calloc(n+NG, sizeof(int));
  npos = calloc(K, sizeof(int)); pos = malloc(sizeof(int*)*K);
  for (int i = 0; i < n; i++) npos[c[i]]++;
  for (int s = 0; s < K; s++){ pos[s] = malloc(sizeof(int)*(npos[s]+1)); npos[s] = 0; }
  for (int i = 0; i < n; i++) pos[c[i]][npos[c[i]]++] = i;
  int fixed[4096]; for (int s = 0; s < K; s++) fixed[s] = -1;
  char *fx = getenv("FIXED"); if (fx && *fx){ char *d = strdup(fx), *tok = strtok(d, ","); while (tok){ int id; char l; if (sscanf(tok, "%d:%c", &id, &l) == 2 && id < K) fixed[id] = l-'a'; tok = strtok(NULL, ","); } }
  char *af = getenv("ANS"); if (af){ FILE *g = fopen(af, "r"); memset(cnt, 0, sizeof cnt); for (int i = 0; i < n; i++){ int ch = fgetc(g); p[i] = ch-'a'; cnt[p[i]]++; } fclose(g); fprintf(stderr, "true score %.2f (ngram %.2f freq %.2f)\n", full()+WF*freqterm(), full(), freqterm()); }
  char *hk = getenv("HELDOUT");
  if (hk){ /* score a fixed key (lines "sym letter", '?' = unread) on this text against 1000 value-shuffled keys */
    int *kk = malloc(sizeof(int)*K); for (int s2 = 0; s2 < K; s2++) kk[s2] = -1;
    FILE *g = fopen(hk, "r"); int id; char l; while (fscanf(g, "%d %c", &id, &l) == 2) if (id < K && l >= 'a' && l <= 'a'+AL-1) kk[id] = l-'a'; fclose(g);
    int *vals = malloc(sizeof(int)*K), *sy = malloc(sizeof(int)*K), nv = 0; for (int s2 = 0; s2 < K; s2++) if (kk[s2] >= 0){ sy[nv] = s2; vals[nv++] = kk[s2]; }
    double real = 0; int nw = 0, cov = 0; for (int i = 0; i < n; i++) cov += kk[c[i]] >= 0;
    #define HSC(KEY, OUT, NW) { double z = 0; int w = 0; for (int i = 0; i + NG <= n; i++){ int ok = 1, x = 0; for (int q = 0; q < NG; q++){ int v = KEY[c[i+q]]; if (v < 0){ ok = 0; break; } x = x*AL+v; } if (ok){ z += lp[x]; w++; } } OUT = w ? z/w : 0; NW = w; }
    HSC(kk, real, nw);
    int NS = getenv("NSHUF") ? atoi(getenv("NSHUF")) : 1000, above = 0; double m = 0; int *sk = malloc(sizeof(int)*K);
    for (int r2 = 0; r2 < NS; r2++){ for (int j = nv-1; j > 0; j--){ int q = rnd()%(j+1); int tmp = vals[j]; vals[j] = vals[q]; vals[q] = tmp; }
      for (int s2 = 0; s2 < K; s2++) sk[s2] = -1; for (int j = 0; j < nv; j++) sk[sy[j]] = vals[j]; double sc; int w2; HSC(sk, sc, w2); m += sc; if (sc >= real) above++; }
    printf("heldout coverage %.3f windows %d real %.4f shuf_mean %.4f percentile %.2f\n", (double)cov/n, nw, real, m/NS, 100.0*(NS-above)/NS);
    return 0; }
  int *best = malloc(sizeof(int)*K), *wk = malloc(sizeof(int)*n); double bestS = -1e300;
  int *starts = malloc(sizeof(int)*(n+1));
  for (int r = 0; r < R; r++){
    for (int s = 0; s < K; s++){ if (fixed[s] >= 0) { key[s] = fixed[s]; continue; } double u = urand(), a = 0; int l = 25; for (int q = 0; q < AL; q++){ a += efreq[q]; if (u < a){ l = q; break; } } key[s] = l; }
    memset(cnt, 0, sizeof cnt);
    for (int i = 0; i < n; i++){ p[i] = key[c[i]]; cnt[p[i]]++; }
    double ng = full(), fq = freqterm(), S = ng + WF*fq, rS = S; int *rk = malloc(sizeof(int)*K); memcpy(rk, key, sizeof(int)*K);
    for (long it = 0; it < IT; it++){
      double T = T0 * (1.0 - (double)it/IT);
      int s = rnd() % K; if (!npos[s] || fixed[s] >= 0) continue;
      int old = key[s], nl = rnd() % AL; if (nl == old) continue;
      /* windows touched */
      int ns = 0, last = -1;
      for (int j = 0; j < npos[s]; j++){ int q = pos[s][j]; int a = q-NG+1; if (a < 0) a = 0; if (a <= last) a = last+1; int b = q; if (b > n-NG) b = n-NG; for (int w = a; w <= b; w++) starts[ns++] = w; if (b > last) last = b; }
      double o = 0; for (int j = 0; j < ns; j++) o += win(starts[j]);
      for (int j = 0; j < npos[s]; j++) p[pos[s][j]] = nl;
      double nw = 0; for (int j = 0; j < ns; j++) nw += win(starts[j]);
      int m = npos[s]; double eo = efreq[old]*n+0.5, en = efreq[nl]*n+0.5;
      double fqd = -(( (cnt[old]-m-eo)*(cnt[old]-m-eo) - (cnt[old]-eo)*(cnt[old]-eo) )/eo + ( (cnt[nl]+m-en)*(cnt[nl]+m-en) - (cnt[nl]-en)*(cnt[nl]-en) )/en);
      double d = (nw - o) + WF*fqd;
      if (d >= 0 || (T > 0 && urand() < exp(d/T))){ key[s] = nl; cnt[old] -= m; cnt[nl] += m; S += d; if (S > rS){ rS = S; memcpy(rk, key, sizeof(int)*K); } }
      else for (int j = 0; j < npos[s]; j++) p[pos[s][j]] = old;
    }
    if (rS > bestS){ bestS = rS; memcpy(best, rk, sizeof(int)*K); }
    fprintf(stderr, "restart %d score %.2f best %.2f\n", r, rS, bestS);
    free(rk);
  }
  printf("score %.4f per_char %.4f\n", bestS, bestS/n);
  for (int s = 0; s < K; s++) printf("%d %c\n", s, 'a'+best[s]);
  for (int i = 0; i < n; i++) putchar('a'+best[c[i]]); putchar('\n');
  (void)wk; (void)mark;
  return 0;
}
