/*  This is a great example of Dynamic Programming.
    Even for a number of 40, the naive recursive method is not acceptable,
    while by just adding an extra array to store the calculated values and
    remove the redundant calculations, make_change2 is much faster than its former one.
*/
#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

#define N 5
#define CHANGES 100

int coins[] = { 1, 5, 10, 21, 25 };
int limits[] = { 10, 10, 10, 10, 10 };
int known_changes[CHANGES];
int unknown = -1;

int make_change(int coins[], int change)
{
    int i;
    for (i = 0; i < N; i++)
    {
        if (coins[i] == change)
            return 1;
    }

    int min_coins = change; // all with 1 cent.
    int j;
    for(j = 1; j <= change / 2; j++)
    {
        int this_coins = make_change(coins, j) + make_change(coins, change - j);
        if(this_coins < min_coins)
            min_coins = this_coins;
    }

    return min_coins;
}

int make_change2(int coins[], int change)
{
    if(known_changes[change] != unknown)
        return known_changes[change];

    int i;
    for (i = 0; i < N; i++)
    {
        if (coins[i] == change)
            return 1;
    }

    int min_coins = change; // all with 1 cent.
    int j;
    for(j = 1; j <= change / 2; j++)
    {
        int this_coins = make_change2(coins, j) + make_change2(coins, change - j);
        if(this_coins < min_coins)
            min_coins = this_coins;
    }

    return (known_changes[change] = min_coins);
}

int main(int argc, char *argv[])
{
    //printf("changes for 3: %d \n", make_change(coins, 3));
    //printf("changes for 5: %d \n", make_change(coins, 5));
    //printf("changes for 8: %d \n", make_change(coins, 8));
    //printf("changes for 21: %d \n", make_change(coins, 21));
    //printf("changes for 32: %d \n", make_change(coins, 32)); // 2 seconds
    //printf("changes for 40: %d \n", make_change(coins, 40)); // not acceptable...
    //printf("changes for 62: %d \n", make_change(coins, 62));
    //printf("changes for 63: %d \n", make_change(coins, 63));

    int i;
    for (i = 0; i < CHANGES; i++)
    {
        known_changes[i] = unknown;
    }

    printf("changes for 3: %d \n", make_change2(coins, 3));
    printf("changes for 5: %d \n", make_change2(coins, 5));
    printf("changes for 8: %d \n", make_change2(coins, 8));
    printf("changes for 21: %d \n", make_change2(coins, 21));
    printf("changes for 32: %d \n", make_change2(coins, 32));
    printf("changes for 40: %d \n", make_change2(coins, 40));
    printf("changes for 62: %d \n", make_change2(coins, 62));
    printf("changes for 63: %d \n", make_change2(coins, 63));

    return 0;
}
