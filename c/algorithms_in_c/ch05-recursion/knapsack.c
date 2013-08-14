/* ch05 5.12 & 5.13 */
#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

#define N 4
#define C 10

double p[] = { 42, 12, 40, 25 };
double w[] = { 7, 3, 4, 5 };
int x[N];
int cx[N];
int max = 0;
int cp = 0;
int cw = 0;

void backtrack(int i)
{
    if (i >= N)
    {
        if (cp > max)
        {
            max = cp;
            int j;
            for (j = 0; j < N; j++)
            {
                x[j] = cx[j];
            }
        }
        return;
    }

    // if the thief can add more jewels
    if (cw + w[i] <= C)
    {
        cx[i] = 1; // mark this jewel
        cw += w[i];
        cp += p[i];
        backtrack(i + 1);

        // restore the bag;
        cw -= w[i];
        cp -= p[i];
    }

    cx[i] = 0;
    backtrack(i + 1);
}

int main(int argc, char *argv[])
{
    backtrack(0);
    printf("%d \n", max);
    show_array(x, N);

    return 0;
}


///////////////////

//typedef struct { int size; int val; } Item;

//Item items[N] = { { 12, 4 }, { 2, 2 }, { 1, 2 }, { 1, 1 }, { 4, 10 } };

//int knap(int cap)
//{
//    int i, space, max, t;
//    for (i = 0, max = 0; i < N; i++)
//    {
//        if((space = cap - items[i].size) >= 0)
//        {
//            if((t = knap(space) + items[i].val) > max)
//                max = t;
//        }
//    }
//    return max;
//}
