#ifndef PQ_H_INCLUDED
#define PQ_H_INCLUDED

#include "item.h"

void pq_init(int);
int pq_empty();
void pq_insert(Item);
Item pq_delmax();
void pq_show();

#endif // PQ_H_INCLUDED
