#include <stdio.h>
#include <stdlib.h>

#include "item.h"
#include "stack.h"
#include "common/cmn_lib.h"

int main(int argc, char *argv[])
{
    int max = 5;

    stack_init(max);
    int i;
    for (i = 0; i < max; i++)
    {
        stack_push(i);
    }
    printf("count: %d \n", stack_count());

    for (i = 0; i < max; i++)
    {
        printf("%d ", stack_pop());
    }
    nl();
    printf("count: %d \n", stack_count());

    return 0;
}
