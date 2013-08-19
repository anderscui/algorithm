#include <stdio.h>
#include <stdlib.h>

#include "item.h"

void randinit(Item a[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        a[i] = item_rand();
}

void scaninit(Item a[], int *n)
{
    int i;
    for (i = 0; i < n; i++)
        if(item_scan(&a[i]) == EOF)
            break;
    *n = i;
}

void show(Item a[], int l, int r)
{
    int i;
    for (i = l; i <= r; i++)
        item_show(a[i]);
    printf("\n");
}

typedef void (*sorter)(Item[], int, int);
void sort(sorter s, Item a[], int l, int r)
{
    (*s)(a, l, r);
}

void shell_sort(Item a[], int l, int r)
{
    int i, j, h;
    for(h = 1; h <= (r - l) / 9; h = 3 * h + 1);

    for(; h > 0; h /= 3)
    {
        for (i = l + h; i <= r; i++)
        {
            Item t = a[i];
            j = i;
            while (j >= (l + h)
                   && less(t, a[j - h]))
            {
                a[j] = a[j - h];
                j -= h;
            }
            a[j] = t;
        }
    }
}

void insert_sort(Item a[], int l, int r)
{
    int i, j;
    // use the min element as sentinel key, and the first two are sorted.
    for (i = r; i > l; i--)
        compexch(a[i - 1], a[i]);

    for (i = l + 2; i <= r; i++)
    {
        Item t = a[i];
        j = i;
        while (less(t, a[j - 1]))
        {
            a[j] = a[j - 1];
            j--;
        }
        a[j] = t;
    }
}

void select_sort(Item a[], int l, int r)
{
    int i, j;
    for (i = l; i < r; i++)
    {
        int min = i;
        for (j = i + 1; j <= r; j++)
        {
            if(less(a[j], a[min]))
                min = j;
        }
        exch(a[i], a[min]);
    }
}

void bubble_sort(Item a[], int l, int r)
{
    int i, j;
    for (i = l; i < r; i++)
    {
        for (j = r; j > l; j--)
        {
            compexch(a[j - 1], a[j]);
        }
    }
}
