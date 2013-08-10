#include <stdio.h>
#include <stdlib.h>

int **malloc2d(int r, int c)
{
    int i;
    int **t = malloc(r * sizeof(int *));
    for (i = 0; i < r; i++)
    {
        t[i] = malloc(c * sizeof(int));
    }

    return t;
}

void print2d(int **a, int r, int c)
{
    int i, j;
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            printf("%2d ", a[i][j]);
        }
        printf("\n");
    }
}

int main(int argc, char *argv[])
{
    int r = 9, c = 9;
    int **a = malloc2d(r, c);
    int i, j;
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            a[i][j] = (i+1) * (j+1);
        }
    }
    print2d(a, r, c);

    return 0;
}
