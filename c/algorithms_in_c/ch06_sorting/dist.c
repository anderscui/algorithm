/* from b1.6.17 see also sort.c
*/

#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

#define M 3

typedef int Item;

#define key(A) (A)
#define less(A, B) (key(A) < key(B))
#define exch(A, B) { Item t = A; A = B; B = t; }
#define compexch(A, B) if (less(B, A)) exch(A, B)

// 0, 1, 2, 0, 1, 2, 0, 1, 2, 0
void sort(Item a[], int l, int r)
{
    int total = (r - l) + 1;
    int i, j, cnt[M];
    int b[total];

    for (j = 0; j < M; j++)
        cnt[j] = 0;

    for (i = l; i <= r; i++)
        cnt[a[i] + 1]++;

    for (j = 1; j < M; j++)
        cnt[j] += cnt[j - 1];

    for (i = l; i <= r; i++)
        b[cnt[a[i]]++] = a[i];

    for (i = l; i <= r; i++)
        a[i] = b[i];
}

int main(int argc, char *argv[])
{
    int i, N = atoi(argv[1]);
    int *a = malloc(N * sizeof(int));
    for (i = 0; i < N; i++)
        a[i] = i % M;

    show_array(a, N); nl();
    sort(a, 0, N - 1);
    show_array(a, N); nl();

    return 0;
}
