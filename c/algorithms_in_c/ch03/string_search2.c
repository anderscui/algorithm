#include <stdio.h>
#include <stdlib.h>

#define N 1000

// cmd: app to_search
int main(int argc, char *argv[])
{
    int i, j, t;
    char a[N];//, *p = argv[1];
    const char *p = "al";

    for (i = 0; i < N-1; a[i] = t, i++)
    {
        if((t = getchar()) == EOF)
            break;
    }
    a[i] = '\0';

    for (i = 0; a[i] != 0; i++)
    {
        for (j = 0; p[j] != 0; j++)
        {
            if(a[i + j] != p[j])
                break;
        }
        if (p[j] == 0)
            printf("%d ", i);
    }
    printf("\n");

    return 0;
}
