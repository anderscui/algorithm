#include <stdio.h>
#include <stdlib.h>

#include "cmn_lib.h"

void nl()
{
    printf("\n");
}

int rand_int()
{
    return rand();
}

int rand_int_less_than(int less_than)
{
    return rand() % less_than;
}

float rand_float()
{
    return 1.0 * rand();
}

void show_array(int a[], int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
}
