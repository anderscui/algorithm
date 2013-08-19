/* from b1.6.3 see also sort.c
*/

#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

typedef int Item;

#define key(A) (A)
#define less(A, B) (key(A) < key(B))
#define exch(A, B) { Item t = A; A = B; B = t; }
#define compexch(A, B) if (less(B, A)) exch(A, B)

// h sequence: 1, 4, 13, 40, 121, ...
// introduced by Knuth.
// perf: < O(N^(3/2))
void sort(Item a[], int l, int r)
{
    int i, j, h;
    for(h = 1; h <= (r - l) / 9; h = 3 * h + 1);

    for(; h > 0; h /= 3)
    {
        for (i = l + h; i <= r; i++)
        {
            Item t = a[i];
            j = i;
            while (j >= (l + h)
                   && less(t, a[j - h]))
            {
                a[j] = a[j - h];
                j -= h;
            }
            a[j] = t;
        }
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
            a[i] = 100 * (1.0 * rand() / RAND_MAX);
        }
    }
    else
    {
        // manual input
        i = 0;
        while(scanf("%d", &a[i]) == 1)
            i++;
    }
    show_array(a, N); nl();
    sort(a, 0, N - 1);
    show_array(a, N); nl();

    return 0;
}
