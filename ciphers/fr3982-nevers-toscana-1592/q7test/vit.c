/* BNF-Q7-SCREEN: exact Viterbi over digit positions x 4-gram context (26^3 states). See screen.py. */
#include <stdlib.h>
#include <string.h>
#define V 26
#define S (V*V*V)
#define NEG -1e30
typedef struct { double sc, lm; int cnt; } cell;
/* tr_off[N+1]: transitions starting at i are tr_off[i]..tr_off[i+1]-1; tr_len digits; tr_m meaning id (-1 null, -2 skip)
   m_off[M+1], m_let letters. path_out (if non-NULL) receives transition ids along best path, returns count via *npath. */
double viterbi(int N, const int *tr_off, const int *tr_len, const int *tr_m, const int *m_off, const int *m_let,
               const double *LP, double null_pen, double skip_pen, double beam, int *out_cnt, double *out_lm,
               int *path_out, int *npath) {
  cell *L[4]; int *live[4]; int nlive[4]; char *isl[4];
  for (int k = 0; k < 4; k++) { L[k] = malloc(sizeof(cell)*S); live[k] = malloc(sizeof(int)*S); isl[k] = calloc(S,1); nlive[k]=0;
    for (int s = 0; s < S; s++) L[k][s].sc = NEG; }
  int *bp_i = NULL, *bp_s = NULL, *bp_t = NULL;
  if (path_out) { size_t sz = (size_t)(N+1)*S; bp_i = malloc(sizeof(int)*sz); bp_s = malloc(sizeof(int)*sz); bp_t = malloc(sizeof(int)*sz); }
  for (int s = 0; s < S; s++) { L[0][s].sc = 0; L[0][s].lm = 0; L[0][s].cnt = 0; live[0][s] = s; isl[0][s] = 1; }
  nlive[0] = S;
  for (int i = 0; i < N; i++) {
    int a = i & 3; cell *cur = L[a];
    double bst = NEG; for (int q = 0; q < nlive[a]; q++) if (cur[live[a][q]].sc > bst) bst = cur[live[a][q]].sc;
    { int w = 0; for (int q = 0; q < nlive[a]; q++) { int s = live[a][q]; if (cur[s].sc >= bst - beam) live[a][w++] = s; else { cur[s].sc = NEG; isl[a][s] = 0; } } nlive[a] = w; }
    for (int t = tr_off[i]; t < tr_off[i+1]; t++) {
      int j = i + tr_len[t]; if (j > N) continue; int b = j & 3; cell *nx = L[b];
      int m = tr_m[t];
      for (int q = 0; q < nlive[a]; q++) {
        int s = live[a][q]; double sc = cur[s].sc, lm = cur[s].lm; int cnt = cur[s].cnt, ctx = s;
        if (m < 0) sc += (m == -1 ? null_pen : skip_pen);
        else for (int k = m_off[m]; k < m_off[m+1]; k++) { int ch = m_let[k]; double lp = LP[ctx*V+ch]; sc += lp; lm += lp; cnt++; ctx = (ctx % (V*V))*V + ch; }
        if (sc > nx[ctx].sc) { nx[ctx].sc = sc; nx[ctx].lm = lm; nx[ctx].cnt = cnt;
          if (!isl[b][ctx]) { isl[b][ctx] = 1; live[b][nlive[b]++] = ctx; }
          if (path_out) { size_t o = (size_t)j*S+ctx; bp_i[o] = i; bp_s[o] = s; bp_t[o] = t; } }
      }
    }
    /* clear layer a for reuse at i+4 */
    for (int q = 0; q < nlive[a]; q++) { int s = live[a][q]; cur[s].sc = NEG; isl[a][s] = 0; } nlive[a] = 0;
  }
  int fa = N & 3; double best = NEG; int bs = -1;
  for (int q = 0; q < nlive[fa]; q++) { int s = live[fa][q]; if (L[fa][s].sc > best) { best = L[fa][s].sc; bs = s; } }
  if (bs >= 0) { *out_cnt = L[fa][bs].cnt; *out_lm = L[fa][bs].lm; } else { *out_cnt = 0; *out_lm = 0; }
  if (path_out && bs >= 0) { int j = N, s = bs, n = 0; while (j > 0) { size_t o = (size_t)j*S+s; path_out[n++] = bp_t[o]; int pi = bp_i[o], ps = bp_s[o]; j = pi; s = ps; } *npath = n; }
  for (int k = 0; k < 4; k++) { free(L[k]); free(live[k]); free(isl[k]); }
  if (path_out) { free(bp_i); free(bp_s); free(bp_t); }
  return best;
}
