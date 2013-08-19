/* from [Sed12] 7.1, 7.2, 7.4;
*/

#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

typedef int Item;

#define key(A) (A)
#define less(A, B) (key(A) < key(B))
#define exch(A, B) { Item t = A; A = B; B = t; }
#define compexch(A, B) if (less(B, A)) exch(A, B)

void insertion(Item a[], int l, int r)
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

void sort(Item a[], int l, int r)
{
    int i;
    if(r <= l)
        return;

    i = partition(a, l, r);
    println("partition: %d", i);
    sort(a, l, i - 1);
    sort(a, i + 1, r);
}

#define M 10
void almost_sort(Item a[], int l, int r)
{
    int i;
    if(r - l <= M)
        return; // ignore the small arrays.

    exch(a[(l + r) / 2], a[r - 1]);
    compexch(a[l], a[r - 1]);
    compexch(a[l], a[r]);
    compexch(a[r - 1], a[r]);

    // here, a[r-1] is the pivot of the three elements.
    i = partition(a, l + 1, r - 1);
    println("partition: %d", i);
    sort(a, l, i - 1);
    sort(a, i + 1, r);
}

void quick_sort(Item a[], int l, int r)
{
    almost_sort(a, l, r);
    insertion(a, l, r);
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
    quick_sort(a, 0, N - 1);
    show_array(a, N); nl();

    return 0;
}
