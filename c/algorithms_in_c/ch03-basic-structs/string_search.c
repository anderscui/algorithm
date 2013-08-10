#include <stdio.h>
#include <stdlib.h>

#define NOT_FOUND -1

int index_of(const char *s1, const char *s2);

int main(int argc, char *argv[])
{
    const char *s = "reject them all!";
    const char *p = "!";

    printf("search '%s' in '%s':\n", p, s);
    printf("index is %d", index_of(s, p));

    return 0;
}

int index_of(const char *s1, const char *s2)
{
    int i, j;
    for (i = 0; s1[i] != 0; i++)
    {
        for (j = 0; s2[j] != 0; j++)
        {
            if(s1[i + j] != s2[j])
                break;
        }

        if (s2[j] == 0)
            return i;
    }

    return NOT_FOUND;
}
