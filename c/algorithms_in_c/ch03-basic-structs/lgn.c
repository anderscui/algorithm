#include <stdio.h>
#include <stdlib.h>

/* b1, 3.1 */

int lg(int n);

int main()
{
    int i, n;
    for (i = 1, n = 10; i <= 6; i++, n *= 10)
        printf("%7d %2d %9d\n", n, lg(n), n * lg(n));
    return 0;
}

int lg(int n)
{
    int i;
    for (i = -1; n > 0; i++, n /= 2) ;
    return i;
}
