#ifndef LIST_H_INCLUDED
#define LIST_H_INCLUDED

#include <stdbool.h>

typedef int Item;
typedef struct node *link;
struct node { Item item; link next; };

bool is_empty();
void init_list();
link insert_node(Item item);
link insert_after(link x, Item item);
link prev_node(Item item);
link find_node(Item item);

// the list should not be empty, otherwise, the "first" is invalid.
Item delete_first();

// if the node is not found, do nothing.
void delete_node(Item item);
void clear_list();

link first_node();
link last_node();
link next_node(link x);
Item node_item(link x);
void visit_list();

void reverse_list();

#endif // LIST_H_INCLUDED
