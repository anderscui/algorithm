#include <assert.h>
#include <stdlib.h>

#include "stack.h"

static StackItem *s;
static int top;
static int max_size;

void stack_init(int n_max)
{
    s = malloc(n_max * sizeof(StackItem));
    top = 0;
    max_size = n_max;
}

void stack_clear(void)
{
    free(s);
    top = 0;
    max_size = 0;
}

bool stack_isempty(void)
{
    return (top == 0);
}

bool stack_isfull(void)
{
    return (top == max_size);
}

int stack_count(void)
{
    return top;
}

StackItem stack_top(void)
{
    assert(top > 0);
    return s[top];
}

void stack_push(StackItem val)
{
    assert(top < max_size);
    s[top++] = val;
}

StackItem stack_pop()
{
    assert(top > 0);
    return s[--top];
}
