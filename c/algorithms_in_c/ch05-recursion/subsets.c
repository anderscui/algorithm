#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

#define N 5

int s[] = { 1, 2, 3, 4, 5 };
int bs[] = { 0, 1 };
int bits[N];

void show_result(int a[], int bits[])
{
    int i;
    for (i = 0; i < N; i++)
    {
        if (bits[i])
        {
            printf("%d ", a[i]);
        }
        else
        {
            printf("_ ");
        }
    }
}

void gen_subsets(int a[], int n)
{
    int j;
    for (j = 0; j < 2; j++)
    {
        bits[n] = bs[j];
        // reach to the end
        if (n == (N - 1))
        {
            show_result(s, bits);
            nl();
        }
        else
        {
            gen_subsets(a, n + 1);
        }
    }
}

int main(int argc, char *argv[])
{
    gen_subsets(bits, 0);
    return 0;
}
