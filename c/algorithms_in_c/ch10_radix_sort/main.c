#include <stdio.h>
#include <stdlib.h>

#include "common/cmn_lib.h"

#define bitsword 32
#define bitsbyte 8
#define bytesword 4
#define R (1 << bitsbyte)

// extract Bth byte of A.
#define digit(A, B) (((A) >> (bitsword-((B)+1)*bitsbyte)) & (R-1))
#define digit_at(A, w) (((A) >> (bitsword-((w)+1))) & 1)

int main()
{
    println("R is %d", R);

    //int i = (2 << 16) - 1;
    int i = 0x01020304;
    int j;
    // 1, 2, 3, 4, high digits are on the left side;
//    for (j = 0; j < bytesword; j++)
//        println("%d", digit(i, j));

    i = 0xAAAAAAAA;
    for (j = 0; j < bitsbyte; j++)
        println("%d", digit_at(i, j));

    return 0;
}
