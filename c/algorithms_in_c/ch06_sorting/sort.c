/* from b1.6.1
   driver program for sorting an array;
   generic data type: Item;
   common operations: key; less; exch/swap; comp and exch;
   simple impl of insertion sorting;
*/

#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

typedef int Item;

#define key(A) (A)
#define less(A, B) (key(A) < key(B))
#define exch(A, B) { Item t = A; A = B; B = t; }
#define compexch(A, B) if (less(B, A)) exch(A, B)

void sort(Item a[], int l, int r)
{
    int i, j;
    for (i = l + 1; i <= r; i++)
    {
        for (j = i; j > l; j--)
        {
            compexch(a[j - 1], a[j]);
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
