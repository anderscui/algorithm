/* from [Sed12] 7.6;
*/

#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

typedef int Item;

#define key(A) (A)
#define less(A, B) (key(A) < key(B))
#define exch(A, B) { Item t = A; A = B; B = t; }
#define compexch(A, B) if (less(B, A)) exch(A, B)

int partition(Item a[], int l, int r)
{
    int i = l - 1, j = r;
    Item v = a[r];
    while(1)
    {
        while(less(a[++i], v));
        while(less(v, a[--j]))
            if(j == l)
                break;

        if(i >= j)
            break;
        exch(a[i], a[j]);
    }
    exch(a[i], a[r]);
    return i;
}

void select_kth(Item a[], int l, int r, int k)
{
    int i;
    if(r <= l)
        return;

    i = partition(a, l, r);
    println("partition: %d", i);
    if (i > k)
        select_kth(a, l, i - 1, k);
    if (i < k)
        select_kth(a, i + 1, r, k);
}

int main(int argc, char *argv[])
{
    int i, N = atoi(argv[1]), sw = atoi(argv[2]);
    int *a = malloc(N * sizeof(int));
    if (sw)
    {
        for (i = 0; i < N; i++)
        {
            //a[i] = 100 * (1.0 * rand() / RAND_MAX);
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
    show_array(a, N); nl();
    select_kth(a, 0, N - 1, 1);
    println("the third one is %d", a[1]);

    return 0;
}
