#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "item.h"
#include "pq.h"

static Item *pq;
static int N;

void pq_init(int n)
{
    pq = malloc(n * sizeof(Item));
    N = 0;
}

int pq_empty()
{
    return (N == 0);
}

// ordered array;
//void pq_insert(Item v)
//{
//    int i = N-1;
//    while (i >= 0 && less(v, pq[i]))
//    {
//        pq[i+1] = pq[i];
//        i--;
//    }
//    pq[i+1] = v;
//    N++;
//}

// unordered array;
void pq_insert(Item v)
{
    pq[N++] = v;
}

Item pq_delmax()
{
    assert(N > 0);

    int i, max = 0;
    for (i = 1; i < N; i++)
    {
        if(less(pq[max], pq[i]))
        {
            max = i;
        }
    }
    exch(pq[max], pq[N-1]);
    return pq[--N];
}

void pq_show()
{
    int i;
    for (i = 0; i < N; i++)
        printf("%d ", pq[i]);
}
