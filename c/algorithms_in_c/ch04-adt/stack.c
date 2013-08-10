#include <assert.h>
#include <stdlib.h>

#include "item.h"
#include "stack.h"

static Item *s;
static int top;
static int max_size;

void stack_init(int n_max)
{
    s = malloc(n_max * sizeof(Item));
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

Item stack_top(void)
{
    assert(top > 0);
    return s[top];
}

void stack_push(Item val)
{
    assert(top < max_size);
    s[top++] = val;
}

Item stack_pop()
{
    assert(top > 0);
    return s[--top];
}
