#include <stdio.h>
#include <stdlib.h>

#include "item.h"

Item item_rand(void)
{
    return 100.0 * rand() / RAND_MAX;
}

int item_scan(Item *x)
{
    //return scanf("%f", x);
    return scanf("%d", x);
}

void item_show(Item x)
{
    //printf("%7.5f ", x);
    printf("%d ", x);
}
