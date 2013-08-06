#include <stdio.h>
#include <stdlib.h>

#define N 10000

int main()
{
    int i, j, a[N];
    for (i = 2; i < N; i++)
        a[i] = 1;

    //float upper = sqrt(N + 1);
    for (i = 2; i < N; i++) {
        if (a[i]) {
            for (j = i; i * j < N; j++)
                a[i * j] = 0;
        }
    }

    int count = 0;
    for (i = 2; i < N; i++) {
        if (a[i]) {
            count++;
            printf("%4d ", i);
        }
    }
    printf("\nThere are %d prime numbers (less than or equal to %d).", count, N);
    return 0;
}
