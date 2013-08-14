// ch05, 5.7 hanoi tower.
// totally this program needs 2^n - 1 moves.

#include <stdio.h>
#include <stdlib.h>

int pos[] = { 0, 1, 2 };
char* spots[] = { "A", "B", "C" };
//char* spots[] = { "第一个", "第二个", "第三个" };

int third_pos(int a, int b)
{
    return (3 - a - b);
}

void moveto(int n, int from, int to)
{
    printf("move %d from %s to %s;\n", n, spots[from], spots[to]);
}

void hanoi(int n, int from, int to)
{
    if(n == 0) return;

    int third = third_pos(from, to);
    hanoi(n-1, from, third);
    moveto(n, from, to);
    hanoi(n-1, third, to);
}

int main(int argc, char *argv[])
{
    hanoi(2, 0, 2);
    return 0;
}
