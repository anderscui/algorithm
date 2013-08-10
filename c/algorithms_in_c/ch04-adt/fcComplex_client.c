#include <stdio.h>
#include <stdlib.h>

#include "fcComplex.h"

int main(int argc, char *argv[])
{
    Complex c1 = comp_new(1.1, 2.2);
    Complex c2 = comp_new(1.1, 3.6);
    Complex mult = comp_mult(c1, c2);
    printf("%2.2f + %2.2fi", mult->re, mult->im);

    return 0;
}
