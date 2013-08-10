#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

int factorial(int n)
{
    if(n == 0)
        return 1;
    return n * factorial(n-1);
}

// m = n * q(uotient) + r(emainder)
int gcd(int m, int n)
{
    if(n == 0)
        return m;

    return gcd(n, m % n);
}

int main()
{
    printf("factorial of 5 is %d", factorial(5));
    nl();

    printf("gcd of 12 and 32 is %d", gcd(12, 32));
    nl();

    return 0;
}
