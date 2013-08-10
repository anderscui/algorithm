#ifndef STACK_H_INCLUDED
#define STACK_H_INCLUDED

#include <stdbool.h>
#include "item.h"

void stack_init(int n_max);
void stack_clear(void);
bool stack_isempty(void);
bool stack_isfull(void);
int stack_count(void);
Item stack_top(void);
void stack_push(Item);
Item stack_pop();

#endif // STACK_H_INCLUDED
