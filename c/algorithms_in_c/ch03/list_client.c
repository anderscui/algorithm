#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "list.h"

int main(int argc, char *argv[])
{
    init_list();
    assert(is_empty());

    insert_node(1);
    insert_node(2);
    insert_node(3);
    assert(!is_empty());

    link first = first_node();
    assert(first != NULL);
    assert(first->item == 3);
    link last = last_node();
    assert(last != NULL);
    assert(last->item == 1);
    insert_after(first, 33);
    insert_after(last, 11);

    printf("nodes created: \n");
    visit_list();

    delete_node(2);
    delete_first();
    printf("nodes deleted: \n");
    visit_list();

    clear_list();
    printf("list cleared: \n");
    visit_list();

    printf("testing reverse function:\n");
    init_list();
    int i;
    for (i = 0; i < 5; i++)
    {
        insert_node(i);
    }
    printf("nodes created: \n");
    visit_list();
    reverse_list();
    printf("nodes reversed: \n");
    visit_list();

    return 0;
}
