#include <stdio.h>
#include <stdlib.h>

#include "complex.h"

Complex comp_new(float re, float im)
{
    Complex c = { re, im };
    return c;
}
float comp_re(Complex c)
{
    return c.re;
}
float comp_im(Complex c)
{
    return c.im;
}
Complex comp_mult(Complex c1, Complex c2)
{
    Complex c;
    c.re = c1.re * c2.re - c1.im * c2.im;
    c.im = c1.re * c2.im + c1.im * c2.re;
    return c;
}
