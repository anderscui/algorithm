/* [Sed12] 9.7 classic impl of heap sort.
*/
#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"
#include "item.h"

#define NARR 10

void fix_down(Item a[], int k, int N)
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

void heap_sort(Item a[], int l, int r)
{
    int k, N = r-l+1;
    Item* pq = a+l-1;
    for (k = N/2; k >= 1; k--)
        fix_down(a, k, N);
    while (N > 1)
    {
        exch(pq[1], pq[N]);
        fix_down(pq, 1, --N);
    }
}

int main(int argc, char *argv[])
{
    Item a[NARR+1];
    a[0] = -1;
    int i;
    for (i = 1; i <= NARR; i++)
        a[i] = item_rand();
    show_array(a, NARR+1); nl();
    heap_sort(a, 1, NARR);
    show_array(a, NARR+1); nl();
    return 0;
}
