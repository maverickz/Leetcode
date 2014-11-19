#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX(a,b) (((a) > (b)) ? (a) : (b))

char *longest_common_suseq(char *p, char *q, int m, int n)
{
    int i;
    int j;
    int **LCS = NULL;
    LCS = (int **)calloc(1, sizeof(int *)*(m+1));
    for (i = 0; i <= m; i++) {
        LCS[i] = (int *)calloc(1, sizeof(int)*(n+1));
    }

    for (i = 0; i <= m; i++) {
        for (j = 0; j <= n; j++) {
            if (i == 0 || j == 0) {
                // Base condition
                LCS[i][j] = 0;
            } else if (p[i-1] == q[j-1]) {
                // Last characters of p and q matches
                LCS[i][j] = 1 + LCS[i-1][j-1];
            } else {
                LCS[i][j] = MAX(LCS[i-1][j], LCS[i][j-1]);
            }
        }
    }
    printf("Longest seq len: %d\n", LCS[m][n]);
    int seq_len = LCS[m][n];
    if (seq_len == 0) {
        return NULL;
    } else {
        char *seq = calloc(1, seq_len+1);
        i = m;
        j = n;
        int k = seq_len;
        seq[seq_len] = '\0';
        while (i > 0 && j > 0) {
            // If the current character in p and q are the same, then
            // the current character is part of LCS
            if (p[i-1] == q[j-1]) {
                seq[--k] = p[i-1];
                i--;
                j--;
            } else if (LCS[i-1][j] > LCS[i][j-1]) {
                i--;
            } else {
                j--;
            }
        }
        return seq;
    } 
}

char X[] = "AGGTAB";
char Y[] = "GXTXAYB";
int main()
{
    printf("%s, %s\n", X, Y);
    int m = strlen(X);
    int n = strlen(Y);
    char *seq = longest_common_suseq(X, Y, m, n);
    if (seq) {
        printf("LCS: %s\n", seq);
    }
    return 0;
}