/* [Sed12] 9.6
*/
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"
#include "item.h"
#include "pq.h"

#define N 10

void pq_sort(Item a[], int l, int r)
{
    pq_init(r - l + 1);
    int i;
    for (i = l; i <= r; i++)
    {
        pq_insert(a[i]);
        //pq_show(); nl();
    }
    for (i = r; i >= l; i--)
    {
        a[i] = pq_delmax();
        //pq_show(); nl();
    }
}

int main(int argc, char *argv[])
{
    int i;
    Item a[N];
    for (i = 0; i < N; i++)
        a[i] = item_rand();

    show_array(a, N); nl();
    pq_sort(a, 0, N-1);
    show_array(a, N); nl();

    return 0;
}
