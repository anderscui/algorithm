/* from b1.6.2 see also sort.c
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
    for (i = l; i < r; i++)
    {
        int min = i;
        for (j = i + 1; j <= r; j++)
        {
            if(less(a[j], a[min]))
                min = j;
        }
        exch(a[i], a[min]);
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
