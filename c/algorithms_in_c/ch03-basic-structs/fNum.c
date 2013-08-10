#include <stdlib.h>

#include "fNum.h"

// RAND_MAX: 0x7FFF = 32767;
Number randNum()
{
    return 1.0 * rand() / RAND_MAX;
}
