#ifndef ARRAY_H_INCLUDED
#define ARRAY_H_INCLUDED

#include "item.h"

typedef void (*sorter)(Item[], int, int);

void randinit(Item[], int);
void scaninit(Item[], int *);
void show(Item[], int, int);
void sort(sorter, Item[], int, int);

void shell_sort(Item[], int, int);
void insert_sort(Item[], int, int);
void select_sort(Item[], int, int);
void bubble_sort(Item[], int, int);

#endif // ARRAY_H_INCLUDED
