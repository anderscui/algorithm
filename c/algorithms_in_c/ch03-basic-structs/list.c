#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "list.h"

link head;

bool is_empty()
{
    return head->next == NULL;
}

void init_list()
{
    head = malloc(sizeof *head);
    head->item = -1;
    head->next = NULL;
}

link insert_node(Item item)
{
    return insert_after(head, item);
}

link insert_after(link x, Item item)
{
    link p = malloc(sizeof *p);
    p->item = item;
    p->next = x->next;
    x->next = p;

    return p;
}

// if the item is the first node, return NULL instead of head node,
// because this impl should hide this detail to other codes.
link prev_node(Item item)
{
    link cur = head->next;
    link prev = NULL;
    while (cur != NULL)
    {
        if (cur->item == item)
        {
            return prev;
        }
        prev = cur;
        cur = cur->next;
    }

    return NULL;
}

link find_node(Item item)
{
    link cur = head->next;
    while (cur != NULL)
    {
        if (cur->item == item)
        {
            return cur;
        }
        cur = cur->next;
    }

    return NULL;
}

Item delete_first()
{
    link first = head->next;
    assert(first != NULL);

    Item item = first->item;
    head->next = first->next;
    free(first);
    return item;
}

void delete_node(Item item)
{
    if (is_empty())
        return;

    link first = head->next;
    if (first->item == item)
    {
        delete_first();
    }
    else
    {
        link prev = prev_node(item);
        if (prev != NULL)
        {
            link to_delete = prev->next;
            prev->next = to_delete->next;
            free(to_delete);
        }
    }
}

void clear_list()
{
    while (!is_empty())
    {
        delete_first();
    }
}

link first_node()
{
    return head->next;
}

link last_node()
{
    link cur = head->next;
    while (cur != NULL)
    {
        if (cur->next == NULL)
        {
            return cur;
        }
        cur = cur->next;
    }

    return NULL;
}

link next_node(link x)
{
    return x->next;
}

Item node_item(link x)
{
    return x->item;
}

void visit_list()
{
    if (is_empty())
    {
        printf("list is empty.\n");
        return;
    }

    link cur = head->next;
    while (cur != NULL)
    {
        printf("%d  ", cur->item);
        cur = cur->next;
    }
    printf("\n");
}

void reverse_list()
{
    link to_process = head->next;
    link processed = NULL;

    link next;
    while (to_process != NULL)
    {
        next = to_process->next;
        head->next = to_process;
        to_process->next = processed;
        processed = to_process;

        to_process = next;
    }
}
