#ifndef QUEUE_H_INCLUDED
#define QUEUE_H_INCLUDED

#include <stdbool.h>
#include "item.h"

void queue_init(int n_max);
void queue_clear(void);
bool queue_isempty(void);
bool queue_isfull(void);
int queue_count(void);
Item queue_front(void);
void queue_enqueue(Item);
Item queue_dequeue();

#endif // QUEUE_H_INCLUDED
