#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

int max(int a[], int l, int r)
{
    if(l == r)
        return a[l];

    int mid = (l + r) / 2;
    int u = max(a, l, mid);
    int v = max(a, mid + 1, r);
    return (u > v) ? u : v;
}

int max2(int a[], int l, int r)
{
    if(r == l)
        return a[l];

    int u = a[l];
    int v = max2(a, l + 1, r);
    return (u > v) ? u : v;
}

int main(int argc, char *argv[])
{
    int len = 10, upper_bound = 50;
    int a[len], i;
    for (i = 0; i < len; i++)
    {
        a[i] = rand_int_less_than(upper_bound);
    }
    printf("array is: ");
    show_array(a, len);
    nl();
    printf("the max element is: %d", max(a, 0, len - 1));
    nl();
    printf("the max2 element is: %d", max(a, 0, len - 1));

    return 0;
}
