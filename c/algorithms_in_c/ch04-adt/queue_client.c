#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "item.h"
#include "queue.h"

int main(int argc, char *argv[])
{
    int n_queue = 3;
    queue_init(n_queue);
    assert(queue_count() == 0);
    assert(queue_isempty());

    queue_enqueue(1);
    queue_enqueue(2);
    queue_enqueue(3);
    assert(queue_count() == n_queue);
    assert(queue_isfull());

    assert(queue_front() == 1);
    assert(queue_dequeue() == 1);
    assert(queue_front() == 2);
    assert(queue_count() == 2);
    queue_enqueue(4);
    assert(queue_count() == n_queue);
    assert(queue_isfull());

    assert(queue_dequeue() == 2);
    assert(queue_dequeue() == 3);
    assert(queue_front() == 4);
    assert(!queue_isempty());
    assert(queue_dequeue() == 4);
    assert(queue_isempty());

    return 0;
}
