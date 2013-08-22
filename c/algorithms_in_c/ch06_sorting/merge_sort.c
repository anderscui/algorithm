/* from [Sed12] 8.1 & 8.2;
*/

#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

typedef int Item;

#define key(A) (A)
#define less(A, B) (key(A) < key(B))
#define exch(A, B) { Item t = A; A = B; B = t; }
#define compexch(A, B) if (less(B, A)) exch(A, B)

void mergeAB(Item c[], Item a[], int M, Item b[], int N)
{
    int i, j, k;
    for (i = 0, j = 0, k = 0; k < M + N ; k++)
    {
        if (i == M)
        {
            c[k] = b[j++];
            continue;
        }
        if (j == N)
        {
            c[k] = a[i++];
            continue;
        }
        c[k] = (less(a[i], b[j])) ? a[i++] : b[j++];
    }
}

#define NAUX 100
Item aux[NAUX];
/** merge a[l..m] and a[m+1..r]
 */
void merge(Item a[], int l, int m, int r)
{
    int i, j, k;
    // use the two loops below to construct a bitonic seq.
    // this way makes i <- l;
    for (i = m + 1; i > l; i--)
        aux[i - 1] = a[i - 1];
    // this way makes j <- r;
    for (j = m; j < r; j++)
        aux[r + m - j] = a[j + 1];

    // loop count is same to l -> r;
    // make sure each loop move one element;
    for (k = l; k <= r; k++)
    {
        if(less(aux[j], aux[i]))
            a[k] = aux[j--];
        else
            a[k] = aux[i++];
    }
}

void merge_sort(Item a[], int l, int r)
{
    if(r <= l)
        return;

    int m = (l + r) / 2;
    merge_sort(a, l, m);
    merge_sort(a, m+1, r);
    merge(a, l, m, r);
}

void insert_sort(Item a[], int l, int r)
{
    int i, j;
    // use the min element as sentinel key, and the first two are sorted.
    for (i = r; i > l; i--)
        compexch(a[i - 1], a[i]);

    for (i = l + 2; i <= r; i++)
    {
        Item t = a[i];
        j = i;
        while (less(t, a[j - 1]))
        {
            a[j] = a[j - 1];
            j--;
        }
        a[j] = t;
    }
}

int main(int argc, char *argv[])
{
    int i, N = atoi(argv[1]), sw = atoi(argv[2]);
    int *a = malloc(N * sizeof(int));
    if (sw)
    {
        for (i = 0; i < N; i++)
        {
            a[i] = rand_int_between(1, 100);
        }
    }
    else
    {
        // manual input
        i = 0;
        while(scanf("%d", &a[i]) == 1)
            i++;
    }
    int b[N];
    copy_array(a, b, N);

    show_array(a, N); nl();
    show_array(b, N); nl();

    merge_sort(a, 0, N - 1);
    insert_sort(b, 0, N - 1);

    show_array(a, N); nl();
    show_array(b, N); nl();

//    int a[] = { 1, 3, 5, 7, 9 };
//    int b[] = { 2, 3, 4, 5, 6, 7 };
//    show_array(a, 5); nl();
//    show_array(b, 6); nl();
//    int c[11];
//    mergeAB(c, a, 5, b, 6);
//    show_array(c, 11); nl();

//    int a[] = { 2, 3, 4, 5, 6, 7, 1, 3, 5, 7, 9 };
//    show_array(a, 11); nl();
//    merge(a, 0, 5, 10);
//    show_array(a, 11); nl();

    return 0;
}
