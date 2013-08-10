#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"
#include "list.h"

void show_node(link node)
{
    printf("%d - ", node->item);
}

int main(int argc, char *argv[])
{
    init_list();
    assert(is_empty());
    assert(list_count() == 0);

    insert_node(1);
    insert_node(2);
    insert_node(3);
    assert(!is_empty());
    assert(list_count() == 3);
    nl();

    list_traverse(show_node);
    nl();
    list_traverseR(show_node);

    return 0;
}
