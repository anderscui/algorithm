#include <stdio.h>
#include <stdlib.h>

typedef int Item;
typedef struct node *link;
struct node { Item item; link next; };

// test case: app 9 5 -> 8
int main(int argc, char *argv[])
{
    int i, n = atoi(argv[1]), m = atoi(argv[2]);
    link t = malloc(sizeof *t);
    link x = t;
    t->item = 1;
    t->next = t;
    for (i = 2; i <= n; i++)
    {
        x = (x->next = malloc(sizeof *x));
        x->item = i;
        x->next = t;
    } // now x points to the last node, t points to the first node;

    while(n-- > 1)
    {
        for (i = 1; i < m; i++)
        {
            x = x->next;
        }
        // the next of x is kicked out;
        x->next = x->next->next;
    }

    printf("%d \n", x->item);
    return 0;
}
