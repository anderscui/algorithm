#ifndef STACK_H_INCLUDED
#define STACK_H_INCLUDED

#include <stdbool.h>

#include "binary_tree.h"

typedef link StackItem;

void stack_init(int n_max);
void stack_clear(void);
bool stack_isempty(void);
bool stack_isfull(void);
int stack_count(void);
StackItem stack_top(void);
void stack_push(StackItem);
StackItem stack_pop();

#endif // STACK_H_INCLUDED
