#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *a;
int i;

int eval()
{
    int x = 0;
    while (a[i] == ' ')
        i++;
    if (a[i] == '+')
    {
        i++;
        return eval() + eval();
    }
    if (a[i] == '*')
    {
        i++;
        return eval() * eval();
    }
    while (a[i] >= '0' && a[i] <= '9')
    {
        x = 10 * x + (a[i++] - '0');
    }
    return x;
}

int main(int argc, char *argv[])
{
    if (argc > 1)
    {
        a = argv[1];
    }
    else
    {
        //a = "* + 2 3 8"; // 40
        a = "* + 7 * * 4 6 + 8 9 5"; // 2075
    }
    printf("%d", eval());

    return 0;
}
