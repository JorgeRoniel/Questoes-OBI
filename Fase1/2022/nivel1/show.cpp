#include <bits/stdc++.h>
using namespace std;
const int MAXN = 110;
int mat[MAXN][MAXN];
int main() {
  int a, n, m; scanf("%d %d %d", &a, &n, &m);
  for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++)
      scanf("%d", &mat[i][j]);
  
  int resp = -1;
  for(int i = n - 1; i >= 0; i--) {
    int qtd = 0, cont = 0;
    for(int j = 0; j < m; j++) {
      if(mat[i][j] == 0) {
        cont++;
        qtd = max(qtd, cont);
      } else cont = 0;
    }
    if(qtd >= a) {
      resp = n - i;
      break;
    }
  }
  
  printf("%d\n", resp);
}

