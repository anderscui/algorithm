#include <stdio.h>
#include <stdlib.h>

// fib seq: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
int fib(int n)
{
    if(n < 1) return 0;
    if(n == 1) return 1;

    return fib(n - 1) + fib(n - 2);
}

int fib2(int n)
{
    // n should be greater than or equal to zero.
    if(n <= 1) return n;

    int x = 0, y = 1;
    int i;
    for (i = 2; i <= n; i++)
    {
        y = x + y;
        x = y - x;
    }
    return y;
}

#define N 50
int knownFibs[50];
int unknown = -1;
// ch05 5.11
int fib3(int n)
{
    if(knownFibs[n] != unknown)
        return knownFibs[n];

    int t;
    if(n <= 1)
    {
        t = n;
    }
    else
    {
        t = fib3(n - 1) + fib3(n - 2);
    }
    return (knownFibs[n] = t);
}

int main(int argc, char *argv[])
{
//    int i;
//    for (i = 0; i < 50; i++)
//    {
//        printf("fib2(%d) = %d \n", i, fib2(i));
//    }

    int i;
    for (i = 0; i < N; i++)
    {
        knownFibs[i] = unknown;
    }
    for (i = 0; i < 20; i++)
    {
        printf("fib3(%d) = %d \n", i, fib3(i));
    }

    return 0;
}
