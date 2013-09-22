#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "item.h"
#include "pq.h"

static Item *pq;
static int N;

static void fix_up(Item a[], int k)
{
    while (k > 1 && less(a[k/2], a[k]))
    {
        exch(a[k/2], a[k]);
        k /= 2;
    }
}

static void fix_down(Item a[], int k, int N)
{
    int i;
    while (2 * k <= N)
    {
        i = 2 * k;
        if(i < N && less(a[i], a[i+1]))
            i++;
        if(!less(a[k], a[i]))
            break;
        exch(a[k], a[i]);
        k = i;
    }
}

void pq_init(int n)
{
    pq = malloc((n+1) * sizeof(Item));
    N = 0;
}

int pq_empty()
{
    return (N == 0);
}

// unordered array;
void pq_insert(Item v)
{
    pq[++N] = v;
    fix_up(pq, N);
}

Item pq_delmax()
{
    assert(N > 0);

    exch(pq[1], pq[N]);
    fix_down(pq, 1, N - 1);
    return pq[N--];
}

void pq_show()
{
    int i;
    for (i = 1; i <= N; i++)
        printf("%d ", pq[i]);
}
