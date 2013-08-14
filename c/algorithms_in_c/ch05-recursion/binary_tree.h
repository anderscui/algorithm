#ifndef BINARY_TREE_H_INCLUDED
#define BINARY_TREE_H_INCLUDED

#define eq(A, B) ((A) == (B))

typedef char Item;

typedef struct node *link;
struct node
{
    Item item;
    link left, right;
};

link new_node(Item item);
int tree_count(link tree);

#endif // BINARY_TREE_H_INCLUDED
