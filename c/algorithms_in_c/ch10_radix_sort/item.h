#ifndef ITEM_H_INCLUDED
#define ITEM_H_INCLUDED

//typedef double Item;
typedef int Item;

#define key(A) (A)
#define less(A, B) (key(A) < key(B))
#define eq(A, B) (key(A) == key(B))
#define exch(A, B) { Item t = A; A = B; B = t; }
#define compexch(A, B) if (less(B, A)) exch(A, B)

Item item_rand(void);
int item_scan(Item *);
void item_show(Item);

#endif // ITEM_H_INCLUDED
