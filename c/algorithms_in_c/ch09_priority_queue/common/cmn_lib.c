#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>

#include "cmn_lib.h"

void println(const char* format, ...)
{
    va_list arglist;
    va_start(arglist, format);
    vprintf(format, arglist); // don't use printf.
    printf("\n");
    va_end(arglist);
}

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

int rand_int_between(int from, int to)
{
    return from + rand_int_less_than(to - from);
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

void copy_array(int a[], int b[], int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        b[i] = a[i];
    }
}
