#include <stdio.h>
#include <stdlib.h>

#include "fcComplex.h"

Complex comp_new(float re, float im)
{
    Complex c = malloc(sizeof *c);
    c->re = re;
    c->im = im;
    return c;
}
float comp_re(Complex c)
{
    return c->re;
}
float comp_im(Complex c)
{
    return c->im;
}
Complex comp_mult(Complex c1, Complex c2)
{
    return comp_new(c1->re * c2->re - c1->im * c2->im,
                    c1->re * c2->im + c1->im * c2->re);
}
