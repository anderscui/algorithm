#include <stdio.h>
#include <stdlib.h>

#include "polynomial.h"

int main(int argc, char *argv[])
{
    Poly p = poly_term(2, 2);
    poly_show(p);
    poly_add(p, poly_term(3, 1));
    poly_show(p);
    poly_add(p, poly_term(5, 0));
    poly_show(p);

    printf("when x is %f, its value is %f \n", 1.0, poly_eval(p, 1.0));
    printf("when x is %f, its value is %f \n", 2.0, poly_eval(p, 2.0));
    printf("when x is %f, its value is %f \n", 2.1, poly_eval(p, 2.1));

    return 0;
}
