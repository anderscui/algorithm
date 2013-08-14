#include <stdio.h>
#include <stdlib.h>

#include "binary_tree.h"

link new_node(Item item)
{
    link p = malloc(sizeof (*p));
    p->left = NULL;
    p->right = NULL;
    p->item = item;

    return p;
}

int tree_count(link tree)
{
    if(tree == NULL)
        return 0;

    return 1 + tree_count(tree->left) + tree_count(tree->right);
}
