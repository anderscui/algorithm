#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"
#include "item.h"
#include "pq.h"

int main(int argc, char *argv[])
{
    pq_init(5);
    assert(pq_empty());

    pq_insert(1);
    pq_insert(2);
    pq_insert(3);
    pq_insert(4);
    pq_insert(5);
    pq_show(); nl();

    int i;
    for (i = 0; i < 5; i++)
    {
        pq_delmax();
        pq_show(); nl();
    }

    return 0;
}
