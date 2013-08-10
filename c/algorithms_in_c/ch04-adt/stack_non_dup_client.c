#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "item.h"
#include "stack_non_dup.h"
#include "common/cmn_lib.h"

int main(int argc, char *argv[])
{
    int max = 5;

    stack_init(max);
    assert(stack_isempty());

    stack_push(1);
    stack_push(2);
    stack_push(3);
    assert(stack_count() == 3);
    assert(stack_top() == 3);
    stack_push(3);
    assert(stack_count() == 3);
    assert(stack_top() == 3);
    stack_push(2);
    assert(stack_count() == 3);
    assert(stack_top() == 3);
    stack_push(4);
    stack_push(5);
    stack_push(5); // stack full, ok to push a duplicate item.

    nl();
    printf("count: %d \n", stack_count());

    return 0;
}
