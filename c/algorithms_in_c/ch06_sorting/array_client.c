#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"
#include "array.h"
#include "item.h"

int main(int argc, char *argv[])
{
    int N = atoi(argv[1]), use_random = atoi(argv[2]);
    Item *a = malloc(N * sizeof(Item));
    if (use_random)
    {
        randinit(a, N);
    }
    else
    {
        scaninit(a, &N);
    }

    println("shell sort");
    show(a, 0, N - 1);
    sort(shell_sort, a, 0, N - 1);
    show(a, 0, N - 1);

    println("insertion sort");
    randinit(a, N);
    show(a, 0, N - 1);
    sort(insert_sort, a, 0, N - 1);
    show(a, 0, N - 1);

    println("selection sort");
    randinit(a, N);
    show(a, 0, N - 1);
    sort(select_sort, a, 0, N - 1);
    show(a, 0, N - 1);

    println("bubble sort");
    randinit(a, N);
    show(a, 0, N - 1);
    sort(bubble_sort, a, 0, N - 1);
    show(a, 0, N - 1);

    return 0;
}
