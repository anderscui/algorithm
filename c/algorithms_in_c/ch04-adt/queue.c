#include <assert.h>
#include <stdlib.h>

#include "item.h"
#include "queue.h"

static Item *q;
static int front;
static int rear;
static int size;
static int max_size;

void queue_init(int n_max)
{
    max_size = n_max;
    q = malloc(max_size * sizeof(Item));
    front = 0;
    rear = 0;
    size = 0;
}

void queue_clear(void)
{
    free(q);
    max_size = 0;
    front = 0;
    rear = 0;
    size = 0;
}

bool queue_isempty(void)
{
    return size == 0;
}

bool queue_isfull(void)
{
    return size == max_size;
}

int queue_count(void)
{
    return size;
}

Item queue_front(void)
{
    assert(size > 0);
    return q[front];
}

void queue_enqueue(Item val)
{
    assert(size < max_size);

    q[rear] = val;
    rear = (rear + 1) % max_size;
    size++;
}

Item queue_dequeue()
{
    assert(size > 0);

    Item t = q[front];
    front = (front + 1) % max_size;
    size--;

    return t;
}
