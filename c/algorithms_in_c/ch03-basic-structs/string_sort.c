// program 3.17 by andersc

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NMAX 1000
#define MMAX 10000

int compare(void *i, void *j)
{
    return strcmp(*(char **)i, *(char **)j);
}

int main(int argc, char *argv[])
{
    char buf[MMAX];
    int M = 0;

    int i, N;
    char* a[NMAX];
    for (N = 0; N < NMAX; N++)
    {
        a[N] = &buf[M];
        if (scanf("%s", a[N]) == EOF)
        {
            break;
        }
        M += strlen(a[N]) + 1;
    }
    qsort(a, N, sizeof(char *), compare);
    for(i = 0; i < N; i++)
        printf("%s \n", a[i]);

    return 0;
}
