/* from [Lev07]
*/

#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

#define M 3

typedef int Item;

#define key(A) (A)
#define less(A, B) (key(A) < key(B))
#define exch(A, B) { Item t = A; A = B; B = t; }
#define compexch(A, B) if (less(B, A)) exch(A, B)

void sort(Item a[], int l, int r)
{
    int len = (r - l) + 1;
    int i, j, cnt[len];
    for (i = 0; i < len; i++)
        cnt[i] = 0;

    for (i = l; i < r; i++)
    {
        for (j = i + 1; j <= r; j++)
        {
            if (a[j] < a[i])
            {
                cnt[i]++;
            }
            else
            {
                cnt[j]++;
            }
        }
    }

    int s[len];
    for (i = 0; i < len; i++)
    {
        s[cnt[i]] = a[i];
    }
    for (i = 0; i < len; i++)
    {
        a[i+l] = s[i];
    }
}

int main(int argc, char *argv[])
{
    int N = 6;
    int a[] = { 62, 31, 84, 96, 19, 47 };

    show_array(a, N); nl();
    sort(a, 0, N - 1);
    show_array(a, N); nl();

    return 0;
}
