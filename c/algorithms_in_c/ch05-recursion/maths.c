#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

int permutation(int n, int m)
{
    // TODO: impl
    return 0;
}

int combination(int n, int m)
{
    if(m == 0 || m == n)
        return 1;

    return combination(n - 1, m) + combination(n - 1, m - 1);
}

int main(int argc, char *argv[])
{
/*    printf("2^31 - 1 is %.0f \n", pow(2, 31) - 1);
    printf("INT_MAX is %d \n", INT_MAX);

    printf("max of 4, 3 is %d \n", MAX(4, 3));
    printf("max of 3, 4 is %d \n", MAX(3, 4));
    printf("max of 2.2, 2.3 is %f \n", MAX(2.2, 2.3)); */

    printf("%d \n", combination(5, 1));
    printf("%d \n", combination(5, 2));
    printf("%d \n", combination(5, 3));
    return 0;
}
