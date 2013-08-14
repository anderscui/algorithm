#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

#define N 3

int a[] = { 1, 2, 3 };

void swap(int a[], int i, int j)
{
    int temp;
    temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

void backtrack(int i)
{
    if (i >= N)
    {
        show_array(a, N);
        nl();
    }

    int j;
    for (j = i; j < N; j++)
    {
        swap(a, i, j);
        backtrack(i + 1);
        swap(a, i, j);
    }
}

int main(int argc, char *argv[])
{
    backtrack(0);
    return 0;
}
