#include <stdio.h>
#include <stdlib.h>

// simulate Bernoulli Trial

int heads();

int main(int argc, char *argv[])
{
    // m trials, n throws, data is stored in res array.
    int i, j, cnt;
    int n = atoi(argv[1]), m = atoi(argv[2]);
    int *res = malloc((n + 1) * sizeof(int));

    for (j = 0; j <= n; j++)
        res[j] = 0;
    for (i = 0; i < m; i++)
    {
        cnt = 0;
        for (j = 0; j <= n; j++)
        {
            if (heads())
                cnt++;
        }
        res[cnt]++;
    }

    for (i = 0; i <= n; i++)
    {
        printf("%2d ", i);
        for (j = 0; j < res[i]; j += 10)
            printf("*");
        printf("\n");
    }

    return 0;
}

int heads()
{
    //or rand() % 2;
    return rand() < RAND_MAX / 2;
}
